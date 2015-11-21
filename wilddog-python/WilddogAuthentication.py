#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wilddog import WilddogApplication
from wilddog import WilddogAuthentication
def authenticationTest():
	secret = 'ofLKdFw3iSpQUCnoqNOnzlEsaCBiccgKrgu83OMK'
	email = 'juzhen@abc.com'
	DSN = 'https://ozil.wilddogio.com'
	authentication = WilddogAuthentication(secret, email, extra={'uid':'1234'})
	wilddog = WilddogApplication(DSN, authentication)
	result = wilddog.get('/student', None)
	print result
 
if __name__ == '__main__':
    authenticationTest()
