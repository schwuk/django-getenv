#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ast

# We're intentionally not using django.core.exceptions.ImproperlyConfigured
# because it would be silently ignored by django at settings loading time.
class ImproperlyConfigured(Exception):
    pass


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
        raise ImproperlyConfigured(
            "Missing required environment variable '%s'" % key)
