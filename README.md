# Misc filename utils #

[![Travis CI Badge](https://api.travis-ci.org/illagrenan/misc-filename-utils.png)](https://travis-ci.org/illagrenan/misc-filename-utils)
&nbsp;
[![Coverage Status](https://coveralls.io/repos/illagrenan/misc-filename-utils/badge.svg)](https://coveralls.io/r/illagrenan/misc-filename-utils)
&nbsp;
[![Requirements Status](https://requires.io/github/illagrenan/misc-filename-utils/requirements.svg?branch=master)](https://requires.io/github/illagrenan/misc-filename-utils/requirements/?branch=master)


## Installation ##

**This package is not yet on PyPI.**

```bash
pip install --upgrade git+git://github.com/illagrenan/misc-filename-utils.git#egg=misc-filename-utils
```

## Usage ##

**get_safe_path_name**
```python
from misc_filename_utils.funcs import get_safe_path_name
>>> get_safe_path_name("\&FoO-bAr##.PDF")
u'foo-bar_.pdf'
```

**upload_path (generic usage)**
```python
from misc_filename_utils.funcs import upload_path

class Person(object):
	pass

>>> upload_path(Person, "IMAGE.pdf")
u'person\\image.pdf'

>>> upload_path(Person(), "IMAGE.pdf")
u'person\\image.pdf'
```

**upload_path (Django example)**
```python
from django.db import models
from misc_filename_utils.funcs import upload_path

class Person(models.Model):
	# Files will be uploaded to MEDIA_ROOT/person/some_file.ext
    image = models.FileField(upload_to=upload_path)
```

**get_filename_from_url**
```python
from misc_filename_utils.funcs import get_filename_from_url

>>> get_filename_from_url("http://www.example.com/some_directory/HOW_TO_FOO.pdf")
u'how_to_foo.pdf'
```
