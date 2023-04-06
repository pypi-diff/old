# Comparing `tmp/rewards-0.0.3.tar.gz` & `tmp/rewards-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rewards-0.0.3.tar", max compression
+gzip compressed data, was "rewards-0.0.4.tar", max compression
```

## Comparing `rewards-0.0.3.tar` & `rewards-0.0.4.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0    15251 2023-04-06 14:35:37.598050 rewards-0.0.3/README.md
--rw-r--r--   0        0        0      457 2023-04-06 15:32:20.035234 rewards-0.0.3/pyproject.toml
--rw-r--r--   0        0        0        5 2023-04-06 14:48:16.966876 rewards-0.0.3/rewards/VERSION
--rw-r--r--   0        0        0      247 2023-04-06 14:35:37.602050 rewards-0.0.3/rewards/__init__.py
--rw-r--r--   0        0        0     3867 2023-04-01 03:47:55.173271 rewards-0.0.3/rewards/agent.py
--rw-r--r--   0        0        0       18 2023-04-06 14:35:37.602050 rewards-0.0.3/rewards/assets/CarRace/__init__.py
--rw-r--r--   0        0        0    79384 2023-03-31 17:19:59.957981 rewards-0.0.3/rewards/assets/CarRace/car.png
--rw-r--r--   0        0        0    60297 2023-04-06 14:35:37.602050 rewards-0.0.3/rewards/assets/CarRace/track-1.png
--rw-r--r--   0        0        0    42293 2023-04-06 14:35:37.602050 rewards-0.0.3/rewards/assets/CarRace/track-2.png
--rw-r--r--   0        0        0    49467 2023-04-06 14:35:37.602050 rewards-0.0.3/rewards/assets/CarRace/track-3.png
--rw-r--r--   0        0        0       18 2023-04-06 14:35:37.602050 rewards-0.0.3/rewards/assets/__init__.py
--rw-r--r--   0        0        0        0 2023-04-02 06:50:32.365576 rewards-0.0.3/rewards/envs/__init__.py
--rw-r--r--   0        0        0    15306 2023-04-06 14:35:37.602050 rewards-0.0.3/rewards/envs/car.py
--rw-r--r--   0        0        0     2634 2023-04-01 03:47:55.173271 rewards-0.0.3/rewards/models.py
--rw-r--r--   0        0        0     5936 2023-04-06 14:35:37.602050 rewards-0.0.3/rewards/trainer.py
--rw-r--r--   0        0        0     6080 2023-04-06 15:31:41.366968 rewards-0.0.3/rewards/workflow.py
--rw-r--r--   0        0        0    15940 1970-01-01 00:00:00.000000 rewards-0.0.3/PKG-INFO
+-rw-r--r--   0        0        0    15251 2023-04-06 14:35:37.598050 rewards-0.0.4/README.md
+-rw-r--r--   0        0        0      457 2023-04-06 15:42:44.330493 rewards-0.0.4/pyproject.toml
+-rw-r--r--   0        0        0        5 2023-04-06 15:42:38.058461 rewards-0.0.4/rewards/VERSION
+-rw-r--r--   0        0        0      247 2023-04-06 14:35:37.602050 rewards-0.0.4/rewards/__init__.py
+-rw-r--r--   0        0        0     3867 2023-04-01 03:47:55.173271 rewards-0.0.4/rewards/agent.py
+-rw-r--r--   0        0        0       18 2023-04-06 14:35:37.602050 rewards-0.0.4/rewards/assets/CarRace/__init__.py
+-rw-r--r--   0        0        0    79384 2023-03-31 17:19:59.957981 rewards-0.0.4/rewards/assets/CarRace/car.png
+-rw-r--r--   0        0        0    60297 2023-04-06 14:35:37.602050 rewards-0.0.4/rewards/assets/CarRace/track-1.png
+-rw-r--r--   0        0        0    42293 2023-04-06 14:35:37.602050 rewards-0.0.4/rewards/assets/CarRace/track-2.png
+-rw-r--r--   0        0        0    49467 2023-04-06 14:35:37.602050 rewards-0.0.4/rewards/assets/CarRace/track-3.png
+-rw-r--r--   0        0        0       18 2023-04-06 14:35:37.602050 rewards-0.0.4/rewards/assets/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-02 06:50:32.365576 rewards-0.0.4/rewards/envs/__init__.py
+-rw-r--r--   0        0        0    15306 2023-04-06 14:35:37.602050 rewards-0.0.4/rewards/envs/car.py
+-rw-r--r--   0        0        0     2634 2023-04-01 03:47:55.173271 rewards-0.0.4/rewards/models.py
+-rw-r--r--   0        0        0     5936 2023-04-06 14:35:37.602050 rewards-0.0.4/rewards/trainer.py
+-rw-r--r--   0        0        0     6109 2023-04-06 15:42:25.954399 rewards-0.0.4/rewards/workflow.py
+-rw-r--r--   0        0        0    15940 1970-01-01 00:00:00.000000 rewards-0.0.4/PKG-INFO
```

### Comparing `rewards-0.0.3/README.md` & `rewards-0.0.4/README.md`

 * *Files identical despite different names*

### Comparing `rewards-0.0.3/rewards/agent.py` & `rewards-0.0.4/rewards/agent.py`

 * *Files identical despite different names*

### Comparing `rewards-0.0.3/rewards/assets/CarRace/car.png` & `rewards-0.0.4/rewards/assets/CarRace/car.png`

 * *Files identical despite different names*

### Comparing `rewards-0.0.3/rewards/assets/CarRace/track-1.png` & `rewards-0.0.4/rewards/assets/CarRace/track-1.png`

 * *Files identical despite different names*

### Comparing `rewards-0.0.3/rewards/assets/CarRace/track-2.png` & `rewards-0.0.4/rewards/assets/CarRace/track-2.png`

 * *Files identical despite different names*

### Comparing `rewards-0.0.3/rewards/assets/CarRace/track-3.png` & `rewards-0.0.4/rewards/assets/CarRace/track-3.png`

 * *Files identical despite different names*

### Comparing `rewards-0.0.3/rewards/envs/car.py` & `rewards-0.0.4/rewards/envs/car.py`

 * *Files identical despite different names*

### Comparing `rewards-0.0.3/rewards/models.py` & `rewards-0.0.4/rewards/models.py`

 * *Files identical despite different names*

### Comparing `rewards-0.0.3/rewards/trainer.py` & `rewards-0.0.4/rewards/trainer.py`

 * *Files identical despite different names*

### Comparing `rewards-0.0.3/rewards/workflow.py` & `rewards-0.0.4/rewards/workflow.py`

 * *Files 1% similar despite different names*

```diff
@@ -166,15 +166,15 @@
 
                     if score > record:
                         self.agent.model.save()
                         record = score
 
                     total_score += score
 
-                    if self.agent.n_games != 0:
+                    if self.agent.n_games != 0 and self.config.ENABLE_WANDB:
                         self.run.log(
                             {
                                 "episode score": score,
                                 "mean score": total_score / self.agent.n_games,
                             }
                         )
```

### Comparing `rewards-0.0.3/PKG-INFO` & `rewards-0.0.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rewards
-Version: 0.0.3
+Version: 0.0.4
 Summary: Start learning about RL and make model and envs in minutes in just few lines of code
 License: MIT
 Author: rewards.ai
 Requires-Python: >=3.10,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
```

