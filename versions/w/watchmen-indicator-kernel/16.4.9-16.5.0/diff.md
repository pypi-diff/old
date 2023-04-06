# Comparing `tmp/watchmen_indicator_kernel-16.4.9.tar.gz` & `tmp/watchmen_indicator_kernel-16.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_indicator_kernel-16.4.9.tar", max compression
+gzip compressed data, was "watchmen_indicator_kernel-16.5.0.tar", max compression
```

## Comparing `watchmen_indicator_kernel-16.4.9.tar` & `watchmen_indicator_kernel-16.5.0.tar`

### file list

```diff
@@ -1,30 +1,39 @@
--rw-r--r--   0        0        0     1281 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/pyproject.toml
--rw-r--r--   0        0        0        0 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/__init__.py
--rw-r--r--   0        0        0      109 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/common/__init__.py
--rw-r--r--   0        0        0       49 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/common/exception.py
--rw-r--r--   0        0        0      521 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/common/settings.py
--rw-r--r--   0        0        0      250 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/__init__.py
--rw-r--r--   0        0        0     2163 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/achievement_data_helper.py
--rw-r--r--   0        0        0     3933 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/achievement_data_service.py
--rw-r--r--   0        0        0     1088 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/bucket_helper.py
--rw-r--r--   0        0        0     9526 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/indicator_criteria_service.py
--rw-r--r--   0        0        0     1330 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/indicator_helper.py
--rw-r--r--   0        0        0     2030 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/inspection_data_helper.py
--rw-r--r--   0        0        0     4703 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/inspection_data_service.py
--rw-r--r--   0        0        0     4177 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/subject_base_achievement_data_service.py
--rw-r--r--   0        0        0    11925 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/subject_base_inspection_data_service.py
--rw-r--r--   0        0        0      786 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/subject_helper.py
--rw-r--r--   0        0        0     5002 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/topic_base_achievement_data_service.py
--rw-r--r--   0        0        0    19431 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/topic_base_inspection_data_service.py
--rw-r--r--   0        0        0      741 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/topic_helper.py
--rw-r--r--   0        0        0      324 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/__init__.py
--rw-r--r--   0        0        0     3272 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/achievement_service.py
--rw-r--r--   0        0        0     1762 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/achievement_task_service.py
--rw-r--r--   0        0        0     8647 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/bucket_service.py
--rw-r--r--   0        0        0     6603 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/indicator_service.py
--rw-r--r--   0        0        0     2796 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/inspection_service.py
--rw-r--r--   0        0        0     2134 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/objective_analysis_service.py
--rw-r--r--   0        0        0       46 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/plugin/__init__.py
--rw-r--r--   0        0        0      678 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/plugin/connector.py
--rw-r--r--   0        0        0     1298 1970-01-01 00:00:00.000000 watchmen_indicator_kernel-16.4.9/setup.py
--rw-r--r--   0        0        0     1228 1970-01-01 00:00:00.000000 watchmen_indicator_kernel-16.4.9/PKG-INFO
+-rw-r--r--   0        0        0     1281 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/__init__.py
+-rw-r--r--   0        0        0       86 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/common/__init__.py
+-rw-r--r--   0        0        0       49 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/common/exception.py
+-rw-r--r--   0        0        0      329 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/common/settings.py
+-rw-r--r--   0        0        0      286 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/__init__.py
+-rw-r--r--   0        0        0       53 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/inspection/__init__.py
+-rw-r--r--   0        0        0     1901 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/inspection/data_helper.py
+-rw-r--r--   0        0        0     4327 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/inspection/inspection_data_service.py
+-rw-r--r--   0        0        0    11588 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/inspection/subject_base_service.py
+-rw-r--r--   0        0        0    19385 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/inspection/topic_base_service.py
+-rw-r--r--   0        0        0      140 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/objective/__init__.py
+-rw-r--r--   0        0        0      313 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/objective/data_helper.py
+-rw-r--r--   0        0        0    27145 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/objective/data_service.py
+-rw-r--r--   0        0        0       59 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/objective_factor/__init__.py
+-rw-r--r--   0        0        0     2678 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/objective_factor/data_helper.py
+-rw-r--r--   0        0        0    11941 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/objective_factor/data_service.py
+-rw-r--r--   0        0        0    21400 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/objective_factor/objective_criteria_service.py
+-rw-r--r--   0        0        0    10799 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/objective_factor/subject_base_service.py
+-rw-r--r--   0        0        0     8341 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/objective_factor/topic_base_service.py
+-rw-r--r--   0        0        0      397 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/__init__.py
+-rw-r--r--   0        0        0     1088 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/bucket.py
+-rw-r--r--   0        0        0      979 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/derived_objective.py
+-rw-r--r--   0        0        0     1051 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/enum.py
+-rw-r--r--   0        0        0      284 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/factor.py
+-rw-r--r--   0        0        0     1330 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/indicator.py
+-rw-r--r--   0        0        0     3110 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/parameter.py
+-rw-r--r--   0        0        0      786 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/subject.py
+-rw-r--r--   0        0        0    12305 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/time_frame.py
+-rw-r--r--   0        0        0     1074 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/topic.py
+-rw-r--r--   0        0        0      268 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/meta/__init__.py
+-rw-r--r--   0        0        0     1762 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/meta/achievement_task_service.py
+-rw-r--r--   0        0        0     8647 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/meta/bucket_service.py
+-rw-r--r--   0        0        0     4960 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/meta/derived_objective_service.py
+-rw-r--r--   0        0        0     6695 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/meta/indicator_service.py
+-rw-r--r--   0        0        0     5783 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/meta/objective_service.py
+-rw-r--r--   0        0        0       46 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/plugin/__init__.py
+-rw-r--r--   0        0        0      678 2023-04-06 09:13:10.388010 watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/plugin/connector.py
+-rw-r--r--   0        0        0     1228 1970-01-01 00:00:00.000000 watchmen_indicator_kernel-16.5.0/PKG-INFO
```

### Comparing `watchmen_indicator_kernel-16.4.9/pyproject.toml` & `watchmen_indicator_kernel-16.5.0/pyproject.toml`

 * *Files 7% similar despite different names*

```diff
@@ -1,28 +1,28 @@
 [tool.poetry]
 name = "watchmen-indicator-kernel"
-version = "16.4.9"
+version = "16.5.0"
 description = ""
 authors = ["botlikes <75356972+botlikes456@users.noreply.github.com>"]
 license = "MIT"
 packages = [
     { include = "watchmen_indicator_kernel", from = "src" }
 ]
 
 [tool.poetry.dependencies]
 python = "^3.9"
-watchmen-inquiry-kernel = "16.4.9"
-watchmen-inquiry-trino = { version = "16.4.9", optional = true }
-watchmen-storage-mysql = { version = "16.4.9", optional = true }
-watchmen-storage-oracle = { version = "16.4.9", optional = true }
-watchmen-storage-mongodb = { version = "16.4.9", optional = true }
-watchmen-storage-mssql = { version = "16.4.9", optional = true }
-watchmen-storage-postgresql = { version = "16.4.9", optional = true }
-watchmen-storage-oss = { version = "16.4.9", optional = true }
-watchmen-storage-s3 = { version = "16.4.9", optional = true }
+watchmen-inquiry-kernel = "16.5.0"
+watchmen-inquiry-trino = { version = "16.5.0", optional = true }
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

### Comparing `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/bucket_helper.py` & `watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/bucket.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/indicator_helper.py` & `watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/indicator.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/inspection_data_helper.py` & `watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/inspection/data_helper.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,42 +1,40 @@
+from datetime import datetime
+
 from watchmen_auth import PrincipalService
-from watchmen_indicator_kernel.common import IndicatorKernelException
-from watchmen_model.common import SubjectId, TopicId
-from watchmen_model.indicator import Indicator, IndicatorBaseOn, Inspection
-from watchmen_utilities import is_not_blank
-from .indicator_helper import ask_indicator
 from .inspection_data_service import InspectionDataService
-from .subject_base_inspection_data_service import SubjectBaseInspectionDataService
-from .subject_helper import ask_subject
-from .topic_base_inspection_data_service import TopicBaseInspectionDataService
-from .topic_helper import ask_topic
-
-
-def get_topic_base_service(
-		inspection: Inspection, indicator: Indicator, topic_id: TopicId,
-		principal_service: PrincipalService
-) -> TopicBaseInspectionDataService:
-	return TopicBaseInspectionDataService(
-		inspection, indicator, ask_topic(topic_id, principal_service), principal_service)
-
 
-def get_subject_base_service(
-		inspection: Inspection, indicator: Indicator, subject_id: SubjectId,
-		principal_service: PrincipalService
-) -> SubjectBaseInspectionDataService:
-	return SubjectBaseInspectionDataService(
-		inspection, indicator, ask_subject(subject_id, principal_service), principal_service)
 
+# def get_topic_base_service(
+# 		inspection: Inspection, indicator: Indicator, topic_id: TopicId,
+# 		dt: datetime,
+# 		principal_service: PrincipalService
+# ) -> TopicBaseInspectionDataService:
+# 	topic = ask_topic(topic_id, principal_service)
+# 	clone_inspection = redress_inspection(inspection, topic, dt, principal_service)
+# 	return TopicBaseInspectionDataService(clone_inspection, indicator, topic, principal_service)
+#
+#
+# def get_subject_base_service(
+# 		inspection: Inspection, indicator: Indicator, subject_id: SubjectId,
+# 		dt: datetime,
+# 		principal_service: PrincipalService
+# ) -> SubjectBaseInspectionDataService:
+# 	subject = ask_subject(subject_id, principal_service)
+# 	clone_inspection = redress_inspection(inspection, subject, dt, principal_service)
+# 	return SubjectBaseInspectionDataService(clone_inspection, indicator, subject, principal_service)
 
-def get_inspection_data_service(inspection: Inspection, principal_service: PrincipalService) -> InspectionDataService:
+# TODO REFACTOR-OBJECTIVE ACHIEVEMENT BREAK DOWN DATA SERVICE, ENTRYPOINT
+def get_inspection_data_service(dt: datetime, principal_service: PrincipalService) -> InspectionDataService:
 	"""
 	to identify that given inspection is based on topic or subject
 	"""
-	indicator = ask_indicator(inspection.indicatorId, principal_service)
-	topic_or_subject_id = indicator.topicOrSubjectId
-	base_on = indicator.baseOn
-	if base_on == IndicatorBaseOn.TOPIC and is_not_blank(topic_or_subject_id):
-		return get_topic_base_service(inspection, indicator, topic_or_subject_id, principal_service)
-	elif base_on == IndicatorBaseOn.SUBJECT and is_not_blank(topic_or_subject_id):
-		return get_subject_base_service(inspection, indicator, topic_or_subject_id, principal_service)
-	else:
-		raise IndicatorKernelException('Indicator is not based on topic or subject, not supported yet.')
+	# indicator = ask_indicator(inspection.indicatorId, principal_service)
+	# topic_or_subject_id = indicator.topicOrSubjectId
+	# base_on = indicator.baseOn
+	# if base_on == IndicatorBaseOn.TOPIC and is_not_blank(topic_or_subject_id):
+	# 	return get_topic_base_service(inspection, indicator, topic_or_subject_id, dt, principal_service)
+	# elif base_on == IndicatorBaseOn.SUBJECT and is_not_blank(topic_or_subject_id):
+	# 	return get_subject_base_service(inspection, indicator, topic_or_subject_id, dt, principal_service)
+	# else:
+	# 	raise IndicatorKernelException('Indicator is not based on topic or subject, not supported yet.')
+	pass
```

### Comparing `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/inspection_data_service.py` & `watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/inspection/inspection_data_service.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,103 +1,94 @@
-from abc import abstractmethod
-from typing import List, Optional, Tuple, Union
+from watchmen_indicator_kernel.data.objective_factor.objective_criteria_service import ObjectiveCriteriaService
 
-from watchmen_auth import PrincipalService
-from watchmen_model.admin import Factor, FactorType
-from watchmen_model.common import ComputedParameter, DataResult, DataResultSet, FactorId, ParameterComputeType, \
-	ParameterKind, SubjectDatasetColumnId, TopicFactorParameter, TopicId
-from watchmen_model.console import ReportIndicator, ReportIndicatorArithmetic, SubjectDatasetColumn
-from watchmen_model.console.subject import SubjectColumnArithmetic
-from watchmen_model.indicator import IndicatorAggregateArithmetic, Inspection, MeasureMethod
-from watchmen_utilities import is_blank
-from .indicator_criteria_service import IndicatorCriteriaService
 
-
-class InspectionDataService(IndicatorCriteriaService):
-	def __init__(self, inspection: Inspection, principal_service: PrincipalService):
-		super().__init__(principal_service)
-		self.inspection = inspection
-		self.TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID: str = 'time_group_year_or_month_column'
-
-	def has_time_group(self) -> Tuple[bool, Optional[FactorId], Optional[MeasureMethod]]:
-		measure_on_time_factor_id = self.inspection.measureOnTimeFactorId
-		if is_blank(measure_on_time_factor_id):
-			return False, None, None
-		measure_on_time = self.inspection.measureOnTime
-		if measure_on_time is None:
-			return False, None, None
-
-		return True, measure_on_time_factor_id, measure_on_time
-
-	# noinspection PyMethodMayBeStatic
-	def is_datetime_factor(self, factor_or_type: Union[Factor, FactorType]) -> bool:
-		factor_type = factor_or_type.type if isinstance(factor_or_type, Factor) else factor_or_type
-		return \
-			factor_type == FactorType.DATETIME \
-			or factor_type == FactorType.FULL_DATETIME \
-			or factor_type == FactorType.DATE \
-			or factor_type == FactorType.DATE_OF_BIRTH
-
-	def fake_time_group_year_or_month_column(
-			self, topic_id: TopicId, factor_id: FactorId, name: str) -> Optional[SubjectDatasetColumn]:
-		"""
-		fake year or month column according to measureOnTime.
-		returns column only when measure on year or month, otherwise return none.
-		"""
-		# fake a new column into subject
-		if self.inspection.measureOnTime == MeasureMethod.YEAR:
-			return SubjectDatasetColumn(
-				columnId=self.TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID,
-				parameter=ComputedParameter(
-					kind=ParameterKind.COMPUTED,
-					type=ParameterComputeType.YEAR_OF,
-					parameters=[
-						TopicFactorParameter(kind=ParameterKind.TOPIC, topicId=topic_id, factorId=factor_id)
-					]
-				),
-				alias=f'{name}_YEAR_',
-				arithmetic=SubjectColumnArithmetic.NONE
-			)
-		elif self.inspection.measureOnTime == MeasureMethod.MONTH:
-			return SubjectDatasetColumn(
-				columnId=self.TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID,
-				parameter=ComputedParameter(
-					kind=ParameterKind.COMPUTED,
-					type=ParameterComputeType.MONTH_OF,
-					parameters=[
-						TopicFactorParameter(kind=ParameterKind.TOPIC, topicId=topic_id, factorId=factor_id)
-					]
-				),
-				alias=f'{name}_MONTH_',
-				arithmetic=SubjectColumnArithmetic.NONE
-			)
-		else:
-			return None
-
-	def fake_report_indicator(self, indicators: List[ReportIndicator], columnId: SubjectDatasetColumnId) -> None:
-		arithmetics = self.inspection.aggregateArithmetics
-		if arithmetics is None or len(arithmetics) == 0:
-			indicators.append(
-				ReportIndicator(columnId=columnId, name='_SUM_', arithmetic=ReportIndicatorArithmetic.SUMMARY))
-		else:
-			if IndicatorAggregateArithmetic.COUNT in arithmetics or IndicatorAggregateArithmetic.COUNT.value in arithmetics:
-				indicators.append(
-					ReportIndicator(columnId=columnId, name='_COUNT_', arithmetic=ReportIndicatorArithmetic.COUNT))
-			if IndicatorAggregateArithmetic.SUM in arithmetics or IndicatorAggregateArithmetic.SUM.value in arithmetics:
-				indicators.append(
-					ReportIndicator(columnId=columnId, name='_SUM_', arithmetic=ReportIndicatorArithmetic.SUMMARY))
-			if IndicatorAggregateArithmetic.AVG in arithmetics or IndicatorAggregateArithmetic.AVG.value in arithmetics:
-				indicators.append(
-					ReportIndicator(columnId=columnId, name='_AVG_', arithmetic=ReportIndicatorArithmetic.AVERAGE))
-			if IndicatorAggregateArithmetic.MAX in arithmetics or IndicatorAggregateArithmetic.MAX.value in arithmetics:
-				indicators.append(
-					ReportIndicator(columnId=columnId, name='_MAX_', arithmetic=ReportIndicatorArithmetic.MAXIMUM))
-			if IndicatorAggregateArithmetic.MIN in arithmetics or IndicatorAggregateArithmetic.MIN.value in arithmetics:
-				indicators.append(
-					ReportIndicator(columnId=columnId, name='_MIN_', arithmetic=ReportIndicatorArithmetic.MINIMUM))
-
-	@abstractmethod
-	def find(self) -> DataResult:
-		pass
-
-	def find_data(self) -> DataResultSet:
-		return self.find().data
+# TODO REFACTOR-OBJECTIVE ACHIEVEMENT BREAK DOWN DATA SERVICE
+class InspectionDataService(ObjectiveCriteriaService):
+	pass
+# def __init__(self, inspection: Inspection, principal_service: PrincipalService):
+# 	super().__init__(principal_service)
+# 	self.inspection = inspection
+# 	self.TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID: str = 'time_group_year_or_month_column'
+# #
+# def has_time_group(self) -> Tuple[bool, Optional[FactorId], Optional[MeasureMethod]]:
+# 	measure_on_time_factor_id = self.inspection.measureOnTimeFactorId
+# 	if is_blank(measure_on_time_factor_id):
+# 		return False, None, None
+# 	measure_on_time = self.inspection.measureOnTime
+# 	if measure_on_time is None:
+# 		return False, None, None
+#
+# 	return True, measure_on_time_factor_id, measure_on_time
+# #
+# # # noinspection PyMethodMayBeStatic
+# # def is_datetime_factor(self, factor_or_type: Union[Factor, FactorType]) -> bool:
+# # 	factor_type = factor_or_type.type if isinstance(factor_or_type, Factor) else factor_or_type
+# # 	return \
+# # 		factor_type == FactorType.DATETIME \
+# # 		or factor_type == FactorType.FULL_DATETIME \
+# # 		or factor_type == FactorType.DATE \
+# # 		or factor_type == FactorType.DATE_OF_BIRTH
+# #
+# def fake_time_group_year_or_month_column(
+# 		self, topic_id: TopicId, factor_id: FactorId, name: str) -> Optional[SubjectDatasetColumn]:
+# 	"""
+# 	fake year or month column according to measureOnTime.
+# 	returns column only when measure on year or month, otherwise return none.
+# 	"""
+# 	# fake a new column into subject
+# 	if self.inspection.measureOnTime == MeasureMethod.YEAR:
+# 		return SubjectDatasetColumn(
+# 			columnId=self.TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID,
+# 			parameter=ComputedParameter(
+# 				kind=ParameterKind.COMPUTED,
+# 				type=ParameterComputeType.YEAR_OF,
+# 				parameters=[
+# 					TopicFactorParameter(kind=ParameterKind.TOPIC, topicId=topic_id, factorId=factor_id)
+# 				]
+# 			),
+# 			alias=f'{name}_YEAR_',
+# 			arithmetic=SubjectColumnArithmetic.NONE
+# 		)
+# 	elif self.inspection.measureOnTime == MeasureMethod.MONTH:
+# 		return SubjectDatasetColumn(
+# 			columnId=self.TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID,
+# 			parameter=ComputedParameter(
+# 				kind=ParameterKind.COMPUTED,
+# 				type=ParameterComputeType.MONTH_OF,
+# 				parameters=[
+# 					TopicFactorParameter(kind=ParameterKind.TOPIC, topicId=topic_id, factorId=factor_id)
+# 				]
+# 			),
+# 			alias=f'{name}_MONTH_',
+# 			arithmetic=SubjectColumnArithmetic.NONE
+# 		)
+# 	else:
+# 		return None
+# #
+# # def fake_report_indicator(self, indicators: List[ReportIndicator], columnId: SubjectDatasetColumnId) -> None:
+# # 	arithmetics = self.inspection.aggregateArithmetics
+# # 	if arithmetics is None or len(arithmetics) == 0:
+# # 		indicators.append(
+# # 			ReportIndicator(columnId=columnId, name='_SUM_', arithmetic=ReportIndicatorArithmetic.SUMMARY))
+# # 	else:
+# # 		if IndicatorAggregateArithmetic.COUNT in arithmetics or IndicatorAggregateArithmetic.COUNT.value in arithmetics:
+# # 			indicators.append(
+# # 				ReportIndicator(columnId=columnId, name='_COUNT_', arithmetic=ReportIndicatorArithmetic.COUNT))
+# # 		if IndicatorAggregateArithmetic.SUM in arithmetics or IndicatorAggregateArithmetic.SUM.value in arithmetics:
+# # 			indicators.append(
+# # 				ReportIndicator(columnId=columnId, name='_SUM_', arithmetic=ReportIndicatorArithmetic.SUMMARY))
+# # 		if IndicatorAggregateArithmetic.AVG in arithmetics or IndicatorAggregateArithmetic.AVG.value in arithmetics:
+# # 			indicators.append(
+# # 				ReportIndicator(columnId=columnId, name='_AVG_', arithmetic=ReportIndicatorArithmetic.AVERAGE))
+# # 		if IndicatorAggregateArithmetic.MAX in arithmetics or IndicatorAggregateArithmetic.MAX.value in arithmetics:
+# # 			indicators.append(
+# # 				ReportIndicator(columnId=columnId, name='_MAX_', arithmetic=ReportIndicatorArithmetic.MAXIMUM))
+# # 		if IndicatorAggregateArithmetic.MIN in arithmetics or IndicatorAggregateArithmetic.MIN.value in arithmetics:
+# # 			indicators.append(
+# # 				ReportIndicator(columnId=columnId, name='_MIN_', arithmetic=ReportIndicatorArithmetic.MINIMUM))
+# #
+# # @abstractmethod
+# # def find(self) -> DataResult:
+# # 	pass
+# #
+# # def find_data(self) -> DataResultSet:
+# # 	return self.find().data
```

### Comparing `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/subject_base_inspection_data_service.py` & `watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/objective_factor/subject_base_service.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,281 +1,243 @@
-from typing import Callable, List, Optional, Tuple
+from decimal import Decimal
+from enum import Enum
+from typing import Optional, Tuple, List, Dict
 
 from watchmen_auth import PrincipalService
-from watchmen_data_kernel.meta import TopicService
-from watchmen_indicator_kernel.common import IndicatorKernelException
-from watchmen_inquiry_kernel.storage import ReportDataService
-from watchmen_model.admin import Factor, Topic
-from watchmen_model.common import ComputedParameter, ConstantParameter, DataResult, DataResultSetRow, \
-	FactorId, ParameterComputeType, ParameterCondition, ParameterExpression, ParameterExpressionOperator, \
-	ParameterJoint, ParameterJointType, ParameterKind, SubjectDatasetColumnId, TopicFactorParameter, TopicId
-from watchmen_model.console import Report, ReportDimension, ReportIndicator, Subject, SubjectDatasetColumn
-from watchmen_model.indicator import Indicator, IndicatorCriteria, Inspection, InspectMeasureOn, InspectMeasureOnType, \
+from watchmen_model.admin import Topic, Factor
+from watchmen_model.common import DataResult, ParameterJoint, ParameterJointType, SubjectId, FactorId, \
+	TopicFactorParameter, TopicId, ComputedParameter, ParameterKind, ParameterComputeType, DataResultSet
+from watchmen_model.console import Report, Subject, SubjectDataset, SubjectDatasetColumn, ReportDimension
+from watchmen_model.console.subject import SubjectColumnArithmetic
+from watchmen_model.indicator import Indicator, IndicatorAggregateArithmetic, Objective, ObjectiveFactorOnIndicator, \
 	MeasureMethod
-from watchmen_utilities import ArrayHelper, is_blank
-from .inspection_data_service import InspectionDataService
+from watchmen_model.indicator.derived_objective import BreakdownTarget, BreakdownDimension, BreakdownDimensionType
+from watchmen_utilities import ArrayHelper
+from .data_service import ObjectiveFactorDataService
+from ..utils import ask_topic, find_factor
+from ..utils.enum import ask_enum
+from ..utils.time_frame import TimeFrame
+from ...common import IndicatorKernelException
 
+TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID: str = 'time_group_year_or_month_column'
 
-def get_report_data_service(subject: Subject, report: Report, principal_service: PrincipalService) -> ReportDataService:
-	return ReportDataService(subject, report, principal_service, True)
 
-
-def get_topic_service(principal_service: PrincipalService) -> TopicService:
-	return TopicService(principal_service)
-
-
-class SubjectBaseInspectionDataService(InspectionDataService):
+class SubjectBaseObjectiveFactorDataService(ObjectiveFactorDataService):
 	def __init__(
-			self, inspection: Inspection, indicator: Indicator, subject: Subject, principal_service: PrincipalService):
-		super().__init__(inspection, principal_service)
-		self.indicator = indicator
+			self, objective: Objective, objective_factor: ObjectiveFactorOnIndicator, indicator: Indicator,
+			subject: Subject,
+			principal_service: PrincipalService):
+		super().__init__(objective, objective_factor, indicator, principal_service)
 		self.subject = subject
-		self.FAKE_TOPIC_ID = '1'
 
-	def ask_column_not_found_message(self, column_id: SubjectDatasetColumnId) -> str:
-		return f'Column[id={column_id}] not found on subject[id={self.subject.subjectId}, name={self.subject.name}].'
+	def get_subject(self) -> Subject:
+		return self.subject
 
-	# noinspection DuplicatedCode
-	def find_column(
-			self, column_id: Optional[SubjectDatasetColumnId],
-			on_factor_id_missed: Callable[[], str]) -> SubjectDatasetColumn:
-		if is_blank(column_id):
-			raise IndicatorKernelException(on_factor_id_missed())
-		column: Optional[SubjectDatasetColumn] = ArrayHelper(self.subject.dataset.columns) \
-			.find(lambda x: x.columnId == column_id)
-		if column is None:
-			raise IndicatorKernelException(self.ask_column_not_found_message(column_id))
-		return column
+	def ask_filter_base_id(self) -> SubjectId:
+		return self.get_subject().subjectId
 
-	def find_columns_of_measure_on_dimension(self) -> List[SubjectDatasetColumn]:
+	def fake_time_frame_to_report(self, report: Report, time_frame: Optional[TimeFrame]):
+		report_filter = self.fake_criteria_to_filter(time_frame)
+		if report_filter is not None:
+			report.filters = report_filter
+
+	def fake_to_subject(self) -> Subject:
 		"""
-		TODO bucket on subject column is not supported yet.
+		to add indicator filter into subject, return a new subject for query purpose, only for this time.
 		"""
-
-		def find_column_of_measure_on(measure_on: InspectMeasureOn) -> Optional[SubjectDatasetColumn]:
-			if measure_on is None or measure_on.type is None or measure_on.type == InspectMeasureOnType.NONE:
-				return None
-			if measure_on.type == InspectMeasureOnType.OTHER:
-				measure_on_factor_id = measure_on.factorId
-				if is_blank(measure_on_factor_id):
-					return None
-				return ArrayHelper(self.subject.dataset.columns).find(lambda x: x.columnId == measure_on_factor_id)
-			elif measure_on.type == InspectMeasureOnType.VALUE:
-				return ArrayHelper(self.subject.dataset.columns).find(lambda x: x.columnId == self.indicator.factorId)
+		subject = self.get_subject()
+		columns = subject.dataset.columns
+		original_subject_filter = subject.dataset.filters
+		if self.has_indicator_filter():
+			if original_subject_filter is not None:
+				subject_filter = ParameterJoint(
+					jointType=ParameterJointType.AND,
+					filters=[original_subject_filter, self.indicator.filter.joint]
+				)
 			else:
-				return None
-
-		return ArrayHelper(self.inspection.measures) \
-			.map(find_column_of_measure_on) \
-			.filter(lambda x: x is not None) \
-			.to_list()
-
-	def find_column_of_time_group_dimension(self) -> Optional[SubjectDatasetColumn]:
-		time_group_existing, measure_on_time_factor_id, _ = self.has_time_group()
-		if time_group_existing:
-			return ArrayHelper(self.subject.dataset.columns).find(lambda x: x.columnId == measure_on_time_factor_id)
+				subject_filter = self.indicator.filter.joint
 		else:
-			return None
+			subject_filter = original_subject_filter
+		return Subject(dataset=SubjectDataset(columns=columns, filters=subject_filter, joins=subject.dataset.joins))
 
-	# noinspection DuplicatedCode
-	def fake_time_range_criteria_to_report(self) -> Optional[ParameterJoint]:
-		time_range_factor_id = self.inspection.timeRangeFactorId
-		if is_blank(time_range_factor_id):
-			return None
-		time_range_column = self.find_column(time_range_factor_id, lambda: 'Time range factor not declared.')
-		time_ranges = ArrayHelper(self.inspection.timeRanges) \
-			.filter(lambda x: x is not None and x.value is not None).to_list()
-		if len(time_ranges) == 0:
-			# no ranges given
-			return None
+	def fake_a_report(self, time_frame: Optional[TimeFrame]) -> Tuple[Subject, Report]:
+		indicator = self.get_indicator()
+		# the indicator factor, actually which is column from subject, is the indicator column of report
+		report_indicator_column_id = indicator.factorId
+		if report_indicator_column_id is None:
+			if self.indicator.aggregateArithmetic != IndicatorAggregateArithmetic.COUNT:
+				raise IndicatorKernelException(
+					f'Indicator[id={indicator.indicatorId}, name={indicator.name}] column not declared, on {self.on_factor_msg()}.')
+			else:
+				# column not declared, and it is a count aggregation, therefore any factor should be ok
+				report_indicator_column_id = self.get_subject().dataset.columns[0].columnId
+		# fake report
+		report = self.fake_to_report(report_indicator_column_id)
+		# fake objective factor to report factor, since they are both based on subject itself
+		self.fake_time_frame_to_report(report, time_frame)
+		subject = self.fake_to_subject()
+		return subject, report
+
+	def ask_value(self, time_frame: Optional[TimeFrame]) -> Optional[Decimal]:
+		subject, report = self.fake_a_report(time_frame)
+		# merge indicator filter to subject filter
+		report_data_service = self.get_report_data_service(subject, report)
+		data_result = report_data_service.find()
+		return self.get_value_from_result(data_result)
 
-		operator = ParameterExpressionOperator.EQUALS if len(time_ranges) == 1 else ParameterExpressionOperator.IN
-		right = time_ranges[0].value if len(time_ranges) == 1 \
-			else ArrayHelper(time_ranges).map(lambda x: x.value).join(',')
-		time_range_measure = self.inspection.timeRangeMeasure
-		if isinstance(time_range_column.parameter, TopicFactorParameter):
-			topic_id = time_range_column.parameter.topicId
-			if is_blank(topic_id):
-				raise IndicatorKernelException(f'Topic not declared for time range factor[id={time_range_factor_id}].')
-			topic = get_topic_service(self.principalService).find_by_id(topic_id)
-			if topic is None:
-				raise IndicatorKernelException(f'Topic[id={topic_id}] not found.')
-			factor_id = time_range_column.parameter.factorId
-			if is_blank(topic_id):
-				raise IndicatorKernelException(f'Factor not declared for time range factor[id={time_range_factor_id}].')
-			factor = ArrayHelper(topic.factors).find(lambda x: x.factorId == factor_id)
-			if factor is None:
-				raise IndicatorKernelException(f'Factor[id={factor_id}] not found on topic[id={topic_id}].')
-			if self.is_datetime_factor(factor):
-				if time_range_measure == MeasureMethod.YEAR:
-					compute_type = ParameterComputeType.YEAR_OF
-				elif time_range_measure == MeasureMethod.MONTH:
-					compute_type = ParameterComputeType.MONTH_OF
-				else:
-					raise IndicatorKernelException(
-						f'Measure method[{time_range_measure}] for factor type[{factor.type}] is not supported.')
-				joint = ParameterJoint(
-					jointType=ParameterJointType.AND,
-					filters=[
-						ParameterExpression(
-							left=ComputedParameter(
-								kind=ParameterKind.COMPUTED,
-								type=compute_type,
-								parameters=[self.build_topic_factor_parameter(self.FAKE_TOPIC_ID, time_range_factor_id)]
-							),
-							operator=operator,
-							right=ConstantParameter(kind=ParameterKind.CONSTANT, value=str(right))
-						)
+	def fake_time_group_year_or_month_column(
+			self, topic_id: TopicId, factor_id: FactorId, name: str) -> Optional[SubjectDatasetColumn]:
+		"""
+		fake year or month column according to measureOnTime.
+		returns column only when measure on year or month, otherwise return none.
+		"""
+		# fake a new column into subject
+		if self.inspection.measureOnTime == MeasureMethod.YEAR:
+			return SubjectDatasetColumn(
+				columnId=TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID,
+				parameter=ComputedParameter(
+					kind=ParameterKind.COMPUTED,
+					type=ParameterComputeType.YEAR_OF,
+					parameters=[
+						TopicFactorParameter(kind=ParameterKind.TOPIC, topicId=topic_id, factorId=factor_id)
 					]
-				)
-			else:
-				joint = ParameterJoint(
-					jointType=ParameterJointType.AND,
-					filters=[
-						ParameterExpression(
-							left=self.build_topic_factor_parameter(self.FAKE_TOPIC_ID, time_range_factor_id),
-							operator=operator,
-							right=ConstantParameter(kind=ParameterKind.CONSTANT, value=str(right))
-						)
+				),
+				alias=f'{name}_YEAR_',
+				arithmetic=SubjectColumnArithmetic.NONE
+			)
+		elif self.inspection.measureOnTime == MeasureMethod.MONTH:
+			return SubjectDatasetColumn(
+				columnId=TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID,
+				parameter=ComputedParameter(
+					kind=ParameterKind.COMPUTED,
+					type=ParameterComputeType.MONTH_OF,
+					parameters=[
+						TopicFactorParameter(kind=ParameterKind.TOPIC, topicId=topic_id, factorId=factor_id)
 					]
-				)
-		else:
-			joint = ParameterJoint(
-				jointType=ParameterJointType.AND,
-				filters=[
-					ParameterExpression(
-						left=self.build_topic_factor_parameter(self.FAKE_TOPIC_ID, time_range_factor_id),
-						operator=operator,
-						right=ConstantParameter(kind=ParameterKind.CONSTANT, value=str(right))
-					)
-				]
+				),
+				alias=f'{name}_MONTH_',
+				arithmetic=SubjectColumnArithmetic.NONE
 			)
-		return joint
+		else:
+			return None
 
-	# noinspection DuplicatedCode
-	def fake_criteria_to_report(self) -> Optional[ParameterJoint]:
-		criteria = ArrayHelper(self.inspection.criteria).filter(lambda x: x is not None).to_list()
-		if len(criteria) == 0:
-			return self.fake_time_range_criteria_to_report()
-
-		def to_condition(a_criteria: IndicatorCriteria) -> ParameterCondition:
-			column = self.find_column(
-				a_criteria.factorId,
-				lambda: f'Column of inspection criteria[{criteria.to_dict()}] not declared.')
-			return self.fake_criteria_to_condition(a_criteria)(self.FAKE_TOPIC_ID, column.columnId)
-
-		return ParameterJoint(
-			jointType=ParameterJointType.AND,
-			filters=ArrayHelper(criteria).map(to_condition).grab(
-				self.fake_time_range_criteria_to_report()).filter(lambda x: x is not None).to_list()
-		)
+	def find_column(self, breakdown_dimension: BreakdownDimension) -> Optional[
+		SubjectDatasetColumn]:
+		return ArrayHelper(self.subject.dataset.columns).find(
+			lambda x: x.columnId == breakdown_dimension.factorOrColumnId)
+
+	# def try_to_fake_time_group_column(self, breakdown_dimension: BreakdownDimension):
+	# 	time_group_column = self.find_column_of_time_group_dimension(breakdown_dimension)
+	# 	if time_group_column is None:
+	# 		return
+	# 	if not isinstance(time_group_column.parameter, TopicFactorParameter):
+	# 		return
+	# 	topic:Topic = ask_topic(time_group_column.parameter.topicId,self.get_principal_service())
+	# 	factor:Factor = find_factor(topic, time_group_column.parameter.factorId)
+	# 	# to figure out that the time group column is datetime type or not
+	# 	# if it is a datetime type, must fake a new column into subject
+	# 	if self.is_datetime_factor(factor):
+	# 		fake_column = self.fake_time_group_year_or_month_column(
+	# 			topic.topicId, factor.factorId, time_group_column.alias)
+	# 		if fake_column is not None:
+	# 			self.subject.dataset.columns.append(fake_column)
 
-	def fake_to_report(self) -> Report:
-		# build indicators
-		indicators: List[ReportIndicator] = []
-		self.fake_report_indicator(indicators, self.indicator.factorId)
 
-		# build dimensions: measure on 1, measure on 2, ..., time group
-		dimensions: List[ReportDimension] = []
-		# measures to dimensions
-		measure_on_columns = self.find_columns_of_measure_on_dimension()
 
+	def try_to_fake_value_column(self,breakdown_dimension:BreakdownDimension,index):
+		column = self.find_column(breakdown_dimension)
+		if column is None:
+			return
+
+		self.subject.dataset.columns.append(SubjectDatasetColumn(columnId=f'{self.FAKED_DIMENSION_ID}_{index}'
+		                                                         , parameter=column.parameter
+		                                                         ))
+
+
+	def try_to_fake_bucket_column(self, breakdown_dimension: BreakdownDimension,index):
+		measure_on_column = self.find_column(breakdown_dimension)
+		if measure_on_column is None:
+			return
+
+		topic:Topic = ask_topic(measure_on_column.parameter.topicId,self.get_principal_service())
+		factor:Optional[Factor] = find_factor(topic, measure_on_column.parameter.factorId)
+		subject_column = self.build_bucket_dataset_column(breakdown_dimension,index,factor,topic.topicId)
+		self.subject.dataset.columns.append(subject_column)
+
+	def regenerate_breakdown_subject(self, breakdown_target: BreakdownTarget):
+
+		for index,breakdown_dimension in enumerate(breakdown_target.dimensions):
+			find_column = self.find_column(breakdown_dimension)
+			if find_column is None:
+				raise Exception("breakdown dimension is not found {}".format(breakdown_dimension.dimensionId))
+			if breakdown_dimension.type == BreakdownDimensionType.TIME_RELATED:
+				computer_column = ComputedParameter()
+				computer_column.type = self.mapping_param_compute_type_to_measure_type(
+					breakdown_dimension.timeMeasureMethod)
+
+				if find_column.parameter.kind == ParameterKind.TOPIC:
+					topic_parameter = TopicFactorParameter(
+						kind=ParameterKind.TOPIC, topicId=find_column.parameter.topicId, factorId=find_column.parameter.factorId,
+						alias=self.FAKED_DIMENSION_NAME)
+				else:
+					raise Exception("not support yet for time related column")
+
+				computer_column.parameters = [topic_parameter]
+				self.subject.dataset.columns.append(SubjectDatasetColumn(columnId=f'{self.FAKED_DIMENSION_ID}_{index}'
+				                                            , parameter=computer_column
+				                                            ))
+
+			elif breakdown_dimension.type == BreakdownDimensionType.BUCKET:
+				self.try_to_fake_bucket_column(breakdown_dimension,index)
+			elif breakdown_dimension.type == BreakdownDimensionType.VALUE:
+				self.try_to_fake_value_column(breakdown_dimension,index)
+				pass
+			else:
+				raise Exception("breakdown type is not support {}".format(breakdown_dimension.type))
+
+	def fake_to_breakdown_report(self,time_frame: Optional[TimeFrame],breakdown_target:BreakdownTarget):
+		subject, report = self.fake_a_report(time_frame)
+		dimensions: List[ReportDimension] = []
 		def measure_to_dimension(column: SubjectDatasetColumn, index: int) -> None:
 			dimensions.append(ReportDimension(columnId=column.columnId, name=f'_BUCKET_ON_{index}_'))
 
-		ArrayHelper(measure_on_columns) \
+		ArrayHelper(subject.dataset.columns) \
+			.filter(
+			lambda x: x.columnId.startswith(self.FAKED_DIMENSION_ID) or x.columnId.startswith(self.MEASURE_ON_COLUMN_ID)) \
 			.each_with_index(lambda x, index: measure_to_dimension(x, index + 1))
 
-		# time group to dimensions
-		time_group_year_or_month_column = ArrayHelper(self.subject.dataset.columns) \
-			.find(lambda x: x.columnId == self.TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID)
-		if time_group_year_or_month_column is not None:
-			dimensions.append(
-				ReportDimension(columnId=self.TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID, name='_TIME_GROUP_'))
-		else:
-			time_group_column = self.find_column_of_time_group_dimension()
-			if time_group_column is not None:
-				dimensions.append(ReportDimension(columnId=time_group_column.columnId, name='_TIME_GROUP_'))
-
-		if len(dimensions) == 0:
-			raise IndicatorKernelException('Neither time group nor bucket not found.')
-
-		report_filter = self.fake_criteria_to_report()
-		if report_filter is None:
-			return Report(indicators=indicators, dimensions=dimensions)
-		else:
-			return Report(indicators=indicators, dimensions=dimensions, filters=report_filter)
+		report.dimensions = dimensions
+		return subject,report
 
-	# noinspection PyMethodMayBeStatic
-	def move_indicators_to_tail(self, row: DataResultSetRow, move_count: int) -> DataResultSetRow:
-		return [*row[move_count:], *row[:move_count]]
-
-	def find_factor(self, topic_id: TopicId, factor_id: FactorId) -> Tuple[Topic, Factor]:
-		topic = get_topic_service(self.principalService).find_by_id(topic_id)
-		factor = ArrayHelper(topic.factors).find(lambda x: x.factorId == factor_id)
-		if factor is None:
-			raise IndicatorKernelException('Factor of time group column not found.')
-
-		return topic, factor
-
-	def try_to_fake_time_group_column(self):
-		time_group_column = self.find_column_of_time_group_dimension()
-		if time_group_column is None:
-			return
-		if not isinstance(time_group_column.parameter, TopicFactorParameter):
-			return
 
-		topic, factor = self.find_factor(time_group_column.parameter.topicId, time_group_column.parameter.factorId)
-		# to figure out that the time group column is datetime type or not
-		# if it is a datetime type, must fake a new column into subject
-		if self.is_datetime_factor(factor):
-			fake_column = self.fake_time_group_year_or_month_column(
-				topic.topicId, factor.factorId, time_group_column.alias)
-			if fake_column is not None:
-				self.subject.dataset.columns.append(fake_column)
-
-	# TODO bucket on subject column is not supported yet
-	# def try_to_fake_measure_on_column(self):
-	# 	measure_on_column = self.find_columns_of_measure_on_dimension()
-	# 	if measure_on_column is None:
-	# 		return
-	# 	if not isinstance(measure_on_column.parameter, TopicFactorParameter):
-	# 		return
-	#
-	# 	topic, factor = self.find_factor(measure_on_column.parameter.topicId, measure_on_column.parameter.factorId)
-	#
-	# 	measure_on = self.inspection.measureOn
-	# 	measure_on_bucket_id = self.inspection.measureOnBucketId
-	# 	if is_blank(measure_on_bucket_id):
-	# 		if measure_on == InspectMeasureOnType.OTHER:
-	# 			# using naturally classification
-	# 			fake_column = SubjectDatasetColumn(
-	# 				columnId='_BUCKET_ON_',
-	# 				parameter=TopicFactorParameter(
-	# 					kind=ParameterKind.TOPIC, topicId=topic.topicId, factorId=factor.factorId),
-	# 				alias='_BUCKET_ON_'
-	# 			)
-	# 		else:
-	# 			raise IndicatorKernelException('Measure on bucket not declared.')
-	# 	else:
-	# 		return
-	#
-	# 	self.subject.dataset.columns.append(fake_column)
 
-	def fake_subject(self):
-		"""
-		fake a time group column when declared
-		"""
-		self.try_to_fake_time_group_column()
+	def __find_enum_for_dimensions_in_subject(self, breakdown_target: BreakdownTarget,subject:Subject) -> Dict[int, Enum]:
+		result = {}
+		for index, dimension in enumerate(breakdown_target.dimensions):
+			# column_id = dimension.
+			self.subject = subject
+			find_column = self.find_column(dimension)
+			if find_column :
+				if isinstance(find_column.parameter, TopicFactorParameter):
+					topic_id = find_column.parameter.topicId
+					factor_id = find_column.parameter.factorId
+					topic = ask_topic(topic_id, self.principalService)
+					factor: Factor = find_factor(topic, factor_id)
+					if factor is None:
+						raise Exception("factor id is not found {}".format(factor_id))
+					if self.is_enum_factor(factor):
+						enum: Enum = ask_enum(factor.enumId, self.principalService)
+						result[index] = enum
+		return result
 
-	def find(self) -> DataResult:
-		self.fake_subject()
-		report = self.fake_to_report()
-		report_data_service = get_report_data_service(self.subject, report, self.principalService)
-		# reorder columns, move indicators to tail of row
-		data_result = report_data_service.find()
-		move_column_count = len(report.indicators)
+
+
+	def ask_breakdown_values(self, time_frame: Optional[TimeFrame], breakdown_target: BreakdownTarget) -> DataResult:
+		self.regenerate_breakdown_subject(breakdown_target)
+		subject, report = self.fake_to_breakdown_report(time_frame,breakdown_target)
+		report_data_service = self.get_report_data_service(subject, report)
+		data_result =  report_data_service.find()
+		enum_dict = self.__find_enum_for_dimensions_in_subject(breakdown_target,subject)
 		return DataResult(
 			columns=data_result.columns,
-			data=ArrayHelper(data_result.data).map(
-				lambda x: self.move_indicators_to_tail(x, move_column_count)).to_list()
+			data=self.replace_result_data_for_enum(data_result, enum_dict)
 		)
```

### Comparing `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/subject_helper.py` & `watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/utils/subject.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/topic_base_inspection_data_service.py` & `watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/data/inspection/topic_base_service.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,470 +1,478 @@
-from typing import Callable, List, Optional
-
 from watchmen_auth import PrincipalService
-from watchmen_data_kernel.meta import TopicService
-from watchmen_indicator_kernel.common import IndicatorKernelException
 from watchmen_inquiry_kernel.storage import ReportDataService
-from watchmen_model.admin import Factor, Topic
-from watchmen_model.common import ComputedParameter, ConstantParameter, DataResult, DataResultSetRow, \
-	FactorId, Parameter, ParameterComputeType, ParameterCondition, ParameterExpression, ParameterExpressionOperator, \
-	ParameterJoint, ParameterJointType, ParameterKind, TopicFactorParameter, TopicId
-from watchmen_model.console import Report, ReportDimension, ReportIndicator, Subject, SubjectDataset, \
-	SubjectDatasetColumn
-from watchmen_model.indicator import Bucket, CategorySegment, CategorySegmentsHolder, Indicator, IndicatorCriteria, \
-	Inspection, InspectMeasureOn, InspectMeasureOnType, MeasureMethod, NumericSegmentsHolder, NumericValueSegment, \
-	OtherCategorySegmentValue, RangeBucketValueIncluding
-from watchmen_utilities import ArrayHelper, is_blank
-from .bucket_helper import ask_bucket
+from watchmen_model.console import Report, Subject
 from .inspection_data_service import InspectionDataService
 
 
-def get_report_data_service(subject: Subject, report: Report, principal_service: PrincipalService) -> ReportDataService:
-	return ReportDataService(subject, report, principal_service, True)
-
-
-def get_topic_service(principal_service: PrincipalService) -> TopicService:
-	return TopicService(principal_service)
+# def get_report_data_service(subject: Subject, report: Report, principal_service: PrincipalService) -> ReportDataService:
+# 	return ReportDataService(subject, report, principal_service, True)
 
 
+# TODO REFACTOR-OBJECTIVE ACHIEVEMENT BREAK DOWN DATA SERVICE, ON TOPIC
 class TopicBaseInspectionDataService(InspectionDataService):
-	def __init__(self, inspection: Inspection, indicator: Indicator, topic: Topic, principal_service: PrincipalService):
-		super().__init__(inspection, principal_service)
-		self.indicator = indicator
-		self.topic = topic
-		self.INDICATOR_FACTOR_COLUMN_ID: str = 'indicator_factor_column'
-		self.TIME_GROUP_COLUMN_ID: str = 'time_group_column'
-		self.MEASURE_ON_COLUMN_ID: str = 'measure_on_column'
-
-	def ask_factor_not_found_message(self, factor_id: FactorId) -> str:
-		return f'Factor[id={factor_id}] not found on topic[id={self.topic.topicId}, name={self.topic.name}].'
-
-	# noinspection DuplicatedCode
-	def find_factor(
-			self, factor_id: Optional[FactorId],
-			on_factor_id_missed: Callable[[], str]) -> Factor:
-		if is_blank(factor_id):
-			raise IndicatorKernelException(on_factor_id_missed())
-		factor: Optional[Factor] = ArrayHelper(self.topic.factors).find(lambda x: x.factorId == factor_id)
-		if factor is None:
-			raise IndicatorKernelException(self.ask_factor_not_found_message(factor_id))
-		return factor
-
-	def fake_indicator_factor_to_dataset_column(self) -> SubjectDatasetColumn:
-		"""
-		fake a dataset column based on indicator factor
-		"""
-		indicator_factor = self.find_factor(
-			self.indicator.factorId,
-			lambda: f'Indicator[id={self.indicator.indicatorId}, name={self.indicator.name}] factor not declared.')
-		return SubjectDatasetColumn(
-			columnId=self.INDICATOR_FACTOR_COLUMN_ID,
-			parameter=TopicFactorParameter(
-				kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=indicator_factor.factorId),
-			alias=f'column_{self.INDICATOR_FACTOR_COLUMN_ID}'
-		)
-
-	def fake_time_group_to_dataset_column(self) -> Optional[SubjectDatasetColumn]:
-		"""
-		fake time group column based on time group.
-		returns yearOf/monthOf when original time group factor is datetime,
-		otherwise use the original factor
-		"""
-		time_group_existing, measure_on_time_factor_id, measure_on_time = self.has_time_group()
-		if not time_group_existing:
-			return None
-
-		measure_on_time_factor = self.find_factor(
-			measure_on_time_factor_id, lambda: 'Measure on time factor not declared.')
-		if self.is_datetime_factor(measure_on_time_factor.type):
-			if measure_on_time == MeasureMethod.YEAR:
-				compute_type = ParameterComputeType.YEAR_OF
-			elif measure_on_time == MeasureMethod.MONTH:
-				compute_type = ParameterComputeType.MONTH_OF
-			else:
-				raise IndicatorKernelException(
-					f'Measure method[{measure_on_time}] for factor type[{measure_on_time_factor.type}] is not supported.')
-			return SubjectDatasetColumn(
-				columnId=self.TIME_GROUP_COLUMN_ID,
-				parameter=ComputedParameter(
-					kind=ParameterKind.COMPUTED,
-					type=compute_type,
-					parameters=[
-						TopicFactorParameter(
-							kind=ParameterKind.TOPIC,
-							topicId=self.topic.topicId, factorId=measure_on_time_factor_id)
-					]
-				),
-				alias=f'column_{self.TIME_GROUP_COLUMN_ID}'
-			)
-		else:
-			return SubjectDatasetColumn(
-				columnId=self.TIME_GROUP_COLUMN_ID,
-				parameter=TopicFactorParameter(
-					kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=measure_on_time_factor_id),
-				alias=f'column_{self.TIME_GROUP_COLUMN_ID}'
-			)
-
-	# noinspection PyMethodMayBeStatic
-	def get_topic_id_from_time_group_column(self, column: SubjectDatasetColumn) -> TopicId:
-		parameter = column.parameter
-		if parameter.kind == ParameterKind.TOPIC:
-			return parameter.topicId
-		else:
-			return parameter.parameters[0].topicId
-
-	# noinspection PyMethodMayBeStatic
-	def get_factor_id_from_time_group_column(self, column: SubjectDatasetColumn) -> FactorId:
-		parameter = column.parameter
-		if parameter.kind == ParameterKind.TOPIC:
-			return parameter.factorId
-		else:
-			return parameter.parameters[0].factorId
-
-	def fake_time_group_year_or_month_to_dataset_column(
-			self, time_group_column: SubjectDatasetColumn) -> Optional[SubjectDatasetColumn]:
-		topic_id = self.get_topic_id_from_time_group_column(time_group_column)
-		topic = get_topic_service(self.principalService).find_by_id(topic_id)
-		factor_id = self.get_factor_id_from_time_group_column(time_group_column)
-		factor = ArrayHelper(topic.factors).find(lambda x: x.factorId == factor_id)
-		if factor is None:
-			raise IndicatorKernelException('Factor of time group column not found.')
-		if self.is_datetime_factor(factor):
-			return self.fake_time_group_year_or_month_column(topic.topicId, factor.factorId, time_group_column.alias)
-		else:
-			return None
-
-	# noinspection PyMethodMayBeStatic
-	def to_numeric_segments_bucket(self, bucket: Bucket) -> NumericSegmentsHolder:
-		if isinstance(bucket, NumericSegmentsHolder):
-			return bucket
-		else:
-			return NumericSegmentsHolder(**bucket.to_dict())
-
-	# noinspection PyMethodMayBeStatic
-	def to_category_segments_bucket(self, bucket: Bucket) -> CategorySegmentsHolder:
-		if isinstance(bucket, CategorySegmentsHolder):
-			return bucket
-		else:
-			return CategorySegmentsHolder(**bucket.to_dict())
-
-	def to_numeric_range_case_route(
-			self, segment: NumericValueSegment, include: RangeBucketValueIncluding,
-			factor: Factor
-	) -> Parameter:
-		name = segment.name
-		min_value = segment.value.min
-		max_value = segment.value.max
-		if include == RangeBucketValueIncluding.INCLUDE_MIN:
-			min_operator = ParameterExpressionOperator.MORE_EQUALS
-			max_operator = ParameterExpressionOperator.LESS
-		else:
-			min_operator = ParameterExpressionOperator.MORE
-			max_operator = ParameterExpressionOperator.LESS_EQUALS
-
-		return ConstantParameter(
-			kind=ParameterKind.CONSTANT,
-			conditional=True,
-			on=ParameterJoint(
-				jointType=ParameterJointType.AND,
-				filters=ArrayHelper([
-					None if min_value is not None else ParameterExpression(
-						left=TopicFactorParameter(
-							kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=factor.factorId),
-						operator=min_operator,
-						right=min_value
-					),
-					None if max_value is not None else ParameterExpression(
-						left=TopicFactorParameter(
-							kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=factor.factorId),
-						operator=max_operator,
-						right=max_value
-					)
-				]).map(lambda x: x is not None).to_list()
-			),
-			value=name
-		)
-
-	def to_category_case_route(self, segment: CategorySegment, factor: Factor) -> Parameter:
-		return ConstantParameter(
-			kind=ParameterKind.CONSTANT,
-			conditional=True,
-			on=ParameterJoint(
-				jointType=ParameterJointType.AND,
-				filters=[
-					ParameterExpression(
-						left=TopicFactorParameter(
-							kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=factor.factorId),
-						operator=ParameterExpressionOperator.IN,
-						right=segment.value
-					),
-				]
-			),
-			value=segment.name
-		)
-
-	def fake_measure_on_column(
-			self, measure_on: InspectMeasureOn, measure_on_index: int) -> Optional[SubjectDatasetColumn]:
-		if measure_on is None or measure_on.type is None or measure_on.type == InspectMeasureOnType.NONE:
-			return None
-		# build factor
-		if measure_on == InspectMeasureOnType.OTHER:
-			measure_on_factor_id = measure_on.factorId
-			if is_blank(measure_on_factor_id):
-				return None
-		elif measure_on == InspectMeasureOnType.VALUE:
-			measure_on_factor_id = self.indicator.factorId
-		else:
-			return None
-		measure_on_factor = self.find_factor(measure_on_factor_id, lambda: 'Measure on factor not declared.')
-		# build bucket
-		measure_on_bucket_id = measure_on.bucketId
-		if is_blank(measure_on_bucket_id):
-			if measure_on == InspectMeasureOnType.OTHER:
-				# using naturally classification
-				return SubjectDatasetColumn(
-					columnId=f'{self.MEASURE_ON_COLUMN_ID}_{measure_on_index}',
-					parameter=TopicFactorParameter(
-						kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=measure_on_factor_id),
-					alias=f'column_{self.MEASURE_ON_COLUMN_ID}_{measure_on_index}'
-				)
-			else:
-				raise IndicatorKernelException('Measure on bucket not declared.')
-		else:
-			bucket = ask_bucket(measure_on_bucket_id, self.principalService)
-			if measure_on == InspectMeasureOnType.VALUE:
-				bucket = self.to_numeric_segments_bucket(bucket)
-				include = RangeBucketValueIncluding.INCLUDE_MIN if bucket.include is None else bucket.include
-				# at least has one value
-				segments = ArrayHelper(bucket.segments) \
-					.filter(lambda x: x.value is not None) \
-					.filter(lambda x: x.value.min is not None or x.value.max is not None) \
-					.to_list()
-				if len(segments) == 0:
-					raise IndicatorKernelException('Numeric range segments not declared.')
-				return SubjectDatasetColumn(
-					columnId=f'{self.MEASURE_ON_COLUMN_ID}_{measure_on_index}',
-					parameter=ComputedParameter(
-						kind=ParameterKind.COMPUTED, type=ParameterComputeType.CASE_THEN,
-						parameters=[
-							*ArrayHelper(segments).map(
-								lambda x: self.to_numeric_range_case_route(x, include, measure_on_factor)).to_list(),
-							# an anyway route, additional
-							ConstantParameter(kind=ParameterKind.CONSTANT, value='-')
-						]
-					),
-					alias=f'column_{self.MEASURE_ON_COLUMN_ID}_{measure_on_index}'
-				)
-			elif measure_on == InspectMeasureOnType.OTHER:
-				bucket = self.to_category_segments_bucket(bucket)
-				segments = ArrayHelper(bucket.segments) \
-					.filter(lambda x: x.value is not None and len(x.value) != 0).to_list()
-				if len(segments) == 0:
-					raise IndicatorKernelException('Category segments not declared.')
-				anyway_segment: CategorySegment = ArrayHelper(segments) \
-					.find(lambda x: len(x.value) == 1 and x.value[0] == OtherCategorySegmentValue)
-				if anyway_segment is not None:
-					conditional_routes = ArrayHelper(segments).filter(lambda x: x != anyway_segment).to_list()
-					anyway_route = ConstantParameter(kind=ParameterKind.CONSTANT, value=anyway_segment.name)
-				else:
-					conditional_routes = segments
-					anyway_route = ConstantParameter(kind=ParameterKind.CONSTANT, value='-')
-
-				return SubjectDatasetColumn(
-					columnId=f'{self.MEASURE_ON_COLUMN_ID}_{measure_on_index}',
-					parameter=ComputedParameter(
-						kind=ParameterKind.COMPUTED, type=ParameterComputeType.CASE_THEN,
-						parameters=[
-							*ArrayHelper(conditional_routes).map(
-								lambda x: self.to_category_case_route(x, measure_on_factor)).to_list(),
-							anyway_route
-						]
-					),
-					alias=f'column_{self.MEASURE_ON_COLUMN_ID}_{measure_on_index}'
-				)
-			else:
-				raise IndicatorKernelException(f'Measure[{measure_on}] is not supported.')
-
-	def fake_measure_on_to_dataset_column(self) -> List[SubjectDatasetColumn]:
-		return ArrayHelper(self.inspection.measures) \
-			.map_with_index(lambda x, index: self.fake_measure_on_column(x, index + 1)) \
-			.filter(lambda x: x is not None) \
-			.to_list()
-
-	# noinspection DuplicatedCode
-	def fake_time_range_to_dataset_filter(self) -> Optional[ParameterJoint]:
-		time_range_factor_id = self.inspection.timeRangeFactorId
-		if is_blank(time_range_factor_id):
-			return None
-		time_range_factor = self.find_factor(time_range_factor_id, lambda: 'Time range factor not declared.')
-		time_ranges = ArrayHelper(self.inspection.timeRanges) \
-			.filter(lambda x: x is not None and x.value is not None).to_list()
-		if len(time_ranges) == 0:
-			# no ranges given
-			return None
-
-		operator = ParameterExpressionOperator.EQUALS if len(time_ranges) == 1 else ParameterExpressionOperator.IN
-		right = time_ranges[0].value if len(time_ranges) == 1 \
-			else ArrayHelper(time_ranges).map(lambda x: x.value).join(',')
-		time_range_measure = self.inspection.timeRangeMeasure
-		if self.is_datetime_factor(time_range_factor):
-			if time_range_measure == MeasureMethod.YEAR:
-				compute_type = ParameterComputeType.YEAR_OF
-			elif time_range_measure == MeasureMethod.MONTH:
-				compute_type = ParameterComputeType.MONTH_OF
-			else:
-				raise IndicatorKernelException(
-					f'Measure method[{time_range_measure}] for factor type[{time_range_factor.type}] is not supported.')
-			joint = ParameterJoint(
-				jointType=ParameterJointType.AND,
-				filters=[
-					ParameterExpression(
-						left=ComputedParameter(
-							kind=ParameterKind.COMPUTED,
-							type=compute_type,
-							parameters=[
-								TopicFactorParameter(
-									kind=ParameterKind.TOPIC,
-									topicId=self.topic.topicId, factorId=time_range_factor_id)
-							]
-						),
-						operator=operator,
-						right=ConstantParameter(kind=ParameterKind.CONSTANT, value=str(right))
-					)
-				]
-			)
-		else:
-			joint = ParameterJoint(
-				jointType=ParameterJointType.AND,
-				filters=[
-					ParameterExpression(
-						left=TopicFactorParameter(
-							kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=time_range_factor_id),
-						operator=operator,
-						right=ConstantParameter(kind=ParameterKind.CONSTANT, value=str(right))
-					)
-				]
-			)
-		return joint
-
-	def has_indicator_filter(self) -> bool:
-		return \
-			self.indicator.filter is not None \
-			and self.indicator.filter.enabled \
-			and self.indicator.filter.joint is not None \
-			and self.indicator.filter.joint.filters is not None \
-			and len(self.indicator.filter.joint.filters) != 0
-
-	# noinspection DuplicatedCode
-	def fake_criteria_to_dataset_filter(self) -> Optional[ParameterJoint]:
-		criteria = ArrayHelper(self.inspection.criteria).filter(lambda x: x is not None).to_list()
-		if len(criteria) == 0:
-			return None
-
-		def to_condition(a_criteria: IndicatorCriteria) -> ParameterCondition:
-			factor = self.find_factor(
-				a_criteria.factorId,
-				lambda: f'Factor of inspection criteria[{criteria.to_dict()}] not declared.')
-			return self.fake_criteria_to_condition(a_criteria)(self.topic.topicId, factor.factorId)
-
-		return ParameterJoint(
-			jointType=ParameterJointType.AND,
-			filters=ArrayHelper(criteria).map(to_condition).to_list()
-		)
-
-	# noinspection DuplicatedCode
-	def build_filters(self) -> Optional[ParameterJoint]:
-		time_range_filter = self.fake_time_range_to_dataset_filter()
-		inspection_filter = self.fake_criteria_to_dataset_filter()
-		indicator_filter = self.indicator.filter.joint if self.has_indicator_filter() else None
-		filters = ArrayHelper([time_range_filter, inspection_filter, indicator_filter]) \
-			.filter(lambda x: x is not None) \
-			.to_list()
-		if len(filters) == 0:
-			return None
-		else:
-			return ParameterJoint(jointType=ParameterJointType.AND, filters=filters)
-
-	def fake_to_subject(self) -> Subject:
-		"""
-		columns:
-			[indicator column]
-			[time group column]: optional, existing when time group declared
-			[time group year/month column]: optional, existing when time group declared and original factor is datetime
-			[measure_on_1, [measure_on_2, measure_on_3, ...]]: optional
-		"""
-		dataset_columns: List[SubjectDatasetColumn] = []
-		# append indicator factor anyway
-		indicator_factor_column = self.fake_indicator_factor_to_dataset_column()
-		dataset_columns.append(indicator_factor_column)
-		# append time group if exists
-		time_group_column = self.fake_time_group_to_dataset_column()
-		if time_group_column is not None:
-			# append time group column
-			dataset_columns.append(time_group_column)
-			time_group_year_or_month_column = self.fake_time_group_year_or_month_to_dataset_column(time_group_column)
-			if time_group_year_or_month_column is not None:
-				dataset_columns.append(time_group_year_or_month_column)
-		# measures
-		measure_on_columns = self.fake_measure_on_to_dataset_column()
-		if len(measure_on_columns) != 0:
-			ArrayHelper(measure_on_columns).each(lambda x: dataset_columns.append(x))
-
-		dataset_filters: Optional[ParameterJoint] = self.build_filters()
-		return Subject(dataset=SubjectDataset(columns=dataset_columns, filters=dataset_filters))
-
-	def fake_report_indicators(self) -> List[ReportIndicator]:
-		indicators: List[ReportIndicator] = []
-		self.fake_report_indicator(indicators, self.INDICATOR_FACTOR_COLUMN_ID)
-		return indicators
-
-	def fake_to_report(self, subject: Subject) -> Report:
-		"""
-		build report based on subject, columns in subject refers to fake_to_subject
-		"""
-		# build indicators
-		indicators: List[ReportIndicator] = self.fake_report_indicators()
-
-		# build dimensions: measure on 1, measure on 2, ..., time group
-		dimensions: List[ReportDimension] = []
-
-		# measures to dimensions
-		def measure_to_dimension(column: SubjectDatasetColumn, index: int) -> None:
-			dimensions.append(ReportDimension(columnId=column.columnId, name=f'_BUCKET_ON_{index}_'))
-
-		ArrayHelper(subject.dataset.columns) \
-			.filter(lambda x: x.columnId.startswith(self.MEASURE_ON_COLUMN_ID)) \
-			.each_with_index(lambda x, index: measure_to_dimension(x, index + 1))
-
-		# time group to dimensions
-		time_group_year_or_month_column = ArrayHelper(subject.dataset.columns) \
-			.find(lambda x: x.columnId == self.TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID)
-		if time_group_year_or_month_column is not None:
-			dimensions.append(
-				ReportDimension(columnId=self.TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID, name='_TIME_GROUP_'))
-		else:
-			time_group_column = ArrayHelper(subject.dataset.columns) \
-				.find(lambda x: x.columnId == self.TIME_GROUP_COLUMN_ID)
-			if time_group_column is not None:
-				dimensions.append(ReportDimension(columnId=self.TIME_GROUP_COLUMN_ID, name='_TIME_GROUP_'))
-
-		if len(dimensions) == 0:
-			raise IndicatorKernelException('Neither time group nor bucket on found.')
-
-		return Report(indicators=indicators, dimensions=dimensions)
-
-	# noinspection PyMethodMayBeStatic
-	def move_indicators_to_tail(self, row: DataResultSetRow, move_count: int) -> DataResultSetRow:
-		return [*row[move_count:], *row[:move_count]]
+	pass
 
-	def find(self) -> DataResult:
-		subject = self.fake_to_subject()
-		report = self.fake_to_report(subject)
-		report_data_service = get_report_data_service(subject, report, self.principalService)
-		# reorder columns, move indicators to tail of row
-		data_result = report_data_service.find()
-		move_column_count = len(report.indicators)
-		return DataResult(
-			columns=data_result.columns,
-			data=ArrayHelper(data_result.data).map(
-				lambda x: self.move_indicators_to_tail(x, move_column_count)).to_list()
-		)
+	#
+	# def __init__(self, inspection: Inspection, indicator: Indicator, topic: Topic, principal_service: PrincipalService):
+	# 	super().__init__(inspection, principal_service)
+	# 	self.indicator = indicator
+	# 	self.topic = topic
+	# 	self.INDICATOR_FACTOR_COLUMN_ID: str = 'indicator_factor_column'
+	# 	self.TIME_GROUP_COLUMN_ID: str = 'time_group_column'
+	# 	self.MEASURE_ON_COLUMN_ID: str = 'measure_on_column'
+	#
+	#
+	# def ask_factor_not_found_message(self, factor_id: FactorId) -> str:
+	# 	return f'Factor[id={factor_id}] not found on topic[id={self.topic.topicId}, name={self.topic.name}].'
+	#
+	#
+	# # noinspection DuplicatedCode
+	# def find_factor(
+	# 		self, factor_id: Optional[FactorId],
+	# 		on_factor_id_missed: Callable[[], str]) -> Factor:
+	# 	if is_blank(factor_id):
+	# 		raise IndicatorKernelException(on_factor_id_missed())
+	# 	factor: Optional[Factor] = ArrayHelper(self.topic.factors).find(lambda x: x.factorId == factor_id)
+	# 	if factor is None:
+	# 		raise IndicatorKernelException(self.ask_factor_not_found_message(factor_id))
+	# 	return factor
+	#
+	#
+	# def fake_indicator_factor_to_dataset_column(self) -> SubjectDatasetColumn:
+	# 	"""
+	# 	fake a dataset column based on indicator factor
+	# 	"""
+	# 	indicator_factor = self.find_factor(
+	# 		self.indicator.factorId,
+	# 		lambda: f'Indicator[id={self.indicator.indicatorId}, name={self.indicator.name}] factor not declared.')
+	# 	return SubjectDatasetColumn(
+	# 		columnId=self.INDICATOR_FACTOR_COLUMN_ID,
+	# 		parameter=TopicFactorParameter(
+	# 			kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=indicator_factor.factorId),
+	# 		alias=f'column_{self.INDICATOR_FACTOR_COLUMN_ID}'
+	# 	)
+	#
+	#
+	# def fake_time_group_to_dataset_column(self) -> Optional[SubjectDatasetColumn]:
+	# 	"""
+	# 	fake time group column based on time group.
+	# 	returns yearOf/monthOf when original time group factor is datetime,
+	# 	otherwise use the original factor
+	# 	"""
+	# 	time_group_existing, measure_on_time_factor_id, measure_on_time = self.has_time_group()
+	# 	if not time_group_existing:
+	# 		return None
+	#
+	# 	measure_on_time_factor = self.find_factor(
+	# 		measure_on_time_factor_id, lambda: 'Measure on time factor not declared.')
+	# 	if self.is_datetime_factor(measure_on_time_factor.type):
+	# 		if measure_on_time == MeasureMethod.YEAR:
+	# 			compute_type = ParameterComputeType.YEAR_OF
+	# 		elif measure_on_time == MeasureMethod.MONTH:
+	# 			compute_type = ParameterComputeType.MONTH_OF
+	# 		else:
+	# 			raise IndicatorKernelException(
+	# 				f'Measure method[{measure_on_time}] for factor type[{measure_on_time_factor.type}] is not supported.')
+	# 		return SubjectDatasetColumn(
+	# 			columnId=self.TIME_GROUP_COLUMN_ID,
+	# 			parameter=ComputedParameter(
+	# 				kind=ParameterKind.COMPUTED,
+	# 				type=compute_type,
+	# 				parameters=[
+	# 					TopicFactorParameter(
+	# 						kind=ParameterKind.TOPIC,
+	# 						topicId=self.topic.topicId, factorId=measure_on_time_factor_id)
+	# 				]
+	# 			),
+	# 			alias=f'column_{self.TIME_GROUP_COLUMN_ID}'
+	# 		)
+	# 	else:
+	# 		return SubjectDatasetColumn(
+	# 			columnId=self.TIME_GROUP_COLUMN_ID,
+	# 			parameter=TopicFactorParameter(
+	# 				kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=measure_on_time_factor_id),
+	# 			alias=f'column_{self.TIME_GROUP_COLUMN_ID}'
+	# 		)
+	#
+	#
+	# # noinspection PyMethodMayBeStatic
+	# def get_topic_id_from_time_group_column(self, column: SubjectDatasetColumn) -> TopicId:
+	# 	parameter = column.parameter
+	# 	if parameter.kind == ParameterKind.TOPIC:
+	# 		return parameter.topicId
+	# 	else:
+	# 		return parameter.parameters[0].topicId
+	#
+	#
+	# # noinspection PyMethodMayBeStatic
+	# def get_factor_id_from_time_group_column(self, column: SubjectDatasetColumn) -> FactorId:
+	# 	parameter = column.parameter
+	# 	if parameter.kind == ParameterKind.TOPIC:
+	# 		return parameter.factorId
+	# 	else:
+	# 		return parameter.parameters[0].factorId
+	#
+	#
+	# def fake_time_group_year_or_month_to_dataset_column(
+	# 		self, time_group_column: SubjectDatasetColumn) -> Optional[SubjectDatasetColumn]:
+	# 	topic_id = self.get_topic_id_from_time_group_column(time_group_column)
+	# 	topic = get_topic_service(self.principalService).find_by_id(topic_id)
+	# 	factor_id = self.get_factor_id_from_time_group_column(time_group_column)
+	# 	factor = ArrayHelper(topic.factors).find(lambda x: x.factorId == factor_id)
+	# 	if factor is None:
+	# 		raise IndicatorKernelException('Factor of time group column not found.')
+	# 	if self.is_datetime_factor(factor):
+	# 		return self.fake_time_group_year_or_month_column(topic.topicId, factor.factorId, time_group_column.alias)
+	# 	else:
+	# 		return None
+	#
+	#
+	# # noinspection PyMethodMayBeStatic
+	# def to_numeric_segments_bucket(self, bucket: Bucket) -> NumericSegmentsHolder:
+	# 	if isinstance(bucket, NumericSegmentsHolder):
+	# 		return bucket
+	# 	else:
+	# 		return NumericSegmentsHolder(**bucket.to_dict())
+	#
+	#
+	# # noinspection PyMethodMayBeStatic
+	# def to_category_segments_bucket(self, bucket: Bucket) -> CategorySegmentsHolder:
+	# 	if isinstance(bucket, CategorySegmentsHolder):
+	# 		return bucket
+	# 	else:
+	# 		return CategorySegmentsHolder(**bucket.to_dict())
+	#
+	#
+	# def to_numeric_range_case_route(
+	# 		self, segment: NumericValueSegment, include: RangeBucketValueIncluding,
+	# 		factor: Factor
+	# ) -> Parameter:
+	# 	name = segment.name
+	# 	min_value = segment.value.min
+	# 	max_value = segment.value.max
+	# 	if include == RangeBucketValueIncluding.INCLUDE_MIN:
+	# 		min_operator = ParameterExpressionOperator.MORE_EQUALS
+	# 		max_operator = ParameterExpressionOperator.LESS
+	# 	else:
+	# 		min_operator = ParameterExpressionOperator.MORE
+	# 		max_operator = ParameterExpressionOperator.LESS_EQUALS
+	#
+	# 	return ConstantParameter(
+	# 		kind=ParameterKind.CONSTANT,
+	# 		conditional=True,
+	# 		on=ParameterJoint(
+	# 			jointType=ParameterJointType.AND,
+	# 			filters=ArrayHelper([
+	# 				None if min_value is not None else ParameterExpression(
+	# 					left=TopicFactorParameter(
+	# 						kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=factor.factorId),
+	# 					operator=min_operator,
+	# 					right=min_value
+	# 				),
+	# 				None if max_value is not None else ParameterExpression(
+	# 					left=TopicFactorParameter(
+	# 						kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=factor.factorId),
+	# 					operator=max_operator,
+	# 					right=max_value
+	# 				)
+	# 			]).map(lambda x: x is not None).to_list()
+	# 		),
+	# 		value=name
+	# 	)
+	#
+	#
+	# def to_category_case_route(self, segment: CategorySegment, factor: Factor) -> Parameter:
+	# 	return ConstantParameter(
+	# 		kind=ParameterKind.CONSTANT,
+	# 		conditional=True,
+	# 		on=ParameterJoint(
+	# 			jointType=ParameterJointType.AND,
+	# 			filters=[
+	# 				ParameterExpression(
+	# 					left=TopicFactorParameter(
+	# 						kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=factor.factorId),
+	# 					operator=ParameterExpressionOperator.IN,
+	# 					right=segment.value
+	# 				),
+	# 			]
+	# 		),
+	# 		value=segment.name
+	# 	)
+	#
+	#
+	# def fake_measure_on_column(
+	# 		self, measure_on: InspectMeasureOn, measure_on_index: int) -> Optional[SubjectDatasetColumn]:
+	# 	if measure_on is None or measure_on.type is None or measure_on.type == InspectMeasureOnType.NONE:
+	# 		return None
+	# 	# build factor
+	# 	if measure_on == InspectMeasureOnType.OTHER:
+	# 		measure_on_factor_id = measure_on.factorId
+	# 		if is_blank(measure_on_factor_id):
+	# 			return None
+	# 	elif measure_on == InspectMeasureOnType.VALUE:
+	# 		measure_on_factor_id = self.indicator.factorId
+	# 	else:
+	# 		return None
+	# 	measure_on_factor = self.find_factor(measure_on_factor_id, lambda: 'Measure on factor not declared.')
+	# 	# build bucket
+	# 	measure_on_bucket_id = measure_on.bucketId
+	# 	if is_blank(measure_on_bucket_id):
+	# 		if measure_on == InspectMeasureOnType.OTHER:
+	# 			# using naturally classification
+	# 			return SubjectDatasetColumn(
+	# 				columnId=f'{self.MEASURE_ON_COLUMN_ID}_{measure_on_index}',
+	# 				parameter=TopicFactorParameter(
+	# 					kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=measure_on_factor_id),
+	# 				alias=f'column_{self.MEASURE_ON_COLUMN_ID}_{measure_on_index}'
+	# 			)
+	# 		else:
+	# 			raise IndicatorKernelException('Measure on bucket not declared.')
+	# 	else:
+	# 		bucket = ask_bucket(measure_on_bucket_id, self.principalService)
+	# 		if measure_on == InspectMeasureOnType.VALUE:
+	# 			bucket = self.to_numeric_segments_bucket(bucket)
+	# 			include = RangeBucketValueIncluding.INCLUDE_MIN if bucket.include is None else bucket.include
+	# 			# at least has one value
+	# 			segments = ArrayHelper(bucket.segments) \
+	# 				.filter(lambda x: x.value is not None) \
+	# 				.filter(lambda x: x.value.min is not None or x.value.max is not None) \
+	# 				.to_list()
+	# 			if len(segments) == 0:
+	# 				raise IndicatorKernelException('Numeric range segments not declared.')
+	# 			return SubjectDatasetColumn(
+	# 				columnId=f'{self.MEASURE_ON_COLUMN_ID}_{measure_on_index}',
+	# 				parameter=ComputedParameter(
+	# 					kind=ParameterKind.COMPUTED, type=ParameterComputeType.CASE_THEN,
+	# 					parameters=[
+	# 						*ArrayHelper(segments).map(
+	# 							lambda x: self.to_numeric_range_case_route(x, include, measure_on_factor)).to_list(),
+	# 						# an anyway route, additional
+	# 						ConstantParameter(kind=ParameterKind.CONSTANT, value='-')
+	# 					]
+	# 				),
+	# 				alias=f'column_{self.MEASURE_ON_COLUMN_ID}_{measure_on_index}'
+	# 			)
+	# 		elif measure_on == InspectMeasureOnType.OTHER:
+	# 			bucket = self.to_category_segments_bucket(bucket)
+	# 			segments = ArrayHelper(bucket.segments) \
+	# 				.filter(lambda x: x.value is not None and len(x.value) != 0).to_list()
+	# 			if len(segments) == 0:
+	# 				raise IndicatorKernelException('Category segments not declared.')
+	# 			anyway_segment: CategorySegment = ArrayHelper(segments) \
+	# 				.find(lambda x: len(x.value) == 1 and x.value[0] == OtherCategorySegmentValue)
+	# 			if anyway_segment is not None:
+	# 				conditional_routes = ArrayHelper(segments).filter(lambda x: x != anyway_segment).to_list()
+	# 				anyway_route = ConstantParameter(kind=ParameterKind.CONSTANT, value=anyway_segment.name)
+	# 			else:
+	# 				conditional_routes = segments
+	# 				anyway_route = ConstantParameter(kind=ParameterKind.CONSTANT, value='-')
+	#
+	# 			return SubjectDatasetColumn(
+	# 				columnId=f'{self.MEASURE_ON_COLUMN_ID}_{measure_on_index}',
+	# 				parameter=ComputedParameter(
+	# 					kind=ParameterKind.COMPUTED, type=ParameterComputeType.CASE_THEN,
+	# 					parameters=[
+	# 						*ArrayHelper(conditional_routes).map(
+	# 							lambda x: self.to_category_case_route(x, measure_on_factor)).to_list(),
+	# 						anyway_route
+	# 					]
+	# 				),
+	# 				alias=f'column_{self.MEASURE_ON_COLUMN_ID}_{measure_on_index}'
+	# 			)
+	# 		else:
+	# 			raise IndicatorKernelException(f'Measure[{measure_on}] is not supported.')
+	#
+	#
+	# def fake_measure_on_to_dataset_column(self) -> List[SubjectDatasetColumn]:
+	# 	return ArrayHelper(self.inspection.measures) \
+	# 		.map_with_index(lambda x, index: self.fake_measure_on_column(x, index + 1)) \
+	# 		.filter(lambda x: x is not None) \
+	# 		.to_list()
+	#
+	#
+	# # noinspection DuplicatedCode
+	# def fake_time_range_to_dataset_filter(self) -> Optional[ParameterJoint]:
+	# 	time_range_factor_id = self.inspection.timeRangeFactorId
+	# 	if is_blank(time_range_factor_id):
+	# 		return None
+	# 	time_range_factor = self.find_factor(time_range_factor_id, lambda: 'Time range factor not declared.')
+	# 	time_ranges = ArrayHelper(self.inspection.timeRanges) \
+	# 		.filter(lambda x: x is not None and x.value is not None).to_list()
+	# 	if len(time_ranges) == 0:
+	# 		# no ranges given
+	# 		return None
+	#
+	# 	operator = ParameterExpressionOperator.EQUALS if len(time_ranges) == 1 else ParameterExpressionOperator.IN
+	# 	right = time_ranges[0].value if len(time_ranges) == 1 \
+	# 		else ArrayHelper(time_ranges).map(lambda x: x.value).join(',')
+	# 	time_range_measure = self.inspection.timeRangeMeasure
+	# 	if self.is_datetime_factor(time_range_factor):
+	# 		if time_range_measure == MeasureMethod.YEAR:
+	# 			compute_type = ParameterComputeType.YEAR_OF
+	# 		elif time_range_measure == MeasureMethod.MONTH:
+	# 			compute_type = ParameterComputeType.MONTH_OF
+	# 		else:
+	# 			raise IndicatorKernelException(
+	# 				f'Measure method[{time_range_measure}] for factor type[{time_range_factor.type}] is not supported.')
+	# 		joint = ParameterJoint(
+	# 			jointType=ParameterJointType.AND,
+	# 			filters=[
+	# 				ParameterExpression(
+	# 					left=ComputedParameter(
+	# 						kind=ParameterKind.COMPUTED,
+	# 						type=compute_type,
+	# 						parameters=[
+	# 							TopicFactorParameter(
+	# 								kind=ParameterKind.TOPIC,
+	# 								topicId=self.topic.topicId, factorId=time_range_factor_id)
+	# 						]
+	# 					),
+	# 					operator=operator,
+	# 					right=ConstantParameter(kind=ParameterKind.CONSTANT, value=str(right))
+	# 				)
+	# 			]
+	# 		)
+	# 	else:
+	# 		joint = ParameterJoint(
+	# 			jointType=ParameterJointType.AND,
+	# 			filters=[
+	# 				ParameterExpression(
+	# 					left=TopicFactorParameter(
+	# 						kind=ParameterKind.TOPIC, topicId=self.topic.topicId, factorId=time_range_factor_id),
+	# 					operator=operator,
+	# 					right=ConstantParameter(kind=ParameterKind.CONSTANT, value=str(right))
+	# 				)
+	# 			]
+	# 		)
+	# 	return joint
+	#
+	#
+	# def has_indicator_filter(self) -> bool:
+	# 	return \
+	# 			self.indicator.filter is not None \
+	# 			and self.indicator.filter.enabled \
+	# 			and self.indicator.filter.joint is not None \
+	# 			and self.indicator.filter.joint.filters is not None \
+	# 			and len(self.indicator.filter.joint.filters) != 0
+	#
+	#
+	# # noinspection DuplicatedCode
+	# def fake_criteria_to_dataset_filter(self) -> Optional[ParameterJoint]:
+	# 	criteria = ArrayHelper(self.inspection.criteria).filter(lambda x: x is not None).to_list()
+	# 	if len(criteria) == 0:
+	# 		return None
+	#
+	# 	def to_condition(a_criteria: IndicatorCriteria) -> ParameterCondition:
+	# 		factor = self.find_factor(
+	# 			a_criteria.factorId,
+	# 			lambda: f'Factor of inspection criteria[{criteria.to_dict()}] not declared.')
+	# 		return self.fake_criteria_to_condition(a_criteria)(self.topic.topicId, factor.factorId)
+	#
+	# 	return ParameterJoint(
+	# 		jointType=ParameterJointType.AND,
+	# 		filters=ArrayHelper(criteria).map(to_condition).to_list()
+	# 	)
+	#
+	#
+	# # noinspection DuplicatedCode
+	# def build_filters(self) -> Optional[ParameterJoint]:
+	# 	time_range_filter = self.fake_time_range_to_dataset_filter()
+	# 	inspection_filter = self.fake_criteria_to_dataset_filter()
+	# 	indicator_filter = self.indicator.filter.joint if self.has_indicator_filter() else None
+	# 	filters = ArrayHelper([time_range_filter, inspection_filter, indicator_filter]) \
+	# 		.filter(lambda x: x is not None) \
+	# 		.to_list()
+	# 	if len(filters) == 0:
+	# 		return None
+	# 	else:
+	# 		return ParameterJoint(jointType=ParameterJointType.AND, filters=filters)
+	#
+	#
+	# def fake_to_subject(self) -> Subject:
+	# 	"""
+	# 	columns:
+	# 		[indicator column]
+	# 		[time group column]: optional, existing when time group declared
+	# 		[time group year/month column]: optional, existing when time group declared and original factor is datetime
+	# 		[measure_on_1, [measure_on_2, measure_on_3, ...]]: optional
+	# 	"""
+	# 	dataset_columns: List[SubjectDatasetColumn] = []
+	# 	# append indicator factor anyway
+	# 	indicator_factor_column = self.fake_indicator_factor_to_dataset_column()
+	# 	dataset_columns.append(indicator_factor_column)
+	# 	# append time group if exists
+	# 	time_group_column = self.fake_time_group_to_dataset_column()
+	# 	if time_group_column is not None:
+	# 		# append time group column
+	# 		dataset_columns.append(time_group_column)
+	# 		time_group_year_or_month_column = self.fake_time_group_year_or_month_to_dataset_column(time_group_column)
+	# 		if time_group_year_or_month_column is not None:
+	# 			dataset_columns.append(time_group_year_or_month_column)
+	# 	# measures
+	# 	measure_on_columns = self.fake_measure_on_to_dataset_column()
+	# 	if len(measure_on_columns) != 0:
+	# 		ArrayHelper(measure_on_columns).each(lambda x: dataset_columns.append(x))
+	#
+	# 	dataset_filters: Optional[ParameterJoint] = self.build_filters()
+	# 	return Subject(dataset=SubjectDataset(columns=dataset_columns, filters=dataset_filters))
+	#
+	#
+	# def fake_report_indicators(self) -> List[ReportIndicator]:
+	# 	indicators: List[ReportIndicator] = []
+	# 	self.fake_report_indicator(indicators, self.INDICATOR_FACTOR_COLUMN_ID)
+	# 	return indicators
+	#
+	#
+	# def fake_to_report(self, subject: Subject) -> Report:
+	# 	"""
+	# 	build report based on subject, columns in subject refers to fake_to_subject
+	# 	"""
+	# 	# build indicators
+	# 	indicators: List[ReportIndicator] = self.fake_report_indicators()
+	#
+	# 	# build dimensions: measure on 1, measure on 2, ..., time group
+	# 	dimensions: List[ReportDimension] = []
+	#
+	# 	# measures to dimensions
+	# 	def measure_to_dimension(column: SubjectDatasetColumn, index: int) -> None:
+	# 		dimensions.append(ReportDimension(columnId=column.columnId, name=f'_BUCKET_ON_{index}_'))
+	#
+	# 	ArrayHelper(subject.dataset.columns) \
+	# 		.filter(lambda x: x.columnId.startswith(self.MEASURE_ON_COLUMN_ID)) \
+	# 		.each_with_index(lambda x, index: measure_to_dimension(x, index + 1))
+	#
+	# 	# time group to dimensions
+	# 	time_group_year_or_month_column = ArrayHelper(subject.dataset.columns) \
+	# 		.find(lambda x: x.columnId == self.TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID)
+	# 	if time_group_year_or_month_column is not None:
+	# 		dimensions.append(
+	# 			ReportDimension(columnId=self.TIME_GROUP_YEAR_OR_MONTH_COLUMN_ID, name='_TIME_GROUP_'))
+	# 	else:
+	# 		time_group_column = ArrayHelper(subject.dataset.columns) \
+	# 			.find(lambda x: x.columnId == self.TIME_GROUP_COLUMN_ID)
+	# 		if time_group_column is not None:
+	# 			dimensions.append(ReportDimension(columnId=self.TIME_GROUP_COLUMN_ID, name='_TIME_GROUP_'))
+	#
+	# 	if len(dimensions) == 0:
+	# 		raise IndicatorKernelException('Neither time group nor bucket on found.')
+	#
+	# 	return Report(indicators=indicators, dimensions=dimensions)
+	#
+	#
+	# # noinspection PyMethodMayBeStatic
+	# def move_indicators_to_tail(self, row: DataResultSetRow, move_count: int) -> DataResultSetRow:
+	# 	return [*row[move_count:], *row[:move_count]]
+	#
+	#
+	# def find(self) -> DataResult:
+	# 	subject = self.fake_to_subject()
+	# 	report = self.fake_to_report(subject)
+	# 	report_data_service = get_report_data_service(subject, report, self.principalService)
+	# 	# reorder columns, move indicators to tail of row
+	# 	data_result = report_data_service.find()
+	# 	move_column_count = len(report.indicators)
+	# 	return DataResult(
+	# 		columns=data_result.columns,
+	# 		data=ArrayHelper(data_result.data).map(
+	# 			lambda x: self.move_indicators_to_tail(x, move_column_count)).to_list()
+	# 	)
```

### Comparing `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/achievement_task_service.py` & `watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/meta/achievement_task_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/bucket_service.py` & `watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/meta/bucket_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/indicator_service.py` & `watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/meta/indicator_service.py`

 * *Files 3% similar despite different names*

```diff
@@ -14,18 +14,14 @@
 		if a_filter is None:
 			return None
 		elif isinstance(a_filter, dict):
 			return a_filter
 		else:
 			return a_filter.dict()
 
-
-
-
-
 	def serialize(self, indicator: Indicator) -> EntityRow:
 		return TupleShaper.serialize_tenant_based(indicator, {
 			'indicator_id': indicator.indicatorId,
 			'name': indicator.name,
 			'topic_or_subject_id': indicator.topicOrSubjectId,
 			'factor_id': indicator.factorId,
 			'aggregate_arithmetic': indicator.aggregateArithmetic,
@@ -155,12 +151,12 @@
 		# noinspection PyTypeChecker
 		values = self.storage.find_distinct_values(self.get_entity_finder_for_columns(
 			criteria=criteria,
 			distinctColumnNames=column_names,
 			distinctValueOnSingleColumn=True
 		))
 		if len(prefix) == 0:
-			return ArrayHelper(values).map(lambda x: x.category1).to_list()
+			return ArrayHelper(values).filter(lambda  x : x.category1).map(lambda x: x.category1).to_list()
 		elif len(prefix) == 1:
-			return ArrayHelper(values).map(lambda x: x.category2).to_list()
+			return ArrayHelper(values).filter(lambda  x : x.category2).map(lambda x: x.category2).to_list()
 		else:
-			return ArrayHelper(values).map(lambda x: x.category3).to_list()
+			return ArrayHelper(values).filter(lambda  x : x.category3).map(lambda x: x.category3).to_list()
```

### Comparing `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/plugin/connector.py` & `watchmen_indicator_kernel-16.5.0/src/watchmen_indicator_kernel/plugin/connector.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.9/PKG-INFO` & `watchmen_indicator_kernel-16.5.0/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: watchmen-indicator-kernel
-Version: 16.4.9
+Version: 16.5.0
 Summary: 
 License: MIT
 Author: botlikes
 Author-email: 75356972+botlikes456@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
@@ -15,16 +15,16 @@
 Provides-Extra: mssql
 Provides-Extra: mysql
 Provides-Extra: oracle
 Provides-Extra: oss
 Provides-Extra: postgresql
 Provides-Extra: s3
 Provides-Extra: trino
-Requires-Dist: watchmen-inquiry-kernel (==16.4.9)
-Requires-Dist: watchmen-inquiry-trino (==16.4.9) ; extra == "trino"
-Requires-Dist: watchmen-storage-mongodb (==16.4.9) ; extra == "mongodb"
-Requires-Dist: watchmen-storage-mssql (==16.4.9) ; extra == "mssql"
-Requires-Dist: watchmen-storage-mysql (==16.4.9) ; extra == "mysql"
-Requires-Dist: watchmen-storage-oracle (==16.4.9) ; extra == "oracle"
-Requires-Dist: watchmen-storage-oss (==16.4.9) ; extra == "oss"
-Requires-Dist: watchmen-storage-postgresql (==16.4.9) ; extra == "postgresql"
-Requires-Dist: watchmen-storage-s3 (==16.4.9) ; extra == "s3"
+Requires-Dist: watchmen-inquiry-kernel (==16.5.0)
+Requires-Dist: watchmen-inquiry-trino (==16.5.0) ; extra == "trino"
+Requires-Dist: watchmen-storage-mongodb (==16.5.0) ; extra == "mongodb"
+Requires-Dist: watchmen-storage-mssql (==16.5.0) ; extra == "mssql"
+Requires-Dist: watchmen-storage-mysql (==16.5.0) ; extra == "mysql"
+Requires-Dist: watchmen-storage-oracle (==16.5.0) ; extra == "oracle"
+Requires-Dist: watchmen-storage-oss (==16.5.0) ; extra == "oss"
+Requires-Dist: watchmen-storage-postgresql (==16.5.0) ; extra == "postgresql"
+Requires-Dist: watchmen-storage-s3 (==16.5.0) ; extra == "s3"
```

