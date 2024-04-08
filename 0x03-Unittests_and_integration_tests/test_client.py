#!/usr/bin/env python3
"""
Module: test_client.py

This module contains the client test
"""


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


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

    @patch('client.GithubOrgClient.org', return_value={
        "login": "test_org",
        "repos_url": "https://api.github.com/orgd/test_org/repos"
        })
    def test_public_repos_url(self, mock_org):
        """
        The method tests the url of public repos
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/test_org/repos"
                )

    @patch('client.GithubOrgClient._public_repos_url')
    @patch('client.GithubOrgClient.get_json')
    def test_public_repos(aelf, mock_get_json, mock_repos_url):
        """
        this method test list of repos from chosen payload
        """
        mock_repos_url.return_value = "https://api.github.com/mock/repos"

        mock_response = [{"name": "Repo 1"}, {"name": "Repo 2"}]
        mock_get_json.return_value = mock_response

        client = GithubOrgClient("org")
        repos = client.public_repos()

        self.assertEqual(repos, mock_response)
        mock_get_json.assert_Called_once_with(
                "https://api.github.com/mock/repos"
                )
        mock_repos_url.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
