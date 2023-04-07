# Comparing `tmp/yaml_setup-0.1.1.tar.gz` & `tmp/yaml_setup-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "yaml_setup-0.1.1.tar", max compression
+gzip compressed data, was "yaml_setup-0.1.2.tar", max compression
```

## Comparing `yaml_setup-0.1.1.tar` & `yaml_setup-0.1.2.tar`

### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0      510 2023-04-07 00:33:54.767379 yaml_setup-0.1.1/pyproject.toml
--rw-r--r--   0        0        0      442 2023-04-06 23:01:07.050946 yaml_setup-0.1.1/README.md
--rw-r--r--   0        0        0       54 2023-04-06 22:52:53.563226 yaml_setup-0.1.1/yamlup/__init__.py
--rw-r--r--   0        0        0       47 2023-04-06 18:42:56.979413 yaml_setup-0.1.1/yamlup/__main__.py
--rw-r--r--   0        0        0     3719 2023-04-07 00:32:35.956357 yaml_setup-0.1.1/yamlup/cli.py
--rw-r--r--   0        0        0    12489 2023-04-07 00:33:40.219551 yaml_setup-0.1.1/yamlup/schema.py
--rw-r--r--   0        0        0     1280 1970-01-01 00:00:00.000000 yaml_setup-0.1.1/setup.py
--rw-r--r--   0        0        0      933 1970-01-01 00:00:00.000000 yaml_setup-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0      510 2023-04-07 00:52:29.952367 yaml_setup-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0      442 2023-04-06 23:01:07.050946 yaml_setup-0.1.2/README.md
+-rw-r--r--   0        0        0       54 2023-04-06 22:52:53.563226 yaml_setup-0.1.2/yamlup/__init__.py
+-rw-r--r--   0        0        0       47 2023-04-06 18:42:56.979413 yaml_setup-0.1.2/yamlup/__main__.py
+-rw-r--r--   0        0        0     6075 2023-04-07 00:52:04.921575 yaml_setup-0.1.2/yamlup/cli.py
+-rw-r--r--   0        0        0    13458 2023-04-07 00:50:39.852392 yaml_setup-0.1.2/yamlup/schema.py
+-rw-r--r--   0        0        0     1280 1970-01-01 00:00:00.000000 yaml_setup-0.1.2/setup.py
+-rw-r--r--   0        0        0      933 1970-01-01 00:00:00.000000 yaml_setup-0.1.2/PKG-INFO
```

### Comparing `yaml_setup-0.1.1/yamlup/cli.py` & `yaml_setup-0.1.2/yamlup/cli.py`

 * *Files 21% similar despite different names*

```diff
@@ -123,7 +123,78 @@
         outfile = outfile or filepath.with_suffix('.md')
         outfile = Path(outfile)
         outfile.parent.mkdir(parents=True, exist_ok=True)
         outfile.with_suffix('.md').write_text(mdtext)
 
     else:
         cout.print(mdtext)
+
+
+
+@app.command(
+    "tasks",
+    help=f"Lists all tasks (high level setups) in the file given as argument",
+    no_args_is_help=True,
+)
+def tasks(
+    filepath: Path = typer.Argument(
+        ...,
+        help="The path to the file to upload.", 
+        exists=True,
+        file_okay=True,
+        dir_okay=False,
+        readable=True
+        ),
+    schema: Path = typer.Option(None, "--schema", "-s", help="Use your own schema."),
+    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode.")
+    ):
+    if schema:
+        cerr("❌ Not yet Implemented through CLI. Please use the python utils.")
+    setup = SetupFile(filepath)
+    cout.print(setup.tasks())
+
+@app.command(
+    "items",
+    help=f"Lists all items within a task (high level setups) in the file given as argument",
+    no_args_is_help=True,
+)
+def items(
+    filepath: Path = typer.Argument(
+        ...,
+        help="The path to the file to upload.", 
+        exists=True,
+        file_okay=True,
+        dir_okay=False,
+        readable=True
+        ),
+    task: str = typer.Argument(..., help="The high level task to check items (downloads) for."),
+    schema: Path = typer.Option(None, "--schema", "-s", help="Use your own schema."),
+    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode.")
+    ):
+    if schema:
+        cerr("❌ Not yet Implemented through CLI. Please use the python utils.")
+    setup = SetupFile(filepath)
+    cout.print(list(setup.task_items(task)))
+
+
+@app.command(
+    "order",
+    help=f"Lists the run order in which the file will execute each command block",
+    no_args_is_help=True,
+)
+def order(
+    filepath: Path = typer.Argument(
+        ...,
+        help="The path to the file to upload.", 
+        exists=True,
+        file_okay=True,
+        dir_okay=False,
+        readable=True
+        ),
+    task: str = typer.Argument(..., help="The high level task to check items (downloads) for."),
+    schema: Path = typer.Option(None, "--schema", "-s", help="Use your own schema."),
+    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode.")
+    ):
+    if schema:
+        cerr("❌ Not yet Implemented through CLI. Please use the python utils.")
+    setup = SetupFile(filepath)
+    cout.print(list(setup.run_order(task)))
```

### Comparing `yaml_setup-0.1.1/yamlup/schema.py` & `yaml_setup-0.1.2/yamlup/schema.py`

 * *Files 4% similar despite different names*

```diff
@@ -180,14 +180,41 @@
 
     def values(self):
         return self._data.values()
     
     def items(self):
         return self._data.items()
     
+    def tasks(self):
+        return list(self._data.keys())
+
+    def task_items_lazy(self, task:str):
+        if task in self._data:
+            tk = self._data[task]
+            for item in tk['items']:
+                yield {"name": item, **{k:v for k,v in tk['items'][item].items()}}
+        else:
+            yield {}
+
+    def task_items(self, task:str, lazy=False):
+        if lazy:
+            return self.task_items_lazy(task)
+        else:
+            return list(self.task_items_lazy(task))
+        
+    def run_order(self,task):
+        if task in self._data:
+            tk = self._data[task]
+            if 'run' in tk:
+                return tk['run']['steps']
+            else:
+                cerr.print(f'❓Error | [green]Task: {task} was found[/green] | [yellow] But no `run` list declared.', style="bold red")
+        else:
+            cerr.print(f'❌ Could not find task: [yellow]{task}[/yellow]', style="bold red")
+    
     def asArray(self, key):
         nestedArray = findAll(key, self._data)
         array = []
 
         for row in nestedArray:
             if isArray(row['value']):
                 base = {k: v if not isArray(v) else v.pop() for k,v in row.items() if k != 'value'}
```

### Comparing `yaml_setup-0.1.1/setup.py` & `yaml_setup-0.1.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 entry_points = \
 {'console_scripts': ['yaml-setup = yamlup.cli:app',
                      'yamlup = yamlup.cli:app',
                      'ymlsetup = yamlup.cli:app']}
 
 setup_kwargs = {
     'name': 'yaml-setup',
-    'version': '0.1.1',
+    'version': '0.1.2',
     'description': '',
     'long_description': "# YAML based Windows setup files with schema validation\n\nAs as example, consider this [README for a windows scoop-based setup](out.md).\n\nThis was produced entirely using this module's CLI from the [YAML setup file](tests/setup.yml).\n\nThe command you need is\n\n```shell\n\nyamlup render /path/to/setup.yml -o /path/to/README.md\n```\n\nThis module doesn't have any other aims besides setup schema validation and formatting its contents.",
     'author': 'arnos-stuff',
     'author_email': 'bcda0276@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `yaml_setup-0.1.1/PKG-INFO` & `yaml_setup-0.1.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: yaml-setup
-Version: 0.1.1
+Version: 0.1.2
 Summary: 
 Author: arnos-stuff
 Author-email: bcda0276@gmail.com
 Requires-Python: >=3.9,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
```

