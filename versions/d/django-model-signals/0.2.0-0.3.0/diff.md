# Comparing `tmp/django_model_signals-0.2.0.tar.gz` & `tmp/django_model_signals-0.3.0.tar.gz`

## Comparing `django_model_signals-0.2.0.tar` & `django_model_signals-0.3.0.tar`

### file list

```diff
@@ -1,12 +1,12 @@
--rw-r--r--   0        0        0      653 2020-02-02 00:00:00.000000 django_model_signals-0.2.0/.github/workflows/publish-to-pypi.yml
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 django_model_signals-0.2.0/django_model_signals/__init__.py
--rw-r--r--   0        0        0     2130 2020-02-02 00:00:00.000000 django_model_signals-0.2.0/django_model_signals/apps.py
--rw-r--r--   0        0        0      957 2020-02-02 00:00:00.000000 django_model_signals-0.2.0/django_model_signals/dispatcher.py
--rw-r--r--   0        0        0     1889 2020-02-02 00:00:00.000000 django_model_signals-0.2.0/django_model_signals/manager.py
--rw-r--r--   0        0        0       97 2020-02-02 00:00:00.000000 django_model_signals-0.2.0/django_model_signals/signals.py
--rw-r--r--   0        0        0      562 2020-02-02 00:00:00.000000 django_model_signals-0.2.0/django_model_signals/transceiver.py
--rw-r--r--   0        0        0       30 2020-02-02 00:00:00.000000 django_model_signals-0.2.0/.gitignore
--rw-r--r--   0        0        0     1071 2020-02-02 00:00:00.000000 django_model_signals-0.2.0/LICENSE.md
--rw-r--r--   0        0        0     1861 2020-02-02 00:00:00.000000 django_model_signals-0.2.0/README.md
--rw-r--r--   0        0        0      649 2020-02-02 00:00:00.000000 django_model_signals-0.2.0/pyproject.toml
--rw-r--r--   0        0        0     2459 2020-02-02 00:00:00.000000 django_model_signals-0.2.0/PKG-INFO
+-rw-r--r--   0        0        0      653 2020-02-02 00:00:00.000000 django_model_signals-0.3.0/.github/workflows/publish-to-pypi.yml
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 django_model_signals-0.3.0/django_model_signals/__init__.py
+-rw-r--r--   0        0        0     1009 2020-02-02 00:00:00.000000 django_model_signals-0.3.0/django_model_signals/apps.py
+-rw-r--r--   0        0        0      649 2020-02-02 00:00:00.000000 django_model_signals-0.3.0/django_model_signals/dispatcher.py
+-rw-r--r--   0        0        0     1889 2020-02-02 00:00:00.000000 django_model_signals-0.3.0/django_model_signals/manager.py
+-rw-r--r--   0        0        0      673 2020-02-02 00:00:00.000000 django_model_signals-0.3.0/django_model_signals/signals.py
+-rw-r--r--   0        0        0     1257 2020-02-02 00:00:00.000000 django_model_signals-0.3.0/django_model_signals/transceiver.py
+-rw-r--r--   0        0        0       30 2020-02-02 00:00:00.000000 django_model_signals-0.3.0/.gitignore
+-rw-r--r--   0        0        0     1071 2020-02-02 00:00:00.000000 django_model_signals-0.3.0/LICENSE.md
+-rw-r--r--   0        0        0     3419 2020-02-02 00:00:00.000000 django_model_signals-0.3.0/README.md
+-rw-r--r--   0        0        0      649 2020-02-02 00:00:00.000000 django_model_signals-0.3.0/pyproject.toml
+-rw-r--r--   0        0        0     4017 2020-02-02 00:00:00.000000 django_model_signals-0.3.0/PKG-INFO
```

### Comparing `django_model_signals-0.2.0/.github/workflows/publish-to-pypi.yml` & `django_model_signals-0.3.0/.github/workflows/publish-to-pypi.yml`

 * *Files identical despite different names*

### Comparing `django_model_signals-0.2.0/django_model_signals/manager.py` & `django_model_signals-0.3.0/django_model_signals/manager.py`

 * *Files identical despite different names*

### Comparing `django_model_signals-0.2.0/LICENSE.md` & `django_model_signals-0.3.0/LICENSE.md`

 * *Files identical despite different names*

### Comparing `django_model_signals-0.2.0/pyproject.toml` & `django_model_signals-0.3.0/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "django-model-signals"
-version = "0.2.0"
+version = "0.3.0"
 authors = [
   { name="Digital Valley", email="techteam@digitalvalley.nl" }
 ]
 description = "Django Model Signals makes it easier to keep model related business logic in your Django models by allowing them to become transceivers of their own signals, including bulk signals."
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

