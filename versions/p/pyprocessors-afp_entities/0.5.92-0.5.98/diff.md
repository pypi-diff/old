# Comparing `tmp/pyprocessors-afp_entities-0.5.92.tar.gz` & `tmp/pyprocessors-afp_entities-0.5.98.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyprocessors-afp_entities-0.5.92.tar", last modified: Tue Feb 14 17:59:10 2023, max compression
+gzip compressed data, was "pyprocessors-afp_entities-0.5.98.tar", last modified: Tue Mar 14 08:19:28 2023, max compression
```

## Comparing `pyprocessors-afp_entities-0.5.92.tar` & `pyprocessors-afp_entities-0.5.98.tar`

### file list

```diff
@@ -1,123 +1,124 @@
--rw-r--r--   0        0        0     1731 2022-10-04 08:09:06.778694 pyprocessors-afp_entities-0.5.92/.gitignore
--rw-r--r--   0        0        0      121 2023-01-20 15:32:17.311095 pyprocessors-afp_entities-0.5.92/AUTHORS.md
--rw-r--r--   0        0        0      268 2022-10-04 08:09:06.779694 pyprocessors-afp_entities-0.5.92/CHANGELOG.md
--rw-r--r--   0        0        0      476 2022-10-04 08:09:06.779694 pyprocessors-afp_entities-0.5.92/Dockerfile
--rw-r--r--   0        0        0    10227 2023-01-20 15:32:17.311095 pyprocessors-afp_entities-0.5.92/Jenkinsfile
--rw-r--r--   0        0        0     1082 2022-10-04 08:09:06.779694 pyprocessors-afp_entities-0.5.92/LICENSE
--rw-r--r--   0        0        0     1627 2023-01-20 15:32:17.312095 pyprocessors-afp_entities-0.5.92/README.md
--rw-r--r--   0        0        0      949 2023-01-20 15:32:17.312095 pyprocessors-afp_entities-0.5.92/RELEASE.md
--rw-r--r--   0        0        0     1559 2022-10-04 08:09:06.781694 pyprocessors-afp_entities-0.5.92/bumpversion.py
--rw-r--r--   0        0        0       62 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.92/docs/.gitignore
--rw-r--r--   0        0        0      268 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.92/docs/CHANGELOG.md
--rw-r--r--   0        0        0     1082 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.92/docs/LICENSE
--rw-r--r--   0        0        0      230 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.92/docs/_build/.buildinfo
--rw-r--r--   0        0        0     4060 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.92/docs/_build/.doctrees/CHANGELOG.doctree
--rw-r--r--   0        0        0    28885 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.92/docs/_build/.doctrees/environment.pickle
--rw-r--r--   0        0        0    10541 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.92/docs/_build/.doctrees/index.doctree
--rw-r--r--   0        0        0     6249 2023-01-20 15:32:17.312095 pyprocessors-afp_entities-0.5.92/docs/_build/CHANGELOG.html
--rw-r--r--   0        0        0     1082 2022-10-04 08:09:06.783694 pyprocessors-afp_entities-0.5.92/docs/_build/LICENSE
--rw-r--r--   0        0        0     4920 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.92/docs/_build/_modules/index.html
--rw-r--r--   0        0        0    24197 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.92/docs/_build/_modules/pyformatters_consolidate/consolidate.html
--rw-r--r--   0        0        0      268 2022-10-04 08:09:06.784695 pyprocessors-afp_entities-0.5.92/docs/_build/_sources/CHANGELOG.md.txt
--rw-r--r--   0        0        0      146 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.92/docs/_build/_sources/index.rst.txt
--rw-r--r--   0        0        0    14652 2022-10-04 08:09:06.785694 pyprocessors-afp_entities-0.5.92/docs/_build/_static/basic.css
--rw-r--r--   0        0        0     3275 2022-10-04 08:09:06.786694 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/badge_only.css
--rw-r--r--   0        0        0    87624 2022-10-04 08:09:06.787695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/Roboto-Slab-Bold.woff
--rw-r--r--   0        0        0    67312 2022-10-04 08:09:06.788694 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/Roboto-Slab-Bold.woff2
--rw-r--r--   0        0        0    86288 2022-10-04 08:09:06.791694 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/Roboto-Slab-Regular.woff
--rw-r--r--   0        0        0    66444 2022-10-04 08:09:06.791694 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/Roboto-Slab-Regular.woff2
--rw-r--r--   0        0        0   165742 2022-10-04 08:09:06.793695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/fontawesome-webfont.eot
--rw-r--r--   0        0        0   444379 2022-10-04 08:09:06.796695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/fontawesome-webfont.svg
--rw-r--r--   0        0        0   165548 2022-10-04 08:09:06.797695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/fontawesome-webfont.ttf
--rw-r--r--   0        0        0    98024 2022-10-04 08:09:06.798695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/fontawesome-webfont.woff
--rw-r--r--   0        0        0    77160 2022-10-04 08:09:06.800695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/fontawesome-webfont.woff2
--rw-r--r--   0        0        0   323344 2022-10-04 08:09:06.805695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-bold-italic.woff
--rw-r--r--   0        0        0   193308 2022-10-04 08:09:06.808695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-bold-italic.woff2
--rw-r--r--   0        0        0   309728 2022-10-04 08:09:06.811695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-bold.woff
--rw-r--r--   0        0        0   184912 2022-10-04 08:09:06.813695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-bold.woff2
--rw-r--r--   0        0        0   328412 2022-10-04 08:09:06.817695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-normal-italic.woff
--rw-r--r--   0        0        0   195704 2022-10-04 08:09:06.818695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-normal-italic.woff2
--rw-r--r--   0        0        0   309192 2022-10-04 08:09:06.824695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-normal.woff
--rw-r--r--   0        0        0   182708 2022-10-04 08:09:06.825695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-normal.woff2
--rw-r--r--   0        0        0   123687 2022-10-04 08:09:06.825695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/theme.css
--rw-r--r--   0        0        0     9592 2022-10-04 08:09:06.825695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/doctools.js
--rw-r--r--   0        0        0      360 2022-10-04 08:09:06.826696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/documentation_options.js
--rw-r--r--   0        0        0      286 2022-10-04 08:09:06.826696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/file.png
--rw-r--r--   0        0        0   109948 2022-10-04 08:09:06.826696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Inconsolata-Bold.ttf
--rw-r--r--   0        0        0    96964 2022-10-04 08:09:06.827695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Inconsolata-Regular.ttf
--rw-r--r--   0        0        0    63184 2022-10-04 08:09:06.827695 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Inconsolata.ttf
--rw-r--r--   0        0        0   656544 2022-10-04 08:09:06.836696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato-Bold.ttf
--rw-r--r--   0        0        0   656568 2022-10-04 08:09:06.844696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato-Regular.ttf
--rw-r--r--   0        0        0   256056 2022-10-04 08:09:06.846696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bold.eot
--rw-r--r--   0        0        0   600856 2022-10-04 08:09:06.847696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bold.ttf
--rw-r--r--   0        0        0   309728 2022-10-04 08:09:06.848696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bold.woff
--rw-r--r--   0        0        0   184912 2022-10-04 08:09:06.848696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bold.woff2
--rw-r--r--   0        0        0   266158 2022-10-04 08:09:06.850696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bolditalic.eot
--rw-r--r--   0        0        0   622572 2022-10-04 08:09:06.856696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bolditalic.ttf
--rw-r--r--   0        0        0   323344 2022-10-04 08:09:06.857696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bolditalic.woff
--rw-r--r--   0        0        0   193308 2022-10-04 08:09:06.857696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bolditalic.woff2
--rw-r--r--   0        0        0   268604 2022-10-04 08:09:06.861696 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-italic.eot
--rw-r--r--   0        0        0   639388 2022-10-04 08:09:06.868697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-italic.ttf
--rw-r--r--   0        0        0   328412 2022-10-04 08:09:06.869697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-italic.woff
--rw-r--r--   0        0        0   195704 2022-10-04 08:09:06.869697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-italic.woff2
--rw-r--r--   0        0        0   253461 2022-10-04 08:09:06.870697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-regular.eot
--rw-r--r--   0        0        0   607720 2022-10-04 08:09:06.870697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-regular.ttf
--rw-r--r--   0        0        0   309192 2022-10-04 08:09:06.872697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-regular.woff
--rw-r--r--   0        0        0   182708 2022-10-04 08:09:06.872697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-regular.woff2
--rw-r--r--   0        0        0   170616 2022-10-04 08:09:06.874697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab-Bold.ttf
--rw-r--r--   0        0        0   169064 2022-10-04 08:09:06.875697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab-Regular.ttf
--rw-r--r--   0        0        0    79520 2022-10-04 08:09:06.878697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.eot
--rw-r--r--   0        0        0   170616 2022-10-04 08:09:06.879697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.ttf
--rw-r--r--   0        0        0    87624 2022-10-04 08:09:06.879697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.woff
--rw-r--r--   0        0        0    67312 2022-10-04 08:09:06.880697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.woff2
--rw-r--r--   0        0        0    78331 2022-10-04 08:09:06.880697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.eot
--rw-r--r--   0        0        0   169064 2022-10-04 08:09:06.882697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.ttf
--rw-r--r--   0        0        0    86288 2022-10-04 08:09:06.883697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.woff
--rw-r--r--   0        0        0    66444 2022-10-04 08:09:06.884697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.woff2
--rw-r--r--   0        0        0   165742 2022-10-04 08:09:06.885697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/fontawesome-webfont.eot
--rw-r--r--   0        0        0   444379 2022-10-04 08:09:06.888697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/fontawesome-webfont.svg
--rw-r--r--   0        0        0   165548 2022-10-04 08:09:06.889697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/fontawesome-webfont.ttf
--rw-r--r--   0        0        0    98024 2022-10-04 08:09:06.889697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/fontawesome-webfont.woff
--rw-r--r--   0        0        0    77160 2022-10-04 08:09:06.889697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/fontawesome-webfont.woff2
--rw-r--r--   0        0        0   287630 2022-10-04 08:09:06.890697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/jquery-3.5.1.js
--rw-r--r--   0        0        0    89476 2022-10-04 08:09:06.891697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/jquery.js
--rw-r--r--   0        0        0      934 2022-10-04 08:09:06.891697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/js/badge_only.js
--rw-r--r--   0        0        0     4370 2022-10-04 08:09:06.891697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/js/html5shiv-printshiv.min.js
--rw-r--r--   0        0        0     2734 2022-10-04 08:09:06.891697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/js/html5shiv.min.js
--rw-r--r--   0        0        0    15414 2022-10-04 08:09:06.891697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/js/modernizr.min.js
--rw-r--r--   0        0        0     4916 2022-10-04 08:09:06.891697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/js/theme.js
--rw-r--r--   0        0        0     3019 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/jupyter-sphinx.css
--rw-r--r--   0        0        0    10854 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/language_data.js
--rw-r--r--   0        0        0       90 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/minus.png
--rw-r--r--   0        0        0       90 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/plus.png
--rw-r--r--   0        0        0     4819 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/pygments.css
--rw-r--r--   0        0        0    16578 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/searchtools.js
--rw-r--r--   0        0        0    68420 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/underscore-1.13.1.js
--rw-r--r--   0        0        0    19530 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.92/docs/_build/_static/underscore.js
--rw-r--r--   0        0        0    10035 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.92/docs/_build/genindex.html
--rw-r--r--   0        0        0     9415 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.92/docs/_build/index.html
--rw-r--r--   0        0        0      671 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.92/docs/_build/objects.inv
--rw-r--r--   0        0        0     5634 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.92/docs/_build/py-modindex.html
--rw-r--r--   0        0        0     5201 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.92/docs/_build/search.html
--rw-r--r--   0        0        0     2790 2023-01-20 15:32:17.314095 pyprocessors-afp_entities-0.5.92/docs/_build/searchindex.js
--rw-r--r--   0        0        0        0 2022-10-04 08:09:06.893697 pyprocessors-afp_entities-0.5.92/docs/_static/.gitkeep
--rw-r--r--   0        0        0        0 2022-10-04 08:09:06.893697 pyprocessors-afp_entities-0.5.92/docs/_templates/.gitkeep
--rw-r--r--   0        0        0     2899 2023-01-20 15:32:17.314095 pyprocessors-afp_entities-0.5.92/docs/conf.py
--rw-r--r--   0        0        0      146 2023-01-20 15:32:17.314095 pyprocessors-afp_entities-0.5.92/docs/index.rst
--rw-r--r--   0        0        0       98 2022-10-04 08:09:06.893697 pyprocessors-afp_entities-0.5.92/mypy.ini
--rw-r--r--   0        0        0     2272 2023-01-20 15:32:17.314095 pyprocessors-afp_entities-0.5.92/pyproject.toml
--rw-r--r--   0        0        0     5461 2023-02-14 17:54:38.171307 pyprocessors-afp_entities-0.5.92/results.xml
--rw-r--r--   0        0        0       60 2023-02-14 17:59:08.916272 pyprocessors-afp_entities-0.5.92/src/pyprocessors_afp_entities/__init__.py
--rw-r--r--   0        0        0    12307 2023-02-14 17:54:38.172307 pyprocessors-afp_entities-0.5.92/src/pyprocessors_afp_entities/afp_entities.py
--rw-r--r--   0        0        0   266240 2022-10-04 08:09:06.901697 pyprocessors-afp_entities-0.5.92/tests/.coverage
--rw-r--r--   0        0        0        0 2022-10-04 08:09:06.902697 pyprocessors-afp_entities-0.5.92/tests/__init__.py
--rw-r--r--   0        0        0    33656 2023-01-20 15:32:17.316095 pyprocessors-afp_entities-0.5.92/tests/data/afp_ner_en-document-test.json
--rw-r--r--   0        0        0     6824 2023-02-09 16:59:22.431761 pyprocessors-afp_entities-0.5.92/tests/data/afp_ner_es-document-test.json
--rw-r--r--   0        0        0    32270 2023-01-20 15:32:17.316095 pyprocessors-afp_entities-0.5.92/tests/data/afp_ner_fr-document-test-whitelist.json
--rw-r--r--   0        0        0    38988 2023-01-12 16:35:46.402331 pyprocessors-afp_entities-0.5.92/tests/data/afp_ner_fr-document-test-whitelist2.json
--rw-r--r--   0        0        0    53390 2023-01-20 15:32:17.316095 pyprocessors-afp_entities-0.5.92/tests/data/afp_ner_fr-document-test.json
--rw-r--r--   0        0        0   104534 2023-01-20 15:32:17.318095 pyprocessors-afp_entities-0.5.92/tests/data/afp_ner_fr-document-test1.json
--rw-r--r--   0        0        0     5389 2023-02-09 17:19:46.841235 pyprocessors-afp_entities-0.5.92/tests/test_afp_entities.py
--rw-r--r--   0        0        0      867 2023-01-20 15:32:17.318095 pyprocessors-afp_entities-0.5.92/tox.ini
--rw-r--r--   0        0        0     1384 1970-01-01 00:00:00.000000 pyprocessors-afp_entities-0.5.92/setup.py
--rw-r--r--   0        0        0     3432 1970-01-01 00:00:00.000000 pyprocessors-afp_entities-0.5.92/PKG-INFO
+-rw-r--r--   0        0        0     1731 2022-10-04 08:09:06.778694 pyprocessors-afp_entities-0.5.98/.gitignore
+-rw-r--r--   0        0        0      121 2023-01-20 15:32:17.311095 pyprocessors-afp_entities-0.5.98/AUTHORS.md
+-rw-r--r--   0        0        0      268 2022-10-04 08:09:06.779694 pyprocessors-afp_entities-0.5.98/CHANGELOG.md
+-rw-r--r--   0        0        0      476 2022-10-04 08:09:06.779694 pyprocessors-afp_entities-0.5.98/Dockerfile
+-rw-r--r--   0        0        0    10227 2023-01-20 15:32:17.311095 pyprocessors-afp_entities-0.5.98/Jenkinsfile
+-rw-r--r--   0        0        0     1082 2022-10-04 08:09:06.779694 pyprocessors-afp_entities-0.5.98/LICENSE
+-rw-r--r--   0        0        0     1627 2023-01-20 15:32:17.312095 pyprocessors-afp_entities-0.5.98/README.md
+-rw-r--r--   0        0        0      949 2023-01-20 15:32:17.312095 pyprocessors-afp_entities-0.5.98/RELEASE.md
+-rw-r--r--   0        0        0     1559 2022-10-04 08:09:06.781694 pyprocessors-afp_entities-0.5.98/bumpversion.py
+-rw-r--r--   0        0        0       62 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.98/docs/.gitignore
+-rw-r--r--   0        0        0      268 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.98/docs/CHANGELOG.md
+-rw-r--r--   0        0        0     1082 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.98/docs/LICENSE
+-rw-r--r--   0        0        0      230 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.98/docs/_build/.buildinfo
+-rw-r--r--   0        0        0     4060 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.98/docs/_build/.doctrees/CHANGELOG.doctree
+-rw-r--r--   0        0        0    28885 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.98/docs/_build/.doctrees/environment.pickle
+-rw-r--r--   0        0        0    10541 2022-10-04 08:09:06.782694 pyprocessors-afp_entities-0.5.98/docs/_build/.doctrees/index.doctree
+-rw-r--r--   0        0        0     6249 2023-01-20 15:32:17.312095 pyprocessors-afp_entities-0.5.98/docs/_build/CHANGELOG.html
+-rw-r--r--   0        0        0     1082 2022-10-04 08:09:06.783694 pyprocessors-afp_entities-0.5.98/docs/_build/LICENSE
+-rw-r--r--   0        0        0     4920 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.98/docs/_build/_modules/index.html
+-rw-r--r--   0        0        0    24197 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.98/docs/_build/_modules/pyformatters_consolidate/consolidate.html
+-rw-r--r--   0        0        0      268 2022-10-04 08:09:06.784695 pyprocessors-afp_entities-0.5.98/docs/_build/_sources/CHANGELOG.md.txt
+-rw-r--r--   0        0        0      146 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.98/docs/_build/_sources/index.rst.txt
+-rw-r--r--   0        0        0    14652 2022-10-04 08:09:06.785694 pyprocessors-afp_entities-0.5.98/docs/_build/_static/basic.css
+-rw-r--r--   0        0        0     3275 2022-10-04 08:09:06.786694 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/badge_only.css
+-rw-r--r--   0        0        0    87624 2022-10-04 08:09:06.787695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/Roboto-Slab-Bold.woff
+-rw-r--r--   0        0        0    67312 2022-10-04 08:09:06.788694 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/Roboto-Slab-Bold.woff2
+-rw-r--r--   0        0        0    86288 2022-10-04 08:09:06.791694 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/Roboto-Slab-Regular.woff
+-rw-r--r--   0        0        0    66444 2022-10-04 08:09:06.791694 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/Roboto-Slab-Regular.woff2
+-rw-r--r--   0        0        0   165742 2022-10-04 08:09:06.793695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/fontawesome-webfont.eot
+-rw-r--r--   0        0        0   444379 2022-10-04 08:09:06.796695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/fontawesome-webfont.svg
+-rw-r--r--   0        0        0   165548 2022-10-04 08:09:06.797695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/fontawesome-webfont.ttf
+-rw-r--r--   0        0        0    98024 2022-10-04 08:09:06.798695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/fontawesome-webfont.woff
+-rw-r--r--   0        0        0    77160 2022-10-04 08:09:06.800695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/fontawesome-webfont.woff2
+-rw-r--r--   0        0        0   323344 2022-10-04 08:09:06.805695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-bold-italic.woff
+-rw-r--r--   0        0        0   193308 2022-10-04 08:09:06.808695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-bold-italic.woff2
+-rw-r--r--   0        0        0   309728 2022-10-04 08:09:06.811695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-bold.woff
+-rw-r--r--   0        0        0   184912 2022-10-04 08:09:06.813695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-bold.woff2
+-rw-r--r--   0        0        0   328412 2022-10-04 08:09:06.817695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-normal-italic.woff
+-rw-r--r--   0        0        0   195704 2022-10-04 08:09:06.818695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-normal-italic.woff2
+-rw-r--r--   0        0        0   309192 2022-10-04 08:09:06.824695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-normal.woff
+-rw-r--r--   0        0        0   182708 2022-10-04 08:09:06.825695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-normal.woff2
+-rw-r--r--   0        0        0   123687 2022-10-04 08:09:06.825695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/theme.css
+-rw-r--r--   0        0        0     9592 2022-10-04 08:09:06.825695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/doctools.js
+-rw-r--r--   0        0        0      360 2022-10-04 08:09:06.826696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/documentation_options.js
+-rw-r--r--   0        0        0      286 2022-10-04 08:09:06.826696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/file.png
+-rw-r--r--   0        0        0   109948 2022-10-04 08:09:06.826696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Inconsolata-Bold.ttf
+-rw-r--r--   0        0        0    96964 2022-10-04 08:09:06.827695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Inconsolata-Regular.ttf
+-rw-r--r--   0        0        0    63184 2022-10-04 08:09:06.827695 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Inconsolata.ttf
+-rw-r--r--   0        0        0   656544 2022-10-04 08:09:06.836696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato-Bold.ttf
+-rw-r--r--   0        0        0   656568 2022-10-04 08:09:06.844696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato-Regular.ttf
+-rw-r--r--   0        0        0   256056 2022-10-04 08:09:06.846696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bold.eot
+-rw-r--r--   0        0        0   600856 2022-10-04 08:09:06.847696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bold.ttf
+-rw-r--r--   0        0        0   309728 2022-10-04 08:09:06.848696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bold.woff
+-rw-r--r--   0        0        0   184912 2022-10-04 08:09:06.848696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bold.woff2
+-rw-r--r--   0        0        0   266158 2022-10-04 08:09:06.850696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bolditalic.eot
+-rw-r--r--   0        0        0   622572 2022-10-04 08:09:06.856696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bolditalic.ttf
+-rw-r--r--   0        0        0   323344 2022-10-04 08:09:06.857696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bolditalic.woff
+-rw-r--r--   0        0        0   193308 2022-10-04 08:09:06.857696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bolditalic.woff2
+-rw-r--r--   0        0        0   268604 2022-10-04 08:09:06.861696 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-italic.eot
+-rw-r--r--   0        0        0   639388 2022-10-04 08:09:06.868697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-italic.ttf
+-rw-r--r--   0        0        0   328412 2022-10-04 08:09:06.869697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-italic.woff
+-rw-r--r--   0        0        0   195704 2022-10-04 08:09:06.869697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-italic.woff2
+-rw-r--r--   0        0        0   253461 2022-10-04 08:09:06.870697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-regular.eot
+-rw-r--r--   0        0        0   607720 2022-10-04 08:09:06.870697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-regular.ttf
+-rw-r--r--   0        0        0   309192 2022-10-04 08:09:06.872697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-regular.woff
+-rw-r--r--   0        0        0   182708 2022-10-04 08:09:06.872697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-regular.woff2
+-rw-r--r--   0        0        0   170616 2022-10-04 08:09:06.874697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab-Bold.ttf
+-rw-r--r--   0        0        0   169064 2022-10-04 08:09:06.875697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab-Regular.ttf
+-rw-r--r--   0        0        0    79520 2022-10-04 08:09:06.878697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.eot
+-rw-r--r--   0        0        0   170616 2022-10-04 08:09:06.879697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.ttf
+-rw-r--r--   0        0        0    87624 2022-10-04 08:09:06.879697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.woff
+-rw-r--r--   0        0        0    67312 2022-10-04 08:09:06.880697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.woff2
+-rw-r--r--   0        0        0    78331 2022-10-04 08:09:06.880697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.eot
+-rw-r--r--   0        0        0   169064 2022-10-04 08:09:06.882697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.ttf
+-rw-r--r--   0        0        0    86288 2022-10-04 08:09:06.883697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.woff
+-rw-r--r--   0        0        0    66444 2022-10-04 08:09:06.884697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.woff2
+-rw-r--r--   0        0        0   165742 2022-10-04 08:09:06.885697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/fontawesome-webfont.eot
+-rw-r--r--   0        0        0   444379 2022-10-04 08:09:06.888697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/fontawesome-webfont.svg
+-rw-r--r--   0        0        0   165548 2022-10-04 08:09:06.889697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/fontawesome-webfont.ttf
+-rw-r--r--   0        0        0    98024 2022-10-04 08:09:06.889697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/fontawesome-webfont.woff
+-rw-r--r--   0        0        0    77160 2022-10-04 08:09:06.889697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/fontawesome-webfont.woff2
+-rw-r--r--   0        0        0   287630 2022-10-04 08:09:06.890697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/jquery-3.5.1.js
+-rw-r--r--   0        0        0    89476 2022-10-04 08:09:06.891697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/jquery.js
+-rw-r--r--   0        0        0      934 2022-10-04 08:09:06.891697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/js/badge_only.js
+-rw-r--r--   0        0        0     4370 2022-10-04 08:09:06.891697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/js/html5shiv-printshiv.min.js
+-rw-r--r--   0        0        0     2734 2022-10-04 08:09:06.891697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/js/html5shiv.min.js
+-rw-r--r--   0        0        0    15414 2022-10-04 08:09:06.891697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/js/modernizr.min.js
+-rw-r--r--   0        0        0     4916 2022-10-04 08:09:06.891697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/js/theme.js
+-rw-r--r--   0        0        0     3019 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/jupyter-sphinx.css
+-rw-r--r--   0        0        0    10854 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/language_data.js
+-rw-r--r--   0        0        0       90 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/minus.png
+-rw-r--r--   0        0        0       90 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/plus.png
+-rw-r--r--   0        0        0     4819 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/pygments.css
+-rw-r--r--   0        0        0    16578 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/searchtools.js
+-rw-r--r--   0        0        0    68420 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/underscore-1.13.1.js
+-rw-r--r--   0        0        0    19530 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.98/docs/_build/_static/underscore.js
+-rw-r--r--   0        0        0    10035 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.98/docs/_build/genindex.html
+-rw-r--r--   0        0        0     9415 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.98/docs/_build/index.html
+-rw-r--r--   0        0        0      671 2022-10-04 08:09:06.892697 pyprocessors-afp_entities-0.5.98/docs/_build/objects.inv
+-rw-r--r--   0        0        0     5634 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.98/docs/_build/py-modindex.html
+-rw-r--r--   0        0        0     5201 2023-01-20 15:32:17.313095 pyprocessors-afp_entities-0.5.98/docs/_build/search.html
+-rw-r--r--   0        0        0     2790 2023-01-20 15:32:17.314095 pyprocessors-afp_entities-0.5.98/docs/_build/searchindex.js
+-rw-r--r--   0        0        0        0 2022-10-04 08:09:06.893697 pyprocessors-afp_entities-0.5.98/docs/_static/.gitkeep
+-rw-r--r--   0        0        0        0 2022-10-04 08:09:06.893697 pyprocessors-afp_entities-0.5.98/docs/_templates/.gitkeep
+-rw-r--r--   0        0        0     2899 2023-01-20 15:32:17.314095 pyprocessors-afp_entities-0.5.98/docs/conf.py
+-rw-r--r--   0        0        0      146 2023-01-20 15:32:17.314095 pyprocessors-afp_entities-0.5.98/docs/index.rst
+-rw-r--r--   0        0        0       98 2022-10-04 08:09:06.893697 pyprocessors-afp_entities-0.5.98/mypy.ini
+-rw-r--r--   0        0        0     2272 2023-01-20 15:32:17.314095 pyprocessors-afp_entities-0.5.98/pyproject.toml
+-rw-r--r--   0        0        0     5461 2023-03-14 08:16:33.669800 pyprocessors-afp_entities-0.5.98/results.xml
+-rw-r--r--   0        0        0       60 2023-03-14 08:19:26.906321 pyprocessors-afp_entities-0.5.98/src/pyprocessors_afp_entities/__init__.py
+-rw-r--r--   0        0        0    12331 2023-03-14 07:56:54.069018 pyprocessors-afp_entities-0.5.98/src/pyprocessors_afp_entities/afp_entities.py
+-rw-r--r--   0        0        0   266240 2022-10-04 08:09:06.901697 pyprocessors-afp_entities-0.5.98/tests/.coverage
+-rw-r--r--   0        0        0        0 2022-10-04 08:09:06.902697 pyprocessors-afp_entities-0.5.98/tests/__init__.py
+-rw-r--r--   0        0        0    33656 2023-01-20 15:32:17.316095 pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_en-document-test.json
+-rw-r--r--   0        0        0     6824 2023-02-09 16:59:22.431761 pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_es-document-test.json
+-rw-r--r--   0        0        0    32270 2023-01-20 15:32:17.316095 pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_fr-document-test-whitelist.json
+-rw-r--r--   0        0        0    38988 2023-01-12 16:35:46.402331 pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_fr-document-test-whitelist2.json
+-rw-r--r--   0        0        0    53390 2023-01-20 15:32:17.316095 pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_fr-document-test.json
+-rw-r--r--   0        0        0   104534 2023-01-20 15:32:17.318095 pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_fr-document-test1.json
+-rw-r--r--   0        0        0    12875 2023-03-14 08:16:33.671800 pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_fr-document-test2.json
+-rw-r--r--   0        0        0     7872 2023-03-14 08:16:33.671800 pyprocessors-afp_entities-0.5.98/tests/test_afp_entities.py
+-rw-r--r--   0        0        0      867 2023-01-20 15:32:17.318095 pyprocessors-afp_entities-0.5.98/tox.ini
+-rw-r--r--   0        0        0     1384 1970-01-01 00:00:00.000000 pyprocessors-afp_entities-0.5.98/setup.py
+-rw-r--r--   0        0        0     3432 1970-01-01 00:00:00.000000 pyprocessors-afp_entities-0.5.98/PKG-INFO
```

### Comparing `pyprocessors-afp_entities-0.5.92/.gitignore` & `pyprocessors-afp_entities-0.5.98/.gitignore`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/Jenkinsfile` & `pyprocessors-afp_entities-0.5.98/Jenkinsfile`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/LICENSE` & `pyprocessors-afp_entities-0.5.98/LICENSE`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/README.md` & `pyprocessors-afp_entities-0.5.98/README.md`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/RELEASE.md` & `pyprocessors-afp_entities-0.5.98/RELEASE.md`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/bumpversion.py` & `pyprocessors-afp_entities-0.5.98/bumpversion.py`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/LICENSE` & `pyprocessors-afp_entities-0.5.98/docs/LICENSE`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/.doctrees/CHANGELOG.doctree` & `pyprocessors-afp_entities-0.5.98/docs/_build/.doctrees/CHANGELOG.doctree`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/.doctrees/environment.pickle` & `pyprocessors-afp_entities-0.5.98/docs/_build/.doctrees/environment.pickle`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/.doctrees/index.doctree` & `pyprocessors-afp_entities-0.5.98/docs/_build/.doctrees/index.doctree`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/CHANGELOG.html` & `pyprocessors-afp_entities-0.5.98/docs/_build/CHANGELOG.html`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/LICENSE` & `pyprocessors-afp_entities-0.5.98/docs/_build/LICENSE`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_modules/index.html` & `pyprocessors-afp_entities-0.5.98/docs/_build/_modules/index.html`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_modules/pyformatters_consolidate/consolidate.html` & `pyprocessors-afp_entities-0.5.98/docs/_build/_modules/pyformatters_consolidate/consolidate.html`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/basic.css` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/basic.css`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/badge_only.css` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/badge_only.css`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/Roboto-Slab-Bold.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/Roboto-Slab-Bold.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/Roboto-Slab-Bold.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/Roboto-Slab-Bold.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/Roboto-Slab-Regular.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/Roboto-Slab-Regular.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/Roboto-Slab-Regular.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/Roboto-Slab-Regular.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/fontawesome-webfont.eot` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/fontawesome-webfont.eot`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/fontawesome-webfont.svg` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/fontawesome-webfont.svg`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/fontawesome-webfont.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/fontawesome-webfont.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/fontawesome-webfont.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/fontawesome-webfont.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/fontawesome-webfont.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/fontawesome-webfont.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-bold-italic.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-bold-italic.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-bold-italic.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-bold-italic.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-bold.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-bold.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-bold.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-bold.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-normal-italic.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-normal-italic.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-normal-italic.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-normal-italic.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-normal.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-normal.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/fonts/lato-normal.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/fonts/lato-normal.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/css/theme.css` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/css/theme.css`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/doctools.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/doctools.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Inconsolata-Bold.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Inconsolata-Bold.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Inconsolata-Regular.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Inconsolata-Regular.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Inconsolata.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Inconsolata.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato-Bold.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato-Bold.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato-Regular.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato-Regular.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bold.eot` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bold.eot`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bold.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bold.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bold.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bold.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bold.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bold.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bolditalic.eot` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bolditalic.eot`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bolditalic.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bolditalic.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bolditalic.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bolditalic.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-bolditalic.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-bolditalic.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-italic.eot` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-italic.eot`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-italic.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-italic.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-italic.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-italic.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-italic.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-italic.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-regular.eot` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-regular.eot`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-regular.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-regular.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-regular.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-regular.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/Lato/lato-regular.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/Lato/lato-regular.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab-Bold.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab-Bold.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab-Regular.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab-Regular.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.eot` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.eot`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-bold.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.eot` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.eot`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/RobotoSlab/roboto-slab-v7-regular.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/fontawesome-webfont.eot` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/fontawesome-webfont.eot`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/fontawesome-webfont.svg` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/fontawesome-webfont.svg`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/fontawesome-webfont.ttf` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/fontawesome-webfont.ttf`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/fontawesome-webfont.woff` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/fontawesome-webfont.woff`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/fonts/fontawesome-webfont.woff2` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/fonts/fontawesome-webfont.woff2`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/jquery-3.5.1.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/jquery-3.5.1.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/jquery.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/jquery.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/js/badge_only.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/js/badge_only.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/js/html5shiv-printshiv.min.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/js/html5shiv-printshiv.min.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/js/html5shiv.min.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/js/html5shiv.min.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/js/modernizr.min.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/js/modernizr.min.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/js/theme.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/js/theme.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/jupyter-sphinx.css` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/jupyter-sphinx.css`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/language_data.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/language_data.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/pygments.css` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/pygments.css`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/searchtools.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/searchtools.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/underscore-1.13.1.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/underscore-1.13.1.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/_static/underscore.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/_static/underscore.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/genindex.html` & `pyprocessors-afp_entities-0.5.98/docs/_build/genindex.html`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/index.html` & `pyprocessors-afp_entities-0.5.98/docs/_build/index.html`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/objects.inv` & `pyprocessors-afp_entities-0.5.98/docs/_build/objects.inv`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/py-modindex.html` & `pyprocessors-afp_entities-0.5.98/docs/_build/py-modindex.html`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/search.html` & `pyprocessors-afp_entities-0.5.98/docs/_build/search.html`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/_build/searchindex.js` & `pyprocessors-afp_entities-0.5.98/docs/_build/searchindex.js`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/docs/conf.py` & `pyprocessors-afp_entities-0.5.98/docs/conf.py`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/pyproject.toml` & `pyprocessors-afp_entities-0.5.98/pyproject.toml`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/results.xml` & `pyprocessors-afp_entities-0.5.98/results.xml`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/src/pyprocessors_afp_entities/afp_entities.py` & `pyprocessors-afp_entities-0.5.98/src/pyprocessors_afp_entities/afp_entities.py`

 * *Files 1% similar despite different names*

```diff
@@ -265,15 +265,16 @@
     return suspicious
 
 
 # noqa: W503
 def annotation_in_group(
     a: Annotation, ann_groups: Dict[str, RangeMap], gnames: List[str] = None
 ):
-    gnames = gnames or [a.labelName]
+    if a.labelName in gnames:
+        gnames = [a.labelName]
     for gname in gnames:
         if (
             gname in ann_groups
             and a.start in ann_groups[gname]
             or a.end in ann_groups[gname]
         ):
             return ann_groups[gname][a.start : a.end]
```

### Comparing `pyprocessors-afp_entities-0.5.92/tests/.coverage` & `pyprocessors-afp_entities-0.5.98/tests/.coverage`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/tests/data/afp_ner_en-document-test.json` & `pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_en-document-test.json`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/tests/data/afp_ner_es-document-test.json` & `pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_es-document-test.json`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/tests/data/afp_ner_fr-document-test-whitelist.json` & `pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_fr-document-test-whitelist.json`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/tests/data/afp_ner_fr-document-test-whitelist2.json` & `pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_fr-document-test-whitelist2.json`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/tests/data/afp_ner_fr-document-test.json` & `pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_fr-document-test.json`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/tests/data/afp_ner_fr-document-test1.json` & `pyprocessors-afp_entities-0.5.98/tests/data/afp_ner_fr-document-test1.json`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/tests/test_afp_entities.py` & `pyprocessors-afp_entities-0.5.98/tests/test_afp_entities.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 import json
 import re
 from pathlib import Path
 
 import pytest
 from dirty_equals import HasLen, IsPartialDict, IsStr, IsList
 from pymultirole_plugins.v1.schema import Document, Annotation
+
 from pyprocessors_afp_entities.afp_entities import (
     AFPEntitiesProcessor,
     AFPEntitiesParameters,
     ConsolidationType,
     group_annotations,
     is_suspicious,
 )
@@ -29,14 +30,25 @@
         doc = json.load(fin)
         original_doc = Document(**doc)
         return original_doc
 
 
 # Arrange
 @pytest.fixture
+def original_doc2():
+    testdir = Path(__file__).parent
+    source = Path(testdir, "data/afp_ner_fr-document-test2.json")
+    with source.open("r") as fin:
+        doc = json.load(fin)
+        original_doc = Document(**doc)
+        return original_doc
+
+
+# Arrange
+@pytest.fixture
 def original_doc_en():
     testdir = Path(__file__).parent
     source = Path(testdir, "data/afp_ner_en-document-test.json")
     with source.open("r") as fin:
         doc = json.load(fin)
         original_doc = Document(**doc)
         return original_doc
@@ -61,15 +73,15 @@
     altText = conso.altTexts[0]
     FINGERPRINT = re.compile(r"([QE]\d+[ ]?)+")
     assert altText.dict() == IsPartialDict(
         name="fingerprint", text=IsStr(regex=FINGERPRINT)
     )
     assert len(conso.annotations) < len(original_doc.annotations)
     conso_groups = group_annotations(conso, by_linking)
-    assert len(conso_groups["candidate"]) == 3
+    assert len(conso_groups["candidate"]) == 8
     assert len(conso_groups["person"]) == 2
     persons = [r.value.dict() for r in conso_groups["person"].ranges()]
     assert persons == IsList(
         IsPartialDict(
             label="AFPPerson",
             text="Frank Garnier",
             terms=IsList(
@@ -86,14 +98,70 @@
         length=2,
     )
     assert len(conso_groups["wikidata"]) == 10
     assert len(conso_groups["location+wikidata"]) == 1
     assert len(conso_groups["organization+wikidata"]) == 2
 
 
+def test_afp_entities_linker2(original_doc2):
+    # linker
+    doc = original_doc2.copy(deep=True)
+    processor = AFPEntitiesProcessor()
+    parameters = AFPEntitiesParameters(type=ConsolidationType.linker)
+    docs = processor.process([doc], parameters)
+    conso: Document = docs[0]
+    assert conso.altTexts == HasLen(1)
+    altText = conso.altTexts[0]
+    FINGERPRINT = re.compile(r"([QE]\d+[ ]?)+")
+    assert altText.dict() == IsPartialDict(
+        name="fingerprint", text=IsStr(regex=FINGERPRINT)
+    )
+    assert len(conso.annotations) < len(original_doc2.annotations)
+    conso_groups = group_annotations(conso, by_linking)
+    assert len(conso_groups["candidate"]) == 1
+    assert len(conso_groups["person"]) == 1
+    persons = [r.value.dict() for r in conso_groups["person"].ranges()]
+    assert persons == IsList(
+        IsPartialDict(
+            label="AFPPerson",
+            text="Jean-Marc Berthon",
+            terms=IsList(
+                IsPartialDict(identifier=IsStr(regex=r"^afpperson.*")), length=1
+            ),
+        ),
+        length=1,
+    )
+    assert len(conso_groups["location+wikidata"]) == 1
+    locations = [r.value.dict() for r in conso_groups["location+wikidata"].ranges()]
+    assert locations == IsList(
+        IsPartialDict(
+            label="AFPLocation",
+            text="France",
+            terms=IsList(
+                IsPartialDict(identifier=IsStr(regex=r"^afplocation.*")),
+                IsPartialDict(identifier=IsStr(regex=r"^Q.*")), length=2
+            ),
+        ),
+        length=1,
+    )
+    assert len(conso_groups["person+wikidata"]) == 1
+    persons = [r.value.dict() for r in conso_groups["person+wikidata"].ranges()]
+    assert persons == IsList(
+        IsPartialDict(
+            label="AFPPerson",
+            text="Elisabeth Borne",
+            terms=IsList(
+                IsPartialDict(identifier=IsStr(regex=r"^afpperson.*")),
+                IsPartialDict(identifier=IsStr(regex=r"^Q.*")), length=2
+            ),
+        ),
+        length=1,
+    )
+
+
 def test_afp_entities_whitelist():
     testdir = Path(__file__).parent
     source = Path(testdir, "data/afp_ner_fr-document-test-whitelist2.json")
     with source.open("r") as fin:
         doc = json.load(fin)
         original_doc = Document(**doc)
     # linker
@@ -126,14 +194,17 @@
             text="Lil Nas X",
             terms=IsList(
                 IsPartialDict(identifier=IsStr(regex=r"^afpperson.*")), length=1
             ),
         ),
         length=2,
     )
+    assert len(conso_groups["location+wikidata"]) == 10
+    assert len(conso_groups["organization+wikidata"]) == 3
+    assert len(conso_groups["person+wikidata"]) == 1
     assert len(conso_groups["wikidata"]) == 1
     assert len(conso_groups["location"]) == 2
 
 
 def test_afp_entities_suspicious():
     testdir = Path(__file__).parent
     source = Path(testdir, "data/afp_ner_es-document-test.json")
```

### Comparing `pyprocessors-afp_entities-0.5.92/tox.ini` & `pyprocessors-afp_entities-0.5.98/tox.ini`

 * *Files identical despite different names*

### Comparing `pyprocessors-afp_entities-0.5.92/setup.py` & `pyprocessors-afp_entities-0.5.98/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -34,15 +34,15 @@
           'dirty-equals']}
 
 entry_points = \
 {'pyprocessors.plugins': ['afp_entities = '
                           'pyprocessors_afp_entities.afp_entities:AFPEntitiesProcessor']}
 
 setup(name='pyprocessors-afp_entities',
-      version='0.5.92',
+      version='0.5.98',
       description='Sherpa Consolidation processor',
       author='Olivier Terrier',
       author_email='olivier.terrier@kairntech.com',
       url='https://github.com/oterrier/pyprocessors_afp_entities/',
       packages=packages,
       package_data=package_data,
       package_dir=package_dir,
```

### Comparing `pyprocessors-afp_entities-0.5.92/PKG-INFO` & `pyprocessors-afp_entities-0.5.98/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyprocessors-afp_entities
-Version: 0.5.92
+Version: 0.5.98
 Summary: Sherpa Consolidation processor
 Home-page: https://github.com/oterrier/pyprocessors_afp_entities/
 Keywords: 
 Author: Olivier Terrier
 Author-email: olivier.terrier@kairntech.com
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
```

