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



    def testForm(self):

	baseUrl = "https://beta.siux.cz"

	self.driver.get("%s/signup" % baseUrl)

	firstnameElem 	= self.driver.find_element_by_id("inp-first-name")
	lastnameElem 	= self.driver.find_element_by_id("inp-last-name")
	emailElem 	= self.driver.find_element_by_id("inp-email")
	btnElem 	= self.driver.find_element_by_css_selector(".btn-success")
	
	# check elements exist
	self.assertIsNotNone(firstnameElem)
	self.assertIsNotNone(lastnameElem)
	self.assertIsNotNone(emailElem)
	self.assertIsNotNone(btnElem)

	firstnameElem.send_keys('Julia')
	lastnameElem.send_keys('Roberts')
	emailElem.send_keys('julia.roberts@siux.cz')

	btnElem.click()

	# ... check new URL or check elements
