from django.test import TestCase

from biscuit.models import Walker, Business
from biscuit.forms import BusinessNameForm, DogWalkerNameForm


class BusinessNameFormTest(TestCase):
	def test_form_renders_business_text_input(self):
		form = BusinessNameForm()
		self.assertIn(
			'placeholder="Enter a business name"', form.as_p())
		self.assertIn('class="form-control input-lg"', form.as_p())

	def test_form_validation_for_blank_items(self):
		form = BusinessNameForm(data={'business_name': ''})
		self.assertFalse(form.is_valid())
		self.assertEqual(
			form.errors['business_name'][0], 'This field is required.')

	def test_form_save_handles_saving_to_a_db(self):
		form = BusinessNameForm(data={'business_name': 'Happy Dogs'})
		new_business = form.save()
		self.assertEqual(new_business, Business.objects.first())
		self.assertEqual(new_business.business_name, 'Happy Dogs')

class DogWalkerFormTest(TestCase):
	def test_form_renders_item_text_input(self):
		form = DogWalkerNameForm()
		self.assertIn(
			'placeholder="Enter the name of the dog walker you wish to add"', form.as_p())
		self.assertIn('class="form-control input-lg"', form.as_p())

	def test_form_validation_for_blank_items(self):
		form = DogWalkerNameForm(data={'walker_name': ''})
		self.assertFalse(form.is_valid())
		self.assertEqual(
			form.errors['walker_name'][0], 'This field is required.')

	def test_form_save_handles_saving_to_a_db(self):
		business = Business.objects.create()
		form = DogWalkerNameForm(data={'walker_name': 'Maite'})
		new_walker = form.save()
		self.assertEqual(new_walker, Walker.objects.first())
		self.assertEqual(new_walker.walker_name, 'Maite')

