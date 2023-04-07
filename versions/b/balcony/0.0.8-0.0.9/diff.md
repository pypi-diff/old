# Comparing `tmp/balcony-0.0.8.tar.gz` & `tmp/balcony-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "balcony-0.0.8.tar", max compression
+gzip compressed data, was "balcony-0.0.9.tar", max compression
```

## Comparing `balcony-0.0.8.tar` & `balcony-0.0.9.tar`

### file list

```diff
@@ -1,29 +1,29 @@
--rw-r--r--   0        0        0    35149 2022-09-26 12:31:10.748997 balcony-0.0.8/LICENSE
--rw-r--r--   0        0        0      353 2022-09-26 12:41:48.924073 balcony-0.0.8/README.md
--rw-r--r--   0        0        0      286 2022-10-09 10:37:47.142816 balcony-0.0.8/balcony/__init__.py
--rw-r--r--   0        0        0       53 2022-10-04 08:01:49.289224 balcony-0.0.8/balcony/__main__.py
--rw-r--r--   0        0        0     1432 2022-10-09 09:50:45.143185 balcony-0.0.8/balcony/app.py
--rw-r--r--   0        0        0    10347 2022-10-08 07:04:48.840377 balcony-0.0.8/balcony/botocore_utils.py
--rw-r--r--   0        0        0     7724 2022-10-09 10:41:41.880849 balcony-0.0.8/balcony/cli.py
--rw-r--r--   0        0        0      264 2022-09-30 20:25:42.597791 balcony-0.0.8/balcony/custom_nodes/__init__.py
--rw-r--r--   0        0        0     1444 2022-09-29 13:15:21.107762 balcony-0.0.8/balcony/custom_nodes/codebuild.py
--rw-r--r--   0        0        0     1091 2022-09-29 13:15:21.107587 balcony-0.0.8/balcony/custom_nodes/ec2.py
--rw-r--r--   0        0        0     2530 2022-09-29 13:15:21.126367 balcony-0.0.8/balcony/custom_nodes/ecs.py
--rw-r--r--   0        0        0     2798 2022-10-07 10:38:54.655726 balcony-0.0.8/balcony/custom_nodes/iam.py
--rw-r--r--   0        0        0     1018 2022-09-29 19:23:48.871446 balcony-0.0.8/balcony/custom_nodes/lambda_functions.py
--rw-r--r--   0        0        0     1410 2022-10-01 08:48:13.809464 balcony-0.0.8/balcony/custom_nodes/s3.py
--rw-r--r--   0        0        0     2214 2022-09-30 20:31:15.045592 balcony-0.0.8/balcony/custom_nodes/ssm.py
--rw-r--r--   0        0        0       26 2022-10-04 07:57:08.884233 balcony-0.0.8/balcony/exceptions.py
--rw-r--r--   0        0        0     2011 2022-10-09 10:37:09.474616 balcony-0.0.8/balcony/factories.py
--rw-r--r--   0        0        0     1261 2022-09-26 08:05:59.761176 balcony-0.0.8/balcony/logs.py
--rw-r--r--   0        0        0     4012 2022-10-09 11:11:51.901472 balcony-0.0.8/balcony/main.py
--rw-r--r--   0        0        0    33760 2022-10-09 10:52:29.206820 balcony-0.0.8/balcony/nodes.py
--rw-r--r--   0        0        0    20631 2022-10-08 07:33:05.175728 balcony-0.0.8/balcony/reader.py
--rw-r--r--   0        0        0     6560 2022-10-09 10:03:48.761239 balcony-0.0.8/balcony/registries.py
--rw-r--r--   0        0        0     9339 2022-10-01 08:20:11.194551 balcony-0.0.8/balcony/relations.py
--rw-r--r--   0        0        0      179 2022-09-26 05:42:59.824683 balcony-0.0.8/balcony/rrr.py
--rw-r--r--   0        0        0        0 2022-10-09 10:36:26.833986 balcony-0.0.8/balcony/settings.py
--rw-r--r--   0        0        0     3231 2022-10-08 07:24:30.953384 balcony-0.0.8/balcony/utils.py
--rw-r--r--   0        0        0      521 2022-10-09 13:34:36.361969 balcony-0.0.8/pyproject.toml
--rw-r--r--   0        0        0     1226 1970-01-01 00:00:00.000000 balcony-0.0.8/setup.py
--rw-r--r--   0        0        0     1124 1970-01-01 00:00:00.000000 balcony-0.0.8/PKG-INFO
+-rw-r--r--   0        0        0    35149 2022-09-26 12:31:10.748997 balcony-0.0.9/LICENSE
+-rw-r--r--   0        0        0      353 2022-09-26 12:41:48.924073 balcony-0.0.9/README.md
+-rw-r--r--   0        0        0      286 2022-10-09 10:37:47.142816 balcony-0.0.9/balcony/__init__.py
+-rw-r--r--   0        0        0       53 2022-10-04 08:01:49.289224 balcony-0.0.9/balcony/__main__.py
+-rw-r--r--   0        0        0     1432 2022-10-09 09:50:45.143185 balcony-0.0.9/balcony/app.py
+-rw-r--r--   0        0        0    10347 2022-10-08 07:04:48.840377 balcony-0.0.9/balcony/botocore_utils.py
+-rw-r--r--   0        0        0     7724 2022-10-09 10:41:41.880849 balcony-0.0.9/balcony/cli.py
+-rw-r--r--   0        0        0      264 2022-09-30 20:25:42.597791 balcony-0.0.9/balcony/custom_nodes/__init__.py
+-rw-r--r--   0        0        0     1444 2022-09-29 13:15:21.107762 balcony-0.0.9/balcony/custom_nodes/codebuild.py
+-rw-r--r--   0        0        0     1095 2022-10-09 17:51:42.748364 balcony-0.0.9/balcony/custom_nodes/ec2.py
+-rw-r--r--   0        0        0     2530 2022-09-29 13:15:21.126367 balcony-0.0.9/balcony/custom_nodes/ecs.py
+-rw-r--r--   0        0        0     3140 2022-10-10 07:22:17.872579 balcony-0.0.9/balcony/custom_nodes/iam.py
+-rw-r--r--   0        0        0     1018 2022-09-29 19:23:48.871446 balcony-0.0.9/balcony/custom_nodes/lambda_functions.py
+-rw-r--r--   0        0        0     1410 2022-10-01 08:48:13.809464 balcony-0.0.9/balcony/custom_nodes/s3.py
+-rw-r--r--   0        0        0     2214 2022-09-30 20:31:15.045592 balcony-0.0.9/balcony/custom_nodes/ssm.py
+-rw-r--r--   0        0        0       26 2022-10-04 07:57:08.884233 balcony-0.0.9/balcony/exceptions.py
+-rw-r--r--   0        0        0     2011 2022-10-09 10:37:09.474616 balcony-0.0.9/balcony/factories.py
+-rw-r--r--   0        0        0     1261 2022-09-26 08:05:59.761176 balcony-0.0.9/balcony/logs.py
+-rw-r--r--   0        0        0     4012 2022-10-09 11:11:51.901472 balcony-0.0.9/balcony/main.py
+-rw-r--r--   0        0        0    33760 2022-10-09 10:52:29.206820 balcony-0.0.9/balcony/nodes.py
+-rw-r--r--   0        0        0    20844 2022-10-11 20:37:36.250496 balcony-0.0.9/balcony/reader.py
+-rw-r--r--   0        0        0     6560 2022-10-09 10:03:48.761239 balcony-0.0.9/balcony/registries.py
+-rw-r--r--   0        0        0     9472 2022-10-09 17:45:39.425216 balcony-0.0.9/balcony/relations.py
+-rw-r--r--   0        0        0      386 2022-10-13 07:07:22.872196 balcony-0.0.9/balcony/rrr.py
+-rw-r--r--   0        0        0      377 2022-10-09 17:48:27.201727 balcony-0.0.9/balcony/settings.py
+-rw-r--r--   0        0        0     3231 2022-10-08 07:24:30.953384 balcony-0.0.9/balcony/utils.py
+-rw-r--r--   0        0        0      521 2022-10-13 07:16:58.915722 balcony-0.0.9/pyproject.toml
+-rw-r--r--   0        0        0     1226 1970-01-01 00:00:00.000000 balcony-0.0.9/setup.py
+-rw-r--r--   0        0        0     1124 1970-01-01 00:00:00.000000 balcony-0.0.9/PKG-INFO
```

### Comparing `balcony-0.0.8/LICENSE` & `balcony-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/app.py` & `balcony-0.0.9/balcony/app.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/botocore_utils.py` & `balcony-0.0.9/balcony/botocore_utils.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/cli.py` & `balcony-0.0.9/balcony/cli.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/custom_nodes/codebuild.py` & `balcony-0.0.9/balcony/custom_nodes/codebuild.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/custom_nodes/ec2.py` & `balcony-0.0.9/balcony/custom_nodes/ec2.py`

 * *Files 1% similar despite different names*

```diff
@@ -11,16 +11,16 @@
 logger = get_logger(__name__)
 
 
 class EC2_SecurityGroups(ResourceNode, ResourceNodeRegistry, service_name="ec2", name="SecurityGroups"):
     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         
-    def get_operations_relations(self, operation_name, relation_map):
-        r = super().get_operations_relations(operation_name, relation_map)
+    # def get_operations_relations(self, operation_name, relation_map):
+    #     r = super().get_operations_relations(operation_name, relation_map)
         
 """
 1. check for already existing operation data
 2. get relations of the operation
 3. find the dependent operations to call
 4. read the target dependent operation
 5. generate JMESpath selectors with the relations
```

### Comparing `balcony-0.0.8/balcony/custom_nodes/ecs.py` & `balcony-0.0.9/balcony/custom_nodes/ecs.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/custom_nodes/iam.py` & `balcony-0.0.9/balcony/custom_nodes/iam.py`

 * *Files 5% similar despite different names*

```diff
@@ -22,24 +22,33 @@
             "service_name": "iam",
             "resource_node_name": "Policy",
             "search_shape_name": "PolicyArn",
             "target_shape_name": "Arn",
             "target_shape_type": "string",
             "operation_name": "ListPolicies",
             "target_path": "Policies[*].Arn"
+        },
+        {
+            "service_name": "iam",
+            "resource_node_name": "Policy",
+            "search_shape_name": "VersionId",
+            "target_shape_name": "DefaultVersionId",
+            "target_shape_type": "string",
+            "operation_name": "ListPolicies",
+            "target_path": "Policies[*].DefaultVersionId"
         }]
 
 class IAM_User(ResourceNode, ResourceNodeRegistry, service_name="iam", name="User"):
     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
     
     def define_extra_relations(self):
         r= super().define_extra_relations()
         return [{
-                "service_name": "iam",
+            "service_name": "iam",
             "resource_node_name": "User",
             "search_shape_name": "UserName",
             "target_shape_name": "UserName",
             "target_shape_type": "string",
             "operation_name": "ListUsers",
             "target_path": "Users[*].UserName"
         }]
```

### Comparing `balcony-0.0.8/balcony/custom_nodes/lambda_functions.py` & `balcony-0.0.9/balcony/custom_nodes/lambda_functions.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/custom_nodes/s3.py` & `balcony-0.0.9/balcony/custom_nodes/s3.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/custom_nodes/ssm.py` & `balcony-0.0.9/balcony/custom_nodes/ssm.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/factories.py` & `balcony-0.0.9/balcony/factories.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/logs.py` & `balcony-0.0.9/balcony/logs.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/main.py` & `balcony-0.0.9/balcony/main.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/nodes.py` & `balcony-0.0.9/balcony/nodes.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/reader.py` & `balcony-0.0.9/balcony/reader.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,22 +1,23 @@
 try:
     from .utils import icompare_two_camel_case_words, str_relations, ifind_similar_names_in_list
     from .botocore_utils import READ_ONLY_VERBS
     from .relations import FindRelationResultTypes, SUCCESSFUL_FIND_RELATION_RESULT_TYPES
-    from .logs import get_logger
+    from .logs import get_logger, get_rich_console
 except ImportError:
     from utils import icompare_two_camel_case_words, str_relations, ifind_similar_names_in_list
     from botocore_utils import READ_ONLY_VERBS
     from relations import FindRelationResultTypes, SUCCESSFUL_FIND_RELATION_RESULT_TYPES
-    from logs import get_logger
+    from logs import get_logger, get_rich_console
 from collections.abc import Iterable
 import jmespath
 from rich.progress import Progress, track, BarColumn, TextColumn, TaskProgressColumn, TimeRemainingColumn
 from rich.table import Column
 logger = get_logger(__name__)
+console = get_rich_console()
 class ServiceReader:
     def __init__(self, service_node):
         self.service_node = service_node
         self.response_data = {}
 
     def add_response_data(self, operation_name, response):
         if operation_name not in self.response_data:
@@ -211,15 +212,15 @@
 
         # send the operations_data to resource_node to create valid_api_parameters
         generated_api_parameters = resource_node.generate_api_parameters_from_operation_data(operation_name, relations_of_operation, related_operations_data)
 
         if generated_api_parameters == []:
             logger.debug(f"FAILED TO AUTO-GENERATE API PARAMETERS. Related Resources couldn't found.")
         elif isinstance(generated_api_parameters, Iterable):
-            for api_parameters in generated_api_parameters:
+            for api_parameters in track(generated_api_parameters, description=f"Calling [green]{operation_name}[/] for [bold]{len(generated_api_parameters)}[/] resources...",transient=True, console=console):
                 self._call_operation(operation_name, api_parameters)
         else:
             logger.debug(f"COULDN'T GENERATE API PARAMETERS. {resource_node_name}.{operation_name}. Generated Parameters: {generated_api_parameters}. Data: {all_related_operations_data}")
             
         return self.search_operation_data(resource_node_name, operation_name)
```

### Comparing `balcony-0.0.8/balcony/registries.py` & `balcony-0.0.9/balcony/registries.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/balcony/relations.py` & `balcony-0.0.9/balcony/relations.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,15 +1,17 @@
 try:
     from .botocore_utils import get_shape_name, flatten_shape_to_its_non_collection_shape_and_target_paths, IDENTIFIER_NAMES
     from .logs import get_logger
     from .utils import icompare_two_camel_case_words
+    from .settings import BALCONY_RELATIONS_DIR
 except ImportError:
     from botocore_utils import get_shape_name, flatten_shape_to_its_non_collection_shape_and_target_paths, IDENTIFIER_NAMES
     from logs import get_logger
     from utils import icompare_two_camel_case_words
+    from settings import BALCONY_RELATIONS_DIR
 
 import json
 import os
 from enum import Enum
 logger = get_logger(__name__)
 
 class FindRelationResultTypes(Enum):
@@ -72,23 +74,25 @@
         resource_node = self.service_node.find_resource_node_by_operation_name(operation_name)
         if not resource_node:
             return False
         relation_map = self
         result = resource_node.find_best_relations_for_operation(operation_name, relation_map)
         return result
             
-    def _save_relations_map_to_file(self, relations_map=None, directory='relations'):
+    def _save_relations_map_to_file(self, relations_map=None):
+        directory = BALCONY_RELATIONS_DIR
         service_name = self.service_node.name
         filepath = os.path.join(directory, f"{service_name}.json")
         relations_map = self.get_relations_map()
         with open(filepath, 'w') as file:
             json.dump(relations_map, file, indent=2, default=str)
         return True
 
-    def _load_relations_from_file(self, directory='relations'):
+    def _load_relations_from_file(self):
+        directory = BALCONY_RELATIONS_DIR
         service_name = self.service_node.name
         filepath = os.path.join(directory, f"{service_name}.json")
         if not os.path.isfile(filepath):
             return False
         relations_map = None
         with open(filepath, 'r') as file:
             relations_map = json.load(file)
```

### Comparing `balcony-0.0.8/balcony/utils.py` & `balcony-0.0.9/balcony/utils.py`

 * *Files identical despite different names*

### Comparing `balcony-0.0.8/pyproject.toml` & `balcony-0.0.9/pyproject.toml`

 * *Files 22% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "balcony"
-version = "0.0.8"
+version = "0.0.9"
 description = "AWS API for humans"
 authors = ["Oguzhan Yilmaz <oguzhanylmz271@gmail.com>"]
 license = "GPL-3.0-or-later"
 readme = "README.md"
 
 [tool.poetry.scripts]
 balcony = "balcony.cli:run_app"
```

### Comparing `balcony-0.0.8/setup.py` & `balcony-0.0.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,15 +15,15 @@
  'typer>=0.6.1,<0.7.0']
 
 entry_points = \
 {'console_scripts': ['balcony = balcony.cli:run_app']}
 
 setup_kwargs = {
     'name': 'balcony',
-    'version': '0.0.8',
+    'version': '0.0.9',
     'description': 'AWS API for humans',
     'long_description': '# balcony\nAWS API for humans\n\n\n## Installation\n\n```bash\npip3 install balcony\n```\n\n## Basic Usage\n\n\n```bash\nbalcony --help\n\n# list all available services\nbalcony aws ls \n\n# list resource nodes of a service\nbalcony aws ls iam\n\n# details about the resource node\nbalcony aws ls iam Policy\n\n# read a Resource Node from AWS API\nbalcony aws read iam Policy\n```',
     'author': 'Oguzhan Yilmaz',
     'author_email': 'oguzhanylmz271@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `balcony-0.0.8/PKG-INFO` & `balcony-0.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: balcony
-Version: 0.0.8
+Version: 0.0.9
 Summary: AWS API for humans
 License: GPL-3.0-or-later
 Author: Oguzhan Yilmaz
 Author-email: oguzhanylmz271@gmail.com
 Requires-Python: >=3.7,<4.0
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
 Classifier: Programming Language :: Python :: 3
```

