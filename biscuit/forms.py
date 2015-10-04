from django import forms
from biscuit.models import Business, Walker


class BusinessNameForm(forms.models.ModelForm):

	class Meta:
		model = Business
		fields = ('business_name',)
		widgets = {
		'text': forms.fields.TextInput(attrs={
			'placeholder': 'Enter a business name',
			'class': 'form-control input-lg',
			}),
		}






class DogWalkerForm(forms.models.ModelForm):

	class Meta:
		model = Walker
		fields = ('walker_name','business',)
		widgets = {
			'text': forms.fields.TextInput(attrs={
				'placeholder': 'Enter a dog walker name',
				'class': 'form-control input-lg',
				}),
		}
