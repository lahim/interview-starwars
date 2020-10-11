import factory

from pathlib import Path

from django.conf import settings

from django.utils.datetime_safe import datetime

from . import models

TEST_CSV_FILE_PATH = Path(settings.BASE_DIR) / 'movieassets' / 'tests' / 'testdata.csv'


class CharacterFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f'Character-{n}')
    source_file = factory.django.FileField(
        filename='test.csv',
        data=b'name,height,mass,hair_color,skin_color,eye_color,birth_year,gender,homeworld,date\\n' \
             b'Luke Skywalker,172,77,blond,fair,blue,19BBY,male,Tatooine,2014-12-20\\n' \
             b'C-3PO,167,75,n/a,gold,yellow,112BBY,n/a,Tatooine,2014-12-20\\n'
    )
    created_date = datetime.now()

    class Meta:
        model = models.Character
