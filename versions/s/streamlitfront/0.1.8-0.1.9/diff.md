# Comparing `tmp/streamlitfront-0.1.8.tar.gz` & `tmp/streamlitfront-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "streamlitfront-0.1.8.tar", last modified: Mon Jun 20 19:25:50 2022, max compression
+gzip compressed data, was "streamlitfront-0.1.9.tar", last modified: Wed Jun 22 03:42:19 2022, max compression
```

## Comparing `streamlitfront-0.1.8.tar` & `streamlitfront-0.1.9.tar`

### file list

```diff
@@ -1,39 +1,40 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-20 19:25:50.217382 streamlitfront-0.1.8/
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     9563 2022-06-20 19:25:50.217382 streamlitfront-0.1.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     7176 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      610 2022-06-20 19:25:50.217382 streamlitfront-0.1.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)       91 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-20 19:25:50.213382 streamlitfront-0.1.8/streamlitfront/
--rw-r--r--   0 runner    (1001) docker     (121)      927 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      456 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/app_maker.py
--rw-r--r--   0 runner    (1001) docker     (121)    15927 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/base.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-20 19:25:50.217382 streamlitfront-0.1.8/streamlitfront/elements/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/elements/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2990 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/elements/elements.py
--rw-r--r--   0 runner    (1001) docker     (121)     1148 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/elements/tree_maker.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-20 19:25:50.217382 streamlitfront-0.1.8/streamlitfront/examples/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/examples/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      453 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/examples/data_binding.py
--rw-r--r--   0 runner    (1001) docker     (121)      545 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/examples/experimentation.py
--rw-r--r--   0 runner    (1001) docker     (121)     1081 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/examples/issues.py
--rw-r--r--   0 runner    (1001) docker     (121)     3759 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/examples/kaggle_front.py
--rw-r--r--   0 runner    (1001) docker     (121)      818 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/examples/mk_app.py
--rw-r--r--   0 runner    (1001) docker     (121)     1452 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/examples/pos_key_args.py
--rw-r--r--   0 runner    (1001) docker     (121)      545 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/examples/simple.py
--rw-r--r--   0 runner    (1001) docker     (121)     1485 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/examples/tw_data_binding.py
--rw-r--r--   0 runner    (1001) docker     (121)     1002 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/examples/various_input_kinds.py
--rw-r--r--   0 runner    (1001) docker     (121)    11079 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/page_funcs.py
--rw-r--r--   0 runner    (1001) docker     (121)      734 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/run_app.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-20 19:25:50.217382 streamlitfront-0.1.8/streamlitfront/scrap/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/scrap/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4861 2022-06-20 19:25:48.000000 streamlitfront-0.1.8/streamlitfront/scrap/alt_renderer.py
--rw-r--r--   0 runner    (1001) docker     (121)     4617 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/session_state.py
--rw-r--r--   0 runner    (1001) docker     (121)    10581 2022-06-20 19:25:04.000000 streamlitfront-0.1.8/streamlitfront/util.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-20 19:25:50.217382 streamlitfront-0.1.8/streamlitfront.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     9563 2022-06-20 19:25:50.000000 streamlitfront-0.1.8/streamlitfront.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1021 2022-06-20 19:25:50.000000 streamlitfront-0.1.8/streamlitfront.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-20 19:25:50.000000 streamlitfront-0.1.8/streamlitfront.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-20 19:25:50.000000 streamlitfront-0.1.8/streamlitfront.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       67 2022-06-20 19:25:50.000000 streamlitfront-0.1.8/streamlitfront.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       15 2022-06-20 19:25:50.000000 streamlitfront-0.1.8/streamlitfront.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 03:42:19.568221 streamlitfront-0.1.9/
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)     9611 2022-06-22 03:42:19.568221 streamlitfront-0.1.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     7224 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      620 2022-06-22 03:42:19.568221 streamlitfront-0.1.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)       91 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 03:42:19.564221 streamlitfront-0.1.9/streamlitfront/
+-rw-r--r--   0 runner    (1001) docker     (121)      927 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      456 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/app_maker.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16650 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/base.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 03:42:19.564221 streamlitfront-0.1.9/streamlitfront/elements/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/elements/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3327 2022-06-22 03:42:17.000000 streamlitfront-0.1.9/streamlitfront/elements/elements.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1493 2022-06-22 03:42:17.000000 streamlitfront-0.1.9/streamlitfront/elements/tree_maker.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 03:42:19.564221 streamlitfront-0.1.9/streamlitfront/examples/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/examples/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      719 2022-06-22 03:42:17.000000 streamlitfront-0.1.9/streamlitfront/examples/dag_app.py
+-rw-r--r--   0 runner    (1001) docker     (121)      453 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/examples/data_binding.py
+-rw-r--r--   0 runner    (1001) docker     (121)      545 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/examples/experimentation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1081 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/examples/issues.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3759 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/examples/kaggle_front.py
+-rw-r--r--   0 runner    (1001) docker     (121)      860 2022-06-22 03:42:17.000000 streamlitfront-0.1.9/streamlitfront/examples/mk_app.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1452 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/examples/pos_key_args.py
+-rw-r--r--   0 runner    (1001) docker     (121)      545 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/examples/simple.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1485 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/examples/tw_data_binding.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1002 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/examples/various_input_kinds.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11079 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/page_funcs.py
+-rw-r--r--   0 runner    (1001) docker     (121)      734 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/run_app.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 03:42:19.564221 streamlitfront-0.1.9/streamlitfront/scrap/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/scrap/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4861 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/scrap/alt_renderer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4617 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/session_state.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10581 2022-06-22 03:41:30.000000 streamlitfront-0.1.9/streamlitfront/util.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 03:42:19.564221 streamlitfront-0.1.9/streamlitfront.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     9611 2022-06-22 03:42:19.000000 streamlitfront-0.1.9/streamlitfront.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1056 2022-06-22 03:42:19.000000 streamlitfront-0.1.9/streamlitfront.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-22 03:42:19.000000 streamlitfront-0.1.9/streamlitfront.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-22 03:42:19.000000 streamlitfront-0.1.9/streamlitfront.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       76 2022-06-22 03:42:19.000000 streamlitfront-0.1.9/streamlitfront.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       15 2022-06-22 03:42:19.000000 streamlitfront-0.1.9/streamlitfront.egg-info/top_level.txt
```

### Comparing `streamlitfront-0.1.8/LICENSE` & `streamlitfront-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/PKG-INFO` & `streamlitfront-0.1.9/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: streamlitfront
-Version: 0.1.8
+Version: 0.1.9
 Summary: Generate streamlit frontends from python functions
 Home-page: https://github.com/i2mint/streamlitfront
 Author: OtoSense
 License: apache-2.0
 Description: 
         # streamlitfront
         Generate streamlit frontends from python functions
@@ -116,25 +116,25 @@
         
         - rendering
         
             You can define the way elements are rendered in the GUI.
             For instance, you can choose to render a text input instead of a number input for a specific parameter of a specific function:
             
             ```python
-            from front.elements import COMPONENT_INT_SLIDER
+            from front.elements import INT_INPUT_SLIDER_COMPONENT
             from streamlitfront import mk_app
             
         
             if __name__ == '__main__':
                 config = {
                     'rendering': {
                         'Foo': {
                             'inputs': {
                                 'a': {
-                                    'component': COMPONENT_INT_SLIDER,
+                                    'component': INT_INPUT_SLIDER_COMPONENT,
                                     'max_value': 10
                                 }
                             }
                         }
                     }
                 }
                 app = mk_app(funcs, config=config)
@@ -147,15 +147,15 @@
         
             ... the input ``a`` is a slider now !
             
         Obviously, you can combine the three types of configuration:
             
         ```python
         from typing import Iterable
-        from front.elements import COMPONENT_INT_SLIDER
+        from front.elements import INT_INPUT_SLIDER_COMPONENT
         from streamlitfront import mk_app
             
         
         def trans(objs: Iterable):
             return list(reversed(objs))
         
         
@@ -167,15 +167,15 @@
                 'obj': {
                     'trans': trans
                 },
                 'rendering': {
                     'foo': {
                         'inputs': {
                             'a': {
-                                'component': COMPONENT_INT_SLIDER,
+                                'component': INT_INPUT_SLIDER_COMPONENT,
                                 'max_value': 10
                             }
                         }
                     }
                 }
             }
             app = mk_app(funcs, config=config)
@@ -188,15 +188,15 @@
         
         ... all three configurations are applied !
         
         You can also overwrite the whole configuration by setting the ``convention`` parameter. Be careful though, by overwritting the default convention, you have to make sure that all configuations are defined. Otherwise, the application would crash or behave unexpectedly.
             
         ```python
         from typing import Any, Callable, Iterable
-        from front.elements import CONTAINER_VIEW, COMPONENT_FLOAT_SLIDER, COMPONENT_TEXT
+        from front.elements import VIEW_CONTAINER, FLOAT_INPUT_SLIDER_COMPONENT, TEXT_INPUT_COMPONENT
         from streamlitfront import mk_app
             
         
         def trans(objs: Iterable):
             return list(reversed(objs))
         
         
@@ -206,24 +206,24 @@
                     'title': 'Another application name'
                 },
                 'obj': {
                     'trans': trans
                 },
                 'rendering': {
                     Callable: {
-                        'container': CONTAINER_VIEW,
+                        'container': VIEW_CONTAINER,
                         'inputs': {
                             float: {
-                                'component': COMPONENT_FLOAT_SLIDER,
+                                'component': FLOAT_INPUT_SLIDER_COMPONENT,
                                 'max_value': 10.0,
                                 'format': '%.2f',
                                 'step': 0.01,
                             },
                             Any: {
-                                'component': COMPONENT_TEXT,
+                                'component': TEXT_INPUT_COMPONENT,
                             },
                         },
                     },
                 },
             }
             app = mk_app(funcs, convention=convention)
             app()
```

### Comparing `streamlitfront-0.1.8/README.md` & `streamlitfront-0.1.9/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -109,25 +109,25 @@
 
 - rendering
 
     You can define the way elements are rendered in the GUI.
     For instance, you can choose to render a text input instead of a number input for a specific parameter of a specific function:
     
     ```python
-    from front.elements import COMPONENT_INT_SLIDER
+    from front.elements import INT_INPUT_SLIDER_COMPONENT
     from streamlitfront import mk_app
     
 
     if __name__ == '__main__':
         config = {
             'rendering': {
                 'Foo': {
                     'inputs': {
                         'a': {
-                            'component': COMPONENT_INT_SLIDER,
+                            'component': INT_INPUT_SLIDER_COMPONENT,
                             'max_value': 10
                         }
                     }
                 }
             }
         }
         app = mk_app(funcs, config=config)
@@ -140,15 +140,15 @@
 
     ... the input ``a`` is a slider now !
     
 Obviously, you can combine the three types of configuration:
     
 ```python
 from typing import Iterable
-from front.elements import COMPONENT_INT_SLIDER
+from front.elements import INT_INPUT_SLIDER_COMPONENT
 from streamlitfront import mk_app
     
 
 def trans(objs: Iterable):
     return list(reversed(objs))
 
 
@@ -160,15 +160,15 @@
         'obj': {
             'trans': trans
         },
         'rendering': {
             'foo': {
                 'inputs': {
                     'a': {
-                        'component': COMPONENT_INT_SLIDER,
+                        'component': INT_INPUT_SLIDER_COMPONENT,
                         'max_value': 10
                     }
                 }
             }
         }
     }
     app = mk_app(funcs, config=config)
@@ -181,15 +181,15 @@
 
 ... all three configurations are applied !
 
 You can also overwrite the whole configuration by setting the ``convention`` parameter. Be careful though, by overwritting the default convention, you have to make sure that all configuations are defined. Otherwise, the application would crash or behave unexpectedly.
     
 ```python
 from typing import Any, Callable, Iterable
-from front.elements import CONTAINER_VIEW, COMPONENT_FLOAT_SLIDER, COMPONENT_TEXT
+from front.elements import VIEW_CONTAINER, FLOAT_INPUT_SLIDER_COMPONENT, TEXT_INPUT_COMPONENT
 from streamlitfront import mk_app
     
 
 def trans(objs: Iterable):
     return list(reversed(objs))
 
 
@@ -199,24 +199,24 @@
             'title': 'Another application name'
         },
         'obj': {
             'trans': trans
         },
         'rendering': {
             Callable: {
-                'container': CONTAINER_VIEW,
+                'container': VIEW_CONTAINER,
                 'inputs': {
                     float: {
-                        'component': COMPONENT_FLOAT_SLIDER,
+                        'component': FLOAT_INPUT_SLIDER_COMPONENT,
                         'max_value': 10.0,
                         'format': '%.2f',
                         'step': 0.01,
                     },
                     Any: {
-                        'component': COMPONENT_TEXT,
+                        'component': TEXT_INPUT_COMPONENT,
                     },
                 },
             },
         },
     }
     app = mk_app(funcs, convention=convention)
     app()
```

### Comparing `streamlitfront-0.1.8/setup.cfg` & `streamlitfront-0.1.9/setup.cfg`

 * *Files 22% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = streamlitfront
-version = 0.1.8
+version = 0.1.9
 url = https://github.com/i2mint/streamlitfront
 platforms = any
 description_file = README.md
 root_url = https://github.com/i2mint/
 license = apache-2.0
 author = OtoSense
 description = Generate streamlit frontends from python functions
@@ -15,14 +15,15 @@
 
 [options]
 packages = find:
 include_package_data = True
 zip_safe = False
 install_requires = 
 	front
+	graphviz
 	i2
 	pydantic
 	streamlit
 	streamlit_pydantic
 	importlib_resources
 
 [egg_info]
```

### Comparing `streamlitfront-0.1.8/streamlitfront/__init__.py` & `streamlitfront-0.1.9/streamlitfront/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront/base.py` & `streamlitfront-0.1.9/streamlitfront/base.py`

 * *Files 2% similar despite different names*

```diff
@@ -368,35 +368,36 @@
     ... }
     >>> app = mk_app(funcs, config=config)
 
     The obj configuration:
     You can define a wrapper to transform the initial object into an output of your
     choice to be rendered:
 
+    >>> from front.app_maker_base import dflt_trans
     >>> def trans(objs: Iterable):
-    ...     return list(reversed(objs))
+    ...     return dflt_trans(reversed(objs))
     >>> config = {
     ...     'obj': {
     ...         'trans': trans
     ...     }
     ... }
     >>> app = mk_app(funcs, config=config)
 
     The rendering configuration:
     You can define the way elements are rendered in the GUI.
     For instance, you can choose to render a text input instead of a number input for a
     specific parameter of a specific function:
 
-    >>> from front.elements import COMPONENT_INT_SLIDER
+    >>> from front.elements import INT_INPUT_SLIDER_COMPONENT
     >>> config = {
     ...     'rendering': {
     ...         'Foo': {
     ...             'inputs': {
     ...                 'a': {
-    ...                     'component': COMPONENT_INT_SLIDER,
+    ...                     'component': INT_INPUT_SLIDER_COMPONENT,
     ...                     'max_value': 10
     ...                 }
     ...             }
     ...         }
     ...     }
     ... }
     >>> app = mk_app(funcs, config=config)
@@ -410,49 +411,67 @@
     ...     'obj': {
     ...         'trans': trans
     ...     },
     ...     'rendering': {
     ...         'Foo': {
     ...             'inputs': {
     ...                 'a': {
-    ...                     'component': COMPONENT_INT_SLIDER,
+    ...                     'component': INT_INPUT_SLIDER_COMPONENT,
     ...                     'max_value': 10
     ...                 }
     ...             }
     ...         }
     ...     }
     ... }
     >>> app = mk_app(funcs, config=config)
 
     You can also overwrite the whole configuration by setting the ``convention``
     parameter. Be careful though, by overwritting the default convention, you have to
     make sure that all configuations are defined. Otherwise, the application would
     crash or behave unexpectedly.
 
-    >>> from front.elements import CONTAINER_VIEW, COMPONENT_FLOAT_SLIDER, COMPONENT_TEXT
+    >>> from meshed import DAG
+    >>> from front.elements import (
+    ...     VIEW_CONTAINER,
+    ...     FLOAT_INPUT_SLIDER_COMPONENT,
+    ...     TEXT_INPUT_COMPONENT,
+    ...     EXEC_SECTION_CONTAINER,
+    ...     SECTION_CONTAINER,
+    ...     GRAPH_COMPONENT
+    ... )
+    >>> 
     >>> convention = {
     ...     'app': {
     ...         'title': 'Another application name'
     ...     },
     ...     'obj': {
     ...         'trans': trans
     ...     },
     ...     'rendering': {
-    ...         Callable: {
-    ...             'container': CONTAINER_VIEW,
-    ...             'inputs': {
-    ...                 float: {
-    ...                     'component': COMPONENT_FLOAT_SLIDER,
-    ...                     'format': '%.2f',
-    ...                     'step': 0.01,
-    ...                 },
-    ...                 Any: {
-    ...                     'component': COMPONENT_TEXT,
+    ...         DAG: {
+    ...             'container': VIEW_CONTAINER,
+    ...             'execution': {
+    ...                 'container': EXEC_SECTION_CONTAINER,
+    ...                 'name': 'Execution',
+    ...                 'inputs': {
+    ...                     float: {
+    ...                         'component': FLOAT_INPUT_SLIDER_COMPONENT,
+    ...                         'format': '%.2f',
+    ...                         'step': 0.01,
+    ...                     },
+    ...                     Any: {'component': TEXT_INPUT_COMPONENT,},
     ...                 },
     ...             },
+    ...             'graph': {
+    ...                 'container': SECTION_CONTAINER,
+    ...                 'name': 'Flow',
+    ...                 'component': GRAPH_COMPONENT,
+    ...                 'display': True,
+    ...                 'display_for_single_node': False,
+    ...             }
     ...         },
     ...     },
     ... }
     >>> app = mk_app(funcs, convention=convention)
 
     :param objs: The target objects to render in the streamlit application.
     :type objs: Iterable
```

### Comparing `streamlitfront-0.1.8/streamlitfront/examples/experimentation.py` & `streamlitfront-0.1.9/streamlitfront/examples/experimentation.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront/examples/issues.py` & `streamlitfront-0.1.9/streamlitfront/examples/issues.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront/examples/kaggle_front.py` & `streamlitfront-0.1.9/streamlitfront/examples/kaggle_front.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront/examples/mk_app.py` & `streamlitfront-0.1.9/streamlitfront/examples/mk_app.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from distutils.command.config import config
 
 from streamlitfront.base import mk_app
-from front.elements import COMPONENT_FLOAT_SLIDER
+from front.elements import FLOAT_INPUT_SLIDER_COMPONENT
 
 
 def foo(a: int = 1, b: int = 2, c=3):
     """This is foo. It computes something"""
     return (a * b) + c
 
 
@@ -28,12 +28,14 @@
         'app': {'title': 'My app'},
         # 'obj': {
         #     'bindings': {
         #         'Foo.a': 'Proportion.x'
         #     }
         # }
         'rendering': {
-            'Proportion': {'inputs': {'p': {'component': COMPONENT_FLOAT_SLIDER,}},}
+            'Proportion': {
+                'inputs': {'p': {'component': FLOAT_INPUT_SLIDER_COMPONENT,}},
+            }
         },
     },
 )
 app()
```

### Comparing `streamlitfront-0.1.8/streamlitfront/examples/pos_key_args.py` & `streamlitfront-0.1.9/streamlitfront/examples/pos_key_args.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront/examples/simple.py` & `streamlitfront-0.1.9/streamlitfront/examples/simple.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront/examples/tw_data_binding.py` & `streamlitfront-0.1.9/streamlitfront/examples/tw_data_binding.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront/examples/various_input_kinds.py` & `streamlitfront-0.1.9/streamlitfront/examples/various_input_kinds.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront/page_funcs.py` & `streamlitfront-0.1.9/streamlitfront/page_funcs.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront/run_app.py` & `streamlitfront-0.1.9/streamlitfront/run_app.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront/scrap/alt_renderer.py` & `streamlitfront-0.1.9/streamlitfront/scrap/alt_renderer.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront/session_state.py` & `streamlitfront-0.1.9/streamlitfront/session_state.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront/util.py` & `streamlitfront-0.1.9/streamlitfront/util.py`

 * *Files identical despite different names*

### Comparing `streamlitfront-0.1.8/streamlitfront.egg-info/PKG-INFO` & `streamlitfront-0.1.9/streamlitfront.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: streamlitfront
-Version: 0.1.8
+Version: 0.1.9
 Summary: Generate streamlit frontends from python functions
 Home-page: https://github.com/i2mint/streamlitfront
 Author: OtoSense
 License: apache-2.0
 Description: 
         # streamlitfront
         Generate streamlit frontends from python functions
@@ -116,25 +116,25 @@
         
         - rendering
         
             You can define the way elements are rendered in the GUI.
             For instance, you can choose to render a text input instead of a number input for a specific parameter of a specific function:
             
             ```python
-            from front.elements import COMPONENT_INT_SLIDER
+            from front.elements import INT_INPUT_SLIDER_COMPONENT
             from streamlitfront import mk_app
             
         
             if __name__ == '__main__':
                 config = {
                     'rendering': {
                         'Foo': {
                             'inputs': {
                                 'a': {
-                                    'component': COMPONENT_INT_SLIDER,
+                                    'component': INT_INPUT_SLIDER_COMPONENT,
                                     'max_value': 10
                                 }
                             }
                         }
                     }
                 }
                 app = mk_app(funcs, config=config)
@@ -147,15 +147,15 @@
         
             ... the input ``a`` is a slider now !
             
         Obviously, you can combine the three types of configuration:
             
         ```python
         from typing import Iterable
-        from front.elements import COMPONENT_INT_SLIDER
+        from front.elements import INT_INPUT_SLIDER_COMPONENT
         from streamlitfront import mk_app
             
         
         def trans(objs: Iterable):
             return list(reversed(objs))
         
         
@@ -167,15 +167,15 @@
                 'obj': {
                     'trans': trans
                 },
                 'rendering': {
                     'foo': {
                         'inputs': {
                             'a': {
-                                'component': COMPONENT_INT_SLIDER,
+                                'component': INT_INPUT_SLIDER_COMPONENT,
                                 'max_value': 10
                             }
                         }
                     }
                 }
             }
             app = mk_app(funcs, config=config)
@@ -188,15 +188,15 @@
         
         ... all three configurations are applied !
         
         You can also overwrite the whole configuration by setting the ``convention`` parameter. Be careful though, by overwritting the default convention, you have to make sure that all configuations are defined. Otherwise, the application would crash or behave unexpectedly.
             
         ```python
         from typing import Any, Callable, Iterable
-        from front.elements import CONTAINER_VIEW, COMPONENT_FLOAT_SLIDER, COMPONENT_TEXT
+        from front.elements import VIEW_CONTAINER, FLOAT_INPUT_SLIDER_COMPONENT, TEXT_INPUT_COMPONENT
         from streamlitfront import mk_app
             
         
         def trans(objs: Iterable):
             return list(reversed(objs))
         
         
@@ -206,24 +206,24 @@
                     'title': 'Another application name'
                 },
                 'obj': {
                     'trans': trans
                 },
                 'rendering': {
                     Callable: {
-                        'container': CONTAINER_VIEW,
+                        'container': VIEW_CONTAINER,
                         'inputs': {
                             float: {
-                                'component': COMPONENT_FLOAT_SLIDER,
+                                'component': FLOAT_INPUT_SLIDER_COMPONENT,
                                 'max_value': 10.0,
                                 'format': '%.2f',
                                 'step': 0.01,
                             },
                             Any: {
-                                'component': COMPONENT_TEXT,
+                                'component': TEXT_INPUT_COMPONENT,
                             },
                         },
                     },
                 },
             }
             app = mk_app(funcs, convention=convention)
             app()
```

### Comparing `streamlitfront-0.1.8/streamlitfront.egg-info/SOURCES.txt` & `streamlitfront-0.1.9/streamlitfront.egg-info/SOURCES.txt`

 * *Files 5% similar despite different names*

```diff
@@ -15,14 +15,15 @@
 streamlitfront.egg-info/not-zip-safe
 streamlitfront.egg-info/requires.txt
 streamlitfront.egg-info/top_level.txt
 streamlitfront/elements/__init__.py
 streamlitfront/elements/elements.py
 streamlitfront/elements/tree_maker.py
 streamlitfront/examples/__init__.py
+streamlitfront/examples/dag_app.py
 streamlitfront/examples/data_binding.py
 streamlitfront/examples/experimentation.py
 streamlitfront/examples/issues.py
 streamlitfront/examples/kaggle_front.py
 streamlitfront/examples/mk_app.py
 streamlitfront/examples/pos_key_args.py
 streamlitfront/examples/simple.py
```

