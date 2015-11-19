from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string


from biscuit import views



class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.index)


class BusinessPageTest(TestCase):

    def test_business_url_resolves_to_business_view(self):
        found = resolve('/business/')
        self.assertEqual(found.func, views.business_home)


class ClientMetricsPageTest(TestCase):

    def test_client_metrics_url_resolves_to_client_page_view(self):
        found = resolve('/client_metrics/')
        self.assertEqual(found.func, views.client_metrics)

class ClientListPageTest(TestCase):

    def test_client_list_url_resolves_to_client_list_view(self):
        found = resolve('/client_list/')
        self.assertEqual(found.func, views.client_list)

class ClientIndivPageTest(TestCase):

    def test_client_indiv_url_resolves_to_client_indiv_view(self):
        found = resolve('/client_indiv/')
        self.assertEqual(found.func, views.client_indiv)


class WalkerMetricsPageTest(TestCase):

    def test_walker_metrics_url_resolves_to_client_metrics_view(self):
        found = resolve('/walker_metrics/')
        self.assertEqual(found.func, views.walker_metrics)


class WalkerListPageTest(TestCase):

    def test_walker_list_url_resolves_to_walker_list_view(self):
        found = resolve('/walker_list/')
        self.assertEqual(found.func, views.walker_list)


class WalkerIndivPageTest(TestCase):

    def test_walker_indiv_url_resolves_to_walker_indiv_view(self):
        found = resolve('/walker_indiv/')
        self.assertEqual(found.func, views.walker_indiv)

class AppointmentListPageTest(TestCase):

    def test_appointment_list_url_resolves_to_appointment_list_view(self):
        found = resolve('/appointment_list/')
        self.assertEqual(found.func, views.appointment_list)


class AppointmentCalendarPageTest(TestCase):

    def test_appointment_calendar_url_resolves_to_app_calendar_views(self):
        found = resolve('/appointment_calendar/')
        self.assertEqual(found.func, views.appointment_calendar)
