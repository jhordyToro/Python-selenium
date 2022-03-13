import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class busqueda_con_selenium(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = cls.driver
        driver.get('http://www.youtube.com')
        driver.maximize_window()

    def test_search_id(self):
        driver = self.driver
        id = driver.find_element_by_id('search')

    def test_search_name(self):
        driver = self.driver
        name = driver.find_element_by_name('search_query')

    def test_search_class(self):
        driver = self.driver
        clas = driver.find_element_by_class_name('ytd-searchbox') 

    def test_search_img(self):
        driver = self.driver
        img = driver.find_element_by_id('img')

    def test_search_Xpath(self):
        driver = self.driver
        xpath = driver.find_element_by_xpath('//*[@id="thumbnail"]/yt-img-shadow')
    #este no corrrio porque creo que no era un elemento css
    def test_search_css(self):
        driver = self.driver
        css = driver.find_element_by_css_selector('div.start yt-icon.guide-icon')
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reporte',report_name = 'xd'))
