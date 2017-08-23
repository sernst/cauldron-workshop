from unittest.mock import patch
from unittest.mock import MagicMock

import cauldron as cd
from cauldron.steptest import StepTestCase


class MockResponse:
    """A mock class that mimics the response from requests.get"""

    @property
    def text(self) -> str:
        """Text of the response"""
        return 'a,b,c\n1,2,3\n4,5,6'


class TestNotebook(StepTestCase):
    """Test suite for the notebook"""

    @patch('requests.get')
    def test_step_pull_data(self, requests_get: MagicMock):
        """Should load files into a data frame"""

        requests_get.return_value = MockResponse()
        self.run_step('S01-Pull-Data.py')

        # Data frame should have been shared
        self.assertIsNotNone(cd.shared.df)

        # Total data frame should have two rows for each letter in the
        # alphabet
        self.assertEqual(len(cd.shared.df), 2 * 26)
