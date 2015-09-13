from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from .biscuit_forms import *
from biscuit.models import Walker, Appointment, Dog

def index(request):

	if request.method == 'POST':
		form = BusinessNameForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/business/')
	else:
		form = BusinessNameForm()

	return render(request, 'index.html', {'form': form})

def business_home(request):
	appointments = Appointment.objects.all()
	all_walkers = Walker.objects.all()
	all_dogs = Dog.objects.all()
	context_dict = {'all_walkers': all_walkers,
					'appointments': appointments,
					'all_dogs': all_dogs}
	return render_to_response('business_home.html', context_dict)