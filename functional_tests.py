from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
		'''
		# And are greeted by a welcome screen.
		self.assertIn('Welcome to Biscuit', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Biscuit', header_text)

		# They are invited to enter the name of their business right away.
		inputbox = self.browser.find_element_by_id('id_new_business')

		inputbox.send_keys('Wagging Tails')
		inputbox.send_keys(Keys.ENTER)

		# They navigate to a new page, where they see their business name in the header
		self.browser.implicitly_wait(3)
		'''

	def test_can_view_business_information(self):
		self.browser.get('http://localhost:8000/business/')

		welcome_message = self.browser.find_element_by_tag_name('h2').text
		self.assertIn('Wiggly Walkers', welcome_message)

		# They are then invited to enter their dog walkers' names.
		#self.fail('Finish the test!')
		walker_input_box = self.browser.find_element_by_id('id_walker_name')
		walker_input_box.send_keys('Sue')
		walker_input_box.send_keys(Keys.ENTER)

		# They then see their dog walker added to the dog walker table
		walkers_table = self.browser.find_element_by_id('id_dog_walkers_list')
		walker_rows = walkers_table.find_elements_by_tag_name('p')
		self.assertIn('Sue - Wiggly Walkers',
			[walker_row.text for walker_row in walker_rows])

		# Veronica then enters the name of one of their clients: Victoria,
		# along with the client's two dogs: Floofy and Snoopy.
		client_input_box = self.browser.find_element_by_id('id_client_name')
		dog_input_box = self.browser.find_element_by_id('id_dog_name')

		client_input_box.send_keys('Victoria')
		client_input_box.send_keys('Floofy')

		client_table = self.browser.find_element_by_id('id_client_list')
		client_rows = client_table.find_element_by_id('p')

		self.assertIn('Victoria - Floofy',
			[client_row.text for client_row in client_rows])

		# Veronica sees that the client section updates with the client's names

		# Veronica adds a repeating dog walking appointment on Wednesdays at 1 pm
		# for both Floofy and Snoopy. These dog walking appointments are assigned
		# to Juan.

		# When Veronica goes back to the home screen and clicks on the <view schedule>
		# button next to Juan, they see that Floofy and Snoopy's appointments have
		# been added to Juan's schedule.

		# Satisfied, they go exit the home page and go to sleep.

	def test_can_add_a_dog_walker_and_view_its_information_later(self):
		self.browser.get('http://localhost:8000/business/')

		dog_walkers_list = self.browser.find_element_by_id('id_dog_walkers_list').text
		self.assertIn('Camille', dog_walkers_list)

		#TODO: Test that can add a dog walker


if __name__ == '__main__':
	unittest.main()
