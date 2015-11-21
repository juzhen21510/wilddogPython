#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import json
import time
import WilddogPythonDataPrepare
from wilddog import WilddogApplication
class putTest(unittest.TestCase):
	def setUp(self):
		self.DSN = 'https://fish1.wilddogio.com'
		self.wilddog = WilddogApplication(self.DSN, None)
		WilddogPythonDataPrepare.dataPrepare()
	def test_put(self):
		result1 = self.wilddog.put('/','sa', {'a':'a'},params=None, headers=None, connection=None) #无中生有
		print result1
		result2 = self.wilddog.put('/','a','lol',params=None, headers=None, connection=None) #改变已有值
		print result2
		result3 = self.wilddog.put('/f','f1', {},params=None, headers=None, connection=None) #赋空值{}相当于删除
		print result3
		result4 = self.wilddog.put('/f','f2', None,params=None, headers=None, connection=None) #赋None 没影响
		print result4
if __name__ == '__main__':
	unittest.main()