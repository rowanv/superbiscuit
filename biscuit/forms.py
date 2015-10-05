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
		exclude = ('business',)
		widgets = {
			'walker_name': forms.fields.TextInput(attrs={
				'placeholder': 'Enter the name of the dog walker you wish to add',
				'class': 'form-control input-lg',
				}),
		}

	def __init__(self, *args, **kwargs):
		super(DogWalkerNameForm, self).__init__(*args, **kwargs)

	def clean(self):
		business_name = self.cleaned_data.get('business_name')
		if not business_name:
			raise forms.ValidationError('Must specify a business')
		return super(BusinessNameForm, self).clean()

