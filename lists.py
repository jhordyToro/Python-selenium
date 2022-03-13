import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class prueba(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver 
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[41]/a').click()

    def test_lists(self):
        driver = self.driver 
        list = [[] for i in range(4)]
        print(list)
        for i in range(4):
            for j in range(5):
                x = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{i + 1}]/td[{j + 1}]')
                list[i].append(x.text)

        print(list)
 
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)