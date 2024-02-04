#!/usr/bin/env python3
"""Test client module"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import (
    patch,
    MagicMock
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