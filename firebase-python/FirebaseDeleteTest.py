#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import FirebasePythonDataPrepare
from firebase import firebase		
class deleteTest(unittest.TestCase):
	def setUp(self):
		self.DSN = 'https://geowa.firebaseio.com'
		self.fb = firebase.FirebaseApplication(self.DSN, None)
		FirebasePythonDataPrepare.dataPrepare()
	def test_delete(self):
		result1 = self.fb.delete('/', 'a', params=None, headers=None, connection=None)
		print result1
		result2 = self.fb.delete('/', 'k', params=None, headers=None, connection=None)
		print result2
		result3 = self.fb.delete('/e', 'e1', params=None, headers=None, connection=None)
		print result3
		result4 = self.fb.delete('/f', 'f1', params=None, headers=None, connection=None)
		print result4
		result5 = self.fb.delete('/f/f4', 'f2', params=None, headers=None, connection=None)
		print result5
		result6 = self.fb.delete('/',None, params=None, headers=None, connection=None)
		print result6
		
if __name__ == '__main__':
    unittest.main()