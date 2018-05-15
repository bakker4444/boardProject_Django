from django.urls import reverse, resolve
from django.test import TestCase
from .views import index, board_topics
from .models import Board

# Create your tests here.
class IndexTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name="Django", description="Django board.")
        url = reverse("index")
        self.response = self.client.get(url)

    def test_index_view_status_code(self):
        return self.assertEqual(self.response.status_code, 200)    ## 200 --> success

    def test_index_url_resolve_index_view(self):
        view = resolve("/")
        self.assertEqual(view.func, index)

    def test_index_view_contains_link_to_topics_page(self):
        board_topics_url = reverse("board_topics", kwargs={"board_id": self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))

    def test_board_topics_view_contains_link_back_to_index_page(self):
        board_topics_url = reverse("board_topics", kwargs={"board_id": 1})
        response = self.client.get(board_topics_url)
        index_url = reverse("index")
        self.assertContains(response, 'href="{0}"'.format(index_url))


class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name="Django", description="Django board.")

    def test_board_topics_view_success_status_code(self):
        url = reverse("board_topics", kwargs={"board_id": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse("board_topics", kwargs={"board_id": 99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEqual(view.func, board_topics)