# Comparing `tmp/rewards-0.0.0.1.tar.gz` & `tmp/rewards-0.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rewards-0.0.0.1.tar", max compression
+gzip compressed data, was "rewards-0.0.1.tar", max compression
```

## Comparing `rewards-0.0.0.1.tar` & `rewards-0.0.1.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0    15251 2023-04-04 13:15:40.590933 rewards-0.0.0.1/README.md
--rw-r--r--   0        0        0      545 2023-04-04 13:15:40.590933 rewards-0.0.0.1/pyproject.toml
--rw-r--r--   0        0        0        6 2023-04-04 13:15:40.590933 rewards-0.0.0.1/rewards/VERSION
--rw-r--r--   0        0        0      247 2023-04-04 13:15:40.590933 rewards-0.0.0.1/rewards/__init__.py
--rw-r--r--   0        0        0     3867 2023-04-04 13:15:40.590933 rewards-0.0.0.1/rewards/agent.py
--rw-r--r--   0        0        0       18 2023-04-04 13:15:40.590933 rewards-0.0.0.1/rewards/assets/CarRace/__init__.py
--rw-r--r--   0        0        0    79384 2023-04-04 13:15:40.590933 rewards-0.0.0.1/rewards/assets/CarRace/car.png
--rw-r--r--   0        0        0    60297 2023-04-04 13:15:40.590933 rewards-0.0.0.1/rewards/assets/CarRace/track-1.png
--rw-r--r--   0        0        0    42293 2023-04-04 13:15:40.590933 rewards-0.0.0.1/rewards/assets/CarRace/track-2.png
--rw-r--r--   0        0        0    49467 2023-04-04 13:15:40.590933 rewards-0.0.0.1/rewards/assets/CarRace/track-3.png
--rw-r--r--   0        0        0       18 2023-04-04 13:15:40.590933 rewards-0.0.0.1/rewards/assets/__init__.py
--rw-r--r--   0        0        0        0 2023-04-04 13:15:40.590933 rewards-0.0.0.1/rewards/envs/__init__.py
--rw-r--r--   0        0        0    15306 2023-04-04 13:15:40.590933 rewards-0.0.0.1/rewards/envs/car.py
--rw-r--r--   0        0        0     2634 2023-04-04 13:15:40.594933 rewards-0.0.0.1/rewards/models.py
--rw-r--r--   0        0        0     5936 2023-04-04 13:15:40.594933 rewards-0.0.0.1/rewards/trainer.py
--rw-r--r--   0        0        0     5689 2023-04-04 13:15:40.594933 rewards-0.0.0.1/rewards/workflow.py
--rw-r--r--   0        0        0    15862 1970-01-01 00:00:00.000000 rewards-0.0.0.1/PKG-INFO
+-rw-r--r--   0        0        0    15251 2023-04-06 14:35:37.598050 rewards-0.0.1/README.md
+-rw-r--r--   0        0        0      452 2023-04-06 14:48:26.878799 rewards-0.0.1/pyproject.toml
+-rw-r--r--   0        0        0        5 2023-04-06 14:48:16.966876 rewards-0.0.1/rewards/VERSION
+-rw-r--r--   0        0        0      247 2023-04-06 14:35:37.602050 rewards-0.0.1/rewards/__init__.py
+-rw-r--r--   0        0        0     3867 2023-04-01 03:47:55.173271 rewards-0.0.1/rewards/agent.py
+-rw-r--r--   0        0        0       18 2023-04-06 14:35:37.602050 rewards-0.0.1/rewards/assets/CarRace/__init__.py
+-rw-r--r--   0        0        0    79384 2023-03-31 17:19:59.957981 rewards-0.0.1/rewards/assets/CarRace/car.png
+-rw-r--r--   0        0        0    60297 2023-04-06 14:35:37.602050 rewards-0.0.1/rewards/assets/CarRace/track-1.png
+-rw-r--r--   0        0        0    42293 2023-04-06 14:35:37.602050 rewards-0.0.1/rewards/assets/CarRace/track-2.png
+-rw-r--r--   0        0        0    49467 2023-04-06 14:35:37.602050 rewards-0.0.1/rewards/assets/CarRace/track-3.png
+-rw-r--r--   0        0        0       18 2023-04-06 14:35:37.602050 rewards-0.0.1/rewards/assets/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-02 06:50:32.365576 rewards-0.0.1/rewards/envs/__init__.py
+-rw-r--r--   0        0        0    15306 2023-04-06 14:35:37.602050 rewards-0.0.1/rewards/envs/car.py
+-rw-r--r--   0        0        0     2634 2023-04-01 03:47:55.173271 rewards-0.0.1/rewards/models.py
+-rw-r--r--   0        0        0     5936 2023-04-06 14:35:37.602050 rewards-0.0.1/rewards/trainer.py
+-rw-r--r--   0        0        0     6040 2023-04-06 14:35:37.602050 rewards-0.0.1/rewards/workflow.py
+-rw-r--r--   0        0        0    15923 1970-01-01 00:00:00.000000 rewards-0.0.1/PKG-INFO
```

### Comparing `rewards-0.0.0.1/README.md` & `rewards-0.0.1/README.md`

 * *Files identical despite different names*

### Comparing `rewards-0.0.0.1/rewards/agent.py` & `rewards-0.0.1/rewards/agent.py`

 * *Files identical despite different names*

### Comparing `rewards-0.0.0.1/rewards/assets/CarRace/car.png` & `rewards-0.0.1/rewards/assets/CarRace/car.png`

 * *Files identical despite different names*

### Comparing `rewards-0.0.0.1/rewards/assets/CarRace/track-1.png` & `rewards-0.0.1/rewards/assets/CarRace/track-1.png`

 * *Files identical despite different names*

### Comparing `rewards-0.0.0.1/rewards/assets/CarRace/track-2.png` & `rewards-0.0.1/rewards/assets/CarRace/track-2.png`

 * *Files identical despite different names*

### Comparing `rewards-0.0.0.1/rewards/assets/CarRace/track-3.png` & `rewards-0.0.1/rewards/assets/CarRace/track-3.png`

 * *Files identical despite different names*

### Comparing `rewards-0.0.0.1/rewards/envs/car.py` & `rewards-0.0.1/rewards/envs/car.py`

 * *Files identical despite different names*

### Comparing `rewards-0.0.0.1/rewards/models.py` & `rewards-0.0.1/rewards/models.py`

 * *Files identical despite different names*

### Comparing `rewards-0.0.0.1/rewards/trainer.py` & `rewards-0.0.1/rewards/trainer.py`

 * *Files identical despite different names*

### Comparing `rewards-0.0.0.1/rewards/workflow.py` & `rewards-0.0.1/rewards/workflow.py`

 * *Files 8% similar despite different names*

```diff
@@ -54,14 +54,16 @@
 
     # Model configuration
     LAYER_CONFIG: Union[List[List[int]], torch.nn.Module] = None # required 
 
     CHECKPOINT_PATH: Optional[str] = None
     REWARD_FUNCTION: Callable = None # required 
 
+    # Tracking configuration 
+    ENABLE_WANDB : bool = False 
 
 class RLWorkFlow:
     def __init__(
         self, experiment_configuration: Optional[WorkFlowConfigurations] = None
     ) -> None:
         """
         **RLWorkFlow** is the module which ables us to run complete RL experiments
@@ -87,44 +89,49 @@
             model=self.model,
             loss=self.config.LOSS,
             optimizer=self.config.OPTIMIZER,
             checkpoint_path=self.config.CHECKPOINT_PATH,
         )
 
         # Once everything is done then upload all configurations to wandb
-
-        wandb_config = self.config.__dict__.copy()
-        wandb_config["REWARD_FUNCTION"] = inspect.getsource(
-            self.config.REWARD_FUNCTION if self.config.REWARD_FUNCTION is not None else default_reward_function
-        )
-
-        if isinstance(self.model, torch.nn.Module):
-            wandb_config.pop("LAYER_CONFIG")
-        wandb_config.pop("CHECKPOINT_PATH")
-
-        self.run = wandb.init(
-            project=self.config.EXPERIMENT_NAME, config=wandb_config
-        )
+        
+        if self.config.ENABLE_WANDB:
+            wandb_config = self.config.__dict__.copy()
+            wandb_config["REWARD_FUNCTION"] = inspect.getsource(
+                self.config.REWARD_FUNCTION if self.config.REWARD_FUNCTION is not None else default_reward_function
+            )
+
+            if isinstance(self.model, torch.nn.Module):
+                wandb_config.pop("LAYER_CONFIG")
+                # Also upload the model to wandb artifact 
+                
+            wandb_config.pop("CHECKPOINT_PATH")
+
+            self.run = wandb.init(
+                project=self.config.EXPERIMENT_NAME, config=wandb_config
+            )
+            
         config_dataframe = pd.DataFrame(
             data={
                 "configuration name": list(wandb_config.keys()),
                 "configuration": [
                     str(ele) for ele in list(wandb_config.values())
                 ],
             }
         )
 
-        config_table = wandb.Table(dataframe=config_dataframe)
-        config_table_artifact = wandb.Artifact(
-            "configuration_artifact", type="dataset"
-        )
-        config_table_artifact.add(config_table, "configuration_table")
+        if self.config.ENABLE_WANDB:
+            config_table = wandb.Table(dataframe=config_dataframe)
+            config_table_artifact = wandb.Artifact(
+                "configuration_artifact", type="dataset"
+            )
+            config_table_artifact.add(config_table, "configuration_table")
 
-        self.run.log({"Configuration": config_table})
-        self.run.log_artifact(config_table_artifact)
+            self.run.log({"Configuration": config_table})
+            self.run.log_artifact(config_table_artifact)
 
         # Build Game
         # TODO:
         # For now we are assuming that we only have just one game and so we are keeping
         # all the game and env config at one place. In next set of version this will be
         # different as we will support it for multiple pre-built envs and custom envs
 
@@ -167,15 +174,16 @@
                         self.run.log(
                             {
                                 "episode score": score,
                                 "mean score": total_score / self.agent.n_games,
                             }
                         )
 
-                self.run.log({"Num Games": self.agent.n_games})
+                if self.config.ENABLE_WANDB:
+                    self.run.log({"Num Games": self.agent.n_games})
 
                 for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                         pygame.quit()
                         break
         except pygame.error:
             print("pygame error")
```

### Comparing `rewards-0.0.0.1/PKG-INFO` & `rewards-0.0.1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,22 +1,24 @@
 Metadata-Version: 2.1
 Name: rewards
-Version: 0.0.0.1
+Version: 0.0.1
 Summary: Start learning about RL and make model and envs in minutes in just few lines of code
 License: MIT
 Author: rewards.ai
 Requires-Python: >=3.10,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
+Requires-Dist: lightning (>=2.0.1,<3.0.0)
 Requires-Dist: matplotlib (>=3.7.1,<4.0.0)
 Requires-Dist: numpy (>=1.24.2,<2.0.0)
-Requires-Dist: pandas (>=1.5.3,<2.0.0)
+Requires-Dist: pandas
 Requires-Dist: pygame (>=2.3.0,<3.0.0)
+Requires-Dist: torch (>=2.0.0,<3.0.0)
 Description-Content-Type: text/markdown
 
 # **rewards** 
 ### A low code sdk for crearing custom environments and deep RL agents. 
 
 
 <br>
```

