# Comparing `tmp/mashumaro-3.5.tar.gz` & `tmp/mashumaro-3.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mashumaro-3.5.tar", last modified: Mon Feb 13 10:27:17 2023, max compression
+gzip compressed data, was "mashumaro-3.6.tar", last modified: Fri Apr  7 09:26:58 2023, max compression
```

## Comparing `mashumaro-3.5.tar` & `mashumaro-3.6.tar`

### file list

```diff
@@ -1,48 +1,55 @@
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-13 10:27:17.795111 mashumaro-3.5/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    11348 2023-02-06 08:24:36.000000 mashumaro-3.5/LICENSE
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    67134 2023-02-13 10:27:17.794881 mashumaro-3.5/PKG-INFO
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    66213 2023-02-13 10:27:04.000000 mashumaro-3.5/README.md
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-13 10:27:17.790754 mashumaro-3.5/mashumaro/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      258 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/__init__.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1415 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/config.py
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-13 10:27:17.792010 mashumaro-3.5/mashumaro/core/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/core/__init__.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1013 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/core/const.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      747 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/core/helpers.py
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-13 10:27:17.792587 mashumaro-3.5/mashumaro/core/meta/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/core/meta/__init__.py
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-13 10:27:17.793007 mashumaro-3.5/mashumaro/core/meta/code/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/core/meta/code/__init__.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    37292 2023-02-13 10:27:04.000000 mashumaro-3.5/mashumaro/core/meta/code/builder.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      707 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/core/meta/code/lines.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    20883 2023-02-13 10:27:04.000000 mashumaro-3.5/mashumaro/core/meta/helpers.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1366 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/core/meta/mixin.py
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-13 10:27:17.793535 mashumaro-3.5/mashumaro/core/meta/types/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/core/meta/types/__init__.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     4109 2023-02-13 10:27:04.000000 mashumaro-3.5/mashumaro/core/meta/types/common.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    25319 2023-02-13 10:27:04.000000 mashumaro-3.5/mashumaro/core/meta/types/pack.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    32058 2023-02-13 10:27:04.000000 mashumaro-3.5/mashumaro/core/meta/types/unpack.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      469 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/dialect.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     4548 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/exceptions.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1392 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/helper.py
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-13 10:27:17.794627 mashumaro-3.5/mashumaro/mixins/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/mixins/__init__.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1673 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/mixins/dict.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      790 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/mixins/json.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1558 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/mixins/msgpack.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1731 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/mixins/orjson.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1000 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/mixins/orjson.pyi
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1392 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/mixins/toml.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1108 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/mixins/yaml.py
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-06 08:24:36.000000 mashumaro-3.5/mashumaro/py.typed
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     2249 2023-02-13 10:27:04.000000 mashumaro-3.5/mashumaro/types.py
-drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-13 10:27:17.791685 mashumaro-3.5/mashumaro.egg-info/
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    67134 2023-02-13 10:27:17.000000 mashumaro-3.5/mashumaro.egg-info/PKG-INFO
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1014 2023-02-13 10:27:17.000000 mashumaro-3.5/mashumaro.egg-info/SOURCES.txt
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        1 2023-02-13 10:27:17.000000 mashumaro-3.5/mashumaro.egg-info/dependency_links.txt
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        1 2023-02-06 08:27:56.000000 mashumaro-3.5/mashumaro.egg-info/not-zip-safe
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      155 2023-02-13 10:27:17.000000 mashumaro-3.5/mashumaro.egg-info/requires.txt
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)       10 2023-02-13 10:27:17.000000 mashumaro-3.5/mashumaro.egg-info/top_level.txt
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      619 2023-02-06 08:24:36.000000 mashumaro-3.5/pyproject.toml
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)       38 2023-02-13 10:27:17.795146 mashumaro-3.5/setup.cfg
--rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1465 2023-02-13 10:27:04.000000 mashumaro-3.5/setup.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 09:26:58.308766 mashumaro-3.6/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    11348 2023-02-06 08:24:36.000000 mashumaro-3.6/LICENSE
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    78282 2023-04-07 09:26:58.308555 mashumaro-3.6/PKG-INFO
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    77363 2023-04-07 09:26:24.000000 mashumaro-3.6/README.md
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 09:26:58.302925 mashumaro-3.6/mashumaro/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      258 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/__init__.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1452 2023-04-07 09:26:24.000000 mashumaro-3.6/mashumaro/config.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 09:26:58.304251 mashumaro-3.6/mashumaro/core/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/core/__init__.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1013 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/core/const.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      825 2023-04-07 09:26:24.000000 mashumaro-3.6/mashumaro/core/helpers.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 09:26:58.304928 mashumaro-3.6/mashumaro/core/meta/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/core/meta/__init__.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 09:26:58.305865 mashumaro-3.6/mashumaro/core/meta/code/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/core/meta/code/__init__.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    37597 2023-04-07 09:26:24.000000 mashumaro-3.6/mashumaro/core/meta/code/builder.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      707 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/core/meta/code/lines.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    20883 2023-02-13 10:27:04.000000 mashumaro-3.6/mashumaro/core/meta/helpers.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1366 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/core/meta/mixin.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 09:26:58.306424 mashumaro-3.6/mashumaro/core/meta/types/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/core/meta/types/__init__.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     4109 2023-02-13 10:27:04.000000 mashumaro-3.6/mashumaro/core/meta/types/common.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    25319 2023-02-13 10:27:04.000000 mashumaro-3.6/mashumaro/core/meta/types/pack.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    32058 2023-02-13 10:27:04.000000 mashumaro-3.6/mashumaro/core/meta/types/unpack.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      469 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/dialect.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     4548 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/exceptions.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1392 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/helper.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 09:26:58.307237 mashumaro-3.6/mashumaro/jsonschema/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      214 2023-04-07 09:26:24.000000 mashumaro-3.6/mashumaro/jsonschema/__init__.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     2170 2023-04-07 09:26:24.000000 mashumaro-3.6/mashumaro/jsonschema/annotations.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     2353 2023-04-07 09:26:24.000000 mashumaro-3.6/mashumaro/jsonschema/builder.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      746 2023-04-07 09:26:24.000000 mashumaro-3.6/mashumaro/jsonschema/dialects.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     5781 2023-04-07 09:26:24.000000 mashumaro-3.6/mashumaro/jsonschema/models.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    25664 2023-04-07 09:26:24.000000 mashumaro-3.6/mashumaro/jsonschema/schema.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 09:26:58.308268 mashumaro-3.6/mashumaro/mixins/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/mixins/__init__.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1673 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/mixins/dict.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      790 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/mixins/json.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1558 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/mixins/msgpack.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1731 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/mixins/orjson.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1000 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/mixins/orjson.pyi
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1392 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/mixins/toml.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1108 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/mixins/yaml.py
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        0 2023-02-06 08:24:36.000000 mashumaro-3.6/mashumaro/py.typed
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     2249 2023-02-13 10:27:04.000000 mashumaro-3.6/mashumaro/types.py
+drwxr-xr-x   0 alexander.tikhonov   (503) staff       (20)        0 2023-04-07 09:26:58.303925 mashumaro-3.6/mashumaro.egg-info/
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)    78282 2023-04-07 09:26:58.000000 mashumaro-3.6/mashumaro.egg-info/PKG-INFO
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1210 2023-04-07 09:26:58.000000 mashumaro-3.6/mashumaro.egg-info/SOURCES.txt
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        1 2023-04-07 09:26:58.000000 mashumaro-3.6/mashumaro.egg-info/dependency_links.txt
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)        1 2023-02-06 08:27:56.000000 mashumaro-3.6/mashumaro.egg-info/not-zip-safe
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      155 2023-04-07 09:26:58.000000 mashumaro-3.6/mashumaro.egg-info/requires.txt
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)       10 2023-04-07 09:26:58.000000 mashumaro-3.6/mashumaro.egg-info/top_level.txt
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)      689 2023-04-07 09:26:24.000000 mashumaro-3.6/pyproject.toml
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)       38 2023-04-07 09:26:58.308804 mashumaro-3.6/setup.cfg
+-rw-r--r--   0 alexander.tikhonov   (503) staff       (20)     1463 2023-04-07 09:26:24.000000 mashumaro-3.6/setup.py
```

### Comparing `mashumaro-3.5/LICENSE` & `mashumaro-3.6/LICENSE`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/PKG-INFO` & `mashumaro-3.6/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: mashumaro
-Version: 3.5
-Summary: Fast serialization framework on top of dataclasses
+Version: 3.6
+Summary: Fast serialization library on top of dataclasses
 Home-page: https://github.com/Fatal1ty/mashumaro
 Author: Alexander Tikhonov
 Author-email: random.gauss@gmail.com
 License: Apache License, Version 2.0
 Platform: all
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Intended Audience :: Developers
@@ -20,29 +20,36 @@
 Description-Content-Type: text/markdown
 Provides-Extra: orjson
 Provides-Extra: msgpack
 Provides-Extra: yaml
 Provides-Extra: toml
 License-File: LICENSE
 
-# mashumaro (マシュマロ)
+# mashumaro
 
-> **mashumaro** is a fast and well tested serialization framework on top of dataclasses.
+###### Fast and well tested serialization library on top of dataclasses
 
 [![Build Status](https://github.com/Fatal1ty/mashumaro/workflows/tests/badge.svg)](https://github.com/Fatal1ty/mashumaro/actions)
 [![Coverage Status](https://coveralls.io/repos/github/Fatal1ty/mashumaro/badge.svg?branch=master)](https://coveralls.io/github/Fatal1ty/mashumaro?branch=master)
 [![Latest Version](https://img.shields.io/pypi/v/mashumaro.svg)](https://pypi.python.org/pypi/mashumaro)
 [![Python Version](https://img.shields.io/pypi/pyversions/mashumaro.svg)](https://pypi.python.org/pypi/mashumaro)
 [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
 
-
-When using dataclasses, you often need to dump and load objects according to
-the described scheme.
-This framework not only adds this ability to serialize in different formats,
-but also makes **serialization rapidly**.
+When using dataclasses, you often need to dump and load objects based on the
+schema you have. Mashumaro not only lets you save and load things in different
+ways, but it also does it _super quick_.
+
+**Key features**
+* 🚀 One of the fastest libraries
+* ☝️ Mature and time-tested
+* 👶 Easy to use out of the box
+* ⚙️ Highly customizable
+* 🎉 Built-in support for JSON, YAML, MessagePack, TOML
+* 📦 Built-in support for almost all Python types including typing-extensions
+* 📝 JSON Schema generation
 
 Table of contents
 --------------------------------------------------------------------------------
 * [Installation](#installation)
 * [Changelog](#changelog)
 * [Supported serialization formats](#supported-serialization-formats)
 * [Supported data types](#supported-data-types)
@@ -93,14 +100,19 @@
       * [Generic dataclass in a field type](#generic-dataclass-in-a-field-type)
     * [`GenericSerializableType` interface](#genericserializabletype-interface)
     * [Serialization hooks](#serialization-hooks)
         * [Before deserialization](#before-deserialization)
         * [After deserialization](#after-deserialization)
         * [Before serialization](#before-serialization)
         * [After serialization](#after-serialization)
+* [JSON Schema](#json-schema)
+    * [Building JSON Schema](#building-json-schema)
+    * [JSON Schema constraints](#json-schema-constraints)
+    * [Extending JSON Schema](#extending-json-schema)
+    * [JSON Schema and custom serialization methods](#json-schema-and-custom-serialization-methods)
 
 Installation
 --------------------------------------------------------------------------------
 
 Use pip to install:
 ```shell
 $ pip install mashumaro
@@ -114,15 +126,15 @@
 
 This project follows the principles of [Semantic Versioning](https://semver.org).
 Changelog is available on [GitHub Releases page](https://github.com/Fatal1ty/mashumaro/releases).
 
 Supported serialization formats
 --------------------------------------------------------------------------------
 
-This framework adds methods for dumping to and loading from the
+This library adds methods for dumping to and loading from the
 following formats:
 
 * [plain dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
 * [JSON](https://www.json.org)
 * [YAML](https://yaml.org)
 * [MessagePack](https://msgpack.org)
 * [TOML](https://toml.io)
@@ -288,15 +300,15 @@
 json_string = my_portfolio.to_json()
 Portfolio.from_json(json_string)  # same as my_portfolio
 ```
 
 How does it work?
 --------------------------------------------------------------------------------
 
-This framework works by taking the schema of the data and generating a
+This library works by taking the schema of the data and generating a
 specific parser and builder for exactly that schema, taking into account the
 specifics of the serialization format. This is much faster than inspection of
 field types on every call of parsing or building at runtime.
 
 These specific parsers and builders are presented by the corresponding
 `from_*` and `to_*` methods. They are compiled during import time (or at
 runtime in some cases) and are set as attributes to your dataclasses.
@@ -315,15 +327,15 @@
 <img src="https://raw.githubusercontent.com/Fatal1ty/mashumaro/master/benchmark/charts/load.png" width="400"><img src="https://raw.githubusercontent.com/Fatal1ty/mashumaro/master/benchmark/charts/dump.png" width="400">
 
 <table>
   <col>
   <colgroup span="2"></colgroup>
   <colgroup span="2"></colgroup>
   <tr>
-    <th rowspan="2">Framework</th>
+    <th rowspan="2">Library</th>
     <th colspan="2" scope="colgroup">From dict</th>
     <th colspan="2" scope="colgroup">To dict</th>
 </tr>
 <tr>
     <th scope="col">Time</th>
     <th scope="col">Slowdown factor</th>
     <th scope="col">Time</th>
@@ -519,14 +531,15 @@
 * Turn an existing regular or generic class into a serializable one
 by inheriting the [`SerializableType`](#serializabletype-interface) class
 * Write different serialization strategies for an existing regular or generic type that is not under your control
 using [`SerializationStrategy`](#serializationstrategy) class
 * Define serialization / deserialization methods:
   * for a specific dataclass field by using [field options](#field-options)
   * for a specific data type used in the dataclass by using [`Config`](#config-options) class
+* Alter input and output data with serialization / deserialization [hooks](#serialization-hooks)
 * Separate serialization scheme from a dataclass in a reusable manner using [dialects](#dialects)
 * Choose from predefined serialization engines for the specific data types, e.g. `datetime` and `NamedTuple`
 
 ### SerializableType interface
 
 If you have a custom class or hierarchy of classes whose instances you want
 to serialize with `mashumaro`, the first option is to implement
@@ -785,15 +798,15 @@
 #### Third-party generic types
 
 To create a generic version of a serialization strategy you need to follow these steps:
 * inherit [`Generic[...]`](https://docs.python.org/3/library/typing.html#typing.Generic) type
 with the number of parameters matching the number of parameters
 of the target generic type
 * Write generic annotations for `serialize` method's return type and for `deserialize` method's argument type
-* Use the origin type of the target generic type in the [`serialization_strategy`](#serializationstrategy-config-option) config section
+* Use the origin type of the target generic type in the [`serialization_strategy`](#serialization_strategy-config-option) config section
 ([`typing.get_origin`](https://docs.python.org/3/library/typing.html#typing.get_origin) might be helpful)
 
 There is no need to add `use_annotations=True` here because it's enabled implicitly
 for generic serialization strategies.
 
 For example, there is a third-party [multidict](https://pypi.org/project/multidict/) package that has a generic `MultiDict` type.
 A generic serialization strategy for it might look like this:
@@ -1770,7 +1783,440 @@
         d.pop('password')
         return d
 
 obj = DataClass(user="name", password="secret")
 print(obj.to_dict())  # {"user": "name"}
 print(obj.to_json())  # '{"user": "name"}'
 ```
+
+JSON Schema
+--------------------------------------------------------------------------------
+
+You can build JSON Schema not only for dataclasses but also for any other
+[supported](#supported-data-types) data
+types. There is support for the following standards:
+* [Draft 2022-12](https://json-schema.org/specification.html)
+* [OpenAPI Specification 3.1.0](https://swagger.io/specification/)
+
+### Building JSON Schema
+
+For simple one-time cases it's recommended to start from using a configurable
+`build_json_schema` function. It returns `JSONSchema` object that can be
+serialized to json or to dict:
+
+```python
+from dataclasses import dataclass
+from typing import List
+from uuid import UUID
+
+from mashumaro.jsonschema import build_json_schema
+
+
+@dataclass
+class User:
+    id: UUID
+    name: str
+
+
+print(build_json_schema(List[User]).to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "items": {
+        "type": "object",
+        "title": "User",
+        "properties": {
+            "id": {
+                "type": "string",
+                "format": "uuid"
+            },
+            "name": {
+                "type": "string"
+            }
+        },
+        "additionalProperties": false,
+        "required": [
+            "id",
+            "name"
+        ]
+    }
+}
+```
+</details>
+
+Additional validation keywords ([see below](#json-schema-constraints))
+can be added using annotations:
+
+```python
+from typing import Annotated, List
+from mashumaro.jsonschema import build_json_schema
+from mashumaro.jsonschema.annotations import Maximum, MaxItems
+
+print(
+    build_json_schema(
+        Annotated[
+            List[Annotated[int, Maximum(42)]],
+            MaxItems(4)
+        ]
+    ).to_json()
+)
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "items": {
+        "type": "integer",
+        "maximum": 42
+    },
+    "maxItems": 4
+}
+```
+</details>
+
+The [`$schema`](https://json-schema.org/draft/2020-12/json-schema-core.html#name-the-schema-keyword)
+keyword can be added by setting `with_dialect_uri` to True:
+
+```python
+print(build_json_schema(str, with_dialect_uri=True).to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "$schema": "https://json-schema.org/draft/2020-12/schema",
+    "type": "string"
+}
+```
+</details>
+
+By default, Draft 2022-12 dialect is being used, but you can change it to
+another one by setting `dialect` parameter:
+
+```python
+from mashumaro.jsonschema import OPEN_API_3_1
+
+print(
+    build_json_schema(
+        str, dialect=OPEN_API_3_1, with_dialect_uri=True
+    ).to_json()
+)
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "$schema": "https://spec.openapis.org/oas/3.1/dialect/base",
+    "type": "string"
+}
+```
+</details>
+
+All dataclass JSON Schemas can or can not be placed in the
+[definitions](https://json-schema.org/draft/2020-12/json-schema-core.html#name-schema-re-use-with-defs)
+section, depending on the `all_refs` parameter, which default value comes
+from a dialect used (`False` for Draft 2022-12, `True` for OpenAPI
+Specification 3.1.0):
+
+```python
+print(build_json_schema(List[User], all_refs=True).to_json())
+```
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "$defs": {
+        "User": {
+            "type": "object",
+            "title": "User",
+            "properties": {
+                "id": {
+                    "type": "string",
+                    "format": "uuid"
+                },
+                "name": {
+                    "type": "string"
+                }
+            },
+            "additionalProperties": false,
+            "required": [
+                "id",
+                "name"
+            ]
+        }
+    },
+    "items": {
+        "$ref": "#/defs/User"
+    }
+}
+```
+</details>
+
+The definitions section can be omitted from the final document by setting
+`with_definitions` parameter to `False`:
+
+```python
+print(
+    build_json_schema(
+        List[User], dialect=OPEN_API_3_1, with_definitions=False
+    ).to_json()
+)
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "items": {
+        "$ref": "#/components/schemas/User"
+    }
+}
+```
+</details>
+
+These omitted definitions could be found later in the `Context` object that
+you could have created and passed to the function, but it could be easier
+to use `JSONSchemaBuilder` for that. For example, you might found it handy
+to build OpenAPI Specification step by step passing your models to the builder
+and get all the registered definitions later. This builder has reasonable
+defaults but can be customized if necessary.
+
+```python
+from mashumaro.jsonschema import JSONSchemaBuilder, OPEN_API_3_1
+
+builder = JSONSchemaBuilder(OPEN_API_3_1)
+
+@dataclass
+class User:
+    id: UUID
+    name: str
+
+@dataclass
+class Device:
+    id: UUID
+    model: str
+
+print(builder.build(List[User]).to_json())
+print(builder.build(List[Device]).to_json())
+print(builder.get_definitions().to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "items": {
+        "$ref": "#/components/schemas/User"
+    }
+}
+```
+```json
+{
+    "type": "array",
+    "items": {
+        "$ref": "#/components/schemas/Device"
+    }
+}
+```
+```json
+{
+    "User": {
+        "type": "object",
+        "title": "User",
+        "properties": {
+            "id": {
+                "type": "string",
+                "format": "uuid"
+            },
+            "name": {
+                "type": "string"
+            }
+        },
+        "additionalProperties": false,
+        "required": [
+            "id",
+            "name"
+        ]
+    },
+    "Device": {
+        "type": "object",
+        "title": "Device",
+        "properties": {
+            "id": {
+                "type": "string",
+                "format": "uuid"
+            },
+            "model": {
+                "type": "string"
+            }
+        },
+        "additionalProperties": false,
+        "required": [
+            "id",
+            "model"
+        ]
+    }
+}
+```
+</details>
+
+### JSON Schema constraints
+
+Apart from required keywords, that are added automatically for certain data
+types, you're free to use additional validation keywords.
+They're presented by the corresponding classes in
+[`mashumaro.jsonschema.annotations`](https://github.com/Fatal1ty/mashumaro/blob/master/mashumaro/jsonschema/annotations.py):
+
+Number constraints:
+* [`Minimum`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-minimum)
+* [`Maximum`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maximum)
+* [`ExclusiveMinimum`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-exclusiveminimum)
+* [`ExclusiveMaximum`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-exclusivemaximum)
+* [`MultipleOf`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-multipleof)
+
+String constraints:
+* [`MinLength`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-minlength)
+* [`MaxLength`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maxlength)
+* [`Pattern`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-pattern)
+
+Array constraints:
+* [`MinItems`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-minitems)
+* [`MaxItems`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maxitems)
+* [`UniqueItems`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-uniqueitems)
+* [`Contains`](https://json-schema.org/draft/2020-12/json-schema-core.html#name-contains)
+* [`MinContains`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-mincontains)
+* [`MaxContains`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maxcontains)
+
+Object constraints:
+* [`MaxProperties`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maxproperties)
+* [`MinProperties`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-minproperties)
+* [`DependentRequired`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-dependentrequired)
+
+### Extending JSON Schema
+
+Using a `Config` class it is possible to override some parts of the schema.
+Currently, it works for dataclass fields via "properties" key:
+
+```python
+from dataclasses import dataclass
+from mashumaro.jsonschema import build_json_schema
+
+@dataclass
+class FooBar:
+    foo: str
+    bar: int
+
+    class Config:
+        json_schema = {
+            "properties": {
+                "foo": {
+                    "type": "string",
+                    "description": "bar"
+                }
+            }
+        }
+
+print(build_json_schema(FooBar).to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "object",
+    "title": "FooBar",
+    "properties": {
+        "foo": {
+            "type": "string",
+            "description": "bar"
+        },
+        "bar": {
+            "type": "integer"
+        }
+    },
+    "additionalProperties": false,
+    "required": [
+        "foo",
+        "bar"
+    ]
+}
+```
+</details>
+
+### JSON Schema and custom serialization methods
+
+Mashumaro provides different ways to override default serialization methods for
+dataclass fields or specific data types. In order for these overrides to be
+reflected in the schema, you need to make sure that the methods have
+annotations of the return value type.
+
+```python
+from dataclasses import dataclass, field
+from mashumaro.config import BaseConfig
+from mashumaro.jsonschema import build_json_schema
+
+def str_as_list(s: str) -> list[str]:
+    return list(s)
+
+def int_as_str(i: int) -> str:
+    return str(i)
+
+@dataclass
+class FooBar:
+    foo: str = field(metadata={"serialize": str_as_list})
+    bar: int
+
+    class Config(BaseConfig):
+        serialization_strategy = {
+            int: {
+                "serialize": int_as_str
+            }
+        }
+
+print(build_json_schema(FooBar).to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "object",
+    "title": "FooBar",
+    "properties": {
+        "foo": {
+            "type": "array",
+            "items": {
+                "type": "string"
+            }
+        },
+        "bar": {
+            "type": "string"
+        }
+    },
+    "additionalProperties": false,
+    "required": [
+        "foo",
+        "bar"
+    ]
+}
+```
+</details>
```

### Comparing `mashumaro-3.5/README.md` & `mashumaro-3.6/README.md`

 * *Files 8% similar despite different names*

```diff
@@ -1,22 +1,29 @@
-# mashumaro (マシュマロ)
+# mashumaro
 
-> **mashumaro** is a fast and well tested serialization framework on top of dataclasses.
+###### Fast and well tested serialization library on top of dataclasses
 
 [![Build Status](https://github.com/Fatal1ty/mashumaro/workflows/tests/badge.svg)](https://github.com/Fatal1ty/mashumaro/actions)
 [![Coverage Status](https://coveralls.io/repos/github/Fatal1ty/mashumaro/badge.svg?branch=master)](https://coveralls.io/github/Fatal1ty/mashumaro?branch=master)
 [![Latest Version](https://img.shields.io/pypi/v/mashumaro.svg)](https://pypi.python.org/pypi/mashumaro)
 [![Python Version](https://img.shields.io/pypi/pyversions/mashumaro.svg)](https://pypi.python.org/pypi/mashumaro)
 [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
 
-
-When using dataclasses, you often need to dump and load objects according to
-the described scheme.
-This framework not only adds this ability to serialize in different formats,
-but also makes **serialization rapidly**.
+When using dataclasses, you often need to dump and load objects based on the
+schema you have. Mashumaro not only lets you save and load things in different
+ways, but it also does it _super quick_.
+
+**Key features**
+* 🚀 One of the fastest libraries
+* ☝️ Mature and time-tested
+* 👶 Easy to use out of the box
+* ⚙️ Highly customizable
+* 🎉 Built-in support for JSON, YAML, MessagePack, TOML
+* 📦 Built-in support for almost all Python types including typing-extensions
+* 📝 JSON Schema generation
 
 Table of contents
 --------------------------------------------------------------------------------
 * [Installation](#installation)
 * [Changelog](#changelog)
 * [Supported serialization formats](#supported-serialization-formats)
 * [Supported data types](#supported-data-types)
@@ -67,14 +74,19 @@
       * [Generic dataclass in a field type](#generic-dataclass-in-a-field-type)
     * [`GenericSerializableType` interface](#genericserializabletype-interface)
     * [Serialization hooks](#serialization-hooks)
         * [Before deserialization](#before-deserialization)
         * [After deserialization](#after-deserialization)
         * [Before serialization](#before-serialization)
         * [After serialization](#after-serialization)
+* [JSON Schema](#json-schema)
+    * [Building JSON Schema](#building-json-schema)
+    * [JSON Schema constraints](#json-schema-constraints)
+    * [Extending JSON Schema](#extending-json-schema)
+    * [JSON Schema and custom serialization methods](#json-schema-and-custom-serialization-methods)
 
 Installation
 --------------------------------------------------------------------------------
 
 Use pip to install:
 ```shell
 $ pip install mashumaro
@@ -88,15 +100,15 @@
 
 This project follows the principles of [Semantic Versioning](https://semver.org).
 Changelog is available on [GitHub Releases page](https://github.com/Fatal1ty/mashumaro/releases).
 
 Supported serialization formats
 --------------------------------------------------------------------------------
 
-This framework adds methods for dumping to and loading from the
+This library adds methods for dumping to and loading from the
 following formats:
 
 * [plain dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
 * [JSON](https://www.json.org)
 * [YAML](https://yaml.org)
 * [MessagePack](https://msgpack.org)
 * [TOML](https://toml.io)
@@ -262,15 +274,15 @@
 json_string = my_portfolio.to_json()
 Portfolio.from_json(json_string)  # same as my_portfolio
 ```
 
 How does it work?
 --------------------------------------------------------------------------------
 
-This framework works by taking the schema of the data and generating a
+This library works by taking the schema of the data and generating a
 specific parser and builder for exactly that schema, taking into account the
 specifics of the serialization format. This is much faster than inspection of
 field types on every call of parsing or building at runtime.
 
 These specific parsers and builders are presented by the corresponding
 `from_*` and `to_*` methods. They are compiled during import time (or at
 runtime in some cases) and are set as attributes to your dataclasses.
@@ -289,15 +301,15 @@
 <img src="https://raw.githubusercontent.com/Fatal1ty/mashumaro/master/benchmark/charts/load.png" width="400"><img src="https://raw.githubusercontent.com/Fatal1ty/mashumaro/master/benchmark/charts/dump.png" width="400">
 
 <table>
   <col>
   <colgroup span="2"></colgroup>
   <colgroup span="2"></colgroup>
   <tr>
-    <th rowspan="2">Framework</th>
+    <th rowspan="2">Library</th>
     <th colspan="2" scope="colgroup">From dict</th>
     <th colspan="2" scope="colgroup">To dict</th>
 </tr>
 <tr>
     <th scope="col">Time</th>
     <th scope="col">Slowdown factor</th>
     <th scope="col">Time</th>
@@ -493,14 +505,15 @@
 * Turn an existing regular or generic class into a serializable one
 by inheriting the [`SerializableType`](#serializabletype-interface) class
 * Write different serialization strategies for an existing regular or generic type that is not under your control
 using [`SerializationStrategy`](#serializationstrategy) class
 * Define serialization / deserialization methods:
   * for a specific dataclass field by using [field options](#field-options)
   * for a specific data type used in the dataclass by using [`Config`](#config-options) class
+* Alter input and output data with serialization / deserialization [hooks](#serialization-hooks)
 * Separate serialization scheme from a dataclass in a reusable manner using [dialects](#dialects)
 * Choose from predefined serialization engines for the specific data types, e.g. `datetime` and `NamedTuple`
 
 ### SerializableType interface
 
 If you have a custom class or hierarchy of classes whose instances you want
 to serialize with `mashumaro`, the first option is to implement
@@ -759,15 +772,15 @@
 #### Third-party generic types
 
 To create a generic version of a serialization strategy you need to follow these steps:
 * inherit [`Generic[...]`](https://docs.python.org/3/library/typing.html#typing.Generic) type
 with the number of parameters matching the number of parameters
 of the target generic type
 * Write generic annotations for `serialize` method's return type and for `deserialize` method's argument type
-* Use the origin type of the target generic type in the [`serialization_strategy`](#serializationstrategy-config-option) config section
+* Use the origin type of the target generic type in the [`serialization_strategy`](#serialization_strategy-config-option) config section
 ([`typing.get_origin`](https://docs.python.org/3/library/typing.html#typing.get_origin) might be helpful)
 
 There is no need to add `use_annotations=True` here because it's enabled implicitly
 for generic serialization strategies.
 
 For example, there is a third-party [multidict](https://pypi.org/project/multidict/) package that has a generic `MultiDict` type.
 A generic serialization strategy for it might look like this:
@@ -1744,7 +1757,440 @@
         d.pop('password')
         return d
 
 obj = DataClass(user="name", password="secret")
 print(obj.to_dict())  # {"user": "name"}
 print(obj.to_json())  # '{"user": "name"}'
 ```
+
+JSON Schema
+--------------------------------------------------------------------------------
+
+You can build JSON Schema not only for dataclasses but also for any other
+[supported](#supported-data-types) data
+types. There is support for the following standards:
+* [Draft 2022-12](https://json-schema.org/specification.html)
+* [OpenAPI Specification 3.1.0](https://swagger.io/specification/)
+
+### Building JSON Schema
+
+For simple one-time cases it's recommended to start from using a configurable
+`build_json_schema` function. It returns `JSONSchema` object that can be
+serialized to json or to dict:
+
+```python
+from dataclasses import dataclass
+from typing import List
+from uuid import UUID
+
+from mashumaro.jsonschema import build_json_schema
+
+
+@dataclass
+class User:
+    id: UUID
+    name: str
+
+
+print(build_json_schema(List[User]).to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "items": {
+        "type": "object",
+        "title": "User",
+        "properties": {
+            "id": {
+                "type": "string",
+                "format": "uuid"
+            },
+            "name": {
+                "type": "string"
+            }
+        },
+        "additionalProperties": false,
+        "required": [
+            "id",
+            "name"
+        ]
+    }
+}
+```
+</details>
+
+Additional validation keywords ([see below](#json-schema-constraints))
+can be added using annotations:
+
+```python
+from typing import Annotated, List
+from mashumaro.jsonschema import build_json_schema
+from mashumaro.jsonschema.annotations import Maximum, MaxItems
+
+print(
+    build_json_schema(
+        Annotated[
+            List[Annotated[int, Maximum(42)]],
+            MaxItems(4)
+        ]
+    ).to_json()
+)
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "items": {
+        "type": "integer",
+        "maximum": 42
+    },
+    "maxItems": 4
+}
+```
+</details>
+
+The [`$schema`](https://json-schema.org/draft/2020-12/json-schema-core.html#name-the-schema-keyword)
+keyword can be added by setting `with_dialect_uri` to True:
+
+```python
+print(build_json_schema(str, with_dialect_uri=True).to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "$schema": "https://json-schema.org/draft/2020-12/schema",
+    "type": "string"
+}
+```
+</details>
+
+By default, Draft 2022-12 dialect is being used, but you can change it to
+another one by setting `dialect` parameter:
+
+```python
+from mashumaro.jsonschema import OPEN_API_3_1
+
+print(
+    build_json_schema(
+        str, dialect=OPEN_API_3_1, with_dialect_uri=True
+    ).to_json()
+)
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "$schema": "https://spec.openapis.org/oas/3.1/dialect/base",
+    "type": "string"
+}
+```
+</details>
+
+All dataclass JSON Schemas can or can not be placed in the
+[definitions](https://json-schema.org/draft/2020-12/json-schema-core.html#name-schema-re-use-with-defs)
+section, depending on the `all_refs` parameter, which default value comes
+from a dialect used (`False` for Draft 2022-12, `True` for OpenAPI
+Specification 3.1.0):
+
+```python
+print(build_json_schema(List[User], all_refs=True).to_json())
+```
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "$defs": {
+        "User": {
+            "type": "object",
+            "title": "User",
+            "properties": {
+                "id": {
+                    "type": "string",
+                    "format": "uuid"
+                },
+                "name": {
+                    "type": "string"
+                }
+            },
+            "additionalProperties": false,
+            "required": [
+                "id",
+                "name"
+            ]
+        }
+    },
+    "items": {
+        "$ref": "#/defs/User"
+    }
+}
+```
+</details>
+
+The definitions section can be omitted from the final document by setting
+`with_definitions` parameter to `False`:
+
+```python
+print(
+    build_json_schema(
+        List[User], dialect=OPEN_API_3_1, with_definitions=False
+    ).to_json()
+)
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "items": {
+        "$ref": "#/components/schemas/User"
+    }
+}
+```
+</details>
+
+These omitted definitions could be found later in the `Context` object that
+you could have created and passed to the function, but it could be easier
+to use `JSONSchemaBuilder` for that. For example, you might found it handy
+to build OpenAPI Specification step by step passing your models to the builder
+and get all the registered definitions later. This builder has reasonable
+defaults but can be customized if necessary.
+
+```python
+from mashumaro.jsonschema import JSONSchemaBuilder, OPEN_API_3_1
+
+builder = JSONSchemaBuilder(OPEN_API_3_1)
+
+@dataclass
+class User:
+    id: UUID
+    name: str
+
+@dataclass
+class Device:
+    id: UUID
+    model: str
+
+print(builder.build(List[User]).to_json())
+print(builder.build(List[Device]).to_json())
+print(builder.get_definitions().to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "items": {
+        "$ref": "#/components/schemas/User"
+    }
+}
+```
+```json
+{
+    "type": "array",
+    "items": {
+        "$ref": "#/components/schemas/Device"
+    }
+}
+```
+```json
+{
+    "User": {
+        "type": "object",
+        "title": "User",
+        "properties": {
+            "id": {
+                "type": "string",
+                "format": "uuid"
+            },
+            "name": {
+                "type": "string"
+            }
+        },
+        "additionalProperties": false,
+        "required": [
+            "id",
+            "name"
+        ]
+    },
+    "Device": {
+        "type": "object",
+        "title": "Device",
+        "properties": {
+            "id": {
+                "type": "string",
+                "format": "uuid"
+            },
+            "model": {
+                "type": "string"
+            }
+        },
+        "additionalProperties": false,
+        "required": [
+            "id",
+            "model"
+        ]
+    }
+}
+```
+</details>
+
+### JSON Schema constraints
+
+Apart from required keywords, that are added automatically for certain data
+types, you're free to use additional validation keywords.
+They're presented by the corresponding classes in
+[`mashumaro.jsonschema.annotations`](https://github.com/Fatal1ty/mashumaro/blob/master/mashumaro/jsonschema/annotations.py):
+
+Number constraints:
+* [`Minimum`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-minimum)
+* [`Maximum`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maximum)
+* [`ExclusiveMinimum`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-exclusiveminimum)
+* [`ExclusiveMaximum`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-exclusivemaximum)
+* [`MultipleOf`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-multipleof)
+
+String constraints:
+* [`MinLength`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-minlength)
+* [`MaxLength`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maxlength)
+* [`Pattern`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-pattern)
+
+Array constraints:
+* [`MinItems`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-minitems)
+* [`MaxItems`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maxitems)
+* [`UniqueItems`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-uniqueitems)
+* [`Contains`](https://json-schema.org/draft/2020-12/json-schema-core.html#name-contains)
+* [`MinContains`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-mincontains)
+* [`MaxContains`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maxcontains)
+
+Object constraints:
+* [`MaxProperties`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maxproperties)
+* [`MinProperties`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-minproperties)
+* [`DependentRequired`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-dependentrequired)
+
+### Extending JSON Schema
+
+Using a `Config` class it is possible to override some parts of the schema.
+Currently, it works for dataclass fields via "properties" key:
+
+```python
+from dataclasses import dataclass
+from mashumaro.jsonschema import build_json_schema
+
+@dataclass
+class FooBar:
+    foo: str
+    bar: int
+
+    class Config:
+        json_schema = {
+            "properties": {
+                "foo": {
+                    "type": "string",
+                    "description": "bar"
+                }
+            }
+        }
+
+print(build_json_schema(FooBar).to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "object",
+    "title": "FooBar",
+    "properties": {
+        "foo": {
+            "type": "string",
+            "description": "bar"
+        },
+        "bar": {
+            "type": "integer"
+        }
+    },
+    "additionalProperties": false,
+    "required": [
+        "foo",
+        "bar"
+    ]
+}
+```
+</details>
+
+### JSON Schema and custom serialization methods
+
+Mashumaro provides different ways to override default serialization methods for
+dataclass fields or specific data types. In order for these overrides to be
+reflected in the schema, you need to make sure that the methods have
+annotations of the return value type.
+
+```python
+from dataclasses import dataclass, field
+from mashumaro.config import BaseConfig
+from mashumaro.jsonschema import build_json_schema
+
+def str_as_list(s: str) -> list[str]:
+    return list(s)
+
+def int_as_str(i: int) -> str:
+    return str(i)
+
+@dataclass
+class FooBar:
+    foo: str = field(metadata={"serialize": str_as_list})
+    bar: int
+
+    class Config(BaseConfig):
+        serialization_strategy = {
+            int: {
+                "serialize": int_as_str
+            }
+        }
+
+print(build_json_schema(FooBar).to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "object",
+    "title": "FooBar",
+    "properties": {
+        "foo": {
+            "type": "array",
+            "items": {
+                "type": "string"
+            }
+        },
+        "bar": {
+            "type": "string"
+        }
+    },
+    "additionalProperties": false,
+    "required": [
+        "foo",
+        "bar"
+    ]
+}
+```
+</details>
```

### Comparing `mashumaro-3.5/mashumaro/config.py` & `mashumaro-3.6/mashumaro/config.py`

 * *Files 9% similar despite different names*

```diff
@@ -43,7 +43,8 @@
     aliases: Dict[str, str] = {}
     serialize_by_alias: bool = False
     namedtuple_as_dict: bool = False
     allow_postponed_evaluation: bool = True
     dialect: Optional[Type[Dialect]] = None
     omit_none: Union[bool, Literal[Sentinel.MISSING]] = Sentinel.MISSING
     orjson_options: Optional[int] = 0
+    json_schema: Dict[str, Any] = {}
```

### Comparing `mashumaro-3.5/mashumaro/core/const.py` & `mashumaro-3.6/mashumaro/core/const.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/core/helpers.py` & `mashumaro-3.6/mashumaro/core/helpers.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,19 +1,23 @@
 import datetime
 import re
 
 __all__ = [
     "parse_timezone",
     "ConfigValue",
+    "UTC_OFFSET_PATTERN",
 ]
 
 
+UTC_OFFSET_PATTERN = r"^UTC(([+-][0-2][0-9]):([0-5][0-9]))?$"
+UTC_OFFSET_RE = re.compile(UTC_OFFSET_PATTERN)
+
+
 def parse_timezone(s: str) -> datetime.timezone:
-    regexp = re.compile(r"^UTC(([+-][0-2][0-9]):([0-5][0-9]))?$")
-    match = regexp.match(s)
+    match = UTC_OFFSET_RE.match(s)
     if not match:
         raise ValueError(
             f"Time zone {s} must be either UTC " f"or in format UTC[+-]hh:mm"
         )
     if match.group(1):
         hours = int(match.group(2))
         minutes = int(match.group(3))
```

### Comparing `mashumaro-3.5/mashumaro/core/meta/code/builder.py` & `mashumaro-3.6/mashumaro/core/meta/code/builder.py`

 * *Files 0% similar despite different names*

```diff
@@ -4,14 +4,16 @@
 import typing
 from contextlib import contextmanager
 
 # noinspection PyProtectedMember
 from dataclasses import _FIELDS, MISSING, Field, is_dataclass  # type: ignore
 from functools import lru_cache
 
+import typing_extensions
+
 from mashumaro.config import (
     ADD_DIALECT_SUPPORT,
     TO_DICT_ADD_BY_ALIAS_FLAG,
     TO_DICT_ADD_OMIT_NONE_FLAG,
     BaseConfig,
     SerializationStrategyValueType,
 )
@@ -107,19 +109,21 @@
         return self.cls.__dict__
 
     @property
     def annotations(self) -> typing.Dict[str, typing.Any]:
         return self.namespace.get("__annotations__", {})
 
     def __get_field_types(
-        self, recursive: bool = True
+        self, recursive: bool = True, include_extras: bool = False
     ) -> typing.Dict[str, typing.Any]:
         fields = {}
         try:
-            field_type_hints = typing.get_type_hints(self.cls)
+            field_type_hints = typing_extensions.get_type_hints(
+                self.cls, include_extras=include_extras
+            )
         except NameError as e:
             name = get_name_error_name(e)
             raise UnresolvedTypeReferenceError(self.cls, name) from None
         for fname, ftype in field_type_hints.items():
             if is_class_var(ftype) or is_init_var(ftype):
                 continue
             if recursive or fname in self.annotations:
@@ -146,14 +150,19 @@
         cls = self._get_field_class(field_name)
         return self.resolved_type_params[cls]
 
     @property
     def field_types(self) -> typing.Dict[str, typing.Any]:
         return self.__get_field_types()
 
+    def get_field_types(
+        self, include_extras: bool = False
+    ) -> typing.Dict[str, typing.Any]:
+        return self.__get_field_types(include_extras=include_extras)
+
     @property  # type: ignore
     @lru_cache()
     def dataclass_fields(self) -> typing.Dict[str, Field]:
         d = {}
         for ancestor in self.cls.__mro__[-1:0:-1]:
             if is_dataclass(ancestor):
                 for field in getattr(ancestor, _FIELDS).values():
```

### Comparing `mashumaro-3.5/mashumaro/core/meta/code/lines.py` & `mashumaro-3.6/mashumaro/core/meta/code/lines.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/core/meta/helpers.py` & `mashumaro-3.6/mashumaro/core/meta/helpers.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/core/meta/mixin.py` & `mashumaro-3.6/mashumaro/core/meta/mixin.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/core/meta/types/common.py` & `mashumaro-3.6/mashumaro/core/meta/types/common.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/core/meta/types/pack.py` & `mashumaro-3.6/mashumaro/core/meta/types/pack.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/core/meta/types/unpack.py` & `mashumaro-3.6/mashumaro/core/meta/types/unpack.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/exceptions.py` & `mashumaro-3.6/mashumaro/exceptions.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/helper.py` & `mashumaro-3.6/mashumaro/helper.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/mixins/dict.py` & `mashumaro-3.6/mashumaro/mixins/dict.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/mixins/json.py` & `mashumaro-3.6/mashumaro/mixins/json.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/mixins/msgpack.py` & `mashumaro-3.6/mashumaro/mixins/msgpack.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/mixins/orjson.py` & `mashumaro-3.6/mashumaro/mixins/orjson.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/mixins/orjson.pyi` & `mashumaro-3.6/mashumaro/mixins/orjson.pyi`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/mixins/toml.py` & `mashumaro-3.6/mashumaro/mixins/toml.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/mixins/yaml.py` & `mashumaro-3.6/mashumaro/mixins/yaml.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro/types.py` & `mashumaro-3.6/mashumaro/types.py`

 * *Files identical despite different names*

### Comparing `mashumaro-3.5/mashumaro.egg-info/PKG-INFO` & `mashumaro-3.6/mashumaro.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: mashumaro
-Version: 3.5
-Summary: Fast serialization framework on top of dataclasses
+Version: 3.6
+Summary: Fast serialization library on top of dataclasses
 Home-page: https://github.com/Fatal1ty/mashumaro
 Author: Alexander Tikhonov
 Author-email: random.gauss@gmail.com
 License: Apache License, Version 2.0
 Platform: all
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Intended Audience :: Developers
@@ -20,29 +20,36 @@
 Description-Content-Type: text/markdown
 Provides-Extra: orjson
 Provides-Extra: msgpack
 Provides-Extra: yaml
 Provides-Extra: toml
 License-File: LICENSE
 
-# mashumaro (マシュマロ)
+# mashumaro
 
-> **mashumaro** is a fast and well tested serialization framework on top of dataclasses.
+###### Fast and well tested serialization library on top of dataclasses
 
 [![Build Status](https://github.com/Fatal1ty/mashumaro/workflows/tests/badge.svg)](https://github.com/Fatal1ty/mashumaro/actions)
 [![Coverage Status](https://coveralls.io/repos/github/Fatal1ty/mashumaro/badge.svg?branch=master)](https://coveralls.io/github/Fatal1ty/mashumaro?branch=master)
 [![Latest Version](https://img.shields.io/pypi/v/mashumaro.svg)](https://pypi.python.org/pypi/mashumaro)
 [![Python Version](https://img.shields.io/pypi/pyversions/mashumaro.svg)](https://pypi.python.org/pypi/mashumaro)
 [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
 
-
-When using dataclasses, you often need to dump and load objects according to
-the described scheme.
-This framework not only adds this ability to serialize in different formats,
-but also makes **serialization rapidly**.
+When using dataclasses, you often need to dump and load objects based on the
+schema you have. Mashumaro not only lets you save and load things in different
+ways, but it also does it _super quick_.
+
+**Key features**
+* 🚀 One of the fastest libraries
+* ☝️ Mature and time-tested
+* 👶 Easy to use out of the box
+* ⚙️ Highly customizable
+* 🎉 Built-in support for JSON, YAML, MessagePack, TOML
+* 📦 Built-in support for almost all Python types including typing-extensions
+* 📝 JSON Schema generation
 
 Table of contents
 --------------------------------------------------------------------------------
 * [Installation](#installation)
 * [Changelog](#changelog)
 * [Supported serialization formats](#supported-serialization-formats)
 * [Supported data types](#supported-data-types)
@@ -93,14 +100,19 @@
       * [Generic dataclass in a field type](#generic-dataclass-in-a-field-type)
     * [`GenericSerializableType` interface](#genericserializabletype-interface)
     * [Serialization hooks](#serialization-hooks)
         * [Before deserialization](#before-deserialization)
         * [After deserialization](#after-deserialization)
         * [Before serialization](#before-serialization)
         * [After serialization](#after-serialization)
+* [JSON Schema](#json-schema)
+    * [Building JSON Schema](#building-json-schema)
+    * [JSON Schema constraints](#json-schema-constraints)
+    * [Extending JSON Schema](#extending-json-schema)
+    * [JSON Schema and custom serialization methods](#json-schema-and-custom-serialization-methods)
 
 Installation
 --------------------------------------------------------------------------------
 
 Use pip to install:
 ```shell
 $ pip install mashumaro
@@ -114,15 +126,15 @@
 
 This project follows the principles of [Semantic Versioning](https://semver.org).
 Changelog is available on [GitHub Releases page](https://github.com/Fatal1ty/mashumaro/releases).
 
 Supported serialization formats
 --------------------------------------------------------------------------------
 
-This framework adds methods for dumping to and loading from the
+This library adds methods for dumping to and loading from the
 following formats:
 
 * [plain dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
 * [JSON](https://www.json.org)
 * [YAML](https://yaml.org)
 * [MessagePack](https://msgpack.org)
 * [TOML](https://toml.io)
@@ -288,15 +300,15 @@
 json_string = my_portfolio.to_json()
 Portfolio.from_json(json_string)  # same as my_portfolio
 ```
 
 How does it work?
 --------------------------------------------------------------------------------
 
-This framework works by taking the schema of the data and generating a
+This library works by taking the schema of the data and generating a
 specific parser and builder for exactly that schema, taking into account the
 specifics of the serialization format. This is much faster than inspection of
 field types on every call of parsing or building at runtime.
 
 These specific parsers and builders are presented by the corresponding
 `from_*` and `to_*` methods. They are compiled during import time (or at
 runtime in some cases) and are set as attributes to your dataclasses.
@@ -315,15 +327,15 @@
 <img src="https://raw.githubusercontent.com/Fatal1ty/mashumaro/master/benchmark/charts/load.png" width="400"><img src="https://raw.githubusercontent.com/Fatal1ty/mashumaro/master/benchmark/charts/dump.png" width="400">
 
 <table>
   <col>
   <colgroup span="2"></colgroup>
   <colgroup span="2"></colgroup>
   <tr>
-    <th rowspan="2">Framework</th>
+    <th rowspan="2">Library</th>
     <th colspan="2" scope="colgroup">From dict</th>
     <th colspan="2" scope="colgroup">To dict</th>
 </tr>
 <tr>
     <th scope="col">Time</th>
     <th scope="col">Slowdown factor</th>
     <th scope="col">Time</th>
@@ -519,14 +531,15 @@
 * Turn an existing regular or generic class into a serializable one
 by inheriting the [`SerializableType`](#serializabletype-interface) class
 * Write different serialization strategies for an existing regular or generic type that is not under your control
 using [`SerializationStrategy`](#serializationstrategy) class
 * Define serialization / deserialization methods:
   * for a specific dataclass field by using [field options](#field-options)
   * for a specific data type used in the dataclass by using [`Config`](#config-options) class
+* Alter input and output data with serialization / deserialization [hooks](#serialization-hooks)
 * Separate serialization scheme from a dataclass in a reusable manner using [dialects](#dialects)
 * Choose from predefined serialization engines for the specific data types, e.g. `datetime` and `NamedTuple`
 
 ### SerializableType interface
 
 If you have a custom class or hierarchy of classes whose instances you want
 to serialize with `mashumaro`, the first option is to implement
@@ -785,15 +798,15 @@
 #### Third-party generic types
 
 To create a generic version of a serialization strategy you need to follow these steps:
 * inherit [`Generic[...]`](https://docs.python.org/3/library/typing.html#typing.Generic) type
 with the number of parameters matching the number of parameters
 of the target generic type
 * Write generic annotations for `serialize` method's return type and for `deserialize` method's argument type
-* Use the origin type of the target generic type in the [`serialization_strategy`](#serializationstrategy-config-option) config section
+* Use the origin type of the target generic type in the [`serialization_strategy`](#serialization_strategy-config-option) config section
 ([`typing.get_origin`](https://docs.python.org/3/library/typing.html#typing.get_origin) might be helpful)
 
 There is no need to add `use_annotations=True` here because it's enabled implicitly
 for generic serialization strategies.
 
 For example, there is a third-party [multidict](https://pypi.org/project/multidict/) package that has a generic `MultiDict` type.
 A generic serialization strategy for it might look like this:
@@ -1770,7 +1783,440 @@
         d.pop('password')
         return d
 
 obj = DataClass(user="name", password="secret")
 print(obj.to_dict())  # {"user": "name"}
 print(obj.to_json())  # '{"user": "name"}'
 ```
+
+JSON Schema
+--------------------------------------------------------------------------------
+
+You can build JSON Schema not only for dataclasses but also for any other
+[supported](#supported-data-types) data
+types. There is support for the following standards:
+* [Draft 2022-12](https://json-schema.org/specification.html)
+* [OpenAPI Specification 3.1.0](https://swagger.io/specification/)
+
+### Building JSON Schema
+
+For simple one-time cases it's recommended to start from using a configurable
+`build_json_schema` function. It returns `JSONSchema` object that can be
+serialized to json or to dict:
+
+```python
+from dataclasses import dataclass
+from typing import List
+from uuid import UUID
+
+from mashumaro.jsonschema import build_json_schema
+
+
+@dataclass
+class User:
+    id: UUID
+    name: str
+
+
+print(build_json_schema(List[User]).to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "items": {
+        "type": "object",
+        "title": "User",
+        "properties": {
+            "id": {
+                "type": "string",
+                "format": "uuid"
+            },
+            "name": {
+                "type": "string"
+            }
+        },
+        "additionalProperties": false,
+        "required": [
+            "id",
+            "name"
+        ]
+    }
+}
+```
+</details>
+
+Additional validation keywords ([see below](#json-schema-constraints))
+can be added using annotations:
+
+```python
+from typing import Annotated, List
+from mashumaro.jsonschema import build_json_schema
+from mashumaro.jsonschema.annotations import Maximum, MaxItems
+
+print(
+    build_json_schema(
+        Annotated[
+            List[Annotated[int, Maximum(42)]],
+            MaxItems(4)
+        ]
+    ).to_json()
+)
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "items": {
+        "type": "integer",
+        "maximum": 42
+    },
+    "maxItems": 4
+}
+```
+</details>
+
+The [`$schema`](https://json-schema.org/draft/2020-12/json-schema-core.html#name-the-schema-keyword)
+keyword can be added by setting `with_dialect_uri` to True:
+
+```python
+print(build_json_schema(str, with_dialect_uri=True).to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "$schema": "https://json-schema.org/draft/2020-12/schema",
+    "type": "string"
+}
+```
+</details>
+
+By default, Draft 2022-12 dialect is being used, but you can change it to
+another one by setting `dialect` parameter:
+
+```python
+from mashumaro.jsonschema import OPEN_API_3_1
+
+print(
+    build_json_schema(
+        str, dialect=OPEN_API_3_1, with_dialect_uri=True
+    ).to_json()
+)
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "$schema": "https://spec.openapis.org/oas/3.1/dialect/base",
+    "type": "string"
+}
+```
+</details>
+
+All dataclass JSON Schemas can or can not be placed in the
+[definitions](https://json-schema.org/draft/2020-12/json-schema-core.html#name-schema-re-use-with-defs)
+section, depending on the `all_refs` parameter, which default value comes
+from a dialect used (`False` for Draft 2022-12, `True` for OpenAPI
+Specification 3.1.0):
+
+```python
+print(build_json_schema(List[User], all_refs=True).to_json())
+```
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "$defs": {
+        "User": {
+            "type": "object",
+            "title": "User",
+            "properties": {
+                "id": {
+                    "type": "string",
+                    "format": "uuid"
+                },
+                "name": {
+                    "type": "string"
+                }
+            },
+            "additionalProperties": false,
+            "required": [
+                "id",
+                "name"
+            ]
+        }
+    },
+    "items": {
+        "$ref": "#/defs/User"
+    }
+}
+```
+</details>
+
+The definitions section can be omitted from the final document by setting
+`with_definitions` parameter to `False`:
+
+```python
+print(
+    build_json_schema(
+        List[User], dialect=OPEN_API_3_1, with_definitions=False
+    ).to_json()
+)
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "items": {
+        "$ref": "#/components/schemas/User"
+    }
+}
+```
+</details>
+
+These omitted definitions could be found later in the `Context` object that
+you could have created and passed to the function, but it could be easier
+to use `JSONSchemaBuilder` for that. For example, you might found it handy
+to build OpenAPI Specification step by step passing your models to the builder
+and get all the registered definitions later. This builder has reasonable
+defaults but can be customized if necessary.
+
+```python
+from mashumaro.jsonschema import JSONSchemaBuilder, OPEN_API_3_1
+
+builder = JSONSchemaBuilder(OPEN_API_3_1)
+
+@dataclass
+class User:
+    id: UUID
+    name: str
+
+@dataclass
+class Device:
+    id: UUID
+    model: str
+
+print(builder.build(List[User]).to_json())
+print(builder.build(List[Device]).to_json())
+print(builder.get_definitions().to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "array",
+    "items": {
+        "$ref": "#/components/schemas/User"
+    }
+}
+```
+```json
+{
+    "type": "array",
+    "items": {
+        "$ref": "#/components/schemas/Device"
+    }
+}
+```
+```json
+{
+    "User": {
+        "type": "object",
+        "title": "User",
+        "properties": {
+            "id": {
+                "type": "string",
+                "format": "uuid"
+            },
+            "name": {
+                "type": "string"
+            }
+        },
+        "additionalProperties": false,
+        "required": [
+            "id",
+            "name"
+        ]
+    },
+    "Device": {
+        "type": "object",
+        "title": "Device",
+        "properties": {
+            "id": {
+                "type": "string",
+                "format": "uuid"
+            },
+            "model": {
+                "type": "string"
+            }
+        },
+        "additionalProperties": false,
+        "required": [
+            "id",
+            "model"
+        ]
+    }
+}
+```
+</details>
+
+### JSON Schema constraints
+
+Apart from required keywords, that are added automatically for certain data
+types, you're free to use additional validation keywords.
+They're presented by the corresponding classes in
+[`mashumaro.jsonschema.annotations`](https://github.com/Fatal1ty/mashumaro/blob/master/mashumaro/jsonschema/annotations.py):
+
+Number constraints:
+* [`Minimum`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-minimum)
+* [`Maximum`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maximum)
+* [`ExclusiveMinimum`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-exclusiveminimum)
+* [`ExclusiveMaximum`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-exclusivemaximum)
+* [`MultipleOf`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-multipleof)
+
+String constraints:
+* [`MinLength`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-minlength)
+* [`MaxLength`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maxlength)
+* [`Pattern`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-pattern)
+
+Array constraints:
+* [`MinItems`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-minitems)
+* [`MaxItems`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maxitems)
+* [`UniqueItems`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-uniqueitems)
+* [`Contains`](https://json-schema.org/draft/2020-12/json-schema-core.html#name-contains)
+* [`MinContains`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-mincontains)
+* [`MaxContains`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maxcontains)
+
+Object constraints:
+* [`MaxProperties`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-maxproperties)
+* [`MinProperties`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-minproperties)
+* [`DependentRequired`](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-dependentrequired)
+
+### Extending JSON Schema
+
+Using a `Config` class it is possible to override some parts of the schema.
+Currently, it works for dataclass fields via "properties" key:
+
+```python
+from dataclasses import dataclass
+from mashumaro.jsonschema import build_json_schema
+
+@dataclass
+class FooBar:
+    foo: str
+    bar: int
+
+    class Config:
+        json_schema = {
+            "properties": {
+                "foo": {
+                    "type": "string",
+                    "description": "bar"
+                }
+            }
+        }
+
+print(build_json_schema(FooBar).to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "object",
+    "title": "FooBar",
+    "properties": {
+        "foo": {
+            "type": "string",
+            "description": "bar"
+        },
+        "bar": {
+            "type": "integer"
+        }
+    },
+    "additionalProperties": false,
+    "required": [
+        "foo",
+        "bar"
+    ]
+}
+```
+</details>
+
+### JSON Schema and custom serialization methods
+
+Mashumaro provides different ways to override default serialization methods for
+dataclass fields or specific data types. In order for these overrides to be
+reflected in the schema, you need to make sure that the methods have
+annotations of the return value type.
+
+```python
+from dataclasses import dataclass, field
+from mashumaro.config import BaseConfig
+from mashumaro.jsonschema import build_json_schema
+
+def str_as_list(s: str) -> list[str]:
+    return list(s)
+
+def int_as_str(i: int) -> str:
+    return str(i)
+
+@dataclass
+class FooBar:
+    foo: str = field(metadata={"serialize": str_as_list})
+    bar: int
+
+    class Config(BaseConfig):
+        serialization_strategy = {
+            int: {
+                "serialize": int_as_str
+            }
+        }
+
+print(build_json_schema(FooBar).to_json())
+```
+
+<details>
+<summary>Click to show the result</summary>
+
+```json
+{
+    "type": "object",
+    "title": "FooBar",
+    "properties": {
+        "foo": {
+            "type": "array",
+            "items": {
+                "type": "string"
+            }
+        },
+        "bar": {
+            "type": "string"
+        }
+    },
+    "additionalProperties": false,
+    "required": [
+        "foo",
+        "bar"
+    ]
+}
+```
+</details>
```

### Comparing `mashumaro-3.5/pyproject.toml` & `mashumaro-3.6/pyproject.toml`

 * *Files 13% similar despite different names*

```diff
@@ -11,21 +11,24 @@
 ]
 disable_error_code = 'empty-body'
 
 [[tool.mypy.overrides]]
 module = [
     'mashumaro.core.meta.types.pack',
     'mashumaro.core.meta.types.unpack',
+    'mashumaro.jsonschema.schema',
 ]
 disable_error_code = 'return'
 
 [flake8]
 max-line-length = 79
 
 [tool.isort]
+profile = 'black'
+line_length = 79
 multi_line_output = 3
 include_trailing_comma = true
 ensure_newline_before_comments = true
 
 [tool.black]
 line-length = 79
 target-version = ['py37', 'py38', 'py39']
```

### Comparing `mashumaro-3.5/setup.py` & `mashumaro-3.6/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/usr/bin/env python
 
 from setuptools import find_packages, setup
 
 setup(
     name="mashumaro",
-    version="3.5",
-    description="Fast serialization framework on top of dataclasses",
+    version="3.6",
+    description="Fast serialization library on top of dataclasses",
     long_description=open("README.md", encoding="utf8").read(),
     long_description_content_type="text/markdown",
     platforms="all",
     classifiers=[
         "License :: OSI Approved :: Apache Software License",
         "Intended Audience :: Developers",
         "Programming Language :: Python :: 3 :: Only",
```

