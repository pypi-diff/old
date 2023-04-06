# Comparing `tmp/rkale-1.0.0.tar.gz` & `tmp/rkale-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rkale-1.0.0.tar", max compression
+gzip compressed data, was "rkale-1.0.1.tar", max compression
```

## Comparing `rkale-1.0.0.tar` & `rkale-1.0.1.tar`

### file list

```diff
@@ -1,11 +1,11 @@
--rw-r--r--   0        0        0     1371 2022-10-05 11:32:24.328587 rkale-1.0.0/README.md
--rw-r--r--   0        0        0      586 2022-10-05 11:32:46.936840 rkale-1.0.0/pyproject.toml
--rw-r--r--   0        0        0       22 2022-10-05 11:32:24.328587 rkale-1.0.0/rkale/__init__.py
--rw-r--r--   0        0        0     2354 2022-10-05 11:32:24.328587 rkale-1.0.0/rkale/config.py
--rw-r--r--   0        0        0      124 2022-10-05 11:32:24.328587 rkale-1.0.0/rkale/exceptions.py
--rw-r--r--   0        0        0     3352 2022-10-05 11:32:24.328587 rkale-1.0.0/rkale/operations.py
--rw-r--r--   0        0        0     1184 2022-10-05 11:32:24.328587 rkale-1.0.0/rkale/project_operations.py
--rw-r--r--   0        0        0     1658 2022-10-05 11:32:24.328587 rkale-1.0.0/rkale/rkale.py
--rw-r--r--   0        0        0     3852 2022-10-05 11:32:24.328587 rkale-1.0.0/rkale/utils.py
--rw-r--r--   0        0        0     2239 1970-01-01 00:00:00.000000 rkale-1.0.0/setup.py
--rw-r--r--   0        0        0     2100 1970-01-01 00:00:00.000000 rkale-1.0.0/PKG-INFO
+-rw-r--r--   0        0        0     1371 2023-04-06 13:22:40.831224 rkale-1.0.1/README.md
+-rw-r--r--   0        0        0      586 2023-04-06 13:23:05.498937 rkale-1.0.1/pyproject.toml
+-rw-r--r--   0        0        0       22 2023-04-06 13:22:40.831224 rkale-1.0.1/rkale/__init__.py
+-rw-r--r--   0        0        0     2354 2023-04-06 13:22:40.831224 rkale-1.0.1/rkale/config.py
+-rw-r--r--   0        0        0      124 2023-04-06 13:22:40.831224 rkale-1.0.1/rkale/exceptions.py
+-rw-r--r--   0        0        0     3352 2023-04-06 13:22:40.831224 rkale-1.0.1/rkale/operations.py
+-rw-r--r--   0        0        0     1184 2023-04-06 13:22:40.831224 rkale-1.0.1/rkale/project_operations.py
+-rw-r--r--   0        0        0     1658 2023-04-06 13:22:40.831224 rkale-1.0.1/rkale/rkale.py
+-rw-r--r--   0        0        0     3871 2023-04-06 13:22:40.831224 rkale-1.0.1/rkale/utils.py
+-rw-r--r--   0        0        0     2239 1970-01-01 00:00:00.000000 rkale-1.0.1/setup.py
+-rw-r--r--   0        0        0     2100 1970-01-01 00:00:00.000000 rkale-1.0.1/PKG-INFO
```

### Comparing `rkale-1.0.0/README.md` & `rkale-1.0.1/README.md`

 * *Files identical despite different names*

### Comparing `rkale-1.0.0/pyproject.toml` & `rkale-1.0.1/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "rkale"
-version = "v1.0.0"
+version = "v1.0.1"
 description = "Rclone wrapper to manage multiple datasets in a project"
 authors = ["nextml <joar@nextml.com>"]
 
 license = "MIT"
 
 readme = 'README.md'
```

### Comparing `rkale-1.0.0/rkale/config.py` & `rkale-1.0.1/rkale/config.py`

 * *Files identical despite different names*

### Comparing `rkale-1.0.0/rkale/operations.py` & `rkale-1.0.1/rkale/operations.py`

 * *Files identical despite different names*

### Comparing `rkale-1.0.0/rkale/project_operations.py` & `rkale-1.0.1/rkale/project_operations.py`

 * *Files identical despite different names*

### Comparing `rkale-1.0.0/rkale/rkale.py` & `rkale-1.0.1/rkale/rkale.py`

 * *Files identical despite different names*

### Comparing `rkale-1.0.0/rkale/utils.py` & `rkale-1.0.1/rkale/utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 import os
 import re
 import subprocess
 import tempfile
 from collections import namedtuple
 from contextlib import contextmanager
 
-from rkale.exceptions import DataRootError
 from tqdm import tqdm
 
+from rkale.exceptions import DataRootError
+
 
 def read(file_path):
     if os.path.exists(file_path):
         return open(file_path, "r").readlines()
     return []
 
 
@@ -111,15 +112,15 @@
     if progress:
         flags.append("--progress")
 
     command = " ".join(["rclone", command, source, destination, *flags])
     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
 
     if progress:
-        pbar = tqdm()
+        pbar = tqdm(desc="Downloading")
         while True:
             line = process.stdout.readline()
             if line:
                 line = line.decode("utf-8")
                 update = re.findall(
                     r"^Transferred.* ([0,1-9][0-9]*) / ([0,1-9][0-9]*)", line
                 )
```

### Comparing `rkale-1.0.0/setup.py` & `rkale-1.0.1/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 ['toml>=0.10.2,<0.11.0', 'tqdm>=4.60.0,<5.0.0']
 
 entry_points = \
 {'console_scripts': ['rkale = rkale.rkale:main']}
 
 setup_kwargs = {
     'name': 'rkale',
-    'version': '1.0.0',
+    'version': '1.0.1',
     'description': 'Rclone wrapper to manage multiple datasets in a project',
     'long_description': '# rkale\n\n## Install\n\nInstall rkale in your project using poetry:\n\n```bash\npoetry add rkale\n```\n\nUse pip if you want a global installation:\n\n```bash\npip install rkale\n```\n\n## Configuration\n\n### Global\n\n`~/.config/rkale/rkale.conf`:\n```toml\n[data]\nroot = "path to data folder where datasets are stored"\n\n[aliases]\nwasabi = "optional alias for remote in rclone.conf"\n\n[rclone] # global flags for rclone\nflags = ["--transfers 32", "--checkers 32"]\n```\n\nIf aliases are empty the remote name from the project config is used in the\nrclone lookup.\n\n### Project\nConfigure project datasets in the pyproject.toml file:\n\n`<project path>/pyproject.toml`:\n```toml\n[[tool.rkale.dataset]]\nname = "dataset_1"\nremote = "remote_1"\n\n[[tool.rkale.dataset]]\nname = "dataset_2"\nremote = "remote_2"\n```\n\nThe remote specified for the dataset must match a remote in the `rclone.conf`\nor an alias in the global rkale configuration.\n\n## Usage\n\n### Python interface\n\n```python\nfrom rkale.config import dataset_paths\n\n\ndef dataset_path():\n    return dataset_paths()["dataset_1"]\n```\n\n### Syncing datasets\n\nSyncs the local datasets to be identical to the remote\n\n```bash\nrkale psync\n```\n\nSyncs the remote datasets to be identical to the local\n\n```bash\nrkale psync --upstream\n```\n\nSame as rclone sync but checks differences first and asks for confirmation\n\n```bash\nrkale sync <source> <destination>\n```\n',
     'author': 'nextml',
     'author_email': 'joar@nextml.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://github.com/nextml-code/rkale',
```

### Comparing `rkale-1.0.0/PKG-INFO` & `rkale-1.0.1/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rkale
-Version: 1.0.0
+Version: 1.0.1
 Summary: Rclone wrapper to manage multiple datasets in a project
 Home-page: https://github.com/nextml-code/rkale
 License: MIT
 Author: nextml
 Author-email: joar@nextml.com
 Requires-Python: >=3.7,<4.0
 Classifier: License :: OSI Approved :: MIT License
```

