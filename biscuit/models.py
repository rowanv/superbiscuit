from django.db import models
from django.utils import timezone

import pandas as pd


class Business(models.Model):
	business_name = models.CharField(max_length=100)

	def __str__(self):
		return self.business_name

class Walker(models.Model):
	walker_name = models.CharField(max_length=100)
	business = models.ForeignKey(Business, null=True, blank=True)

	def __str__(self):
		return str(self.walker_name) + ' - ' + str(self.business)

class Dog(models.Model):
	name = models.CharField(max_length=100)
	owner = models.CharField(max_length=100)
	breed = models.CharField(max_length=100, default='Friendly Mutt')
	birthday = models.DateField()

	def __str__(self):
		return self.name

class Owner(models.Model):
	owner_first_name = models.CharField(max_length=100)
	owner_last_name = models.CharField(max_length=100)
	owner_email = models.EmailField()

	owner_address_1 = models.CharField(max_length=100, null=True, blank=True)
	owner_address_2 = models.CharField(max_length=100, null=True, blank=True)
	owner_address_city = models.CharField(max_length=100, null=True, blank=True)
	owner_address_state = models.CharField(max_length=100, null=True, blank=True)
	owner_address_country = models.CharField(max_length=100, null=True, blank=True)

	client_since = models.DateTimeField(default=timezone.now())

	business = models.ForeignKey(Business, null=True, blank=True)

	def __str__(self):
		return str(self.owner_first_name) + ' ' + str(self.owner_last_name)


class Appointment(models.Model):
	time = models.DateTimeField() #represented in Python by a datetime.datetime instance.
	dog_walked = models.ForeignKey(Dog)

	def __str__(self):
		return(str(self.time) + str(self.dog_walked))





class ItemResponse:
    '''represents a response to a SQL query from a database'''

    def __init__(self, query):
        self.query = query



class SingleItemResponse(ItemResponse):

    def __init__(self, connection, query):
        ItemResponse.__init__(self, query)

    def fetch_result(self):
    	pass


class TableItemResponse(ItemResponse):

    def __init__(self, query):
        ItemResponse.__init__(self, query)

    def fetch_table(self):
        pass


class Vignette:
    '''Represents a single item of visual representation on dashboard'''

    def __init__(self, query):
        self.query = query



class IndicatorPanel(Vignette):
    '''Represents an indicator panel vignette in dashboard'''

    def __init__(self, query):
        Vignette.__init__(self, query)
        if query is not None:
            self.panel_num = SingleItemResponse(connection, query).fetch_result()
        self.panel_colour_to_class_mapping = {
            'blue': 'panel-primary',
            'green': 'panel-green',
            'yellow': 'panel-yellow',
            'red': 'panel-red'
        }
        self.panel_icon_to_class_mapping = {
            'shopping_cart': 'fa-shopping-cart',
            'comments': 'fa-comments',
            'tasks': 'fa-tasks',
            'support': 'fa-support'
        }

    def set_values(self, panel_colour, panel_icon, panel_text, *args):
        self.panel_class = self.panel_colour_to_class_mapping[panel_colour]
        self.icon_class = self.panel_icon_to_class_mapping[panel_icon]
        self.panel_text = panel_text
        if args:
            self.panel_details_link = args[0]
        else:
            self.panel_details_link = None


    def get_html_rep(self):
        panel_html = '''
                <div class="col-lg-3 col-md-6">
                    <div class="panel {}">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa {} fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">{}</div>
                                    <div>{}</div>
                                </div>
                            </div>
                        </div>
                        <a href="{}">
                            <div class="panel-footer">
                                <span class="pull-left">View Details</span>
                                <span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>
                                <div class="clearfix"></div>
                            </div>
                        </a>
                    </div>
                </div>
        '''.format(self.panel_class, self.icon_class,
                   self.panel_num, self.panel_text, self.panel_details_link)
        return panel_html


