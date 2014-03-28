from __future__ import absolute_import

from .base import *

########## TEST SETTINGS
TEST_DISCOVER_TOP_LEVEL = SITE_ROOT
TEST_DISCOVER_ROOT = SITE_ROOT
TEST_DISCOVER_PATTERN = "test_*.py"
########## IN-MEMORY TEST DATABASE
DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'test_campi',
         'USER': 'campi',
         'PASSWORD': 'campi',
     }
}
