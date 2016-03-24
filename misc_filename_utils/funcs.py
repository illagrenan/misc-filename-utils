# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

import inspect
import os

from slugify import Slugify

slugify_filename = Slugify()
slugify_filename.separator = '_'
slugify_filename.safe_chars = '-.'
slugify_filename.max_length = 255


def get_safe_path_name(filename):
    assert isinstance(filename, (str, unicode))

    safe_filename = slugify_filename(filename)

    return safe_filename.lower()


def get_filename_from_url(url):
    """
    Convert URL to filename.

    Example:

        URL `http://www.example.com/foo.pdf` will be converted to `foo.pdf`.

    :param url: URL pointing to file.
    :return: Filename.
    """
    raw_filename = url.split('/')[-1]
    raw_filename = get_safe_path_name(raw_filename)

    return raw_filename


def upload_path(instance, filename):
    if inspect.isclass(instance):
        base_dir = get_safe_path_name(instance.__name__)
    else:
        base_dir = get_safe_path_name(instance.__class__.__name__)

    target_filename = get_safe_path_name(os.path.basename(filename))

    return os.path.join(base_dir, target_filename)
