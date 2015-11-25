from django.core.exceptions import ValidationError
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .forms import BusinessNameForm, DogWalkerNameForm, OwnerInfoForm
from biscuit.models import Walker, Appointment, Dog, Business, Owner, IndicatorPanel


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
    b = Business.objects.get(business_name='Wiggly Walkers')
    appointments = Appointment.objects.all()
    all_dogs = Dog.objects.all()
    all_businesses = Business.objects.all()
    context_dict = {'all_businesses': all_businesses,
                    'appointments': appointments,
                    'all_dogs': all_dogs,
                    'dog_walker_form': DogWalkerNameForm(initial={'business': b}),
                    }
    if request.method == 'POST':
        form = DogWalkerNameForm(data=request.POST)
        if form.is_valid():
            w = form.save()
            w.save()
        return render(request, 'business_home.html', context_dict)
    return render(request, 'business_home.html', context_dict)
    #need render instead of render_to_response for csrf token

def owner_list_add(request):
    b = Business.objects.get(business_name='Wiggly Walkers')
    all_owners = Owner.objects.all()
    context_dict = {'all_owners': all_owners,
                    'form': OwnerInfoForm(initial={'business': b})}
    if request.method == 'POST':
        form = OwnerInfoForm(data=request.POST)
    return render(request, 'owner_list_add.html', context_dict)

def client_metrics(request):
    return render(request, 'client_metrics.html')

def client_list(request):
    return render(request, 'client_list.html')

def client_indiv(request):
    return render(request, 'client_indiv.html')

def walker_metrics(request):
    walker_list_link = '/business/walker_list/'
    blue_panel = IndicatorPanel(None)
    blue_panel.set_values('blue', 'tasks', 'Total No. of Walkers', walker_list_link)
    total_walkers = len([x for x in Walker.objects.all()])
    blue_panel.panel_num = str(total_walkers)
    #To do: add if statement to limit to this business' walkers
    green_panel = IndicatorPanel(None)
    green_panel.set_values('green', 'comments', 'Most Walks', walker_list_link)
    green_panel.panel_num = 'Sue'
    #TO DO: have this actually pull walker with most walks

    yellow_panel = IndicatorPanel(None)
    yellow_panel.set_values('yellow', 'tasks', 'Walkers Added This Mo.',
        walker_list_link)
    yellow_panel.panel_num = '1'

    red_panel = IndicatorPanel(None)
    red_panel.set_values('red', 'support', 'Lost This Month', walker_list_link)
    red_panel.panel_num = '0'

    context_dict = {
    'panels_html': [
            green_panel.get_html_rep(),
            blue_panel.get_html_rep(),
            yellow_panel.get_html_rep(),
            red_panel.get_html_rep(),

        ],
    }
    print(blue_panel.get_html_rep())
    return render(request, 'walker_metrics.html', context_dict)

def walker_list(request):
    all_walkers = Walker.objects.all()
    b = Business.objects.get(business_name='Wiggly Walkers')
    context_dict = {'all_walkers': all_walkers,
                    'dog_walker_form': DogWalkerNameForm(initial={'business': b}),
                    }

    if request.method == 'POST':
        form = DogWalkerNameForm(data=request.POST)
        if form.is_valid():
            w = form.save()
            w.save()
        return render(request, 'walker_list.html', context_dict)
    return render(request, 'walker_list.html', context_dict)

def walker_indiv(request, walker_id):
    context_dict = {
        'walker_data': Walker.objects.get(id=walker_id)
    }
    if not walker_id:
        raise Http404('You must provide a Walker ID')
    return render(request, 'walker_indiv.html', context_dict)

def appointment_calendar(request):
    return render(request, 'appointment_calendar.html')

def appointment_list(request):
    return render(request, 'appointment_list.html')

