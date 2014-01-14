django-getenv
=============

.. image:: https://travis-ci.org/schwuk/django-getenv.png?branch=master
    :target: https://travis-ci.org/schwuk/django-getenv

.. image:: https://pypip.in/v/django-getenv/badge.png
    :target: https://pypi.python.org/pypi/django-getenv/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/django-getenv/badge.png
    :target: https://crate.io/packages/django-getenv/
    :alt: Number of PyPI downloads

If you're using
`django-dotenv <https://github.com/jacobian/django-dotenv>`__ to get the
most out of your ``.env`` file, you want to use the values there in your
`Django <https://www.djangoproject.com/>`__ project's settings.

It will convert boolean, integer and float values to their native Python
types.

There's nothing here that is Django specific, but I'm using it with
Django so that's what I've called it.

Installation
------------

::

    pip install django-getenv

Usage
-----

In your ``settings.py`` file (or equivalent), add:

::

    from getenv import env

Then to read in your environment variables, do this:

::

    SECRET_KEY = env("SECRET_KEY")

If you want to provide a default (in case the environment variable isn't
set), try:

::

    SECRET_KEY = env("SECRET_KEY", "a_secret_key")

For best results, mix with
`django-dotenv <https://github.com/jacobian/django-dotenv>`__ and
`dj-database-url <https://github.com/kennethreitz/dj-database-url>`__.
