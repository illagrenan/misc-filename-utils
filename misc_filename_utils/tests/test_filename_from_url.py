# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

from unittest import TestCase

from misc_filename_utils.funcs import get_safe_path_name, get_filename_from_url


class SafePathTestCase(TestCase):
    def test_safe_path_name(self):
        test_data = [
            ("ABC.pdf", "abc.pdf"),
            ("čřž", "crz"),
            ("&&", ""),
            ("A-B-C.DOCx", "a-b-c.docx"),
        ]

        for unsafe_filename, expected in test_data:
            self.assertEqual(get_safe_path_name(unsafe_filename), expected)


class FilenameFromUrlTestCase(TestCase):
    def test_filename_from_url(self):
        test_data = [
            ("http://www.example.com/foo.pdf", "foo.pdf"),
            ("http://example.com/foo/bar/foo-bar.jpg?h600", "foo-bar.jpg"),
            ("fooBar.JPG", "fooBar.jpg"),
            ("\n\n\n\t\t\tfooBar.JPG     \n\t   ", "fooBar.jpg"),
        ]

        for url, expected_filename in test_data:
            self.assertEqual(get_filename_from_url(url), expected_filename)
