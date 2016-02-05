# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Request'
        db.create_table(u'hello_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('file_path', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('ver_protocol', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal(u'hello', ['Request'])


    def backwards(self, orm):
        # Deleting model 'Request'
        db.delete_table(u'hello_request')


    models = {
        u'hello.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'other': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'hello.request': {
            'Meta': {'ordering': "['-date_time']", 'object_name': 'Request'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ver_protocol': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['hello']