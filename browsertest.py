#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import unittest


class BrowserTestCase(unittest.TestCase):

	def __init__(self, methodName='runTest', driver=None):

	        super(BrowserTestCase, self).__init__(methodName)
        	self.driver = driver



	@staticmethod
	def param(testCaseClass, driver=None):

        	testLoader 		= unittest.TestLoader()
	        testCaseNameList	= testLoader.getTestCaseNames(testCaseClass)

	        suite = unittest.TestSuite()

	        for testCaseName in testCaseNameList:
        	    suite.addTest( testCaseClass(testCaseName, driver=driver) )

	        return suite



	def setUp(self):

		pass	



	def tearDown(self):

		pass



"""
class BrowserTest(BrowserTestCase):

	def test_something(self):
        	print 'driver = %s' % self.driver
	        self.assertEqual(1, 1)

	def test_something_else(self):
	        self.assertEqual(2, 3)
"""



if __name__ == '__main__':

	pass
	#suite = unittest.TestSuite()
	#suite.addTest( BrowserTestCase.param(BrowserTest, driver='driver') )
	#result = unittest.TextTestRunner(verbosity=2).run(suite)

	#print "errors: %s" % result.errors
	#print "failures: %s" % result.failures
	#print "test successful: %s" % result.wasSuccessful()
	#print "run test: %s" % result.testsRun
