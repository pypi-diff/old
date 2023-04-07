# Comparing `tmp/pye2-0.3.1.tar.gz` & `tmp/pye2-0.3.2.tar.gz`

## Comparing `pye2-0.3.1.tar` & `pye2-0.3.2.tar`

### file list

```diff
@@ -1,47 +1,52 @@
--rw-r--r--   0        0        0      261 2020-02-02 00:00:00.000000 pye2-0.3.1/TODOs.md
--rw-r--r--   0        0        0       75 2020-02-02 00:00:00.000000 pye2-0.3.1/__init__.py
--rw-r--r--   0        0        0       14 2020-02-02 00:00:00.000000 pye2-0.3.1/requirements.txt
--rw-r--r--   0        0        0     1291 2020-02-02 00:00:00.000000 pye2-0.3.1/.github/workflows/python-publish.yml
--rw-r--r--   0        0        0      115 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/__init__.py
--rw-r--r--   0        0        0      339 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/version.py
--rw-r--r--   0        0        0      818 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/base/__init__.py
--rw-r--r--   0        0        0    18533 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/base/generic_session.py
--rw-r--r--   0        0        0    16351 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/base/pipeline.py
--rw-r--r--   0        0        0    18533 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/base/tmpeb3hj3eh
--rw-r--r--   0        0        0       29 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/base/payload/__init__.py
--rw-r--r--   0        0        0      824 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/base/payload/payload.py
--rw-r--r--   0        0        0      790 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/comm/__init__.py
--rw-r--r--   0        0        0     9139 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/comm/amqp_wrapper.py
--rw-r--r--   0        0        0    10508 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/comm/mqtt_wrapper.py
--rw-r--r--   0        0        0      177 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/const/README.md
--rw-r--r--   0        0        0     1032 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/const/__init__.py
--rw-r--r--   0        0        0     2598 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/const/base.py
--rw-r--r--   0        0        0     1873 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/const/comms.py
--rw-r--r--   0        0        0     1734 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/const/heartbeat.py
--rw-r--r--   0        0        0      890 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/const/misc.py
--rw-r--r--   0        0        0     2564 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/const/payload.py
--rw-r--r--   0        0        0       49 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/default/__init__.py
--rw-r--r--   0        0        0     5753 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/default/mqtt_session.py
--rw-r--r--   0        0        0      761 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/io_formatter/__init__.py
--rw-r--r--   0        0        0     1334 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/io_formatter/consts.py
--rw-r--r--   0        0        0     3619 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/io_formatter/io_formatter_manager.py
--rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/io_formatter/base/__init__.py
--rw-r--r--   0        0        0     3423 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/io_formatter/base/base_formatter.py
--rw-r--r--   0        0        0      696 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/io_formatter/default/__init__.py
--rw-r--r--   0        0        0     1148 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/io_formatter/default/a_dummy.py
--rw-r--r--   0        0        0    11753 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/io_formatter/default/cavi2.py
--rw-r--r--   0        0        0       56 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/io_formatter/mixins/__init__.py
--rw-r--r--   0        0        0     4810 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/io_formatter/mixins/plugins_manager_mixin.py
--rw-r--r--   0        0        0       38 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/utils/__init__.py
--rw-r--r--   0        0        0     1759 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/utils/code.py
--rw-r--r--   0        0        0     1625 2020-02-02 00:00:00.000000 pye2-0.3.1/PyE2/utils/code_exec.py
--rw-r--r--   0        0        0     4182 2020-02-02 00:00:00.000000 pye2-0.3.1/xperimental/custom_exec_tutorial.py
--rw-r--r--   0        0        0     1881 2020-02-02 00:00:00.000000 pye2-0.3.1/xperimental/dedist_example.py
--rw-r--r--   0        0        0     2300 2020-02-02 00:00:00.000000 pye2-0.3.1/xperimental/dedist_example_initiator.py
--rw-r--r--   0        0        0      276 2020-02-02 00:00:00.000000 pye2-0.3.1/xperimental/dedist_example_worker.py
--rw-r--r--   0        0        0     3350 2020-02-02 00:00:00.000000 pye2-0.3.1/xperimental/ex1.py
--rw-r--r--   0        0        0     2457 2020-02-02 00:00:00.000000 pye2-0.3.1/.gitignore
--rw-r--r--   0        0        0    11357 2020-02-02 00:00:00.000000 pye2-0.3.1/LICENSE
--rw-r--r--   0        0        0     5791 2020-02-02 00:00:00.000000 pye2-0.3.1/README.md
--rw-r--r--   0        0        0      760 2020-02-02 00:00:00.000000 pye2-0.3.1/pyproject.toml
--rw-r--r--   0        0        0     6430 2020-02-02 00:00:00.000000 pye2-0.3.1/PKG-INFO
+-rw-r--r--   0        0        0      219 2020-02-02 00:00:00.000000 pye2-0.3.2/TODOs.md
+-rw-r--r--   0        0        0       75 2020-02-02 00:00:00.000000 pye2-0.3.2/__init__.py
+-rw-r--r--   0        0        0       14 2020-02-02 00:00:00.000000 pye2-0.3.2/requirements.txt
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 pye2-0.3.2/winrun.bat
+-rw-r--r--   0        0        0     1291 2020-02-02 00:00:00.000000 pye2-0.3.2/.github/workflows/python-publish.yml
+-rw-r--r--   0        0        0      115 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/__init__.py
+-rw-r--r--   0        0        0      330 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/version.py
+-rw-r--r--   0        0        0      845 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/base/__init__.py
+-rw-r--r--   0        0        0    16027 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/base/generic_session.py
+-rw-r--r--   0        0        0     4391 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/base/logger.py
+-rw-r--r--   0        0        0    18391 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/base/pipeline.py
+-rw-r--r--   0        0        0    18533 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/base/tmpeb3hj3eh
+-rw-r--r--   0        0        0       29 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/base/payload/__init__.py
+-rw-r--r--   0        0        0      824 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/base/payload/payload.py
+-rw-r--r--   0        0        0      790 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/comm/__init__.py
+-rw-r--r--   0        0        0     9139 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/comm/amqp_wrapper.py
+-rw-r--r--   0        0        0    10508 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/comm/mqtt_wrapper.py
+-rw-r--r--   0        0        0      177 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/const/README.md
+-rw-r--r--   0        0        0     1032 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/const/__init__.py
+-rw-r--r--   0        0        0     2598 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/const/base.py
+-rw-r--r--   0        0        0     1873 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/const/comms.py
+-rw-r--r--   0        0        0     1734 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/const/heartbeat.py
+-rw-r--r--   0        0        0      890 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/const/misc.py
+-rw-r--r--   0        0        0     2564 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/const/payload.py
+-rw-r--r--   0        0        0       49 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/default/__init__.py
+-rw-r--r--   0        0        0     5975 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/default/mqtt_session.py
+-rw-r--r--   0        0        0      761 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/io_formatter/__init__.py
+-rw-r--r--   0        0        0     1334 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/io_formatter/consts.py
+-rw-r--r--   0        0        0     3619 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/io_formatter/io_formatter_manager.py
+-rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/io_formatter/base/__init__.py
+-rw-r--r--   0        0        0     3423 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/io_formatter/base/base_formatter.py
+-rw-r--r--   0        0        0      696 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/io_formatter/default/__init__.py
+-rw-r--r--   0        0        0     1148 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/io_formatter/default/a_dummy.py
+-rw-r--r--   0        0        0    11753 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/io_formatter/default/cavi2.py
+-rw-r--r--   0        0        0       56 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/io_formatter/mixins/__init__.py
+-rw-r--r--   0        0        0     4810 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/io_formatter/mixins/plugins_manager_mixin.py
+-rw-r--r--   0        0        0       38 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/utils/__init__.py
+-rw-r--r--   0        0        0     1759 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/utils/code.py
+-rw-r--r--   0        0        0     1625 2020-02-02 00:00:00.000000 pye2-0.3.2/PyE2/utils/code_exec.py
+-rw-r--r--   0        0        0     3774 2020-02-02 00:00:00.000000 pye2-0.3.2/xperimental/attach_example.py
+-rw-r--r--   0        0        0     3350 2020-02-02 00:00:00.000000 pye2-0.3.2/xperimental/ex1.py
+-rw-r--r--   0        0        0      384 2020-02-02 00:00:00.000000 pye2-0.3.2/xperimental/hello.py
+-rw-r--r--   0        0        0     4182 2020-02-02 00:00:00.000000 pye2-0.3.2/xperimental/remote_exec.py
+-rw-r--r--   0        0        0      451 2020-02-02 00:00:00.000000 pye2-0.3.2/xperimental/_archive/test.py
+-rw-r--r--   0        0        0     1924 2020-02-02 00:00:00.000000 pye2-0.3.2/xperimental/decentralized/dedist_example.py
+-rw-r--r--   0        0        0     2300 2020-02-02 00:00:00.000000 pye2-0.3.2/xperimental/decentralized/dedist_example_initiator.py
+-rw-r--r--   0        0        0      276 2020-02-02 00:00:00.000000 pye2-0.3.2/xperimental/decentralized/dedist_example_worker.py
+-rw-r--r--   0        0        0     2457 2020-02-02 00:00:00.000000 pye2-0.3.2/.gitignore
+-rw-r--r--   0        0        0    11357 2020-02-02 00:00:00.000000 pye2-0.3.2/LICENSE
+-rw-r--r--   0        0        0     6094 2020-02-02 00:00:00.000000 pye2-0.3.2/README.md
+-rw-r--r--   0        0        0      760 2020-02-02 00:00:00.000000 pye2-0.3.2/pyproject.toml
+-rw-r--r--   0        0        0     6733 2020-02-02 00:00:00.000000 pye2-0.3.2/PKG-INFO
```

### Comparing `pye2-0.3.1/.github/workflows/python-publish.yml` & `pye2-0.3.2/.github/workflows/python-publish.yml`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/base/__init__.py` & `pye2-0.3.2/PyE2/base/__init__.py`

 * *Files 9% similar despite different names*

```diff
@@ -16,9 +16,10 @@
 @copyright: Lummetry.AI
 @author: Lummetry\.AI - Stefan Saraev
 @project: 
 @description:
 """
 
 from .generic_session import GenericSession
+from .logger import Logger
 from .payload import Payload
 from .pipeline import Pipeline
```

### Comparing `pye2-0.3.1/PyE2/base/generic_session.py` & `pye2-0.3.2/PyE2/base/tmpeb3hj3eh`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/base/pipeline.py` & `pye2-0.3.2/PyE2/base/pipeline.py`

 * *Files 3% similar despite different names*

```diff
@@ -14,20 +14,23 @@
 
 
 @copyright: Lummetry.AI
 @author: Lummetry\.AI - Stefan Saraev
 @project: 
 @description:
 """
-
+from time import time
 from ..utils.code_exec import code_to_base64
 
 
+WAIT_FOR_WORKER = 15
+
+
 class Pipeline(object):
-  def __init__(self, session, log, *, e2id, name, data_source, config={}, plugins, on_data, silent=False, on_notification=None, **kwargs) -> None:
+  def __init__(self, session, log, *, e2id, name, data_source, config={}, plugins, on_data, silent=True, on_notification=None, **kwargs) -> None:
     self.log = log
     self.session = session
     self.e2id = e2id
     self.name = name
     self.data_source = data_source
     self.config = config
     self.plugins = plugins
@@ -136,16 +139,17 @@
     )
 
     self._add_payload_instance_callback_to_session(
         signature, instance_id, on_data)
     if on_notification is not None:
       self._add_notification_instance_callback_to_session(
           signature, instance_id, on_notification)
-    self.P("Starting plugin {}:{} with params {}".format(
-        signature, instance_id, params))
+    self.P("Starting plugin {}:{}".format(
+        signature, instance_id))
+    self.D("with params {}".format(params))
     return "##".join([self.e2id, self.name, signature, instance_id])
 
   def stop_plugin_instance(self, signature, instance_id=None, /):
     """Stop a plugin instance from this pipeline. The function can accept either the signature and the instance_id of the desired instance,
     or the identifier returned from `start_plugin_instance` or `start_custom_instance` or `attach_to_instance` or `attach_to_custom_instance`.
 
     Args:
@@ -206,21 +210,22 @@
     Args:
         instance_id (str): name of the instance. There can be multiple instances of the same plugin, mostly with different prameters
         params (dict): parameters used to customize the functionality.
         on_data (Callable[[Pipeline, str, str, dict], None]): Callback that handles messages received from this instance. As arguments, it has a reference to this Pipeline object, along with the payload itself.
         plain_code (str, optional): A string containing the entire code that is to be executed remotely on an AiXp node. Defaults to None.
         plain_code_path (str, optional): A string containing the path to the code that is to be executed remotely on an AiXp node. Defaults to None.
         on_notification (Callable[[Pipeline, dict], None], optional): Callback that handles notifications received from this instance. As arguments, it has a reference to this Pipeline object, along with the payload itself. Defaults to None.
-  
+
     Raises:
         Exception: The code was not provided.
 
     Returns:
         str: An identifier for this instance, useful for stopping an instance.
     """
+
     def custom_exec_on_data(self, data):
       exec_data = None
       if "SB_IMPLEMENTATION" in data or "EE_FORMATTER" in data:
         exec_data = data.get('EXEC_RESULT', data.get('EXEC_INFO'))
         exec_error = data.get('EXEC_ERRORS', 'no keyword error')
       else:
         try:
@@ -276,15 +281,15 @@
     meaning it processes data from this pipelines data source. The code used for the custom instance must be provided either as a string, or as a path to a file. Parameters can be passed either in the params dict, or as kwargs.
     The REST-like custom plugin instance will execute only once. If one desires to execute a custom code periodically, use `start_custom_plugin`.
 
     Args:
         params (dict, optional): parameters used to customize the functionality. Defaults to {}.
         plain_code (str, optional): A string containing the entire code that is to be executed remotely on an AiXp node. Defaults to None.
         plain_code_path (str, optional): A string containing the path to the code that is to be executed remotely on an AiXp node. Defaults to None.
-  
+
     Raises:
         Exception: The code was not provided.
 
     Returns:
         Tuple[Any, Any]: a tuple containing the result of the execution and the error, if any. 
         If the execution completed succesfully, the `error` is None, and the `result` is the returned value of the custom code.
     """
@@ -344,15 +349,20 @@
     """
     # remove callbacks
     self.session.send_command_delete_pipeline(self.e2id, self.name)
     self.session.remove_pipeline_callbacks(self)
     return
 
   def P(self, *args, **kwargs):
-    """Print info to stdout if the session was created with the silent argument set to `False`. 
+    """Print info to stdout.
+    """
+    return self.log.P(*args, **kwargs)
+
+  def D(self, *args, **kwargs):
+    """Print debug info to stdout if the session was created with the silent argument set to `False`. 
     The silent argument is passed to the Pipeline object when creating it with `create_pipeline` or `attach_to_pipeline`.
     """
     if not self.silent:
       return self.log.P(*args, **kwargs)
 
   def attach_to_instance(self, signature, instance_id, on_data, on_notification=None):
     """Attach to an existing instance on this pipeline. 
@@ -388,7 +398,46 @@
             signature, instance_id, on_data)
         if on_notification is not None:
           self._add_notification_instance_callback_to_session(
               signature, instance_id, on_notification)
         return "##".join([self.e2id, self.name, signature, instance_id])
 
     raise Exception("Unable to attach to instance. Instance does not exist")
+
+  def attach_to_custom_instance(self, instance_id, on_data, on_notification=None):
+    """Attach to an existing custom execution instance on this pipeline. 
+    This method is useful when one wishes to attach an 
+    `on_data` and `on_notification` callbacks to said instance.
+
+    Args:
+        instance_id (str): name of the instance.
+        on_data (Callable[[Pipeline, str, str, dict], None]): Callback that handles messages received from this instance. As arguments, it has a reference to this Pipeline object, along with the payload itself.
+        on_notification (Callable[[Pipeline, dict], None], optional): Callback that handles notifications received from this instance. As arguments, it has a reference to this Pipeline object, along with the payload itself. Defaults to None.
+
+    Raises:
+        Exception: the pipeline does not contain plugins with a given signature or it does not contain the desired instance.
+
+    Returns:
+        str: An identifier for this instance, useful for stopping an instance.
+    """
+
+    def custom_exec_on_data(self, data):
+      exec_data = None
+      if "SB_IMPLEMENTATION" in data or "EE_FORMATTER" in data:
+        exec_data = data.get('EXEC_RESULT', data.get('EXEC_INFO'))
+        exec_error = data.get('EXEC_ERRORS', 'no keyword error')
+      else:
+        try:
+          exec_data = data['specificValue']['exec_result']
+        except Exception as e:
+          self.P(e, color='r')
+          self.P(data, color='r')
+        exec_error = data['specificValue']['exec_errors']
+
+      if exec_error is not None:
+        self.P("Error received from <CUSTOM_EXEC_01:{}>: {}".format(
+            instance_id, exec_error), color="r")
+      if exec_data is not None:
+        on_data(self, exec_data)
+      return
+
+    return self.attach_to_instance("CUSTOM_EXEC_01", instance_id, custom_exec_on_data, on_notification)
```

### Comparing `pye2-0.3.1/PyE2/base/tmpeb3hj3eh` & `pye2-0.3.2/PyE2/base/generic_session.py`

 * *Files 11% similar despite different names*

```diff
@@ -15,154 +15,22 @@
 
 @copyright: Lummetry.AI
 @author: Lummetry\.AI - Stefan Saraev
 @project: 
 @description:
 """
 
-import os
-import sys
-import traceback
-from time import localtime, mktime, strftime, strptime, sleep
+from time import sleep
 from time import time as tm
 
 from ..const import comms as comm_ct
-from .pipeline import Pipeline
-from .payload import Payload
 from ..io_formatter import IOFormatterManager
-
-
-class Logger():
-  def __init__(self, **kwargs) -> None:
-    return
-
-  def P(self, msg, **kwargs):
-    print(msg)
-
-  def get_unique_id(self, size=8):
-    """
-    efficient and low-colision function for small unique id generation
-    """
-    import random
-    import string
-    alphabet = string.ascii_lowercase + string.digits
-    uid = ''.join(random.choices(alphabet, k=size))
-    return uid
-
-  def start_timer(self, *args, **kwargs):
-    return
-
-  def end_timer(self, *args, **kwargs):
-    return
-
-  def stop_timer(self, *args, **kwargs):
-    return
-
-  def time_to_str(self, t=None, fmt='%Y-%m-%d %H:%M:%S'):
-    if t is None:
-      t = tm()
-    return strftime(fmt, localtime(t))
-
-  def get_error_info(self, return_err_val=False):
-    """
-    Returns error_type, file, method, line for last error if available
-
-    Parameters
-    ----------
-    return_err_val: boolean, optional
-      Whether the method returns or not the error message (err_val)
-
-    Returns
-    -------
-    if not return_err_val:
-      (tuple) str, str, str, str : errortype, file, method, line
-    else:
-      (tuple) str, str, str, str, str : errortype, file, method, line, err message
-    """
-    err_type, err_val, err_trace = sys.exc_info()
-    if False:
-      # dont try this at home :) if you want to pickle a logger instance after
-      # `get_error_info` was triggered, then it won't work because `self._last_extracted_error`
-      # contain an object of type `traceback` and tracebacks cannot be pickled
-      self._last_extracted_error = err_type, err_val, err_trace
-    # endif
-    if err_type is not None:
-      str_err = err_type.__name__
-      stack_summary = traceback.extract_tb(err_trace)
-      last_error_frame = stack_summary[-1]
-      fn = os.path.splitext(os.path.split(last_error_frame.filename)[-1])[0]
-      lineno = last_error_frame.lineno
-      func_name = last_error_frame.name
-      if not return_err_val:
-        return str_err, 'File: ' + fn, 'Func: ' + func_name, 'Line: ' + str(lineno)
-      else:
-        return str_err, 'File: ' + fn, 'Func: ' + func_name, 'Line: ' + str(lineno), str(err_val)
-    else:
-      return "", "", "", "", ""
-
-  def dict_pretty_format(self, d, indent=4, as_str=True, display_callback=None, display=False, limit_str=250):
-    assert isinstance(d, dict), "`d` must be dict"
-    if display and display_callback is None:
-      display_callback = self.P
-    lst_data = []
-
-    def deep_parse(dct, ind=indent):
-      for ki, key in enumerate(dct):
-        # dct actually can be dict or list
-        str_key = str(key) if not isinstance(key, str) else '"{}"'.format(key)
-        if isinstance(dct, dict):
-          value = dct[key]
-          lst_data.append(' ' * ind + str(str_key) + ' : ')
-        else:
-          value = key
-        if isinstance(value, dict):
-          if lst_data[-1][-1] in ['[', ',']:
-            lst_data.append(' ' * ind + '{')
-          else:
-            lst_data[-1] = lst_data[-1] + '{'
-          deep_parse(value, ind=ind + indent)
-          lst_data.append(' ' * ind + '}')
-        elif isinstance(value, list) and len(value) > 0 and isinstance(value[0], dict):
-          lst_data[-1] = lst_data[-1] + '['
-          deep_parse(value, ind=ind + indent)
-          lst_data.append(' ' * ind + ']')
-        else:
-          str_value = str(value) if not isinstance(value, str) else '"{}"'.format(value)
-          if isinstance(value, str) and len(str_value) > limit_str:
-            str_value = str_value[:limit_str]
-          lst_data[-1] = lst_data[-1] + str_value
-
-        if ki < (len(dct) - 1):
-          lst_data[-1] = lst_data[-1] + ','
-      return
-
-    deep_parse(dct=d, ind=0)
-
-    displaybuff = "{\n"
-    for itm in lst_data:
-      displaybuff += '  ' + itm + '\n'
-    displaybuff += "}"
-
-    if display_callback is not None:
-      displaybuff = "Dict pretty formatter:\n" + displaybuff
-      display_callback(displaybuff)
-    if as_str:
-      return displaybuff
-    else:
-      return lst_data
-
-  def camel_to_snake(self, s):
-    import re
-    if s.isupper():
-      result = s.lower()
-    else:
-      s = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
-      s = s.replace('__', '_')
-      result = s
-    return result
+from .logger import Logger
+from .payload import Payload
+from .pipeline import Pipeline
 
 
 class GenericSession(object):
   default_config = {
       "CONFIG_CHANNEL": {
           "TOPIC": "lummetry/{}/config"
       },
@@ -174,28 +42,28 @@
       },
       "PAYLOADS_CHANNEL": {
           "TOPIC": "lummetry/payloads"
       },
       "QOS": 0
   }
 
-  def __init__(self, *, host, port, user, pwd, name='pySDK', config={}, log=None, on_notification=None, on_heartbeat=None, silent=False, **kwargs) -> None:
+  def __init__(self, *, host, port, user, pwd, name='pySDK', config={}, log=None, on_notification=None, on_heartbeat=None, silent=True, **kwargs) -> None:
     """Create a session object that allows to connect to a communication server and to interact with nodes from the AiXp network.
 
     Args:
         host (str): Hostname of the server
         port (int): port
         user (str): username
         pwd (str): password
         name (str, optional): Will be used as `SESSION_ID` when communicating with AiXp nodes. Defaults to 'pySDK'.
         config (dict, optional): Configures the names of the channels this session will connect to. Defaults to {}.
         log (Logger, optional): instance of a Logger class that provides utility functions and prettier logs. Useful for Hyperfy devs. Defaults to None.
         on_notification (Callable[[Session, dict], None], optional): Callback that handles the notification received by this session. Defaults to None.
         on_heartbeat (Callable[[Session, dict], None], optional): Callback that handles the heartbeat received by this session. Defaults to None.
-        silent (bool, optional): This flag controlls if the `.P` method dumps text to the stdout. Defaults to False.
+        silent (bool, optional): This flag controlls if the `.D` method dumps text to the stdout. Defaults to True.
     """
     if log is None:
       log = Logger()
 
     super(GenericSession, self).__init__()
 
     self.silent = silent
@@ -220,14 +88,16 @@
     self.notification_instance_callbacks = []
 
     self.payload_pipeline_callbacks = []
     self.notification_pipeline_callbacks = []
     self.heartbeat_pipeline_callbacks = []
     self.own_pipelines = []
 
+    self.connected = False
+
     self.formatter_wrapper = IOFormatterManager(log)
 
     return
 
   @property
   def server(self):
     return self._config[comm_ct.HOST]
@@ -258,15 +128,15 @@
 
   def _on_heartbeat_default(self, dict_msg: dict):
     msg_eeid = dict_msg['EE_ID']
     msg_active_configs = dict_msg['CONFIG_STREAMS']
 
     # default action
     # TODO: print stuff
-    self.P("Received hb from: {}".format(msg_eeid))
+    self.D("Received hb from: {}".format(msg_eeid))
     self._online_boxes[msg_eeid] = {
         config['NAME']: config for config in msg_active_configs}
 
     # call the pipeline defined callbacks, if any
     for pipeline, callback in self.heartbeat_pipeline_callbacks:
       if msg_eeid == pipeline.e2id:
         callback(pipeline, dict_msg)
@@ -293,15 +163,15 @@
       self.custom_on_notification(self, dict_msg)
 
     # call default action on notif
     # TODO: maybe print stuff
     color = None
     if notification_type != "NORMAL":
       color = 'r'
-    self.P("Received notification {} from <{}/{}>: {}".format(notification_type,
+    self.D("Received notification {} from <{}/{}>: {}".format(notification_type,
            msg_eeid, msg_stream, notification), color=color)
 
     return
 
   # TODO: maybe convert dict_msg to Payload object
   #       also maybe strip the dict from useless info for the user of the sdk
   #       Add try-except + sleep
@@ -360,72 +230,92 @@
   def send_command_delete_pipeline(self, worker, stream_name):
     self._send_command_to_box('ARCHIVE_CONFIG', worker, stream_name)
 
   def _send_payload(self, to, payload):
     raise NotImplementedError
 
   def P(self, *args, **kwargs):
-    """Print info to stdout if the session was created with the silent argument set to `False`
+    """Print info to stdout
+    """
+    self.log.P(*args, **kwargs)
+
+  def D(self, *args, **kwargs):
+    """Print debug info to stdout if the session was created with the silent argument set to `False`
     """
     if not self.silent:
       self.log.P(*args, **kwargs)
+    return
 
   def connect(self) -> None:
     """Connect to the communication server using the credentials provided when creating this instance
     """
     raise NotImplementedError
 
-  def create_pipeline(self, *, e2id, name, data_source, config={}, plugins=[], on_data, on_notification=None, **kwargs) -> Pipeline:
+  def create_pipeline(self, *, e2id, name, data_source, config={}, plugins=[], on_data, on_notification=None, max_wait_time=0, **kwargs) -> Pipeline:
     """Create a new pipeline on a box. A pipeline is the equivalent of the "config file" used by the Hyperfy dev team internaly.
     A pipeline allows one to define what is the data acquisition type and source, and what plugins will run on that data.
+    `max_wait_time` controls how much to wait for the given node to be indexed by the session before creating the pipeline.
+    A node is indexed if it sent any heartbeats since the session connected.
 
     Args:
         e2id (str): Name of the AiXp node.
         name (str): Name of the pipeline. This is good to be kept unique, as it allows multiple parties to overwrite each others configurations.
         data_source (str): Name of the DataCaptureThread plugin to be used for acquisition.
         on_data (Callable[[Pipeline, str, str, dict], None]): Callback that handles messages received from this pipeline. As arguments, it has a reference to this Pipeline object, the name of the Signature and the name of the Instance that sent the message, along with the payload itself.
         plugins (list): List of dictionaries which contain the configurations of each plugin instance that is desired to run on the box. Defaults to []. Should be left [], and instances should be created with the api.
         config (dict, optional): Data acquisition specific parameters. Defaults to {}.
         on_notification (Callable[[Pipeline, dict], None], optional): Callback that handles notifications received from this pipeline. As arguments, it has a reference to this Pipeline object, along with the payload itself. Defaults to None.
-
+        max_wait_time(float, optional): Max wait time before creating the pipeline. Defaults to 0.
     Returns:
         Pipeline: a Pipeline object which can be used to control plugin instances.
     """
+    _start = tm()
+    found = False
+    while (tm() - _start) < max_wait_time:
+      avail_workers = self.get_active_nodes()
+      if e2id in avail_workers:
+        found = True
+        break
+      sleep(0.1)
+
+    if not found:
+      self.P("WARNING: could not find worker '{}' in {:.1f}s. The job may not have a valid active worker.".format(
+          self.e2id, tm() - _start
+      ), color='r')
     pipeline = Pipeline(
-      self,
-      self.log,
-      e2id=e2id,
-      name=name,
-      data_source=data_source,
-      config=config,
-      plugins=plugins,
-      on_data=on_data,
-      on_notification=on_notification,
-      silent=self.silent,
-      **kwargs
-     )
+        self,
+        self.log,
+        e2id=e2id,
+        name=name,
+        data_source=data_source,
+        config=config,
+        plugins=plugins,
+        on_data=on_data,
+        on_notification=on_notification,
+        silent=self.silent,
+        **kwargs
+    )
     self.own_pipelines.append(pipeline)
     return pipeline
-  
-  
+
   def close_own_pipelines(self):
     # iterate through all CREATED pipelines from this session and close them
     for pipeline in self.own_pipelines:
-      pipeline.close()    
+      pipeline.close()
     return
 
   def close(self, close_pipelines=False, **kwargs):
     """Close the session, releasing all resources and closing all threads
     """
     # TODO: Stefan: here we need to change from abstract to concrete - all pipelines MUST
     #       be deallocated. The child re-implementations must call self().__close__ beforehand
     if close_pipelines:
       self.close_own_pipelines()
     return
-  
+
   def get_active_nodes(self):
     """Get the list of all AiXp nodes that sent a message since this session was created, and that are considered online
 
     Returns:
         list: List of names of all the AiXp nodes that are considered online
     """
     return list(self._online_boxes.keys())
@@ -437,62 +327,82 @@
         e2id (str): name of the AiXp node
 
     Returns:
         dict: The key is the name of the pipeline, and the value is the entire config dictionary of that pipeline.
     """
     return self._online_boxes.get(e2id, None)
 
-  def attach_to_pipeline(self, e2id, pipeline_name, on_data, on_notification=None, **kwargs) -> Pipeline:
+  def attach_to_pipeline(self, e2id, pipeline_name, on_data, on_notification=None, max_wait_time=0, **kwargs) -> Pipeline:
     """Create a Pipeline object and attach to an existing pipeline on a box.
     Useful when one wants to treat an existing pipeline as one of his own, 
     or when one wants to attach callbacks to various events (on_data, on_notification). 
+    `max_wait_time` controls how much to wait for the given node to be indexed by the session before attaching to the pipeline.
+    A node is indexed if it sent any heartbeats since the session connected.
 
     Args:
         e2id (str): Name of the AiXp node.
         pipeline_name (str): Name of the pipeline
         on_data (Callable[[Pipeline, str, str, dict], None]): Callback that handles messages received from this pipeline. As arguments, it has a reference to this Pipeline object, the name of the Signature and the name of the Instance that sent the message, along with the payload itself.
         on_notification (Callable[[Pipeline, dict], None], optional): Callback that handles notifications received from this pipeline. As arguments, it has a reference to this Pipeline object, along with the payload itself. Defaults to None.
+        max_wait_time(float, optional): Max wait time before creating the pipeline. Defaults to 0.
 
     Raises:
         Exception: The session does not consider the node online or the pipeline does not exist on that box.
 
     Returns:
         Pipeline: a Pipeline object which can be used to control plugin instances.
     """
+    _start = tm()
+    while (tm() - _start) < max_wait_time:
+      avail_workers = self.get_active_nodes()
+      if e2id in avail_workers:
+        break
+      sleep(0.1)
+
     if e2id not in self._online_boxes:
       raise Exception("Unable to attach to pipeline. Node does not exist")
 
     if pipeline_name not in self._online_boxes[e2id]:
       raise Exception("Unable to attach to pipeline. Pipeline does not exist")
 
     pipeline_config = {
         k.lower(): v for k, v in self._online_boxes[e2id][pipeline_name].items()}
     data_source = pipeline_config['type']
     return Pipeline(self, self.log, e2id=e2id, config={}, data_source=data_source, create_pipeline=False, silent=self.silent, on_data=on_data, on_notification=on_notification, **pipeline_config, **kwargs)
-  
-  
-  def wait_until_sigint(self, close_session=True, close_pipelines=False):
+
+  def run(self, wait=True, close_session=True, close_pipelines=False):
     """
-    This simple method will lock the main thread in a loop until a SIGINT signal is received
+    This simple method will lock the main thread in a loop.
+    This method can call `self.connect()`.
+    This method can close the session and can close all pipelines when doing so.
 
     Parameters
     ----------
+    wait: bool, float
+      If `True`, will wait forever.
+      If `False`, will not wait at all
+      If type `float`, will wait said amount of seconds
+
     close_session : bool, optional
       If `True` will close the session when the loop is exited. The default is True.
 
     close_pipelines : bool, optional
       If `True` will close all pipelines initiated by this session when the loop is exited. The default is True.
 
     Returns
     -------
     None.
 
     """
+    if not self.connected:
+      self.connect()
+
+    _start_timer = tm()
     try:
-      while True:
+      while (isinstance(wait, bool) and wait) or (tm() - _start_timer) < wait:
         sleep(0.1)
     except KeyboardInterrupt:
       self.P("CTRL+C detected. Stopping loop.", color='r')
-      
+
     if close_session:
       self.close(close_pipelines=close_pipelines)
     return
```

### Comparing `pye2-0.3.1/PyE2/base/payload/payload.py` & `pye2-0.3.2/PyE2/base/payload/payload.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/comm/__init__.py` & `pye2-0.3.2/PyE2/comm/__init__.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/comm/amqp_wrapper.py` & `pye2-0.3.2/PyE2/comm/amqp_wrapper.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/comm/mqtt_wrapper.py` & `pye2-0.3.2/PyE2/comm/mqtt_wrapper.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/const/__init__.py` & `pye2-0.3.2/PyE2/const/__init__.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/const/base.py` & `pye2-0.3.2/PyE2/const/base.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/const/comms.py` & `pye2-0.3.2/PyE2/const/comms.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/const/heartbeat.py` & `pye2-0.3.2/PyE2/const/heartbeat.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/const/misc.py` & `pye2-0.3.2/PyE2/const/misc.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/const/payload.py` & `pye2-0.3.2/PyE2/const/payload.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/default/mqtt_session.py` & `pye2-0.3.2/PyE2/default/mqtt_session.py`

 * *Files 6% similar despite different names*

```diff
@@ -29,15 +29,16 @@
 from ..base import GenericSession
 
 
 # TODO: implement send_command, send_payload,
 #       to be used by the Pipeline class
 class MqttSession(GenericSession):
   def __init__(self, *, host, port, user, pwd, name='pySDK', config={}, log=None, on_notification=None, on_heartbeat=None, silent=False, **kwargs) -> None:
-    super(MqttSession, self).__init__(host=host, port=port, user=user, pwd=pwd, name=name, config=config, log=log, on_notification=on_notification, on_heartbeat=on_heartbeat, silent=silent, **kwargs)
+    super(MqttSession, self).__init__(host=host, port=port, user=user, pwd=pwd, name=name, config=config,
+                                      log=log, on_notification=on_notification, on_heartbeat=on_heartbeat, silent=silent, **kwargs)
 
     self._payload_messages = deque()
     self._default_communicator = MQTTWrapper(
         log=self.log,
         config=self._config,
         send_channel_name=comm_ct.COMMUNICATION_CONFIG_CHANNEL,
         recv_channel_name=comm_ct.COMMUNICATION_PAYLOADS_CHANNEL,
@@ -62,52 +63,52 @@
         config=self._config,
         recv_channel_name=comm_ct.COMMUNICATION_NOTIF_CHANNEL,
         comm_type=comm_ct.COMMUNICATION_NOTIFICATIONS,
         recv_buff=self._notif_messages
         # on_message=self._on_notification_default_mqtt_callback
     )
 
-    self.running = False
+    self._running = False
 
     self._payload_thread = Thread(target=self._handle_payloads, args=())
     self._notif_thread = Thread(target=self._handle_notifs, args=())
     self._hb_thread = Thread(target=self._handle_hbs, args=())
 
     return
 
   def _handle_payloads(self):
-    while self.running:
+    while self._running:
       if len(self._payload_messages) == 0:
         sleep(0.01)
         continue
       current_msg = self._payload_messages.popleft()
       self._on_payload_default_mqtt_callback(current_msg)
     # end while self.running
 
     while len(self._payload_messages) > 0:
       current_msg = self._payload_messages.popleft()
       self._on_payload_default_mqtt_callback(current_msg)
     return
 
   def _handle_notifs(self):
-    while self.running:
+    while self._running:
       if len(self._notif_messages) == 0:
         sleep(0.01)
         continue
       current_msg = self._notif_messages.popleft()
       self._on_notification_default_mqtt_callback(current_msg)
     # end while self.running
 
     while len(self._notif_messages) > 0:
       current_msg = self._notif_messages.popleft()
       self._on_notification_default_mqtt_callback(current_msg)
     return
 
   def _handle_hbs(self):
-    while self.running:
+    while self._running:
       if len(self._hb_messages) == 0:
         sleep(0.01)
         continue
       current_msg = self._hb_messages.popleft()
       self._on_heartbeat_default_mqtt_callback(current_msg)
     # end while self.running
 
@@ -140,31 +141,39 @@
 
     self._heartbeats_communicator.server_connect()
     self._heartbeats_communicator.subscribe()
 
     self._notifications_communicator.server_connect()
     self._notifications_communicator.subscribe()
 
-    self.running = True
+    self._running = True
+    self._payload_thread.setDaemon(True)
     self._payload_thread.start()
+    self._notif_thread.setDaemon(True)
     self._notif_thread.start()
+    self._hb_thread.setDaemon(True)
     self._hb_thread.start()
 
+    self.connected = True
+
     return
 
   def close(self, close_pipelines=False, **kwargs):
     super(MqttSession, self).close(close_pipelines=close_pipelines, **kwargs)
-    
+
     self._default_communicator.release()
     self._heartbeats_communicator.release()
     self._notifications_communicator.release()
-    self.running = False
+    self._running = False
     self._payload_thread.join()
     self._notif_thread.join()
     self._hb_thread.join()
+    self.connected = False
+
+    return
 
   def _send_payload(self, to, msg):
     payload = json.dumps(msg)
 
     self._default_communicator._send_to = to
     self._default_communicator.send(payload)
     return
```

### Comparing `pye2-0.3.1/PyE2/io_formatter/__init__.py` & `pye2-0.3.2/PyE2/io_formatter/__init__.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/io_formatter/consts.py` & `pye2-0.3.2/PyE2/io_formatter/consts.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/io_formatter/io_formatter_manager.py` & `pye2-0.3.2/PyE2/io_formatter/io_formatter_manager.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/io_formatter/base/__init__.py` & `pye2-0.3.2/PyE2/io_formatter/base/__init__.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/io_formatter/base/base_formatter.py` & `pye2-0.3.2/PyE2/io_formatter/base/base_formatter.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/io_formatter/default/__init__.py` & `pye2-0.3.2/PyE2/io_formatter/default/__init__.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/io_formatter/default/a_dummy.py` & `pye2-0.3.2/PyE2/io_formatter/default/a_dummy.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/io_formatter/default/cavi2.py` & `pye2-0.3.2/PyE2/io_formatter/default/cavi2.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/io_formatter/mixins/plugins_manager_mixin.py` & `pye2-0.3.2/PyE2/io_formatter/mixins/plugins_manager_mixin.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/utils/code.py` & `pye2-0.3.2/PyE2/utils/code.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/PyE2/utils/code_exec.py` & `pye2-0.3.2/PyE2/utils/code_exec.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/xperimental/custom_exec_tutorial.py` & `pye2-0.3.2/xperimental/remote_exec.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/xperimental/dedist_example.py` & `pye2-0.3.2/xperimental/decentralized/dedist_example.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 
+import os
 from PyE2 import Session, code_to_base64
 
 SERVER_CONFIG = {
     'host': "jenkinsx.globalintelligence.ro",
     'port': 31083,
     'user': "coreaixp",
     'pwd': "s3cret-passw0rd"
@@ -13,28 +14,31 @@
   print(data)
   return
 
 
 def pipeline_on_data(pipeline, signature, instance, data):
   pass
 
+
 if __name__ == '__main__':
-  
-  WORKER_CODE_PATH = 'xperimental/dedist_example_worker.py'
-  INITIATOR_CODE_PATH = 'xperimental/dedist_example_initiator.py'
+  folder = os.path.split(__file__)[0]  
+  WORKER_CODE_PATH = os.path.join(folder, 'dedist_example_worker.py')
+  INITIATOR_CODE_PATH = os.path.join(folder, 'dedist_example_initiator.py')
   
   with open(WORKER_CODE_PATH, 'rt') as fh:
     worker_code = fh.read()
     
-  e2id = 'stefan-box' # provide a known EE id
-  sess = Session(**SERVER_CONFIG, silent=True)
+  e2id = 'E2dkr-0339' # provide a known EE id
+  sess = Session(**SERVER_CONFIG, silent=False)
   sess.connect()
   
-  listener_params = {k.upper(): v for k, v in SERVER_CONFIG.items()}
-  listener_params["PASS"] = listener_params["PWD"]
+  listener_params = {
+    **SERVER_CONFIG
+  }
+  listener_params["PASS"] = listener_params["pwd"]
   listener_params["TOPIC"] = "lummetry/payloads"
   
   pipeline = sess.create_pipeline(
       e2id=e2id,
       name='test_dist_jobs',
       # data_source='Void',
       # config={},
@@ -59,11 +63,11 @@
         # this will be used within plugin as `plugin.cfg_worker_code`
         'WORKER_CODE': code_to_base64(worker_code) 
         },
       on_data=instance_on_data,
       process_delay=0.2
   )
   
-  sess.wait_until_sigint(close_session=True, close_pipelines=True)
+  sess.run(wait=True, close_session=True, close_pipelines=True)
```

### Comparing `pye2-0.3.1/xperimental/dedist_example_initiator.py` & `pye2-0.3.2/xperimental/decentralized/dedist_example_initiator.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/xperimental/ex1.py` & `pye2-0.3.2/xperimental/ex1.py`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/.gitignore` & `pye2-0.3.2/.gitignore`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/LICENSE` & `pye2-0.3.2/LICENSE`

 * *Files identical despite different names*

### Comparing `pye2-0.3.1/README.md` & `pye2-0.3.2/README.md`

 * *Files 15% similar despite different names*

```diff
@@ -10,24 +10,37 @@
 ## Quick start "Hello world!"
 
 Below is a simple "Hello world!" style application that creates a session by connecting to a known communication broker, listens for processing nodes heartbeats and displays the basic compute capabilities of the discovered nodes such as CPU & RAM.
 
 ### Importing and configuration
 
 ```
+from PyE2 import Session
 ```
 
 ### Preparing callbacks
 
 ```
+def on_hb(session, data):
+  print(data['EE_ID'], " has a ", data['CPU'])
+  return
 ```
 
 ### Running a simple main loop
 
 ```
+if __name__ == '__main__':
+  sess = Session(
+    host='jenkinsx.globalintelligence.ro',
+    port=31083,
+    user='aixpanduser',
+    pwd='ReDeN2023',
+    on_heartbeat=on_hb
+  )
+  sess.run(wait=10)
 ```
 
 ## Advanced quick-start with decentralized distributed jobs
 
 For a more advanced quick-start we are going to create a execution pipeline on a target processing node that will request a specific number of workers in the network (including itself) to run a brute prime number search job.
 The initiator job itself will create the request for the required number of discovered worker peers then will listen for results. Finally after a given configurable amount of time will close its own execution pipeline as well as each worker pipeline.
```

### Comparing `pye2-0.3.1/pyproject.toml` & `pye2-0.3.2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling", "pika", "paho-mqtt"]
 build-backend = "hatchling.build"
 
 [project]
 name = "PyE2"
-version = "0.3.1"
+version = "0.3.2"
 authors = [
   { name="Stefan Saraev", email="stefan.saraev@global-technical.com" },
   { name="Cristan Bleotiu", email="cristan.bleotiu@global-technical.com" },
   { name="Andrei Ionut Damian", email="andrei.damian@lummetry.ai" },
 ]
 description = "PyE2 is an SDK used to communicate with the AiXpand network"
 readme = "README.md"
```

### Comparing `pye2-0.3.1/PKG-INFO` & `pye2-0.3.2/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PyE2
-Version: 0.3.1
+Version: 0.3.2
 Summary: PyE2 is an SDK used to communicate with the AiXpand network
 Project-URL: Homepage, https://github.com/AiXpand/PyE2
 Project-URL: Bug Tracker, https://github.com/AiXpand/PyE2/issues
 Author-email: Stefan Saraev <stefan.saraev@global-technical.com>, Cristan Bleotiu <cristan.bleotiu@global-technical.com>, Andrei Ionut Damian <andrei.damian@lummetry.ai>
 License-File: LICENSE
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
@@ -24,24 +24,37 @@
 ## Quick start "Hello world!"
 
 Below is a simple "Hello world!" style application that creates a session by connecting to a known communication broker, listens for processing nodes heartbeats and displays the basic compute capabilities of the discovered nodes such as CPU & RAM.
 
 ### Importing and configuration
 
 ```
+from PyE2 import Session
 ```
 
 ### Preparing callbacks
 
 ```
+def on_hb(session, data):
+  print(data['EE_ID'], " has a ", data['CPU'])
+  return
 ```
 
 ### Running a simple main loop
 
 ```
+if __name__ == '__main__':
+  sess = Session(
+    host='jenkinsx.globalintelligence.ro',
+    port=31083,
+    user='aixpanduser',
+    pwd='ReDeN2023',
+    on_heartbeat=on_hb
+  )
+  sess.run(wait=10)
 ```
 
 ## Advanced quick-start with decentralized distributed jobs
 
 For a more advanced quick-start we are going to create a execution pipeline on a target processing node that will request a specific number of workers in the network (including itself) to run a brute prime number search job.
 The initiator job itself will create the request for the required number of discovered worker peers then will listen for results. Finally after a given configurable amount of time will close its own execution pipeline as well as each worker pipeline.
```

