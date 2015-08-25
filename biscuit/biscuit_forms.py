from django import forms

from .models import Business

class BusinessNameForm(forms.ModelForm):

	class Meta:
		model = Business
		fields = ('business_name',)

