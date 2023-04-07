# Comparing `tmp/manim_slides-4.9.1.tar.gz` & `tmp/manim_slides-4.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "manim_slides-4.9.1.tar", max compression
+gzip compressed data, was "manim_slides-4.9.2.tar", max compression
```

## Comparing `manim_slides-4.9.1.tar` & `manim_slides-4.9.2.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0     1073 2023-02-25 16:41:40.136241 manim_slides-4.9.1/LICENSE.md
--rw-r--r--   0        0        0     7841 2023-02-25 16:41:40.136241 manim_slides-4.9.1/README.md
--rw-r--r--   0        0        0       96 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/__init__.py
--rw-r--r--   0        0        0     2518 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/__main__.py
--rw-r--r--   0        0        0       22 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/__version__.py
--rw-r--r--   0        0        0     2206 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/commons.py
--rw-r--r--   0        0        0     7388 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/config.py
--rw-r--r--   0        0        0    14295 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/convert.py
--rw-r--r--   0        0        0    13193 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/data/revealjs_template.html
--rw-r--r--   0        0        0       70 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/defaults.py
--rw-r--r--   0        0        0     2116 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/manim.py
--rw-r--r--   0        0        0    28546 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/present.py
--rw-r--r--   0        0        0     7451 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/resources.py
--rw-r--r--   0        0        0     8305 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/slide.py
--rw-r--r--   0        0        0     5733 2023-02-25 16:41:40.140241 manim_slides-4.9.1/manim_slides/wizard.py
--rw-r--r--   0        0        0     2526 2023-02-25 16:41:40.144241 manim_slides-4.9.1/pyproject.toml
--rw-r--r--   0        0        0     9326 1970-01-01 00:00:00.000000 manim_slides-4.9.1/PKG-INFO
+-rw-r--r--   0        0        0     1073 2023-02-25 23:18:15.517869 manim_slides-4.9.2/LICENSE.md
+-rw-r--r--   0        0        0     7841 2023-02-25 23:18:15.517869 manim_slides-4.9.2/README.md
+-rw-r--r--   0        0        0       96 2023-02-25 23:18:15.517869 manim_slides-4.9.2/manim_slides/__init__.py
+-rw-r--r--   0        0        0     2518 2023-02-25 23:18:15.517869 manim_slides-4.9.2/manim_slides/__main__.py
+-rw-r--r--   0        0        0       22 2023-02-25 23:18:15.517869 manim_slides-4.9.2/manim_slides/__version__.py
+-rw-r--r--   0        0        0     2206 2023-02-25 23:18:15.517869 manim_slides-4.9.2/manim_slides/commons.py
+-rw-r--r--   0        0        0     7388 2023-02-25 23:18:15.517869 manim_slides-4.9.2/manim_slides/config.py
+-rw-r--r--   0        0        0    14290 2023-02-25 23:18:15.517869 manim_slides-4.9.2/manim_slides/convert.py
+-rw-r--r--   0        0        0    13193 2023-02-25 23:18:15.517869 manim_slides-4.9.2/manim_slides/data/revealjs_template.html
+-rw-r--r--   0        0        0       70 2023-02-25 23:18:15.517869 manim_slides-4.9.2/manim_slides/defaults.py
+-rw-r--r--   0        0        0     2116 2023-02-25 23:18:15.517869 manim_slides-4.9.2/manim_slides/manim.py
+-rw-r--r--   0        0        0    28546 2023-02-25 23:18:15.517869 manim_slides-4.9.2/manim_slides/present.py
+-rw-r--r--   0        0        0     7451 2023-02-25 23:18:15.521869 manim_slides-4.9.2/manim_slides/resources.py
+-rw-r--r--   0        0        0     8305 2023-02-25 23:18:15.521869 manim_slides-4.9.2/manim_slides/slide.py
+-rw-r--r--   0        0        0     5733 2023-02-25 23:18:15.521869 manim_slides-4.9.2/manim_slides/wizard.py
+-rw-r--r--   0        0        0     2526 2023-02-25 23:18:15.521869 manim_slides-4.9.2/pyproject.toml
+-rw-r--r--   0        0        0     9326 1970-01-01 00:00:00.000000 manim_slides-4.9.2/PKG-INFO
```

### Comparing `manim_slides-4.9.1/LICENSE.md` & `manim_slides-4.9.2/LICENSE.md`

 * *Files identical despite different names*

### Comparing `manim_slides-4.9.1/README.md` & `manim_slides-4.9.2/README.md`

 * *Files identical despite different names*

### Comparing `manim_slides-4.9.1/manim_slides/__main__.py` & `manim_slides-4.9.2/manim_slides/__main__.py`

 * *Files identical despite different names*

### Comparing `manim_slides-4.9.1/manim_slides/commons.py` & `manim_slides-4.9.2/manim_slides/commons.py`

 * *Files identical despite different names*

### Comparing `manim_slides-4.9.1/manim_slides/config.py` & `manim_slides-4.9.2/manim_slides/config.py`

 * *Files identical despite different names*

### Comparing `manim_slides-4.9.1/manim_slides/convert.py` & `manim_slides-4.9.2/manim_slides/convert.py`

 * *Files 1% similar despite different names*

```diff
@@ -329,15 +329,15 @@
 
         os.makedirs(full_assets_dir, exist_ok=True)
 
         for presentation_config in self.presentation_configs:
             presentation_config.concat_animations().copy_to(full_assets_dir)
 
         with open(dest, "w") as f:
-            sections = "".join(self.get_sections_iter(full_assets_dir))
+            sections = "".join(self.get_sections_iter(assets_dir))
 
             revealjs_template = self.load_template()
             content = revealjs_template.format(sections=sections, **self.dict())
 
             f.write(content)
```

### Comparing `manim_slides-4.9.1/manim_slides/data/revealjs_template.html` & `manim_slides-4.9.2/manim_slides/data/revealjs_template.html`

 * *Files identical despite different names*

### Comparing `manim_slides-4.9.1/manim_slides/manim.py` & `manim_slides-4.9.2/manim_slides/manim.py`

 * *Files identical despite different names*

### Comparing `manim_slides-4.9.1/manim_slides/present.py` & `manim_slides-4.9.2/manim_slides/present.py`

 * *Files identical despite different names*

### Comparing `manim_slides-4.9.1/manim_slides/resources.py` & `manim_slides-4.9.2/manim_slides/resources.py`

 * *Files identical despite different names*

### Comparing `manim_slides-4.9.1/manim_slides/slide.py` & `manim_slides-4.9.2/manim_slides/slide.py`

 * *Files identical despite different names*

### Comparing `manim_slides-4.9.1/manim_slides/wizard.py` & `manim_slides-4.9.2/manim_slides/wizard.py`

 * *Files identical despite different names*

### Comparing `manim_slides-4.9.1/pyproject.toml` & `manim_slides-4.9.2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -57,15 +57,15 @@
 license = "MIT"
 name = "manim-slides"
 packages = [
   {include = "manim_slides"}
 ]
 readme = "README.md"
 repository = "https://github.com/jeertmans/manim-slides"
-version = "4.9.1"
+version = "4.9.2"
 
 [tool.poetry.dependencies]
 click = "^8.1.3"
 click-default-group = "^1.2.2"
 numpy = "^1.19"
 opencv-python = "^4.6.0.66"
 pydantic = "^1.10.2"
```

### Comparing `manim_slides-4.9.1/PKG-INFO` & `manim_slides-4.9.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: manim-slides
-Version: 4.9.1
+Version: 4.9.2
 Summary: Tool for live presentations using manim
 Home-page: https://github.com/jeertmans/manim-slides
 License: MIT
 Keywords: manim,slides,plugin,manimgl
 Author: Jérome Eertmans
 Author-email: jeertmans@icloud.com
 Requires-Python: >=3.8.1,<3.12
```

