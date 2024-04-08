#!/usr/bin/env python3
"""
Module: test_client.py

This module contains the client test
"""


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    This class tests the GithubOrgClient
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    @patch('client.GithubOrgClient._GithubOrgClient__session.get')
    def test_org(self, org_name, mock_get):
        """
        This metod tests if GithubOrgClient.rg returns the correct value
        """
        test_url = f'https://api.github.com/orgs/{org_name}'
        expected_result = mock_get.return_value
        expected_result.json.return_value = {"payload": "test_payload"}

        client = GithubOrgClient(org_name)
        response = client.org

        self.assertEqual(response, expected_result.json.return_value)
        mock_get.assert_called_once_with(test_url)
        expected_result.json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
