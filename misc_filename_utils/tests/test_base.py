# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
from unittest import TestCase

from future import standard_library

from misc_filename_utils.funcs import get_safe_path_name, get_filename_from_url, upload_path

standard_library.install_aliases()


class BaseTestCase(TestCase):
    def test_safe_path_name(self):
        test_data = [
            ("ABC.pdf", "abc.pdf"),
            ("čřž", "crz"),
            ("&&", ""),
            ("A-B-C.DOCx", "a-b-c.docx"),
        ]

        for unsafe_filename, expected in test_data:
            self.assertEqual(get_safe_path_name(unsafe_filename), expected)

    def test_filename_from_url(self):
        test_data = [
            ("http://www.example.com/foo.pdf", "foo.pdf"),
            ("http://example.com/foo/bar/foo-bar.jpg?h600", "foo-bar.jpg")
        ]

        for url, expected in test_data:
            self.assertEqual(get_filename_from_url(url), expected)

    def test_upload_path(self):
        class MockUserObject(object):
            pass

        test_data = [
            (MockUserObject(), "http://www.example.com/foo.pdf", os.path.normpath("mockuserobject/foo.pdf")),
            (MockUserObject, "http://www.example.com/foo.pdf", os.path.normpath("mockuserobject/foo.pdf")),
            (int, "abc.DOCX", os.path.normpath("int/abc.docx")),
        ]

        for obj, filename, expected in test_data:
            self.assertEqual(upload_path(obj, filename), expected)
