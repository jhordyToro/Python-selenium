import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Hello(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello(self):
        driver = self.driver
        driver.get("https://www.youtube.com")

    def test_visit_wikipedia(self):
        self.driver.get("https://www.facebook.com")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__=="__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
