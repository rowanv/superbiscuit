import os
import datetime
import django


def populate():
    rover = Dog(name='Rover',
        owner='Beatriz',
        breed='Doberman Pinscher',
        birthday=datetime.date(2014,1,3))
    rover.save()

    sue = Dog(name='Sue',
        owner='Beatriz',
        breed='Chihuahua',
        birthday=datetime.date(2011,7,1))
    sue.save()

    miles = Dog(name='Miles',
        owner='Maite',
        breed='German Shepherd',
        birthday=datetime.date(2010,4,12))
    miles.save()

    appointment_1 = Appointment(
        time=datetime.datetime(2015,9,12,8,30),
        dog_walked=rover)
    appointment_1.save()

    appointment_2 = Appointment(
        time=datetime.datetime(2015,9,13,8,30),
        dog_walked=rover)
    appointment_2.save()

    appointment_3 = Appointment(
        time=datetime.datetime(2015,9,14,8,30),
        dog_walked=rover)
    appointment_3.save()

    appointment_4 = Appointment(
        time=datetime.datetime(2015,9,15,8,30),
        dog_walked=rover)
    appointment_4.save()

    appointment_5 = Appointment(
        time=datetime.datetime(2015,9,16,8,30),
        dog_walked=rover)
    appointment_5.save()

    appointment_6 = Appointment(
        time=datetime.datetime(2015,10,1,11,00),
        dog_walked=miles)
    appointment_6.save()

    appointment_7 = Appointment(
        time=datetime.datetime(2015,10,3,11,00),
        dog_walked=miles)
    appointment_7.save()

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
    for d in Dog.objects.all():
        print(d)
    for a in Appointment.objects.all():
        print(a)

def add_business(business):
    b = Business.objects.get_or_create(business_name=business)
    return b

def add_walker(business, walker_name):
    b_id = Business.objects.get(business_name=business).id
    w = Walker.objects.get_or_create(business_id=b_id, walker_name=walker_name)
    return w
def add_dog(name, owner, breed, birthday):
    name = Dog.objects.get_or_create(name=name)


if __name__ == '__main__':
    print('Starting Biscuit population script...')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superbiscuit.settings')
    django.setup()
    from biscuit.models import Business, Walker, Dog, Appointment
    populate()