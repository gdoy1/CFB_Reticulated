import unittest
from selenium import webdriver
class Testindex(unittest.TestCase):
    """class to test basic functionality of a web-based input form"""
    def setUp(self):
        """set up function to set the web driver, in this case chrome"""
        self.driver=webdriver.Chrome('./chromedriver')

    def test_input_form (self):
        driver= self.driver
        driver.get("file:///:C:/Users/elfre/PycharmProjects/CFB_Reticulated/app/tests")

        driver.fine_element_by_id("patients-age").send_keys("70")
        driver.find_element_by_id("patients-weight").send_keys("70")
        driver.fine_element_by_id("female-button").click()
        driver.fine_element_by_id("ok-button").click()

if __name__=="__main__":
    unittest.main()