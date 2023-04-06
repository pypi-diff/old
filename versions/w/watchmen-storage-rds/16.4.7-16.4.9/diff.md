# Comparing `tmp/watchmen_storage_rds-16.4.7.tar.gz` & `tmp/watchmen_storage_rds-16.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_storage_rds-16.4.7.tar", max compression
+gzip compressed data, was "watchmen_storage_rds-16.4.9.tar", max compression
```

## Comparing `watchmen_storage_rds-16.4.7.tar` & `watchmen_storage_rds-16.4.9.tar`

### file list

```diff
@@ -1,14 +1,14 @@
--rw-r--r--   0        0        0      455 2023-01-18 10:06:03.466851 watchmen_storage_rds-16.4.7/pyproject.toml
--rw-r--r--   0        0        0      643 2023-01-18 10:06:03.466851 watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/__init__.py
--rw-r--r--   0        0        0      652 2023-01-18 10:06:03.466851 watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/dbscript_builder.py
--rw-r--r--   0        0        0      518 2023-01-18 10:06:03.466851 watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/ext_types.py
--rw-r--r--   0        0        0      672 2023-01-18 10:06:03.466851 watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/settings.py
--rw-r--r--   0        0        0      923 2023-01-18 10:06:03.466851 watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/sort_build.py
--rw-r--r--   0        0        0    17222 2023-01-18 10:06:03.466851 watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/storage_rds.py
--rw-r--r--   0        0        0    16715 2023-01-18 10:06:03.466851 watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/table_defs.py
--rw-r--r--   0        0        0     2249 2023-01-18 10:06:03.466851 watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/table_defs_helper.py
--rw-r--r--   0        0        0    20801 2023-01-18 10:06:03.466851 watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/topic_data_storage_rds.py
--rw-r--r--   0        0        0     8191 2023-01-18 10:06:03.466851 watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/topic_table_generate.py
--rw-r--r--   0        0        0       50 2023-01-18 10:06:03.466851 watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/types.py
--rw-r--r--   0        0        0      727 1970-01-01 00:00:00.000000 watchmen_storage_rds-16.4.7/setup.py
--rw-r--r--   0        0        0      524 1970-01-01 00:00:00.000000 watchmen_storage_rds-16.4.7/PKG-INFO
+-rw-r--r--   0        0        0      455 2023-02-23 10:23:46.016776 watchmen_storage_rds-16.4.9/pyproject.toml
+-rw-r--r--   0        0        0      643 2023-02-23 10:23:46.016776 watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/__init__.py
+-rw-r--r--   0        0        0      652 2023-02-23 10:23:46.016776 watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/dbscript_builder.py
+-rw-r--r--   0        0        0      518 2023-02-23 10:23:46.016776 watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/ext_types.py
+-rw-r--r--   0        0        0      672 2023-02-23 10:23:46.016776 watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/settings.py
+-rw-r--r--   0        0        0      941 2023-02-23 10:23:46.016776 watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/sort_build.py
+-rw-r--r--   0        0        0    17290 2023-02-23 10:23:46.016776 watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/storage_rds.py
+-rw-r--r--   0        0        0    20144 2023-02-23 10:23:46.016776 watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/table_defs.py
+-rw-r--r--   0        0        0     2249 2023-02-23 10:23:46.016776 watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/table_defs_helper.py
+-rw-r--r--   0        0        0    20801 2023-02-23 10:23:46.016776 watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/topic_data_storage_rds.py
+-rw-r--r--   0        0        0     8191 2023-02-23 10:23:46.016776 watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/topic_table_generate.py
+-rw-r--r--   0        0        0      916 2023-02-23 10:23:46.016776 watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/types.py
+-rw-r--r--   0        0        0      727 1970-01-01 00:00:00.000000 watchmen_storage_rds-16.4.9/setup.py
+-rw-r--r--   0        0        0      524 1970-01-01 00:00:00.000000 watchmen_storage_rds-16.4.9/PKG-INFO
```

### Comparing `watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/__init__.py` & `watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/__init__.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/dbscript_builder.py` & `watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/dbscript_builder.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/ext_types.py` & `watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/ext_types.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/settings.py` & `watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/settings.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/sort_build.py` & `watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/sort_build.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 from typing import Union  # noqa
 
-from sqlalchemy import asc, desc
+from sqlalchemy import asc, desc, text
 
 from watchmen_storage import EntitySort, EntitySortColumn, EntitySortMethod, UnsupportedSortMethodException
 from watchmen_utilities import ArrayHelper
 from .types import SQLAlchemyStatement
 
 
 def build_sort_column(column: EntitySortColumn):
 	if column.method == EntitySortMethod.ASC:
-		return asc(column.name)
+		return asc(text(column.name))
 	elif column.method == EntitySortMethod.DESC:
-		return desc(column.name)
+		return desc(text(column.name))
 	else:
 		raise UnsupportedSortMethodException(f'Unsupported sort method[{column.method}].')
 
 
 def build_sort(sort: EntitySort) -> Union[None, list]:
 	if sort is None or len(sort) == 0:
 		return None
```

### Comparing `watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/storage_rds.py` & `watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/storage_rds.py`

 * *Files 0% similar despite different names*

```diff
@@ -17,15 +17,15 @@
 	EntityStraightAggregateColumn, EntityStraightColumn, EntityStraightValuesFinder, EntityUpdater, \
 	TooManyEntitiesFoundException, TransactionalStorageSPI, UnexpectedStorageException, \
 	UnsupportedStraightColumnException
 from watchmen_utilities import ArrayHelper, is_blank, serialize_to_json
 from .settings import ask_connection_leak_time_in_seconds, ask_detect_connection_leak_enabled, \
 	ask_print_connection_leak_interval
 from .table_defs import find_table
-from .types import SQLAlchemyStatement
+from .types import SQLAlchemyStatement, get_column_type
 
 logger = getLogger(__name__)
 
 alive_conn_dict: Dict[str, Tuple[Any, float]] = {}
 
 
 def print_conn_dict() -> None:
@@ -305,15 +305,15 @@
 		return self.find_on_statement_by_finder(table, statement, finder)
 
 	def find_distinct_values(self, finder: EntityDistinctValuesFinder) -> EntityList:
 		table = self.find_table(finder.name)
 		if len(finder.distinctColumnNames) != 1 or not finder.distinctValueOnSingleColumn:
 			statement = select(*ArrayHelper(finder.distinctColumnNames).map(text).to_list()).select_from(table)
 		else:
-			statement = select(distinct(finder.distinctColumnNames[0])).select_from(table)
+			statement = select(distinct(text(finder.distinctColumnNames[0]))).select_from(table)
 		return self.find_on_statement_by_finder(table, statement, finder)
 
 	# noinspection PyMethodMayBeStatic
 	def get_alias_from_straight_column(self, straight_column: EntityStraightColumn) -> Any:
 		return straight_column.columnName if is_blank(straight_column.alias) else straight_column.alias
 
 	# noinspection PyMethodMayBeStatic
@@ -330,15 +330,15 @@
 			elif straight_column.arithmetic == EntityColumnAggregateArithmetic.MAX:
 				return func.max(literal_column(straight_column.columnName)) \
 					.label(self.get_alias_from_straight_column(straight_column))
 			elif straight_column.arithmetic == EntityColumnAggregateArithmetic.MIN:
 				return func.min(literal_column(straight_column.columnName)) \
 					.label(self.get_alias_from_straight_column(straight_column))
 		elif isinstance(straight_column, EntityStraightColumn):
-			return literal_column(straight_column.columnName) \
+			return literal_column(straight_column.columnName, get_column_type(straight_column.columnType)) \
 				.label(self.get_alias_from_straight_column(straight_column))
 
 		raise UnsupportedStraightColumnException(f'Straight column[{straight_column.to_dict()}] is not supported.')
 
 	def translate_straight_group_bys(
 			self, statement: SQLAlchemyStatement, straight_columns: List[EntityStraightColumn]) -> SQLAlchemyStatement:
 		group_columns = ArrayHelper(straight_columns) \
```

### Comparing `watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/table_defs.py` & `watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/table_defs.py`

 * *Files 10% similar despite different names*

```diff
@@ -303,20 +303,90 @@
 table_achievement_plugin_tasks = Table(
 	'achievement_plugin_tasks', meta_data,
 	create_pk('achievement_task_id'), create_tuple_id_column('achievement_id'), create_tuple_id_column('plugin_id'),
 	create_str('status', 10, False), create_str('url', 512),
 	create_tenant_id(), create_user_id(),
 	*create_tuple_audit_columns()
 )
-table_oss_collector_competitive_lock = Table(
-	'collector_competitive_lock', meta_data,
-	create_pk('lock_id'), create_str('resource_id', 500),
+table_competitive_lock = Table(
+	'competitive_lock', meta_data,
+	create_pk('lock_id', Integer), create_str('resource_id', 500),
+	create_datetime('registered_at', False), create_tenant_id()
+)
+table_scheduled_task = Table(
+	'scheduled_task', meta_data,
+	create_pk('task_id', Integer), create_str('resource_id', 500),
+	create_str('topic_code', 50), create_json('content'),
 	create_str('model_name', 20), create_str('object_id', 100),
-	create_datetime('registered_at', False), create_tenant_id(),
-	create_int('status', False)
+	create_json('depend_on'), create_json('parent_task_id'),
+	create_int('is_finished', False), create_json('result'),
+	create_tenant_id(),
+	*create_tuple_audit_columns()
+)
+table_collector_model_config = Table(
+	'collector_model_config', meta_data,
+	create_pk('model_id'), create_str('model_name', 50),
+	create_json('depend_on'), create_str('raw_topic_code', 50),
+	create_int('is_paralleled'),
+	create_tenant_id(), *create_tuple_audit_columns(),
+	create_optimistic_lock()
+)
+table_collector_table_config = Table(
+	'collector_table_config', meta_data,
+	create_pk('config_id'), create_str('name', 50),
+	create_str('table_name', 50), create_json('primary_key'), create_str('object_key', 50),
+	create_str('model_name', 50), create_str('parent_name', 50), create_json('join_keys'),
+	create_json('conditions'), create_str('label', 50),
+	create_json('depend_on'), create_int('triggered'),
+	create_str('audit_column', 50), create_str('data_source_id', 50),
+	create_int('is_list'),
+	create_tenant_id(), *create_tuple_audit_columns(),
+	create_optimistic_lock()
+)
+table_trigger_event = Table(
+	'trigger_event', meta_data,
+	create_pk('event_trigger_id', Integer),
+	create_date('start_time'), create_date('end_time'),
+	create_int('is_finished', False),
+	create_tenant_id(), *create_tuple_audit_columns()
+)
+table_trigger_model = Table(
+	'trigger_model', meta_data,
+	create_pk('model_trigger_id', Integer),
+	create_str('model_name', 50),
+	create_int('is_finished', False),
+	create_int('event_trigger_id', False),
+	create_tenant_id(), *create_tuple_audit_columns()
+)
+table_trigger_table = Table(
+	'trigger_table', meta_data,
+	create_pk('table_trigger_id', Integer), create_str('table_name', 50),
+	create_str('model_name', 50), create_int('data_count'),
+	create_int('is_extracted', False),
+	create_int('model_trigger_id', False),
+	create_int('event_trigger_id', False),
+	create_tenant_id(), *create_tuple_audit_columns()
+)
+table_change_data_record = Table(
+	'change_data_record', meta_data,
+	create_pk('change_record_id', Integer), create_str('model_name', 50), create_str('table_name', 50),
+	create_json('data_id'), create_str('root_table_name', 50), create_json('root_data_id'),
+	create_int('is_merged', False), create_json('result'),
+	create_int('table_trigger_id', False), create_int('model_trigger_id', False), create_int('event_trigger_id', False),
+	create_tenant_id(), *create_tuple_audit_columns()
+)
+table_change_data_json = Table(
+	'change_data_json', meta_data,
+	create_pk('change_json_id', Integer), create_str('resource_id', 100),
+	create_str('model_name', 50), create_str('object_id', 50),
+	create_str('table_name', 50), create_json('data_id'),
+	create_json('content'), create_json('depend_on'), create_int('is_posted', False), create_int('task_id', True),
+	create_json('result'),
+	create_int('table_trigger_id', False), create_int('model_trigger_id', False), create_int('event_trigger_id', False),
+	create_tenant_id(), *create_tuple_audit_columns()
 )
 table_operations = Table(
 	'operations', meta_data,
 	create_pk('record_id'), create_str('operation_type', 20),
 	create_str('tuple_type', 20), create_str('tuple_key', 20),
 	create_str('tuple_id', 50), create_json('content'), create_str('version_num', 50),
 	create_tenant_id(), *create_tuple_audit_columns()
@@ -369,17 +439,26 @@
 	# indicator
 	'buckets': table_buckets,
 	'indicators': table_indicators,
 	'inspections': table_inspections,
 	'achievements': table_achievements,
 	'objective_analysis': table_objective_analysis,
 	'achievement_plugin_tasks': table_achievement_plugin_tasks,
-	'oss_collector_competitive_lock': table_oss_collector_competitive_lock,
+	'competitive_lock': table_competitive_lock,
+	'scheduled_task': table_scheduled_task,
 	'operations': table_operations,
-	'package_versions': table_package_versions
+	'package_versions': table_package_versions,
+	# collector
+	'collector_model_config': table_collector_model_config,
+	'collector_table_config': table_collector_table_config,
+	'trigger_event': table_trigger_event,
+	'trigger_model': table_trigger_model,
+	'trigger_table': table_trigger_table,
+	'change_data_record': table_change_data_record,
+	'change_data_json': table_change_data_json
 
 }
 
 
 # noinspection DuplicatedCode
 def register_meta_table(table_name: str, table_def: Table) -> None:
 	tables[table_name] = table_def
```

### Comparing `watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/table_defs_helper.py` & `watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/table_defs_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/topic_data_storage_rds.py` & `watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/topic_data_storage_rds.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_rds-16.4.7/src/watchmen_storage_rds/topic_table_generate.py` & `watchmen_storage_rds-16.4.9/src/watchmen_storage_rds/topic_table_generate.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_rds-16.4.7/setup.py` & `watchmen_storage_rds-16.4.9/setup.py`

 * *Files 11% similar despite different names*

```diff
@@ -7,19 +7,19 @@
 packages = \
 ['watchmen_storage_rds']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['SQLAlchemy==1.4.35', 'watchmen-storage==16.4.7']
+['SQLAlchemy==1.4.35', 'watchmen-storage==16.4.9']
 
 setup_kwargs = {
     'name': 'watchmen-storage-rds',
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

### Comparing `watchmen_storage_rds-16.4.7/PKG-INFO` & `watchmen_storage_rds-16.4.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 Metadata-Version: 2.1
 Name: watchmen-storage-rds
-Version: 16.4.7
+Version: 16.4.9
 Summary: 
 License: MIT
 Author: botlikes
 Author-email: 75356972+botlikes456@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Requires-Dist: SQLAlchemy (==1.4.35)
-Requires-Dist: watchmen-storage (==16.4.7)
+Requires-Dist: watchmen-storage (==16.4.9)
```

