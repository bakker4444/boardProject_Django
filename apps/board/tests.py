from django.urls import reverse, resolve
from django.test import TestCase
from .views import index

# Create your tests here.
class IndexTests(TestCase):

    def test_index_view_status_code(self):
        url = reverse("index")      ## urls name, not actual address
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)    ## 200 --> success

    def test_index_url_resolve_index_view(self):
        view = resolve("/")
        self.assertEqual(view.func, index)

class BoardTopicsTests(TestCase):

    def setUp(self):
        Board.objects.create(name="Django", description="Django board.")

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEqual(view.func, board_topics)