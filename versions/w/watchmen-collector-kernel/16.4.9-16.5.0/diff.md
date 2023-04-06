# Comparing `tmp/watchmen_collector_kernel-16.4.9.tar.gz` & `tmp/watchmen_collector_kernel-16.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_collector_kernel-16.4.9.tar", max compression
+gzip compressed data, was "watchmen_collector_kernel-16.5.0.tar", max compression
```

## Comparing `watchmen_collector_kernel-16.4.9.tar` & `watchmen_collector_kernel-16.5.0.tar`

### file list

```diff
@@ -1,38 +1,44 @@
--rw-r--r--   0        0        0     1061 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/LICENSE
--rw-r--r--   0        0        0     1179 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/pyproject.toml
--rw-r--r--   0        0        0        0 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/__init__.py
--rw-r--r--   0        0        0      175 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/common/__init__.py
--rw-r--r--   0        0        0      302 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/common/constants.py
--rw-r--r--   0        0        0      542 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/__init__.py
--rw-r--r--   0        0        0      495 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/change_data_json.py
--rw-r--r--   0        0        0      330 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/change_data_record.py
--rw-r--r--   0        0        0      288 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/collector_model_config.py
--rw-r--r--   0        0        0     2143 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/collector_table_config.py
--rw-r--r--   0        0        0      264 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/competitive_lock.py
--rw-r--r--   0        0        0     1942 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/condition.py
--rw-r--r--   0        0        0      674 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/scheduled_task.py
--rw-r--r--   0        0        0      251 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/trigger_event.py
--rw-r--r--   0        0        0      175 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/trigger_model.py
--rw-r--r--   0        0        0      229 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/trigger_table.py
--rw-r--r--   0        0        0      426 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/__init__.py
--rw-r--r--   0        0        0     2360 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/criteria_builder.py
--rw-r--r--   0        0        0     2873 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/data_capture.py
--rw-r--r--   0        0        0     2928 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/extract_source.py
--rw-r--r--   0        0        0     2452 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/extract_utils.py
--rw-r--r--   0        0        0      965 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/lock_clean.py
--rw-r--r--   0        0        0      842 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/lock_helper.py
--rw-r--r--   0        0        0     1673 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/task_housekeeping.py
--rw-r--r--   0        0        0     3050 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/task_service.py
--rw-r--r--   0        0        0     6790 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/trigger_collector.py
--rw-r--r--   0        0        0      832 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/__init__.py
--rw-r--r--   0        0        0     7536 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/change_data_json_service.py
--rw-r--r--   0        0        0     7463 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/change_data_record_service.py
--rw-r--r--   0        0        0     3830 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/collector_model_config_service.py
--rw-r--r--   0        0        0     5659 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/collector_table_config_service.py
--rw-r--r--   0        0        0     2534 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/competitive_lock_service.py
--rw-r--r--   0        0        0     5376 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/scheduled_task_service.py
--rw-r--r--   0        0        0     3099 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/trigger_event_service.py
--rw-r--r--   0        0        0     3219 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/trigger_model_service.py
--rw-r--r--   0        0        0     3779 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/trigger_table_service.py
--rw-r--r--   0        0        0     1254 1970-01-01 00:00:00.000000 watchmen_collector_kernel-16.4.9/setup.py
--rw-r--r--   0        0        0     1135 1970-01-01 00:00:00.000000 watchmen_collector_kernel-16.4.9/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-04-06 09:13:10.376010 watchmen_collector_kernel-16.5.0/LICENSE
+-rw-r--r--   0        0        0     1197 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/__init__.py
+-rw-r--r--   0        0        0      263 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/common/__init__.py
+-rw-r--r--   0        0        0      302 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/common/constants.py
+-rw-r--r--   0        0        0      697 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/common/settings.py
+-rw-r--r--   0        0        0      666 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/__init__.py
+-rw-r--r--   0        0        0      495 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/change_data_json.py
+-rw-r--r--   0        0        0       99 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/change_data_json_history.py
+-rw-r--r--   0        0        0      330 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/change_data_record.py
+-rw-r--r--   0        0        0      106 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/change_data_record_history.py
+-rw-r--r--   0        0        0      288 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/collector_model_config.py
+-rw-r--r--   0        0        0     2143 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/collector_table_config.py
+-rw-r--r--   0        0        0      264 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/competitive_lock.py
+-rw-r--r--   0        0        0     1942 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/condition.py
+-rw-r--r--   0        0        0     1362 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/scheduled_task.py
+-rw-r--r--   0        0        0       93 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/scheduled_task_history.py
+-rw-r--r--   0        0        0      251 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/trigger_event.py
+-rw-r--r--   0        0        0      175 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/trigger_model.py
+-rw-r--r--   0        0        0      229 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/trigger_table.py
+-rw-r--r--   0        0        0      426 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/__init__.py
+-rw-r--r--   0        0        0     2360 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/criteria_builder.py
+-rw-r--r--   0        0        0     2873 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/data_capture.py
+-rw-r--r--   0        0        0     2928 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/extract_source.py
+-rw-r--r--   0        0        0     2452 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/extract_utils.py
+-rw-r--r--   0        0        0     1142 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/lock_clean.py
+-rw-r--r--   0        0        0      842 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/lock_helper.py
+-rw-r--r--   0        0        0     1673 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/task_housekeeping.py
+-rw-r--r--   0        0        0     3634 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/task_service.py
+-rw-r--r--   0        0        0     6790 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/trigger_collector.py
+-rw-r--r--   0        0        0     1173 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/__init__.py
+-rw-r--r--   0        0        0     1774 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/change_data_json_history_service.py
+-rw-r--r--   0        0        0     8464 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/change_data_json_service.py
+-rw-r--r--   0        0        0     1845 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/change_data_record_history_service.py
+-rw-r--r--   0        0        0     7953 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/change_data_record_service.py
+-rw-r--r--   0        0        0     3830 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/collector_model_config_service.py
+-rw-r--r--   0        0        0     5659 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/collector_table_config_service.py
+-rw-r--r--   0        0        0     2534 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/competitive_lock_service.py
+-rw-r--r--   0        0        0     1586 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/scheduled_task_history_service.py
+-rw-r--r--   0        0        0     6825 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/scheduled_task_service.py
+-rw-r--r--   0        0        0     3099 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/trigger_event_service.py
+-rw-r--r--   0        0        0     3219 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/trigger_model_service.py
+-rw-r--r--   0        0        0     3779 2023-04-06 09:13:10.380010 watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/trigger_table_service.py
+-rw-r--r--   0        0        0     1174 1970-01-01 00:00:00.000000 watchmen_collector_kernel-16.5.0/PKG-INFO
```

### Comparing `watchmen_collector_kernel-16.4.9/LICENSE` & `watchmen_collector_kernel-16.5.0/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/pyproject.toml` & `watchmen_collector_kernel-16.5.0/pyproject.toml`

 * *Files 17% similar despite different names*

```diff
@@ -1,27 +1,28 @@
 [tool.poetry]
 name = "watchmen-collector-kernel"
-version = "16.4.9"
+version = "16.5.0"
 description = ""
 authors = ["botlikes <75356972+botlikes456@users.noreply.github.com>"]
 license = "MIT"
 packages = [
     { include = "watchmen_collector_kernel", from = "src" }
 ]
 
 [tool.poetry.dependencies]
 python = "^3.9"
-watchmen-data-kernel = "16.4.9"
-watchmen-storage-mysql = { version = "16.4.9", optional = true }
-watchmen-storage-oracle = { version = "16.4.9", optional = true }
-watchmen-storage-mongodb = { version = "16.4.9", optional = true }
-watchmen-storage-mssql = { version = "16.4.9", optional = true }
-watchmen-storage-postgresql = { version = "16.4.9", optional = true }
-watchmen-storage-oss = { version = "16.4.9", optional = true }
-watchmen-storage-s3 = { version = "16.4.9", optional = true }
+numpy = "^1.23.3"
+watchmen-data-kernel = "16.5.0"
+watchmen-storage-mysql = { version = "16.5.0", optional = true }
+watchmen-storage-oracle = { version = "16.5.0", optional = true }
+watchmen-storage-mongodb = { version = "16.5.0", optional = true }
+watchmen-storage-mssql = { version = "16.5.0", optional = true }
+watchmen-storage-postgresql = { version = "16.5.0", optional = true }
+watchmen-storage-oss = { version = "16.5.0", optional = true }
+watchmen-storage-s3 = { version = "16.5.0", optional = true }
 
 [tool.poetry.dev-dependencies]
 
 [tool.poetry.extras]
 mysql = ["watchmen-storage-mysql"]
 oracle = ["watchmen-storage-oracle"]
 mongodb = ["watchmen-storage-mongodb"]
```

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/__init__.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/__init__.py`

 * *Files 14% similar despite different names*

```diff
@@ -5,11 +5,13 @@
 from .collector_table_config import CollectorTableConfig
 
 from .trigger_event import TriggerEvent
 from .trigger_model import TriggerModel
 from .trigger_table import TriggerTable
 
 from .change_data_record import ChangeDataRecord
+from .change_data_record_history import ChangeDataRecordHistory
 from .change_data_json import ChangeDataJson
+from .change_data_json_history import ChangeDataJsonHistory
 
 from .condition import construct_conditions, Condition, ConditionJoint, ConditionExpression, \
 	ConditionJointConjunction
```

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/collector_table_config.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/collector_table_config.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/condition.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/model/condition.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/criteria_builder.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/criteria_builder.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/data_capture.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/data_capture.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/extract_source.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/extract_source.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/extract_utils.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/extract_utils.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/lock_clean.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/lock_clean.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,35 +1,37 @@
 from datetime import datetime, timedelta
 from logging import getLogger
 from threading import Thread
 
 from time import sleep
 
+from watchmen_collector_kernel.common import ask_lock_clean_interval, ask_lock_clean_timeout
 from watchmen_collector_kernel.storage import get_competitive_lock_service
 from watchmen_meta.common import ask_meta_storage
 
 
 class LockClean:
 
 	def __init__(self):
 		self.lock_service = get_competitive_lock_service(ask_meta_storage())
-		self.cleanInterval = 60
+		self.cleanInterval = ask_lock_clean_interval()
+		self.cleanTimeout = ask_lock_clean_timeout()
 
 	def run(self):
 		try:
 			while True:
 				self.clean_lock()
 				sleep(self.cleanInterval)
 		except Exception as e:
 			getLogger(__name__).error(e, exc_info=True, stack_info=True)
 			sleep(60)
 			self.restart()
 
 	def clean_lock(self):
-		query_time = datetime.now() - timedelta(minutes=120)
+		query_time = datetime.now() - timedelta(seconds=self.cleanTimeout)
 		locks = self.lock_service.find_overtime_lock(query_time)
 		for lock in locks:
 			self.lock_service.delete_by_id(lock.lockId)
 
 	def restart(self):
 		Thread(target=LockClean.run, args=(self,), daemon=True).start()
```

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/lock_helper.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/lock_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/task_housekeeping.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/task_housekeeping.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/task_service.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/task_service.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from logging import getLogger
 from traceback import format_exc
 from typing import Callable, Dict, Optional, List
 
 from watchmen_auth import PrincipalService
 from watchmen_collector_kernel.model import ScheduledTask
 from watchmen_collector_kernel.model.scheduled_task import Dependence
-from watchmen_collector_kernel.storage import get_scheduled_task_service
+from watchmen_collector_kernel.storage import get_scheduled_task_service, get_scheduled_task_history_service
 from watchmen_model.common import ScheduledTaskId
 from watchmen_storage import TransactionalStorageSPI, SnowflakeGenerator
 from watchmen_utilities import ArrayHelper
 
 logger = getLogger(__name__)
 
 
@@ -22,41 +22,53 @@
 	             ):
 		self.storage = storage
 		self.snowflake_generator = snowflake_generator
 		self.principal_service = principal_service
 		self.scheduled_task_service = get_scheduled_task_service(self.storage,
 		                                                         self.snowflake_generator,
 		                                                         self.principal_service)
+		self.scheduled_task_history_service = get_scheduled_task_history_service(self.storage,
+		                                                                         self.snowflake_generator,
+		                                                                         self.principal_service)
 
 	# noinspection PyMethodMayBeStatic
 	def consume_task(self, task: ScheduledTask, executed: Callable[[str, Dict, str], None]) -> ScheduledTask:
 		try:
 			executed(task.topicCode, task.content, task.tenantId)
-			task.isFinished = True
-			return self.scheduled_task_service.update_task(task)
+			return self.update_task_result(task)
 		except Exception as e:
 			logger.error(e, exc_info=True, stack_info=True)
 			task.isFinished = True
 			task.result = format_exc()
 			return self.scheduled_task_service.update_task(task)
 
+	def update_task_result(self, task: ScheduledTask) -> ScheduledTask:
+		self.scheduled_task_service.begin_transaction()
+		try:
+			task.isFinished = True
+			self.scheduled_task_history_service.create(task)
+			self.scheduled_task_service.delete(task.taskId)
+			self.scheduled_task_service.commit_transaction()
+			return task
+		except Exception as e:
+			raise e
+
 	def is_dependencies_finished(self, task: ScheduledTask) -> bool:
-		return ArrayHelper(task.parentTaskId).every(self.is_parent_task_finished) \
-		       and self.is_dependence_finished(task.dependOn, task.tenantId)
+		return ArrayHelper(task.parentTaskId).every(self.is_parent_task_finished) and self.is_dependence_finished(task.dependOn, task.tenantId)
 
 	def is_parent_task_finished(self, task_id: ScheduledTaskId) -> bool:
 		existed_task = self.scheduled_task_service.find_task_by_id(task_id)
-		return self.is_finished(existed_task)
+		if existed_task:
+			return self.is_finished(existed_task)
+		else:
+			return True
 
 	# noinspection PyMethodMayBeStatic
 	def is_finished(self, task: ScheduledTask) -> bool:
-		if task.status == TaskStatus.SUCCESS or task.status == TaskStatus.FAILED:
-			return True
-		else:
-			return False
+		return task.isFinished
 
 	def is_dependence_finished(self, depend_on: Optional[List[Dependence]], tenant_id: str) -> bool:
 		if ArrayHelper(depend_on).every(lambda dependence: self.is_dependent_task_finished(dependence, tenant_id)):
 			return True
 		else:
 			return False
```

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/trigger_collector.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/service/trigger_collector.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/change_data_json_service.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/change_data_json_service.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from typing import List, Dict, Any, Optional
 
 from watchmen_auth import PrincipalService
-from watchmen_collector_kernel.common import IS_POSTED, CHANGE_JSON_ID, TENANT_ID, MODEL_TRIGGER_ID
+from watchmen_collector_kernel.common import IS_POSTED, CHANGE_JSON_ID, TENANT_ID, MODEL_TRIGGER_ID, ask_partial_size
 from watchmen_collector_kernel.model import ChangeDataJson
 from watchmen_meta.common import TupleService, TupleShaper
 from watchmen_meta.common.storage_service import StorableId
-from watchmen_model.common import Storable, ChangeJsonId
+from watchmen_model.common import Storable, ChangeJsonId, Pageable
 from watchmen_storage import EntityName, EntityRow, EntityShaper, TransactionalStorageSPI, SnowflakeGenerator, \
 	ColumnNameLiteral, EntityCriteriaExpression, EntityStraightValuesFinder, EntityStraightColumn, EntitySortColumn, \
 	EntitySortMethod
 
 
 class ChangeDataJsonShaper(EntityShaper):
 	def serialize(self, entity: ChangeDataJson) -> EntityRow:
@@ -102,23 +102,52 @@
 				],
 				straightColumns=[EntityStraightColumn(columnName=CHANGE_JSON_ID),
 				                 EntityStraightColumn(columnName=TENANT_ID)]
 			))
 		finally:
 			self.close_transaction()
 
+	def find_partial_json(self, model_trigger_id: int) -> List[ChangeDataJson]:
+		self.begin_transaction()
+		try:
+			return self.storage.page(self.get_entity_pager(
+				criteria=[
+					EntityCriteriaExpression(left=ColumnNameLiteral(columnName=IS_POSTED), right=False),
+					EntityCriteriaExpression(left=ColumnNameLiteral(columnName=MODEL_TRIGGER_ID),
+					                         right=model_trigger_id)
+				],
+				pageable=Pageable(pageNumber=1, pageSize=ask_partial_size())
+			)).data
+		finally:
+			self.close_transaction()
+
+	def is_existed(self, change_json: ChangeDataJson) -> bool:
+		self.begin_transaction()
+		try:
+			return self.storage.exists(self.get_entity_finder(
+				criteria=[
+					EntityCriteriaExpression(
+						left=ColumnNameLiteral(
+							columnName=self.get_storable_id_column_name()
+						),
+						right=change_json.changeJsonId)
+				]
+			))
+		finally:
+			self.close_transaction()
+
 	def find_json_by_id(self, change_json_id: str) -> ChangeDataJson:
 		self.begin_transaction()
 		try:
 			# noinspection PyTypeChecker
 			return self.find_by_id(change_json_id)
 		finally:
 			self.close_transaction()
 
-	def find_id_by_resource_id(self, resource_id: str) -> Optional[ChangeDataJson]:
+	def find_by_resource_id(self, resource_id: str) -> Optional[ChangeDataJson]:
 		try:
 			self.storage.connect()
 			return self.storage.find_one(self.get_entity_finder(
 				criteria=[
 					EntityCriteriaExpression(left=ColumnNameLiteral(columnName='resource_id'), right=resource_id)
 				]
 			))
```

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/change_data_record_service.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/change_data_record_service.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 from typing import List, Optional, Dict
 
 from watchmen_auth import PrincipalService
-from watchmen_collector_kernel.common import CHANGE_RECORD_ID, TENANT_ID, IS_MERGED
+from watchmen_collector_kernel.common import CHANGE_RECORD_ID, TENANT_ID, IS_MERGED, ask_partial_size
 from watchmen_collector_kernel.model import ChangeDataRecord
 from watchmen_meta.common import TupleService, TupleShaper
 from watchmen_meta.common.storage_service import StorableId
-from watchmen_model.common import Storable, ChangeRecordId
+from watchmen_model.common import Storable, ChangeRecordId, Pageable
 from watchmen_storage import EntityName, EntityRow, EntityShaper, TransactionalStorageSPI, SnowflakeGenerator, \
-	EntityCriteriaExpression, ColumnNameLiteral, EntityStraightValuesFinder, EntityStraightColumn, EntityColumnType
+	EntityCriteriaExpression, ColumnNameLiteral, EntityStraightValuesFinder, EntityStraightColumn, EntityColumnType, \
+	EntityPager
 from watchmen_utilities import ArrayHelper
 
 
 class ChangeDataRecordShaper(EntityShaper):
 	def serialize(self, entity: ChangeDataRecord) -> EntityRow:
 		return TupleShaper.serialize_tenant_based(entity,
 		                                          {
@@ -106,27 +107,42 @@
 				],
 				straightColumns=[EntityStraightColumn(columnName=CHANGE_RECORD_ID),
 				                 EntityStraightColumn(columnName=TENANT_ID)]
 			))
 		finally:
 			self.close_transaction()
 
-	def count_unmerged_records(self) -> int:
+	def find_partial_records(self) -> List[ChangeDataRecord]:
 		self.begin_transaction()
 		try:
-			# noinspection PyTypeChecker
-			return self.storage.count(self.get_entity_finder(
+			return self.storage.page(self.get_entity_pager(
 				criteria=[
 					EntityCriteriaExpression(left=ColumnNameLiteral(columnName=IS_MERGED), right=False)
+				],
+				pageable=Pageable(pageNumber=1, pageSize=ask_partial_size())
+			)).data
+		finally:
+			self.close_transaction()
+
+	def is_existed(self, change_record: ChangeDataRecord) -> bool:
+		self.begin_transaction()
+		try:
+			return self.storage.exists(self.get_entity_finder(
+				criteria=[
+					EntityCriteriaExpression(
+						left=ColumnNameLiteral(
+							columnName=self.get_storable_id_column_name()
+						),
+						right=change_record.changeRecordId)
 				]
 			))
 		finally:
 			self.close_transaction()
 
-	def find_change_record_by_id(self, change_record_id: ChangeRecordId) -> ChangeDataRecord:
+	def find_change_record_by_id(self, change_record_id: ChangeRecordId) -> Optional[ChangeDataRecord]:
 		self.begin_transaction()
 		try:
 			# noinspection PyTypeChecker
 			return self.find_by_id(change_record_id)
 		finally:
 			self.close_transaction()
 
@@ -139,16 +155,16 @@
 					name=self.get_entity_name(),
 					shaper=self.get_entity_shaper(),
 					criteria=[
 						EntityCriteriaExpression(left=ColumnNameLiteral(columnName='table_trigger_id'),
 						                         right=table_trigger_id)
 					],
 					straightColumns=[EntityStraightColumn(columnName='data_id', columnType=EntityColumnType.JSON)]
-					)
 				)
+			)
 			return ArrayHelper(result).map(lambda x: x.get('data_id')).to_list()
 		finally:
 			self.close_transaction()
 
 	def is_event_finished(self, event_trigger_id: int) -> bool:
 		self.begin_transaction()
 		try:
```

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/collector_model_config_service.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/collector_model_config_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/collector_table_config_service.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/collector_table_config_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/competitive_lock_service.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/competitive_lock_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/scheduled_task_service.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/scheduled_task_service.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,30 +1,48 @@
 from typing import Optional, List, Any, Dict
 
+from watchmen_collector_kernel.common import ask_partial_size
+from watchmen_utilities import ArrayHelper
+
+from watchmen_collector_kernel.model.scheduled_task import Dependence
+
 from watchmen_auth import PrincipalService
 from watchmen_collector_kernel.model import ScheduledTask
 from watchmen_meta.common import TupleService, TupleShaper
 from watchmen_meta.common.storage_service import StorableId
-from watchmen_model.common import Storable, ScheduledTaskId
+from watchmen_model.common import Storable, ScheduledTaskId, Pageable
 from watchmen_storage import EntityName, EntityRow, EntityShaper, TransactionalStorageSPI, \
 	EntityCriteriaExpression, ColumnNameLiteral, SnowflakeGenerator, EntitySortColumn, EntitySortMethod, \
-	EntityCriteriaJoint, EntityCriteriaJointConjunction, EntityStraightValuesFinder, EntityStraightColumn, \
-	EntityCriteriaOperator
+	EntityCriteriaJoint, EntityStraightValuesFinder, EntityStraightColumn
 
 
 class ScheduledTaskShaper(EntityShaper):
+
+	@staticmethod
+	def serialize_dependence(dependence: Dependence) -> dict:
+		if isinstance(dependence, dict):
+			return dependence
+		else:
+			return dependence.dict()
+
+	@staticmethod
+	def serialize_depend_on(depend_on: Optional[List[Dependence]]) -> Optional[list]:
+		if depend_on is None:
+			return None
+		return ArrayHelper(depend_on).map(lambda x: ScheduledTaskShaper.serialize_dependence(x)).to_list()
+
 	def serialize(self, entity: ScheduledTask) -> EntityRow:
 		return TupleShaper.serialize_tenant_based(entity, {
 			'task_id': entity.taskId,
 			'resource_id': entity.resourceId,
 			'topic_code': entity.topicCode,
 			'content': entity.content,
 			'model_name': entity.modelName,
 			'object_id': entity.objectId,
-			'depend_on': entity.dependOn,
+			'depend_on': ScheduledTaskShaper.serialize_depend_on(entity.dependOn),
 			'parent_task_id': entity.parentTaskId,
 			'tenant_id': entity.tenantId,
 			'is_finished': entity.isFinished,
 			'result': entity.result
 		})
 
 	def deserialize(self, row: EntityRow) -> ScheduledTask:
@@ -114,21 +132,51 @@
 				                 EntityStraightColumn(columnName='resource_id'),
 				                 EntityStraightColumn(columnName='tenant_id')],
 				sort=[EntitySortColumn(name='resource_id', method=EntitySortMethod.ASC)]
 			))
 		finally:
 			self.close_transaction()
 
+	def find_partial_tasks(self) -> List[ScheduledTask]:
+		self.begin_transaction()
+		try:
+			return self.storage.page(self.get_entity_pager(
+				criteria=[
+					EntityCriteriaExpression(left=ColumnNameLiteral(columnName='is_finished'), right=False)
+				],
+				pageable=Pageable(pageNumber=1, pageSize=ask_partial_size())
+			)).data
+		finally:
+			self.close_transaction()
+
+	def is_existed(self, task: ScheduledTask) -> bool:
+		self.begin_transaction()
+		try:
+			return self.storage.exists(self.get_entity_finder(
+				criteria=[
+					EntityCriteriaExpression(
+						left=ColumnNameLiteral(
+							columnName=self.get_storable_id_column_name()
+						),
+						right=task.taskId)
+				]
+			))
+		finally:
+			self.close_transaction()
+
 	def find_by_resource_id(self, resource_id: str) -> List[Dict[str, Any]]:
 		self.begin_transaction()
 		try:
 			return self.storage.find_straight_values(EntityStraightValuesFinder(
 				name=self.get_entity_name(),
-				criteria=[EntityCriteriaExpression(left=ColumnNameLiteral(columnName='resource_id'), right=resource_id)],
-				straightColumns=['task_id', 'resource_id', 'tenant_id']
+				criteria=[
+					EntityCriteriaExpression(left=ColumnNameLiteral(columnName='resource_id'), right=resource_id)],
+				straightColumns=[EntityStraightColumn(columnName='task_id'),
+				                 EntityStraightColumn(columnName='resource_id'),
+				                 EntityStraightColumn(columnName='tenant_id')]
 			))
 		finally:
 			self.close_transaction()
 
 	def is_dependent_task_finished(self, model_name: str, object_id: str, tenant_id: str) -> bool:
 		self.begin_transaction()
 		try:
@@ -144,12 +192,13 @@
 					EntityCriteriaExpression(left=ColumnNameLiteral(columnName='tenant_id'),
 					                         right=tenant_id)
 				]
 			)) == 0
 		finally:
 			self.close_transaction()
 
+
 def get_scheduled_task_service(storage: TransactionalStorageSPI,
                                snowflake_generator: SnowflakeGenerator,
                                principal_service: PrincipalService
                                ) -> ScheduledTaskService:
 	return ScheduledTaskService(storage, snowflake_generator, principal_service)
```

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/trigger_event_service.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/trigger_event_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/trigger_model_service.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/trigger_model_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/trigger_table_service.py` & `watchmen_collector_kernel-16.5.0/src/watchmen_collector_kernel/storage/trigger_table_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.9/PKG-INFO` & `watchmen_collector_kernel-16.5.0/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: watchmen-collector-kernel
-Version: 16.4.9
+Version: 16.5.0
 Summary: 
 License: MIT
 Author: botlikes
 Author-email: 75356972+botlikes456@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
@@ -14,15 +14,16 @@
 Provides-Extra: mongodb
 Provides-Extra: mssql
 Provides-Extra: mysql
 Provides-Extra: oracle
 Provides-Extra: oss
 Provides-Extra: postgresql
 Provides-Extra: s3
-Requires-Dist: watchmen-data-kernel (==16.4.9)
-Requires-Dist: watchmen-storage-mongodb (==16.4.9) ; extra == "mongodb"
-Requires-Dist: watchmen-storage-mssql (==16.4.9) ; extra == "mssql"
-Requires-Dist: watchmen-storage-mysql (==16.4.9) ; extra == "mysql"
-Requires-Dist: watchmen-storage-oracle (==16.4.9) ; extra == "oracle"
-Requires-Dist: watchmen-storage-oss (==16.4.9) ; extra == "oss"
-Requires-Dist: watchmen-storage-postgresql (==16.4.9) ; extra == "postgresql"
-Requires-Dist: watchmen-storage-s3 (==16.4.9) ; extra == "s3"
+Requires-Dist: numpy (>=1.23.3,<2.0.0)
+Requires-Dist: watchmen-data-kernel (==16.5.0)
+Requires-Dist: watchmen-storage-mongodb (==16.5.0) ; extra == "mongodb"
+Requires-Dist: watchmen-storage-mssql (==16.5.0) ; extra == "mssql"
+Requires-Dist: watchmen-storage-mysql (==16.5.0) ; extra == "mysql"
+Requires-Dist: watchmen-storage-oracle (==16.5.0) ; extra == "oracle"
+Requires-Dist: watchmen-storage-oss (==16.5.0) ; extra == "oss"
+Requires-Dist: watchmen-storage-postgresql (==16.5.0) ; extra == "postgresql"
+Requires-Dist: watchmen-storage-s3 (==16.5.0) ; extra == "s3"
```

