from django.core.urlresolvers import resolve
from django.test import TestCase, Client
from django.http import HttpRequest
from django.template.loader import render_to_string

from biscuit.views import index, business_home
from biscuit.models import Walker, Business


class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, index)

	def test_home_page_returns_correct_html(self):
	#	request = HttpRequest()
	#	response = index(request)
	#	expected_html = render_to_string('index.html')
	#	self.assertEqual(response.content.decode(), expected_html)
		pass

	def test_home_page_redirects_after_POST(self):
		pass


	def test_business_page_can_save_dog_walker_POST_request(self):
		pass

	def test_business_page_redirects_after_post(self):
		pass

	def test_home_page_only_saves_items_when_necessary(self):
		pass

	def test_business_page_only_saves_items_when_necessary(self):
		pass


