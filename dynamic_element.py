import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class prueba(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver 
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[9]/a').click()

    def test_galeri(self):
        driver = self.driver
        list = []
        cantidad = 5
        contador = 0

        while len(list) < 5:
            list.clear()
            contador += 1
            for i in range(cantidad):
                try:
                    element = driver.find_element_by_xpath(f"/html/body/div[2]/div/div/ul/li[{i + 1}]/a")
                    list.append(element.text)
                    print(list)
                except:
                    driver.refresh()

        print(f'el numero de intentos fue {contador}')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

