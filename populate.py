import os
import django

def populate():
    wiggly_walkers = add_business('Wiggly Walkers')
    add_walker(business='Wiggly Walkers', walker_name='Alfredo')
    add_walker(business='Wiggly Walkers', walker_name='Adelaide')
    add_walker(business='Wiggly Walkers', walker_name='Anton')
    we_walk_your_pup = add_business('We Walk Your Pup')
    add_walker('We Walk Your Pup', walker_name='Camille')
    add_walker('We Walk Your Pup', walker_name='Carine')
    add_walker('We Walk Your Pup', walker_name='Bruno')
    pups_ahoy = add_business('Pups Ahoy')
    add_walker('Pups Ahoy', walker_name='Diane')
    add_walker('Pups Ahoy', walker_name='Estelle')
    add_walker('Pups Ahoy', walker_name='Eric')
    for b in Business.objects.all():
        for w in Walker.objects.filter(business=b):
            print ("- {0} - {1}".format(str(b), str(w)))

def add_business(business):
    b = Business.objects.get_or_create(business_name=business)
    return b

def add_walker(business, walker_name):
    b_id = Business.objects.get(business_name=business).id
    w = Walker.objects.get_or_create(business_id=b_id, walker_name=walker_name)
    return w

if __name__ == '__main__':
    print('Starting Biscuit population script...')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superbiscuit.settings')
    django.setup()
    from biscuit.models import Business, Walker
    populate()