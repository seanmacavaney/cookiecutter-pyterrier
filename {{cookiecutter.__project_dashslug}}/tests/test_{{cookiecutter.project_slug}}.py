import unittest
import pandas as pd

from {{ cookiecutter.project_slug }} import MyAwesomeTransformer


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    def test_something(self):
        # Arrange
        transformer = MyAwesomeTransformer()
        inp = pd.DataFrame()

        # Act
        res = transformer(inp)

        # Assert
        pd.testing.assert_frame_equal(inp, res)
