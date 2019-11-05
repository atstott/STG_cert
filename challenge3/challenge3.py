import unittest
from selenium import webdriver

class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/atstott/chromedriver.exe")
        self.driver.implicitly_wait(100)

    def tearDown(self):
        self.driver.close()
        print("Good Job Andrew")

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        popular_items = self.driver.find_elements_by_xpath("\
            //*[@id='tabTrending']/div[1]/div/div/ul/li/a")
        for item in popular_items:
            print(item.text, item.get_attribute("href"))

if __name__=='__main__':
    unittest.main()