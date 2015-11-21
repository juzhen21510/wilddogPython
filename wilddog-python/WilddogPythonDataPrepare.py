#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wilddog import WilddogApplication
def dataPrepare():
	wilddog = WilddogApplication('https://fish1.wilddogio.com',None)
	result = wilddog.put('/','/',{'a':'a','b':'b','c':'c','d':'d','e':{'e1':1,'e2':2},'f':{'f1':{'name':'zidane','age':42,'retire':True,'chineseName':'齐达内'},'f2':{'name':'messi','age':27,'retire':False,'chineseName':'梅西'}}}, params=None, headers=None, connection=None) 
if __name__ == '__main__':
	dataPrepare()