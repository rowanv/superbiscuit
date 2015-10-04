from django.core.exceptions import ValidationError
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from .forms import BusinessNameForm
from biscuit.models import Walker, Appointment, Dog, Business


def index(request):

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
	context_dict = {'all_walkers': all_walkers,
					'appointments': appointments,
					'all_dogs': all_dogs}
	return render_to_response('business_home.html', context_dict)
