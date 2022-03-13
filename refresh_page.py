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
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[43]/a').click()

    def test_typo(self):
        driver = self.driver 
        typo = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
        texto = typo.text
        asert = ("Sometimes you'll see a typo, other times you won,t.")
        intentos = 1

        while texto != asert:
            intentos += 1
            driver.refresh()
            typo = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
            texto = typo.text
        if texto == asert:
            print(f'le tomo {intentos} intentos :D')
            print(texto)
            print(asert)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2) 