# Comparing `tmp/up42-py-0.9.2.tar.gz` & `tmp/up42-py-0.9.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/up42-py-0.9.2.tar", last modified: Sat Jul  4 13:35:43 2020, max compression
+gzip compressed data, was "dist/up42-py-0.9.3.tar", last modified: Wed Jul 15 08:44:17 2020, max compression
```

## Comparing `up42-py-0.9.2.tar` & `up42-py-0.9.3.tar`

### file list

```diff
@@ -1,39 +1,39 @@
-drwxr-xr-x   0 christoph.rieke   (501) staff       (20)        0 2020-07-04 13:35:43.798055 up42-py-0.9.2/
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     5178 2020-07-04 13:35:43.797701 up42-py-0.9.2/PKG-INFO
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     3909 2020-06-29 19:07:02.000000 up42-py-0.9.2/README.md
--rw-r--r--   0 christoph.rieke   (501) staff       (20)       38 2020-07-04 13:35:43.798182 up42-py-0.9.2/setup.cfg
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     1156 2020-05-05 12:09:18.000000 up42-py-0.9.2/setup.py
-drwxr-xr-x   0 christoph.rieke   (501) staff       (20)        0 2020-07-04 13:35:43.766402 up42-py-0.9.2/tests/
--rw-r--r--   0 christoph.rieke   (501) staff       (20)        0 2020-04-16 13:11:05.000000 up42-py-0.9.2/tests/__init__.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)      799 2020-07-04 12:26:42.000000 up42-py-0.9.2/tests/context.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)      962 2020-04-27 14:02:14.000000 up42-py-0.9.2/tests/e2e.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     4113 2020-05-07 09:50:38.000000 up42-py-0.9.2/tests/fixtures.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     3858 2020-04-27 13:22:11.000000 up42-py-0.9.2/tests/test_auth.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     4124 2020-06-29 19:07:02.000000 up42-py-0.9.2/tests/test_catalog.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     9930 2020-04-27 14:02:14.000000 up42-py-0.9.2/tests/test_cli.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     1446 2020-04-16 13:11:05.000000 up42-py-0.9.2/tests/test_initialization.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     9526 2020-07-04 12:26:42.000000 up42-py-0.9.2/tests/test_job.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     4312 2020-05-07 08:37:27.000000 up42-py-0.9.2/tests/test_jobtask.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     5377 2020-05-06 16:00:14.000000 up42-py-0.9.2/tests/test_project.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     6367 2020-04-27 13:22:11.000000 up42-py-0.9.2/tests/test_tools.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     8785 2020-07-04 12:26:42.000000 up42-py-0.9.2/tests/test_utils.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)    17082 2020-05-07 09:50:38.000000 up42-py-0.9.2/tests/test_workflow.py
-drwxr-xr-x   0 christoph.rieke   (501) staff       (20)        0 2020-07-04 13:35:43.774482 up42-py-0.9.2/up42/
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     4435 2020-05-05 12:09:23.000000 up42-py-0.9.2/up42/__init__.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     9360 2020-04-27 13:22:11.000000 up42-py-0.9.2/up42/auth.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)    10190 2020-06-29 19:07:02.000000 up42-py-0.9.2/up42/catalog.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)    20181 2020-05-05 10:54:11.000000 up42-py-0.9.2/up42/cli.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)    15288 2020-07-04 12:26:42.000000 up42-py-0.9.2/up42/job.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     5746 2020-04-27 22:02:01.000000 up42-py-0.9.2/up42/jobtask.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     6662 2020-05-06 16:00:14.000000 up42-py-0.9.2/up42/project.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)    14424 2020-06-25 08:39:23.000000 up42-py-0.9.2/up42/tools.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)    15151 2020-07-04 12:26:42.000000 up42-py-0.9.2/up42/utils.py
--rw-r--r--   0 christoph.rieke   (501) staff       (20)    20283 2020-05-07 09:50:38.000000 up42-py-0.9.2/up42/workflow.py
-drwxr-xr-x   0 christoph.rieke   (501) staff       (20)        0 2020-07-04 13:35:43.796960 up42-py-0.9.2/up42_py.egg-info/
--rw-r--r--   0 christoph.rieke   (501) staff       (20)     5178 2020-07-04 13:35:43.000000 up42-py-0.9.2/up42_py.egg-info/PKG-INFO
--rw-r--r--   0 christoph.rieke   (501) staff       (20)      662 2020-07-04 13:35:43.000000 up42-py-0.9.2/up42_py.egg-info/SOURCES.txt
--rw-r--r--   0 christoph.rieke   (501) staff       (20)        1 2020-07-04 13:35:43.000000 up42-py-0.9.2/up42_py.egg-info/dependency_links.txt
--rw-r--r--   0 christoph.rieke   (501) staff       (20)       58 2020-07-04 13:35:43.000000 up42-py-0.9.2/up42_py.egg-info/entry_points.txt
--rw-r--r--   0 christoph.rieke   (501) staff       (20)        1 2020-03-24 12:32:50.000000 up42-py-0.9.2/up42_py.egg-info/not-zip-safe
--rw-r--r--   0 christoph.rieke   (501) staff       (20)       98 2020-07-04 13:35:43.000000 up42-py-0.9.2/up42_py.egg-info/requires.txt
--rw-r--r--   0 christoph.rieke   (501) staff       (20)        5 2020-07-04 13:35:43.000000 up42-py-0.9.2/up42_py.egg-info/top_level.txt
+drwxr-xr-x   0 christoph.rieke   (501) staff       (20)        0 2020-07-15 08:44:17.985724 up42-py-0.9.3/
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     4941 2020-07-15 08:44:17.985319 up42-py-0.9.3/PKG-INFO
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     3712 2020-07-06 16:29:30.000000 up42-py-0.9.3/README.md
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)       38 2020-07-15 08:44:17.985871 up42-py-0.9.3/setup.cfg
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     1156 2020-05-05 12:09:18.000000 up42-py-0.9.3/setup.py
+drwxr-xr-x   0 christoph.rieke   (501) staff       (20)        0 2020-07-15 08:44:17.922757 up42-py-0.9.3/tests/
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)        0 2020-04-16 13:11:05.000000 up42-py-0.9.3/tests/__init__.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)      799 2020-07-04 12:26:42.000000 up42-py-0.9.3/tests/context.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)      962 2020-04-27 14:02:14.000000 up42-py-0.9.3/tests/e2e.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     4113 2020-05-07 09:50:38.000000 up42-py-0.9.3/tests/fixtures.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     3858 2020-04-27 13:22:11.000000 up42-py-0.9.3/tests/test_auth.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     4124 2020-06-29 19:07:02.000000 up42-py-0.9.3/tests/test_catalog.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     9930 2020-04-27 14:02:14.000000 up42-py-0.9.3/tests/test_cli.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     1446 2020-04-16 13:11:05.000000 up42-py-0.9.3/tests/test_initialization.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)    10068 2020-07-15 08:37:10.000000 up42-py-0.9.3/tests/test_job.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     4312 2020-05-07 08:37:27.000000 up42-py-0.9.3/tests/test_jobtask.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     5377 2020-05-06 16:00:14.000000 up42-py-0.9.3/tests/test_project.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     6367 2020-04-27 13:22:11.000000 up42-py-0.9.3/tests/test_tools.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     8785 2020-07-04 12:26:42.000000 up42-py-0.9.3/tests/test_utils.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)    17082 2020-05-07 09:50:38.000000 up42-py-0.9.3/tests/test_workflow.py
+drwxr-xr-x   0 christoph.rieke   (501) staff       (20)        0 2020-07-15 08:44:17.949414 up42-py-0.9.3/up42/
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     4435 2020-05-05 12:09:23.000000 up42-py-0.9.3/up42/__init__.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     9360 2020-04-27 13:22:11.000000 up42-py-0.9.3/up42/auth.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)    10113 2020-07-06 16:29:30.000000 up42-py-0.9.3/up42/catalog.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)    20181 2020-05-05 10:54:11.000000 up42-py-0.9.3/up42/cli.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)    15379 2020-07-15 08:37:10.000000 up42-py-0.9.3/up42/job.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     5662 2020-07-06 16:29:30.000000 up42-py-0.9.3/up42/jobtask.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     6525 2020-07-06 16:29:30.000000 up42-py-0.9.3/up42/project.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)    14311 2020-07-06 16:29:30.000000 up42-py-0.9.3/up42/tools.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)    15178 2020-07-15 08:37:10.000000 up42-py-0.9.3/up42/utils.py
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)    20079 2020-07-06 16:29:30.000000 up42-py-0.9.3/up42/workflow.py
+drwxr-xr-x   0 christoph.rieke   (501) staff       (20)        0 2020-07-15 08:44:17.984468 up42-py-0.9.3/up42_py.egg-info/
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)     4941 2020-07-15 08:44:17.000000 up42-py-0.9.3/up42_py.egg-info/PKG-INFO
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)      662 2020-07-15 08:44:17.000000 up42-py-0.9.3/up42_py.egg-info/SOURCES.txt
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)        1 2020-07-15 08:44:17.000000 up42-py-0.9.3/up42_py.egg-info/dependency_links.txt
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)       58 2020-07-15 08:44:17.000000 up42-py-0.9.3/up42_py.egg-info/entry_points.txt
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)        1 2020-03-24 12:32:50.000000 up42-py-0.9.3/up42_py.egg-info/not-zip-safe
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)       98 2020-07-15 08:44:17.000000 up42-py-0.9.3/up42_py.egg-info/requires.txt
+-rw-r--r--   0 christoph.rieke   (501) staff       (20)        5 2020-07-15 08:44:17.000000 up42-py-0.9.3/up42_py.egg-info/top_level.txt
```

### Comparing `up42-py-0.9.2/PKG-INFO` & `up42-py-0.9.3/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: up42-py
-Version: 0.9.2
+Version: 0.9.3
 Summary: Python SDK for UP42
 Home-page: https://github.com/up42/up42-py
 Author: UP42
 Author-email: support@up42.com
 License: MIT
 Description: 
         <p align="center">
@@ -21,93 +21,88 @@
         
         <p align="center">
             <b>
               <a href="https://up42.github.io/up42-py/">Documentation</a> &nbsp; • &nbsp;
               <a href="http://www.up42.com">UP42.com</a> &nbsp; • &nbsp;
               <a href="#support">Support</a>
             </b>
+        </p>
         
         ## Highlights
         - Python package for easy access to **[UP42's](http://www.up42.com)** **geospatial datasets** & **processing workflows**
+        - Use UP42 functionality together with your preffered Python libraries!
         - For geospatial **analysis** & **product builders**!
         - Interactive maps & **visualization**, ideal with Jupyter notebooks  
         - Command Line Interface (**CLI**)
-        - Developer tools for UP42 custom blocks (coming soon)
         
         
         <img align="right" href="https://up42.github.io/up42-py/" src="docs/assets/docs.png" alt="" height="200"/>
         
         ## Installation & Documentation
         
         See the **[documentation](https://up42.github.io/up42-py/)** for **getting started guides**, **examples** and the **code reference**.
         
         The package requires Python > 3.6.
         
         ```bash
         pip install up42-py
         ```
         
-        ## Overview
+        <br>
         
-        - The UP42 Python SDK uses six object classes, representing the **hierarchical structure of UP42**:
-            - **Project > Workflow > Job > JobTask**
-            - **Catalog**
-            - **Tools**
-        - Each object can **spawn elements of one level below**, e.g.
-            - `project = up42.initialize_project()`
-            - `workflow = Project().create_workflow()`
-            - `job = workflow.run_job()`
+        ## 30-second Example
         
+        The UP42 Python package uses six classes, representing the **hierarchical structure of UP42**: **Project > Workflow > Job > JobTask** and **Catalog** & **Tools**
         
-        ## 30-second Example
+        ![](docs/assets/vizualisations.jpg)
         
-        ![eo-learn-workflow0illustration](docs/assets/vizualisations.jpg)
         
-        After [authentication](https://up42.github.io/up42-py/authentication/) with the UP42 project, 
-        a new workflow is created and filled with tasks ([Sentinel-2 data](https://marketplace.up42.com/block/3a381e6b-acb7-4cec-ae65-50798ce80e64), 
-        [Image Sharpening](https://marketplace.up42.com/block/e374ea64-dc3b-4500-bb4b-974260fb203e)). 
-        The area of interest and workflow parameters are defined. After running the job, the results are downloaded and visualized.
+        A **new workflow** consisting of [**Sentinel-2 data**](https://marketplace.up42.com/block/3a381e6b-acb7-4cec-ae65-50798ce80e64)
+        and [**Image Sharpening**](https://marketplace.up42.com/block/e374ea64-dc3b-4500-bb4b-974260fb203e) is created.
+        The area of interest and workflow parameters are defined. After **running the job**, 
+        the results are **downloaded** and visualized.
         
         ```python
         import up42
+        up42.authenticate(project_id="12345", project_api_key="12345")
+        # up42.authenticate(cfg_file="config.json")
         
-        up42.authenticate(project_id="123", project_api_key="456")
         project = up42.initialize_project()
-        
         workflow = project.create_workflow(name="30-seconds-workflow", use_existing=True)
-        # Add blocks/tasks to the workflow.
+        
+        # Add data and processing blocks to the workflow.
         print(up42.get_blocks(basic=True))
-        input_tasks= ['sobloo-s2-l1c-aoiclipped', 'sharpening']
+        input_tasks = ['sobloo-s2-l1c-aoiclipped', 'sharpening']
         workflow.add_workflow_tasks(input_tasks=input_tasks)
         
-        # Define the aoi and input parameters of the workflow to run it.
+        # Define the aoi and input parameters of the workflow.
         aoi = workflow.get_example_aoi(as_dataframe=True)
         #aoi = workflow.read_vector_file("data/aoi_berlin.geojson", as_dataframe=True)
         input_parameters = workflow.construct_parameters(geometry=aoi, 
                                                          geometry_operation="bbox", 
                                                          start_date="2018-01-01",
                                                          end_date="2020-12-31",
                                                          limit=1)
         input_parameters["sobloo-s2-l1c-aoiclipped:1"].update({"max_cloud_cover":60})
         
-        # Run a test job to query data availability and check the configuration.
+        # Run a test job to check data availability and configuration.
         test_job = workflow.test_job(input_parameters=input_parameters, track_status=True)
         test_results = test_job.get_results_json()
         print(test_results)
         
         # Run the actual job.
         job = workflow.run_job(input_parameters=input_parameters, track_status=True)
         
         job.download_results()
         job.plot_results()
         ```
         
         ## Support
         
-        For any kind of issues or suggestions please contact us via Email **[support@up42.com](mailto:support@up42.com)** or open a **[github issue](https://github.com/up42/up42-py/issues)**.
+        For any kind of issues or suggestions please see the [**documentation**](https://up42.github.io/up42-py/), open a **[github issue](https://github.com/up42/up42-py/issues)** or contact us via Email **[support@up42.com](mailto:support@up42.com)**
         
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

#### html2text {}

```diff
@@ -1,50 +1,49 @@
-Metadata-Version: 2.1 Name: up42-py Version: 0.9.2 Summary: Python SDK for UP42
+Metadata-Version: 2.1 Name: up42-py Version: 0.9.3 Summary: Python SDK for UP42
 Home-page: https://github.com/up42/up42-py Author: UP42 Author-email:
 support@up42.com License: MIT Description:
     Python SDK for UP42, the geospatial marketplace and developer platform.
 ![](docs/assets/github-banner-3.jpg)
   [https://img.shields.io/pypi/v/up42-py?color=brightgreen] [./coverage.svg]
         [https://img.shields.io/twitter/follow/UP42_.svg?style=social]
- Documentation   â¢   UP42.com   â¢   Support ## Highlights - Python package
-for easy access to **[UP42's](http://www.up42.com)** **geospatial datasets** &
-**processing workflows** - For geospatial **analysis** & **product builders**!
-- Interactive maps & **visualization**, ideal with Jupyter notebooks - Command
-Line Interface (**CLI**) - Developer tools for UP42 custom blocks (coming soon)
-      ## Installation & Documentation See the **[documentation](https://
-up42.github.io/up42-py/)** for **getting started guides**, **examples** and the
-  **code reference**. The package requires Python > 3.6. ```bash pip install
-    up42-py ``` ## Overview - The UP42 Python SDK uses six object classes,
- representing the **hierarchical structure of UP42**: - **Project > Workflow >
-Job > JobTask** - **Catalog** - **Tools** - Each object can **spawn elements of
- one level below**, e.g. - `project = up42.initialize_project()` - `workflow =
-Project().create_workflow()` - `job = workflow.run_job()` ## 30-second Example
-   ![eo-learn-workflow0illustration](docs/assets/vizualisations.jpg) After
-[authentication](https://up42.github.io/up42-py/authentication/) with the UP42
-  project, a new workflow is created and filled with tasks ([Sentinel-2 data]
-  (https://marketplace.up42.com/block/3a381e6b-acb7-4cec-ae65-50798ce80e64),
-[Image Sharpening](https://marketplace.up42.com/block/e374ea64-dc3b-4500-bb4b-
-974260fb203e)). The area of interest and workflow parameters are defined. After
- running the job, the results are downloaded and visualized. ```python import
-   up42 up42.authenticate(project_id="123", project_api_key="456") project =
-up42.initialize_project() workflow = project.create_workflow(name="30-seconds-
-    workflow", use_existing=True) # Add blocks/tasks to the workflow. print
-    (up42.get_blocks(basic=True)) input_tasks= ['sobloo-s2-l1c-aoiclipped',
+                Documentation   â¢   UP42.com   â¢   Support
+## Highlights - Python package for easy access to **[UP42's](http://
+www.up42.com)** **geospatial datasets** & **processing workflows** - Use UP42
+functionality together with your preffered Python libraries! - For geospatial
+**analysis** & **product builders**! - Interactive maps & **visualization**,
+ideal with Jupyter notebooks - Command Line Interface (**CLI**)  ##
+Installation & Documentation See the **[documentation](https://up42.github.io/
+up42-py/)** for **getting started guides**, **examples** and the **code
+reference**. The package requires Python > 3.6. ```bash pip install up42-py ```
+
+## 30-second Example The UP42 Python package uses six classes, representing the
+**hierarchical structure of UP42**: **Project > Workflow > Job > JobTask** and
+**Catalog** & **Tools** ![](docs/assets/vizualisations.jpg) A **new workflow**
+consisting of [**Sentinel-2 data**](https://marketplace.up42.com/block/
+3a381e6b-acb7-4cec-ae65-50798ce80e64) and [**Image Sharpening**](https://
+marketplace.up42.com/block/e374ea64-dc3b-4500-bb4b-974260fb203e) is created.
+The area of interest and workflow parameters are defined. After **running the
+job**, the results are **downloaded** and visualized. ```python import up42
+up42.authenticate(project_id="12345", project_api_key="12345") #
+up42.authenticate(cfg_file="config.json") project = up42.initialize_project()
+workflow = project.create_workflow(name="30-seconds-workflow",
+use_existing=True) # Add data and processing blocks to the workflow. print
+(up42.get_blocks(basic=True)) input_tasks = ['sobloo-s2-l1c-aoiclipped',
 'sharpening'] workflow.add_workflow_tasks(input_tasks=input_tasks) # Define the
-           aoi and input parameters of the workflow to run it. aoi =
- workflow.get_example_aoi(as_dataframe=True) #aoi = workflow.read_vector_file
-       ("data/aoi_berlin.geojson", as_dataframe=True) input_parameters =
-    workflow.construct_parameters(geometry=aoi, geometry_operation="bbox",
-   start_date="2018-01-01", end_date="2020-12-31", limit=1) input_parameters
-["sobloo-s2-l1c-aoiclipped:1"].update({"max_cloud_cover":60}) # Run a test job
-      to query data availability and check the configuration. test_job =
-    workflow.test_job(input_parameters=input_parameters, track_status=True)
-test_results = test_job.get_results_json() print(test_results) # Run the actual
-        job. job = workflow.run_job(input_parameters=input_parameters,
-track_status=True) job.download_results() job.plot_results() ``` ## Support For
-       any kind of issues or suggestions please contact us via Email **
-[support@up42.com](mailto:support@up42.com)** or open a **[github issue](https:
-//github.com/up42/up42-py/issues)**. Platform: UNKNOWN Classifier: Programming
-  Language :: Python :: 3 Classifier: License :: OSI Approved :: MIT License
- Classifier: Operating System :: OS Independent Classifier: Development Status
- :: 4 - Beta Classifier: Intended Audience :: Developers Description-Content-
-                             Type: text/markdown
+aoi and input parameters of the workflow. aoi = workflow.get_example_aoi
+(as_dataframe=True) #aoi = workflow.read_vector_file("data/aoi_berlin.geojson",
+as_dataframe=True) input_parameters = workflow.construct_parameters
+(geometry=aoi, geometry_operation="bbox", start_date="2018-01-01",
+end_date="2020-12-31", limit=1) input_parameters["sobloo-s2-l1c-aoiclipped:
+1"].update({"max_cloud_cover":60}) # Run a test job to check data availability
+and configuration. test_job = workflow.test_job
+(input_parameters=input_parameters, track_status=True) test_results =
+test_job.get_results_json() print(test_results) # Run the actual job. job =
+workflow.run_job(input_parameters=input_parameters, track_status=True)
+job.download_results() job.plot_results() ``` ## Support For any kind of issues
+or suggestions please see the [**documentation**](https://up42.github.io/up42-
+py/), open a **[github issue](https://github.com/up42/up42-py/issues)** or
+contact us via Email **[support@up42.com](mailto:support@up42.com)** Platform:
+UNKNOWN Classifier: Programming Language :: Python :: 3 Classifier: License ::
+OSI Approved :: MIT License Classifier: Operating System :: OS Independent
+Classifier: Development Status :: 4 - Beta Classifier: Intended Audience ::
+Developers Description-Content-Type: text/markdown
```

### Comparing `up42-py-0.9.2/README.md` & `up42-py-0.9.3/README.md`

 * *Files 10% similar despite different names*

```diff
@@ -13,86 +13,81 @@
 
 <p align="center">
     <b>
       <a href="https://up42.github.io/up42-py/">Documentation</a> &nbsp; • &nbsp;
       <a href="http://www.up42.com">UP42.com</a> &nbsp; • &nbsp;
       <a href="#support">Support</a>
     </b>
+</p>
 
 ## Highlights
 - Python package for easy access to **[UP42's](http://www.up42.com)** **geospatial datasets** & **processing workflows**
+- Use UP42 functionality together with your preffered Python libraries!
 - For geospatial **analysis** & **product builders**!
 - Interactive maps & **visualization**, ideal with Jupyter notebooks  
 - Command Line Interface (**CLI**)
-- Developer tools for UP42 custom blocks (coming soon)
 
 
 <img align="right" href="https://up42.github.io/up42-py/" src="docs/assets/docs.png" alt="" height="200"/>
 
 ## Installation & Documentation
 
 See the **[documentation](https://up42.github.io/up42-py/)** for **getting started guides**, **examples** and the **code reference**.
 
 The package requires Python > 3.6.
 
 ```bash
 pip install up42-py
 ```
 
-## Overview
+<br>
 
-- The UP42 Python SDK uses six object classes, representing the **hierarchical structure of UP42**:
-    - **Project > Workflow > Job > JobTask**
-    - **Catalog**
-    - **Tools**
-- Each object can **spawn elements of one level below**, e.g.
-    - `project = up42.initialize_project()`
-    - `workflow = Project().create_workflow()`
-    - `job = workflow.run_job()`
+## 30-second Example
 
+The UP42 Python package uses six classes, representing the **hierarchical structure of UP42**: **Project > Workflow > Job > JobTask** and **Catalog** & **Tools**
 
-## 30-second Example
+![](docs/assets/vizualisations.jpg)
 
-![eo-learn-workflow0illustration](docs/assets/vizualisations.jpg)
 
-After [authentication](https://up42.github.io/up42-py/authentication/) with the UP42 project, 
-a new workflow is created and filled with tasks ([Sentinel-2 data](https://marketplace.up42.com/block/3a381e6b-acb7-4cec-ae65-50798ce80e64), 
-[Image Sharpening](https://marketplace.up42.com/block/e374ea64-dc3b-4500-bb4b-974260fb203e)). 
-The area of interest and workflow parameters are defined. After running the job, the results are downloaded and visualized.
+A **new workflow** consisting of [**Sentinel-2 data**](https://marketplace.up42.com/block/3a381e6b-acb7-4cec-ae65-50798ce80e64)
+and [**Image Sharpening**](https://marketplace.up42.com/block/e374ea64-dc3b-4500-bb4b-974260fb203e) is created.
+The area of interest and workflow parameters are defined. After **running the job**, 
+the results are **downloaded** and visualized.
 
 ```python
 import up42
+up42.authenticate(project_id="12345", project_api_key="12345")
+# up42.authenticate(cfg_file="config.json")
 
-up42.authenticate(project_id="123", project_api_key="456")
 project = up42.initialize_project()
-
 workflow = project.create_workflow(name="30-seconds-workflow", use_existing=True)
-# Add blocks/tasks to the workflow.
+
+# Add data and processing blocks to the workflow.
 print(up42.get_blocks(basic=True))
-input_tasks= ['sobloo-s2-l1c-aoiclipped', 'sharpening']
+input_tasks = ['sobloo-s2-l1c-aoiclipped', 'sharpening']
 workflow.add_workflow_tasks(input_tasks=input_tasks)
 
-# Define the aoi and input parameters of the workflow to run it.
+# Define the aoi and input parameters of the workflow.
 aoi = workflow.get_example_aoi(as_dataframe=True)
 #aoi = workflow.read_vector_file("data/aoi_berlin.geojson", as_dataframe=True)
 input_parameters = workflow.construct_parameters(geometry=aoi, 
                                                  geometry_operation="bbox", 
                                                  start_date="2018-01-01",
                                                  end_date="2020-12-31",
                                                  limit=1)
 input_parameters["sobloo-s2-l1c-aoiclipped:1"].update({"max_cloud_cover":60})
 
-# Run a test job to query data availability and check the configuration.
+# Run a test job to check data availability and configuration.
 test_job = workflow.test_job(input_parameters=input_parameters, track_status=True)
 test_results = test_job.get_results_json()
 print(test_results)
 
 # Run the actual job.
 job = workflow.run_job(input_parameters=input_parameters, track_status=True)
 
 job.download_results()
 job.plot_results()
 ```
 
 ## Support
 
-For any kind of issues or suggestions please contact us via Email **[support@up42.com](mailto:support@up42.com)** or open a **[github issue](https://github.com/up42/up42-py/issues)**.
+For any kind of issues or suggestions please see the [**documentation**](https://up42.github.io/up42-py/), open a **[github issue](https://github.com/up42/up42-py/issues)** or contact us via Email **[support@up42.com](mailto:support@up42.com)**
```

#### html2text {}

```diff
@@ -1,43 +1,42 @@
     Python SDK for UP42, the geospatial marketplace and developer platform.
 ![](docs/assets/github-banner-3.jpg)
   [https://img.shields.io/pypi/v/up42-py?color=brightgreen] [./coverage.svg]
         [https://img.shields.io/twitter/follow/UP42_.svg?style=social]
- Documentation   â¢   UP42.com   â¢   Support ## Highlights - Python package
-for easy access to **[UP42's](http://www.up42.com)** **geospatial datasets** &
-**processing workflows** - For geospatial **analysis** & **product builders**!
-- Interactive maps & **visualization**, ideal with Jupyter notebooks - Command
-Line Interface (**CLI**) - Developer tools for UP42 custom blocks (coming soon)
-      ## Installation & Documentation See the **[documentation](https://
-up42.github.io/up42-py/)** for **getting started guides**, **examples** and the
-  **code reference**. The package requires Python > 3.6. ```bash pip install
-    up42-py ``` ## Overview - The UP42 Python SDK uses six object classes,
- representing the **hierarchical structure of UP42**: - **Project > Workflow >
-Job > JobTask** - **Catalog** - **Tools** - Each object can **spawn elements of
- one level below**, e.g. - `project = up42.initialize_project()` - `workflow =
-Project().create_workflow()` - `job = workflow.run_job()` ## 30-second Example
-   ![eo-learn-workflow0illustration](docs/assets/vizualisations.jpg) After
-[authentication](https://up42.github.io/up42-py/authentication/) with the UP42
-  project, a new workflow is created and filled with tasks ([Sentinel-2 data]
-  (https://marketplace.up42.com/block/3a381e6b-acb7-4cec-ae65-50798ce80e64),
-[Image Sharpening](https://marketplace.up42.com/block/e374ea64-dc3b-4500-bb4b-
-974260fb203e)). The area of interest and workflow parameters are defined. After
- running the job, the results are downloaded and visualized. ```python import
-   up42 up42.authenticate(project_id="123", project_api_key="456") project =
-up42.initialize_project() workflow = project.create_workflow(name="30-seconds-
-    workflow", use_existing=True) # Add blocks/tasks to the workflow. print
-    (up42.get_blocks(basic=True)) input_tasks= ['sobloo-s2-l1c-aoiclipped',
+                Documentation   â¢   UP42.com   â¢   Support
+## Highlights - Python package for easy access to **[UP42's](http://
+www.up42.com)** **geospatial datasets** & **processing workflows** - Use UP42
+functionality together with your preffered Python libraries! - For geospatial
+**analysis** & **product builders**! - Interactive maps & **visualization**,
+ideal with Jupyter notebooks - Command Line Interface (**CLI**)  ##
+Installation & Documentation See the **[documentation](https://up42.github.io/
+up42-py/)** for **getting started guides**, **examples** and the **code
+reference**. The package requires Python > 3.6. ```bash pip install up42-py ```
+
+## 30-second Example The UP42 Python package uses six classes, representing the
+**hierarchical structure of UP42**: **Project > Workflow > Job > JobTask** and
+**Catalog** & **Tools** ![](docs/assets/vizualisations.jpg) A **new workflow**
+consisting of [**Sentinel-2 data**](https://marketplace.up42.com/block/
+3a381e6b-acb7-4cec-ae65-50798ce80e64) and [**Image Sharpening**](https://
+marketplace.up42.com/block/e374ea64-dc3b-4500-bb4b-974260fb203e) is created.
+The area of interest and workflow parameters are defined. After **running the
+job**, the results are **downloaded** and visualized. ```python import up42
+up42.authenticate(project_id="12345", project_api_key="12345") #
+up42.authenticate(cfg_file="config.json") project = up42.initialize_project()
+workflow = project.create_workflow(name="30-seconds-workflow",
+use_existing=True) # Add data and processing blocks to the workflow. print
+(up42.get_blocks(basic=True)) input_tasks = ['sobloo-s2-l1c-aoiclipped',
 'sharpening'] workflow.add_workflow_tasks(input_tasks=input_tasks) # Define the
-           aoi and input parameters of the workflow to run it. aoi =
- workflow.get_example_aoi(as_dataframe=True) #aoi = workflow.read_vector_file
-       ("data/aoi_berlin.geojson", as_dataframe=True) input_parameters =
-    workflow.construct_parameters(geometry=aoi, geometry_operation="bbox",
-   start_date="2018-01-01", end_date="2020-12-31", limit=1) input_parameters
-["sobloo-s2-l1c-aoiclipped:1"].update({"max_cloud_cover":60}) # Run a test job
-      to query data availability and check the configuration. test_job =
-    workflow.test_job(input_parameters=input_parameters, track_status=True)
-test_results = test_job.get_results_json() print(test_results) # Run the actual
-        job. job = workflow.run_job(input_parameters=input_parameters,
-track_status=True) job.download_results() job.plot_results() ``` ## Support For
-       any kind of issues or suggestions please contact us via Email **
-[support@up42.com](mailto:support@up42.com)** or open a **[github issue](https:
-                     //github.com/up42/up42-py/issues)**.
+aoi and input parameters of the workflow. aoi = workflow.get_example_aoi
+(as_dataframe=True) #aoi = workflow.read_vector_file("data/aoi_berlin.geojson",
+as_dataframe=True) input_parameters = workflow.construct_parameters
+(geometry=aoi, geometry_operation="bbox", start_date="2018-01-01",
+end_date="2020-12-31", limit=1) input_parameters["sobloo-s2-l1c-aoiclipped:
+1"].update({"max_cloud_cover":60}) # Run a test job to check data availability
+and configuration. test_job = workflow.test_job
+(input_parameters=input_parameters, track_status=True) test_results =
+test_job.get_results_json() print(test_results) # Run the actual job. job =
+workflow.run_job(input_parameters=input_parameters, track_status=True)
+job.download_results() job.plot_results() ``` ## Support For any kind of issues
+or suggestions please see the [**documentation**](https://up42.github.io/up42-
+py/), open a **[github issue](https://github.com/up42/up42-py/issues)** or
+contact us via Email **[support@up42.com](mailto:support@up42.com)**
```

### Comparing `up42-py-0.9.2/setup.py` & `up42-py-0.9.3/setup.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/tests/context.py` & `up42-py-0.9.3/tests/context.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/tests/e2e.py` & `up42-py-0.9.3/tests/e2e.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/tests/fixtures.py` & `up42-py-0.9.3/tests/fixtures.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/tests/test_auth.py` & `up42-py-0.9.3/tests/test_auth.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/tests/test_catalog.py` & `up42-py-0.9.3/tests/test_catalog.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/tests/test_cli.py` & `up42-py-0.9.3/tests/test_cli.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/tests/test_initialization.py` & `up42-py-0.9.3/tests/test_initialization.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/tests/test_job.py` & `up42-py-0.9.3/tests/test_job.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,16 +1,15 @@
 import os
 from pathlib import Path
 import tempfile
 import tarfile
-from unittest.mock import patch
+from shutil import copyfile
 
 import requests_mock
 import pytest
-import geopandas as gpd
 from folium import Map
 
 # pylint: disable=unused-import
 from .fixtures import auth_mock, auth_live, job_mock, job_live, jobtask_mock
 import up42  # pylint: disable=wrong-import-order
 
 
@@ -249,13 +248,28 @@
     with tarfile.open(fp_tgz) as tar:
         tar.extractall(fp_tgz.parent)
     fp_tif = (
         fp_tgz.parent
         / "output/7e17f023-a8e3-43bd-aaac-5bbef749c7f4/7e17f023-a8e3-43bd-aaac-5bbef749c7f4_0-0.tif"
     )
     fp_data_json = fp_tgz.parent / "output/data.json"
-    df = gpd.read_file(fp_data_json)
 
     job_mock.results = [str(fp_tif), str(fp_data_json)]
-    with patch.object(job_mock, "get_results_json", return_value=df):
-        map_object = job_mock.map_results()
+    map_object = job_mock.map_results()
+    assert isinstance(map_object, Map)
+
+
+def test_map_results_additional_geojson(job_mock):
+    fp_tgz = Path(__file__).resolve().parent / "mock_data/result_tif.tgz"
+    with tarfile.open(fp_tgz) as tar:
+        tar.extractall(fp_tgz.parent)
+    fp_tif = (
+        fp_tgz.parent
+        / "output/7e17f023-a8e3-43bd-aaac-5bbef749c7f4/7e17f023-a8e3-43bd-aaac-5bbef749c7f4_0-0.tif"
+    )
+    fp_data_json = fp_tgz.parent / "output/data.json"
+    fp_data_geojson = fp_tgz.parent / "output/additional_vector_file.geojson"
+    copyfile(fp_data_json, fp_data_geojson)
+
+    job_mock.results = [str(fp_tif), str(fp_data_json), str(fp_data_geojson)]
+    map_object = job_mock.map_results()
     assert isinstance(map_object, Map)
```

### Comparing `up42-py-0.9.2/tests/test_jobtask.py` & `up42-py-0.9.3/tests/test_jobtask.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/tests/test_project.py` & `up42-py-0.9.3/tests/test_project.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/tests/test_tools.py` & `up42-py-0.9.3/tests/test_tools.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/tests/test_utils.py` & `up42-py-0.9.3/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/tests/test_workflow.py` & `up42-py-0.9.3/tests/test_workflow.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/up42/__init__.py` & `up42-py-0.9.3/up42/__init__.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/up42/auth.py` & `up42-py-0.9.3/up42/auth.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/up42/catalog.py` & `up42-py-0.9.3/up42/catalog.py`

 * *Files 2% similar despite different names*

```diff
@@ -48,19 +48,17 @@
         "provider": "sobloo-image",
     },
 }
 
 # pylint: disable=duplicate-code
 class Catalog(Tools):
     def __init__(self, auth: Auth):
-        """The Catalog class enables access to the UP42 catalog search. You can search
+        """
+        The Catalog class enables access to the UP42 catalog search. You can search
         for satellite image scenes for different sensors and criteria like cloud cover etc.
-
-        Public Methods:
-            construct_parameters, search, download_quicklooks
         """
         self.auth = auth
         self.quicklooks = None
 
     def __repr__(self):
         return f"Catalog(auth={self.auth})"
 
@@ -89,15 +87,15 @@
         Follows STAC principles and property names.
 
         Args:
             geometry: The search geometry, one of Dict, Feature, FeatureCollection,
                 List, GeoDataFrame, Point, Polygon.
             start_date: Query period starting day, format "2020-01-01".
             end_date: Query period ending day, format "2020-01-01".
-            sensors: The satellite sensor(s) to search for, one or multiple of
+            sensors: The satellite sensors to search for, one or multiple of
                 ["pleiades", "spot", "sentinel1", "sentinel2", "sentinel3", "sentinel5p"]
             limit: The maximum number of search results to return.
             max_cloudcover: Maximum cloudcover % - 100 will return all scenes, 8.4 will return all
                 scenes with 8.4 or less cloudcover.
             sortby: The property to sort by, "cloudCoverage", "acquisitionDate",
                 "acquisitionIdentifier", "incidenceAngle", "snowCover"
             ascending: Ascending sort order by default, descending if False.
@@ -146,15 +144,15 @@
         self, search_parameters: Dict, as_dataframe: bool = True
     ) -> Union[GeoDataFrame, Dict]:
         """
         Searches the catalog for the the search parameters and returns the metadata of
         the matching scenes.
 
         Args:
-            search_params: The catalog search parameters, see example.
+            search_parameters: The catalog search parameters, see example.
             as_dataframe: return type, GeoDataFrame if True (default), FeatureCollection if False.
 
         Returns:
             The search results as a GeoDataFrame, optionally as json dict.
 
         Example:
             ```python
@@ -218,16 +216,16 @@
     ) -> List[str]:
         """
         Gets the quicklooks of scenes from a single sensor. After download, can
         be plotted via catalog.plot_quicklooks().
 
         Args:
             image_ids: provider image_id in the form "6dffb8be-c2ab-46e3-9c1c-6958a54e4527"
-            sensors: The satellite sensor(s) to search for, one of
-                "pleiades", "spot", "sentinel1", "sentinel2", "sentinel3", "sentinel5p".
+            sensor: The satellite sensor of the image_ids, one of "pleiades", "spot",
+                "sentinel1", "sentinel2", "sentinel3", "sentinel5p".
             output_directory: The file output directory, defaults to the current working
                 directory.
 
         Returns:
             List of quicklook image output file paths.
         """
         if sensor not in list(supported_sensors.keys()):
```

### Comparing `up42-py-0.9.2/up42/cli.py` & `up42-py-0.9.3/up42/cli.py`

 * *Files identical despite different names*

### Comparing `up42-py-0.9.2/up42/job.py` & `up42-py-0.9.3/up42/job.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 import logging
 from pathlib import Path
 from time import sleep
 from typing import Dict, List, Union
 
 import folium
 from geopandas import GeoDataFrame
+import geopandas as gpd
 import numpy as np
 import requests
 import requests.exceptions
 from shapely.geometry import box
 from rasterio.vrt import WarpedVRT
 import rasterio
 
@@ -32,21 +33,17 @@
 
 
 # pylint: disable=duplicate-code
 class Job(Tools):
     def __init__(
         self, auth: Auth, project_id: str, job_id: str, order_ids: List[str] = None,
     ):
-        """The Job class provides access to the results, parameters and tasks of UP42
+        """
+        The Job class provides access to the results, parameters and tasks of UP42
         Jobs (Workflows that have been run as Jobs).
-
-        Public Methods:
-            get_status, track_status, cancel_job, download_quicklooks, get_results_json
-            download_results, upload_results_to_bucket, map_results,
-            get_logs, get_jobtasks, get_jobtasks_results_json
         """
         self.auth = auth
         self.project_id = project_id
         self.job_id = job_id
         self.quicklooks = None
         self.results = None
         if order_ids is None:
@@ -237,17 +234,18 @@
 
     def map_results(self, show_images=True, name_column: str = "uid") -> None:
         """
         Displays data.json, and if available, one or multiple results geotiffs.
 
         Args:
             show_images: Shows images if True (default), only features if False.
-            name_column: Name of the column that provides the Feature/Layer name.
-        # TODO: Make generic with scene_id column integrated.
+            name_column: Name of the feature property that provides the Feature/Layer name.
         """
+        # TODO: Make generic with scene_id column integrated.
+        # TODO: Add way to also display data block image together with processing output vectors
         if self.results is None:
             raise ValueError(
                 "You first need to download the results via job.download_results()!"
             )
 
         def _style_function(feature):  # pylint: disable=unused-argument
             return {
@@ -261,17 +259,23 @@
             return {
                 "fillColor": "#ffaf00",
                 "color": "red",
                 "weight": 3.5,
                 "dashArray": "5, 5",
             }
 
-        # Add feature to map.
-        # TODO: Blocks that have results in separate json file.
-        df: GeoDataFrame = self.get_results_json(as_dataframe=True)  # type: ignore
+        # Add features to map.
+        # Some blocks store vector results in an additional geojson file.
+        json_fp = [fp for fp in self.results if fp.endswith(".geojson")]
+        if json_fp:
+            json_fp = json_fp[0]
+        else:
+            json_fp = [fp for fp in self.results if fp.endswith(".json")][0]
+        df: GeoDataFrame = gpd.read_file(json_fp)
+
         centroid = box(*df.total_bounds).centroid
         m = folium_base_map(lat=centroid.y, lon=centroid.x,)
 
         for idx, row in df.iterrows():  # type: ignore
             try:
                 feature_name = row.loc[name_column]
             except KeyError:
```

### Comparing `up42-py-0.9.2/up42/jobtask.py` & `up42-py-0.9.3/up42/jobtask.py`

 * *Files 5% similar despite different names*

```diff
@@ -12,20 +12,18 @@
 
 
 # pylint: disable=duplicate-code
 class JobTask(Tools):
     def __init__(
         self, auth: Auth, project_id: str, job_id: str, jobtask_id: str,
     ):
-        """The JobTask class provides access to the results and parameters of single
+        """
+        The JobTask class provides access to the results and parameters of single
         Tasks of UP42 Jobs (each Job contains one or multiple Jobtasks, one for each
         block in the workflow).
-
-        Public Methods:
-            get_results_json, download_results, download_quicklooks
         """
         self.auth = auth
         self.project_id = project_id
         self.job_id = job_id
         self.jobtask_id = jobtask_id
         self.quicklooks = None
         self.results = None
```

### Comparing `up42-py-0.9.2/up42/project.py` & `up42-py-0.9.3/up42/project.py`

 * *Files 2% similar despite different names*

```diff
@@ -13,18 +13,14 @@
 
 
 class Project(Tools):
     def __init__(self, auth: Auth, project_id: str):
         """
         The Project class can query all available workflows and spawn new workflows
         within an UP42 project. Also handles project user settings.
-
-        Public Methods:
-            create_workflow, get_workflows, get_jobs, get_project_settings,
-            update_project_settings
         """
         self.auth = auth
         self.project_id = project_id
         if self.auth.get_info:
             self.info = self._get_info()
 
     def __repr__(self):
```

### Comparing `up42-py-0.9.2/up42/tools.py` & `up42-py-0.9.3/up42/tools.py`

 * *Files 4% similar despite different names*

```diff
@@ -27,17 +27,14 @@
 # pylint: disable=no-member, duplicate-code
 class Tools:
     def __init__(self, auth=None):
         """
         The tools class contains functionality that is not bound to a specific UP42 object,
         e.g. for aoi handling etc., UP42 block information, validatin a block manifest etc.
         They can be accessed from every object and also from the imported up42 package directly.
-
-        Public methods:
-            read_vector_file, get_example_aoi, draw_aoi, plot_coverage, plot_quicklooks
         """
         if auth:
             self.auth = auth
         self.quicklooks = None
         self.results = None
 
     # pylint: disable=no-self-use
```

### Comparing `up42-py-0.9.2/up42/utils.py` & `up42-py-0.9.3/up42/utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -225,15 +225,15 @@
     filepaths = [Path(path) for path in filepaths]
 
     imagepaths = [
         path for path in filepaths if str(path.suffix) in plot_file_format  # type: ignore
     ]
     if not imagepaths:
         raise ValueError(
-            f"Only files of the formats {plot_file_format} can " "currently be plotted."
+            f"This function only plots files of format {plot_file_format}."
         )
 
     if not titles:
         titles = [Path(fp).stem for fp in imagepaths]
     if not isinstance(titles, list):
         titles = [titles]  # type: ignore
 
@@ -324,14 +324,15 @@
                 {"geometry": [vector.buffer(0.00001)]}, crs=4326
             )  # Around 1m buffer # TODO: Find better solution than small buffer?
         elif isinstance(vector, GeoDataFrame):
             df = vector
             if df.crs.to_string() != "EPSG:4326":
                 df = df.to_crs(epsg=4326)
 
+    df.geometry = df.geometry.buffer(0)
     if as_dataframe:
         return df
     else:
         fc = df.__geo_interface__
         return fc
```

### Comparing `up42-py-0.9.2/up42/workflow.py` & `up42-py-0.9.3/up42/workflow.py`

 * *Files 1% similar despite different names*

```diff
@@ -20,18 +20,14 @@
 
 class Workflow(Tools):
     def __init__(self, auth: Auth, project_id: str, workflow_id: str):
         """
         The Workflow class can query all available and spawn new jobs for
         an UP42 Workflow and helps to find and set the the workflow tasks, parameters
         and aoi.
-
-        Public Methods:
-            get_compatible_blocks, get_workflow_tasks, add_workflow_tasks, get_parameters_info,
-            construct_parameters, test_job, run_job, get_jobs, update_name, delete
         """
         self.auth = auth
         self.project_id = project_id
         self.workflow_id = workflow_id
         if self.auth.get_info:
             self.info = self._get_info()
```

### Comparing `up42-py-0.9.2/up42_py.egg-info/PKG-INFO` & `up42-py-0.9.3/up42_py.egg-info/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: up42-py
-Version: 0.9.2
+Version: 0.9.3
 Summary: Python SDK for UP42
 Home-page: https://github.com/up42/up42-py
 Author: UP42
 Author-email: support@up42.com
 License: MIT
 Description: 
         <p align="center">
@@ -21,93 +21,88 @@
         
         <p align="center">
             <b>
               <a href="https://up42.github.io/up42-py/">Documentation</a> &nbsp; • &nbsp;
               <a href="http://www.up42.com">UP42.com</a> &nbsp; • &nbsp;
               <a href="#support">Support</a>
             </b>
+        </p>
         
         ## Highlights
         - Python package for easy access to **[UP42's](http://www.up42.com)** **geospatial datasets** & **processing workflows**
+        - Use UP42 functionality together with your preffered Python libraries!
         - For geospatial **analysis** & **product builders**!
         - Interactive maps & **visualization**, ideal with Jupyter notebooks  
         - Command Line Interface (**CLI**)
-        - Developer tools for UP42 custom blocks (coming soon)
         
         
         <img align="right" href="https://up42.github.io/up42-py/" src="docs/assets/docs.png" alt="" height="200"/>
         
         ## Installation & Documentation
         
         See the **[documentation](https://up42.github.io/up42-py/)** for **getting started guides**, **examples** and the **code reference**.
         
         The package requires Python > 3.6.
         
         ```bash
         pip install up42-py
         ```
         
-        ## Overview
+        <br>
         
-        - The UP42 Python SDK uses six object classes, representing the **hierarchical structure of UP42**:
-            - **Project > Workflow > Job > JobTask**
-            - **Catalog**
-            - **Tools**
-        - Each object can **spawn elements of one level below**, e.g.
-            - `project = up42.initialize_project()`
-            - `workflow = Project().create_workflow()`
-            - `job = workflow.run_job()`
+        ## 30-second Example
         
+        The UP42 Python package uses six classes, representing the **hierarchical structure of UP42**: **Project > Workflow > Job > JobTask** and **Catalog** & **Tools**
         
-        ## 30-second Example
+        ![](docs/assets/vizualisations.jpg)
         
-        ![eo-learn-workflow0illustration](docs/assets/vizualisations.jpg)
         
-        After [authentication](https://up42.github.io/up42-py/authentication/) with the UP42 project, 
-        a new workflow is created and filled with tasks ([Sentinel-2 data](https://marketplace.up42.com/block/3a381e6b-acb7-4cec-ae65-50798ce80e64), 
-        [Image Sharpening](https://marketplace.up42.com/block/e374ea64-dc3b-4500-bb4b-974260fb203e)). 
-        The area of interest and workflow parameters are defined. After running the job, the results are downloaded and visualized.
+        A **new workflow** consisting of [**Sentinel-2 data**](https://marketplace.up42.com/block/3a381e6b-acb7-4cec-ae65-50798ce80e64)
+        and [**Image Sharpening**](https://marketplace.up42.com/block/e374ea64-dc3b-4500-bb4b-974260fb203e) is created.
+        The area of interest and workflow parameters are defined. After **running the job**, 
+        the results are **downloaded** and visualized.
         
         ```python
         import up42
+        up42.authenticate(project_id="12345", project_api_key="12345")
+        # up42.authenticate(cfg_file="config.json")
         
-        up42.authenticate(project_id="123", project_api_key="456")
         project = up42.initialize_project()
-        
         workflow = project.create_workflow(name="30-seconds-workflow", use_existing=True)
-        # Add blocks/tasks to the workflow.
+        
+        # Add data and processing blocks to the workflow.
         print(up42.get_blocks(basic=True))
-        input_tasks= ['sobloo-s2-l1c-aoiclipped', 'sharpening']
+        input_tasks = ['sobloo-s2-l1c-aoiclipped', 'sharpening']
         workflow.add_workflow_tasks(input_tasks=input_tasks)
         
-        # Define the aoi and input parameters of the workflow to run it.
+        # Define the aoi and input parameters of the workflow.
         aoi = workflow.get_example_aoi(as_dataframe=True)
         #aoi = workflow.read_vector_file("data/aoi_berlin.geojson", as_dataframe=True)
         input_parameters = workflow.construct_parameters(geometry=aoi, 
                                                          geometry_operation="bbox", 
                                                          start_date="2018-01-01",
                                                          end_date="2020-12-31",
                                                          limit=1)
         input_parameters["sobloo-s2-l1c-aoiclipped:1"].update({"max_cloud_cover":60})
         
-        # Run a test job to query data availability and check the configuration.
+        # Run a test job to check data availability and configuration.
         test_job = workflow.test_job(input_parameters=input_parameters, track_status=True)
         test_results = test_job.get_results_json()
         print(test_results)
         
         # Run the actual job.
         job = workflow.run_job(input_parameters=input_parameters, track_status=True)
         
         job.download_results()
         job.plot_results()
         ```
         
         ## Support
         
-        For any kind of issues or suggestions please contact us via Email **[support@up42.com](mailto:support@up42.com)** or open a **[github issue](https://github.com/up42/up42-py/issues)**.
+        For any kind of issues or suggestions please see the [**documentation**](https://up42.github.io/up42-py/), open a **[github issue](https://github.com/up42/up42-py/issues)** or contact us via Email **[support@up42.com](mailto:support@up42.com)**
         
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

#### html2text {}

```diff
@@ -1,50 +1,49 @@
-Metadata-Version: 2.1 Name: up42-py Version: 0.9.2 Summary: Python SDK for UP42
+Metadata-Version: 2.1 Name: up42-py Version: 0.9.3 Summary: Python SDK for UP42
 Home-page: https://github.com/up42/up42-py Author: UP42 Author-email:
 support@up42.com License: MIT Description:
     Python SDK for UP42, the geospatial marketplace and developer platform.
 ![](docs/assets/github-banner-3.jpg)
   [https://img.shields.io/pypi/v/up42-py?color=brightgreen] [./coverage.svg]
         [https://img.shields.io/twitter/follow/UP42_.svg?style=social]
- Documentation   â¢   UP42.com   â¢   Support ## Highlights - Python package
-for easy access to **[UP42's](http://www.up42.com)** **geospatial datasets** &
-**processing workflows** - For geospatial **analysis** & **product builders**!
-- Interactive maps & **visualization**, ideal with Jupyter notebooks - Command
-Line Interface (**CLI**) - Developer tools for UP42 custom blocks (coming soon)
-      ## Installation & Documentation See the **[documentation](https://
-up42.github.io/up42-py/)** for **getting started guides**, **examples** and the
-  **code reference**. The package requires Python > 3.6. ```bash pip install
-    up42-py ``` ## Overview - The UP42 Python SDK uses six object classes,
- representing the **hierarchical structure of UP42**: - **Project > Workflow >
-Job > JobTask** - **Catalog** - **Tools** - Each object can **spawn elements of
- one level below**, e.g. - `project = up42.initialize_project()` - `workflow =
-Project().create_workflow()` - `job = workflow.run_job()` ## 30-second Example
-   ![eo-learn-workflow0illustration](docs/assets/vizualisations.jpg) After
-[authentication](https://up42.github.io/up42-py/authentication/) with the UP42
-  project, a new workflow is created and filled with tasks ([Sentinel-2 data]
-  (https://marketplace.up42.com/block/3a381e6b-acb7-4cec-ae65-50798ce80e64),
-[Image Sharpening](https://marketplace.up42.com/block/e374ea64-dc3b-4500-bb4b-
-974260fb203e)). The area of interest and workflow parameters are defined. After
- running the job, the results are downloaded and visualized. ```python import
-   up42 up42.authenticate(project_id="123", project_api_key="456") project =
-up42.initialize_project() workflow = project.create_workflow(name="30-seconds-
-    workflow", use_existing=True) # Add blocks/tasks to the workflow. print
-    (up42.get_blocks(basic=True)) input_tasks= ['sobloo-s2-l1c-aoiclipped',
+                Documentation   â¢   UP42.com   â¢   Support
+## Highlights - Python package for easy access to **[UP42's](http://
+www.up42.com)** **geospatial datasets** & **processing workflows** - Use UP42
+functionality together with your preffered Python libraries! - For geospatial
+**analysis** & **product builders**! - Interactive maps & **visualization**,
+ideal with Jupyter notebooks - Command Line Interface (**CLI**)  ##
+Installation & Documentation See the **[documentation](https://up42.github.io/
+up42-py/)** for **getting started guides**, **examples** and the **code
+reference**. The package requires Python > 3.6. ```bash pip install up42-py ```
+
+## 30-second Example The UP42 Python package uses six classes, representing the
+**hierarchical structure of UP42**: **Project > Workflow > Job > JobTask** and
+**Catalog** & **Tools** ![](docs/assets/vizualisations.jpg) A **new workflow**
+consisting of [**Sentinel-2 data**](https://marketplace.up42.com/block/
+3a381e6b-acb7-4cec-ae65-50798ce80e64) and [**Image Sharpening**](https://
+marketplace.up42.com/block/e374ea64-dc3b-4500-bb4b-974260fb203e) is created.
+The area of interest and workflow parameters are defined. After **running the
+job**, the results are **downloaded** and visualized. ```python import up42
+up42.authenticate(project_id="12345", project_api_key="12345") #
+up42.authenticate(cfg_file="config.json") project = up42.initialize_project()
+workflow = project.create_workflow(name="30-seconds-workflow",
+use_existing=True) # Add data and processing blocks to the workflow. print
+(up42.get_blocks(basic=True)) input_tasks = ['sobloo-s2-l1c-aoiclipped',
 'sharpening'] workflow.add_workflow_tasks(input_tasks=input_tasks) # Define the
-           aoi and input parameters of the workflow to run it. aoi =
- workflow.get_example_aoi(as_dataframe=True) #aoi = workflow.read_vector_file
-       ("data/aoi_berlin.geojson", as_dataframe=True) input_parameters =
-    workflow.construct_parameters(geometry=aoi, geometry_operation="bbox",
-   start_date="2018-01-01", end_date="2020-12-31", limit=1) input_parameters
-["sobloo-s2-l1c-aoiclipped:1"].update({"max_cloud_cover":60}) # Run a test job
-      to query data availability and check the configuration. test_job =
-    workflow.test_job(input_parameters=input_parameters, track_status=True)
-test_results = test_job.get_results_json() print(test_results) # Run the actual
-        job. job = workflow.run_job(input_parameters=input_parameters,
-track_status=True) job.download_results() job.plot_results() ``` ## Support For
-       any kind of issues or suggestions please contact us via Email **
-[support@up42.com](mailto:support@up42.com)** or open a **[github issue](https:
-//github.com/up42/up42-py/issues)**. Platform: UNKNOWN Classifier: Programming
-  Language :: Python :: 3 Classifier: License :: OSI Approved :: MIT License
- Classifier: Operating System :: OS Independent Classifier: Development Status
- :: 4 - Beta Classifier: Intended Audience :: Developers Description-Content-
-                             Type: text/markdown
+aoi and input parameters of the workflow. aoi = workflow.get_example_aoi
+(as_dataframe=True) #aoi = workflow.read_vector_file("data/aoi_berlin.geojson",
+as_dataframe=True) input_parameters = workflow.construct_parameters
+(geometry=aoi, geometry_operation="bbox", start_date="2018-01-01",
+end_date="2020-12-31", limit=1) input_parameters["sobloo-s2-l1c-aoiclipped:
+1"].update({"max_cloud_cover":60}) # Run a test job to check data availability
+and configuration. test_job = workflow.test_job
+(input_parameters=input_parameters, track_status=True) test_results =
+test_job.get_results_json() print(test_results) # Run the actual job. job =
+workflow.run_job(input_parameters=input_parameters, track_status=True)
+job.download_results() job.plot_results() ``` ## Support For any kind of issues
+or suggestions please see the [**documentation**](https://up42.github.io/up42-
+py/), open a **[github issue](https://github.com/up42/up42-py/issues)** or
+contact us via Email **[support@up42.com](mailto:support@up42.com)** Platform:
+UNKNOWN Classifier: Programming Language :: Python :: 3 Classifier: License ::
+OSI Approved :: MIT License Classifier: Operating System :: OS Independent
+Classifier: Development Status :: 4 - Beta Classifier: Intended Audience ::
+Developers Description-Content-Type: text/markdown
```

### Comparing `up42-py-0.9.2/up42_py.egg-info/SOURCES.txt` & `up42-py-0.9.3/up42_py.egg-info/SOURCES.txt`

 * *Files identical despite different names*

