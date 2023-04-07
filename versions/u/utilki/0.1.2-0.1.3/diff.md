# Comparing `tmp/utilki-0.1.2.tar.gz` & `tmp/utilki-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "utilki-0.1.2.tar", max compression
+gzip compressed data, was "utilki-0.1.3.tar", max compression
```

## Comparing `utilki-0.1.2.tar` & `utilki-0.1.3.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0      859 2023-04-07 09:22:40.435495 utilki-0.1.2/README.md
--rw-r--r--   0        0        0      511 2023-04-07 09:30:50.493727 utilki-0.1.2/pyproject.toml
--rw-r--r--   0        0        0       73 2023-04-06 19:12:02.029197 utilki-0.1.2/utilki/__init__.py
--rw-r--r--   0        0        0     2196 2023-04-07 09:24:46.978148 utilki-0.1.2/utilki/cli.py
--rw-r--r--   0        0        0     2148 2023-04-07 09:04:04.272868 utilki-0.1.2/utilki/task_mixin.py
--rw-r--r--   0        0        0     1614 2023-04-07 09:33:11.828525 utilki-0.1.2/setup.py
--rw-r--r--   0        0        0     1263 2023-04-07 09:33:11.828776 utilki-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0      921 2023-04-07 09:39:03.009675 utilki-0.1.3/README.md
+-rw-r--r--   0        0        0      511 2023-04-07 13:49:12.445773 utilki-0.1.3/pyproject.toml
+-rw-r--r--   0        0        0       73 2023-04-06 19:12:02.029197 utilki-0.1.3/utilki/__init__.py
+-rw-r--r--   0        0        0     2168 2023-04-07 09:37:49.369962 utilki-0.1.3/utilki/cli.py
+-rw-r--r--   0        0        0     2853 2023-04-07 13:46:41.063717 utilki-0.1.3/utilki/task_mixin.py
+-rw-r--r--   0        0        0     1676 2023-04-07 13:49:41.962742 utilki-0.1.3/setup.py
+-rw-r--r--   0        0        0     1325 2023-04-07 13:49:41.963016 utilki-0.1.3/PKG-INFO
```

### Comparing `utilki-0.1.2/README.md` & `utilki-0.1.3/README.md`

 * *Files 12% similar despite different names*

```diff
@@ -8,16 +8,14 @@
 pip install utilki
 ```
 
 ## TaskMixin
 
 Mixin class that adds `create()` classmethod to dataclass you define as your task params. Useful when you have a lot of container based tasks executed on remote clusters (e.g. Kubernetes, Hashicorp Nomad, etc.). It reads task params from environment variables, parses, and validates them. 
 
-Note: requires you 
-
 ```python
 from utilki import TaskMixin
 
 @dataclass
 class Task(TaskMixin):
     ayy: float = 69.69
     lmao: str = "420"
@@ -33,9 +31,11 @@
 ```
 
 ## Cli
 
 ### Venv
 
 ```bash
-utilki venv 3.8.10
+$ utilki venv 3.8.10
+$ Enter venv name: new_venv
+$ Created venv `new_venv` with Python version 3.8.10
 ```
```

### Comparing `utilki-0.1.2/utilki/cli.py` & `utilki-0.1.3/utilki/cli.py`

 * *Files 4% similar despite different names*

```diff
@@ -62,13 +62,13 @@
                     text=True,
                 )
                 if res.returncode != 0:
                     click.echo(res.stderr)
                     return
 
     click.echo(
-        f"Successfully created virtual environment `{venv_name}` with Python version {python_version}"
+        f"Created venv `{venv_name}` with Python version {python_version}"
     )
 
 
 if __name__ == "__main__":
     cli()
```

### Comparing `utilki-0.1.2/utilki/task_mixin.py` & `utilki-0.1.3/utilki/task_mixin.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,9 +1,11 @@
 from datetime import datetime
+import inspect
 import os
+import typing
 
 
 class TaskMixin:
     @classmethod
     def create(cls):
         params = [
             (param.name, param.type)
@@ -24,39 +26,55 @@
         else:
             raise TypeError("Invalid datetime format")
 
     @classmethod
     def parse(cls, param_name, param_type):
         param = os.getenv(param_name, cls.get_default(param_name))
         print(param, param_type, param_name)
-        if issubclass(param_type, datetime):
-            if isinstance(param, datetime):
-                return param
-            elif isinstance(param, str):
-                has_t_or_colon = ":" in param or "T" in param
-                num_parts = len(param.split("-"))
-                if has_t_or_colon:
-                    param = param.replace(" ", "-")
-                    param = param.replace("T", "-")
-                    param = param.replace(":", "-")
-                    return cls.get_date(param)
-                elif num_parts == 3:
-                    return cls.get_date(param)
+        if inspect.isclass(param_type):
+            print("isclass")
+            if issubclass(param_type, datetime):
+                if isinstance(param, datetime):
+                    return param
+                elif isinstance(param, str):
+                    has_t_or_colon = ":" in param or "T" in param
+                    num_parts = len(param.split("-"))
+                    if has_t_or_colon:
+                        param = param.replace(" ", "-")
+                        param = param.replace("T", "-")
+                        param = param.replace(":", "-")
+                        return cls.get_date(param)
+                    elif num_parts == 3:
+                        return cls.get_date(param)
+                    else:
+                        raise TypeError("Invalid datetime format")
                 else:
-                    raise TypeError("Invalid datetime format")
+                    raise TypeError("Invalid default value")
+            elif issubclass(param_type, bool):
+                return parse_bool(param)
+            elif issubclass(param_type, int):
+                return int(param)
+            elif issubclass(param_type, float):
+                return float(param)
+            elif issubclass(param_type, str):
+                return str(param)
             else:
-                raise TypeError("Invalid default value")
-        elif issubclass(param_type, bool):
-            if param in ["True", "true", True]:
-                return True
-            elif param in ["False", "false", False]:
-                return False
-            else:
-                raise TypeError("Invalid boolean format")
-        elif issubclass(param_type, int):
-            return int(param)
-        elif issubclass(param_type, float):
-            return float(param)
-        elif issubclass(param_type, str):
-            return str(param)
+                raise TypeError("Invalid type")
         else:
-            raise TypeError("Invalid type")
+            print("not isclass")
+            if param_type == typing.Tuple[int]:
+                return tuple(map(int, param.split(",")))
+            elif param_type == typing.Tuple[str]:
+                return tuple(map(str, param.split(",")))
+            elif param_type == typing.Tuple[float]:
+                return tuple(map(float, param.split(",")))
+            elif param_type == typing.Tuple[bool]:
+                return tuple(map(parse_bool, param.split(",")))
+
+
+def parse_bool(param):
+    if param in ["True", "true", True]:
+        return True
+    elif param in ["False", "false", False]:
+        return False
+    else:
+        raise TypeError("Invalid boolean format")
```

### Comparing `utilki-0.1.2/setup.py` & `utilki-0.1.3/setup.py`

 * *Files 14% similar despite different names*

```diff
@@ -11,17 +11,17 @@
 ['click>=8.1.3,<9.0.0']
 
 entry_points = \
 {'console_scripts': ['utilki = utilki.cli:cli']}
 
 setup_kwargs = {
     'name': 'utilki',
-    'version': '0.1.2',
+    'version': '0.1.3',
     'description': 'A collection of useful utilities',
-    'long_description': '# utilki\n\nutils that are frequently used by me and might be useful for others\n\n## installation\n\n```bash\npip install utilki\n```\n\n## TaskMixin\n\nMixin class that adds `create()` classmethod to dataclass you define as your task params. Useful when you have a lot of container based tasks executed on remote clusters (e.g. Kubernetes, Hashicorp Nomad, etc.). It reads task params from environment variables, parses, and validates them. \n\nNote: requires you \n\n```python\nfrom utilki import TaskMixin\n\n@dataclass\nclass Task(TaskMixin):\n    ayy: float = 69.69\n    lmao: str = "420"\n\nos.environ["ayy"] = "42.42"\nos.environ["lmao"] = "69"\n\nt = Task.create()\nprint(f"ayy: {t.ayy}, type: {type(t.ayy)}")\n# ayy: 42.42, type: <class \'float\'>\nprint(f"lmao: {t.lmao}, type: {type(t.lmao)}")\n# lmao: 69, type: <class \'str\'>\n```\n\n## Cli\n\n### Venv\n\n```bash\nutilki venv 3.8.10\n```',
+    'long_description': '# utilki\n\nutils that are frequently used by me and might be useful for others\n\n## installation\n\n```bash\npip install utilki\n```\n\n## TaskMixin\n\nMixin class that adds `create()` classmethod to dataclass you define as your task params. Useful when you have a lot of container based tasks executed on remote clusters (e.g. Kubernetes, Hashicorp Nomad, etc.). It reads task params from environment variables, parses, and validates them. \n\n```python\nfrom utilki import TaskMixin\n\n@dataclass\nclass Task(TaskMixin):\n    ayy: float = 69.69\n    lmao: str = "420"\n\nos.environ["ayy"] = "42.42"\nos.environ["lmao"] = "69"\n\nt = Task.create()\nprint(f"ayy: {t.ayy}, type: {type(t.ayy)}")\n# ayy: 42.42, type: <class \'float\'>\nprint(f"lmao: {t.lmao}, type: {type(t.lmao)}")\n# lmao: 69, type: <class \'str\'>\n```\n\n## Cli\n\n### Venv\n\n```bash\n$ utilki venv 3.8.10\n$ Enter venv name: new_venv\n$ Created venv `new_venv` with Python version 3.8.10\n```',
     'author': 'Khaidar Bikmaev',
     'author_email': 'khaidar@bikmaev.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': None,
     'packages': packages,
     'package_data': package_data,
```

### Comparing `utilki-0.1.2/PKG-INFO` & `utilki-0.1.3/PKG-INFO`

 * *Files 26% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: utilki
-Version: 0.1.2
+Version: 0.1.3
 Summary: A collection of useful utilities
 Author: Khaidar Bikmaev
 Author-email: khaidar@bikmaev.com
 Requires-Python: >=3.8.1
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.9
@@ -21,16 +21,14 @@
 pip install utilki
 ```
 
 ## TaskMixin
 
 Mixin class that adds `create()` classmethod to dataclass you define as your task params. Useful when you have a lot of container based tasks executed on remote clusters (e.g. Kubernetes, Hashicorp Nomad, etc.). It reads task params from environment variables, parses, and validates them. 
 
-Note: requires you 
-
 ```python
 from utilki import TaskMixin
 
 @dataclass
 class Task(TaskMixin):
     ayy: float = 69.69
     lmao: str = "420"
@@ -46,9 +44,11 @@
 ```
 
 ## Cli
 
 ### Venv
 
 ```bash
-utilki venv 3.8.10
+$ utilki venv 3.8.10
+$ Enter venv name: new_venv
+$ Created venv `new_venv` with Python version 3.8.10
 ```
```

