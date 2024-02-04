#!/usr/bin/env python3
"""Test client module"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import (
    patch,
    MagicMock,
    PropertyMock
)


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

            with patch.object(GithubOrgClient, "public_repos_url",
                              new_callable=PropertyMock) as mock_repos:
                mock_repos.return_value = a
                a = f"https://api.github.com/orgs/{org_name}/repos"
                mock_get_json.return_value = repos_payload

                github_client = GithubOrgClient(org_name)
                result = github_client.public_repos()

                mock_repos.assert_called_once()
                mock_get_json.assert_called_once_with(
                    f"https://api.github.com/orgs/{org_name}/repos"
                    )
                self.assertEqual(result, ["repos1", "repos2"])
