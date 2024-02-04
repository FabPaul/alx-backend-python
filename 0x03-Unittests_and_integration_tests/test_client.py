#!/usr/bin/env python3
"""Test client module"""

import unittest
from client import GithubOrgClient
from parameterized import (
    parameterized,
    parameterized_class
)
from unittest.mock import (
    patch,
    MagicMock,
    PropertyMock
)
from typing import Dict
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test class"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org_name, expected_result,
                 mocked_function: MagicMock) -> None:
        """Test org"""
        mocked_function.return_value = MagicMock(
            return_value=expected_result)

        github_client = GithubOrgClient(org_name)
        self.assertEqual(github_client.org(), expected_result)
        mocked_function.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )

    def test_public_repos_url(self):
        """Test public repos url"""
        with patch("client.GithubOrgClient", callable=PropertyMock) as mock:
            mock.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos",
                }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/orgs/google/repos"
                )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test public repos"""
        org_name = "google"
        repos_payload = [{"name": "repos1"}, {"name": "repos2"}]

        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = (
                f"https://api.github.com/orgs/{org_name}/repos"
                )
            mock_get_json.return_value = repos_payload

            github_client = GithubOrgClient(org_name)
            result = github_client.public_repos()

            mock_repos.assert_called_once()
            mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}/repos"
                )
            self.assertEqual(result, ["repos1", "repos2"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, ("my_license"), True),
        ({"license": {"key": "other_license"}}, ("my_license"), False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected_result):
        """Test has license"""
        github_client = GithubOrgClient("org_name")
        result = github_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test class"""

    @classmethod
    def setUpClass(cls) -> None:
        """Set Up Class"""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()
        org_payload, repos_payload, expected_repos, apache2_repos = (
            TEST_PAYLOAD[0]
            )

        cls.mock_get.side_effect = [
            MagicMock(json=cls._json_mock(org_payload)),
            MagicMock(json=cls._json_mock(repos_payload)),
            MagicMock(json=cls._json_mock(apache2_repos)),
            MagicMock(json=cls._json_mock(expected_repos)),
        ]

    @classmethod
    def tearDownClass(cls) -> None:
        """Teardown Class"""
        cls.get_patcher.stop()

    @staticmethod
    def _json_mock(return_value):
        """Helper function to createa MagicMock for json method"""
        mock_json = MagicMock(return_value=return_value)
        return mock_json

    def test_public_repos_integration(self):
        """Public repo integration test"""
        github_client = GithubOrgClient("org_name")
        result = github_client.public_repos()
        self.assertEqual(result, self.expected_repos)
