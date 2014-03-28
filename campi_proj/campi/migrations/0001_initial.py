# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Phone'
        db.create_table(u'campi_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'campi', ['Phone'])

        # Adding model 'Service'
        db.create_table(u'campi_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'campi', ['Service'])

        # Adding model 'Building'
        db.create_table(u'campi_building', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('osmid', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('polygon', self.gf('django.contrib.gis.db.models.fields.PolygonField')()),
            ('wheelchair', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'campi', ['Building'])

        # Adding model 'Sector'
        db.create_table(u'campi_sector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campi.Sector'])),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('building', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campi.Building'])),
        ))
        db.send_create_signal(u'campi', ['Sector'])

        # Adding M2M table for field services on 'Sector'
        m2m_table_name = db.shorten_name(u'campi_sector_services')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sector', models.ForeignKey(orm[u'campi.sector'], null=False)),
            ('service', models.ForeignKey(orm[u'campi.service'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sector_id', 'service_id'])

        # Adding M2M table for field phones on 'Sector'
        m2m_table_name = db.shorten_name(u'campi_sector_phones')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sector', models.ForeignKey(orm[u'campi.sector'], null=False)),
            ('phone', models.ForeignKey(orm[u'campi.phone'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sector_id', 'phone_id'])


    def backwards(self, orm):
        # Deleting model 'Phone'
        db.delete_table(u'campi_phone')

        # Deleting model 'Service'
        db.delete_table(u'campi_service')

        # Deleting model 'Building'
        db.delete_table(u'campi_building')

        # Deleting model 'Sector'
        db.delete_table(u'campi_sector')

        # Removing M2M table for field services on 'Sector'
        db.delete_table(db.shorten_name(u'campi_sector_services'))

        # Removing M2M table for field phones on 'Sector'
        db.delete_table(db.shorten_name(u'campi_sector_phones'))


    models = {
        u'campi.building': {
            'Meta': {'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'osmid': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'polygon': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'wheelchair': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'campi.phone': {
            'Meta': {'object_name': 'Phone'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        },
        u'campi.sector': {
            'Meta': {'object_name': 'Sector'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campi.Building']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campi.Sector']"}),
            'phones': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['campi.Phone']", 'symmetrical': 'False'}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['campi.Service']", 'symmetrical': 'False'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'campi.service': {
            'Meta': {'object_name': 'Service'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['campi']