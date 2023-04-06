# Comparing `tmp/zoom-background-changer-0.1.1.tar.gz` & `tmp/zoom-background-changer-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "zoom-background-changer-0.1.1.tar", max compression
+gzip compressed data, was "zoom-background-changer-0.1.2.tar", max compression
```

## Comparing `zoom-background-changer-0.1.1.tar` & `zoom-background-changer-0.1.2.tar`

### file list

```diff
@@ -1,6 +1,6 @@
--rw-r--r--   0        0        0     1430 2023-04-06 16:01:27.083578 zoom-background-changer-0.1.1/README.md
--rw-r--r--   0        0        0      499 2023-04-06 16:01:35.004424 zoom-background-changer-0.1.1/pyproject.toml
--rw-r--r--   0        0        0        0 2023-04-06 14:56:06.480991 zoom-background-changer-0.1.1/zoom_background_changer/__init__.py
--rw-r--r--   0        0        0     2755 2023-04-06 15:49:32.674122 zoom-background-changer-0.1.1/zoom_background_changer/main.py
--rw-r--r--   0        0        0     2324 1970-01-01 00:00:00.000000 zoom-background-changer-0.1.1/setup.py
--rw-r--r--   0        0        0     1884 1970-01-01 00:00:00.000000 zoom-background-changer-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0     1398 2023-04-06 18:31:21.096992 zoom-background-changer-0.1.2/README.md
+-rw-r--r--   0        0        0      499 2023-04-06 18:35:36.656242 zoom-background-changer-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-04-06 14:56:06.480991 zoom-background-changer-0.1.2/zoom_background_changer/__init__.py
+-rw-r--r--   0        0        0     2755 2023-04-06 15:49:32.674122 zoom-background-changer-0.1.2/zoom_background_changer/main.py
+-rw-r--r--   0        0        0     2292 1970-01-01 00:00:00.000000 zoom-background-changer-0.1.2/setup.py
+-rw-r--r--   0        0        0     1852 1970-01-01 00:00:00.000000 zoom-background-changer-0.1.2/PKG-INFO
```

### Comparing `zoom-background-changer-0.1.1/README.md` & `zoom-background-changer-0.1.2/README.md`

 * *Files 19% similar despite different names*

```diff
@@ -19,31 +19,31 @@
 ```bash
 pip install zoom-background-changer
 ```
 
 ## Usage
 
 ```bash
-change-zoom-background
+zoom-background-changer
 ```
 
 ## Prompt Template
 
 Can be adjusted by creating a file called `.zoom-background-changer` in your `$HOME` directory.
 
 This file should contain the following:
 
 ```json
 {
-  "prompt_template": "Today is {date} and the weather is {weather} in {location}.",
-  "location": "Boston, MA"
+  "prompt": "Today is {date} and the weather is {weather} in {city}.",
+  "city": "Boston"
 }
 ```
 
 ### Available Variables
 
 - `{date}`: The current date
 - `{weather}`: The current weather, from `https://wttr.in/`
-- `{location}`: The current location, set from the `location` key in the `.zoom-background-changer` file. Defaults to `Boston, MA`.
+- `{city}`: The current city, set from the `city` key in the `.zoom-background-changer` file. Defaults to `Boston, MA`.
 - `{time}`: The current time
 
 If you would like to request other variables to be available, please open an issue!
```

### Comparing `zoom-background-changer-0.1.1/zoom_background_changer/main.py` & `zoom-background-changer-0.1.2/zoom_background_changer/main.py`

 * *Files identical despite different names*

### Comparing `zoom-background-changer-0.1.1/setup.py` & `zoom-background-changer-0.1.2/setup.py`

 * *Files 18% similar despite different names*

```diff
@@ -12,17 +12,17 @@
 
 entry_points = \
 {'console_scripts': ['zoom-background-changer = '
                      'zoom_background_changer.main:main']}
 
 setup_kwargs = {
     'name': 'zoom-background-changer',
-    'version': '0.1.1',
+    'version': '0.1.2',
     'description': 'Changes your Zoom background using OpenAI Image Generation.',
-    'long_description': '# Zoom Background Changer\n\nThis is a python script that will use OpenAI\'s GPT-3 API to generate a new background image for your Zoom meetings.\nIt can be run as a cron task, manually, or as part of a workflow when you open Zoom!\n\nThe script will generate a new background image based on the current date and weather, and overwrite you existing Zoom background.\n\n## Requirements\n\n- Only works on macOS (for now!)\n- Python 3.9+\n- OpenAI API Key\n  - You can get a free API key from OpenAI [here](https://platform.openai.com/).\n  - You will need to create an account and generate an API key.\n  - You will need to add your API key to the `OPENAI_API_KEY` environment variable.\n\n## Installation\n\n```bash\npip install zoom-background-changer\n```\n\n## Usage\n\n```bash\nchange-zoom-background\n```\n\n## Prompt Template\n\nCan be adjusted by creating a file called `.zoom-background-changer` in your `$HOME` directory.\n\nThis file should contain the following:\n\n```json\n{\n  "prompt_template": "Today is {date} and the weather is {weather} in {location}.",\n  "location": "Boston, MA"\n}\n```\n\n### Available Variables\n\n- `{date}`: The current date\n- `{weather}`: The current weather, from `https://wttr.in/`\n- `{location}`: The current location, set from the `location` key in the `.zoom-background-changer` file. Defaults to `Boston, MA`.\n- `{time}`: The current time\n\nIf you would like to request other variables to be available, please open an issue!\n',
+    'long_description': '# Zoom Background Changer\n\nThis is a python script that will use OpenAI\'s GPT-3 API to generate a new background image for your Zoom meetings.\nIt can be run as a cron task, manually, or as part of a workflow when you open Zoom!\n\nThe script will generate a new background image based on the current date and weather, and overwrite you existing Zoom background.\n\n## Requirements\n\n- Only works on macOS (for now!)\n- Python 3.9+\n- OpenAI API Key\n  - You can get a free API key from OpenAI [here](https://platform.openai.com/).\n  - You will need to create an account and generate an API key.\n  - You will need to add your API key to the `OPENAI_API_KEY` environment variable.\n\n## Installation\n\n```bash\npip install zoom-background-changer\n```\n\n## Usage\n\n```bash\nzoom-background-changer\n```\n\n## Prompt Template\n\nCan be adjusted by creating a file called `.zoom-background-changer` in your `$HOME` directory.\n\nThis file should contain the following:\n\n```json\n{\n  "prompt": "Today is {date} and the weather is {weather} in {city}.",\n  "city": "Boston"\n}\n```\n\n### Available Variables\n\n- `{date}`: The current date\n- `{weather}`: The current weather, from `https://wttr.in/`\n- `{city}`: The current city, set from the `city` key in the `.zoom-background-changer` file. Defaults to `Boston, MA`.\n- `{time}`: The current time\n\nIf you would like to request other variables to be available, please open an issue!\n',
     'author': 'Kyle Montag',
     'author_email': 'thekylemontag@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
     'packages': packages,
     'package_data': package_data,
```

### Comparing `zoom-background-changer-0.1.1/PKG-INFO` & `zoom-background-changer-0.1.2/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: zoom-background-changer
-Version: 0.1.1
+Version: 0.1.2
 Summary: Changes your Zoom background using OpenAI Image Generation.
 Author: Kyle Montag
 Author-email: thekylemontag@gmail.com
 Requires-Python: >=3.9,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -32,32 +32,32 @@
 ```bash
 pip install zoom-background-changer
 ```
 
 ## Usage
 
 ```bash
-change-zoom-background
+zoom-background-changer
 ```
 
 ## Prompt Template
 
 Can be adjusted by creating a file called `.zoom-background-changer` in your `$HOME` directory.
 
 This file should contain the following:
 
 ```json
 {
-  "prompt_template": "Today is {date} and the weather is {weather} in {location}.",
-  "location": "Boston, MA"
+  "prompt": "Today is {date} and the weather is {weather} in {city}.",
+  "city": "Boston"
 }
 ```
 
 ### Available Variables
 
 - `{date}`: The current date
 - `{weather}`: The current weather, from `https://wttr.in/`
-- `{location}`: The current location, set from the `location` key in the `.zoom-background-changer` file. Defaults to `Boston, MA`.
+- `{city}`: The current city, set from the `city` key in the `.zoom-background-changer` file. Defaults to `Boston, MA`.
 - `{time}`: The current time
 
 If you would like to request other variables to be available, please open an issue!
```

