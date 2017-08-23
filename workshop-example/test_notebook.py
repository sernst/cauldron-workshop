import pandas as pd
import cauldron as cd
from cauldron.steptest import StepTestCase


class TestNotebook(StepTestCase):
    """Testing my notebook"""

    def test_step_one(self):
        """Should run step one without error"""

        result = self.run_step('S01.py')
        self.assertTrue(result.success)

    def test_step_two(self):
        """Should run step two without error"""

        cd.shared.df = pd.DataFrame([
            {'a': 1, 'b': 1},
            {'a': 2, 'b': 2}
        ])

        result = self.run_step('S02-More-Detail.py')
        self.assertTrue(result.success)
