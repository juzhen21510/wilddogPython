#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import json
import time
import WilddogPythonDataPrepare
from wilddog import WilddogApplication
class patchTest(unittest.TestCase):
	def setUp(self):
		self.DSN = 'https://fish1.wilddogio.com'
		self.wilddog = WilddogApplication(self.DSN, None)
		WilddogPythonDataPrepare.dataPrepare()
	def test_patch(self):
		result1 = self.wilddog.patch('/e', {'e2':'e2'}, params=None, headers=None, connection=None)
		result2 = self.wilddog.patch('/e', {'e3': 11}, params=None, headers=None, connection=None)
		result3 = self.wilddog.patch('/e', {'e4': False}, params=None, headers=None, connection=None)
		result4 = self.wilddog.patch('/e', {'e5': '矩阵'}, params=None, headers=None, connection=None)
		result5 = self.wilddog.patch('/e', {'e6': None}, params=None, headers=None, connection=None)
if __name__ == '__main__':
	unittest.main()