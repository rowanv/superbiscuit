from django import forms
from biscuit.models import Business, Walker

class BusinessNameForm(forms.Modelform):
	business_name = forms.CharField(label='Business Name', max_length=100, required=True)

	class Meta:
		model = Business

class DogWalkerForm(forms.ModelForm):
	walker = forms.CharField(label='Dog Walker Name', max_length=100, required=True)
	class Meta:
		model = Walker
