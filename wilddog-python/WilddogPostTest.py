#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import json
import time
import WilddogPythonDataPrepare
from wilddog import WilddogApplication
class postTest(unittest.TestCase):
	def setUp(self):
		self.DSN = 'https://fish1.wilddogio.com'
		self.wilddog = WilddogApplication(self.DSN, None)
		WilddogPythonDataPrepare.dataPrepare()
	def test_post(self):
		result1 = self.wilddog.post('/g', 'juzhen', params=None, headers=None, connection=None)
		result2 = self.wilddog.post('/g', True, params=None, headers=None, connection=None)
		result3 = self.wilddog.post('/g', 1, params=None, headers=None, connection=None)
		result4 = self.wilddog.post('/g', '矩阵', params=None, headers=None, connection=None)
		result5 = self.wilddog.post('/g', None, params=None, headers=None, connection=None)

if __name__ == '__main__':
	unittest.main()