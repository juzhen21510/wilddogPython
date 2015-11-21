#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import FirebasePythonDataPrepare
from firebase import firebase		
class postTest(unittest.TestCase):
	def setUp(self):
		self.DSN = 'https://geowa.firebaseio.com'
		self.fb = firebase.FirebaseApplication(self.DSN, None)
		FirebasePythonDataPrepare.dataPrepare()
	def test_post(self):
		result1 = self.fb.post('/g', 'juzhen', params=None, headers=None, connection=None)
		result2 = self.fb.post('/g', True, params=None, headers=None, connection=None)
		result3 = self.fb.post('/g', 1, params=None, headers=None, connection=None)
		result4 = self.fb.post('/g', '矩阵', params=None, headers=None, connection=None)
		result5 = self.fb.post('/g', None, params=None, headers=None, connection=None)
if __name__ == '__main__':
    unittest.main()