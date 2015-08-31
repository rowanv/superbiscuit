from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from .biscuit_forms import *
from biscuit.models import Walker

def index(request):

	if request.method == 'POST':
		form = BusinessNameForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/business/')
	else:
		form = BusinessNameForm()

	return render(request, 'index.html', {'form': form})

def business_home(request):
	walker_names = [walker_object.walker_name for walker_object in Walker.objects.all()]
	context_dict = {'dog_walkers': walker_names}
	return render_to_response('business_home.html', context_dict)