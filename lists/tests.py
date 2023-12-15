from django.test import TestCase
from django.urls import resolve
#from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
# Create your tests here.


class HomePageTest(TestCase):

    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')       #resolve :Django内部函数，解析url，并将其映射到对应的视图函数上
    #     self.assertEqual(found.func,home_page)

    # def test_home_page_return_correct_html(self):
    #     response = self.client.get('/')
    #     html = response.content.decode('utf-8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.endswith('</html>'))
    #
    #     self.assertTemplateUsed(response, 'home.html')
    #
    def test_uses_home_temlates(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')


    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')





