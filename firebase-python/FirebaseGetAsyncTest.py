#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from firebase.firebase import FirebaseApplication, FirebaseAuthentication


if __name__ == '__main__':
    SECRET = 'AXVwrDy1iXGlOgIF44itVhyOu7IswiMwttVtlVvd1'
    DSN = 'https://geowa.firebaseio.com'
    EMAIL = 'juzhen21510@163.com'
    authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
    firebase = FirebaseApplication(DSN, authentication)

    firebase.get('/users', None,
                 params={'print': 'pretty'},
                 headers={'X_FANCY_HEADER': 'very fancy'})

    data = {'name': 'Ozgur Vatansever', 'age': 26,
            'created_at': datetime.datetime.now()}

    snapshot = firebase.post('/users', data)
    print(snapshot['name'])

    def callback_get(response):
        print response
    firebase.get_async('/users', snapshot['name'], callback=callback_get)