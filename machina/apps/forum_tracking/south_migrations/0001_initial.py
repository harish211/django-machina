# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ForumReadTrack'
        db.create_table(u'forum_tracking_forumreadtrack', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'forum_tracks', to=orm['auth.User'])),
            ('forum', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'tracks', to=orm['forum.Forum'])),
            ('mark_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'forum_tracking', ['ForumReadTrack'])

        # Adding unique constraint on 'ForumReadTrack', fields ['user', 'forum']
        db.create_unique(u'forum_tracking_forumreadtrack', ['user_id', 'forum_id'])

        # Adding model 'TopicReadTrack'
        db.create_table(u'forum_tracking_topicreadtrack', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'topic_tracks', to=orm['auth.User'])),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'tracks', to=orm['forum_conversation.Topic'])),
            ('mark_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'forum_tracking', ['TopicReadTrack'])

        # Adding unique constraint on 'TopicReadTrack', fields ['user', 'topic']
        db.create_unique(u'forum_tracking_topicreadtrack', ['user_id', 'topic_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'TopicReadTrack', fields ['user', 'topic']
        db.delete_unique(u'forum_tracking_topicreadtrack', ['user_id', 'topic_id'])

        # Removing unique constraint on 'ForumReadTrack', fields ['user', 'forum']
        db.delete_unique(u'forum_tracking_forumreadtrack', ['user_id', 'forum_id'])

        # Deleting model 'ForumReadTrack'
        db.delete_table(u'forum_tracking_forumreadtrack')

        # Deleting model 'TopicReadTrack'
        db.delete_table(u'forum_tracking_topicreadtrack')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'forum.forum': {
            'Meta': {'ordering': "[u'tree_id', u'lft']", 'object_name': 'Forum'},
            u'_description_rendered': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('machina.models.fields.MarkupTextField', [], {'blank': 'True', 'null': 'True', u'no_rendered_field': 'True'}),
            'display_sub_forum_list': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('machina.models.fields.ExtendedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'link_redirects': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'link_redirects_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['forum.Forum']"}),
            'posts_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'real_topics_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'topics_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'forum_conversation.topic': {
            'Meta': {'ordering': "[u'-type', u'-updated']", 'object_name': 'Topic'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'forum': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'topics'", 'to': u"orm['forum.Forum']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'posts_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '300'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'subscriptions'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'views_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        },
        u'forum_tracking.forumreadtrack': {
            'Meta': {'unique_together': "([u'user', u'forum'],)", 'object_name': 'ForumReadTrack'},
            'forum': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'tracks'", 'to': u"orm['forum.Forum']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mark_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'forum_tracks'", 'to': u"orm['auth.User']"})
        },
        u'forum_tracking.topicreadtrack': {
            'Meta': {'unique_together': "([u'user', u'topic'],)", 'object_name': 'TopicReadTrack'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mark_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'tracks'", 'to': u"orm['forum_conversation.Topic']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'topic_tracks'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['forum_tracking']