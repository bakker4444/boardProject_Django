from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("boards/<int:pk>/", views.board_topics, name="board_topics"),
    # re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics')
]
