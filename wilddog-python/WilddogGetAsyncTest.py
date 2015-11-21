#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from wilddog import WilddogApplication, WilddogAuthentication


if __name__ == '__main__':
    SECRET = 'e133UCbA5KjMnJrynk2Bb7FEo9raMAhHob7eqMWh'
    DSN = 'https://fish1.wilddogio.com'
    EMAIL = 'juzhen@wilddog.com'
    authentication = WilddogAuthentication(SECRET,EMAIL, True, True, extra={'uid':'1234'})
    wilddog = WilddogApplication(DSN, authentication)

    wilddog.get('/users', None,
                 params={'print': 'pretty'},
                 headers={'X_FANCY_HEADER': 'very fancy'})

    data = {'name': 'Ozgur Vatansever', 'age': 26,
            'created_at': datetime.datetime.now()}

    snapshot = wilddog.post('/users', data)
    print('***' + snapshot['name'])

    def callback_get(response):
        print response
    wilddog.get_async('/users', snapshot['name'], callback=callback_get)