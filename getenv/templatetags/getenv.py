from django import template
from .. import env


register = template.Library()
@register.simple_tag(name="getenv")
def getenv(envvar, default=''):

    """ Return an environment variable for use in a template. """
    """ If environment variable doesn't exist return a default value """

    return env(envvar) or default

