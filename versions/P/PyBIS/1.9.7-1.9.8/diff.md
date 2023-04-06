# Comparing `tmp/PyBIS-1.9.7.tar.gz` & `tmp/PyBIS-1.9.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/PyBIS-1.9.7.tar", last modified: Tue Oct 22 22:37:31 2019, max compression
+gzip compressed data, was "dist/PyBIS-1.9.8.tar", last modified: Thu Oct 24 09:09:49 2019, max compression
```

## Comparing `PyBIS-1.9.7.tar` & `PyBIS-1.9.8.tar`

### file list

```diff
@@ -1,40 +1,40 @@
-drwxr-xr-x   0 vermeul    (502) staff       (20)        0 2019-10-22 22:37:31.000000 PyBIS-1.9.7/
--rw-r--r--   0 vermeul    (502) staff       (20)    25089 2019-10-22 22:37:31.000000 PyBIS-1.9.7/PKG-INFO
--rw-r--r--   0 vermeul    (502) staff       (20)    11357 2019-03-04 15:22:24.000000 PyBIS-1.9.7/LICENSE
--rw-r--r--   0 vermeul    (502) staff       (20)     5088 2019-10-22 22:34:39.000000 PyBIS-1.9.7/CHANGELOG.md
-drwxr-xr-x   0 vermeul    (502) staff       (20)        0 2019-10-22 22:37:30.000000 PyBIS-1.9.7/PyBIS.egg-info/
--rw-r--r--   0 vermeul    (502) staff       (20)    25089 2019-10-22 22:37:29.000000 PyBIS-1.9.7/PyBIS.egg-info/PKG-INFO
--rw-r--r--   0 vermeul    (502) staff       (20)      641 2019-10-22 22:37:29.000000 PyBIS-1.9.7/PyBIS.egg-info/SOURCES.txt
--rw-r--r--   0 vermeul    (502) staff       (20)       57 2019-10-22 22:37:29.000000 PyBIS-1.9.7/PyBIS.egg-info/requires.txt
--rw-r--r--   0 vermeul    (502) staff       (20)        6 2019-10-22 22:37:29.000000 PyBIS-1.9.7/PyBIS.egg-info/top_level.txt
--rw-r--r--   0 vermeul    (502) staff       (20)        1 2019-10-22 22:37:29.000000 PyBIS-1.9.7/PyBIS.egg-info/dependency_links.txt
--rw-r--r--   0 vermeul    (502) staff       (20)       78 2018-11-13 15:52:02.000000 PyBIS-1.9.7/MANIFEST.in
--rw-r--r--   0 vermeul    (502) staff       (20)    19647 2019-10-22 22:33:31.000000 PyBIS-1.9.7/README.md
--rw-r--r--   0 vermeul    (502) staff       (20)     1075 2019-10-22 22:34:39.000000 PyBIS-1.9.7/setup.py
--rw-r--r--   0 vermeul    (502) staff       (20)      359 2019-08-07 09:11:01.000000 PyBIS-1.9.7/TODOS.md
-drwxr-xr-x   0 vermeul    (502) staff       (20)        0 2019-10-22 22:37:31.000000 PyBIS-1.9.7/pybis/
--rw-r--r--   0 vermeul    (502) staff       (20)     6752 2019-08-23 09:13:59.000000 PyBIS-1.9.7/pybis/things.py
--rw-r--r--   0 vermeul    (502) staff       (20)     2362 2019-09-17 10:13:54.000000 PyBIS-1.9.7/pybis/material.py
--rw-r--r--   0 vermeul    (502) staff       (20)     4084 2019-08-19 12:39:05.000000 PyBIS-1.9.7/pybis/person.py
--rw-r--r--   0 vermeul    (502) staff       (20)    36727 2019-10-22 22:33:31.000000 PyBIS-1.9.7/pybis/attribute.py
--rw-r--r--   0 vermeul    (502) staff       (20)    25463 2019-10-22 22:33:31.000000 PyBIS-1.9.7/pybis/definitions.py
--rw-r--r--   0 vermeul    (502) staff       (20)     6403 2019-10-01 14:12:57.000000 PyBIS-1.9.7/pybis/property.py
--rw-r--r--   0 vermeul    (502) staff       (20)      167 2019-10-22 22:34:39.000000 PyBIS-1.9.7/pybis/__init__.py
--rw-r--r--   0 vermeul    (502) staff       (20)     6170 2018-09-03 08:20:50.000000 PyBIS-1.9.7/pybis/semantic_annotation.py
--rw-r--r--   0 vermeul    (502) staff       (20)     1252 2019-08-23 09:13:59.000000 PyBIS-1.9.7/pybis/role_assignment.py
--rw-r--r--   0 vermeul    (502) staff       (20)     9398 2019-09-17 10:56:21.000000 PyBIS-1.9.7/pybis/entity_type.py
--rw-r--r--   0 vermeul    (502) staff       (20)    26537 2019-08-23 09:13:59.000000 PyBIS-1.9.7/pybis/dataset.py
--rw-r--r--   0 vermeul    (502) staff       (20)     4071 2019-08-23 09:13:59.000000 PyBIS-1.9.7/pybis/experiment.py
--rw-r--r--   0 vermeul    (502) staff       (20)   122614 2019-10-01 14:12:57.000000 PyBIS-1.9.7/pybis/pybis.py
--rw-r--r--   0 vermeul    (502) staff       (20)      904 2018-06-11 14:30:14.000000 PyBIS-1.9.7/pybis/attachment.py
--rw-r--r--   0 vermeul    (502) staff       (20)     7070 2019-08-23 09:13:59.000000 PyBIS-1.9.7/pybis/utils.py
--rw-r--r--   0 vermeul    (502) staff       (20)     6242 2019-08-23 10:34:30.000000 PyBIS-1.9.7/pybis/openbis_object.py
--rw-r--r--   0 vermeul    (502) staff       (20)    12843 2019-06-11 08:12:08.000000 PyBIS-1.9.7/pybis/data_set.py
--rw-r--r--   0 vermeul    (502) staff       (20)     5384 2019-08-23 09:13:59.000000 PyBIS-1.9.7/pybis/sample.py
--rw-r--r--   0 vermeul    (502) staff       (20)     4856 2019-08-23 09:13:59.000000 PyBIS-1.9.7/pybis/group.py
--rw-r--r--   0 vermeul    (502) staff       (20)     1718 2019-08-23 09:13:59.000000 PyBIS-1.9.7/pybis/space.py
--rw-r--r--   0 vermeul    (502) staff       (20)     8962 2019-09-17 10:13:54.000000 PyBIS-1.9.7/pybis/vocabulary.py
--rw-r--r--   0 vermeul    (502) staff       (20)     1386 2019-08-23 09:13:59.000000 PyBIS-1.9.7/pybis/project.py
--rw-r--r--   0 vermeul    (502) staff       (20)      799 2019-08-23 09:13:59.000000 PyBIS-1.9.7/pybis/tag.py
--rw-r--r--   0 vermeul    (502) staff       (20)       38 2019-10-22 22:37:31.000000 PyBIS-1.9.7/setup.cfg
--rw-r--r--   0 vermeul    (502) staff       (20)    18754 2019-05-21 19:45:32.000000 PyBIS-1.9.7/README.rst
+drwxr-xr-x   0 vermeul    (502) staff       (20)        0 2019-10-24 09:09:49.000000 PyBIS-1.9.8/
+-rw-r--r--   0 vermeul    (502) staff       (20)    29035 2019-10-24 09:09:49.000000 PyBIS-1.9.8/PKG-INFO
+-rw-r--r--   0 vermeul    (502) staff       (20)    11357 2019-03-04 15:22:24.000000 PyBIS-1.9.8/LICENSE
+-rw-r--r--   0 vermeul    (502) staff       (20)     5315 2019-10-24 09:09:05.000000 PyBIS-1.9.8/CHANGELOG.md
+drwxr-xr-x   0 vermeul    (502) staff       (20)        0 2019-10-24 09:09:49.000000 PyBIS-1.9.8/PyBIS.egg-info/
+-rw-r--r--   0 vermeul    (502) staff       (20)    29035 2019-10-24 09:09:48.000000 PyBIS-1.9.8/PyBIS.egg-info/PKG-INFO
+-rw-r--r--   0 vermeul    (502) staff       (20)      641 2019-10-24 09:09:48.000000 PyBIS-1.9.8/PyBIS.egg-info/SOURCES.txt
+-rw-r--r--   0 vermeul    (502) staff       (20)       57 2019-10-24 09:09:48.000000 PyBIS-1.9.8/PyBIS.egg-info/requires.txt
+-rw-r--r--   0 vermeul    (502) staff       (20)        6 2019-10-24 09:09:48.000000 PyBIS-1.9.8/PyBIS.egg-info/top_level.txt
+-rw-r--r--   0 vermeul    (502) staff       (20)        1 2019-10-24 09:09:48.000000 PyBIS-1.9.8/PyBIS.egg-info/dependency_links.txt
+-rw-r--r--   0 vermeul    (502) staff       (20)       78 2018-11-13 15:52:02.000000 PyBIS-1.9.8/MANIFEST.in
+-rw-r--r--   0 vermeul    (502) staff       (20)    22753 2019-10-24 09:08:40.000000 PyBIS-1.9.8/README.md
+-rw-r--r--   0 vermeul    (502) staff       (20)     1075 2019-10-24 09:09:05.000000 PyBIS-1.9.8/setup.py
+-rw-r--r--   0 vermeul    (502) staff       (20)      359 2019-08-07 09:11:01.000000 PyBIS-1.9.8/TODOS.md
+drwxr-xr-x   0 vermeul    (502) staff       (20)        0 2019-10-24 09:09:49.000000 PyBIS-1.9.8/pybis/
+-rw-r--r--   0 vermeul    (502) staff       (20)     6752 2019-08-23 09:13:59.000000 PyBIS-1.9.8/pybis/things.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     2362 2019-09-17 10:13:54.000000 PyBIS-1.9.8/pybis/material.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     4084 2019-08-19 12:39:05.000000 PyBIS-1.9.8/pybis/person.py
+-rw-r--r--   0 vermeul    (502) staff       (20)    37485 2019-10-24 09:09:05.000000 PyBIS-1.9.8/pybis/attribute.py
+-rw-r--r--   0 vermeul    (502) staff       (20)    25415 2019-10-24 09:08:40.000000 PyBIS-1.9.8/pybis/definitions.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     6403 2019-10-01 14:12:57.000000 PyBIS-1.9.8/pybis/property.py
+-rw-r--r--   0 vermeul    (502) staff       (20)      167 2019-10-24 09:09:05.000000 PyBIS-1.9.8/pybis/__init__.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     6170 2018-09-03 08:20:50.000000 PyBIS-1.9.8/pybis/semantic_annotation.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     1252 2019-08-23 09:13:59.000000 PyBIS-1.9.8/pybis/role_assignment.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     9706 2019-10-24 09:08:40.000000 PyBIS-1.9.8/pybis/entity_type.py
+-rw-r--r--   0 vermeul    (502) staff       (20)    26537 2019-08-23 09:13:59.000000 PyBIS-1.9.8/pybis/dataset.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     4071 2019-08-23 09:13:59.000000 PyBIS-1.9.8/pybis/experiment.py
+-rw-r--r--   0 vermeul    (502) staff       (20)   124216 2019-10-24 09:09:05.000000 PyBIS-1.9.8/pybis/pybis.py
+-rw-r--r--   0 vermeul    (502) staff       (20)      904 2018-06-11 14:30:14.000000 PyBIS-1.9.8/pybis/attachment.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     7253 2019-10-24 09:08:40.000000 PyBIS-1.9.8/pybis/utils.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     6242 2019-10-23 12:45:58.000000 PyBIS-1.9.8/pybis/openbis_object.py
+-rw-r--r--   0 vermeul    (502) staff       (20)    12843 2019-06-11 08:12:08.000000 PyBIS-1.9.8/pybis/data_set.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     5384 2019-08-23 09:13:59.000000 PyBIS-1.9.8/pybis/sample.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     4856 2019-08-23 09:13:59.000000 PyBIS-1.9.8/pybis/group.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     1718 2019-08-23 09:13:59.000000 PyBIS-1.9.8/pybis/space.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     8962 2019-09-17 10:13:54.000000 PyBIS-1.9.8/pybis/vocabulary.py
+-rw-r--r--   0 vermeul    (502) staff       (20)     1386 2019-08-23 09:13:59.000000 PyBIS-1.9.8/pybis/project.py
+-rw-r--r--   0 vermeul    (502) staff       (20)      799 2019-08-23 09:13:59.000000 PyBIS-1.9.8/pybis/tag.py
+-rw-r--r--   0 vermeul    (502) staff       (20)       38 2019-10-24 09:09:49.000000 PyBIS-1.9.8/setup.cfg
+-rw-r--r--   0 vermeul    (502) staff       (20)    18754 2019-05-21 19:45:32.000000 PyBIS-1.9.8/README.rst
```

### Comparing `PyBIS-1.9.7/PKG-INFO` & `PyBIS-1.9.8/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PyBIS
-Version: 1.9.7
+Version: 1.9.8
 Summary: openBIS connection and interaction, optimized for using with Jupyter
 Home-page: https://sissource.ethz.ch/sispub/openbis/tree/master/pybis
 Author: Swen Vermeul • ID SIS • ETH Zürich
 Author-email: swen@ethz.ch
 License: Apache Software License Version 2.0
 Description: # Welcome to pyBIS!
         pyBIS is a Python module for interacting with openBIS, designed to be used in Jupyter. It offers some sort of IDE for openBIS, supporting TAB completition and input checks, making the life of a researcher hopefully easier.
@@ -24,73 +24,87 @@
         
         If you haven't done yet, install Jupyter Notebook:
         
         ```
         pip install jupyter
         ```
         
-        # Usage
+        # General Usage
         
         ## Tab completition and other hints
         Used in a Jupyter Notebook environment, pybis helps you to enter the commands. After every dot `.` you might hit the `TAB` key in order to look at the available commands.
         
         If you are unsure what parameters to add to a , add a question mark right after the method and hit `SHIFT+ENTER`. Jupyter will then look up the signature of the method and show some helpful docstring.
         
         When working with properties of entities, they might use a **controlled vocabulary** or are of a specific **property type**. Add an underscore `_` character right after the property and hit `SHIFT+ENTER` to show the valid values. When a property only acceps a controlled vocabulary, you will be shown the valid terms in a nicely formatted table.
         
-        ## connect to from OpenBIS
+        ## connect to OpenBIS
+        
+        Interactivel, i.e. within a Jupyter notebook, you can use `getpass` to enter your password:
         
         ```
         from pybis import Openbis
         o = Openbis('https://example.com', verify_certificates=False)
         
         import getpass
         password = getpass.getpass()
         
         o.login('username', password, save_token=True)   # save the session token in ~/.pybis/example.com.token
         ```
         
+        In a script you would rather use two environment variables to provide username and password:
+        
+        ```
+        from pybis import Openbis
+        o = Openbis(os.environ['OPENBIS_HOST'], verify_certificates=False)
+        
+        o.login(os.environ['OPENBIS_USERNAME'], os.environ['OPENBIS_PASSWORD'])
+        ```
+        
+        
         Check whether the session token is still valid and log out:
         
         ```
         o.token
         o.is_session_active()
         o.logout()
         ```
         
-        ## browsing masterdata
+        # Masterdata
+        OpenBIS stores quite a lot of meta-data along with your dataSets. The collection of data that describes this meta-data (i.e. meta-meta-data) is called masterdata. It consists of:
+        
+        * sample types
+        * dataSet types
+        * material types
+        * experiment types
+        * property types
+        * vocabularies
+        * vocabulary terms
+        * plugins (jython scripts that allow complex data checks)
+        * tags
+        * semantic annotations
+        
+        ## browse masterdata
+        
         ```
         sample_types = o.get_sample_types()  # get a list of sample types 
         sample_types.df                      # DataFrame object
         st = o.get_sample_types()[3]         # get 4th element of that list
         st = o.get_sample_type('YEAST')
         st.code
         st.generatedCodePrefix
-        st.attrs.all()                       # get all attributs as a dict
-        st.validationPlugin                  # returns a plugin object
+        st.attrs.all()                       # get all attributes as a dict
+        st.get_validationPlugin()            # returns a plugin object
         
-        st.get_property_assignments()
-        st.assign_property(
-        	prop='diff_time',
-        	section = '',
-        	ordinal = 5,
-        	mandatory = True,
-        	initialValueForExistingEntities = 'initial value'
-        	showInEditView = True,
-        	showRawValueInForms = True
-        )
+        st.get_property_assignments()        # show the list of properties
+                                             # for that sample type
         
         o.get_material_types()
-        # etc. — see above
-        
         o.get_dataset_types()
-        # etc. — see above
-        
         o.get_experiment_types()
-        # etc. — see above
         
         o.get_property_types()
         pt = o.get_property_type('BARCODE_COMPLEXITY_CHECKER')
         pt.attrs.all()
         
         o.get_plugins()
         pl = o.get_plugin('Diff_time')
@@ -98,32 +112,27 @@
         
         o.get_vocabularies()
         o.get_vocabulary('BACTERIAL_ANTIBIOTIC_RESISTANCE')
         o.get_terms(vocabulary='STORAGE')
         o.get_tags()
         ```
         
-        ## create plugins and property types
-        ```
-        pl = o.new_plugin(
-            name       ='my_new_entry_validation_plugin',
-            pluginType ='ENTITY_VALIDATION',               # or 'DYNAMIC_PROPERTY' or 'MANAGED_PROPERTY',
-            entityKind = None,                             # or 'SAMPLE', 'MATERIAL', 'EXPERIMENT', 'DATA_SET'
-            script     = 'def calculate(): pass'           # a JYTHON script
-        )
-        pl.save()
+        ## create property types
+        
+        Samples (objects), experiments (collections) and dataSets contain general **attributes** as well as type-specific **properties**. Before they can be assigned to their respective type, they need to be created first.
         
+        ```
         pt = o.new_property_type(
             code        = 'MY_NEW_PROPERTY_TYPE', 
             label       = 'yet another property type', 
             description = 'my first property',
             dataType    = 'VARCHAR'
         )
         
-        pt2 = o.new_property_type(
+        pt_voc = o.new_property_type(
             code        = 'MY_CONTROLLED_VOCABULARY', 
             label       = 'label me', 
             description = 'give me a description',
             dataType    = 'CONTROLLEDVOCABULARY',
             vocabulary  = 'STORAGE'
         )
         ```
@@ -139,14 +148,110 @@
         * `HYPERLINK`
         * `XML`
         * `CONTROLLEDVOCABULARY`
         * `MATERIAL`
         
         When choosing `CONTROLLEDVOCABULARY`, you must specify a `vocabulary` attribute (see example). Likewise, when choosing `MATERIAL`, a `materialType` attribute must be provided.
         
+        ## create sample types
+        
+        
+        ```
+        sample_type = o.new_sample_type(
+            code = 'my_own_sample_type',      # mandatory
+            generatedCodePrefix	 = 'S',       # mandatory
+            description = '',
+            autoGeneratedCode = True,
+            subcodeUnique = False,
+            listable	= True,
+            showContainer = False,
+            showParents = True,
+            showParentMetadata = False,
+            validationPlugin = 'Has_Parents'  # see plugins below
+        )
+        sample_type.save()
+        ```
+        
+        ## assign properties to sample type
+        
+        A sample type needs to be saved before properties can be assigned to. This assignment procedure applies to all entity types (dataset type, experiment type, material type).
+        
+        ```
+        sample_type.assign_property(
+        	prop = 'diff_time',             # mandatory
+        	section = '',
+        	ordinal = 5,
+        	mandatory = True,
+        	initialValueForExistingEntities = 'initial value'
+        	showInEditView = True,
+        	showRawValueInForms = True
+        )
+        sample_type.revoke_property('diff_time')
+        sample_type.get_property_assignments()
+        ```
+        
+        ## create dataset types
+        
+        ```
+        dataset_type = o.new_dataset_type(
+            code = 'my_dataset_type',       # mandatory
+            description=None,
+            mainDataSetPattern=None,
+            mainDataSetPath=None,
+            disallowDeletion=False,
+            validationPlugin=None,
+        )
+        dataset_type.save()
+        dataset_type.assign_property('property_name')
+        dataset_type.revoke_property('property_name')
+        dataset_type.get_property_assignments()
+        ```
+        
+        ## create experiment types
+        
+        ```
+        experiment_type = o.new_experiment_type(
+            code, 
+            description=None,
+            validationPlugin=None,
+        )
+        experiment_type.save()
+        experiment_type.assign_property('property_name')
+        experiment_type.revoke_property('property_name')
+        experiment_type.get_property_assignments()
+        ```
+        
+        ## create material types
+        
+        ```
+        material_type = o.new_material_type(
+            code, 
+            description=None,
+            validationPlugin=None,
+        )
+        material_type.save()
+        material_type.assign_property('property_name')
+        material_type.revoke_property('property_name')
+        material_type.get_property_assignments()
+        
+        ```
+        
+        ## create plugins
+        
+        Plugins are Jython scripts that can accomplish more complex data-checks than ordinary types and vocabularies can achieve. They are assigned to entity types (dataset type, sample type etc). [Documentation and examples can be found here](https://wiki-bsse.ethz.ch/display/openBISDoc/Properties+Handled+By+Scripts)
+        
+        ```
+        pl = o.new_plugin(
+            name       ='my_new_entry_validation_plugin',
+            pluginType ='ENTITY_VALIDATION',               # or 'DYNAMIC_PROPERTY' or 'MANAGED_PROPERTY',
+            entityKind = None,                             # or 'SAMPLE', 'MATERIAL', 'EXPERIMENT', 'DATA_SET'
+            script     = 'def calculate(): pass'           # a JYTHON script
+        )
+        pl.save()
+        ```
         
         ## Users, Groups and RoleAssignments
         
         ```
         o.get_groups()
         group = o.new_group(code='group_name', description='...')
         group = o.get_group('group_name')
```

### Comparing `PyBIS-1.9.7/LICENSE` & `PyBIS-1.9.8/LICENSE`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/CHANGELOG.md` & `PyBIS-1.9.8/CHANGELOG.md`

 * *Files 7% similar despite different names*

```diff
@@ -1,7 +1,16 @@
+## Changes with pybis-1.9.8
+
+* new: create and update Dateset Types
+* new: create and update Experiment Types
+* new: create and update Material Types
+* many bugfixes
+* extended documentation about creating these entity types
+
+
 ## Changes with pybis-1.9.7
 
 * bugfix for creating propertyTypes of type controlled vocabulary and material
 
 
 ## Changes with pybis-1.9.6
```

### Comparing `PyBIS-1.9.7/PyBIS.egg-info/PKG-INFO` & `PyBIS-1.9.8/PyBIS.egg-info/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PyBIS
-Version: 1.9.7
+Version: 1.9.8
 Summary: openBIS connection and interaction, optimized for using with Jupyter
 Home-page: https://sissource.ethz.ch/sispub/openbis/tree/master/pybis
 Author: Swen Vermeul • ID SIS • ETH Zürich
 Author-email: swen@ethz.ch
 License: Apache Software License Version 2.0
 Description: # Welcome to pyBIS!
         pyBIS is a Python module for interacting with openBIS, designed to be used in Jupyter. It offers some sort of IDE for openBIS, supporting TAB completition and input checks, making the life of a researcher hopefully easier.
@@ -24,73 +24,87 @@
         
         If you haven't done yet, install Jupyter Notebook:
         
         ```
         pip install jupyter
         ```
         
-        # Usage
+        # General Usage
         
         ## Tab completition and other hints
         Used in a Jupyter Notebook environment, pybis helps you to enter the commands. After every dot `.` you might hit the `TAB` key in order to look at the available commands.
         
         If you are unsure what parameters to add to a , add a question mark right after the method and hit `SHIFT+ENTER`. Jupyter will then look up the signature of the method and show some helpful docstring.
         
         When working with properties of entities, they might use a **controlled vocabulary** or are of a specific **property type**. Add an underscore `_` character right after the property and hit `SHIFT+ENTER` to show the valid values. When a property only acceps a controlled vocabulary, you will be shown the valid terms in a nicely formatted table.
         
-        ## connect to from OpenBIS
+        ## connect to OpenBIS
+        
+        Interactivel, i.e. within a Jupyter notebook, you can use `getpass` to enter your password:
         
         ```
         from pybis import Openbis
         o = Openbis('https://example.com', verify_certificates=False)
         
         import getpass
         password = getpass.getpass()
         
         o.login('username', password, save_token=True)   # save the session token in ~/.pybis/example.com.token
         ```
         
+        In a script you would rather use two environment variables to provide username and password:
+        
+        ```
+        from pybis import Openbis
+        o = Openbis(os.environ['OPENBIS_HOST'], verify_certificates=False)
+        
+        o.login(os.environ['OPENBIS_USERNAME'], os.environ['OPENBIS_PASSWORD'])
+        ```
+        
+        
         Check whether the session token is still valid and log out:
         
         ```
         o.token
         o.is_session_active()
         o.logout()
         ```
         
-        ## browsing masterdata
+        # Masterdata
+        OpenBIS stores quite a lot of meta-data along with your dataSets. The collection of data that describes this meta-data (i.e. meta-meta-data) is called masterdata. It consists of:
+        
+        * sample types
+        * dataSet types
+        * material types
+        * experiment types
+        * property types
+        * vocabularies
+        * vocabulary terms
+        * plugins (jython scripts that allow complex data checks)
+        * tags
+        * semantic annotations
+        
+        ## browse masterdata
+        
         ```
         sample_types = o.get_sample_types()  # get a list of sample types 
         sample_types.df                      # DataFrame object
         st = o.get_sample_types()[3]         # get 4th element of that list
         st = o.get_sample_type('YEAST')
         st.code
         st.generatedCodePrefix
-        st.attrs.all()                       # get all attributs as a dict
-        st.validationPlugin                  # returns a plugin object
+        st.attrs.all()                       # get all attributes as a dict
+        st.get_validationPlugin()            # returns a plugin object
         
-        st.get_property_assignments()
-        st.assign_property(
-        	prop='diff_time',
-        	section = '',
-        	ordinal = 5,
-        	mandatory = True,
-        	initialValueForExistingEntities = 'initial value'
-        	showInEditView = True,
-        	showRawValueInForms = True
-        )
+        st.get_property_assignments()        # show the list of properties
+                                             # for that sample type
         
         o.get_material_types()
-        # etc. — see above
-        
         o.get_dataset_types()
-        # etc. — see above
-        
         o.get_experiment_types()
-        # etc. — see above
         
         o.get_property_types()
         pt = o.get_property_type('BARCODE_COMPLEXITY_CHECKER')
         pt.attrs.all()
         
         o.get_plugins()
         pl = o.get_plugin('Diff_time')
@@ -98,32 +112,27 @@
         
         o.get_vocabularies()
         o.get_vocabulary('BACTERIAL_ANTIBIOTIC_RESISTANCE')
         o.get_terms(vocabulary='STORAGE')
         o.get_tags()
         ```
         
-        ## create plugins and property types
-        ```
-        pl = o.new_plugin(
-            name       ='my_new_entry_validation_plugin',
-            pluginType ='ENTITY_VALIDATION',               # or 'DYNAMIC_PROPERTY' or 'MANAGED_PROPERTY',
-            entityKind = None,                             # or 'SAMPLE', 'MATERIAL', 'EXPERIMENT', 'DATA_SET'
-            script     = 'def calculate(): pass'           # a JYTHON script
-        )
-        pl.save()
+        ## create property types
+        
+        Samples (objects), experiments (collections) and dataSets contain general **attributes** as well as type-specific **properties**. Before they can be assigned to their respective type, they need to be created first.
         
+        ```
         pt = o.new_property_type(
             code        = 'MY_NEW_PROPERTY_TYPE', 
             label       = 'yet another property type', 
             description = 'my first property',
             dataType    = 'VARCHAR'
         )
         
-        pt2 = o.new_property_type(
+        pt_voc = o.new_property_type(
             code        = 'MY_CONTROLLED_VOCABULARY', 
             label       = 'label me', 
             description = 'give me a description',
             dataType    = 'CONTROLLEDVOCABULARY',
             vocabulary  = 'STORAGE'
         )
         ```
@@ -139,14 +148,110 @@
         * `HYPERLINK`
         * `XML`
         * `CONTROLLEDVOCABULARY`
         * `MATERIAL`
         
         When choosing `CONTROLLEDVOCABULARY`, you must specify a `vocabulary` attribute (see example). Likewise, when choosing `MATERIAL`, a `materialType` attribute must be provided.
         
+        ## create sample types
+        
+        
+        ```
+        sample_type = o.new_sample_type(
+            code = 'my_own_sample_type',      # mandatory
+            generatedCodePrefix	 = 'S',       # mandatory
+            description = '',
+            autoGeneratedCode = True,
+            subcodeUnique = False,
+            listable	= True,
+            showContainer = False,
+            showParents = True,
+            showParentMetadata = False,
+            validationPlugin = 'Has_Parents'  # see plugins below
+        )
+        sample_type.save()
+        ```
+        
+        ## assign properties to sample type
+        
+        A sample type needs to be saved before properties can be assigned to. This assignment procedure applies to all entity types (dataset type, experiment type, material type).
+        
+        ```
+        sample_type.assign_property(
+        	prop = 'diff_time',             # mandatory
+        	section = '',
+        	ordinal = 5,
+        	mandatory = True,
+        	initialValueForExistingEntities = 'initial value'
+        	showInEditView = True,
+        	showRawValueInForms = True
+        )
+        sample_type.revoke_property('diff_time')
+        sample_type.get_property_assignments()
+        ```
+        
+        ## create dataset types
+        
+        ```
+        dataset_type = o.new_dataset_type(
+            code = 'my_dataset_type',       # mandatory
+            description=None,
+            mainDataSetPattern=None,
+            mainDataSetPath=None,
+            disallowDeletion=False,
+            validationPlugin=None,
+        )
+        dataset_type.save()
+        dataset_type.assign_property('property_name')
+        dataset_type.revoke_property('property_name')
+        dataset_type.get_property_assignments()
+        ```
+        
+        ## create experiment types
+        
+        ```
+        experiment_type = o.new_experiment_type(
+            code, 
+            description=None,
+            validationPlugin=None,
+        )
+        experiment_type.save()
+        experiment_type.assign_property('property_name')
+        experiment_type.revoke_property('property_name')
+        experiment_type.get_property_assignments()
+        ```
+        
+        ## create material types
+        
+        ```
+        material_type = o.new_material_type(
+            code, 
+            description=None,
+            validationPlugin=None,
+        )
+        material_type.save()
+        material_type.assign_property('property_name')
+        material_type.revoke_property('property_name')
+        material_type.get_property_assignments()
+        
+        ```
+        
+        ## create plugins
+        
+        Plugins are Jython scripts that can accomplish more complex data-checks than ordinary types and vocabularies can achieve. They are assigned to entity types (dataset type, sample type etc). [Documentation and examples can be found here](https://wiki-bsse.ethz.ch/display/openBISDoc/Properties+Handled+By+Scripts)
+        
+        ```
+        pl = o.new_plugin(
+            name       ='my_new_entry_validation_plugin',
+            pluginType ='ENTITY_VALIDATION',               # or 'DYNAMIC_PROPERTY' or 'MANAGED_PROPERTY',
+            entityKind = None,                             # or 'SAMPLE', 'MATERIAL', 'EXPERIMENT', 'DATA_SET'
+            script     = 'def calculate(): pass'           # a JYTHON script
+        )
+        pl.save()
+        ```
         
         ## Users, Groups and RoleAssignments
         
         ```
         o.get_groups()
         group = o.new_group(code='group_name', description='...')
         group = o.get_group('group_name')
```

### Comparing `PyBIS-1.9.7/PyBIS.egg-info/SOURCES.txt` & `PyBIS-1.9.8/PyBIS.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/README.md` & `PyBIS-1.9.8/README.md`

 * *Files 10% similar despite different names*

```diff
@@ -16,73 +16,87 @@
 
 If you haven't done yet, install Jupyter Notebook:
 
 ```
 pip install jupyter
 ```
 
-# Usage
+# General Usage
 
 ## Tab completition and other hints
 Used in a Jupyter Notebook environment, pybis helps you to enter the commands. After every dot `.` you might hit the `TAB` key in order to look at the available commands.
 
 If you are unsure what parameters to add to a , add a question mark right after the method and hit `SHIFT+ENTER`. Jupyter will then look up the signature of the method and show some helpful docstring.
 
 When working with properties of entities, they might use a **controlled vocabulary** or are of a specific **property type**. Add an underscore `_` character right after the property and hit `SHIFT+ENTER` to show the valid values. When a property only acceps a controlled vocabulary, you will be shown the valid terms in a nicely formatted table.
 
-## connect to from OpenBIS
+## connect to OpenBIS
+
+Interactivel, i.e. within a Jupyter notebook, you can use `getpass` to enter your password:
 
 ```
 from pybis import Openbis
 o = Openbis('https://example.com', verify_certificates=False)
 
 import getpass
 password = getpass.getpass()
 
 o.login('username', password, save_token=True)   # save the session token in ~/.pybis/example.com.token
 ```
 
+In a script you would rather use two environment variables to provide username and password:
+
+```
+from pybis import Openbis
+o = Openbis(os.environ['OPENBIS_HOST'], verify_certificates=False)
+
+o.login(os.environ['OPENBIS_USERNAME'], os.environ['OPENBIS_PASSWORD'])
+```
+
+
 Check whether the session token is still valid and log out:
 
 ```
 o.token
 o.is_session_active()
 o.logout()
 ```
 
-## browsing masterdata
+# Masterdata
+OpenBIS stores quite a lot of meta-data along with your dataSets. The collection of data that describes this meta-data (i.e. meta-meta-data) is called masterdata. It consists of:
+
+* sample types
+* dataSet types
+* material types
+* experiment types
+* property types
+* vocabularies
+* vocabulary terms
+* plugins (jython scripts that allow complex data checks)
+* tags
+* semantic annotations
+
+## browse masterdata
+
 ```
 sample_types = o.get_sample_types()  # get a list of sample types 
 sample_types.df                      # DataFrame object
 st = o.get_sample_types()[3]         # get 4th element of that list
 st = o.get_sample_type('YEAST')
 st.code
 st.generatedCodePrefix
-st.attrs.all()                       # get all attributs as a dict
-st.validationPlugin                  # returns a plugin object
+st.attrs.all()                       # get all attributes as a dict
+st.get_validationPlugin()            # returns a plugin object
 
-st.get_property_assignments()
-st.assign_property(
-	prop='diff_time',
-	section = '',
-	ordinal = 5,
-	mandatory = True,
-	initialValueForExistingEntities = 'initial value'
-	showInEditView = True,
-	showRawValueInForms = True
-)
+st.get_property_assignments()        # show the list of properties
+                                     # for that sample type
 
 o.get_material_types()
-# etc. — see above
-
 o.get_dataset_types()
-# etc. — see above
-
 o.get_experiment_types()
-# etc. — see above
 
 o.get_property_types()
 pt = o.get_property_type('BARCODE_COMPLEXITY_CHECKER')
 pt.attrs.all()
 
 o.get_plugins()
 pl = o.get_plugin('Diff_time')
@@ -90,32 +104,27 @@
 
 o.get_vocabularies()
 o.get_vocabulary('BACTERIAL_ANTIBIOTIC_RESISTANCE')
 o.get_terms(vocabulary='STORAGE')
 o.get_tags()
 ```
 
-## create plugins and property types
-```
-pl = o.new_plugin(
-    name       ='my_new_entry_validation_plugin',
-    pluginType ='ENTITY_VALIDATION',               # or 'DYNAMIC_PROPERTY' or 'MANAGED_PROPERTY',
-    entityKind = None,                             # or 'SAMPLE', 'MATERIAL', 'EXPERIMENT', 'DATA_SET'
-    script     = 'def calculate(): pass'           # a JYTHON script
-)
-pl.save()
+## create property types
+
+Samples (objects), experiments (collections) and dataSets contain general **attributes** as well as type-specific **properties**. Before they can be assigned to their respective type, they need to be created first.
 
+```
 pt = o.new_property_type(
     code        = 'MY_NEW_PROPERTY_TYPE', 
     label       = 'yet another property type', 
     description = 'my first property',
     dataType    = 'VARCHAR'
 )
 
-pt2 = o.new_property_type(
+pt_voc = o.new_property_type(
     code        = 'MY_CONTROLLED_VOCABULARY', 
     label       = 'label me', 
     description = 'give me a description',
     dataType    = 'CONTROLLEDVOCABULARY',
     vocabulary  = 'STORAGE'
 )
 ```
@@ -131,14 +140,110 @@
 * `HYPERLINK`
 * `XML`
 * `CONTROLLEDVOCABULARY`
 * `MATERIAL`
 
 When choosing `CONTROLLEDVOCABULARY`, you must specify a `vocabulary` attribute (see example). Likewise, when choosing `MATERIAL`, a `materialType` attribute must be provided.
 
+## create sample types
+
+
+```
+sample_type = o.new_sample_type(
+    code = 'my_own_sample_type',      # mandatory
+    generatedCodePrefix	 = 'S',       # mandatory
+    description = '',
+    autoGeneratedCode = True,
+    subcodeUnique = False,
+    listable	= True,
+    showContainer = False,
+    showParents = True,
+    showParentMetadata = False,
+    validationPlugin = 'Has_Parents'  # see plugins below
+)
+sample_type.save()
+```
+
+## assign properties to sample type
+
+A sample type needs to be saved before properties can be assigned to. This assignment procedure applies to all entity types (dataset type, experiment type, material type).
+
+```
+sample_type.assign_property(
+	prop = 'diff_time',             # mandatory
+	section = '',
+	ordinal = 5,
+	mandatory = True,
+	initialValueForExistingEntities = 'initial value'
+	showInEditView = True,
+	showRawValueInForms = True
+)
+sample_type.revoke_property('diff_time')
+sample_type.get_property_assignments()
+```
+
+## create dataset types
+
+```
+dataset_type = o.new_dataset_type(
+    code = 'my_dataset_type',       # mandatory
+    description=None,
+    mainDataSetPattern=None,
+    mainDataSetPath=None,
+    disallowDeletion=False,
+    validationPlugin=None,
+)
+dataset_type.save()
+dataset_type.assign_property('property_name')
+dataset_type.revoke_property('property_name')
+dataset_type.get_property_assignments()
+```
+
+## create experiment types
+
+```
+experiment_type = o.new_experiment_type(
+    code, 
+    description=None,
+    validationPlugin=None,
+)
+experiment_type.save()
+experiment_type.assign_property('property_name')
+experiment_type.revoke_property('property_name')
+experiment_type.get_property_assignments()
+```
+
+## create material types
+
+```
+material_type = o.new_material_type(
+    code, 
+    description=None,
+    validationPlugin=None,
+)
+material_type.save()
+material_type.assign_property('property_name')
+material_type.revoke_property('property_name')
+material_type.get_property_assignments()
+
+```
+
+## create plugins
+
+Plugins are Jython scripts that can accomplish more complex data-checks than ordinary types and vocabularies can achieve. They are assigned to entity types (dataset type, sample type etc). [Documentation and examples can be found here](https://wiki-bsse.ethz.ch/display/openBISDoc/Properties+Handled+By+Scripts)
+
+```
+pl = o.new_plugin(
+    name       ='my_new_entry_validation_plugin',
+    pluginType ='ENTITY_VALIDATION',               # or 'DYNAMIC_PROPERTY' or 'MANAGED_PROPERTY',
+    entityKind = None,                             # or 'SAMPLE', 'MATERIAL', 'EXPERIMENT', 'DATA_SET'
+    script     = 'def calculate(): pass'           # a JYTHON script
+)
+pl.save()
+```
 
 ## Users, Groups and RoleAssignments
 
 ```
 o.get_groups()
 group = o.new_group(code='group_name', description='...')
 group = o.get_group('group_name')
```

### Comparing `PyBIS-1.9.7/setup.py` & `PyBIS-1.9.8/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 from setuptools import setup, find_packages
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setup(
     name='PyBIS',
-    version= '1.9.7',
+    version= '1.9.8',
     author='Swen Vermeul • ID SIS • ETH Zürich',
     author_email='swen@ethz.ch',
     description='openBIS connection and interaction, optimized for using with Jupyter',
     long_description=long_description,
     long_description_content_type="text/markdown",
     url='https://sissource.ethz.ch/sispub/openbis/tree/master/pybis',
     packages=find_packages(),
```

### Comparing `PyBIS-1.9.7/pybis/things.py` & `PyBIS-1.9.8/pybis/things.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/material.py` & `PyBIS-1.9.8/pybis/material.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/person.py` & `PyBIS-1.9.8/pybis/person.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/attribute.py` & `PyBIS-1.9.8/pybis/attribute.py`

 * *Files 1% similar despite different names*

```diff
@@ -57,17 +57,23 @@
         for attr in self._defs['attrs']:
             if attr in ["code", "permId", "identifier", "type"]:
                 self.__dict__['_' + attr] = data.get(attr, None)
                 # remove the @id attribute
                 if isinstance(self.__dict__['_' + attr], dict):
                     self.__dict__['_' + attr].pop('@id')
 
-            elif attr == 'vocabularyCode':
+            elif attr in ['vocabularyCode']:
                 self.__dict__['_'+attr] = data.get('permId', {}).get(attr, None)
 
+            elif attr in ['validationPlugin']:
+                d = data.get(attr, None)
+                if d is not None:
+                    d = d['permId']
+                self.__dict__['_' + attr] = d
+
             elif attr in ["space"]:
                 d = data.get(attr, None)
                 if d is not None:
                     d = d['permId']
                 self.__dict__['_' + attr] = d
 
             elif attr in ["sample", "experiment", "project", "container"]:
@@ -233,17 +239,18 @@
 		    })
 
                 up_obj['userIds'] = {
                     "actions": actions,
                     "@type": "as.dto.common.update.IdListUpdateValue" 
                 }
 
-            elif attr in 'description label official ordinal'.split():
+            elif attr in 'description label official ordinal autoGeneratedCode subcodeUnique listable showContainer showParents showParentMetadata disallowDeletion validationPlugin'.split():
                 # alway update common fields
-                up_obj[attr] = {
+                key = attr2ids.get(attr, attr)
+                up_obj[key] = {
                     "value": self.__dict__['_'+attr],
                     "isModified": True,
                     "@type": "as.dto.common.update.FieldUpdateValue"
                 }
 
             elif '_' + attr in self.__dict__:
                 # handle multivalue attributes (parents, children, tags etc.)
@@ -264,21 +271,16 @@
                     }
                 else:
                     # handle single attributes (space, experiment, project, container, etc.)
                     value = self.__dict__.get('_' + attr, {})
                     if value is None:
                         pass
                     elif isinstance(value, bool):
-                        # for boolean values no type is needed
+                        # for boolean values where no type is needed
                         up_obj[attr] = value
-                        #{
-                        #    "value": value,
-                        #    "isModified": True,
-                        #    "@type": "as.dto.common.update.FieldUpdateValue"
-                        #}
                     elif isinstance(value, dict) and len(value) == 0:
                         # value is {}: it means that we want this attribute to be
                         # deleted, not updated.
                         up_obj[attr2ids[attr]] = {
                             "@type": "as.dto.common.update.FieldUpdateValue",
                             "isModified": True,
                         }
@@ -321,14 +323,15 @@
             'permid'     : 'permId',
             'collection' : 'experiment',
             'object'     : 'sample'
         }
         if name in name_map:
             name = name_map[name]
 
+
         int_name = '_' + name
         if int_name in self.__dict__:
             if int_name == '_attachments':
                 attachments = []
                 for att in self._attachments:
                     attachments.append({
                         "fileName":    att.get('fileName'),
@@ -463,25 +466,40 @@
         elif name in ["tags"]:
             self.set_tags(value)
 
         elif name in ["users"]:
             self.set_users(value)
 
         elif name in ["vocabulary"]:
-            self.__dict__['_vocabulary'] = {
-                "@type": "as.dto.vocabulary.id.VocabularyPermId",
-                "permId": value.upper()
-            }
+            if value is None or value == '':
+                self.__dict__['_vocabulary'] = None
+            else:
+                self.__dict__['_vocabulary'] = {
+                    "@type": "as.dto.vocabulary.id.VocabularyPermId",
+                    "permId": value.upper()
+                }
+
+        elif name in ["validationPlugin"]:
+            if value is None or value == '':
+                self.__dict__['_validationPlugin'] = None
+            else:
+                self.__dict__['_validationPlugin'] = {
+                    "@type": "as.dto.plugin.id.PluginPermId",
+                    "permId": value
+                }
 
         elif name in ["materialType"]:
-            self.__dict__['_materialType'] = {
-                "@type": "as.dto.entitytype.id.EntityTypePermId",
-                "permId": value.upper(),
-                "entityKind": "MATERIAL"
-            }
+            if value is None or value == '':
+                self.__dict__['_materialType'] = None
+            else:
+                self.__dict__['_materialType'] = {
+                    "@type": "as.dto.entitytype.id.EntityTypePermId",
+                    "permId": value.upper(),
+                    "entityKind": "MATERIAL"
+                }
 
         elif name in ["attachments"]:
             if isinstance(value, list):
                 for item in value:
                     if isinstance(item, dict):
                         self.add_attachment(**item)
                     else:
```

### Comparing `PyBIS-1.9.7/pybis/definitions.py` & `PyBIS-1.9.8/pybis/definitions.py`

 * *Files 0% similar despite different names*

```diff
@@ -78,16 +78,16 @@
             },
             "delete": {
                 "@type": "as.dto.sample.delete.SampleTypeDeletionOptions"
             },
             "identifier": "typeId",
         },
         "materialType": {
-            "attrs_new":    "code description validationPluginId".split(),
-            "attrs_up":          "description validationPluginId".split(),
+            "attrs_new":    "code description validationPlugin".split(),
+            "attrs_up":          "description validationPlugin".split(),
             "attrs": "permId code description validationPlugin".split(),
             "search": {
                 "@type": "as.dto.material.search.MaterialTypeSearchCriteria"
             },
             "fetch": {
                 "@type": "as.dto.material.fetchoptions.MaterialTypeFetchOptions"
             },
@@ -99,16 +99,16 @@
             },
             "delete": {
                 "@type": "as.dto.material.delete.MaterialTypeDeletionOptions"
             },
             "identifier": "typeId",
         },
         "dataSetType": {
-            "attrs_new":    "code description mainDataSetPattern mainDataSetPath disallowDeletion validationPluginId".split(),
-            "attrs_up":          "description mainDataSetPattern mainDataSetPath disallowDeletion validationPluginId".split(),
+            "attrs_new":    "code description mainDataSetPattern mainDataSetPath disallowDeletion validationPlugin".split(),
+            "attrs_up":          "description mainDataSetPattern mainDataSetPath disallowDeletion validationPlugin".split(),
             "attrs": "permId code description mainDataSetPattern mainDataSetPath disallowDeletion modificationDate validationPlugin".split(),
             "search": {
                 "@type": "as.dto.dataset.search.DataSetTypeSearchCriteria"
             },
             "fetch": {
                 "@type": "as.dto.dataset.fetchoptions.DataSetTypeFetchOptions"
             },
@@ -120,28 +120,28 @@
             },
             "delete": {
                 "@type": "as.dto.dataset.delete.DataSetTypeDeletionOptions"
             },
             "identifier": "typeId",
         },
         "experimentType": {
-            "attrs_new":        "code description modificationDate validationPluginId".split(),
-            "attrs_up":              "description modificationDate validationPluginId".split(),
+            "attrs_new": "code description validationPlugin".split(),
+            "attrs_up":  "description modificationDate validationPlugin".split(),
             "attrs":     "permId code description modificationDate validationPlugin".split(),
             "search": {
                 "@type": "as.dto.experiment.search.ExperimentTypeSearchCriteria"
             },
             "fetch": {
                 "@type": "as.dto.experiment.fetchoptions.ExperimentTypeFetchOptions"
             },
             "create": {
                 "@type": "as.dto.experiment.create.ExperimentTypeCreation"
             },
             "update": {
-                "@type": "as.dto.experiment.create.ExperimentTypeUpdate"
+                "@type": "as.dto.experiment.update.ExperimentTypeUpdate"
             },
             "delete": {
                 "@type": "as.dto.experiment.delete.ExperimentTypeDeletionOptions"
             },
             "identifier": "typeId",
         },
         "propertyType": {
```

### Comparing `PyBIS-1.9.7/pybis/property.py` & `PyBIS-1.9.8/pybis/property.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/semantic_annotation.py` & `PyBIS-1.9.8/pybis/semantic_annotation.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/role_assignment.py` & `PyBIS-1.9.8/pybis/role_assignment.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/entity_type.py` & `PyBIS-1.9.8/pybis/entity_type.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 from tabulate import tabulate
 from texttable import Texttable
 from pandas import DataFrame
 from .openbis_object import OpenBisObject
 from .things import Things
 from .utils import check_datatype, split_identifier, format_timestamp, is_identifier, is_permid, nvl, extract_permid, extract_code, extract_name, VERBOSE
-from .definitions import get_method_for_entity, get_type_for_entity
+from .definitions import get_method_for_entity, get_type_for_entity, get_definition_for_entity
 
 class EntityType:
     """ EntityTypes define a variety of an entity, eg. sample, dataSet, experiment
     This is the parent class of the SampleType, DataSetType, ExperimentType and
     MaterialType classes.
     """ 
 
@@ -33,21 +33,29 @@
         return [
             'code', 'description', 'autoGeneratedCode', 'subcodeUnique',
             'generatedCodePrefix', 'listable', 'showContainer', 'showParents',
             'showParentMetadata', 'validationPlugin',
         ]
 
     def __dir__(self):
-        return self._attrs() + [
+        defs = get_definition_for_entity(self.entity)
+        attrs = [
             'get_property_assignments()',
             'assign_property()',
             'revoke_property()',
             'move_property_to_top()',
             'move_property_after()',
+            'get_validationPlugin()',
+            'save()',
+            'delete()',
         ]
+        if self.is_new:
+            return attrs + defs['attrs_new']
+        else:
+            return attrs + list(set(defs['attrs'] + defs['attrs_up']))
 
     def __getattr__(self, name):
         if name in self._attrs():
             if name in self.data:
                 return self.data[name]
             else:
                 return ''
@@ -173,15 +181,15 @@
         raise ValueError("not implemented yet")
 
     def move_property_after(self, property, after_property):
         raise ValueError("not implemented yet")
 
 
     @property
-    def validationPlugin(self):
+    def get_validationPlugin(self):
         """Returns a validation plugin object when called.
         Returns None when no validation plugin is defined.
         """
         try:
             return self.openbis.get_plugin(self._validationPlugin['name'])
         except Exception:
             pass
```

### Comparing `PyBIS-1.9.7/pybis/dataset.py` & `PyBIS-1.9.8/pybis/dataset.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/experiment.py` & `PyBIS-1.9.8/pybis/experiment.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/pybis.py` & `PyBIS-1.9.8/pybis/pybis.py`

 * *Files 2% similar despite different names*

```diff
@@ -24,15 +24,15 @@
 import zlib
 from collections import namedtuple
 from texttable import Texttable
 from tabulate import tabulate
 
 from . import data_set as pbds
 from .utils import parse_jackson, check_datatype, split_identifier, format_timestamp, is_identifier, is_permid, nvl, VERBOSE
-from .utils import extract_attr, extract_permid, extract_code,extract_deletion,extract_identifier,extract_nested_identifier,extract_nested_permid,extract_property_assignments,extract_role_assignments,extract_person, extract_person_details,extract_id,extract_userId
+from .utils import extract_attr, extract_permid, extract_code,extract_deletion,extract_identifier,extract_nested_identifier,extract_nested_permid, extract_nested_permids, extract_property_assignments,extract_role_assignments,extract_person, extract_person_details,extract_id,extract_userId
 from .entity_type import EntityType, SampleType, DataSetType, MaterialType, ExperimentType
 from .vocabulary import Vocabulary, VocabularyTerm
 from .openbis_object import OpenBisObject 
 from .definitions import openbis_definitions, get_definition_for_entity, fetch_option, get_fetchoption_for_entity, get_type_for_entity, get_method_for_entity
 
 # import the various openBIS entities
 from .things import Things
@@ -678,82 +678,89 @@
             pass
         else:
             print("Session is no longer valid. Please log in again.")
 
 
     def __dir__(self):
         return [
-            'url', 'port', 'hostname',
-            'login(username, password, save_token=True)', 'logout()', 'is_session_active()', 'token', 'is_token_valid("")',
+            'url', 'port', 'hostname', 'token',
+            'login()', 
+            'logout()', 
+            'is_session_active()', 
+            'is_token_valid()',
             "get_server_information()",
-            "get_dataset('permId')",
+            "get_dataset()",
             "get_datasets()",
-            "get_dataset_type('type')",
+            "get_dataset_type()",
             "get_dataset_types()",
             "get_datastores()",
-            "gen_code(entity, prefix)",
+            "gen_code()",
             "get_deletions()",
-            "get_experiment('permId', withAttachments=False)",
+            "get_experiment()",
             "get_experiments()",
-            "get_experiment_type('type')",
+            "get_experiment_type()",
             "get_experiment_types()",
-            "get_collection('permId', withAttachments=False)",
+            "get_collection()",
             "get_collections()",
-            "get_collection_type('type')",
+            "get_collection_type()",
             "get_collection_types()",
-            "get_external_data_management_system(permId)",
-            "get_material_type('type')",
+            "get_external_data_management_system()",
+            "get_material_type()",
             "get_material_types()",
-            "get_project('project')",
-            "get_projects(space=None, code=None)",
-            "get_sample('id')",
-            "get_object('id')", # "get_sample('id')" alias
+            "get_project()",
+            "get_projects()",
+            "get_sample()",
+            "get_object()",
             "get_samples()",
-            "get_objects()", # "get_samples()" alias
-            "get_sample_type('type')",
-            "get_object_type('type')", # "get_sample_type(type))" alias
+            "get_objects()",
+            "get_sample_type()",
+            "get_object_type()",
             "get_sample_types()",
-            "get_object_types()", # "get_sample_types()" alias
+            "get_object_types()",
             "get_property_types()",
             "get_property_type()",
             "new_property_type()",
             "get_semantic_annotations()",
-            "get_semantic_annotation(permId, only_data = False)",
-            "get_space(code)",
+            "get_semantic_annotation()",
+            "get_space()",
             "get_spaces()",
             "get_tags()",
-            "get_tag(tagId)",
-            "new_tag(code, description)",
+            "get_tag()",
+            "new_tag()",
             "get_terms()",
             "get_term()",
             "get_vocabularies()",
             "get_vocabulary()",
-            "new_person(userId, space)",
+            "new_person()",
             "get_persons()",
-            "get_person(userId)",
+            "get_person()",
             "get_groups()",
-            "get_group(code)",
+            "get_group()",
             "get_role_assignments()",
-            "get_role_assignment(techId)",
+            "get_role_assignment()",
             "get_plugins()",
-            "get_plugin(code)",
-            "new_plugin(code)",
-            "new_group(code, description, userIds)",
-            'new_space(name, description)',
-            'new_project(space, code, description, attachments)',
-            'new_experiment(type, code, project, props={})',
-            'new_collection(type, code, project, props={})',
-            'new_sample(type, space, project, experiment, parents)',
-            'new_object(type, space, project, experiment, parents)', # 'new_sample(type, space, project, experiment)' alias
+            "get_plugin()",
+            "new_plugin()",
+            "new_group()",
+            'new_space()',
+            'new_project()',
+            'new_experiment()',
+            'new_collection()',
+            'new_sample()',
+            'new_object()',
             'new_sample_type()',
             'new_object_type()',
-            'new_dataset(type, parent, experiment, sample, files=[], folder, props={})',
-            'new_semantic_annotation(entityType, propertyType)',
-            'update_sample(sampleId, space, project, experiment, parents, children, components, properties, tagIds, attachments)',
-            'update_object(sampleId, space, project, experiment, parents, children, components, properties, tagIds, attachments)', # 'update_sample(sampleId, space, project, experiment, parents, children, components, properties, tagIds, attachments)' alias
+            'new_dataset()',
+            'new_dataset_type()',
+            'new_experiment_type()',
+            'new_collection_type()',
+            'new_material_type()',
+            'new_semantic_annotation()',
+            'update_sample()',
+            'update_object()', 
         ]
 
     def _repr_html_(self):
         html = """
             <table border="1" class="dataframe">
             <thead>
                 <tr style="text-align: right;">
@@ -2616,27 +2623,50 @@
         entityKind  -- MATERIAL, EXPERIMENT, SAMPLE, DATA_SET
         script      -- string of the script itself
         available   --
         """
         return Plugin(self, name=name, pluginType=pluginType, **kwargs) 
         
 
-    def new_property_type(self, code, label, description, dataType, **kwargs):
-        return PropertyType(openbis_obj=self, code=code, label=label, description=description, dataType=dataType, **kwargs)
+    def new_property_type(self, 
+        code,
+        label,
+        description,
+        dataType,
+        managedInternally = False,
+        internalNameSpace= False,
+        vocabulary = None,
+        materialType = None,
+        schema = None,
+        transformation = None,
+    ):
+        return PropertyType(
+            openbis_obj=self,
+            code=code,
+            label=label,
+            description=description,
+            dataType=dataType,
+            managedInternally = managedInternally,
+            internalNameSpace= internalNameSpace,
+            vocabulary = vocabulary,
+            materialType = materialType,
+            schema = schema,
+            transformation = transformation,
+        )
 
     def get_property_type(self, code, only_data=False, start_with=None, count=None):
         identifiers = []
         only_one = False
         if not isinstance(code, list):
             code = [code]
             only_one = True
 
         for c in code:
             identifiers.append({
-                "permId": c,
+                "permId": c.upper(),
                 "@type": "as.dto.property.id.PropertyTypePermId"
             })
 
         fetchopts = fetch_option['propertyType']
         options = ['vocabulary', 'materialType', 'semanticAnnotations', 'registrator']
         for option in options:
             fetchopts[option] = fetch_option[option]
@@ -2704,14 +2734,16 @@
         attrs = openbis_definitions('propertyType')['attrs']
         if len(objects) == 0:
             df = DataFrame(columns=attrs)
         else:
             df = DataFrame(objects)
             df['registrationDate'] = df['registrationDate'].map(format_timestamp)
             df['registrator'] = df['registrator'].map(extract_person)
+            df['vocabulary'] = df['vocabulary'].map(extract_code)
+            df['semanticAnnotations'] = df['semanticAnnotations'].map(extract_nested_permids)
         
         return Things(
             openbis_obj = self,
             entity = 'propertyType',
             single_item_method = self.get_property_type,
             df = df[attrs],
             start_with = start_with,
@@ -2831,14 +2863,16 @@
             entity_types = DataFrame(columns=attrs)
         else:
             objects = resp['objects']
             parse_jackson(objects)
             entity_types = DataFrame(objects)
             entity_types['permId'] = entity_types['permId'].map(extract_permid)
             entity_types['modificationDate'] = entity_types['modificationDate'].map(format_timestamp)
+            entity_types['validationPlugin'] = entity_types['validationPlugin'].map(extract_nested_permid
+            )
 
         single_item_method = getattr(self, cls._single_item_method_name)
         return Things(
             openbis_obj = self,
             entity = entity,
             df = entity_types[attrs],
             start_with = start_with,
@@ -3354,29 +3388,87 @@
             kwargs['experiment'] = kwargs['collection']
             kwargs.pop('collection', None)
         sample_type = self.get_sample_type(type)
         return Sample(self, type=sample_type, project=project, data=None, props=props, **kwargs)
 
     new_object = new_sample # Alias
 
-    def new_sample_type(self, 
-            code,
-            **kwargs
-        ):
-        return SampleType(self, code=code, **kwargs)
+    def new_sample_type(self,
+        code, 
+        generatedCodePrefix,
+        subcodeUnique=False,
+        autoGeneratedCode=False,
+        listable=True,
+        showContainer=False,
+        showParents=True,
+        showParentMetadata=False,
+        validationPlugin=None
+    ):
+        """Creates a new sample type.
+        """
 
+        return SampleType(self, 
+            code=code, 
+            generatedCodePrefix = generatedCodePrefix,
+            autoGeneratedCode = autoGeneratedCode,
+            listable = listable,
+            showContainer = showContainer,
+            showParents = showParents,
+            showParentMetadata = showParentMetadata,
+            validationPlugin = validationPlugin,
+        )
     new_object_type = new_sample_type
 
     def new_dataset_type(self, 
-            code,
-            **kwargs
-        ):
-        return DataSetType(self, code=code, **kwargs)
+        code,
+        description=None,
+        mainDataSetPattern=None,
+        mainDataSetPath=None,
+        disallowDeletion=False,
+        validationPlugin=None,
+    ):
+        """Creates a new dataSet type.
+        """
 
-    new_object_type = new_sample_type
+        return DataSetType(self,
+            code=code, 
+            description=description, 
+            mainDataSetPattern=mainDataSetPattern,
+            mainDataSetPath=mainDataSetPath,
+            disallowDeletion=disallowDeletion,
+            validationPlugin=validationPlugin,
+        )
+
+    def new_experiment_type(self, 
+        code, 
+        description=None,
+        validationPlugin=None,
+    ):
+        """Creates a new experiment type (collection type)
+        """
+        return ExperimentType(self,
+            code=code, 
+            description=description, 
+            validationPlugin=validationPlugin,
+        )
+    new_collection_type = new_experiment_type
+
+
+    def new_material_type(self,
+        code, 
+        description=None,
+        validationPlugin=None,
+    ):
+        """Creates a new material type.
+        """
+        return MaterialType(self,
+            code=code,
+            description=description,
+            validationPlugin=validationPlugin,
+        )
 
     def new_dataset(self, type=None, kind='PHYSICAL_DATA', files=None, props=None, folder=None, **kwargs):
         """ Creates a new dataset of a given sample type.
         """
 
         type_obj = self.get_dataset_type(type.upper())
         if 'object' in kwargs:
```

### Comparing `PyBIS-1.9.7/pybis/attachment.py` & `PyBIS-1.9.8/pybis/attachment.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/utils.py` & `PyBIS-1.9.8/pybis/utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -14,15 +14,16 @@
        Objects that are found the first time are added an attribute «@id».
        Any further findings only carry this reference id.
        This function is used to dereference the output.
     """
     interesting=['tags', 'registrator', 'modifier', 'owner', 'type', 'parents', 
         'children', 'containers', 'container', 'properties', 'experiment', 'sample',
         'project', 'space', 'propertyType', 'entityType', 'propertyType', 'propertyAssignment',
-        'externalDms', 'roleAssignments', 'user', 'users', 'authorizationGroup', 'vocabulary'
+        'externalDms', 'roleAssignments', 'user', 'users', 'authorizationGroup', 'vocabulary',
+        'validationPlugin'
     ]
     found = {} 
     def build_cache(graph):
         if isinstance(graph, list):
             for item in graph:
                 build_cache(item)
         elif isinstance(graph, dict) and len(graph) > 0:
@@ -179,14 +180,20 @@
     return ident['identifier']['identifier']
 
 
 def extract_nested_permid(permid):
     if not isinstance(permid, dict):
         return '' if permid is None else str(permid)
     return '' if permid['permId']['permId'] is None else permid['permId']['permId'] 
+    
+def extract_nested_permids(items):
+    if not isinstance(items, list):
+        return []
+
+    return list(item['permId']['permId'] for item in items)
 
 
 def extract_property_assignments(pas):
     pa_strings = []
     for pa in pas:
         if not isinstance(pa['propertyType'], dict):
             pa_strings.append(pa['propertyType'])
```

### Comparing `PyBIS-1.9.7/pybis/openbis_object.py` & `PyBIS-1.9.8/pybis/openbis_object.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/data_set.py` & `PyBIS-1.9.8/pybis/data_set.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/sample.py` & `PyBIS-1.9.8/pybis/sample.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/group.py` & `PyBIS-1.9.8/pybis/group.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/space.py` & `PyBIS-1.9.8/pybis/space.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/vocabulary.py` & `PyBIS-1.9.8/pybis/vocabulary.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/project.py` & `PyBIS-1.9.8/pybis/project.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/pybis/tag.py` & `PyBIS-1.9.8/pybis/tag.py`

 * *Files identical despite different names*

### Comparing `PyBIS-1.9.7/README.rst` & `PyBIS-1.9.8/README.rst`

 * *Files identical despite different names*

