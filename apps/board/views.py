from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.all()
    context = {
        "boards": boards
    }
    return render(request, "index.html", context)

def board_topics(request, board_id):
    ## OPTION 1: try, except, raise error
    # try:
    #     board = Board.objects.get(pk=board_id)
    # except Board.DoesNotExist:
    #     raise Http404

    ## OPTION 2: using django shortcuts
    board = get_object_or_404(Board, pk=board_id)

    context = {
        "board" : board
    }
    return render(request, "topics.html", context)
