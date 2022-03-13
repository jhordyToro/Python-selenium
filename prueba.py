import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class RegisterNewUser(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo.onestepcheckout.com/")
	def test_try(self):
		driver =self.driver
		driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[1]').click()
		driver.find_element_by_link_text('Log In').click()
		driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span').click()
		self.assertEqual('Create New Customer Account', driver.title)

		firstname = driver.find_element_by_id('firstname')
		lastname = driver.find_element_by_id('lastname')
		email = driver.find_element_by_id('email_address')
		password = driver.find_element_by_id('password')
		confirmar = driver.find_element_by_id('confirmation')
		Button = driver.find_element_by_id('is_subscribed')
		enviar = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')

		self.assertTrue(firstname.is_enabled() 
		and lastname.is_enabled()
		and email.is_enabled()
		and password.is_enabled()
		and confirmar.is_enabled()
		and Button.is_enabled()
		and enviar.is_enabled())

		firstname.send_keys('Test')
		lastname.send_keys('Test')
		email.send_keys('arqcftlothxuknlxkt@awdrt.com') #sacado de 10-minute mail
		password.send_keys('Test')
		confirmar.send_keys('Test')
		enviar.click()
 
	def tearDown(self):	
		self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)
