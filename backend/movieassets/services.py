import logging
import pathlib
import datetime
import uuid
import os

import requests
import petl as etl

from typing import Optional
from urllib.parse import urljoin
from asgiref.sync import sync_to_async
from django.conf import settings
from rest_framework import status

from . import models

logger = logging.getLogger(__name__)


def _create_character(name: str, csv_file: pathlib.Path):
    obj = models.Character(name=name)

    with csv_file.open('rb') as f:
        obj.source_file.save(csv_file.name, f)

    obj.save()


create_character = sync_to_async(_create_character, thread_sensitive=True)


async def fetch_people():
    url = urljoin(settings.SWAPI_URL, 'people')
    logger.debug(f'fetching people data from: {url}')

    resp = requests.get(url)
    logger.debug(f'resp status: {resp.status_code}')

    if resp.status_code != status.HTTP_200_OK:
        return None

    media_root = pathlib.Path(settings.MEDIA_ROOT)
    if not media_root.exists():
        os.makedirs(str(media_root))

    data_file = media_root / f'fetch_{str(uuid.uuid4())}.json'
    with data_file.open('w') as f:
        f.write(resp.text)
    table = etl.fromjson(data_file)
    table = etl.addcolumn(table, 'date', etl.facet(table, 'edited'))
    table = etl.convert(table, 'date',
                        lambda v: datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d'))

    table = etl.convert(table, 'homeworld', lambda v: fetch_planet_name(v))
    table = etl.cutout(table, 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url')

    name = str(uuid.uuid4())
    upload_dir = pathlib.Path(settings.MOVIE_CHARACTER_FILE_UPLOAD_DIR)
    if not upload_dir.exists():
        os.makedirs(str(upload_dir))
    csv_file = upload_dir / f'{name}.csv'
    etl.tocsv(table, csv_file, encoding='utf-8')

    data_file.unlink()

    await create_character(name, csv_file)


def fetch_planet_name(url: str) -> Optional[str]:
    if not url:
        return None

    resp = requests.get(url)
    if resp.status_code != status.HTTP_200_OK:
        logger.warning(
            f'Planet with provided url: {url} cannot be fetched. Status: {resp.status_code} Details: {str(resp.text)}')
        return None
    data = resp.json()
    return data['name'] if 'name' in data else None


def load_characters_from_csv(obj: models.Character, offset=None, count_by_columns=None):
    table = etl.fromcsv(obj.source_file.path)
    columns = etl.header(table)

    if offset:
        table = etl.rowslice(table, offset)
        
    if count_by_columns:
        table = etl.aggregate(table, key=count_by_columns, aggregation=len, value=count_by_columns)

    headers = etl.header(table)
    body = etl.data(table)
    return columns, headers, body
