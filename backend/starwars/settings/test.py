import os
from pathlib import Path

from .base import *

STATIC_ROOT = './temp/test/static'
MEDIA_ROOT = './temp/test/media'

if not os.path.exists(STATIC_ROOT):
    os.makedirs(STATIC_ROOT)

if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)
