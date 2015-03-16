# -*- coding:utf-8 -*-
"""
Author: Rick James
Date: 3-16-2015
Purpose: Rubicon ISE Interview

Todo:
    - Integrate exceptions with base App or keep blueprint
        specific isolated?

"""

class APIException(Exception):

    def __init__(self, message, status_code=None,
        payload=None, request=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        self.request = request

    def to_dict(self):
        response = dict(self.payload or ())
        response['message'] = self.message
        return response

