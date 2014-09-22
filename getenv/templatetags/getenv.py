from django import template
from .. import env


register = template.Library()
@register.simple_tag(name="getenv")
def getenv(envvar):

    """ Return an environment variable for use in a template. """

    return env(envvar)

