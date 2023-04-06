# Comparing `tmp/django_components-0.9.1.tar.gz` & `tmp/django_components-0.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/django_components-0.9.1.tar", last modified: Sat Feb 27 15:42:09 2021, max compression
+gzip compressed data, was "dist/django_components-0.9.2.tar", last modified: Wed Mar 10 21:45:56 2021, max compression
```

## Comparing `django_components-0.9.1.tar` & `django_components-0.9.2.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 emilstenstrom  (1000) emilstenstrom  (1000)        0 2021-02-27 15:42:09.576148 django_components-0.9.1/
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)    14195 2021-02-27 15:42:09.576148 django_components-0.9.1/PKG-INFO
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)    11164 2021-02-27 15:39:31.000000 django_components-0.9.1/README.md
-drwxr-xr-x   0 emilstenstrom  (1000) emilstenstrom  (1000)        0 2021-02-27 15:42:09.566148 django_components-0.9.1/django_components/
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)      427 2021-02-06 09:10:25.000000 django_components-0.9.1/django_components/__init__.py
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)      596 2021-02-20 09:03:40.000000 django_components-0.9.1/django_components/app_settings.py
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)      167 2021-02-06 09:10:25.000000 django_components-0.9.1/django_components/apps.py
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)     4038 2021-02-27 15:38:41.000000 django_components-0.9.1/django_components/component.py
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)      807 2020-12-08 20:22:57.000000 django_components-0.9.1/django_components/component_registry.py
-drwxr-xr-x   0 emilstenstrom  (1000) emilstenstrom  (1000)        0 2021-02-27 15:42:09.576148 django_components-0.9.1/django_components/templatetags/
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)        0 2020-12-08 20:22:57.000000 django_components-0.9.1/django_components/templatetags/__init__.py
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)     8299 2021-02-20 09:03:40.000000 django_components-0.9.1/django_components/templatetags/component_tags.py
-drwxr-xr-x   0 emilstenstrom  (1000) emilstenstrom  (1000)        0 2021-02-27 15:42:09.576148 django_components-0.9.1/django_components.egg-info/
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)    14195 2021-02-27 15:42:09.000000 django_components-0.9.1/django_components.egg-info/PKG-INFO
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)      485 2021-02-27 15:42:09.000000 django_components-0.9.1/django_components.egg-info/SOURCES.txt
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)        1 2021-02-27 15:42:09.000000 django_components-0.9.1/django_components.egg-info/dependency_links.txt
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)       12 2021-02-27 15:42:09.000000 django_components-0.9.1/django_components.egg-info/requires.txt
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)       18 2021-02-27 15:42:09.000000 django_components-0.9.1/django_components.egg-info/top_level.txt
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)      208 2021-02-27 15:42:09.576148 django_components-0.9.1/setup.cfg
--rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)     1215 2021-02-27 15:40:27.000000 django_components-0.9.1/setup.py
+drwxr-xr-x   0 emilstenstrom  (1000) emilstenstrom  (1000)        0 2021-03-10 21:45:56.340000 django_components-0.9.2/
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)    14239 2021-03-10 21:45:56.340000 django_components-0.9.2/PKG-INFO
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)    11201 2021-03-10 21:38:23.000000 django_components-0.9.2/README.md
+drwxr-xr-x   0 emilstenstrom  (1000) emilstenstrom  (1000)        0 2021-03-10 21:45:56.340000 django_components-0.9.2/django_components/
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)      427 2021-02-06 09:10:25.000000 django_components-0.9.2/django_components/__init__.py
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)      596 2021-02-20 09:03:40.000000 django_components-0.9.2/django_components/app_settings.py
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)      167 2021-02-06 09:10:25.000000 django_components-0.9.2/django_components/apps.py
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)     5054 2021-03-10 21:38:59.000000 django_components-0.9.2/django_components/component.py
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)      807 2020-12-08 20:22:57.000000 django_components-0.9.2/django_components/component_registry.py
+drwxr-xr-x   0 emilstenstrom  (1000) emilstenstrom  (1000)        0 2021-03-10 21:45:56.340000 django_components-0.9.2/django_components/templatetags/
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)        0 2020-12-08 20:22:57.000000 django_components-0.9.2/django_components/templatetags/__init__.py
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)     8299 2021-02-20 09:03:40.000000 django_components-0.9.2/django_components/templatetags/component_tags.py
+drwxr-xr-x   0 emilstenstrom  (1000) emilstenstrom  (1000)        0 2021-03-10 21:45:56.340000 django_components-0.9.2/django_components.egg-info/
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)    14239 2021-03-10 21:45:56.000000 django_components-0.9.2/django_components.egg-info/PKG-INFO
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)      485 2021-03-10 21:45:56.000000 django_components-0.9.2/django_components.egg-info/SOURCES.txt
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)        1 2021-03-10 21:45:56.000000 django_components-0.9.2/django_components.egg-info/dependency_links.txt
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)       12 2021-03-10 21:45:56.000000 django_components-0.9.2/django_components.egg-info/requires.txt
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)       18 2021-03-10 21:45:56.000000 django_components-0.9.2/django_components.egg-info/top_level.txt
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)      208 2021-03-10 21:45:56.340000 django_components-0.9.2/setup.cfg
+-rw-r--r--   0 emilstenstrom  (1000) emilstenstrom  (1000)     1215 2021-03-10 21:43:02.000000 django_components-0.9.2/setup.py
```

### Comparing `django_components-0.9.1/PKG-INFO` & `django_components-0.9.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django_components
-Version: 0.9.1
+Version: 0.9.2
 Summary: A way to create simple reusable template components in Django.
 Home-page: https://github.com/EmilStenstrom/django-components/
 Author: Emil Stenström
 Author-email: emil@emilstenstrom.se
 License: MIT
 Description: # django-components
         <a href="https://github.com/EmilStenstrom/django-components/actions?query=workflow%3A%22Run+tests%22"><img align="right" src="https://github.com/EmilStenstrom/django-components/workflows/Run%20tests/badge.svg" alt="Show test status"></a>
@@ -165,34 +165,35 @@
                     "date": date,
                 }
         
             def template(self, context):
                 return "[your app]/components/calendar/calendar.html"
         
             class Media:
-                css = {'all': ['[your app]/components/calendar/calendar.css']}
-                js = ['[your app]/components/calendar/calendar.js']
+                css = '[your app]/components/calendar/calendar.css'
+                js = '[your app]/components/calendar/calendar.js'
         ```
         
         And voilá!! We've created our first component.
         
         # Use the component in a template
         
-        First load the `component_tags` tag library, then use the `component_dependencies` and `component` tags to render the component to the page.
+        First load the `component_tags` tag library, then use the `component_[js/css]_dependencies` and `component` tags to render the component to the page.
         
         ```htmldjango
         {% load component_tags %}
         <!DOCTYPE html>
         <html>
         <head>
             <title>My example calendar</title>
-            {% component_dependencies %}
+            {% component_css_dependencies %}
         </head>
         <body>
             {% component "calendar" date="2015-06-19" %}
+            {% component_js_dependencies %}
         </body>
         <html>
         ```
         
         The output from the above template will be:
         
         ```html
```

### Comparing `django_components-0.9.1/README.md` & `django_components-0.9.2/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -157,34 +157,35 @@
             "date": date,
         }
 
     def template(self, context):
         return "[your app]/components/calendar/calendar.html"
 
     class Media:
-        css = {'all': ['[your app]/components/calendar/calendar.css']}
-        js = ['[your app]/components/calendar/calendar.js']
+        css = '[your app]/components/calendar/calendar.css'
+        js = '[your app]/components/calendar/calendar.js'
 ```
 
 And voilá!! We've created our first component.
 
 # Use the component in a template
 
-First load the `component_tags` tag library, then use the `component_dependencies` and `component` tags to render the component to the page.
+First load the `component_tags` tag library, then use the `component_[js/css]_dependencies` and `component` tags to render the component to the page.
 
 ```htmldjango
 {% load component_tags %}
 <!DOCTYPE html>
 <html>
 <head>
     <title>My example calendar</title>
-    {% component_dependencies %}
+    {% component_css_dependencies %}
 </head>
 <body>
     {% component "calendar" date="2015-06-19" %}
+    {% component_js_dependencies %}
 </body>
 <html>
 ```
 
 The output from the above template will be:
 
 ```html
```

### Comparing `django_components-0.9.1/django_components/app_settings.py` & `django_components-0.9.2/django_components/app_settings.py`

 * *Files identical despite different names*

### Comparing `django_components-0.9.1/django_components/component.py` & `django_components-0.9.2/django_components/component.py`

 * *Files 13% similar despite different names*

```diff
@@ -10,16 +10,40 @@
 from django.utils.safestring import mark_safe
 
 # Allow "component.AlreadyRegistered" instead of having to import these everywhere
 from django_components.component_registry import AlreadyRegistered, ComponentRegistry, NotRegistered  # noqa
 
 TEMPLATE_CACHE_SIZE = getattr(settings, "COMPONENTS", {}).get('TEMPLATE_CACHE_SIZE', 128)
 
+class SimplifiedInterfaceMediaDefiningClass(MediaDefiningClass):
+    def __new__(mcs, name, bases, attrs):
+        if "Media" in attrs:
+            media = attrs["Media"]
+
+            # Allow: class Media: css = "style.css"
+            if isinstance(media.css, str):
+                media.css = [media.css]
+
+            # Allow: class Media: css = ["style.css"]
+            if isinstance(media.css, list):
+                media.css = {"all": media.css}
+
+            # Allow: class Media: css = {"all": "style.css"}
+            if isinstance(media.css, dict):
+                for media_type, path_list in media.css.items():
+                    if isinstance(path_list, str):
+                        media.css[media_type] = [path_list]
+
+            # Allow: class Media: js = "script.js"
+            if isinstance(media.js, str):
+                media.js = [media.js]
 
-class Component(metaclass=MediaDefiningClass):
+        return super().__new__(mcs, name, bases, attrs)
+
+class Component(metaclass=SimplifiedInterfaceMediaDefiningClass):
 
     def __init__(self, component_name):
         self.__component_name = component_name
         self.instance_template = None
         self.slots = {}
 
     def context(self):
@@ -41,23 +65,27 @@
     def render_js_dependencies(self):
         """Render only JS dependencies available in the media class."""
 
         return mark_safe("\n".join(self.media.render_js()))
 
     @staticmethod
     def slots_in_template(template):
-        return {node.name: node.nodelist for node in template.template.nodelist if is_slot_node(node)}
+        return {node.name: node.nodelist for node in template.template.nodelist if Component.is_slot_node(node)}
+
+    @staticmethod
+    def is_slot_node(node):
+        return node.token.token_type == TokenType.BLOCK and node.token.split_contents()[0] == "slot"
 
     @lru_cache(maxsize=TEMPLATE_CACHE_SIZE)
     def compile_instance_template(self, template_name):
         """Use component's base template and the slots used for this instance to compile
         a unified template for this instance."""
 
         component_template = get_template(template_name)
-        slots_in_template = self.slots_in_template(component_template)
+        slots_in_template = Component.slots_in_template(component_template)
 
         defined_slot_names = set(slots_in_template.keys())
         filled_slot_names = set(self.slots.keys())
         unexpected_slots = filled_slot_names - defined_slot_names
         if unexpected_slots:
             if settings.DEBUG:
                 warnings.warn(
@@ -67,15 +95,15 @@
                 )
             for unexpected_slot in unexpected_slots:
                 del self.slots[unexpected_slot]
 
         combined_slots = dict(slots_in_template, **self.slots)
         if combined_slots:
             # Replace slot nodes with their nodelists, then combine into a single, flat nodelist
-            node_iterator = ([node] if not is_slot_node(node) else combined_slots[node.name]
+            node_iterator = ([node] if not Component.is_slot_node(node) else combined_slots[node.name]
                              for node in component_template.template.nodelist)
 
             instance_template = copy(component_template.template)
             instance_template.nodelist = NodeList(chain.from_iterable(node_iterator))
         else:
             instance_template = component_template.template
 
@@ -87,18 +115,14 @@
         return instance_template.render(context)
 
     class Media:
         css = {}
         js = []
 
 
-def is_slot_node(node):
-    return node.token.token_type == TokenType.BLOCK and node.token.split_contents()[0] == "slot"
-
-
 # This variable represents the global component registry
 registry = ComponentRegistry()
 
 def register(name):
     """Class decorator to register a component.
```

### Comparing `django_components-0.9.1/django_components/component_registry.py` & `django_components-0.9.2/django_components/component_registry.py`

 * *Files identical despite different names*

### Comparing `django_components-0.9.1/django_components/templatetags/component_tags.py` & `django_components-0.9.2/django_components/templatetags/component_tags.py`

 * *Files identical despite different names*

### Comparing `django_components-0.9.1/django_components.egg-info/PKG-INFO` & `django_components-0.9.2/django_components.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-components
-Version: 0.9.1
+Version: 0.9.2
 Summary: A way to create simple reusable template components in Django.
 Home-page: https://github.com/EmilStenstrom/django-components/
 Author: Emil Stenström
 Author-email: emil@emilstenstrom.se
 License: MIT
 Description: # django-components
         <a href="https://github.com/EmilStenstrom/django-components/actions?query=workflow%3A%22Run+tests%22"><img align="right" src="https://github.com/EmilStenstrom/django-components/workflows/Run%20tests/badge.svg" alt="Show test status"></a>
@@ -165,34 +165,35 @@
                     "date": date,
                 }
         
             def template(self, context):
                 return "[your app]/components/calendar/calendar.html"
         
             class Media:
-                css = {'all': ['[your app]/components/calendar/calendar.css']}
-                js = ['[your app]/components/calendar/calendar.js']
+                css = '[your app]/components/calendar/calendar.css'
+                js = '[your app]/components/calendar/calendar.js'
         ```
         
         And voilá!! We've created our first component.
         
         # Use the component in a template
         
-        First load the `component_tags` tag library, then use the `component_dependencies` and `component` tags to render the component to the page.
+        First load the `component_tags` tag library, then use the `component_[js/css]_dependencies` and `component` tags to render the component to the page.
         
         ```htmldjango
         {% load component_tags %}
         <!DOCTYPE html>
         <html>
         <head>
             <title>My example calendar</title>
-            {% component_dependencies %}
+            {% component_css_dependencies %}
         </head>
         <body>
             {% component "calendar" date="2015-06-19" %}
+            {% component_js_dependencies %}
         </body>
         <html>
         ```
         
         The output from the above template will be:
         
         ```html
```

### Comparing `django_components-0.9.1/setup.py` & `django_components-0.9.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 # -*- coding: utf-8 -*-
 import os
 
 from setuptools import find_packages, setup
 
-VERSION = '0.9.1'
+VERSION = '0.9.2'
 
 setup(
     name="django_components",
     packages=find_packages(exclude=["tests"]),
     version=VERSION,
     description="A way to create simple reusable template components in Django.",
     long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
```

