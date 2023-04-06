# Comparing `tmp/plone.schema-1.4.0.tar.gz` & `tmp/plone.schema-2.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/plone.schema-1.4.0.tar", last modified: Thu Apr 28 16:22:37 2022, max compression
+gzip compressed data, was "plone.schema-2.0.0.tar", last modified: Thu Apr  6 09:41:59 2023, max compression
```

## Comparing `plone.schema-1.4.0.tar` & `plone.schema-2.0.0.tar`

### file list

```diff
@@ -1,39 +1,40 @@
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-04-28 16:22:37.000000 plone.schema-1.4.0/
--rw-r--r--   0 maurits    (501) staff       (20)     2967 2022-04-28 16:22:37.000000 plone.schema-1.4.0/PKG-INFO
--rw-r--r--   0 maurits    (501) staff       (20)       70 2022-04-28 16:22:36.000000 plone.schema-1.4.0/CONTRIBUTING.rst
--rw-r--r--   0 maurits    (501) staff       (20)      397 2022-04-28 16:22:36.000000 plone.schema-1.4.0/pyproject.toml
--rw-r--r--   0 maurits    (501) staff       (20)      162 2022-04-28 16:22:36.000000 plone.schema-1.4.0/MANIFEST.in
--rw-r--r--   0 maurits    (501) staff       (20)     1610 2022-04-28 16:22:36.000000 plone.schema-1.4.0/setup.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone.schema.egg-info/
--rw-r--r--   0 maurits    (501) staff       (20)     2967 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone.schema.egg-info/PKG-INFO
--rw-r--r--   0 maurits    (501) staff       (20)        1 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone.schema.egg-info/not-zip-safe
--rw-r--r--   0 maurits    (501) staff       (20)        6 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone.schema.egg-info/namespace_packages.txt
--rw-r--r--   0 maurits    (501) staff       (20)      853 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone.schema.egg-info/SOURCES.txt
--rw-r--r--   0 maurits    (501) staff       (20)      140 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone.schema.egg-info/requires.txt
--rw-r--r--   0 maurits    (501) staff       (20)        6 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone.schema.egg-info/top_level.txt
--rw-r--r--   0 maurits    (501) staff       (20)        1 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone.schema.egg-info/dependency_links.txt
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone/
--rw-r--r--   0 maurits    (501) staff       (20)      244 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone/schema/
--rw-r--r--   0 maurits    (501) staff       (20)     1679 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)     1956 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/jsonfield.py
--rw-r--r--   0 maurits    (501) staff       (20)      266 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/handler.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone/schema/tests/
--rw-r--r--   0 maurits    (501) staff       (20)      602 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/tests/test_doctests.py
--rw-r--r--   0 maurits    (501) staff       (20)       14 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/tests/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     1602 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone/schema/browser/
--rw-r--r--   0 maurits    (501) staff       (20)      842 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/browser/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)     1448 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/browser/jsonfield.py
--rw-r--r--   0 maurits    (501) staff       (20)        0 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/browser/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)      663 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/browser/email.py
--rw-r--r--   0 maurits    (501) staff       (20)      648 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/browser/uri.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2022-04-28 16:22:37.000000 plone.schema-1.4.0/plone/schema/browser/templates/
--rw-r--r--   0 maurits    (501) staff       (20)     1031 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/browser/templates/email_display.pt
--rw-r--r--   0 maurits    (501) staff       (20)     1014 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/browser/templates/uri_display.pt
--rw-r--r--   0 maurits    (501) staff       (20)      981 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/email.py
--rw-r--r--   0 maurits    (501) staff       (20)      836 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/editor.py
--rw-r--r--   0 maurits    (501) staff       (20)      255 2022-04-28 16:22:36.000000 plone.schema-1.4.0/plone/schema/path.py
--rw-r--r--   0 maurits    (501) staff       (20)      102 2022-04-28 16:22:37.000000 plone.schema-1.4.0/setup.cfg
--rw-r--r--   0 maurits    (501) staff       (20)       57 2022-04-28 16:22:36.000000 plone.schema-1.4.0/README.rst
--rw-r--r--   0 maurits    (501) staff       (20)     1311 2022-04-28 16:22:36.000000 plone.schema-1.4.0/CHANGES.rst
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 09:41:59.932867 plone.schema-2.0.0/
+-rw-r--r--   0 maurits    (501) staff       (20)     1935 2023-04-06 09:41:59.000000 plone.schema-2.0.0/CHANGES.rst
+-rw-r--r--   0 maurits    (501) staff       (20)       70 2023-04-06 09:41:59.000000 plone.schema-2.0.0/CONTRIBUTING.rst
+-rw-r--r--   0 maurits    (501) staff       (20)      162 2023-04-06 09:41:59.000000 plone.schema-2.0.0/MANIFEST.in
+-rw-r--r--   0 maurits    (501) staff       (20)     3536 2023-04-06 09:41:59.932990 plone.schema-2.0.0/PKG-INFO
+-rw-r--r--   0 maurits    (501) staff       (20)      617 2023-04-06 09:41:59.000000 plone.schema-2.0.0/README.rst
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 09:41:59.925217 plone.schema-2.0.0/plone/
+-rw-r--r--   0 maurits    (501) staff       (20)      245 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 09:41:59.929795 plone.schema-2.0.0/plone/schema/
+-rw-r--r--   0 maurits    (501) staff       (20)     1524 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 09:41:59.931331 plone.schema-2.0.0/plone/schema/browser/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/browser/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)      835 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/browser/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)      697 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/browser/email.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1474 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/browser/jsonfield.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 09:41:59.931982 plone.schema-2.0.0/plone/schema/browser/templates/
+-rw-r--r--   0 maurits    (501) staff       (20)      862 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/browser/templates/email_display.pt
+-rw-r--r--   0 maurits    (501) staff       (20)      845 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/browser/templates/uri_display.pt
+-rw-r--r--   0 maurits    (501) staff       (20)      618 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/browser/uri.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1541 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)      862 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/editor.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1010 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/email.py
+-rw-r--r--   0 maurits    (501) staff       (20)      243 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/handler.py
+-rw-r--r--   0 maurits    (501) staff       (20)      158 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/interfaces.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1899 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/jsonfield.py
+-rw-r--r--   0 maurits    (501) staff       (20)      255 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/path.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 09:41:59.932621 plone.schema-2.0.0/plone/schema/tests/
+-rw-r--r--   0 maurits    (501) staff       (20)       14 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/tests/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)      146 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone/schema/tests/test_doctests.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 09:41:59.927362 plone.schema-2.0.0/plone.schema.egg-info/
+-rw-r--r--   0 maurits    (501) staff       (20)     3536 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone.schema.egg-info/PKG-INFO
+-rw-r--r--   0 maurits    (501) staff       (20)      880 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone.schema.egg-info/SOURCES.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        1 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone.schema.egg-info/dependency_links.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        6 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone.schema.egg-info/namespace_packages.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        1 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone.schema.egg-info/not-zip-safe
+-rw-r--r--   0 maurits    (501) staff       (20)      124 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone.schema.egg-info/requires.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        6 2023-04-06 09:41:59.000000 plone.schema-2.0.0/plone.schema.egg-info/top_level.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     1704 2023-04-06 09:41:59.000000 plone.schema-2.0.0/pyproject.toml
+-rw-r--r--   0 maurits    (501) staff       (20)      268 2023-04-06 09:41:59.933504 plone.schema-2.0.0/setup.cfg
+-rw-r--r--   0 maurits    (501) staff       (20)     1544 2023-04-06 09:41:59.000000 plone.schema-2.0.0/setup.py
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `plone.schema-1.4.0/setup.py` & `plone.schema-2.0.0/setup.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,53 +1,49 @@
-from setuptools import setup, find_packages
+from setuptools import find_packages
+from setuptools import setup
 
-version = '1.4.0'
 
-long_description = open("README.rst").read() + "\n" + \
-                   open("CHANGES.rst").read()
+version = "2.0.0"
+
+long_description = open("README.rst").read() + "\n" + open("CHANGES.rst").read()
 
 setup(
-    name='plone.schema',
+    name="plone.schema",
     version=version,
-    description='Plone specific extensions and fields for zope schematas',
+    description="Plone specific extensions and fields for zope schematas",
     long_description=long_description,
     classifiers=[
         "Development Status :: 5 - Production/Stable",
-        "Framework :: Zope2",
-        "Framework :: Zope :: 4",
+        "Framework :: Zope :: 5",
         "Framework :: Plone",
-        "Framework :: Plone :: 5.0",
-        "Framework :: Plone :: 5.1",
-        "Framework :: Plone :: 5.2",
+        "Framework :: Plone :: 6.0",
         "Framework :: Plone :: Core",
         "Programming Language :: Python",
-        "Programming Language :: Python :: 2.7",
-        "Programming Language :: Python :: 3.6",
-        "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
+        "Programming Language :: Python :: 3.9",
+        "Programming Language :: Python :: 3.10",
+        "Programming Language :: Python :: 3.11",
         "Topic :: Software Development :: Libraries :: Python Modules",
         "License :: OSI Approved :: BSD License",
     ],
-    keywords='plone schema',
-    author='Plone Foundation',
-    author_email='plone-developers@lists.sourceforge.net',
-    url='http://plone.org/',
-    license='BSD',
+    keywords="schema z3cform email uri json field widget",
+    author="Plone Foundation",
+    author_email="plone-developers@lists.sourceforge.net",
+    url="https://github.com/plone/plone.schema",
+    license="BSD",
     packages=find_packages(),
-    namespace_packages=['plone'],
+    namespace_packages=["plone"],
     include_package_data=True,
     zip_safe=False,
+    python_requires=">=3.8",
     install_requires=[
-        'setuptools',
-        'plone.app.z3cform',
-        'jsonschema',
-        'z3c.form',
-        'zope.component',
-        'zope.i18nmessageid',
-        'zope.interface',
-        'zope.schema',
+        "jsonschema",
+        "setuptools",
+        "z3c.form",
+        "zope.i18nmessageid",
     ],
-    extras_require={'test': [
-        'six',
-        'plone.app.testing'
-    ]},
+    extras_require={
+        "test": [],
+        "schemaeditor": ["plone.schemaeditor"],
+        "supermodel": ["plone.supermodel"],
+    },
 )
```

### Comparing `plone.schema-1.4.0/plone.schema.egg-info/SOURCES.txt` & `plone.schema-2.0.0/plone.schema.egg-info/SOURCES.txt`

 * *Files 9% similar despite different names*

```diff
@@ -14,14 +14,15 @@
 plone.schema.egg-info/requires.txt
 plone.schema.egg-info/top_level.txt
 plone/schema/__init__.py
 plone/schema/configure.zcml
 plone/schema/editor.py
 plone/schema/email.py
 plone/schema/handler.py
+plone/schema/interfaces.py
 plone/schema/jsonfield.py
 plone/schema/path.py
 plone/schema/browser/__init__.py
 plone/schema/browser/configure.zcml
 plone/schema/browser/email.py
 plone/schema/browser/jsonfield.py
 plone/schema/browser/uri.py
```

### Comparing `plone.schema-1.4.0/plone/schema/configure.zcml` & `plone.schema-2.0.0/plone/schema/configure.zcml`

 * *Files 6% similar despite different names*

```diff
@@ -1,61 +1,62 @@
 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:five="http://namespaces.zope.org/five"
     xmlns:i18n="http://namespaces.zope.org/i18n"
     xmlns:zcml="http://namespaces.zope.org/zcml"
-    i18n_domain="plone">
+    i18n_domain="plone"
+    >
 
-    <!-- Configure widgets if z3c.form is installed -->
-    <include zcml:condition="installed z3c.form" package=".browser" />
+  <!-- Configure widgets -->
+  <include package=".browser" />
 
-    <!-- Configure plone.supermodel support if available -->
-    <configure zcml:condition="installed plone.supermodel">
-      <utility
-          component=".handler.URIHandler"
-          name="plone.schema.URI"
-          />
-
-      <utility
-          component=".handler.EmailHandler"
-          name="plone.schema.email.Email"
-          />
-
-      <utility
-          component=".handler.JSONHandler"
-          name="plone.schema.jsonfield.JSONField"
-          />
-
-    </configure>
-
-    <!-- Configure plone.schemaeditor field factory if installed -->
-    <configure zcml:condition="installed plone.schemaeditor">
-      <class class="zope.schema.URI">
-        <implements interface=".editor.IURI" />
-      </class>
-
-      <class class="plone.schema.email.Email">
-        <implements interface=".editor.IEmail" />
-      </class>
-
-      <class class="plone.schema.jsonfield.JSONField">
-        <implements interface=".editor.IJSON" />
-      </class>
-
-      <utility
-          name="zope.schema._field.URI"
-          component=".editor.URIFactory"
-          />
-
-      <utility
-          name="plone.schema.email.Email"
-          component=".editor.EmailFactory"
-          />
-
-      <utility
-          name="plone.schema.jsonfield.JSONField"
-          component=".editor.JSONFactory"
-          />
+  <!-- Configure plone.supermodel support if available -->
+  <configure zcml:condition="installed plone.supermodel">
+    <utility
+        name="plone.schema.URI"
+        component=".handler.URIHandler"
+        />
+
+    <utility
+        name="plone.schema.email.Email"
+        component=".handler.EmailHandler"
+        />
+
+    <utility
+        name="plone.schema.jsonfield.JSONField"
+        component=".handler.JSONHandler"
+        />
+
+  </configure>
+
+  <!-- Configure plone.schemaeditor field factory if installed -->
+  <configure zcml:condition="installed plone.schemaeditor">
+    <class class="zope.schema.URI">
+      <implements interface=".editor.IURI" />
+    </class>
+
+    <class class="plone.schema.email.Email">
+      <implements interface=".editor.IEmail" />
+    </class>
+
+    <class class="plone.schema.jsonfield.JSONField">
+      <implements interface=".editor.IJSON" />
+    </class>
+
+    <utility
+        name="zope.schema._field.URI"
+        component=".editor.URIFactory"
+        />
+
+    <utility
+        name="plone.schema.email.Email"
+        component=".editor.EmailFactory"
+        />
+
+    <utility
+        name="plone.schema.jsonfield.JSONField"
+        component=".editor.JSONFactory"
+        />
 
-    </configure>
+  </configure>
 
 </configure>
```

### Comparing `plone.schema-1.4.0/plone/schema/jsonfield.py` & `plone.schema-2.0.0/plone/schema/jsonfield.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,24 +1,23 @@
-import ast
-import json
-import jsonschema
-from plone.schema import _
+from json import JSONDecodeError
+from zope.i18nmessageid import MessageFactory
 from zope.interface import Attribute
 from zope.interface import implementer
 from zope.schema import Field
 from zope.schema._bootstrapinterfaces import WrongType
 from zope.schema.interfaces import IField
-from zope.schema.interfaces import WrongContainedType
 from zope.schema.interfaces import IFromUnicode
+from zope.schema.interfaces import WrongContainedType
+
+import ast
+import json
+import jsonschema
+
 
-try:
-    from json import JSONDecodeError
-except ImportError:
-    # Python 2
-    JSONDecodeError = ValueError
+_ = MessageFactory("plone")
 
 
 DEFAULT_JSON_SCHEMA = json.dumps({"type": "object", "properties": {}})
 
 
 class IJSONField(IField):
     """A text field that stores A JSON."""
@@ -36,33 +35,33 @@
 
         self.widget = widget
 
         try:
             self.json_schema = json.loads(schema)
         except ValueError:
             raise WrongType
-        super(JSONField, self).__init__(**kw)
+        super().__init__(**kw)
 
     def _validate(self, value):
-        super(JSONField, self)._validate(value)
+        super()._validate(value)
 
         try:
             jsonschema.validate(value, self.json_schema)
         except jsonschema.ValidationError as e:
             raise WrongContainedType(e.message, self.__name__)
 
     def fromUnicode(self, value):
         """Get value from unicode.
 
         Value can be a valid JSON object:
 
             >>> JSONField().fromUnicode('{"items": []}')
             {'items': []}
 
-        or it can be a Pyhon dict stored as string:
+        or it can be a Python dict stored as string:
 
             >>> JSONField().fromUnicode("{'items': []}")
             {'items': []}
 
         """
         try:
             v = json.loads(value)
```

### Comparing `plone.schema-1.4.0/plone/schema/__init__.py` & `plone.schema-2.0.0/plone/schema/__init__.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,19 +1,13 @@
-from zope.i18nmessageid import MessageFactory
-_ = MessageFactory('plone')
-
-
 from .email import Email
 from .email import IEmail
-
-from .path import Path
-from .path import IPath
-
-from .jsonfield import JSONField
 from .jsonfield import IJSONField
+from .jsonfield import JSONField
+from .path import IPath
+from .path import Path
 
 # zope.schema convenience imports
 from zope.schema._field import ASCII
 from zope.schema._field import ASCIILine
 from zope.schema._field import Bool
 from zope.schema._field import Bytes
 from zope.schema._field import BytesLine
```

### Comparing `plone.schema-1.4.0/plone/schema/browser/configure.zcml` & `plone.schema-2.0.0/plone/schema/browser/configure.zcml`

 * *Files 16% similar despite different names*

```diff
@@ -1,30 +1,34 @@
 <configure
     xmlns="http://namespaces.zope.org/zope"
-    xmlns:z3c="http://namespaces.zope.org/z3c"
     xmlns:browser="http://namespaces.zope.org/browser"
-    i18n_domain="plone">
+    xmlns:z3c="http://namespaces.zope.org/z3c"
+    i18n_domain="plone"
+    >
 
-    <include package="z3c.form" file="meta.zcml" />
-    <include package="z3c.form" />
+  <include
+      package="z3c.form"
+      file="meta.zcml"
+      />
+  <include package="z3c.form" />
 
-    <adapter factory=".uri.URIFieldWidget" />
-    <adapter factory=".email.EmailFieldWidget" />
-    <adapter factory=".jsonfield.JSONFieldWidget" />
+  <adapter factory=".uri.URIFieldWidget" />
+  <adapter factory=".email.EmailFieldWidget" />
+  <adapter factory=".jsonfield.JSONFieldWidget" />
 
-    <z3c:widgetTemplate
-      mode="display"
+  <z3c:widgetTemplate
       widget=".uri.IURIWidget"
-      layer="z3c.form.interfaces.IFormLayer"
       template="templates/uri_display.pt"
+      layer="..interfaces.IFormLayer"
+      mode="display"
       />
 
-    <z3c:widgetTemplate
-      mode="display"
+  <z3c:widgetTemplate
       widget=".email.IEmailWidget"
-      layer="z3c.form.interfaces.IFormLayer"
       template="templates/email_display.pt"
+      layer="..interfaces.IFormLayer"
+      mode="display"
       />
 
-    <adapter factory=".jsonfield.JSONDataConverter" />
+  <adapter factory=".jsonfield.JSONDataConverter" />
 
 </configure>
```

### Comparing `plone.schema-1.4.0/plone/schema/browser/jsonfield.py` & `plone.schema-2.0.0/plone/schema/browser/jsonfield.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,54 +1,58 @@
-from zope.component import adapter
-from zope.interface import implementer
-from z3c.form.interfaces import ITextAreaWidget
-from z3c.form.interfaces import IFieldWidget
+from ..interfaces import IFormLayer
+from ..jsonfield import IJSONField
 from z3c.form.browser.textarea import TextAreaWidget
-from z3c.form.widget import FieldWidget
 from z3c.form.interfaces import IDataConverter
+from z3c.form.interfaces import IFieldWidget
+from z3c.form.interfaces import ITextAreaWidget
 from z3c.form.interfaces import IWidget
-from plone.app.z3cform.interfaces import IPloneFormLayer
+from z3c.form.widget import FieldWidget
+from zope.component import adapter
 from zope.component import adapts
-from plone.schema.jsonfield import IJSONField
+from zope.i18nmessageid import MessageFactory
+from zope.interface import implementer
 
 import json
 
 
+_ = MessageFactory("plone")
+
+
 class IJSONFieldWidget(ITextAreaWidget):
-    """ JSON Widget """
+    """JSON Widget"""
 
 
 @implementer(IJSONFieldWidget)
 class JSONWidget(TextAreaWidget):
-    klass = u'json-widget'
+    klass = "json-widget"
     value = None
 
 
-@adapter(IJSONField, IPloneFormLayer)
+@adapter(IJSONField, IFormLayer)
 @implementer(IFieldWidget)
 def JSONFieldWidget(field, request):
     return FieldWidget(field, JSONWidget(request))
 
 
 @implementer(IDataConverter)
-class JSONDataConverter(object):
+class JSONDataConverter:
     """A JSON data converter."""
 
     adapts(IJSONField, IWidget)
 
     def __init__(self, field, widget):
         self.field = field
         self.widget = widget
 
     def toWidgetValue(self, value):
         """See interfaces.IDataConverter"""
         if value is self.field.missing_value:
-            return u''
+            return ""
         return json.dumps(value, indent=True)
 
     def toFieldValue(self, value):
         """See interfaces.IDataConverter"""
 
-        if value == u'':
+        if value == "":
             return self.field.missing_value
 
         return self.field.fromUnicode(value)
```

### Comparing `plone.schema-1.4.0/plone/schema/browser/email.py` & `plone.schema-2.0.0/plone/schema/browser/email.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,26 +1,28 @@
-from zope.component import adapter
-from zope.interface import implementer
-from z3c.form.interfaces import ITextWidget
-from z3c.form.interfaces import IFieldWidget
+from ..email import IEmail
+from ..interfaces import IFormLayer
 from z3c.form.browser.text import TextWidget
+from z3c.form.interfaces import IFieldWidget
+from z3c.form.interfaces import ITextWidget
 from z3c.form.widget import FieldWidget
+from zope.component import adapter
+from zope.i18nmessageid import MessageFactory
+from zope.interface import implementer
 
-from plone.app.z3cform.interfaces import IPloneFormLayer
 
-from plone.schema.email import IEmail
+_ = MessageFactory("plone")
 
 
 class IEmailWidget(ITextWidget):
-    """ Email Widget """
+    """Email Widget"""
 
 
 @implementer(IEmailWidget)
 class EmailWidget(TextWidget):
-    klass = u'email-widget'
+    klass = "email-widget"
     value = None
 
 
-@adapter(IEmail, IPloneFormLayer)
+@adapter(IEmail, IFormLayer)
 @implementer(IFieldWidget)
 def EmailFieldWidget(field, request):
     return FieldWidget(field, EmailWidget(request))
```

### Comparing `plone.schema-1.4.0/plone/schema/browser/uri.py` & `plone.schema-2.0.0/plone/schema/browser/uri.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,25 +1,24 @@
+from ..interfaces import IFormLayer
 from z3c.form.browser.text import TextWidget
 from z3c.form.interfaces import IFieldWidget
 from z3c.form.interfaces import ITextWidget
 from z3c.form.widget import FieldWidget
 from zope.component import adapter
 from zope.interface import implementer
 from zope.schema.interfaces import IURI
 
-from plone.app.z3cform.interfaces import IPloneFormLayer
-
 
 class IURIWidget(ITextWidget):
-    """ URI Widget """
+    """URI Widget"""
 
 
 @implementer(IURIWidget)
 class URIWidget(TextWidget):
-    klass = u'uri-widget'
+    klass = "uri-widget"
     value = None
 
 
-@adapter(IURI, IPloneFormLayer)
+@adapter(IURI, IFormLayer)
 @implementer(IFieldWidget)
 def URIFieldWidget(field, request):
     return FieldWidget(field, URIWidget(request))
```

### Comparing `plone.schema-1.4.0/plone/schema/browser/templates/email_display.pt` & `plone.schema-2.0.0/plone/schema/browser/templates/email_display.pt`

 * *Files 16% similar despite different names*

```diff
@@ -1,24 +1,32 @@
 <html xmlns="http://www.w3.org/1999/xhtml"
       xmlns:tal="http://xml.zope.org/namespaces/tal"
-      tal:omit-tag="">
-    <span id="" class=""
-          tal:attributes="id view/id;
-                          class view/klass;
-                          style view/style;
-                          title view/title;
-                          lang view/lang;
-                          onclick view/onclick;
-                          ondblclick view/ondblclick;
-                          onmousedown view/onmousedown;
-                          onmouseup view/onmouseup;
-                          onmouseover view/onmouseover;
-                          onmousemove view/onmousemove;
-                          onmouseout view/onmouseout;
-                          onkeypress view/onkeypress;
-                          onkeydown view/onkeydown;
-                          onkeyup view/onkeyup">
-    <a tal:condition="view/value" 
+      tal:omit-tag=""
+>
+  <span class=""
+        id=""
+        tal:attributes="
+          id view/id;
+          class view/klass;
+          style view/style;
+          title view/title;
+          lang view/lang;
+          onclick view/onclick;
+          ondblclick view/ondblclick;
+          onmousedown view/onmousedown;
+          onmouseup view/onmouseup;
+          onmouseover view/onmouseover;
+          onmousemove view/onmousemove;
+          onmouseout view/onmouseout;
+          onkeypress view/onkeypress;
+          onkeydown view/onkeydown;
+          onkeyup view/onkeyup;
+        "
+  >
+    <a tal:condition="view/value"
        tal:content="view/value"
-       tal:attributes="href string:mailto:${view/value}"/>
+       tal:attributes="
+         href string:mailto:${view/value};
+       "
+    ></a>
   </span>
 </html>
```

### Comparing `plone.schema-1.4.0/plone/schema/browser/templates/uri_display.pt` & `plone.schema-2.0.0/plone/schema/browser/templates/uri_display.pt`

 * *Files 9% similar despite different names*

```diff
@@ -1,24 +1,32 @@
 <html xmlns="http://www.w3.org/1999/xhtml"
       xmlns:tal="http://xml.zope.org/namespaces/tal"
-      tal:omit-tag="">
-    <span id="" class=""
-          tal:attributes="id view/id;
-                          class view/klass;
-                          style view/style;
-                          title view/title;
-                          lang view/lang;
-                          onclick view/onclick;
-                          ondblclick view/ondblclick;
-                          onmousedown view/onmousedown;
-                          onmouseup view/onmouseup;
-                          onmouseover view/onmouseover;
-                          onmousemove view/onmousemove;
-                          onmouseout view/onmouseout;
-                          onkeypress view/onkeypress;
-                          onkeydown view/onkeydown;
-                          onkeyup view/onkeyup">
-    <a tal:condition="view/value" 
+      tal:omit-tag=""
+>
+  <span class=""
+        id=""
+        tal:attributes="
+          id view/id;
+          class view/klass;
+          style view/style;
+          title view/title;
+          lang view/lang;
+          onclick view/onclick;
+          ondblclick view/ondblclick;
+          onmousedown view/onmousedown;
+          onmouseup view/onmouseup;
+          onmouseover view/onmouseover;
+          onmousemove view/onmousemove;
+          onmouseout view/onmouseout;
+          onkeypress view/onkeypress;
+          onkeydown view/onkeydown;
+          onkeyup view/onkeyup;
+        "
+  >
+    <a tal:condition="view/value"
        tal:content="view/value"
-       tal:attributes="href view/value"/>
+       tal:attributes="
+         href view/value;
+       "
+    ></a>
   </span>
 </html>
```

### Comparing `plone.schema-1.4.0/plone/schema/email.py` & `plone.schema-2.0.0/plone/schema/email.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,36 +1,38 @@
-from plone.schema import _
+from zope.i18nmessageid import MessageFactory
 from zope.interface import implementer
 from zope.schema import NativeStringLine
 from zope.schema.interfaces import IFromUnicode
 from zope.schema.interfaces import INativeStringLine
 from zope.schema.interfaces import ValidationError
+
 import re
 
+
+_ = MessageFactory("plone")
+
 # Taken from http://www.regular-expressions.info/email.html
 _isemail = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}"
 _isemail = re.compile(_isemail).match
 
 
 class IEmail(INativeStringLine):
-    """A field containing an email address
-    """
+    """A field containing an email address"""
 
 
 class InvalidEmail(ValidationError):
     __doc__ = _("""The specified email is not valid.""")
 
 
 @implementer(IEmail, IFromUnicode)
 class Email(NativeStringLine):
-    """Email schema field
-    """
+    """Email schema field"""
 
     def _validate(self, value):
-        super(Email, self)._validate(value)
+        super()._validate(value)
         if _isemail(value):
             return
 
         raise InvalidEmail(value)
 
     def fromUnicode(self, value):
         v = str(value.strip())
```

### Comparing `plone.schema-1.4.0/plone/schema/editor.py` & `plone.schema-2.0.0/plone/schema/editor.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,30 +1,32 @@
-from plone.schema import _
-from plone.schema.email import Email, IEmail
+from .email import Email
+from .email import IEmail
+from .jsonfield import IJSONField
+from .jsonfield import JSONField
 from plone.schemaeditor.fields import FieldFactory
+from zope.i18nmessageid import MessageFactory
 from zope.interface import Attribute
 from zope.schema import URI
 from zope.schema.interfaces import IURI
-from plone.schema.jsonfield import IJSONField
-from plone.schema.jsonfield import JSONField
 
 
-class IURI(IURI):
+_ = MessageFactory("plone")
+
 
+class IURI(IURI):
     # prevent some settings from being included in the field edit form
-    default = Attribute('')
+    default = Attribute("")
 
 
 class IEmail(IEmail):
-
     # prevent some settings from being included in the field edit form
-    default = Attribute('')
+    default = Attribute("")
 
 
 class IJSON(IJSONField):
     # prevent some settings from being included in the field edit form
-    default = Attribute('')
+    default = Attribute("")
 
 
-URIFactory = FieldFactory(URI, _(u'URL'))
-EmailFactory = FieldFactory(Email, _(u'Email'))
-JSONFactory = FieldFactory(JSONField, _(u'JSONField'))
+URIFactory = FieldFactory(URI, _("URL"))
+EmailFactory = FieldFactory(Email, _("Email"))
+JSONFactory = FieldFactory(JSONField, _("JSONField"))
```

