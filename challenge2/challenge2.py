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
        search_bar = self.driver.find_element_by_id("input-search")
        search_bar.click()
        search_bar.send_keys('Exotics')
        search_button = self.driver.find_element_by_xpath('//*[@id="search-form"]/div/div[2]/button')
        search_button.click()
        # exotics_category = self.driver.find_element_by_link_text("Exotics")
        # exotics_category.click()
        search_results = self.driver.find_elements_by_xpath(\
            "//*[@id='serverSideDataTable']/tbody/tr/td/span[@data-uname='lotsearchLotmake']")
        index = 0
        number_of_porsche = 0
        make_list = []
        for result in search_results:
            result = search_results[index]
            if result.text == "PORSCHE":
                number_of_porsche += 1
            make_list.append(result.text)
            index += 1
        self.driver.implicitly_wait(10)
        print("Test found", number_of_porsche, "results for your search")
        self.assertIn("PORSCHE", make_list)

if __name__=='__main__':
    unittest.main()