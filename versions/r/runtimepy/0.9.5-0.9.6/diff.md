# Comparing `tmp/runtimepy-0.9.5.tar.gz` & `tmp/runtimepy-0.9.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "runtimepy-0.9.5.tar", last modified: Thu Dec 15 22:39:00 2022, max compression
+gzip compressed data, was "runtimepy-0.9.6.tar", last modified: Fri Jan 27 08:47:01 2023, max compression
```

## Comparing `runtimepy-0.9.5.tar` & `runtimepy-0.9.6.tar`

### file list

```diff
@@ -1,85 +1,86 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.928460 runtimepy-0.9.5/
--rw-r--r--   0 runner    (1001) docker     (123)     1071 2022-12-15 22:37:45.000000 runtimepy-0.9.5/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3094 2022-12-15 22:39:00.928460 runtimepy-0.9.5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2210 2022-12-15 22:37:45.000000 runtimepy-0.9.5/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     1140 2022-12-15 22:37:45.000000 runtimepy-0.9.5/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.924460 runtimepy-0.9.5/runtimepy/
--rw-r--r--   0 runner    (1001) docker     (123)      313 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      332 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)      893 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/app.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.924460 runtimepy-0.9.5/runtimepy/channel/
--rw-r--r--   0 runner    (1001) docker     (123)     2697 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/channel/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.924460 runtimepy-0.9.5/runtimepy/channel/environment/
--rw-r--r--   0 runner    (1001) docker     (123)      715 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/channel/environment/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3481 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/channel/environment/array.py
--rw-r--r--   0 runner    (1001) docker     (123)     6891 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/channel/environment/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3764 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/channel/environment/create.py
--rw-r--r--   0 runner    (1001) docker     (123)     6347 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/channel/environment/file.py
--rw-r--r--   0 runner    (1001) docker     (123)      530 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/channel/environment/names.py
--rw-r--r--   0 runner    (1001) docker     (123)     1582 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/channel/registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.924460 runtimepy-0.9.5/runtimepy/commands/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/commands/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      747 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/commands/all.py
--rw-r--r--   0 runner    (1001) docker     (123)     1679 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/commands/tui.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.920460 runtimepy-0.9.5/runtimepy/data/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.924460 runtimepy-0.9.5/runtimepy/data/schemas/
--rw-r--r--   0 runner    (1001) docker     (123)      835 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/data/schemas/BitFields.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      651 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/data/schemas/ChannelRegistry.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      483 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/data/schemas/EnumRegistry.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      100 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/dev_requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)     2010 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/entry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.924460 runtimepy-0.9.5/runtimepy/enum/
--rw-r--r--   0 runner    (1001) docker     (123)     4648 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/enum/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1105 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/enum/registry.py
--rw-r--r--   0 runner    (1001) docker     (123)     1027 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/enum/type.py
--rw-r--r--   0 runner    (1001) docker     (123)     4573 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/mapping.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.924460 runtimepy-0.9.5/runtimepy/mixins/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/mixins/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      719 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/mixins/enum.py
--rw-r--r--   0 runner    (1001) docker     (123)      660 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/mixins/regex.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.924460 runtimepy-0.9.5/runtimepy/net/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/net/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.928460 runtimepy-0.9.5/runtimepy/net/websocket/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/net/websocket/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4078 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/net/websocket/connection.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.928460 runtimepy-0.9.5/runtimepy/primitives/
--rw-r--r--   0 runner    (1001) docker     (123)     1725 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6793 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/array.py
--rw-r--r--   0 runner    (1001) docker     (123)     4955 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      803 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/bool.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.928460 runtimepy-0.9.5/runtimepy/primitives/field/
--rw-r--r--   0 runner    (1001) docker     (123)     3383 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/field/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6620 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/field/fields.py
--rw-r--r--   0 runner    (1001) docker     (123)     5807 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/field/manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     1219 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/float.py
--rw-r--r--   0 runner    (1001) docker     (123)     3055 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/int.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.928460 runtimepy-0.9.5/runtimepy/primitives/type/
--rw-r--r--   0 runner    (1001) docker     (123)     1510 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/type/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2878 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/type/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      508 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/type/bool.py
--rw-r--r--   0 runner    (1001) docker     (123)     1313 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/type/float.py
--rw-r--r--   0 runner    (1001) docker     (123)     3054 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/primitives/type/int.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.928460 runtimepy-0.9.5/runtimepy/registry/
--rw-r--r--   0 runner    (1001) docker     (123)     3135 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/registry/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      735 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/registry/bool.py
--rw-r--r--   0 runner    (1001) docker     (123)      815 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/registry/item.py
--rw-r--r--   0 runner    (1001) docker     (123)     1785 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/registry/name.py
--rw-r--r--   0 runner    (1001) docker     (123)       60 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      766 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/schemas.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.928460 runtimepy-0.9.5/runtimepy/task/
--rw-r--r--   0 runner    (1001) docker     (123)     5771 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/task/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.928460 runtimepy-0.9.5/runtimepy/tui/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/tui/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.928460 runtimepy-0.9.5/runtimepy/tui/channels/
--rw-r--r--   0 runner    (1001) docker     (123)     5321 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/tui/channels/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1102 2022-12-15 22:37:45.000000 runtimepy-0.9.5/runtimepy/tui/task.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-15 22:39:00.924460 runtimepy-0.9.5/runtimepy.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3094 2022-12-15 22:39:00.000000 runtimepy-0.9.5/runtimepy.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1888 2022-12-15 22:39:00.000000 runtimepy-0.9.5/runtimepy.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-15 22:39:00.000000 runtimepy-0.9.5/runtimepy.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       51 2022-12-15 22:39:00.000000 runtimepy-0.9.5/runtimepy.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      128 2022-12-15 22:39:00.000000 runtimepy-0.9.5/runtimepy.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2022-12-15 22:39:00.000000 runtimepy-0.9.5/runtimepy.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-15 22:39:00.928460 runtimepy-0.9.5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      829 2022-12-15 22:37:45.000000 runtimepy-0.9.5/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.978177 runtimepy-0.9.6/
+-rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-01-27 08:45:44.000000 runtimepy-0.9.6/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3094 2023-01-27 08:47:01.978177 runtimepy-0.9.6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2210 2023-01-27 08:45:44.000000 runtimepy-0.9.6/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1140 2023-01-27 08:45:44.000000 runtimepy-0.9.6/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.970177 runtimepy-0.9.6/runtimepy/
+-rw-r--r--   0 runner    (1001) docker     (123)      313 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      332 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      893 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/app.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.970177 runtimepy-0.9.6/runtimepy/channel/
+-rw-r--r--   0 runner    (1001) docker     (123)     2697 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/channel/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.970177 runtimepy-0.9.6/runtimepy/channel/environment/
+-rw-r--r--   0 runner    (1001) docker     (123)      715 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/channel/environment/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3481 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/channel/environment/array.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6891 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/channel/environment/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3764 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/channel/environment/create.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6347 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/channel/environment/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)      530 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/channel/environment/names.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1582 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/channel/registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/commands/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/commands/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      747 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/commands/all.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1679 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/commands/tui.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.966177 runtimepy-0.9.6/runtimepy/data/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/data/schemas/
+-rw-r--r--   0 runner    (1001) docker     (123)      835 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/data/schemas/BitFields.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      651 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/data/schemas/ChannelRegistry.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      483 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/data/schemas/EnumRegistry.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      100 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/dev_requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/entry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/enum/
+-rw-r--r--   0 runner    (1001) docker     (123)     4648 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/enum/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1105 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/enum/registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1027 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/enum/type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4573 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/mapping.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/mixins/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/mixins/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      719 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/mixins/enum.py
+-rw-r--r--   0 runner    (1001) docker     (123)      660 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/mixins/regex.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/net/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/net/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5282 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/net/connection.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/net/websocket/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/net/websocket/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2341 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/net/websocket/connection.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/primitives/
+-rw-r--r--   0 runner    (1001) docker     (123)     1725 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6793 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/array.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4955 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      803 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/bool.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/primitives/field/
+-rw-r--r--   0 runner    (1001) docker     (123)     3383 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/field/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6620 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/field/fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5807 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/field/manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1219 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/float.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3055 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/int.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/primitives/type/
+-rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/type/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2878 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/type/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      508 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/type/bool.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1313 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/type/float.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3054 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/primitives/type/int.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/registry/
+-rw-r--r--   0 runner    (1001) docker     (123)     3135 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/registry/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      735 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/registry/bool.py
+-rw-r--r--   0 runner    (1001) docker     (123)      815 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/registry/item.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1785 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/registry/name.py
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      766 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/schemas.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/task/
+-rw-r--r--   0 runner    (1001) docker     (123)     5771 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/task/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/tui/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/tui/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.974177 runtimepy-0.9.6/runtimepy/tui/channels/
+-rw-r--r--   0 runner    (1001) docker     (123)     5321 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/tui/channels/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1102 2023-01-27 08:45:44.000000 runtimepy-0.9.6/runtimepy/tui/task.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 08:47:01.970177 runtimepy-0.9.6/runtimepy.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3094 2023-01-27 08:47:01.000000 runtimepy-0.9.6/runtimepy.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1916 2023-01-27 08:47:01.000000 runtimepy-0.9.6/runtimepy.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-27 08:47:01.000000 runtimepy-0.9.6/runtimepy.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       51 2023-01-27 08:47:01.000000 runtimepy-0.9.6/runtimepy.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      128 2023-01-27 08:47:01.000000 runtimepy-0.9.6/runtimepy.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-01-27 08:47:01.000000 runtimepy-0.9.6/runtimepy.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-27 08:47:01.978177 runtimepy-0.9.6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      829 2023-01-27 08:45:44.000000 runtimepy-0.9.6/setup.py
```

### Comparing `runtimepy-0.9.5/LICENSE` & `runtimepy-0.9.6/LICENSE`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/PKG-INFO` & `runtimepy-0.9.6/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: runtimepy
-Version: 0.9.5
+Version: 0.9.6
 Summary: A framework for implementing Python services.
 Home-page: https://github.com/vkottler/runtimepy
 Author: Vaughn Kottler
 Author-email: Vaughn Kottler <vaughnkottler@gmail.com>
 Maintainer-email: Vaughn Kottler <vaughnkottler@gmail.com>
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
@@ -21,19 +21,19 @@
 Provides-Extra: test
 License-File: LICENSE
 
 <!--
     =====================================
     generator=datazen
     version=3.1.0
-    hash=11a246701195a0b0fd552c9c37e7a20e
+    hash=63d8f8a798339435b00a65b4455bb831
     =====================================
 -->
 
-# runtimepy ([0.9.5](https://pypi.org/project/runtimepy/))
+# runtimepy ([0.9.6](https://pypi.org/project/runtimepy/))
 
 [![python](https://img.shields.io/pypi/pyversions/runtimepy.svg)](https://pypi.org/project/runtimepy/)
 ![Build Status](https://github.com/vkottler/runtimepy/workflows/Python%20Package/badge.svg)
 [![codecov](https://codecov.io/gh/vkottler/runtimepy/branch/master/graphs/badge.svg?branch=master)](https://codecov.io/github/vkottler/runtimepy)
 ![PyPI - Status](https://img.shields.io/pypi/status/runtimepy)
 ![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/runtimepy)
 
@@ -60,15 +60,15 @@
 * `windows-latest`
 
 # Introduction
 
 # Command-line Options
 
 ```
-$ ./venv3.7/bin/runtimepy -h
+$ ./venv3.8/bin/runtimepy -h
 
 usage: runtimepy [-h] [--version] [-v] [-C DIR] {tui,noop} ...
 
 A framework for implementing Python services.
 
 optional arguments:
   -h, --help         show this help message and exit
```

### Comparing `runtimepy-0.9.5/README.md` & `runtimepy-0.9.6/runtimepy.egg-info/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,16 +1,39 @@
+Metadata-Version: 2.1
+Name: runtimepy
+Version: 0.9.6
+Summary: A framework for implementing Python services.
+Home-page: https://github.com/vkottler/runtimepy
+Author: Vaughn Kottler
+Author-email: Vaughn Kottler <vaughnkottler@gmail.com>
+Maintainer-email: Vaughn Kottler <vaughnkottler@gmail.com>
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Operating System :: Microsoft :: Windows
+Classifier: Operating System :: MacOS
+Classifier: Operating System :: POSIX :: Linux
+Classifier: Operating System :: Unix
+Classifier: Development Status :: 5 - Production/Stable
+Classifier: License :: OSI Approved :: MIT License
+Requires-Python: >=3.7
+Description-Content-Type: text/markdown
+Provides-Extra: test
+License-File: LICENSE
+
 <!--
     =====================================
     generator=datazen
     version=3.1.0
-    hash=11a246701195a0b0fd552c9c37e7a20e
+    hash=63d8f8a798339435b00a65b4455bb831
     =====================================
 -->
 
-# runtimepy ([0.9.5](https://pypi.org/project/runtimepy/))
+# runtimepy ([0.9.6](https://pypi.org/project/runtimepy/))
 
 [![python](https://img.shields.io/pypi/pyversions/runtimepy.svg)](https://pypi.org/project/runtimepy/)
 ![Build Status](https://github.com/vkottler/runtimepy/workflows/Python%20Package/badge.svg)
 [![codecov](https://codecov.io/gh/vkottler/runtimepy/branch/master/graphs/badge.svg?branch=master)](https://codecov.io/github/vkottler/runtimepy)
 ![PyPI - Status](https://img.shields.io/pypi/status/runtimepy)
 ![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/runtimepy)
 
@@ -37,15 +60,15 @@
 * `windows-latest`
 
 # Introduction
 
 # Command-line Options
 
 ```
-$ ./venv3.7/bin/runtimepy -h
+$ ./venv3.8/bin/runtimepy -h
 
 usage: runtimepy [-h] [--version] [-v] [-C DIR] {tui,noop} ...
 
 A framework for implementing Python services.
 
 optional arguments:
   -h, --help         show this help message and exit
```

### Comparing `runtimepy-0.9.5/pyproject.toml` & `runtimepy-0.9.6/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools-wrapper", "trove-classifiers"]
 build-backend = "setuptools.build_meta:__legacy__"
 
 [project]
 name = "runtimepy"
-version = "0.9.5"
+version = "0.9.6"
 description = "A framework for implementing Python services."
 readme = "README.md"
 requires-python = ">=3.7"
 authors = [
   {name = "Vaughn Kottler", email = "vaughnkottler@gmail.com"}
 ]
 maintainers = [
```

### Comparing `runtimepy-0.9.5/runtimepy/app.py` & `runtimepy-0.9.6/runtimepy/app.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/channel/__init__.py` & `runtimepy-0.9.6/runtimepy/channel/__init__.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/channel/environment/__init__.py` & `runtimepy-0.9.6/runtimepy/channel/environment/__init__.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/channel/environment/array.py` & `runtimepy-0.9.6/runtimepy/channel/environment/array.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/channel/environment/base.py` & `runtimepy-0.9.6/runtimepy/channel/environment/base.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/channel/environment/create.py` & `runtimepy-0.9.6/runtimepy/channel/environment/create.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/channel/environment/file.py` & `runtimepy-0.9.6/runtimepy/channel/environment/file.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/channel/environment/names.py` & `runtimepy-0.9.6/runtimepy/channel/environment/names.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/channel/registry.py` & `runtimepy-0.9.6/runtimepy/channel/registry.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/commands/all.py` & `runtimepy-0.9.6/runtimepy/commands/all.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/commands/tui.py` & `runtimepy-0.9.6/runtimepy/commands/tui.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/data/schemas/BitFields.yaml` & `runtimepy-0.9.6/runtimepy/data/schemas/BitFields.yaml`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/data/schemas/ChannelRegistry.yaml` & `runtimepy-0.9.6/runtimepy/data/schemas/ChannelRegistry.yaml`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/entry.py` & `runtimepy-0.9.6/runtimepy/entry.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/enum/__init__.py` & `runtimepy-0.9.6/runtimepy/enum/__init__.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/enum/registry.py` & `runtimepy-0.9.6/runtimepy/enum/registry.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/enum/type.py` & `runtimepy-0.9.6/runtimepy/enum/type.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/mapping.py` & `runtimepy-0.9.6/runtimepy/mapping.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/mixins/enum.py` & `runtimepy-0.9.6/runtimepy/mixins/enum.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/mixins/regex.py` & `runtimepy-0.9.6/runtimepy/mixins/regex.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/__init__.py` & `runtimepy-0.9.6/runtimepy/primitives/__init__.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/array.py` & `runtimepy-0.9.6/runtimepy/primitives/array.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/base.py` & `runtimepy-0.9.6/runtimepy/primitives/base.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/bool.py` & `runtimepy-0.9.6/runtimepy/primitives/bool.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/field/__init__.py` & `runtimepy-0.9.6/runtimepy/primitives/field/__init__.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/field/fields.py` & `runtimepy-0.9.6/runtimepy/primitives/field/fields.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/field/manager.py` & `runtimepy-0.9.6/runtimepy/primitives/field/manager.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/float.py` & `runtimepy-0.9.6/runtimepy/primitives/float.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/int.py` & `runtimepy-0.9.6/runtimepy/primitives/int.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/type/__init__.py` & `runtimepy-0.9.6/runtimepy/primitives/type/__init__.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/type/base.py` & `runtimepy-0.9.6/runtimepy/primitives/type/base.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/type/float.py` & `runtimepy-0.9.6/runtimepy/primitives/type/float.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/primitives/type/int.py` & `runtimepy-0.9.6/runtimepy/primitives/type/int.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/registry/__init__.py` & `runtimepy-0.9.6/runtimepy/registry/__init__.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/registry/bool.py` & `runtimepy-0.9.6/runtimepy/registry/bool.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/registry/item.py` & `runtimepy-0.9.6/runtimepy/registry/item.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/registry/name.py` & `runtimepy-0.9.6/runtimepy/registry/name.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/schemas.py` & `runtimepy-0.9.6/runtimepy/schemas.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/task/__init__.py` & `runtimepy-0.9.6/runtimepy/task/__init__.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/tui/channels/__init__.py` & `runtimepy-0.9.6/runtimepy/tui/channels/__init__.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy/tui/task.py` & `runtimepy-0.9.6/runtimepy/tui/task.py`

 * *Files identical despite different names*

### Comparing `runtimepy-0.9.5/runtimepy.egg-info/SOURCES.txt` & `runtimepy-0.9.6/runtimepy.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -34,14 +34,15 @@
 runtimepy/enum/__init__.py
 runtimepy/enum/registry.py
 runtimepy/enum/type.py
 runtimepy/mixins/__init__.py
 runtimepy/mixins/enum.py
 runtimepy/mixins/regex.py
 runtimepy/net/__init__.py
+runtimepy/net/connection.py
 runtimepy/net/websocket/__init__.py
 runtimepy/net/websocket/connection.py
 runtimepy/primitives/__init__.py
 runtimepy/primitives/array.py
 runtimepy/primitives/base.py
 runtimepy/primitives/bool.py
 runtimepy/primitives/float.py
```

### Comparing `runtimepy-0.9.5/setup.py` & `runtimepy-0.9.6/setup.py`

 * *Files identical despite different names*

