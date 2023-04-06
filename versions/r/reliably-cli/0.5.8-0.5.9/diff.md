# Comparing `tmp/reliably-cli-0.5.8.tar.gz` & `tmp/reliably-cli-0.5.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "reliably-cli-0.5.8.tar", last modified: Thu Mar 16 15:29:54 2023, max compression
+gzip compressed data, was "reliably-cli-0.5.9.tar", last modified: Thu Mar 16 15:51:23 2023, max compression
```

## Comparing `reliably-cli-0.5.8.tar` & `reliably-cli-0.5.9.tar`

### file list

```diff
@@ -1,25 +1,25 @@
--rw-r--r--   0        0        0    11357 2023-03-16 15:29:38.298798 reliably-cli-0.5.8/LICENSE
--rw-r--r--   0        0        0     1472 2023-03-16 15:29:38.298798 reliably-cli-0.5.8/README.md
--rw-r--r--   0        0        0     2404 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/pyproject.toml
--rw-r--r--   0        0        0      114 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/reliably_cli/__init__.py
--rw-r--r--   0        0        0      881 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/reliably_cli/__main__.py
--rw-r--r--   0        0        0      166 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/reliably_cli/__version__.py
--rw-r--r--   0        0        0     1221 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/reliably_cli/agent/__init__.py
--rw-r--r--   0        0        0     1545 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/reliably_cli/agent/cli.py
--rw-r--r--   0        0        0     2770 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/reliably_cli/agent/plan/__init__.py
--rw-r--r--   0        0        0     1352 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/reliably_cli/agent/plan/providers/__init__.py
--rw-r--r--   0        0        0     3493 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/reliably_cli/agent/plan/providers/github.py
--rw-r--r--   0        0        0     1215 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/reliably_cli/client.py
--rw-r--r--   0        0        0     1087 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/reliably_cli/config/__init__.py
--rw-r--r--   0        0        0     3552 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/reliably_cli/config/cli.py
--rw-r--r--   0        0        0     2403 2023-03-16 15:29:38.302799 reliably-cli-0.5.8/reliably_cli/config/types.py
--rw-r--r--   0        0        0      546 2023-03-16 15:29:38.306799 reliably-cli-0.5.8/reliably_cli/format.py
--rw-r--r--   0        0        0      126 2023-03-16 15:29:38.306799 reliably-cli-0.5.8/reliably_cli/log.py
--rw-r--r--   0        0        0        0 2023-03-16 15:29:38.306799 reliably-cli-0.5.8/reliably_cli/services/__init__.py
--rw-r--r--   0        0        0      211 2023-03-16 15:29:38.306799 reliably-cli-0.5.8/reliably_cli/services/cli.py
--rw-r--r--   0        0        0     2388 2023-03-16 15:29:38.306799 reliably-cli-0.5.8/reliably_cli/services/org.py
--rw-r--r--   0        0        0     5851 2023-03-16 15:29:38.306799 reliably-cli-0.5.8/reliably_cli/services/plan.py
--rw-r--r--   0        0        0     1777 2023-03-16 15:29:38.306799 reliably-cli-0.5.8/reliably_cli/types.py
--rw-r--r--   0        0        0      662 2023-03-16 15:29:38.306799 reliably-cli-0.5.8/tests/conftest.py
--rw-r--r--   0        0        0      581 2023-03-16 15:29:38.306799 reliably-cli-0.5.8/tests/test_cli.py
--rw-r--r--   0        0        0     1751 1970-01-01 00:00:00.000000 reliably-cli-0.5.8/PKG-INFO
+-rw-r--r--   0        0        0    11357 2023-03-16 15:50:55.186972 reliably-cli-0.5.9/LICENSE
+-rw-r--r--   0        0        0     1472 2023-03-16 15:50:55.190972 reliably-cli-0.5.9/README.md
+-rw-r--r--   0        0        0     2404 2023-03-16 15:50:55.190972 reliably-cli-0.5.9/pyproject.toml
+-rw-r--r--   0        0        0      114 2023-03-16 15:50:55.190972 reliably-cli-0.5.9/reliably_cli/__init__.py
+-rw-r--r--   0        0        0      881 2023-03-16 15:50:55.190972 reliably-cli-0.5.9/reliably_cli/__main__.py
+-rw-r--r--   0        0        0      166 2023-03-16 15:50:55.190972 reliably-cli-0.5.9/reliably_cli/__version__.py
+-rw-r--r--   0        0        0     1221 2023-03-16 15:50:55.190972 reliably-cli-0.5.9/reliably_cli/agent/__init__.py
+-rw-r--r--   0        0        0     1545 2023-03-16 15:50:55.190972 reliably-cli-0.5.9/reliably_cli/agent/cli.py
+-rw-r--r--   0        0        0     2770 2023-03-16 15:50:55.190972 reliably-cli-0.5.9/reliably_cli/agent/plan/__init__.py
+-rw-r--r--   0        0        0     1352 2023-03-16 15:50:55.190972 reliably-cli-0.5.9/reliably_cli/agent/plan/providers/__init__.py
+-rw-r--r--   0        0        0     3493 2023-03-16 15:50:55.190972 reliably-cli-0.5.9/reliably_cli/agent/plan/providers/github.py
+-rw-r--r--   0        0        0     1215 2023-03-16 15:50:55.190972 reliably-cli-0.5.9/reliably_cli/client.py
+-rw-r--r--   0        0        0     1087 2023-03-16 15:50:55.194972 reliably-cli-0.5.9/reliably_cli/config/__init__.py
+-rw-r--r--   0        0        0     3552 2023-03-16 15:50:55.194972 reliably-cli-0.5.9/reliably_cli/config/cli.py
+-rw-r--r--   0        0        0     2403 2023-03-16 15:50:55.194972 reliably-cli-0.5.9/reliably_cli/config/types.py
+-rw-r--r--   0        0        0      546 2023-03-16 15:50:55.194972 reliably-cli-0.5.9/reliably_cli/format.py
+-rw-r--r--   0        0        0      126 2023-03-16 15:50:55.194972 reliably-cli-0.5.9/reliably_cli/log.py
+-rw-r--r--   0        0        0        0 2023-03-16 15:50:55.194972 reliably-cli-0.5.9/reliably_cli/services/__init__.py
+-rw-r--r--   0        0        0      211 2023-03-16 15:50:55.194972 reliably-cli-0.5.9/reliably_cli/services/cli.py
+-rw-r--r--   0        0        0     2388 2023-03-16 15:50:55.194972 reliably-cli-0.5.9/reliably_cli/services/org.py
+-rw-r--r--   0        0        0     5851 2023-03-16 15:50:55.194972 reliably-cli-0.5.9/reliably_cli/services/plan.py
+-rw-r--r--   0        0        0     1777 2023-03-16 15:50:55.194972 reliably-cli-0.5.9/reliably_cli/types.py
+-rw-r--r--   0        0        0      662 2023-03-16 15:50:55.194972 reliably-cli-0.5.9/tests/conftest.py
+-rw-r--r--   0        0        0      581 2023-03-16 15:50:55.194972 reliably-cli-0.5.9/tests/test_cli.py
+-rw-r--r--   0        0        0     1751 1970-01-01 00:00:00.000000 reliably-cli-0.5.9/PKG-INFO
```

### Comparing `reliably-cli-0.5.8/LICENSE` & `reliably-cli-0.5.9/LICENSE`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/README.md` & `reliably-cli-0.5.9/README.md`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/pyproject.toml` & `reliably-cli-0.5.9/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -16,15 +16,15 @@
     "ruamel.yaml>=0.17.21",
     "rich>=13.3.1",
     "chaostoolkit-addons>=0.4.0",
     "chaostoolkit>=1.15.0",
     "chaostoolkit-lib>=1.33.1",
     "chaostoolkit-reliably>=0.22.0",
 ]
-version = "0.5.8"
+version = "0.5.9"
 
 [project.license]
 text = "Apache-2.0"
 
 [project.scripts]
 reliably = "reliably_cli.__main__:cli"
```

### Comparing `reliably-cli-0.5.8/reliably_cli/__main__.py` & `reliably-cli-0.5.9/reliably_cli/__main__.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/agent/__init__.py` & `reliably-cli-0.5.9/reliably_cli/agent/__init__.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/agent/cli.py` & `reliably-cli-0.5.9/reliably_cli/agent/cli.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/agent/plan/__init__.py` & `reliably-cli-0.5.9/reliably_cli/agent/plan/__init__.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/agent/plan/providers/__init__.py` & `reliably-cli-0.5.9/reliably_cli/agent/plan/providers/__init__.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/agent/plan/providers/github.py` & `reliably-cli-0.5.9/reliably_cli/agent/plan/providers/github.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/client.py` & `reliably-cli-0.5.9/reliably_cli/client.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/config/__init__.py` & `reliably-cli-0.5.9/reliably_cli/config/__init__.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/config/cli.py` & `reliably-cli-0.5.9/reliably_cli/config/cli.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/config/types.py` & `reliably-cli-0.5.9/reliably_cli/config/types.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/format.py` & `reliably-cli-0.5.9/reliably_cli/format.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/services/org.py` & `reliably-cli-0.5.9/reliably_cli/services/org.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/services/plan.py` & `reliably-cli-0.5.9/reliably_cli/services/plan.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/reliably_cli/types.py` & `reliably-cli-0.5.9/reliably_cli/types.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/tests/conftest.py` & `reliably-cli-0.5.9/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/tests/test_cli.py` & `reliably-cli-0.5.9/tests/test_cli.py`

 * *Files identical despite different names*

### Comparing `reliably-cli-0.5.8/PKG-INFO` & `reliably-cli-0.5.9/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: reliably-cli
-Version: 0.5.8
+Version: 0.5.9
 Summary: Reliably CLI
 License: Apache-2.0
 Author-email: Sylvain Hellegouarch <sylvain@reliably.com>
 Requires-Python: >=3.10
 Provides-Extra: bin-builder
 Provides-Extra: chaostoolkit
 Description-Content-Type: text/markdown
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: reliably-cli Version: 0.5.8 Summary: Reliably CLI
+Metadata-Version: 2.1 Name: reliably-cli Version: 0.5.9 Summary: Reliably CLI
 License: Apache-2.0 Author-email: Sylvain Hellegouarch
 reliably.com> Requires-Python: >=3.10 Provides-Extra: bin-builder Provides-
 Extra: chaostoolkit Description-Content-Type: text/markdown
                                     *****
  [https://raw.githubusercontent.com/reliablyhq/cli/main/public/logo.png] *****
                 *** Reliably CLI | Optimise your operations ***
         [Release]_[Supported_Python]_[Build]_[GitHub_issues]_[License]
```

