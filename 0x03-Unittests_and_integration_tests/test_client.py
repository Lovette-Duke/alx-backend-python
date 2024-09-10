#!/usr/bin/env python3
"""unit and integrated test module """
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """tests GithubOrgClient class"""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """checks if GithubOrgClient class returns the correct value """
        endpoint = 'https://api.github.com/orgs/{}'.format(org_name)
        memo = GithubOrgClient(org_name)
        memo.org()
        mock_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """checks that the _public_repos_url method returns correct value"""
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            res = GithubOrgClient(name)._public_repos_url
            self.assertEqual(res, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """checks that the list of repos is expected repo vaules"""
        json_list = [{"name": "Google"}, {"name": "Yahoo"}]
        org = "mock"
        mock_json.return_value = json_list
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as repos_url:
            repos_url.return_value = 'hello/world'
            res = GithubOrgClient(org).public_repos()
            check = [i["name"] for i in json_list]
            self.assertEqual(res, check)
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """tests the has_license method"""
        res = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(res, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for fixtures """

    @classmethod
    def setUpClass(cls):
        """returns sample payloads in fixtures"""

        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)

        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """stops the patcher"""
        cls.get_patcher.stop()
