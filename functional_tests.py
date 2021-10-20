from selenium import webdriver
import unittest

browser = webdriver.Firefox()

# An all patients files are availbale on the webbroser
browser.get("http://localhost:8000")

header_text = browser.find_element_by_tag_name("h1").text
unittest.assertIn("EMR", header_text)
# A name Textbox, DOB, Address Textbox is available

# When adding a name , address and clicking on add a patient will appear in the list
# When adding a patient a unique id will be visible

# close browser
browser.quit()