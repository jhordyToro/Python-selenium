import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class prueba(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver 
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[13]/a').click()

    def test_dynamic(self):
        driver = self.driver
        driver.find_element_by_css_selector('#checkbox').click()
        driver.find_element_by_css_selector('#checkbox-example > button').click()
        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#checkbox-example > button')))
        driver.find_element_by_css_selector('#checkbox-example > button').click()
        
        driver.find_element_by_css_selector('#input-example > button').click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#input-example > input[type=text]')))
        driver.find_element_by_css_selector('#input-example > input[type=text]').send_keys('manuel turizo xd')
        driver.find_element_by_css_selector('#input-example > button').click()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

        