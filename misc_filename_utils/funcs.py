# !/usr/bin/python
# coding=utf-8

from __future__ import (absolute_import, division, print_function, unicode_literals)

import inspect
import os
import os.path

try:
    # Python 3.x
    from urllib.parse import urlsplit
except ImportError:
    # Python 2.x
    from urlparse import urlsplit

from slugify import Slugify

slugify_filename = Slugify(to_lower=True)
slugify_filename.separator = '_'
slugify_filename.safe_chars = '-.'
slugify_filename.max_length = 255


def get_safe_path_name(filename):
    """
    :type filename: unicode
    :rtype: unicode
    """
    safe_filename = slugify_filename(filename)

    return safe_filename.lower()


def get_filename_from_url(url):
    """
    Convert URL to filename.

    Example:

        URL `http://www.example.com/foo.pdf` will be converted to `foo.pdf`.

    :type url: unicode
    :rtype: unicode
    """

    name, extension = os.path.splitext(os.path.basename(urlsplit(url).path))
    fin = "{filename}{extension_with_dot}".format(filename=name.strip(), extension_with_dot=extension.strip().lower())

    return fin


def upload_path(instance, filename):
    """
    Get upload path for Django model.

    :type instance: object
    :type filename: unicode
    :rtype: unicode
    """
    if inspect.isclass(instance):
        base_dir = get_safe_path_name(instance.__name__)
    else:
        base_dir = get_safe_path_name(instance.__class__.__name__)

    target_filename = get_safe_path_name(os.path.basename(filename))

    return os.path.join(base_dir, target_filename)
