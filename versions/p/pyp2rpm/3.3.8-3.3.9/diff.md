# Comparing `tmp/pyp2rpm-3.3.8.tar.gz` & `tmp/pyp2rpm-3.3.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyp2rpm-3.3.8.tar", last modified: Tue Feb 22 07:29:10 2022, max compression
+gzip compressed data, was "pyp2rpm-3.3.9.tar", last modified: Fri Apr  7 01:53:06 2023, max compression
```

## Comparing `pyp2rpm-3.3.8.tar` & `pyp2rpm-3.3.9.tar`

### file list

```diff
@@ -1,95 +1,95 @@
-drwxrwxr-x   0 gordon   (556600005) gordon   (556600005)        0 2022-02-22 07:29:10.414967 pyp2rpm-3.3.8/
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     7287 2022-02-22 07:28:50.000000 pyp2rpm-3.3.8/CHANGELOG
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1113 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/LICENSE
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)      647 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/MANIFEST.in
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1350 2022-02-22 07:29:10.414967 pyp2rpm-3.3.8/PKG-INFO
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     5214 2021-06-20 21:10:20.000000 pyp2rpm-3.3.8/README.md
-drwxrwxr-x   0 gordon   (556600005) gordon   (556600005)        0 2022-02-22 07:29:10.409967 pyp2rpm-3.3.8/pyp2rpm/
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)       65 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/pyp2rpm/__init__.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    11259 2021-06-14 00:00:02.000000 pyp2rpm-3.3.8/pyp2rpm/archive.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    10767 2021-06-20 21:10:20.000000 pyp2rpm-3.3.8/pyp2rpm/bin.py
-drwxrwxr-x   0 gordon   (556600005) gordon   (556600005)        0 2022-02-22 07:29:10.409967 pyp2rpm-3.3.8/pyp2rpm/command/
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)        0 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/pyp2rpm/command/__init__.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3380 2019-08-04 21:57:28.000000 pyp2rpm-3.3.8/pyp2rpm/command/extract_dist.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    12735 2021-06-20 06:55:08.000000 pyp2rpm-3.3.8/pyp2rpm/convertor.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     7427 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/pyp2rpm/dependency_convert.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4210 2021-06-13 22:58:14.000000 pyp2rpm-3.3.8/pyp2rpm/dependency_parser.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)      444 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/pyp2rpm/exceptions.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4406 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/pyp2rpm/filters.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1676 2019-10-03 22:55:20.000000 pyp2rpm-3.3.8/pyp2rpm/logger.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    22117 2022-02-22 07:02:20.000000 pyp2rpm-3.3.8/pyp2rpm/metadata_extractors.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     2763 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/pyp2rpm/module_runners.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    10264 2019-09-29 18:05:53.000000 pyp2rpm-3.3.8/pyp2rpm/name_convertor.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4030 2021-06-13 22:58:14.000000 pyp2rpm-3.3.8/pyp2rpm/package_data.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     8957 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/pyp2rpm/package_getters.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     5290 2021-06-13 22:58:14.000000 pyp2rpm-3.3.8/pyp2rpm/settings.py
-drwxrwxr-x   0 gordon   (556600005) gordon   (556600005)        0 2022-02-22 07:29:10.410967 pyp2rpm-3.3.8/pyp2rpm/templates/
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     6002 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/pyp2rpm/templates/epel6.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4744 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/pyp2rpm/templates/epel7.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4955 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/pyp2rpm/templates/fedora.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1738 2021-06-13 22:58:14.000000 pyp2rpm-3.3.8/pyp2rpm/templates/macros.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4854 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/pyp2rpm/templates/mageia.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     5259 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/pyp2rpm/templates/pld.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     5318 2019-08-04 21:57:28.000000 pyp2rpm-3.3.8/pyp2rpm/utils.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)       18 2022-02-22 07:28:50.000000 pyp2rpm-3.3.8/pyp2rpm/version.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4338 2021-06-20 21:10:20.000000 pyp2rpm-3.3.8/pyp2rpm/virtualenv.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3487 2019-08-04 21:57:28.000000 pyp2rpm-3.3.8/pyp2rpm.1
-drwxrwxr-x   0 gordon   (556600005) gordon   (556600005)        0 2022-02-22 07:29:10.409967 pyp2rpm-3.3.8/pyp2rpm.egg-info/
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1350 2022-02-22 07:29:10.000000 pyp2rpm-3.3.8/pyp2rpm.egg-info/PKG-INFO
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     2567 2022-02-22 07:29:10.000000 pyp2rpm-3.3.8/pyp2rpm.egg-info/SOURCES.txt
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)        1 2022-02-22 07:29:10.000000 pyp2rpm-3.3.8/pyp2rpm.egg-info/dependency_links.txt
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)       46 2022-02-22 07:29:10.000000 pyp2rpm-3.3.8/pyp2rpm.egg-info/entry_points.txt
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)       82 2022-02-22 07:29:10.000000 pyp2rpm-3.3.8/pyp2rpm.egg-info/requires.txt
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)        8 2022-02-22 07:29:10.000000 pyp2rpm-3.3.8/pyp2rpm.egg-info/top_level.txt
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)       63 2022-02-22 07:29:10.414967 pyp2rpm-3.3.8/setup.cfg
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3071 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/setup.py
-drwxrwxr-x   0 gordon   (556600005) gordon   (556600005)        0 2022-02-22 07:29:10.410967 pyp2rpm-3.3.8/tests/
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4170 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_archive.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     5132 2021-06-14 00:00:02.000000 pyp2rpm-3.3.8/tests/test_convertor.py
-drwxrwxr-x   0 gordon   (556600005) gordon   (556600005)        0 2022-02-22 07:29:10.413967 pyp2rpm-3.3.8/tests/test_data/
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)      164 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_data/LICENSE
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)  1386619 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_data/Sphinx-1.1.3-py2.6.egg
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    46455 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_data/bitarray-0.8.0.tar.gz
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1806 2021-06-28 15:08:43.000000 pyp2rpm-3.3.8/tests/test_data/coverage_pth-0.0.1.tar.gz
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    27730 2021-06-20 21:10:20.000000 pyp2rpm-3.3.8/tests/test_data/django.json
-drwxrwxr-x   0 gordon   (556600005) gordon   (556600005)        0 2022-02-22 07:29:10.413967 pyp2rpm-3.3.8/tests/test_data/isholiday-0.1/
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)      290 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/tests/test_data/isholiday-0.1/PKG-INFO
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1541 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/tests/test_data/isholiday-0.1/isholiday.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)       59 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/tests/test_data/isholiday-0.1/setup.cfg
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)      362 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/tests/test_data/isholiday-0.1/setup.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    64384 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_data/netjsonconfig-0.5.1.tar.gz
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    29417 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_data/pkginfo-1.2b1.tar.gz
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    28193 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_data/plumbum-0.9.0.tar.gz
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)   270730 2021-06-14 00:00:02.000000 pyp2rpm-3.3.8/tests/test_data/py2exe-0.9.2.2-py33.py34-none-any.whl
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)   307445 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_data/pytest-2.2.3.zip
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3556 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/tests/test_data/python-Jinja2_dnfnc.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1950 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/tests/test_data/python-Jinja2_epel6_dnfnc.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1950 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/tests/test_data/python-Jinja2_epel6_nc.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3931 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/tests/test_data/python-Jinja2_epel7_dnfnc.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3931 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/tests/test_data/python-Jinja2_epel7_nc.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3634 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/tests/test_data/python-Jinja2_mageia_py23.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3556 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/tests/test_data/python-Jinja2_nc.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3611 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/tests/test_data/python-Jinja2_py23_autonc.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     2451 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/tests/test_data/python-Jinja2_py2_autonc.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     2449 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/tests/test_data/python-Jinja2_py3_autonc.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1904 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/tests/test_data/python-paperwork-backend.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     6432 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/tests/test_data/python-sphinx_autonc.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1023 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/tests/test_data/python-utest.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1175 2021-12-19 21:38:02.000000 pyp2rpm-3.3.8/tests/test_data/python-utest_epel7.spec
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3236 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_data/restsh-0.1.tar.gz
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)   472023 2021-06-14 00:00:02.000000 pyp2rpm-3.3.8/tests/test_data/setuptools-19.6-py2.py3-none-any.whl
-drwxrwxr-x   0 gordon   (556600005) gordon   (556600005)        0 2022-02-22 07:29:10.413967 pyp2rpm-3.3.8/tests/test_data/utest/
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)      754 2021-06-13 22:58:14.000000 pyp2rpm-3.3.8/tests/test_data/utest/setup.py
-drwxrwxr-x   0 gordon   (556600005) gordon   (556600005)        0 2022-02-22 07:29:10.413967 pyp2rpm-3.3.8/tests/test_data/utest/utest/
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)        0 2021-06-13 22:58:14.000000 pyp2rpm-3.3.8/tests/test_data/utest/utest/__init__.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    19089 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_data/versiontools-1.9.1.tar.gz
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     2406 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/tests/test_dependency_parser.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)      954 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_extract_distribution.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1837 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_filters.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     5633 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/tests/test_integration.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    17866 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/tests/test_metadata_extractors.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     5301 2022-01-01 23:54:41.000000 pyp2rpm-3.3.8/tests/test_name_convertor.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1918 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_package_data.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     6925 2021-06-20 21:10:20.000000 pyp2rpm-3.3.8/tests/test_package_getters.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     2983 2019-07-25 22:42:31.000000 pyp2rpm-3.3.8/tests/test_utils.py
--rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4776 2021-06-20 21:10:20.000000 pyp2rpm-3.3.8/tests/test_virtualenv.py
+drwxr-xr-x   0 gordon   (556600005) gordon   (556600005)        0 2023-04-07 01:53:06.824486 pyp2rpm-3.3.9/
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     7407 2023-04-07 01:52:56.000000 pyp2rpm-3.3.9/CHANGELOG
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1113 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/LICENSE
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)      647 2023-04-06 05:31:18.000000 pyp2rpm-3.3.9/MANIFEST.in
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     1331 2023-04-07 01:53:06.824486 pyp2rpm-3.3.9/PKG-INFO
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     5246 2023-04-07 01:26:32.000000 pyp2rpm-3.3.9/README.md
+drwxr-xr-x   0 gordon   (556600005) gordon   (556600005)        0 2023-04-07 01:53:06.820486 pyp2rpm-3.3.9/pyp2rpm/
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)       65 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/pyp2rpm/__init__.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    11259 2021-06-14 00:00:02.000000 pyp2rpm-3.3.9/pyp2rpm/archive.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    10767 2021-06-20 21:10:20.000000 pyp2rpm-3.3.9/pyp2rpm/bin.py
+drwxr-xr-x   0 gordon   (556600005) gordon   (556600005)        0 2023-04-07 01:53:06.820486 pyp2rpm-3.3.9/pyp2rpm/command/
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)        0 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/pyp2rpm/command/__init__.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3380 2019-08-04 21:57:28.000000 pyp2rpm-3.3.9/pyp2rpm/command/extract_dist.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    12735 2021-06-20 06:55:08.000000 pyp2rpm-3.3.9/pyp2rpm/convertor.py
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     7427 2023-04-06 05:31:18.000000 pyp2rpm-3.3.9/pyp2rpm/dependency_convert.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4210 2021-06-13 22:58:14.000000 pyp2rpm-3.3.9/pyp2rpm/dependency_parser.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)      444 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/pyp2rpm/exceptions.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4406 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/pyp2rpm/filters.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1676 2019-10-03 22:55:20.000000 pyp2rpm-3.3.9/pyp2rpm/logger.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    22117 2022-02-22 07:02:20.000000 pyp2rpm-3.3.9/pyp2rpm/metadata_extractors.py
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     2763 2023-04-06 05:31:18.000000 pyp2rpm-3.3.9/pyp2rpm/module_runners.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    10264 2019-09-29 18:05:53.000000 pyp2rpm-3.3.9/pyp2rpm/name_convertor.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4030 2021-06-13 22:58:14.000000 pyp2rpm-3.3.9/pyp2rpm/package_data.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     8957 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/pyp2rpm/package_getters.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     5290 2021-06-13 22:58:14.000000 pyp2rpm-3.3.9/pyp2rpm/settings.py
+drwxr-xr-x   0 gordon   (556600005) gordon   (556600005)        0 2023-04-07 01:53:06.820486 pyp2rpm-3.3.9/pyp2rpm/templates/
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     6002 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/pyp2rpm/templates/epel6.spec
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     4743 2023-04-07 01:26:29.000000 pyp2rpm-3.3.9/pyp2rpm/templates/epel7.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4955 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/pyp2rpm/templates/fedora.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1738 2021-06-13 22:58:14.000000 pyp2rpm-3.3.9/pyp2rpm/templates/macros.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4854 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/pyp2rpm/templates/mageia.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     5259 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/pyp2rpm/templates/pld.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     5318 2019-08-04 21:57:28.000000 pyp2rpm-3.3.9/pyp2rpm/utils.py
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)       18 2023-04-07 01:52:56.000000 pyp2rpm-3.3.9/pyp2rpm/version.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4338 2021-06-20 21:10:20.000000 pyp2rpm-3.3.9/pyp2rpm/virtualenv.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3487 2019-08-04 21:57:28.000000 pyp2rpm-3.3.9/pyp2rpm.1
+drwxr-xr-x   0 gordon   (556600005) gordon   (556600005)        0 2023-04-07 01:53:06.820486 pyp2rpm-3.3.9/pyp2rpm.egg-info/
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1331 2023-04-07 01:53:06.000000 pyp2rpm-3.3.9/pyp2rpm.egg-info/PKG-INFO
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     2567 2023-04-07 01:53:06.000000 pyp2rpm-3.3.9/pyp2rpm.egg-info/SOURCES.txt
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)        1 2023-04-07 01:53:06.000000 pyp2rpm-3.3.9/pyp2rpm.egg-info/dependency_links.txt
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)       45 2023-04-07 01:53:06.000000 pyp2rpm-3.3.9/pyp2rpm.egg-info/entry_points.txt
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)       82 2023-04-07 01:53:06.000000 pyp2rpm-3.3.9/pyp2rpm.egg-info/requires.txt
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)        8 2023-04-07 01:53:06.000000 pyp2rpm-3.3.9/pyp2rpm.egg-info/top_level.txt
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)       63 2023-04-07 01:53:06.825486 pyp2rpm-3.3.9/setup.cfg
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     3228 2023-04-07 01:26:29.000000 pyp2rpm-3.3.9/setup.py
+drwxr-xr-x   0 gordon   (556600005) gordon   (556600005)        0 2023-04-07 01:53:06.821486 pyp2rpm-3.3.9/tests/
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4170 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_archive.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     5132 2021-06-14 00:00:02.000000 pyp2rpm-3.3.9/tests/test_convertor.py
+drwxr-xr-x   0 gordon   (556600005) gordon   (556600005)        0 2023-04-07 01:53:06.824486 pyp2rpm-3.3.9/tests/test_data/
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)      164 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_data/LICENSE
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)  1386619 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_data/Sphinx-1.1.3-py2.6.egg
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    46455 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_data/bitarray-0.8.0.tar.gz
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1806 2021-06-28 15:08:43.000000 pyp2rpm-3.3.9/tests/test_data/coverage_pth-0.0.1.tar.gz
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    27730 2021-06-20 21:10:20.000000 pyp2rpm-3.3.9/tests/test_data/django.json
+drwxr-xr-x   0 gordon   (556600005) gordon   (556600005)        0 2023-04-07 01:53:06.824486 pyp2rpm-3.3.9/tests/test_data/isholiday-0.1/
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)      290 2023-04-06 05:31:18.000000 pyp2rpm-3.3.9/tests/test_data/isholiday-0.1/PKG-INFO
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     1541 2023-04-06 05:31:18.000000 pyp2rpm-3.3.9/tests/test_data/isholiday-0.1/isholiday.py
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)       59 2023-04-06 05:31:18.000000 pyp2rpm-3.3.9/tests/test_data/isholiday-0.1/setup.cfg
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)      362 2023-04-06 05:31:18.000000 pyp2rpm-3.3.9/tests/test_data/isholiday-0.1/setup.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    64384 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_data/netjsonconfig-0.5.1.tar.gz
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    29417 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_data/pkginfo-1.2b1.tar.gz
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    28193 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_data/plumbum-0.9.0.tar.gz
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)   270730 2021-06-14 00:00:02.000000 pyp2rpm-3.3.9/tests/test_data/py2exe-0.9.2.2-py33.py34-none-any.whl
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)   307445 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_data/pytest-2.2.3.zip
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3556 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/tests/test_data/python-Jinja2_dnfnc.spec
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     1950 2023-04-06 05:31:18.000000 pyp2rpm-3.3.9/tests/test_data/python-Jinja2_epel6_dnfnc.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1950 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/tests/test_data/python-Jinja2_epel6_nc.spec
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     3948 2023-04-07 01:26:29.000000 pyp2rpm-3.3.9/tests/test_data/python-Jinja2_epel7_dnfnc.spec
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     3948 2023-04-07 01:26:29.000000 pyp2rpm-3.3.9/tests/test_data/python-Jinja2_epel7_nc.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3634 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/tests/test_data/python-Jinja2_mageia_py23.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3556 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/tests/test_data/python-Jinja2_nc.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3611 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/tests/test_data/python-Jinja2_py23_autonc.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     2451 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/tests/test_data/python-Jinja2_py2_autonc.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     2449 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/tests/test_data/python-Jinja2_py3_autonc.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1904 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/tests/test_data/python-paperwork-backend.spec
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     6432 2023-04-06 05:31:18.000000 pyp2rpm-3.3.9/tests/test_data/python-sphinx_autonc.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1023 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/tests/test_data/python-utest.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1175 2021-12-19 21:38:02.000000 pyp2rpm-3.3.9/tests/test_data/python-utest_epel7.spec
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     3236 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_data/restsh-0.1.tar.gz
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)   472023 2021-06-14 00:00:02.000000 pyp2rpm-3.3.9/tests/test_data/setuptools-19.6-py2.py3-none-any.whl
+drwxr-xr-x   0 gordon   (556600005) gordon   (556600005)        0 2023-04-07 01:53:06.824486 pyp2rpm-3.3.9/tests/test_data/utest/
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)      754 2021-06-13 22:58:14.000000 pyp2rpm-3.3.9/tests/test_data/utest/setup.py
+drwxr-xr-x   0 gordon   (556600005) gordon   (556600005)        0 2023-04-07 01:53:06.824486 pyp2rpm-3.3.9/tests/test_data/utest/utest/
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)        0 2021-06-13 22:58:14.000000 pyp2rpm-3.3.9/tests/test_data/utest/utest/__init__.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)    19089 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_data/versiontools-1.9.1.tar.gz
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     2299 2023-04-07 01:26:29.000000 pyp2rpm-3.3.9/tests/test_dependency_parser.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)      954 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_extract_distribution.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1837 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_filters.py
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     5633 2023-04-06 05:31:18.000000 pyp2rpm-3.3.9/tests/test_integration.py
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)    17866 2023-04-06 05:31:18.000000 pyp2rpm-3.3.9/tests/test_metadata_extractors.py
+-rw-r--r--   0 gordon   (556600005) gordon   (556600005)     5301 2023-04-06 05:31:18.000000 pyp2rpm-3.3.9/tests/test_name_convertor.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     1918 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_package_data.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     6925 2021-06-20 21:10:20.000000 pyp2rpm-3.3.9/tests/test_package_getters.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     2983 2019-07-25 22:42:31.000000 pyp2rpm-3.3.9/tests/test_utils.py
+-rw-rw-r--   0 gordon   (556600005) gordon   (556600005)     4776 2021-06-20 21:10:20.000000 pyp2rpm-3.3.9/tests/test_virtualenv.py
```

### Comparing `pyp2rpm-3.3.8/CHANGELOG` & `pyp2rpm-3.3.9/CHANGELOG`

 * *Files 2% similar despite different names*

```diff
@@ -1,7 +1,11 @@
+3.3.9
+* Fix tests when using setuptools >= 67 (issue #290)
+* Use sphinx-build-%{python3_version} on EPEL7 (issue #272)
+
 3.3.8
 * Sync dependency conversion with pyreq2rpm
 
 3.3.7
 * Ensure that all tests pass under Python 3.10
 * Include rc/post/dev in version (issue #259)
 * Handle all-zero versions without crashing
```

### Comparing `pyp2rpm-3.3.8/LICENSE` & `pyp2rpm-3.3.9/LICENSE`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/MANIFEST.in` & `pyp2rpm-3.3.9/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/PKG-INFO` & `pyp2rpm-3.3.9/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,17 +1,16 @@
 Metadata-Version: 2.1
 Name: pyp2rpm
-Version: 3.3.8
+Version: 3.3.9
 Summary: Convert Python packages to RPM SPECFILES
 Home-page: https://github.com/fedora-python/pyp2rpm
 Author: Bohuslav "Slavek" Kabrda, Robert Kuska, Michal Cyprian, Iryna Shcherbina
 Author-email: bkabrda@redhat.com, rkuska@redhat.com, mcyprian@redhat.com, ishcherb@redhat.com
 License: MIT
 Keywords: pypi,rpm,spec,specfile,convert
-Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Console
 Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: System Administrators
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: POSIX :: Linux
 Classifier: Programming Language :: Python
@@ -24,8 +23,7 @@
 
 Convert Python packages to RPM SPECFILES. The packages can be downloaded from
 PyPI and the produced SPEC is in line with Fedora Packaging Guidelines or Mageia Python Policy.
 
 Users can provide their own templates for rendering the package metadata. Both the package
 source and metadata can be extracted from PyPI or from local filesystem (local file doesn't
 provide that much information though).
-
```

### Comparing `pyp2rpm-3.3.8/README.md` & `pyp2rpm-3.3.9/README.md`

 * *Files 9% similar despite different names*

```diff
@@ -1,32 +1,36 @@
 
 ![Logo](https://rkuska.fedorapeople.org/pyp2rpm_large.png)
 
 pyp2rpm
 =======
 
-A tool to convert a PyPI package to an RPM SPECFILE or to generate an SRPM.
+A tool to convert a PyPI package to an RPM `SPECFILE` or to generate an SRPM.
 Under heavy development, see the TODO file for a list of planned features.
 pyp2rpm currently ships with Fedora and Mageia specific templates.
 
 ## Usage
 
 The simplest use case is to run:
+```sh
+pyp2rpm package_name
+```
 
-    pyp2rpm package_name
-
-This downloads the package from PyPI and outputs the RPM SPECFILE.
+This downloads the package from PyPI and outputs the RPM `SPECFILE`.
 
 Or:
-
-    pyp2rpm package_name --srpm
+```sh
+pyp2rpm package_name --srpm
+```
 
 This downloads the package from PyPI and creates a SRPM file.
 
-All of the options are (print this by running pyp2rpm -h):
+All of the `pyp2rpm` options are:
+
+    $ pyp2rpm -h
 
     usage: pyp2rpm [-h] [-v VERSION] [-d SAVE_DIR] [-r RPM_NAME]
                    [-t TEMPLATE] [-o DISTRO] [-b BASE_PYTHON]
                    [-p PYTHON_VERSION] [--srpm] [--proxy PROXY] PACKAGE
 
     Convert PyPI package to RPM specfile or SRPM.
 
@@ -86,30 +90,35 @@
                                   the SCL (to convert Requires/BuildRequires
                                   properly). Lines in the file are in form of
                                   "pkg-name %%{?custom_prefix}", where the prefix
                                   part is optional.
 
 
 To run the unit tests, cd into the checked out directory and run:
-
-    PYTHONPATH=$(pwd) py.test
+```sh
+PYTHONPATH="$(pwd)" py.test
+```
 
 or run:
-
-    python setup.py test
+```sh
+python setup.py test
+```
 
 
 ## Example usage
 
 ![alt tag](https://mcyprian.fedorapeople.org/pyp2rpm_guide.gif
 "Record of pyp2rpm usage")
 
 ## Contributing
 
 We will gladly accept any pull request or feature request.
 With complex pull requests, please include unit tests in *pytest* and use *flexmock* if you need mocking.
 
-Tests can be run locally using docker:
- docker build -t pyp2rpm-test .
- docker run -v $(pwd):$(pwd):z -w $(pwd) -it pyp2rpm-test
+Tests can be run in a local container:
+
+```sh
+docker build -t pyp2rpm-test .
+docker run -v "$(pwd):$(pwd):z" -w "$(pwd)" -it pyp2rpm-test
+```
 
 pyp2rpm is licensed under the MIT/Expat license.
```

### Comparing `pyp2rpm-3.3.8/pyp2rpm/archive.py` & `pyp2rpm-3.3.9/pyp2rpm/archive.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/bin.py` & `pyp2rpm-3.3.9/pyp2rpm/bin.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/command/extract_dist.py` & `pyp2rpm-3.3.9/pyp2rpm/command/extract_dist.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/convertor.py` & `pyp2rpm-3.3.9/pyp2rpm/convertor.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/dependency_convert.py` & `pyp2rpm-3.3.9/pyp2rpm/dependency_convert.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/dependency_parser.py` & `pyp2rpm-3.3.9/pyp2rpm/dependency_parser.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/filters.py` & `pyp2rpm-3.3.9/pyp2rpm/filters.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/logger.py` & `pyp2rpm-3.3.9/pyp2rpm/logger.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/metadata_extractors.py` & `pyp2rpm-3.3.9/pyp2rpm/metadata_extractors.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/module_runners.py` & `pyp2rpm-3.3.9/pyp2rpm/module_runners.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/name_convertor.py` & `pyp2rpm-3.3.9/pyp2rpm/name_convertor.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/package_data.py` & `pyp2rpm-3.3.9/pyp2rpm/package_data.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/package_getters.py` & `pyp2rpm-3.3.9/pyp2rpm/package_getters.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/settings.py` & `pyp2rpm-3.3.9/pyp2rpm/settings.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/templates/epel6.spec` & `pyp2rpm-3.3.9/pyp2rpm/templates/epel6.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/templates/epel7.spec` & `pyp2rpm-3.3.9/pyp2rpm/templates/epel7.spec`

 * *Files 0% similar despite different names*

```diff
@@ -47,15 +47,15 @@
 
 %build
 {%- for pv in data.sorted_python_versions %}
 {% if data.has_extension %}CFLAGS="$RPM_OPT_FLAGS" {% endif %}%{__python{{ pv }}} setup.py build
 {%- endfor %}
 {%- if data.sphinx_dir %}
 # generate html docs
-PYTHONPATH=${PWD} {{ "sphinx-build"|script_name_for_python_version(data.base_python_version, False, False) }} {{ data.sphinx_dir }} html
+PYTHONPATH=${PWD} {{ "sphinx-build"|script_name_for_python_version(data.base_python_version, True, False) }} {{ data.sphinx_dir }} html
 # remove the sphinx-build leftovers
 rm -rf html/.{doctrees,buildinfo}
 {%- endif %}
 
 %install
 {%- if data.python_versions|length > 0 %}
 # Must do the default python version install last because
```

### Comparing `pyp2rpm-3.3.8/pyp2rpm/templates/fedora.spec` & `pyp2rpm-3.3.9/pyp2rpm/templates/fedora.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/templates/macros.spec` & `pyp2rpm-3.3.9/pyp2rpm/templates/macros.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/templates/mageia.spec` & `pyp2rpm-3.3.9/pyp2rpm/templates/mageia.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/templates/pld.spec` & `pyp2rpm-3.3.9/pyp2rpm/templates/pld.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/utils.py` & `pyp2rpm-3.3.9/pyp2rpm/utils.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm/virtualenv.py` & `pyp2rpm-3.3.9/pyp2rpm/virtualenv.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm.1` & `pyp2rpm-3.3.9/pyp2rpm.1`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/pyp2rpm.egg-info/PKG-INFO` & `pyp2rpm-3.3.9/pyp2rpm.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,17 +1,16 @@
 Metadata-Version: 2.1
 Name: pyp2rpm
-Version: 3.3.8
+Version: 3.3.9
 Summary: Convert Python packages to RPM SPECFILES
 Home-page: https://github.com/fedora-python/pyp2rpm
 Author: Bohuslav "Slavek" Kabrda, Robert Kuska, Michal Cyprian, Iryna Shcherbina
 Author-email: bkabrda@redhat.com, rkuska@redhat.com, mcyprian@redhat.com, ishcherb@redhat.com
 License: MIT
 Keywords: pypi,rpm,spec,specfile,convert
-Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Console
 Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: System Administrators
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: POSIX :: Linux
 Classifier: Programming Language :: Python
@@ -24,8 +23,7 @@
 
 Convert Python packages to RPM SPECFILES. The packages can be downloaded from
 PyPI and the produced SPEC is in line with Fedora Packaging Guidelines or Mageia Python Policy.
 
 Users can provide their own templates for rendering the package metadata. Both the package
 source and metadata can be extracted from PyPI or from local filesystem (local file doesn't
 provide that much information though).
-
```

### Comparing `pyp2rpm-3.3.8/pyp2rpm.egg-info/SOURCES.txt` & `pyp2rpm-3.3.9/pyp2rpm.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/setup.py` & `pyp2rpm-3.3.9/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -54,15 +54,17 @@
     setup_requires=['setuptools',
                     'flexmock >= 0.9.3',
                     'pytest-runner',
                     'click',
                     'Jinja2',
                     ],
     tests_require=['packaging < 21;python_version<"3.5"', 'pytest < 5;python_version<"3.5"',
-                   'pytest < 6.2;python_version=="3.5"', 'pytest;python_version>="3.6"'],
+                   'pytest < 6.2;python_version=="3.5"', 'pytest < 7.1;python_version=="3.6"',
+                   'iniconfig < 2.0;python_version=="3.6"',
+                   'pytest;python_version>="3.7"', 'attrs < 21.1.0;python_version<"3.5"',],
     extras_require={
         'venv metadata': ['virtualenv-api'],
         'sclize': ['spec2scl >= 1.2.0']
     },
     classifiers=['Development Status :: 4 - Beta',
                  'Environment :: Console',
                  'Intended Audience :: Developers',
```

### Comparing `pyp2rpm-3.3.8/tests/test_archive.py` & `pyp2rpm-3.3.9/tests/test_archive.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_convertor.py` & `pyp2rpm-3.3.9/tests/test_convertor.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/Sphinx-1.1.3-py2.6.egg` & `pyp2rpm-3.3.9/tests/test_data/Sphinx-1.1.3-py2.6.egg`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/bitarray-0.8.0.tar.gz` & `pyp2rpm-3.3.9/tests/test_data/bitarray-0.8.0.tar.gz`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/coverage_pth-0.0.1.tar.gz` & `pyp2rpm-3.3.9/tests/test_data/coverage_pth-0.0.1.tar.gz`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/django.json` & `pyp2rpm-3.3.9/tests/test_data/django.json`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/isholiday-0.1/isholiday.py` & `pyp2rpm-3.3.9/tests/test_data/isholiday-0.1/isholiday.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/netjsonconfig-0.5.1.tar.gz` & `pyp2rpm-3.3.9/tests/test_data/netjsonconfig-0.5.1.tar.gz`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/pkginfo-1.2b1.tar.gz` & `pyp2rpm-3.3.9/tests/test_data/pkginfo-1.2b1.tar.gz`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/plumbum-0.9.0.tar.gz` & `pyp2rpm-3.3.9/tests/test_data/plumbum-0.9.0.tar.gz`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/py2exe-0.9.2.2-py33.py34-none-any.whl` & `pyp2rpm-3.3.9/tests/test_data/py2exe-0.9.2.2-py33.py34-none-any.whl`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/pytest-2.2.3.zip` & `pyp2rpm-3.3.9/tests/test_data/pytest-2.2.3.zip`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-Jinja2_dnfnc.spec` & `pyp2rpm-3.3.9/tests/test_data/python-Jinja2_dnfnc.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-Jinja2_epel6_dnfnc.spec` & `pyp2rpm-3.3.9/tests/test_data/python-Jinja2_epel6_dnfnc.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-Jinja2_epel6_nc.spec` & `pyp2rpm-3.3.9/tests/test_data/python-Jinja2_epel6_nc.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-Jinja2_epel7_dnfnc.spec` & `pyp2rpm-3.3.9/tests/test_data/python-Jinja2_epel7_dnfnc.spec`

 * *Files 2% similar despite different names*

```diff
@@ -67,15 +67,15 @@
 # Remove bundled egg-info
 rm -rf %{pypi_name}.egg-info
 
 %build
 %{__python2} setup.py build
 %{__python3} setup.py build
 # generate html docs
-PYTHONPATH=${PWD} sphinx-build-3 docs html
+PYTHONPATH=${PWD} sphinx-build-%{python3_version} docs html
 # remove the sphinx-build leftovers
 rm -rf html/.{doctrees,buildinfo}
 
 %install
 # Must do the default python version install last because
 # the scripts in /usr/bin are overwritten with every setup.py install.
 %{__python2} setup.py install --skip-build --root %{buildroot}
```

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-Jinja2_epel7_nc.spec` & `pyp2rpm-3.3.9/tests/test_data/python-Jinja2_epel7_nc.spec`

 * *Files 2% similar despite different names*

```diff
@@ -67,15 +67,15 @@
 # Remove bundled egg-info
 rm -rf %{pypi_name}.egg-info
 
 %build
 %{__python2} setup.py build
 %{__python3} setup.py build
 # generate html docs
-PYTHONPATH=${PWD} sphinx-build-3 docs html
+PYTHONPATH=${PWD} sphinx-build-%{python3_version} docs html
 # remove the sphinx-build leftovers
 rm -rf html/.{doctrees,buildinfo}
 
 %install
 # Must do the default python version install last because
 # the scripts in /usr/bin are overwritten with every setup.py install.
 %{__python2} setup.py install --skip-build --root %{buildroot}
```

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-Jinja2_mageia_py23.spec` & `pyp2rpm-3.3.9/tests/test_data/python-Jinja2_mageia_py23.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-Jinja2_nc.spec` & `pyp2rpm-3.3.9/tests/test_data/python-Jinja2_nc.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-Jinja2_py23_autonc.spec` & `pyp2rpm-3.3.9/tests/test_data/python-Jinja2_py23_autonc.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-Jinja2_py2_autonc.spec` & `pyp2rpm-3.3.9/tests/test_data/python-Jinja2_py2_autonc.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-Jinja2_py3_autonc.spec` & `pyp2rpm-3.3.9/tests/test_data/python-Jinja2_py3_autonc.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-paperwork-backend.spec` & `pyp2rpm-3.3.9/tests/test_data/python-paperwork-backend.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-sphinx_autonc.spec` & `pyp2rpm-3.3.9/tests/test_data/python-sphinx_autonc.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-utest.spec` & `pyp2rpm-3.3.9/tests/test_data/python-utest.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/python-utest_epel7.spec` & `pyp2rpm-3.3.9/tests/test_data/python-utest_epel7.spec`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/restsh-0.1.tar.gz` & `pyp2rpm-3.3.9/tests/test_data/restsh-0.1.tar.gz`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/setuptools-19.6-py2.py3-none-any.whl` & `pyp2rpm-3.3.9/tests/test_data/setuptools-19.6-py2.py3-none-any.whl`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/utest/setup.py` & `pyp2rpm-3.3.9/tests/test_data/utest/setup.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_data/versiontools-1.9.1.tar.gz` & `pyp2rpm-3.3.9/tests/test_data/versiontools-1.9.1.tar.gz`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_dependency_parser.py` & `pyp2rpm-3.3.9/tests/test_dependency_parser.py`

 * *Files 5% similar despite different names*

```diff
@@ -50,17 +50,14 @@
          ),
         ('pyp2rpm~=0.9.3', True, True,
          [['Requires', 'pyp2rpm', '({name} >= 0.9.3 with {name} < 0.10)']]
          ),
         ('pyp2rpm~=0.9.3.1', True, True,
          [['Requires', 'pyp2rpm', '({name} >= 0.9.3.1 with {name} < 0.9.4)']]
          ),
-        ('nb2plots>0+unknown', True, True,
-         [['Requires', 'nb2plots', '{name} > 0.0']]
-         ),
 
     ])
     def test_dependency_to_rpm(self, d, r, rich, expected):
         # we can't convert lists of lists into sets => compare len and contents
         rpm_deps = dependency_to_rpm(R.parse(d), r, rich)
         for dep in expected:
             assert dep in rpm_deps
```

### Comparing `pyp2rpm-3.3.8/tests/test_extract_distribution.py` & `pyp2rpm-3.3.9/tests/test_extract_distribution.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_filters.py` & `pyp2rpm-3.3.9/tests/test_filters.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_integration.py` & `pyp2rpm-3.3.9/tests/test_integration.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_metadata_extractors.py` & `pyp2rpm-3.3.9/tests/test_metadata_extractors.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_name_convertor.py` & `pyp2rpm-3.3.9/tests/test_name_convertor.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_package_data.py` & `pyp2rpm-3.3.9/tests/test_package_data.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_package_getters.py` & `pyp2rpm-3.3.9/tests/test_package_getters.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_utils.py` & `pyp2rpm-3.3.9/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `pyp2rpm-3.3.8/tests/test_virtualenv.py` & `pyp2rpm-3.3.9/tests/test_virtualenv.py`

 * *Files identical despite different names*

