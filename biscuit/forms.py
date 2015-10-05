from django import forms
from biscuit.models import Business, Walker


class BusinessNameForm(forms.models.ModelForm):

	class Meta:
		model = Business
		fields = ('business_name',)
		widgets = {
		'business_name': forms.fields.TextInput(attrs={
			'placeholder': 'Enter a business name',
			'class': 'form-control input-lg',
			}),
		}






class DogWalkerNameForm(forms.models.ModelForm):

	class Meta:
		model = Walker
		fields = ('walker_name',)
		widgets = {
			'walker_name': forms.fields.TextInput(attrs={
				'placeholder': 'Enter the name of the dog walker you wish to add',
				'class': 'form-control input-lg',
				}),
		}


