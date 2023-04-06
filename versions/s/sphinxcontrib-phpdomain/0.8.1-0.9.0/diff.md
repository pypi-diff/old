# Comparing `tmp/sphinxcontrib-phpdomain-0.8.1.tar.gz` & `tmp/sphinxcontrib-phpdomain-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/sphinxcontrib-phpdomain-0.8.1.tar", last modified: Sun Jul 24 03:24:02 2022, max compression
+gzip compressed data, was "dist/sphinxcontrib-phpdomain-0.9.0.tar", last modified: Thu Aug 11 02:34:30 2022, max compression
```

## Comparing `sphinxcontrib-phpdomain-0.8.1.tar` & `sphinxcontrib-phpdomain-0.9.0.tar`

### file list

```diff
@@ -1,40 +1,40 @@
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/.github/
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/.github/workflows/
--rw-rw-r--   0 mark      (1000) mark      (1000)      598 2021-12-11 02:56:56.000000 sphinxcontrib-phpdomain-0.8.1/.github/workflows/ci.yml
--rw-rw-r--   0 mark      (1000) mark      (1000)       52 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/.gitignore
--rw-rw-r--   0 mark      (1000) mark      (1000)     2342 2022-07-24 03:23:36.000000 sphinxcontrib-phpdomain-0.8.1/CHANGES
--rw-rw-r--   0 mark      (1000) mark      (1000)     1418 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/LICENSE
--rw-rw-r--   0 mark      (1000) mark      (1000)       68 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/MANIFEST.in
--rw-rw-r--   0 mark      (1000) mark      (1000)      813 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/PKG-INFO
--rw-rw-r--   0 mark      (1000) mark      (1000)     2468 2020-08-05 05:24:02.000000 sphinxcontrib-phpdomain-0.8.1/README.rst
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/doc/
--rw-rw-r--   0 mark      (1000) mark      (1000)     4701 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/doc/Makefile
--rw-rw-r--   0 mark      (1000) mark      (1000)     6988 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/doc/conf.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      170 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/doc/index.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     4172 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/doc/make.bat
--rw-rw-r--   0 mark      (1000) mark      (1000)     4731 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/doc/reference.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)       18 2021-12-11 02:56:56.000000 sphinxcontrib-phpdomain-0.8.1/requirements.txt
--rw-rw-r--   0 mark      (1000) mark      (1000)       76 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/setup.cfg
--rw-rw-r--   0 mark      (1000) mark      (1000)     1289 2022-07-24 03:22:52.000000 sphinxcontrib-phpdomain-0.8.1/setup.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/sphinxcontrib/
--rw-rw-r--   0 mark      (1000) mark      (1000)      365 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/sphinxcontrib/__init__.py
--rw-rw-r--   0 mark      (1000) mark      (1000)    26996 2022-07-24 03:19:19.000000 sphinxcontrib-phpdomain-0.8.1/sphinxcontrib/phpdomain.py
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/sphinxcontrib_phpdomain.egg-info/
--rw-rw-r--   0 mark      (1000) mark      (1000)      813 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/sphinxcontrib_phpdomain.egg-info/PKG-INFO
--rw-rw-r--   0 mark      (1000) mark      (1000)      719 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/sphinxcontrib_phpdomain.egg-info/SOURCES.txt
--rw-rw-r--   0 mark      (1000) mark      (1000)        1 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/sphinxcontrib_phpdomain.egg-info/dependency_links.txt
--rw-rw-r--   0 mark      (1000) mark      (1000)       14 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/sphinxcontrib_phpdomain.egg-info/namespace_packages.txt
--rw-rw-r--   0 mark      (1000) mark      (1000)        1 2020-08-05 05:26:58.000000 sphinxcontrib-phpdomain-0.8.1/sphinxcontrib_phpdomain.egg-info/not-zip-safe
--rw-rw-r--   0 mark      (1000) mark      (1000)       17 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/sphinxcontrib_phpdomain.egg-info/requires.txt
--rw-rw-r--   0 mark      (1000) mark      (1000)       14 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/sphinxcontrib_phpdomain.egg-info/top_level.txt
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/test/
--rw-rw-r--   0 mark      (1000) mark      (1000)     4701 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/test/Makefile
-drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-07-24 03:24:02.000000 sphinxcontrib-phpdomain-0.8.1/test/_static/
--rw-rw-r--   0 mark      (1000) mark      (1000)        0 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/test/_static/.gitignore
--rw-rw-r--   0 mark      (1000) mark      (1000)     7079 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/test/conf.py
--rw-rw-r--   0 mark      (1000) mark      (1000)      322 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/test/index.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     4172 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/test/make.bat
--rw-rw-r--   0 mark      (1000) mark      (1000)     8947 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/test/test_doc.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)     1147 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/test/test_doc2.rst
--rw-rw-r--   0 mark      (1000) mark      (1000)      545 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.8.1/test/test_nesting_regression.rst
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/.github/
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/.github/workflows/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      598 2021-12-11 02:56:56.000000 sphinxcontrib-phpdomain-0.9.0/.github/workflows/ci.yml
+-rw-rw-r--   0 mark      (1000) mark      (1000)       63 2022-08-11 02:32:39.000000 sphinxcontrib-phpdomain-0.9.0/.gitignore
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2450 2022-08-11 02:33:19.000000 sphinxcontrib-phpdomain-0.9.0/CHANGES
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1418 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/LICENSE
+-rw-rw-r--   0 mark      (1000) mark      (1000)       68 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/MANIFEST.in
+-rw-rw-r--   0 mark      (1000) mark      (1000)      813 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/PKG-INFO
+-rw-rw-r--   0 mark      (1000) mark      (1000)     2468 2020-08-05 05:24:02.000000 sphinxcontrib-phpdomain-0.9.0/README.rst
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/doc/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4701 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/doc/Makefile
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6988 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/doc/conf.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      170 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/doc/index.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4172 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/doc/make.bat
+-rw-rw-r--   0 mark      (1000) mark      (1000)     6538 2022-08-11 02:32:39.000000 sphinxcontrib-phpdomain-0.9.0/doc/reference.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)       18 2021-12-11 02:56:56.000000 sphinxcontrib-phpdomain-0.9.0/requirements.txt
+-rw-rw-r--   0 mark      (1000) mark      (1000)       76 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/setup.cfg
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1289 2022-08-11 02:33:27.000000 sphinxcontrib-phpdomain-0.9.0/setup.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/sphinxcontrib/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      365 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/sphinxcontrib/__init__.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)    28151 2022-08-11 02:32:39.000000 sphinxcontrib-phpdomain-0.9.0/sphinxcontrib/phpdomain.py
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/sphinxcontrib_phpdomain.egg-info/
+-rw-rw-r--   0 mark      (1000) mark      (1000)      813 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/sphinxcontrib_phpdomain.egg-info/PKG-INFO
+-rw-rw-r--   0 mark      (1000) mark      (1000)      719 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/sphinxcontrib_phpdomain.egg-info/SOURCES.txt
+-rw-rw-r--   0 mark      (1000) mark      (1000)        1 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/sphinxcontrib_phpdomain.egg-info/dependency_links.txt
+-rw-rw-r--   0 mark      (1000) mark      (1000)       14 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/sphinxcontrib_phpdomain.egg-info/namespace_packages.txt
+-rw-rw-r--   0 mark      (1000) mark      (1000)        1 2020-08-05 05:26:58.000000 sphinxcontrib-phpdomain-0.9.0/sphinxcontrib_phpdomain.egg-info/not-zip-safe
+-rw-rw-r--   0 mark      (1000) mark      (1000)       17 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/sphinxcontrib_phpdomain.egg-info/requires.txt
+-rw-rw-r--   0 mark      (1000) mark      (1000)       14 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/sphinxcontrib_phpdomain.egg-info/top_level.txt
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/test/
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4701 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/test/Makefile
+drwxrwxr-x   0 mark      (1000) mark      (1000)        0 2022-08-11 02:34:30.000000 sphinxcontrib-phpdomain-0.9.0/test/_static/
+-rw-rw-r--   0 mark      (1000) mark      (1000)        0 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/test/_static/.gitignore
+-rw-rw-r--   0 mark      (1000) mark      (1000)     7079 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/test/conf.py
+-rw-rw-r--   0 mark      (1000) mark      (1000)      322 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/test/index.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     4172 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/test/make.bat
+-rw-rw-r--   0 mark      (1000) mark      (1000)    11742 2022-08-11 02:32:39.000000 sphinxcontrib-phpdomain-0.9.0/test/test_doc.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)     1147 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/test/test_doc2.rst
+-rw-rw-r--   0 mark      (1000) mark      (1000)      545 2020-08-05 05:23:31.000000 sphinxcontrib-phpdomain-0.9.0/test/test_nesting_regression.rst
```

### Comparing `sphinxcontrib-phpdomain-0.8.1/.github/workflows/ci.yml` & `sphinxcontrib-phpdomain-0.9.0/.github/workflows/ci.yml`

 * *Files identical despite different names*

### Comparing `sphinxcontrib-phpdomain-0.8.1/CHANGES` & `sphinxcontrib-phpdomain-0.9.0/CHANGES`

 * *Files 4% similar despite different names*

```diff
@@ -1,7 +1,13 @@
+0.9.0
+=====
+
+* Added support for PHP enums. Simple, Backed and Advanced enum declarations
+  are supported.
+
 0.8.1
 =====
 
 * Only show the method name for `:php:doc:` links on namespaced classes.
 
 0.8.0
 =====
```

### Comparing `sphinxcontrib-phpdomain-0.8.1/LICENSE` & `sphinxcontrib-phpdomain-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `sphinxcontrib-phpdomain-0.8.1/PKG-INFO` & `sphinxcontrib-phpdomain-0.9.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: sphinxcontrib-phpdomain
-Version: 0.8.1
+Version: 0.9.0
 Summary: Sphinx extension to enable documenting PHP code
 Home-page: https://github.com/markstory/sphinxcontrib-phpdomain
 Author: Mark Story
 Author-email: mark@mark-story.com
 License: BSD
 Download-URL: http://pypi.python.org/pypi/sphinxcontrib-phpdomain
 Description:
```

### Comparing `sphinxcontrib-phpdomain-0.8.1/README.rst` & `sphinxcontrib-phpdomain-0.9.0/README.rst`

 * *Files identical despite different names*

### Comparing `sphinxcontrib-phpdomain-0.8.1/doc/Makefile` & `sphinxcontrib-phpdomain-0.9.0/doc/Makefile`

 * *Files identical despite different names*

### Comparing `sphinxcontrib-phpdomain-0.8.1/doc/conf.py` & `sphinxcontrib-phpdomain-0.9.0/doc/conf.py`

 * *Files identical despite different names*

### Comparing `sphinxcontrib-phpdomain-0.8.1/doc/make.bat` & `sphinxcontrib-phpdomain-0.9.0/doc/make.bat`

 * *Files identical despite different names*

### Comparing `sphinxcontrib-phpdomain-0.8.1/doc/reference.rst` & `sphinxcontrib-phpdomain-0.9.0/doc/reference.rst`

 * *Files 21% similar despite different names*

```diff
@@ -46,14 +46,70 @@
    should follow or be nested inside this directive.
 
 .. rst:directive:: .. php:trait:: name
 
    Describe a trait.  Methods beloning to the trait should follow or be nested
    inside this directive.
 
+.. rst:directive:: .. php:enum:: name [ : type ]
+
+   Describes an enum. Cases, methods, and constants belonging to the enum
+   should be inside this directive's body::
+
+        .. php:enum:: Suit
+
+            In playing cards, a suit is one of the categories into which the
+            cards of a deck are divided.
+
+            .. php:case:: Hearts
+
+                Hearts is one of the four suits in playing cards.
+
+            .. php:case:: Diamonds
+
+                Diamonds is one of the four suits in playing cards.
+
+            .. php:case:: Clubs
+
+                Clubs is one of the four suits in playing cards.
+
+            .. php:case:: Spades
+
+                Spades is one of the four suits in playing cards.
+
+            .. php:method:: color() -> string
+
+                Returns "Red" for hearts and diamonds and "black" for clubs
+                and spades.
+
+            .. php:const:: Roses : Hearts
+
+                An alias for :php:case:`Suit::Hearts`.
+
+   You may describe a backed enum by specifying the optional enum type and
+   case values::
+
+        .. php:enum:: Suit : string
+
+            In playing cards, a suit is one of the categories into which the
+            cards of a deck are divided.
+
+            .. php:case:: Hearts : 'H'
+
+            .. php:case:: Diamonds : 'D'
+
+            .. php:case:: Clubs : 'C'
+
+            .. php:case:: Spades : 'S'
+
+.. rst:directive:: .. php:case:: name [ : value ]
+
+   Describes an enum case. If describing a backed enum case, you may also
+   provide the case value. See :rst:dir:`php:enum` for examples.
+
 .. rst:directive:: .. php:class:: name
 
    Describes a class.  Methods, attributes, and constants belonging to the class
    should be inside this directive's body::
 
         .. php:class:: MyClass
         
@@ -162,7 +218,18 @@
 
    Reference an interface.  A namespaced name may be used.
 
 .. rst:role:: php:trait
 
    Reference a trait. A namespaced name may be used.
 
+.. rst:role:: php:enum
+
+   Reference an enum. A namespaced name may be used::
+
+     :php:enum:`Example\\Suit`
+
+.. rst:role:: php:case
+
+   Reference an enum case. A namespace name may be used::
+
+     :php:case:`Example\\Suit::Hearts`
```

### Comparing `sphinxcontrib-phpdomain-0.8.1/setup.py` & `sphinxcontrib-phpdomain-0.9.0/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 This package contains the phpdomain Sphinx extension.
 
 This extension provides a PHP domain for sphinx
 '''
 
 setup(
     name='sphinxcontrib-phpdomain',
-    version='0.8.1',
+    version='0.9.0',
     url='https://github.com/markstory/sphinxcontrib-phpdomain',
     download_url='http://pypi.python.org/pypi/sphinxcontrib-phpdomain',
     license='BSD',
     author='Mark Story',
     author_email='mark@mark-story.com',
     description='Sphinx extension to enable documenting PHP code',
     long_description=long_desc,
```

### Comparing `sphinxcontrib-phpdomain-0.8.1/sphinxcontrib/phpdomain.py` & `sphinxcontrib-phpdomain-0.9.0/sphinxcontrib/phpdomain.py`

 * *Files 1% similar despite different names*

```diff
@@ -24,16 +24,17 @@
 
 php_sig_re = re.compile(
     r'''^ (public\ |protected\ |private\ )? # visibility
           (final\ |abstract\ |static\ )?    # modifiers
           ([\w.]*\:\:)?                     # class name(s)
           (\$?\w+)  \s*                     # thing name
           (?: \((.*)\)                      # optional: arguments
-          (?:\s* -> \s* (.*))?              # return annotation
-          )? $                              # and nothing more
+          (?:\s* -> \s* (.*))?)?            # return annotation
+          (?:\s* : \s* (.*))?               # backed enum type / case value
+          $                                 # and nothing more
           ''', re.VERBOSE)
 
 
 NS = '\\'
 
 separators = {
   'method': '::',
@@ -42,15 +43,17 @@
   'namespace': NS,
   'global': '',
   'const': '::',
   'attr': '::$',
   'exception': '',
   'staticmethod': '::',
   'interface': NS,
-  'trait': NS
+  'trait': NS,
+  'enum': NS,
+  'case': '::',
 }
 
 php_separator = re.compile(r"(\w+)?(?:[:]{2})?")
 
 
 def _pseudo_parse_arglist(signode, arglist):
     # type: (addnodes.desc_signature, unicode) -> None
@@ -153,15 +156,15 @@
         * it is stripped from the displayed name if present
         * it is added to the full name (return value) if not present
         """
         m = php_sig_re.match(sig)
         if m is None:
             raise ValueError
 
-        visibility, modifiers, name_prefix, name, arglist, retann = m.groups()
+        visibility, modifiers, name_prefix, name, arglist, retann, enumtype = m.groups()
 
         if not name_prefix:
             name_prefix = ""
 
         # determine module and class name (if applicable), as well as full name
         modname = self.options.get(
             'namespace', self.env.temp_data.get('php:namespace'))
@@ -187,15 +190,15 @@
                 classname = classname.rstrip('::')
                 fullname = name_prefix + classname + separator + name
             elif name_prefix:
                 classname = classname.rstrip('::')
                 fullname = name_prefix + name
 
             # Currently in a class, but not creating another class,
-            elif classname and not self.objtype in ['class', 'exception', 'interface', 'trait']:
+            elif classname and not self.objtype in ['class', 'exception', 'interface', 'trait', 'enum']:
                 if not self.env.temp_data['php:in_class']:
                     name_prefix = classname + separator
 
                 fullname = classname + separator + name
             else:
                 classname = ''
                 fullname = name
@@ -235,20 +238,24 @@
         signode += addnodes.desc_name(name, name)
         if not arglist:
             if self.needs_arglist():
                 # for callables, add an empty parameter list
                 signode += addnodes.desc_parameterlist()
             if retann:
                 signode += addnodes.desc_returns(retann, retann)
+            elif enumtype:
+                signode += addnodes.desc_returns(enumtype, enumtype)
             return fullname, name_prefix
 
         _pseudo_parse_arglist(signode, arglist)
 
         if retann:
             signode += addnodes.desc_returns(retann, retann)
+        elif enumtype:
+            signode += addnodes.desc_returns(enumtype, enumtype)
         return fullname, name_prefix
 
     def get_index_text(self, modname, name):
         """
         Return the text for the index entry of the object.
         """
         raise NotImplementedError('must be implemented in subclasses')
@@ -337,15 +344,15 @@
         else:
             return ''
 
 
 class PhpClasslike(PhpObject):
     """
     Description of a class-like object
-    (classes, exceptions, interfaces, traits).
+    (classes, exceptions, interfaces, traits, enums).
     """
 
     def get_signature_prefix(self, sig):
         return self.objtype + ' '
 
     def get_index_text(self, modname, name_cls):
         if self.objtype == 'class':
@@ -356,14 +363,18 @@
             if not modname:
                 return _('%s (interface)') % name_cls[0]
             return _('%s (interface in %s)') % (name_cls[0], modname)
         elif self.objtype == 'trait':
             if not modname:
                 return _('%s (trait)') % name_cls[0]
             return _('%s (trait in %s)') % (name_cls[0], modname)
+        elif self.objtype == 'enum':
+            if not modname:
+                return _('%s (enum)') % name_cls[0]
+            return _('%s (enum in %s)') % (name_cls[0], modname)
         elif self.objtype == 'exception':
             return name_cls[0]
         else:
             return ''
 
     def after_content(self):
         self.env.temp_data['php:in_class'] = False
@@ -380,24 +391,26 @@
     """
 
     def get_signature_prefix(self, sig):
         if self.objtype == 'attr':
             return _('property ')
         if self.objtype == 'staticmethod':
             return _('static ')
+        if self.objtype == 'case':
+            return _('case ')
         return ''
 
     def needs_arglist(self):
         return self.objtype == 'method'
 
     def get_index_text(self, modname, name_cls):
         name, cls = name_cls
         add_modules = self.env.config.add_module_names
 
-        if self.objtype.endswith('method') or self.objtype == 'attr':
+        if self.objtype.endswith('method') or self.objtype == 'attr' or self.objtype == 'case':
             try:
                 clsname, propname = php_rsplit(name)
             except ValueError:
                 propname = name
                 clsname = None
 
         if self.objtype.endswith('method'):
@@ -410,14 +423,21 @@
         elif self.objtype == 'attr':
             if modname and clsname is None:
                 return _('%s (in namespace %s)') % (name, modname)
             elif modname and add_modules:
                 return _('%s (%s\\%s property)') % (propname, modname, clsname)
             else:
                 return _('%s (%s property)') % (propname, clsname)
+        elif self.objtype == 'case':
+            if modname and clsname is None:
+                return _('%s enum case') % (name)
+            elif modname and add_modules:
+                return _('%s (%s\\%s enum case)') % (propname, modname, clsname)
+            else:
+                return _('%s (%s enum case)') % (propname, clsname)
         else:
             return ''
 
 
 class PhpNamespace(Directive):
     """
     Directive to start a new PHP namespace, which are similar to modules.
@@ -582,27 +602,31 @@
         'method': ObjType(_('method'), 'meth', 'obj'),
         'class': ObjType(_('class'), 'class', 'obj'),
         'attr': ObjType(_('attribute'), 'attr', 'obj'),
         'exception': ObjType(_('exception'), 'exc', 'obj'),
         'namespace': ObjType(_('namespace'), 'ns', 'obj'),
         'interface': ObjType(_('interface'), 'interface', 'obj'),
         'trait': ObjType(_('trait'), 'trait', 'obj'),
+        'enum': ObjType(_('enum'), 'enum', 'obj'),
+        'case': ObjType(_('case'), 'case', 'obj'),
     }
 
     directives = {
         'function': PhpNamespacelevel,
         'global': PhpGloballevel,
         'const': PhpNamespacelevel,
         'class': PhpClasslike,
         'method': PhpClassmember,
         'staticmethod': PhpClassmember,
         'attr': PhpClassmember,
+        'case': PhpClassmember,
         'exception': PhpClasslike,
         'interface': PhpClasslike,
         'trait': PhpClasslike,
+        'enum': PhpClasslike,
         'namespace': PhpNamespace,
         'currentmodule': PhpCurrentNamespace,
         'currentnamespace': PhpCurrentNamespace,
     }
 
     roles = {
         'func': PhpXRefRole(fix_parens=False),
@@ -612,14 +636,16 @@
         'meth': PhpXRefRole(fix_parens=False),
         'attr': PhpXRefRole(),
         'const': PhpXRefRole(),
         'ns': PhpXRefRole(),
         'obj': PhpXRefRole(),
         'interface': PhpXRefRole(),
         'trait': PhpXRefRole(),
+        'enum': PhpXRefRole(),
+        'case': PhpXRefRole(),
     }
 
     initial_data = {
         'objects': {},  # fullname -> docname, objtype
         'namespaces': {},  # namespace -> docname, synopsis
     }
     indices = [
```

### Comparing `sphinxcontrib-phpdomain-0.8.1/sphinxcontrib_phpdomain.egg-info/PKG-INFO` & `sphinxcontrib-phpdomain-0.9.0/sphinxcontrib_phpdomain.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: sphinxcontrib-phpdomain
-Version: 0.8.1
+Version: 0.9.0
 Summary: Sphinx extension to enable documenting PHP code
 Home-page: https://github.com/markstory/sphinxcontrib-phpdomain
 Author: Mark Story
 Author-email: mark@mark-story.com
 License: BSD
 Download-URL: http://pypi.python.org/pypi/sphinxcontrib-phpdomain
 Description:
```

### Comparing `sphinxcontrib-phpdomain-0.8.1/sphinxcontrib_phpdomain.egg-info/SOURCES.txt` & `sphinxcontrib-phpdomain-0.9.0/sphinxcontrib_phpdomain.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sphinxcontrib-phpdomain-0.8.1/test/Makefile` & `sphinxcontrib-phpdomain-0.9.0/test/Makefile`

 * *Files identical despite different names*

### Comparing `sphinxcontrib-phpdomain-0.8.1/test/conf.py` & `sphinxcontrib-phpdomain-0.9.0/test/conf.py`

 * *Files identical despite different names*

### Comparing `sphinxcontrib-phpdomain-0.8.1/test/make.bat` & `sphinxcontrib-phpdomain-0.9.0/test/make.bat`

 * *Files identical despite different names*

### Comparing `sphinxcontrib-phpdomain-0.8.1/test/test_doc2.rst` & `sphinxcontrib-phpdomain-0.9.0/test/test_doc2.rst`

 * *Files identical despite different names*

### Comparing `sphinxcontrib-phpdomain-0.8.1/test/test_nesting_regression.rst` & `sphinxcontrib-phpdomain-0.9.0/test/test_nesting_regression.rst`

 * *Files identical despite different names*

