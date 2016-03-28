# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
from unittest import TestCase

from misc_filename_utils.funcs import upload_path


class DjangoUploadPathTestCase(TestCase):
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
