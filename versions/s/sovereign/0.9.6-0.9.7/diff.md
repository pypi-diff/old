# Comparing `tmp/sovereign-0.9.6.tar.gz` & `tmp/sovereign-0.9.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sovereign-0.9.6.tar", last modified: Thu Mar 11 23:25:56 2021, max compression
+gzip compressed data, was "sovereign-0.9.7.tar", last modified: Fri Mar 12 03:23:50 2021, max compression
```

## Comparing `sovereign-0.9.6.tar` & `sovereign-0.9.7.tar`

### file list

```diff
@@ -1,44 +1,44 @@
--rw-r--r--   0        0        0      560 2021-03-11 23:23:43.942972 sovereign-0.9.6/LICENSE.txt
--rw-r--r--   0        0        0     4021 2021-03-11 23:23:43.942972 sovereign-0.9.6/README.md
--rw-r--r--   0        0        0     3321 2021-03-11 23:23:43.946972 sovereign-0.9.6/pyproject.toml
--rw-r--r--   0        0        0     1298 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/__init__.py
--rw-r--r--   0        0        0     3578 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/app.py
--rw-r--r--   0        0        0     5219 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/config_loader.py
--rw-r--r--   0        0        0     2091 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/context.py
--rw-r--r--   0        0        0     1369 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/decorators.py
--rw-r--r--   0        0        0     5357 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/discovery.py
--rw-r--r--   0        0        0     1841 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/logs.py
--rw-r--r--   0        0        0     3230 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/middlewares.py
--rw-r--r--   0        0        0     1827 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/modifiers/__init__.py
--rw-r--r--   0        0        0     2893 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/modifiers/lib.py
--rw-r--r--   0        0        0      327 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/modifiers/test.py
--rw-r--r--   0        0        0    12476 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/schemas.py
--rw-r--r--   0        0        0      664 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/server.py
--rw-r--r--   0        0        0     9279 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/sources/__init__.py
--rw-r--r--   0        0        0     1736 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/sources/file.py
--rw-r--r--   0        0        0      883 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/sources/inline.py
--rw-r--r--   0        0        0      809 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/sources/lib.py
--rw-r--r--   0        0        0     1158 2021-03-11 23:23:43.946972 sovereign-0.9.6/src/sovereign/static/sass/style.scss
--rw-r--r--   0        0        0   447517 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/static/style.css
--rw-r--r--   0        0        0     1937 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/statistics.py
--rw-r--r--   0        0        0     2363 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/templates/base.html
--rw-r--r--   0        0        0      603 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/templates/err.html
--rw-r--r--   0        0        0     6247 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/templates/resources.html
--rw-r--r--   0        0        0      666 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/templates/ul_filter.html
--rw-r--r--   0        0        0        0 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/utils/__init__.py
--rw-r--r--   0        0        0     1644 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/utils/auth.py
--rw-r--r--   0        0        0     1607 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/utils/crypto.py
--rw-r--r--   0        0        0     2598 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/utils/dictupdate.py
--rw-r--r--   0        0        0     3234 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/utils/eds.py
--rw-r--r--   0        0        0      793 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/utils/mock.py
--rw-r--r--   0        0        0      981 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/utils/templates.py
--rw-r--r--   0        0        0      307 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/utils/version_info.py
--rw-r--r--   0        0        0      968 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/utils/weighted_clusters.py
--rw-r--r--   0        0        0        0 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/views/__init__.py
--rw-r--r--   0        0        0     3940 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/views/admin.py
--rw-r--r--   0        0        0     1731 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/views/crypto.py
--rw-r--r--   0        0        0     4038 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/views/discovery.py
--rw-r--r--   0        0        0     1101 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/views/healthchecks.py
--rw-r--r--   0        0        0     6689 2021-03-11 23:23:43.950972 sovereign-0.9.6/src/sovereign/views/interface.py
--rw-r--r--   0        0        0     6059 2021-03-11 23:25:56.582166 sovereign-0.9.6/setup.py
--rw-r--r--   0        0        0     6161 2021-03-11 23:25:56.582685 sovereign-0.9.6/PKG-INFO
+-rw-r--r--   0        0        0      560 2021-03-12 03:21:36.677631 sovereign-0.9.7/LICENSE.txt
+-rw-r--r--   0        0        0     4021 2021-03-12 03:21:36.677631 sovereign-0.9.7/README.md
+-rw-r--r--   0        0        0     3321 2021-03-12 03:21:36.681630 sovereign-0.9.7/pyproject.toml
+-rw-r--r--   0        0        0     1298 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/__init__.py
+-rw-r--r--   0        0        0     3578 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/app.py
+-rw-r--r--   0        0        0     5219 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/config_loader.py
+-rw-r--r--   0        0        0     2091 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/context.py
+-rw-r--r--   0        0        0     1369 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/decorators.py
+-rw-r--r--   0        0        0     5357 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/discovery.py
+-rw-r--r--   0        0        0     1841 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/logs.py
+-rw-r--r--   0        0        0     3230 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/middlewares.py
+-rw-r--r--   0        0        0     1827 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/modifiers/__init__.py
+-rw-r--r--   0        0        0     2893 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/modifiers/lib.py
+-rw-r--r--   0        0        0      327 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/modifiers/test.py
+-rw-r--r--   0        0        0    12476 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/schemas.py
+-rw-r--r--   0        0        0      664 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/server.py
+-rw-r--r--   0        0        0     9279 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/sources/__init__.py
+-rw-r--r--   0        0        0     1736 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/sources/file.py
+-rw-r--r--   0        0        0      883 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/sources/inline.py
+-rw-r--r--   0        0        0      809 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/sources/lib.py
+-rw-r--r--   0        0        0     1158 2021-03-12 03:21:36.681630 sovereign-0.9.7/src/sovereign/static/sass/style.scss
+-rw-r--r--   0        0        0   447517 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/static/style.css
+-rw-r--r--   0        0        0     1937 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/statistics.py
+-rw-r--r--   0        0        0     2296 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/templates/base.html
+-rw-r--r--   0        0        0      603 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/templates/err.html
+-rw-r--r--   0        0        0     6366 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/templates/resources.html
+-rw-r--r--   0        0        0      666 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/templates/ul_filter.html
+-rw-r--r--   0        0        0        0 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/utils/__init__.py
+-rw-r--r--   0        0        0     1644 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/utils/auth.py
+-rw-r--r--   0        0        0     1607 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/utils/crypto.py
+-rw-r--r--   0        0        0     2598 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/utils/dictupdate.py
+-rw-r--r--   0        0        0     3234 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/utils/eds.py
+-rw-r--r--   0        0        0      793 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/utils/mock.py
+-rw-r--r--   0        0        0      981 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/utils/templates.py
+-rw-r--r--   0        0        0      307 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/utils/version_info.py
+-rw-r--r--   0        0        0      968 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/utils/weighted_clusters.py
+-rw-r--r--   0        0        0        0 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/views/__init__.py
+-rw-r--r--   0        0        0     3940 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/views/admin.py
+-rw-r--r--   0        0        0     1731 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/views/crypto.py
+-rw-r--r--   0        0        0     4038 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/views/discovery.py
+-rw-r--r--   0        0        0     1101 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/views/healthchecks.py
+-rw-r--r--   0        0        0     6858 2021-03-12 03:21:36.685630 sovereign-0.9.7/src/sovereign/views/interface.py
+-rw-r--r--   0        0        0     6059 2021-03-12 03:23:50.702263 sovereign-0.9.7/setup.py
+-rw-r--r--   0        0        0     6161 2021-03-12 03:23:50.702766 sovereign-0.9.7/PKG-INFO
```

### Comparing `sovereign-0.9.6/LICENSE.txt` & `sovereign-0.9.7/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/README.md` & `sovereign-0.9.7/README.md`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/pyproject.toml` & `sovereign-0.9.7/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "sovereign"
-version = "0.9.6"
+version = "0.9.7"
 description = "Envoy Proxy control-plane written in Python"
 license = "Apache-2.0"
 packages = [
     { include = "sovereign", from = "src", format = "sdist" }
 ]
 readme = "README.md"
 #include = ["CHANGELOG.md", "CODE_OF_CONDUCT.md"]
```

### Comparing `sovereign-0.9.6/src/sovereign/__init__.py` & `sovereign-0.9.7/src/sovereign/__init__.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/app.py` & `sovereign-0.9.7/src/sovereign/app.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/config_loader.py` & `sovereign-0.9.7/src/sovereign/config_loader.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/context.py` & `sovereign-0.9.7/src/sovereign/context.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/decorators.py` & `sovereign-0.9.7/src/sovereign/decorators.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/discovery.py` & `sovereign-0.9.7/src/sovereign/discovery.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/logs.py` & `sovereign-0.9.7/src/sovereign/logs.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/middlewares.py` & `sovereign-0.9.7/src/sovereign/middlewares.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/modifiers/__init__.py` & `sovereign-0.9.7/src/sovereign/modifiers/__init__.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/modifiers/lib.py` & `sovereign-0.9.7/src/sovereign/modifiers/lib.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/schemas.py` & `sovereign-0.9.7/src/sovereign/schemas.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/server.py` & `sovereign-0.9.7/src/sovereign/server.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/sources/__init__.py` & `sovereign-0.9.7/src/sovereign/sources/__init__.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/sources/file.py` & `sovereign-0.9.7/src/sovereign/sources/file.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/sources/inline.py` & `sovereign-0.9.7/src/sovereign/sources/inline.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/sources/lib.py` & `sovereign-0.9.7/src/sovereign/sources/lib.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/static/sass/style.scss` & `sovereign-0.9.7/src/sovereign/static/sass/style.scss`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/static/style.css` & `sovereign-0.9.7/src/sovereign/static/style.css`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/statistics.py` & `sovereign-0.9.7/src/sovereign/statistics.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/templates/base.html` & `sovereign-0.9.7/src/sovereign/templates/base.html`

 * *Files 11% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 <!DOCTYPE html>
 <html lang="en" class="has-navbar-fixed-top">
 <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
-    <link rel="stylesheet" type="text/css" href="/static/mystyles.css">
+    <link rel="stylesheet" type="text/css" href="/static/style.css">
     <title>{% block title %}{% endblock %} - Sovereign</title>
     {%- block head %}{% endblock %}
 </head>
 <body>
 <div class="columns">
     <div class="column"></div>
     {%- block nav %}
@@ -54,13 +54,11 @@
 
     {%- block body %}
     {% endblock -%}
     </div>
     <div class="column"></div>
 </div>
 <footer class="footer">
-    <div class="content has-text-centered is-small">
-        <p>{{ last_update }}</p>
-    </div>
+{% block footer %}{% endblock %}
 </footer>
 </body>
 </html>
```

#### html2text {}

```diff
@@ -6,8 +6,8 @@
 {%- set active_page = resource_type|default('redirect_to_docs') -%}
 ***_sovereign_***
 Resources
 {%- for type in all_types %} {{_type_}} {%- endfor %}
 OpenAPI
  {%- endblock %} {%- block subnav %} {%- endblock %} {%- block body %} {%
 endblock -%}
-{{ last_update }}
+ {% block footer %}{% endblock %}
```

### Comparing `sovereign-0.9.6/src/sovereign/templates/err.html` & `sovereign-0.9.7/src/sovereign/templates/err.html`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/templates/resources.html` & `sovereign-0.9.7/src/sovereign/templates/resources.html`

 * *Files 4% similar despite different names*

```diff
@@ -148,7 +148,12 @@
                 <p class="content is-small">
                     {{ vs_count }} {{ plural.get(vs_count, 'resources') }}
                 </p>
             </div>
         </nav>
     {% endif %}
 {% endblock -%}
+{% block footer %}
+<div class="content has-text-centered is-small">
+    <p>{{ last_update }}</p>
+</div>
+{% endblock %}
```

### Comparing `sovereign-0.9.6/src/sovereign/templates/ul_filter.html` & `sovereign-0.9.7/src/sovereign/templates/ul_filter.html`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/utils/auth.py` & `sovereign-0.9.7/src/sovereign/utils/auth.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/utils/crypto.py` & `sovereign-0.9.7/src/sovereign/utils/crypto.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/utils/dictupdate.py` & `sovereign-0.9.7/src/sovereign/utils/dictupdate.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/utils/eds.py` & `sovereign-0.9.7/src/sovereign/utils/eds.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/utils/mock.py` & `sovereign-0.9.7/src/sovereign/utils/mock.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/utils/templates.py` & `sovereign-0.9.7/src/sovereign/utils/templates.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/utils/weighted_clusters.py` & `sovereign-0.9.7/src/sovereign/utils/weighted_clusters.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/views/admin.py` & `sovereign-0.9.7/src/sovereign/views/admin.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/views/crypto.py` & `sovereign-0.9.7/src/sovereign/views/crypto.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/views/discovery.py` & `sovereign-0.9.7/src/sovereign/views/discovery.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/views/healthchecks.py` & `sovereign-0.9.7/src/sovereign/views/healthchecks.py`

 * *Files identical despite different names*

### Comparing `sovereign-0.9.6/src/sovereign/views/interface.py` & `sovereign-0.9.7/src/sovereign/views/interface.py`

 * *Files 4% similar despite different names*

```diff
@@ -11,18 +11,25 @@
 from sovereign.views.discovery import perform_discovery
 
 router = APIRouter()
 
 all_types = [t.value for t in DiscoveryTypes]
 
 
-@router.get('/', summary='Redirect to resource interface')
+@router.get('/')
 async def ui_main(request: Request):
     try:
-        return RedirectResponse(url=f'/ui/resources/{all_types[0]}')
+        return html_templates.TemplateResponse(
+            name='base.html',
+            media_type='text/html',
+            context={
+                'request': request,
+                'all_types': all_types,
+                'last_update': str(source_metadata),
+            })
     except IndexError:
         return html_templates.TemplateResponse(
             name='err.html',
             media_type='text/html',
             context={
                 'request': request,
                 'title': 'No resource types configured',
```

### Comparing `sovereign-0.9.6/setup.py` & `sovereign-0.9.7/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -44,15 +44,15 @@
  'sovereign.modifiers': ['sovereign_3rd_party_test = '
                          'sovereign.modifiers.test:Test'],
  'sovereign.sources': ['file = sovereign.sources.file:File',
                        'inline = sovereign.sources.inline:Inline']}
 
 setup_kwargs = {
     'name': 'sovereign',
-    'version': '0.9.6',
+    'version': '0.9.7',
     'description': 'Envoy Proxy control-plane written in Python',
     'long_description': 'sovereign\n=========\n\nMission statement\n-----------------\nThis project implements a JSON control-plane based on the [envoy](https://envoyproxy.io) [data-plane-api](https://github.com/envoyproxy/data-plane-api)\n\nThe purpose of `sovereign` is to supply downstream envoy proxies with \nconfiguration in near-realtime by responding to discovery requests.\n\nMechanism of Operation\n----------------------\ntl;dr version:\n```\n* Polls HTTP/File/Other for data\n* (optional) Applies transforms to the data\n* Uses the data to generate Envoy configuration from templates\n```\n\nIn a nutshell, Sovereign \ngathers contextual data (*"sources"* and *"template context"*), \noptionally applies transforms to that data (using *"modifiers"*) and finally \nuses the data to generate envoy configuration from either python code, or jinja2 templates.\n\nThis is performed in a semi-stateless way, where the only state is data cached in memory.\n\nTemplate context is intended to be statically configured, whereas *Sources* \nare meant to be dynamic - for example, fetching from an API, an S3 bucket, \nor a file that receives updates.\n\n*Modifiers* can mutate the data retrieved from sources, just in case the data \nis in a less than favorable structure.\n\nBoth modifiers and sources are pluggable, i.e. it\'s easy to write your own and \nplug them into Sovereign for your use-case.\n\nCurrently, Sovereign supports only providing configuration to Envoy as JSON. \nThat is to say, gRPC is not supported yet. Contributions in this area are highly\nappreciated!\n\nThe JSON configuration can be viewed in real-time with Sovereign\'s read-only web interface.\n\nRequirements\n------------\n* Python 3.8+\n\nInstallation\n------------\n```\npip install sovereign\n```\n\nDocumentation\n-------------\n[Read the docs here!](https://vsyrakis.bitbucket.io/sovereign/docs/)\n\n:new: Read-only user interface\n------------------------\nAdded in `v0.5.3`!\n\nThis interface allows you to browse the resources currently returned by Sovereign.\n\n![Sovereign User Interface Screenshot](https://bitbucket.org/atlassian/sovereign/src/master/assets/sovereign_ui.png)\n\nLocal development\n=================\n\nRequirements\n------------\n* Docker\n* Docker-compose\n\nInstalling dependencies for dev\n-------------------------------\nI recommend creating a virtualenv before doing any dev work\n\n```\npython3 -m venv venv\nsource venv/bin/activate\npip install -r requirements-dev.txt\n```\n\nRunning locally\n---------------\nRunning the test env\n\n```\nmake run\n```\n    \nRunning the test env daemonized\n\n```\nmake run-daemon\n```\n\nPylint\n\n```\nmake lint\n```\n\nUnit tests\n\n```\nmake unit\n```\n\nAcceptance tests\n\n```\nmake run-daemon acceptance\n```\n\n\nContributors\n============\n\nPull requests, issues and comments welcome. For pull requests:\n\n* Add tests for new features and bug fixes\n* Follow the existing style\n* Separate unrelated changes into multiple pull requests\n\nSee the existing issues for things to start contributing.\n\nFor bigger changes, make sure you start a discussion first by creating\nan issue and explaining the intended change.\n\nAtlassian requires contributors to sign a Contributor License Agreement,\nknown as a CLA. This serves as a record stating that the contributor is\nentitled to contribute the code/documentation/translation to the project\nand is willing to have it used in distributions and derivative works\n(or is willing to transfer ownership).\n\nPrior to accepting your contributions we ask that you please follow the appropriate\nlink below to digitally sign the CLA. The Corporate CLA is for those who are\ncontributing as a member of an organization and the individual CLA is for\nthose contributing as an individual.\n\n* [CLA for corporate contributors](https://na2.docusign.net/Member/PowerFormSigning.aspx?PowerFormId=e1c17c66-ca4d-4aab-a953-2c231af4a20b)\n* [CLA for individuals](https://na2.docusign.net/Member/PowerFormSigning.aspx?PowerFormId=3f94fbdc-2fbe-46ac-b14c-5d152700ae5d)\n\n\nLicense\n========\n\nCopyright (c) 2018 Atlassian and others.\nApache 2.0 licensed, see [LICENSE.txt](LICENSE.txt) file.\n\n\n',
     'author': 'Vasili Syrakis',
     'author_email': 'vsyrakis@atlassian.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://pypi.org/project/sovereign/',
```

### Comparing `sovereign-0.9.6/PKG-INFO` & `sovereign-0.9.7/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sovereign
-Version: 0.9.6
+Version: 0.9.7
 Summary: Envoy Proxy control-plane written in Python
 Home-page: https://pypi.org/project/sovereign/
 License: Apache-2.0
 Keywords: envoy,envoyproxy,control-plane,management,server
 Author: Vasili Syrakis
 Author-email: vsyrakis@atlassian.com
 Requires-Python: >=3.8,<4.0
```

