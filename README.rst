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
`dtxg` can be installed from PyPI using `pip`::

	from dtxg.parser import parse, UtcTime, country_tz
	
	# test2
	a = parse(" Thứ ba, 18/6/2019 | 4:41:27 Chiều", language='西班牙语', tzinfo='UTC', country=None, fuzzy=True)
	print(a)

	# test2
	utctime = UtcTime(language='西班牙语', country='中国')
	a = utctime.parse(" Thứ ba, 18/6/2019 | 4:41:27 Chiều", fuzzy=True)
	print(a)

	print(country_tz.country_tz)    		查看各国时区(即country_tz的有效参数)
	print(country_tz.country_language)      	查看各国语言(即language的有效参数)
	pytz.all_timezones 				查看所有地区时区，(即tzinfo的有效参数)

	lanauge 传入时间字符串的语言种类
	tzinfo  时区
	country 国家，用于tzinfo为空时获取时区信息
	fuzzy	模糊匹配
	返回utc时间
	没有解析到时间会抛出异常

	可识别 "2019-06-10T08:00:00-05:00"  "UTC", "GMT", "Z", "z" 
	优先识别字符串中的时区，其次识别tzinfo传入的时区，如果两者都没有，则以传入country的首都时区返回utc时间，
	如果都为空，则返回原时间


Contributing
============

We welcome many types of contributions - bug reports, pull requests (code, infrastructure or documentation fixes). For more information about how to contribute to the project, see the ``CONTRIBUTING.md`` file in the repository.
