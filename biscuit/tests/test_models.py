from django.core.exceptions import ValidationError
from django.test import TestCase

from biscuit.models import Business, Walker, Appointment
from unittest import skip


class BusinessModelTest(TestCase):

	def test_default_text(self):
		business = Business()
		self.assertEqual(business.business_name, '')

	def test_cannot_save_empty_business_names(self):
		business = Business(business_name='')
		with self.assertRaises(ValidationError):
			business.save()
			business.full_clean()

class WalkerModelTest(TestCase):

	def test_default_text(self):
		walker = Walker()
		self.assertEqual(walker.walker_name, '')

	def test_cannot_save_empty_walker_names(self):
		walker = Walker(walker_name='')
		with self.assertRaises(ValidationError):
			walker.save()
			walker.full_clean()
	#TODO: Edit this so has a business name when change models

class AppointmentModelTest(TestCase):

	def test_default_text(self):
		appointment = Appointment()
		self.assertEqual(appointment.time, None)

	@skip
	def test_cannot_save_empty_appointment_time(self):
		appointment = Appointment(time=None)
		with self.assertRaises(ValidationError):
			appointment.save()
			appointment.full_clean()
	#TODO: Edit this so get validation error instead of an integrity
	#error -- currently there is duplicate item validation



