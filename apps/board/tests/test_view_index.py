from django.urls import reverse, resolve
from django.test import TestCase

from ..views import index
from ..models import Board


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
        board_topics_url = reverse("board_topics", kwargs={"pk": self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
