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



    def testContent(self):

	baseUrl = "https://beta.siux.cz"

	self.driver.get(baseUrl)

	btnElem = self.driver.find_element_by_css_selector("#carousel-hp-content .btn-yellow")

	# check element exists
	self.assertIsNotNone(btnElem)

	btnElem.click()

	# check target URL
        self.assertEquals("%s/signup" % baseUrl, self.driver.current_url)
