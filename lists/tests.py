from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')       #resolve :Django内部函数，解析url，并将其映射到对应的视图函数上
        self.assertEqual(found.func,home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))


