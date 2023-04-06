# Comparing `tmp/activetune-0.0.3.tar.gz` & `tmp/activetune-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "activetune-0.0.3.tar", last modified: Mon Mar 27 14:29:28 2023, max compression
+gzip compressed data, was "activetune-0.0.5.tar", last modified: Thu Apr  6 14:43:46 2023, max compression
```

## Comparing `activetune-0.0.3.tar` & `activetune-0.0.5.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxrwxrwx   0        0        0        0 2023-03-27 14:29:28.776589 activetune-0.0.3/
--rw-rw-rw-   0        0        0       89 2023-03-27 14:29:28.766778 activetune-0.0.3/PKG-INFO
--rw-rw-rw-   0        0        0      969 2023-03-24 12:36:44.000000 activetune-0.0.3/README.md
-drwxrwxrwx   0        0        0        0 2023-03-27 14:29:28.766778 activetune-0.0.3/activetune/
--rw-rw-rw-   0        0        0       47 2023-03-27 12:13:54.000000 activetune-0.0.3/activetune/__init__.py
--rw-rw-rw-   0        0        0     2768 2023-03-27 12:13:45.000000 activetune-0.0.3/activetune/api.py
-drwxrwxrwx   0        0        0        0 2023-03-27 14:29:28.766778 activetune-0.0.3/activetune.egg-info/
--rw-rw-rw-   0        0        0       89 2023-03-27 14:29:28.000000 activetune-0.0.3/activetune.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      261 2023-03-27 14:29:28.000000 activetune-0.0.3/activetune.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-27 14:29:28.000000 activetune-0.0.3/activetune.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2023-03-20 12:09:14.000000 activetune-0.0.3/activetune.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0        9 2023-03-27 14:29:28.000000 activetune-0.0.3/activetune.egg-info/requires.txt
--rw-rw-rw-   0        0        0       11 2023-03-27 14:29:28.000000 activetune-0.0.3/activetune.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-03-27 14:29:28.776589 activetune-0.0.3/setup.cfg
--rw-rw-rw-   0        0        0      350 2023-03-27 12:14:00.000000 activetune-0.0.3/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:43:46.932307 activetune-0.0.5/
+-rw-rw-rw-   0        0        0       89 2023-04-06 14:43:46.931246 activetune-0.0.5/PKG-INFO
+-rw-rw-rw-   0        0        0      969 2023-03-24 12:36:44.000000 activetune-0.0.5/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 14:43:46.913271 activetune-0.0.5/activetune/
+-rw-rw-rw-   0        0        0       47 2023-04-06 14:42:31.000000 activetune-0.0.5/activetune/__init__.py
+-rw-rw-rw-   0        0        0     2764 2023-04-06 14:42:06.000000 activetune-0.0.5/activetune/api.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:43:46.930326 activetune-0.0.5/activetune.egg-info/
+-rw-rw-rw-   0        0        0       89 2023-04-06 14:43:46.000000 activetune-0.0.5/activetune.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      261 2023-04-06 14:43:46.000000 activetune-0.0.5/activetune.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 14:43:46.000000 activetune-0.0.5/activetune.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2023-03-20 12:09:14.000000 activetune-0.0.5/activetune.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0        9 2023-04-06 14:43:46.000000 activetune-0.0.5/activetune.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       11 2023-04-06 14:43:46.000000 activetune-0.0.5/activetune.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 14:43:46.932307 activetune-0.0.5/setup.cfg
+-rw-rw-rw-   0        0        0      350 2023-04-06 14:42:36.000000 activetune-0.0.5/setup.py
```

### Comparing `activetune-0.0.3/README.md` & `activetune-0.0.5/README.md`

 * *Files identical despite different names*

### Comparing `activetune-0.0.3/activetune/api.py` & `activetune-0.0.5/activetune/api.py`

 * *Files 5% similar despite different names*

```diff
@@ -16,15 +16,15 @@
             self.url + "/api/set_openai_key", {"token": self.token, "key": key}
         ).json()
 
     def create_dataset(self, name: str, description: str = ""):
         return requests.get(
             self.url + "/api/create_dataset",
             {"token": self.token, "name": name, "description": description},
-        ).json()
+        ).text
 
     def list_datasets(self):
         return requests.get(
             self.url + "/api/get_datasets", {"token": self.token}
         ).json()
 
     def add_sample(
@@ -45,15 +45,15 @@
                 "input": input,
                 "model_output": model_output,
                 "model_id": model_id,
                 "expected_output": expected_output,
                 "feedback": feedback,
                 "meta": json.dumps(meta),
             },
-        ).json()
+        ).text
 
     def get_data(self, dataset_id: str):
         return requests.get(
             self.url + "/api/get_data", {"token": self.token, "dataset_id": dataset_id}
         ).json()
 
     def set_feedback(self, sample_id: str, value: int):
```

