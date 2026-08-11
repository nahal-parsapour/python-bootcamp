#
import unittest
from unittest.mock import patch, Mock
import sys, os
import importlib.util
from requests.exceptions import ConnectionError

file_path = os.path.join(os.path.dirname(__file__), '..', 'src', '05RewriteEx1&2_api-client.py')
spec = importlib.util.spec_from_file_location("api_client", file_path)
api_client = importlib.util.module_from_spec(spec)
spec.loader.exec_module(api_client)

class TestAPI(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_all_titles(self, mock_get):
        # Should not be empty and should have at least one title
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"userId": 1, "id": 1, "title": "sunt aut facere"},
            {"userId": 1, "id": 2, "title": "qui est esse"}
        ]
        mock_get.return_value = mock_response

        titles = api_client.fetch_titles_from_api(user_id=1)

        self.assertTrue(len(titles) > 0, "Titles can't be empty")
        self.assertIsInstance(titles, list, "Output must be a list")
        self.assertGreaterEqual(len(titles), 1, "At least one title is required")

        for title in titles:
            self.assertIsInstance(title, str, "Title must be a string")


    @patch('requests.get')
    def test_fetch_titles_from_api(self, mock_get):
        # handles connection error
        mock_get.side_effect = ConnectionError("Simulated connection error")
        titles = api_client.fetch_titles_from_api()
        self.assertEqual(titles, [], "Expected empty list when an error occurs")

if __name__ == '__main__':
    unittest.main()