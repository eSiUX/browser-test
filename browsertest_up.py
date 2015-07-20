#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import xmlrpclib, os


class BrowserTestUp():

	def __init__(self, browserTestModule='', client=None, advanceId=None, siuxApi='http://api.esiux.net:3035/RPC2'):

		self.__browserTestModule 	= browserTestModule
		self.__client			= client
		self.__advanceId		= advanceId

		self.__rpc = xmlrpclib.ServerProxy(siuxApi)


		
	def upload(self, desc=''):

		ret = {
			'statusCode'	: 'OK',
			'statusMessage'	: 'Advanced browser test uploaded.'
		}

		if not os.path.exists(self.__browserTestModule):
			ret['statusCode']	= 'WRONG_ARG'
			ret['statusMessage']	= 'File not exist'
			return ret

		moduleFile 	= self.__browserTestModule.split('/')[-1]
		module		= moduleFile.split('.')[0]

		try:	
			browserTestModule = __import__(module)

		except SyntaxError, err:
			ret['statusCode'] 	= 'WRONG_ARG'
			ret['statusMessage']	= err

			return ret

		try:
			browserTestModule.BrowserTest

		except AttributeError:
			ret['statusCode'] 	= 'WRONG_ARG'
			ret['statusMessage']	= "Module has no class 'BrowserTest'"

			return ret

		attrList = dir(browserTestModule.BrowserTest)

		testMethod = [ attr for attr in attrList if attr.startswith('test') ]

		if not testMethod:

			ret['statusCode']	= 'WRONG_ARG'
			ret['statusMessage']	= 'Not exist test method'

			return ret

		defUnitTestMethod = [ attr for attr in attrList if attr in ('tearDown', 'setUp') ]

		if len(defUnitTestMethod) != 2:
			ret['statusCode'] 	= 'WRONG_ARG'
			ret['statusMessage']	= 'BrowserTest is not instance of unittest'

			return ret

		f = open(self.__browserTestModule, 'r')
		fileData = f.read()

		retAdvancedCodeAdd = self.__rpc.selenium.advanced.code.add(self.__client, self.__advanceId, fileData, desc)

                return retAdvancedCodeAdd



if __name__ == '__main__':
	
	bTU = BrowserTestUp('MODULE_FILE', 'CLIENT_HASH', 'ADVANCE_ID', 'http://localhost:3035')

	retUpload = bTU.upload()
	print retUpload
