# Comparing `tmp/datclass-0.1.8.tar.gz` & `tmp/datclass-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "datclass-0.1.8.tar", last modified: Mon Apr  3 06:46:17 2023, max compression
+gzip compressed data, was "datclass-0.1.9.tar", last modified: Wed Apr  5 06:03:35 2023, max compression
```

## Comparing `datclass-0.1.8.tar` & `datclass-0.1.9.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 06:46:17.372141 datclass-0.1.8/
--rw-r--r--   0 runner    (1001) docker     (123)     1063 2023-04-03 06:46:12.000000 datclass-0.1.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-03 06:46:12.000000 datclass-0.1.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     7481 2023-04-03 06:46:17.372141 datclass-0.1.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     6743 2023-04-03 06:46:12.000000 datclass-0.1.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     1091 2023-04-03 06:46:12.000000 datclass-0.1.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-03 06:46:12.000000 datclass-0.1.8/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-03 06:46:17.372141 datclass-0.1.8/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 06:46:17.372141 datclass-0.1.8/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 06:46:17.372141 datclass-0.1.8/src/datclass/
--rw-r--r--   0 runner    (1001) docker     (123)     4174 2023-04-03 06:46:16.000000 datclass-0.1.8/src/datclass/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       65 2023-04-03 06:46:12.000000 datclass-0.1.8/src/datclass/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7727 2023-04-03 06:46:12.000000 datclass-0.1.8/src/datclass/gens.py
--rw-r--r--   0 runner    (1001) docker     (123)     2805 2023-04-03 06:46:12.000000 datclass-0.1.8/src/datclass/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 06:46:17.372141 datclass-0.1.8/src/datclass.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     7481 2023-04-03 06:46:17.000000 datclass-0.1.8/src/datclass.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-04-03 06:46:17.000000 datclass-0.1.8/src/datclass.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-03 06:46:17.000000 datclass-0.1.8/src/datclass.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       43 2023-04-03 06:46:17.000000 datclass-0.1.8/src/datclass.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       45 2023-04-03 06:46:17.000000 datclass-0.1.8/src/datclass.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-03 06:46:17.000000 datclass-0.1.8/src/datclass.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:03:35.830290 datclass-0.1.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     1063 2023-04-05 06:03:30.000000 datclass-0.1.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-05 06:03:30.000000 datclass-0.1.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     7481 2023-04-05 06:03:35.826290 datclass-0.1.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     6743 2023-04-05 06:03:30.000000 datclass-0.1.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1091 2023-04-05 06:03:30.000000 datclass-0.1.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-05 06:03:30.000000 datclass-0.1.9/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-05 06:03:35.830290 datclass-0.1.9/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:03:35.826290 datclass-0.1.9/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:03:35.826290 datclass-0.1.9/src/datclass/
+-rw-r--r--   0 runner    (1001) docker     (123)     4174 2023-04-05 06:03:35.000000 datclass-0.1.9/src/datclass/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       65 2023-04-05 06:03:30.000000 datclass-0.1.9/src/datclass/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7722 2023-04-05 06:03:30.000000 datclass-0.1.9/src/datclass/gens.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2805 2023-04-05 06:03:30.000000 datclass-0.1.9/src/datclass/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 06:03:35.826290 datclass-0.1.9/src/datclass.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     7481 2023-04-05 06:03:35.000000 datclass-0.1.9/src/datclass.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-04-05 06:03:35.000000 datclass-0.1.9/src/datclass.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 06:03:35.000000 datclass-0.1.9/src/datclass.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       43 2023-04-05 06:03:35.000000 datclass-0.1.9/src/datclass.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       45 2023-04-05 06:03:35.000000 datclass-0.1.9/src/datclass.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-05 06:03:35.000000 datclass-0.1.9/src/datclass.egg-info/top_level.txt
```

### Comparing `datclass-0.1.8/LICENSE` & `datclass-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `datclass-0.1.8/PKG-INFO` & `datclass-0.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: datclass
-Version: 0.1.8
+Version: 0.1.9
 Summary: python package dataclass utils
 Author: foyoux
 Project-URL: Source, https://github.com/foyoux/datclass
 Project-URL: Homepage, https://github.com/foyoux/datclass
 Project-URL: Bug Tracker, https://github.com/foyoux/datclass/issues
 Keywords: dataclass
 Classifier: Programming Language :: Python
```

### Comparing `datclass-0.1.8/README.md` & `datclass-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `datclass-0.1.8/pyproject.toml` & `datclass-0.1.9/pyproject.toml`

 * *Files identical despite different names*

### Comparing `datclass-0.1.8/src/datclass/__init__.py` & `datclass-0.1.9/src/datclass/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 __title__ = 'datclass'
 __author__ = 'foyoux'
-__version__ = '0.1.8'
+__version__ = '0.1.9'
 
 __all__ = [
     'main',
     'DatGen',
     'DatClass',
 ]
```

### Comparing `datclass-0.1.8/src/datclass/gens.py` & `datclass-0.1.9/src/datclass/gens.py`

 * *Files 1% similar despite different names*

```diff
@@ -151,24 +151,24 @@
         if cls_name == attr_name:
             # 类名与属性名重名，则尾加下划线（此种情况现已不存在，因为属性名的首字母会置为小写）
             cls_name = f'{cls_name}_'
         if keyword.iskeyword(cls_name):
             # 是关键字（eg: None），则加下划线
             cls_name = f'{cls_name}_'
         # 返回之前先记录
-        self.class_map.append(cls_name)
         return cls_name
 
-    def gen_datclass(self, dat: Union[list, dict], name='Object', recursive=False, level=0) -> Class:
+    def gen_datclass(self, dat: Union[list, dict], name='Object', recursive=True, level=0) -> Class:
         """
         :param dat: 列表 或者 字典
         :param name: 主类名称
         :param recursive: 是否递归生成
         :param level: 层级，用以解决 类名 冲突问题
         """
+        self.class_map.append(name)
         try:
             dat = merge_list_dict(dat)
         except TypeError:
             pass
         # 这些针对模块
         self.imports.dataclass = True
         self.imports.DatClass = True
```

### Comparing `datclass-0.1.8/src/datclass/utils.py` & `datclass-0.1.9/src/datclass/utils.py`

 * *Files identical despite different names*

### Comparing `datclass-0.1.8/src/datclass.egg-info/PKG-INFO` & `datclass-0.1.9/src/datclass.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: datclass
-Version: 0.1.8
+Version: 0.1.9
 Summary: python package dataclass utils
 Author: foyoux
 Project-URL: Source, https://github.com/foyoux/datclass
 Project-URL: Homepage, https://github.com/foyoux/datclass
 Project-URL: Bug Tracker, https://github.com/foyoux/datclass/issues
 Keywords: dataclass
 Classifier: Programming Language :: Python
```

