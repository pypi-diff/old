# Comparing `tmp/vdk-notebook-0.1.824443273.tar.gz` & `tmp/vdk-notebook-0.1.830072376.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "vdk-notebook-0.1.824443273.tar", last modified: Fri Mar 31 14:25:59 2023, max compression
+gzip compressed data, was "vdk-notebook-0.1.830072376.tar", last modified: Thu Apr  6 12:03:19 2023, max compression
```

## Comparing `vdk-notebook-0.1.824443273.tar` & `vdk-notebook-0.1.830072376.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 14:25:59.938684 vdk-notebook-0.1.824443273/
--rw-r--r--   0 root         (0) root         (0)     1804 2023-03-31 14:25:59.938684 vdk-notebook-0.1.824443273/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     1263 2023-03-31 14:25:48.000000 vdk-notebook-0.1.824443273/README.md
--rw-r--r--   0 root         (0) root         (0)       38 2023-03-31 14:25:59.938684 vdk-notebook-0.1.824443273/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)     1007 2023-03-31 14:25:51.000000 vdk-notebook-0.1.824443273/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 14:25:59.938684 vdk-notebook-0.1.824443273/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 14:25:59.934684 vdk-notebook-0.1.824443273/src/vdk/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 14:25:59.934684 vdk-notebook-0.1.824443273/src/vdk/plugin/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 14:25:59.938684 vdk-notebook-0.1.824443273/src/vdk/plugin/notebook/
--rw-rw-rw-   0 root         (0) root         (0)      348 2023-03-31 14:25:48.000000 vdk-notebook-0.1.824443273/src/vdk/plugin/notebook/cell.py
--rw-rw-rw-   0 root         (0) root         (0)     4148 2023-03-31 14:25:48.000000 vdk-notebook-0.1.824443273/src/vdk/plugin/notebook/notebook.py
--rw-rw-rw-   0 root         (0) root         (0)     4271 2023-03-31 14:25:48.000000 vdk-notebook-0.1.824443273/src/vdk/plugin/notebook/notebook_based_step.py
--rw-rw-rw-   0 root         (0) root         (0)      990 2023-03-31 14:25:48.000000 vdk-notebook-0.1.824443273/src/vdk/plugin/notebook/notebook_plugin.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 14:25:59.938684 vdk-notebook-0.1.824443273/src/vdk_notebook.egg-info/
--rw-r--r--   0 root         (0) root         (0)     1804 2023-03-31 14:25:59.000000 vdk-notebook-0.1.824443273/src/vdk_notebook.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      439 2023-03-31 14:25:59.000000 vdk-notebook-0.1.824443273/src/vdk_notebook.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-31 14:25:59.000000 vdk-notebook-0.1.824443273/src/vdk_notebook.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       64 2023-03-31 14:25:59.000000 vdk-notebook-0.1.824443273/src/vdk_notebook.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        9 2023-03-31 14:25:59.000000 vdk-notebook-0.1.824443273/src/vdk_notebook.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        4 2023-03-31 14:25:59.000000 vdk-notebook-0.1.824443273/src/vdk_notebook.egg-info/top_level.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-31 14:25:59.938684 vdk-notebook-0.1.824443273/tests/
--rw-rw-rw-   0 root         (0) root         (0)     2028 2023-03-31 14:25:48.000000 vdk-notebook-0.1.824443273/tests/test_plugin.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 12:03:19.683823 vdk-notebook-0.1.830072376/
+-rw-r--r--   0 root         (0) root         (0)     1804 2023-04-06 12:03:19.683823 vdk-notebook-0.1.830072376/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     1263 2023-04-06 12:03:07.000000 vdk-notebook-0.1.830072376/README.md
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 12:03:19.683823 vdk-notebook-0.1.830072376/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)     1007 2023-04-06 12:03:10.000000 vdk-notebook-0.1.830072376/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 12:03:19.683823 vdk-notebook-0.1.830072376/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 12:03:19.683823 vdk-notebook-0.1.830072376/src/vdk/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 12:03:19.683823 vdk-notebook-0.1.830072376/src/vdk/plugin/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 12:03:19.683823 vdk-notebook-0.1.830072376/src/vdk/plugin/notebook/
+-rw-rw-rw-   0 root         (0) root         (0)      522 2023-04-06 12:03:07.000000 vdk-notebook-0.1.830072376/src/vdk/plugin/notebook/cell.py
+-rw-rw-rw-   0 root         (0) root         (0)     4196 2023-04-06 12:03:07.000000 vdk-notebook-0.1.830072376/src/vdk/plugin/notebook/notebook.py
+-rw-rw-rw-   0 root         (0) root         (0)     4442 2023-04-06 12:03:07.000000 vdk-notebook-0.1.830072376/src/vdk/plugin/notebook/notebook_based_step.py
+-rw-rw-rw-   0 root         (0) root         (0)     2008 2023-04-06 12:03:07.000000 vdk-notebook-0.1.830072376/src/vdk/plugin/notebook/notebook_plugin.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 12:03:19.683823 vdk-notebook-0.1.830072376/src/vdk_notebook.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1804 2023-04-06 12:03:19.000000 vdk-notebook-0.1.830072376/src/vdk_notebook.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      439 2023-04-06 12:03:19.000000 vdk-notebook-0.1.830072376/src/vdk_notebook.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 12:03:19.000000 vdk-notebook-0.1.830072376/src/vdk_notebook.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       64 2023-04-06 12:03:19.000000 vdk-notebook-0.1.830072376/src/vdk_notebook.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        9 2023-04-06 12:03:19.000000 vdk-notebook-0.1.830072376/src/vdk_notebook.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        4 2023-04-06 12:03:19.000000 vdk-notebook-0.1.830072376/src/vdk_notebook.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 12:03:19.683823 vdk-notebook-0.1.830072376/tests/
+-rw-rw-rw-   0 root         (0) root         (0)     2028 2023-04-06 12:03:07.000000 vdk-notebook-0.1.830072376/tests/test_plugin.py
```

### Comparing `vdk-notebook-0.1.824443273/PKG-INFO` & `vdk-notebook-0.1.830072376/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vdk-notebook
-Version: 0.1.824443273
+Version: 0.1.830072376
 Summary: A VDK plugin for working with notebooks
 Home-page: https://github.com/vmware/versatile-data-kit
 Classifier: Development Status :: 3 - Alpha
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `vdk-notebook-0.1.824443273/README.md` & `vdk-notebook-0.1.830072376/README.md`

 * *Files identical despite different names*

### Comparing `vdk-notebook-0.1.824443273/setup.py` & `vdk-notebook-0.1.830072376/setup.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # Copyright 2021-2023 VMware, Inc.
 # SPDX-License-Identifier: Apache-2.0
 import pathlib
 
 import setuptools
 
 
-__version__ = "0.1.824443273"
+__version__ = "0.1.830072376"
 
 setuptools.setup(
     name="vdk-notebook",
     version=__version__,
     url="https://github.com/vmware/versatile-data-kit",
     description="A VDK plugin for working with notebooks",
     long_description=pathlib.Path("README.md").read_text(),
```

### Comparing `vdk-notebook-0.1.824443273/src/vdk/plugin/notebook/notebook.py` & `vdk-notebook-0.1.830072376/src/vdk/plugin/notebook/notebook.py`

 * *Files 1% similar despite different names*

```diff
@@ -23,15 +23,15 @@
     """
 
     @staticmethod
     def get_notebook_files(directory: pathlib.Path) -> List[pathlib.Path]:
         """Locates the files in a directory, that are supported for execution.
         Files supported for execution are: .ipynb
         Other files in the directory are ignored.
-        :return: List of files from the directory that supported for execution, sorted alphabetically by name.
+        :return: List of files from the directory that supported for execution, sorted alphabetically by name.s
         :rtype: :class:`.list`
         """
         script_files = [
             x for x in directory.iterdir() if (x.name.lower().endswith(".ipynb"))
         ]
         script_files.sort(key=lambda x: x.name)
         log.debug(f"Script files of {directory} are {script_files}")
@@ -71,15 +71,16 @@
                                     str(index),
                                 ]
                             ),
                             type=TYPE_PYTHON,
                             runner_func=NotebookStepFuncFactory.run_python_step,
                             file_path=file_path,
                             job_dir=context.job_directory,
-                            code=cell.source,
+                            source=cell.source,
+                            cell_id=cell.id,
                             module=python_module,
                         )
                         notebook_steps.append(step)
                         context.step_builder.add_step(step)
                 index += 1
 
             log.debug(f"{len(notebook_steps)} " f"cells with vdk tag were detected!")
```

### Comparing `vdk-notebook-0.1.824443273/src/vdk/plugin/notebook/notebook_based_step.py` & `vdk-notebook-0.1.830072376/src/vdk/plugin/notebook/notebook_based_step.py`

 * *Files 5% similar despite different names*

```diff
@@ -8,15 +8,14 @@
 
 from vdk.api.job_input import IJobInput
 from vdk.internal.builtin_plugins.run.step import Step
 from vdk.internal.core import errors
 
 log = logging.getLogger(__name__)
 
-
 # consists may duplicates of
 # https://github.com/vmware/versatile-data-kit/blob/main/projects/vdk-core/src/vdk/internal/builtin_plugins/run/file_based_step.py
 
 # The function accept NotebookStep (below class) and IJobInput and
 # return true if the step has been executed and false if it is not (valid) executable step.
 # On error it's expected to raise an exception.
 NotebookStepFunction = Callable[["NotebookStep", IJobInput], bool]
@@ -32,34 +31,36 @@
     ::type: str - string representing a step type (sql or python).
     ::runner_func: StepFunction - function that will execute the actual step
     ::file_path: pathlib.Path - file where the step is defined
     ::job_dir: pathlib.Path - the root job directory
     ::parent: Step | None = None - parent Step
 
     Additional attributes:
-    ::code: str - the code string retrieved from Jupyter code cell
+    ::source: str - the code string retrieved from Jupyter code cell
     ::module: module object - the module the code belongs to
     (see imp.new_module in https://docs.python.org/3/library/imp.html)
     """
 
     def __init__(
         self,
         name,
         type,
         runner_func,
         file_path,
         job_dir,
-        code,
+        source,
+        cell_id,
         module=None,
         parent=None,
     ):
         super().__init__(name, type, runner_func, file_path, job_dir, parent)
         self.runner_func = runner_func
-        self.code = code
+        self.source = source
         self.module = module
+        self.cell_id = cell_id
 
 
 class NotebookStepFuncFactory:
     """
     Implementations of runner_func for running Notebook steps
     """
 
@@ -67,38 +68,40 @@
     def run_python_step(step: NotebookStep, job_input: IJobInput) -> bool:
         try:
             sys.path.insert(0, str(step.job_dir))
             success = False
             try:
                 log.debug("Loading %s ..." % step.name)
                 step.module.job_input = job_input
-                exec(step.code, step.module.__dict__)
+                exec(step.source, step.module.__dict__)
                 log.debug("Loading %s SUCCESS" % step.name)
                 success = True
             except SyntaxError as e:
                 log.info("Loading %s FAILURE" % step.name)
                 errors.log_and_rethrow(
                     to_be_fixed_by=errors.ResolvableBy.USER_ERROR,
                     log=log,
-                    what_happened=f"Failed loading job sources of {step.name} from {step.file_path.name}",
+                    what_happened=f"Failed loading job sources of {step.name} from cell with id:{step.cell_id}"
+                    f" from {step.file_path.name}",
                     why_it_happened=f"{e.__class__.__name__} at line {e.lineno} of {step.name}"
                     f": {e.args[0]}",
                     consequences=f"Current Step {step.name} from {step.file_path}"
                     f"will fail, and as a result the whole Data Job will fail. ",
                     countermeasures=f"Please, check the {step.file_path.name} file again for syntax errors",
                     exception=e,
                     wrap_in_vdk_error=True,
                 )
             except Exception as e:
                 cl, exc, tb = sys.exc_info()
                 line_number = traceback.extract_tb(tb)[-1][1]
                 errors.log_and_rethrow(
                     to_be_fixed_by=errors.ResolvableBy.USER_ERROR,
                     log=log,
-                    what_happened=f"Failed loading job sources of {step.name} from {step.file_path.name}",
+                    what_happened=f"Failed loading job sources of {step.name} from cell with id:{step.cell_id}"
+                    f" from {step.file_path.name}",
                     why_it_happened=f"{e.__class__.__name__} at line {line_number} of {step.name}"
                     f": {e.args[0]}",
                     consequences=f"Current Step {step.name} from {step.file_path}"
                     f"will fail, and as a result the whole Data Job will fail. ",
                     countermeasures=f"Please, check the {step.file_path.name} file again for errors",
                     exception=e,
                     wrap_in_vdk_error=True,
```

### Comparing `vdk-notebook-0.1.824443273/src/vdk_notebook.egg-info/PKG-INFO` & `vdk-notebook-0.1.830072376/src/vdk_notebook.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vdk-notebook
-Version: 0.1.824443273
+Version: 0.1.830072376
 Summary: A VDK plugin for working with notebooks
 Home-page: https://github.com/vmware/versatile-data-kit
 Classifier: Development Status :: 3 - Alpha
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `vdk-notebook-0.1.824443273/tests/test_plugin.py` & `vdk-notebook-0.1.830072376/tests/test_plugin.py`

 * *Files identical despite different names*

