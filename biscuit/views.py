from django.shortcuts import render
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
	dog_walker_list = Walker.objects.all()
	context_dict = {'dog_walkers': dog_walker_list}
	return render(request, 'business_home.html', context_dict)