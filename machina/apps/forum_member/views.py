# -*- coding: utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

# Third party imports
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic import ListView

# Local application / specific library imports
from machina.conf import settings as machina_settings
from machina.core.db.models import get_model
from machina.core.loading import get_class

Forum = get_model('forum', 'Forum')
ForumProfile = get_model('forum_member', 'ForumProfile')
Topic = get_model('forum_conversation', 'Topic')

PermissionHandler = get_class('forum_permission.handler', 'PermissionHandler')
perm_handler = PermissionHandler()


class UserTopicsView(ListView):
    """
    Provides a list of all the topics in which the current user has
    posted messages.
    """
    template_name = 'forum_member/user_topics_list.html'
    context_object_name = 'topics'
    paginate_by = machina_settings.FORUM_TOPICS_NUMBER_PER_PAGE

    def get_queryset(self):
        forums = perm_handler.forum_list_filter(
            Forum.objects.all(), self.request.user)
        topics = Topic.objects.filter(
            forum__in=forums,
            posts__poster_id=self.request.user.id,
            posts__approved=True)
        return topics.order_by('-updated')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserTopicsView, self).dispatch(request, *args, **kwargs)


class ForumProfileDetailView(DetailView):
    """
    Shows a user's forum profile.
    """
    template_name = 'forum_member/forum_profile_detail.html'
    context_object_name = 'profile'

    def get_queryset(self):
        user_model = get_user_model()
        return user_model.objects.all()

    def get_object(self, queryset=None):
        user = super(ForumProfileDetailView, self).get_object(queryset)
        profile, dummy = ForumProfile.objects.get_or_create(user=user)
        return profile

    def get_context_data(self, **kwargs):
        context = super(ForumProfileDetailView, self).get_context_data(**kwargs)

        # Computes the number of topics added by the considered member
        context['topics_count'] = Topic.objects.filter(
            approved=True, poster=self.object.user).count()
        return context
