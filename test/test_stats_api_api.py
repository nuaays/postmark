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
from postmark.apis.stats_api_api import StatsAPIApi


class TestStatsAPIApi(unittest.TestCase):
    """ StatsAPIApi unit test stubs """

    def setUp(self):
        self.api = postmark.apis.stats_api_api.StatsAPIApi()

    def tearDown(self):
        pass

    def test_get_bounce_counts(self):
        """
        Test case for get_bounce_counts

        Get bounce counts
        """
        pass

    def test_get_outbound_click_counts(self):
        """
        Test case for get_outbound_click_counts

        Get click counts
        """
        pass

    def test_get_outbound_click_counts_by_browser_family(self):
        """
        Test case for get_outbound_click_counts_by_browser_family

        Get browser usage by family
        """
        pass

    def test_get_outbound_click_counts_by_location(self):
        """
        Test case for get_outbound_click_counts_by_location

        Get clicks by body location
        """
        pass

    def test_get_outbound_click_counts_by_platform(self):
        """
        Test case for get_outbound_click_counts_by_platform

        Get browser plaform usage
        """
        pass

    def test_get_outbound_open_counts(self):
        """
        Test case for get_outbound_open_counts

        Get email open counts
        """
        pass

    def test_get_outbound_open_counts_by_email_client(self):
        """
        Test case for get_outbound_open_counts_by_email_client

        Get email client usage
        """
        pass

    def test_get_outbound_open_counts_by_platform(self):
        """
        Test case for get_outbound_open_counts_by_platform

        Get email platform usage
        """
        pass

    def test_get_outbound_open_counts_by_reading_time(self):
        """
        Test case for get_outbound_open_counts_by_reading_time

        Get email read times
        """
        pass

    def test_get_outbound_overview_statistics(self):
        """
        Test case for get_outbound_overview_statistics

        Get outbound overview
        """
        pass

    def test_get_sent_counts(self):
        """
        Test case for get_sent_counts

        Get sent counts
        """
        pass

    def test_get_spam_complaints(self):
        """
        Test case for get_spam_complaints

        Get spam complaints
        """
        pass

    def test_get_tracked_email_counts(self):
        """
        Test case for get_tracked_email_counts

        Get tracked email counts
        """
        pass


if __name__ == '__main__':
    unittest.main()
