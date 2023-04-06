# Comparing `tmp/Faker-9.9.0.tar.gz` & `tmp/Faker-9.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "Faker-9.9.0.tar", last modified: Mon Nov 29 21:42:15 2021, max compression
+gzip compressed data, was "Faker-9.9.1.tar", last modified: Tue Dec  7 15:55:50 2021, max compression
```

## Comparing `Faker-9.9.0.tar` & `Faker-9.9.1.tar`

### file list

```diff
@@ -1,1100 +1,1100 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.351740 Faker-9.9.0/
--rw-r--r--   0 runner    (1001) docker     (121)    58369 2021-11-29 21:42:05.000000 Faker-9.9.0/CHANGELOG.md
--rw-r--r--   0 runner    (1001) docker     (121)      263 2021-11-29 21:42:04.000000 Faker-9.9.0/CITATION.cff
--rw-r--r--   0 runner    (1001) docker     (121)     1650 2021-11-29 21:42:04.000000 Faker-9.9.0/CONTRIBUTING.rst
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.235734 Faker-9.9.0/Faker.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    15284 2021-11-29 21:42:14.000000 Faker-9.9.0/Faker.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    23218 2021-11-29 21:42:15.000000 Faker-9.9.0/Faker.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-11-29 21:42:14.000000 Faker-9.9.0/Faker.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      111 2021-11-29 21:42:14.000000 Faker-9.9.0/Faker.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)       96 2021-11-29 21:42:14.000000 Faker-9.9.0/Faker.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        6 2021-11-29 21:42:14.000000 Faker-9.9.0/Faker.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-11-29 21:42:14.000000 Faker-9.9.0/Faker.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)     1060 2021-11-29 21:42:04.000000 Faker-9.9.0/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (121)      582 2021-11-29 21:42:04.000000 Faker-9.9.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)    15284 2021-11-29 21:42:15.351740 Faker-9.9.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    14109 2021-11-29 21:42:04.000000 Faker-9.9.0/README.rst
--rw-r--r--   0 runner    (1001) docker     (121)      815 2021-11-29 21:42:04.000000 Faker-9.9.0/RELEASE_PROCESS.rst
--rw-r--r--   0 runner    (1001) docker     (121)        6 2021-11-29 21:42:06.000000 Faker-9.9.0/VERSION
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.235734 Faker-9.9.0/faker/
--rw-r--r--   0 runner    (1001) docker     (121)      166 2021-11-29 21:42:06.000000 Faker-9.9.0/faker/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      107 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/__main__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9659 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/cli.py
--rw-r--r--   0 runner    (1001) docker     (121)      343 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/config.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.235734 Faker-9.9.0/faker/contrib/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/contrib/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.235734 Faker-9.9.0/faker/contrib/pytest/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/contrib/pytest/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1114 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/contrib/pytest/plugin.py
--rw-r--r--   0 runner    (1001) docker     (121)     3976 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/documentor.py
--rw-r--r--   0 runner    (1001) docker     (121)      506 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (121)     4552 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/factory.py
--rw-r--r--   0 runner    (1001) docker     (121)     6547 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/generator.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.235734 Faker-9.9.0/faker/providers/
--rw-r--r--   0 runner    (1001) docker     (121)    24669 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.235734 Faker-9.9.0/faker/providers/address/
--rw-r--r--   0 runner    (1001) docker     (121)     3683 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.235734 Faker-9.9.0/faker/providers/address/cs_CZ/
--rw-r--r--   0 runner    (1001) docker     (121)    26882 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/cs_CZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.235734 Faker-9.9.0/faker/providers/address/da_DK/
--rw-r--r--   0 runner    (1001) docker     (121)     7714 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/da_DK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/de/
--rw-r--r--   0 runner    (1001) docker     (121)     5668 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/de/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/de_AT/
--rw-r--r--   0 runner    (1001) docker     (121)     6261 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/de_AT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/de_CH/
--rw-r--r--   0 runner    (1001) docker     (121)     1962 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/de_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/de_DE/
--rw-r--r--   0 runner    (1001) docker     (121)    10232 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/de_DE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)   148988 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/en/
--rw-r--r--   0 runner    (1001) docker     (121)     5642 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/en/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/en_AU/
--rw-r--r--   0 runner    (1001) docker     (121)     6566 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/en_AU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/en_CA/
--rw-r--r--   0 runner    (1001) docker     (121)     8939 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/en_CA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/en_GB/
--rw-r--r--   0 runner    (1001) docker     (121)    10725 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/en_GB/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/en_IE/
--rw-r--r--   0 runner    (1001) docker     (121)     1336 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/en_IE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/en_IN/
--rw-r--r--   0 runner    (1001) docker     (121)     8591 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/en_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/en_NZ/
--rw-r--r--   0 runner    (1001) docker     (121)     7132 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/en_NZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/en_PH/
--rw-r--r--   0 runner    (1001) docker     (121)    43162 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/en_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.239734 Faker-9.9.0/faker/providers/address/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)    12268 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/es/
--rw-r--r--   0 runner    (1001) docker     (121)     4410 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/es/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/es_CO/
--rw-r--r--   0 runner    (1001) docker     (121)    42947 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/es_CO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/es_ES/
--rw-r--r--   0 runner    (1001) docker     (121)     3291 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/es_ES/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/es_MX/
--rw-r--r--   0 runner    (1001) docker     (121)     4914 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/es_MX/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/fa_IR/
--rw-r--r--   0 runner    (1001) docker     (121)     8017 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/fa_IR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/fi_FI/
--rw-r--r--   0 runner    (1001) docker     (121)    16854 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/fi_FI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/fil_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      164 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/fil_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/fr_CH/
--rw-r--r--   0 runner    (1001) docker     (121)     8682 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/fr_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)    11701 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/he_IL/
--rw-r--r--   0 runner    (1001) docker     (121)    16425 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/he_IL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/hi_IN/
--rw-r--r--   0 runner    (1001) docker     (121)     7699 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/hi_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/hr_HR/
--rwxr-xr-x   0 runner    (1001) docker     (121)    12722 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/hr_HR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/hu_HU/
--rw-r--r--   0 runner    (1001) docker     (121)    10954 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/hu_HU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/hy_AM/
--rw-r--r--   0 runner    (1001) docker     (121)    20543 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/hy_AM/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/id_ID/
--rw-r--r--   0 runner    (1001) docker     (121)    11528 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/id_ID/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/it_IT/
--rw-r--r--   0 runner    (1001) docker     (121)    10938 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/it_IT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/ja_JP/
--rw-r--r--   0 runner    (1001) docker     (121)    16159 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/ja_JP/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/ka_GE/
--rw-r--r--   0 runner    (1001) docker     (121)    53808 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/ka_GE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.243734 Faker-9.9.0/faker/providers/address/ko_KR/
--rw-r--r--   0 runner    (1001) docker     (121)    14994 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/ko_KR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/ne_NP/
--rw-r--r--   0 runner    (1001) docker     (121)    22771 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/ne_NP/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/nl_BE/
--rw-r--r--   0 runner    (1001) docker     (121)    65192 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/nl_BE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/nl_NL/
--rw-r--r--   0 runner    (1001) docker     (121)    57923 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/nl_NL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/no_NO/
--rw-r--r--   0 runner    (1001) docker     (121)     2490 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/no_NO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/pl_PL/
--rw-r--r--   0 runner    (1001) docker     (121)    14642 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/pl_PL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/pt_BR/
--rw-r--r--   0 runner    (1001) docker     (121)    22991 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/pt_BR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/pt_PT/
--rw-r--r--   0 runner    (1001) docker     (121)    38109 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/pt_PT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/ro_RO/
--rw-r--r--   0 runner    (1001) docker     (121)     9629 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/ro_RO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)    48537 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/sk_SK/
--rw-r--r--   0 runner    (1001) docker     (121)   122027 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/sk_SK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/sl_SI/
--rwxr-xr-x   0 runner    (1001) docker     (121)    42397 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/sl_SI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/sv_SE/
--rw-r--r--   0 runner    (1001) docker     (121)     8160 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/sv_SE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/ta_IN/
--rw-r--r--   0 runner    (1001) docker     (121)    16944 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/ta_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/th/
--rw-r--r--   0 runner    (1001) docker     (121)     9792 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/th/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)    12993 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/tl_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      164 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/tl_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.247734 Faker-9.9.0/faker/providers/address/uk_UA/
--rw-r--r--   0 runner    (1001) docker     (121)    75352 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/uk_UA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/address/zh_CN/
--rw-r--r--   0 runner    (1001) docker     (121)     9895 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/zh_CN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/address/zh_TW/
--rw-r--r--   0 runner    (1001) docker     (121)     8293 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/address/zh_TW/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/
--rw-r--r--   0 runner    (1001) docker     (121)      517 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/ar_JO/
--rw-r--r--   0 runner    (1001) docker     (121)     1567 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/ar_JO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/ar_PS/
--rw-r--r--   0 runner    (1001) docker     (121)     1744 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/ar_PS/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/ar_SA/
--rw-r--r--   0 runner    (1001) docker     (121)     2318 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/ar_SA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/de_DE/
--rw-r--r--   0 runner    (1001) docker     (121)     6463 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/de_DE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)      555 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/en_CA/
--rw-r--r--   0 runner    (1001) docker     (121)      919 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/en_CA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/en_GB/
--rw-r--r--   0 runner    (1001) docker     (121)      322 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/en_GB/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/en_NZ/
--rw-r--r--   0 runner    (1001) docker     (121)      640 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/en_NZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/en_PH/
--rw-r--r--   0 runner    (1001) docker     (121)     2476 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/en_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)     3280 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/es_CO/
--rw-r--r--   0 runner    (1001) docker     (121)      360 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/es_CO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/es_ES/
--rw-r--r--   0 runner    (1001) docker     (121)     3940 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/es_ES/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/fil_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      238 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/fil_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)      374 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.251735 Faker-9.9.0/faker/providers/automotive/he_IL/
--rw-r--r--   0 runner    (1001) docker     (121)      321 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/he_IL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/hu_HU/
--rw-r--r--   0 runner    (1001) docker     (121)      277 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/hu_HU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/id_ID/
--rw-r--r--   0 runner    (1001) docker     (121)      349 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/id_ID/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/nl_NL/
--rw-r--r--   0 runner    (1001) docker     (121)     2533 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/nl_NL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/no_NO/
--rw-r--r--   0 runner    (1001) docker     (121)      316 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/no_NO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/pl_PL/
--rw-r--r--   0 runner    (1001) docker     (121)     1007 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/pl_PL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/pt_BR/
--rw-r--r--   0 runner    (1001) docker     (121)      183 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/pt_BR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/pt_PT/
--rw-r--r--   0 runner    (1001) docker     (121)      391 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/pt_PT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/ro_RO/
--rw-r--r--   0 runner    (1001) docker     (121)     1181 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/ro_RO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)     7827 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/sk_SK/
--rw-r--r--   0 runner    (1001) docker     (121)     2641 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/sk_SK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/sv_SE/
--rw-r--r--   0 runner    (1001) docker     (121)      428 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/sv_SE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)      948 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/tl_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      237 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/tl_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/automotive/tr_TR/
--rw-r--r--   0 runner    (1001) docker     (121)      868 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/automotive/tr_TR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/bank/
--rw-r--r--   0 runner    (1001) docker     (121)     6121 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/bank/de_AT/
--rw-r--r--   0 runner    (1001) docker     (121)      190 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/de_AT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/bank/de_CH/
--rw-r--r--   0 runner    (1001) docker     (121)      191 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/de_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/bank/de_DE/
--rw-r--r--   0 runner    (1001) docker     (121)      192 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/de_DE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/bank/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)      197 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.255735 Faker-9.9.0/faker/providers/bank/en_GB/
--rw-r--r--   0 runner    (1001) docker     (121)      192 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/en_GB/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/en_IE/
--rw-r--r--   0 runner    (1001) docker     (121)      197 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/en_IE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/en_PH/
--rw-r--r--   0 runner    (1001) docker     (121)     2690 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/en_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/es_ES/
--rw-r--r--   0 runner    (1001) docker     (121)      194 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/es_ES/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/fi_FI/
--rw-r--r--   0 runner    (1001) docker     (121)      188 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/fi_FI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/fil_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      220 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/fil_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/fr_CH/
--rw-r--r--   0 runner    (1001) docker     (121)      219 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/fr_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)      197 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/it_CH/
--rw-r--r--   0 runner    (1001) docker     (121)      219 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/it_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/it_IT/
--rw-r--r--   0 runner    (1001) docker     (121)      197 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/it_IT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/nl_NL/
--rw-r--r--   0 runner    (1001) docker     (121)      188 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/nl_NL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/no_NO/
--rw-r--r--   0 runner    (1001) docker     (121)      185 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/no_NO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/pl_PL/
--rw-r--r--   0 runner    (1001) docker     (121)      180 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/pl_PL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/pt_PT/
--rw-r--r--   0 runner    (1001) docker     (121)      195 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/pt_PT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/ro_RO/
--rw-r--r--   0 runner    (1001) docker     (121)      883 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/ro_RO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)    21826 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)     1059 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/tl_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      219 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/tl_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/bank/tr_TR/
--rw-r--r--   0 runner    (1001) docker     (121)      196 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/bank/tr_TR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/barcode/
--rw-r--r--   0 runner    (1001) docker     (121)     3972 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/barcode/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/barcode/en_CA/
--rw-r--r--   0 runner    (1001) docker     (121)      664 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/barcode/en_CA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/barcode/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)    11356 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/barcode/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.259735 Faker-9.9.0/faker/providers/barcode/es_ES/
--rw-r--r--   0 runner    (1001) docker     (121)      244 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/barcode/es_ES/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/barcode/fr_CA/
--rw-r--r--   0 runner    (1001) docker     (121)      217 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/barcode/fr_CA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/barcode/ja_JP/
--rw-r--r--   0 runner    (1001) docker     (121)     1476 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/barcode/ja_JP/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/
--rw-r--r--   0 runner    (1001) docker     (121)     9113 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/ar_PS/
--rw-r--r--   0 runner    (1001) docker     (121)     6973 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/ar_PS/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/bg_BG/
--rw-r--r--   0 runner    (1001) docker     (121)     3337 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/bg_BG/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10362 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/color.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)     4247 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)      141 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/es_ES/
--rw-r--r--   0 runner    (1001) docker     (121)     6202 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/es_ES/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/fa_IR/
--rw-r--r--   0 runner    (1001) docker     (121)     7079 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/fa_IR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)     6038 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/he_IL/
--rw-r--r--   0 runner    (1001) docker     (121)     1729 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/he_IL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/hr_HR/
--rw-r--r--   0 runner    (1001) docker     (121)     6323 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/hr_HR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/hu_HU/
--rw-r--r--   0 runner    (1001) docker     (121)      444 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/hu_HU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/hy_AM/
--rw-r--r--   0 runner    (1001) docker     (121)     8297 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/hy_AM/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/pt_BR/
--rw-r--r--   0 runner    (1001) docker     (121)     9674 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/pt_BR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)     3402 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/sk_SK/
--rw-r--r--   0 runner    (1001) docker     (121)      469 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/sk_SK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)     1660 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/color/uk_UA/
--rw-r--r--   0 runner    (1001) docker     (121)    11365 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/color/uk_UA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/company/
--rw-r--r--   0 runner    (1001) docker     (121)    13647 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/company/bg_BG/
--rw-r--r--   0 runner    (1001) docker     (121)      552 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/bg_BG/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.263735 Faker-9.9.0/faker/providers/company/cs_CZ/
--rw-r--r--   0 runner    (1001) docker     (121)      309 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/cs_CZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/de_DE/
--rw-r--r--   0 runner    (1001) docker     (121)      753 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/de_DE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)      423 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/en_PH/
--rw-r--r--   0 runner    (1001) docker     (121)     3694 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/en_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)       87 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/es_MX/
--rw-r--r--   0 runner    (1001) docker     (121)    11494 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/es_MX/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/fa_IR/
--rw-r--r--   0 runner    (1001) docker     (121)    49816 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/fa_IR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/fi_FI/
--rw-r--r--   0 runner    (1001) docker     (121)     2067 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/fi_FI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/fil_PH/
--rw-r--r--   0 runner    (1001) docker     (121)     2750 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/fil_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/fr_CH/
--rw-r--r--   0 runner    (1001) docker     (121)     1313 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/fr_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)     3983 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/hr_HR/
--rwxr-xr-x   0 runner    (1001) docker     (121)      313 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/hr_HR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/hu_HU/
--rw-r--r--   0 runner    (1001) docker     (121)      488 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/hu_HU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/hy_AM/
--rw-r--r--   0 runner    (1001) docker     (121)     9891 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/hy_AM/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/id_ID/
--rw-r--r--   0 runner    (1001) docker     (121)      933 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/id_ID/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/it_IT/
--rw-r--r--   0 runner    (1001) docker     (121)     9716 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/it_IT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/ja_JP/
--rw-r--r--   0 runner    (1001) docker     (121)      762 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/ja_JP/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/ko_KR/
--rw-r--r--   0 runner    (1001) docker     (121)     9720 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/ko_KR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/nl_NL/
--rw-r--r--   0 runner    (1001) docker     (121)    11853 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/nl_NL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/no_NO/
--rw-r--r--   0 runner    (1001) docker     (121)      534 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/no_NO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/pl_PL/
--rw-r--r--   0 runner    (1001) docker     (121)     3912 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/pl_PL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/pt_BR/
--rw-r--r--   0 runner    (1001) docker     (121)     2972 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/pt_BR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.267736 Faker-9.9.0/faker/providers/company/pt_PT/
--rw-r--r--   0 runner    (1001) docker     (121)     1198 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/pt_PT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/company/ro_RO/
--rw-r--r--   0 runner    (1001) docker     (121)      639 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/ro_RO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/company/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)    45104 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/company/sk_SK/
--rw-r--r--   0 runner    (1001) docker     (121)      327 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/sk_SK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/company/sl_SI/
--rwxr-xr-x   0 runner    (1001) docker     (121)      255 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/sl_SI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/company/sv_SE/
--rw-r--r--   0 runner    (1001) docker     (121)      322 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/sv_SE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/company/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)     4169 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/company/tl_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      154 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/tl_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/company/tr_TR/
--rw-r--r--   0 runner    (1001) docker     (121)     1189 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/tr_TR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/company/zh_CN/
--rw-r--r--   0 runner    (1001) docker     (121)     2164 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/zh_CN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/company/zh_TW/
--rw-r--r--   0 runner    (1001) docker     (121)     3054 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/company/zh_TW/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/credit_card/
--rw-r--r--   0 runner    (1001) docker     (121)     7111 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/credit_card/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/credit_card/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)      157 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/credit_card/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/credit_card/fa_IR/
--rw-r--r--   0 runner    (1001) docker     (121)     5190 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/credit_card/fa_IR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/credit_card/pt_PT/
--rw-r--r--   0 runner    (1001) docker     (121)     5671 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/credit_card/pt_PT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/credit_card/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)     3179 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/credit_card/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/currency/
--rw-r--r--   0 runner    (1001) docker     (121)    10794 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/currency/cs_CZ/
--rw-r--r--   0 runner    (1001) docker     (121)      282 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/cs_CZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/currency/de_AT/
--rw-r--r--   0 runner    (1001) docker     (121)      292 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/de_AT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/currency/de_DE/
--rw-r--r--   0 runner    (1001) docker     (121)      285 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/de_DE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/currency/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)     7622 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/currency/en_AU/
--rw-r--r--   0 runner    (1001) docker     (121)      280 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/en_AU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.271736 Faker-9.9.0/faker/providers/currency/en_CA/
--rw-r--r--   0 runner    (1001) docker     (121)      273 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/en_CA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)      262 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/es_ES/
--rw-r--r--   0 runner    (1001) docker     (121)     6293 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/es_ES/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/fr_CA/
--rw-r--r--   0 runner    (1001) docker     (121)      280 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/fr_CA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)      285 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/it_IT/
--rw-r--r--   0 runner    (1001) docker     (121)      285 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/it_IT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/nl_NL/
--rw-r--r--   0 runner    (1001) docker     (121)      296 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/nl_NL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/pl_PL/
--rw-r--r--   0 runner    (1001) docker     (121)      282 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/pl_PL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/pt_BR/
--rw-r--r--   0 runner    (1001) docker     (121)      263 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/pt_BR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/ro_RO/
--rw-r--r--   0 runner    (1001) docker     (121)      282 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/ro_RO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)     8246 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/sk_SK/
--rw-r--r--   0 runner    (1001) docker     (121)      285 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/sk_SK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/sv_SE/
--rw-r--r--   0 runner    (1001) docker     (121)     5844 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/sv_SE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/currency/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)    10596 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/currency/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/date_time/
--rw-r--r--   0 runner    (1001) docker     (121)    81158 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/date_time/ar_AA/
--rw-r--r--   0 runner    (1001) docker     (121)    54779 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/ar_AA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/date_time/ar_EG/
--rw-r--r--   0 runner    (1001) docker     (121)      465 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/ar_EG/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.275736 Faker-9.9.0/faker/providers/date_time/bn_BD/
--rw-r--r--   0 runner    (1001) docker     (121)     1050 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/bn_BD/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/cs_CZ/
--rw-r--r--   0 runner    (1001) docker     (121)      785 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/cs_CZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/de_AT/
--rw-r--r--   0 runner    (1001) docker     (121)      781 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/de_AT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/de_DE/
--rw-r--r--   0 runner    (1001) docker     (121)      780 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/de_DE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)      957 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/en_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      144 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/en_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)       89 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/es_ES/
--rw-r--r--   0 runner    (1001) docker     (121)      780 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/es_ES/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/fil_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      829 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/fil_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)      869 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/hi_IN/
--rw-r--r--   0 runner    (1001) docker     (121)     1065 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/hi_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/hr_HR/
--rw-r--r--   0 runner    (1001) docker     (121)      885 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/hr_HR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/hu_HU/
--rw-r--r--   0 runner    (1001) docker     (121)      894 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/hu_HU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/hy_AM/
--rw-r--r--   0 runner    (1001) docker     (121)      929 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/hy_AM/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/id_ID/
--rw-r--r--   0 runner    (1001) docker     (121)      861 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/id_ID/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/it_IT/
--rw-r--r--   0 runner    (1001) docker     (121)      792 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/it_IT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/ko_KR/
--rw-r--r--   0 runner    (1001) docker     (121)      862 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/ko_KR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/nl_NL/
--rw-r--r--   0 runner    (1001) docker     (121)      783 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/nl_NL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/pl_PL/
--rw-r--r--   0 runner    (1001) docker     (121)      801 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/pl_PL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/pt_BR/
--rw-r--r--   0 runner    (1001) docker     (121)      807 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/pt_BR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/pt_PT/
--rw-r--r--   0 runner    (1001) docker     (121)      807 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/pt_PT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/ro_RO/
--rw-r--r--   0 runner    (1001) docker     (121)      782 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/ro_RO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)    55616 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.279736 Faker-9.9.0/faker/providers/date_time/sk_SK/
--rw-r--r--   0 runner    (1001) docker     (121)      779 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/sk_SK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/date_time/sl_SI/
--rw-r--r--   0 runner    (1001) docker     (121)      868 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/sl_SI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/date_time/ta_IN/
--rw-r--r--   0 runner    (1001) docker     (121)     1080 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/ta_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/date_time/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)    12290 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/date_time/tl_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      155 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/tl_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/date_time/tr_TR/
--rw-r--r--   0 runner    (1001) docker     (121)      775 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/date_time/tr_TR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/file/
--rw-r--r--   0 runner    (1001) docker     (121)    12990 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/file/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/file/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)       81 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/file/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/geo/
--rw-r--r--   0 runner    (1001) docker     (121)    70599 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/geo/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/geo/de_AT/
--rw-r--r--   0 runner    (1001) docker     (121)      299 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/geo/de_AT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/geo/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)      989 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/geo/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/geo/en_IE/
--rw-r--r--   0 runner    (1001) docker     (121)     3029 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/geo/en_IE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/geo/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)       81 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/geo/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/geo/pt_PT/
--rw-r--r--   0 runner    (1001) docker     (121)     2669 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/geo/pt_PT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/geo/tr_TR/
--rw-r--r--   0 runner    (1001) docker     (121)     6742 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/geo/tr_TR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/internet/
--rw-r--r--   0 runner    (1001) docker     (121)    24149 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/internet/ar_AA/
--rw-r--r--   0 runner    (1001) docker     (121)     1095 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/ar_AA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/internet/bg_BG/
--rw-r--r--   0 runner    (1001) docker     (121)     2474 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/bg_BG/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/internet/bs_BA/
--rw-r--r--   0 runner    (1001) docker     (121)      566 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/bs_BA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/internet/cs_CZ/
--rw-r--r--   0 runner    (1001) docker     (121)      803 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/cs_CZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.283736 Faker-9.9.0/faker/providers/internet/de_AT/
--rw-r--r--   0 runner    (1001) docker     (121)      424 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/de_AT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/de_DE/
--rw-r--r--   0 runner    (1001) docker     (121)      588 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/de_DE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)     2430 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/en_AU/
--rw-r--r--   0 runner    (1001) docker     (121)      412 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/en_AU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/en_GB/
--rw-r--r--   0 runner    (1001) docker     (121)      552 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/en_GB/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/en_NZ/
--rw-r--r--   0 runner    (1001) docker     (121)      426 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/en_NZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/en_PH/
--rw-r--r--   0 runner    (1001) docker     (121)     2097 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/en_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)       89 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/es_ES/
--rw-r--r--   0 runner    (1001) docker     (121)      494 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/es_ES/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/fa_IR/
--rw-r--r--   0 runner    (1001) docker     (121)      328 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/fa_IR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/fi_FI/
--rw-r--r--   0 runner    (1001) docker     (121)      333 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/fi_FI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/fil_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      167 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/fil_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/fr_CH/
--rw-r--r--   0 runner    (1001) docker     (121)      770 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/fr_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)      932 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/hr_HR/
--rwxr-xr-x   0 runner    (1001) docker     (121)      665 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/hr_HR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/hu_HU/
--rw-r--r--   0 runner    (1001) docker     (121)      524 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/hu_HU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/id_ID/
--rw-r--r--   0 runner    (1001) docker     (121)      562 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/id_ID/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/it_IT/
--rw-r--r--   0 runner    (1001) docker     (121)      828 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/it_IT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/ja_JP/
--rw-r--r--   0 runner    (1001) docker     (121)      523 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/ja_JP/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/ko_KR/
--rw-r--r--   0 runner    (1001) docker     (121)      345 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/ko_KR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/no_NO/
--rw-r--r--   0 runner    (1001) docker     (121)      450 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/no_NO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/pl_PL/
--rw-r--r--   0 runner    (1001) docker     (121)      520 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/pl_PL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/pt_BR/
--rw-r--r--   0 runner    (1001) docker     (121)      618 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/pt_BR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/pt_PT/
--rw-r--r--   0 runner    (1001) docker     (121)      270 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/pt_PT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/ro_RO/
--rw-r--r--   0 runner    (1001) docker     (121)      796 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/ro_RO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.287737 Faker-9.9.0/faker/providers/internet/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)     2234 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/internet/sk_SK/
--rw-r--r--   0 runner    (1001) docker     (121)      854 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/sk_SK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/internet/sl_SI/
--rwxr-xr-x   0 runner    (1001) docker     (121)     1220 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/sl_SI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/internet/sv_SE/
--rw-r--r--   0 runner    (1001) docker     (121)      482 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/sv_SE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/internet/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)      670 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/internet/tl_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      167 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/tl_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/internet/uk_UA/
--rw-r--r--   0 runner    (1001) docker     (121)     1722 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/uk_UA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/internet/zh_CN/
--rw-r--r--   0 runner    (1001) docker     (121)     2550 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/zh_CN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/internet/zh_TW/
--rw-r--r--   0 runner    (1001) docker     (121)      516 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/internet/zh_TW/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/isbn/
--rw-r--r--   0 runner    (1001) docker     (121)     3024 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/isbn/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/isbn/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)       81 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/isbn/en_US/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2680 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/isbn/isbn.py
--rw-r--r--   0 runner    (1001) docker     (121)     1824 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/isbn/rules.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/job/
--rw-r--r--   0 runner    (1001) docker     (121)    21162 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/job/ar_AA/
--rw-r--r--   0 runner    (1001) docker     (121)     3828 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/ar_AA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/job/bs_BA/
--rw-r--r--   0 runner    (1001) docker     (121)   179846 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/bs_BA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/job/de_DE/
--rw-r--r--   0 runner    (1001) docker     (121)      953 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/de_DE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/job/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)    26642 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.291737 Faker-9.9.0/faker/providers/job/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)       81 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/fa_IR/
--rw-r--r--   0 runner    (1001) docker     (121)     2433 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/fa_IR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/fi_FI/
--rw-r--r--   0 runner    (1001) docker     (121)     6120 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/fi_FI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/fr_CH/
--rw-r--r--   0 runner    (1001) docker     (121)    43169 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/fr_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)    29131 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/hr_HR/
--rw-r--r--   0 runner    (1001) docker     (121)    10408 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/hr_HR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/hu_HU/
--rw-r--r--   0 runner    (1001) docker     (121)    12939 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/hu_HU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/hy_AM/
--rw-r--r--   0 runner    (1001) docker     (121)    11265 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/hy_AM/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/ja_JP/
--rw-r--r--   0 runner    (1001) docker     (121)     1635 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/ja_JP/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/ko_KR/
--rw-r--r--   0 runner    (1001) docker     (121)    16624 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/ko_KR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/pl_PL/
--rw-r--r--   0 runner    (1001) docker     (121)     5539 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/pl_PL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/pt_BR/
--rw-r--r--   0 runner    (1001) docker     (121)    20541 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/pt_BR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/pt_PT/
--rw-r--r--   0 runner    (1001) docker     (121)    18585 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/pt_PT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/ro_RO/
--rw-r--r--   0 runner    (1001) docker     (121)   170683 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/ro_RO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)    18139 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/sk_SK/
--rw-r--r--   0 runner    (1001) docker     (121)    17587 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/sk_SK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)     3883 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/tr_TR/
--rw-r--r--   0 runner    (1001) docker     (121)    17006 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/tr_TR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.295737 Faker-9.9.0/faker/providers/job/uk_UA/
--rw-r--r--   0 runner    (1001) docker     (121)     5087 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/uk_UA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/job/zh_CN/
--rw-r--r--   0 runner    (1001) docker     (121)    28916 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/zh_CN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/job/zh_TW/
--rw-r--r--   0 runner    (1001) docker     (121)    14340 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/job/zh_TW/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/
--rw-r--r--   0 runner    (1001) docker     (121)     9633 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/ar_AA/
--rw-r--r--   0 runner    (1001) docker     (121)    15983 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/ar_AA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/cs_CZ/
--rw-r--r--   0 runner    (1001) docker     (121)    37358 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/cs_CZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)    10015 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/en_PH/
--rw-r--r--   0 runner    (1001) docker     (121)     2841 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/en_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)    17423 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/fil_PH/
--rw-r--r--   0 runner    (1001) docker     (121)    11282 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/fil_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)    27163 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/he_IL/
--rw-r--r--   0 runner    (1001) docker     (121)     3287 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/he_IL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/hy_AM/
--rw-r--r--   0 runner    (1001) docker     (121)     4687 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/hy_AM/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/ja_JP/
--rw-r--r--   0 runner    (1001) docker     (121)     4797 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/ja_JP/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/la/
--rw-r--r--   0 runner    (1001) docker     (121)     3506 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/la/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/pl_PL/
--rw-r--r--   0 runner    (1001) docker     (121)    38418 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/pl_PL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.299737 Faker-9.9.0/faker/providers/lorem/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)    13398 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/lorem/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)    11292 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/lorem/tl_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      325 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/tl_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/lorem/zh_CN/
--rw-r--r--   0 runner    (1001) docker     (121)     6408 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/zh_CN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/lorem/zh_TW/
--rw-r--r--   0 runner    (1001) docker     (121)     6408 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/lorem/zh_TW/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/misc/
--rw-r--r--   0 runner    (1001) docker     (121)    28301 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/misc/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/misc/en_PH/
--rw-r--r--   0 runner    (1001) docker     (121)     4398 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/misc/en_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/misc/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)       81 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/misc/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/misc/fil_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      151 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/misc/fil_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/misc/tl_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      151 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/misc/tl_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/person/
--rw-r--r--   0 runner    (1001) docker     (121)     9354 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/person/ar_AA/
--rw-r--r--   0 runner    (1001) docker     (121)    24858 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/ar_AA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/person/ar_PS/
--rw-r--r--   0 runner    (1001) docker     (121)     1141 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/ar_PS/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/person/ar_SA/
--rw-r--r--   0 runner    (1001) docker     (121)     1279 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/ar_SA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/person/bg_BG/
--rw-r--r--   0 runner    (1001) docker     (121)    43245 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/bg_BG/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/person/cs_CZ/
--rw-r--r--   0 runner    (1001) docker     (121)     7204 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/cs_CZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/person/de_AT/
--rw-r--r--   0 runner    (1001) docker     (121)    29783 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/de_AT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/person/de_CH/
--rw-r--r--   0 runner    (1001) docker     (121)    41031 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/de_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/person/de_DE/
--rw-r--r--   0 runner    (1001) docker     (121)    46673 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/de_DE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/person/dk_DK/
--rw-r--r--   0 runner    (1001) docker     (121)    11645 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/dk_DK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.303737 Faker-9.9.0/faker/providers/person/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)    66301 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/en/
--rw-r--r--   0 runner    (1001) docker     (121)   139274 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/en/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/en_GB/
--rw-r--r--   0 runner    (1001) docker     (121)    22799 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/en_GB/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/en_IE/
--rw-r--r--   0 runner    (1001) docker     (121)    58684 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/en_IE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/en_IN/
--rw-r--r--   0 runner    (1001) docker     (121)    12385 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/en_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/en_NZ/
--rw-r--r--   0 runner    (1001) docker     (121)    40961 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/en_NZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/en_TH/
--rw-r--r--   0 runner    (1001) docker     (121)     6008 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/en_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)    66194 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/es/
--rw-r--r--   0 runner    (1001) docker     (121)     3631 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/es/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/es_CA/
--rw-r--r--   0 runner    (1001) docker     (121)     1720 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/es_CA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/es_CO/
--rw-r--r--   0 runner    (1001) docker     (121)    35716 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/es_CO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/es_ES/
--rw-r--r--   0 runner    (1001) docker     (121)    39907 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/es_ES/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/es_MX/
--rw-r--r--   0 runner    (1001) docker     (121)    18791 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/es_MX/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/et_EE/
--rw-r--r--   0 runner    (1001) docker     (121)    13913 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/et_EE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/fa_IR/
--rw-r--r--   0 runner    (1001) docker     (121)     8309 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/fa_IR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/fi_FI/
--rw-r--r--   0 runner    (1001) docker     (121)    29043 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/fi_FI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/fr_CA/
--rw-r--r--   0 runner    (1001) docker     (121)     9745 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/fr_CA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/fr_CH/
--rw-r--r--   0 runner    (1001) docker     (121)     6997 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/fr_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)    12993 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.307738 Faker-9.9.0/faker/providers/person/fr_QC/
--rw-r--r--   0 runner    (1001) docker     (121)      290 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/fr_QC/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/ga_IE/
--rw-r--r--   0 runner    (1001) docker     (121)    73538 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/ga_IE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/he_IL/
--rw-r--r--   0 runner    (1001) docker     (121)    60492 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/he_IL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/hi_IN/
--rw-r--r--   0 runner    (1001) docker     (121)     6585 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/hi_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/hr_HR/
--rwxr-xr-x   0 runner    (1001) docker     (121)    19776 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/hr_HR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/hu_HU/
--rw-r--r--   0 runner    (1001) docker     (121)    16159 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/hu_HU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/hy_AM/
--rw-r--r--   0 runner    (1001) docker     (121)    27051 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/hy_AM/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/id_ID/
--rw-r--r--   0 runner    (1001) docker     (121)    19283 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/id_ID/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/it_IT/
--rw-r--r--   0 runner    (1001) docker     (121)    32695 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/it_IT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/ja_JP/
--rw-r--r--   0 runner    (1001) docker     (121)    10929 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/ja_JP/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/ka_GE/
--rw-r--r--   0 runner    (1001) docker     (121)    25812 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/ka_GE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/ko_KR/
--rw-r--r--   0 runner    (1001) docker     (121)     5579 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/ko_KR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/lt_LT/
--rw-r--r--   0 runner    (1001) docker     (121)     4706 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/lt_LT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/lv_LV/
--rw-r--r--   0 runner    (1001) docker     (121)     6766 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/lv_LV/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/ne_NP/
--rw-r--r--   0 runner    (1001) docker     (121)    44009 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/ne_NP/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.311738 Faker-9.9.0/faker/providers/person/nl_NL/
--rw-r--r--   0 runner    (1001) docker     (121)    32776 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/nl_NL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/no_NO/
--rw-r--r--   0 runner    (1001) docker     (121)     7074 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/no_NO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/or_IN/
--rw-r--r--   0 runner    (1001) docker     (121)    35828 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/or_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/pl_PL/
--rw-r--r--   0 runner    (1001) docker     (121)    95392 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/pl_PL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/pt_BR/
--rw-r--r--   0 runner    (1001) docker     (121)     7230 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/pt_BR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/pt_PT/
--rw-r--r--   0 runner    (1001) docker     (121)     6791 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/pt_PT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/ro_RO/
--rw-r--r--   0 runner    (1001) docker     (121)    14264 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/ro_RO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)    37558 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/sl_SI/
--rwxr-xr-x   0 runner    (1001) docker     (121)     9540 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/sl_SI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/sv_SE/
--rw-r--r--   0 runner    (1001) docker     (121)    21588 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/sv_SE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/ta_IN/
--rw-r--r--   0 runner    (1001) docker     (121)    35625 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/ta_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)    35440 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/tr_TR/
--rw-r--r--   0 runner    (1001) docker     (121)    30905 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/tr_TR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/tw_GH/
--rw-r--r--   0 runner    (1001) docker     (121)    11402 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/tw_GH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/uk_UA/
--rw-r--r--   0 runner    (1001) docker     (121)    19506 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/uk_UA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/zh_CN/
--rw-r--r--   0 runner    (1001) docker     (121)    16427 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/zh_CN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/person/zh_TW/
--rw-r--r--   0 runner    (1001) docker     (121)    15875 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/person/zh_TW/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/phone_number/
--rw-r--r--   0 runner    (1001) docker     (121)     5811 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/phone_number/ar_AE/
--rw-r--r--   0 runner    (1001) docker     (121)     2580 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/ar_AE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.315738 Faker-9.9.0/faker/providers/phone_number/ar_JO/
--rw-r--r--   0 runner    (1001) docker     (121)     1772 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/ar_JO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/ar_PS/
--rw-r--r--   0 runner    (1001) docker     (121)     3605 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/ar_PS/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/bg_BG/
--rwxr-xr-x   0 runner    (1001) docker     (121)      390 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/bg_BG/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/bs_BA/
--rw-r--r--   0 runner    (1001) docker     (121)      879 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/bs_BA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/cs_CZ/
--rw-r--r--   0 runner    (1001) docker     (121)      913 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/cs_CZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/de_DE/
--rw-r--r--   0 runner    (1001) docker     (121)      455 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/de_DE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/dk_DK/
--rw-r--r--   0 runner    (1001) docker     (121)      395 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/dk_DK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)      523 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/en_AU/
--rw-r--r--   0 runner    (1001) docker     (121)     1317 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/en_AU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/en_CA/
--rw-r--r--   0 runner    (1001) docker     (121)      349 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/en_CA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/en_GB/
--rw-r--r--   0 runner    (1001) docker     (121)     7437 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/en_GB/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/en_IN/
--rw-r--r--   0 runner    (1001) docker     (121)      178 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/en_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/en_NZ/
--rw-r--r--   0 runner    (1001) docker     (121)     1247 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/en_NZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/en_PH/
--rw-r--r--   0 runner    (1001) docker     (121)     8171 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/en_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)     1281 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/es_CO/
--rw-r--r--   0 runner    (1001) docker     (121)     1043 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/es_CO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/es_ES/
--rw-r--r--   0 runner    (1001) docker     (121)     1504 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/es_ES/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/es_MX/
--rw-r--r--   0 runner    (1001) docker     (121)      765 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/es_MX/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/fa_IR/
--rw-r--r--   0 runner    (1001) docker     (121)     2658 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/fa_IR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/fi_FI/
--rw-r--r--   0 runner    (1001) docker     (121)      260 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/fi_FI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.319738 Faker-9.9.0/faker/providers/phone_number/fil_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      177 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/fil_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/fr_CH/
--rw-r--r--   0 runner    (1001) docker     (121)      979 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/fr_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)     4471 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/he_IL/
--rw-r--r--   0 runner    (1001) docker     (121)      468 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/he_IL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/hi_IN/
--rw-r--r--   0 runner    (1001) docker     (121)      232 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/hi_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/hr_HR/
--rwxr-xr-x   0 runner    (1001) docker     (121)      803 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/hr_HR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/hu_HU/
--rw-r--r--   0 runner    (1001) docker     (121)      284 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/hu_HU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/hy_AM/
--rw-r--r--   0 runner    (1001) docker     (121)      442 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/hy_AM/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/id_ID/
--rw-r--r--   0 runner    (1001) docker     (121)      648 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/id_ID/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/it_IT/
--rw-r--r--   0 runner    (1001) docker     (121)      303 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/it_IT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/ja_JP/
--rw-r--r--   0 runner    (1001) docker     (121)      207 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/ja_JP/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/ko_KR/
--rw-r--r--   0 runner    (1001) docker     (121)      686 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/ko_KR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/lt_LT/
--rw-r--r--   0 runner    (1001) docker     (121)      184 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/lt_LT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/lv_LV/
--rw-r--r--   0 runner    (1001) docker     (121)      184 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/lv_LV/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/ne_NP/
--rw-r--r--   0 runner    (1001) docker     (121)      229 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/ne_NP/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.323738 Faker-9.9.0/faker/providers/phone_number/nl_BE/
--rw-r--r--   0 runner    (1001) docker     (121)      512 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/nl_BE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/nl_NL/
--rw-r--r--   0 runner    (1001) docker     (121)      512 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/nl_NL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/no_NO/
--rw-r--r--   0 runner    (1001) docker     (121)      328 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/no_NO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/pl_PL/
--rw-r--r--   0 runner    (1001) docker     (121)      895 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/pl_PL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/pt_BR/
--rw-r--r--   0 runner    (1001) docker     (121)     3537 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/pt_BR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/pt_PT/
--rw-r--r--   0 runner    (1001) docker     (121)     1013 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/pt_PT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/ro_RO/
--rw-r--r--   0 runner    (1001) docker     (121)     2484 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/ro_RO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)      379 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/sk_SK/
--rw-r--r--   0 runner    (1001) docker     (121)      387 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/sk_SK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/sl_SI/
--rwxr-xr-x   0 runner    (1001) docker     (121)      361 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/sl_SI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/sv_SE/
--rw-r--r--   0 runner    (1001) docker     (121)      367 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/sv_SE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/ta_IN/
--rw-r--r--   0 runner    (1001) docker     (121)      232 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/ta_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)     1826 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/tl_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      177 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/tl_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/tr_TR/
--rw-r--r--   0 runner    (1001) docker     (121)      349 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/tr_TR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/tw_GH/
--rw-r--r--   0 runner    (1001) docker     (121)      578 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/tw_GH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/uk_UA/
--rw-r--r--   0 runner    (1001) docker     (121)      318 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/uk_UA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/zh_CN/
--rw-r--r--   0 runner    (1001) docker     (121)      681 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/zh_CN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/phone_number/zh_TW/
--rw-r--r--   0 runner    (1001) docker     (121)      348 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/phone_number/zh_TW/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/profile/
--rw-r--r--   0 runner    (1001) docker     (121)     2082 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/profile/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/profile/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)      127 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/profile/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.327739 Faker-9.9.0/faker/providers/python/
--rw-r--r--   0 runner    (1001) docker     (121)    16763 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/python/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/python/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)      125 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/python/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/
--rw-r--r--   0 runner    (1001) docker     (121)      235 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/bg_BG/
--rw-r--r--   0 runner    (1001) docker     (121)      447 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/bg_BG/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/cs_CZ/
--rw-r--r--   0 runner    (1001) docker     (121)     1418 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/cs_CZ/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/de_AT/
--rw-r--r--   0 runner    (1001) docker     (121)      407 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/de_AT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/de_CH/
--rw-r--r--   0 runner    (1001) docker     (121)       86 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/de_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/de_DE/
--rw-r--r--   0 runner    (1001) docker     (121)      403 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/de_DE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/dk_DK/
--rw-r--r--   0 runner    (1001) docker     (121)      344 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/dk_DK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/el_CY/
--rw-r--r--   0 runner    (1001) docker     (121)      348 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/el_CY/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/el_GR/
--rw-r--r--   0 runner    (1001) docker     (121)      803 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/el_GR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/en_CA/
--rw-r--r--   0 runner    (1001) docker     (121)     2968 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/en_CA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/en_GB/
--rw-r--r--   0 runner    (1001) docker     (121)     1303 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/en_GB/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/en_IE/
--rw-r--r--   0 runner    (1001) docker     (121)      459 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/en_IE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/en_IN/
--rw-r--r--   0 runner    (1001) docker     (121)      731 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/en_IN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/en_PH/
--rw-r--r--   0 runner    (1001) docker     (121)     2638 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/en_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)     6852 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/es_CA/
--rw-r--r--   0 runner    (1001) docker     (121)      157 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/es_CA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/es_CO/
--rw-r--r--   0 runner    (1001) docker     (121)     2108 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/es_CO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/es_ES/
--rw-r--r--   0 runner    (1001) docker     (121)     3387 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/es_ES/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.331739 Faker-9.9.0/faker/providers/ssn/es_MX/
--rw-r--r--   0 runner    (1001) docker     (121)     5725 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/es_MX/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/et_EE/
--rw-r--r--   0 runner    (1001) docker     (121)     2742 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/et_EE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/fi_FI/
--rw-r--r--   0 runner    (1001) docker     (121)     2485 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/fi_FI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/fil_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      152 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/fil_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/fr_CH/
--rw-r--r--   0 runner    (1001) docker     (121)     1523 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/fr_CH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/fr_FR/
--rw-r--r--   0 runner    (1001) docker     (121)     6772 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/fr_FR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/he_IL/
--rw-r--r--   0 runner    (1001) docker     (121)      830 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/he_IL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/hr_HR/
--rw-r--r--   0 runner    (1001) docker     (121)     1453 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/hr_HR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/hu_HU/
--rw-r--r--   0 runner    (1001) docker     (121)     4387 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/hu_HU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/it_IT/
--rw-r--r--   0 runner    (1001) docker     (121)     1925 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/it_IT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/ko_KR/
--rw-r--r--   0 runner    (1001) docker     (121)      252 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/ko_KR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/lb_LU/
--rw-r--r--   0 runner    (1001) docker     (121)      416 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/lb_LU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/lt_LT/
--rw-r--r--   0 runner    (1001) docker     (121)      451 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/lt_LT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/lv_LV/
--rw-r--r--   0 runner    (1001) docker     (121)      407 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/lv_LV/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/mt_MT/
--rw-r--r--   0 runner    (1001) docker     (121)      404 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/mt_MT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/nl_BE/
--rw-r--r--   0 runner    (1001) docker     (121)     2332 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/nl_BE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/nl_NL/
--rw-r--r--   0 runner    (1001) docker     (121)     1622 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/nl_NL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/no_NO/
--rw-r--r--   0 runner    (1001) docker     (121)     3339 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/no_NO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/pl_PL/
--rw-r--r--   0 runner    (1001) docker     (121)     2200 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/pl_PL/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.335739 Faker-9.9.0/faker/providers/ssn/pt_BR/
--rw-r--r--   0 runner    (1001) docker     (121)     1823 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/pt_BR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/ssn/pt_PT/
--rw-r--r--   0 runner    (1001) docker     (121)      411 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/pt_PT/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/ssn/ro_RO/
--rw-r--r--   0 runner    (1001) docker     (121)     3472 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/ro_RO/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/ssn/ru_RU/
--rw-r--r--   0 runner    (1001) docker     (121)      106 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/ru_RU/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/ssn/sk_SK/
--rw-r--r--   0 runner    (1001) docker     (121)     1370 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/sk_SK/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/ssn/sl_SI/
--rw-r--r--   0 runner    (1001) docker     (121)      408 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/sl_SI/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/ssn/sv_SE/
--rw-r--r--   0 runner    (1001) docker     (121)     3016 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/sv_SE/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/ssn/th_TH/
--rw-r--r--   0 runner    (1001) docker     (121)     1892 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/th_TH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/ssn/tl_PH/
--rw-r--r--   0 runner    (1001) docker     (121)      152 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/tl_PH/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/ssn/tr_TR/
--rw-r--r--   0 runner    (1001) docker     (121)      632 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/tr_TR/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/ssn/uk_UA/
--rw-r--r--   0 runner    (1001) docker     (121)     1138 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/uk_UA/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/ssn/zh_CN/
--rw-r--r--   0 runner    (1001) docker     (121)    64760 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/zh_CN/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/ssn/zh_TW/
--rw-r--r--   0 runner    (1001) docker     (121)      206 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/ssn/zh_TW/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/user_agent/
--rw-r--r--   0 runner    (1001) docker     (121)    11120 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/user_agent/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.339739 Faker-9.9.0/faker/providers/user_agent/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)      131 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/providers/user_agent/en_US/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10945 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/proxy.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/py.typed
--rw-r--r--   0 runner    (1001) docker     (121)      398 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/typing.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.343740 Faker-9.9.0/faker/utils/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      629 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/utils/checksums.py
--rw-r--r--   0 runner    (1001) docker     (121)      535 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/utils/datasets.py
--rw-r--r--   0 runner    (1001) docker     (121)      950 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/utils/decorators.py
--rw-r--r--   0 runner    (1001) docker     (121)     2312 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/utils/distribution.py
--rw-r--r--   0 runner    (1001) docker     (121)     1753 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/utils/loading.py
--rw-r--r--   0 runner    (1001) docker     (121)     1039 2021-11-29 21:42:04.000000 Faker-9.9.0/faker/utils/text.py
--rw-r--r--   0 runner    (1001) docker     (121)      268 2021-11-29 21:42:04.000000 Faker-9.9.0/mypy.ini
--rw-r--r--   0 runner    (1001) docker     (121)      200 2021-11-29 21:42:15.355740 Faker-9.9.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2578 2021-11-29 21:42:04.000000 Faker-9.9.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.343740 Faker-9.9.0/tests/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)       30 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.343740 Faker-9.9.0/tests/mymodule/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/mymodule/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.343740 Faker-9.9.0/tests/mymodule/en_US/
--rw-r--r--   0 runner    (1001) docker     (121)      113 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/mymodule/en_US/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.351740 Faker-9.9.0/tests/providers/
--rw-r--r--   0 runner    (1001) docker     (121)    10006 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1049 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/conftest.py
--rw-r--r--   0 runner    (1001) docker     (121)    71204 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_address.py
--rw-r--r--   0 runner    (1001) docker     (121)     9670 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_automotive.py
--rw-r--r--   0 runner    (1001) docker     (121)     9600 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_bank.py
--rw-r--r--   0 runner    (1001) docker     (121)    13075 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_barcode.py
--rw-r--r--   0 runner    (1001) docker     (121)    14289 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_color.py
--rw-r--r--   0 runner    (1001) docker     (121)    16757 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_company.py
--rw-r--r--   0 runner    (1001) docker     (121)     6303 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_credit_card.py
--rw-r--r--   0 runner    (1001) docker     (121)    12133 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_currency.py
--rw-r--r--   0 runner    (1001) docker     (121)    40088 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_date_time.py
--rw-r--r--   0 runner    (1001) docker     (121)     2128 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_dynamic.py
--rw-r--r--   0 runner    (1001) docker     (121)     1579 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_file.py
--rw-r--r--   0 runner    (1001) docker     (121)     3542 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_geo.py
--rw-r--r--   0 runner    (1001) docker     (121)    29607 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_internet.py
--rw-r--r--   0 runner    (1001) docker     (121)     2585 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_isbn.py
--rw-r--r--   0 runner    (1001) docker     (121)     3504 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_job.py
--rw-r--r--   0 runner    (1001) docker     (121)     9887 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_lorem.py
--rw-r--r--   0 runner    (1001) docker     (121)    25747 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_misc.py
--rw-r--r--   0 runner    (1001) docker     (121)    34319 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_person.py
--rw-r--r--   0 runner    (1001) docker     (121)    13276 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_phone_number.py
--rw-r--r--   0 runner    (1001) docker     (121)     1523 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_profile.py
--rw-r--r--   0 runner    (1001) docker     (121)    17225 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_python.py
--rw-r--r--   0 runner    (1001) docker     (121)    37291 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_ssn.py
--rw-r--r--   0 runner    (1001) docker     (121)     1430 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/providers/test_user_agent.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.351740 Faker-9.9.0/tests/pytest/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/pytest/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.351740 Faker-9.9.0/tests/pytest/session_overrides/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/pytest/session_overrides/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      940 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/pytest/session_overrides/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.351740 Faker-9.9.0/tests/pytest/session_overrides/session_locale/
--rw-r--r--   0 runner    (1001) docker     (121)       28 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/pytest/session_overrides/session_locale/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      193 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/pytest/session_overrides/session_locale/conftest.py
--rw-r--r--   0 runner    (1001) docker     (121)     1262 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/pytest/session_overrides/session_locale/test_autouse_faker_locale.py
--rw-r--r--   0 runner    (1001) docker     (121)     1233 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/pytest/session_overrides/session_locale/test_autouse_faker_seed.py
--rw-r--r--   0 runner    (1001) docker     (121)     1647 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/pytest/session_overrides/session_locale/test_manual_injection.py
--rw-r--r--   0 runner    (1001) docker     (121)     1203 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/pytest/test_autouse_faker_locale.py
--rw-r--r--   0 runner    (1001) docker     (121)     1213 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/pytest/test_autouse_faker_seed.py
--rw-r--r--   0 runner    (1001) docker     (121)     1603 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/pytest/test_manual_injection.py
--rw-r--r--   0 runner    (1001) docker     (121)     1184 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/pytest/test_unique_clear.py
--rw-r--r--   0 runner    (1001) docker     (121)    10512 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/test_factory.py
--rw-r--r--   0 runner    (1001) docker     (121)     5224 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/test_generator.py
--rw-r--r--   0 runner    (1001) docker     (121)     2599 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/test_providers_formats.py
--rw-r--r--   0 runner    (1001) docker     (121)    15812 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/test_proxy.py
--rw-r--r--   0 runner    (1001) docker     (121)     1955 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/test_unique.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:15.351740 Faker-9.9.0/tests/utils/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7346 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/utils/random_state.json
--rw-r--r--   0 runner    (1001) docker     (121)     4474 2021-11-29 21:42:04.000000 Faker-9.9.0/tests/utils/test_utils.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.888595 Faker-9.9.1/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    58503 2021-12-07 15:55:10.000000 Faker-9.9.1/CHANGELOG.md
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      263 2021-08-12 17:07:14.000000 Faker-9.9.1/CITATION.cff
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1650 2019-10-15 17:30:33.000000 Faker-9.9.1/CONTRIBUTING.rst
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.053934 Faker-9.9.1/Faker.egg-info/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    19117 2021-12-07 15:55:49.000000 Faker-9.9.1/Faker.egg-info/PKG-INFO
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    23218 2021-12-07 15:55:49.000000 Faker-9.9.1/Faker.egg-info/SOURCES.txt
+-rw-r--r--   0 flavio.curella   (502) staff       (20)        1 2021-12-07 15:55:49.000000 Faker-9.9.1/Faker.egg-info/dependency_links.txt
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      111 2021-12-07 15:55:49.000000 Faker-9.9.1/Faker.egg-info/entry_points.txt
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       96 2021-12-07 15:55:49.000000 Faker-9.9.1/Faker.egg-info/requires.txt
+-rw-r--r--   0 flavio.curella   (502) staff       (20)        6 2021-12-07 15:55:49.000000 Faker-9.9.1/Faker.egg-info/top_level.txt
+-rw-r--r--   0 flavio.curella   (502) staff       (20)        1 2019-11-13 18:18:01.000000 Faker-9.9.1/Faker.egg-info/zip-safe
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1060 2021-10-25 16:49:56.000000 Faker-9.9.1/LICENSE.txt
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      582 2021-10-19 14:31:10.000000 Faker-9.9.1/MANIFEST.in
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    19117 2021-12-07 15:55:50.888913 Faker-9.9.1/PKG-INFO
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    14109 2021-10-25 16:49:39.000000 Faker-9.9.1/README.rst
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      815 2020-10-01 19:48:16.000000 Faker-9.9.1/RELEASE_PROCESS.rst
+-rw-r--r--   0 flavio.curella   (502) staff       (20)        6 2021-12-07 15:55:31.000000 Faker-9.9.1/VERSION
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.057934 Faker-9.9.1/faker/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      166 2021-12-07 15:55:31.000000 Faker-9.9.1/faker/__init__.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      107 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/__main__.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9659 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/cli.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      343 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/config.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.058213 Faker-9.9.1/faker/contrib/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)        0 2020-05-12 15:20:18.000000 Faker-9.9.1/faker/contrib/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.058812 Faker-9.9.1/faker/contrib/pytest/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)        0 2020-05-12 15:20:18.000000 Faker-9.9.1/faker/contrib/pytest/__init__.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1114 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/contrib/pytest/plugin.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3976 2021-11-29 18:09:11.000000 Faker-9.9.1/faker/documentor.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      506 2021-10-19 14:31:10.000000 Faker-9.9.1/faker/exceptions.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     4552 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/factory.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6547 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/generator.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.059178 Faker-9.9.1/faker/providers/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    24669 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.064879 Faker-9.9.1/faker/providers/address/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3683 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/providers/address/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.065388 Faker-9.9.1/faker/providers/address/cs_CZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    26882 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/cs_CZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.065799 Faker-9.9.1/faker/providers/address/da_DK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     7714 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/da_DK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.066068 Faker-9.9.1/faker/providers/address/de/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     5668 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/de/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.066339 Faker-9.9.1/faker/providers/address/de_AT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6261 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/de_AT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.066759 Faker-9.9.1/faker/providers/address/de_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1962 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/de_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.067018 Faker-9.9.1/faker/providers/address/de_DE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10232 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/de_DE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.067335 Faker-9.9.1/faker/providers/address/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)   148988 2021-11-29 18:11:05.000000 Faker-9.9.1/faker/providers/address/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.067906 Faker-9.9.1/faker/providers/address/en/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     5642 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/en/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.068338 Faker-9.9.1/faker/providers/address/en_AU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6566 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/en_AU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.068655 Faker-9.9.1/faker/providers/address/en_CA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     8939 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/providers/address/en_CA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.069001 Faker-9.9.1/faker/providers/address/en_GB/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10725 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/en_GB/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.069262 Faker-9.9.1/faker/providers/address/en_IE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1336 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/en_IE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.069669 Faker-9.9.1/faker/providers/address/en_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     8591 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/en_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.070229 Faker-9.9.1/faker/providers/address/en_NZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     7132 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/en_NZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.071235 Faker-9.9.1/faker/providers/address/en_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    43162 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/address/en_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.071708 Faker-9.9.1/faker/providers/address/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    12268 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.072651 Faker-9.9.1/faker/providers/address/es/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     4410 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/es/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.073052 Faker-9.9.1/faker/providers/address/es_CO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    42947 2021-11-29 18:11:03.000000 Faker-9.9.1/faker/providers/address/es_CO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.073588 Faker-9.9.1/faker/providers/address/es_ES/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3291 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/es_ES/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.073897 Faker-9.9.1/faker/providers/address/es_MX/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     4914 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/es_MX/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.074450 Faker-9.9.1/faker/providers/address/fa_IR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     8017 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/fa_IR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.074944 Faker-9.9.1/faker/providers/address/fi_FI/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    16854 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/fi_FI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.075442 Faker-9.9.1/faker/providers/address/fil_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      164 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/fil_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.075817 Faker-9.9.1/faker/providers/address/fr_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     8682 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/fr_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.076145 Faker-9.9.1/faker/providers/address/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    11701 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.076502 Faker-9.9.1/faker/providers/address/he_IL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    16425 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/he_IL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.076927 Faker-9.9.1/faker/providers/address/hi_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     7699 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/hi_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.077219 Faker-9.9.1/faker/providers/address/hr_HR/
+-rwxr-xr-x   0 flavio.curella   (502) staff       (20)    12722 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/hr_HR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.077529 Faker-9.9.1/faker/providers/address/hu_HU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10954 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/hu_HU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.077936 Faker-9.9.1/faker/providers/address/hy_AM/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    20543 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/hy_AM/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.078369 Faker-9.9.1/faker/providers/address/id_ID/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    11528 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/id_ID/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.078692 Faker-9.9.1/faker/providers/address/it_IT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10938 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/address/it_IT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.078995 Faker-9.9.1/faker/providers/address/ja_JP/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    16159 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/ja_JP/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.079296 Faker-9.9.1/faker/providers/address/ka_GE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    53808 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/ka_GE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.105330 Faker-9.9.1/faker/providers/address/ko_KR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    14994 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/ko_KR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.105739 Faker-9.9.1/faker/providers/address/ne_NP/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    22771 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/address/ne_NP/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.106435 Faker-9.9.1/faker/providers/address/nl_BE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    65192 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/nl_BE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.106891 Faker-9.9.1/faker/providers/address/nl_NL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    57923 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/nl_NL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.107367 Faker-9.9.1/faker/providers/address/no_NO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2490 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/providers/address/no_NO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.107867 Faker-9.9.1/faker/providers/address/pl_PL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    14642 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/pl_PL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.108117 Faker-9.9.1/faker/providers/address/pt_BR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    22991 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/address/pt_BR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.108451 Faker-9.9.1/faker/providers/address/pt_PT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    38109 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/pt_PT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.108826 Faker-9.9.1/faker/providers/address/ro_RO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9629 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/ro_RO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.109274 Faker-9.9.1/faker/providers/address/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    48537 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/address/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.109600 Faker-9.9.1/faker/providers/address/sk_SK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)   122027 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/sk_SK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.110147 Faker-9.9.1/faker/providers/address/sl_SI/
+-rwxr-xr-x   0 flavio.curella   (502) staff       (20)    42397 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/sl_SI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.110607 Faker-9.9.1/faker/providers/address/sv_SE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     8160 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/sv_SE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.110898 Faker-9.9.1/faker/providers/address/ta_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    16944 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/ta_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.111326 Faker-9.9.1/faker/providers/address/th/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9792 2021-06-02 12:40:17.000000 Faker-9.9.1/faker/providers/address/th/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.111570 Faker-9.9.1/faker/providers/address/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    12993 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.111817 Faker-9.9.1/faker/providers/address/tl_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      164 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/tl_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.112102 Faker-9.9.1/faker/providers/address/uk_UA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    75352 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/address/uk_UA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.112610 Faker-9.9.1/faker/providers/address/zh_CN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9895 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/providers/address/zh_CN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.112852 Faker-9.9.1/faker/providers/address/zh_TW/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     8293 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/providers/address/zh_TW/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.113089 Faker-9.9.1/faker/providers/automotive/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      517 2021-11-29 18:09:13.000000 Faker-9.9.1/faker/providers/automotive/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.113370 Faker-9.9.1/faker/providers/automotive/ar_JO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1567 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/ar_JO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.113606 Faker-9.9.1/faker/providers/automotive/ar_PS/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1744 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/ar_PS/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.114131 Faker-9.9.1/faker/providers/automotive/ar_SA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2318 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/ar_SA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.114606 Faker-9.9.1/faker/providers/automotive/de_DE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6463 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/de_DE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.115164 Faker-9.9.1/faker/providers/automotive/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      555 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.115787 Faker-9.9.1/faker/providers/automotive/en_CA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      919 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/en_CA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.116464 Faker-9.9.1/faker/providers/automotive/en_GB/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      322 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/en_GB/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.116986 Faker-9.9.1/faker/providers/automotive/en_NZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      640 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/en_NZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.117742 Faker-9.9.1/faker/providers/automotive/en_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2476 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/en_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.118386 Faker-9.9.1/faker/providers/automotive/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3280 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.118920 Faker-9.9.1/faker/providers/automotive/es_CO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      360 2021-11-02 21:08:47.000000 Faker-9.9.1/faker/providers/automotive/es_CO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.119280 Faker-9.9.1/faker/providers/automotive/es_ES/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3940 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/providers/automotive/es_ES/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.119569 Faker-9.9.1/faker/providers/automotive/fil_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      238 2020-09-22 19:25:55.000000 Faker-9.9.1/faker/providers/automotive/fil_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.120078 Faker-9.9.1/faker/providers/automotive/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      374 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.120768 Faker-9.9.1/faker/providers/automotive/he_IL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      321 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/he_IL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.121293 Faker-9.9.1/faker/providers/automotive/hu_HU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      277 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/hu_HU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.121783 Faker-9.9.1/faker/providers/automotive/id_ID/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      349 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/id_ID/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.122166 Faker-9.9.1/faker/providers/automotive/nl_NL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2533 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/providers/automotive/nl_NL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.122534 Faker-9.9.1/faker/providers/automotive/no_NO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      316 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/no_NO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.123055 Faker-9.9.1/faker/providers/automotive/pl_PL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1007 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/providers/automotive/pl_PL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.123496 Faker-9.9.1/faker/providers/automotive/pt_BR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      183 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/pt_BR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.123977 Faker-9.9.1/faker/providers/automotive/pt_PT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      391 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/pt_PT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.124373 Faker-9.9.1/faker/providers/automotive/ro_RO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1181 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/ro_RO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.124663 Faker-9.9.1/faker/providers/automotive/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     7827 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.125202 Faker-9.9.1/faker/providers/automotive/sk_SK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2641 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/sk_SK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.125534 Faker-9.9.1/faker/providers/automotive/sv_SE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      428 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/sv_SE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.125885 Faker-9.9.1/faker/providers/automotive/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      948 2021-10-19 14:31:10.000000 Faker-9.9.1/faker/providers/automotive/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.126318 Faker-9.9.1/faker/providers/automotive/tl_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      237 2020-09-22 19:25:55.000000 Faker-9.9.1/faker/providers/automotive/tl_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.155090 Faker-9.9.1/faker/providers/automotive/tr_TR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      868 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/automotive/tr_TR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.155611 Faker-9.9.1/faker/providers/bank/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6121 2021-11-29 18:10:59.000000 Faker-9.9.1/faker/providers/bank/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.156059 Faker-9.9.1/faker/providers/bank/de_AT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      190 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/de_AT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.156426 Faker-9.9.1/faker/providers/bank/de_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      191 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/de_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.156750 Faker-9.9.1/faker/providers/bank/de_DE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      192 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/de_DE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.157194 Faker-9.9.1/faker/providers/bank/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      197 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.157450 Faker-9.9.1/faker/providers/bank/en_GB/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      192 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/en_GB/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.157695 Faker-9.9.1/faker/providers/bank/en_IE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      197 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/en_IE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.157953 Faker-9.9.1/faker/providers/bank/en_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2690 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/en_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.158390 Faker-9.9.1/faker/providers/bank/es_ES/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      194 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/es_ES/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.158638 Faker-9.9.1/faker/providers/bank/fi_FI/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      188 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/fi_FI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.158892 Faker-9.9.1/faker/providers/bank/fil_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      220 2020-09-22 19:25:55.000000 Faker-9.9.1/faker/providers/bank/fil_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.159247 Faker-9.9.1/faker/providers/bank/fr_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      219 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/fr_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.159604 Faker-9.9.1/faker/providers/bank/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      197 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.160168 Faker-9.9.1/faker/providers/bank/it_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      219 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/it_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.160714 Faker-9.9.1/faker/providers/bank/it_IT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      197 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/it_IT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.161121 Faker-9.9.1/faker/providers/bank/nl_NL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      188 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/nl_NL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.161692 Faker-9.9.1/faker/providers/bank/no_NO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      185 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/no_NO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.162343 Faker-9.9.1/faker/providers/bank/pl_PL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      180 2021-11-23 14:57:26.000000 Faker-9.9.1/faker/providers/bank/pl_PL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.162822 Faker-9.9.1/faker/providers/bank/pt_PT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      195 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/pt_PT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.163169 Faker-9.9.1/faker/providers/bank/ro_RO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      883 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/ro_RO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.163525 Faker-9.9.1/faker/providers/bank/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    21826 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/bank/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.164508 Faker-9.9.1/faker/providers/bank/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1059 2021-06-02 12:40:21.000000 Faker-9.9.1/faker/providers/bank/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.165035 Faker-9.9.1/faker/providers/bank/tl_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      219 2020-09-22 19:25:55.000000 Faker-9.9.1/faker/providers/bank/tl_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.165546 Faker-9.9.1/faker/providers/bank/tr_TR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      196 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/bank/tr_TR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.166032 Faker-9.9.1/faker/providers/barcode/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3972 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/barcode/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.166652 Faker-9.9.1/faker/providers/barcode/en_CA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      664 2020-09-22 19:25:55.000000 Faker-9.9.1/faker/providers/barcode/en_CA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.167215 Faker-9.9.1/faker/providers/barcode/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    11356 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/barcode/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.167779 Faker-9.9.1/faker/providers/barcode/es_ES/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      244 2020-09-22 19:25:55.000000 Faker-9.9.1/faker/providers/barcode/es_ES/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.168356 Faker-9.9.1/faker/providers/barcode/fr_CA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      217 2020-09-22 19:25:55.000000 Faker-9.9.1/faker/providers/barcode/fr_CA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.168902 Faker-9.9.1/faker/providers/barcode/ja_JP/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1476 2021-10-19 14:31:10.000000 Faker-9.9.1/faker/providers/barcode/ja_JP/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.169877 Faker-9.9.1/faker/providers/color/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9113 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.170230 Faker-9.9.1/faker/providers/color/ar_PS/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6973 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/ar_PS/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.170875 Faker-9.9.1/faker/providers/color/bg_BG/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3337 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/bg_BG/__init__.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10362 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/color/color.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.171241 Faker-9.9.1/faker/providers/color/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     4247 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.171691 Faker-9.9.1/faker/providers/color/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      141 2020-09-22 19:25:55.000000 Faker-9.9.1/faker/providers/color/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.172019 Faker-9.9.1/faker/providers/color/es_ES/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6202 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/es_ES/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.172579 Faker-9.9.1/faker/providers/color/fa_IR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     7079 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/fa_IR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.173111 Faker-9.9.1/faker/providers/color/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6038 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.173578 Faker-9.9.1/faker/providers/color/he_IL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1729 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/he_IL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.174080 Faker-9.9.1/faker/providers/color/hr_HR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6323 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/hr_HR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.194084 Faker-9.9.1/faker/providers/color/hu_HU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      444 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/hu_HU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.194597 Faker-9.9.1/faker/providers/color/hy_AM/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     8297 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/hy_AM/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.195069 Faker-9.9.1/faker/providers/color/pt_BR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9674 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/pt_BR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.195473 Faker-9.9.1/faker/providers/color/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3402 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.195858 Faker-9.9.1/faker/providers/color/sk_SK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      469 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/sk_SK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.196220 Faker-9.9.1/faker/providers/color/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1660 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.196622 Faker-9.9.1/faker/providers/color/uk_UA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    11365 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/color/uk_UA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.197076 Faker-9.9.1/faker/providers/company/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    13647 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/company/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.197582 Faker-9.9.1/faker/providers/company/bg_BG/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      552 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/bg_BG/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.198005 Faker-9.9.1/faker/providers/company/cs_CZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      309 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/cs_CZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.198444 Faker-9.9.1/faker/providers/company/de_DE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      753 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/de_DE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.198869 Faker-9.9.1/faker/providers/company/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      423 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.199293 Faker-9.9.1/faker/providers/company/en_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3694 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/company/en_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.199823 Faker-9.9.1/faker/providers/company/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       87 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/company/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.200320 Faker-9.9.1/faker/providers/company/es_MX/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    11494 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/es_MX/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.200789 Faker-9.9.1/faker/providers/company/fa_IR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    49816 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/fa_IR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.201488 Faker-9.9.1/faker/providers/company/fi_FI/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2067 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/fi_FI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.201935 Faker-9.9.1/faker/providers/company/fil_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2750 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/company/fil_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.202384 Faker-9.9.1/faker/providers/company/fr_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1313 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/fr_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.202815 Faker-9.9.1/faker/providers/company/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3983 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/company/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.203250 Faker-9.9.1/faker/providers/company/hr_HR/
+-rwxr-xr-x   0 flavio.curella   (502) staff       (20)      313 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/hr_HR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.203817 Faker-9.9.1/faker/providers/company/hu_HU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      488 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/hu_HU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.204497 Faker-9.9.1/faker/providers/company/hy_AM/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9891 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/hy_AM/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.205153 Faker-9.9.1/faker/providers/company/id_ID/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      933 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/id_ID/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.205574 Faker-9.9.1/faker/providers/company/it_IT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9716 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/it_IT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.206107 Faker-9.9.1/faker/providers/company/ja_JP/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      762 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/ja_JP/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.206664 Faker-9.9.1/faker/providers/company/ko_KR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9720 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/ko_KR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.207374 Faker-9.9.1/faker/providers/company/nl_NL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    11853 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/nl_NL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.207969 Faker-9.9.1/faker/providers/company/no_NO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      534 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/no_NO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.208443 Faker-9.9.1/faker/providers/company/pl_PL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3912 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/pl_PL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.208905 Faker-9.9.1/faker/providers/company/pt_BR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2972 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/company/pt_BR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.209339 Faker-9.9.1/faker/providers/company/pt_PT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1198 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/pt_PT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.209801 Faker-9.9.1/faker/providers/company/ro_RO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      639 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/ro_RO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.210202 Faker-9.9.1/faker/providers/company/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    45104 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/company/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.210677 Faker-9.9.1/faker/providers/company/sk_SK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      327 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/sk_SK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.211004 Faker-9.9.1/faker/providers/company/sl_SI/
+-rwxr-xr-x   0 flavio.curella   (502) staff       (20)      255 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/sl_SI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.211282 Faker-9.9.1/faker/providers/company/sv_SE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      322 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/sv_SE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.211661 Faker-9.9.1/faker/providers/company/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     4169 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.212010 Faker-9.9.1/faker/providers/company/tl_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      154 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/tl_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.212354 Faker-9.9.1/faker/providers/company/tr_TR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1189 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/tr_TR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.212782 Faker-9.9.1/faker/providers/company/zh_CN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2164 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/zh_CN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.234552 Faker-9.9.1/faker/providers/company/zh_TW/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3054 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/company/zh_TW/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.234992 Faker-9.9.1/faker/providers/credit_card/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     7111 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/credit_card/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.235279 Faker-9.9.1/faker/providers/credit_card/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      157 2020-09-22 19:25:55.000000 Faker-9.9.1/faker/providers/credit_card/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.235603 Faker-9.9.1/faker/providers/credit_card/fa_IR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     5190 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/credit_card/fa_IR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.235889 Faker-9.9.1/faker/providers/credit_card/pt_PT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     5671 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/credit_card/pt_PT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.236253 Faker-9.9.1/faker/providers/credit_card/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3179 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/credit_card/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.236492 Faker-9.9.1/faker/providers/currency/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10794 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.236749 Faker-9.9.1/faker/providers/currency/cs_CZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      282 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/cs_CZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.236995 Faker-9.9.1/faker/providers/currency/de_AT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      292 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/de_AT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.237341 Faker-9.9.1/faker/providers/currency/de_DE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      285 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/de_DE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.237586 Faker-9.9.1/faker/providers/currency/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     7622 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.237837 Faker-9.9.1/faker/providers/currency/en_AU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      280 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/en_AU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.238084 Faker-9.9.1/faker/providers/currency/en_CA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      273 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/en_CA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.238329 Faker-9.9.1/faker/providers/currency/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      262 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/currency/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.238637 Faker-9.9.1/faker/providers/currency/es_ES/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6293 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/es_ES/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.238944 Faker-9.9.1/faker/providers/currency/fr_CA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      280 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/fr_CA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.239374 Faker-9.9.1/faker/providers/currency/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      285 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.239674 Faker-9.9.1/faker/providers/currency/it_IT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      285 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/it_IT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.240228 Faker-9.9.1/faker/providers/currency/nl_NL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      296 2021-10-19 14:31:10.000000 Faker-9.9.1/faker/providers/currency/nl_NL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.240707 Faker-9.9.1/faker/providers/currency/pl_PL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      282 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/pl_PL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.241239 Faker-9.9.1/faker/providers/currency/pt_BR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      263 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/currency/pt_BR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.241633 Faker-9.9.1/faker/providers/currency/ro_RO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      282 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/ro_RO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.242083 Faker-9.9.1/faker/providers/currency/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     8246 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.242642 Faker-9.9.1/faker/providers/currency/sk_SK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      285 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/currency/sk_SK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.243137 Faker-9.9.1/faker/providers/currency/sv_SE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     5844 2020-10-08 14:18:58.000000 Faker-9.9.1/faker/providers/currency/sv_SE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.243602 Faker-9.9.1/faker/providers/currency/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10596 2021-06-02 12:40:35.000000 Faker-9.9.1/faker/providers/currency/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.244059 Faker-9.9.1/faker/providers/date_time/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    81158 2021-11-29 18:11:05.000000 Faker-9.9.1/faker/providers/date_time/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.244789 Faker-9.9.1/faker/providers/date_time/ar_AA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    54779 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/ar_AA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.245540 Faker-9.9.1/faker/providers/date_time/ar_EG/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      465 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/ar_EG/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.245891 Faker-9.9.1/faker/providers/date_time/bn_BD/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1050 2021-10-19 14:31:10.000000 Faker-9.9.1/faker/providers/date_time/bn_BD/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.246427 Faker-9.9.1/faker/providers/date_time/cs_CZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      785 2020-05-24 19:30:00.000000 Faker-9.9.1/faker/providers/date_time/cs_CZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.247082 Faker-9.9.1/faker/providers/date_time/de_AT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      781 2020-05-24 19:30:00.000000 Faker-9.9.1/faker/providers/date_time/de_AT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.247692 Faker-9.9.1/faker/providers/date_time/de_DE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      780 2020-05-12 15:20:18.000000 Faker-9.9.1/faker/providers/date_time/de_DE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.248195 Faker-9.9.1/faker/providers/date_time/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      957 2021-10-07 15:44:38.000000 Faker-9.9.1/faker/providers/date_time/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.248756 Faker-9.9.1/faker/providers/date_time/en_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      144 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/en_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.249378 Faker-9.9.1/faker/providers/date_time/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       89 2019-10-15 17:30:33.000000 Faker-9.9.1/faker/providers/date_time/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.249934 Faker-9.9.1/faker/providers/date_time/es_ES/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      780 2020-05-24 19:30:00.000000 Faker-9.9.1/faker/providers/date_time/es_ES/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.250424 Faker-9.9.1/faker/providers/date_time/fil_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      829 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/fil_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.250723 Faker-9.9.1/faker/providers/date_time/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      869 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.251105 Faker-9.9.1/faker/providers/date_time/hi_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1065 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/hi_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.251540 Faker-9.9.1/faker/providers/date_time/hr_HR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      885 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/hr_HR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.251924 Faker-9.9.1/faker/providers/date_time/hu_HU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      894 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/hu_HU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.252284 Faker-9.9.1/faker/providers/date_time/hy_AM/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      929 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/hy_AM/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.252569 Faker-9.9.1/faker/providers/date_time/id_ID/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      861 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/id_ID/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.252857 Faker-9.9.1/faker/providers/date_time/it_IT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      792 2020-05-24 19:30:00.000000 Faker-9.9.1/faker/providers/date_time/it_IT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.253140 Faker-9.9.1/faker/providers/date_time/ko_KR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      862 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/ko_KR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.253532 Faker-9.9.1/faker/providers/date_time/nl_NL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      783 2021-10-04 15:24:45.000000 Faker-9.9.1/faker/providers/date_time/nl_NL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.253863 Faker-9.9.1/faker/providers/date_time/pl_PL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      801 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/pl_PL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.279858 Faker-9.9.1/faker/providers/date_time/pt_BR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      807 2021-08-20 18:05:18.000000 Faker-9.9.1/faker/providers/date_time/pt_BR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.280244 Faker-9.9.1/faker/providers/date_time/pt_PT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      807 2020-10-13 14:18:59.000000 Faker-9.9.1/faker/providers/date_time/pt_PT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.280507 Faker-9.9.1/faker/providers/date_time/ro_RO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      782 2021-06-02 12:40:45.000000 Faker-9.9.1/faker/providers/date_time/ro_RO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.280803 Faker-9.9.1/faker/providers/date_time/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    55616 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.281266 Faker-9.9.1/faker/providers/date_time/sk_SK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      779 2020-05-24 19:30:00.000000 Faker-9.9.1/faker/providers/date_time/sk_SK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.281735 Faker-9.9.1/faker/providers/date_time/sl_SI/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      868 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/sl_SI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.282044 Faker-9.9.1/faker/providers/date_time/ta_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1080 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/ta_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.282320 Faker-9.9.1/faker/providers/date_time/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    12290 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/date_time/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.282624 Faker-9.9.1/faker/providers/date_time/tl_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      155 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/date_time/tl_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.283002 Faker-9.9.1/faker/providers/date_time/tr_TR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      775 2020-05-24 19:30:00.000000 Faker-9.9.1/faker/providers/date_time/tr_TR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.283342 Faker-9.9.1/faker/providers/file/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    12990 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/file/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.283707 Faker-9.9.1/faker/providers/file/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       81 2019-10-15 17:30:33.000000 Faker-9.9.1/faker/providers/file/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.284192 Faker-9.9.1/faker/providers/geo/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    70599 2021-11-29 18:11:05.000000 Faker-9.9.1/faker/providers/geo/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.284963 Faker-9.9.1/faker/providers/geo/de_AT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      299 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/geo/de_AT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.285588 Faker-9.9.1/faker/providers/geo/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      989 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/geo/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.286258 Faker-9.9.1/faker/providers/geo/en_IE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3029 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/geo/en_IE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.286860 Faker-9.9.1/faker/providers/geo/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       81 2019-10-15 17:30:33.000000 Faker-9.9.1/faker/providers/geo/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.287321 Faker-9.9.1/faker/providers/geo/pt_PT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2669 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/geo/pt_PT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.287741 Faker-9.9.1/faker/providers/geo/tr_TR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6742 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/geo/tr_TR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.288068 Faker-9.9.1/faker/providers/internet/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    24149 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/internet/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.288500 Faker-9.9.1/faker/providers/internet/ar_AA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1095 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/ar_AA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.288805 Faker-9.9.1/faker/providers/internet/bg_BG/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2474 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/bg_BG/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.289187 Faker-9.9.1/faker/providers/internet/bs_BA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      566 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/bs_BA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.289812 Faker-9.9.1/faker/providers/internet/cs_CZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      803 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/cs_CZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.290413 Faker-9.9.1/faker/providers/internet/de_AT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      424 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/de_AT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.290904 Faker-9.9.1/faker/providers/internet/de_DE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      588 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/de_DE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.291214 Faker-9.9.1/faker/providers/internet/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2430 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.291539 Faker-9.9.1/faker/providers/internet/en_AU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      412 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/en_AU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.291915 Faker-9.9.1/faker/providers/internet/en_GB/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      552 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/en_GB/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.292559 Faker-9.9.1/faker/providers/internet/en_NZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      426 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/en_NZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.292981 Faker-9.9.1/faker/providers/internet/en_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2097 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/en_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.293501 Faker-9.9.1/faker/providers/internet/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       89 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/internet/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.294105 Faker-9.9.1/faker/providers/internet/es_ES/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      494 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/es_ES/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.294428 Faker-9.9.1/faker/providers/internet/fa_IR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      328 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/fa_IR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.295023 Faker-9.9.1/faker/providers/internet/fi_FI/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      333 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/fi_FI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.295629 Faker-9.9.1/faker/providers/internet/fil_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      167 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/fil_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.296159 Faker-9.9.1/faker/providers/internet/fr_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      770 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/fr_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.296702 Faker-9.9.1/faker/providers/internet/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      932 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.297072 Faker-9.9.1/faker/providers/internet/hr_HR/
+-rwxr-xr-x   0 flavio.curella   (502) staff       (20)      665 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/hr_HR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.297488 Faker-9.9.1/faker/providers/internet/hu_HU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      524 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/hu_HU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.297934 Faker-9.9.1/faker/providers/internet/id_ID/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      562 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/id_ID/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.298290 Faker-9.9.1/faker/providers/internet/it_IT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      828 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/it_IT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.298611 Faker-9.9.1/faker/providers/internet/ja_JP/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      523 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/ja_JP/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.298931 Faker-9.9.1/faker/providers/internet/ko_KR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      345 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/ko_KR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.299333 Faker-9.9.1/faker/providers/internet/no_NO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      450 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/no_NO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.299781 Faker-9.9.1/faker/providers/internet/pl_PL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      520 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/pl_PL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.326070 Faker-9.9.1/faker/providers/internet/pt_BR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      618 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/pt_BR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.326999 Faker-9.9.1/faker/providers/internet/pt_PT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      270 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/pt_PT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.327584 Faker-9.9.1/faker/providers/internet/ro_RO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      796 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/ro_RO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.328058 Faker-9.9.1/faker/providers/internet/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2234 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.328755 Faker-9.9.1/faker/providers/internet/sk_SK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      854 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/sk_SK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.329818 Faker-9.9.1/faker/providers/internet/sl_SI/
+-rwxr-xr-x   0 flavio.curella   (502) staff       (20)     1220 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/sl_SI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.330468 Faker-9.9.1/faker/providers/internet/sv_SE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      482 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/sv_SE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.331100 Faker-9.9.1/faker/providers/internet/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      670 2021-06-11 21:29:55.000000 Faker-9.9.1/faker/providers/internet/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.331661 Faker-9.9.1/faker/providers/internet/tl_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      167 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/tl_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.332610 Faker-9.9.1/faker/providers/internet/uk_UA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1722 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/uk_UA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.333036 Faker-9.9.1/faker/providers/internet/zh_CN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2550 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/zh_CN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.333497 Faker-9.9.1/faker/providers/internet/zh_TW/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      516 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/internet/zh_TW/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.334986 Faker-9.9.1/faker/providers/isbn/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3024 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/isbn/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.335595 Faker-9.9.1/faker/providers/isbn/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       81 2019-10-15 17:30:33.000000 Faker-9.9.1/faker/providers/isbn/en_US/__init__.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2680 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/isbn/isbn.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1824 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/isbn/rules.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.336180 Faker-9.9.1/faker/providers/job/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    21162 2021-10-19 14:31:10.000000 Faker-9.9.1/faker/providers/job/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.336848 Faker-9.9.1/faker/providers/job/ar_AA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3828 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/ar_AA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.337290 Faker-9.9.1/faker/providers/job/bs_BA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)   179846 2020-08-04 21:32:10.000000 Faker-9.9.1/faker/providers/job/bs_BA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.338048 Faker-9.9.1/faker/providers/job/de_DE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      953 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/de_DE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.338529 Faker-9.9.1/faker/providers/job/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    26642 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.339352 Faker-9.9.1/faker/providers/job/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       81 2019-10-15 17:30:33.000000 Faker-9.9.1/faker/providers/job/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.339840 Faker-9.9.1/faker/providers/job/fa_IR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2433 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/job/fa_IR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.340334 Faker-9.9.1/faker/providers/job/fi_FI/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6120 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/fi_FI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.340973 Faker-9.9.1/faker/providers/job/fr_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    43169 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/job/fr_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.342172 Faker-9.9.1/faker/providers/job/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    29131 2020-08-17 15:07:35.000000 Faker-9.9.1/faker/providers/job/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.342992 Faker-9.9.1/faker/providers/job/hr_HR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10408 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/job/hr_HR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.343581 Faker-9.9.1/faker/providers/job/hu_HU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    12939 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/hu_HU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.344359 Faker-9.9.1/faker/providers/job/hy_AM/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    11265 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/job/hy_AM/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.344808 Faker-9.9.1/faker/providers/job/ja_JP/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1635 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/ja_JP/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.345248 Faker-9.9.1/faker/providers/job/ko_KR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    16624 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/ko_KR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.345788 Faker-9.9.1/faker/providers/job/pl_PL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     5539 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/job/pl_PL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.346122 Faker-9.9.1/faker/providers/job/pt_BR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    20541 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/job/pt_BR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.346713 Faker-9.9.1/faker/providers/job/pt_PT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    18585 2020-10-01 14:43:39.000000 Faker-9.9.1/faker/providers/job/pt_PT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.347220 Faker-9.9.1/faker/providers/job/ro_RO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)   170683 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/ro_RO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.348257 Faker-9.9.1/faker/providers/job/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    18139 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.348746 Faker-9.9.1/faker/providers/job/sk_SK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    17587 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/sk_SK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.349217 Faker-9.9.1/faker/providers/job/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3883 2021-06-02 12:40:19.000000 Faker-9.9.1/faker/providers/job/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.375579 Faker-9.9.1/faker/providers/job/tr_TR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    17006 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/tr_TR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.376197 Faker-9.9.1/faker/providers/job/uk_UA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     5087 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/uk_UA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.376687 Faker-9.9.1/faker/providers/job/zh_CN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    28916 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/job/zh_CN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.377145 Faker-9.9.1/faker/providers/job/zh_TW/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    14340 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/job/zh_TW/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.377553 Faker-9.9.1/faker/providers/lorem/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9633 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/lorem/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.377867 Faker-9.9.1/faker/providers/lorem/ar_AA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    15983 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/ar_AA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.378261 Faker-9.9.1/faker/providers/lorem/cs_CZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    37358 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/cs_CZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.378730 Faker-9.9.1/faker/providers/lorem/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10015 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.379225 Faker-9.9.1/faker/providers/lorem/en_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2841 2021-11-29 18:11:00.000000 Faker-9.9.1/faker/providers/lorem/en_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.379529 Faker-9.9.1/faker/providers/lorem/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    17423 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.379877 Faker-9.9.1/faker/providers/lorem/fil_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    11282 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/fil_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.380244 Faker-9.9.1/faker/providers/lorem/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    27163 2020-09-22 19:25:55.000000 Faker-9.9.1/faker/providers/lorem/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.380959 Faker-9.9.1/faker/providers/lorem/he_IL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3287 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/he_IL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.381430 Faker-9.9.1/faker/providers/lorem/hy_AM/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     4687 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/hy_AM/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.381701 Faker-9.9.1/faker/providers/lorem/ja_JP/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     4797 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/ja_JP/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.381972 Faker-9.9.1/faker/providers/lorem/la/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3506 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/la/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.382363 Faker-9.9.1/faker/providers/lorem/pl_PL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    38418 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/pl_PL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.383103 Faker-9.9.1/faker/providers/lorem/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    13398 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.383488 Faker-9.9.1/faker/providers/lorem/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    11292 2021-06-02 12:40:34.000000 Faker-9.9.1/faker/providers/lorem/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.383963 Faker-9.9.1/faker/providers/lorem/tl_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      325 2020-09-22 19:25:55.000000 Faker-9.9.1/faker/providers/lorem/tl_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.384524 Faker-9.9.1/faker/providers/lorem/zh_CN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6408 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/zh_CN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.385324 Faker-9.9.1/faker/providers/lorem/zh_TW/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6408 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/lorem/zh_TW/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.385698 Faker-9.9.1/faker/providers/misc/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    28301 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/misc/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.386241 Faker-9.9.1/faker/providers/misc/en_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     4398 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/misc/en_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.386798 Faker-9.9.1/faker/providers/misc/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       81 2019-10-15 17:30:33.000000 Faker-9.9.1/faker/providers/misc/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.387288 Faker-9.9.1/faker/providers/misc/fil_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      151 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/misc/fil_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.388285 Faker-9.9.1/faker/providers/misc/tl_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      151 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/misc/tl_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.388941 Faker-9.9.1/faker/providers/person/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9354 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/person/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.389335 Faker-9.9.1/faker/providers/person/ar_AA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    24858 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/ar_AA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.389916 Faker-9.9.1/faker/providers/person/ar_PS/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1141 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/ar_PS/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.390379 Faker-9.9.1/faker/providers/person/ar_SA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1279 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/ar_SA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.391083 Faker-9.9.1/faker/providers/person/bg_BG/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    43245 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/bg_BG/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.391893 Faker-9.9.1/faker/providers/person/cs_CZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     7204 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/cs_CZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.392425 Faker-9.9.1/faker/providers/person/de_AT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    29783 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/de_AT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.392837 Faker-9.9.1/faker/providers/person/de_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    41031 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/de_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.393263 Faker-9.9.1/faker/providers/person/de_DE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    46673 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/de_DE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.393672 Faker-9.9.1/faker/providers/person/dk_DK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    11645 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/dk_DK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.393982 Faker-9.9.1/faker/providers/person/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    66301 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.394503 Faker-9.9.1/faker/providers/person/en/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)   139274 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/en/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.395236 Faker-9.9.1/faker/providers/person/en_GB/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    22799 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/en_GB/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.395753 Faker-9.9.1/faker/providers/person/en_IE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    58684 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/en_IE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.396349 Faker-9.9.1/faker/providers/person/en_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    12385 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/en_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.397082 Faker-9.9.1/faker/providers/person/en_NZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    40961 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/en_NZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.421117 Faker-9.9.1/faker/providers/person/en_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6008 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/en_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.421636 Faker-9.9.1/faker/providers/person/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    66194 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.422336 Faker-9.9.1/faker/providers/person/es/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3631 2021-11-02 21:08:47.000000 Faker-9.9.1/faker/providers/person/es/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.422596 Faker-9.9.1/faker/providers/person/es_CA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1720 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/es_CA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.422855 Faker-9.9.1/faker/providers/person/es_CO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    35716 2021-11-02 21:08:47.000000 Faker-9.9.1/faker/providers/person/es_CO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.423317 Faker-9.9.1/faker/providers/person/es_ES/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    39907 2021-11-02 21:08:47.000000 Faker-9.9.1/faker/providers/person/es_ES/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.423705 Faker-9.9.1/faker/providers/person/es_MX/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    18791 2021-11-02 21:08:47.000000 Faker-9.9.1/faker/providers/person/es_MX/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.424009 Faker-9.9.1/faker/providers/person/et_EE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    13913 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/et_EE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.424263 Faker-9.9.1/faker/providers/person/fa_IR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     8309 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/fa_IR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.424671 Faker-9.9.1/faker/providers/person/fi_FI/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    29043 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/fi_FI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.425025 Faker-9.9.1/faker/providers/person/fr_CA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9745 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/fr_CA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.425302 Faker-9.9.1/faker/providers/person/fr_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6997 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/fr_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.425558 Faker-9.9.1/faker/providers/person/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    12993 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.425976 Faker-9.9.1/faker/providers/person/fr_QC/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      290 2021-11-29 18:09:12.000000 Faker-9.9.1/faker/providers/person/fr_QC/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.426405 Faker-9.9.1/faker/providers/person/ga_IE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    73538 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/ga_IE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.427180 Faker-9.9.1/faker/providers/person/he_IL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    60492 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/he_IL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.427838 Faker-9.9.1/faker/providers/person/hi_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6585 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/hi_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.428310 Faker-9.9.1/faker/providers/person/hr_HR/
+-rwxr-xr-x   0 flavio.curella   (502) staff       (20)    19776 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/hr_HR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.428848 Faker-9.9.1/faker/providers/person/hu_HU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    16159 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/hu_HU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.429434 Faker-9.9.1/faker/providers/person/hy_AM/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    27051 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/hy_AM/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.430129 Faker-9.9.1/faker/providers/person/id_ID/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    19283 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/id_ID/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.430770 Faker-9.9.1/faker/providers/person/it_IT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    32695 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/it_IT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.431379 Faker-9.9.1/faker/providers/person/ja_JP/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10929 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/person/ja_JP/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.431842 Faker-9.9.1/faker/providers/person/ka_GE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    25812 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/ka_GE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.432438 Faker-9.9.1/faker/providers/person/ko_KR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     5579 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/ko_KR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.432898 Faker-9.9.1/faker/providers/person/lt_LT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     4706 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/lt_LT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.433384 Faker-9.9.1/faker/providers/person/lv_LV/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6766 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/lv_LV/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.433755 Faker-9.9.1/faker/providers/person/ne_NP/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    44009 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/ne_NP/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.434192 Faker-9.9.1/faker/providers/person/nl_NL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    32776 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/nl_NL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.434645 Faker-9.9.1/faker/providers/person/no_NO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     7074 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/no_NO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.435005 Faker-9.9.1/faker/providers/person/or_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    35828 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/or_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.435472 Faker-9.9.1/faker/providers/person/pl_PL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    95392 2021-11-29 18:11:06.000000 Faker-9.9.1/faker/providers/person/pl_PL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.436096 Faker-9.9.1/faker/providers/person/pt_BR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     7230 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/pt_BR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.436392 Faker-9.9.1/faker/providers/person/pt_PT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6791 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/pt_PT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.436646 Faker-9.9.1/faker/providers/person/ro_RO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    14264 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/ro_RO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.437054 Faker-9.9.1/faker/providers/person/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    37558 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.437509 Faker-9.9.1/faker/providers/person/sl_SI/
+-rwxr-xr-x   0 flavio.curella   (502) staff       (20)     9540 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/sl_SI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.468068 Faker-9.9.1/faker/providers/person/sv_SE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    21588 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/sv_SE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.468559 Faker-9.9.1/faker/providers/person/ta_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    35625 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/ta_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.468954 Faker-9.9.1/faker/providers/person/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    35440 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.469354 Faker-9.9.1/faker/providers/person/tr_TR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    30905 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/tr_TR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.469710 Faker-9.9.1/faker/providers/person/tw_GH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    11402 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/tw_GH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.470021 Faker-9.9.1/faker/providers/person/uk_UA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    19506 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/uk_UA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.470353 Faker-9.9.1/faker/providers/person/zh_CN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    16427 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/zh_CN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.470740 Faker-9.9.1/faker/providers/person/zh_TW/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    15875 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/person/zh_TW/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.471052 Faker-9.9.1/faker/providers/phone_number/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     5811 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.471516 Faker-9.9.1/faker/providers/phone_number/ar_AE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2580 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/phone_number/ar_AE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.471855 Faker-9.9.1/faker/providers/phone_number/ar_JO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1772 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/ar_JO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.472165 Faker-9.9.1/faker/providers/phone_number/ar_PS/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3605 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/phone_number/ar_PS/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.472474 Faker-9.9.1/faker/providers/phone_number/bg_BG/
+-rwxr-xr-x   0 flavio.curella   (502) staff       (20)      390 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/bg_BG/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.472772 Faker-9.9.1/faker/providers/phone_number/bs_BA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      879 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/bs_BA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.473065 Faker-9.9.1/faker/providers/phone_number/cs_CZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      913 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/cs_CZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.473416 Faker-9.9.1/faker/providers/phone_number/de_DE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      455 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/de_DE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.473719 Faker-9.9.1/faker/providers/phone_number/dk_DK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      395 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/dk_DK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.474027 Faker-9.9.1/faker/providers/phone_number/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      523 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.474348 Faker-9.9.1/faker/providers/phone_number/en_AU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1317 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/en_AU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.474662 Faker-9.9.1/faker/providers/phone_number/en_CA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      349 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/en_CA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.474956 Faker-9.9.1/faker/providers/phone_number/en_GB/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     7437 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/en_GB/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.475329 Faker-9.9.1/faker/providers/phone_number/en_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      178 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/en_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.475653 Faker-9.9.1/faker/providers/phone_number/en_NZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1247 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/en_NZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.475952 Faker-9.9.1/faker/providers/phone_number/en_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     8171 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/phone_number/en_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.476288 Faker-9.9.1/faker/providers/phone_number/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1281 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.476603 Faker-9.9.1/faker/providers/phone_number/es_CO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1043 2021-11-02 21:08:47.000000 Faker-9.9.1/faker/providers/phone_number/es_CO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.476965 Faker-9.9.1/faker/providers/phone_number/es_ES/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1504 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/es_ES/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.477419 Faker-9.9.1/faker/providers/phone_number/es_MX/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      765 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/es_MX/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.477818 Faker-9.9.1/faker/providers/phone_number/fa_IR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2658 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/fa_IR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.478155 Faker-9.9.1/faker/providers/phone_number/fi_FI/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      260 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/fi_FI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.478468 Faker-9.9.1/faker/providers/phone_number/fil_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      177 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/fil_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.478788 Faker-9.9.1/faker/providers/phone_number/fr_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      979 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/fr_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.479098 Faker-9.9.1/faker/providers/phone_number/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     4471 2021-10-27 16:49:52.000000 Faker-9.9.1/faker/providers/phone_number/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.479444 Faker-9.9.1/faker/providers/phone_number/he_IL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      468 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/he_IL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.479775 Faker-9.9.1/faker/providers/phone_number/hi_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      232 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/hi_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.480102 Faker-9.9.1/faker/providers/phone_number/hr_HR/
+-rwxr-xr-x   0 flavio.curella   (502) staff       (20)      803 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/hr_HR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.480481 Faker-9.9.1/faker/providers/phone_number/hu_HU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      284 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/hu_HU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.480809 Faker-9.9.1/faker/providers/phone_number/hy_AM/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      442 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/hy_AM/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.481135 Faker-9.9.1/faker/providers/phone_number/id_ID/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      648 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/id_ID/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.481471 Faker-9.9.1/faker/providers/phone_number/it_IT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      303 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/it_IT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.481811 Faker-9.9.1/faker/providers/phone_number/ja_JP/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      207 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/ja_JP/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.482140 Faker-9.9.1/faker/providers/phone_number/ko_KR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      686 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/ko_KR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.482713 Faker-9.9.1/faker/providers/phone_number/lt_LT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      184 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/lt_LT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.483123 Faker-9.9.1/faker/providers/phone_number/lv_LV/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      184 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/lv_LV/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.483541 Faker-9.9.1/faker/providers/phone_number/ne_NP/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      229 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/ne_NP/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.483886 Faker-9.9.1/faker/providers/phone_number/nl_BE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      512 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/nl_BE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.484246 Faker-9.9.1/faker/providers/phone_number/nl_NL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      512 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/nl_NL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.484591 Faker-9.9.1/faker/providers/phone_number/no_NO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      328 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/no_NO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.484927 Faker-9.9.1/faker/providers/phone_number/pl_PL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      895 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/pl_PL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.485278 Faker-9.9.1/faker/providers/phone_number/pt_BR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3537 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/pt_BR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.485612 Faker-9.9.1/faker/providers/phone_number/pt_PT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1013 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/pt_PT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.485967 Faker-9.9.1/faker/providers/phone_number/ro_RO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2484 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/ro_RO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.486346 Faker-9.9.1/faker/providers/phone_number/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      379 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.549991 Faker-9.9.1/faker/providers/phone_number/sk_SK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      387 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/sk_SK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.605397 Faker-9.9.1/faker/providers/phone_number/sl_SI/
+-rwxr-xr-x   0 flavio.curella   (502) staff       (20)      361 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/sl_SI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.605978 Faker-9.9.1/faker/providers/phone_number/sv_SE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      367 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/sv_SE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.606471 Faker-9.9.1/faker/providers/phone_number/ta_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      232 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/ta_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.613469 Faker-9.9.1/faker/providers/phone_number/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1826 2021-06-02 12:40:17.000000 Faker-9.9.1/faker/providers/phone_number/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.614209 Faker-9.9.1/faker/providers/phone_number/tl_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      177 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/tl_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.614572 Faker-9.9.1/faker/providers/phone_number/tr_TR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      349 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/tr_TR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.614865 Faker-9.9.1/faker/providers/phone_number/tw_GH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      578 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/tw_GH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.615161 Faker-9.9.1/faker/providers/phone_number/uk_UA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      318 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/uk_UA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.615732 Faker-9.9.1/faker/providers/phone_number/zh_CN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      681 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/zh_CN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.616100 Faker-9.9.1/faker/providers/phone_number/zh_TW/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      348 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/phone_number/zh_TW/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.616556 Faker-9.9.1/faker/providers/profile/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2082 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/profile/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.719165 Faker-9.9.1/faker/providers/profile/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      127 2021-06-02 12:40:21.000000 Faker-9.9.1/faker/providers/profile/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.719929 Faker-9.9.1/faker/providers/python/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    16099 2021-12-07 15:54:38.000000 Faker-9.9.1/faker/providers/python/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.720526 Faker-9.9.1/faker/providers/python/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      125 2021-06-02 12:40:21.000000 Faker-9.9.1/faker/providers/python/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.720900 Faker-9.9.1/faker/providers/ssn/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      235 2021-10-19 14:31:10.000000 Faker-9.9.1/faker/providers/ssn/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.721249 Faker-9.9.1/faker/providers/ssn/bg_BG/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      447 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/bg_BG/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.721588 Faker-9.9.1/faker/providers/ssn/cs_CZ/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1418 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/ssn/cs_CZ/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.721916 Faker-9.9.1/faker/providers/ssn/de_AT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      407 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/de_AT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.722250 Faker-9.9.1/faker/providers/ssn/de_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       86 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/ssn/de_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.722644 Faker-9.9.1/faker/providers/ssn/de_DE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      403 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/de_DE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.723010 Faker-9.9.1/faker/providers/ssn/dk_DK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      344 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/dk_DK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.723356 Faker-9.9.1/faker/providers/ssn/el_CY/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      348 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/el_CY/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.723800 Faker-9.9.1/faker/providers/ssn/el_GR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      803 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/el_GR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.724177 Faker-9.9.1/faker/providers/ssn/en_CA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2968 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/en_CA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.724533 Faker-9.9.1/faker/providers/ssn/en_GB/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1303 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/en_GB/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.724877 Faker-9.9.1/faker/providers/ssn/en_IE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      459 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/en_IE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.725268 Faker-9.9.1/faker/providers/ssn/en_IN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      731 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/en_IN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.725634 Faker-9.9.1/faker/providers/ssn/en_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2638 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/en_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.726138 Faker-9.9.1/faker/providers/ssn/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6852 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/ssn/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.726514 Faker-9.9.1/faker/providers/ssn/es_CA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      157 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/ssn/es_CA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.726855 Faker-9.9.1/faker/providers/ssn/es_CO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2108 2021-11-29 18:09:14.000000 Faker-9.9.1/faker/providers/ssn/es_CO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.727199 Faker-9.9.1/faker/providers/ssn/es_ES/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3387 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/ssn/es_ES/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.727538 Faker-9.9.1/faker/providers/ssn/es_MX/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     5725 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/ssn/es_MX/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.727917 Faker-9.9.1/faker/providers/ssn/et_EE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2742 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/ssn/et_EE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.728248 Faker-9.9.1/faker/providers/ssn/fi_FI/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2485 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/ssn/fi_FI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.728576 Faker-9.9.1/faker/providers/ssn/fil_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      152 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/fil_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.728899 Faker-9.9.1/faker/providers/ssn/fr_CH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1523 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/fr_CH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.729234 Faker-9.9.1/faker/providers/ssn/fr_FR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6772 2021-10-27 16:43:00.000000 Faker-9.9.1/faker/providers/ssn/fr_FR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.729595 Faker-9.9.1/faker/providers/ssn/he_IL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      830 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/he_IL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.729919 Faker-9.9.1/faker/providers/ssn/hr_HR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1453 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/hr_HR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.730243 Faker-9.9.1/faker/providers/ssn/hu_HU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     4387 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/ssn/hu_HU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.730634 Faker-9.9.1/faker/providers/ssn/it_IT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1925 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/ssn/it_IT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.730968 Faker-9.9.1/faker/providers/ssn/ko_KR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      252 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/ko_KR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.731314 Faker-9.9.1/faker/providers/ssn/lb_LU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      416 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/lb_LU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.790482 Faker-9.9.1/faker/providers/ssn/lt_LT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      451 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/lt_LT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.791227 Faker-9.9.1/faker/providers/ssn/lv_LV/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      407 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/lv_LV/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.791732 Faker-9.9.1/faker/providers/ssn/mt_MT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      404 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/mt_MT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.792223 Faker-9.9.1/faker/providers/ssn/nl_BE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2332 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/nl_BE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.792745 Faker-9.9.1/faker/providers/ssn/nl_NL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1622 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/nl_NL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.793343 Faker-9.9.1/faker/providers/ssn/no_NO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3339 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/ssn/no_NO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.793851 Faker-9.9.1/faker/providers/ssn/pl_PL/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2200 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/pl_PL/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.794355 Faker-9.9.1/faker/providers/ssn/pt_BR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1823 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/pt_BR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.794844 Faker-9.9.1/faker/providers/ssn/pt_PT/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      411 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/pt_PT/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.795282 Faker-9.9.1/faker/providers/ssn/ro_RO/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3472 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/ro_RO/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.795700 Faker-9.9.1/faker/providers/ssn/ru_RU/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      106 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/providers/ssn/ru_RU/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.796095 Faker-9.9.1/faker/providers/ssn/sk_SK/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1370 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/ssn/sk_SK/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.796539 Faker-9.9.1/faker/providers/ssn/sl_SI/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      408 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/sl_SI/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.810600 Faker-9.9.1/faker/providers/ssn/sv_SE/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3016 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/ssn/sv_SE/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.810936 Faker-9.9.1/faker/providers/ssn/th_TH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1892 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/providers/ssn/th_TH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.817542 Faker-9.9.1/faker/providers/ssn/tl_PH/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      152 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/tl_PH/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.818051 Faker-9.9.1/faker/providers/ssn/tr_TR/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      632 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/tr_TR/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.818684 Faker-9.9.1/faker/providers/ssn/uk_UA/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1138 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/providers/ssn/uk_UA/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.819376 Faker-9.9.1/faker/providers/ssn/zh_CN/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    64760 2021-11-29 18:11:05.000000 Faker-9.9.1/faker/providers/ssn/zh_CN/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.820148 Faker-9.9.1/faker/providers/ssn/zh_TW/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      206 2021-10-19 14:31:10.000000 Faker-9.9.1/faker/providers/ssn/zh_TW/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.820547 Faker-9.9.1/faker/providers/user_agent/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    11120 2021-11-29 18:11:02.000000 Faker-9.9.1/faker/providers/user_agent/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.820907 Faker-9.9.1/faker/providers/user_agent/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      131 2021-06-02 12:40:21.000000 Faker-9.9.1/faker/providers/user_agent/en_US/__init__.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10945 2021-11-29 18:15:42.000000 Faker-9.9.1/faker/proxy.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)        0 2021-07-14 14:24:37.000000 Faker-9.9.1/faker/py.typed
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      398 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/typing.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.823402 Faker-9.9.1/faker/utils/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)        0 2020-01-14 18:13:54.000000 Faker-9.9.1/faker/utils/__init__.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      629 2021-06-02 12:40:23.000000 Faker-9.9.1/faker/utils/checksums.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      535 2021-11-29 18:09:18.000000 Faker-9.9.1/faker/utils/datasets.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      950 2021-10-22 22:30:06.000000 Faker-9.9.1/faker/utils/decorators.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2312 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/utils/distribution.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1753 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/utils/loading.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1039 2021-11-29 18:11:01.000000 Faker-9.9.1/faker/utils/text.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      268 2021-10-19 14:31:10.000000 Faker-9.9.1/mypy.ini
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      200 2021-12-07 15:55:50.889390 Faker-9.9.1/setup.cfg
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2578 2021-11-29 18:09:10.000000 Faker-9.9.1/setup.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.825447 Faker-9.9.1/tests/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)        0 2019-10-15 17:30:33.000000 Faker-9.9.1/tests/__init__.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       30 2020-10-08 14:43:43.000000 Faker-9.9.1/tests/conftest.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.825691 Faker-9.9.1/tests/mymodule/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       17 2019-10-15 17:30:33.000000 Faker-9.9.1/tests/mymodule/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.825937 Faker-9.9.1/tests/mymodule/en_US/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      113 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/mymodule/en_US/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.869155 Faker-9.9.1/tests/providers/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10006 2021-11-29 18:11:02.000000 Faker-9.9.1/tests/providers/__init__.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1049 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/providers/conftest.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    71204 2021-11-29 18:11:06.000000 Faker-9.9.1/tests/providers/test_address.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9670 2021-11-29 18:11:02.000000 Faker-9.9.1/tests/providers/test_automotive.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9600 2021-11-23 14:57:26.000000 Faker-9.9.1/tests/providers/test_bank.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    13075 2021-11-29 18:11:03.000000 Faker-9.9.1/tests/providers/test_barcode.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    14289 2021-11-29 18:11:03.000000 Faker-9.9.1/tests/providers/test_color.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    16757 2021-11-29 18:15:42.000000 Faker-9.9.1/tests/providers/test_company.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     6303 2021-11-29 18:09:11.000000 Faker-9.9.1/tests/providers/test_credit_card.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    12133 2021-11-29 18:11:03.000000 Faker-9.9.1/tests/providers/test_currency.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    40088 2021-11-29 18:11:05.000000 Faker-9.9.1/tests/providers/test_date_time.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2128 2021-10-25 16:25:41.000000 Faker-9.9.1/tests/providers/test_dynamic.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1579 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/providers/test_file.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3542 2021-11-29 18:11:02.000000 Faker-9.9.1/tests/providers/test_geo.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    29607 2021-11-29 18:11:04.000000 Faker-9.9.1/tests/providers/test_internet.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2585 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/providers/test_isbn.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     3504 2021-06-02 12:40:45.000000 Faker-9.9.1/tests/providers/test_job.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     9887 2021-11-29 18:11:03.000000 Faker-9.9.1/tests/providers/test_lorem.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    25747 2021-11-29 18:11:04.000000 Faker-9.9.1/tests/providers/test_misc.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    34319 2021-11-29 18:15:42.000000 Faker-9.9.1/tests/providers/test_person.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    13276 2021-11-29 18:11:04.000000 Faker-9.9.1/tests/providers/test_phone_number.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1523 2021-06-02 12:40:21.000000 Faker-9.9.1/tests/providers/test_profile.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    17225 2021-12-07 15:54:38.000000 Faker-9.9.1/tests/providers/test_python.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    37291 2021-11-29 18:15:42.000000 Faker-9.9.1/tests/providers/test_ssn.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1430 2021-11-29 18:11:03.000000 Faker-9.9.1/tests/providers/test_user_agent.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.870949 Faker-9.9.1/tests/pytest/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)        0 2020-05-12 15:20:18.000000 Faker-9.9.1/tests/pytest/__init__.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.886207 Faker-9.9.1/tests/pytest/session_overrides/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)        0 2020-05-12 15:20:18.000000 Faker-9.9.1/tests/pytest/session_overrides/__init__.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      940 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/pytest/session_overrides/conftest.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.887677 Faker-9.9.1/tests/pytest/session_overrides/session_locale/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)       28 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/pytest/session_overrides/session_locale/__init__.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)      193 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/pytest/session_overrides/session_locale/conftest.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1262 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/pytest/session_overrides/session_locale/test_autouse_faker_locale.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1233 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/pytest/session_overrides/session_locale/test_autouse_faker_seed.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1647 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/pytest/session_overrides/session_locale/test_manual_injection.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1203 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/pytest/test_autouse_faker_locale.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1213 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/pytest/test_autouse_faker_seed.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1603 2021-10-22 22:30:06.000000 Faker-9.9.1/tests/pytest/test_manual_injection.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1184 2020-10-08 14:43:43.000000 Faker-9.9.1/tests/pytest/test_unique_clear.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    10512 2021-11-29 18:11:04.000000 Faker-9.9.1/tests/test_factory.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     5224 2021-11-29 18:11:04.000000 Faker-9.9.1/tests/test_generator.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     2599 2021-01-11 16:08:11.000000 Faker-9.9.1/tests/test_providers_formats.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)    15812 2021-11-29 18:11:04.000000 Faker-9.9.1/tests/test_proxy.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     1955 2021-11-29 18:11:04.000000 Faker-9.9.1/tests/test_unique.py
+drwxr-xr-x   0 flavio.curella   (502) staff       (20)        0 2021-12-07 15:55:50.888381 Faker-9.9.1/tests/utils/
+-rw-r--r--   0 flavio.curella   (502) staff       (20)        0 2019-10-15 17:30:33.000000 Faker-9.9.1/tests/utils/__init__.py
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     7346 2019-10-15 17:30:33.000000 Faker-9.9.1/tests/utils/random_state.json
+-rw-r--r--   0 flavio.curella   (502) staff       (20)     4474 2021-11-29 18:15:42.000000 Faker-9.9.1/tests/utils/test_utils.py
```

### Comparing `Faker-9.9.0/CHANGELOG.md` & `Faker-9.9.1/CHANGELOG.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,13 @@
 ## Changelog
 
+### [v9.9.1 - 2021-11-29](https://github.com/joke2k/faker/compare/v9.8.4...v9.9.0)
+
+* Revert "deprecate positional `allowed_types`".
+
 ### [v9.9.0 - 2021-11-29](https://github.com/joke2k/faker/compare/v9.8.4...v9.9.0)
 
 * deprecate positional `allowed_types` (#1573). Thanks @fcurella.
 
 ### [v9.8.4 - 2021-11-29](https://github.com/joke2k/faker/compare/v9.8.3...v9.8.4)
 
 * Fix positional ``value_types``.
```

### Comparing `Faker-9.9.0/CONTRIBUTING.rst` & `Faker-9.9.1/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/Faker.egg-info/PKG-INFO` & `Faker-9.9.1/README.rst`

 * *Files 6% similar despite different names*

```diff
@@ -1,36 +1,7 @@
-Metadata-Version: 2.1
-Name: Faker
-Version: 9.9.0
-Summary: Faker is a Python package that generates fake data for you.
-Home-page: https://github.com/joke2k/faker
-Author: joke2k
-Author-email: joke2k@gmail.com
-License: MIT License
-Keywords: faker fixtures data test mock generator
-Platform: any
-Classifier: Development Status :: 5 - Production/Stable
-Classifier: Environment :: Console
-Classifier: Intended Audience :: Developers
-Classifier: Programming Language :: Python
-Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3 :: Only
-Classifier: Programming Language :: Python :: 3.6
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: Implementation :: CPython
-Classifier: Programming Language :: Python :: Implementation :: PyPy
-Classifier: Topic :: Software Development :: Libraries :: Python Modules
-Classifier: Topic :: Software Development :: Testing
-Classifier: Topic :: Utilities
-Classifier: License :: OSI Approved :: MIT License
-Requires-Python: >=3.6
-License-File: LICENSE.txt
-
 *Faker* is a Python package that generates fake data for you. Whether
 you need to bootstrap your database, create good-looking XML documents,
 fill-in your persistence to stress test it, or anonymize data taken from
 a production service, Faker is for you.
 
 Faker is heavily inspired by `PHP Faker`_, `Perl Faker`_, and by `Ruby Faker`_.
 
@@ -504,9 +475,7 @@
 .. |build| image:: https://github.com/joke2k/faker/workflows/Python%20Tests/badge.svg?branch=master&event=push
     :target: https://github.com/joke2k/faker/actions?query=workflow%3A%22Python+Tests%22+branch%3Amaster+event%3Apush
     :alt: Build status of the master branch on Mac/Linux
 
 .. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
     :target: https://raw.githubusercontent.com/joke2k/faker/master/LICENSE.txt
     :alt: Package license
-
-
```

### Comparing `Faker-9.9.0/Faker.egg-info/SOURCES.txt` & `Faker-9.9.1/Faker.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/LICENSE.txt` & `Faker-9.9.1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/MANIFEST.in` & `Faker-9.9.1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/RELEASE_PROCESS.rst` & `Faker-9.9.1/RELEASE_PROCESS.rst`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/cli.py` & `Faker-9.9.1/faker/cli.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/contrib/pytest/plugin.py` & `Faker-9.9.1/faker/contrib/pytest/plugin.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/documentor.py` & `Faker-9.9.1/faker/documentor.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/factory.py` & `Faker-9.9.1/faker/factory.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/generator.py` & `Faker-9.9.1/faker/generator.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/__init__.py` & `Faker-9.9.1/faker/providers/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/__init__.py` & `Faker-9.9.1/faker/providers/address/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/cs_CZ/__init__.py` & `Faker-9.9.1/faker/providers/address/cs_CZ/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/da_DK/__init__.py` & `Faker-9.9.1/faker/providers/address/da_DK/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/de/__init__.py` & `Faker-9.9.1/faker/providers/address/de/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/de_AT/__init__.py` & `Faker-9.9.1/faker/providers/address/de_AT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/de_CH/__init__.py` & `Faker-9.9.1/faker/providers/address/de_CH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/de_DE/__init__.py` & `Faker-9.9.1/faker/providers/address/de_DE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/el_GR/__init__.py` & `Faker-9.9.1/faker/providers/address/el_GR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/en/__init__.py` & `Faker-9.9.1/faker/providers/address/en/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/en_AU/__init__.py` & `Faker-9.9.1/faker/providers/address/en_AU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/en_CA/__init__.py` & `Faker-9.9.1/faker/providers/address/en_CA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/en_GB/__init__.py` & `Faker-9.9.1/faker/providers/address/en_GB/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/en_IE/__init__.py` & `Faker-9.9.1/faker/providers/address/en_IE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/en_IN/__init__.py` & `Faker-9.9.1/faker/providers/address/en_IN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/en_NZ/__init__.py` & `Faker-9.9.1/faker/providers/address/en_NZ/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/en_PH/__init__.py` & `Faker-9.9.1/faker/providers/address/en_PH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/en_US/__init__.py` & `Faker-9.9.1/faker/providers/address/en_US/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/es/__init__.py` & `Faker-9.9.1/faker/providers/address/es/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/es_CO/__init__.py` & `Faker-9.9.1/faker/providers/address/es_CO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/es_ES/__init__.py` & `Faker-9.9.1/faker/providers/address/es_ES/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/es_MX/__init__.py` & `Faker-9.9.1/faker/providers/address/es_MX/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/fa_IR/__init__.py` & `Faker-9.9.1/faker/providers/address/fa_IR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/fi_FI/__init__.py` & `Faker-9.9.1/faker/providers/address/fi_FI/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/fr_CH/__init__.py` & `Faker-9.9.1/faker/providers/address/fr_CH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/fr_FR/__init__.py` & `Faker-9.9.1/faker/providers/address/fr_FR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/he_IL/__init__.py` & `Faker-9.9.1/faker/providers/address/he_IL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/hi_IN/__init__.py` & `Faker-9.9.1/faker/providers/address/hi_IN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/hr_HR/__init__.py` & `Faker-9.9.1/faker/providers/address/hr_HR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/hu_HU/__init__.py` & `Faker-9.9.1/faker/providers/address/hu_HU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/hy_AM/__init__.py` & `Faker-9.9.1/faker/providers/address/hy_AM/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/id_ID/__init__.py` & `Faker-9.9.1/faker/providers/address/id_ID/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/it_IT/__init__.py` & `Faker-9.9.1/faker/providers/address/it_IT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/ja_JP/__init__.py` & `Faker-9.9.1/faker/providers/address/ja_JP/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/ka_GE/__init__.py` & `Faker-9.9.1/faker/providers/address/ka_GE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/ko_KR/__init__.py` & `Faker-9.9.1/faker/providers/address/ko_KR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/ne_NP/__init__.py` & `Faker-9.9.1/faker/providers/address/ne_NP/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/nl_BE/__init__.py` & `Faker-9.9.1/faker/providers/address/nl_BE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/nl_NL/__init__.py` & `Faker-9.9.1/faker/providers/address/nl_NL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/no_NO/__init__.py` & `Faker-9.9.1/faker/providers/address/no_NO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/pl_PL/__init__.py` & `Faker-9.9.1/faker/providers/address/pl_PL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/pt_BR/__init__.py` & `Faker-9.9.1/faker/providers/address/pt_BR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/pt_PT/__init__.py` & `Faker-9.9.1/faker/providers/address/pt_PT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/ro_RO/__init__.py` & `Faker-9.9.1/faker/providers/address/ro_RO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/ru_RU/__init__.py` & `Faker-9.9.1/faker/providers/address/ru_RU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/sk_SK/__init__.py` & `Faker-9.9.1/faker/providers/address/sk_SK/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/sl_SI/__init__.py` & `Faker-9.9.1/faker/providers/address/sl_SI/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/sv_SE/__init__.py` & `Faker-9.9.1/faker/providers/address/sv_SE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/ta_IN/__init__.py` & `Faker-9.9.1/faker/providers/address/ta_IN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/th/__init__.py` & `Faker-9.9.1/faker/providers/address/th/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/address/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/uk_UA/__init__.py` & `Faker-9.9.1/faker/providers/address/uk_UA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/zh_CN/__init__.py` & `Faker-9.9.1/faker/providers/address/zh_CN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/address/zh_TW/__init__.py` & `Faker-9.9.1/faker/providers/address/zh_TW/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/__init__.py` & `Faker-9.9.1/faker/providers/automotive/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/ar_JO/__init__.py` & `Faker-9.9.1/faker/providers/automotive/ar_JO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/ar_PS/__init__.py` & `Faker-9.9.1/faker/providers/automotive/ar_PS/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/ar_SA/__init__.py` & `Faker-9.9.1/faker/providers/automotive/ar_SA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/de_DE/__init__.py` & `Faker-9.9.1/faker/providers/automotive/de_DE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/el_GR/__init__.py` & `Faker-9.9.1/faker/providers/automotive/el_GR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/en_CA/__init__.py` & `Faker-9.9.1/faker/providers/automotive/en_CA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/en_NZ/__init__.py` & `Faker-9.9.1/faker/providers/automotive/en_NZ/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/en_PH/__init__.py` & `Faker-9.9.1/faker/providers/automotive/en_PH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/en_US/__init__.py` & `Faker-9.9.1/faker/providers/automotive/en_US/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/es_ES/__init__.py` & `Faker-9.9.1/faker/providers/automotive/es_ES/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/nl_NL/__init__.py` & `Faker-9.9.1/faker/providers/automotive/nl_NL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/pl_PL/__init__.py` & `Faker-9.9.1/faker/providers/automotive/pl_PL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/ro_RO/__init__.py` & `Faker-9.9.1/faker/providers/automotive/ro_RO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/ru_RU/__init__.py` & `Faker-9.9.1/faker/providers/automotive/ru_RU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/sk_SK/__init__.py` & `Faker-9.9.1/faker/providers/automotive/sk_SK/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/automotive/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/automotive/tr_TR/__init__.py` & `Faker-9.9.1/faker/providers/automotive/tr_TR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/bank/__init__.py` & `Faker-9.9.1/faker/providers/bank/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/bank/en_PH/__init__.py` & `Faker-9.9.1/faker/providers/bank/en_PH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/bank/ro_RO/__init__.py` & `Faker-9.9.1/faker/providers/bank/ro_RO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/bank/ru_RU/__init__.py` & `Faker-9.9.1/faker/providers/bank/ru_RU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/bank/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/bank/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/barcode/__init__.py` & `Faker-9.9.1/faker/providers/barcode/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/barcode/en_CA/__init__.py` & `Faker-9.9.1/faker/providers/barcode/en_CA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/barcode/en_US/__init__.py` & `Faker-9.9.1/faker/providers/barcode/en_US/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/barcode/ja_JP/__init__.py` & `Faker-9.9.1/faker/providers/barcode/ja_JP/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/__init__.py` & `Faker-9.9.1/faker/providers/color/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/ar_PS/__init__.py` & `Faker-9.9.1/faker/providers/color/ar_PS/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/bg_BG/__init__.py` & `Faker-9.9.1/faker/providers/color/bg_BG/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/color.py` & `Faker-9.9.1/faker/providers/color/color.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/el_GR/__init__.py` & `Faker-9.9.1/faker/providers/color/el_GR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/es_ES/__init__.py` & `Faker-9.9.1/faker/providers/color/es_ES/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/fa_IR/__init__.py` & `Faker-9.9.1/faker/providers/color/fa_IR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/fr_FR/__init__.py` & `Faker-9.9.1/faker/providers/color/fr_FR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/he_IL/__init__.py` & `Faker-9.9.1/faker/providers/color/he_IL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/hr_HR/__init__.py` & `Faker-9.9.1/faker/providers/color/hr_HR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/hy_AM/__init__.py` & `Faker-9.9.1/faker/providers/color/hy_AM/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/pt_BR/__init__.py` & `Faker-9.9.1/faker/providers/color/pt_BR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/ru_RU/__init__.py` & `Faker-9.9.1/faker/providers/color/ru_RU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/color/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/color/uk_UA/__init__.py` & `Faker-9.9.1/faker/providers/color/uk_UA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/__init__.py` & `Faker-9.9.1/faker/providers/company/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/bg_BG/__init__.py` & `Faker-9.9.1/faker/providers/company/bg_BG/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/de_DE/__init__.py` & `Faker-9.9.1/faker/providers/company/de_DE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/en_PH/__init__.py` & `Faker-9.9.1/faker/providers/company/en_PH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/es_MX/__init__.py` & `Faker-9.9.1/faker/providers/company/es_MX/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/fa_IR/__init__.py` & `Faker-9.9.1/faker/providers/company/fa_IR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/fi_FI/__init__.py` & `Faker-9.9.1/faker/providers/company/fi_FI/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/fil_PH/__init__.py` & `Faker-9.9.1/faker/providers/company/fil_PH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/fr_CH/__init__.py` & `Faker-9.9.1/faker/providers/company/fr_CH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/fr_FR/__init__.py` & `Faker-9.9.1/faker/providers/company/fr_FR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/hy_AM/__init__.py` & `Faker-9.9.1/faker/providers/company/hy_AM/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/id_ID/__init__.py` & `Faker-9.9.1/faker/providers/company/id_ID/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/it_IT/__init__.py` & `Faker-9.9.1/faker/providers/company/it_IT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/ja_JP/__init__.py` & `Faker-9.9.1/faker/providers/company/ja_JP/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/ko_KR/__init__.py` & `Faker-9.9.1/faker/providers/company/ko_KR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/nl_NL/__init__.py` & `Faker-9.9.1/faker/providers/company/nl_NL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/no_NO/__init__.py` & `Faker-9.9.1/faker/providers/company/no_NO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/pl_PL/__init__.py` & `Faker-9.9.1/faker/providers/company/pl_PL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/pt_BR/__init__.py` & `Faker-9.9.1/faker/providers/company/pt_BR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/pt_PT/__init__.py` & `Faker-9.9.1/faker/providers/company/pt_PT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/ro_RO/__init__.py` & `Faker-9.9.1/faker/providers/company/ro_RO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/ru_RU/__init__.py` & `Faker-9.9.1/faker/providers/company/ru_RU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/company/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/tr_TR/__init__.py` & `Faker-9.9.1/faker/providers/company/tr_TR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/zh_CN/__init__.py` & `Faker-9.9.1/faker/providers/company/zh_CN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/company/zh_TW/__init__.py` & `Faker-9.9.1/faker/providers/company/zh_TW/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/credit_card/__init__.py` & `Faker-9.9.1/faker/providers/credit_card/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/credit_card/fa_IR/__init__.py` & `Faker-9.9.1/faker/providers/credit_card/fa_IR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/credit_card/pt_PT/__init__.py` & `Faker-9.9.1/faker/providers/credit_card/pt_PT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/credit_card/ru_RU/__init__.py` & `Faker-9.9.1/faker/providers/credit_card/ru_RU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/currency/__init__.py` & `Faker-9.9.1/faker/providers/currency/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/currency/el_GR/__init__.py` & `Faker-9.9.1/faker/providers/currency/el_GR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/currency/es_ES/__init__.py` & `Faker-9.9.1/faker/providers/currency/es_ES/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/currency/ru_RU/__init__.py` & `Faker-9.9.1/faker/providers/currency/ru_RU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/currency/sv_SE/__init__.py` & `Faker-9.9.1/faker/providers/currency/sv_SE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/currency/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/currency/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/__init__.py` & `Faker-9.9.1/faker/providers/date_time/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/ar_AA/__init__.py` & `Faker-9.9.1/faker/providers/date_time/ar_AA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/bn_BD/__init__.py` & `Faker-9.9.1/faker/providers/date_time/bn_BD/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/cs_CZ/__init__.py` & `Faker-9.9.1/faker/providers/date_time/cs_CZ/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/de_AT/__init__.py` & `Faker-9.9.1/faker/providers/date_time/de_AT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/de_DE/__init__.py` & `Faker-9.9.1/faker/providers/date_time/de_DE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/el_GR/__init__.py` & `Faker-9.9.1/faker/providers/date_time/el_GR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/es_ES/__init__.py` & `Faker-9.9.1/faker/providers/date_time/es_ES/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/fil_PH/__init__.py` & `Faker-9.9.1/faker/providers/date_time/fil_PH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/fr_FR/__init__.py` & `Faker-9.9.1/faker/providers/date_time/fr_FR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/hi_IN/__init__.py` & `Faker-9.9.1/faker/providers/date_time/hi_IN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/hr_HR/__init__.py` & `Faker-9.9.1/faker/providers/date_time/hr_HR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/hu_HU/__init__.py` & `Faker-9.9.1/faker/providers/date_time/hu_HU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/hy_AM/__init__.py` & `Faker-9.9.1/faker/providers/date_time/hy_AM/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/id_ID/__init__.py` & `Faker-9.9.1/faker/providers/date_time/id_ID/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/it_IT/__init__.py` & `Faker-9.9.1/faker/providers/date_time/it_IT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/ko_KR/__init__.py` & `Faker-9.9.1/faker/providers/date_time/ko_KR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/nl_NL/__init__.py` & `Faker-9.9.1/faker/providers/date_time/nl_NL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/pl_PL/__init__.py` & `Faker-9.9.1/faker/providers/date_time/pl_PL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/pt_BR/__init__.py` & `Faker-9.9.1/faker/providers/date_time/pt_BR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/pt_PT/__init__.py` & `Faker-9.9.1/faker/providers/date_time/pt_PT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/ro_RO/__init__.py` & `Faker-9.9.1/faker/providers/date_time/ro_RO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/ru_RU/__init__.py` & `Faker-9.9.1/faker/providers/date_time/ru_RU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/sk_SK/__init__.py` & `Faker-9.9.1/faker/providers/date_time/sk_SK/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/sl_SI/__init__.py` & `Faker-9.9.1/faker/providers/date_time/sl_SI/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/ta_IN/__init__.py` & `Faker-9.9.1/faker/providers/date_time/ta_IN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/date_time/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/date_time/tr_TR/__init__.py` & `Faker-9.9.1/faker/providers/date_time/tr_TR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/file/__init__.py` & `Faker-9.9.1/faker/providers/file/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/geo/__init__.py` & `Faker-9.9.1/faker/providers/geo/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/geo/el_GR/__init__.py` & `Faker-9.9.1/faker/providers/geo/el_GR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/geo/en_IE/__init__.py` & `Faker-9.9.1/faker/providers/geo/en_IE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/geo/pt_PT/__init__.py` & `Faker-9.9.1/faker/providers/geo/pt_PT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/geo/tr_TR/__init__.py` & `Faker-9.9.1/faker/providers/geo/tr_TR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/__init__.py` & `Faker-9.9.1/faker/providers/internet/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/ar_AA/__init__.py` & `Faker-9.9.1/faker/providers/internet/ar_AA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/bg_BG/__init__.py` & `Faker-9.9.1/faker/providers/internet/bg_BG/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/bs_BA/__init__.py` & `Faker-9.9.1/faker/providers/internet/bs_BA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/cs_CZ/__init__.py` & `Faker-9.9.1/faker/providers/internet/cs_CZ/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/de_DE/__init__.py` & `Faker-9.9.1/faker/providers/internet/de_DE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/el_GR/__init__.py` & `Faker-9.9.1/faker/providers/internet/el_GR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/en_GB/__init__.py` & `Faker-9.9.1/faker/providers/internet/en_GB/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/en_PH/__init__.py` & `Faker-9.9.1/faker/providers/internet/en_PH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/fr_CH/__init__.py` & `Faker-9.9.1/faker/providers/internet/fr_CH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/fr_FR/__init__.py` & `Faker-9.9.1/faker/providers/internet/fr_FR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/hr_HR/__init__.py` & `Faker-9.9.1/faker/providers/internet/hr_HR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/hu_HU/__init__.py` & `Faker-9.9.1/faker/providers/internet/hu_HU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/id_ID/__init__.py` & `Faker-9.9.1/faker/providers/internet/id_ID/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/it_IT/__init__.py` & `Faker-9.9.1/faker/providers/internet/it_IT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/ja_JP/__init__.py` & `Faker-9.9.1/faker/providers/internet/ja_JP/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/pl_PL/__init__.py` & `Faker-9.9.1/faker/providers/internet/pl_PL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/pt_BR/__init__.py` & `Faker-9.9.1/faker/providers/internet/pt_BR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/ro_RO/__init__.py` & `Faker-9.9.1/faker/providers/internet/ro_RO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/ru_RU/__init__.py` & `Faker-9.9.1/faker/providers/internet/ru_RU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/sk_SK/__init__.py` & `Faker-9.9.1/faker/providers/internet/sk_SK/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/sl_SI/__init__.py` & `Faker-9.9.1/faker/providers/internet/sl_SI/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/internet/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/uk_UA/__init__.py` & `Faker-9.9.1/faker/providers/internet/uk_UA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/zh_CN/__init__.py` & `Faker-9.9.1/faker/providers/internet/zh_CN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/internet/zh_TW/__init__.py` & `Faker-9.9.1/faker/providers/internet/zh_TW/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/isbn/__init__.py` & `Faker-9.9.1/faker/providers/isbn/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/isbn/isbn.py` & `Faker-9.9.1/faker/providers/isbn/isbn.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/isbn/rules.py` & `Faker-9.9.1/faker/providers/isbn/rules.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/__init__.py` & `Faker-9.9.1/faker/providers/job/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/ar_AA/__init__.py` & `Faker-9.9.1/faker/providers/job/ar_AA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/bs_BA/__init__.py` & `Faker-9.9.1/faker/providers/job/bs_BA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/de_DE/__init__.py` & `Faker-9.9.1/faker/providers/job/de_DE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/el_GR/__init__.py` & `Faker-9.9.1/faker/providers/job/el_GR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/fa_IR/__init__.py` & `Faker-9.9.1/faker/providers/job/fa_IR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/fi_FI/__init__.py` & `Faker-9.9.1/faker/providers/job/fi_FI/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/fr_CH/__init__.py` & `Faker-9.9.1/faker/providers/job/fr_CH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/fr_FR/__init__.py` & `Faker-9.9.1/faker/providers/job/fr_FR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/hr_HR/__init__.py` & `Faker-9.9.1/faker/providers/job/hr_HR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/hu_HU/__init__.py` & `Faker-9.9.1/faker/providers/job/hu_HU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/hy_AM/__init__.py` & `Faker-9.9.1/faker/providers/job/hy_AM/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/ja_JP/__init__.py` & `Faker-9.9.1/faker/providers/job/ja_JP/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/ko_KR/__init__.py` & `Faker-9.9.1/faker/providers/job/ko_KR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/pl_PL/__init__.py` & `Faker-9.9.1/faker/providers/job/pl_PL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/pt_BR/__init__.py` & `Faker-9.9.1/faker/providers/job/pt_BR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/pt_PT/__init__.py` & `Faker-9.9.1/faker/providers/job/pt_PT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/ro_RO/__init__.py` & `Faker-9.9.1/faker/providers/job/ro_RO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/ru_RU/__init__.py` & `Faker-9.9.1/faker/providers/job/ru_RU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/sk_SK/__init__.py` & `Faker-9.9.1/faker/providers/job/sk_SK/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/job/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/tr_TR/__init__.py` & `Faker-9.9.1/faker/providers/job/tr_TR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/uk_UA/__init__.py` & `Faker-9.9.1/faker/providers/job/uk_UA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/zh_CN/__init__.py` & `Faker-9.9.1/faker/providers/job/zh_CN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/job/zh_TW/__init__.py` & `Faker-9.9.1/faker/providers/job/zh_TW/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/__init__.py` & `Faker-9.9.1/faker/providers/lorem/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/ar_AA/__init__.py` & `Faker-9.9.1/faker/providers/lorem/ar_AA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/cs_CZ/__init__.py` & `Faker-9.9.1/faker/providers/lorem/cs_CZ/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/el_GR/__init__.py` & `Faker-9.9.1/faker/providers/lorem/el_GR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/en_PH/__init__.py` & `Faker-9.9.1/faker/providers/lorem/en_PH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/en_US/__init__.py` & `Faker-9.9.1/faker/providers/lorem/en_US/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/fil_PH/__init__.py` & `Faker-9.9.1/faker/providers/lorem/fil_PH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/fr_FR/__init__.py` & `Faker-9.9.1/faker/providers/lorem/fr_FR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/he_IL/__init__.py` & `Faker-9.9.1/faker/providers/lorem/he_IL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/hy_AM/__init__.py` & `Faker-9.9.1/faker/providers/lorem/hy_AM/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/ja_JP/__init__.py` & `Faker-9.9.1/faker/providers/lorem/ja_JP/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/la/__init__.py` & `Faker-9.9.1/faker/providers/lorem/la/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/pl_PL/__init__.py` & `Faker-9.9.1/faker/providers/lorem/pl_PL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/ru_RU/__init__.py` & `Faker-9.9.1/faker/providers/lorem/ru_RU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/lorem/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/zh_CN/__init__.py` & `Faker-9.9.1/faker/providers/lorem/zh_CN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/lorem/zh_TW/__init__.py` & `Faker-9.9.1/faker/providers/lorem/zh_TW/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/misc/__init__.py` & `Faker-9.9.1/faker/providers/misc/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/misc/en_PH/__init__.py` & `Faker-9.9.1/faker/providers/misc/en_PH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/__init__.py` & `Faker-9.9.1/faker/providers/person/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/ar_AA/__init__.py` & `Faker-9.9.1/faker/providers/person/ar_AA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/ar_PS/__init__.py` & `Faker-9.9.1/faker/providers/person/ar_PS/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/ar_SA/__init__.py` & `Faker-9.9.1/faker/providers/person/ar_SA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/bg_BG/__init__.py` & `Faker-9.9.1/faker/providers/person/bg_BG/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/cs_CZ/__init__.py` & `Faker-9.9.1/faker/providers/person/cs_CZ/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/de_AT/__init__.py` & `Faker-9.9.1/faker/providers/person/de_AT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/de_CH/__init__.py` & `Faker-9.9.1/faker/providers/person/de_CH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/de_DE/__init__.py` & `Faker-9.9.1/faker/providers/person/de_DE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/dk_DK/__init__.py` & `Faker-9.9.1/faker/providers/person/dk_DK/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/el_GR/__init__.py` & `Faker-9.9.1/faker/providers/person/el_GR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/en/__init__.py` & `Faker-9.9.1/faker/providers/person/en/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/en_GB/__init__.py` & `Faker-9.9.1/faker/providers/person/en_GB/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/en_IE/__init__.py` & `Faker-9.9.1/faker/providers/person/en_IE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/en_IN/__init__.py` & `Faker-9.9.1/faker/providers/person/en_IN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/en_NZ/__init__.py` & `Faker-9.9.1/faker/providers/person/en_NZ/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/en_TH/__init__.py` & `Faker-9.9.1/faker/providers/person/en_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/en_US/__init__.py` & `Faker-9.9.1/faker/providers/person/en_US/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/es/__init__.py` & `Faker-9.9.1/faker/providers/person/es/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/es_CA/__init__.py` & `Faker-9.9.1/faker/providers/person/es_CA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/es_CO/__init__.py` & `Faker-9.9.1/faker/providers/person/es_CO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/es_ES/__init__.py` & `Faker-9.9.1/faker/providers/person/es_ES/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/es_MX/__init__.py` & `Faker-9.9.1/faker/providers/person/es_MX/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/et_EE/__init__.py` & `Faker-9.9.1/faker/providers/person/et_EE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/fa_IR/__init__.py` & `Faker-9.9.1/faker/providers/person/fa_IR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/fi_FI/__init__.py` & `Faker-9.9.1/faker/providers/person/fi_FI/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/fr_CA/__init__.py` & `Faker-9.9.1/faker/providers/person/fr_CA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/fr_CH/__init__.py` & `Faker-9.9.1/faker/providers/person/fr_CH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/fr_FR/__init__.py` & `Faker-9.9.1/faker/providers/person/fr_FR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/ga_IE/__init__.py` & `Faker-9.9.1/faker/providers/person/ga_IE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/he_IL/__init__.py` & `Faker-9.9.1/faker/providers/person/he_IL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/hi_IN/__init__.py` & `Faker-9.9.1/faker/providers/person/hi_IN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/hr_HR/__init__.py` & `Faker-9.9.1/faker/providers/person/hr_HR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/hu_HU/__init__.py` & `Faker-9.9.1/faker/providers/person/hu_HU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/hy_AM/__init__.py` & `Faker-9.9.1/faker/providers/person/hy_AM/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/id_ID/__init__.py` & `Faker-9.9.1/faker/providers/person/id_ID/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/it_IT/__init__.py` & `Faker-9.9.1/faker/providers/person/it_IT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/ja_JP/__init__.py` & `Faker-9.9.1/faker/providers/person/ja_JP/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/ka_GE/__init__.py` & `Faker-9.9.1/faker/providers/person/ka_GE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/ko_KR/__init__.py` & `Faker-9.9.1/faker/providers/person/ko_KR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/lt_LT/__init__.py` & `Faker-9.9.1/faker/providers/person/lt_LT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/lv_LV/__init__.py` & `Faker-9.9.1/faker/providers/person/lv_LV/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/ne_NP/__init__.py` & `Faker-9.9.1/faker/providers/person/ne_NP/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/nl_NL/__init__.py` & `Faker-9.9.1/faker/providers/person/nl_NL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/no_NO/__init__.py` & `Faker-9.9.1/faker/providers/person/no_NO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/or_IN/__init__.py` & `Faker-9.9.1/faker/providers/person/or_IN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/pl_PL/__init__.py` & `Faker-9.9.1/faker/providers/person/pl_PL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/pt_BR/__init__.py` & `Faker-9.9.1/faker/providers/person/pt_BR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/pt_PT/__init__.py` & `Faker-9.9.1/faker/providers/person/pt_PT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/ro_RO/__init__.py` & `Faker-9.9.1/faker/providers/person/ro_RO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/ru_RU/__init__.py` & `Faker-9.9.1/faker/providers/person/ru_RU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/sl_SI/__init__.py` & `Faker-9.9.1/faker/providers/person/sl_SI/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/sv_SE/__init__.py` & `Faker-9.9.1/faker/providers/person/sv_SE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/ta_IN/__init__.py` & `Faker-9.9.1/faker/providers/person/ta_IN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/person/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/tr_TR/__init__.py` & `Faker-9.9.1/faker/providers/person/tr_TR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/tw_GH/__init__.py` & `Faker-9.9.1/faker/providers/person/tw_GH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/uk_UA/__init__.py` & `Faker-9.9.1/faker/providers/person/uk_UA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/zh_CN/__init__.py` & `Faker-9.9.1/faker/providers/person/zh_CN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/person/zh_TW/__init__.py` & `Faker-9.9.1/faker/providers/person/zh_TW/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/ar_AE/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/ar_AE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/ar_JO/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/ar_JO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/ar_PS/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/ar_PS/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/bs_BA/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/bs_BA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/cs_CZ/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/cs_CZ/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/el_GR/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/el_GR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/en_AU/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/en_AU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/en_GB/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/en_GB/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/en_NZ/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/en_NZ/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/en_PH/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/en_PH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/en_US/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/en_US/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/es_CO/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/es_CO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/es_ES/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/es_ES/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/es_MX/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/es_MX/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/fa_IR/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/fa_IR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/fr_CH/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/fr_CH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/fr_FR/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/fr_FR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/hr_HR/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/hr_HR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/id_ID/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/id_ID/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/ko_KR/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/ko_KR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/nl_BE/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/nl_BE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/nl_NL/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/nl_NL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/pl_PL/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/pl_PL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/pt_BR/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/pt_BR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/pt_PT/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/pt_PT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/ro_RO/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/ro_RO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/tw_GH/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/tw_GH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/phone_number/zh_CN/__init__.py` & `Faker-9.9.1/faker/providers/phone_number/zh_CN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/profile/__init__.py` & `Faker-9.9.1/faker/providers/profile/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/python/__init__.py` & `Faker-9.9.1/faker/providers/python/__init__.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,19 +1,18 @@
 import math
 import string
 import sys
 import warnings
 
 from decimal import Decimal
-from typing import Any, Dict, Iterable, Iterator, List, Optional, Set, Tuple, Type, Union, no_type_check
+from typing import Any, Dict, Iterable, Iterator, List, Optional, Set, Tuple, Union, no_type_check
 
 from .. import BaseProvider, ElementsType
 
-TypesNames = List[str]
-TypesSpec = Union[List[Type], Tuple[Type, ...]]
+ValueTypes = Optional[Union[List[str], Tuple[str, ...]]]
 
 
 class Provider(BaseProvider):
     default_value_types: ElementsType = (
         "str",
         "str",
         "str",
@@ -23,34 +22,25 @@
         "int",
         "decimal",
         "date_time",
         "uri",
         "email",
     )
 
-    def _check_signature(self, value_types: Optional[TypesSpec], allowed_types: Optional[TypesSpec]) -> TypesSpec:
+    def _check_signature(self, value_types: ValueTypes, allowed_types: Tuple[str]) -> Tuple[str, ...]:
         if value_types is not None and not isinstance(value_types, (list, tuple)):
-            value_types = (value_types,)
+            value_types = [value_types]
             warnings.warn(
                 "Passing `value_types` as positional arguments is going to be "
                 "deprecated.  Pass them as a list or tuple instead.",
                 PendingDeprecationWarning,
             )
-        if allowed_types is not None and not isinstance(allowed_types, (list, tuple)):
-            allowed_types = (allowed_types,)
-            warnings.warn(
-                "Passing `allowed_types` as positional arguments is going to be "
-                "deprecated.  Pass them as a list or tuple instead.",
-                PendingDeprecationWarning,
-            )
         if value_types is None:
             value_types = ()
-        if allowed_types is None:
-            allowed_types = ()
-        return tuple(value_types) + tuple(allowed_types)
+        return tuple(value_types) + allowed_types
 
     def pybool(self) -> bool:
         return self.random_int(0, 1) == 1
 
     def pystr(self, min_chars: Optional[int] = None, max_chars: int = 20) -> str:
         """
         Generates a random string of upper and lowercase letters.
@@ -250,48 +240,48 @@
 
         return result
 
     def pytuple(
         self,
         nb_elements: int = 10,
         variable_nb_elements: bool = True,
-        value_types: Optional[TypesSpec] = None,
-        allowed_types: Optional[TypesSpec] = None,
+        value_types: ValueTypes = None,
+        *allowed_types: str,
     ) -> Tuple[Any, ...]:
         return tuple(
             self._pyiterable(
                 nb_elements=nb_elements,
                 variable_nb_elements=variable_nb_elements,
                 value_types=value_types,
                 allowed_types=allowed_types,
             )
         )
 
     def pyset(
         self,
         nb_elements: int = 10,
         variable_nb_elements: bool = True,
-        value_types: Optional[TypesSpec] = None,
-        allowed_types: Optional[TypesSpec] = None,
+        value_types: ValueTypes = None,
+        *allowed_types: str,
     ) -> Set[Any]:
         return set(
             self._pyiterable(
                 nb_elements=nb_elements,
                 variable_nb_elements=variable_nb_elements,
                 value_types=value_types,
                 allowed_types=allowed_types,
             )
         )
 
     def pylist(
         self,
         nb_elements: int = 10,
         variable_nb_elements: bool = True,
-        value_types: Optional[TypesSpec] = None,
-        allowed_types: Optional[TypesSpec] = None,
+        value_types: ValueTypes = None,
+        *allowed_types: str,
     ) -> List[Any]:
         return list(
             self._pyiterable(
                 nb_elements=nb_elements,
                 variable_nb_elements=variable_nb_elements,
                 value_types=value_types,
                 allowed_types=allowed_types,
@@ -299,23 +289,23 @@
         )
 
     @no_type_check
     def pyiterable(
         self,
         nb_elements: int = 10,
         variable_nb_elements: bool = True,
-        value_types: Optional[TypesSpec] = None,
-        allowed_types: Optional[TypesSpec] = None,
+        value_types: ValueTypes = None,
+        *allowed_types: str,
     ) -> Iterable[Any]:
-        value_types: TypesSpec = self._check_signature(value_types, allowed_types)
+        value_types = self._check_signature(value_types, allowed_types)
         return self.random_element([self.pylist, self.pytuple, self.pyset])(
             nb_elements=nb_elements,
             variable_nb_elements=variable_nb_elements,
             value_types=value_types,
-            allowed_types=allowed_types,
+            *allowed_types,
         )
 
     def _random_type(self, type_list: List[str]) -> str:
         value_type: str = self.random_element(type_list)
 
         method_name = f"py{value_type}"
         if hasattr(self, method_name):
@@ -323,21 +313,23 @@
 
         return self.generator.format(value_type)
 
     def _pyiterable(
         self,
         nb_elements: int = 10,
         variable_nb_elements: bool = True,
-        value_types: Optional[TypesSpec] = None,
-        allowed_types: Optional[TypesSpec] = None,
+        value_types: ValueTypes = None,
+        allowed_types: ValueTypes = None,
     ) -> Iterator:
+        if allowed_types is None:
+            allowed_types = ()
 
-        value_types: TypesSpec = self._check_signature(value_types, allowed_types)
+        value_types = self._check_signature(value_types, allowed_types)  # type: ignore
 
-        value_types: TypesNames = [
+        value_types = [
             t if isinstance(t, str) else getattr(t, "__name__", type(t).__name__).lower()
             for t in value_types
             # avoid recursion
             if t not in ["iterable", "list", "tuple", "dict", "set"]
         ]
         if not value_types:
             value_types = self.default_value_types  # type: ignore
@@ -348,16 +340,16 @@
         for _ in range(nb_elements):
             yield self._random_type(value_types)
 
     def pydict(
         self,
         nb_elements: int = 10,
         variable_nb_elements: bool = True,
-        value_types: Optional[TypesSpec] = None,
-        allowed_types: Optional[TypesSpec] = None,
+        value_types: ValueTypes = None,
+        *allowed_types: str,
     ) -> Dict[Any, Any]:
         """
         Returns a dictionary.
 
         :nb_elements: number of elements for dictionary
         :variable_nb_elements: is use variable number of elements for dictionary
         :value_types: type of dictionary values
@@ -373,20 +365,18 @@
                     variable_nb_elements=False,
                     value_types=value_types,
                     allowed_types=allowed_types,
                 ),
             )
         )
 
-    def pystruct(
-        self, count: int = 10, value_types: Optional[TypesSpec] = None, allowed_types: Optional[TypesSpec] = None
-    ) -> Tuple[List, Dict, Dict]:
-        value_types: TypesSpec = self._check_signature(value_types, allowed_types)
+    def pystruct(self, count: int = 10, value_types: ValueTypes = None, *allowed_types: str) -> Tuple[List, Dict, Dict]:
+        value_types = self._check_signature(value_types, allowed_types)  # type: ignore
 
-        value_types: TypesNames = [
+        value_types = [
             t if isinstance(t, str) else getattr(t, "__name__", type(t).__name__).lower()
             for t in value_types
             # avoid recursion
             if t != "struct"
         ]
         if not value_types:
             value_types = self.default_value_types  # type: ignore
```

### Comparing `Faker-9.9.0/faker/providers/ssn/cs_CZ/__init__.py` & `Faker-9.9.1/faker/providers/ssn/cs_CZ/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/el_GR/__init__.py` & `Faker-9.9.1/faker/providers/ssn/el_GR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/en_CA/__init__.py` & `Faker-9.9.1/faker/providers/ssn/en_CA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/en_GB/__init__.py` & `Faker-9.9.1/faker/providers/ssn/en_GB/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/en_IN/__init__.py` & `Faker-9.9.1/faker/providers/ssn/en_IN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/en_PH/__init__.py` & `Faker-9.9.1/faker/providers/ssn/en_PH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/en_US/__init__.py` & `Faker-9.9.1/faker/providers/ssn/en_US/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/es_CO/__init__.py` & `Faker-9.9.1/faker/providers/ssn/es_CO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/es_ES/__init__.py` & `Faker-9.9.1/faker/providers/ssn/es_ES/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/es_MX/__init__.py` & `Faker-9.9.1/faker/providers/ssn/es_MX/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/et_EE/__init__.py` & `Faker-9.9.1/faker/providers/ssn/et_EE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/fi_FI/__init__.py` & `Faker-9.9.1/faker/providers/ssn/fi_FI/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/fr_CH/__init__.py` & `Faker-9.9.1/faker/providers/ssn/fr_CH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/fr_FR/__init__.py` & `Faker-9.9.1/faker/providers/ssn/fr_FR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/he_IL/__init__.py` & `Faker-9.9.1/faker/providers/ssn/he_IL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/hr_HR/__init__.py` & `Faker-9.9.1/faker/providers/ssn/hr_HR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/hu_HU/__init__.py` & `Faker-9.9.1/faker/providers/ssn/hu_HU/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/it_IT/__init__.py` & `Faker-9.9.1/faker/providers/ssn/it_IT/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/nl_BE/__init__.py` & `Faker-9.9.1/faker/providers/ssn/nl_BE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/nl_NL/__init__.py` & `Faker-9.9.1/faker/providers/ssn/nl_NL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/no_NO/__init__.py` & `Faker-9.9.1/faker/providers/ssn/no_NO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/pl_PL/__init__.py` & `Faker-9.9.1/faker/providers/ssn/pl_PL/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/pt_BR/__init__.py` & `Faker-9.9.1/faker/providers/ssn/pt_BR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/ro_RO/__init__.py` & `Faker-9.9.1/faker/providers/ssn/ro_RO/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/sk_SK/__init__.py` & `Faker-9.9.1/faker/providers/ssn/sk_SK/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/sv_SE/__init__.py` & `Faker-9.9.1/faker/providers/ssn/sv_SE/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/th_TH/__init__.py` & `Faker-9.9.1/faker/providers/ssn/th_TH/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/tr_TR/__init__.py` & `Faker-9.9.1/faker/providers/ssn/tr_TR/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/uk_UA/__init__.py` & `Faker-9.9.1/faker/providers/ssn/uk_UA/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/ssn/zh_CN/__init__.py` & `Faker-9.9.1/faker/providers/ssn/zh_CN/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/providers/user_agent/__init__.py` & `Faker-9.9.1/faker/providers/user_agent/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/proxy.py` & `Faker-9.9.1/faker/proxy.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/utils/checksums.py` & `Faker-9.9.1/faker/utils/checksums.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/utils/datasets.py` & `Faker-9.9.1/faker/utils/datasets.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/utils/decorators.py` & `Faker-9.9.1/faker/utils/decorators.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/utils/distribution.py` & `Faker-9.9.1/faker/utils/distribution.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/utils/loading.py` & `Faker-9.9.1/faker/utils/loading.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/faker/utils/text.py` & `Faker-9.9.1/faker/utils/text.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/setup.py` & `Faker-9.9.1/setup.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/__init__.py` & `Faker-9.9.1/tests/providers/__init__.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/conftest.py` & `Faker-9.9.1/tests/providers/conftest.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_address.py` & `Faker-9.9.1/tests/providers/test_address.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_automotive.py` & `Faker-9.9.1/tests/providers/test_automotive.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_bank.py` & `Faker-9.9.1/tests/providers/test_bank.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_barcode.py` & `Faker-9.9.1/tests/providers/test_barcode.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_color.py` & `Faker-9.9.1/tests/providers/test_color.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_company.py` & `Faker-9.9.1/tests/providers/test_company.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_credit_card.py` & `Faker-9.9.1/tests/providers/test_credit_card.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_currency.py` & `Faker-9.9.1/tests/providers/test_currency.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_date_time.py` & `Faker-9.9.1/tests/providers/test_date_time.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_dynamic.py` & `Faker-9.9.1/tests/providers/test_dynamic.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_file.py` & `Faker-9.9.1/tests/providers/test_file.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_geo.py` & `Faker-9.9.1/tests/providers/test_geo.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_internet.py` & `Faker-9.9.1/tests/providers/test_internet.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_isbn.py` & `Faker-9.9.1/tests/providers/test_isbn.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_job.py` & `Faker-9.9.1/tests/providers/test_job.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_lorem.py` & `Faker-9.9.1/tests/providers/test_lorem.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_misc.py` & `Faker-9.9.1/tests/providers/test_misc.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_person.py` & `Faker-9.9.1/tests/providers/test_person.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_phone_number.py` & `Faker-9.9.1/tests/providers/test_phone_number.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_profile.py` & `Faker-9.9.1/tests/providers/test_profile.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_python.py` & `Faker-9.9.1/tests/providers/test_python.py`

 * *Files 0% similar despite different names*

```diff
@@ -472,11 +472,11 @@
             assert len(w) == 1
         assert some_list
         for item in some_list:
             assert isinstance(item, int)
 
         with warnings.catch_warnings(record=True) as w:
             some_list = self.factory.pylist(10, True, int, float)
-            assert len(w) == 2
+            assert len(w) == 1
         assert some_list
         for item in some_list:
             assert isinstance(item, (int, float))
```

### Comparing `Faker-9.9.0/tests/providers/test_ssn.py` & `Faker-9.9.1/tests/providers/test_ssn.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/providers/test_user_agent.py` & `Faker-9.9.1/tests/providers/test_user_agent.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/pytest/session_overrides/conftest.py` & `Faker-9.9.1/tests/pytest/session_overrides/conftest.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/pytest/session_overrides/session_locale/test_autouse_faker_locale.py` & `Faker-9.9.1/tests/pytest/session_overrides/session_locale/test_autouse_faker_locale.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/pytest/session_overrides/session_locale/test_autouse_faker_seed.py` & `Faker-9.9.1/tests/pytest/session_overrides/session_locale/test_autouse_faker_seed.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/pytest/session_overrides/session_locale/test_manual_injection.py` & `Faker-9.9.1/tests/pytest/session_overrides/session_locale/test_manual_injection.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/pytest/test_autouse_faker_locale.py` & `Faker-9.9.1/tests/pytest/test_autouse_faker_locale.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/pytest/test_autouse_faker_seed.py` & `Faker-9.9.1/tests/pytest/test_autouse_faker_seed.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/pytest/test_manual_injection.py` & `Faker-9.9.1/tests/pytest/test_manual_injection.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/pytest/test_unique_clear.py` & `Faker-9.9.1/tests/pytest/test_unique_clear.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/test_factory.py` & `Faker-9.9.1/tests/test_factory.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/test_generator.py` & `Faker-9.9.1/tests/test_generator.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/test_providers_formats.py` & `Faker-9.9.1/tests/test_providers_formats.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/test_proxy.py` & `Faker-9.9.1/tests/test_proxy.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/test_unique.py` & `Faker-9.9.1/tests/test_unique.py`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/utils/random_state.json` & `Faker-9.9.1/tests/utils/random_state.json`

 * *Files identical despite different names*

### Comparing `Faker-9.9.0/tests/utils/test_utils.py` & `Faker-9.9.1/tests/utils/test_utils.py`

 * *Files identical despite different names*

