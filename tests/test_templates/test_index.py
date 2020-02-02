#!/usr/bin/python3
""" Tests for the view using selenium for python
"""
import unittest
from selenium import webdriver


class Test_index(unittest.TestCase):
    """ Tests the view of the home page index
    """
    def setUp(self):
        """ New set up clase for every test
        """
        self.driver = webdriver.Chrome()
        self.driver.get("https://tusavirus.herokuapp.com/")


    def tearDown(self):
        """Method to be executed after each test
        """
        self.driver.quit()


    def test_submit(self):
        """ Tests if a new element with correct input is correctly submitted
        """
        self.jurisdictions_field = self.driver.find_element_by_name("name")
        self.sick_people_field = self.driver.find_element_by_name("victims")

        self.jurisdictions_field.send_keys("Antioquia")
        self.sick_people_field.send_keys("1 million")
        self.sick_people_field.submit()

        continue_link = self.driver.find_element_by_link_text('Submit')
        self.assertTrue("New jurisdiction added succesfully" in continue_link)
