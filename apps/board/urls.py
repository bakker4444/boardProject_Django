from django.contrib import admin
from django.urls import path, re_path, include

from . import views


urlpatterns = [
    re_path(r"^boards/(?P<pk>\d+)/$", views.board_topics, name="board_topics"),
    re_path(r"^boards/(?P<pk>\d+)/new/$", views.new_topic, name="new_topic"),
    path("", views.index, name="index"),
]
