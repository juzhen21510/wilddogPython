#!/usr/bin/env python
# -*- coding: utf-8 -*-
from firebase import firebase
def dataPrepare():
	fb = firebase.FirebaseApplication('https://geowa.firebaseio.com',None)
	result = fb.put('/','/',{'a':'a','b':'b','c':'c','d':'d','e':{'e1':1,'e2':2},'f':{'f1':{'name':'zidane','age':42,'retire':True,'chineseName':'齐达内'},'f2':{'name':'messi','age':27,'retire':False,'chineseName':'梅西'}}}, params=None, headers=None, connection=None) 
if __name__ == '__main__':
	dataPrepare()