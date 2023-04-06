# Comparing `tmp/terka-1.2.0.tar.gz` & `tmp/terka-1.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "terka-1.2.0.tar", last modified: Wed Apr  5 21:38:33 2023, max compression
+gzip compressed data, was "terka-1.2.1.tar", last modified: Thu Apr  6 20:01:06 2023, max compression
```

## Comparing `terka-1.2.0.tar` & `terka-1.2.1.tar`

### file list

```diff
@@ -1,49 +1,50 @@
-drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-05 21:38:33.183880 terka-1.2.0/
--rw-r--r--   0 am        (1000) am        (1000)     1210 2023-04-05 21:38:33.183880 terka-1.2.0/PKG-INFO
--rw-r--r--   0 am        (1000) am        (1000)      917 2023-03-06 22:25:53.000000 terka-1.2.0/README.md
--rw-r--r--   0 am        (1000) am        (1000)       38 2023-04-05 21:38:33.183880 terka-1.2.0/setup.cfg
--rw-r--r--   0 am        (1000) am        (1000)      872 2023-04-05 14:06:56.000000 terka-1.2.0/setup.py
-drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-05 21:38:33.179880 terka-1.2.0/src/
--rw-r--r--   0 am        (1000) am        (1000)        0 2023-01-26 19:46:39.000000 terka-1.2.0/src/__init__.py
-drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-05 21:38:33.179880 terka-1.2.0/src/adapters/
--rw-r--r--   0 am        (1000) am        (1000)        0 2023-01-26 19:46:39.000000 terka-1.2.0/src/adapters/__init__.py
--rw-r--r--   0 am        (1000) am        (1000)     9878 2023-04-01 18:58:38.000000 terka-1.2.0/src/adapters/orm.py
--rw-r--r--   0 am        (1000) am        (1000)     6137 2023-03-11 22:07:24.000000 terka-1.2.0/src/adapters/repository.py
-drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-05 21:38:33.179880 terka-1.2.0/src/domain/
--rw-r--r--   0 am        (1000) am        (1000)        0 2023-01-26 19:46:39.000000 terka-1.2.0/src/domain/__init__.py
--rw-r--r--   0 am        (1000) am        (1000)      583 2023-03-07 21:56:12.000000 terka-1.2.0/src/domain/collaborators.py
--rw-r--r--   0 am        (1000) am        (1000)    31450 2023-04-05 14:29:18.000000 terka-1.2.0/src/domain/commands.py
--rw-r--r--   0 am        (1000) am        (1000)      827 2023-03-06 19:56:41.000000 terka-1.2.0/src/domain/commentary.py
--rw-r--r--   0 am        (1000) am        (1000)      102 2023-01-26 19:46:39.000000 terka-1.2.0/src/domain/element.py
--rw-r--r--   0 am        (1000) am        (1000)     1440 2023-03-12 20:44:34.000000 terka-1.2.0/src/domain/event_history.py
--rw-r--r--   0 am        (1000) am        (1000)      356 2023-01-29 21:37:09.000000 terka-1.2.0/src/domain/helpers.py
--rw-r--r--   0 am        (1000) am        (1000)      892 2023-03-17 11:37:47.000000 terka-1.2.0/src/domain/project.py
--rw-r--r--   0 am        (1000) am        (1000)     1805 2023-04-05 14:05:47.000000 terka-1.2.0/src/domain/sprint.py
--rw-r--r--   0 am        (1000) am        (1000)      635 2023-03-12 20:21:41.000000 terka-1.2.0/src/domain/tag.py
--rw-r--r--   0 am        (1000) am        (1000)     2039 2023-02-17 13:43:37.000000 terka-1.2.0/src/domain/task.py
--rw-r--r--   0 am        (1000) am        (1000)      792 2023-01-26 19:46:39.000000 terka-1.2.0/src/domain/user.py
-drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-05 21:38:33.179880 terka-1.2.0/src/entrypoints/
--rw-r--r--   0 am        (1000) am        (1000)        0 2023-02-11 17:56:56.000000 terka-1.2.0/src/entrypoints/__init__.py
--rw-r--r--   0 am        (1000) am        (1000)     3660 2023-04-01 18:44:17.000000 terka-1.2.0/src/entrypoints/cli.py
-drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-05 21:38:33.179880 terka-1.2.0/src/service_layer/
--rw-r--r--   0 am        (1000) am        (1000)        0 2023-01-26 19:46:39.000000 terka-1.2.0/src/service_layer/__init__.py
--rw-r--r--   0 am        (1000) am        (1000)    20884 2023-04-05 14:24:28.000000 terka-1.2.0/src/service_layer/printer.py
--rw-r--r--   0 am        (1000) am        (1000)     2283 2023-01-26 19:46:39.000000 terka-1.2.0/src/service_layer/services.py
--rw-r--r--   0 am        (1000) am        (1000)     3882 2023-02-12 14:00:44.000000 terka-1.2.0/src/service_layer/ui.py
--rw-r--r--   0 am        (1000) am        (1000)      698 2023-02-12 13:59:50.000000 terka-1.2.0/src/service_layer/vertical_layout.css
--rw-r--r--   0 am        (1000) am        (1000)     6584 2023-04-05 12:50:17.000000 terka-1.2.0/src/utils.py
-drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-05 21:38:33.183880 terka-1.2.0/terka.egg-info/
--rw-r--r--   0 am        (1000) am        (1000)     1210 2023-04-05 21:38:32.000000 terka-1.2.0/terka.egg-info/PKG-INFO
--rw-r--r--   0 am        (1000) am        (1000)      902 2023-04-05 21:38:33.000000 terka-1.2.0/terka.egg-info/SOURCES.txt
--rw-r--r--   0 am        (1000) am        (1000)        1 2023-04-05 21:38:32.000000 terka-1.2.0/terka.egg-info/dependency_links.txt
--rw-r--r--   0 am        (1000) am        (1000)       51 2023-04-05 21:38:32.000000 terka-1.2.0/terka.egg-info/entry_points.txt
--rw-r--r--   0 am        (1000) am        (1000)       37 2023-04-05 21:38:32.000000 terka-1.2.0/terka.egg-info/requires.txt
--rw-r--r--   0 am        (1000) am        (1000)       10 2023-04-05 21:38:32.000000 terka-1.2.0/terka.egg-info/top_level.txt
-drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-05 21:38:33.183880 terka-1.2.0/tests/
--rw-r--r--   0 am        (1000) am        (1000)        0 2023-01-26 19:46:39.000000 terka-1.2.0/tests/__init__.py
--rw-r--r--   0 am        (1000) am        (1000)      424 2023-01-26 19:46:39.000000 terka-1.2.0/tests/conftest.py
--rw-r--r--   0 am        (1000) am        (1000)       43 2023-01-26 19:46:39.000000 terka-1.2.0/tests/test_commands.py
--rw-r--r--   0 am        (1000) am        (1000)     2818 2023-01-26 19:46:39.000000 terka-1.2.0/tests/test_orm.py
--rw-r--r--   0 am        (1000) am        (1000)      956 2023-01-26 19:46:39.000000 terka-1.2.0/tests/test_task.py
--rw-r--r--   0 am        (1000) am        (1000)     1281 2023-01-26 19:46:39.000000 terka-1.2.0/tests/test_user.py
--rw-r--r--   0 am        (1000) am        (1000)      265 2023-01-26 19:46:39.000000 terka-1.2.0/tests/test_utils.py
+drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-06 20:01:06.577793 terka-1.2.1/
+-rw-r--r--   0 am        (1000) am        (1000)    11357 2023-04-05 21:39:45.000000 terka-1.2.1/LICENSE
+-rw-r--r--   0 am        (1000) am        (1000)     1232 2023-04-06 20:01:06.577793 terka-1.2.1/PKG-INFO
+-rw-r--r--   0 am        (1000) am        (1000)      917 2023-03-06 22:25:53.000000 terka-1.2.1/README.md
+-rw-r--r--   0 am        (1000) am        (1000)       38 2023-04-06 20:01:06.577793 terka-1.2.1/setup.cfg
+-rw-r--r--   0 am        (1000) am        (1000)      872 2023-04-06 20:00:38.000000 terka-1.2.1/setup.py
+drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-06 20:01:06.573793 terka-1.2.1/src/
+-rw-r--r--   0 am        (1000) am        (1000)        0 2023-01-26 19:46:39.000000 terka-1.2.1/src/__init__.py
+drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-06 20:01:06.573793 terka-1.2.1/src/adapters/
+-rw-r--r--   0 am        (1000) am        (1000)        0 2023-01-26 19:46:39.000000 terka-1.2.1/src/adapters/__init__.py
+-rw-r--r--   0 am        (1000) am        (1000)     9878 2023-04-01 18:58:38.000000 terka-1.2.1/src/adapters/orm.py
+-rw-r--r--   0 am        (1000) am        (1000)     6137 2023-03-11 22:07:24.000000 terka-1.2.1/src/adapters/repository.py
+drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-06 20:01:06.573793 terka-1.2.1/src/domain/
+-rw-r--r--   0 am        (1000) am        (1000)        0 2023-01-26 19:46:39.000000 terka-1.2.1/src/domain/__init__.py
+-rw-r--r--   0 am        (1000) am        (1000)      576 2023-04-06 18:49:11.000000 terka-1.2.1/src/domain/collaborators.py
+-rw-r--r--   0 am        (1000) am        (1000)    31450 2023-04-05 14:29:18.000000 terka-1.2.1/src/domain/commands.py
+-rw-r--r--   0 am        (1000) am        (1000)      827 2023-03-06 19:56:41.000000 terka-1.2.1/src/domain/commentary.py
+-rw-r--r--   0 am        (1000) am        (1000)      102 2023-01-26 19:46:39.000000 terka-1.2.1/src/domain/element.py
+-rw-r--r--   0 am        (1000) am        (1000)     1440 2023-03-12 20:44:34.000000 terka-1.2.1/src/domain/event_history.py
+-rw-r--r--   0 am        (1000) am        (1000)      356 2023-01-29 21:37:09.000000 terka-1.2.1/src/domain/helpers.py
+-rw-r--r--   0 am        (1000) am        (1000)      892 2023-03-17 11:37:47.000000 terka-1.2.1/src/domain/project.py
+-rw-r--r--   0 am        (1000) am        (1000)     1805 2023-04-05 14:05:47.000000 terka-1.2.1/src/domain/sprint.py
+-rw-r--r--   0 am        (1000) am        (1000)      639 2023-04-06 19:04:21.000000 terka-1.2.1/src/domain/tag.py
+-rw-r--r--   0 am        (1000) am        (1000)     2039 2023-02-17 13:43:37.000000 terka-1.2.1/src/domain/task.py
+-rw-r--r--   0 am        (1000) am        (1000)      792 2023-01-26 19:46:39.000000 terka-1.2.1/src/domain/user.py
+drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-06 20:01:06.573793 terka-1.2.1/src/entrypoints/
+-rw-r--r--   0 am        (1000) am        (1000)        0 2023-02-11 17:56:56.000000 terka-1.2.1/src/entrypoints/__init__.py
+-rw-r--r--   0 am        (1000) am        (1000)     3660 2023-04-01 18:44:17.000000 terka-1.2.1/src/entrypoints/cli.py
+drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-06 20:01:06.573793 terka-1.2.1/src/service_layer/
+-rw-r--r--   0 am        (1000) am        (1000)        0 2023-01-26 19:46:39.000000 terka-1.2.1/src/service_layer/__init__.py
+-rw-r--r--   0 am        (1000) am        (1000)    21166 2023-04-06 19:02:24.000000 terka-1.2.1/src/service_layer/printer.py
+-rw-r--r--   0 am        (1000) am        (1000)     2283 2023-01-26 19:46:39.000000 terka-1.2.1/src/service_layer/services.py
+-rw-r--r--   0 am        (1000) am        (1000)     3882 2023-02-12 14:00:44.000000 terka-1.2.1/src/service_layer/ui.py
+-rw-r--r--   0 am        (1000) am        (1000)      698 2023-02-12 13:59:50.000000 terka-1.2.1/src/service_layer/vertical_layout.css
+-rw-r--r--   0 am        (1000) am        (1000)     6584 2023-04-05 12:50:17.000000 terka-1.2.1/src/utils.py
+drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-06 20:01:06.577793 terka-1.2.1/terka.egg-info/
+-rw-r--r--   0 am        (1000) am        (1000)     1232 2023-04-06 20:01:06.000000 terka-1.2.1/terka.egg-info/PKG-INFO
+-rw-r--r--   0 am        (1000) am        (1000)      910 2023-04-06 20:01:06.000000 terka-1.2.1/terka.egg-info/SOURCES.txt
+-rw-r--r--   0 am        (1000) am        (1000)        1 2023-04-06 20:01:06.000000 terka-1.2.1/terka.egg-info/dependency_links.txt
+-rw-r--r--   0 am        (1000) am        (1000)       51 2023-04-06 20:01:06.000000 terka-1.2.1/terka.egg-info/entry_points.txt
+-rw-r--r--   0 am        (1000) am        (1000)       37 2023-04-06 20:01:06.000000 terka-1.2.1/terka.egg-info/requires.txt
+-rw-r--r--   0 am        (1000) am        (1000)       10 2023-04-06 20:01:06.000000 terka-1.2.1/terka.egg-info/top_level.txt
+drwxr-xr-x   0 am        (1000) am        (1000)        0 2023-04-06 20:01:06.577793 terka-1.2.1/tests/
+-rw-r--r--   0 am        (1000) am        (1000)        0 2023-01-26 19:46:39.000000 terka-1.2.1/tests/__init__.py
+-rw-r--r--   0 am        (1000) am        (1000)      424 2023-01-26 19:46:39.000000 terka-1.2.1/tests/conftest.py
+-rw-r--r--   0 am        (1000) am        (1000)       43 2023-01-26 19:46:39.000000 terka-1.2.1/tests/test_commands.py
+-rw-r--r--   0 am        (1000) am        (1000)     2818 2023-01-26 19:46:39.000000 terka-1.2.1/tests/test_orm.py
+-rw-r--r--   0 am        (1000) am        (1000)      956 2023-01-26 19:46:39.000000 terka-1.2.1/tests/test_task.py
+-rw-r--r--   0 am        (1000) am        (1000)     1281 2023-01-26 19:46:39.000000 terka-1.2.1/tests/test_user.py
+-rw-r--r--   0 am        (1000) am        (1000)      265 2023-01-26 19:46:39.000000 terka-1.2.1/tests/test_utils.py
```

### Comparing `terka-1.2.0/PKG-INFO` & `terka-1.2.1/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,16 +1,17 @@
 Metadata-Version: 2.1
 Name: terka
-Version: 1.2.0
+Version: 1.2.1
 Summary: CLI utility for creating and managing tasks in a terminal
 Home-page: https://github.com/AndreyMarkinPPC/terka
 Author: Andrei Markin
 Author-email: andrey.markin.ppc@gmail.com
 License: Apache 2.0
 Description-Content-Type: text/markdown
+License-File: LICENSE
 
 # Terka - Ter[minal] Ka[nban]
 
 `terka` (pronounced *tyorka* or *Тёрка*) is a CLI tool that helps you manage your tasks
 in the terminal. Create task, assign it to a project, update it status, write
 comments and many more!
```

### Comparing `terka-1.2.0/README.md` & `terka-1.2.1/README.md`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/setup.py` & `terka-1.2.1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 from setuptools import setup, find_packages
 
 HERE = pathlib.Path(__file__).parent
 README = (HERE / "README.md").read_text()
 
 setup(
     name="terka",
-    version="1.2.0",
+    version="1.2.1",
     description="CLI utility for creating and managing tasks in a terminal",
     long_description=README,
     long_description_content_type="text/markdown",
     author="Andrei Markin",
     author_email="andrey.markin.ppc@gmail.com",
     license="Apache 2.0",
     url="https://github.com/AndreyMarkinPPC/terka",
```

### Comparing `terka-1.2.0/src/adapters/orm.py` & `terka-1.2.1/src/adapters/orm.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/adapters/repository.py` & `terka-1.2.1/src/adapters/repository.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/domain/collaborators.py` & `terka-1.2.1/src/domain/collaborators.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 class CollaboratorMixin:
     def __repr__(self):
-        return f"<Collaborator> {self.id}"
+        return str(self.users.name)
 
 
 class TaskCollaborator(CollaboratorMixin):
 
     def __init__(self,
                  id: int,
                  collaborator_id: int,
```

### Comparing `terka-1.2.0/src/domain/commands.py` & `terka-1.2.1/src/domain/commands.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/domain/commentary.py` & `terka-1.2.1/src/domain/commentary.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/domain/event_history.py` & `terka-1.2.1/src/domain/event_history.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/domain/project.py` & `terka-1.2.1/src/domain/project.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/domain/sprint.py` & `terka-1.2.1/src/domain/sprint.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/domain/tag.py` & `terka-1.2.1/src/domain/tag.py`

 * *Files 19% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 
     def __repr__(self):
         return f"<Tag> {self.text}"
 
 
 class TagMixin:
     def __repr__(self):
-        return f"<Tag> {self.tag}"
+        return f"{self.base_tag.text}"
 
 
 class TaskTag(TagMixin):
 
     def __init__(self,
                  id: int,
                  tag_id: int,
```

### Comparing `terka-1.2.0/src/domain/task.py` & `terka-1.2.1/src/domain/task.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/domain/user.py` & `terka-1.2.1/src/domain/user.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/entrypoints/cli.py` & `terka-1.2.1/src/entrypoints/cli.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/service_layer/printer.py` & `terka-1.2.1/src/service_layer/printer.py`

 * *Files 0% similar despite different names*

```diff
@@ -16,16 +16,17 @@
     def __init__(self, box=rich.box.SIMPLE) -> None:
         self.box = box
         self.console = Console()
 
     def print_new_object(self, obj, project):
         table = Table(box=self.box)
         attributes = self._get_attributes(obj)
-        for column, _ in attributes:
-            table.add_column(column)
+        for column, value in attributes:
+            if value:
+                table.add_column(column)
         table.add_row(*list(zip(*attributes))[1])
         self.console.print(table)
 
     def print_history(self, entities):
         table = Table(box=self.box)
         print("History:")
         for column in ("date", "type", "old_value", "new_value"):
@@ -130,15 +131,18 @@
 
             for user, story_point in sorted(collaborators_dict.items(),
                                             key=lambda x: x[1],
                                             reverse=True):
                 collaborators.append(f"{user} ({story_point})")
 
             collaborators = ", ".join(collaborators)
-            open_tasks = [task for task in tasks if task.status.name not in ("DONE", "DELETED")]
+            open_tasks = [
+                task for task in tasks
+                if task.status.name not in ("DONE", "DELETED")
+            ]
             table.add_row(str(entity.id), str(entity.start_date),
                           str(entity.end_date), entity.goal,
                           entity.status.name, str(len(open_tasks)),
                           str(len(tasks)), str(sum(story_points)),
                           collaborators)
         self.console.print(table)
         if show_tasks:
@@ -432,18 +436,23 @@
             self.console.print(table)
 
     def _get_attributes(self, obj) -> List[Tuple[str, str]]:
         import inspect
         attributes = []
         for name, value in inspect.getmembers(obj):
             if not name.startswith("_") and not inspect.ismethod(value):
-                if hasattr(value, "name"):
+                if not value:
+                    continue
+                elif hasattr(value, "name"):
                     attributes.append((name, value.name))
                 elif isinstance(value, datetime):
                     attributes.append((name, value.strftime("%Y-%m-%d %H:%M")))
+                elif isinstance(value, set):
+                    values = value.pop()
+                    attributes.append((name, str(values)))
                 else:
                     attributes.append((name, str(value)))
         return attributes
 
     def _sort_open_tasks(self, entities):
         return len([
             task for task in entities.tasks
```

### Comparing `terka-1.2.0/src/service_layer/services.py` & `terka-1.2.1/src/service_layer/services.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/service_layer/ui.py` & `terka-1.2.1/src/service_layer/ui.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/service_layer/vertical_layout.css` & `terka-1.2.1/src/service_layer/vertical_layout.css`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/src/utils.py` & `terka-1.2.1/src/utils.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/terka.egg-info/PKG-INFO` & `terka-1.2.1/terka.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,16 +1,17 @@
 Metadata-Version: 2.1
 Name: terka
-Version: 1.2.0
+Version: 1.2.1
 Summary: CLI utility for creating and managing tasks in a terminal
 Home-page: https://github.com/AndreyMarkinPPC/terka
 Author: Andrei Markin
 Author-email: andrey.markin.ppc@gmail.com
 License: Apache 2.0
 Description-Content-Type: text/markdown
+License-File: LICENSE
 
 # Terka - Ter[minal] Ka[nban]
 
 `terka` (pronounced *tyorka* or *Тёрка*) is a CLI tool that helps you manage your tasks
 in the terminal. Create task, assign it to a project, update it status, write
 comments and many more!
```

### Comparing `terka-1.2.0/terka.egg-info/SOURCES.txt` & `terka-1.2.1/terka.egg-info/SOURCES.txt`

 * *Files 10% similar despite different names*

```diff
@@ -1,7 +1,8 @@
+LICENSE
 README.md
 setup.py
 src/__init__.py
 src/utils.py
 src/adapters/__init__.py
 src/adapters/orm.py
 src/adapters/repository.py
```

### Comparing `terka-1.2.0/tests/test_orm.py` & `terka-1.2.1/tests/test_orm.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/tests/test_task.py` & `terka-1.2.1/tests/test_task.py`

 * *Files identical despite different names*

### Comparing `terka-1.2.0/tests/test_user.py` & `terka-1.2.1/tests/test_user.py`

 * *Files identical despite different names*

