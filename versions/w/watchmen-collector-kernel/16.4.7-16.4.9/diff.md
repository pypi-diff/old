# Comparing `tmp/watchmen_collector_kernel-16.4.7.tar.gz` & `tmp/watchmen_collector_kernel-16.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_collector_kernel-16.4.7.tar", max compression
+gzip compressed data, was "watchmen_collector_kernel-16.4.9.tar", max compression
```

## Comparing `watchmen_collector_kernel-16.4.7.tar` & `watchmen_collector_kernel-16.4.9.tar`

### file list

```diff
@@ -1,17 +1,38 @@
--rw-r--r--   0        0        0     1061 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/LICENSE
--rw-r--r--   0        0        0     1183 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/pyproject.toml
--rw-r--r--   0        0        0        0 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/__init__.py
--rw-r--r--   0        0        0       43 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/common/__init__.py
--rw-r--r--   0        0        0      287 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/common/settings.py
--rw-r--r--   0        0        0       44 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/connector/__init__.py
--rw-r--r--   0        0        0     1806 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/connector/handler.py
--rw-r--r--   0        0        0     1964 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/connector/housekeeping.py
--rw-r--r--   0        0        0     7896 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/connector/s3_connector.py
--rw-r--r--   0        0        0      190 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/lock/__init__.py
--rw-r--r--   0        0        0      294 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/lock/distributed_lock.py
--rw-r--r--   0        0        0     4481 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/lock/oss_collector_lock_service.py
--rw-r--r--   0        0        0     1074 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/lock/unique_key_distributed_lock.py
--rw-r--r--   0        0        0       72 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/model/__init__.py
--rw-r--r--   0        0        0      456 2023-01-18 10:06:03.426851 watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/model/oss_collector_competitive_lock.py
--rw-r--r--   0        0        0     1257 1970-01-01 00:00:00.000000 watchmen_collector_kernel-16.4.7/setup.py
--rw-r--r--   0        0        0     1139 1970-01-01 00:00:00.000000 watchmen_collector_kernel-16.4.7/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/LICENSE
+-rw-r--r--   0        0        0     1179 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/__init__.py
+-rw-r--r--   0        0        0      175 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/common/__init__.py
+-rw-r--r--   0        0        0      302 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/common/constants.py
+-rw-r--r--   0        0        0      542 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/__init__.py
+-rw-r--r--   0        0        0      495 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/change_data_json.py
+-rw-r--r--   0        0        0      330 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/change_data_record.py
+-rw-r--r--   0        0        0      288 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/collector_model_config.py
+-rw-r--r--   0        0        0     2143 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/collector_table_config.py
+-rw-r--r--   0        0        0      264 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/competitive_lock.py
+-rw-r--r--   0        0        0     1942 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/condition.py
+-rw-r--r--   0        0        0      674 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/scheduled_task.py
+-rw-r--r--   0        0        0      251 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/trigger_event.py
+-rw-r--r--   0        0        0      175 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/trigger_model.py
+-rw-r--r--   0        0        0      229 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/model/trigger_table.py
+-rw-r--r--   0        0        0      426 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/__init__.py
+-rw-r--r--   0        0        0     2360 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/criteria_builder.py
+-rw-r--r--   0        0        0     2873 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/data_capture.py
+-rw-r--r--   0        0        0     2928 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/extract_source.py
+-rw-r--r--   0        0        0     2452 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/extract_utils.py
+-rw-r--r--   0        0        0      965 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/lock_clean.py
+-rw-r--r--   0        0        0      842 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/lock_helper.py
+-rw-r--r--   0        0        0     1673 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/task_housekeeping.py
+-rw-r--r--   0        0        0     3050 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/task_service.py
+-rw-r--r--   0        0        0     6790 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/trigger_collector.py
+-rw-r--r--   0        0        0      832 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/__init__.py
+-rw-r--r--   0        0        0     7536 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/change_data_json_service.py
+-rw-r--r--   0        0        0     7463 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/change_data_record_service.py
+-rw-r--r--   0        0        0     3830 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/collector_model_config_service.py
+-rw-r--r--   0        0        0     5659 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/collector_table_config_service.py
+-rw-r--r--   0        0        0     2534 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/competitive_lock_service.py
+-rw-r--r--   0        0        0     5376 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/scheduled_task_service.py
+-rw-r--r--   0        0        0     3099 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/trigger_event_service.py
+-rw-r--r--   0        0        0     3219 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/trigger_model_service.py
+-rw-r--r--   0        0        0     3779 2023-02-23 10:23:45.972775 watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/trigger_table_service.py
+-rw-r--r--   0        0        0     1254 1970-01-01 00:00:00.000000 watchmen_collector_kernel-16.4.9/setup.py
+-rw-r--r--   0        0        0     1135 1970-01-01 00:00:00.000000 watchmen_collector_kernel-16.4.9/PKG-INFO
```

### Comparing `watchmen_collector_kernel-16.4.7/LICENSE` & `watchmen_collector_kernel-16.4.9/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_collector_kernel-16.4.7/pyproject.toml` & `watchmen_collector_kernel-16.4.9/pyproject.toml`

 * *Files 19% similar despite different names*

```diff
@@ -1,27 +1,27 @@
 [tool.poetry]
 name = "watchmen-collector-kernel"
-version = "16.4.7"
+version = "16.4.9"
 description = ""
 authors = ["botlikes <75356972+botlikes456@users.noreply.github.com>"]
 license = "MIT"
 packages = [
     { include = "watchmen_collector_kernel", from = "src" }
 ]
 
 [tool.poetry.dependencies]
 python = "^3.9"
-watchmen-pipeline-kernel = "16.4.7"
-watchmen-storage-mysql = { version = "16.4.7", optional = true }
-watchmen-storage-oracle = { version = "16.4.7", optional = true }
-watchmen-storage-mongodb = { version = "16.4.7", optional = true }
-watchmen-storage-mssql = { version = "16.4.7", optional = true }
-watchmen-storage-postgresql = { version = "16.4.7", optional = true }
-watchmen-storage-oss = { version = "16.4.7", optional = true }
-watchmen-storage-s3 = { version = "16.4.7", optional = true }
+watchmen-data-kernel = "16.4.9"
+watchmen-storage-mysql = { version = "16.4.9", optional = true }
+watchmen-storage-oracle = { version = "16.4.9", optional = true }
+watchmen-storage-mongodb = { version = "16.4.9", optional = true }
+watchmen-storage-mssql = { version = "16.4.9", optional = true }
+watchmen-storage-postgresql = { version = "16.4.9", optional = true }
+watchmen-storage-oss = { version = "16.4.9", optional = true }
+watchmen-storage-s3 = { version = "16.4.9", optional = true }
 
 [tool.poetry.dev-dependencies]
 
 [tool.poetry.extras]
 mysql = ["watchmen-storage-mysql"]
 oracle = ["watchmen-storage-oracle"]
 mongodb = ["watchmen-storage-mongodb"]
```

### Comparing `watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/connector/housekeeping.py` & `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/service/task_housekeeping.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,58 +1,61 @@
-from datetime import datetime, date, timedelta
+from datetime import date, datetime, timedelta
 from logging import getLogger
 from threading import Thread
 from typing import List
 
-from watchmen_collector_kernel.common import S3CollectorSettings
-from watchmen_collector_kernel.lock import get_oss_collector_lock_service
-from watchmen_collector_kernel.model import OSSCollectorCompetitiveLock
 from time import sleep
 
+from watchmen_collector_kernel.storage import get_competitive_lock_service
+from watchmen_collector_kernel.model import CompetitiveLock
+
 
 class CleanTask:
-	
-	def __init__(self,  settings: S3CollectorSettings):
-		self.lock_service = get_oss_collector_lock_service()
+
+	def __init__(self):
+		self.lock_service = get_competitive_lock_service()
 		self.processed_date = []
-		self.cleanTaskInterval = settings.clean_task_interval
-	
+		self.cleanTaskInterval = 3600
+
 	def run(self):
 		try:
 			while True:
 				self.clean_task()
 				sleep(self.cleanTaskInterval)
 		except Exception as e:
 			getLogger(__name__).error(e, exc_info=True, stack_info=True)
+			sleep(30)
 			self.restart()
-	
+
 	def clean_task(self):
 		query_datetime = datetime.now()
-		query_date = query_datetime.date() - timedelta(hours=query_datetime.hour,
-		                                               minutes=query_datetime.minute,
-		                                               seconds=query_datetime.second,
-		                                               microseconds=query_datetime.microsecond)
+		delta = timedelta(
+			hours=query_datetime.hour,
+			minutes=query_datetime.minute,
+			seconds=query_datetime.second,
+			microseconds=query_datetime.microsecond)
+		query_date = query_datetime.date() - delta
 		if self.is_processed(query_date):
 			return "Done"
 		else:
 			tasks = self.get_task_list(query_date)
 			for task in tasks:
 				self.lock_service.delete_by_id(task.lockId)
 			self.processed_date.append(query_date.strftime('%Y-%m-%d'))
-	
-	def get_task_list(self, clean_date) -> List[OSSCollectorCompetitiveLock]:
+
+	def get_task_list(self, clean_date) -> List[CompetitiveLock]:
 		return self.lock_service.find_completed_task(clean_date)
-	
+
 	def is_processed(self, query_date: date) -> bool:
 		date_str = query_date.strftime('%Y-%m-%d')
 		if date_str in self.processed_date:
 			return True
 		else:
 			return False
-	
+
 	def restart(self):
 		Thread(target=CleanTask.run, args=(self,), daemon=True).start()
 
 
-def init_task_housekeeping(settings: S3CollectorSettings):
-	cleanTask = CleanTask(settings)
-	Thread(target=CleanTask.run, args=(cleanTask,), daemon=True).start()
+def init_task_housekeeping():
+	clean_task = CleanTask()
+	Thread(target=CleanTask.run, args=(clean_task,), daemon=True).start()
```

### Comparing `watchmen_collector_kernel-16.4.7/src/watchmen_collector_kernel/lock/oss_collector_lock_service.py` & `watchmen_collector_kernel-16.4.9/src/watchmen_collector_kernel/storage/collector_model_config_service.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,127 +1,107 @@
-from datetime import datetime
-from typing import List
+from typing import Optional, List
 
-from watchmen_meta.common import EntityService, ask_meta_storage
+from watchmen_auth import PrincipalService
+from watchmen_collector_kernel.model import CollectorModelConfig
+from watchmen_meta.common import TupleService, TupleShaper
 from watchmen_meta.common.storage_service import StorableId
-from watchmen_model.common import Storable, OssCollectorCompetitiveLockId
-from watchmen_storage import EntityShaper, EntityRow, EntityName, TransactionalStorageSPI, \
-	EntityHelper, EntityIdHelper, EntityFinder, ColumnNameLiteral, EntityCriteriaExpression, Entity
-from watchmen_collector_kernel.model import OSSCollectorCompetitiveLock
-
-
-class OSSCollectorCompetitiveLockShaper(EntityShaper):
-	def serialize(self, entity: OSSCollectorCompetitiveLock) -> EntityRow:
-		return {
-			'lock_id': entity.lockId,
-			'resource_id': entity.resourceId,
-			'model_name': entity.modelName,
-			'object_id': entity.objectId,
-			'registered_at': entity.registeredAt,
-			'tenant_id': entity.tenantId,
-			'status': entity.status
-		}
-	
-	def deserialize(self, row: EntityRow) -> OSSCollectorCompetitiveLock:
-		return OSSCollectorCompetitiveLock(
-			lockId=row.get('lock_id'),
-			resourceId=row.get('resource_id'),
+from watchmen_model.common import Storable, TenantId, CollectorModelConfigId
+from watchmen_storage import EntityName, EntityRow, EntityShaper, TransactionalStorageSPI, SnowflakeGenerator, \
+	EntityCriteriaExpression, ColumnNameLiteral
+
+
+class CollectorModelConfigShaper(EntityShaper):
+	def serialize(self, config: CollectorModelConfig) -> EntityRow:
+		return TupleShaper.serialize_tenant_based(config, {
+			'model_id': config.modelId,
+			'model_name': config.modelName,
+			'depend_on': config.dependOn,
+			'raw_topic_code': config.rawTopicCode,
+			'is_paralleled': config.isParalleled
+		})
+
+	def deserialize(self, row: EntityRow) -> CollectorModelConfig:
+		# noinspection PyTypeChecker
+		return TupleShaper.deserialize_tenant_based(row, CollectorModelConfig(
+			modelId=row.get('model_id'),
 			modelName=row.get('model_name'),
-			objectId=row.get('object_id'),
-			registeredAt=row.get('registered_at'),
-			tenantId=row.get('tenant_id'),
-			status=row.get('status')
-		)
-
-
-OSS_COLLECTOR_COMPETITIVE_LOCK_TABLE = 'oss_collector_competitive_lock'
-OSS_COLLECTOR_COMPETITIVE_LOCK_ENTITY_SHAPER = OSSCollectorCompetitiveLockShaper()
-
-
-class OssCollectorLockService(EntityService):
-	
-	def __init__(self, storage: TransactionalStorageSPI):
-		super().__init__(storage)
-	
+			dependOn=row.get('depend_on'),
+			rawTopicCode=row.get('raw_topic_code'),
+			isParalleled=row.get('is_paralleled')
+		))
+
+
+COLLECTOR_MODEL_CONFIG_ENTITY_NAME = 'collector_model_config'
+COLLECTOR_MODEL_CONFIG_ENTITY_SHAPER = CollectorModelConfigShaper()
+
+
+class CollectorModelConfigService(TupleService):
+	def should_record_operation(self) -> bool:
+		return False
+
 	def get_entity_name(self) -> EntityName:
-		return OSS_COLLECTOR_COMPETITIVE_LOCK_TABLE
-	
+		return COLLECTOR_MODEL_CONFIG_ENTITY_NAME
+
 	def get_entity_shaper(self) -> EntityShaper:
-		return OSS_COLLECTOR_COMPETITIVE_LOCK_ENTITY_SHAPER
-	
+		return COLLECTOR_MODEL_CONFIG_ENTITY_SHAPER
+
+	# noinspection SpellCheckingInspection
 	def get_storable_id_column_name(self) -> EntityName:
-		return 'lock_id'
-	
-	def get_storable_id(self, storable: OSSCollectorCompetitiveLock) -> StorableId:
-		return storable.lockId
-	
-	def set_storable_id(self, storable: OSSCollectorCompetitiveLock,
-	                    storable_id: OssCollectorCompetitiveLockId) -> Storable:
-		storable.lockId = storable_id
+		return "model_id"
+
+	def get_storable_id(self, storable: CollectorModelConfig) -> StorableId:
+		return storable.modelId
+
+	# noinspection SpellCheckingInspection
+	def set_storable_id(self, storable: CollectorModelConfig, storable_id: CollectorModelConfigId) -> Storable:
+		storable.modelId = storable_id
 		return storable
-	
-	def insert_one(self, lock: OSSCollectorCompetitiveLock):
-		try:
-			self.storage.connect()
-			self.storage.insert_one(
-				lock,
-				EntityHelper(name=OSS_COLLECTOR_COMPETITIVE_LOCK_TABLE, shaper=OSS_COLLECTOR_COMPETITIVE_LOCK_ENTITY_SHAPER)
-			)
-		finally:
-			self.storage.close()
-	
-	def delete_by_id(self, id_: OssCollectorCompetitiveLockId):
+
+	def create_model_config(self, model_config: CollectorModelConfig) -> CollectorModelConfig:
 		try:
 			self.storage.connect()
-			self.storage.delete_by_id(id_,
-			                          EntityIdHelper(idColumnName='lock_id',
-			                                         name=OSS_COLLECTOR_COMPETITIVE_LOCK_TABLE,
-			                                         shaper=OSS_COLLECTOR_COMPETITIVE_LOCK_ENTITY_SHAPER)
-			                          )
+			# noinspection PyTypeChecker
+			return self.create(model_config)
 		finally:
 			self.storage.close()
-	
-	def update_one(self, one: Entity) -> int:
+
+	def update_model_config(self, model_config: CollectorModelConfig) -> CollectorModelConfig:
 		try:
 			self.storage.connect()
-			self.storage.update_one(one,
-			                        EntityIdHelper(idColumnName='lock_id',
-			                                       name=OSS_COLLECTOR_COMPETITIVE_LOCK_TABLE,
-			                                       shaper=OSS_COLLECTOR_COMPETITIVE_LOCK_ENTITY_SHAPER)
-			                        )
+			# noinspection PyTypeChecker
+			return self.update(model_config)
 		finally:
 			self.storage.close()
-	
-	def find_by_dependency(self, model_name: str, object_id: str) -> int:
+
+	def find_by_model_id(self, model_id: str) -> Optional[CollectorModelConfig]:
+		self.begin_transaction()
 		try:
-			self.storage.connect()
-			return self.storage.count(EntityFinder(
-				name=self.get_entity_name(),
-				shaper=self.get_entity_shaper(),
+			return self.storage.find_one(self.get_entity_finder(
 				criteria=[
-					EntityCriteriaExpression(left=ColumnNameLiteral(columnName='model_name'), right=model_name),
-					EntityCriteriaExpression(left=ColumnNameLiteral(columnName='object_id'), right=object_id),
-					EntityCriteriaExpression(left=ColumnNameLiteral(columnName='status'), right=0)
-				]
+					EntityCriteriaExpression(left=ColumnNameLiteral(columnName='model_id'), right=model_id)]
 			))
 		finally:
-			self.storage.close()
+			self.close_transaction()
+
+	def find_by_tenant(self, tenant_id: TenantId) -> Optional[List[CollectorModelConfig]]:
+		# noinspection PyTypeChecker
+		return self.storage.find(self.get_entity_finder(
+			criteria=[
+				EntityCriteriaExpression(left=ColumnNameLiteral(columnName='tenant_id'), right=tenant_id)]
+		))
 
-	def find_completed_task(self, query_date: datetime) -> List:
+	def find_by_name(self, model_name: str) -> Optional[CollectorModelConfig]:
+		self.begin_transaction()
 		try:
-			self.storage.connect()
-			return self.storage.find(EntityFinder(
-				name=self.get_entity_name(),
-				shaper=self.get_entity_shaper(),
+			return self.storage.find_one(self.get_entity_finder(
 				criteria=[
-					EntityCriteriaExpression(left=ColumnNameLiteral(columnName='registered_at'),
-					                         operator="less-than",
-					                         right=query_date),
-					EntityCriteriaExpression(left=ColumnNameLiteral(columnName='status'), right=1)
-				]
+					EntityCriteriaExpression(left=ColumnNameLiteral(columnName='model_name'), right=model_name)]
 			))
 		finally:
-			self.storage.close()
-	
+			self.close_transaction()
+
 
-def get_oss_collector_lock_service() -> OssCollectorLockService:
-	return OssCollectorLockService(ask_meta_storage())
+def get_collector_model_config_service(storage: TransactionalStorageSPI,
+                                       snowflake_generator: SnowflakeGenerator,
+                                       principal_service: PrincipalService
+                                       ) -> CollectorModelConfigService:
+	return CollectorModelConfigService(storage, snowflake_generator, principal_service)
```

### Comparing `watchmen_collector_kernel-16.4.7/setup.py` & `watchmen_collector_kernel-16.4.9/setup.py`

 * *Files 24% similar despite different names*

```diff
@@ -3,36 +3,36 @@
 
 package_dir = \
 {'': 'src'}
 
 packages = \
 ['watchmen_collector_kernel',
  'watchmen_collector_kernel.common',
- 'watchmen_collector_kernel.connector',
- 'watchmen_collector_kernel.lock',
- 'watchmen_collector_kernel.model']
+ 'watchmen_collector_kernel.model',
+ 'watchmen_collector_kernel.service',
+ 'watchmen_collector_kernel.storage']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['watchmen-pipeline-kernel==16.4.7']
+['watchmen-data-kernel==16.4.9']
 
 extras_require = \
-{'mongodb': ['watchmen-storage-mongodb==16.4.7'],
- 'mssql': ['watchmen-storage-mssql==16.4.7'],
- 'mysql': ['watchmen-storage-mysql==16.4.7'],
- 'oracle': ['watchmen-storage-oracle==16.4.7'],
- 'oss': ['watchmen-storage-oss==16.4.7'],
- 'postgresql': ['watchmen-storage-postgresql==16.4.7'],
- 's3': ['watchmen-storage-s3==16.4.7']}
+{'mongodb': ['watchmen-storage-mongodb==16.4.9'],
+ 'mssql': ['watchmen-storage-mssql==16.4.9'],
+ 'mysql': ['watchmen-storage-mysql==16.4.9'],
+ 'oracle': ['watchmen-storage-oracle==16.4.9'],
+ 'oss': ['watchmen-storage-oss==16.4.9'],
+ 'postgresql': ['watchmen-storage-postgresql==16.4.9'],
+ 's3': ['watchmen-storage-s3==16.4.9']}
 
 setup_kwargs = {
     'name': 'watchmen-collector-kernel',
-    'version': '16.4.7',
+    'version': '16.4.9',
     'description': '',
     'long_description': 'None',
     'author': 'botlikes',
     'author_email': '75356972+botlikes456@users.noreply.github.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `watchmen_collector_kernel-16.4.7/PKG-INFO` & `watchmen_collector_kernel-16.4.9/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: watchmen-collector-kernel
-Version: 16.4.7
+Version: 16.4.9
 Summary: 
 License: MIT
 Author: botlikes
 Author-email: 75356972+botlikes456@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
@@ -14,15 +14,15 @@
 Provides-Extra: mongodb
 Provides-Extra: mssql
 Provides-Extra: mysql
 Provides-Extra: oracle
 Provides-Extra: oss
 Provides-Extra: postgresql
 Provides-Extra: s3
-Requires-Dist: watchmen-pipeline-kernel (==16.4.7)
-Requires-Dist: watchmen-storage-mongodb (==16.4.7) ; extra == "mongodb"
-Requires-Dist: watchmen-storage-mssql (==16.4.7) ; extra == "mssql"
-Requires-Dist: watchmen-storage-mysql (==16.4.7) ; extra == "mysql"
-Requires-Dist: watchmen-storage-oracle (==16.4.7) ; extra == "oracle"
-Requires-Dist: watchmen-storage-oss (==16.4.7) ; extra == "oss"
-Requires-Dist: watchmen-storage-postgresql (==16.4.7) ; extra == "postgresql"
-Requires-Dist: watchmen-storage-s3 (==16.4.7) ; extra == "s3"
+Requires-Dist: watchmen-data-kernel (==16.4.9)
+Requires-Dist: watchmen-storage-mongodb (==16.4.9) ; extra == "mongodb"
+Requires-Dist: watchmen-storage-mssql (==16.4.9) ; extra == "mssql"
+Requires-Dist: watchmen-storage-mysql (==16.4.9) ; extra == "mysql"
+Requires-Dist: watchmen-storage-oracle (==16.4.9) ; extra == "oracle"
+Requires-Dist: watchmen-storage-oss (==16.4.9) ; extra == "oss"
+Requires-Dist: watchmen-storage-postgresql (==16.4.9) ; extra == "postgresql"
+Requires-Dist: watchmen-storage-s3 (==16.4.9) ; extra == "s3"
```

