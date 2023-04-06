# Comparing `tmp/muutils-0.3.6.tar.gz` & `tmp/muutils-0.3.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "muutils-0.3.6.tar", max compression
+gzip compressed data, was "muutils-0.3.7.tar", max compression
```

## Comparing `muutils-0.3.6.tar` & `muutils-0.3.7.tar`

### file list

```diff
@@ -1,41 +1,41 @@
--rw-r--r--   0        0        0    35823 2021-01-10 20:54:08.928022 muutils-0.3.6/LICENSE
--rw-r--r--   0        0        0       22 2023-04-05 21:47:49.277905 muutils-0.3.6/muutils/__init__.py
--rw-r--r--   0        0        0     3910 2023-03-24 22:25:29.757321 muutils-0.3.6/muutils/_wip/dataclass_validator.py
--rw-r--r--   0        0        0     4652 2023-02-16 09:10:54.613167 muutils-0.3.6/muutils/_wip/experiments.ipynb
--rw-r--r--   0        0        0     5835 2023-03-24 22:25:29.757321 muutils-0.3.6/muutils/_wip/gptdataset.py
--rw-r--r--   0        0        0    23453 2023-03-24 22:25:29.758323 muutils-0.3.6/muutils/_wip/json_serialize_old.py
--rw-r--r--   0        0        0     3286 2023-03-24 22:25:29.758323 muutils-0.3.6/muutils/_wip/lazy_externals.py
--rw-r--r--   0        0        0     9214 2023-03-24 22:25:29.759320 muutils-0.3.6/muutils/_wip/newargparser.py
--rw-r--r--   0        0        0     7414 2023-03-24 22:25:29.760323 muutils-0.3.6/muutils/_wip/torch_util_old.py
--rw-r--r--   0        0        0     2037 2023-04-05 21:47:49.278906 muutils-0.3.6/muutils/dictmagic.py
--rw-r--r--   0        0        0     1613 2023-03-06 19:25:21.018548 muutils-0.3.6/muutils/group_equiv.py
--rw-r--r--   0        0        0      897 2023-03-24 22:25:29.761326 muutils-0.3.6/muutils/json_serialize/__init__.py
--rw-r--r--   0        0        0     6016 2023-03-30 19:44:39.204722 muutils-0.3.6/muutils/json_serialize/array.py
--rw-r--r--   0        0        0    13391 2023-03-24 22:25:29.762321 muutils-0.3.6/muutils/json_serialize/dataclass_factories.py
--rw-r--r--   0        0        0     8906 2023-04-05 06:39:57.784877 muutils-0.3.6/muutils/json_serialize/json_serialize.py
--rw-r--r--   0        0        0    15588 2023-04-05 21:47:49.279906 muutils-0.3.6/muutils/json_serialize/serializable_dataclass.py
--rw-r--r--   0        0        0     3764 2023-03-28 07:47:43.743882 muutils-0.3.6/muutils/json_serialize/util.py
--rw-r--r--   0        0        0     1878 2023-03-24 22:25:29.764321 muutils-0.3.6/muutils/jsonlines.py
--rw-r--r--   0        0        0      267 2023-03-06 19:25:21.021547 muutils-0.3.6/muutils/logger/__init__.py
--rw-r--r--   0        0        0     1183 2023-03-06 19:25:21.021547 muutils-0.3.6/muutils/logger/exception_context.py
--rw-r--r--   0        0        0     1667 2023-03-24 22:25:29.765321 muutils-0.3.6/muutils/logger/headerfuncs.py
--rw-r--r--   0        0        0     2072 2023-03-24 22:25:29.765321 muutils-0.3.6/muutils/logger/log_util.py
--rw-r--r--   0        0        0    10669 2023-03-24 22:25:29.766326 muutils-0.3.6/muutils/logger/logger.py
--rw-r--r--   0        0        0     3796 2023-03-24 22:25:29.767323 muutils-0.3.6/muutils/logger/loggingstream.py
--rw-r--r--   0        0        0     2124 2023-03-24 22:25:29.768323 muutils-0.3.6/muutils/logger/simplelogger.py
--rw-r--r--   0        0        0     2488 2023-03-24 22:25:29.769322 muutils-0.3.6/muutils/logger/timing.py
--rw-r--r--   0        0        0     2231 2023-03-24 22:25:29.770322 muutils-0.3.6/muutils/misc.py
--rw-r--r--   0        0        0        0 2023-03-28 07:47:43.743882 muutils-0.3.6/muutils/py.typed
--rw-r--r--   0        0        0     8778 2023-03-24 22:25:29.771346 muutils-0.3.6/muutils/statcounter.py
--rw-r--r--   0        0        0     6322 2023-03-30 07:34:00.609964 muutils-0.3.6/muutils/sysinfo.py
--rw-r--r--   0        0        0    10013 2023-04-02 02:41:11.904089 muutils-0.3.6/muutils/tensor_utils.py
--rw-r--r--   0        0        0      139 2023-03-24 22:25:29.773320 muutils-0.3.6/muutils/zanj/__init__.py
--rw-r--r--   0        0        0     1469 2023-03-25 05:30:53.722117 muutils-0.3.6/muutils/zanj/externals.py
--rw-r--r--   0        0        0    11113 2023-03-30 19:44:39.207720 muutils-0.3.6/muutils/zanj/loading.py
--rw-r--r--   0        0        0     4151 2023-03-30 19:44:39.207720 muutils-0.3.6/muutils/zanj/readme.md
--rw-r--r--   0        0        0     8121 2023-03-30 19:44:39.208721 muutils-0.3.6/muutils/zanj/serializing.py
--rw-r--r--   0        0        0     8034 2023-04-04 06:14:55.118638 muutils-0.3.6/muutils/zanj/torchutil.py
--rw-r--r--   0        0        0     7520 2023-04-04 06:14:55.119640 muutils-0.3.6/muutils/zanj/zanj.py
--rw-r--r--   0        0        0      967 2023-04-05 21:47:49.280968 muutils-0.3.6/pyproject.toml
--rw-r--r--   0        0        0     1575 2023-02-16 09:10:54.612163 muutils-0.3.6/README.md
--rw-r--r--   0        0        0     2405 1970-01-01 00:00:00.000000 muutils-0.3.6/PKG-INFO
+-rw-r--r--   0        0        0    35823 2021-01-10 20:54:08.928022 muutils-0.3.7/LICENSE
+-rw-r--r--   0        0        0       22 2023-04-06 20:16:17.214645 muutils-0.3.7/muutils/__init__.py
+-rw-r--r--   0        0        0     3910 2023-03-24 22:25:29.757321 muutils-0.3.7/muutils/_wip/dataclass_validator.py
+-rw-r--r--   0        0        0     4652 2023-02-16 09:10:54.613167 muutils-0.3.7/muutils/_wip/experiments.ipynb
+-rw-r--r--   0        0        0     5835 2023-03-24 22:25:29.757321 muutils-0.3.7/muutils/_wip/gptdataset.py
+-rw-r--r--   0        0        0    23453 2023-03-24 22:25:29.758323 muutils-0.3.7/muutils/_wip/json_serialize_old.py
+-rw-r--r--   0        0        0     3286 2023-03-24 22:25:29.758323 muutils-0.3.7/muutils/_wip/lazy_externals.py
+-rw-r--r--   0        0        0     9214 2023-03-24 22:25:29.759320 muutils-0.3.7/muutils/_wip/newargparser.py
+-rw-r--r--   0        0        0     7414 2023-03-24 22:25:29.760323 muutils-0.3.7/muutils/_wip/torch_util_old.py
+-rw-r--r--   0        0        0     2037 2023-04-05 21:49:57.934337 muutils-0.3.7/muutils/dictmagic.py
+-rw-r--r--   0        0        0     1613 2023-03-06 19:25:21.018548 muutils-0.3.7/muutils/group_equiv.py
+-rw-r--r--   0        0        0      897 2023-03-24 22:25:29.761326 muutils-0.3.7/muutils/json_serialize/__init__.py
+-rw-r--r--   0        0        0     6016 2023-03-30 19:44:39.204722 muutils-0.3.7/muutils/json_serialize/array.py
+-rw-r--r--   0        0        0    13391 2023-03-24 22:25:29.762321 muutils-0.3.7/muutils/json_serialize/dataclass_factories.py
+-rw-r--r--   0        0        0     8906 2023-04-05 06:39:57.784877 muutils-0.3.7/muutils/json_serialize/json_serialize.py
+-rw-r--r--   0        0        0    15588 2023-04-05 21:47:49.279906 muutils-0.3.7/muutils/json_serialize/serializable_dataclass.py
+-rw-r--r--   0        0        0     3764 2023-03-28 07:47:43.743882 muutils-0.3.7/muutils/json_serialize/util.py
+-rw-r--r--   0        0        0     1878 2023-03-24 22:25:29.764321 muutils-0.3.7/muutils/jsonlines.py
+-rw-r--r--   0        0        0      267 2023-03-06 19:25:21.021547 muutils-0.3.7/muutils/logger/__init__.py
+-rw-r--r--   0        0        0     1183 2023-03-06 19:25:21.021547 muutils-0.3.7/muutils/logger/exception_context.py
+-rw-r--r--   0        0        0     1667 2023-03-24 22:25:29.765321 muutils-0.3.7/muutils/logger/headerfuncs.py
+-rw-r--r--   0        0        0     2072 2023-03-24 22:25:29.765321 muutils-0.3.7/muutils/logger/log_util.py
+-rw-r--r--   0        0        0    10669 2023-03-24 22:25:29.766326 muutils-0.3.7/muutils/logger/logger.py
+-rw-r--r--   0        0        0     3796 2023-03-24 22:25:29.767323 muutils-0.3.7/muutils/logger/loggingstream.py
+-rw-r--r--   0        0        0     2124 2023-03-24 22:25:29.768323 muutils-0.3.7/muutils/logger/simplelogger.py
+-rw-r--r--   0        0        0     2488 2023-03-24 22:25:29.769322 muutils-0.3.7/muutils/logger/timing.py
+-rw-r--r--   0        0        0     2231 2023-03-24 22:25:29.770322 muutils-0.3.7/muutils/misc.py
+-rw-r--r--   0        0        0        0 2023-03-28 07:47:43.743882 muutils-0.3.7/muutils/py.typed
+-rw-r--r--   0        0        0     8778 2023-03-24 22:25:29.771346 muutils-0.3.7/muutils/statcounter.py
+-rw-r--r--   0        0        0     6322 2023-03-30 07:34:00.609964 muutils-0.3.7/muutils/sysinfo.py
+-rw-r--r--   0        0        0    10013 2023-04-02 02:41:11.904089 muutils-0.3.7/muutils/tensor_utils.py
+-rw-r--r--   0        0        0      139 2023-03-24 22:25:29.773320 muutils-0.3.7/muutils/zanj/__init__.py
+-rw-r--r--   0        0        0     1469 2023-03-25 05:30:53.722117 muutils-0.3.7/muutils/zanj/externals.py
+-rw-r--r--   0        0        0    11113 2023-03-30 19:44:39.207720 muutils-0.3.7/muutils/zanj/loading.py
+-rw-r--r--   0        0        0     4151 2023-03-30 19:44:39.207720 muutils-0.3.7/muutils/zanj/readme.md
+-rw-r--r--   0        0        0     8121 2023-03-30 19:44:39.208721 muutils-0.3.7/muutils/zanj/serializing.py
+-rw-r--r--   0        0        0     8681 2023-04-06 20:15:44.284139 muutils-0.3.7/muutils/zanj/torchutil.py
+-rw-r--r--   0        0        0     7520 2023-04-04 06:14:55.119640 muutils-0.3.7/muutils/zanj/zanj.py
+-rw-r--r--   0        0        0      967 2023-04-06 20:16:08.561376 muutils-0.3.7/pyproject.toml
+-rw-r--r--   0        0        0     1575 2023-02-16 09:10:54.612163 muutils-0.3.7/README.md
+-rw-r--r--   0        0        0     2405 1970-01-01 00:00:00.000000 muutils-0.3.7/PKG-INFO
```

### Comparing `muutils-0.3.6/LICENSE` & `muutils-0.3.7/LICENSE`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/_wip/dataclass_validator.py` & `muutils-0.3.7/muutils/_wip/dataclass_validator.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/_wip/experiments.ipynb` & `muutils-0.3.7/muutils/_wip/experiments.ipynb`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/_wip/gptdataset.py` & `muutils-0.3.7/muutils/_wip/gptdataset.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/_wip/json_serialize_old.py` & `muutils-0.3.7/muutils/_wip/json_serialize_old.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/_wip/lazy_externals.py` & `muutils-0.3.7/muutils/_wip/lazy_externals.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/_wip/newargparser.py` & `muutils-0.3.7/muutils/_wip/newargparser.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/_wip/torch_util_old.py` & `muutils-0.3.7/muutils/_wip/torch_util_old.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/dictmagic.py` & `muutils-0.3.7/muutils/dictmagic.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/group_equiv.py` & `muutils-0.3.7/muutils/group_equiv.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/json_serialize/__init__.py` & `muutils-0.3.7/muutils/json_serialize/__init__.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/json_serialize/array.py` & `muutils-0.3.7/muutils/json_serialize/array.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/json_serialize/dataclass_factories.py` & `muutils-0.3.7/muutils/json_serialize/dataclass_factories.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/json_serialize/json_serialize.py` & `muutils-0.3.7/muutils/json_serialize/json_serialize.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/json_serialize/serializable_dataclass.py` & `muutils-0.3.7/muutils/json_serialize/serializable_dataclass.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/json_serialize/util.py` & `muutils-0.3.7/muutils/json_serialize/util.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/jsonlines.py` & `muutils-0.3.7/muutils/jsonlines.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/logger/exception_context.py` & `muutils-0.3.7/muutils/logger/exception_context.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/logger/headerfuncs.py` & `muutils-0.3.7/muutils/logger/headerfuncs.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/logger/log_util.py` & `muutils-0.3.7/muutils/logger/log_util.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/logger/logger.py` & `muutils-0.3.7/muutils/logger/logger.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/logger/loggingstream.py` & `muutils-0.3.7/muutils/logger/loggingstream.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/logger/simplelogger.py` & `muutils-0.3.7/muutils/logger/simplelogger.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/logger/timing.py` & `muutils-0.3.7/muutils/logger/timing.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/misc.py` & `muutils-0.3.7/muutils/misc.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/statcounter.py` & `muutils-0.3.7/muutils/statcounter.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/sysinfo.py` & `muutils-0.3.7/muutils/sysinfo.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/tensor_utils.py` & `muutils-0.3.7/muutils/tensor_utils.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/zanj/externals.py` & `muutils-0.3.7/muutils/zanj/externals.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/zanj/loading.py` & `muutils-0.3.7/muutils/zanj/loading.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/zanj/readme.md` & `muutils-0.3.7/muutils/zanj/readme.md`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/zanj/serializing.py` & `muutils-0.3.7/muutils/zanj/serializing.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/muutils/zanj/torchutil.py` & `muutils-0.3.7/muutils/zanj/torchutil.py`

 * *Files 6% similar despite different names*

```diff
@@ -187,26 +187,45 @@
 
         # return the new class
         return cls
 
     return wrapper
 
 
+class ConfigMismatchException(ValueError):
+    def __init__(self, msg: str, diff):
+        super().__init__(msg)
+        self.diff = diff
+
+    def __str__(self):
+        return f"{super().__str__()}: {self.diff}"
+
+
 def assert_model_cfg_equality(model_a: ConfiguredModel, model_b: ConfiguredModel):
-    """check both models are correct instances and have the same config"""
-    assert isinstance(model_a, ConfiguredModel)
-    assert isinstance(model_a.zanj_model_config, SerializableDataclass)
-    assert isinstance(model_b, ConfiguredModel)
-    assert isinstance(model_b.zanj_model_config, SerializableDataclass)
+    """check both models are correct instances and have the same config
+
+    Raises:
+        ConfigMismatchException: if the configs don't match, e.diff will contain the diff
+    """
+    assert isinstance(model_a, ConfiguredModel), "model_a must be a ConfiguredModel"
+    assert isinstance(
+        model_a.zanj_model_config, SerializableDataclass
+    ), "model_a must have a zanj_model_config"
+    assert isinstance(model_b, ConfiguredModel), "model_b must be a ConfiguredModel"
+    assert isinstance(
+        model_b.zanj_model_config, SerializableDataclass
+    ), "model_b must have a zanj_model_config"
 
     cls_type: type = type(model_a.zanj_model_config)
 
-    assert (
-        model_a.zanj_model_config == model_b.zanj_model_config
-    ), f"configs don't match: {cls_type.diff(model_a.zanj_model_config, model_b.zanj_model_config)}"
+    if not (model_a.zanj_model_config == model_b.zanj_model_config):
+        raise ConfigMismatchException(
+            f"configs of type {type(model_a.zanj_model_config)}, {type(model_b.zanj_model_config)} don't match",
+            diff=cls_type.diff(model_a.zanj_model_config, model_b.zanj_model_config),
+        )
 
 
 def assert_model_exact_equality(model_a: ConfiguredModel, model_b: ConfiguredModel):
     """check the models are exactly equal, including state dict contents"""
     assert_model_cfg_equality(model_a, model_b)
 
     model_a_sd_keys: set[str] = set(model_a.state_dict().keys())
```

### Comparing `muutils-0.3.6/muutils/zanj/zanj.py` & `muutils-0.3.7/muutils/zanj/zanj.py`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/pyproject.toml` & `muutils-0.3.7/pyproject.toml`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "muutils"
-version = "0.3.6"
+version = "0.3.7"
 description = "A collection of miscellaneous python utilities"
 license = "GPL-3.0-only"
 authors = ["mivanit <mivanits@umich.edu>"]
 readme = "README.md"
 classifiers=[
     "Programming Language :: Python :: 3",
     "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
```

### Comparing `muutils-0.3.6/README.md` & `muutils-0.3.7/README.md`

 * *Files identical despite different names*

### Comparing `muutils-0.3.6/PKG-INFO` & `muutils-0.3.7/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: muutils
-Version: 0.3.6
+Version: 0.3.7
 Summary: A collection of miscellaneous python utilities
 Home-page: https://github.com/mivanit/muutils
 License: GPL-3.0-only
 Author: mivanit
 Author-email: mivanits@umich.edu
 Requires-Python: >=3.10,<4.0
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
```

