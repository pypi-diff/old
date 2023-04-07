# Comparing `tmp/sfrout-0.0.8.tar.gz` & `tmp/sfrout-0.0.9.tar.gz`

## Comparing `sfrout-0.0.8.tar` & `sfrout-0.0.9.tar`

### file list

```diff
@@ -1,100 +1,80 @@
--rw-r--r--   0        0        0    53248 2020-02-02 00:00:00.000000 sfrout-0.0.8/.coverage
--rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 sfrout-0.0.8/.coveragerc
--rw-r--r--   0        0        0     1343 2020-02-02 00:00:00.000000 sfrout-0.0.8/CHANGELOG.md
--rw-r--r--   0        0        0      186 2020-02-02 00:00:00.000000 sfrout-0.0.8/pytest.ini
--rw-r--r--   0        0        0      171 2020-02-02 00:00:00.000000 sfrout-0.0.8/requirements.txt
--rw-r--r--   0        0        0      638 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/Makefile
--rwxr-xr-x   0        0        0      804 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/make.bat
--rw-r--r--   0        0        0   254436 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/doctrees/components.doctree
--rw-r--r--   0        0        0   479153 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/doctrees/environment.pickle
--rw-r--r--   0        0        0     5568 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/doctrees/index.doctree
--rw-r--r--   0        0        0    15086 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/doctrees/intro.doctree
--rw-r--r--   0        0        0     2442 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/doctrees/main.doctree
--rw-r--r--   0        0        0     2758 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/doctrees/modules.doctree
--rw-r--r--   0        0        0      234 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/.buildinfo
--rw-r--r--   0        0        0   106722 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/components.html
--rw-r--r--   0        0        0    21759 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/genindex.html
--rw-r--r--   0        0        0     6727 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/index.html
--rw-r--r--   0        0        0     9430 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/intro.html
--rw-r--r--   0        0        0     4466 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/main.html
--rw-r--r--   0        0        0    24181 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/modules.html
--rw-r--r--   0        0        0      942 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/objects.inv
--rw-r--r--   0        0        0     5470 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/py-modindex.html
--rw-r--r--   0        0        0     3960 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/search.html
--rw-r--r--   0        0        0    11875 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/searchindex.js
--rw-r--r--   0        0        0     4046 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_modules/index.html
--rw-r--r--   0        0        0    28603 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_modules/components/config.html
--rw-r--r--   0        0        0    48341 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_modules/components/connectors.html
--rw-r--r--   0        0        0    31812 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_modules/components/containers.html
--rw-r--r--   0        0        0     7062 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_modules/components/exceptions.html
--rw-r--r--   0        0        0    37550 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_modules/components/handlers.html
--rw-r--r--   0        0        0    11695 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_modules/components/loggers.html
--rw-r--r--   0        0        0     1122 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_sources/components.rst.txt
--rw-r--r--   0        0        0      486 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_sources/index.rst.txt
--rw-r--r--   0        0        0     2953 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_sources/intro.rst.txt
--rw-r--r--   0        0        0      107 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_sources/main.rst.txt
--rw-r--r--   0        0        0       69 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_sources/modules.rst.txt
--rw-r--r--   0        0        0    15715 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/basic.css
--rw-r--r--   0        0        0     4472 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/doctools.js
--rw-r--r--   0        0        0      433 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/documentation_options.js
--rw-r--r--   0        0        0      286 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/file.png
--rw-r--r--   0        0        0     4957 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/language_data.js
--rw-r--r--   0        0        0       90 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/minus.png
--rw-r--r--   0        0        0       90 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/plus.png
--rw-r--r--   0        0        0     4892 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/pygments.css
--rw-r--r--   0        0        0    18215 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/searchtools.js
--rw-r--r--   0        0        0     4712 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/sphinx_highlight.js
--rw-r--r--   0        0        0     3229 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/badge_only.css
--rw-r--r--   0        0        0   135235 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/theme.css
--rw-r--r--   0        0        0    87624 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff
--rw-r--r--   0        0        0    67312 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff2
--rw-r--r--   0        0        0    86288 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff
--rw-r--r--   0        0        0    66444 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff2
--rw-r--r--   0        0        0   165742 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.eot
--rw-r--r--   0        0        0   444379 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.svg
--rw-r--r--   0        0        0   165548 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.ttf
--rw-r--r--   0        0        0    98024 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.woff
--rw-r--r--   0        0        0    77160 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.woff2
--rw-r--r--   0        0        0   323344 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-bold-italic.woff
--rw-r--r--   0        0        0   193308 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-bold-italic.woff2
--rw-r--r--   0        0        0   309728 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-bold.woff
--rw-r--r--   0        0        0   184912 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-bold.woff2
--rw-r--r--   0        0        0   328412 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-normal-italic.woff
--rw-r--r--   0        0        0   195704 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-normal-italic.woff2
--rw-r--r--   0        0        0   309192 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-normal.woff
--rw-r--r--   0        0        0   182708 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-normal.woff2
--rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/js/badge_only.js
--rw-r--r--   0        0        0     4370 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/js/html5shiv-printshiv.min.js
--rw-r--r--   0        0        0     2734 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/js/html5shiv.min.js
--rw-r--r--   0        0        0     5023 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/build/html/_static/js/theme.js
--rw-r--r--   0        0        0     1122 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/source/components.rst
--rw-r--r--   0        0        0     1147 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/source/conf.py
--rw-r--r--   0        0        0      486 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/source/index.rst
--rw-r--r--   0        0        0     2953 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/source/intro.rst
--rw-r--r--   0        0        0      107 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/source/main.rst
--rw-r--r--   0        0        0       69 2020-02-02 00:00:00.000000 sfrout-0.0.8/docs/source/modules.rst
--rw-r--r--   0        0        0      256 2020-02-02 00:00:00.000000 sfrout-0.0.8/example/reports-default.csv
--rw-r--r--   0        0        0       77 2020-02-02 00:00:00.000000 sfrout-0.0.8/src/sfrout/__init__.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 sfrout-0.0.8/src/sfrout/app/__init__.py
--rw-r--r--   0        0        0     2285 2020-02-02 00:00:00.000000 sfrout-0.0.8/src/sfrout/app/cli.py
--rw-r--r--   0        0        0     4178 2020-02-02 00:00:00.000000 sfrout-0.0.8/src/sfrout/app/main.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 sfrout-0.0.8/src/sfrout/components/__init__.py
--rw-r--r--   0        0        0     7098 2020-02-02 00:00:00.000000 sfrout-0.0.8/src/sfrout/components/config.py
--rw-r--r--   0        0        0    13009 2020-02-02 00:00:00.000000 sfrout-0.0.8/src/sfrout/components/connectors.py
--rw-r--r--   0        0        0     8839 2020-02-02 00:00:00.000000 sfrout-0.0.8/src/sfrout/components/containers.py
--rw-r--r--   0        0        0      792 2020-02-02 00:00:00.000000 sfrout-0.0.8/src/sfrout/components/exceptions.py
--rw-r--r--   0        0        0     8765 2020-02-02 00:00:00.000000 sfrout-0.0.8/src/sfrout/components/handlers.py
--rw-r--r--   0        0        0     2051 2020-02-02 00:00:00.000000 sfrout-0.0.8/src/sfrout/components/loggers.py
--rw-r--r--   0        0        0     5081 2020-02-02 00:00:00.000000 sfrout-0.0.8/tests/conftest.py
--rw-r--r--   0        0        0     3040 2020-02-02 00:00:00.000000 sfrout-0.0.8/tests/test_config.py
--rw-r--r--   0        0        0      770 2020-02-02 00:00:00.000000 sfrout-0.0.8/tests/test_connector.py
--rw-r--r--   0        0        0      811 2020-02-02 00:00:00.000000 sfrout-0.0.8/tests/test_container.py
--rw-r--r--   0        0        0      131 2020-02-02 00:00:00.000000 sfrout-0.0.8/tests/sample_files/correct_multi_sfdc.csv
--rw-r--r--   0        0        0      371 2020-02-02 00:00:00.000000 sfrout-0.0.8/tests/sample_files/correct_multi_sfdc_opt_params.csv
--rw-r--r--   0        0        0       96 2020-02-02 00:00:00.000000 sfrout-0.0.8/tests/sample_files/correct_single_sfdc.csv
--rw-r--r--   0        0        0      216 2020-02-02 00:00:00.000000 sfrout-0.0.8/tests/sample_files/correct_single_sfdc_opt_params.csv
--rw-r--r--   0        0        0       43 2020-02-02 00:00:00.000000 sfrout-0.0.8/.gitignore
--rw-r--r--   0        0        0    11547 2020-02-02 00:00:00.000000 sfrout-0.0.8/LICENSE.md
--rw-r--r--   0        0        0     7796 2020-02-02 00:00:00.000000 sfrout-0.0.8/README.md
--rw-r--r--   0        0        0     1273 2020-02-02 00:00:00.000000 sfrout-0.0.8/pyproject.toml
--rw-r--r--   0        0        0     8608 2020-02-02 00:00:00.000000 sfrout-0.0.8/PKG-INFO
+-rw-r--r--   0        0        0    53248 2020-02-02 00:00:00.000000 sfrout-0.0.9/.coverage
+-rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 sfrout-0.0.9/.coveragerc
+-rw-r--r--   0        0        0     1343 2020-02-02 00:00:00.000000 sfrout-0.0.9/CHANGELOG.md
+-rw-r--r--   0        0        0      186 2020-02-02 00:00:00.000000 sfrout-0.0.9/pytest.ini
+-rw-r--r--   0        0        0      171 2020-02-02 00:00:00.000000 sfrout-0.0.9/requirements.txt
+-rw-r--r--   0        0        0      638 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/Makefile
+-rwxr-xr-x   0        0        0      804 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/make.bat
+-rw-r--r--   0        0        0    63571 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/doctrees/environment.pickle
+-rw-r--r--   0        0        0    33233 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/doctrees/index.doctree
+-rw-r--r--   0        0        0      234 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/.buildinfo
+-rw-r--r--   0        0        0     3509 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/genindex.html
+-rw-r--r--   0        0        0    12582 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/index.html
+-rw-r--r--   0        0        0      280 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/objects.inv
+-rw-r--r--   0        0        0     3791 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/py-modindex.html
+-rw-r--r--   0        0        0     3641 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/search.html
+-rw-r--r--   0        0        0     3547 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/searchindex.js
+-rw-r--r--   0        0        0     3337 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_modules/index.html
+-rw-r--r--   0        0        0    15698 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_modules/main.html
+-rw-r--r--   0        0        0    47486 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_modules/components/connectors.html
+-rw-r--r--   0        0        0      706 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_sources/index.rst.txt
+-rw-r--r--   0        0        0    15715 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/basic.css
+-rw-r--r--   0        0        0     4472 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/doctools.js
+-rw-r--r--   0        0        0      433 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/documentation_options.js
+-rw-r--r--   0        0        0      286 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/file.png
+-rw-r--r--   0        0        0     4957 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/language_data.js
+-rw-r--r--   0        0        0       90 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/minus.png
+-rw-r--r--   0        0        0       90 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/plus.png
+-rw-r--r--   0        0        0     4892 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/pygments.css
+-rw-r--r--   0        0        0    18215 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/searchtools.js
+-rw-r--r--   0        0        0     4712 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/sphinx_highlight.js
+-rw-r--r--   0        0        0     3229 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/badge_only.css
+-rw-r--r--   0        0        0   135235 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/theme.css
+-rw-r--r--   0        0        0    87624 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff
+-rw-r--r--   0        0        0    67312 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff2
+-rw-r--r--   0        0        0    86288 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff
+-rw-r--r--   0        0        0    66444 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff2
+-rw-r--r--   0        0        0   165742 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.eot
+-rw-r--r--   0        0        0   444379 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.svg
+-rw-r--r--   0        0        0   165548 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.ttf
+-rw-r--r--   0        0        0    98024 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.woff
+-rw-r--r--   0        0        0    77160 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.woff2
+-rw-r--r--   0        0        0   323344 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-bold-italic.woff
+-rw-r--r--   0        0        0   193308 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-bold-italic.woff2
+-rw-r--r--   0        0        0   309728 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-bold.woff
+-rw-r--r--   0        0        0   184912 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-bold.woff2
+-rw-r--r--   0        0        0   328412 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-normal-italic.woff
+-rw-r--r--   0        0        0   195704 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-normal-italic.woff2
+-rw-r--r--   0        0        0   309192 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-normal.woff
+-rw-r--r--   0        0        0   182708 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-normal.woff2
+-rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/js/badge_only.js
+-rw-r--r--   0        0        0     4370 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/js/html5shiv-printshiv.min.js
+-rw-r--r--   0        0        0     2734 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/js/html5shiv.min.js
+-rw-r--r--   0        0        0     5023 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/build/html/_static/js/theme.js
+-rw-r--r--   0        0        0     1223 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/source/conf.py
+-rw-r--r--   0        0        0      706 2020-02-02 00:00:00.000000 sfrout-0.0.9/docs/source/index.rst
+-rw-r--r--   0        0        0      256 2020-02-02 00:00:00.000000 sfrout-0.0.9/example/reports-default.csv
+-rw-r--r--   0        0        0       73 2020-02-02 00:00:00.000000 sfrout-0.0.9/src/sfrout/__init__.py
+-rw-r--r--   0        0        0     4193 2020-02-02 00:00:00.000000 sfrout-0.0.9/src/sfrout/main.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 sfrout-0.0.9/src/sfrout/app/__init__.py
+-rw-r--r--   0        0        0     2279 2020-02-02 00:00:00.000000 sfrout-0.0.9/src/sfrout/app/cli.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 sfrout-0.0.9/src/sfrout/components/__init__.py
+-rw-r--r--   0        0        0     7098 2020-02-02 00:00:00.000000 sfrout-0.0.9/src/sfrout/components/config.py
+-rw-r--r--   0        0        0    13009 2020-02-02 00:00:00.000000 sfrout-0.0.9/src/sfrout/components/connectors.py
+-rw-r--r--   0        0        0     8839 2020-02-02 00:00:00.000000 sfrout-0.0.9/src/sfrout/components/containers.py
+-rw-r--r--   0        0        0      792 2020-02-02 00:00:00.000000 sfrout-0.0.9/src/sfrout/components/exceptions.py
+-rw-r--r--   0        0        0     8765 2020-02-02 00:00:00.000000 sfrout-0.0.9/src/sfrout/components/handlers.py
+-rw-r--r--   0        0        0     2051 2020-02-02 00:00:00.000000 sfrout-0.0.9/src/sfrout/components/loggers.py
+-rw-r--r--   0        0        0     5081 2020-02-02 00:00:00.000000 sfrout-0.0.9/tests/conftest.py
+-rw-r--r--   0        0        0     3040 2020-02-02 00:00:00.000000 sfrout-0.0.9/tests/test_config.py
+-rw-r--r--   0        0        0      770 2020-02-02 00:00:00.000000 sfrout-0.0.9/tests/test_connector.py
+-rw-r--r--   0        0        0      811 2020-02-02 00:00:00.000000 sfrout-0.0.9/tests/test_container.py
+-rw-r--r--   0        0        0      131 2020-02-02 00:00:00.000000 sfrout-0.0.9/tests/sample_files/correct_multi_sfdc.csv
+-rw-r--r--   0        0        0      371 2020-02-02 00:00:00.000000 sfrout-0.0.9/tests/sample_files/correct_multi_sfdc_opt_params.csv
+-rw-r--r--   0        0        0       96 2020-02-02 00:00:00.000000 sfrout-0.0.9/tests/sample_files/correct_single_sfdc.csv
+-rw-r--r--   0        0        0      216 2020-02-02 00:00:00.000000 sfrout-0.0.9/tests/sample_files/correct_single_sfdc_opt_params.csv
+-rw-r--r--   0        0        0       43 2020-02-02 00:00:00.000000 sfrout-0.0.9/.gitignore
+-rw-r--r--   0        0        0    11547 2020-02-02 00:00:00.000000 sfrout-0.0.9/LICENSE.md
+-rw-r--r--   0        0        0     7796 2020-02-02 00:00:00.000000 sfrout-0.0.9/README.md
+-rw-r--r--   0        0        0     1273 2020-02-02 00:00:00.000000 sfrout-0.0.9/pyproject.toml
+-rw-r--r--   0        0        0     8608 2020-02-02 00:00:00.000000 sfrout-0.0.9/PKG-INFO
```

### Comparing `sfrout-0.0.8/.coverage` & `sfrout-0.0.9/.coverage`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/CHANGELOG.md` & `sfrout-0.0.9/CHANGELOG.md`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/Makefile` & `sfrout-0.0.9/docs/Makefile`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/make.bat` & `sfrout-0.0.9/docs/make.bat`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/main.html` & `sfrout-0.0.9/docs/build/html/py-modindex.html`

 * *Files 22% similar despite different names*

```diff
@@ -1,27 +1,32 @@
 <!DOCTYPE html>
 <html class="writer-html5" lang="en" >
 <head>
-  <meta charset="utf-8" /><meta name="generator" content="Docutils 0.18.1: http://docutils.sourceforge.net/" />
-
+  <meta charset="utf-8" />
   <meta name="viewport" content="width=device-width, initial-scale=1.0" />
-  <title>main module &mdash; sfrout 0.0.7 documentation</title>
+  <title>Python Module Index &mdash; sfrout 0.0.7 documentation</title>
       <link rel="stylesheet" href="_static/pygments.css" type="text/css" />
       <link rel="stylesheet" href="_static/css/theme.css" type="text/css" />
   <!--[if lt IE 9]>
     <script src="_static/js/html5shiv.min.js"></script>
   <![endif]-->
   
         <script data-url_root="./" id="documentation_options" src="_static/documentation_options.js"></script>
         <script src="_static/doctools.js"></script>
         <script src="_static/sphinx_highlight.js"></script>
     <script src="_static/js/theme.js"></script>
     <link rel="index" title="Index" href="genindex.html" />
     <link rel="search" title="Search" href="search.html" />
-    <link rel="prev" title="src" href="modules.html" /> 
+ 
+
+    <script>
+      DOCUMENTATION_OPTIONS.COLLAPSE_INDEX = true;
+    </script>
+
+
 </head>
 
 <body class="wy-body-for-nav"> 
   <div class="wy-grid-for-nav">
     <nav data-toggle="wy-nav-shift" class="wy-nav-side">
       <div class="wy-side-scroll">
         <div class="wy-side-nav-search" >
@@ -35,60 +40,61 @@
   <form id="rtd-search-form" class="wy-form" action="search.html" method="get">
     <input type="text" name="q" placeholder="Search docs" aria-label="Search docs" />
     <input type="hidden" name="check_keywords" value="yes" />
     <input type="hidden" name="area" value="default" />
   </form>
 </div>
         </div><div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="Navigation menu">
-              <p class="caption" role="heading"><span class="caption-text">Contents:</span></p>
-<ul class="current">
-<li class="toctree-l1"><a class="reference internal" href="intro.html">Introduction</a></li>
-<li class="toctree-l1"><a class="reference internal" href="components.html">components package</a></li>
-<li class="toctree-l1 current"><a class="reference internal" href="modules.html">src</a><ul class="current">
-<li class="toctree-l2"><a class="reference internal" href="components.html">components package</a></li>
-<li class="toctree-l2 current"><a class="current reference internal" href="#">main module</a></li>
-</ul>
-</li>
-</ul>
-
+              <!-- Local TOC -->
+              <div class="local-toc"></div>
         </div>
       </div>
     </nav>
 
     <section data-toggle="wy-nav-shift" class="wy-nav-content-wrap"><nav class="wy-nav-top" aria-label="Mobile navigation menu" >
           <i data-toggle="wy-nav-top" class="fa fa-bars"></i>
           <a href="index.html">sfrout</a>
       </nav>
 
       <div class="wy-nav-content">
         <div class="rst-content">
           <div role="navigation" aria-label="Page navigation">
   <ul class="wy-breadcrumbs">
       <li><a href="index.html" class="icon icon-home" aria-label="Home"></a></li>
-          <li class="breadcrumb-item"><a href="modules.html">src</a></li>
-      <li class="breadcrumb-item active">main module</li>
+      <li class="breadcrumb-item active">Python Module Index</li>
       <li class="wy-breadcrumbs-aside">
-            <a href="_sources/main.rst.txt" rel="nofollow"> View page source</a>
       </li>
   </ul>
   <hr/>
 </div>
           <div role="main" class="document" itemscope="itemscope" itemtype="http://schema.org/Article">
            <div itemprop="articleBody">
              
-  <section id="main-module">
-<h1>main module<a class="headerlink" href="#main-module" title="Permalink to this heading"></a></h1>
-</section>
+
+   <h1>Python Module Index</h1>
+
+   <div class="modindex-jumpbox">
+   <a href="#cap-c"><strong>c</strong></a>
+   </div>
+
+   <table class="indextable modindextable">
+     <tr class="pcap"><td></td><td>&#160;</td><td></td></tr>
+     <tr class="cap" id="cap-c"><td></td><td>
+       <strong>c</strong></td><td></td></tr>
+     <tr>
+       <td></td>
+       <td>
+       <a href="index.html#module-components"><code class="xref">components</code></a></td><td>
+       <em></em></td></tr>
+   </table>
 
 
            </div>
           </div>
-          <footer><div class="rst-footer-buttons" role="navigation" aria-label="Footer">
-        <a href="modules.html" class="btn btn-neutral float-left" title="src" accesskey="p" rel="prev"><span class="fa fa-arrow-circle-left" aria-hidden="true"></span> Previous</a>
-    </div>
+          <footer>
 
   <hr/>
 
   <div role="contentinfo">
     <p>&#169; Copyright 2023, Lukasz Hoszowski.</p>
   </div>
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

#### html2text {}

```diff
@@ -1,24 +1,19 @@
 
 
 
 
 
-
 sfrout
 [q                   ]
-Contents:
-    * Introduction
-    * components_package
-    * src
-          o components_package
-          o main_module
    sfrout
-    * src
-    * main module
-    * View_page_source
+    * Python Module Index
 ===============================================================================
-****** main moduleï ******
-Previous
+****** Python Module Index ******
+c
+  
+ c
+ components
+
 ===============================================================================
 © Copyright 2023, Lukasz Hoszowski.
 Built with Sphinx using a theme provided by Read_the_Docs.
```

### Comparing `sfrout-0.0.8/docs/build/html/search.html` & `sfrout-0.0.9/docs/build/html/search.html`

 * *Files 11% similar despite different names*

```diff
@@ -36,21 +36,16 @@
   <form id="rtd-search-form" class="wy-form" action="#" method="get">
     <input type="text" name="q" placeholder="Search docs" aria-label="Search docs" />
     <input type="hidden" name="check_keywords" value="yes" />
     <input type="hidden" name="area" value="default" />
   </form>
 </div>
         </div><div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="Navigation menu">
-              <p class="caption" role="heading"><span class="caption-text">Contents:</span></p>
-<ul>
-<li class="toctree-l1"><a class="reference internal" href="intro.html">Introduction</a></li>
-<li class="toctree-l1"><a class="reference internal" href="components.html">components package</a></li>
-<li class="toctree-l1"><a class="reference internal" href="modules.html">src</a></li>
-</ul>
-
+              <!-- Local TOC -->
+              <div class="local-toc"></div>
         </div>
       </div>
     </nav>
 
     <section data-toggle="wy-nav-shift" class="wy-nav-content-wrap"><nav class="wy-nav-top" aria-label="Mobile navigation menu" >
           <i data-toggle="wy-nav-top" class="fa fa-bars"></i>
           <a href="index.html">sfrout</a>
```

#### html2text {}

```diff
@@ -1,18 +1,14 @@
 
 
 
 
 
 sfrout
 [q                   ]
-Contents:
-    * Introduction
-    * components_package
-    * src
    sfrout
     * Search
 ===============================================================================
 Please activate JavaScript to enable the search functionality.
 
 ===============================================================================
 © Copyright 2023, Lukasz Hoszowski.
```

### Comparing `sfrout-0.0.8/docs/build/html/_modules/index.html` & `sfrout-0.0.9/docs/build/html/genindex.html`

 * *Files 16% similar despite different names*

```diff
@@ -1,84 +1,87 @@
 <!DOCTYPE html>
 <html class="writer-html5" lang="en" >
 <head>
   <meta charset="utf-8" />
   <meta name="viewport" content="width=device-width, initial-scale=1.0" />
-  <title>Overview: module code &mdash; sfrout 0.0.7 documentation</title>
-      <link rel="stylesheet" href="../_static/pygments.css" type="text/css" />
-      <link rel="stylesheet" href="../_static/css/theme.css" type="text/css" />
+  <title>Index &mdash; sfrout 0.0.7 documentation</title>
+      <link rel="stylesheet" href="_static/pygments.css" type="text/css" />
+      <link rel="stylesheet" href="_static/css/theme.css" type="text/css" />
   <!--[if lt IE 9]>
-    <script src="../_static/js/html5shiv.min.js"></script>
+    <script src="_static/js/html5shiv.min.js"></script>
   <![endif]-->
   
-        <script data-url_root="../" id="documentation_options" src="../_static/documentation_options.js"></script>
-        <script src="../_static/doctools.js"></script>
-        <script src="../_static/sphinx_highlight.js"></script>
-    <script src="../_static/js/theme.js"></script>
-    <link rel="index" title="Index" href="../genindex.html" />
-    <link rel="search" title="Search" href="../search.html" /> 
+        <script data-url_root="./" id="documentation_options" src="_static/documentation_options.js"></script>
+        <script src="_static/doctools.js"></script>
+        <script src="_static/sphinx_highlight.js"></script>
+    <script src="_static/js/theme.js"></script>
+    <link rel="index" title="Index" href="#" />
+    <link rel="search" title="Search" href="search.html" /> 
 </head>
 
 <body class="wy-body-for-nav"> 
   <div class="wy-grid-for-nav">
     <nav data-toggle="wy-nav-shift" class="wy-nav-side">
       <div class="wy-side-scroll">
         <div class="wy-side-nav-search" >
 
           
           
-          <a href="../index.html" class="icon icon-home">
+          <a href="index.html" class="icon icon-home">
             sfrout
           </a>
 <div role="search">
-  <form id="rtd-search-form" class="wy-form" action="../search.html" method="get">
+  <form id="rtd-search-form" class="wy-form" action="search.html" method="get">
     <input type="text" name="q" placeholder="Search docs" aria-label="Search docs" />
     <input type="hidden" name="check_keywords" value="yes" />
     <input type="hidden" name="area" value="default" />
   </form>
 </div>
         </div><div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="Navigation menu">
-              <p class="caption" role="heading"><span class="caption-text">Contents:</span></p>
-<ul>
-<li class="toctree-l1"><a class="reference internal" href="../intro.html">Introduction</a></li>
-<li class="toctree-l1"><a class="reference internal" href="../components.html">components package</a></li>
-<li class="toctree-l1"><a class="reference internal" href="../modules.html">src</a></li>
-</ul>
-
+              <!-- Local TOC -->
+              <div class="local-toc"></div>
         </div>
       </div>
     </nav>
 
     <section data-toggle="wy-nav-shift" class="wy-nav-content-wrap"><nav class="wy-nav-top" aria-label="Mobile navigation menu" >
           <i data-toggle="wy-nav-top" class="fa fa-bars"></i>
-          <a href="../index.html">sfrout</a>
+          <a href="index.html">sfrout</a>
       </nav>
 
       <div class="wy-nav-content">
         <div class="rst-content">
           <div role="navigation" aria-label="Page navigation">
   <ul class="wy-breadcrumbs">
-      <li><a href="../index.html" class="icon icon-home" aria-label="Home"></a></li>
-      <li class="breadcrumb-item active">Overview: module code</li>
+      <li><a href="index.html" class="icon icon-home" aria-label="Home"></a></li>
+      <li class="breadcrumb-item active">Index</li>
       <li class="wy-breadcrumbs-aside">
       </li>
   </ul>
   <hr/>
 </div>
           <div role="main" class="document" itemscope="itemscope" itemtype="http://schema.org/Article">
            <div itemprop="articleBody">
              
-  <h1>All modules for which code is available</h1>
-<ul><li><a href="components/config.html">components.config</a></li>
-<li><a href="components/connectors.html">components.connectors</a></li>
-<li><a href="components/containers.html">components.containers</a></li>
-<li><a href="components/exceptions.html">components.exceptions</a></li>
-<li><a href="components/handlers.html">components.handlers</a></li>
-<li><a href="components/loggers.html">components.loggers</a></li>
-</ul>
+
+<h1 id="index">Index</h1>
+
+<div class="genindex-jumpbox">
+ <a href="#R"><strong>R</strong></a>
+ 
+</div>
+<h2 id="R">R</h2>
+<table style="width: 100%" class="indextable genindextable"><tr>
+  <td style="width: 33%; vertical-align: top;"><ul>
+      <li><a href="index.html#main.run">run() (in module main)</a>
+</li>
+  </ul></td>
+</tr></table>
+
+
 
            </div>
           </div>
           <footer>
 
   <hr/>
```

#### html2text {}

```diff
@@ -1,25 +1,18 @@
 
 
 
 
 
 sfrout
 [q                   ]
-Contents:
-    * Introduction
-    * components_package
-    * src
    sfrout
-    * Overview: module code
+    * Index
 ===============================================================================
-****** All modules for which code is available ******
-    * components.config
-    * components.connectors
-    * components.containers
-    * components.exceptions
-    * components.handlers
-    * components.loggers
+****** Index ******
+R
+***** R *****
+    * run()_(in_module_main)
 
 ===============================================================================
 © Copyright 2023, Lukasz Hoszowski.
 Built with Sphinx using a theme provided by Read_the_Docs.
```

### Comparing `sfrout-0.0.8/docs/build/html/_modules/components/connectors.html` & `sfrout-0.0.9/docs/build/html/_modules/components/connectors.html`

 * *Files 1% similar despite different names*

```diff
@@ -33,21 +33,16 @@
   <form id="rtd-search-form" class="wy-form" action="../../search.html" method="get">
     <input type="text" name="q" placeholder="Search docs" aria-label="Search docs" />
     <input type="hidden" name="check_keywords" value="yes" />
     <input type="hidden" name="area" value="default" />
   </form>
 </div>
         </div><div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="Navigation menu">
-              <p class="caption" role="heading"><span class="caption-text">Contents:</span></p>
-<ul>
-<li class="toctree-l1"><a class="reference internal" href="../../intro.html">Introduction</a></li>
-<li class="toctree-l1"><a class="reference internal" href="../../components.html">components package</a></li>
-<li class="toctree-l1"><a class="reference internal" href="../../modules.html">src</a></li>
-</ul>
-
+              <!-- Local TOC -->
+              <div class="local-toc"></div>
         </div>
       </div>
     </nav>
 
     <section data-toggle="wy-nav-shift" class="wy-nav-content-wrap"><nav class="wy-nav-top" aria-label="Mobile navigation menu" >
           <i data-toggle="wy-nav-top" class="fa fa-bars"></i>
           <a href="../../index.html">sfrout</a>
@@ -84,15 +79,15 @@
 
 <span class="kn">from</span> <span class="nn">.containers</span> <span class="kn">import</span> <span class="n">ReportProtocol</span>
 
 
 <span class="n">logger_main</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="vm">__name__</span><span class="p">)</span>
 
 
-<div class="viewcode-block" id="Connector"><a class="viewcode-back" href="../../components.html#components.connectors.Connector">[docs]</a><span class="nd">@runtime_checkable</span>
+<span class="nd">@runtime_checkable</span>
 <span class="k">class</span> <span class="nc">Connector</span><span class="p">(</span><span class="n">Protocol</span><span class="p">):</span>
 <span class="w">    </span><span class="sd">&quot;&quot;&quot;Protocol class for connector object.</span>
 
 <span class="sd">    :param queue: Shared queue object.</span>
 <span class="sd">    :type queue: Queue</span>
 <span class="sd">    :param timeout: Request&#39;s timeout value in seconds.</span>
 <span class="sd">    :type timeout: int</span>
@@ -100,34 +95,34 @@
 <span class="sd">    :type headers: dict[str, str]</span>
 <span class="sd">    &quot;&quot;&quot;</span>
 
     <span class="n">queue</span><span class="p">:</span> <span class="n">Queue</span>
     <span class="n">timeout</span><span class="p">:</span> <span class="nb">int</span>
     <span class="n">headers</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span>
 
-<div class="viewcode-block" id="Connector.check_connection"><a class="viewcode-back" href="../../components.html#components.connectors.Connector.check_connection">[docs]</a>    <span class="k">def</span> <span class="nf">check_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
+    <span class="k">def</span> <span class="nf">check_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
 <span class="w">        </span><span class="sd">&quot;&quot;&quot;Checks connection with given domain.</span>
 
 <span class="sd">        :return: Flag, True if connection is established, False otherwise.</span>
 <span class="sd">        :rtype: bool</span>
 <span class="sd">        &quot;&quot;&quot;</span>
-        <span class="o">...</span></div>
+        <span class="o">...</span>
 
-<div class="viewcode-block" id="Connector.report_gathering"><a class="viewcode-back" href="../../components.html#components.connectors.Connector.report_gathering">[docs]</a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">report_gathering</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reports</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ReportProtocol</span><span class="p">],</span> <span class="n">session</span><span class="p">:</span> <span class="n">aiohttp</span><span class="o">.</span><span class="n">ClientSession</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
+    <span class="k">async</span> <span class="k">def</span> <span class="nf">report_gathering</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reports</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ReportProtocol</span><span class="p">],</span> <span class="n">session</span><span class="p">:</span> <span class="n">aiohttp</span><span class="o">.</span><span class="n">ClientSession</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
 <span class="w">        </span><span class="sd">&quot;&quot;&quot;Collects asynchronous responses from the servers.</span>
 
 <span class="sd">        :param reports: Collection of ReportProtocol objects.</span>
 <span class="sd">        :type reports: list[ReportProt]</span>
 <span class="sd">        :param session: HTTP client session object to handle request in transaction.</span>
 <span class="sd">        :type session: aiohttp.ClientSession</span>
 <span class="sd">        &quot;&quot;&quot;</span>
-        <span class="o">...</span></div></div>
+        <span class="o">...</span>
 
 
-<div class="viewcode-block" id="SfdcConnector"><a class="viewcode-back" href="../../components.html#components.connectors.SfdcConnector">[docs]</a><span class="k">class</span> <span class="nc">SfdcConnector</span><span class="p">():</span>
+<div class="viewcode-block" id="SfdcConnector"><a class="viewcode-back" href="../../index.html#components.connectors.SfdcConnector">[docs]</a><span class="k">class</span> <span class="nc">SfdcConnector</span><span class="p">():</span>
 <span class="w">    </span><span class="sd">&quot;&quot;&quot;Concrete class representing Connector object for SFDC</span>
 
 <span class="sd">    :param queue: Shared queue object.</span>
 <span class="sd">    :type queue: Queue</span>
 <span class="sd">    :param verbose: CLI parameter used as switch between progress bar and logging to stdout on INFO level. Defaults to False.</span>
 <span class="sd">    :type timeout: int</span>
 <span class="sd">    :param timeout: Request&#39;s timeout value in seconds. Defaults to 900.</span>
@@ -255,15 +250,15 @@
             <span class="n">logger_main</span><span class="o">.</span><span class="n">critical</span><span class="p">(</span><span class="s1">&#39;SID not ok!!!&#39;</span><span class="p">)</span>
             <span class="bp">self</span><span class="o">.</span><span class="n">sid</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span>
             <span class="bp">self</span><span class="o">.</span><span class="n">sid_valid</span> <span class="o">=</span> <span class="kc">False</span>
             <span class="bp">self</span><span class="o">.</span><span class="n">check</span> <span class="o">=</span> <span class="kc">False</span>
 
             <span class="k">return</span> <span class="kc">False</span>
           
-<div class="viewcode-block" id="SfdcConnector.check_connection"><a class="viewcode-back" href="../../components.html#components.connectors.SfdcConnector.check_connection">[docs]</a>    <span class="k">def</span> <span class="nf">check_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
+<div class="viewcode-block" id="SfdcConnector.check_connection"><a class="viewcode-back" href="../../index.html#components.connectors.SfdcConnector.check_connection">[docs]</a>    <span class="k">def</span> <span class="nf">check_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
 <span class="w">        </span><span class="sd">&quot;&quot;&quot;Checks the connection with given domain.</span>
 
 <span class="sd">        :return: Flag, True if connection was successful, False wasn&#39;t.</span>
 <span class="sd">        :rtype: bool</span>
 <span class="sd">        &quot;&quot;&quot;</span>
         <span class="bp">self</span><span class="o">.</span><span class="n">_parse_headers</span><span class="p">()</span>
         
@@ -394,15 +389,15 @@
 
         <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_toggle_progress_bar</span><span class="p">(</span><span class="n">tasks</span><span class="p">)</span>
 
         <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span><span class="o">*</span><span class="n">tasks</span><span class="p">)</span>
 
         <span class="k">return</span> <span class="kc">None</span>
 
-<div class="viewcode-block" id="SfdcConnector.handle_requests"><a class="viewcode-back" href="../../components.html#components.connectors.SfdcConnector.handle_requests">[docs]</a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">handle_requests</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reports</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ReportProtocol</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
+<div class="viewcode-block" id="SfdcConnector.handle_requests"><a class="viewcode-back" href="../../index.html#components.connectors.SfdcConnector.handle_requests">[docs]</a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">handle_requests</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reports</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ReportProtocol</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
 <span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates session and process asynchronous tasks.</span>
 
 <span class="sd">        :param reports: Collection of `ReportProtocol` instances.</span>
 <span class="sd">        :type reports: list[ReportProtocol]</span>
 <span class="sd">        &quot;&quot;&quot;</span>
 
         <span class="n">logger_main</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">&quot;Awaiting responses&quot;</span><span class="p">)</span>
```

#### html2text {}

```diff
@@ -1,18 +1,14 @@
 
 
 
 
 
 sfrout
 [q                   ]
-Contents:
-    * Introduction
-    * components_package
-    * src
    sfrout
     * Module_code
     * components.connectors
 ===============================================================================
 ****** Source code for components.connectors ******
 import logging
 import asyncio
@@ -29,15 +25,15 @@
 
 from .containers import ReportProtocol
 
 
 logger_main = logging.getLogger(__name__)
 
 
-[docs]@runtime_checkable
+@runtime_checkable
 class Connector(Protocol):
     """Protocol class for connector object.
 
     :param queue: Shared queue object.
     :type queue: Queue
     :param timeout: Request's timeout value in seconds.
     :type timeout: int
@@ -45,37 +41,35 @@
     :type headers: dict[str, str]
     """
 
     queue: Queue
     timeout: int
     headers: dict[str, str]
 
-[docs]    def check_connection(self) -> bool:
+    def check_connection(self) -> bool:
         """Checks connection with given domain.
 
         :return: Flag, True if connection is established, False otherwise.
         :rtype: bool
         """
         ...
 
-
-[docs]    async def report_gathering(self, reports: list[ReportProtocol],
-session: aiohttp.ClientSession) -> None:
+    async def report_gathering(self, reports: list[ReportProtocol], session:
+aiohttp.ClientSession) -> None:
         """Collects asynchronous responses from the servers.
 
         :param reports: Collection of ReportProtocol objects.
         :type reports: list[ReportProt]
         :param session: HTTP client session object to handle request in
 transaction.
         :type session: aiohttp.ClientSession
         """
         ...
 
 
-
 [docs]class SfdcConnector():
     """Concrete class representing Connector object for SFDC
 
     :param queue: Shared queue object.
     :type queue: Queue
     :param verbose: CLI parameter used as switch between progress bar and
 logging to stdout on INFO level. Defaults to False.
```

### Comparing `sfrout-0.0.8/docs/build/html/_static/basic.css` & `sfrout-0.0.9/docs/build/html/_static/basic.css`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/doctools.js` & `sfrout-0.0.9/docs/build/html/_static/doctools.js`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/language_data.js` & `sfrout-0.0.9/docs/build/html/_static/language_data.js`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/pygments.css` & `sfrout-0.0.9/docs/build/html/_static/pygments.css`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/searchtools.js` & `sfrout-0.0.9/docs/build/html/_static/searchtools.js`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/sphinx_highlight.js` & `sfrout-0.0.9/docs/build/html/_static/sphinx_highlight.js`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/badge_only.css` & `sfrout-0.0.9/docs/build/html/_static/css/badge_only.css`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/theme.css` & `sfrout-0.0.9/docs/build/html/_static/css/theme.css`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff2` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff2`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff2` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff2`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.eot` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.eot`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.svg` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.svg`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.ttf` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.ttf`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.woff` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.woff`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.woff2` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.woff2`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-bold-italic.woff` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-bold-italic.woff`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-bold-italic.woff2` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-bold-italic.woff2`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-bold.woff` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-bold.woff`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-bold.woff2` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-bold.woff2`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-normal-italic.woff` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-normal-italic.woff`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-normal-italic.woff2` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-normal-italic.woff2`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-normal.woff` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-normal.woff`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/css/fonts/lato-normal.woff2` & `sfrout-0.0.9/docs/build/html/_static/css/fonts/lato-normal.woff2`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/js/badge_only.js` & `sfrout-0.0.9/docs/build/html/_static/js/badge_only.js`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/js/html5shiv-printshiv.min.js` & `sfrout-0.0.9/docs/build/html/_static/js/html5shiv-printshiv.min.js`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/js/html5shiv.min.js` & `sfrout-0.0.9/docs/build/html/_static/js/html5shiv.min.js`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/build/html/_static/js/theme.js` & `sfrout-0.0.9/docs/build/html/_static/js/theme.js`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/docs/source/conf.py` & `sfrout-0.0.9/docs/source/conf.py`

 * *Files 4% similar despite different names*

```diff
@@ -16,15 +16,17 @@
 release = '0.0.7'
 
 # -- General configuration ---------------------------------------------------
 # https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
 
 extensions = ['sphinx.ext.autodoc',
               'sphinx.ext.viewcode',
-              'sphinx.ext.napoleon']
+              'sphinx.ext.napoleon',
+              'sphinx.ext.duration',
+              'sphinx.ext.coverage']
 
 templates_path = ['_templates']
 exclude_patterns = []
 
 
 
 # -- Options for HTML output -------------------------------------------------
```

### Comparing `sfrout-0.0.8/src/sfrout/app/cli.py` & `sfrout-0.0.9/src/sfrout/app/cli.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 #!/usr/bin/env python3.11
 
 import click
-from ..app.main import run
+from main import run
 
 
 CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
 
 
 @click.command(context_settings=CONTEXT_SETTINGS)
 @click.argument('domain', type=click.STRING)
```

### Comparing `sfrout-0.0.8/src/sfrout/app/main.py` & `sfrout-0.0.9/src/sfrout/main.py`

 * *Files 13% similar despite different names*

```diff
@@ -8,19 +8,19 @@
 
 import time
 import asyncio
 import logging
 
 from queue import Queue
 
-from ..components.connectors import SfdcConnector
-from ..components.containers import ReportsContainer
-from ..components.handlers import WorkerFactory
-from ..components.config import Config
-from ..components.loggers import logger_configurer
+from components.connectors import SfdcConnector
+from components.containers import ReportsContainer
+from components.handlers import WorkerFactory
+from components.config import Config
+from components.loggers import logger_configurer
 
 
 def run(*,
         domain: str, 
         reports_path: str, 
         reports_list: list[dict[str, str]]=[],
         summary_filepath: str="",
@@ -34,29 +34,29 @@
         ) -> None:
     """Main function of the program.
 
     :param domain: SalesForce domain of your organization -> "https://corp.my.salesforce.com/"
     :type domain: str    
     :param reports_path: Path to reports.csv file, template -> https://github.com/LukaszHoszowski/sfrout/blob/main/example/reports-default.csv
     :type reports_path: str
-    :param reports_list: List of the reports as dictionaries -> [{'name': 'RaportName', 'id': '00O1V00000999GHES', 'path': WindowsPath('C:/downloads')}
+    :param reports_list: List of the reports as dictionaries -> ``[{'name': 'RaportName', 'id': '00O1V00000999GHES', 'path': WindowsPath('C:/downloads')}]``
     :type reports_list: list[dict[str, str]]
-    :param summary_filepath: File path to summary report -> 'C:/downloads/summary.csv'
+    :param summary_filepath: File path to summary report -> ``C:/downloads/summary.csv``
     :type summary_filepath: str
-    :param log_path: Path to log file -> 'C:/downloads/logs/'
+    :param log_path: Path to log file -> ``C:/downloads/logs/``
     :type log_path: str
-    :param report: Single report mode -> 'RaportName,00O1V00000999GHES,C:/downloads'
+    :param report: Single report mode -> ``RaportName,00O1V00000999GHES,C:/downloads``
     :type report: str
-    :param path: Save location path override -> 'C:/new_downloads'
+    :param path: Save location path override -> ``C:/new_downloads``
     :type path: str
-    :param threads: Number of threads to use. (Default: half of available threads of the machine) 
+    :param threads: Number of threads to use. (Default: ``half of available threads of the machine``) 
     :type threads: int
-    :param stdout_loglevel: Log level for stdout logging -> ['critical'|'error'|'warn'|'warning'|'info'|'debug'] (Default: ``WARNING``)
+    :param stdout_loglevel: Log level for stdout logging -> ``['critical'|'error'|'warn'|'warning'|'info'|'debug']`` (Default: ``WARNING``)
     :type stdout_loglevel: str
-    :param file_loglevel: Log level for file logging -> ['critical'|'error'|'warn'|'warning'|'info'|'debug'] (Default: ``WARNING``)
+    :param file_loglevel: Log level for file logging -> ``['critical'|'error'|'warn'|'warning'|'info'|'debug']`` (Default: ``WARNING``)
     :type file_loglevel: str 
     :param verbose: Toggles between Progress Bar and stdout logging (Default: ``False``)
     :type verbose: bool
     """
 
     t0 = time.time()
```

### Comparing `sfrout-0.0.8/src/sfrout/components/config.py` & `sfrout-0.0.9/src/sfrout/components/config.py`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/src/sfrout/components/connectors.py` & `sfrout-0.0.9/src/sfrout/components/connectors.py`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/src/sfrout/components/containers.py` & `sfrout-0.0.9/src/sfrout/components/containers.py`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/src/sfrout/components/exceptions.py` & `sfrout-0.0.9/src/sfrout/components/exceptions.py`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/src/sfrout/components/handlers.py` & `sfrout-0.0.9/src/sfrout/components/handlers.py`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/src/sfrout/components/loggers.py` & `sfrout-0.0.9/src/sfrout/components/loggers.py`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/tests/conftest.py` & `sfrout-0.0.9/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/tests/test_config.py` & `sfrout-0.0.9/tests/test_config.py`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/tests/test_connector.py` & `sfrout-0.0.9/tests/test_connector.py`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/tests/test_container.py` & `sfrout-0.0.9/tests/test_container.py`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/LICENSE.md` & `sfrout-0.0.9/LICENSE.md`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/README.md` & `sfrout-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `sfrout-0.0.8/pyproject.toml` & `sfrout-0.0.9/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "sfrout"
-version = "0.0.8"
+version = "0.0.9"
 authors = [
   {name="Lukasz Hoszowski", email="lukasz.hoszowski@mail.com"},
 ]
 description = "Scalable, asynchronious SalesForce (SFDC) report downloader for SSO/SAML clients"
 readme = "README.md"
 requires-python = ">=3.11"
 classifiers = [
```

### Comparing `sfrout-0.0.8/PKG-INFO` & `sfrout-0.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sfrout
-Version: 0.0.8
+Version: 0.0.9
 Summary: Scalable, asynchronious SalesForce (SFDC) report downloader for SSO/SAML clients
 Project-URL: Homepage, https://github.com/LukaszHoszowski/sfrout
 Project-URL: Bug Tracker, https://github.com/LukaszHoszowski/sfrout/issues
 Author-email: Lukasz Hoszowski <lukasz.hoszowski@mail.com>
 License-File: LICENSE.md
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: End Users/Desktop
```

