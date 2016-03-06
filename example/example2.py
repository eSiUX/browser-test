#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from browsertest import BrowserTestCase


class BrowserTest(BrowserTestCase):


    def setUp(self):
	" Default unittest method call before test "
    	pass



    def tearDown(self):
	" Default unittest method call after test "
	pass



    def testStepByStep(self):

	baseUrl = "https://www.siux.cz"

	self.driver.get(baseUrl)

	menuElem1 = self.driver.find_element_by_link_text("Infrastruktura")

	# check element exists on first page
	self.assertIsNotNone(menuElem1)

	menuElem1.click()

	# check first target URL
        self.assertEquals("%s/sit" % baseUrl, self.driver.current_url)

	menuElem2 = self.driver.find_element_by_link_text("Kontakt")

	# check element exists on second page
	self.assertIsNotNone(menuElem2)

	menuElem2.click()

	# check second target URL
        self.assertEquals("%s/kontakt" % baseUrl, self.driver.current_url)
