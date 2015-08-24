from selenium import webdriver
import unittest

browser = webdriver.Firefox()



class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_business_and_view_its_information_later(self):
		

		# Our enterprising user, Veronica, owner of a dog-walking business has
		# heard of a cool new app for helping them run their dog walking business.

		# They checkout the app's homepage
		self.browser.get('http://localhost:8000')

		# And are greeted by a welcome screen.
		self.assertIn('Welcome to Biscuit!', self.browser.title)
		self.fail('Finish the test!')


		# They are invited to enter the name of their business right away.

		# They navigate to a new page, where they see their business name in the header

		# They are then invited to enter their dog walkers' names.

		# Veronica enters their dog walkers' names (Veronica, Juan, and Mateo).

		# Veronica sees that the page updates with the dog walker names.

		# Veronica then enters the name of one of their clients: Victoria,
		# along with the client's two dogs: Floofy and Snoopy.

		# Veronica sees that the client section updates with the client's names

		# Veronica adds a repeating dog walking appointment on Wednesdays at 1 pm
		# for both Floofy and Snoopy. These dog walking appointments are assigned
		# to Juan.

		# When Veronica goes back to the home screen and clicks on the <view schedule>
		# button next to Juan, they see that Floofy and Snoopy's appointments have
		# been added to Juan's schedule.

		# Satisfied, they go exit the home page and go to sleep. 
		browser.quit()

if __name__ == '__main__':
	unittest.main()
