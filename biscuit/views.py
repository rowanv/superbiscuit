from django.core.exceptions import ValidationError
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from .forms import BusinessNameForm, DogWalkerNameForm
from biscuit.models import Walker, Appointment, Dog, Business


def index(request):
	if request.method == 'POST':
		form = BusinessNameForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/business')

	return render(request, 'index.html', {'form': BusinessNameForm()})

'''
def index(request):
	business_ = Business.objects.create()
	try:
		business_.full_clean()
		business_.save()
		return HttpResponseRedirect('/business')
	except ValidationError:
		business_.delete()
		error = 'No empty business names'
		return render(request, 'index.html', {'error': error})
	return render(request, 'index.html',
		{'form': BusinessNameForm()})
'''

def business_home(request):
	appointments = Appointment.objects.all()
	all_walkers = Walker.objects.all()
	all_dogs = Dog.objects.all()
	all_businesses = Business.objects.all()
	context_dict = {'all_businesses': all_businesses,
					'all_walkers': all_walkers,
					'appointments': appointments,
					'all_dogs': all_dogs,
					'dog_walker_form': DogWalkerNameForm()}
	if request.method == 'POST':
		form = DogWalkerNameForm(data=request.POST)
		if form.is_valid():
			b = Business.objects.get(business_name='Wiggly Walkers')
			form.business = b
			form.save()
			return render(request, 'business_home.html', context_dict)
	return render(request, 'business_home.html', context_dict)
	#need render instead of render_to_response for csrf token
