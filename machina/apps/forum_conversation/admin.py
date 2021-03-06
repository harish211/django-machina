# -*- coding: utf-8 -*-

# Standard library imports
# Third party imports
from django.contrib import admin

# Local application / specific library imports
from machina.core.db.models import get_model

Attachment = get_model('forum_attachments', 'Attachment')
Post = get_model('forum_conversation', 'Post')
Topic = get_model('forum_conversation', 'Topic')


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [AttachmentInline, ]
    list_display = ('__str__', 'topic', 'poster', 'updated', 'approved')
    list_filter = ('created', 'updated',)
    raw_id_fields = ('poster', )
    search_fields = ('content',)
    list_editable = ('approved',)


class TopicAdmin(admin.ModelAdmin):
    inlines = (PostInline,)
    list_display = ('subject', 'forum', 'created', 'first_post', 'last_post', 'posts_count', 'approved')
    list_filter = ('created', 'updated',)
    raw_id_fields = ('poster', 'subscribers', )
    search_fields = ('subject',)
    list_editable = ('approved',)


admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
