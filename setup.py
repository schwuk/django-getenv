from setuptools import setup

setup(
    name = "django-getenv",
    description = "Read settings from environment variables.",
    version = "1.2",
    author = "David Murphy",
    author_email = "dave@schwuk.com",
    url = "http://github.com/schwuk/django-getenv",
    py_modules = ['getenv'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ]
)
