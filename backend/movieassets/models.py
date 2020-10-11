from pathlib import Path
from urllib.parse import urljoin

from django.db import models
from django.utils.translation import gettext_lazy as _

from django.conf import settings

from . import helpers


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Created date'))
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name=_('Last modified date'))

    class Meta:
        abstract = True


class Character(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    source_file = models.FileField(upload_to=helpers.path(settings.MOVIE_CHARACTER_FILE_UPLOAD_DIR),
                                   verbose_name=_('File'))

    class Meta:
        ordering = ('-created_date',)


class Planets(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    source_file = models.FileField(upload_to=helpers.path(settings.MOVIE_PLANETS_FILE_UPLOAD_DIR),
                                   verbose_name=_('File'))
