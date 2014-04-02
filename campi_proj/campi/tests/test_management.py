# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core import management

from ..models import Building


class TestImportBuildings(TestCase):

    def setUp(self):
        management.call_command('import_buildings',
                                'campi/tests/data/building1.geojson')

    def test_import(self):
        self.assertEqual(Building.objects.all().count(), 1)
        self.assertEqual(Building.objects.get(osmid='160025283').name,
                            u'Prédio da Reitoria')
        self.assertEqual(Building.objects.get(osmid='160025283').wheelchair,
                            u'')

    def test_update(self):
        management.call_command('import_buildings',
                                'campi/tests/data/building2.geojson')

        self.assertEqual(Building.objects.get(osmid='160025283').name,
                            u'Prédio da Reitoria - 2')
        self.assertEqual(Building.objects.get(osmid='160025283').wheelchair,
                            'limited')