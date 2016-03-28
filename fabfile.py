# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

import sys

import six


if not six.PY2:
    print("Run Fabfile only under Python 2.x")
    sys.exit(0)

from fabric.context_managers import settings

from fabric.contrib.console import confirm
from fabric.decorators import task
from fabric.operations import local


@task()
def test_install():
    with settings(warn_only=True):
        local("pip uninstall misc-filename-utils --yes")
        print("Uninstall OK.")

    local("pip install --use-wheel --no-index --find-links dist misc-filename-utils")
    local("pip uninstall misc-filename-utils --yes")

    print("Install OK.")


@task()
def test():
    local("nosetests --with-coverage --cover-package=misc_filename_utils --cover-tests --cover-erase --with-doctest")

    print("Test OK.")


@task()
def build():
    local("pandoc --from=markdown --to=rst README.md -o _generated/README.rst")
    local("python setup.py sdist")
    local("python setup.py bdist_wheel")

    print("Build OK.")


@task()
def publish():
    if confirm(u'Really publish?', default=False):
        local('python setup.py sdist upload -r pypi')
        local('python setup.py bdist_wheel upload -r pypi')

        print("Published.")
