#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import FirebasePythonDataPrepare
from firebase import firebase		
class putTest(unittest.TestCase):
	def setUp(self):
		self.DSN = 'https://geowa.firebaseio.com'
		self.fb = firebase.FirebaseApplication(self.DSN, None)
		FirebasePythonDataPrepare.dataPrepare()
	def test_put(self):
		result1 = self.fb.put('/','sa', {'a':'a'},params=None, headers=None, connection=None) #无中生有
		print result1
		result2 = self.fb.put('/','a','lol',params=None, headers=None, connection=None) #改变已有值
		print result2
		result3 = self.fb.put('/f','f1', {},params=None, headers=None, connection=None) #赋空值{}相当于删除
		print result3
		result4 = self.fb.put('/f','f2', None,params=None, headers=None, connection=None) #赋None 相当于删除
		print result4
if __name__ == '__main__':
    unittest.main()