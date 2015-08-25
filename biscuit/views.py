from django.shortcuts import render
from django.http import HttpResponse

from .biscuit_forms import *

def index(request):

	if request.method == 'POST':
		form = BusinessNameForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/business/')
	else:
		form = BusinessNameForm()

	return render(request, 'index.html', {'form': form})

def business_home(request):
	return render(request, 'business_home.html')