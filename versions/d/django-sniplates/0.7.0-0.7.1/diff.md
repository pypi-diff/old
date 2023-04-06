# Comparing `tmp/django-sniplates-0.7.0.tar.gz` & `tmp/django_sniplates-0.7.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/django-sniplates-0.7.0.tar", last modified: Wed Jan 22 21:01:20 2020, max compression
+gzip compressed data, was "django_sniplates-0.7.1.tar", max compression
```

## Comparing `django-sniplates-0.7.0.tar` & `django_sniplates-0.7.1.tar`

### file list

```diff
@@ -1,33 +1,8 @@
-drwxr-xr-x   0 curtis    (1000) curtis    (1000)        0 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/
-drwxr-xr-x   0 curtis    (1000) curtis    (1000)        0 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/docs/
--rw-r--r--   0 curtis    (1000) curtis    (1000)     2380 2020-01-21 21:11:57.000000 django-sniplates-0.7.0/docs/index.rst
--rw-r--r--   0 curtis    (1000) curtis    (1000)     6719 2015-06-16 05:46:32.000000 django-sniplates-0.7.0/docs/make.bat
--rw-r--r--   0 curtis    (1000) curtis    (1000)     3794 2018-12-30 21:55:10.000000 django-sniplates-0.7.0/docs/changelog.rst
--rw-r--r--   0 curtis    (1000) curtis    (1000)      318 2016-01-24 06:58:53.000000 django-sniplates-0.7.0/docs/filters.rst
--rw-r--r--   0 curtis    (1000) curtis    (1000)      311 2015-06-16 05:46:32.000000 django-sniplates-0.7.0/docs/formulation.rst
--rw-r--r--   0 curtis    (1000) curtis    (1000)     6798 2015-06-16 05:46:32.000000 django-sniplates-0.7.0/docs/Makefile
--rw-r--r--   0 curtis    (1000) curtis    (1000)     8236 2015-08-21 10:11:06.000000 django-sniplates-0.7.0/docs/conf.py
--rw-r--r--   0 curtis    (1000) curtis    (1000)     5075 2016-06-27 23:47:25.000000 django-sniplates-0.7.0/docs/tags.rst
--rw-r--r--   0 curtis    (1000) curtis    (1000)     2808 2016-01-24 21:34:19.000000 django-sniplates-0.7.0/docs/extractor.rst
--rw-r--r--   0 curtis    (1000) curtis    (1000)      205 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/setup.cfg
--rw-r--r--   0 curtis    (1000) curtis    (1000)      161 2016-11-27 22:31:07.000000 django-sniplates-0.7.0/README.md
-drwxr-xr-x   0 curtis    (1000) curtis    (1000)        0 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/django_sniplates.egg-info/
--rw-r--r--   0 curtis    (1000) curtis    (1000)      579 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/django_sniplates.egg-info/SOURCES.txt
--rw-r--r--   0 curtis    (1000) curtis    (1000)      830 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/django_sniplates.egg-info/PKG-INFO
--rw-r--r--   0 curtis    (1000) curtis    (1000)        1 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/django_sniplates.egg-info/not-zip-safe
--rw-r--r--   0 curtis    (1000) curtis    (1000)        1 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/django_sniplates.egg-info/dependency_links.txt
--rw-r--r--   0 curtis    (1000) curtis    (1000)       12 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/django_sniplates.egg-info/requires.txt
--rw-r--r--   0 curtis    (1000) curtis    (1000)       10 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/django_sniplates.egg-info/top_level.txt
--rw-r--r--   0 curtis    (1000) curtis    (1000)      830 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/PKG-INFO
--rw-r--r--   0 curtis    (1000) curtis    (1000)     1081 2015-06-16 05:48:22.000000 django-sniplates-0.7.0/LICENSE
--rw-r--r--   0 curtis    (1000) curtis    (1000)     1092 2020-01-21 21:09:55.000000 django-sniplates-0.7.0/setup.py
--rw-r--r--   0 curtis    (1000) curtis    (1000)      211 2015-08-21 10:04:57.000000 django-sniplates-0.7.0/MANIFEST.in
-drwxr-xr-x   0 curtis    (1000) curtis    (1000)        0 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/sniplates/
--rw-r--r--   0 curtis    (1000) curtis    (1000)        0 2015-06-16 05:48:22.000000 django-sniplates-0.7.0/sniplates/__init__.py
-drwxr-xr-x   0 curtis    (1000) curtis    (1000)        0 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/sniplates/templates/
-drwxr-xr-x   0 curtis    (1000) curtis    (1000)        0 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/sniplates/templates/sniplates/
--rw-r--r--   0 curtis    (1000) curtis    (1000)     5802 2018-08-08 02:43:21.000000 django-sniplates-0.7.0/sniplates/templates/sniplates/django.html
-drwxr-xr-x   0 curtis    (1000) curtis    (1000)        0 2020-01-22 21:01:20.000000 django-sniplates-0.7.0/sniplates/templatetags/
--rw-r--r--   0 curtis    (1000) curtis    (1000)    14615 2020-01-21 21:06:55.000000 django-sniplates-0.7.0/sniplates/templatetags/sniplates.py
--rw-r--r--   0 curtis    (1000) curtis    (1000)        0 2015-06-16 05:48:22.000000 django-sniplates-0.7.0/sniplates/templatetags/__init__.py
--rwxr-xr-x   0 curtis    (1000) curtis    (1000)      864 2018-08-08 11:56:34.000000 django-sniplates-0.7.0/runtests.py
+-rw-r--r--   0        0        0     1081 2015-06-16 05:48:22.120258 django_sniplates-0.7.1/LICENSE
+-rw-r--r--   0        0        0      161 2016-11-27 22:31:07.075991 django_sniplates-0.7.1/README.md
+-rw-r--r--   0        0        0      970 2023-04-06 11:45:12.505301 django_sniplates-0.7.1/pyproject.toml
+-rw-r--r--   0        0        0        0 2020-05-03 23:01:36.827240 django_sniplates-0.7.1/src/sniplates/__init__.py
+-rw-r--r--   0        0        0     5802 2020-05-03 23:01:36.827240 django_sniplates-0.7.1/src/sniplates/templates/sniplates/django.html
+-rw-r--r--   0        0        0        0 2020-05-03 23:01:36.827240 django_sniplates-0.7.1/src/sniplates/templatetags/__init__.py
+-rw-r--r--   0        0        0    14608 2022-06-09 22:49:27.230952 django_sniplates-0.7.1/src/sniplates/templatetags/sniplates.py
+-rw-r--r--   0        0        0     1400 1970-01-01 00:00:00.000000 django_sniplates-0.7.1/PKG-INFO
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `django-sniplates-0.7.0/django_sniplates.egg-info/PKG-INFO` & `django_sniplates-0.7.1/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,23 +1,38 @@
-Metadata-Version: 1.1
+Metadata-Version: 2.1
 Name: django-sniplates
-Version: 0.7.0
+Version: 0.7.1
 Summary: Efficient template macro sets for Django
-Home-page: http://github.com/funkybob/django-sniplates
+License: MIT
+Keywords: django,templates,forms
 Author: Curtis Maloney
 Author-email: curtis@tinbrain.net
-License: UNKNOWN
-Description: UNKNOWN
-Keywords: django,templates,forms
-Platform: UNKNOWN
+Requires-Python: >=3.6,<4.0
 Classifier: Environment :: Web Environment
 Classifier: Framework :: Django
 Classifier: Framework :: Django :: 2.2
 Classifier: Framework :: Django :: 3.0
 Classifier: License :: OSI Approved :: BSD License
+Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
-Classifier: Programming Language :: Python :: 3.5
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.6
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
-Requires: Django (>=2.2)
+Requires-Dist: django (>=3.0.5,<4.0.0)
+Project-URL: Documentation, https://sniplates.readthedocs.io/en/latest/
+Description-Content-Type: text/markdown
+
+django-sniplates
+================
+
+Template snippet libraries for Django
+
+Read the documentation at [Read The Docs](https://sniplates.readthedocs.io/en/latest/)
+
```

### Comparing `django-sniplates-0.7.0/LICENSE` & `django_sniplates-0.7.1/LICENSE`

 * *Files identical despite different names*

### Comparing `django-sniplates-0.7.0/sniplates/templates/sniplates/django.html` & `django_sniplates-0.7.1/src/sniplates/templates/sniplates/django.html`

 * *Files identical despite different names*

### Comparing `django-sniplates-0.7.0/sniplates/templatetags/sniplates.py` & `django_sniplates-0.7.1/src/sniplates/templatetags/sniplates.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 
 from django import template
 from django.forms.utils import flatatt
 from django.forms.widgets import DateTimeBaseInput
 from django.template.base import token_kwargs
 from django.template.loader import get_template
 from django.template.loader_tags import BLOCK_CONTEXT_KEY, BlockContext, BlockNode, ExtendsNode
-from django.utils.encoding import force_text
+from django.utils.encoding import force_str
 from django.utils.functional import cached_property
 
 register = template.Library()
 
 '''
 Sniplates
 
@@ -254,15 +254,15 @@
 class ChoiceWrapper(tuple):
 
     def __new__(cls, value=None, display=None):
         tuple_args = [value, display]
         return super(ChoiceWrapper, cls).__new__(cls, tuple(tuple_args))
 
     def __init__(self, value, display):
-        self.value = force_text(value)
+        self.value = force_str(value)
         self._display = display
 
     def __repr__(self):
         return 'ChoiceWrapper(value=%s, display=%s)' % (self.value, self.display)
 
     def __iter__(self):
         # overriden from tuple to retrun the formatted display
@@ -271,19 +271,19 @@
 
     def is_group(self):
         return isinstance(self._display, (list, tuple))
 
     @property
     def display(self):
         """
-        When dealing with optgroups, ensure that the value is properly force_text'd.
+        When dealing with optgroups, ensure that the value is properly force_str'd.
         """
         if not self.is_group():
             return self._display
-        return ((force_text(k), v) for k, v in self._display)
+        return ((force_str(k), v) for k, v in self._display)
 
 
 class FieldExtractor(dict):
     '''
     Base class for extracting Field details.
     Acts as a dict so we can push it on the context stack.
     '''
@@ -315,16 +315,16 @@
     @cached_property
     def raw_value(self):
         return self.form_field.value()
 
     @cached_property
     def value(self):
         if isinstance(self.raw_value, (tuple, list)):
-            return [force_text(bit) for bit in self.raw_value]
-        return force_text(self.raw_value)
+            return [force_str(bit) for bit in self.raw_value]
+        return force_str(self.raw_value)
 
     @cached_property
     def initial(self):
         data = self.form_field.form.initial.get(self.form_field.name, self.form_field.field.initial)
         if callable(data):
             data = data()
             # If this is an auto-generated default date, nix the
@@ -415,15 +415,15 @@
     @cached_property
     def choices(self):
         c = self['widget'].choices
         if not c:
             return c
 
         return tuple(
-            ChoiceWrapper(value=force_text(k), display=v)
+            ChoiceWrapper(value=force_str(k), display=v)
             for k, v in c
         )
 
 
 class DateTimeBaseExtractor(FieldExtractor):
     """
     Applies the date/time/datetime formatting to the value.
```

