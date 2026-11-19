from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from ..views import IndexView,PostDetailView

class TestUrl(TestCase):

    def test_blog_index_url(self):
        url = reverse('blog:home')
        self.assertEqual(resolve(url).func.view_class,IndexView)

    def test_blog_post_detail(self):
        url = reverse('blog:post_detail',kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class,PostDetailView)
