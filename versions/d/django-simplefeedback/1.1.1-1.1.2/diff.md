# Comparing `tmp/django_simplefeedback-1.1.1.tar.gz` & `tmp/django_simplefeedback-1.1.2.tar.gz`

## Comparing `django_simplefeedback-1.1.1.tar` & `django_simplefeedback-1.1.2.tar`

### file list

```diff
@@ -1,23 +1,24 @@
--rw-r--r--   0        0        0      123 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/MANIFEST.in
--rw-r--r--   0        0        0       27 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/requirements.txt
--rw-r--r--   0        0        0     2286 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/runtests.py
--rw-r--r--   0        0        0     1103 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/setup.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/__init__.py
--rw-r--r--   0        0        0     1314 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/admin.py
--rw-r--r--   0        0        0      108 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/apps.py
--rw-r--r--   0        0        0     2769 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/models.py
--rw-r--r--   0        0        0      187 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/serializers.py
--rw-r--r--   0        0        0     4805 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/tests.py
--rw-r--r--   0        0        0      293 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/urls.py
--rw-r--r--   0        0        0     1083 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/views.py
--rw-r--r--   0        0        0     1391 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/migrations/0001_initial.py
--rw-r--r--   0        0        0      523 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/migrations/0002_auto_20180115_1854.py
--rw-r--r--   0        0        0      699 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/migrations/0003_ticket_assignee.py
--rw-r--r--   0        0        0      802 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/migrations/0004_auto_20180612_1559.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/migrations/__init__.py
--rw-r--r--   0        0        0      189 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/simple_feedback/templates/email/notify_template.html
--rw-r--r--   0        0        0       47 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/.gitignore
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/LICENSE
--rw-r--r--   0        0        0     2785 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/README.md
--rw-r--r--   0        0        0      691 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/pyproject.toml
--rw-r--r--   0        0        0     3367 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.1/PKG-INFO
+-rw-r--r--   0        0        0      123 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/MANIFEST.in
+-rw-r--r--   0        0        0       27 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/requirements.txt
+-rw-r--r--   0        0        0     2286 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/runtests.py
+-rw-r--r--   0        0        0     1103 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/setup.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/__init__.py
+-rw-r--r--   0        0        0     1314 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/admin.py
+-rw-r--r--   0        0        0      108 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/apps.py
+-rw-r--r--   0        0        0     2769 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/models.py
+-rw-r--r--   0        0        0      187 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/serializers.py
+-rw-r--r--   0        0        0     4805 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/tests.py
+-rw-r--r--   0        0        0      293 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/urls.py
+-rw-r--r--   0        0        0     1083 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/views.py
+-rw-r--r--   0        0        0     1391 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/migrations/0001_initial.py
+-rw-r--r--   0        0        0      523 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/migrations/0002_auto_20180115_1854.py
+-rw-r--r--   0        0        0      699 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/migrations/0003_ticket_assignee.py
+-rw-r--r--   0        0        0      802 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/migrations/0004_auto_20180612_1559.py
+-rw-r--r--   0        0        0      401 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/migrations/0005_alter_ticket_meta.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/migrations/__init__.py
+-rw-r--r--   0        0        0      189 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/simple_feedback/templates/email/notify_template.html
+-rw-r--r--   0        0        0       47 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/.gitignore
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/LICENSE
+-rw-r--r--   0        0        0     2785 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/README.md
+-rw-r--r--   0        0        0      691 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/pyproject.toml
+-rw-r--r--   0        0        0     3367 2020-02-02 00:00:00.000000 django_simplefeedback-1.1.2/PKG-INFO
```

### Comparing `django_simplefeedback-1.1.1/runtests.py` & `django_simplefeedback-1.1.2/runtests.py`

 * *Files identical despite different names*

### Comparing `django_simplefeedback-1.1.1/setup.py` & `django_simplefeedback-1.1.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,15 +5,15 @@
     long_description = fh.read()
 
 # allow setup.py to be run from any path
 os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
 setup(
     name='django-simplefeedback',
-    version='1.1.1',
+    version='1.1.2',
     packages=find_packages(),
     include_package_data=True,
     license='BSD License',  # example license
     description='A simple Django app to handle user tickets.',
     long_description=long_description,
     long_description_content_type="text/markdown",
     url='https://www.github.com/pulilab/django-simple-feedback',
```

### Comparing `django_simplefeedback-1.1.1/simple_feedback/admin.py` & `django_simplefeedback-1.1.2/simple_feedback/admin.py`

 * *Files identical despite different names*

### Comparing `django_simplefeedback-1.1.1/simple_feedback/models.py` & `django_simplefeedback-1.1.2/simple_feedback/models.py`

 * *Files identical despite different names*

### Comparing `django_simplefeedback-1.1.1/simple_feedback/tests.py` & `django_simplefeedback-1.1.2/simple_feedback/tests.py`

 * *Files identical despite different names*

### Comparing `django_simplefeedback-1.1.1/simple_feedback/views.py` & `django_simplefeedback-1.1.2/simple_feedback/views.py`

 * *Files identical despite different names*

### Comparing `django_simplefeedback-1.1.1/simple_feedback/migrations/0001_initial.py` & `django_simplefeedback-1.1.2/simple_feedback/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `django_simplefeedback-1.1.1/simple_feedback/migrations/0002_auto_20180115_1854.py` & `django_simplefeedback-1.1.2/simple_feedback/migrations/0002_auto_20180115_1854.py`

 * *Files identical despite different names*

### Comparing `django_simplefeedback-1.1.1/simple_feedback/migrations/0003_ticket_assignee.py` & `django_simplefeedback-1.1.2/simple_feedback/migrations/0003_ticket_assignee.py`

 * *Files identical despite different names*

### Comparing `django_simplefeedback-1.1.1/simple_feedback/migrations/0004_auto_20180612_1559.py` & `django_simplefeedback-1.1.2/simple_feedback/migrations/0004_auto_20180612_1559.py`

 * *Files identical despite different names*

### Comparing `django_simplefeedback-1.1.1/README.md` & `django_simplefeedback-1.1.2/README.md`

 * *Files identical despite different names*

### Comparing `django_simplefeedback-1.1.1/pyproject.toml` & `django_simplefeedback-1.1.2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "django-simplefeedback"
-version = "1.1.1"
+version = "1.1.2"
 authors = [
   { name="Zoltan Ilcsik", email="zi@pulilab.com" },
   { name="Fekete Gyorgy", email="f@pulilab.com" },
 ]
 description = "A simple Django app to handle user tickets."
 readme = "README.md"
 license = { file="LICENSE" }
```

### Comparing `django_simplefeedback-1.1.1/PKG-INFO` & `django_simplefeedback-1.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-simplefeedback
-Version: 1.1.1
+Version: 1.1.2
 Summary: A simple Django app to handle user tickets.
 Project-URL: Homepage, https://github.com/pulilab/django-simple-feedback
 Project-URL: Bug Tracker, https://github.com/pulilab/django-simple-feedback/issues
 Author-email: Zoltan Ilcsik <zi@pulilab.com>, Fekete Gyorgy <f@pulilab.com>
 License-File: LICENSE
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

