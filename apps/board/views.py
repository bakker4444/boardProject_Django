from django.shortcuts import render, HttpResponse
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.all()
    context = {
        "boards": boards
    }
    return render(request, "index.html", context)

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        "board" : board
    }
    return render(request, "topics.html", context)
