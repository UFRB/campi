from django.contrib.gis import admin

from .models import Building, Phone, Sector, Service

admin.site.register(Building, admin.OSMGeoAdmin)
admin.site.register(Phone)
admin.site.register(Sector)
admin.site.register(Service)