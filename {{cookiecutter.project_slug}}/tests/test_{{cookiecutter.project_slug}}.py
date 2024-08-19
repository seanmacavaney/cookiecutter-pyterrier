import unittest
import {{ cookiecutter.project_slug }}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""
    def test_something(self):
        """Test something."""
