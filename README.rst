dtxg - powerful extensions to dateutil
==========================================

|pypi| |support| |licence|

|gitter| |readthedocs|

|travis| |appveyor| |pipelines| |coverage|

.. |pypi| image:: https://img.shields.io/pypi/v/python-dateutil.svg?style=flat-square
    :target: https://pypi.org/project/python-dateutil/
    :alt: pypi version

.. |support| image:: https://img.shields.io/pypi/pyversions/python-dateutil.svg?style=flat-square
    :target: https://pypi.org/project/python-dateutil/
    :alt: supported Python version

.. |travis| image:: https://img.shields.io/travis/dateutil/dateutil/master.svg?style=flat-square&label=Travis%20Build
    :target: https://travis-ci.org/dateutil/dateutil
    :alt: travis build status

.. |appveyor| image:: https://img.shields.io/appveyor/ci/dateutil/dateutil/master.svg?style=flat-square&logo=appveyor
    :target: https://ci.appveyor.com/project/dateutil/dateutil
    :alt: appveyor build status

.. |pipelines| image:: https://dev.azure.com/pythondateutilazure/dateutil/_apis/build/status/dateutil.dateutil?branchName=master
    :target: https://dev.azure.com/pythondateutilazure/dateutil/_build/latest?definitionId=1&branchName=master
    :alt: azure pipelines build status

.. |coverage| image:: https://codecov.io/github/dateutil/dateutil/coverage.svg?branch=master
    :target: https://codecov.io/github/dateutil/dateutil?branch=master
    :alt: Code coverage

.. |gitter| image:: https://badges.gitter.im/dateutil/dateutil.svg
   :alt: Join the chat at https://gitter.im/dateutil/dateutil
   :target: https://gitter.im/dateutil/dateutil

.. |licence| image:: https://img.shields.io/pypi/l/python-dateutil.svg?style=flat-square
    :target: https://pypi.org/project/python-dateutil/
    :alt: licence

.. |readthedocs| image:: https://img.shields.io/readthedocs/dateutil/latest.svg?style=flat-square&label=Read%20the%20Docs
   :alt: Read the documentation at https://dateutil.readthedocs.io/en/latest/
   :target: https://dateutil.readthedocs.io/en/latest/

The `dtxg` module provides powerful extensions to
the standard `dateutil` module, available in Python.

Installation
============
`dtxg` can be installed from PyPI using `pip`::

	pip install dtxg

Download
========
dtxg is available on PyPI
https://pypi.org/project/dtxg/

Code
====
The code and issue tracker are hosted on Github:
https://github.com/yangsongbai1/dtxg/

Features
========

* Extensions to the dateutil module to support time resolution in multiple languages
* Utc time can be returned based on the time zone parameter

Quick example
=============
:

	from dtxg.parser import parse, UtcTime, country_tz

	a = parse(" Thứ ba, 18/6/2019 | 4:41:27 Chiều", language='西班牙语', tzinfo='UTC', country=None, fuzzy=True)
	print(a)


	# test2
	utctime = UtcTime(language='西班牙语', tzinfo=None, country='中国')
	a = utctime.parse(" Thứ ba, 18/6/2019 | 4:41:27 Chiều", fuzzy=True)
	print(a)


Contributing
============

We welcome many types of contributions - bug reports, pull requests (code, infrastructure or documentation fixes). For more information about how to contribute to the project, see the ``CONTRIBUTING.md`` file in the repository.
