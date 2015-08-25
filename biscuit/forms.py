from django import forms

class BusinessNameForm(forms.form):
	business_name = forms.CharField(label='Business Name', max_length=100, required=True)