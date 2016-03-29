# coding=utf-8
import io

from setuptools import setup

try:
    from pypandoc import convert


    def read_md(file_name):
        # http://stackoverflow.com/a/23265673/752142
        return convert(file_name, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")


    def read_md(file_name):
        try:
            return io.open(file_name, 'r', encoding='utf-8').read()
        except UnicodeDecodeError:
            return "Encoding problems with README.md"

# https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
setup(
    name='misc_filename_utils',
    version='0.0.1',
    description='TODO Add description',
    long_description=read_md('README.md'),
    url='https://github.com/illagrenan/misc-filename-utils',
    license='MIT',
    author='Vašek Dohnal',
    author_email='vaclav.dohnal@gmail.com',
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
