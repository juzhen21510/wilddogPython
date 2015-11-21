#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import FirebasePythonDataPrepare
from firebase import firebase		
class patchTest(unittest.TestCase):
	def setUp(self):
		self.DSN = 'https://geowa.firebaseio.com'
		self.fb = firebase.FirebaseApplication(self.DSN, None)
		FirebasePythonDataPrepare.dataPrepare()
	def test_patch(self):
		result1 = self.fb.patch('/e', {'e2':'e2'}, params=None, headers=None, connection=None)
		result2 = self.fb.patch('/e', {'e4': 11}, params=None, headers=None, connection=None)
		result3 = self.fb.patch('/e', {'e5': False}, params=None, headers=None, connection=None)
		result4 = self.fb.patch('/e', {'e6': '矩阵'}, params=None, headers=None, connection=None)
		result5 = self.fb.patch('/e', {'e7': None}, params=None, headers=None, connection=None)
if __name__ == '__main__':
    unittest.main()