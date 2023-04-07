# Comparing `tmp/firebase-rest-api-1.8.0.tar.gz` & `tmp/firebase-rest-api-1.8.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "firebase-rest-api-1.8.0.tar", last modified: Mon Aug 15 19:00:16 2022, max compression
+gzip compressed data, was "firebase-rest-api-1.8.1.tar", last modified: Wed Feb  8 19:58:19 2023, max compression
```

## Comparing `firebase-rest-api-1.8.0.tar` & `firebase-rest-api-1.8.1.tar`

### file list

```diff
@@ -1,61 +1,61 @@
--rw-r--r--   0        0        0       66 2022-08-15 19:00:11.282089 firebase-rest-api-1.8.0/.gitattributes
--rw-r--r--   0        0        0     2759 2022-08-15 19:00:11.282089 firebase-rest-api-1.8.0/.github/ISSUE_TEMPLATE/bug-report.yml
--rw-r--r--   0        0        0      363 2022-08-15 19:00:11.282089 firebase-rest-api-1.8.0/.github/ISSUE_TEMPLATE/config.yml
--rw-r--r--   0        0        0     1238 2022-08-15 19:00:11.282089 firebase-rest-api-1.8.0/.github/ISSUE_TEMPLATE/docs.yml
--rw-r--r--   0        0        0     1698 2022-08-15 19:00:11.282089 firebase-rest-api-1.8.0/.github/ISSUE_TEMPLATE/feature-request.yml
--rw-r--r--   0        0        0      762 2022-08-15 19:00:11.282089 firebase-rest-api-1.8.0/.github/ISSUE_TEMPLATE/others.yml
--rw-r--r--   0        0        0     1489 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/.github/workflows/build.yml
--rw-r--r--   0        0        0      940 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/.github/workflows/greetings.yml
--rw-r--r--   0        0        0      598 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/.github/workflows/publish.yml
--rw-r--r--   0        0        0     1389 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/.github/workflows/release.yml
--rw-r--r--   0        0        0     3929 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/.github/workflows/tests.yml
--rw-r--r--   0        0        0     2762 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/.gitignore
--rw-r--r--   0        0        0      710 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/.readthedocs.yaml
--rw-r--r--   0        0        0     6359 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/CHANGELOG.md
--rw-r--r--   0        0        0     1074 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/LICENSE
--rw-r--r--   0        0        0     2551 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/README.md
--rw-r--r--   0        0        0      409 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/_static/css/my-styles.css
--rw-r--r--   0        0        0     2907 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/conf.py
--rw-r--r--   0        0        0      129 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/firebase/firebase.auth.rst
--rw-r--r--   0        0        0      141 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/firebase/firebase.database.rst
--rw-r--r--   0        0        0      144 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/firebase/firebase.firestore.rst
--rw-r--r--   0        0        0       98 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/firebase/firebase.rst
--rw-r--r--   0        0        0      138 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/firebase/firebase.storage.rst
--rw-r--r--   0        0        0      151 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/firebase/modules.rst
--rw-r--r--   0        0        0     7614 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/guide/authentication.rst
--rw-r--r--   0        0        0     8518 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/guide/database.rst
--rw-r--r--   0        0        0     3706 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/guide/firebase-rest-api.rst
--rw-r--r--   0        0        0    10444 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/guide/firestore.rst
--rw-r--r--   0        0        0     3488 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/guide/setup.rst
--rw-r--r--   0        0        0     2097 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/guide/storage.rst
--rw-r--r--   0        0        0     2422 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/index.rst
--rw-r--r--   0        0        0       72 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/docs/requirements.txt
--rw-r--r--   0        0        0     2544 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/__init__.py
--rw-r--r--   0        0        0      975 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/_custom_requests.py
--rw-r--r--   0        0        0      536 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/_exception.py
--rw-r--r--   0        0        0     1305 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/_service_account_credentials.py
--rw-r--r--   0        0        0    19967 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/auth/__init__.py
--rw-r--r--   0        0        0    19916 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/database/__init__.py
--rw-r--r--   0        0        0      737 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/database/_closable_sse_client.py
--rw-r--r--   0        0        0     4723 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/database/_custom_sse_client.py
--rw-r--r--   0        0        0     1562 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/database/_db_convert.py
--rw-r--r--   0        0        0      429 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/database/_keep_auth_session.py
--rw-r--r--   0        0        0     1472 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/database/_stream.py
--rw-r--r--   0        0        0    19967 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/firestore/__init__.py
--rw-r--r--   0        0        0     5023 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/firestore/_utils.py
--rw-r--r--   0        0        0     6915 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/firebase/storage/__init__.py
--rw-r--r--   0        0        0     1713 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/pyproject.toml
--rw-r--r--   0        0        0      136 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/requirements.txt
--rw-r--r--   0        0        0      219 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/tests/__init__.py
--rw-r--r--   0        0        0     1841 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/tests/config.py
--rw-r--r--   0        0        0      678 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/tests/config.template.py
--rw-r--r--   0        0        0     1310 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/tests/conftest.py
--rw-r--r--   0        0        0      140 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/tests/requirements.txt
--rw-r--r--   0        0        0     3686 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/tests/static/test-file.txt
--rw-r--r--   0        0        0     6446 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/tests/test_auth.py
--rw-r--r--   0        0        0     4800 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/tests/test_database.py
--rw-r--r--   0        0        0    20410 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/tests/test_firestore.py
--rw-r--r--   0        0        0     1156 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/tests/test_setup.py
--rw-r--r--   0        0        0     2372 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/tests/test_storage.py
--rw-r--r--   0        0        0     1030 2022-08-15 19:00:11.286089 firebase-rest-api-1.8.0/tests/tools.py
--rw-r--r--   0        0        0     4404 1970-01-01 00:00:00.000000 firebase-rest-api-1.8.0/PKG-INFO
+-rw-r--r--   0        0        0       66 2023-02-08 19:58:13.362050 firebase-rest-api-1.8.1/.gitattributes
+-rw-r--r--   0        0        0     2759 2023-02-08 19:58:13.362050 firebase-rest-api-1.8.1/.github/ISSUE_TEMPLATE/bug-report.yml
+-rw-r--r--   0        0        0      363 2023-02-08 19:58:13.362050 firebase-rest-api-1.8.1/.github/ISSUE_TEMPLATE/config.yml
+-rw-r--r--   0        0        0     1238 2023-02-08 19:58:13.362050 firebase-rest-api-1.8.1/.github/ISSUE_TEMPLATE/docs.yml
+-rw-r--r--   0        0        0     1698 2023-02-08 19:58:13.362050 firebase-rest-api-1.8.1/.github/ISSUE_TEMPLATE/feature-request.yml
+-rw-r--r--   0        0        0      762 2023-02-08 19:58:13.362050 firebase-rest-api-1.8.1/.github/ISSUE_TEMPLATE/others.yml
+-rw-r--r--   0        0        0     1490 2023-02-08 19:58:13.362050 firebase-rest-api-1.8.1/.github/workflows/build.yml
+-rw-r--r--   0        0        0      940 2023-02-08 19:58:13.362050 firebase-rest-api-1.8.1/.github/workflows/greetings.yml
+-rw-r--r--   0        0        0      598 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/.github/workflows/publish.yml
+-rw-r--r--   0        0        0     1389 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/.github/workflows/release.yml
+-rw-r--r--   0        0        0     3929 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/.github/workflows/tests.yml
+-rw-r--r--   0        0        0     2762 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/.gitignore
+-rw-r--r--   0        0        0      710 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/.readthedocs.yaml
+-rw-r--r--   0        0        0     6725 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/CHANGELOG.md
+-rw-r--r--   0        0        0     1074 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/LICENSE
+-rw-r--r--   0        0        0     3260 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/README.md
+-rw-r--r--   0        0        0      409 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/_static/css/my-styles.css
+-rw-r--r--   0        0        0     2907 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/conf.py
+-rw-r--r--   0        0        0      129 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/firebase/firebase.auth.rst
+-rw-r--r--   0        0        0      141 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/firebase/firebase.database.rst
+-rw-r--r--   0        0        0      144 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/firebase/firebase.firestore.rst
+-rw-r--r--   0        0        0       98 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/firebase/firebase.rst
+-rw-r--r--   0        0        0      138 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/firebase/firebase.storage.rst
+-rw-r--r--   0        0        0      151 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/firebase/modules.rst
+-rw-r--r--   0        0        0     7614 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/guide/authentication.rst
+-rw-r--r--   0        0        0     8518 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/guide/database.rst
+-rw-r--r--   0        0        0     3706 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/guide/firebase-rest-api.rst
+-rw-r--r--   0        0        0    10444 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/guide/firestore.rst
+-rw-r--r--   0        0        0     3488 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/guide/setup.rst
+-rw-r--r--   0        0        0     2097 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/guide/storage.rst
+-rw-r--r--   0        0        0     2422 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/index.rst
+-rw-r--r--   0        0        0       72 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/docs/requirements.txt
+-rw-r--r--   0        0        0     2544 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/__init__.py
+-rw-r--r--   0        0        0      975 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/_custom_requests.py
+-rw-r--r--   0        0        0      536 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/_exception.py
+-rw-r--r--   0        0        0     1305 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/_service_account_credentials.py
+-rw-r--r--   0        0        0    19967 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/auth/__init__.py
+-rw-r--r--   0        0        0    19916 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/database/__init__.py
+-rw-r--r--   0        0        0      737 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/database/_closable_sse_client.py
+-rw-r--r--   0        0        0     4723 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/database/_custom_sse_client.py
+-rw-r--r--   0        0        0     1562 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/database/_db_convert.py
+-rw-r--r--   0        0        0      429 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/database/_keep_auth_session.py
+-rw-r--r--   0        0        0     1472 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/database/_stream.py
+-rw-r--r--   0        0        0    19967 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/firestore/__init__.py
+-rw-r--r--   0        0        0     5082 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/firestore/_utils.py
+-rw-r--r--   0        0        0     6915 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/firebase/storage/__init__.py
+-rw-r--r--   0        0        0     1713 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/pyproject.toml
+-rw-r--r--   0        0        0      136 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/requirements.txt
+-rw-r--r--   0        0        0      219 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/tests/__init__.py
+-rw-r--r--   0        0        0     1841 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/tests/config.py
+-rw-r--r--   0        0        0      678 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/tests/config.template.py
+-rw-r--r--   0        0        0     1310 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/tests/conftest.py
+-rw-r--r--   0        0        0      140 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/tests/requirements.txt
+-rw-r--r--   0        0        0     3686 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/tests/static/test-file.txt
+-rw-r--r--   0        0        0     6446 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/tests/test_auth.py
+-rw-r--r--   0        0        0     4800 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/tests/test_database.py
+-rw-r--r--   0        0        0    20429 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/tests/test_firestore.py
+-rw-r--r--   0        0        0     1156 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/tests/test_setup.py
+-rw-r--r--   0        0        0     2372 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/tests/test_storage.py
+-rw-r--r--   0        0        0     1030 2023-02-08 19:58:13.366050 firebase-rest-api-1.8.1/tests/tools.py
+-rw-r--r--   0        0        0     5113 1970-01-01 00:00:00.000000 firebase-rest-api-1.8.1/PKG-INFO
```

### Comparing `firebase-rest-api-1.8.0/.github/ISSUE_TEMPLATE/bug-report.yml` & `firebase-rest-api-1.8.1/.github/ISSUE_TEMPLATE/bug-report.yml`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/.github/ISSUE_TEMPLATE/docs.yml` & `firebase-rest-api-1.8.1/.github/ISSUE_TEMPLATE/docs.yml`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/.github/ISSUE_TEMPLATE/feature-request.yml` & `firebase-rest-api-1.8.1/.github/ISSUE_TEMPLATE/feature-request.yml`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/.github/ISSUE_TEMPLATE/others.yml` & `firebase-rest-api-1.8.1/.github/ISSUE_TEMPLATE/others.yml`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/.github/workflows/build.yml` & `firebase-rest-api-1.8.1/.github/workflows/build.yml`

 * *Files 1% similar despite different names*

```diff
@@ -21,15 +21,15 @@
     # This workflow contains a single job called "build"
     build:
 
         # The type of runner that the job will run on
         runs-on: ${{ matrix.os }}
         strategy:
             matrix:
-                python-version: [ "3.6", "3.7", "3.8", "3.9", "3.10" ]
+                python-version: [ "3.7", "3.8", "3.9", "3.10", "3.11" ]
                 os: [ macos-latest, ubuntu-latest, windows-latest ]
 
         # Steps represent a sequence of tasks that will be executed as part of the job
         steps:
 
             # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
             -   uses: actions/checkout@v3
```

### Comparing `firebase-rest-api-1.8.0/.github/workflows/greetings.yml` & `firebase-rest-api-1.8.1/.github/workflows/greetings.yml`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/.github/workflows/publish.yml` & `firebase-rest-api-1.8.1/.github/workflows/publish.yml`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/.github/workflows/release.yml` & `firebase-rest-api-1.8.1/.github/workflows/release.yml`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/.github/workflows/tests.yml` & `firebase-rest-api-1.8.1/.github/workflows/tests.yml`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/.gitignore` & `firebase-rest-api-1.8.1/.gitignore`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/.readthedocs.yaml` & `firebase-rest-api-1.8.1/.readthedocs.yaml`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/CHANGELOG.md` & `firebase-rest-api-1.8.1/CHANGELOG.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,7 +1,16 @@
+## [1.8.1](https://github.com/AsifArmanRahman/firebase-rest-api/compare/v1.8.0...v1.8.1) (2023-02-08)
+
+
+### Bug Fixes
+
+* unsupported type error thrown for empty array field ([63cce77](https://github.com/AsifArmanRahman/firebase-rest-api/commit/63cce77420a999f0e151a32c8e389593b84dc357)), closes [#7](https://github.com/AsifArmanRahman/firebase-rest-api/issues/7)
+
+
+
 # [1.8.0](https://github.com/AsifArmanRahman/firebase-rest-api/compare/v1.7.0...v1.8.0) (2022-08-15)
 
 
 ### Features
 
 * **auth:** sign in with facebook ([0bcead3](https://github.com/AsifArmanRahman/firebase-rest-api/commit/0bcead336128195932120c371be70f0afd5595ae))
 * **firestore:** add list_of_documents() method ([04c8e20](https://github.com/AsifArmanRahman/firebase-rest-api/commit/04c8e20b98693e4e285266a571f7fcd9b7c10c4e))
```

### Comparing `firebase-rest-api-1.8.0/LICENSE` & `firebase-rest-api-1.8.1/LICENSE`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/docs/conf.py` & `firebase-rest-api-1.8.1/docs/conf.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/docs/guide/authentication.rst` & `firebase-rest-api-1.8.1/docs/guide/authentication.rst`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/docs/guide/database.rst` & `firebase-rest-api-1.8.1/docs/guide/database.rst`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/docs/guide/firebase-rest-api.rst` & `firebase-rest-api-1.8.1/docs/guide/firebase-rest-api.rst`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/docs/guide/firestore.rst` & `firebase-rest-api-1.8.1/docs/guide/firestore.rst`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/docs/guide/setup.rst` & `firebase-rest-api-1.8.1/docs/guide/setup.rst`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/docs/guide/storage.rst` & `firebase-rest-api-1.8.1/docs/guide/storage.rst`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/docs/index.rst` & `firebase-rest-api-1.8.1/docs/index.rst`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/firebase/__init__.py` & `firebase-rest-api-1.8.1/firebase/__init__.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/firebase/_custom_requests.py` & `firebase-rest-api-1.8.1/firebase/_custom_requests.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/firebase/_exception.py` & `firebase-rest-api-1.8.1/firebase/_exception.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/firebase/_service_account_credentials.py` & `firebase-rest-api-1.8.1/firebase/_service_account_credentials.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/firebase/auth/__init__.py` & `firebase-rest-api-1.8.1/firebase/auth/__init__.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/firebase/database/__init__.py` & `firebase-rest-api-1.8.1/firebase/database/__init__.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/firebase/database/_closable_sse_client.py` & `firebase-rest-api-1.8.1/firebase/database/_closable_sse_client.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/firebase/database/_custom_sse_client.py` & `firebase-rest-api-1.8.1/firebase/database/_custom_sse_client.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/firebase/database/_db_convert.py` & `firebase-rest-api-1.8.1/firebase/database/_db_convert.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/firebase/database/_stream.py` & `firebase-rest-api-1.8.1/firebase/database/_stream.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/firebase/firestore/__init__.py` & `firebase-rest-api-1.8.1/firebase/firestore/__init__.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/firebase/firestore/_utils.py` & `firebase-rest-api-1.8.1/firebase/firestore/_utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -28,19 +28,20 @@
 	data_to_restructure = data['fields']
 
 	for key, val in data_to_restructure.items():
 
 		if val.get('mapValue'):
 			data_to_restructure[key] = _from_datastore(val['mapValue'])
 
-		elif val.get('arrayValue'):
+		elif isinstance(val.get('arrayValue'), dict):
 			arr = []
 
-			for x in val['arrayValue']['values']:
-				arr.append(_decode_datastore(x))
+			if val['arrayValue'].get('values'):
+				for x in val['arrayValue']['values']:
+					arr.append(_decode_datastore(x))
 
 			data_to_restructure[key] = arr
 
 		else:
 			data_to_restructure[key] = _decode_datastore(val)
 
 	return data_to_restructure
```

### Comparing `firebase-rest-api-1.8.0/firebase/storage/__init__.py` & `firebase-rest-api-1.8.1/firebase/storage/__init__.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/pyproject.toml` & `firebase-rest-api-1.8.1/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ['flit_core >=3.2,<4']
 build-backend = 'flit_core.buildapi'
 
 [project]
 name = "firebase-rest-api"
-version = "1.8.0"
+version = "1.8.1"
 readme = "README.md"
 description = "A simple python wrapper for Google's Firebase REST API's."
 requires-python = ">=3.6"
 keywords = [
   "firebase",
   "firebase-auth",
   "firebase-database",
```

### Comparing `firebase-rest-api-1.8.0/tests/config.py` & `firebase-rest-api-1.8.1/tests/config.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/tests/config.template.py` & `firebase-rest-api-1.8.1/tests/config.template.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/tests/conftest.py` & `firebase-rest-api-1.8.1/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/tests/static/test-file.txt` & `firebase-rest-api-1.8.1/tests/static/test-file.txt`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/tests/test_auth.py` & `firebase-rest-api-1.8.1/tests/test_auth.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/tests/test_database.py` & `firebase-rest-api-1.8.1/tests/test_database.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/tests/test_firestore.py` & `firebase-rest-api-1.8.1/tests/test_firestore.py`

 * *Files 0% similar despite different names*

```diff
@@ -101,15 +101,16 @@
 	movies1 = {
 		'name': 'Dr. Strange',
 		'lead': {'name': 'Benedict Cumberbatch'},
 		'released': False,
 		'year': 2016,
 		'rating': 7.5,
 		'prequel': None,
-		'cast': ['Tilda Swinton', 'Rachel McAdams', 'Mads Mikkelsen', 'Chiwetel Ejiofor', 'Benedict Wong']
+		'cast': ['Tilda Swinton', 'Rachel McAdams', 'Mads Mikkelsen', 'Chiwetel Ejiofor', 'Benedict Wong'],
+		'producers': []
 	}
 
 	movies2 = {
 		'name': 'Black Panther',
 		'lead': {'name': 'Chadwick Boseman'},
 		'released': False,
 		'year': 2018,
```

### Comparing `firebase-rest-api-1.8.0/tests/test_setup.py` & `firebase-rest-api-1.8.1/tests/test_setup.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/tests/test_storage.py` & `firebase-rest-api-1.8.1/tests/test_storage.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/tests/tools.py` & `firebase-rest-api-1.8.1/tests/tools.py`

 * *Files identical despite different names*

### Comparing `firebase-rest-api-1.8.0/PKG-INFO` & `firebase-rest-api-1.8.1/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 00000000: 4d65 7461 6461 7461 2d56 6572 7369 6f6e  Metadata-Version
 00000010: 3a20 322e 310a 4e61 6d65 3a20 6669 7265  : 2.1.Name: fire
 00000020: 6261 7365 2d72 6573 742d 6170 690a 5665  base-rest-api.Ve
-00000030: 7273 696f 6e3a 2031 2e38 2e30 0a53 756d  rsion: 1.8.0.Sum
+00000030: 7273 696f 6e3a 2031 2e38 2e31 0a53 756d  rsion: 1.8.1.Sum
 00000040: 6d61 7279 3a20 4120 7369 6d70 6c65 2070  mary: A simple p
 00000050: 7974 686f 6e20 7772 6170 7065 7220 666f  ython wrapper fo
 00000060: 7220 476f 6f67 6c65 2773 2046 6972 6562  r Google's Fireb
 00000070: 6173 6520 5245 5354 2041 5049 2773 2e0a  ase REST API's..
 00000080: 4b65 7977 6f72 6473 3a20 6669 7265 6261  Keywords: fireba
 00000090: 7365 2c66 6972 6562 6173 652d 6175 7468  se,firebase-auth
 000000a0: 2c66 6972 6562 6173 652d 6461 7461 6261  ,firebase-databa
@@ -109,168 +109,212 @@
 000006c0: 732e 696f 2f0a 5072 6f6a 6563 742d 5552  s.io/.Project-UR
 000006d0: 4c3a 2053 6f75 7263 652c 2068 7474 7073  L: Source, https
 000006e0: 3a2f 2f67 6974 6875 622e 636f 6d2f 4173  ://github.com/As
 000006f0: 6966 4172 6d61 6e52 6168 6d61 6e2f 6669  ifArmanRahman/fi
 00000700: 7265 6261 7365 2d72 6573 742d 6170 690a  rebase-rest-api.
 00000710: 5072 6f76 6964 6573 2d45 7874 7261 3a20  Provides-Extra: 
 00000720: 646f 6373 0a50 726f 7669 6465 732d 4578  docs.Provides-Ex
-00000730: 7472 613a 2074 6573 7473 0a0a 2320 4669  tra: tests..# Fi
-00000740: 7265 6261 7365 2052 4553 5420 4150 490a  rebase REST API.
-00000750: 0a5b 215b 6275 696c 645d 2868 7474 7073  .[![build](https
-00000760: 3a2f 2f67 6974 6875 622e 636f 6d2f 4173  ://github.com/As
-00000770: 6966 4172 6d61 6e52 6168 6d61 6e2f 6669  ifArmanRahman/fi
-00000780: 7265 6261 7365 2d72 6573 742d 6170 692f  rebase-rest-api/
-00000790: 6163 7469 6f6e 732f 776f 726b 666c 6f77  actions/workflow
-000007a0: 732f 6275 696c 642e 796d 6c2f 6261 6467  s/build.yml/badg
-000007b0: 652e 7376 6729 5d28 6874 7470 733a 2f2f  e.svg)](https://
-000007c0: 6769 7468 7562 2e63 6f6d 2f41 7369 6641  github.com/AsifA
-000007d0: 726d 616e 5261 686d 616e 2f66 6972 6562  rmanRahman/fireb
-000007e0: 6173 652d 7265 7374 2d61 7069 2f61 6374  ase-rest-api/act
-000007f0: 696f 6e73 2f77 6f72 6b66 6c6f 7773 2f62  ions/workflows/b
-00000800: 7569 6c64 2e79 6d6c 290a 5b21 5b74 6573  uild.yml).[![tes
-00000810: 7473 5d28 6874 7470 733a 2f2f 6769 7468  ts](https://gith
-00000820: 7562 2e63 6f6d 2f41 7369 6641 726d 616e  ub.com/AsifArman
-00000830: 5261 686d 616e 2f66 6972 6562 6173 652d  Rahman/firebase-
-00000840: 7265 7374 2d61 7069 2f61 6374 696f 6e73  rest-api/actions
-00000850: 2f77 6f72 6b66 6c6f 7773 2f74 6573 7473  /workflows/tests
-00000860: 2e79 6d6c 2f62 6164 6765 2e73 7667 295d  .yml/badge.svg)]
-00000870: 2868 7474 7073 3a2f 2f67 6974 6875 622e  (https://github.
-00000880: 636f 6d2f 4173 6966 4172 6d61 6e52 6168  com/AsifArmanRah
-00000890: 6d61 6e2f 6669 7265 6261 7365 2d72 6573  man/firebase-res
-000008a0: 742d 6170 692f 6163 7469 6f6e 732f 776f  t-api/actions/wo
-000008b0: 726b 666c 6f77 732f 7465 7374 732e 796d  rkflows/tests.ym
-000008c0: 6c29 0a5b 215b 446f 6375 6d65 6e74 6174  l).[![Documentat
-000008d0: 696f 6e20 5374 6174 7573 5d28 6874 7470  ion Status](http
-000008e0: 733a 2f2f 7265 6164 7468 6564 6f63 732e  s://readthedocs.
-000008f0: 6f72 672f 7072 6f6a 6563 7473 2f66 6972  org/projects/fir
-00000900: 6562 6173 652d 7265 7374 2d61 7069 2f62  ebase-rest-api/b
-00000910: 6164 6765 2f3f 7665 7273 696f 6e3d 6c61  adge/?version=la
-00000920: 7465 7374 295d 2868 7474 7073 3a2f 2f66  test)](https://f
-00000930: 6972 6562 6173 652d 7265 7374 2d61 7069  irebase-rest-api
-00000940: 2e72 6561 6474 6865 646f 6373 2e69 6f2f  .readthedocs.io/
-00000950: 656e 2f6c 6174 6573 742f 3f62 6164 6765  en/latest/?badge
-00000960: 3d6c 6174 6573 7429 0a5b 215b 636f 6465  =latest).[![code
-00000970: 636f 765d 2868 7474 7073 3a2f 2f63 6f64  cov](https://cod
-00000980: 6563 6f76 2e69 6f2f 6768 2f41 7369 6641  ecov.io/gh/AsifA
-00000990: 726d 616e 5261 686d 616e 2f66 6972 6562  rmanRahman/fireb
-000009a0: 6173 652d 7265 7374 2d61 7069 2f62 7261  ase-rest-api/bra
-000009b0: 6e63 682f 6d61 696e 2f67 7261 7068 2f62  nch/main/graph/b
-000009c0: 6164 6765 2e73 7667 3f74 6f6b 656e 3d4e  adge.svg?token=N
-000009d0: 3754 4531 5756 5a37 5729 5d28 6874 7470  7TE1WVZ7W)](http
-000009e0: 733a 2f2f 636f 6465 636f 762e 696f 2f67  s://codecov.io/g
-000009f0: 682f 4173 6966 4172 6d61 6e52 6168 6d61  h/AsifArmanRahma
-00000a00: 6e2f 6669 7265 6261 7365 2d72 6573 742d  n/firebase-rest-
-00000a10: 6170 6929 0a5b 215b 5079 5049 202d 2050  api).[![PyPI - P
-00000a20: 7974 686f 6e20 5665 7273 696f 6e5d 2868  ython Version](h
-00000a30: 7474 7073 3a2f 2f69 6d67 2e73 6869 656c  ttps://img.shiel
-00000a40: 6473 2e69 6f2f 7079 7069 2f70 7976 6572  ds.io/pypi/pyver
-00000a50: 7369 6f6e 732f 6669 7265 6261 7365 2d72  sions/firebase-r
-00000a60: 6573 742d 6170 693f 6c6f 676f 3d70 7974  est-api?logo=pyt
-00000a70: 686f 6e26 6c6f 676f 436f 6c6f 723d 696e  hon&logoColor=in
-00000a80: 666f 726d 6174 696f 6e61 6c29 5d28 6874  formational)](ht
-00000a90: 7470 733a 2f2f 7079 7069 2e6f 7267 2f70  tps://pypi.org/p
-00000aa0: 726f 6a65 6374 2f66 6972 6562 6173 652d  roject/firebase-
-00000ab0: 7265 7374 2d61 7069 2f29 0a5b 215b 5079  rest-api/).[![Py
-00000ac0: 5049 5d28 6874 7470 733a 2f2f 696d 672e  PI](https://img.
-00000ad0: 7368 6965 6c64 732e 696f 2f70 7970 692f  shields.io/pypi/
-00000ae0: 762f 6669 7265 6261 7365 2d72 6573 742d  v/firebase-rest-
-00000af0: 6170 693f 636f 6c6f 723d 626c 7565 266c  api?color=blue&l
-00000b00: 6f67 6f3d 7079 7069 266c 6f67 6f43 6f6c  ogo=pypi&logoCol
-00000b10: 6f72 3d77 6869 7465 295d 2868 7474 7073  or=white)](https
-00000b20: 3a2f 2f70 7970 692e 6f72 672f 7072 6f6a  ://pypi.org/proj
-00000b30: 6563 742f 6669 7265 6261 7365 2d72 6573  ect/firebase-res
-00000b40: 742d 6170 692f 290a 0a0a 4120 7369 6d70  t-api/)...A simp
-00000b50: 6c65 2070 7974 686f 6e20 7772 6170 7065  le python wrappe
-00000b60: 7220 666f 7220 5b47 6f6f 676c 6527 7320  r for [Google's 
-00000b70: 4669 7265 6261 7365 2052 4553 5420 4150  Firebase REST AP
-00000b80: 4927 735d 2868 7474 7073 3a2f 2f66 6972  I's](https://fir
-00000b90: 6562 6173 652e 676f 6f67 6c65 2e63 6f6d  ebase.google.com
-00000ba0: 292e 0a0a 2323 2049 6e73 7461 6c6c 6174  )...## Installat
-00000bb0: 696f 6e0a 0a60 6060 7079 7468 6f6e 0a70  ion..```python.p
-00000bc0: 6970 2069 6e73 7461 6c6c 2066 6972 6562  ip install fireb
-00000bd0: 6173 652d 7265 7374 2d61 7069 0a60 6060  ase-rest-api.```
-00000be0: 0a0a 0a23 2320 5175 6963 6b20 5374 6172  ...## Quick Star
-00000bf0: 740a 0a49 6e20 6f72 6465 7220 746f 2075  t..In order to u
-00000c00: 7365 2074 6869 7320 6c69 6272 6172 792c  se this library,
-00000c10: 2079 6f75 2066 6972 7374 206e 6565 6420   you first need 
-00000c20: 746f 2067 6f20 7468 726f 7567 6820 7468  to go through th
-00000c30: 6520 666f 6c6c 6f77 696e 6720 7374 6570  e following step
-00000c40: 733a 0a0a 312e 2053 656c 6563 7420 6f72  s:..1. Select or
-00000c50: 2063 7265 6174 6520 6120 4669 7265 6261   create a Fireba
-00000c60: 7365 2070 726f 6a65 6374 2066 726f 6d20  se project from 
-00000c70: 5b46 6972 6562 6173 655d 2868 7474 7073  [Firebase](https
-00000c80: 3a2f 2f63 6f6e 736f 6c65 2e66 6972 6562  ://console.fireb
-00000c90: 6173 652e 676f 6f67 6c65 2e63 6f6d 2920  ase.google.com) 
-00000ca0: 436f 6e73 6f6c 652e 0a0a 322e 2052 6567  Console...2. Reg
-00000cb0: 6973 7465 7220 616e 2057 6562 2041 7070  ister an Web App
-00000cc0: 2e0a 0a0a 2323 2320 4578 616d 706c 6520  ....### Example 
-00000cd0: 5573 6167 650a 0a60 6060 7079 7468 6f6e  Usage..```python
-00000ce0: 0a23 2049 6d70 6f72 7420 4669 7265 6261  .# Import Fireba
-00000cf0: 7365 2052 4553 5420 4150 4920 6c69 6272  se REST API libr
-00000d00: 6172 790a 696d 706f 7274 2066 6972 6562  ary.import fireb
-00000d10: 6173 650a 0a23 2046 6972 6562 6173 6520  ase..# Firebase 
-00000d20: 636f 6e66 6967 7572 6174 696f 6e0a 636f  configuration.co
-00000d30: 6e66 6967 203d 207b 0a20 2020 2261 7069  nfig = {.   "api
-00000d40: 4b65 7922 3a20 2261 7069 4b65 7922 2c0a  Key": "apiKey",.
-00000d50: 2020 2022 6175 7468 446f 6d61 696e 223a     "authDomain":
-00000d60: 2022 7072 6f6a 6563 7449 642e 6669 7265   "projectId.fire
-00000d70: 6261 7365 6170 702e 636f 6d22 2c0a 2020  baseapp.com",.  
-00000d80: 2022 6461 7461 6261 7365 5552 4c22 3a20   "databaseURL": 
-00000d90: 2268 7474 7073 3a2f 2f64 6174 6162 6173  "https://databas
-00000da0: 654e 616d 652e 6669 7265 6261 7365 696f  eName.firebaseio
-00000db0: 2e63 6f6d 222c 0a20 2020 2270 726f 6a65  .com",.   "proje
-00000dc0: 6374 4964 223a 2022 7072 6f6a 6563 7449  ctId": "projectI
-00000dd0: 6422 2c0a 2020 2022 7374 6f72 6167 6542  d",.   "storageB
-00000de0: 7563 6b65 7422 3a20 2270 726f 6a65 6374  ucket": "project
-00000df0: 4964 2e61 7070 7370 6f74 2e63 6f6d 222c  Id.appspot.com",
-00000e00: 0a20 2020 226d 6573 7361 6769 6e67 5365  .   "messagingSe
-00000e10: 6e64 6572 4964 223a 2022 6d65 7373 6167  nderId": "messag
-00000e20: 696e 6753 656e 6465 7249 6422 2c0a 2020  ingSenderId",.  
-00000e30: 2022 6170 7049 6422 3a20 2261 7070 4964   "appId": "appId
-00000e40: 220a 7d0a 0a23 2049 6e73 7461 6e74 6961  ".}..# Instantia
-00000e50: 7465 7320 6120 4669 7265 6261 7365 2061  tes a Firebase a
-00000e60: 7070 0a61 7070 203d 2066 6972 6562 6173  pp.app = firebas
-00000e70: 652e 696e 6974 6961 6c69 7a65 5f61 7070  e.initialize_app
-00000e80: 2863 6f6e 6669 6729 0a0a 0a23 2046 6972  (config)...# Fir
-00000e90: 6562 6173 6520 4175 7468 656e 7469 6361  ebase Authentica
-00000ea0: 7469 6f6e 0a61 7574 6820 3d20 6170 702e  tion.auth = app.
-00000eb0: 6175 7468 2829 0a0a 2320 4372 6561 7465  auth()..# Create
-00000ec0: 206e 6577 2075 7365 7220 616e 6420 7369   new user and si
-00000ed0: 676e 2069 6e0a 6175 7468 2e63 7265 6174  gn in.auth.creat
-00000ee0: 655f 7573 6572 5f77 6974 685f 656d 6169  e_user_with_emai
-00000ef0: 6c5f 616e 645f 7061 7373 776f 7264 2865  l_and_password(e
-00000f00: 6d61 696c 2c20 7061 7373 776f 7264 290a  mail, password).
-00000f10: 7573 6572 203d 2061 7574 682e 7369 676e  user = auth.sign
-00000f20: 5f69 6e5f 7769 7468 5f65 6d61 696c 5f61  _in_with_email_a
-00000f30: 6e64 5f70 6173 7377 6f72 6428 656d 6169  nd_password(emai
-00000f40: 6c2c 2070 6173 7377 6f72 6429 0a0a 0a23  l, password)...#
-00000f50: 2046 6972 6562 6173 6520 5265 616c 7469   Firebase Realti
-00000f60: 6d65 2044 6174 6162 6173 650a 6462 203d  me Database.db =
-00000f70: 2061 7070 2e64 6174 6162 6173 6528 290a   app.database().
-00000f80: 0a23 2044 6174 6120 746f 2073 6176 6520  .# Data to save 
-00000f90: 696e 2064 6174 6162 6173 650a 6461 7461  in database.data
-00000fa0: 203d 207b 0a20 2020 226e 616d 6522 3a20   = {.   "name": 
-00000fb0: 2252 6f62 6572 7420 446f 776e 6579 204a  "Robert Downey J
-00000fc0: 722e 222c 0a20 2020 2265 6d61 696c 223a  r.",.   "email":
-00000fd0: 2075 7365 722e 6765 7428 2765 6d61 696c   user.get('email
-00000fe0: 2729 0a7d 0a0a 2320 5374 6f72 6520 6461  ').}..# Store da
-00000ff0: 7461 2074 6f20 4669 7265 6261 7365 2044  ta to Firebase D
-00001000: 6174 6162 6173 650a 6462 2e63 6869 6c64  atabase.db.child
-00001010: 2822 7573 6572 7322 292e 7075 7368 2864  ("users").push(d
-00001020: 6174 612c 2075 7365 722e 6765 7428 2769  ata, user.get('i
-00001030: 6454 6f6b 656e 2729 290a 0a0a 2320 4669  dToken'))...# Fi
-00001040: 7265 6261 7365 2053 746f 7261 6765 0a73  rebase Storage.s
-00001050: 746f 7261 6765 203d 2061 7070 2e73 746f  torage = app.sto
-00001060: 7261 6765 2829 0a0a 2320 4669 6c65 2074  rage()..# File t
-00001070: 6f20 7374 6f72 6520 696e 2073 746f 7261  o store in stora
-00001080: 6765 0a66 696c 655f 7061 7468 203d 2027  ge.file_path = '
-00001090: 7374 6174 6963 2f69 6d67 2f65 7861 6d70  static/img/examp
-000010a0: 6c65 2e70 6e67 270a 0a23 2053 746f 7265  le.png'..# Store
-000010b0: 2066 696c 6520 746f 2046 6972 6562 6173   file to Firebas
-000010c0: 6520 5374 6f72 6167 650a 7374 6f72 6167  e Storage.storag
-000010d0: 652e 6368 696c 6428 7573 6572 2e67 6574  e.child(user.get
-000010e0: 2827 6c6f 6361 6c49 6427 2929 2e63 6869  ('localId')).chi
-000010f0: 6c64 2827 7570 6c6f 6164 6564 2d70 6963  ld('uploaded-pic
-00001100: 7475 7265 2e70 6e67 2729 2e70 7574 2866  ture.png').put(f
-00001110: 696c 655f 7061 7468 2c20 7573 6572 2e67  ile_path, user.g
-00001120: 6574 2827 6964 546f 6b65 6e27 2929 0a60  et('idToken')).`
-00001130: 6060 0a0a                                ``..
+00000730: 7472 613a 2074 6573 7473 0a0a 3c64 6976  tra: tests..<div
+00000740: 2061 6c69 676e 3d22 6365 6e74 6572 223e   align="center">
+00000750: 0a0a 2020 203c 6831 3e20 4669 7265 6261  ..   <h1> Fireba
+00000760: 7365 2052 4553 5420 4150 4920 3c2f 6831  se REST API </h1
+00000770: 3e0a 0a20 2020 3c70 3e41 2073 696d 706c  >..   <p>A simpl
+00000780: 6520 7079 7468 6f6e 2077 7261 7070 6572  e python wrapper
+00000790: 2066 6f72 203c 6120 6872 6566 3d22 6874   for <a href="ht
+000007a0: 7470 733a 2f2f 6669 7265 6261 7365 2e67  tps://firebase.g
+000007b0: 6f6f 676c 652e 636f 6d22 3e47 6f6f 676c  oogle.com">Googl
+000007c0: 6527 7320 4669 7265 6261 7365 2052 4553  e's Firebase RES
+000007d0: 5420 4150 4927 733c 2f61 3e2e 3c2f 703e  T API's</a>.</p>
+000007e0: 0a20 2020 3c62 723e 0a0a 3c2f 6469 763e  .   <br>..</div>
+000007f0: 0a0a 3c64 6976 2061 6c69 676e 3d22 6365  ..<div align="ce
+00000800: 6e74 6572 223e 0a20 2020 3c61 2068 7265  nter">.   <a hre
+00000810: 663d 2268 7474 7073 3a2f 2f70 6570 792e  f="https://pepy.
+00000820: 7465 6368 2f70 726f 6a65 6374 2f66 6972  tech/project/fir
+00000830: 6562 6173 652d 7265 7374 2d61 7069 223e  ebase-rest-api">
+00000840: 200a 2020 2020 2020 3c69 6d67 2061 6c74   .      <img alt
+00000850: 3d22 546f 7461 6c20 446f 776e 6c6f 6164  ="Total Download
+00000860: 7322 2073 7263 3d22 6874 7470 733a 2f2f  s" src="https://
+00000870: 7374 6174 6963 2e70 6570 792e 7465 6368  static.pepy.tech
+00000880: 2f70 6572 736f 6e61 6c69 7a65 642d 6261  /personalized-ba
+00000890: 6467 652f 6669 7265 6261 7365 2d72 6573  dge/firebase-res
+000008a0: 742d 6170 693f 7065 7269 6f64 3d74 6f74  t-api?period=tot
+000008b0: 616c 2675 6e69 7473 3d69 6e74 6572 6e61  al&units=interna
+000008c0: 7469 6f6e 616c 5f73 7973 7465 6d26 6c65  tional_system&le
+000008d0: 6674 5f63 6f6c 6f72 3d62 6c75 6526 7269  ft_color=blue&ri
+000008e0: 6768 745f 636f 6c6f 723d 6772 6579 266c  ght_color=grey&l
+000008f0: 6566 745f 7465 7874 3d44 6f77 6e6c 6f61  eft_text=Downloa
+00000900: 6473 223e 0a20 2020 3c2f 613e 0a3c 2f64  ds">.   </a>.</d
+00000910: 6976 3e0a 0a3c 6469 7620 616c 6967 6e3d  iv>..<div align=
+00000920: 2263 656e 7465 7222 3e0a 0a20 2020 3c61  "center">..   <a
+00000930: 2068 7265 663d 2268 7474 7073 3a2f 2f67   href="https://g
+00000940: 6974 6875 622e 636f 6d2f 4173 6966 4172  ithub.com/AsifAr
+00000950: 6d61 6e52 6168 6d61 6e2f 6669 7265 6261  manRahman/fireba
+00000960: 7365 2d72 6573 742d 6170 692f 6163 7469  se-rest-api/acti
+00000970: 6f6e 732f 776f 726b 666c 6f77 732f 6275  ons/workflows/bu
+00000980: 696c 642e 796d 6c22 3e20 0a20 2020 2020  ild.yml"> .     
+00000990: 203c 696d 6720 616c 743d 2247 6974 4875   <img alt="GitHu
+000009a0: 6220 576f 726b 666c 6f77 2053 7461 7475  b Workflow Statu
+000009b0: 7322 2073 7263 3d22 6874 7470 733a 2f2f  s" src="https://
+000009c0: 696d 672e 7368 6965 6c64 732e 696f 2f67  img.shields.io/g
+000009d0: 6974 6875 622f 6163 7469 6f6e 732f 776f  ithub/actions/wo
+000009e0: 726b 666c 6f77 2f73 7461 7475 732f 4173  rkflow/status/As
+000009f0: 6966 4172 6d61 6e52 6168 6d61 6e2f 6669  ifArmanRahman/fi
+00000a00: 7265 6261 7365 2d72 6573 742d 6170 692f  rebase-rest-api/
+00000a10: 6275 696c 642e 796d 6c3f 6c6f 676f 3d47  build.yml?logo=G
+00000a20: 6974 4875 6222 3e0a 2020 203c 2f61 3e0a  itHub">.   </a>.
+00000a30: 2020 203c 6120 6872 6566 3d22 6874 7470     <a href="http
+00000a40: 733a 2f2f 6769 7468 7562 2e63 6f6d 2f41  s://github.com/A
+00000a50: 7369 6641 726d 616e 5261 686d 616e 2f66  sifArmanRahman/f
+00000a60: 6972 6562 6173 652d 7265 7374 2d61 7069  irebase-rest-api
+00000a70: 2f61 6374 696f 6e73 2f77 6f72 6b66 6c6f  /actions/workflo
+00000a80: 7773 2f74 6573 7473 2e79 6d6c 223e 0a20  ws/tests.yml">. 
+00000a90: 2020 2020 203c 696d 6720 616c 743d 2247       <img alt="G
+00000aa0: 6974 4875 6220 576f 726b 666c 6f77 2053  itHub Workflow S
+00000ab0: 7461 7475 7322 2073 7263 3d22 6874 7470  tatus" src="http
+00000ac0: 733a 2f2f 696d 672e 7368 6965 6c64 732e  s://img.shields.
+00000ad0: 696f 2f67 6974 6875 622f 6163 7469 6f6e  io/github/action
+00000ae0: 732f 776f 726b 666c 6f77 2f73 7461 7475  s/workflow/statu
+00000af0: 732f 6173 6966 6172 6d61 6e72 6168 6d61  s/asifarmanrahma
+00000b00: 6e2f 6669 7265 6261 7365 2d72 6573 742d  n/firebase-rest-
+00000b10: 6170 692f 7465 7374 732e 796d 6c3f 6c61  api/tests.yml?la
+00000b20: 6265 6c3d 7465 7374 7326 6c6f 676f 3d50  bel=tests&logo=P
+00000b30: 7974 6573 7422 3e0a 2020 203c 2f61 3e0a  ytest">.   </a>.
+00000b40: 2020 203c 6120 6872 6566 3d22 6874 7470     <a href="http
+00000b50: 733a 2f2f 6669 7265 6261 7365 2d72 6573  s://firebase-res
+00000b60: 742d 6170 692e 7265 6164 7468 6564 6f63  t-api.readthedoc
+00000b70: 732e 696f 2f65 6e2f 6c61 7465 7374 2f22  s.io/en/latest/"
+00000b80: 3e0a 2020 2020 2020 3c69 6d67 2061 6c74  >.      <img alt
+00000b90: 3d22 5265 6164 2074 6865 2044 6f63 7322  ="Read the Docs"
+00000ba0: 2073 7263 3d22 6874 7470 733a 2f2f 696d   src="https://im
+00000bb0: 672e 7368 6965 6c64 732e 696f 2f72 6561  g.shields.io/rea
+00000bc0: 6474 6865 646f 6373 2f66 6972 6562 6173  dthedocs/firebas
+00000bd0: 652d 7265 7374 2d61 7069 3f6c 6f67 6f3d  e-rest-api?logo=
+00000be0: 5265 6164 2532 3074 6865 2532 3044 6f63  Read%20the%20Doc
+00000bf0: 7326 6c6f 676f 436f 6c6f 723d 7768 6974  s&logoColor=whit
+00000c00: 6522 3e0a 2020 203c 2f61 3e0a 2020 203c  e">.   </a>.   <
+00000c10: 6120 6872 6566 3d22 6874 7470 733a 2f2f  a href="https://
+00000c20: 636f 6465 636f 762e 696f 2f67 682f 4173  codecov.io/gh/As
+00000c30: 6966 4172 6d61 6e52 6168 6d61 6e2f 6669  ifArmanRahman/fi
+00000c40: 7265 6261 7365 2d72 6573 742d 6170 6922  rebase-rest-api"
+00000c50: 3e20 0a20 2020 2020 203c 696d 6720 616c  > .      <img al
+00000c60: 743d 2243 6f64 6543 6f76 2220 7372 633d  t="CodeCov" src=
+00000c70: 2268 7474 7073 3a2f 2f63 6f64 6563 6f76  "https://codecov
+00000c80: 2e69 6f2f 6768 2f41 7369 6641 726d 616e  .io/gh/AsifArman
+00000c90: 5261 686d 616e 2f66 6972 6562 6173 652d  Rahman/firebase-
+00000ca0: 7265 7374 2d61 7069 2f62 7261 6e63 682f  rest-api/branch/
+00000cb0: 6d61 696e 2f67 7261 7068 2f62 6164 6765  main/graph/badge
+00000cc0: 2e73 7667 3f74 6f6b 656e 3d4e 3754 4531  .svg?token=N7TE1
+00000cd0: 5756 5a37 5722 3e20 0a20 2020 3c2f 613e  WVZ7W"> .   </a>
+00000ce0: 0a0a 3c2f 6469 763e 0a0a 3c64 6976 2061  ..</div>..<div a
+00000cf0: 6c69 676e 3d22 6365 6e74 6572 223e 0a20  lign="center">. 
+00000d00: 2020 3c61 2068 7265 663d 2268 7474 7073    <a href="https
+00000d10: 3a2f 2f70 7970 692e 6f72 672f 7072 6f6a  ://pypi.org/proj
+00000d20: 6563 742f 6669 7265 6261 7365 2d72 6573  ect/firebase-res
+00000d30: 742d 6170 692f 223e 200a 2020 2020 2020  t-api/"> .      
+00000d40: 3c69 6d67 2061 6c74 3d22 5079 5049 202d  <img alt="PyPI -
+00000d50: 2050 7974 686f 6e20 5665 7273 696f 6e22   Python Version"
+00000d60: 2073 7263 3d22 6874 7470 733a 2f2f 696d   src="https://im
+00000d70: 672e 7368 6965 6c64 732e 696f 2f70 7970  g.shields.io/pyp
+00000d80: 692f 7079 7665 7273 696f 6e73 2f66 6972  i/pyversions/fir
+00000d90: 6562 6173 652d 7265 7374 2d61 7069 3f6c  ebase-rest-api?l
+00000da0: 6f67 6f3d 7079 7468 6f6e 223e 0a20 2020  ogo=python">.   
+00000db0: 3c2f 613e 0a20 2020 3c61 2068 7265 663d  </a>.   <a href=
+00000dc0: 2268 7474 7073 3a2f 2f70 7970 692e 6f72  "https://pypi.or
+00000dd0: 672f 7072 6f6a 6563 742f 6669 7265 6261  g/project/fireba
+00000de0: 7365 2d72 6573 742d 6170 692f 223e 200a  se-rest-api/"> .
+00000df0: 2020 2020 2020 3c69 6d67 2061 6c74 3d22        <img alt="
+00000e00: 5079 5049 2220 7372 633d 2268 7474 7073  PyPI" src="https
+00000e10: 3a2f 2f69 6d67 2e73 6869 656c 6473 2e69  ://img.shields.i
+00000e20: 6f2f 7079 7069 2f76 2f66 6972 6562 6173  o/pypi/v/firebas
+00000e30: 652d 7265 7374 2d61 7069 3f6c 6f67 6f3d  e-rest-api?logo=
+00000e40: 5079 5049 266c 6f67 6f43 6f6c 6f72 3d77  PyPI&logoColor=w
+00000e50: 6869 7465 223e 0a20 2020 3c2f 613e 0a3c  hite">.   </a>.<
+00000e60: 2f64 6976 3e0a 0a0a 0a23 2320 496e 7374  /div>....## Inst
+00000e70: 616c 6c61 7469 6f6e 0a0a 6060 6070 7974  allation..```pyt
+00000e80: 686f 6e0a 7069 7020 696e 7374 616c 6c20  hon.pip install 
+00000e90: 6669 7265 6261 7365 2d72 6573 742d 6170  firebase-rest-ap
+00000ea0: 690a 6060 600a 0a0a 2323 2051 7569 636b  i.```...## Quick
+00000eb0: 2053 7461 7274 0a0a 496e 206f 7264 6572   Start..In order
+00000ec0: 2074 6f20 7573 6520 7468 6973 206c 6962   to use this lib
+00000ed0: 7261 7279 2c20 796f 7520 6669 7273 7420  rary, you first 
+00000ee0: 6e65 6564 2074 6f20 676f 2074 6872 6f75  need to go throu
+00000ef0: 6768 2074 6865 2066 6f6c 6c6f 7769 6e67  gh the following
+00000f00: 2073 7465 7073 3a0a 0a31 2e20 5365 6c65   steps:..1. Sele
+00000f10: 6374 206f 7220 6372 6561 7465 2061 2046  ct or create a F
+00000f20: 6972 6562 6173 6520 7072 6f6a 6563 7420  irebase project 
+00000f30: 6672 6f6d 205b 4669 7265 6261 7365 5d28  from [Firebase](
+00000f40: 6874 7470 733a 2f2f 636f 6e73 6f6c 652e  https://console.
+00000f50: 6669 7265 6261 7365 2e67 6f6f 676c 652e  firebase.google.
+00000f60: 636f 6d29 2043 6f6e 736f 6c65 2e0a 0a32  com) Console...2
+00000f70: 2e20 5265 6769 7374 6572 2061 6e20 5765  . Register an We
+00000f80: 6220 4170 702e 0a0a 0a23 2323 2045 7861  b App....### Exa
+00000f90: 6d70 6c65 2055 7361 6765 0a0a 6060 6070  mple Usage..```p
+00000fa0: 7974 686f 6e0a 2320 496d 706f 7274 2046  ython.# Import F
+00000fb0: 6972 6562 6173 6520 5245 5354 2041 5049  irebase REST API
+00000fc0: 206c 6962 7261 7279 0a69 6d70 6f72 7420   library.import 
+00000fd0: 6669 7265 6261 7365 0a0a 2320 4669 7265  firebase..# Fire
+00000fe0: 6261 7365 2063 6f6e 6669 6775 7261 7469  base configurati
+00000ff0: 6f6e 0a63 6f6e 6669 6720 3d20 7b0a 2020  on.config = {.  
+00001000: 2022 6170 694b 6579 223a 2022 6170 694b   "apiKey": "apiK
+00001010: 6579 222c 0a20 2020 2261 7574 6844 6f6d  ey",.   "authDom
+00001020: 6169 6e22 3a20 2270 726f 6a65 6374 4964  ain": "projectId
+00001030: 2e66 6972 6562 6173 6561 7070 2e63 6f6d  .firebaseapp.com
+00001040: 222c 0a20 2020 2264 6174 6162 6173 6555  ",.   "databaseU
+00001050: 524c 223a 2022 6874 7470 733a 2f2f 6461  RL": "https://da
+00001060: 7461 6261 7365 4e61 6d65 2e66 6972 6562  tabaseName.fireb
+00001070: 6173 6569 6f2e 636f 6d22 2c0a 2020 2022  aseio.com",.   "
+00001080: 7072 6f6a 6563 7449 6422 3a20 2270 726f  projectId": "pro
+00001090: 6a65 6374 4964 222c 0a20 2020 2273 746f  jectId",.   "sto
+000010a0: 7261 6765 4275 636b 6574 223a 2022 7072  rageBucket": "pr
+000010b0: 6f6a 6563 7449 642e 6170 7073 706f 742e  ojectId.appspot.
+000010c0: 636f 6d22 2c0a 2020 2022 6d65 7373 6167  com",.   "messag
+000010d0: 696e 6753 656e 6465 7249 6422 3a20 226d  ingSenderId": "m
+000010e0: 6573 7361 6769 6e67 5365 6e64 6572 4964  essagingSenderId
+000010f0: 222c 0a20 2020 2261 7070 4964 223a 2022  ",.   "appId": "
+00001100: 6170 7049 6422 0a7d 0a0a 2320 496e 7374  appId".}..# Inst
+00001110: 616e 7469 6174 6573 2061 2046 6972 6562  antiates a Fireb
+00001120: 6173 6520 6170 700a 6170 7020 3d20 6669  ase app.app = fi
+00001130: 7265 6261 7365 2e69 6e69 7469 616c 697a  rebase.initializ
+00001140: 655f 6170 7028 636f 6e66 6967 290a 0a0a  e_app(config)...
+00001150: 2320 4669 7265 6261 7365 2041 7574 6865  # Firebase Authe
+00001160: 6e74 6963 6174 696f 6e0a 6175 7468 203d  ntication.auth =
+00001170: 2061 7070 2e61 7574 6828 290a 0a23 2043   app.auth()..# C
+00001180: 7265 6174 6520 6e65 7720 7573 6572 2061  reate new user a
+00001190: 6e64 2073 6967 6e20 696e 0a61 7574 682e  nd sign in.auth.
+000011a0: 6372 6561 7465 5f75 7365 725f 7769 7468  create_user_with
+000011b0: 5f65 6d61 696c 5f61 6e64 5f70 6173 7377  _email_and_passw
+000011c0: 6f72 6428 656d 6169 6c2c 2070 6173 7377  ord(email, passw
+000011d0: 6f72 6429 0a75 7365 7220 3d20 6175 7468  ord).user = auth
+000011e0: 2e73 6967 6e5f 696e 5f77 6974 685f 656d  .sign_in_with_em
+000011f0: 6169 6c5f 616e 645f 7061 7373 776f 7264  ail_and_password
+00001200: 2865 6d61 696c 2c20 7061 7373 776f 7264  (email, password
+00001210: 290a 0a0a 2320 4669 7265 6261 7365 2052  )...# Firebase R
+00001220: 6561 6c74 696d 6520 4461 7461 6261 7365  ealtime Database
+00001230: 0a64 6220 3d20 6170 702e 6461 7461 6261  .db = app.databa
+00001240: 7365 2829 0a0a 2320 4461 7461 2074 6f20  se()..# Data to 
+00001250: 7361 7665 2069 6e20 6461 7461 6261 7365  save in database
+00001260: 0a64 6174 6120 3d20 7b0a 2020 2022 6e61  .data = {.   "na
+00001270: 6d65 223a 2022 526f 6265 7274 2044 6f77  me": "Robert Dow
+00001280: 6e65 7920 4a72 2e22 2c0a 2020 2022 656d  ney Jr.",.   "em
+00001290: 6169 6c22 3a20 7573 6572 2e67 6574 2827  ail": user.get('
+000012a0: 656d 6169 6c27 290a 7d0a 0a23 2053 746f  email').}..# Sto
+000012b0: 7265 2064 6174 6120 746f 2046 6972 6562  re data to Fireb
+000012c0: 6173 6520 4461 7461 6261 7365 0a64 622e  ase Database.db.
+000012d0: 6368 696c 6428 2275 7365 7273 2229 2e70  child("users").p
+000012e0: 7573 6828 6461 7461 2c20 7573 6572 2e67  ush(data, user.g
+000012f0: 6574 2827 6964 546f 6b65 6e27 2929 0a0a  et('idToken'))..
+00001300: 0a23 2046 6972 6562 6173 6520 5374 6f72  .# Firebase Stor
+00001310: 6167 650a 7374 6f72 6167 6520 3d20 6170  age.storage = ap
+00001320: 702e 7374 6f72 6167 6528 290a 0a23 2046  p.storage()..# F
+00001330: 696c 6520 746f 2073 746f 7265 2069 6e20  ile to store in 
+00001340: 7374 6f72 6167 650a 6669 6c65 5f70 6174  storage.file_pat
+00001350: 6820 3d20 2773 7461 7469 632f 696d 672f  h = 'static/img/
+00001360: 6578 616d 706c 652e 706e 6727 0a0a 2320  example.png'..# 
+00001370: 5374 6f72 6520 6669 6c65 2074 6f20 4669  Store file to Fi
+00001380: 7265 6261 7365 2053 746f 7261 6765 0a73  rebase Storage.s
+00001390: 746f 7261 6765 2e63 6869 6c64 2875 7365  torage.child(use
+000013a0: 722e 6765 7428 276c 6f63 616c 4964 2729  r.get('localId')
+000013b0: 292e 6368 696c 6428 2775 706c 6f61 6465  ).child('uploade
+000013c0: 642d 7069 6374 7572 652e 706e 6727 292e  d-picture.png').
+000013d0: 7075 7428 6669 6c65 5f70 6174 682c 2075  put(file_path, u
+000013e0: 7365 722e 6765 7428 2769 6454 6f6b 656e  ser.get('idToken
+000013f0: 2729 290a 6060 600a 0a                   ')).```..
```

