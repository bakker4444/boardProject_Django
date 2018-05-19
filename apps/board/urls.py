from django.contrib import admin
from django.urls import path, re_path, include

from . import views


urlpatterns = [
    re_path(r"^boards/(?P<pk>\d+)/$", views.board_topics, name="board_topics"),
    re_path(r"^boards/(?P<pk>\d+)/new/$", views.new_topic, name="new_topic"),
    re_path(r"^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$", views.topic_posts, name="topic_posts"),
    path("", views.index, name="index"),
]
