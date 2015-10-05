from django import forms
from biscuit.models import Business, Walker, Owner


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
		fields = ('walker_name', 'business')
		widgets = {
			'walker_name': forms.fields.TextInput(attrs={
				'placeholder': 'Enter the name of the dog walker you wish to add',
				'class': 'form-control input-lg',
				}),
		}

	def __init__(self, *args, **kwargs):
		super(DogWalkerNameForm, self).__init__(*args, **kwargs)

class OwnerInfoForm(forms.models.ModelForm):

	class Meta:
		model = Owner
		fields = ('owner_first_name', 'owner_last_name', 'owner_email',
			'owner_address_1', 'owner_address_2', 'owner_address_city',
			'owner_address_state', 'owner_address_country',
			'business')
		widgets = {
			'owner_first_name': forms.fields.TextInput(attrs={
				'placeholder': 'First Name',
				'class': 'form-control input-lg',
				}),
		}
	#TODO: fix this form's styling


