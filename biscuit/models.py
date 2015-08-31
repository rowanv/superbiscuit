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
