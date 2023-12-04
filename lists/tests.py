from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')       #resolve Django 内部石铜函数，解析url，并将其映射到对应的视图函数上
        self.assertEqual(found.func,home_page)


