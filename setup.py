# coding=utf-8

from setuptools import setup

# https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
setup(
    name='misc_filename_utils',
    version='0.0.1',
    description='TODO Add description',

    # ########################################################################
    #
    # README.rst is generated from README.md:
    #
    # $ pandoc --from=markdown --to=rst README.md -o README.rst
    #
    # ~ OR ~
    #
    # $ fab build
    # ########################################################################
    long_description=(open('README.rst').read()),

    url='https://github.com/illagrenan/misc-filename-utils',
    license='MIT',
    author='Vašek Dohnal',
    author_email='vaclav.dohnal@gmail.com',

    # The exclude makes sure that a top-level tests package doesn’t get
    # installed (it’s still part of the source distribution)
    # since that would wreak havoc.
    # find_packages(exclude=['tests*'])
    packages=['misc_filename_utils'],


    install_requires=['awesome-slugify'],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Console',
        'Intended Audience :: Developers'
    ],
)