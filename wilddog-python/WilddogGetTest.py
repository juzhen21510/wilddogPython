#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import json
import time
import WilddogPythonDataPrepare
from wilddog import WilddogApplication
		
class getTest(unittest.TestCase):
	def setUp(self):
		self.DSN = 'https://fish1.wilddogio.com'
		self.wilddog = WilddogApplication(self.DSN, None)
		WilddogPythonDataPrepare.dataPrepare()
	def test_get_str(self):
		result = self.wilddog.get('/a', None)
		self.assertEqual(result, 'a')
	def test_get_boolean(self):
		result = self.wilddog.get('/f/f1/retire', None)
		self.assertEqual(result, True)
	def test_get_number(self):
		result = self.wilddog.get('/e/e1', None)
		self.assertEqual(result, 1)
	def test_get_chinese(self):
		result1 = self.wilddog.get('/f/f1', None)
		print result1
	def test_get_all(self):
		result = self.wilddog.get('/', None)
		print result
if __name__ == '__main__':
    unittest.main()