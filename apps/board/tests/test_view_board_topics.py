from django.urls import reverse, resolve
from django.test import TestCase

from ..views import board_topics
from ..models import Board


class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name="Django", description="Django board.")

    def test_board_topics_view_success_status_code(self):
        url = reverse("board_topics", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse("board_topics", kwargs={"pk": 99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve("/boards/1/")
        self.assertEqual(view.func, board_topics)

    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse("board_topics", kwargs={"pk": 1})
        indexpage_url = reverse("index")
        new_topic_url = reverse("new_topic", kwargs={"pk": 1})
        response = self.client.get(board_topics_url)
        self.assertContains(response, 'href="{0}"'.format(indexpage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))
