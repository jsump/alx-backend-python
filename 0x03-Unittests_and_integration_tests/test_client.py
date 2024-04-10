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
        expected_result = {"payload": "test_payload"}

        mock_get.return_value = expected_result

        client = GithubOrgClient(org_name)
        response = client.org

        self.assertEqual(response, expected_result)
        mock_get.assert_called_once_with(test_url)

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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_license(self, repo, license_key, expected_Result):
        """
        Test whether GithubOrgClient has license
        """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(
        (
            'org_payload',
            'repos_payload',
            'expected_repos',
            'apache2_repos'
            ),
        [(org_payload, repos_payload, expected_repos, apache2_repos)])
class TestIntergrationGithubOrgClient(unittest.TestCase):
    """
    This class tests intergration
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up class
        """
        clas.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """
            This method makes sure the mock or requests returns correct values
            """
            if url == 'https://api/github.com/orgs/test_org':
                return Mock(json=lambda: cls.org_payload)
            elif url == 'https://api.github.com/orgs/test_org/repos':
                return Mock(json=lambda: cls.repos_payload)

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownclass(cls):
        """
        this method stops the patcher
        """
        cls.get_patcher.stop()

    def test_puplic_repos(self):
        """
        test public repos
        """
        client = githubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public repos with license
        """
        client = GithubOrgClient("test_org")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
