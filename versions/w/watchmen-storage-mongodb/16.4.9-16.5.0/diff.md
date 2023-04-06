# Comparing `tmp/watchmen_storage_mongodb-16.4.9.tar.gz` & `tmp/watchmen_storage_mongodb-16.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_storage_mongodb-16.4.9.tar", max compression
+gzip compressed data, was "watchmen_storage_mongodb-16.5.0.tar", max compression
```

## Comparing `watchmen_storage_mongodb-16.4.9.tar` & `watchmen_storage_mongodb-16.5.0.tar`

### file list

```diff
@@ -1,16 +1,15 @@
--rw-r--r--   0        0        0     1061 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/LICENSE
--rw-r--r--   0        0        0      460 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/pyproject.toml
--rw-r--r--   0        0        0      210 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/__init__.py
--rw-r--r--   0        0        0      703 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/codes_options.py
--rw-r--r--   0        0        0     1308 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/data_source_mongo.py
--rw-r--r--   0        0        0     2540 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/document_defs_helper.py
--rw-r--r--   0        0        0    16846 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/document_defs_mongo.py
--rw-r--r--   0        0        0     2541 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/document_mongo.py
--rw-r--r--   0        0        0     5220 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/engine_mongo.py
--rw-r--r--   0        0        0      509 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/sort_build.py
--rw-r--r--   0        0        0    21084 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/storage_mongo.py
--rw-r--r--   0        0        0     1899 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/storage_mongo_configuration.py
--rw-r--r--   0        0        0    11657 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/topic_document_generate.py
--rw-r--r--   0        0        0    24666 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/where_build.py
--rw-r--r--   0        0        0      738 1970-01-01 00:00:00.000000 watchmen_storage_mongodb-16.4.9/setup.py
--rw-r--r--   0        0        0      531 1970-01-01 00:00:00.000000 watchmen_storage_mongodb-16.4.9/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/LICENSE
+-rw-r--r--   0        0        0      460 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/pyproject.toml
+-rw-r--r--   0        0        0      210 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/__init__.py
+-rw-r--r--   0        0        0      703 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/codes_options.py
+-rw-r--r--   0        0        0     1308 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/data_source_mongo.py
+-rw-r--r--   0        0        0     2540 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/document_defs_helper.py
+-rw-r--r--   0        0        0    17650 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/document_defs_mongo.py
+-rw-r--r--   0        0        0     2541 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/document_mongo.py
+-rw-r--r--   0        0        0     5220 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/engine_mongo.py
+-rw-r--r--   0        0        0      509 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/sort_build.py
+-rw-r--r--   0        0        0    21084 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/storage_mongo.py
+-rw-r--r--   0        0        0     1899 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/storage_mongo_configuration.py
+-rw-r--r--   0        0        0    11657 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/topic_document_generate.py
+-rw-r--r--   0        0        0    24666 2023-04-06 09:13:10.412011 watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/where_build.py
+-rw-r--r--   0        0        0      531 1970-01-01 00:00:00.000000 watchmen_storage_mongodb-16.5.0/PKG-INFO
```

### Comparing `watchmen_storage_mongodb-16.4.9/LICENSE` & `watchmen_storage_mongodb-16.5.0/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/codes_options.py` & `watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/codes_options.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/data_source_mongo.py` & `watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/data_source_mongo.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/document_defs_helper.py` & `watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/document_defs_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/document_defs_mongo.py` & `watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/document_defs_mongo.py`

 * *Files 4% similar despite different names*

```diff
@@ -227,14 +227,15 @@
 	columns=[
 		create_pk('lock_id'), create_tuple_id_column('tenant_id', False), create_tuple_id_column('scheduler_id', False),
 		create_str('frequency', False), create_datetime('process_date', False), create_int('row_count', False),
 		create_str('status', False),
 		create_tuple_id_column('user_id', False), create_datetime('created_at', False)
 	]
 )
+# system
 table_collector_competitive_lock = MongoDocument(
 	name='collector_competitive_lock',
 	columns=[
 		create_pk('lock_id'), create_str('resource_id', False),
 		create_str('model_name', False), create_str('object_id', False),
 		create_datetime('registered_at', False), create_tenant_id(),
 		create_int('status', False)
@@ -259,15 +260,15 @@
 	]
 )
 
 # gui
 table_favorites = MongoDocument(
 	name='favorites',
 	columns=[
-		create_json('connected_space_ids'), create_json('dashboard_ids'),
+		create_json('connected_space_ids'), create_json('dashboard_ids'), create_json('derived_objective_ids'),
 		create_tenant_id(), create_user_id(primary_key=True), create_last_visit_time()
 	]
 )
 table_last_snapshot = MongoDocument(
 	name='last_snapshots',
 	columns=[
 		create_str('language'),
@@ -330,108 +331,129 @@
 		create_str('frequency', False), create_datetime('process_date', False),
 		create_str('status', False),
 		create_tuple_id_column('user_id', False), create_datetime('created_at', False)
 	]
 )
 # indicator
 # noinspection DuplicatedCode
+table_buckets = MongoDocument(
+	name='buckets',
+	columns=[
+		create_pk('bucket_id'), create_str('name'),
+		create_str('type', False), create_str('include'),
+		create_str('measure'), create_tuple_id_column('enum_id'),
+		create_json('segments'), create_description(),
+		create_tenant_id(), *create_tuple_audit_columns(), create_optimistic_lock()
+	]
+)
 table_indicators = MongoDocument(
 	name='indicators',
 	columns=[
 		create_pk('indicator_id'), create_str('name'),
 		create_tuple_id_column('topic_or_subject_id'), create_tuple_id_column('factor_id'),
 		create_str('aggregate_arithmetic', False),
 		create_str('base_on'),
 		create_str('category_1'), create_str('category_2'), create_str('category_3'),
 		create_json('value_buckets'), create_json('relevants'),
 		create_json('filter'),
 		create_description(),
 		create_tenant_id(), *create_tuple_audit_columns(), create_optimistic_lock()
 	]
 )
-table_buckets = MongoDocument(
-	name='buckets',
+table_objectives = MongoDocument(
+	name='objectives',
 	columns=[
-		create_pk('bucket_id'), create_str('name'),
-		create_str('type', False), create_str('include'),
-		create_str('measure'), create_tuple_id_column('enum_id'),
-		create_json('segments'), create_description(),
-		create_tenant_id(), *create_tuple_audit_columns(), create_optimistic_lock()
-	]
-)
-
-# noinspection DuplicatedCode
-table_inspections = MongoDocument(
-	name='inspections',
-	columns=[
-		create_pk('inspection_id'), create_str('name'),
-		create_tuple_id_column('indicator_id'),
-		create_json('aggregate_arithmetics'),
-		create_json('measures'),
-		create_str('time_range_measure'), create_tuple_id_column('time_range_factor_id'),
-		create_json('time_ranges'),
-		create_str('measure_on_time'), create_tuple_id_column('measure_on_time_factor_id'),
-		create_json('criteria'),
-		create_tenant_id(), *create_tuple_audit_columns(), create_optimistic_lock()
-	]
-)
-table_achievements = MongoDocument(
-	name='achievements',
-	columns=[
-		create_pk('achievement_id'), create_str('name'),
-		create_str('time_range_type'), create_str('time_range_year'), create_str('time_range_month'),
-		create_bool('compare_with_prev_time_range'), create_bool('final_score_is_ratio'),
-		create_json('indicators'), create_json('plugin_ids'),
+		create_pk('objective_id'), create_str('name'),
 		create_description(),
+		create_json('time_frame'), create_json('targets'), create_json('variables'), create_json('factors'),
+		create_json('group_ids'),
 		create_tenant_id(), *create_tuple_audit_columns(), create_optimistic_lock()
 	]
 )
-table_objective_analysis = MongoDocument(
-	name='objective_analysis',
+table_derived_objectives = MongoDocument(
+	name='derived_objectives',
 	columns=[
-		create_pk('analysis_id'), create_str('title'),
-		create_description(), create_json('perspectives'),
-		create_tenant_id(), *create_tuple_audit_columns(), create_optimistic_lock()
+		create_pk('derived_objective_id'),
+		create_str('name', False), create_description(),
+		create_tuple_id_column('objective_id', False), create_json('definition'),
+		create_tenant_id(), create_user_id(), create_last_visit_time(), *create_tuple_audit_columns()
 	]
 )
+
 table_achievement_plugin_tasks = MongoDocument(
 	name='achievement_plugin_tasks',
 	columns=[
 		create_pk('achievement_task_id'), create_tuple_id_column('achievement_id'), create_tuple_id_column('plugin_id'),
 		create_str('status'), create_str('url'),
 		create_tenant_id(), create_user_id(),
 		*create_tuple_audit_columns()
 	]
 )
 
+table_subscription_event = MongoDocument(
+	'subscription_events',
+	columns=[
+		create_pk('subscription_event_id'),
+		create_tuple_id_column('notification_id'),
+		create_tuple_id_column('event_id'),
+		create_tuple_id_column("source_id"),
+		create_str('weekday'), create_str('day'),
+		create_int('hour'), create_int('minute'),
+		create_bool('enabled', False),
+		create_int('status'),
+		create_str('frequency', False),
+		create_user_id(),
+		create_tenant_id(), *create_tuple_audit_columns(), create_optimistic_lock()
+
+	]
+)
+
+table_notification_definition = MongoDocument(
+	'notification_definitions', columns=[
+		create_pk('notification_id'),
+		create_str('type'),
+		create_json('params'),
+		create_user_id(),
+		create_tenant_id(), *create_tuple_audit_columns(), create_optimistic_lock()
+	]
+)
+
+table_subscription_event_locks = MongoDocument(
+	'subscription_event_locks', columns=[
+		create_pk('subscription_event_lock_id'), create_tuple_id_column('tenant_id', False),
+		create_tuple_id_column('subscription_event_id', False),
+		create_datetime('process_date', False),
+		create_str('status', False),
+		create_tuple_id_column('user_id', False),
+		create_datetime('created_at', False)
+	]
+)
+
 # noinspection DuplicatedCode
 tables: Dict[str, MongoDocument] = {
 	# snowflake workers
 	SNOWFLAKE_WORKER_ID_TABLE: table_snowflake_competitive_workers,
 	# system
 	'pats': table_pats,
 	'tenants': table_tenants,
 	'external_writers': table_external_writers,
 	'plugins': table_plugins,
 	'data_sources': table_data_sources,
 	'key_stores': table_key_stores,
-	'operations': table_operations,
-	'versions': table_versions,
 	# admin
 	'users': table_users,
 	'user_groups': table_user_groups,
 	'spaces': table_spaces,
 	'enums': table_enums,
 	'enum_items': table_enum_items,
 	'topics': table_topics,
 	'pipelines': table_pipelines,
 	'pipeline_graphics': table_pipeline_graphics,
 	'snapshot_schedulers': table_snapshot_schedulers,
 	'snapshot_job_locks': table_snapshot_job_locks,
-	'collector_competitive_lock': table_collector_competitive_lock,
 	# console
 	'connected_spaces': table_connected_spaces,
 	'connected_space_graphics': table_connected_space_graphics,
 	'subjects': table_subjects,
 	'reports': table_reports,
 	'dashboards': table_dashboards,
 	# gui
@@ -443,20 +465,27 @@
 	# dqc
 	'catalogs': table_catalogs,
 	'monitor_rules': table_monitor_rules,
 	'monitor_job_locks': table_monitor_job_locks,
 	# indicator
 	'buckets': table_buckets,
 	'indicators': table_indicators,
-	'inspections': table_inspections,
-	'achievements': table_achievements,
-	'objective_analysis': table_objective_analysis,
+	'objectives': table_objectives,
+	'derived_objectives': table_derived_objectives,
 	'achievement_plugin_tasks': table_achievement_plugin_tasks,
+	# system
+	'collector_competitive_lock': table_collector_competitive_lock,
+	'operations': table_operations,
+	'package_versions': table_package_versions,
+	# webhook
+	'subscription_event_locks': table_subscription_event_locks,
+	'subscription_events': table_subscription_event,
+	'notification_definitions': table_notification_definition,
 	# trino
-	'_schema': table_trino_schema
+	'_schema': table_trino_schema,
 }
 
 # noinspection DuplicatedCode
 topic_documents: Dict[TopicId, Tuple[MongoDocument, datetime]] = {}
 
 
 def find_document(table_name: str) -> MongoDocument:
```

### Comparing `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/document_mongo.py` & `watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/document_mongo.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/engine_mongo.py` & `watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/engine_mongo.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/storage_mongo.py` & `watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/storage_mongo.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/storage_mongo_configuration.py` & `watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/storage_mongo_configuration.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/topic_document_generate.py` & `watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/topic_document_generate.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/where_build.py` & `watchmen_storage_mongodb-16.5.0/src/watchmen_storage_mongodb/where_build.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.9/PKG-INFO` & `watchmen_storage_mongodb-16.5.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 Metadata-Version: 2.1
 Name: watchmen-storage-mongodb
-Version: 16.4.9
+Version: 16.5.0
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
 Requires-Dist: pymongo (>=4.1.0,<5.0.0)
-Requires-Dist: watchmen-storage (==16.4.9)
+Requires-Dist: watchmen-storage (==16.5.0)
```

