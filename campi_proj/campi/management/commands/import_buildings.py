# -*- coding: utf-8 -*-

import simplejson

from django.core.management.base import BaseCommand

from ...models import Building


class Command(BaseCommand):
    args = 'filename'
    help = 'Import buildings from a GeoJSON file'

    def create_or_update_building(feature):
        if Building.objects.get(osmid = feature['properties']['osmid'])

    def handle(self, *args, **options):
        for filename in args:
            data_json = open(filename, 'r').read()
            data = simplejson.loads(data_json)

            for feature in data['features']:
                if feature['geometry']['type'] == 'Polygon'
