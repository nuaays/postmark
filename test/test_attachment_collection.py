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
from postmark.models.attachment_collection import AttachmentCollection


class TestAttachmentCollection(unittest.TestCase):
    """ AttachmentCollection unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAttachmentCollection(self):
        """
        Test AttachmentCollection
        """
        model = postmark.models.attachment_collection.AttachmentCollection()


if __name__ == '__main__':
    unittest.main()