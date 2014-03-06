#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_getenv
----------------------------------

Tests for `getenv` module.
"""

import unittest
import os

from getenv import env, ImproperlyConfigured


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
        If we specify a non-existent environment variable that's required, we
        get an error
        """
        self.assertRaises(ImproperlyConfigured, env, "FRABJOUS", required=True)

    def test_missing_required_var_with_default(self):
        """
        If for whatever reason, we specify a non-existent environment variable
        that's required, but give it a default we'll get that default back.
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


if __name__ == '__main__':
    unittest.main()
