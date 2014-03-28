# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core import management

from ..models import Building


class TestImportBuildings(TestCase):

    def setUp(self):
        management.call_command('import_buildings',
                                '../public/json/test_one_building.geojson')

    def test_import(self):
        self.assertEqual(Building.objects.all().count(), 1)
