# Comparing `tmp/Architectural Lens-0.0.2.tar.gz` & `tmp/Architectural Lens-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "Architectural Lens-0.0.2.tar", last modified: Thu Mar 30 19:50:24 2023, max compression
+gzip compressed data, was "Architectural Lens-0.0.3.tar", last modified: Thu Apr  6 10:11:52 2023, max compression
```

## Comparing `Architectural Lens-0.0.2.tar` & `Architectural Lens-0.0.3.tar`

### file list

```diff
@@ -1,35 +1,35 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:50:24.511218 Architectural Lens-0.0.2/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:50:24.507218 Architectural Lens-0.0.2/Architectural_Lens.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      314 2023-03-30 19:50:24.000000 Architectural Lens-0.0.2/Architectural_Lens.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      733 2023-03-30 19:50:24.000000 Architectural Lens-0.0.2/Architectural_Lens.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-30 19:50:24.000000 Architectural Lens-0.0.2/Architectural_Lens.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-03-30 19:50:24.000000 Architectural Lens-0.0.2/Architectural_Lens.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       57 2023-03-30 19:50:24.000000 Architectural Lens-0.0.2/Architectural_Lens.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        4 2023-03-30 19:50:24.000000 Architectural Lens-0.0.2/Architectural_Lens.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      314 2023-03-30 19:50:24.511218 Architectural Lens-0.0.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    10752 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-03-30 19:50:24.511218 Architectural Lens-0.0.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      733 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:50:24.507218 Architectural Lens-0.0.2/src/
--rw-r--r--   0 runner    (1001) docker     (123)       64 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3512 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/cli_interface.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:50:24.507218 Architectural Lens-0.0.2/src/core/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/core/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2631 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/core/bt_file.py
--rw-r--r--   0 runner    (1001) docker     (123)     3923 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/core/bt_graph.py
--rw-r--r--   0 runner    (1001) docker     (123)     2676 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/core/bt_module.py
--rw-r--r--   0 runner    (1001) docker     (123)       30 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/main.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:50:24.507218 Architectural Lens-0.0.2/src/plantuml/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/plantuml/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      290 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/plantuml/fetch_git.py
--rw-r--r--   0 runner    (1001) docker     (123)    19854 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/plantuml/plantuml_file_creator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:50:24.511218 Architectural Lens-0.0.2/src/plantumlv2/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/plantumlv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5187 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/plantumlv2/pu_entities.py
--rw-r--r--   0 runner    (1001) docker     (123)     8995 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/plantumlv2/pu_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)      341 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/plantumlv2/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:50:24.511218 Architectural Lens-0.0.2/src/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      424 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/utils/config_manager_singleton.py
--rw-r--r--   0 runner    (1001) docker     (123)     1530 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/utils/functions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1894 2023-03-30 19:50:14.000000 Architectural Lens-0.0.2/src/utils/path_manager_singleton.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:11:52.719928 Architectural Lens-0.0.3/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:11:52.715928 Architectural Lens-0.0.3/Architectural_Lens.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      314 2023-04-06 10:11:52.000000 Architectural Lens-0.0.3/Architectural_Lens.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      733 2023-04-06 10:11:52.000000 Architectural Lens-0.0.3/Architectural_Lens.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 10:11:52.000000 Architectural Lens-0.0.3/Architectural_Lens.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-04-06 10:11:52.000000 Architectural Lens-0.0.3/Architectural_Lens.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-04-06 10:11:52.000000 Architectural Lens-0.0.3/Architectural_Lens.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        4 2023-04-06 10:11:52.000000 Architectural Lens-0.0.3/Architectural_Lens.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      314 2023-04-06 10:11:52.719928 Architectural Lens-0.0.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    10856 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-06 10:11:52.723928 Architectural Lens-0.0.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      733 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:11:52.715928 Architectural Lens-0.0.3/src/
+-rw-r--r--   0 runner    (1001) docker     (123)       64 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3421 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/cli_interface.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:11:52.719928 Architectural Lens-0.0.3/src/core/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2812 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/core/bt_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3923 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/core/bt_graph.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2676 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/core/bt_module.py
+-rw-r--r--   0 runner    (1001) docker     (123)       30 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/main.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:11:52.719928 Architectural Lens-0.0.3/src/plantuml/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/plantuml/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      290 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/plantuml/fetch_git.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19854 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/plantuml/plantuml_file_creator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:11:52.719928 Architectural Lens-0.0.3/src/plantumlv2/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/plantumlv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5187 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/plantumlv2/pu_entities.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9348 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/plantumlv2/pu_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)      341 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/plantumlv2/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:11:52.719928 Architectural Lens-0.0.3/src/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      424 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/utils/config_manager_singleton.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1530 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/utils/functions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1894 2023-04-06 10:11:40.000000 Architectural Lens-0.0.3/src/utils/path_manager_singleton.py
```

### Comparing `Architectural Lens-0.0.2/Architectural_Lens.egg-info/SOURCES.txt` & `Architectural Lens-0.0.3/Architectural_Lens.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `Architectural Lens-0.0.2/README.md` & `Architectural Lens-0.0.3/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -1,53 +1,55 @@
 # Architectural Lens
 
-MT-Diagrams is a Python software tool that generates customizable visual package views, showcasing the packages in your system and their dependencies. It offers the flexibility to include or exclude specific packages to suit your requirements for comprehensible views.
+Architectural-Lens is a Python software tool that generates customizable visual package views, showcasing the packages in your system and their dependencies. It offers the flexibility to include or exclude specific packages to suit your requirements for comprehensible views.
 
-Moreover, MT-Diagrams can highlight the differences between your working branch and a specified remote branch, including added or removed dependencies and created or deleted packages, by using green and red highlighting.
+Moreover, Architectural-Lens can highlight the differences between your working branch and a specified remote branch, including added or removed dependencies and created or deleted packages, by using green and red highlighting.
 
-Lastly, MT-Diagrams can display the highlighted differences in the system views when a pull request is created on GitHub. It automatically generates the views specified in your config, highlights the differences, and displays them in your pull request, simplifying the review process.
+Lastly, Architectural-Lens can display the highlighted differences in the system views when a pull request is created on GitHub. It automatically generates the views specified in your config, highlights the differences, and displays them in your pull request, simplifying the review process.
 
 To help you get started, this readme includes various options in combination with the setup of a config file.
 
+### Runs on Python 3.9, 3.10, 3.11
+
 ## Installation
 
-To install mt-diagrams, simply use the pip package manager by running the following command:
+To install Architectural-Lens, simply use the pip package manager by running the following command:
 
-`pip install mt-diagrams` (You might need administrative right to perform the operation)
+`pip install Architectural-Lens` (You might need administrative right to perform the operation)
 
-This will download and install the necessary files and dependencies needed for mt-diagrams to run properly.
+This will download and install the necessary files and dependencies needed for Architectural-Lens to run properly.
 
 ## Commands
 
 All commands must be run from the project's root folder
 
 <b>The system has 4 commands:</b> 
 
 
--`mt-diagrams init`- Creates the config template
+-`archlens init`- Creates the config template
 
--`mt-diagrams render` - Renders the views specified in the config
+-`archlens render` - Renders the views specified in the config
 
--`mt-diagrams render-diff` - Renders the differences in the views between your working branch and a specified branch
+-`archlens render-diff` - Renders the differences in the views between your working branch and a specified branch
 
--`mt-diagrams create-action` Creates the github action which will automatically add the difference views to pull requests.
+-`archlens create-action` Creates the github action which will automatically add the difference views to pull requests.
 
 # Using the system
 
-In this section, we will guide you through using the MT-Diagrams system by explaining the commands and output with the example of an API project called 'zeeguu-api' that can be found at https://github.com/zeeguu/api.
+In this section, we will guide you through using the Architectural-Lens system by explaining the commands and output with the example of an API project called 'zeeguu-api' that can be found at https://github.com/zeeguu/api.
 
 Although the project is not large, understanding the system even for this project size of roughly 40 packages can be challenging. To begin generating views, you need to be in the root of your project and run the following command:
 
-- `mt-diagrams init` 
+- `archlens init` 
 
-This will create an "mt-config.json" file in your root folder, where you can edit your desired views. This is the initial config:
+This will create an "archlens.json" file in your root folder, where you can edit your desired views. This is the initial config:
 
 ```json
  {
-    "$schema": "https://raw.githubusercontent.com/Perlten/MT-diagrams/master/config.schema.json",
+    "$schema": "https://raw.githubusercontent.com/Perlten/Architectural-Lens/master/config.schema.json",
     "name": "",
     "rootFolder": "",
     "github": {
         "url": "",
         "branch": "main"
     },
     "saveLocation": "./diagrams/",
@@ -63,27 +65,27 @@
 
 Here are two views of the 'zeeguu-api' project that we will be using as examples:
 
 - A complete view of the system
 
 ![Zeeguu view](.github/readme/zeeguu-completeView.png)
 
-Hard to grasp? MT-diagrams agrees with you, which is why this tool exists.
+Hard to grasp? Architectural-Lens agrees with you, which is why this tool exists.
 
 - A view of the system where everything except "core" and its sub-packages has been scraped away:
 
 ![Zeeguu core view](.github/readme/zeeguu-coreViewxx.png)
 
-Here is an edited version of the "mt-config.json" file for the 'zeeguu-api' project, which represents the first two views we created earlier, along with comments explaining each field briefly:
+Here is an edited version of the "archlens.json" file for the 'zeeguu-api' project, which represents the first two views we created earlier, along with comments explaining each field briefly:
 
-The "views" field in the "mt-config.json" file allows you to define as many views as you need for your project. Simply add a new object with a unique name for each view you want to create. For example, if you wanted to create a view that showed only the "utils" package in the "api" folder, you could add the following to the "views" field:
+The "views" field in the "archlens.json" file allows you to define as many views as you need for your project. Simply add a new object with a unique name for each view you want to create. For example, if you wanted to create a view that showed only the "utils" package in the "api" folder, you could add the following to the "views" field:
 
 ```json
 {
-    "$schema": "https://raw.githubusercontent.com/Perlten/MT-diagrams/master/config.schema.json",
+    "$schema": "https://raw.githubusercontent.com/Perlten/Architectural-Lens/master/config.schema.json",
     "name": "zeeguu", # Name of project
     "rootFolder": "zeeguu", # Name of source folder containing the root package (Usually a folder called src)
     "github": {
         "url": "https://github.com/zeeguu/api", # Link to project's Github
         "branch": "master" # Name of main/master branch of project
     },
     "saveLocation": "./diagrams/", # Location to store generated diagrams
@@ -98,16 +100,16 @@
             "ignorePackages": []
         }
     }
 }
 
 ```
 
-### You can render the views specified in your "mt-config.json" file by running the command:
-- `mt-diagrams render`
+### You can render the views specified in your "archlens.json" file by running the command:
+- `archlens render`
 
 This will generate the diagrams for all the views defined in your configuration file and save them in the location specified in the "saveLocation" field of your configuration.
 
 ## Further Filtering of packages
 
 If you find the core view to be too large, you can create a new view that further filters the packages. Instead of giving a path to the package "core", you can limit it further by specifying that you want to see "core" and only its sub-packages that are 1 layer down.
 
@@ -115,19 +117,19 @@
 
 For example, the following configuration file defines a view for the "core" package and its immediate sub-packages:
 
 ![Zeeguu core view](.github/readme/zeeguu-coreViewDepthFiltered.png)
 
 This will create a view that shows only the "core" package and its immediate sub-packages.
 
-Here is an example of the mt-config.json file used to generate the filtered view:
+Here is an example of the archlens.json file used to generate the filtered view:
 
 ```json
 {
-    "$schema": "https://raw.githubusercontent.com/Perlten/MT-diagrams/master/config.schema.json",
+    "$schema": "https://raw.githubusercontent.com/Perlten/Architectural-Lens/master/config.schema.json",
     "name": "zeeguu", 
     "rootFolder": "zeeguu", 
     "github": {
         "url": "https://github.com/zeeguu/api", 
         "branch": "master" 
     },
     "saveLocation": "./diagrams/", 
@@ -158,19 +160,19 @@
     "depth": 1
     }
  ]
 
 ```
 
 ## Arrows
-Each arrow in the system diagram represents a dependency between two packages, and the number on the arrow indicates the number of dependencies going in that direction. If you prefer not to see these arrows, you can use the optional "showDependencyCount" setting, which is a boolean. When set to "false", the dependency count will be hidden in all views. Here is an example of how to set this option in your mt-config.json file:
+Each arrow in the system diagram represents a dependency between two packages, and the number on the arrow indicates the number of dependencies going in that direction. If you prefer not to see these arrows, you can use the optional "showDependencyCount" setting, which is a boolean. When set to "false", the dependency count will be hidden in all views. Here is an example of how to set this option in your archlens.json file:
 
 ```json
 {
-    "$schema": "https://raw.githubusercontent.com/Perlten/MT-diagrams/master/config.schema.json",
+    "$schema": "https://raw.githubusercontent.com/Perlten/Architectural-Lens/master/config.schema.json",
     "name": "zeeguu", # Name of project
     "rootFolder": "zeeguu", # Name of source folder
     "github": {
         "url": "https://github.com/zeeguu/api", # Link to project's Github
         "branch": "master" # Name of main/master branch of project
     },
     "showDependencyCount": false, <------ here we remove the arrows.
@@ -190,19 +192,19 @@
 "api/test" #Removes the package api/test and all of its sub packages
 ]
 ```
 
 To clarify, the first method using an asterisk (*) will remove any package containing the specified keyword, while the second method will remove only the specified package and all of its sub-packages. This can be useful for cleaning up clutter in the diagram or for excluding certain packages that are not relevant to the analysis.
 
 ## The difference views
-To generate a difference view using MT-Diagrams, you need to be on a branch other than the one specified in the configuration file. Usually, you would compare your current branch with the main/master branch, but you have the flexibility to choose any branch you desire. For the following example, I have narrowed down the view by filtering out only the "core/model" package.
+To generate a difference view using Architectural-Lens, you need to be on a branch other than the one specified in the configuration file. Usually, you would compare your current branch with the main/master branch, but you have the flexibility to choose any branch you desire. For the following example, I have narrowed down the view by filtering out only the "core/model" package.
 
 ```json
 {
-    "$schema": "https://raw.githubusercontent.com/Perlten/MT-diagrams/master/config.schema.json",
+    "$schema": "https://raw.githubusercontent.com/Perlten/Architectural-Lens/master/config.schema.json",
     "name": "zeeguu", 
     "rootFolder": "zeeguu", 
     "github": {
         "url": "https://github.com/zeeguu/api", 
         "branch": "master" 
     },
     "saveLocation": "./diagrams/", 
@@ -216,23 +218,23 @@
     }
 }
 ```
 For the next example, the core view is further filtered to show only "core/model". Three changes were made in comparison to the main branch: the package "smart_watch" was deleted, a new package called "smart_watch_two" was added, and a dependency from "word_knowledge" to "model" was removed.
 
 To render this new view displaying the changes, a new command must be run:
 
-- `mt-diagrams render-diff`
+- `archlens render-diff`
 
 ![Zeeguu core view](.github/readme/zeeguu-modelViewdiffView.png)
 
 If there are no diffrences, a diagram without diffrences will still be generated.
 
 
 ## Github action - Pull request
 
 To display the difference views in your pull requests, run the command:
 
-- `mt-diagrams create-action`
+- `archlens create-action`
 
 This command generates the necessary files in the .github folder, creating it if it doesn't already exist. Once this is done, you can create a pull request, and the difference view will be visible to the reviewer, as shown in the image below. If there are no diffrences, a diagram without diffrences will still be generated.
 
 ![Zeeguu core view](.github/readme/zeeguu-modelViewDiffGithub.png)
```

### Comparing `Architectural Lens-0.0.2/setup.py` & `Architectural Lens-0.0.3/setup.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_packages
 
 setup(
     name="Architectural Lens",
-    version="0.0.2",
+    version="0.0.3",
     description="Thesis project",
     author="Nikolai Perlt",
     author_email="npe@itu.dk",
     url="https://github.com/Perlten/MT-diagrams",
     packages=find_packages(),
     long_description="This is the long description",
     install_requires=[
```

### Comparing `Architectural Lens-0.0.2/src/cli_interface.py` & `Architectural Lens-0.0.3/src/cli_interface.py`

 * *Files 4% similar despite different names*

```diff
@@ -3,27 +3,24 @@
 import os
 import requests
 import jsonschema
 import tempfile
 import shutil
 from pathlib import Path
 from src.utils.path_manager_singleton import PathManagerSingleton
-from src.utils.functions import verify_config_options
+
+# from src.utils.functions import verify_config_options
 from src.utils.config_manager_singleton import ConfigManagerSingleton
 
 from src.plantumlv2.pu_manager import render_pu, render_diff_pu
 
 from src.core.bt_graph import BTGraph
 
 from src.plantuml.fetch_git import fetch_git_repo
 
-from src.plantuml.plantuml_file_creator import (
-    plantuml_diagram_creator_sub_domains,
-)
-
 from astroid.manager import AstroidManager
 
 import astroid
 
 astroid.MANAGER = None
 
 app = typer.Typer(add_completion=True)
```

### Comparing `Architectural Lens-0.0.2/src/core/bt_file.py` & `Architectural Lens-0.0.3/src/core/bt_file.py`

 * *Files 8% similar despite different names*

```diff
@@ -61,15 +61,15 @@
                 return
 
             self.edge_to.append(other)
 
 
 def get_imported_modules(
     ast: astroid.Module, root_location: str, am: AstroidManager
-):
+) -> list:
     imported_modules = []
     for sub_node in ast.body:
         try:
             if isinstance(sub_node, astroid.node_classes.ImportFrom):
                 sub_node: astroid.node_classes.ImportFrom = sub_node
 
                 module_node = am.ast_from_module_name(
@@ -84,12 +84,16 @@
                         module_node = am.ast_from_module_name(
                             name,
                             context_file=root_location,
                         )
                         imported_modules.append(module_node)
                     except Exception:
                         continue
+            elif hasattr(sub_node, "body"):
+                imported_modules.extend(
+                    get_imported_modules(sub_node, root_location, am)
+                )
 
         except astroid.AstroidImportError:
             continue
 
     return imported_modules
```

### Comparing `Architectural Lens-0.0.2/src/core/bt_graph.py` & `Architectural Lens-0.0.3/src/core/bt_graph.py`

 * *Files identical despite different names*

### Comparing `Architectural Lens-0.0.2/src/core/bt_module.py` & `Architectural Lens-0.0.3/src/core/bt_module.py`

 * *Files identical despite different names*

### Comparing `Architectural Lens-0.0.2/src/plantuml/plantuml_file_creator.py` & `Architectural Lens-0.0.3/src/plantuml/plantuml_file_creator.py`

 * *Files identical despite different names*

### Comparing `Architectural Lens-0.0.2/src/plantumlv2/pu_entities.py` & `Architectural Lens-0.0.3/src/plantumlv2/pu_entities.py`

 * *Files identical despite different names*

### Comparing `Architectural Lens-0.0.2/src/plantumlv2/pu_manager.py` & `Architectural Lens-0.0.3/src/plantumlv2/pu_manager.py`

 * *Files 3% similar despite different names*

```diff
@@ -201,15 +201,21 @@
             if isinstance(package_view, str):
                 if package.path.startswith(filter_path.replace(".", "/")):
                     filtered_packages_set.add(package)
 
             if isinstance(package_view, dict):
                 filter_path = package_view["packagePath"].replace(".", "/")
                 view_depth = package_view["depth"]
-                if package.path == filter_path:
+                if filter_path == "" and package.parent_path == ".":
+                    filtered_packages_set.add(package)
+                    depth_filter_packages = _find_packages_with_depth(
+                        package, view_depth - 1, packages_map
+                    )
+                    filtered_packages_set.update(depth_filter_packages)
+                elif package.path == filter_path:
                     filtered_packages_set.add(package)
                     depth_filter_packages = _find_packages_with_depth(
                         package, view_depth, packages_map
                     )
                     filtered_packages_set.update(depth_filter_packages)
 
     if len(view["packages"]) == 0:
```

### Comparing `Architectural Lens-0.0.2/src/utils/functions.py` & `Architectural Lens-0.0.3/src/utils/functions.py`

 * *Files identical despite different names*

### Comparing `Architectural Lens-0.0.2/src/utils/path_manager_singleton.py` & `Architectural Lens-0.0.3/src/utils/path_manager_singleton.py`

 * *Files identical despite different names*

