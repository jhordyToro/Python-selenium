import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class auto(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.maximize_window()
        driver.get('https://google.com')

    def test_autoo(self):
        driver = self.driver
        buscar = driver.find_element_by_name('q')
        buscar.click()
        buscar.clear()
        buscar.send_keys('youtube')
        buscar.submit()

        driver.back()
        driver.forward()
        driver.refresh()

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)

        



