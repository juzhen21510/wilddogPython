#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import json
import time
import WilddogPythonDataPrepare
from wilddog import WilddogApplication
class deleteTest(unittest.TestCase):
	def setUp(self):
		self.DSN = 'https://fish1.wilddogio.com'
		self.wilddog = WilddogApplication(self.DSN, None)
		WilddogPythonDataPrepare.dataPrepare()
	def test_delete(self):
		result1 = self.wilddog.delete('/', 'a', params=None, headers=None, connection=None)
		print result1
		result2 = self.wilddog.delete('/', 'k', params=None, headers=None, connection=None)
		print result2
		result3 = self.wilddog.delete('/e', 'e1', params=None, headers=None, connection=None)
		print result3
		result4 = self.wilddog.delete('/f', 'f1', params=None, headers=None, connection=None)
		print result4
		result5 = self.wilddog.delete('/f/f4', 'f2', params=None, headers=None, connection=None)
		print result5
		result6 = self.wilddog.delete('/',None, params=None, headers=None, connection=None)
		print result6
if __name__ == '__main__':
	unittest.main()