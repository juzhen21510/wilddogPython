#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import FirebasePythonDataPrepare
from firebase import firebase		
class getTest(unittest.TestCase):
	def setUp(self):
		self.DSN = 'https://geowa.firebaseio.com'
		self.fb = firebase.FirebaseApplication(self.DSN, None)
		FirebasePythonDataPrepare.dataPrepare()
	def test_get_str(self):
		result = self.fb.get('/a', None)
		self.assertEqual(result, 'a')
	def test_get_boolean(self):
		result = self.fb.get('/f/f1/retire', None)
		self.assertEqual(result, True)
	def test_get_number(self):
		result = self.fb.get('/e/e1', None)
		self.assertEqual(result, 1)
	def test_get_chinese(self):
		result1 = self.fb.get('/f/f1/chineseName', None)
		print result1
	def test_get_all(self):
		result = self.fb.get('/', None)
		print result
class getAsyncTest(unittest.TestCase):
	def setUp(self):
		self.DSN = 'https://geowa.firebaseio.com'
		self.fb = firebase.FirebaseApplication(self.DSN, None)
		FirebasePythonDataPrepare.dataPrepare()
	def cb(response):
		print response
	def test_get_async(self):
		result = self.fb.get_async('/', None, callback=cb)
if __name__ == '__main__':
    unittest.main()