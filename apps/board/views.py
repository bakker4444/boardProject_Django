from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewTopicForm, PostForm
from .models import Board, Topic, Post


def index(request):
    boards = Board.objects.all()
    context = {
        "boards": boards
    }
    return render(request, "index.html", context)


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {
        "board": board
    }
    return render(request, "topics.html", context)


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get("message"),
                topic=topic,
                created_by=request.user
            )
            return redirect("topic_posts", pk=pk, topic_pk=topic.pk)
    else:
        form = NewTopicForm()
    context = {
        "board": board,
        "form": form
    }
    return render(request, "new_topic.html", context)


def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    context = {
        "topic": topic
    }
    return render(request, "topic_posts.html", context)


@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect("topic_posts", pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    context = {
        "topic": topic,
        "form": form
    }
    return render(request, "reply_topic.html", context)
