import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class prueba(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver 
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    def test_prueba(self):
        driver = self.driver
        add = int(input('cuantos cuadros quieres agregar? '))
        delete = int(input('cuantos cuadros quieres eliminar? '))
        total = add - delete

        for i in range(add):
            driver.find_element_by_xpath('//*[@id="content"]/div/button').click()
        for i in range(delete):
                try:
                    driver.find_element_by_xpath('//*[@id="elements"]/button').click()
                except:
                    print('estas tratando de eliminar mas de las agregadas')
        print(f'quedaron {total} tablas sin eliminar')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
        


                

