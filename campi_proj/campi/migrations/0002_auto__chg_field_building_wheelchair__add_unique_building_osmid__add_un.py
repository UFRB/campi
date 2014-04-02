# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Building.wheelchair'
        db.alter_column(u'campi_building', 'wheelchair', self.gf('django.db.models.fields.CharField')(max_length=10))
        # Adding unique constraint on 'Building', fields ['osmid']
        db.create_unique(u'campi_building', ['osmid'])

        # Adding unique constraint on 'Phone', fields ['number']
        db.create_unique(u'campi_phone', ['number'])


    def backwards(self, orm):
        # Removing unique constraint on 'Phone', fields ['number']
        db.delete_unique(u'campi_phone', ['number'])

        # Removing unique constraint on 'Building', fields ['osmid']
        db.delete_unique(u'campi_building', ['osmid'])


        # Changing field 'Building.wheelchair'
        db.alter_column(u'campi_building', 'wheelchair', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'campi.building': {
            'Meta': {'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'osmid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'polygon': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'wheelchair': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'campi.phone': {
            'Meta': {'object_name': 'Phone'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'})
        },
        u'campi.sector': {
            'Meta': {'object_name': 'Sector'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campi.Building']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campi.Sector']", 'blank': 'True'}),
            'phones': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['campi.Phone']", 'symmetrical': 'False', 'blank': 'True'}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['campi.Service']", 'symmetrical': 'False', 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'campi.service': {
            'Meta': {'object_name': 'Service'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['campi']