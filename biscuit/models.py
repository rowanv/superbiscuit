from django.db import models

class Business(models.Model):
	business_name = models.CharField(max_length=100)

	def __str__(self):
		return self.business_name

class Walker(models.Model):
	business = models.ForeignKey(Business)
	walker_name = models.CharField(max_length=100)

	def __str__(self):
		return self.walker_name

class Dog(models.Model):
	name = models.CharField(max_length=100)
	owner = models.CharField(max_length=100)
	breed = models.CharField(max_length=100, default='Friendly Mutt')
	birthday = models.DateField()

	def __str__(self):
		return self.name


class Appointment(models.Model):
	time = models.DateTimeField() #represented in Python by a datetime.datetime instance.
	dog_walked = models.ForeignKey(Dog)

	def __str__(self):
		return(str(self.time) + dog_walked)

