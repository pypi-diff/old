# Comparing `tmp/aioambient-2022.10.0.tar.gz` & `tmp/aioambient-2023.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aioambient-2022.10.0.tar", max compression
+gzip compressed data, was "aioambient-2023.4.0.tar", max compression
```

## Comparing `aioambient-2022.10.0.tar` & `aioambient-2023.4.0.tar`

### file list

```diff
@@ -1,12 +1,11 @@
--rw-r--r--   0        0        0     1072 2022-10-29 18:45:50.597561 aioambient-2022.10.0/LICENSE
--rw-r--r--   0        0        0     6969 2022-10-29 18:45:50.597561 aioambient-2022.10.0/README.md
--rw-r--r--   0        0        0       99 2022-10-29 18:45:50.597561 aioambient-2022.10.0/aioambient/__init__.py
--rw-r--r--   0        0        0     3851 2022-10-29 18:45:50.597561 aioambient-2022.10.0/aioambient/api.py
--rw-r--r--   0        0        0      113 2022-10-29 18:45:50.597561 aioambient-2022.10.0/aioambient/const.py
--rw-r--r--   0        0        0      315 2022-10-29 18:45:50.597561 aioambient-2022.10.0/aioambient/errors.py
--rw-r--r--   0        0        0        0 2022-10-29 18:45:50.597561 aioambient-2022.10.0/aioambient/py.typed
--rw-r--r--   0        0        0      464 2022-10-29 18:45:50.597561 aioambient-2022.10.0/aioambient/util/__init__.py
--rw-r--r--   0        0        0     7871 2022-10-29 18:45:50.597561 aioambient-2022.10.0/aioambient/websocket.py
--rw-r--r--   0        0        0     3780 2022-10-29 18:45:50.597561 aioambient-2022.10.0/pyproject.toml
--rw-r--r--   0        0        0     7971 1970-01-01 00:00:00.000000 aioambient-2022.10.0/setup.py
--rw-r--r--   0        0        0     8288 1970-01-01 00:00:00.000000 aioambient-2022.10.0/PKG-INFO
+-rw-r--r--   0        0        0     1072 2023-04-07 02:29:33.896863 aioambient-2023.4.0/LICENSE
+-rw-r--r--   0        0        0     7744 2023-04-07 02:29:33.896863 aioambient-2023.4.0/README.md
+-rw-r--r--   0        0        0       99 2023-04-07 02:29:33.896863 aioambient-2023.4.0/aioambient/__init__.py
+-rw-r--r--   0        0        0     3851 2023-04-07 02:29:33.896863 aioambient-2023.4.0/aioambient/api.py
+-rw-r--r--   0        0        0      113 2023-04-07 02:29:33.896863 aioambient-2023.4.0/aioambient/const.py
+-rw-r--r--   0        0        0      315 2023-04-07 02:29:33.896863 aioambient-2023.4.0/aioambient/errors.py
+-rw-r--r--   0        0        0        0 2023-04-07 02:29:33.896863 aioambient-2023.4.0/aioambient/py.typed
+-rw-r--r--   0        0        0      464 2023-04-07 02:29:33.896863 aioambient-2023.4.0/aioambient/util/__init__.py
+-rw-r--r--   0        0        0     7871 2023-04-07 02:29:33.896863 aioambient-2023.4.0/aioambient/websocket.py
+-rw-r--r--   0        0        0     3574 2023-04-07 02:29:33.896863 aioambient-2023.4.0/pyproject.toml
+-rw-r--r--   0        0        0     9059 1970-01-01 00:00:00.000000 aioambient-2023.4.0/PKG-INFO
```

### Comparing `aioambient-2022.10.0/LICENSE` & `aioambient-2023.4.0/LICENSE`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 MIT License
 
-Copyright (c) 2017-2022 Aaron Bach
+Copyright (c) 2017-2023 Aaron Bach
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
```

### Comparing `aioambient-2022.10.0/README.md` & `aioambient-2023.4.0/README.md`

 * *Files 9% similar despite different names*

```diff
@@ -1,22 +1,26 @@
 # 🌤 aioambient: An async library for Ambient Weather Personal Weather Stations
 
-[![CI](https://github.com/bachya/aioambient/workflows/CI/badge.svg)](https://github.com/bachya/aioambient/actions)
-[![PyPi](https://img.shields.io/pypi/v/aioambient.svg)](https://pypi.python.org/pypi/aioambient)
-[![Version](https://img.shields.io/pypi/pyversions/aioambient.svg)](https://pypi.python.org/pypi/aioambient)
-[![License](https://img.shields.io/pypi/l/aioambient.svg)](https://github.com/bachya/aioambient/blob/main/LICENSE)
-[![Code Coverage](https://codecov.io/gh/bachya/aioambient/branch/dev/graph/badge.svg)](https://codecov.io/gh/bachya/aioambient)
-[![Maintainability](https://api.codeclimate.com/v1/badges/81a9f8274abf325b2fa4/maintainability)](https://codeclimate.com/github/bachya/aioambient/maintainability)
-[![Say Thanks](https://img.shields.io/badge/SayThanks-!-1EAEDB.svg)](https://saythanks.io/to/bachya)
+[![CI][ci-badge]][ci]
+[![PyPI][pypi-badge]][pypi]
+[![Version][version-badge]][version]
+[![License][license-badge]][license]
+[![Code Coverage][codecov-badge]][codecov]
+[![Maintainability][maintainability-badge]][maintainability]
 
 <a href="https://www.buymeacoffee.com/bachya1208P" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
 
-`aioambient` is a Python3, asyncio-driven library that interfaces with both the
-REST and Websocket APIs provided by
-[Ambient Weather](https://ambientweather.net).
+`aioambient` is a Python3, asyncio-driven library that interfaces with both the REST and
+Websocket APIs provided by [Ambient Weather][ambient-weather].
+
+- [Installation](#installation)
+- [Python Versions](#python-versions)
+- [API and Application Keys](#api-and-application-keys)
+- [Usage](#usage)
+- [Contributing](#contributing)
 
 # Installation
 
 ```bash
 pip install aioambient
 ```
 
@@ -26,17 +30,17 @@
 
 - Python 3.9
 - Python 3.10
 - Python 3.11
 
 # API and Application Keys
 
-Utilizing `aioambient` requires both an Application Key and an API Key from
-Ambient Weather. You can generate both from the Profile page in your
-[Ambient Weather Dashboard](https://dashboard.ambientweather.net).
+Utilizing `aioambient` requires both an Application Key and an API Key from Ambient
+Weather. You can generate both from the Profile page in your
+[Ambient Weather Dashboard][ambient-weather-dashboard].
 
 # Usage
 
 ## REST API
 
 ```python
 import asyncio
@@ -62,17 +66,16 @@
 
 
 asyncio.run(main())
 ```
 
 By default, the library creates a new connection to Ambient Weather with each coroutine.
 If you are calling a large number of coroutines (or merely want to squeeze out every
-second of runtime savings possible), an
-[`aiohttp`](https://github.com/aio-libs/aiohttp) `ClientSession` can be used for connection
-pooling:
+second of runtime savings possible), an [`aiohttp`][aiohttp] `ClientSession` can be used for
+connection pooling:
 
 ```python
 import asyncio
 from datetime import date
 
 from aiohttp import ClientSession
 
@@ -94,15 +97,15 @@
         await api.get_device_details("<DEVICE MAC ADDRESS>", end_date=date(2019, 1, 16))
 
 
 asyncio.run(main())
 ```
 
 Please be aware of Ambient Weather's
-[rate limiting policies](https://ambientweather.docs.apiary.io/#introduction/rate-limiting).
+[rate limiting policies][ambient-weather-rate-limiting].
 
 ## Websocket API
 
 ```python
 import asyncio
 
 from aiohttp import ClientSession
@@ -188,19 +191,41 @@
 
 
 asyncio.run(main())
 ```
 
 # Contributing
 
-1. [Check for open features/bugs](https://github.com/bachya/aioambient/issues)
-   or [initiate a discussion on one](https://github.com/bachya/aioambient/issues/new).
-2. [Fork the repository](https://github.com/bachya/aioambient/fork).
+Thanks to all of [our contributors][contributors] so far!
+
+1. [Check for open features/bugs][issues] or [initiate a discussion on one][new-issue].
+2. [Fork the repository][fork].
 3. (_optional, but highly recommended_) Create a virtual environment: `python3 -m venv .venv`
-4. (_optional, but highly recommended_) Enter the virtual environment: `source ./venv/bin/activate`
+4. (_optional, but highly recommended_) Enter the virtual environment: `source ./.venv/bin/activate`
 5. Install the dev environment: `script/setup`
-6. Code your new feature or bug fix.
+6. Code your new feature or bug fix on a new branch.
 7. Write tests that cover your new functionality.
 8. Run tests and ensure 100% code coverage: `poetry run pytest --cov aioambient tests`
 9. Update `README.md` with any new documentation.
-10. Add yourself to `AUTHORS.md`.
-11. Submit a pull request!
+10. Submit a pull request!
+
+[aiohttp]: https://github.com/aio-libs/aiohttp
+[ambient-weather-dashboard]: https://dashboard.ambientweather.net
+[ambient-weather-rate-limiting]: https://ambientweather.docs.apiary.io/#introduction/rate-limiting
+[ambient-weather]: https://ambientweather.net
+[ci-badge]: https://github.com/bachya/aioambient/workflows/CI/badge.svg
+[ci]: https://github.com/bachya/aioambient/actions
+[codecov-badge]: https://codecov.io/gh/bachya/aioambient/branch/dev/graph/badge.svg
+[codecov]: https://codecov.io/gh/bachya/aioambient
+[contributors]: https://github.com/bachya/aioambient/graphs/contributors
+[fork]: https://github.com/bachya/aioambient/fork
+[issues]: https://github.com/bachya/aioambient/issues
+[license-badge]: https://img.shields.io/pypi/l/aioambient.svg
+[license]: https://github.com/bachya/aioambient/blob/main/LICENSE
+[maintainability-badge]: https://api.codeclimate.com/v1/badges/81a9f8274abf325b2fa4/maintainability
+[maintainability]: https://codeclimate.com/github/bachya/aioambient/maintainability
+[new-issue]: https://github.com/bachya/aioambient/issues/new
+[new-issue]: https://github.com/bachya/aioambient/issues/new
+[pypi-badge]: https://img.shields.io/pypi/v/aioambient.svg
+[pypi]: https://pypi.python.org/pypi/aioambient
+[version-badge]: https://img.shields.io/pypi/pyversions/aioambient.svg
+[version]: https://pypi.python.org/pypi/aioambient
```

### Comparing `aioambient-2022.10.0/aioambient/api.py` & `aioambient-2023.4.0/aioambient/api.py`

 * *Files identical despite different names*

### Comparing `aioambient-2022.10.0/aioambient/websocket.py` & `aioambient-2023.4.0/aioambient/websocket.py`

 * *Files identical despite different names*

### Comparing `aioambient-2022.10.0/pyproject.toml` & `aioambient-2023.4.0/pyproject.toml`

 * *Files 7% similar despite different names*

```diff
@@ -37,15 +37,15 @@
 warn_return_any = true
 warn_unreachable = true
 warn_unused_configs = true
 warn_unused_ignores = true
 
 [tool.poetry]
 name = "aioambient"
-version = "2022.10.0"
+version = "2023.04.0"
 description = "A clean, async-friendly library for the Ambient Weather API"
 readme = "README.md"
 authors = ["Aaron Bach <bachya1208@gmail.com>"]
 license = "MIT"
 repository = "https://github.com/bachya/aioambient"
 classifiers = [
     "License :: OSI Approved :: MIT License",
@@ -59,44 +59,36 @@
 ]
 
 [tool.poetry.dependencies]
 aiohttp = ">=3.8.0"
 python = "^3.9.0"
 python-engineio = ">=3.13.1,<5.0.0"
 python-socketio = ">=4.6,<6.0"
-websockets = ">=9.1,<11.0"
+websockets = ">=11.0.1"
 
 [tool.poetry.group.dev.dependencies]
 aresponses = "^2.1.6"
 asynctest = "^0.13.0"
 bandit = "^1.7.4"
-black = "^22.10.0"
+black = ">=22.10,<24.0"
 blacken-docs = "^1.12.1"
 codespell = "^2.2.2"
-coverage = {version = "^6.5", extras = ["toml"]}
+coverage = {version = ">=6.5,<8.0", extras = ["toml"]}
 darglint = "^1.8.1"
-flake8 = "^4.0.1"
-flake8-bandit = "^3.0.0"
-flake8-bugbear = "^22.10.27"
-flake8-builtins = "^2.0.0"
-flake8-comprehensions = "^3.10.0"
-flake8-docstrings = "^1.5.0"
-flake8-eradicate = "^1.4.0"
-flake8-markdown = "^0.3.0"
-flake8-simplify = "^0.19.3"
 isort = "^5.10.1"
-mypy = "^0.982"
-pre-commit = "^2.20.0"
+mypy = "^1.2.0"
+pre-commit = ">=2.20,<4.0"
 pre-commit-hooks = "^4.3.0"
 pylint = "^2.15.5"
 pytest = "^7.2.0"
 pytest-aiohttp = "^1.0.0"
-pytest-asyncio = "^0.20.1"
+pytest-asyncio = ">=0.20.1,<0.22.0"
 pytest-cov = "^4.0.0"
 pyupgrade = "^3.1.0"
+ruff = "^0.0.261"
 safety = "^2.3.1"
 vulture = "^2.6"
 yamllint = "^1.28.0"
 
 [tool.poetry.urls]
 "Bug Tracker" = "https://github.com/bachya/aioambient/issues"
 Changelog = "https://github.com/bachya/aioambient/releases"
```

### Comparing `aioambient-2022.10.0/setup.py` & `aioambient-2023.4.0/PKG-INFO`

 * *Files 21% similar despite different names*

```diff
@@ -1,499 +1,567 @@
-00000000: 2320 2d2a 2d20 636f 6469 6e67 3a20 7574  # -*- coding: ut
-00000010: 662d 3820 2d2a 2d0a 6672 6f6d 2073 6574  f-8 -*-.from set
-00000020: 7570 746f 6f6c 7320 696d 706f 7274 2073  uptools import s
-00000030: 6574 7570 0a0a 7061 636b 6167 6573 203d  etup..packages =
-00000040: 205c 0a5b 2761 696f 616d 6269 656e 7427   \.['aioambient'
-00000050: 2c20 2761 696f 616d 6269 656e 742e 7574  , 'aioambient.ut
-00000060: 696c 275d 0a0a 7061 636b 6167 655f 6461  il']..package_da
-00000070: 7461 203d 205c 0a7b 2727 3a20 5b27 2a27  ta = \.{'': ['*'
-00000080: 5d7d 0a0a 696e 7374 616c 6c5f 7265 7175  ]}..install_requ
-00000090: 6972 6573 203d 205c 0a5b 2761 696f 6874  ires = \.['aioht
-000000a0: 7470 3e3d 332e 382e 3027 2c0a 2027 7079  tp>=3.8.0',. 'py
-000000b0: 7468 6f6e 2d65 6e67 696e 6569 6f3e 3d33  thon-engineio>=3
-000000c0: 2e31 332e 312c 3c35 2e30 2e30 272c 0a20  .13.1,<5.0.0',. 
-000000d0: 2770 7974 686f 6e2d 736f 636b 6574 696f  'python-socketio
-000000e0: 3e3d 342e 362c 3c36 2e30 272c 0a20 2777  >=4.6,<6.0',. 'w
-000000f0: 6562 736f 636b 6574 733e 3d39 2e31 2c3c  ebsockets>=9.1,<
-00000100: 3131 2e30 275d 0a0a 7365 7475 705f 6b77  11.0']..setup_kw
-00000110: 6172 6773 203d 207b 0a20 2020 2027 6e61  args = {.    'na
-00000120: 6d65 273a 2027 6169 6f61 6d62 6965 6e74  me': 'aioambient
-00000130: 272c 0a20 2020 2027 7665 7273 696f 6e27  ',.    'version'
-00000140: 3a20 2732 3032 322e 3130 2e30 272c 0a20  : '2022.10.0',. 
-00000150: 2020 2027 6465 7363 7269 7074 696f 6e27     'description'
-00000160: 3a20 2741 2063 6c65 616e 2c20 6173 796e  : 'A clean, asyn
-00000170: 632d 6672 6965 6e64 6c79 206c 6962 7261  c-friendly libra
-00000180: 7279 2066 6f72 2074 6865 2041 6d62 6965  ry for the Ambie
-00000190: 6e74 2057 6561 7468 6572 2041 5049 272c  nt Weather API',
-000001a0: 0a20 2020 2027 6c6f 6e67 5f64 6573 6372  .    'long_descr
-000001b0: 6970 7469 6f6e 273a 2027 2320 f09f 8ca4  iption': '# ....
-000001c0: 2061 696f 616d 6269 656e 743a 2041 6e20   aioambient: An 
-000001d0: 6173 796e 6320 6c69 6272 6172 7920 666f  async library fo
-000001e0: 7220 416d 6269 656e 7420 5765 6174 6865  r Ambient Weathe
-000001f0: 7220 5065 7273 6f6e 616c 2057 6561 7468  r Personal Weath
-00000200: 6572 2053 7461 7469 6f6e 735c 6e5c 6e5b  er Stations\n\n[
-00000210: 215b 4349 5d28 6874 7470 733a 2f2f 6769  ![CI](https://gi
-00000220: 7468 7562 2e63 6f6d 2f62 6163 6879 612f  thub.com/bachya/
-00000230: 6169 6f61 6d62 6965 6e74 2f77 6f72 6b66  aioambient/workf
-00000240: 6c6f 7773 2f43 492f 6261 6467 652e 7376  lows/CI/badge.sv
-00000250: 6729 5d28 6874 7470 733a 2f2f 6769 7468  g)](https://gith
-00000260: 7562 2e63 6f6d 2f62 6163 6879 612f 6169  ub.com/bachya/ai
-00000270: 6f61 6d62 6965 6e74 2f61 6374 696f 6e73  oambient/actions
-00000280: 295c 6e5b 215b 5079 5069 5d28 6874 7470  )\n[![PyPi](http
-00000290: 733a 2f2f 696d 672e 7368 6965 6c64 732e  s://img.shields.
-000002a0: 696f 2f70 7970 692f 762f 6169 6f61 6d62  io/pypi/v/aioamb
-000002b0: 6965 6e74 2e73 7667 295d 2868 7474 7073  ient.svg)](https
-000002c0: 3a2f 2f70 7970 692e 7079 7468 6f6e 2e6f  ://pypi.python.o
-000002d0: 7267 2f70 7970 692f 6169 6f61 6d62 6965  rg/pypi/aioambie
-000002e0: 6e74 295c 6e5b 215b 5665 7273 696f 6e5d  nt)\n[![Version]
-000002f0: 2868 7474 7073 3a2f 2f69 6d67 2e73 6869  (https://img.shi
-00000300: 656c 6473 2e69 6f2f 7079 7069 2f70 7976  elds.io/pypi/pyv
-00000310: 6572 7369 6f6e 732f 6169 6f61 6d62 6965  ersions/aioambie
-00000320: 6e74 2e73 7667 295d 2868 7474 7073 3a2f  nt.svg)](https:/
-00000330: 2f70 7970 692e 7079 7468 6f6e 2e6f 7267  /pypi.python.org
-00000340: 2f70 7970 692f 6169 6f61 6d62 6965 6e74  /pypi/aioambient
-00000350: 295c 6e5b 215b 4c69 6365 6e73 655d 2868  )\n[![License](h
-00000360: 7474 7073 3a2f 2f69 6d67 2e73 6869 656c  ttps://img.shiel
-00000370: 6473 2e69 6f2f 7079 7069 2f6c 2f61 696f  ds.io/pypi/l/aio
-00000380: 616d 6269 656e 742e 7376 6729 5d28 6874  ambient.svg)](ht
-00000390: 7470 733a 2f2f 6769 7468 7562 2e63 6f6d  tps://github.com
-000003a0: 2f62 6163 6879 612f 6169 6f61 6d62 6965  /bachya/aioambie
-000003b0: 6e74 2f62 6c6f 622f 6d61 696e 2f4c 4943  nt/blob/main/LIC
-000003c0: 454e 5345 295c 6e5b 215b 436f 6465 2043  ENSE)\n[![Code C
-000003d0: 6f76 6572 6167 655d 2868 7474 7073 3a2f  overage](https:/
-000003e0: 2f63 6f64 6563 6f76 2e69 6f2f 6768 2f62  /codecov.io/gh/b
-000003f0: 6163 6879 612f 6169 6f61 6d62 6965 6e74  achya/aioambient
-00000400: 2f62 7261 6e63 682f 6465 762f 6772 6170  /branch/dev/grap
-00000410: 682f 6261 6467 652e 7376 6729 5d28 6874  h/badge.svg)](ht
-00000420: 7470 733a 2f2f 636f 6465 636f 762e 696f  tps://codecov.io
-00000430: 2f67 682f 6261 6368 7961 2f61 696f 616d  /gh/bachya/aioam
-00000440: 6269 656e 7429 5c6e 5b21 5b4d 6169 6e74  bient)\n[![Maint
-00000450: 6169 6e61 6269 6c69 7479 5d28 6874 7470  ainability](http
-00000460: 733a 2f2f 6170 692e 636f 6465 636c 696d  s://api.codeclim
-00000470: 6174 652e 636f 6d2f 7631 2f62 6164 6765  ate.com/v1/badge
-00000480: 732f 3831 6139 6638 3237 3461 6266 3332  s/81a9f8274abf32
-00000490: 3562 3266 6134 2f6d 6169 6e74 6169 6e61  5b2fa4/maintaina
-000004a0: 6269 6c69 7479 295d 2868 7474 7073 3a2f  bility)](https:/
-000004b0: 2f63 6f64 6563 6c69 6d61 7465 2e63 6f6d  /codeclimate.com
-000004c0: 2f67 6974 6875 622f 6261 6368 7961 2f61  /github/bachya/a
-000004d0: 696f 616d 6269 656e 742f 6d61 696e 7461  ioambient/mainta
-000004e0: 696e 6162 696c 6974 7929 5c6e 5b21 5b53  inability)\n[![S
-000004f0: 6179 2054 6861 6e6b 735d 2868 7474 7073  ay Thanks](https
-00000500: 3a2f 2f69 6d67 2e73 6869 656c 6473 2e69  ://img.shields.i
-00000510: 6f2f 6261 6467 652f 5361 7954 6861 6e6b  o/badge/SayThank
-00000520: 732d 212d 3145 4145 4442 2e73 7667 295d  s-!-1EAEDB.svg)]
-00000530: 2868 7474 7073 3a2f 2f73 6179 7468 616e  (https://saythan
-00000540: 6b73 2e69 6f2f 746f 2f62 6163 6879 6129  ks.io/to/bachya)
-00000550: 5c6e 5c6e 3c61 2068 7265 663d 2268 7474  \n\n<a href="htt
-00000560: 7073 3a2f 2f77 7777 2e62 7579 6d65 6163  ps://www.buymeac
-00000570: 6f66 6665 652e 636f 6d2f 6261 6368 7961  offee.com/bachya
-00000580: 3132 3038 5022 2074 6172 6765 743d 225f  1208P" target="_
-00000590: 626c 616e 6b22 3e3c 696d 6720 7372 633d  blank"><img src=
-000005a0: 2268 7474 7073 3a2f 2f63 646e 2e62 7579  "https://cdn.buy
-000005b0: 6d65 6163 6f66 6665 652e 636f 6d2f 6275  meacoffee.com/bu
-000005c0: 7474 6f6e 732f 6465 6661 756c 742d 6f72  ttons/default-or
-000005d0: 616e 6765 2e70 6e67 2220 616c 743d 2242  ange.png" alt="B
-000005e0: 7579 204d 6520 4120 436f 6666 6565 2220  uy Me A Coffee" 
-000005f0: 6865 6967 6874 3d22 3431 2220 7769 6474  height="41" widt
-00000600: 683d 2231 3734 223e 3c2f 613e 5c6e 5c6e  h="174"></a>\n\n
-00000610: 6061 696f 616d 6269 656e 7460 2069 7320  `aioambient` is 
-00000620: 6120 5079 7468 6f6e 332c 2061 7379 6e63  a Python3, async
-00000630: 696f 2d64 7269 7665 6e20 6c69 6272 6172  io-driven librar
-00000640: 7920 7468 6174 2069 6e74 6572 6661 6365  y that interface
-00000650: 7320 7769 7468 2062 6f74 6820 7468 655c  s with both the\
-00000660: 6e52 4553 5420 616e 6420 5765 6273 6f63  nREST and Websoc
-00000670: 6b65 7420 4150 4973 2070 726f 7669 6465  ket APIs provide
-00000680: 6420 6279 5c6e 5b41 6d62 6965 6e74 2057  d by\n[Ambient W
-00000690: 6561 7468 6572 5d28 6874 7470 733a 2f2f  eather](https://
-000006a0: 616d 6269 656e 7477 6561 7468 6572 2e6e  ambientweather.n
-000006b0: 6574 292e 5c6e 5c6e 2320 496e 7374 616c  et).\n\n# Instal
-000006c0: 6c61 7469 6f6e 5c6e 5c6e 6060 6062 6173  lation\n\n```bas
-000006d0: 685c 6e70 6970 2069 6e73 7461 6c6c 2061  h\npip install a
-000006e0: 696f 616d 6269 656e 745c 6e60 6060 5c6e  ioambient\n```\n
-000006f0: 5c6e 2320 5079 7468 6f6e 2056 6572 7369  \n# Python Versi
-00000700: 6f6e 735c 6e5c 6e60 6169 6f61 6d62 6965  ons\n\n`aioambie
-00000710: 6e74 6020 6973 2063 7572 7265 6e74 6c79  nt` is currently
-00000720: 2073 7570 706f 7274 6564 206f 6e3a 5c6e   supported on:\n
-00000730: 5c6e 2d20 5079 7468 6f6e 2033 2e39 5c6e  \n- Python 3.9\n
-00000740: 2d20 5079 7468 6f6e 2033 2e31 305c 6e2d  - Python 3.10\n-
-00000750: 2050 7974 686f 6e20 332e 3131 5c6e 5c6e   Python 3.11\n\n
-00000760: 2320 4150 4920 616e 6420 4170 706c 6963  # API and Applic
-00000770: 6174 696f 6e20 4b65 7973 5c6e 5c6e 5574  ation Keys\n\nUt
-00000780: 696c 697a 696e 6720 6061 696f 616d 6269  ilizing `aioambi
-00000790: 656e 7460 2072 6571 7569 7265 7320 626f  ent` requires bo
-000007a0: 7468 2061 6e20 4170 706c 6963 6174 696f  th an Applicatio
-000007b0: 6e20 4b65 7920 616e 6420 616e 2041 5049  n Key and an API
-000007c0: 204b 6579 2066 726f 6d5c 6e41 6d62 6965   Key from\nAmbie
-000007d0: 6e74 2057 6561 7468 6572 2e20 596f 7520  nt Weather. You 
-000007e0: 6361 6e20 6765 6e65 7261 7465 2062 6f74  can generate bot
-000007f0: 6820 6672 6f6d 2074 6865 2050 726f 6669  h from the Profi
-00000800: 6c65 2070 6167 6520 696e 2079 6f75 725c  le page in your\
-00000810: 6e5b 416d 6269 656e 7420 5765 6174 6865  n[Ambient Weathe
-00000820: 7220 4461 7368 626f 6172 645d 2868 7474  r Dashboard](htt
-00000830: 7073 3a2f 2f64 6173 6862 6f61 7264 2e61  ps://dashboard.a
-00000840: 6d62 6965 6e74 7765 6174 6865 722e 6e65  mbientweather.ne
-00000850: 7429 2e5c 6e5c 6e23 2055 7361 6765 5c6e  t).\n\n# Usage\n
-00000860: 5c6e 2323 2052 4553 5420 4150 495c 6e5c  \n## REST API\n\
-00000870: 6e60 6060 7079 7468 6f6e 5c6e 696d 706f  n```python\nimpo
-00000880: 7274 2061 7379 6e63 696f 5c6e 6672 6f6d  rt asyncio\nfrom
-00000890: 2064 6174 6574 696d 6520 696d 706f 7274   datetime import
-000008a0: 2064 6174 655c 6e5c 6e66 726f 6d20 6169   date\n\nfrom ai
-000008b0: 6f68 7474 7020 696d 706f 7274 2043 6c69  ohttp import Cli
-000008c0: 656e 7453 6573 7369 6f6e 5c6e 5c6e 6672  entSession\n\nfr
-000008d0: 6f6d 2061 696f 616d 6269 656e 7420 696d  om aioambient im
-000008e0: 706f 7274 2041 5049 5c6e 5c6e 5c6e 6173  port API\n\n\nas
-000008f0: 796e 6320 6465 6620 6d61 696e 2829 202d  ync def main() -
-00000900: 3e20 4e6f 6e65 3a5c 6e20 2020 2022 2222  > None:\n    """
-00000910: 4372 6561 7465 2074 6865 2061 696f 6874  Create the aioht
-00000920: 7470 2073 6573 7369 6f6e 2061 6e64 2072  tp session and r
-00000930: 756e 2074 6865 2065 7861 6d70 6c65 2e22  un the example."
-00000940: 2222 5c6e 2020 2020 6170 6920 3d20 4150  ""\n    api = AP
-00000950: 4928 223c 594f 5552 2041 5050 4c49 4341  I("<YOUR APPLICA
-00000960: 5449 4f4e 204b 4559 3e22 2c20 223c 594f  TION KEY>", "<YO
-00000970: 5552 2041 5049 204b 4559 3e22 295c 6e5c  UR API KEY>")\n\
-00000980: 6e20 2020 2023 2047 6574 2061 6c6c 2064  n    # Get all d
-00000990: 6576 6963 6573 2069 6e20 616e 2061 6363  evices in an acc
-000009a0: 6f75 6e74 3a5c 6e20 2020 2061 7761 6974  ount:\n    await
-000009b0: 2061 7069 2e67 6574 5f64 6576 6963 6573   api.get_devices
-000009c0: 2829 5c6e 5c6e 2020 2020 2320 4765 7420  ()\n\n    # Get 
-000009d0: 616c 6c20 7374 6f72 6564 2072 6561 6469  all stored readi
-000009e0: 6e67 7320 6672 6f6d 2061 2064 6576 6963  ngs from a devic
-000009f0: 653a 5c6e 2020 2020 6177 6169 7420 6170  e:\n    await ap
-00000a00: 692e 6765 745f 6465 7669 6365 5f64 6574  i.get_device_det
-00000a10: 6169 6c73 2822 3c44 4556 4943 4520 4d41  ails("<DEVICE MA
-00000a20: 4320 4144 4452 4553 533e 2229 5c6e 5c6e  C ADDRESS>")\n\n
-00000a30: 2020 2020 2320 4765 7420 616c 6c20 7374      # Get all st
-00000a40: 6f72 6564 2072 6561 6469 6e67 7320 6672  ored readings fr
-00000a50: 6f6d 2061 2064 6576 6963 6520 2873 7461  om a device (sta
-00000a60: 7274 696e 6720 6174 2061 2064 6174 6574  rting at a datet
-00000a70: 696d 6529 3a5c 6e20 2020 2061 7761 6974  ime):\n    await
-00000a80: 2061 7069 2e67 6574 5f64 6576 6963 655f   api.get_device_
-00000a90: 6465 7461 696c 7328 223c 4445 5649 4345  details("<DEVICE
-00000aa0: 204d 4143 2041 4444 5245 5353 3e22 2c20   MAC ADDRESS>", 
-00000ab0: 656e 645f 6461 7465 3d64 6174 6528 3230  end_date=date(20
-00000ac0: 3139 2c20 312c 2031 3629 295c 6e5c 6e5c  19, 1, 16))\n\n\
-00000ad0: 6e61 7379 6e63 696f 2e72 756e 286d 6169  nasyncio.run(mai
-00000ae0: 6e28 2929 5c6e 6060 605c 6e5c 6e42 7920  n())\n```\n\nBy 
-00000af0: 6465 6661 756c 742c 2074 6865 206c 6962  default, the lib
-00000b00: 7261 7279 2063 7265 6174 6573 2061 206e  rary creates a n
-00000b10: 6577 2063 6f6e 6e65 6374 696f 6e20 746f  ew connection to
-00000b20: 2041 6d62 6965 6e74 2057 6561 7468 6572   Ambient Weather
-00000b30: 2077 6974 6820 6561 6368 2063 6f72 6f75   with each corou
-00000b40: 7469 6e65 2e5c 6e49 6620 796f 7520 6172  tine.\nIf you ar
-00000b50: 6520 6361 6c6c 696e 6720 6120 6c61 7267  e calling a larg
-00000b60: 6520 6e75 6d62 6572 206f 6620 636f 726f  e number of coro
-00000b70: 7574 696e 6573 2028 6f72 206d 6572 656c  utines (or merel
-00000b80: 7920 7761 6e74 2074 6f20 7371 7565 657a  y want to squeez
-00000b90: 6520 6f75 7420 6576 6572 795c 6e73 6563  e out every\nsec
-00000ba0: 6f6e 6420 6f66 2072 756e 7469 6d65 2073  ond of runtime s
-00000bb0: 6176 696e 6773 2070 6f73 7369 626c 6529  avings possible)
-00000bc0: 2c20 616e 5c6e 5b60 6169 6f68 7474 7060  , an\n[`aiohttp`
-00000bd0: 5d28 6874 7470 733a 2f2f 6769 7468 7562  ](https://github
-00000be0: 2e63 6f6d 2f61 696f 2d6c 6962 732f 6169  .com/aio-libs/ai
-00000bf0: 6f68 7474 7029 2060 436c 6965 6e74 5365  ohttp) `ClientSe
-00000c00: 7373 696f 6e60 2063 616e 2062 6520 7573  ssion` can be us
-00000c10: 6564 2066 6f72 2063 6f6e 6e65 6374 696f  ed for connectio
-00000c20: 6e5c 6e70 6f6f 6c69 6e67 3a5c 6e5c 6e60  n\npooling:\n\n`
-00000c30: 6060 7079 7468 6f6e 5c6e 696d 706f 7274  ``python\nimport
-00000c40: 2061 7379 6e63 696f 5c6e 6672 6f6d 2064   asyncio\nfrom d
-00000c50: 6174 6574 696d 6520 696d 706f 7274 2064  atetime import d
-00000c60: 6174 655c 6e5c 6e66 726f 6d20 6169 6f68  ate\n\nfrom aioh
-00000c70: 7474 7020 696d 706f 7274 2043 6c69 656e  ttp import Clien
-00000c80: 7453 6573 7369 6f6e 5c6e 5c6e 6672 6f6d  tSession\n\nfrom
-00000c90: 2061 696f 616d 6269 656e 7420 696d 706f   aioambient impo
-00000ca0: 7274 2041 5049 5c6e 5c6e 5c6e 6173 796e  rt API\n\n\nasyn
-00000cb0: 6320 6465 6620 6d61 696e 2829 202d 3e20  c def main() -> 
-00000cc0: 4e6f 6e65 3a5c 6e20 2020 2022 2222 4372  None:\n    """Cr
-00000cd0: 6561 7465 2074 6865 2061 696f 6874 7470  eate the aiohttp
-00000ce0: 2073 6573 7369 6f6e 2061 6e64 2072 756e   session and run
-00000cf0: 2074 6865 2065 7861 6d70 6c65 2e22 2222   the example."""
-00000d00: 5c6e 2020 2020 6173 796e 6320 7769 7468  \n    async with
-00000d10: 2043 6c69 656e 7453 6573 7369 6f6e 2829   ClientSession()
-00000d20: 2061 7320 7365 7373 696f 6e3a 5c6e 2020   as session:\n  
-00000d30: 2020 2020 2020 6170 6920 3d20 4150 4928        api = API(
-00000d40: 223c 594f 5552 2041 5050 4c49 4341 5449  "<YOUR APPLICATI
-00000d50: 4f4e 204b 4559 3e22 2c20 223c 594f 5552  ON KEY>", "<YOUR
-00000d60: 2041 5049 204b 4559 3e22 295c 6e5c 6e20   API KEY>")\n\n 
-00000d70: 2020 2020 2020 2023 2047 6574 2061 6c6c         # Get all
-00000d80: 2064 6576 6963 6573 2069 6e20 616e 2061   devices in an a
-00000d90: 6363 6f75 6e74 3a5c 6e20 2020 2020 2020  ccount:\n       
-00000da0: 2061 7761 6974 2061 7069 2e67 6574 5f64   await api.get_d
-00000db0: 6576 6963 6573 2829 5c6e 5c6e 2020 2020  evices()\n\n    
-00000dc0: 2020 2020 2320 4765 7420 616c 6c20 7374      # Get all st
-00000dd0: 6f72 6564 2072 6561 6469 6e67 7320 6672  ored readings fr
-00000de0: 6f6d 2061 2064 6576 6963 653a 5c6e 2020  om a device:\n  
-00000df0: 2020 2020 2020 6177 6169 7420 6170 692e        await api.
-00000e00: 6765 745f 6465 7669 6365 5f64 6574 6169  get_device_detai
-00000e10: 6c73 2822 3c44 4556 4943 4520 4d41 4320  ls("<DEVICE MAC 
-00000e20: 4144 4452 4553 533e 2229 5c6e 5c6e 2020  ADDRESS>")\n\n  
-00000e30: 2020 2020 2020 2320 4765 7420 616c 6c20        # Get all 
-00000e40: 7374 6f72 6564 2072 6561 6469 6e67 7320  stored readings 
-00000e50: 6672 6f6d 2061 2064 6576 6963 6520 2873  from a device (s
-00000e60: 7461 7274 696e 6720 6174 2061 2064 6174  tarting at a dat
-00000e70: 6574 696d 6529 3a5c 6e20 2020 2020 2020  etime):\n       
-00000e80: 2061 7761 6974 2061 7069 2e67 6574 5f64   await api.get_d
-00000e90: 6576 6963 655f 6465 7461 696c 7328 223c  evice_details("<
-00000ea0: 4445 5649 4345 204d 4143 2041 4444 5245  DEVICE MAC ADDRE
-00000eb0: 5353 3e22 2c20 656e 645f 6461 7465 3d64  SS>", end_date=d
-00000ec0: 6174 6528 3230 3139 2c20 312c 2031 3629  ate(2019, 1, 16)
-00000ed0: 295c 6e5c 6e5c 6e61 7379 6e63 696f 2e72  )\n\n\nasyncio.r
-00000ee0: 756e 286d 6169 6e28 2929 5c6e 6060 605c  un(main())\n```\
-00000ef0: 6e5c 6e50 6c65 6173 6520 6265 2061 7761  n\nPlease be awa
-00000f00: 7265 206f 6620 416d 6269 656e 7420 5765  re of Ambient We
-00000f10: 6174 6865 725c 2773 5c6e 5b72 6174 6520  ather\'s\n[rate 
-00000f20: 6c69 6d69 7469 6e67 2070 6f6c 6963 6965  limiting policie
-00000f30: 735d 2868 7474 7073 3a2f 2f61 6d62 6965  s](https://ambie
-00000f40: 6e74 7765 6174 6865 722e 646f 6373 2e61  ntweather.docs.a
-00000f50: 7069 6172 792e 696f 2f23 696e 7472 6f64  piary.io/#introd
-00000f60: 7563 7469 6f6e 2f72 6174 652d 6c69 6d69  uction/rate-limi
-00000f70: 7469 6e67 292e 5c6e 5c6e 2323 2057 6562  ting).\n\n## Web
-00000f80: 736f 636b 6574 2041 5049 5c6e 5c6e 6060  socket API\n\n``
-00000f90: 6070 7974 686f 6e5c 6e69 6d70 6f72 7420  `python\nimport 
-00000fa0: 6173 796e 6369 6f5c 6e5c 6e66 726f 6d20  asyncio\n\nfrom 
-00000fb0: 6169 6f68 7474 7020 696d 706f 7274 2043  aiohttp import C
-00000fc0: 6c69 656e 7453 6573 7369 6f6e 5c6e 5c6e  lientSession\n\n
-00000fd0: 6672 6f6d 2061 696f 616d 6269 656e 7420  from aioambient 
-00000fe0: 696d 706f 7274 2057 6562 736f 636b 6574  import Websocket
-00000ff0: 5c6e 5c6e 5c6e 6173 796e 6320 6465 6620  \n\n\nasync def 
-00001000: 6d61 696e 2829 202d 3e20 4e6f 6e65 3a5c  main() -> None:\
-00001010: 6e20 2020 2022 2222 4372 6561 7465 2074  n    """Create t
-00001020: 6865 2061 696f 6874 7470 2073 6573 7369  he aiohttp sessi
-00001030: 6f6e 2061 6e64 2072 756e 2074 6865 2065  on and run the e
-00001040: 7861 6d70 6c65 2e22 2222 5c6e 2020 2020  xample."""\n    
-00001050: 7765 6273 6f63 6b65 7420 3d20 5765 6273  websocket = Webs
-00001060: 6f63 6b65 7428 223c 594f 5552 2041 5050  ocket("<YOUR APP
-00001070: 4c49 4341 5449 4f4e 204b 4559 3e22 2c20  LICATION KEY>", 
-00001080: 223c 594f 5552 2041 5049 204b 4559 3e22  "<YOUR API KEY>"
-00001090: 295c 6e5c 6e20 2020 2023 204e 6f74 6520  )\n\n    # Note 
-000010a0: 7468 6174 2079 6f75 2063 616e 2077 6174  that you can wat
-000010b0: 6368 206d 756c 7469 706c 6520 4150 4920  ch multiple API 
-000010c0: 6b65 7973 2061 7420 6f6e 6365 3a5c 6e20  keys at once:\n 
-000010d0: 2020 2077 6562 736f 636b 6574 203d 2057     websocket = W
-000010e0: 6562 736f 636b 6574 2822 594f 5552 2041  ebsocket("YOUR A
-000010f0: 5050 4c49 4341 5449 4f4e 204b 4559 222c  PPLICATION KEY",
-00001100: 205b 223c 4150 4920 4b45 5920 313e 222c   ["<API KEY 1>",
-00001110: 2022 3c41 5049 204b 4559 2032 3e22 5d29   "<API KEY 2>"])
-00001120: 5c6e 5c6e 2020 2020 2320 4465 6669 6e65  \n\n    # Define
-00001130: 2061 206d 6574 686f 6420 7468 6174 2073   a method that s
-00001140: 686f 756c 6420 6265 2066 6972 6564 2077  hould be fired w
-00001150: 6865 6e20 7468 6520 7765 6273 6f63 6b65  hen the websocke
-00001160: 7420 636c 6965 6e74 5c6e 2020 2020 2320  t client\n    # 
-00001170: 636f 6e6e 6563 7473 3a5c 6e20 2020 2064  connects:\n    d
-00001180: 6566 2063 6f6e 6e65 6374 5f6d 6574 686f  ef connect_metho
-00001190: 6428 293a 5c6e 2020 2020 2020 2020 2222  d():\n        ""
-000011a0: 2250 7269 6e74 2061 2073 696d 706c 6520  "Print a simple 
-000011b0: 2268 656c 6c6f 2220 6d65 7373 6167 652e  "hello" message.
-000011c0: 2222 225c 6e20 2020 2020 2020 2070 7269  """\n        pri
-000011d0: 6e74 2822 436c 6965 6e74 2068 6173 2063  nt("Client has c
-000011e0: 6f6e 6e65 6374 6564 2074 6f20 7468 6520  onnected to the 
-000011f0: 7765 6273 6f63 6b65 7422 295c 6e5c 6e20  websocket")\n\n 
-00001200: 2020 2077 6562 736f 636b 6574 2e6f 6e5f     websocket.on_
-00001210: 636f 6e6e 6563 7428 636f 6e6e 6563 745f  connect(connect_
-00001220: 6d65 7468 6f64 295c 6e5c 6e20 2020 2023  method)\n\n    #
-00001230: 2041 6c74 6572 6e61 7469 7665 6c79 2c20   Alternatively, 
-00001240: 6465 6669 6e65 2061 2063 6f72 6f75 7469  define a corouti
-00001250: 6e65 2068 616e 646c 6572 3a5c 6e20 2020  ne handler:\n   
-00001260: 2061 7379 6e63 2064 6566 2063 6f6e 6e65   async def conne
-00001270: 6374 5f63 6f72 6f75 7469 6e65 2829 3a5c  ct_coroutine():\
-00001280: 6e20 2020 2020 2020 2022 2222 5761 6974  n        """Wait
-00001290: 7320 666f 7220 3320 7365 636f 6e64 732c  s for 3 seconds,
-000012a0: 2074 6865 6e20 7072 696e 7420 6120 7369   then print a si
-000012b0: 6d70 6c65 2022 6865 6c6c 6f22 206d 6573  mple "hello" mes
-000012c0: 7361 6765 2e22 2222 5c6e 2020 2020 2020  sage."""\n      
-000012d0: 2020 6177 6169 7420 6173 796e 6369 6f2e    await asyncio.
-000012e0: 736c 6565 7028 3329 5c6e 2020 2020 2020  sleep(3)\n      
-000012f0: 2020 7072 696e 7428 2243 6c69 656e 7420    print("Client 
-00001300: 6861 7320 636f 6e6e 6563 7465 6420 746f  has connected to
-00001310: 2074 6865 2077 6562 736f 636b 6574 2229   the websocket")
-00001320: 5c6e 5c6e 2020 2020 7765 6273 6f63 6b65  \n\n    websocke
-00001330: 742e 6173 796e 635f 6f6e 5f63 6f6e 6e65  t.async_on_conne
-00001340: 6374 2863 6f6e 6e65 6374 5f63 6f72 6f75  ct(connect_corou
-00001350: 7469 6e65 295c 6e5c 6e20 2020 2023 2044  tine)\n\n    # D
-00001360: 6566 696e 6520 6120 6d65 7468 6f64 2074  efine a method t
-00001370: 6861 7420 7368 6f75 6c64 2062 6520 7275  hat should be ru
-00001380: 6e20 7570 6f6e 2073 7562 7363 7269 6269  n upon subscribi
-00001390: 6e67 2074 6f20 7468 6520 416d 6269 656e  ng to the Ambien
-000013a0: 745c 6e20 2020 2023 2057 6561 7468 6572  t\n    # Weather
-000013b0: 2063 6c6f 7564 3a5c 6e20 2020 2064 6566   cloud:\n    def
-000013c0: 2073 7562 7363 7269 6265 645f 6d65 7468   subscribed_meth
-000013d0: 6f64 2864 6174 6129 3a5c 6e20 2020 2020  od(data):\n     
-000013e0: 2020 2022 2222 5072 696e 7420 7468 6520     """Print the 
-000013f0: 6461 7461 2072 6563 6569 7665 6420 7570  data received up
-00001400: 6f6e 2073 7562 7363 7269 6269 6e67 2e22  on subscribing."
-00001410: 2222 5c6e 2020 2020 2020 2020 7072 696e  ""\n        prin
-00001420: 7428 6622 5375 6273 6372 6970 7469 6f6e  t(f"Subscription
-00001430: 2064 6174 6120 7265 6365 6976 6564 3a20   data received: 
-00001440: 7b64 6174 617d 2229 5c6e 5c6e 2020 2020  {data}")\n\n    
-00001450: 7765 6273 6f63 6b65 742e 6f6e 5f73 7562  websocket.on_sub
-00001460: 7363 7269 6265 6428 7375 6273 6372 6962  scribed(subscrib
-00001470: 6564 5f6d 6574 686f 6429 5c6e 5c6e 2020  ed_method)\n\n  
-00001480: 2020 2320 416c 7465 726e 6174 6976 656c    # Alternativel
-00001490: 792c 2064 6566 696e 6520 6120 636f 726f  y, define a coro
-000014a0: 7574 696e 6520 6861 6e64 6c65 723a 5c6e  utine handler:\n
-000014b0: 2020 2020 6173 796e 6320 6465 6620 7375      async def su
-000014c0: 6273 6372 6962 6564 5f63 6f72 6f75 7469  bscribed_corouti
-000014d0: 6e65 2864 6174 6129 3a5c 6e20 2020 2020  ne(data):\n     
-000014e0: 2020 2022 2222 5761 6974 7320 666f 7220     """Waits for 
-000014f0: 3320 7365 636f 6e64 732c 2074 6865 6e20  3 seconds, then 
-00001500: 7072 696e 7420 7468 6520 696e 636f 6d69  print the incomi
-00001510: 6e67 2064 6174 612e 2222 225c 6e20 2020  ng data."""\n   
-00001520: 2020 2020 2061 7761 6974 2061 7379 6e63       await async
-00001530: 696f 2e73 6c65 6570 2833 295c 6e20 2020  io.sleep(3)\n   
-00001540: 2020 2020 2070 7269 6e74 2866 2253 7562       print(f"Sub
-00001550: 7363 7269 7074 696f 6e20 6461 7461 2072  scription data r
-00001560: 6563 6569 7665 643a 207b 6461 7461 7d22  eceived: {data}"
-00001570: 295c 6e5c 6e20 2020 2077 6562 736f 636b  )\n\n    websock
-00001580: 6574 2e61 7379 6e63 5f6f 6e5f 7375 6273  et.async_on_subs
-00001590: 6372 6962 6564 2873 7562 7363 7269 6265  cribed(subscribe
-000015a0: 645f 636f 726f 7574 696e 6529 5c6e 5c6e  d_coroutine)\n\n
-000015b0: 2020 2020 2320 4465 6669 6e65 2061 206d      # Define a m
-000015c0: 6574 686f 6420 7468 6174 2073 686f 756c  ethod that shoul
-000015d0: 6420 6265 2072 756e 2075 706f 6e20 7265  d be run upon re
-000015e0: 6365 6976 696e 6720 6461 7461 3a5c 6e20  ceiving data:\n 
-000015f0: 2020 2064 6566 2064 6174 615f 6d65 7468     def data_meth
-00001600: 6f64 2864 6174 6129 3a5c 6e20 2020 2020  od(data):\n     
-00001610: 2020 2022 2222 5072 696e 7420 7468 6520     """Print the 
-00001620: 6461 7461 2072 6563 6569 7665 642e 2222  data received.""
-00001630: 225c 6e20 2020 2020 2020 2070 7269 6e74  "\n        print
-00001640: 2866 2244 6174 6120 7265 6365 6976 6564  (f"Data received
-00001650: 3a20 7b64 6174 617d 2229 5c6e 5c6e 2020  : {data}")\n\n  
-00001660: 2020 7765 6273 6f63 6b65 742e 6f6e 5f64    websocket.on_d
-00001670: 6174 6128 6461 7461 5f6d 6574 686f 6429  ata(data_method)
-00001680: 5c6e 5c6e 2020 2020 2320 416c 7465 726e  \n\n    # Altern
-00001690: 6174 6976 656c 792c 2064 6566 696e 6520  atively, define 
-000016a0: 6120 636f 726f 7574 696e 6520 6861 6e64  a coroutine hand
-000016b0: 6c65 723a 5c6e 2020 2020 6173 796e 6320  ler:\n    async 
-000016c0: 6465 6620 6461 7461 5f63 6f72 6f75 7469  def data_corouti
-000016d0: 6e65 2864 6174 6129 3a5c 6e20 2020 2020  ne(data):\n     
-000016e0: 2020 2022 2222 5761 6974 2066 6f72 2033     """Wait for 3
-000016f0: 2073 6563 6f6e 6473 2c20 7468 656e 2070   seconds, then p
-00001700: 7269 6e74 2074 6865 2064 6174 6120 7265  rint the data re
-00001710: 6365 6976 6564 2e22 2222 5c6e 2020 2020  ceived."""\n    
-00001720: 2020 2020 6177 6169 7420 6173 796e 6369      await asynci
-00001730: 6f2e 736c 6565 7028 3329 5c6e 2020 2020  o.sleep(3)\n    
-00001740: 2020 2020 7072 696e 7428 6622 4461 7461      print(f"Data
-00001750: 2072 6563 6569 7665 643a 207b 6461 7461   received: {data
-00001760: 7d22 295c 6e5c 6e20 2020 2077 6562 736f  }")\n\n    webso
-00001770: 636b 6574 2e61 7379 6e63 5f6f 6e5f 6461  cket.async_on_da
-00001780: 7461 2864 6174 615f 636f 726f 7574 696e  ta(data_coroutin
-00001790: 6529 5c6e 5c6e 2020 2020 2320 4465 6669  e)\n\n    # Defi
-000017a0: 6e65 2061 206d 6574 686f 6420 7468 6174  ne a method that
-000017b0: 2073 686f 756c 6420 6265 2072 756e 2077   should be run w
-000017c0: 6865 6e20 7468 6520 7765 6273 6f63 6b65  hen the websocke
-000017d0: 7420 636c 6965 6e74 5c6e 2020 2020 2320  t client\n    # 
-000017e0: 6469 7363 6f6e 6e65 6374 733a 5c6e 2020  disconnects:\n  
-000017f0: 2020 6465 6620 6469 7363 6f6e 6e65 6374    def disconnect
-00001800: 5f6d 6574 686f 6428 6461 7461 293a 5c6e  _method(data):\n
-00001810: 2020 2020 2020 2020 2222 2250 7269 6e74          """Print
-00001820: 2061 2073 696d 706c 6520 2267 6f6f 6462   a simple "goodb
-00001830: 7965 2220 6d65 7373 6167 652e 2222 225c  ye" message."""\
-00001840: 6e20 2020 2020 2020 2070 7269 6e74 2822  n        print("
-00001850: 436c 6965 6e74 2068 6173 2064 6973 636f  Client has disco
-00001860: 6e6e 6563 7465 6420 6672 6f6d 2074 6865  nnected from the
-00001870: 2077 6562 736f 636b 6574 2229 5c6e 5c6e   websocket")\n\n
-00001880: 2020 2020 7765 6273 6f63 6b65 742e 6f6e      websocket.on
-00001890: 5f64 6973 636f 6e6e 6563 7428 6469 7363  _disconnect(disc
-000018a0: 6f6e 6e65 6374 5f6d 6574 686f 6429 5c6e  onnect_method)\n
-000018b0: 5c6e 2020 2020 2320 416c 7465 726e 6174  \n    # Alternat
-000018c0: 6976 656c 792c 2064 6566 696e 6520 6120  ively, define a 
-000018d0: 636f 726f 7574 696e 6520 6861 6e64 6c65  coroutine handle
-000018e0: 723a 5c6e 2020 2020 6173 796e 6320 6465  r:\n    async de
-000018f0: 6620 6469 7363 6f6e 6e65 6374 5f63 6f72  f disconnect_cor
-00001900: 6f75 7469 6e65 2864 6174 6129 3a5c 6e20  outine(data):\n 
-00001910: 2020 2020 2020 2022 2222 5761 6974 2066         """Wait f
-00001920: 6f72 2033 2073 6563 6f6e 6473 2c20 7468  or 3 seconds, th
-00001930: 656e 2070 7269 6e74 2061 2073 696d 706c  en print a simpl
-00001940: 6520 2267 6f6f 6462 7965 2220 6d65 7373  e "goodbye" mess
-00001950: 6167 652e 2222 225c 6e20 2020 2020 2020  age."""\n       
-00001960: 2061 7761 6974 2061 7379 6e63 696f 2e73   await asyncio.s
-00001970: 6c65 6570 2833 295c 6e20 2020 2020 2020  leep(3)\n       
-00001980: 2070 7269 6e74 2822 436c 6965 6e74 2068   print("Client h
-00001990: 6173 2064 6973 636f 6e6e 6563 7465 6420  as disconnected 
-000019a0: 6672 6f6d 2074 6865 2077 6562 736f 636b  from the websock
-000019b0: 6574 2229 5c6e 5c6e 2020 2020 7765 6273  et")\n\n    webs
-000019c0: 6f63 6b65 742e 6173 796e 635f 6f6e 5f64  ocket.async_on_d
-000019d0: 6973 636f 6e6e 6563 7428 6469 7363 6f6e  isconnect(discon
-000019e0: 6e65 6374 5f63 6f72 6f75 7469 6e65 295c  nect_coroutine)\
-000019f0: 6e5c 6e20 2020 2023 2043 6f6e 6e65 6374  n\n    # Connect
-00001a00: 2074 6f20 7468 6520 7765 6273 6f63 6b65   to the websocke
-00001a10: 743a 5c6e 2020 2020 6177 6169 7420 7765  t:\n    await we
-00001a20: 6273 6f63 6b65 742e 636f 6e6e 6563 7428  bsocket.connect(
-00001a30: 295c 6e5c 6e20 2020 2023 2041 7420 616e  )\n\n    # At an
-00001a40: 7920 706f 696e 742c 2064 6973 636f 6e6e  y point, disconn
-00001a50: 6563 7420 6672 6f6d 2074 6865 2077 6562  ect from the web
-00001a60: 736f 636b 6574 3a5c 6e20 2020 2061 7761  socket:\n    awa
-00001a70: 6974 2077 6562 736f 636b 6574 2e64 6973  it websocket.dis
-00001a80: 636f 6e6e 6563 7428 295c 6e5c 6e5c 6e61  connect()\n\n\na
-00001a90: 7379 6e63 696f 2e72 756e 286d 6169 6e28  syncio.run(main(
-00001aa0: 2929 5c6e 6060 605c 6e5c 6e23 2043 6f6e  ))\n```\n\n# Con
-00001ab0: 7472 6962 7574 696e 675c 6e5c 6e31 2e20  tributing\n\n1. 
-00001ac0: 5b43 6865 636b 2066 6f72 206f 7065 6e20  [Check for open 
-00001ad0: 6665 6174 7572 6573 2f62 7567 735d 2868  features/bugs](h
-00001ae0: 7474 7073 3a2f 2f67 6974 6875 622e 636f  ttps://github.co
-00001af0: 6d2f 6261 6368 7961 2f61 696f 616d 6269  m/bachya/aioambi
-00001b00: 656e 742f 6973 7375 6573 295c 6e20 2020  ent/issues)\n   
-00001b10: 6f72 205b 696e 6974 6961 7465 2061 2064  or [initiate a d
-00001b20: 6973 6375 7373 696f 6e20 6f6e 206f 6e65  iscussion on one
-00001b30: 5d28 6874 7470 733a 2f2f 6769 7468 7562  ](https://github
-00001b40: 2e63 6f6d 2f62 6163 6879 612f 6169 6f61  .com/bachya/aioa
-00001b50: 6d62 6965 6e74 2f69 7373 7565 732f 6e65  mbient/issues/ne
-00001b60: 7729 2e5c 6e32 2e20 5b46 6f72 6b20 7468  w).\n2. [Fork th
-00001b70: 6520 7265 706f 7369 746f 7279 5d28 6874  e repository](ht
-00001b80: 7470 733a 2f2f 6769 7468 7562 2e63 6f6d  tps://github.com
-00001b90: 2f62 6163 6879 612f 6169 6f61 6d62 6965  /bachya/aioambie
-00001ba0: 6e74 2f66 6f72 6b29 2e5c 6e33 2e20 285f  nt/fork).\n3. (_
-00001bb0: 6f70 7469 6f6e 616c 2c20 6275 7420 6869  optional, but hi
-00001bc0: 6768 6c79 2072 6563 6f6d 6d65 6e64 6564  ghly recommended
-00001bd0: 5f29 2043 7265 6174 6520 6120 7669 7274  _) Create a virt
-00001be0: 7561 6c20 656e 7669 726f 6e6d 656e 743a  ual environment:
-00001bf0: 2060 7079 7468 6f6e 3320 2d6d 2076 656e   `python3 -m ven
-00001c00: 7620 2e76 656e 7660 5c6e 342e 2028 5f6f  v .venv`\n4. (_o
-00001c10: 7074 696f 6e61 6c2c 2062 7574 2068 6967  ptional, but hig
-00001c20: 686c 7920 7265 636f 6d6d 656e 6465 645f  hly recommended_
-00001c30: 2920 456e 7465 7220 7468 6520 7669 7274  ) Enter the virt
-00001c40: 7561 6c20 656e 7669 726f 6e6d 656e 743a  ual environment:
-00001c50: 2060 736f 7572 6365 202e 2f76 656e 762f   `source ./venv/
-00001c60: 6269 6e2f 6163 7469 7661 7465 605c 6e35  bin/activate`\n5
-00001c70: 2e20 496e 7374 616c 6c20 7468 6520 6465  . Install the de
-00001c80: 7620 656e 7669 726f 6e6d 656e 743a 2060  v environment: `
-00001c90: 7363 7269 7074 2f73 6574 7570 605c 6e36  script/setup`\n6
-00001ca0: 2e20 436f 6465 2079 6f75 7220 6e65 7720  . Code your new 
-00001cb0: 6665 6174 7572 6520 6f72 2062 7567 2066  feature or bug f
-00001cc0: 6978 2e5c 6e37 2e20 5772 6974 6520 7465  ix.\n7. Write te
-00001cd0: 7374 7320 7468 6174 2063 6f76 6572 2079  sts that cover y
-00001ce0: 6f75 7220 6e65 7720 6675 6e63 7469 6f6e  our new function
-00001cf0: 616c 6974 792e 5c6e 382e 2052 756e 2074  ality.\n8. Run t
-00001d00: 6573 7473 2061 6e64 2065 6e73 7572 6520  ests and ensure 
-00001d10: 3130 3025 2063 6f64 6520 636f 7665 7261  100% code covera
-00001d20: 6765 3a20 6070 6f65 7472 7920 7275 6e20  ge: `poetry run 
-00001d30: 7079 7465 7374 202d 2d63 6f76 2061 696f  pytest --cov aio
-00001d40: 616d 6269 656e 7420 7465 7374 7360 5c6e  ambient tests`\n
-00001d50: 392e 2055 7064 6174 6520 6052 4541 444d  9. Update `READM
-00001d60: 452e 6d64 6020 7769 7468 2061 6e79 206e  E.md` with any n
-00001d70: 6577 2064 6f63 756d 656e 7461 7469 6f6e  ew documentation
-00001d80: 2e5c 6e31 302e 2041 6464 2079 6f75 7273  .\n10. Add yours
-00001d90: 656c 6620 746f 2060 4155 5448 4f52 532e  elf to `AUTHORS.
-00001da0: 6d64 602e 5c6e 3131 2e20 5375 626d 6974  md`.\n11. Submit
-00001db0: 2061 2070 756c 6c20 7265 7175 6573 7421   a pull request!
-00001dc0: 5c6e 272c 0a20 2020 2027 6175 7468 6f72  \n',.    'author
-00001dd0: 273a 2027 4161 726f 6e20 4261 6368 272c  ': 'Aaron Bach',
-00001de0: 0a20 2020 2027 6175 7468 6f72 5f65 6d61  .    'author_ema
-00001df0: 696c 273a 2027 6261 6368 7961 3132 3038  il': 'bachya1208
-00001e00: 4067 6d61 696c 2e63 6f6d 272c 0a20 2020  @gmail.com',.   
-00001e10: 2027 6d61 696e 7461 696e 6572 273a 2027   'maintainer': '
-00001e20: 4e6f 6e65 272c 0a20 2020 2027 6d61 696e  None',.    'main
-00001e30: 7461 696e 6572 5f65 6d61 696c 273a 2027  tainer_email': '
-00001e40: 4e6f 6e65 272c 0a20 2020 2027 7572 6c27  None',.    'url'
-00001e50: 3a20 2768 7474 7073 3a2f 2f67 6974 6875  : 'https://githu
-00001e60: 622e 636f 6d2f 6261 6368 7961 2f61 696f  b.com/bachya/aio
-00001e70: 616d 6269 656e 7427 2c0a 2020 2020 2770  ambient',.    'p
-00001e80: 6163 6b61 6765 7327 3a20 7061 636b 6167  ackages': packag
-00001e90: 6573 2c0a 2020 2020 2770 6163 6b61 6765  es,.    'package
-00001ea0: 5f64 6174 6127 3a20 7061 636b 6167 655f  _data': package_
-00001eb0: 6461 7461 2c0a 2020 2020 2769 6e73 7461  data,.    'insta
-00001ec0: 6c6c 5f72 6571 7569 7265 7327 3a20 696e  ll_requires': in
-00001ed0: 7374 616c 6c5f 7265 7175 6972 6573 2c0a  stall_requires,.
-00001ee0: 2020 2020 2770 7974 686f 6e5f 7265 7175      'python_requ
-00001ef0: 6972 6573 273a 2027 3e3d 332e 392e 302c  ires': '>=3.9.0,
-00001f00: 3c34 2e30 2e30 272c 0a7d 0a0a 0a73 6574  <4.0.0',.}...set
-00001f10: 7570 282a 2a73 6574 7570 5f6b 7761 7267  up(**setup_kwarg
-00001f20: 7329 0a                                  s).
+00000000: 4d65 7461 6461 7461 2d56 6572 7369 6f6e  Metadata-Version
+00000010: 3a20 322e 310a 4e61 6d65 3a20 6169 6f61  : 2.1.Name: aioa
+00000020: 6d62 6965 6e74 0a56 6572 7369 6f6e 3a20  mbient.Version: 
+00000030: 3230 3233 2e34 2e30 0a53 756d 6d61 7279  2023.4.0.Summary
+00000040: 3a20 4120 636c 6561 6e2c 2061 7379 6e63  : A clean, async
+00000050: 2d66 7269 656e 646c 7920 6c69 6272 6172  -friendly librar
+00000060: 7920 666f 7220 7468 6520 416d 6269 656e  y for the Ambien
+00000070: 7420 5765 6174 6865 7220 4150 490a 486f  t Weather API.Ho
+00000080: 6d65 2d70 6167 653a 2068 7474 7073 3a2f  me-page: https:/
+00000090: 2f67 6974 6875 622e 636f 6d2f 6261 6368  /github.com/bach
+000000a0: 7961 2f61 696f 616d 6269 656e 740a 4c69  ya/aioambient.Li
+000000b0: 6365 6e73 653a 204d 4954 0a41 7574 686f  cense: MIT.Autho
+000000c0: 723a 2041 6172 6f6e 2042 6163 680a 4175  r: Aaron Bach.Au
+000000d0: 7468 6f72 2d65 6d61 696c 3a20 6261 6368  thor-email: bach
+000000e0: 7961 3132 3038 4067 6d61 696c 2e63 6f6d  ya1208@gmail.com
+000000f0: 0a52 6571 7569 7265 732d 5079 7468 6f6e  .Requires-Python
+00000100: 3a20 3e3d 332e 392e 302c 3c34 2e30 2e30  : >=3.9.0,<4.0.0
+00000110: 0a43 6c61 7373 6966 6965 723a 204c 6963  .Classifier: Lic
+00000120: 656e 7365 203a 3a20 4f53 4920 4170 7072  ense :: OSI Appr
+00000130: 6f76 6564 203a 3a20 4d49 5420 4c69 6365  oved :: MIT Lice
+00000140: 6e73 650a 436c 6173 7369 6669 6572 3a20  nse.Classifier: 
+00000150: 5072 6f67 7261 6d6d 696e 6720 4c61 6e67  Programming Lang
+00000160: 7561 6765 203a 3a20 5079 7468 6f6e 0a43  uage :: Python.C
+00000170: 6c61 7373 6966 6965 723a 2050 726f 6772  lassifier: Progr
+00000180: 616d 6d69 6e67 204c 616e 6775 6167 6520  amming Language 
+00000190: 3a3a 2050 7974 686f 6e20 3a3a 2033 0a43  :: Python :: 3.C
+000001a0: 6c61 7373 6966 6965 723a 2050 726f 6772  lassifier: Progr
+000001b0: 616d 6d69 6e67 204c 616e 6775 6167 6520  amming Language 
+000001c0: 3a3a 2050 7974 686f 6e20 3a3a 2033 2e39  :: Python :: 3.9
+000001d0: 0a43 6c61 7373 6966 6965 723a 2050 726f  .Classifier: Pro
+000001e0: 6772 616d 6d69 6e67 204c 616e 6775 6167  gramming Languag
+000001f0: 6520 3a3a 2050 7974 686f 6e20 3a3a 2033  e :: Python :: 3
+00000200: 2e31 300a 436c 6173 7369 6669 6572 3a20  .10.Classifier: 
+00000210: 5072 6f67 7261 6d6d 696e 6720 4c61 6e67  Programming Lang
+00000220: 7561 6765 203a 3a20 5079 7468 6f6e 203a  uage :: Python :
+00000230: 3a20 332e 3131 0a43 6c61 7373 6966 6965  : 3.11.Classifie
+00000240: 723a 2050 726f 6772 616d 6d69 6e67 204c  r: Programming L
+00000250: 616e 6775 6167 6520 3a3a 2050 7974 686f  anguage :: Pytho
+00000260: 6e20 3a3a 2033 0a43 6c61 7373 6966 6965  n :: 3.Classifie
+00000270: 723a 2050 726f 6772 616d 6d69 6e67 204c  r: Programming L
+00000280: 616e 6775 6167 6520 3a3a 2050 7974 686f  anguage :: Pytho
+00000290: 6e20 3a3a 2033 2e31 300a 436c 6173 7369  n :: 3.10.Classi
+000002a0: 6669 6572 3a20 5072 6f67 7261 6d6d 696e  fier: Programmin
+000002b0: 6720 4c61 6e67 7561 6765 203a 3a20 5079  g Language :: Py
+000002c0: 7468 6f6e 203a 3a20 332e 3131 0a43 6c61  thon :: 3.11.Cla
+000002d0: 7373 6966 6965 723a 2050 726f 6772 616d  ssifier: Program
+000002e0: 6d69 6e67 204c 616e 6775 6167 6520 3a3a  ming Language ::
+000002f0: 2050 7974 686f 6e20 3a3a 2033 2e39 0a43   Python :: 3.9.C
+00000300: 6c61 7373 6966 6965 723a 2050 726f 6772  lassifier: Progr
+00000310: 616d 6d69 6e67 204c 616e 6775 6167 6520  amming Language 
+00000320: 3a3a 2050 7974 686f 6e20 3a3a 2049 6d70  :: Python :: Imp
+00000330: 6c65 6d65 6e74 6174 696f 6e20 3a3a 2043  lementation :: C
+00000340: 5079 7468 6f6e 0a43 6c61 7373 6966 6965  Python.Classifie
+00000350: 723a 2050 726f 6772 616d 6d69 6e67 204c  r: Programming L
+00000360: 616e 6775 6167 6520 3a3a 2050 7974 686f  anguage :: Pytho
+00000370: 6e20 3a3a 2049 6d70 6c65 6d65 6e74 6174  n :: Implementat
+00000380: 696f 6e20 3a3a 2050 7950 790a 5265 7175  ion :: PyPy.Requ
+00000390: 6972 6573 2d44 6973 743a 2061 696f 6874  ires-Dist: aioht
+000003a0: 7470 2028 3e3d 332e 382e 3029 0a52 6571  tp (>=3.8.0).Req
+000003b0: 7569 7265 732d 4469 7374 3a20 7079 7468  uires-Dist: pyth
+000003c0: 6f6e 2d65 6e67 696e 6569 6f20 283e 3d33  on-engineio (>=3
+000003d0: 2e31 332e 312c 3c35 2e30 2e30 290a 5265  .13.1,<5.0.0).Re
+000003e0: 7175 6972 6573 2d44 6973 743a 2070 7974  quires-Dist: pyt
+000003f0: 686f 6e2d 736f 636b 6574 696f 2028 3e3d  hon-socketio (>=
+00000400: 342e 362c 3c36 2e30 290a 5265 7175 6972  4.6,<6.0).Requir
+00000410: 6573 2d44 6973 743a 2077 6562 736f 636b  es-Dist: websock
+00000420: 6574 7320 283e 3d31 312e 302e 3129 0a50  ets (>=11.0.1).P
+00000430: 726f 6a65 6374 2d55 524c 3a20 4275 6720  roject-URL: Bug 
+00000440: 5472 6163 6b65 722c 2068 7474 7073 3a2f  Tracker, https:/
+00000450: 2f67 6974 6875 622e 636f 6d2f 6261 6368  /github.com/bach
+00000460: 7961 2f61 696f 616d 6269 656e 742f 6973  ya/aioambient/is
+00000470: 7375 6573 0a50 726f 6a65 6374 2d55 524c  sues.Project-URL
+00000480: 3a20 4368 616e 6765 6c6f 672c 2068 7474  : Changelog, htt
+00000490: 7073 3a2f 2f67 6974 6875 622e 636f 6d2f  ps://github.com/
+000004a0: 6261 6368 7961 2f61 696f 616d 6269 656e  bachya/aioambien
+000004b0: 742f 7265 6c65 6173 6573 0a50 726f 6a65  t/releases.Proje
+000004c0: 6374 2d55 524c 3a20 5265 706f 7369 746f  ct-URL: Reposito
+000004d0: 7279 2c20 6874 7470 733a 2f2f 6769 7468  ry, https://gith
+000004e0: 7562 2e63 6f6d 2f62 6163 6879 612f 6169  ub.com/bachya/ai
+000004f0: 6f61 6d62 6965 6e74 0a44 6573 6372 6970  oambient.Descrip
+00000500: 7469 6f6e 2d43 6f6e 7465 6e74 2d54 7970  tion-Content-Typ
+00000510: 653a 2074 6578 742f 6d61 726b 646f 776e  e: text/markdown
+00000520: 0a0a 2320 f09f 8ca4 2061 696f 616d 6269  ..# .... aioambi
+00000530: 656e 743a 2041 6e20 6173 796e 6320 6c69  ent: An async li
+00000540: 6272 6172 7920 666f 7220 416d 6269 656e  brary for Ambien
+00000550: 7420 5765 6174 6865 7220 5065 7273 6f6e  t Weather Person
+00000560: 616c 2057 6561 7468 6572 2053 7461 7469  al Weather Stati
+00000570: 6f6e 730a 0a5b 215b 4349 5d5b 6369 2d62  ons..[![CI][ci-b
+00000580: 6164 6765 5d5d 5b63 695d 0a5b 215b 5079  adge]][ci].[![Py
+00000590: 5049 5d5b 7079 7069 2d62 6164 6765 5d5d  PI][pypi-badge]]
+000005a0: 5b70 7970 695d 0a5b 215b 5665 7273 696f  [pypi].[![Versio
+000005b0: 6e5d 5b76 6572 7369 6f6e 2d62 6164 6765  n][version-badge
+000005c0: 5d5d 5b76 6572 7369 6f6e 5d0a 5b21 5b4c  ]][version].[![L
+000005d0: 6963 656e 7365 5d5b 6c69 6365 6e73 652d  icense][license-
+000005e0: 6261 6467 655d 5d5b 6c69 6365 6e73 655d  badge]][license]
+000005f0: 0a5b 215b 436f 6465 2043 6f76 6572 6167  .[![Code Coverag
+00000600: 655d 5b63 6f64 6563 6f76 2d62 6164 6765  e][codecov-badge
+00000610: 5d5d 5b63 6f64 6563 6f76 5d0a 5b21 5b4d  ]][codecov].[![M
+00000620: 6169 6e74 6169 6e61 6269 6c69 7479 5d5b  aintainability][
+00000630: 6d61 696e 7461 696e 6162 696c 6974 792d  maintainability-
+00000640: 6261 6467 655d 5d5b 6d61 696e 7461 696e  badge]][maintain
+00000650: 6162 696c 6974 795d 0a0a 3c61 2068 7265  ability]..<a hre
+00000660: 663d 2268 7474 7073 3a2f 2f77 7777 2e62  f="https://www.b
+00000670: 7579 6d65 6163 6f66 6665 652e 636f 6d2f  uymeacoffee.com/
+00000680: 6261 6368 7961 3132 3038 5022 2074 6172  bachya1208P" tar
+00000690: 6765 743d 225f 626c 616e 6b22 3e3c 696d  get="_blank"><im
+000006a0: 6720 7372 633d 2268 7474 7073 3a2f 2f63  g src="https://c
+000006b0: 646e 2e62 7579 6d65 6163 6f66 6665 652e  dn.buymeacoffee.
+000006c0: 636f 6d2f 6275 7474 6f6e 732f 6465 6661  com/buttons/defa
+000006d0: 756c 742d 6f72 616e 6765 2e70 6e67 2220  ult-orange.png" 
+000006e0: 616c 743d 2242 7579 204d 6520 4120 436f  alt="Buy Me A Co
+000006f0: 6666 6565 2220 6865 6967 6874 3d22 3431  ffee" height="41
+00000700: 2220 7769 6474 683d 2231 3734 223e 3c2f  " width="174"></
+00000710: 613e 0a0a 6061 696f 616d 6269 656e 7460  a>..`aioambient`
+00000720: 2069 7320 6120 5079 7468 6f6e 332c 2061   is a Python3, a
+00000730: 7379 6e63 696f 2d64 7269 7665 6e20 6c69  syncio-driven li
+00000740: 6272 6172 7920 7468 6174 2069 6e74 6572  brary that inter
+00000750: 6661 6365 7320 7769 7468 2062 6f74 6820  faces with both 
+00000760: 7468 6520 5245 5354 2061 6e64 0a57 6562  the REST and.Web
+00000770: 736f 636b 6574 2041 5049 7320 7072 6f76  socket APIs prov
+00000780: 6964 6564 2062 7920 5b41 6d62 6965 6e74  ided by [Ambient
+00000790: 2057 6561 7468 6572 5d5b 616d 6269 656e   Weather][ambien
+000007a0: 742d 7765 6174 6865 725d 2e0a 0a2d 205b  t-weather]...- [
+000007b0: 496e 7374 616c 6c61 7469 6f6e 5d28 2369  Installation](#i
+000007c0: 6e73 7461 6c6c 6174 696f 6e29 0a2d 205b  nstallation).- [
+000007d0: 5079 7468 6f6e 2056 6572 7369 6f6e 735d  Python Versions]
+000007e0: 2823 7079 7468 6f6e 2d76 6572 7369 6f6e  (#python-version
+000007f0: 7329 0a2d 205b 4150 4920 616e 6420 4170  s).- [API and Ap
+00000800: 706c 6963 6174 696f 6e20 4b65 7973 5d28  plication Keys](
+00000810: 2361 7069 2d61 6e64 2d61 7070 6c69 6361  #api-and-applica
+00000820: 7469 6f6e 2d6b 6579 7329 0a2d 205b 5573  tion-keys).- [Us
+00000830: 6167 655d 2823 7573 6167 6529 0a2d 205b  age](#usage).- [
+00000840: 436f 6e74 7269 6275 7469 6e67 5d28 2363  Contributing](#c
+00000850: 6f6e 7472 6962 7574 696e 6729 0a0a 2320  ontributing)..# 
+00000860: 496e 7374 616c 6c61 7469 6f6e 0a0a 6060  Installation..``
+00000870: 6062 6173 680a 7069 7020 696e 7374 616c  `bash.pip instal
+00000880: 6c20 6169 6f61 6d62 6965 6e74 0a60 6060  l aioambient.```
+00000890: 0a0a 2320 5079 7468 6f6e 2056 6572 7369  ..# Python Versi
+000008a0: 6f6e 730a 0a60 6169 6f61 6d62 6965 6e74  ons..`aioambient
+000008b0: 6020 6973 2063 7572 7265 6e74 6c79 2073  ` is currently s
+000008c0: 7570 706f 7274 6564 206f 6e3a 0a0a 2d20  upported on:..- 
+000008d0: 5079 7468 6f6e 2033 2e39 0a2d 2050 7974  Python 3.9.- Pyt
+000008e0: 686f 6e20 332e 3130 0a2d 2050 7974 686f  hon 3.10.- Pytho
+000008f0: 6e20 332e 3131 0a0a 2320 4150 4920 616e  n 3.11..# API an
+00000900: 6420 4170 706c 6963 6174 696f 6e20 4b65  d Application Ke
+00000910: 7973 0a0a 5574 696c 697a 696e 6720 6061  ys..Utilizing `a
+00000920: 696f 616d 6269 656e 7460 2072 6571 7569  ioambient` requi
+00000930: 7265 7320 626f 7468 2061 6e20 4170 706c  res both an Appl
+00000940: 6963 6174 696f 6e20 4b65 7920 616e 6420  ication Key and 
+00000950: 616e 2041 5049 204b 6579 2066 726f 6d20  an API Key from 
+00000960: 416d 6269 656e 740a 5765 6174 6865 722e  Ambient.Weather.
+00000970: 2059 6f75 2063 616e 2067 656e 6572 6174   You can generat
+00000980: 6520 626f 7468 2066 726f 6d20 7468 6520  e both from the 
+00000990: 5072 6f66 696c 6520 7061 6765 2069 6e20  Profile page in 
+000009a0: 796f 7572 0a5b 416d 6269 656e 7420 5765  your.[Ambient We
+000009b0: 6174 6865 7220 4461 7368 626f 6172 645d  ather Dashboard]
+000009c0: 5b61 6d62 6965 6e74 2d77 6561 7468 6572  [ambient-weather
+000009d0: 2d64 6173 6862 6f61 7264 5d2e 0a0a 2320  -dashboard]...# 
+000009e0: 5573 6167 650a 0a23 2320 5245 5354 2041  Usage..## REST A
+000009f0: 5049 0a0a 6060 6070 7974 686f 6e0a 696d  PI..```python.im
+00000a00: 706f 7274 2061 7379 6e63 696f 0a66 726f  port asyncio.fro
+00000a10: 6d20 6461 7465 7469 6d65 2069 6d70 6f72  m datetime impor
+00000a20: 7420 6461 7465 0a0a 6672 6f6d 2061 696f  t date..from aio
+00000a30: 6874 7470 2069 6d70 6f72 7420 436c 6965  http import Clie
+00000a40: 6e74 5365 7373 696f 6e0a 0a66 726f 6d20  ntSession..from 
+00000a50: 6169 6f61 6d62 6965 6e74 2069 6d70 6f72  aioambient impor
+00000a60: 7420 4150 490a 0a0a 6173 796e 6320 6465  t API...async de
+00000a70: 6620 6d61 696e 2829 202d 3e20 4e6f 6e65  f main() -> None
+00000a80: 3a0a 2020 2020 2222 2243 7265 6174 6520  :.    """Create 
+00000a90: 7468 6520 6169 6f68 7474 7020 7365 7373  the aiohttp sess
+00000aa0: 696f 6e20 616e 6420 7275 6e20 7468 6520  ion and run the 
+00000ab0: 6578 616d 706c 652e 2222 220a 2020 2020  example.""".    
+00000ac0: 6170 6920 3d20 4150 4928 223c 594f 5552  api = API("<YOUR
+00000ad0: 2041 5050 4c49 4341 5449 4f4e 204b 4559   APPLICATION KEY
+00000ae0: 3e22 2c20 223c 594f 5552 2041 5049 204b  >", "<YOUR API K
+00000af0: 4559 3e22 290a 0a20 2020 2023 2047 6574  EY>")..    # Get
+00000b00: 2061 6c6c 2064 6576 6963 6573 2069 6e20   all devices in 
+00000b10: 616e 2061 6363 6f75 6e74 3a0a 2020 2020  an account:.    
+00000b20: 6177 6169 7420 6170 692e 6765 745f 6465  await api.get_de
+00000b30: 7669 6365 7328 290a 0a20 2020 2023 2047  vices()..    # G
+00000b40: 6574 2061 6c6c 2073 746f 7265 6420 7265  et all stored re
+00000b50: 6164 696e 6773 2066 726f 6d20 6120 6465  adings from a de
+00000b60: 7669 6365 3a0a 2020 2020 6177 6169 7420  vice:.    await 
+00000b70: 6170 692e 6765 745f 6465 7669 6365 5f64  api.get_device_d
+00000b80: 6574 6169 6c73 2822 3c44 4556 4943 4520  etails("<DEVICE 
+00000b90: 4d41 4320 4144 4452 4553 533e 2229 0a0a  MAC ADDRESS>")..
+00000ba0: 2020 2020 2320 4765 7420 616c 6c20 7374      # Get all st
+00000bb0: 6f72 6564 2072 6561 6469 6e67 7320 6672  ored readings fr
+00000bc0: 6f6d 2061 2064 6576 6963 6520 2873 7461  om a device (sta
+00000bd0: 7274 696e 6720 6174 2061 2064 6174 6574  rting at a datet
+00000be0: 696d 6529 3a0a 2020 2020 6177 6169 7420  ime):.    await 
+00000bf0: 6170 692e 6765 745f 6465 7669 6365 5f64  api.get_device_d
+00000c00: 6574 6169 6c73 2822 3c44 4556 4943 4520  etails("<DEVICE 
+00000c10: 4d41 4320 4144 4452 4553 533e 222c 2065  MAC ADDRESS>", e
+00000c20: 6e64 5f64 6174 653d 6461 7465 2832 3031  nd_date=date(201
+00000c30: 392c 2031 2c20 3136 2929 0a0a 0a61 7379  9, 1, 16))...asy
+00000c40: 6e63 696f 2e72 756e 286d 6169 6e28 2929  ncio.run(main())
+00000c50: 0a60 6060 0a0a 4279 2064 6566 6175 6c74  .```..By default
+00000c60: 2c20 7468 6520 6c69 6272 6172 7920 6372  , the library cr
+00000c70: 6561 7465 7320 6120 6e65 7720 636f 6e6e  eates a new conn
+00000c80: 6563 7469 6f6e 2074 6f20 416d 6269 656e  ection to Ambien
+00000c90: 7420 5765 6174 6865 7220 7769 7468 2065  t Weather with e
+00000ca0: 6163 6820 636f 726f 7574 696e 652e 0a49  ach coroutine..I
+00000cb0: 6620 796f 7520 6172 6520 6361 6c6c 696e  f you are callin
+00000cc0: 6720 6120 6c61 7267 6520 6e75 6d62 6572  g a large number
+00000cd0: 206f 6620 636f 726f 7574 696e 6573 2028   of coroutines (
+00000ce0: 6f72 206d 6572 656c 7920 7761 6e74 2074  or merely want t
+00000cf0: 6f20 7371 7565 657a 6520 6f75 7420 6576  o squeeze out ev
+00000d00: 6572 790a 7365 636f 6e64 206f 6620 7275  ery.second of ru
+00000d10: 6e74 696d 6520 7361 7669 6e67 7320 706f  ntime savings po
+00000d20: 7373 6962 6c65 292c 2061 6e20 5b60 6169  ssible), an [`ai
+00000d30: 6f68 7474 7060 5d5b 6169 6f68 7474 705d  ohttp`][aiohttp]
+00000d40: 2060 436c 6965 6e74 5365 7373 696f 6e60   `ClientSession`
+00000d50: 2063 616e 2062 6520 7573 6564 2066 6f72   can be used for
+00000d60: 0a63 6f6e 6e65 6374 696f 6e20 706f 6f6c  .connection pool
+00000d70: 696e 673a 0a0a 6060 6070 7974 686f 6e0a  ing:..```python.
+00000d80: 696d 706f 7274 2061 7379 6e63 696f 0a66  import asyncio.f
+00000d90: 726f 6d20 6461 7465 7469 6d65 2069 6d70  rom datetime imp
+00000da0: 6f72 7420 6461 7465 0a0a 6672 6f6d 2061  ort date..from a
+00000db0: 696f 6874 7470 2069 6d70 6f72 7420 436c  iohttp import Cl
+00000dc0: 6965 6e74 5365 7373 696f 6e0a 0a66 726f  ientSession..fro
+00000dd0: 6d20 6169 6f61 6d62 6965 6e74 2069 6d70  m aioambient imp
+00000de0: 6f72 7420 4150 490a 0a0a 6173 796e 6320  ort API...async 
+00000df0: 6465 6620 6d61 696e 2829 202d 3e20 4e6f  def main() -> No
+00000e00: 6e65 3a0a 2020 2020 2222 2243 7265 6174  ne:.    """Creat
+00000e10: 6520 7468 6520 6169 6f68 7474 7020 7365  e the aiohttp se
+00000e20: 7373 696f 6e20 616e 6420 7275 6e20 7468  ssion and run th
+00000e30: 6520 6578 616d 706c 652e 2222 220a 2020  e example.""".  
+00000e40: 2020 6173 796e 6320 7769 7468 2043 6c69    async with Cli
+00000e50: 656e 7453 6573 7369 6f6e 2829 2061 7320  entSession() as 
+00000e60: 7365 7373 696f 6e3a 0a20 2020 2020 2020  session:.       
+00000e70: 2061 7069 203d 2041 5049 2822 3c59 4f55   api = API("<YOU
+00000e80: 5220 4150 504c 4943 4154 494f 4e20 4b45  R APPLICATION KE
+00000e90: 593e 222c 2022 3c59 4f55 5220 4150 4920  Y>", "<YOUR API 
+00000ea0: 4b45 593e 2229 0a0a 2020 2020 2020 2020  KEY>")..        
+00000eb0: 2320 4765 7420 616c 6c20 6465 7669 6365  # Get all device
+00000ec0: 7320 696e 2061 6e20 6163 636f 756e 743a  s in an account:
+00000ed0: 0a20 2020 2020 2020 2061 7761 6974 2061  .        await a
+00000ee0: 7069 2e67 6574 5f64 6576 6963 6573 2829  pi.get_devices()
+00000ef0: 0a0a 2020 2020 2020 2020 2320 4765 7420  ..        # Get 
+00000f00: 616c 6c20 7374 6f72 6564 2072 6561 6469  all stored readi
+00000f10: 6e67 7320 6672 6f6d 2061 2064 6576 6963  ngs from a devic
+00000f20: 653a 0a20 2020 2020 2020 2061 7761 6974  e:.        await
+00000f30: 2061 7069 2e67 6574 5f64 6576 6963 655f   api.get_device_
+00000f40: 6465 7461 696c 7328 223c 4445 5649 4345  details("<DEVICE
+00000f50: 204d 4143 2041 4444 5245 5353 3e22 290a   MAC ADDRESS>").
+00000f60: 0a20 2020 2020 2020 2023 2047 6574 2061  .        # Get a
+00000f70: 6c6c 2073 746f 7265 6420 7265 6164 696e  ll stored readin
+00000f80: 6773 2066 726f 6d20 6120 6465 7669 6365  gs from a device
+00000f90: 2028 7374 6172 7469 6e67 2061 7420 6120   (starting at a 
+00000fa0: 6461 7465 7469 6d65 293a 0a20 2020 2020  datetime):.     
+00000fb0: 2020 2061 7761 6974 2061 7069 2e67 6574     await api.get
+00000fc0: 5f64 6576 6963 655f 6465 7461 696c 7328  _device_details(
+00000fd0: 223c 4445 5649 4345 204d 4143 2041 4444  "<DEVICE MAC ADD
+00000fe0: 5245 5353 3e22 2c20 656e 645f 6461 7465  RESS>", end_date
+00000ff0: 3d64 6174 6528 3230 3139 2c20 312c 2031  =date(2019, 1, 1
+00001000: 3629 290a 0a0a 6173 796e 6369 6f2e 7275  6))...asyncio.ru
+00001010: 6e28 6d61 696e 2829 290a 6060 600a 0a50  n(main()).```..P
+00001020: 6c65 6173 6520 6265 2061 7761 7265 206f  lease be aware o
+00001030: 6620 416d 6269 656e 7420 5765 6174 6865  f Ambient Weathe
+00001040: 7227 730a 5b72 6174 6520 6c69 6d69 7469  r's.[rate limiti
+00001050: 6e67 2070 6f6c 6963 6965 735d 5b61 6d62  ng policies][amb
+00001060: 6965 6e74 2d77 6561 7468 6572 2d72 6174  ient-weather-rat
+00001070: 652d 6c69 6d69 7469 6e67 5d2e 0a0a 2323  e-limiting]...##
+00001080: 2057 6562 736f 636b 6574 2041 5049 0a0a   Websocket API..
+00001090: 6060 6070 7974 686f 6e0a 696d 706f 7274  ```python.import
+000010a0: 2061 7379 6e63 696f 0a0a 6672 6f6d 2061   asyncio..from a
+000010b0: 696f 6874 7470 2069 6d70 6f72 7420 436c  iohttp import Cl
+000010c0: 6965 6e74 5365 7373 696f 6e0a 0a66 726f  ientSession..fro
+000010d0: 6d20 6169 6f61 6d62 6965 6e74 2069 6d70  m aioambient imp
+000010e0: 6f72 7420 5765 6273 6f63 6b65 740a 0a0a  ort Websocket...
+000010f0: 6173 796e 6320 6465 6620 6d61 696e 2829  async def main()
+00001100: 202d 3e20 4e6f 6e65 3a0a 2020 2020 2222   -> None:.    ""
+00001110: 2243 7265 6174 6520 7468 6520 6169 6f68  "Create the aioh
+00001120: 7474 7020 7365 7373 696f 6e20 616e 6420  ttp session and 
+00001130: 7275 6e20 7468 6520 6578 616d 706c 652e  run the example.
+00001140: 2222 220a 2020 2020 7765 6273 6f63 6b65  """.    websocke
+00001150: 7420 3d20 5765 6273 6f63 6b65 7428 223c  t = Websocket("<
+00001160: 594f 5552 2041 5050 4c49 4341 5449 4f4e  YOUR APPLICATION
+00001170: 204b 4559 3e22 2c20 223c 594f 5552 2041   KEY>", "<YOUR A
+00001180: 5049 204b 4559 3e22 290a 0a20 2020 2023  PI KEY>")..    #
+00001190: 204e 6f74 6520 7468 6174 2079 6f75 2063   Note that you c
+000011a0: 616e 2077 6174 6368 206d 756c 7469 706c  an watch multipl
+000011b0: 6520 4150 4920 6b65 7973 2061 7420 6f6e  e API keys at on
+000011c0: 6365 3a0a 2020 2020 7765 6273 6f63 6b65  ce:.    websocke
+000011d0: 7420 3d20 5765 6273 6f63 6b65 7428 2259  t = Websocket("Y
+000011e0: 4f55 5220 4150 504c 4943 4154 494f 4e20  OUR APPLICATION 
+000011f0: 4b45 5922 2c20 5b22 3c41 5049 204b 4559  KEY", ["<API KEY
+00001200: 2031 3e22 2c20 223c 4150 4920 4b45 5920   1>", "<API KEY 
+00001210: 323e 225d 290a 0a20 2020 2023 2044 6566  2>"])..    # Def
+00001220: 696e 6520 6120 6d65 7468 6f64 2074 6861  ine a method tha
+00001230: 7420 7368 6f75 6c64 2062 6520 6669 7265  t should be fire
+00001240: 6420 7768 656e 2074 6865 2077 6562 736f  d when the webso
+00001250: 636b 6574 2063 6c69 656e 740a 2020 2020  cket client.    
+00001260: 2320 636f 6e6e 6563 7473 3a0a 2020 2020  # connects:.    
+00001270: 6465 6620 636f 6e6e 6563 745f 6d65 7468  def connect_meth
+00001280: 6f64 2829 3a0a 2020 2020 2020 2020 2222  od():.        ""
+00001290: 2250 7269 6e74 2061 2073 696d 706c 6520  "Print a simple 
+000012a0: 2268 656c 6c6f 2220 6d65 7373 6167 652e  "hello" message.
+000012b0: 2222 220a 2020 2020 2020 2020 7072 696e  """.        prin
+000012c0: 7428 2243 6c69 656e 7420 6861 7320 636f  t("Client has co
+000012d0: 6e6e 6563 7465 6420 746f 2074 6865 2077  nnected to the w
+000012e0: 6562 736f 636b 6574 2229 0a0a 2020 2020  ebsocket")..    
+000012f0: 7765 6273 6f63 6b65 742e 6f6e 5f63 6f6e  websocket.on_con
+00001300: 6e65 6374 2863 6f6e 6e65 6374 5f6d 6574  nect(connect_met
+00001310: 686f 6429 0a0a 2020 2020 2320 416c 7465  hod)..    # Alte
+00001320: 726e 6174 6976 656c 792c 2064 6566 696e  rnatively, defin
+00001330: 6520 6120 636f 726f 7574 696e 6520 6861  e a coroutine ha
+00001340: 6e64 6c65 723a 0a20 2020 2061 7379 6e63  ndler:.    async
+00001350: 2064 6566 2063 6f6e 6e65 6374 5f63 6f72   def connect_cor
+00001360: 6f75 7469 6e65 2829 3a0a 2020 2020 2020  outine():.      
+00001370: 2020 2222 2257 6169 7473 2066 6f72 2033    """Waits for 3
+00001380: 2073 6563 6f6e 6473 2c20 7468 656e 2070   seconds, then p
+00001390: 7269 6e74 2061 2073 696d 706c 6520 2268  rint a simple "h
+000013a0: 656c 6c6f 2220 6d65 7373 6167 652e 2222  ello" message.""
+000013b0: 220a 2020 2020 2020 2020 6177 6169 7420  ".        await 
+000013c0: 6173 796e 6369 6f2e 736c 6565 7028 3329  asyncio.sleep(3)
+000013d0: 0a20 2020 2020 2020 2070 7269 6e74 2822  .        print("
+000013e0: 436c 6965 6e74 2068 6173 2063 6f6e 6e65  Client has conne
+000013f0: 6374 6564 2074 6f20 7468 6520 7765 6273  cted to the webs
+00001400: 6f63 6b65 7422 290a 0a20 2020 2077 6562  ocket")..    web
+00001410: 736f 636b 6574 2e61 7379 6e63 5f6f 6e5f  socket.async_on_
+00001420: 636f 6e6e 6563 7428 636f 6e6e 6563 745f  connect(connect_
+00001430: 636f 726f 7574 696e 6529 0a0a 2020 2020  coroutine)..    
+00001440: 2320 4465 6669 6e65 2061 206d 6574 686f  # Define a metho
+00001450: 6420 7468 6174 2073 686f 756c 6420 6265  d that should be
+00001460: 2072 756e 2075 706f 6e20 7375 6273 6372   run upon subscr
+00001470: 6962 696e 6720 746f 2074 6865 2041 6d62  ibing to the Amb
+00001480: 6965 6e74 0a20 2020 2023 2057 6561 7468  ient.    # Weath
+00001490: 6572 2063 6c6f 7564 3a0a 2020 2020 6465  er cloud:.    de
+000014a0: 6620 7375 6273 6372 6962 6564 5f6d 6574  f subscribed_met
+000014b0: 686f 6428 6461 7461 293a 0a20 2020 2020  hod(data):.     
+000014c0: 2020 2022 2222 5072 696e 7420 7468 6520     """Print the 
+000014d0: 6461 7461 2072 6563 6569 7665 6420 7570  data received up
+000014e0: 6f6e 2073 7562 7363 7269 6269 6e67 2e22  on subscribing."
+000014f0: 2222 0a20 2020 2020 2020 2070 7269 6e74  "".        print
+00001500: 2866 2253 7562 7363 7269 7074 696f 6e20  (f"Subscription 
+00001510: 6461 7461 2072 6563 6569 7665 643a 207b  data received: {
+00001520: 6461 7461 7d22 290a 0a20 2020 2077 6562  data}")..    web
+00001530: 736f 636b 6574 2e6f 6e5f 7375 6273 6372  socket.on_subscr
+00001540: 6962 6564 2873 7562 7363 7269 6265 645f  ibed(subscribed_
+00001550: 6d65 7468 6f64 290a 0a20 2020 2023 2041  method)..    # A
+00001560: 6c74 6572 6e61 7469 7665 6c79 2c20 6465  lternatively, de
+00001570: 6669 6e65 2061 2063 6f72 6f75 7469 6e65  fine a coroutine
+00001580: 2068 616e 646c 6572 3a0a 2020 2020 6173   handler:.    as
+00001590: 796e 6320 6465 6620 7375 6273 6372 6962  ync def subscrib
+000015a0: 6564 5f63 6f72 6f75 7469 6e65 2864 6174  ed_coroutine(dat
+000015b0: 6129 3a0a 2020 2020 2020 2020 2222 2257  a):.        """W
+000015c0: 6169 7473 2066 6f72 2033 2073 6563 6f6e  aits for 3 secon
+000015d0: 6473 2c20 7468 656e 2070 7269 6e74 2074  ds, then print t
+000015e0: 6865 2069 6e63 6f6d 696e 6720 6461 7461  he incoming data
+000015f0: 2e22 2222 0a20 2020 2020 2020 2061 7761  .""".        awa
+00001600: 6974 2061 7379 6e63 696f 2e73 6c65 6570  it asyncio.sleep
+00001610: 2833 290a 2020 2020 2020 2020 7072 696e  (3).        prin
+00001620: 7428 6622 5375 6273 6372 6970 7469 6f6e  t(f"Subscription
+00001630: 2064 6174 6120 7265 6365 6976 6564 3a20   data received: 
+00001640: 7b64 6174 617d 2229 0a0a 2020 2020 7765  {data}")..    we
+00001650: 6273 6f63 6b65 742e 6173 796e 635f 6f6e  bsocket.async_on
+00001660: 5f73 7562 7363 7269 6265 6428 7375 6273  _subscribed(subs
+00001670: 6372 6962 6564 5f63 6f72 6f75 7469 6e65  cribed_coroutine
+00001680: 290a 0a20 2020 2023 2044 6566 696e 6520  )..    # Define 
+00001690: 6120 6d65 7468 6f64 2074 6861 7420 7368  a method that sh
+000016a0: 6f75 6c64 2062 6520 7275 6e20 7570 6f6e  ould be run upon
+000016b0: 2072 6563 6569 7669 6e67 2064 6174 613a   receiving data:
+000016c0: 0a20 2020 2064 6566 2064 6174 615f 6d65  .    def data_me
+000016d0: 7468 6f64 2864 6174 6129 3a0a 2020 2020  thod(data):.    
+000016e0: 2020 2020 2222 2250 7269 6e74 2074 6865      """Print the
+000016f0: 2064 6174 6120 7265 6365 6976 6564 2e22   data received."
+00001700: 2222 0a20 2020 2020 2020 2070 7269 6e74  "".        print
+00001710: 2866 2244 6174 6120 7265 6365 6976 6564  (f"Data received
+00001720: 3a20 7b64 6174 617d 2229 0a0a 2020 2020  : {data}")..    
+00001730: 7765 6273 6f63 6b65 742e 6f6e 5f64 6174  websocket.on_dat
+00001740: 6128 6461 7461 5f6d 6574 686f 6429 0a0a  a(data_method)..
+00001750: 2020 2020 2320 416c 7465 726e 6174 6976      # Alternativ
+00001760: 656c 792c 2064 6566 696e 6520 6120 636f  ely, define a co
+00001770: 726f 7574 696e 6520 6861 6e64 6c65 723a  routine handler:
+00001780: 0a20 2020 2061 7379 6e63 2064 6566 2064  .    async def d
+00001790: 6174 615f 636f 726f 7574 696e 6528 6461  ata_coroutine(da
+000017a0: 7461 293a 0a20 2020 2020 2020 2022 2222  ta):.        """
+000017b0: 5761 6974 2066 6f72 2033 2073 6563 6f6e  Wait for 3 secon
+000017c0: 6473 2c20 7468 656e 2070 7269 6e74 2074  ds, then print t
+000017d0: 6865 2064 6174 6120 7265 6365 6976 6564  he data received
+000017e0: 2e22 2222 0a20 2020 2020 2020 2061 7761  .""".        awa
+000017f0: 6974 2061 7379 6e63 696f 2e73 6c65 6570  it asyncio.sleep
+00001800: 2833 290a 2020 2020 2020 2020 7072 696e  (3).        prin
+00001810: 7428 6622 4461 7461 2072 6563 6569 7665  t(f"Data receive
+00001820: 643a 207b 6461 7461 7d22 290a 0a20 2020  d: {data}")..   
+00001830: 2077 6562 736f 636b 6574 2e61 7379 6e63   websocket.async
+00001840: 5f6f 6e5f 6461 7461 2864 6174 615f 636f  _on_data(data_co
+00001850: 726f 7574 696e 6529 0a0a 2020 2020 2320  routine)..    # 
+00001860: 4465 6669 6e65 2061 206d 6574 686f 6420  Define a method 
+00001870: 7468 6174 2073 686f 756c 6420 6265 2072  that should be r
+00001880: 756e 2077 6865 6e20 7468 6520 7765 6273  un when the webs
+00001890: 6f63 6b65 7420 636c 6965 6e74 0a20 2020  ocket client.   
+000018a0: 2023 2064 6973 636f 6e6e 6563 7473 3a0a   # disconnects:.
+000018b0: 2020 2020 6465 6620 6469 7363 6f6e 6e65      def disconne
+000018c0: 6374 5f6d 6574 686f 6428 6461 7461 293a  ct_method(data):
+000018d0: 0a20 2020 2020 2020 2022 2222 5072 696e  .        """Prin
+000018e0: 7420 6120 7369 6d70 6c65 2022 676f 6f64  t a simple "good
+000018f0: 6279 6522 206d 6573 7361 6765 2e22 2222  bye" message."""
+00001900: 0a20 2020 2020 2020 2070 7269 6e74 2822  .        print("
+00001910: 436c 6965 6e74 2068 6173 2064 6973 636f  Client has disco
+00001920: 6e6e 6563 7465 6420 6672 6f6d 2074 6865  nnected from the
+00001930: 2077 6562 736f 636b 6574 2229 0a0a 2020   websocket")..  
+00001940: 2020 7765 6273 6f63 6b65 742e 6f6e 5f64    websocket.on_d
+00001950: 6973 636f 6e6e 6563 7428 6469 7363 6f6e  isconnect(discon
+00001960: 6e65 6374 5f6d 6574 686f 6429 0a0a 2020  nect_method)..  
+00001970: 2020 2320 416c 7465 726e 6174 6976 656c    # Alternativel
+00001980: 792c 2064 6566 696e 6520 6120 636f 726f  y, define a coro
+00001990: 7574 696e 6520 6861 6e64 6c65 723a 0a20  utine handler:. 
+000019a0: 2020 2061 7379 6e63 2064 6566 2064 6973     async def dis
+000019b0: 636f 6e6e 6563 745f 636f 726f 7574 696e  connect_coroutin
+000019c0: 6528 6461 7461 293a 0a20 2020 2020 2020  e(data):.       
+000019d0: 2022 2222 5761 6974 2066 6f72 2033 2073   """Wait for 3 s
+000019e0: 6563 6f6e 6473 2c20 7468 656e 2070 7269  econds, then pri
+000019f0: 6e74 2061 2073 696d 706c 6520 2267 6f6f  nt a simple "goo
+00001a00: 6462 7965 2220 6d65 7373 6167 652e 2222  dbye" message.""
+00001a10: 220a 2020 2020 2020 2020 6177 6169 7420  ".        await 
+00001a20: 6173 796e 6369 6f2e 736c 6565 7028 3329  asyncio.sleep(3)
+00001a30: 0a20 2020 2020 2020 2070 7269 6e74 2822  .        print("
+00001a40: 436c 6965 6e74 2068 6173 2064 6973 636f  Client has disco
+00001a50: 6e6e 6563 7465 6420 6672 6f6d 2074 6865  nnected from the
+00001a60: 2077 6562 736f 636b 6574 2229 0a0a 2020   websocket")..  
+00001a70: 2020 7765 6273 6f63 6b65 742e 6173 796e    websocket.asyn
+00001a80: 635f 6f6e 5f64 6973 636f 6e6e 6563 7428  c_on_disconnect(
+00001a90: 6469 7363 6f6e 6e65 6374 5f63 6f72 6f75  disconnect_corou
+00001aa0: 7469 6e65 290a 0a20 2020 2023 2043 6f6e  tine)..    # Con
+00001ab0: 6e65 6374 2074 6f20 7468 6520 7765 6273  nect to the webs
+00001ac0: 6f63 6b65 743a 0a20 2020 2061 7761 6974  ocket:.    await
+00001ad0: 2077 6562 736f 636b 6574 2e63 6f6e 6e65   websocket.conne
+00001ae0: 6374 2829 0a0a 2020 2020 2320 4174 2061  ct()..    # At a
+00001af0: 6e79 2070 6f69 6e74 2c20 6469 7363 6f6e  ny point, discon
+00001b00: 6e65 6374 2066 726f 6d20 7468 6520 7765  nect from the we
+00001b10: 6273 6f63 6b65 743a 0a20 2020 2061 7761  bsocket:.    awa
+00001b20: 6974 2077 6562 736f 636b 6574 2e64 6973  it websocket.dis
+00001b30: 636f 6e6e 6563 7428 290a 0a0a 6173 796e  connect()...asyn
+00001b40: 6369 6f2e 7275 6e28 6d61 696e 2829 290a  cio.run(main()).
+00001b50: 6060 600a 0a23 2043 6f6e 7472 6962 7574  ```..# Contribut
+00001b60: 696e 670a 0a54 6861 6e6b 7320 746f 2061  ing..Thanks to a
+00001b70: 6c6c 206f 6620 5b6f 7572 2063 6f6e 7472  ll of [our contr
+00001b80: 6962 7574 6f72 735d 5b63 6f6e 7472 6962  ibutors][contrib
+00001b90: 7574 6f72 735d 2073 6f20 6661 7221 0a0a  utors] so far!..
+00001ba0: 312e 205b 4368 6563 6b20 666f 7220 6f70  1. [Check for op
+00001bb0: 656e 2066 6561 7475 7265 732f 6275 6773  en features/bugs
+00001bc0: 5d5b 6973 7375 6573 5d20 6f72 205b 696e  ][issues] or [in
+00001bd0: 6974 6961 7465 2061 2064 6973 6375 7373  itiate a discuss
+00001be0: 696f 6e20 6f6e 206f 6e65 5d5b 6e65 772d  ion on one][new-
+00001bf0: 6973 7375 655d 2e0a 322e 205b 466f 726b  issue]..2. [Fork
+00001c00: 2074 6865 2072 6570 6f73 6974 6f72 795d   the repository]
+00001c10: 5b66 6f72 6b5d 2e0a 332e 2028 5f6f 7074  [fork]..3. (_opt
+00001c20: 696f 6e61 6c2c 2062 7574 2068 6967 686c  ional, but highl
+00001c30: 7920 7265 636f 6d6d 656e 6465 645f 2920  y recommended_) 
+00001c40: 4372 6561 7465 2061 2076 6972 7475 616c  Create a virtual
+00001c50: 2065 6e76 6972 6f6e 6d65 6e74 3a20 6070   environment: `p
+00001c60: 7974 686f 6e33 202d 6d20 7665 6e76 202e  ython3 -m venv .
+00001c70: 7665 6e76 600a 342e 2028 5f6f 7074 696f  venv`.4. (_optio
+00001c80: 6e61 6c2c 2062 7574 2068 6967 686c 7920  nal, but highly 
+00001c90: 7265 636f 6d6d 656e 6465 645f 2920 456e  recommended_) En
+00001ca0: 7465 7220 7468 6520 7669 7274 7561 6c20  ter the virtual 
+00001cb0: 656e 7669 726f 6e6d 656e 743a 2060 736f  environment: `so
+00001cc0: 7572 6365 202e 2f2e 7665 6e76 2f62 696e  urce ./.venv/bin
+00001cd0: 2f61 6374 6976 6174 6560 0a35 2e20 496e  /activate`.5. In
+00001ce0: 7374 616c 6c20 7468 6520 6465 7620 656e  stall the dev en
+00001cf0: 7669 726f 6e6d 656e 743a 2060 7363 7269  vironment: `scri
+00001d00: 7074 2f73 6574 7570 600a 362e 2043 6f64  pt/setup`.6. Cod
+00001d10: 6520 796f 7572 206e 6577 2066 6561 7475  e your new featu
+00001d20: 7265 206f 7220 6275 6720 6669 7820 6f6e  re or bug fix on
+00001d30: 2061 206e 6577 2062 7261 6e63 682e 0a37   a new branch..7
+00001d40: 2e20 5772 6974 6520 7465 7374 7320 7468  . Write tests th
+00001d50: 6174 2063 6f76 6572 2079 6f75 7220 6e65  at cover your ne
+00001d60: 7720 6675 6e63 7469 6f6e 616c 6974 792e  w functionality.
+00001d70: 0a38 2e20 5275 6e20 7465 7374 7320 616e  .8. Run tests an
+00001d80: 6420 656e 7375 7265 2031 3030 2520 636f  d ensure 100% co
+00001d90: 6465 2063 6f76 6572 6167 653a 2060 706f  de coverage: `po
+00001da0: 6574 7279 2072 756e 2070 7974 6573 7420  etry run pytest 
+00001db0: 2d2d 636f 7620 6169 6f61 6d62 6965 6e74  --cov aioambient
+00001dc0: 2074 6573 7473 600a 392e 2055 7064 6174   tests`.9. Updat
+00001dd0: 6520 6052 4541 444d 452e 6d64 6020 7769  e `README.md` wi
+00001de0: 7468 2061 6e79 206e 6577 2064 6f63 756d  th any new docum
+00001df0: 656e 7461 7469 6f6e 2e0a 3130 2e20 5375  entation..10. Su
+00001e00: 626d 6974 2061 2070 756c 6c20 7265 7175  bmit a pull requ
+00001e10: 6573 7421 0a0a 5b61 696f 6874 7470 5d3a  est!..[aiohttp]:
+00001e20: 2068 7474 7073 3a2f 2f67 6974 6875 622e   https://github.
+00001e30: 636f 6d2f 6169 6f2d 6c69 6273 2f61 696f  com/aio-libs/aio
+00001e40: 6874 7470 0a5b 616d 6269 656e 742d 7765  http.[ambient-we
+00001e50: 6174 6865 722d 6461 7368 626f 6172 645d  ather-dashboard]
+00001e60: 3a20 6874 7470 733a 2f2f 6461 7368 626f  : https://dashbo
+00001e70: 6172 642e 616d 6269 656e 7477 6561 7468  ard.ambientweath
+00001e80: 6572 2e6e 6574 0a5b 616d 6269 656e 742d  er.net.[ambient-
+00001e90: 7765 6174 6865 722d 7261 7465 2d6c 696d  weather-rate-lim
+00001ea0: 6974 696e 675d 3a20 6874 7470 733a 2f2f  iting]: https://
+00001eb0: 616d 6269 656e 7477 6561 7468 6572 2e64  ambientweather.d
+00001ec0: 6f63 732e 6170 6961 7279 2e69 6f2f 2369  ocs.apiary.io/#i
+00001ed0: 6e74 726f 6475 6374 696f 6e2f 7261 7465  ntroduction/rate
+00001ee0: 2d6c 696d 6974 696e 670a 5b61 6d62 6965  -limiting.[ambie
+00001ef0: 6e74 2d77 6561 7468 6572 5d3a 2068 7474  nt-weather]: htt
+00001f00: 7073 3a2f 2f61 6d62 6965 6e74 7765 6174  ps://ambientweat
+00001f10: 6865 722e 6e65 740a 5b63 692d 6261 6467  her.net.[ci-badg
+00001f20: 655d 3a20 6874 7470 733a 2f2f 6769 7468  e]: https://gith
+00001f30: 7562 2e63 6f6d 2f62 6163 6879 612f 6169  ub.com/bachya/ai
+00001f40: 6f61 6d62 6965 6e74 2f77 6f72 6b66 6c6f  oambient/workflo
+00001f50: 7773 2f43 492f 6261 6467 652e 7376 670a  ws/CI/badge.svg.
+00001f60: 5b63 695d 3a20 6874 7470 733a 2f2f 6769  [ci]: https://gi
+00001f70: 7468 7562 2e63 6f6d 2f62 6163 6879 612f  thub.com/bachya/
+00001f80: 6169 6f61 6d62 6965 6e74 2f61 6374 696f  aioambient/actio
+00001f90: 6e73 0a5b 636f 6465 636f 762d 6261 6467  ns.[codecov-badg
+00001fa0: 655d 3a20 6874 7470 733a 2f2f 636f 6465  e]: https://code
+00001fb0: 636f 762e 696f 2f67 682f 6261 6368 7961  cov.io/gh/bachya
+00001fc0: 2f61 696f 616d 6269 656e 742f 6272 616e  /aioambient/bran
+00001fd0: 6368 2f64 6576 2f67 7261 7068 2f62 6164  ch/dev/graph/bad
+00001fe0: 6765 2e73 7667 0a5b 636f 6465 636f 765d  ge.svg.[codecov]
+00001ff0: 3a20 6874 7470 733a 2f2f 636f 6465 636f  : https://codeco
+00002000: 762e 696f 2f67 682f 6261 6368 7961 2f61  v.io/gh/bachya/a
+00002010: 696f 616d 6269 656e 740a 5b63 6f6e 7472  ioambient.[contr
+00002020: 6962 7574 6f72 735d 3a20 6874 7470 733a  ibutors]: https:
+00002030: 2f2f 6769 7468 7562 2e63 6f6d 2f62 6163  //github.com/bac
+00002040: 6879 612f 6169 6f61 6d62 6965 6e74 2f67  hya/aioambient/g
+00002050: 7261 7068 732f 636f 6e74 7269 6275 746f  raphs/contributo
+00002060: 7273 0a5b 666f 726b 5d3a 2068 7474 7073  rs.[fork]: https
+00002070: 3a2f 2f67 6974 6875 622e 636f 6d2f 6261  ://github.com/ba
+00002080: 6368 7961 2f61 696f 616d 6269 656e 742f  chya/aioambient/
+00002090: 666f 726b 0a5b 6973 7375 6573 5d3a 2068  fork.[issues]: h
+000020a0: 7474 7073 3a2f 2f67 6974 6875 622e 636f  ttps://github.co
+000020b0: 6d2f 6261 6368 7961 2f61 696f 616d 6269  m/bachya/aioambi
+000020c0: 656e 742f 6973 7375 6573 0a5b 6c69 6365  ent/issues.[lice
+000020d0: 6e73 652d 6261 6467 655d 3a20 6874 7470  nse-badge]: http
+000020e0: 733a 2f2f 696d 672e 7368 6965 6c64 732e  s://img.shields.
+000020f0: 696f 2f70 7970 692f 6c2f 6169 6f61 6d62  io/pypi/l/aioamb
+00002100: 6965 6e74 2e73 7667 0a5b 6c69 6365 6e73  ient.svg.[licens
+00002110: 655d 3a20 6874 7470 733a 2f2f 6769 7468  e]: https://gith
+00002120: 7562 2e63 6f6d 2f62 6163 6879 612f 6169  ub.com/bachya/ai
+00002130: 6f61 6d62 6965 6e74 2f62 6c6f 622f 6d61  oambient/blob/ma
+00002140: 696e 2f4c 4943 454e 5345 0a5b 6d61 696e  in/LICENSE.[main
+00002150: 7461 696e 6162 696c 6974 792d 6261 6467  tainability-badg
+00002160: 655d 3a20 6874 7470 733a 2f2f 6170 692e  e]: https://api.
+00002170: 636f 6465 636c 696d 6174 652e 636f 6d2f  codeclimate.com/
+00002180: 7631 2f62 6164 6765 732f 3831 6139 6638  v1/badges/81a9f8
+00002190: 3237 3461 6266 3332 3562 3266 6134 2f6d  274abf325b2fa4/m
+000021a0: 6169 6e74 6169 6e61 6269 6c69 7479 0a5b  aintainability.[
+000021b0: 6d61 696e 7461 696e 6162 696c 6974 795d  maintainability]
+000021c0: 3a20 6874 7470 733a 2f2f 636f 6465 636c  : https://codecl
+000021d0: 696d 6174 652e 636f 6d2f 6769 7468 7562  imate.com/github
+000021e0: 2f62 6163 6879 612f 6169 6f61 6d62 6965  /bachya/aioambie
+000021f0: 6e74 2f6d 6169 6e74 6169 6e61 6269 6c69  nt/maintainabili
+00002200: 7479 0a5b 6e65 772d 6973 7375 655d 3a20  ty.[new-issue]: 
+00002210: 6874 7470 733a 2f2f 6769 7468 7562 2e63  https://github.c
+00002220: 6f6d 2f62 6163 6879 612f 6169 6f61 6d62  om/bachya/aioamb
+00002230: 6965 6e74 2f69 7373 7565 732f 6e65 770a  ient/issues/new.
+00002240: 5b6e 6577 2d69 7373 7565 5d3a 2068 7474  [new-issue]: htt
+00002250: 7073 3a2f 2f67 6974 6875 622e 636f 6d2f  ps://github.com/
+00002260: 6261 6368 7961 2f61 696f 616d 6269 656e  bachya/aioambien
+00002270: 742f 6973 7375 6573 2f6e 6577 0a5b 7079  t/issues/new.[py
+00002280: 7069 2d62 6164 6765 5d3a 2068 7474 7073  pi-badge]: https
+00002290: 3a2f 2f69 6d67 2e73 6869 656c 6473 2e69  ://img.shields.i
+000022a0: 6f2f 7079 7069 2f76 2f61 696f 616d 6269  o/pypi/v/aioambi
+000022b0: 656e 742e 7376 670a 5b70 7970 695d 3a20  ent.svg.[pypi]: 
+000022c0: 6874 7470 733a 2f2f 7079 7069 2e70 7974  https://pypi.pyt
+000022d0: 686f 6e2e 6f72 672f 7079 7069 2f61 696f  hon.org/pypi/aio
+000022e0: 616d 6269 656e 740a 5b76 6572 7369 6f6e  ambient.[version
+000022f0: 2d62 6164 6765 5d3a 2068 7474 7073 3a2f  -badge]: https:/
+00002300: 2f69 6d67 2e73 6869 656c 6473 2e69 6f2f  /img.shields.io/
+00002310: 7079 7069 2f70 7976 6572 7369 6f6e 732f  pypi/pyversions/
+00002320: 6169 6f61 6d62 6965 6e74 2e73 7667 0a5b  aioambient.svg.[
+00002330: 7665 7273 696f 6e5d 3a20 6874 7470 733a  version]: https:
+00002340: 2f2f 7079 7069 2e70 7974 686f 6e2e 6f72  //pypi.python.or
+00002350: 672f 7079 7069 2f61 696f 616d 6269 656e  g/pypi/aioambien
+00002360: 740a 0a                                  t..
```

