# Comparing `tmp/rewards-0.0.5.tar.gz` & `tmp/rewards-0.0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rewards-0.0.5.tar", max compression
+gzip compressed data, was "rewards-0.0.6.tar", max compression
```

## Comparing `rewards-0.0.5.tar` & `rewards-0.0.6.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0    15251 2023-04-06 14:35:37.598050 rewards-0.0.5/README.md
--rw-r--r--   0        0        0      457 2023-04-06 18:04:16.041532 rewards-0.0.5/pyproject.toml
--rw-r--r--   0        0        0        5 2023-04-06 15:42:38.058461 rewards-0.0.5/rewards/VERSION
--rw-r--r--   0        0        0      247 2023-04-06 14:35:37.602050 rewards-0.0.5/rewards/__init__.py
--rw-r--r--   0        0        0     3867 2023-04-01 03:47:55.173271 rewards-0.0.5/rewards/agent.py
--rw-r--r--   0        0        0       18 2023-04-06 14:35:37.602050 rewards-0.0.5/rewards/assets/CarRace/__init__.py
--rw-r--r--   0        0        0    79384 2023-03-31 17:19:59.957981 rewards-0.0.5/rewards/assets/CarRace/car.png
--rw-r--r--   0        0        0    60297 2023-04-06 14:35:37.602050 rewards-0.0.5/rewards/assets/CarRace/track-1.png
--rw-r--r--   0        0        0    42293 2023-04-06 14:35:37.602050 rewards-0.0.5/rewards/assets/CarRace/track-2.png
--rw-r--r--   0        0        0    49467 2023-04-06 14:35:37.602050 rewards-0.0.5/rewards/assets/CarRace/track-3.png
--rw-r--r--   0        0        0       18 2023-04-06 14:35:37.602050 rewards-0.0.5/rewards/assets/__init__.py
--rw-r--r--   0        0        0        0 2023-04-02 06:50:32.365576 rewards-0.0.5/rewards/envs/__init__.py
--rw-r--r--   0        0        0    15306 2023-04-06 14:35:37.602050 rewards-0.0.5/rewards/envs/car.py
--rw-r--r--   0        0        0     2679 2023-04-06 17:59:58.902994 rewards-0.0.5/rewards/models.py
--rw-r--r--   0        0        0     5936 2023-04-06 14:35:37.602050 rewards-0.0.5/rewards/trainer.py
--rw-r--r--   0        0        0     6150 2023-04-06 18:01:07.763831 rewards-0.0.5/rewards/workflow.py
--rw-r--r--   0        0        0    15940 1970-01-01 00:00:00.000000 rewards-0.0.5/PKG-INFO
+-rw-r--r--   0        0        0    15251 2023-04-06 14:35:37.598050 rewards-0.0.6/README.md
+-rw-r--r--   0        0        0      456 2023-04-07 10:32:27.099387 rewards-0.0.6/pyproject.toml
+-rw-r--r--   0        0        0        5 2023-04-06 15:42:38.058461 rewards-0.0.6/rewards/VERSION
+-rw-r--r--   0        0        0      247 2023-04-06 14:35:37.602050 rewards-0.0.6/rewards/__init__.py
+-rw-r--r--   0        0        0     3837 2023-04-07 09:50:29.384498 rewards-0.0.6/rewards/agent.py
+-rw-r--r--   0        0        0       18 2023-04-06 14:35:37.602050 rewards-0.0.6/rewards/assets/CarRace/__init__.py
+-rw-r--r--   0        0        0    79384 2023-03-31 17:19:59.957981 rewards-0.0.6/rewards/assets/CarRace/car.png
+-rw-r--r--   0        0        0    60297 2023-04-06 14:35:37.602050 rewards-0.0.6/rewards/assets/CarRace/track-1.png
+-rw-r--r--   0        0        0    42293 2023-04-06 14:35:37.602050 rewards-0.0.6/rewards/assets/CarRace/track-2.png
+-rw-r--r--   0        0        0    49467 2023-04-06 14:35:37.602050 rewards-0.0.6/rewards/assets/CarRace/track-3.png
+-rw-r--r--   0        0        0       18 2023-04-06 14:35:37.602050 rewards-0.0.6/rewards/assets/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-02 06:50:32.365576 rewards-0.0.6/rewards/envs/__init__.py
+-rw-r--r--   0        0        0    15306 2023-04-06 14:35:37.602050 rewards-0.0.6/rewards/envs/car.py
+-rw-r--r--   0        0        0     5173 2023-04-07 10:30:46.515282 rewards-0.0.6/rewards/models.py
+-rw-r--r--   0        0        0     5845 2023-04-07 09:52:51.808349 rewards-0.0.6/rewards/trainer.py
+-rw-r--r--   0        0        0     6358 2023-04-07 09:57:30.807928 rewards-0.0.6/rewards/workflow.py
+-rw-r--r--   0        0        0    15940 1970-01-01 00:00:00.000000 rewards-0.0.6/PKG-INFO
```

### Comparing `rewards-0.0.5/README.md` & `rewards-0.0.6/README.md`

 * *Files identical despite different names*

### Comparing `rewards-0.0.5/rewards/agent.py` & `rewards-0.0.6/rewards/agent.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 import os
+import glob 
 import random
 from collections import deque
 from dataclasses import dataclass
 from pathlib import Path
 from typing import Any, List, Optional, Union
 
 import numpy as np
@@ -20,15 +21,16 @@
     DEVICE: str = "cpu"
 
 
 class Agent(AgentConf):
     def __init__(
         self,
         model: torch.nn.Module,
-        checkpoint_path: Optional[str] = None,
+        checkpoint_folder_path: Optional[str] = None,
+        model_name : Optional[str] = None, 
         lr: float = 0.01,
         epsilon: float = 0.25,
         gamma: float = 0.9,
     ) -> None:
         super(Agent, self).__init__()
         """The Agent class which acts as a RL agent similar like Open AI's gym agent
 
@@ -42,23 +44,19 @@
         self.n_games = 0
         self.epsilon = epsilon
         self.lr = lr
         self.gamma = gamma
 
         self.memory = deque(maxlen=self.MAX_MEMORY)
         self.model = model
-        if checkpoint_path:
-            self.model.load_state_dict(
-                torch.load(
-                    os.path.join(checkpoint_path),
-                    map_location=self.DEVICE,
-                )
-            )
-            self.model.eval()
-
+        
+        # Lates changes loading the model directly if exists 
+        
+        self.model.load(checkpoint_folder_path, model_name, self.DEVICE)
+        
     def get_state(self, game: Any) -> np.ndarray:
         """Returns the current state of the game.
         NOTE: Some Assumptions:
         - We assume that the game environment is made using pygame
         - We also assume that the agent inside the game uses `radars` that keeps track of its all position and other parameters.
 
         Args:
```

### Comparing `rewards-0.0.5/rewards/assets/CarRace/car.png` & `rewards-0.0.6/rewards/assets/CarRace/car.png`

 * *Files identical despite different names*

### Comparing `rewards-0.0.5/rewards/assets/CarRace/track-1.png` & `rewards-0.0.6/rewards/assets/CarRace/track-1.png`

 * *Files identical despite different names*

### Comparing `rewards-0.0.5/rewards/assets/CarRace/track-2.png` & `rewards-0.0.6/rewards/assets/CarRace/track-2.png`

 * *Files identical despite different names*

### Comparing `rewards-0.0.5/rewards/assets/CarRace/track-3.png` & `rewards-0.0.6/rewards/assets/CarRace/track-3.png`

 * *Files identical despite different names*

### Comparing `rewards-0.0.5/rewards/envs/car.py` & `rewards-0.0.6/rewards/envs/car.py`

 * *Files identical despite different names*

### Comparing `rewards-0.0.5/rewards/trainer.py` & `rewards-0.0.6/rewards/trainer.py`

 * *Files 2% similar despite different names*

```diff
@@ -42,26 +42,21 @@
         self.model = training_params["model"]
         loss_fn, optimizer_info = self._get_loss_optimizer_info(
             training_params["loss"], training_params["optimizer"]
         )
         self.criterion = loss_fn()
         self.optimizer = optimizer_info(self.model.parameters(), lr=self.lr)
 
-        if training_params["checkpoint_path"]:
-            self.model.load_state_dict(
-                torch.load(
-                    training_params["checkpoint_path"], map_location="cpu"
-                )
-            )
-
         super(QTrainer, self).__init__(
             model=self.model,
             lr=self.lr,
             epsilon=self.epsilon,
             gamma=self.gamma,
+            checkpoint_folder_path=training_params['checkpoint_folder_path'], 
+            model_name=training_params['model_name']
         )
 
     def _get_loss_optimizer_info(
         self, loss: str, optimizer: str
     ) -> List[Union[int, str, float]]:
         """_summary_
```

### Comparing `rewards-0.0.5/rewards/workflow.py` & `rewards-0.0.6/rewards/workflow.py`

 * *Files 3% similar despite different names*

```diff
@@ -26,14 +26,15 @@
         return 1
     return 0
 
 
 @dataclass(kw_only=True)
 class WorkFlowConfigurations:
     # wandb experiment
+    DEVICE : str = "cpu"
     EXPERIMENT_NAME: str = "sample RL experiment"
 
     # Environment configuration
 
     ENVIRONMENT_NAME: str = "car-race"
     ENVIRONMENT_WORLD: Union[str, int] = 1
 
@@ -51,15 +52,16 @@
     # RL Configuration
     GAMMA: float = 0.99
     EPSILON: float = 0.99
 
     # Model configuration
     LAYER_CONFIG: Union[List[List[int]], torch.nn.Module] = None # required 
 
-    CHECKPOINT_PATH: Optional[str] = None
+    CHECKPOINT_FOLDER_PATH: Optional[str] = None
+    CHECKPOINT_MODEL_NAME: Optional[str] = None
     REWARD_FUNCTION: Callable = None # required 
 
     # Tracking configuration 
     ENABLE_WANDB : bool = False 
 
 class RLWorkFlow:
     def __init__(
@@ -85,30 +87,31 @@
         self.agent = QTrainer(
             lr=self.config.LR,
             gamma=self.config.GAMMA,
             epsilon=self.config.EPSILON,
             model=self.model,
             loss=self.config.LOSS,
             optimizer=self.config.OPTIMIZER,
-            checkpoint_path=self.config.CHECKPOINT_PATH,
+            checkpoint_folder_path=self.config.CHECKPOINT_FOLDER_PATH,
+            model_name = self.config.CHECKPOINT_MODEL_NAME
         )
 
         # Once everything is done then upload all configurations to wandb
         
         if self.config.ENABLE_WANDB:
             wandb_config = self.config.__dict__.copy()
             wandb_config["REWARD_FUNCTION"] = inspect.getsource(
                 self.config.REWARD_FUNCTION if self.config.REWARD_FUNCTION is not None else default_reward_function
             )
 
             if isinstance(self.model, torch.nn.Module):
                 wandb_config.pop("LAYER_CONFIG")
                 # Also upload the model to wandb artifact 
                 
-            wandb_config.pop("CHECKPOINT_PATH")
+            wandb_config.pop("CHECKPOINT_FOLDER_PATH")
 
             self.run = wandb.init(
                 project=self.config.EXPERIMENT_NAME, config=wandb_config
             )
             
         if self.config.ENABLE_WANDB:
             config_dataframe = pd.DataFrame(
@@ -161,15 +164,15 @@
 
                 if done:
                     self.game.initialize()
                     self.agent.n_games += 1
                     self.agent.train_long_memory()
 
                     if score > record:
-                        self.agent.model.save(folder_path = self.config.CHECKPOINT_PATH)
+                        self.agent.model.save(self.config.CHECKPOINT_FOLDER_PATH, self.config.CHECKPOINT_MODEL_NAME, self.config.DEVICE)
                         record = score
 
                     total_score += score
 
                     if self.agent.n_games != 0 and self.config.ENABLE_WANDB:
                         self.run.log(
                             {
```

### Comparing `rewards-0.0.5/PKG-INFO` & `rewards-0.0.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rewards
-Version: 0.0.5
+Version: 0.0.6
 Summary: Start learning about RL and make model and envs in minutes in just few lines of code
 License: MIT
 Author: rewards.ai
 Requires-Python: >=3.10,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
```

