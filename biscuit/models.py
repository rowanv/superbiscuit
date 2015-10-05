from django.db import models
from django.utils import timezone

class Business(models.Model):
	business_name = models.CharField(max_length=100)

	def __str__(self):
		return self.business_name

class Walker(models.Model):
	walker_name = models.CharField(max_length=100)
	business = models.ForeignKey(Business, null=True, blank=True)

	def __str__(self):
		return str(self.walker_name) + ' - ' + str(self.business)

class Dog(models.Model):
	name = models.CharField(max_length=100)
	owner = models.CharField(max_length=100)
	breed = models.CharField(max_length=100, default='Friendly Mutt')
	birthday = models.DateField()

	def __str__(self):
		return self.name

class Owner(models.Model):
	owner_first_name = models.CharField(max_length=100)
	owner_last_name = models.CharField(max_length=100)
	owner_email = models.EmailField()

	owner_address_1 = models.CharField(max_length=100, null=True, blank=True)
	owner_address_2 = models.CharField(max_length=100, null=True, blank=True)
	owner_address_city = models.CharField(max_length=100, null=True, blank=True)
	owner_address_state = models.CharField(max_length=100, null=True, blank=True)
	owner_address_country = models.CharField(max_length=100, null=True, blank=True)

	client_since = models.DateTimeField(default=timezone.now())

	business = models.ForeignKey(Business, null=True, blank=True)

	def __str__(self):
		return str(self.owner_first_name) + ' ' + str(self.owner_last_name)


class Appointment(models.Model):
	time = models.DateTimeField() #represented in Python by a datetime.datetime instance.
	dog_walked = models.ForeignKey(Dog)

	def __str__(self):
		return(str(self.time) + str(self.dog_walked))

