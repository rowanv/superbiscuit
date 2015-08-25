from django.db import models

class Business(models.Model):
	business_name = models.CharField(max_length=100)

	def __str__(self):
		return self.business_name
