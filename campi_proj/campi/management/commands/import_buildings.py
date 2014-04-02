# -*- coding: utf-8 -*-

import simplejson

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Polygon

from ...models import Building


def create_building(feature):
    building = Building(osmid=feature['id'].split('/')[-1],
                        polygon=Polygon(feature['geometry']['coordinates'][0]))

    if feature['properties'].get('name') is not None:
        building.name = feature['properties'].get('name')

    if feature['properties'].get('wheelchair') is not None:
        building.wheelchair = feature['properties'].get('wheelchair')

    building.save()


def update_building(building, feature):
    if building.name != feature['properties'].get('name'):
        building.name = feature['properties'].get('name')

    if building.wheelchair != feature['properties'].get('wheelchair'):
        building.wheelchair = feature['properties'].get('wheelchair')

    if building.polygon != Polygon(feature['geometry']['coordinates'][0]):
        building.polygon = Polygon(feature['geometry']['coordinates'][0])

    building.save()


class Command(BaseCommand):
    args = 'filename'
    help = 'Import or update buildings from a GeoJSON file.'

    def handle(self, *args, **options):
        for filename in args:
            data_json = open(filename, 'r').read()
            data = simplejson.loads(data_json)

            for feature in data['features']:
                if feature['geometry'].get('type') == 'Polygon':
                    try:
                        building = Building.objects.get(
                                        osmid=feature.get('id').split('/')[-1])
                        update_building(building, feature)
                    except Building.DoesNotExist:
                        create_building(feature)