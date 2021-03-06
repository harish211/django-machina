# -*- coding: utf-8 -*-

# Standard library imports
# Third party imports
from django import VERSION as DJANGO_VERSION
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

# Local application / specific library imports

# PILImage
try:
    # Try from the Pillow (or one variant of PIL) install location first.
    from PIL import Image as PILImage
except ImportError as err:  # pragma: no cover
    try:
        # If that failed, try the alternate import syntax for PIL.
        import Image as PILImage  # noqa
    except ImportError as err:
        # Neither worked, so it's likely not installed.
        raise ImproperlyConfigured(
            _("Neither Pillow nor PIL could be imported: %s") % err
        )


# Django slugify
try:
    from django.utils.text import slugify
except ImportError:  # pragma: no cover
    from django.template.defaultfilters import slugify  # noqa


# force_bytes
try:
    from django.utils.encoding import force_bytes
except ImportError:  # pragma: no cover
    from django.utils.encoding import smart_str as force_bytes  # noqa


# get_cache
if DJANGO_VERSION >= (1, 7):
    from django.core.cache import caches

    def get_cache(key):
        return caches[key]
else:  # pragma: no cover
    from django.core.cache import get_cache  # noqa
