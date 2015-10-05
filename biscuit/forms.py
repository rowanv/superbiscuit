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
		fields = ('walker_name','business',)
		widgets = {
			'walker_name': forms.fields.TextInput(attrs={
				'placeholder': 'Enter the name of the dog walker you wish to add',
				'class': 'form-control input-lg',
				}),
		}

	def __init__(self, *args, **kwargs):
		super(DogWalkerNameForm, self).__init__(*args, **kwargs)

		post_data = kwargs.get('data', None)
		if post_data:
			#We received POST data, fill the forms in with the business
			#name returned.
			self.business_name_data = {
				key: post_data[key]
				for key in post_data
				if key.startswith('business_name-')
			}
		else:
			# we didn't get any POST data
			#Fill the forms in with the business data from the linked business
			self.business_name_form = BusinessNameForm(
				prefix='business_name')
	def is_valid(self):
		if not self.business_name_form.is_valid():
			return False
		return super(BusinessNameForm, self).is_valid()

	def save(self, for_business):

		business_name = self.business_name_form.save()

		walker_name = super(DogWalkerNameForm, self).save(*args, **kwargs)

		walker_name.business_name = business_name
		walker_name.save()
		return walker_name

