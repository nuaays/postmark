# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import postmark
from postmark.rest import ApiException
from postmark.models.extended_message_open_event_information_client import ExtendedMessageOpenEventInformationClient


class TestExtendedMessageOpenEventInformationClient(unittest.TestCase):
    """ ExtendedMessageOpenEventInformationClient unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExtendedMessageOpenEventInformationClient(self):
        """
        Test ExtendedMessageOpenEventInformationClient
        """
        model = postmark.models.extended_message_open_event_information_client.ExtendedMessageOpenEventInformationClient()


if __name__ == '__main__':
    unittest.main()