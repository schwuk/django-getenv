import os
import ast
import unittest

try:
    from django.core.exceptions import ImproperlyConfigured
except ImportError:
    # If they aren't using django, define our own error
    class ImproperlyConfigured(Exception): pass


def env(key, default=None, required=False):
    """
    Retrieves environment variables and returns Python natives. The (optional)
    default will be returned if the environment variable does not exist.
    """
    try:
        value = os.environ[key]
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return value
    except KeyError:
        if default or not required:
            return default
        raise ImproperlyConfigured("Missing required environment variable '%s'" % key)


class TestEnv(unittest.TestCase):
    """Tests for the env() function."""
    def test_missing_var_with_no_default(self):
        """
        If we specify a non-existent environment variable, but don't specify a
        default, we'll get None back.
        """
        self.assertIsNone(env("FRABJOUS"))

    def test_missing_var_with_default(self):
        """
        If we specify a non-existent environment variable with a default, we'll
        get that default back.
        """
        self.assertEqual(env("FRABJOUS", "day"), "day")

    def test_missing_required_var_with_no_default(self):
        """
        If we specify a non-existent environment variable that's required, we get an error
        """
        self.assertRaises(ImproperlyConfigured, env, "FRABJOUS", required=True)

    def test_missing_required_var_with_default(self):
        """
        If for whatever reason, we specify a non-existent environment variable that's required, but give it a
        default we'll get that default back.
        """
        self.assertEqual(env("FRABJOUS", "day", required=True), "day")

    def test_var(self):
        """
        If the environment variable is present, we'll get the value back.
        """
        value = "raven"
        os.environ["WRITING_DESK"] = value
        self.assertEqual(env("WRITING_DESK"), value)

    def test_var_with_default(self):
        """
        If the environment variable is present, we'll get the value back, even
        if we supply a default.
        """
        value = "raven"
        os.environ["WRITING_DESK"] = value
        self.assertEqual(env("WRITING_DESK", "rabbit"), value)

    def test_cast_to_int(self):
        """
        If the environment variable is a number, we'll get an int back.
        """
        os.environ["FRUMIOUS"] = "1"
        self.assertEqual(env("FRUMIOUS"), 1)

    def test_cast_to_bool(self):
        """
        If the environment variable is a True or False, we'll get a bool back.
        """
        os.environ["FRUMIOUS"] = "True"
        self.assertEqual(env("FRUMIOUS"), True)


if __name__ == "__main__":
    unittest.main()
