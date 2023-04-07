# Comparing `tmp/gusty-0.9.0.tar.gz` & `tmp/gusty-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gusty-0.9.0.tar", last modified: Fri May 20 19:09:03 2022, max compression
+gzip compressed data, was "gusty-0.9.1.tar", last modified: Tue May 24 14:58:44 2022, max compression
```

## Comparing `gusty-0.9.0.tar` & `gusty-0.9.1.tar`

### file list

```diff
@@ -1,37 +1,37 @@
-drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-05-20 19:09:03.323188 gusty-0.9.0/
--rw-rw-r--   0 chris     (1000) chris     (1000)     1077 2021-03-20 13:56:01.000000 gusty-0.9.0/LICENSE
--rw-rw-r--   0 chris     (1000) chris     (1000)    13631 2022-05-20 19:09:03.323188 gusty-0.9.0/PKG-INFO
--rw-rw-r--   0 chris     (1000) chris     (1000)    13170 2022-05-20 19:07:17.000000 gusty-0.9.0/README.md
-drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-05-20 19:09:03.319188 gusty-0.9.0/gusty/
--rw-rw-r--   0 chris     (1000) chris     (1000)     2852 2022-02-01 22:13:09.000000 gusty-0.9.0/gusty/__init__.py
--rw-rw-r--   0 chris     (1000) chris     (1000)    35569 2022-05-20 19:07:17.000000 gusty-0.9.0/gusty/building.py
--rw-rw-r--   0 chris     (1000) chris     (1000)       50 2021-12-09 23:18:34.000000 gusty-0.9.0/gusty/errors.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     1325 2022-02-20 00:43:58.000000 gusty-0.9.0/gusty/external_sensor.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     2189 2021-05-12 23:06:15.000000 gusty-0.9.0/gusty/importing.py
-drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-05-20 19:09:03.319188 gusty-0.9.0/gusty/parsing/
--rw-rw-r--   0 chris     (1000) chris     (1000)     2707 2022-05-20 19:07:17.000000 gusty-0.9.0/gusty/parsing/__init__.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     1935 2022-05-18 17:27:23.000000 gusty-0.9.0/gusty/parsing/loaders.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     5270 2022-05-20 11:47:06.000000 gusty-0.9.0/gusty/parsing/parsers.py
--rw-rw-r--   0 chris     (1000) chris     (1000)      154 2022-05-18 17:26:46.000000 gusty-0.9.0/gusty/utils.py
-drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-05-20 19:09:03.319188 gusty-0.9.0/gusty.egg-info/
--rw-rw-r--   0 chris     (1000) chris     (1000)    13631 2022-05-20 19:09:02.000000 gusty-0.9.0/gusty.egg-info/PKG-INFO
--rw-rw-r--   0 chris     (1000) chris     (1000)      707 2022-05-20 19:09:03.000000 gusty-0.9.0/gusty.egg-info/SOURCES.txt
--rw-rw-r--   0 chris     (1000) chris     (1000)        1 2022-05-20 19:09:02.000000 gusty-0.9.0/gusty.egg-info/dependency_links.txt
--rw-rw-r--   0 chris     (1000) chris     (1000)       60 2022-05-20 19:09:03.000000 gusty-0.9.0/gusty.egg-info/requires.txt
--rw-rw-r--   0 chris     (1000) chris     (1000)       12 2022-05-20 19:09:03.000000 gusty-0.9.0/gusty.egg-info/top_level.txt
--rw-rw-r--   0 chris     (1000) chris     (1000)       38 2022-05-20 19:09:03.323188 gusty-0.9.0/setup.cfg
--rw-rw-r--   0 chris     (1000) chris     (1000)      833 2022-05-20 19:07:17.000000 gusty-0.9.0/setup.py
-drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-05-20 19:09:03.323188 gusty-0.9.0/tests/
--rw-rw-r--   0 chris     (1000) chris     (1000)        0 2021-03-20 13:56:01.000000 gusty-0.9.0/tests/__init__.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     3487 2022-05-20 14:33:23.000000 gusty-0.9.0/tests/test_adjusted_behavior.py
--rw-rw-r--   0 chris     (1000) chris     (1000)      717 2021-04-26 19:57:54.000000 gusty-0.9.0/tests/test_custom_operators.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     5020 2022-05-18 17:23:58.000000 gusty-0.9.0/tests/test_default_behavior.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     1146 2022-02-19 22:48:53.000000 gusty-0.9.0/tests/test_external_deps.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     1272 2022-05-18 17:23:58.000000 gusty-0.9.0/tests/test_ignore_subfolders.py
--rw-rw-r--   0 chris     (1000) chris     (1000)      905 2021-03-20 13:56:01.000000 gusty-0.9.0/tests/test_importing.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     2240 2022-05-18 17:23:58.000000 gusty-0.9.0/tests/test_loader.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     2196 2022-05-20 19:07:17.000000 gusty-0.9.0/tests/test_multi_task.py
--rw-rw-r--   0 chris     (1000) chris     (1000)      618 2021-12-09 23:18:34.000000 gusty-0.9.0/tests/test_no_dir.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     1972 2022-05-18 17:23:58.000000 gusty-0.9.0/tests/test_parsing.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     1653 2022-05-18 14:17:08.000000 gusty-0.9.0/tests/test_python_tasks.py
--rw-rw-r--   0 chris     (1000) chris     (1000)     1364 2022-05-18 17:23:58.000000 gusty-0.9.0/tests/test_task_group_dependencies.py
+drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-05-24 14:58:44.056876 gusty-0.9.1/
+-rw-rw-r--   0 chris     (1000) chris     (1000)     1077 2021-03-20 13:56:01.000000 gusty-0.9.1/LICENSE
+-rw-rw-r--   0 chris     (1000) chris     (1000)    13604 2022-05-24 14:58:44.056876 gusty-0.9.1/PKG-INFO
+-rw-rw-r--   0 chris     (1000) chris     (1000)    13143 2022-05-22 23:34:43.000000 gusty-0.9.1/README.md
+drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-05-24 14:58:44.056876 gusty-0.9.1/gusty/
+-rw-rw-r--   0 chris     (1000) chris     (1000)     2852 2022-02-01 22:13:09.000000 gusty-0.9.1/gusty/__init__.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)    35853 2022-05-24 14:55:54.000000 gusty-0.9.1/gusty/building.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)       50 2021-12-09 23:18:34.000000 gusty-0.9.1/gusty/errors.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     1325 2022-02-20 00:43:58.000000 gusty-0.9.1/gusty/external_sensor.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     2189 2021-05-12 23:06:15.000000 gusty-0.9.1/gusty/importing.py
+drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-05-24 14:58:44.056876 gusty-0.9.1/gusty/parsing/
+-rw-rw-r--   0 chris     (1000) chris     (1000)     2707 2022-05-20 19:07:17.000000 gusty-0.9.1/gusty/parsing/__init__.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     1935 2022-05-18 17:27:23.000000 gusty-0.9.1/gusty/parsing/loaders.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     5270 2022-05-20 11:47:06.000000 gusty-0.9.1/gusty/parsing/parsers.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)      154 2022-05-18 17:26:46.000000 gusty-0.9.1/gusty/utils.py
+drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-05-24 14:58:44.056876 gusty-0.9.1/gusty.egg-info/
+-rw-rw-r--   0 chris     (1000) chris     (1000)    13604 2022-05-24 14:58:43.000000 gusty-0.9.1/gusty.egg-info/PKG-INFO
+-rw-rw-r--   0 chris     (1000) chris     (1000)      707 2022-05-24 14:58:44.000000 gusty-0.9.1/gusty.egg-info/SOURCES.txt
+-rw-rw-r--   0 chris     (1000) chris     (1000)        1 2022-05-24 14:58:43.000000 gusty-0.9.1/gusty.egg-info/dependency_links.txt
+-rw-rw-r--   0 chris     (1000) chris     (1000)       60 2022-05-24 14:58:43.000000 gusty-0.9.1/gusty.egg-info/requires.txt
+-rw-rw-r--   0 chris     (1000) chris     (1000)       12 2022-05-24 14:58:44.000000 gusty-0.9.1/gusty.egg-info/top_level.txt
+-rw-rw-r--   0 chris     (1000) chris     (1000)       38 2022-05-24 14:58:44.056876 gusty-0.9.1/setup.cfg
+-rw-rw-r--   0 chris     (1000) chris     (1000)      833 2022-05-24 14:01:40.000000 gusty-0.9.1/setup.py
+drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-05-24 14:58:44.056876 gusty-0.9.1/tests/
+-rw-rw-r--   0 chris     (1000) chris     (1000)        0 2021-03-20 13:56:01.000000 gusty-0.9.1/tests/__init__.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     3723 2022-05-24 14:01:12.000000 gusty-0.9.1/tests/test_adjusted_behavior.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)      717 2021-04-26 19:57:54.000000 gusty-0.9.1/tests/test_custom_operators.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     5020 2022-05-18 17:23:58.000000 gusty-0.9.1/tests/test_default_behavior.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     1146 2022-02-19 22:48:53.000000 gusty-0.9.1/tests/test_external_deps.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     1272 2022-05-18 17:23:58.000000 gusty-0.9.1/tests/test_ignore_subfolders.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)      905 2021-03-20 13:56:01.000000 gusty-0.9.1/tests/test_importing.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     2240 2022-05-18 17:23:58.000000 gusty-0.9.1/tests/test_loader.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     2196 2022-05-20 19:07:17.000000 gusty-0.9.1/tests/test_multi_task.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)      618 2021-12-09 23:18:34.000000 gusty-0.9.1/tests/test_no_dir.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     1972 2022-05-18 17:23:58.000000 gusty-0.9.1/tests/test_parsing.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     1653 2022-05-18 14:17:08.000000 gusty-0.9.1/tests/test_python_tasks.py
+-rw-rw-r--   0 chris     (1000) chris     (1000)     1364 2022-05-18 17:23:58.000000 gusty-0.9.1/tests/test_task_group_dependencies.py
```

### Comparing `gusty-0.9.0/LICENSE` & `gusty-0.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/PKG-INFO` & `gusty-0.9.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gusty
-Version: 0.9.0
+Version: 0.9.1
 Summary: Making DAG construction easier
 Home-page: https://github.com/chriscardillo/gusty
 Author: Chris Cardillo, Michael Chow, David Robinson
 Author-email: cfcardillo23@gmail.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
@@ -223,15 +223,14 @@
 
 ### Multi-Task Generation
 
 Sometimes task definitions can be repetitive. To account for this, gusty allows for a `multi_task_spec` block in any frontmatter. This allows you to generate multiple similar tasks with a single task definition file! For example, let's say you wanted to create two bash tasks, each containing a different `bash_command`. You can define these two tasks in a single task definition file like so:
 
 ```yml
 operator: airflow.operators.bash.BashOperator
-bash_command: echo default
 multi_task_spec:
   bash_task_1:
     bash_command: echo first_task
   bash_task_2:
     bash_command: echo second_task
 ```
```

### Comparing `gusty-0.9.0/README.md` & `gusty-0.9.1/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -209,15 +209,14 @@
 
 ### Multi-Task Generation
 
 Sometimes task definitions can be repetitive. To account for this, gusty allows for a `multi_task_spec` block in any frontmatter. This allows you to generate multiple similar tasks with a single task definition file! For example, let's say you wanted to create two bash tasks, each containing a different `bash_command`. You can define these two tasks in a single task definition file like so:
 
 ```yml
 operator: airflow.operators.bash.BashOperator
-bash_command: echo default
 multi_task_spec:
   bash_task_1:
     bash_command: echo first_task
   bash_task_2:
     bash_command: echo second_task
 ```
```

### Comparing `gusty-0.9.0/gusty/__init__.py` & `gusty-0.9.1/gusty/__init__.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/gusty/building.py` & `gusty-0.9.1/gusty/building.py`

 * *Files 0% similar despite different names*

```diff
@@ -314,14 +314,21 @@
                 # level_metadata (provided via METADATA.yml)
                 level_default_args = level_metadata["default_args"]
                 # metadata defaults updated with level_metadata
                 metadata_default_args.update(level_default_args)
                 # updated and resolved attached back to level_metadata
                 level_metadata.update({"default_args": metadata_default_args})
 
+            # special case - wait_for_defaults
+            if (
+                self.schematic[id]["parent_id"] is None
+                and "wait_for_defaults" in level_metadata.keys()
+            ):
+                self.wait_for_defaults.update(level_metadata["wait_for_defaults"])
+
         else:
             level_metadata = {}
         metadata_defaults.update(level_metadata)
         self.schematic[id]["metadata"] = metadata_defaults
 
         # dependencies get explicity set at the level-"level" for each level
         # and must be pulled out separately from other metadata.
```

### Comparing `gusty-0.9.0/gusty/external_sensor.py` & `gusty-0.9.1/gusty/external_sensor.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/gusty/importing.py` & `gusty-0.9.1/gusty/importing.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/gusty/parsing/__init__.py` & `gusty-0.9.1/gusty/parsing/__init__.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/gusty/parsing/loaders.py` & `gusty-0.9.1/gusty/parsing/loaders.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/gusty/parsing/parsers.py` & `gusty-0.9.1/gusty/parsing/parsers.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/gusty.egg-info/PKG-INFO` & `gusty-0.9.1/gusty.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gusty
-Version: 0.9.0
+Version: 0.9.1
 Summary: Making DAG construction easier
 Home-page: https://github.com/chriscardillo/gusty
 Author: Chris Cardillo, Michael Chow, David Robinson
 Author-email: cfcardillo23@gmail.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
@@ -223,15 +223,14 @@
 
 ### Multi-Task Generation
 
 Sometimes task definitions can be repetitive. To account for this, gusty allows for a `multi_task_spec` block in any frontmatter. This allows you to generate multiple similar tasks with a single task definition file! For example, let's say you wanted to create two bash tasks, each containing a different `bash_command`. You can define these two tasks in a single task definition file like so:
 
 ```yml
 operator: airflow.operators.bash.BashOperator
-bash_command: echo default
 multi_task_spec:
   bash_task_1:
     bash_command: echo first_task
   bash_task_2:
     bash_command: echo second_task
 ```
```

### Comparing `gusty-0.9.0/gusty.egg-info/SOURCES.txt` & `gusty-0.9.1/gusty.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/setup.py` & `gusty-0.9.1/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="gusty",
-    version="0.9.0",
+    version="0.9.1",
     author="Chris Cardillo, Michael Chow, David Robinson",
     author_email="cfcardillo23@gmail.com",
     description="Making DAG construction easier",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/chriscardillo/gusty",
     packages=setuptools.find_packages(),
```

### Comparing `gusty-0.9.0/tests/test_adjusted_behavior.py` & `gusty-0.9.1/tests/test_adjusted_behavior.py`

 * *Files 6% similar despite different names*

```diff
@@ -83,14 +83,24 @@
     wait_for_tasks_adjusted = [
         task.__dict__["poke_interval"] == 12 for task in wait_for_tasks
     ]
 
     assert all(wait_for_tasks_adjusted)
 
 
+def test_metadata_wait_for_defaults(dag):
+    wait_for_task = [
+        task
+        for task_id, task in dag.task_dict.items()
+        if task_id.startswith("wait_for_")
+    ][0]
+
+    assert wait_for_task.__dict__["timeout"] == 1234
+
+
 def test_prefixed_dependencies_work(dag):
     # if a user turns task group prefixes/suffixes on, gusty should proactively check
     # for prefixed/suffixed dependencies in addition to whatever is provided in a task's spec
     # e.g. in a task group "tg" with prefixes turned on, the dependency to look for is "tg_task",
     #      but the user only specified "task" in the depedencies block.
     assert (
         "prefixes.prefixes_check"
```

### Comparing `gusty-0.9.0/tests/test_custom_operators.py` & `gusty-0.9.1/tests/test_custom_operators.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/tests/test_default_behavior.py` & `gusty-0.9.1/tests/test_default_behavior.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/tests/test_external_deps.py` & `gusty-0.9.1/tests/test_external_deps.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/tests/test_ignore_subfolders.py` & `gusty-0.9.1/tests/test_ignore_subfolders.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/tests/test_importing.py` & `gusty-0.9.1/tests/test_importing.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/tests/test_loader.py` & `gusty-0.9.1/tests/test_loader.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/tests/test_multi_task.py` & `gusty-0.9.1/tests/test_multi_task.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/tests/test_no_dir.py` & `gusty-0.9.1/tests/test_no_dir.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/tests/test_parsing.py` & `gusty-0.9.1/tests/test_parsing.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/tests/test_python_tasks.py` & `gusty-0.9.1/tests/test_python_tasks.py`

 * *Files identical despite different names*

### Comparing `gusty-0.9.0/tests/test_task_group_dependencies.py` & `gusty-0.9.1/tests/test_task_group_dependencies.py`

 * *Files identical despite different names*

