from django.contrib import admin
from django.urls import path, re_path, include

from . import views


urlpatterns = [
    re_path(r"^boards/(?P<pk>\d+)/$", views.board_topics, name="board_topics"),
    re_path(r"^boards/(?P<pk>\d+)/new/$", views.new_topic, name="new_topic"),
    re_path(r"^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$", views.topic_posts, name="topic_posts"),
    re_path(r"^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$", views.reply_topic, name="reply_topic"),
    re_path(r"^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$", views.PostUpdateView.as_view(), name="edit_post"),
    path("", views.BoardListView.as_view(), name="index"),
]
