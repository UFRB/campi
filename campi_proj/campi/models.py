from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Phone(models.Model):

    PHONE_TYPES = (
        ('fixedline', _(u'Fixed-Line')),
        ('telefax', _(u'Telefax')),
        ('mobile', _(u'Mobile Phone')),
        ('voipsoftphone', _(u'VOIP Softphone')),
        ('voipdevice', _(u'VOIP Device')),
        )

    number = models.CharField(max_length=11, unique=True)
    category = models.CharField(choices=PHONE_TYPES, max_length=100)

    def __unicode__(self):
        return self.number


class Service(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Building(models.Model):

    WHEEL_STATUS = (
        ('yes', _(u'Accessible')),
        ('no', _(u'Not Accessible')),
        ('limited', _(u'Limited Accessibility')),
        )

    name = models.CharField(max_length=200, blank=True)
    osmid = models.CharField(max_length=15, unique=True)
    wheelchair = models.CharField(choices=WHEEL_STATUS, max_length=10, blank=True)
    polygon = models.PolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.osmid)


class Sector(models.Model):

    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', blank=True)
    services = models.ManyToManyField(Service, blank=True)
    site = models.URLField(max_length=200, blank=True)
    phones = models.ManyToManyField(Phone, blank=True)
    address = models.CharField(max_length=255, blank=True)
    building = models.ForeignKey(Building)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name


from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^django\.contrib\.gis\.db\.models\.fields\.PolygonField"])