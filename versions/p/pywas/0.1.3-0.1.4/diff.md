# Comparing `tmp/pywas-0.1.3.tar.gz` & `tmp/pywas-0.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pywas-0.1.3.tar", max compression
+gzip compressed data, was "pywas-0.1.4.tar", max compression
```

## Comparing `pywas-0.1.3.tar` & `pywas-0.1.4.tar`

### file list

```diff
@@ -1,19 +1,19 @@
--rw-r--r--   0        0        0     1047 2023-04-03 10:10:37.028428 pywas-0.1.3/pyproject.toml
--rw-r--r--   0        0        0        0 2023-02-16 13:16:09.383160 pywas-0.1.3/pywas/__init__.py
--rw-r--r--   0        0        0      454 2023-02-21 07:49:57.976013 pywas-0.1.3/pywas/main.py
--rw-r--r--   0        0        0       33 2023-02-16 13:16:09.385162 pywas-0.1.3/pywas/parse/__init__.py
--rw-r--r--   0        0        0      196 2023-02-21 07:47:28.837685 pywas-0.1.3/pywas/parse/__pycache__/__init__.cpython-39.pyc
--rw-r--r--   0        0        0     1031 2023-03-29 14:50:32.053036 pywas-0.1.3/pywas/parse/__pycache__/results.cpython-39.pyc
--rw-r--r--   0        0        0      529 2023-03-29 14:49:51.622875 pywas-0.1.3/pywas/parse/results.py
--rw-r--r--   0        0        0     1444 2023-02-16 13:16:09.386163 pywas-0.1.3/pywas/parse/spice3raw.py
--rw-r--r--   0        0        0      821 2022-12-15 08:47:48.745278 pywas-0.1.3/pywas/template/char_mos.net
--rw-r--r--   0        0        0       18 2023-02-16 13:16:09.387164 pywas-0.1.3/pywas/wrapper/__init__.py
--rw-r--r--   0        0        0      172 2023-02-21 07:47:28.521501 pywas-0.1.3/pywas/wrapper/__pycache__/__init__.cpython-39.pyc
--rw-r--r--   0        0        0     3111 2023-03-07 14:27:10.950734 pywas-0.1.3/pywas/wrapper/__pycache__/base_wrapper.cpython-39.pyc
--rw-r--r--   0        0        0     2881 2023-03-07 14:27:10.734579 pywas-0.1.3/pywas/wrapper/__pycache__/ngspice.cpython-39.pyc
--rw-r--r--   0        0        0     2982 2023-03-07 14:18:47.865175 pywas-0.1.3/pywas/wrapper/base_wrapper.py
--rw-r--r--   0        0        0     3194 2023-03-07 14:18:47.866179 pywas-0.1.3/pywas/wrapper/ngspice.py
--rw-r--r--   0        0        0       90 2023-02-22 15:53:11.871477 pywas-0.1.3/pywas/wrapper/template.py
--rw-r--r--   0        0        0     1555 2023-04-03 10:02:56.385819 pywas-0.1.3/README.md
--rw-r--r--   0        0        0     2476 1970-01-01 00:00:00.000000 pywas-0.1.3/setup.py
--rw-r--r--   0        0        0     2210 1970-01-01 00:00:00.000000 pywas-0.1.3/PKG-INFO
+-rw-r--r--   0        0        0      922 2023-04-06 12:37:52.275409 pywas-0.1.4/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-02-16 13:16:09.383160 pywas-0.1.4/pywas/__init__.py
+-rw-r--r--   0        0        0      518 2023-04-06 12:34:13.121225 pywas-0.1.4/pywas/main.py
+-rw-r--r--   0        0        0       33 2023-02-16 13:16:09.385162 pywas-0.1.4/pywas/parse/__init__.py
+-rw-r--r--   0        0        0      196 2023-02-21 07:47:28.837685 pywas-0.1.4/pywas/parse/__pycache__/__init__.cpython-39.pyc
+-rw-r--r--   0        0        0     1031 2023-03-29 14:50:32.053036 pywas-0.1.4/pywas/parse/__pycache__/results.cpython-39.pyc
+-rw-r--r--   0        0        0      529 2023-03-29 14:49:51.622875 pywas-0.1.4/pywas/parse/results.py
+-rw-r--r--   0        0        0     1444 2023-02-16 13:16:09.386163 pywas-0.1.4/pywas/parse/spice3raw.py
+-rw-r--r--   0        0        0      821 2022-12-15 08:47:48.745278 pywas-0.1.4/pywas/template/char_mos.net
+-rw-r--r--   0        0        0       18 2023-02-16 13:16:09.387164 pywas-0.1.4/pywas/wrapper/__init__.py
+-rw-r--r--   0        0        0      172 2023-02-21 07:47:28.521501 pywas-0.1.4/pywas/wrapper/__pycache__/__init__.cpython-39.pyc
+-rw-r--r--   0        0        0     3155 2023-04-06 12:22:51.004591 pywas-0.1.4/pywas/wrapper/__pycache__/base_wrapper.cpython-39.pyc
+-rw-r--r--   0        0        0     2881 2023-03-07 14:27:10.734579 pywas-0.1.4/pywas/wrapper/__pycache__/ngspice.cpython-39.pyc
+-rw-r--r--   0        0        0     3026 2023-04-06 12:22:49.248412 pywas-0.1.4/pywas/wrapper/base_wrapper.py
+-rw-r--r--   0        0        0     3194 2023-03-07 14:18:47.866179 pywas-0.1.4/pywas/wrapper/ngspice.py
+-rw-r--r--   0        0        0       90 2023-02-22 15:53:11.871477 pywas-0.1.4/pywas/wrapper/template.py
+-rw-r--r--   0        0        0     1744 2023-04-06 12:34:13.121225 pywas-0.1.4/README.md
+-rw-r--r--   0        0        0     2646 1970-01-01 00:00:00.000000 pywas-0.1.4/setup.py
+-rw-r--r--   0        0        0     2363 1970-01-01 00:00:00.000000 pywas-0.1.4/PKG-INFO
```

### Comparing `pywas-0.1.3/pyproject.toml` & `pywas-0.1.4/pyproject.toml`

 * *Files 23% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "pywas"
-version = "0.1.3"
+version = "0.1.4"
 description = ""
 authors = ["Patarimi <mpqqch@gmail.com>"]
 readme = "README.md"
 
 [tool.poetry.scripts]
 pywas = "pywas.main:cli"
 
@@ -12,32 +12,28 @@
 doc         = "typer pywas.main utils docs --name pyWAS --output README.md"
 show-update = "poetry show -l -o"
 lock-req    = "poetry export -o requirements.txt --without-hashes"
 publish     = "poetry publish --build --username __token__ --password $PYPI_TOKEN"
 
 [tool.poetry.dependencies]
 python = "^3.8"
-fastapi-jsonrpc = "^2.2.0"
-uvicorn = {extras = ["standard"], version = "^0.20.0"}
 typer = "^0.7.0"
 h5py = "^3.7.0"
 numpy = "^1.23.2"
 jinja2 = "^3.1.2"
 wget = "^3.2"
 pyyaml = "^6.0"
+rich = "^13.3.3"
+pydantic = "^1.10.7"
 
 
 [tool.poetry.group.dev.dependencies]
 pytest = "^7.2.0"
 black = "^23.1.0"
 pre-commit = "^3.1.1"
 tox = "^4.0.0"
 typer-cli = "^0.0.13"
 poethepoet = "^0.19.0"
 
-[tool.poetry.group.em-sim.dependencies]
-tidy3d = "^1.8.2"
-gdstk = "^0.9.35"
-
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
```

### Comparing `pywas-0.1.3/pywas/parse/__pycache__/results.cpython-39.pyc` & `pywas-0.1.4/pywas/parse/__pycache__/results.cpython-39.pyc`

 * *Files identical despite different names*

### Comparing `pywas-0.1.3/pywas/parse/results.py` & `pywas-0.1.4/pywas/parse/results.py`

 * *Files identical despite different names*

### Comparing `pywas-0.1.3/pywas/parse/spice3raw.py` & `pywas-0.1.4/pywas/parse/spice3raw.py`

 * *Files identical despite different names*

### Comparing `pywas-0.1.3/pywas/template/char_mos.net` & `pywas-0.1.4/pywas/template/char_mos.net`

 * *Files identical despite different names*

### Comparing `pywas-0.1.3/pywas/wrapper/__pycache__/base_wrapper.cpython-39.pyc` & `pywas-0.1.4/pywas/wrapper/__pycache__/base_wrapper.cpython-39.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.9, timestamp-based, .py timestamp: Tue Mar  7 14:18:47 2023 UTC, .py size: 2982 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 21% similar despite different names*

```diff
@@ -1,195 +1,198 @@
-00000000: 610d 0d0a 0000 0000 c747 0764 a60b 0000  a........G.d....
+00000000: 610d 0d0a 0000 0000 99b9 2e64 d20b 0000  a..........d....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 0004 0000 0040 0000 0073 d800 0000 6400  .....@...s....d.
+00000020: 0004 0000 0040 0000 0073 e400 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 5a02 6401 6403 6c03  Z.d.d.l.Z.d.d.l.
 00000040: 6d04 5a04 6d05 5a05 6d06 5a06 0100 6401  m.Z.m.Z.m.Z...d.
 00000050: 6404 6c07 6d08 5a08 0100 6401 6405 6c09  d.l.m.Z...d.d.l.
 00000060: 6d0a 5a0a 6d0b 5a0b 6d0c 5a0c 0100 6401  m.Z.m.Z.m.Z...d.
 00000070: 6402 6c0d 5a0d 6401 6406 6c0e 6d0f 5a0f  d.l.Z.d.d.l.m.Z.
 00000080: 0100 6401 6402 6c10 5a10 6401 6407 6c0d  ..d.d.l.Z.d.d.l.
 00000090: 6d11 5a11 0100 6401 6402 6c12 5a12 6401  m.Z...d.d.l.Z.d.
-000000a0: 6408 6c02 6d13 5a13 0100 4700 6409 640a  d.l.m.Z...G.d.d.
-000000b0: 8400 640a 6504 8303 5a14 6513 8300 9b00  ..d.e...Z.e.....
-000000c0: 640b 9d02 6601 6505 6515 640c 9c02 640d  d...f.e.e.d...d.
-000000d0: 640e 8405 5a16 6513 8300 9b00 640b 9d02  d...Z.e.....d...
-000000e0: 6601 6515 6505 640f 9c02 6410 6411 8405  f.e.e.d...d.d...
-000000f0: 5a17 6518 6402 6412 9c02 6413 6414 8404  Z.e.d.d...d.d...
-00000100: 5a19 6402 5300 2915 7a20 0a42 6173 6520  Z.d.S.).z .Base 
-00000110: 636c 6173 7320 666f 7220 7370 6963 6520  class for spice 
-00000120: 7369 6d75 6c61 746f 720a e900 0000 004e  simulator......N
-00000130: 2903 da09 4261 7365 4d6f 6465 6cda 0846  )...BaseModel..F
-00000140: 696c 6550 6174 68da 0d44 6972 6563 746f  ilePath..Directo
-00000150: 7279 5061 7468 2901 da04 456e 756d 2903  ryPath)...Enum).
-00000160: da04 4c69 7374 da08 4f70 7469 6f6e 616c  ..List..Optional
-00000170: da08 4361 6c6c 6162 6c65 2901 da0a 5265  ..Callable)...Re
-00000180: 7375 6c74 4469 6374 2901 da0c 5374 7265  sultDict)...Stre
-00000190: 616d 5265 6164 6572 2901 da06 6765 7463  amReader)...getc
-000001a0: 7764 6300 0000 0000 0000 0000 0000 0000  wdc.............
-000001b0: 0000 0004 0000 0040 0000 0073 a400 0000  .......@...s....
-000001c0: 6500 5a01 6400 5a02 5500 6503 6504 6401  e.Z.d.Z.U.e.e.d.
-000001d0: 3c00 6505 6503 1900 6504 6402 3c00 6503  <.e.e...e.d.<.e.
-000001e0: 6504 6403 3c00 6506 6507 1900 6504 6404  e.d.<.e.e...e.d.
-000001f0: 3c00 6508 6700 6509 6602 1900 6504 6405  <.e.g.e.f...e.d.
-00000200: 3c00 6508 6700 6509 6602 1900 6504 6406  <.e.g.e.f...e.d.
-00000210: 3c00 6508 650a 6701 6507 6602 1900 6504  <.e.e.g.e.f...e.
-00000220: 6407 3c00 6508 650a 6701 6507 6602 1900  d.<.e.e.g.e.f...
-00000230: 6504 6408 3c00 650b 8300 9b00 6409 9d02  e.d.<.e.....d...
-00000240: 6601 650c 650d 640a 9c02 640b 640c 8405  f.e.e.d...d.d...
-00000250: 5a0e 650c 640d 9c01 640e 640f 8404 5a0f  Z.e.d...d.d...Z.
-00000260: 6410 5300 2911 da0b 4261 7365 5772 6170  d.S.)...BaseWrap
-00000270: 7065 72da 046e 616d 65da 0f69 6e70 7574  per..name..input
-00000280: 5f65 7874 656e 7369 6f6e da10 6f75 7470  _extension..outp
-00000290: 7574 5f65 7874 656e 7369 6f6e da07 7265  ut_extension..re
-000002a0: 7375 6c74 73da 0769 6e73 7461 6c6c da06  sults..install..
-000002b0: 636f 6e66 6967 da09 7061 7273 655f 6f75  config..parse_ou
-000002c0: 74da 0970 6172 7365 5f65 7272 da03 746d  t..parse_err..tm
-000002d0: 7029 02da 0873 696d 5f66 696c 65da 0a6f  p)...sim_file..o
-000002e0: 7574 5f66 6f6c 6465 7263 0300 0000 0000  ut_folderc......
-000002f0: 0000 0000 0000 0a00 0000 0800 0000 c300  ................
-00000300: 0000 73b8 0000 0074 007c 0183 017d 0374  ..s....t.|...}.t
-00000310: 0183 007d 047a 887c 047c 006a 0219 0064  ...}.z.|.|.j...d
-00000320: 0119 007d 0574 036a 047c 059b 0064 029d  ...}.t.j.|...d..
-00000330: 027c 0374 036a 056a 0674 036a 056a 0664  .|.t.j.j.t.j.j.d
-00000340: 038d 0449 0064 0448 007d 0674 03a0 077c  ...I.d.H.}.t...|
-00000350: 00a0 087c 066a 09a1 01a1 017d 0774 03a0  ...|.j.....}.t..
-00000360: 077c 00a0 0a7c 066a 0b7c 02a1 02a1 017d  .|...|.j.|.....}
-00000370: 0874 03a0 0c7c 06a0 0da1 007c 077c 08a1  .t...|.....|.|..
-00000380: 0349 0064 0448 007d 097c 03a0 0ea1 0001  .I.d.H.}.|......
-00000390: 007c 0964 0519 007c 005f 0f57 006e 1c04  .|.d...|._.W.n..
-000003a0: 0074 1079 b201 0001 0001 0074 117c 006a  .t.y.......t.|.j
-000003b0: 0283 0101 0059 006e 0230 0064 0453 0029  .....Y.n.0.d.S.)
-000003c0: 0661 2501 0000 0a20 2020 2020 2020 2072  .a%....        r
-000003d0: 756e 2074 6865 2073 7069 6365 2073 696d  un the spice sim
-000003e0: 756c 6174 696f 6e20 6465 7363 7269 6265  ulation describe
-000003f0: 2062 7920 7468 6520 5f73 7069 6365 5f66   by the _spice_f
-00000400: 696c 650a 2020 2020 2020 2020 3a70 6172  ile.        :par
-00000410: 616d 2073 696d 5f66 696c 653a 2069 6e70  am sim_file: inp
-00000420: 7574 2066 696c 6520 746f 2062 6520 7072  ut file to be pr
-00000430: 6f63 6573 7320 6279 2074 6865 2070 726f  ocess by the pro
-00000440: 6772 616d 0a20 2020 2020 2020 203a 7061  gram.        :pa
-00000450: 7261 6d20 6f75 745f 666f 6c64 6572 3a20  ram out_folder: 
-00000460: 6469 7265 6374 6f72 7920 746f 2077 7269  directory to wri
-00000470: 7465 2073 696d 756c 6174 696f 6e20 6c6f  te simulation lo
-00000480: 670a 2020 2020 2020 2020 3a72 6574 7572  g.        :retur
-00000490: 6e3a 2061 2074 656d 7020 6669 6c65 206f  n: a temp file o
-000004a0: 6620 7468 6520 7261 7720 6f75 7420 6f66  f the raw out of
-000004b0: 2074 6865 2073 696d 756c 6174 6f72 2028   the simulator (
-000004c0: 746f 2062 6520 7072 6f63 6573 7320 6279  to be process by
-000004d0: 2073 6572 6961 6c69 7a65 5f72 6573 756c   serialize_resul
-000004e0: 7429 0a20 2020 2020 2020 20da 0470 6174  t).        ..pat
-000004f0: 687a 0320 2d73 2903 da05 7374 6469 6eda  hz. -s)...stdin.
-00000500: 0673 7464 6f75 74da 0673 7464 6572 724e  .stdout..stderrN
-00000510: e901 0000 0029 12da 046f 7065 6eda 096c  .....)...open..l
-00000520: 6f61 645f 636f 6e66 720d 0000 00da 0761  oad_confr......a
-00000530: 7379 6e63 696f da17 6372 6561 7465 5f73  syncio..create_s
-00000540: 7562 7072 6f63 6573 735f 7368 656c 6cda  ubprocess_shell.
-00000550: 0a73 7562 7072 6f63 6573 73da 0450 4950  .subprocess..PIP
-00000560: 45da 0b63 7265 6174 655f 7461 736b 7213  E..create_taskr.
-00000570: 0000 0072 1a00 0000 7214 0000 0072 1b00  ...r....r....r..
-00000580: 0000 da06 6761 7468 6572 da04 7761 6974  ....gather..wait
-00000590: da05 636c 6f73 6572 1000 0000 da08 4b65  ..closer......Ke
-000005a0: 7945 7272 6f72 da0e 706c 6561 7365 5f69  yError..please_i
-000005b0: 6e73 7461 6c6c 290a da04 7365 6c66 7216  nstall)...selfr.
-000005c0: 0000 0072 1700 0000 da03 6369 72da 0463  ...r......cir..c
-000005d0: 6f6e 6672 1800 0000 da04 7072 6f63 5a0c  onfr......procZ.
-000005e0: 7374 645f 6f75 745f 7461 736b 5a0c 7374  std_out_taskZ.st
-000005f0: 645f 6572 725f 7461 736b da03 7265 73a9  d_err_task..res.
-00000600: 0072 2e00 0000 fa45 433a 5c55 7365 7273  .r.....EC:\Users
-00000610: 5c50 6f74 6572 6561 755c 5079 6368 6172  \Potereau\Pychar
-00000620: 6d50 726f 6a65 6374 735c 7079 5745 535c  mProjects\pyWES\
-00000630: 7079 7761 735c 7772 6170 7065 725c 6261  pywas\wrapper\ba
-00000640: 7365 5f77 7261 7070 6572 2e70 79da 0372  se_wrapper.py..r
-00000650: 756e 2700 0000 7322 0000 0000 0b08 0106  un'...s"........
-00000660: 0102 010e 0104 0108 0102 0106 0106 fc0c  ................
-00000670: 0612 0114 0118 0108 010e 010c 017a 0f42  .............z.B
-00000680: 6173 6557 7261 7070 6572 2e72 756e 2901  aseWrapper.run).
-00000690: da04 6669 6c65 6302 0000 0000 0000 0000  ..filec.........
-000006a0: 0000 0004 0000 0008 0000 0043 0000 0073  ...........C...s
-000006b0: 5000 0000 7400 a001 7c01 6401 a102 8f30  P...t...|.d....0
-000006c0: 7d02 7c00 6a02 4400 5d18 7d03 7c00 6a02  }.|.j.D.].}.|.j.
-000006d0: 7c03 1900 7c02 6402 7c03 9b00 9d02 3c00  |...|.d.|.....<.
-000006e0: 7114 5700 6400 0400 0400 8303 0100 6e10  q.W.d.........n.
-000006f0: 3100 7342 3000 0100 0100 0100 5900 0100  1.sB0.......Y...
-00000700: 6400 5300 2903 4eda 0177 7a04 7265 732f  d.S.).N..wz.res/
-00000710: 2903 da04 6835 7079 da04 4669 6c65 7210  )...h5py..Filer.
-00000720: 0000 0029 0472 2900 0000 7231 0000 00da  ...).r)...r1....
-00000730: 0166 722d 0000 0072 2e00 0000 722e 0000  .fr-...r....r...
-00000740: 0072 2f00 0000 da06 6578 706f 7274 4400  .r/.....exportD.
-00000750: 0000 7306 0000 0000 010e 010a 017a 1242  ..s..........z.B
-00000760: 6173 6557 7261 7070 6572 2e65 7870 6f72  aseWrapper.expor
-00000770: 744e 2910 da08 5f5f 6e61 6d65 5f5f da0a  tN)...__name__..
-00000780: 5f5f 6d6f 6475 6c65 5f5f da0c 5f5f 7175  __module__..__qu
-00000790: 616c 6e61 6d65 5f5f da03 7374 72da 0f5f  alname__..str.._
-000007a0: 5f61 6e6e 6f74 6174 696f 6e73 5f5f 7206  _annotations__r.
-000007b0: 0000 0072 0700 0000 7209 0000 0072 0800  ...r....r....r..
-000007c0: 0000 da04 626f 6f6c 720a 0000 0072 0b00  ....boolr....r..
-000007d0: 0000 7203 0000 0072 0400 0000 7230 0000  ..r....r....r0..
-000007e0: 0072 3600 0000 722e 0000 0072 2e00 0000  .r6...r....r....
-000007f0: 722e 0000 0072 2f00 0000 720c 0000 0011  r....r/...r.....
-00000800: 0000 0073 1c00 0000 0a01 0801 0c01 0801  ...s............
-00000810: 0c05 1005 1005 1201 1205 0afd 0202 0201  ................
-00000820: 02fd 0c1d 720c 0000 007a 0c2f 636f 6e66  ....r....z./conf
-00000830: 6967 2e79 616d 6c29 02da 0963 6f6e 665f  ig.yaml)...conf_
-00000840: 6669 6c65 da06 7265 7475 726e 6301 0000  file..returnc...
-00000850: 0000 0000 0000 0000 0003 0000 0008 0000  ................
-00000860: 0043 0000 0073 8000 0000 7400 6a01 a002  .C...s....t.j...
-00000870: 7c00 a101 7336 7403 7c00 6401 8302 8f10  |...s6t.|.d.....
-00000880: 7d01 5700 6400 0400 0400 8303 0100 6e10  }.W.d.........n.
-00000890: 3100 732c 3000 0100 0100 0100 5900 0100  1.s,0.......Y...
-000008a0: 7403 7c00 8301 8f20 7d01 7404 6a05 7c01  t.|.... }.t.j.|.
-000008b0: 7404 6a06 6402 8d02 7d02 5700 6400 0400  t.j.d...}.W.d...
-000008c0: 0400 8303 0100 6e10 3100 7364 3000 0100  ......n.1.sd0...
-000008d0: 0100 0100 5900 0100 7c02 6400 7500 727c  ....Y...|.d.u.r|
-000008e0: 7407 8300 5300 7c02 5300 2903 4e72 3200  t...S.|.S.).Nr2.
-000008f0: 0000 2901 da06 4c6f 6164 6572 2908 da02  ..)...Loader)...
-00000900: 6f73 7218 0000 00da 0669 7366 696c 6572  osr......isfiler
-00000910: 1d00 0000 da04 7961 6d6c da04 6c6f 6164  ......yaml..load
-00000920: 723f 0000 00da 0464 6963 7429 0372 3d00  r?.....dict).r=.
-00000930: 0000 7235 0000 0072 2b00 0000 722e 0000  ..r5...r+...r...
-00000940: 0072 2e00 0000 722f 0000 0072 1e00 0000  .r....r/...r....
-00000950: 4a00 0000 7310 0000 0000 010c 010c 011e  J...s...........
-00000960: 010a 012e 0108 0106 0172 1e00 0000 2902  .........r....).
-00000970: 722b 0000 0072 3d00 0000 6302 0000 0000  r+...r=...c.....
-00000980: 0000 0000 0000 0005 0000 0008 0000 0043  ...............C
-00000990: 0000 0073 6200 0000 7400 7c01 8301 7d02  ...sb...t.|...}.
-000009a0: 7c00 4400 5d10 7d03 7c00 7c03 1900 7c02  |.D.].}.|.|...|.
-000009b0: 7c03 3c00 710c 7401 7c01 6401 8302 8f26  |.<.q.t.|.d....&
-000009c0: 7d04 7c04 a002 7403 6a04 7c02 7403 6a05  }.|...t.j.|.t.j.
-000009d0: 6402 8d02 a101 0100 5700 6400 0400 0400  d.......W.d.....
-000009e0: 8303 0100 6e10 3100 7354 3000 0100 0100  ....n.1.sT0.....
-000009f0: 0100 5900 0100 6400 5300 2903 4e72 3200  ..Y...d.S.).Nr2.
-00000a00: 0000 2901 da06 4475 6d70 6572 2906 721e  ..)...Dumper).r.
-00000a10: 0000 0072 1d00 0000 da05 7772 6974 6572  ...r......writer
-00000a20: 4200 0000 da04 6475 6d70 7245 0000 0029  B.....dumprE...)
-00000a30: 0572 2b00 0000 723d 0000 005a 0863 6f6e  .r+...r=...Z.con
-00000a40: 665f 6f6c 64da 036b 6579 7235 0000 0072  f_old..keyr5...r
-00000a50: 2e00 0000 722e 0000 0072 2f00 0000 da0a  ....r....r/.....
-00000a60: 7772 6974 655f 636f 6e66 5500 0000 730a  write_confU...s.
-00000a70: 0000 0000 0108 0108 020e 010c 0172 4900  .............rI.
-00000a80: 0000 2902 da09 7072 6f67 5f6e 616d 6572  ..)...prog_namer
-00000a90: 3e00 0000 6301 0000 0000 0000 0000 0000  >...c...........
-00000aa0: 0001 0000 0005 0000 0043 0000 0073 1800  .........C...s..
-00000ab0: 0000 7400 7c00 9b00 6401 7c00 9b00 6402  ..t.|...d.|...d.
-00000ac0: 9d04 8301 0100 6400 5300 2903 4e7a 2d20  ......d.S.).Nz- 
-00000ad0: 6e6f 7420 666f 756e 6420 696e 2063 6f6e  not found in con
-00000ae0: 6669 6720 6669 6c65 2e20 506c 6561 7365  fig file. Please
-00000af0: 2072 756e 2027 7079 7761 7320 7a09 2069   run 'pywas z. i
-00000b00: 6e73 7461 6c6c 2729 01da 0570 7269 6e74  nstall')...print
-00000b10: 2901 724a 0000 0072 2e00 0000 722e 0000  ).rJ...r....r...
-00000b20: 0072 2f00 0000 7228 0000 005e 0000 0073  .r/...r(...^...s
-00000b30: 0600 0000 0001 0201 0eff 7228 0000 0029  ..........r(...)
-00000b40: 1ada 075f 5f64 6f63 5f5f 5a07 6f73 2e70  ...__doc__Z.os.p
-00000b50: 6174 6872 4000 0000 da08 7079 6461 6e74  athr@.....pydant
-00000b60: 6963 7202 0000 0072 0300 0000 7204 0000  icr....r....r...
-00000b70: 00da 0465 6e75 6d72 0500 0000 da06 7479  ...enumr......ty
-00000b80: 7069 6e67 7206 0000 0072 0700 0000 7208  pingr....r....r.
-00000b90: 0000 0072 1f00 0000 5a13 7079 7761 732e  ...r....Z.pywas.
-00000ba0: 7061 7273 652e 7265 7375 6c74 7372 0900  parse.resultsr..
-00000bb0: 0000 7233 0000 0072 0a00 0000 7242 0000  ..r3...r....rB..
-00000bc0: 0072 0b00 0000 720c 0000 0072 4400 0000  .r....r....rD...
-00000bd0: 721e 0000 0072 4900 0000 723a 0000 0072  r....rI...r:...r
-00000be0: 2800 0000 722e 0000 0072 2e00 0000 722e  (...r....r....r.
-00000bf0: 0000 0072 2f00 0000 da08 3c6d 6f64 756c  ...r/.....<modul
-00000c00: 653e 0100 0000 731c 0000 0004 0308 0214  e>....s.........
-00000c10: 010c 0114 0108 010c 0108 010c 0108 010c  ................
-00000c20: 0310 391c 0b1c 09                        ..9....
+000000a0: 6408 6c02 6d13 5a13 0100 6401 6409 6c14  d.l.m.Z...d.d.l.
+000000b0: 6d15 5a15 0100 4700 640a 640b 8400 640b  m.Z...G.d.d...d.
+000000c0: 6504 8303 5a16 6513 8300 9b00 640c 9d02  e...Z.e.....d...
+000000d0: 6601 6505 6517 640d 9c02 640e 640f 8405  f.e.e.d...d.d...
+000000e0: 5a18 6513 8300 9b00 640c 9d02 6601 6517  Z.e.....d...f.e.
+000000f0: 6505 6410 9c02 6411 6412 8405 5a19 651a  e.d...d.d...Z.e.
+00000100: 6402 6413 9c02 6414 6415 8404 5a1b 6402  d.d...d.d...Z.d.
+00000110: 5300 2916 7a20 0a42 6173 6520 636c 6173  S.).z .Base clas
+00000120: 7320 666f 7220 7370 6963 6520 7369 6d75  s for spice simu
+00000130: 6c61 746f 720a e900 0000 004e 2903 da09  lator......N)...
+00000140: 4261 7365 4d6f 6465 6cda 0846 696c 6550  BaseModel..FileP
+00000150: 6174 68da 0d44 6972 6563 746f 7279 5061  ath..DirectoryPa
+00000160: 7468 2901 da04 456e 756d 2903 da04 4c69  th)...Enum)...Li
+00000170: 7374 da08 4f70 7469 6f6e 616c da08 4361  st..Optional..Ca
+00000180: 6c6c 6162 6c65 2901 da0a 5265 7375 6c74  llable)...Result
+00000190: 4469 6374 2901 da0c 5374 7265 616d 5265  Dict)...StreamRe
+000001a0: 6164 6572 2901 da06 6765 7463 7764 a901  ader)...getcwd..
+000001b0: da05 7072 696e 7463 0000 0000 0000 0000  ..printc........
+000001c0: 0000 0000 0000 0000 0400 0000 4000 0000  ............@...
+000001d0: 73a4 0000 0065 005a 0164 005a 0255 0065  s....e.Z.d.Z.U.e
+000001e0: 0365 0464 013c 0065 0565 0319 0065 0464  .e.d.<.e.e...e.d
+000001f0: 023c 0065 0365 0464 033c 0065 0665 0719  .<.e.e.d.<.e.e..
+00000200: 0065 0464 043c 0065 0867 0065 0966 0219  .e.d.<.e.g.e.f..
+00000210: 0065 0464 053c 0065 0867 0065 0966 0219  .e.d.<.e.g.e.f..
+00000220: 0065 0464 063c 0065 0865 0a67 0165 0766  .e.d.<.e.e.g.e.f
+00000230: 0219 0065 0464 073c 0065 0865 0a67 0165  ...e.d.<.e.e.g.e
+00000240: 0766 0219 0065 0464 083c 0065 0b83 009b  .f...e.d.<.e....
+00000250: 0064 099d 0266 0165 0c65 0d64 0a9c 0264  .d...f.e.e.d...d
+00000260: 0b64 0c84 055a 0e65 0c64 0d9c 0164 0e64  .d...Z.e.d...d.d
+00000270: 0f84 045a 0f64 1053 0029 11da 0b42 6173  ...Z.d.S.)...Bas
+00000280: 6557 7261 7070 6572 da04 6e61 6d65 da0f  eWrapper..name..
+00000290: 696e 7075 745f 6578 7465 6e73 696f 6eda  input_extension.
+000002a0: 106f 7574 7075 745f 6578 7465 6e73 696f  .output_extensio
+000002b0: 6eda 0772 6573 756c 7473 da07 696e 7374  n..results..inst
+000002c0: 616c 6cda 0663 6f6e 6669 67da 0970 6172  all..config..par
+000002d0: 7365 5f6f 7574 da09 7061 7273 655f 6572  se_out..parse_er
+000002e0: 72da 0374 6d70 2902 da08 7369 6d5f 6669  r..tmp)...sim_fi
+000002f0: 6c65 da0a 6f75 745f 666f 6c64 6572 6303  le..out_folderc.
+00000300: 0000 0000 0000 0000 0000 000a 0000 0008  ................
+00000310: 0000 00c3 0000 0073 be00 0000 7400 7c01  .......s....t.|.
+00000320: 8301 7d03 7401 8300 7d04 7a88 7c04 7c00  ..}.t...}.z.|.|.
+00000330: 6a02 1900 6401 1900 7d05 7403 6a04 7c05  j...d...}.t.j.|.
+00000340: 9b00 6402 9d02 7c03 7403 6a05 6a06 7403  ..d...|.t.j.j.t.
+00000350: 6a05 6a06 6403 8d04 4900 6404 4800 7d06  j.j.d...I.d.H.}.
+00000360: 7403 a007 7c00 a008 7c06 6a09 a101 a101  t...|...|.j.....
+00000370: 7d07 7403 a007 7c00 a00a 7c06 6a0b 7c02  }.t...|...|.j.|.
+00000380: a102 a101 7d08 7403 a00c 7c06 a00d a100  ....}.t...|.....
+00000390: 7c07 7c08 a103 4900 6404 4800 7d09 7c03  |.|...I.d.H.}.|.
+000003a0: a00e a100 0100 7c09 6405 1900 7c00 5f0f  ......|.d...|._.
+000003b0: 5700 6e22 0400 7410 79b8 0100 0100 0100  W.n"..t.y.......
+000003c0: 7411 7c00 6a02 8301 0100 7412 8300 0100  t.|.j.....t.....
+000003d0: 5900 6e02 3000 6404 5300 2906 6125 0100  Y.n.0.d.S.).a%..
+000003e0: 000a 2020 2020 2020 2020 7275 6e20 7468  ..        run th
+000003f0: 6520 7370 6963 6520 7369 6d75 6c61 7469  e spice simulati
+00000400: 6f6e 2064 6573 6372 6962 6520 6279 2074  on describe by t
+00000410: 6865 205f 7370 6963 655f 6669 6c65 0a20  he _spice_file. 
+00000420: 2020 2020 2020 203a 7061 7261 6d20 7369         :param si
+00000430: 6d5f 6669 6c65 3a20 696e 7075 7420 6669  m_file: input fi
+00000440: 6c65 2074 6f20 6265 2070 726f 6365 7373  le to be process
+00000450: 2062 7920 7468 6520 7072 6f67 7261 6d0a   by the program.
+00000460: 2020 2020 2020 2020 3a70 6172 616d 206f          :param o
+00000470: 7574 5f66 6f6c 6465 723a 2064 6972 6563  ut_folder: direc
+00000480: 746f 7279 2074 6f20 7772 6974 6520 7369  tory to write si
+00000490: 6d75 6c61 7469 6f6e 206c 6f67 0a20 2020  mulation log.   
+000004a0: 2020 2020 203a 7265 7475 726e 3a20 6120       :return: a 
+000004b0: 7465 6d70 2066 696c 6520 6f66 2074 6865  temp file of the
+000004c0: 2072 6177 206f 7574 206f 6620 7468 6520   raw out of the 
+000004d0: 7369 6d75 6c61 746f 7220 2874 6f20 6265  simulator (to be
+000004e0: 2070 726f 6365 7373 2062 7920 7365 7269   process by seri
+000004f0: 616c 697a 655f 7265 7375 6c74 290a 2020  alize_result).  
+00000500: 2020 2020 2020 da04 7061 7468 7a03 202d        ..pathz. -
+00000510: 7329 03da 0573 7464 696e da06 7374 646f  s)...stdin..stdo
+00000520: 7574 da06 7374 6465 7272 4ee9 0100 0000  ut..stderrN.....
+00000530: 2913 da04 6f70 656e da09 6c6f 6164 5f63  )...open..load_c
+00000540: 6f6e 6672 0f00 0000 da07 6173 796e 6369  onfr......asynci
+00000550: 6fda 1763 7265 6174 655f 7375 6270 726f  o..create_subpro
+00000560: 6365 7373 5f73 6865 6c6c da0a 7375 6270  cess_shell..subp
+00000570: 726f 6365 7373 da04 5049 5045 da0b 6372  rocess..PIPE..cr
+00000580: 6561 7465 5f74 6173 6b72 1500 0000 721c  eate_taskr....r.
+00000590: 0000 0072 1600 0000 721d 0000 00da 0667  ...r....r......g
+000005a0: 6174 6865 72da 0477 6169 74da 0563 6c6f  ather..wait..clo
+000005b0: 7365 7212 0000 00da 084b 6579 4572 726f  ser......KeyErro
+000005c0: 72da 0e70 6c65 6173 655f 696e 7374 616c  r..please_instal
+000005d0: 6cda 0465 7869 7429 0ada 0473 656c 6672  l..exit)...selfr
+000005e0: 1800 0000 7219 0000 00da 0363 6972 da04  ....r......cir..
+000005f0: 636f 6e66 721a 0000 00da 0470 726f 635a  confr......procZ
+00000600: 0c73 7464 5f6f 7574 5f74 6173 6b5a 0c73  .std_out_taskZ.s
+00000610: 7464 5f65 7272 5f74 6173 6bda 0372 6573  td_err_task..res
+00000620: a900 7231 0000 00fa 4543 3a5c 5573 6572  ..r1....EC:\User
+00000630: 735c 506f 7465 7265 6175 5c50 7963 6861  s\Potereau\Pycha
+00000640: 726d 5072 6f6a 6563 7473 5c70 7957 4553  rmProjects\pyWES
+00000650: 5c70 7977 6173 5c77 7261 7070 6572 5c62  \pywas\wrapper\b
+00000660: 6173 655f 7772 6170 7065 722e 7079 da03  ase_wrapper.py..
+00000670: 7275 6e28 0000 0073 2400 0000 000b 0801  run(...s$.......
+00000680: 0601 0201 0e01 0401 0801 0201 0601 06fc  ................
+00000690: 0c06 1201 1401 1801 0801 0e01 0c01 0a01  ................
+000006a0: 7a0f 4261 7365 5772 6170 7065 722e 7275  z.BaseWrapper.ru
+000006b0: 6e29 01da 0466 696c 6563 0200 0000 0000  n)...filec......
+000006c0: 0000 0000 0000 0400 0000 0800 0000 4300  ..............C.
+000006d0: 0000 7350 0000 0074 00a0 017c 0164 01a1  ..sP...t...|.d..
+000006e0: 028f 307d 027c 006a 0244 005d 187d 037c  ..0}.|.j.D.].}.|
+000006f0: 006a 027c 0319 007c 0264 027c 039b 009d  .j.|...|.d.|....
+00000700: 023c 0071 1457 0064 0004 0004 0083 0301  .<.q.W.d........
+00000710: 006e 1031 0073 4230 0001 0001 0001 0059  .n.1.sB0.......Y
+00000720: 0001 0064 0053 0029 034e da01 777a 0472  ...d.S.).N..wz.r
+00000730: 6573 2f29 03da 0468 3570 79da 0446 696c  es/)...h5py..Fil
+00000740: 6572 1200 0000 2904 722c 0000 0072 3400  er....).r,...r4.
+00000750: 0000 da01 6672 3000 0000 7231 0000 0072  ....fr0...r1...r
+00000760: 3100 0000 7232 0000 00da 0665 7870 6f72  1...r2.....expor
+00000770: 7446 0000 0073 0600 0000 0001 0e01 0a01  tF...s..........
+00000780: 7a12 4261 7365 5772 6170 7065 722e 6578  z.BaseWrapper.ex
+00000790: 706f 7274 4e29 10da 085f 5f6e 616d 655f  portN)...__name_
+000007a0: 5fda 0a5f 5f6d 6f64 756c 655f 5fda 0c5f  _..__module__.._
+000007b0: 5f71 7561 6c6e 616d 655f 5fda 0373 7472  _qualname__..str
+000007c0: da0f 5f5f 616e 6e6f 7461 7469 6f6e 735f  ..__annotations_
+000007d0: 5f72 0600 0000 7207 0000 0072 0900 0000  _r....r....r....
+000007e0: 7208 0000 00da 0462 6f6f 6c72 0a00 0000  r......boolr....
+000007f0: 720b 0000 0072 0300 0000 7204 0000 0072  r....r....r....r
+00000800: 3300 0000 7239 0000 0072 3100 0000 7231  3...r9...r1...r1
+00000810: 0000 0072 3100 0000 7232 0000 0072 0e00  ...r1...r2...r..
+00000820: 0000 1200 0000 731c 0000 000a 0108 010c  ......s.........
+00000830: 0108 010c 0510 0510 0512 0112 050a fd02  ................
+00000840: 0202 0102 fd0c 1e72 0e00 0000 7a0c 2f63  .......r....z./c
+00000850: 6f6e 6669 672e 7961 6d6c 2902 da09 636f  onfig.yaml)...co
+00000860: 6e66 5f66 696c 65da 0672 6574 7572 6e63  nf_file..returnc
+00000870: 0100 0000 0000 0000 0000 0000 0300 0000  ................
+00000880: 0800 0000 4300 0000 7380 0000 0074 006a  ....C...s....t.j
+00000890: 01a0 027c 00a1 0173 3674 037c 0064 0183  ...|...s6t.|.d..
+000008a0: 028f 107d 0157 0064 0004 0004 0083 0301  ...}.W.d........
+000008b0: 006e 1031 0073 2c30 0001 0001 0001 0059  .n.1.s,0.......Y
+000008c0: 0001 0074 037c 0083 018f 207d 0174 046a  ...t.|.... }.t.j
+000008d0: 057c 0174 046a 0664 028d 027d 0257 0064  .|.t.j.d...}.W.d
+000008e0: 0004 0004 0083 0301 006e 1031 0073 6430  .........n.1.sd0
+000008f0: 0001 0001 0001 0059 0001 007c 0264 0075  .......Y...|.d.u
+00000900: 0072 7c74 0783 0053 007c 0253 0029 034e  .r|t...S.|.S.).N
+00000910: 7235 0000 0029 01da 064c 6f61 6465 7229  r5...)...Loader)
+00000920: 08da 026f 7372 1a00 0000 da06 6973 6669  ...osr......isfi
+00000930: 6c65 721f 0000 00da 0479 616d 6cda 046c  ler......yaml..l
+00000940: 6f61 6472 4200 0000 da04 6469 6374 2903  oadrB.....dict).
+00000950: 7240 0000 0072 3800 0000 722e 0000 0072  r@...r8...r....r
+00000960: 3100 0000 7231 0000 0072 3200 0000 7220  1...r1...r2...r 
+00000970: 0000 004c 0000 0073 1000 0000 0001 0c01  ...L...s........
+00000980: 0c01 1e01 0a01 2e01 0801 0601 7220 0000  ............r ..
+00000990: 0029 0272 2e00 0000 7240 0000 0063 0200  .).r....r@...c..
+000009a0: 0000 0000 0000 0000 0000 0500 0000 0800  ................
+000009b0: 0000 4300 0000 7362 0000 0074 007c 0183  ..C...sb...t.|..
+000009c0: 017d 027c 0044 005d 107d 037c 007c 0319  .}.|.D.].}.|.|..
+000009d0: 007c 027c 033c 0071 0c74 017c 0164 0183  .|.|.<.q.t.|.d..
+000009e0: 028f 267d 047c 04a0 0274 036a 047c 0274  ..&}.|...t.j.|.t
+000009f0: 036a 0564 028d 02a1 0101 0057 0064 0004  .j.d.......W.d..
+00000a00: 0004 0083 0301 006e 1031 0073 5430 0001  .......n.1.sT0..
+00000a10: 0001 0001 0059 0001 0064 0053 0029 034e  .....Y...d.S.).N
+00000a20: 7235 0000 0029 01da 0644 756d 7065 7229  r5...)...Dumper)
+00000a30: 0672 2000 0000 721f 0000 00da 0577 7269  .r ...r......wri
+00000a40: 7465 7245 0000 00da 0464 756d 7072 4800  terE.....dumprH.
+00000a50: 0000 2905 722e 0000 0072 4000 0000 5a08  ..).r....r@...Z.
+00000a60: 636f 6e66 5f6f 6c64 da03 6b65 7972 3800  conf_old..keyr8.
+00000a70: 0000 7231 0000 0072 3100 0000 7232 0000  ..r1...r1...r2..
+00000a80: 00da 0a77 7269 7465 5f63 6f6e 6657 0000  ...write_confW..
+00000a90: 0073 0a00 0000 0001 0801 0802 0e01 0c01  .s..............
+00000aa0: 724c 0000 0029 02da 0970 726f 675f 6e61  rL...)...prog_na
+00000ab0: 6d65 7241 0000 0063 0100 0000 0000 0000  merA...c........
+00000ac0: 0000 0000 0100 0000 0500 0000 4300 0000  ............C...
+00000ad0: 7318 0000 0074 007c 009b 0064 017c 009b  s....t.|...d.|..
+00000ae0: 0064 029d 0483 0101 0064 0053 0029 034e  .d.......d.S.).N
+00000af0: 7a2d 206e 6f74 2066 6f75 6e64 2069 6e20  z- not found in 
+00000b00: 636f 6e66 6967 2066 696c 652e 2050 6c65  config file. Ple
+00000b10: 6173 6520 7275 6e20 2770 7977 6173 207a  ase run 'pywas z
+00000b20: 0920 696e 7374 616c 6c27 720c 0000 0029  . install'r....)
+00000b30: 0172 4d00 0000 7231 0000 0072 3100 0000  .rM...r1...r1...
+00000b40: 7232 0000 0072 2a00 0000 6000 0000 7306  r2...r*...`...s.
+00000b50: 0000 0000 0102 010e ff72 2a00 0000 291c  .........r*...).
+00000b60: da07 5f5f 646f 635f 5f5a 076f 732e 7061  ..__doc__Z.os.pa
+00000b70: 7468 7243 0000 00da 0870 7964 616e 7469  thrC.....pydanti
+00000b80: 6372 0200 0000 7203 0000 0072 0400 0000  cr....r....r....
+00000b90: da04 656e 756d 7205 0000 00da 0674 7970  ..enumr......typ
+00000ba0: 696e 6772 0600 0000 7207 0000 0072 0800  ingr....r....r..
+00000bb0: 0000 7221 0000 005a 1370 7977 6173 2e70  ..r!...Z.pywas.p
+00000bc0: 6172 7365 2e72 6573 756c 7473 7209 0000  arse.resultsr...
+00000bd0: 0072 3600 0000 720a 0000 0072 4500 0000  .r6...r....rE...
+00000be0: 720b 0000 00da 0472 6963 6872 0d00 0000  r......richr....
+00000bf0: 720e 0000 0072 4700 0000 7220 0000 0072  r....rG...r ...r
+00000c00: 4c00 0000 723d 0000 0072 2a00 0000 7231  L...r=...r*...r1
+00000c10: 0000 0072 3100 0000 7231 0000 0072 3200  ...r1...r1...r2.
+00000c20: 0000 da08 3c6d 6f64 756c 653e 0100 0000  ....<module>....
+00000c30: 731e 0000 0004 0308 0214 010c 0114 0108  s...............
+00000c40: 010c 0108 010c 0108 010c 010c 0310 3a1c  ..............:.
+00000c50: 0b1c 09                                  ...
```

### Comparing `pywas-0.1.3/pywas/wrapper/__pycache__/ngspice.cpython-39.pyc` & `pywas-0.1.4/pywas/wrapper/__pycache__/ngspice.cpython-39.pyc`

 * *Files identical despite different names*

### Comparing `pywas-0.1.3/pywas/wrapper/base_wrapper.py` & `pywas-0.1.4/pywas/wrapper/base_wrapper.py`

 * *Files 2% similar despite different names*

```diff
@@ -8,14 +8,15 @@
 from typing import List, Optional, Callable
 import asyncio
 from pywas.parse.results import ResultDict
 import h5py
 from asyncio import StreamReader
 import yaml
 from os import getcwd
+from rich import print
 
 
 class BaseWrapper(BaseModel):
     name: str
     input_extension: List[str]
     output_extension: str
     results: Optional[ResultDict]
@@ -60,14 +61,15 @@
             std_out_task = asyncio.create_task(self.parse_out(proc.stdout))
             std_err_task = asyncio.create_task(self.parse_err(proc.stderr, out_folder))
             res = await asyncio.gather(proc.wait(), std_out_task, std_err_task)
             cir.close()
             self.results = res[1]
         except KeyError:
             please_install(self.name)
+            exit()
 
     def export(self, file: FilePath):
         with h5py.File(file, "w") as f:
             for res in self.results:
                 f[f"res/{res}"] = self.results[res]
```

### Comparing `pywas-0.1.3/pywas/wrapper/ngspice.py` & `pywas-0.1.4/pywas/wrapper/ngspice.py`

 * *Files identical despite different names*

### Comparing `pywas-0.1.3/README.md` & `pywas-0.1.4/README.md`

 * *Files 5% similar despite different names*

```diff
@@ -18,16 +18,33 @@
 
 * `--install-completion`: Install completion for the current shell.
 * `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
 * `--help`: Show this message and exit.
 
 **Commands**:
 
+* `new`
 * `ngspice`
 
+## `pyWAS new`
+
+**Usage**:
+
+```console
+$ pyWAS new [OPTIONS] NAME
+```
+
+**Arguments**:
+
+* `NAME`: [required]
+
+**Options**:
+
+* `--help`: Show this message and exit.
+
 ## `pyWAS ngspice`
 
 **Usage**:
 
 ```console
 $ pyWAS ngspice [OPTIONS] COMMAND [ARGS]...
 ```
```

### Comparing `pywas-0.1.3/setup.py` & `pywas-0.1.4/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -4,31 +4,31 @@
 packages = \
 ['pywas', 'pywas.parse', 'pywas.wrapper']
 
 package_data = \
 {'': ['*'], 'pywas': ['template/*']}
 
 install_requires = \
-['fastapi-jsonrpc>=2.2.0,<3.0.0',
- 'h5py>=3.7.0,<4.0.0',
+['h5py>=3.7.0,<4.0.0',
  'jinja2>=3.1.2,<4.0.0',
  'numpy>=1.23.2,<2.0.0',
+ 'pydantic>=1.10.7,<2.0.0',
  'pyyaml>=6.0,<7.0',
+ 'rich>=13.3.3,<14.0.0',
  'typer>=0.7.0,<0.8.0',
- 'uvicorn[standard]>=0.20.0,<0.21.0',
  'wget>=3.2,<4.0']
 
 entry_points = \
 {'console_scripts': ['pywas = pywas.main:cli']}
 
 setup_kwargs = {
     'name': 'pywas',
-    'version': '0.1.3',
+    'version': '0.1.4',
     'description': '',
-    'long_description': '# `pyWAS`\n\n*Py*thon *W*rapper for *A*nalog design *S*oftware\n\n**Installation using [pipx](https://pypa.github.io/pipx/installation/)**:\n\n```console\n$ pipx install pywas\n```\n\n**Usage**:\n\n```console\n$ pyWAS [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `ngspice`\n\n## `pyWAS ngspice`\n\n**Usage**:\n\n```console\n$ pyWAS ngspice [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `config`\n* `install`: Install ngspice executable in the correct...\n* `run`: Should not be named "run"\n\n### `pyWAS ngspice config`\n\n**Usage**:\n\n```console\n$ pyWAS ngspice config [OPTIONS] KEY PATH\n```\n\n**Arguments**:\n\n* `KEY`: [required]\n* `PATH`: [required]\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n### `pyWAS ngspice install`\n\nInstall ngspice executable in the correct location.\n\n**Usage**:\n\n```console\n$ pyWAS ngspice install [OPTIONS]\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n### `pyWAS ngspice run`\n\nShould not be named "run"\n\n**Usage**:\n\n```console\n$ pyWAS ngspice run [OPTIONS] IN_FILE\n```\n\n**Arguments**:\n\n* `IN_FILE`: [required]\n\n**Options**:\n\n* `--out-folder TEXT`: [default: C:\\Users\\Potereau\\PycharmProjects\\pyWES/tmp/]\n* `--help`: Show this message and exit.\n',
+    'long_description': '# `pyWAS`\n\n*Py*thon *W*rapper for *A*nalog design *S*oftware\n\n**Installation using [pipx](https://pypa.github.io/pipx/installation/)**:\n\n```console\n$ pipx install pywas\n```\n\n**Usage**:\n\n```console\n$ pyWAS [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `new`\n* `ngspice`\n\n## `pyWAS new`\n\n**Usage**:\n\n```console\n$ pyWAS new [OPTIONS] NAME\n```\n\n**Arguments**:\n\n* `NAME`: [required]\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n## `pyWAS ngspice`\n\n**Usage**:\n\n```console\n$ pyWAS ngspice [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `config`\n* `install`: Install ngspice executable in the correct...\n* `run`: Should not be named "run"\n\n### `pyWAS ngspice config`\n\n**Usage**:\n\n```console\n$ pyWAS ngspice config [OPTIONS] KEY PATH\n```\n\n**Arguments**:\n\n* `KEY`: [required]\n* `PATH`: [required]\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n### `pyWAS ngspice install`\n\nInstall ngspice executable in the correct location.\n\n**Usage**:\n\n```console\n$ pyWAS ngspice install [OPTIONS]\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n### `pyWAS ngspice run`\n\nShould not be named "run"\n\n**Usage**:\n\n```console\n$ pyWAS ngspice run [OPTIONS] IN_FILE\n```\n\n**Arguments**:\n\n* `IN_FILE`: [required]\n\n**Options**:\n\n* `--out-folder TEXT`: [default: C:\\Users\\Potereau\\PycharmProjects\\pyWES/tmp/]\n* `--help`: Show this message and exit.\n',
     'author': 'Patarimi',
     'author_email': 'mpqqch@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
     'packages': packages,
     'package_data': package_data,
```

### Comparing `pywas-0.1.3/PKG-INFO` & `pywas-0.1.4/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,26 +1,26 @@
 Metadata-Version: 2.1
 Name: pywas
-Version: 0.1.3
+Version: 0.1.4
 Summary: 
 Author: Patarimi
 Author-email: mpqqch@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
-Requires-Dist: fastapi-jsonrpc (>=2.2.0,<3.0.0)
 Requires-Dist: h5py (>=3.7.0,<4.0.0)
 Requires-Dist: jinja2 (>=3.1.2,<4.0.0)
 Requires-Dist: numpy (>=1.23.2,<2.0.0)
+Requires-Dist: pydantic (>=1.10.7,<2.0.0)
 Requires-Dist: pyyaml (>=6.0,<7.0)
+Requires-Dist: rich (>=13.3.3,<14.0.0)
 Requires-Dist: typer (>=0.7.0,<0.8.0)
-Requires-Dist: uvicorn[standard] (>=0.20.0,<0.21.0)
 Requires-Dist: wget (>=3.2,<4.0)
 Description-Content-Type: text/markdown
 
 # `pyWAS`
 
 *Py*thon *W*rapper for *A*nalog design *S*oftware
 
@@ -40,16 +40,33 @@
 
 * `--install-completion`: Install completion for the current shell.
 * `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
 * `--help`: Show this message and exit.
 
 **Commands**:
 
+* `new`
 * `ngspice`
 
+## `pyWAS new`
+
+**Usage**:
+
+```console
+$ pyWAS new [OPTIONS] NAME
+```
+
+**Arguments**:
+
+* `NAME`: [required]
+
+**Options**:
+
+* `--help`: Show this message and exit.
+
 ## `pyWAS ngspice`
 
 **Usage**:
 
 ```console
 $ pyWAS ngspice [OPTIONS] COMMAND [ARGS]...
 ```
```

