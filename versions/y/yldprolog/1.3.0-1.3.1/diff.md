# Comparing `tmp/yldprolog-1.3.0.tar.gz` & `tmp/yldprolog-1.3.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "yldprolog-1.3.0.tar", last modified: Mon Apr  3 10:27:16 2023, max compression
+gzip compressed data, was "yldprolog-1.3.1.tar", last modified: Thu Apr  6 11:39:31 2023, max compression
```

## Comparing `yldprolog-1.3.0.tar` & `yldprolog-1.3.1.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxr-xr-x   0 themel     (501) staff       (20)        0 2023-04-03 10:27:16.020381 yldprolog-1.3.0/
--rw-r--r--   0 themel     (501) staff       (20)     2705 2023-04-03 10:27:16.020592 yldprolog-1.3.0/PKG-INFO
--rw-r--r--   0 themel     (501) staff       (20)     2251 2023-03-15 15:15:13.000000 yldprolog-1.3.0/README.md
--rw-r--r--   0 themel     (501) staff       (20)      150 2023-03-15 15:15:13.000000 yldprolog-1.3.0/pyproject.toml
--rw-r--r--   0 themel     (501) staff       (20)      816 2023-04-03 10:27:16.021664 yldprolog-1.3.0/setup.cfg
--rw-r--r--   0 themel     (501) staff       (20)       38 2023-03-15 15:15:13.000000 yldprolog-1.3.0/setup.py
-drwxr-xr-x   0 themel     (501) staff       (20)        0 2023-04-03 10:27:16.003714 yldprolog-1.3.0/src/
-drwxr-xr-x   0 themel     (501) staff       (20)        0 2023-04-03 10:27:16.012674 yldprolog-1.3.0/src/yldprolog/
--rw-r--r--   0 themel     (501) staff       (20)        0 2023-03-15 15:15:13.000000 yldprolog-1.3.0/src/yldprolog/__init__.py
--rwxr-xr-x   0 themel     (501) staff       (20)     4771 2023-04-03 10:15:13.000000 yldprolog-1.3.0/src/yldprolog/compiler.py
--rw-r--r--   0 themel     (501) staff       (20)    20587 2023-04-03 10:15:05.000000 yldprolog-1.3.0/src/yldprolog/engine.py
--rw-r--r--   0 themel     (501) staff       (20)      486 2023-03-15 15:15:13.000000 yldprolog-1.3.0/src/yldprolog/errors.py
--rw-r--r--   0 themel     (501) staff       (20)     6977 2023-03-15 15:29:17.000000 yldprolog-1.3.0/src/yldprolog/prologLexer.py
--rw-r--r--   0 themel     (501) staff       (20)     3775 2023-03-15 15:29:17.000000 yldprolog-1.3.0/src/yldprolog/prologListener.py
--rw-r--r--   0 themel     (501) staff       (20)    40583 2023-03-15 15:29:17.000000 yldprolog-1.3.0/src/yldprolog/prologParser.py
--rw-r--r--   0 themel     (501) staff       (20)     2395 2023-03-15 15:29:17.000000 yldprolog-1.3.0/src/yldprolog/prologVisitor.py
--rw-r--r--   0 themel     (501) staff       (20)    22377 2023-04-03 10:14:54.000000 yldprolog-1.3.0/src/yldprolog/yp_generator.py
--rw-r--r--   0 themel     (501) staff       (20)    12105 2023-04-03 10:14:40.000000 yldprolog-1.3.0/src/yldprolog/yp_prolog_visitor.py
-drwxr-xr-x   0 themel     (501) staff       (20)        0 2023-04-03 10:27:16.018303 yldprolog-1.3.0/src/yldprolog.egg-info/
--rw-r--r--   0 themel     (501) staff       (20)     2705 2023-04-03 10:27:15.000000 yldprolog-1.3.0/src/yldprolog.egg-info/PKG-INFO
--rw-r--r--   0 themel     (501) staff       (20)      598 2023-04-03 10:27:15.000000 yldprolog-1.3.0/src/yldprolog.egg-info/SOURCES.txt
--rw-r--r--   0 themel     (501) staff       (20)        1 2023-04-03 10:27:15.000000 yldprolog-1.3.0/src/yldprolog.egg-info/dependency_links.txt
--rw-r--r--   0 themel     (501) staff       (20)       50 2023-04-03 10:27:15.000000 yldprolog-1.3.0/src/yldprolog.egg-info/entry_points.txt
--rw-r--r--   0 themel     (501) staff       (20)       36 2023-04-03 10:27:15.000000 yldprolog-1.3.0/src/yldprolog.egg-info/requires.txt
--rw-r--r--   0 themel     (501) staff       (20)       10 2023-04-03 10:27:15.000000 yldprolog-1.3.0/src/yldprolog.egg-info/top_level.txt
-drwxr-xr-x   0 themel     (501) staff       (20)        0 2023-04-03 10:27:16.019822 yldprolog-1.3.0/tests/
--rw-r--r--   0 themel     (501) staff       (20)     2926 2023-04-03 10:15:22.000000 yldprolog-1.3.0/tests/test_compiler.py
--rw-r--r--   0 themel     (501) staff       (20)    20808 2023-04-03 10:15:31.000000 yldprolog-1.3.0/tests/test_engine.py
+drwxr-xr-x   0 themel     (501) staff       (20)        0 2023-04-06 11:39:31.616977 yldprolog-1.3.1/
+-rw-r--r--   0 themel     (501) staff       (20)     2705 2023-04-06 11:39:31.617172 yldprolog-1.3.1/PKG-INFO
+-rw-r--r--   0 themel     (501) staff       (20)     2251 2023-03-15 15:15:13.000000 yldprolog-1.3.1/README.md
+-rw-r--r--   0 themel     (501) staff       (20)      150 2023-03-15 15:15:13.000000 yldprolog-1.3.1/pyproject.toml
+-rw-r--r--   0 themel     (501) staff       (20)      816 2023-04-06 11:39:31.618167 yldprolog-1.3.1/setup.cfg
+-rw-r--r--   0 themel     (501) staff       (20)       38 2023-03-15 15:15:13.000000 yldprolog-1.3.1/setup.py
+drwxr-xr-x   0 themel     (501) staff       (20)        0 2023-04-06 11:39:31.595219 yldprolog-1.3.1/src/
+drwxr-xr-x   0 themel     (501) staff       (20)        0 2023-04-06 11:39:31.609140 yldprolog-1.3.1/src/yldprolog/
+-rw-r--r--   0 themel     (501) staff       (20)        0 2023-03-15 15:15:13.000000 yldprolog-1.3.1/src/yldprolog/__init__.py
+-rwxr-xr-x   0 themel     (501) staff       (20)     4771 2023-04-03 10:15:13.000000 yldprolog-1.3.1/src/yldprolog/compiler.py
+-rw-r--r--   0 themel     (501) staff       (20)    20627 2023-04-06 11:26:54.000000 yldprolog-1.3.1/src/yldprolog/engine.py
+-rw-r--r--   0 themel     (501) staff       (20)      486 2023-03-15 15:15:13.000000 yldprolog-1.3.1/src/yldprolog/errors.py
+-rw-r--r--   0 themel     (501) staff       (20)     6977 2023-03-15 15:29:17.000000 yldprolog-1.3.1/src/yldprolog/prologLexer.py
+-rw-r--r--   0 themel     (501) staff       (20)     3775 2023-03-15 15:29:17.000000 yldprolog-1.3.1/src/yldprolog/prologListener.py
+-rw-r--r--   0 themel     (501) staff       (20)    40583 2023-03-15 15:29:17.000000 yldprolog-1.3.1/src/yldprolog/prologParser.py
+-rw-r--r--   0 themel     (501) staff       (20)     2395 2023-03-15 15:29:17.000000 yldprolog-1.3.1/src/yldprolog/prologVisitor.py
+-rw-r--r--   0 themel     (501) staff       (20)    22377 2023-04-03 10:14:54.000000 yldprolog-1.3.1/src/yldprolog/yp_generator.py
+-rw-r--r--   0 themel     (501) staff       (20)    12105 2023-04-03 10:14:40.000000 yldprolog-1.3.1/src/yldprolog/yp_prolog_visitor.py
+drwxr-xr-x   0 themel     (501) staff       (20)        0 2023-04-06 11:39:31.613989 yldprolog-1.3.1/src/yldprolog.egg-info/
+-rw-r--r--   0 themel     (501) staff       (20)     2705 2023-04-06 11:39:31.000000 yldprolog-1.3.1/src/yldprolog.egg-info/PKG-INFO
+-rw-r--r--   0 themel     (501) staff       (20)      598 2023-04-06 11:39:31.000000 yldprolog-1.3.1/src/yldprolog.egg-info/SOURCES.txt
+-rw-r--r--   0 themel     (501) staff       (20)        1 2023-04-06 11:39:31.000000 yldprolog-1.3.1/src/yldprolog.egg-info/dependency_links.txt
+-rw-r--r--   0 themel     (501) staff       (20)       50 2023-04-06 11:39:31.000000 yldprolog-1.3.1/src/yldprolog.egg-info/entry_points.txt
+-rw-r--r--   0 themel     (501) staff       (20)       36 2023-04-06 11:39:31.000000 yldprolog-1.3.1/src/yldprolog.egg-info/requires.txt
+-rw-r--r--   0 themel     (501) staff       (20)       10 2023-04-06 11:39:31.000000 yldprolog-1.3.1/src/yldprolog.egg-info/top_level.txt
+drwxr-xr-x   0 themel     (501) staff       (20)        0 2023-04-06 11:39:31.615610 yldprolog-1.3.1/tests/
+-rw-r--r--   0 themel     (501) staff       (20)     2926 2023-04-03 10:15:22.000000 yldprolog-1.3.1/tests/test_compiler.py
+-rw-r--r--   0 themel     (501) staff       (20)    21698 2023-04-06 11:30:19.000000 yldprolog-1.3.1/tests/test_engine.py
```

### Comparing `yldprolog-1.3.0/PKG-INFO` & `yldprolog-1.3.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: yldprolog
-Version: 1.3.0
+Version: 1.3.1
 Summary: A rewrite of Yield Prolog for Python
 Home-page: https://github.com/timhemel/yldprolog
 Author: Tim Hemel
 Author-email: tim@securesoftware.nl
 Keywords: prolog
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU Affero General Public License v3
```

### Comparing `yldprolog-1.3.0/README.md` & `yldprolog-1.3.1/README.md`

 * *Files identical despite different names*

### Comparing `yldprolog-1.3.0/setup.cfg` & `yldprolog-1.3.1/setup.cfg`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = yldprolog
-version = 1.3.0
+version = 1.3.1
 author = Tim Hemel
 author_email = tim@securesoftware.nl
 description = A rewrite of Yield Prolog for Python
 long_description_content_type = text/markdown
 long_description = file: README.md
 url = https://github.com/timhemel/yldprolog
 license_files = LICENSE LICENSE-YieldProlog LICENSE-grammar
```

### Comparing `yldprolog-1.3.0/src/yldprolog/compiler.py` & `yldprolog-1.3.1/src/yldprolog/compiler.py`

 * *Files identical despite different names*

### Comparing `yldprolog-1.3.0/src/yldprolog/engine.py` & `yldprolog-1.3.1/src/yldprolog/engine.py`

 * *Files 1% similar despite different names*

```diff
@@ -500,18 +500,19 @@
         '''insert name(values) in the set of facts. If append is False, insert the
         fact at the beginning, otherwise at the end.'''
         try:
             clauses = self._find_predicates(name.name(), len(values))
             # indexedanswers
         except YPException as e:
             clauses = []
+        answer = Answer([get_value(v) for v in values])
         if append:
-            clauses.append(Answer(values))
+            clauses.append(answer)
         else:
-            clauses.insert(0, Answer(values))
+            clauses.insert(0, answer)
         self._update_predicate(name, len(values), clauses)
 
     def query(self, name, args):
         """Creates a Prolog query for the symbol name, with arguments args. name is a string,
         args is a list of Prolog terms. The query will only be constructed, but not evaluated.
         Returns a Python generator of boolean values.
```

### Comparing `yldprolog-1.3.0/src/yldprolog/prologLexer.py` & `yldprolog-1.3.1/src/yldprolog/prologLexer.py`

 * *Files identical despite different names*

### Comparing `yldprolog-1.3.0/src/yldprolog/prologListener.py` & `yldprolog-1.3.1/src/yldprolog/prologListener.py`

 * *Files identical despite different names*

### Comparing `yldprolog-1.3.0/src/yldprolog/prologParser.py` & `yldprolog-1.3.1/src/yldprolog/prologParser.py`

 * *Files identical despite different names*

### Comparing `yldprolog-1.3.0/src/yldprolog/prologVisitor.py` & `yldprolog-1.3.1/src/yldprolog/prologVisitor.py`

 * *Files identical despite different names*

### Comparing `yldprolog-1.3.0/src/yldprolog/yp_generator.py` & `yldprolog-1.3.1/src/yldprolog/yp_generator.py`

 * *Files identical despite different names*

### Comparing `yldprolog-1.3.0/src/yldprolog/yp_prolog_visitor.py` & `yldprolog-1.3.1/src/yldprolog/yp_prolog_visitor.py`

 * *Files identical despite different names*

### Comparing `yldprolog-1.3.0/src/yldprolog.egg-info/PKG-INFO` & `yldprolog-1.3.1/src/yldprolog.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: yldprolog
-Version: 1.3.0
+Version: 1.3.1
 Summary: A rewrite of Yield Prolog for Python
 Home-page: https://github.com/timhemel/yldprolog
 Author: Tim Hemel
 Author-email: tim@securesoftware.nl
 Keywords: prolog
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU Affero General Public License v3
```

### Comparing `yldprolog-1.3.0/src/yldprolog.egg-info/SOURCES.txt` & `yldprolog-1.3.1/src/yldprolog.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `yldprolog-1.3.0/tests/test_compiler.py` & `yldprolog-1.3.1/tests/test_compiler.py`

 * *Files identical despite different names*

### Comparing `yldprolog-1.3.0/tests/test_engine.py` & `yldprolog-1.3.1/tests/test_engine.py`

 * *Files 2% similar despite different names*

```diff
@@ -542,14 +542,46 @@
     yp = YP()
     yp.load_script_from_string(s, overwrite=False)
     v = yp.variable()
     q = yp.query('isp', [ v ])
     r = [ to_python(v) for x in q ]
     assert r == [ 'c', 'a', 'a', 'b' ]
 
+def test_builtin_predicate_assertz_instantiated_variable():
+    s = compile_prolog_from_string('''
+    name(tom).
+    name(jerry).
+    initp() :- name(Y), assertz(p(Y)).
+    isp(X) :- p(X).
+    ''', TestContext)
+    yp = YP()
+    yp.load_script_from_string(s, overwrite=False)
+    q = yp.query('initp', [ ])
+    r = list(q)
+    v = yp.variable()
+    q = yp.query('isp', [ v ])
+    r = [ to_python(v) for x in q ]
+    assert r == [ 'tom', 'jerry' ]
+
+def test_builtin_predicate_assertz_free_variable():
+    s = compile_prolog_from_string('''
+    name(tom).
+    name(jerry).
+    initp() :- assertz(p(_)).
+    isp(X) :- name(X), p(X).
+    ''', TestContext)
+    yp = YP()
+    yp.load_script_from_string(s, overwrite=False)
+    q = yp.query('initp', [ ])
+    r = list(q)
+    v = yp.variable()
+    q = yp.query('isp', [ v ])
+    r = [ to_python(v) for x in q ]
+    assert r == [ 'tom', 'jerry' ]
+
 def test_builtin_predicate_retract_single_atom():
     s = compile_prolog_from_string('''
     foo(X) :- assertz(p(b)), assertz(p(a)), asserta(p(c)), retract(p(a)), p(X).
     ''', TestContext)
     yp = YP()
     yp.load_script_from_string(s, overwrite=False)
     v = yp.variable()
```

