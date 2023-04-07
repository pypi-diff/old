# Comparing `tmp/teller_cli-0.3.6.tar.gz` & `tmp/teller_cli-0.3.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "teller_cli-0.3.6.tar", max compression
+gzip compressed data, was "teller_cli-0.3.7.tar", max compression
```

## Comparing `teller_cli-0.3.6.tar` & `teller_cli-0.3.7.tar`

### file list

```diff
@@ -1,11 +1,11 @@
--rw-r--r--   0        0        0     1356 2023-04-02 06:28:41.263825 teller_cli-0.3.6/README.md
--rw-r--r--   0        0        0      534 2023-04-02 02:38:54.117223 teller_cli-0.3.6/pyproject.toml
--rw-r--r--   0        0        0     4907 2023-04-02 06:16:14.878486 teller_cli-0.3.6/teller_cli/__init__.py
--rw-r--r--   0        0        0       87 2023-03-10 04:52:35.334095 teller_cli-0.3.6/teller_cli/__main__.py
--rw-r--r--   0        0        0        0 2023-03-10 02:42:44.447116 teller_cli-0.3.6/teller_cli/core/__init__.py
--rw-r--r--   0        0        0     3459 2023-03-31 04:55:21.543518 teller_cli-0.3.6/teller_cli/core/config.py
--rw-r--r--   0        0        0      561 2023-04-02 06:16:14.851429 teller_cli-0.3.6/teller_cli/core/utils/__init__.py
--rw-r--r--   0        0        0    11751 2023-04-02 06:16:14.931707 teller_cli-0.3.6/teller_cli/core/world/__init__.py
--rw-r--r--   0        0        0     6418 2023-04-02 06:16:14.892794 teller_cli-0.3.6/teller_cli/core/world/download.py
--rw-r--r--   0        0        0     2338 1970-01-01 00:00:00.000000 teller_cli-0.3.6/setup.py
--rw-r--r--   0        0        0     1993 1970-01-01 00:00:00.000000 teller_cli-0.3.6/PKG-INFO
+-rw-r--r--   0        0        0     1356 2023-04-02 06:28:41.263825 teller_cli-0.3.7/README.md
+-rw-r--r--   0        0        0      562 2023-04-07 03:42:21.470753 teller_cli-0.3.7/pyproject.toml
+-rw-r--r--   0        0        0     4916 2023-04-05 15:28:25.306827 teller_cli-0.3.7/teller_cli/__init__.py
+-rw-r--r--   0        0        0       87 2023-03-10 04:52:35.334095 teller_cli-0.3.7/teller_cli/__main__.py
+-rw-r--r--   0        0        0        0 2023-03-10 02:42:44.447116 teller_cli-0.3.7/teller_cli/core/__init__.py
+-rw-r--r--   0        0        0     3459 2023-03-31 04:55:21.543518 teller_cli-0.3.7/teller_cli/core/config.py
+-rw-r--r--   0        0        0      561 2023-04-02 06:16:14.851429 teller_cli-0.3.7/teller_cli/core/utils/__init__.py
+-rw-r--r--   0        0        0    12730 2023-04-07 04:38:04.618943 teller_cli-0.3.7/teller_cli/core/world/__init__.py
+-rw-r--r--   0        0        0     6360 2023-04-07 08:52:01.716761 teller_cli-0.3.7/teller_cli/core/world/download.py
+-rw-r--r--   0        0        0     2373 1970-01-01 00:00:00.000000 teller_cli-0.3.7/setup.py
+-rw-r--r--   0        0        0     2092 1970-01-01 00:00:00.000000 teller_cli-0.3.7/PKG-INFO
```

### Comparing `teller_cli-0.3.6/README.md` & `teller_cli-0.3.7/README.md`

 * *Files identical despite different names*

### Comparing `teller_cli-0.3.6/pyproject.toml` & `teller_cli-0.3.7/pyproject.toml`

 * *Files 20% similar despite different names*

```diff
@@ -1,24 +1,25 @@
 [tool.poetry]
 name = "teller-cli"
-version = "0.3.6"
+version = "0.3.7"
 description = ""
 authors = ["JakePIXL <jakewjevans@gmail.com>"]
 readme = "README.md"
 packages = [{include = "teller_cli"}]
 
 [tool.poetry.dependencies]
-python = "^3.10"
+python = "^3.9"
 typer = {extras = ["all"], version = "^0.7.0"}
 httpx = "^0.23.3"
 keyring = "^23.13.1"
 nbtlib = "^2.0.4"
 nanoid = "^2.0.0"
 python-slugify = "^8.0.1"
 prompt-toolkit = "^3.0.38"
+nanoid-dictionary = "^2.4.0"
 
 [tool.poetry.scripts]
 teller-cli = "teller_cli:app"
 
 
 [build-system]
 requires = ["poetry-core"]
```

### Comparing `teller_cli-0.3.6/teller_cli/__init__.py` & `teller_cli-0.3.7/teller_cli/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -35,15 +35,18 @@
     if not os.path.isabs(folder_path):
         folder_path = os.path.join(default_saves_folder, folder_path)
 
     if not os.path.exists(folder_path):
         print("> [bold red]World does not exist.")
         raise Exception
 
-    _, _, _, vault_id = get_info(folder_path)
+    try:
+        _, _, _, vault_id = get_info(folder_path)
+    except Exception as e:
+        print(e)
 
     world_id = grab_world(api_token, api_url, vault_id)
 
     if not world_id:
         world_id = create_world(api_token, api_url, folder_path)
     try:
         zip_file = compress_folder(folder_path)
@@ -154,15 +157,14 @@
     replace: Union[bool, None] = typer.Option(default=False, help="Replaces old world"),
     save: Union[bool, None] = typer.Option(default=False, help="Saves downloaded zip"),
 ):
     api_url, api_token, default_saves_folder = create_or_load_config_file("teller.toml")
 
     final_save_path = save_path if save_path else default_saves_folder
 
-    # print("> [red bold]Not implemented yet.")
     item_id = browse_worlds(api_url, api_token)
 
     world_name, snapshot_id, file_name = download.from_owned(
         snapshot_id=item_id, url=api_url, token=api_token
     )
 
     print("> Extracting snapshot into saves folder")
@@ -178,8 +180,8 @@
     except Exception:
         print("> [bold red]Error downloading world.")
 
     if not save:
         os.remove(file_name)
 
 
-__version__ = "0.3.6"
+__version__ = "0.3.7"
```

### Comparing `teller_cli-0.3.6/teller_cli/core/config.py` & `teller_cli-0.3.7/teller_cli/core/config.py`

 * *Files identical despite different names*

### Comparing `teller_cli-0.3.6/teller_cli/core/utils/__init__.py` & `teller_cli-0.3.7/teller_cli/core/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `teller_cli-0.3.6/teller_cli/core/world/__init__.py` & `teller_cli-0.3.7/teller_cli/core/world/__init__.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,19 +1,24 @@
 import base64
 from datetime import datetime as dt
+import json
 import math
 import os
 import shutil
 import httpx
+from nanoid import generate
+from nanoid_dictionary import uppercase, numbers
 import nbtlib
 import zipfile
 
 from rich import print
 from rich.progress import Progress
-from slugify import slugify
+from rich.prompt import Confirm
+
+# from slugify import slugify
 from prompt_toolkit.shortcuts import radiolist_dialog
 
 from teller_cli.core.utils import format_bytes
 
 
 def chunk_and_upload(file_path: str, world_id: str, url: str, token: str):
     if not os.path.exists(file_path):
@@ -21,17 +26,25 @@
 
     client = httpx.Client()
 
     chunk_size = 4194304
 
     file_size = os.path.getsize(file_path)
 
-    file_name = os.path.basename(file_path)
+    if file_size >= 2147483648:
+        print("> [red bold]This world is greater than 2gb and should not be uploaded!")
+        cont_question = Confirm.ask("> Do you want to continue?")
+
+        if not cont_question:
+            print("> [red bold]Exitting.")
+            os.remove(file_path)
+            exit()
+        print("> [yellow]Your in for the long haul champ.")
 
-    # num_parts = math.ceil(file_size / chunk_size)
+    file_name = os.path.basename(file_path)
 
     snapshot_response = client.post(
         url=f"{url}/snapshots",
         json={"world_id": world_id, "size": file_size},
         headers={"X-Space-App-Key": token},
     )
 
@@ -102,14 +115,15 @@
                     print("> [bold orange]Request Failed: Part already reported.")
                     current_chunk += chunk_size
                     part += 1
                     continue
 
                 if not looped_response.status_code == 200:
                     print("> [bold red]Request Failed: Server error occured.")
+                    print(looped_response.text())
                     failed += 1
                     continue
 
                 current_chunk += chunk_size
                 part += 1
 
                 progress.update(
@@ -120,15 +134,15 @@
 
                 if current_chunk >= file_size:
                     finished = True
                     progress.update(upload_task, description="> [green]Finsihed.")
 
                     print("> [bold green]All parts uploaded.")
 
-        except Exception or KeyboardInterrupt as e:
+        except Exception as e:
             progress.update(upload_task, description="> [bold red]Failed.")
 
             if e == KeyboardInterrupt:
                 print("> [bold red]Canceled file upload, removing snapshot.")
             else:
                 print(e)
                 print("> [bold red]Upload failed removing snapshot.")
@@ -172,32 +186,34 @@
     print(f"> Found folder: [cyan]{folder_name}")
 
     print(f"> Compressing folder: [cyan]{folder_name}")
 
     # Create a zip file for the folder
     zip_filename = folder_name + ".zip"
 
-    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
-        # Add all files in the folder to the zip file
-        for root, dirs, files in os.walk(folder_path):
-            for file in files:
-                file_path = os.path.join(root, file)
-                zipf.write(file_path, os.path.relpath(file_path, folder_path))
+    try:
+        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
+            # Add all files in the folder to the zip file
+            for root, dirs, files in os.walk(folder_path):
+                for file in files:
+                    file_path = os.path.join(root, file)
+                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
+    except Exception:
+        try:
+            os.remove(zip_filename)
+        except Exception:
+            pass
 
     return zip_filename
 
 
 def encode_icon(world_path: str):
     icon_path = os.path.join(world_path, "icon.png")
 
     if not os.path.exists(icon_path):
-        # raise Exception
-        icon_path = "pack.png"
-
-    if not os.path.exists(icon_path):
         raise Exception
 
     # Read the contents of the PNG file into a bytes object
     with open(icon_path, "rb") as f:
         image_bytes = f.read()
 
     # Encode the image as Base64 using the standard Base64 alphabet and no line breaks
@@ -219,17 +235,31 @@
     seed = nbtlib.serialize_tag(world_data["Data"]["WorldGenSettings"]["seed"]).split(
         "L"
     )[0]
     difficulty = int(
         nbtlib.serialize_tag(world_data["Data"]["Difficulty"]).split("b")[0]
     ) + int(nbtlib.serialize_tag(world_data["Data"]["hardcore"]).split("b")[0])
 
-    vault_id = f"{seed}-{slugify(level_name, max_length=15)}"
+    if os.path.exists(os.path.join(world_path, ".chunkvault-lite")):
+        try:
+            with open(os.path.join(world_path, ".chunkvault-lite"), "r") as f:
+                json_data = json.loads(f.read())
+        except Exception:
+            raise Exception
+
+        vault_id = json_data["ID"]
 
-    # print(f"World Vault ID: {vault_id}")
+    else:
+        vault_id = generate(uppercase + numbers)
+
+        try:
+            with open(os.path.join(world_path, ".chunkvault-lite"), "w") as f:
+                f.write(json.dumps({"ID": vault_id}))
+        except Exception:
+            raise Exception
 
     return level_name, seed, difficulty, vault_id
 
 
 def get_deep_info(world_path: str):
     if not os.path.exists(world_path):
         print(f"> [bold red]Error finding world at: [cyan]'{world_path}'")
```

### Comparing `teller_cli-0.3.6/teller_cli/core/world/download.py` & `teller_cli-0.3.7/teller_cli/core/world/download.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 import math
 import os
 import httpx
 
 from rich import print
 from rich.progress import Progress
-import slugify
 from urllib.parse import urlparse
 
 
 def from_owned(snapshot_id: str, url: str, token: str):
     client = httpx.Client()
 
     print(f"> Grabbing snapshot: [cyan]{snapshot_id}")
@@ -209,8 +208,8 @@
             os.remove(filename)
 
         print("> [bold red]Please try again later.")
         exit()
 
     print("> World downloaded successfully.")
 
-    return world["name"], f"{world['seed']}-{slugify.slugify(world['name'])}", filename
+    return world["name"], world_id, filename
```

### Comparing `teller_cli-0.3.6/setup.py` & `teller_cli-0.3.7/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -9,35 +9,36 @@
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
 ['httpx>=0.23.3,<0.24.0',
  'keyring>=23.13.1,<24.0.0',
+ 'nanoid-dictionary>=2.4.0,<3.0.0',
  'nanoid>=2.0.0,<3.0.0',
  'nbtlib>=2.0.4,<3.0.0',
  'prompt-toolkit>=3.0.38,<4.0.0',
  'python-slugify>=8.0.1,<9.0.0',
  'typer[all]>=0.7.0,<0.8.0']
 
 entry_points = \
 {'console_scripts': ['teller-cli = teller_cli:app']}
 
 setup_kwargs = {
     'name': 'teller-cli',
-    'version': '0.3.6',
+    'version': '0.3.7',
     'description': '',
     'long_description': '# Teller-CLI for ChunkVault-Lite\n\nTeller-CLI is an open source Python/Typer-based CLI tool for uploading Minecraft world backups to ChunkVault-Lite, an open source backup solution provided by Valink Solutions.\n\n## Testing\n\nLimited testing was done on MacOS 13 and Windows 10\n\n## Usage\n\nTo use Teller-CLI, first install the tool:\n\n```bash\n    pip install teller-cli\n```\n\nThen, run the following command to create a snapshot:\n\n```bash\n    teller-cli upload "/path/to/world"\n```\n\nThis will upload the specified backup to ChunkVault-Lite.\n\n### First Launch\n\nOn first launch, Teller-CLI will prompt you to enter the API URL for your ChunkVault-Lite instance. The trailing slash is not necessary, so you can enter the URL without it.\n\nAfter entering the API URL, Teller-CLI will prompt you to enter your API token. You can obtain this token from your ChunkVault-Lite instance. This token is required for authentication purposes and allows Teller-CLI to access your backups.\n\nOnce you have entered the API URL and token, Teller-CLI will store this information locally for future use. You can update this information at any time by running the `teller-cli config` command.\n\n---\n\n## Additional Information\n\nChunkVault-Lite is hosted in a separatly. For more information on ChunkVault-Lite visit the [Repository](https://github.com/Valink-Solutions/ChunkVault-Lite)\n',
     'author': 'JakePIXL',
     'author_email': 'jakewjevans@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
     'packages': packages,
     'package_data': package_data,
     'install_requires': install_requires,
     'entry_points': entry_points,
-    'python_requires': '>=3.10,<4.0',
+    'python_requires': '>=3.9,<4.0',
 }
 
 
 setup(**setup_kwargs)
```

### Comparing `teller_cli-0.3.6/PKG-INFO` & `teller_cli-0.3.7/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,20 +1,22 @@
 Metadata-Version: 2.1
 Name: teller-cli
-Version: 0.3.6
+Version: 0.3.7
 Summary: 
 Author: JakePIXL
 Author-email: jakewjevans@gmail.com
-Requires-Python: >=3.10,<4.0
+Requires-Python: >=3.9,<4.0
 Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Requires-Dist: httpx (>=0.23.3,<0.24.0)
 Requires-Dist: keyring (>=23.13.1,<24.0.0)
 Requires-Dist: nanoid (>=2.0.0,<3.0.0)
+Requires-Dist: nanoid-dictionary (>=2.4.0,<3.0.0)
 Requires-Dist: nbtlib (>=2.0.4,<3.0.0)
 Requires-Dist: prompt-toolkit (>=3.0.38,<4.0.0)
 Requires-Dist: python-slugify (>=8.0.1,<9.0.0)
 Requires-Dist: typer[all] (>=0.7.0,<0.8.0)
 Description-Content-Type: text/markdown
 
 # Teller-CLI for ChunkVault-Lite
```

