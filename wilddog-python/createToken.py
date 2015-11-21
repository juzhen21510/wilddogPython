#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wilddog import wilddog_token_generator

auth_payload = {"uid" : "1111", "provider" : "custom"}
secret = "ofLKdFw3iSpQUCnoqNOnzlEsaCBiccgKrgu83OMK"
token = wilddog_token_generator.create_token(secret, auth_payload)
print token
