from selenium import webdriver
import unittest


class PatientOverviewTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_access_the_overview_page(self):
        # An all patients files are availbale on the webbroser
        self.browser.get("http://localhost:8000")

        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("EMR", header_text)


# A name Textbox, DOB, Address Textbox is available

# When adding a name , address and clicking on add a patient will appear in the list
# When adding a patient a unique id will be visible

# close browser
