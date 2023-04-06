# Comparing `tmp/joonmyung-1.3.9.tar.gz` & `tmp/joonmyung-1.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/joonmyung-1.3.9.tar", last modified: Wed Mar  8 20:12:53 2023, max compression
+gzip compressed data, was "dist/joonmyung-1.4.0.tar", last modified: Thu Apr  6 05:36:56 2023, max compression
```

## Comparing `joonmyung-1.3.9.tar` & `joonmyung-1.4.0.tar`

### file list

```diff
@@ -1,26 +1,28 @@
-drwxr-xr-x   0 joonmyung   (501) staff       (20)        0 2023-03-08 20:12:53.000000 joonmyung-1.3.9/
--rw-r--r--   0 joonmyung   (501) staff       (20)      241 2023-03-08 20:12:53.000000 joonmyung-1.3.9/PKG-INFO
--rw-r--r--   0 joonmyung   (501) staff       (20)      862 2023-03-08 13:25:35.000000 joonmyung-1.3.9/README.md
-drwxr-xr-x   0 joonmyung   (501) staff       (20)        0 2023-03-08 20:12:53.000000 joonmyung-1.3.9/joonmyung/
--rw-r--r--   0 joonmyung   (501) staff       (20)       15 2023-02-22 17:22:56.000000 joonmyung-1.3.9/joonmyung/__init__.py
--rw-r--r--   0 joonmyung   (501) staff       (20)      695 2023-02-24 17:07:52.000000 joonmyung-1.3.9/joonmyung/data.py
--rw-r--r--   0 joonmyung   (501) staff       (20)    13286 2023-03-06 13:16:50.000000 joonmyung-1.3.9/joonmyung/draw.py
--rw-r--r--   0 joonmyung   (501) staff       (20)     2755 2023-02-22 17:22:56.000000 joonmyung-1.3.9/joonmyung/file.py
--rw-r--r--   0 joonmyung   (501) staff       (20)      920 2023-02-22 17:22:56.000000 joonmyung-1.3.9/joonmyung/gradcam.py
--rw-r--r--   0 joonmyung   (501) staff       (20)     4443 2023-03-08 20:06:10.000000 joonmyung-1.3.9/joonmyung/log.py
-drwxr-xr-x   0 joonmyung   (501) staff       (20)        0 2023-03-08 20:12:53.000000 joonmyung-1.3.9/joonmyung/meta_data/
--rw-r--r--   0 joonmyung   (501) staff       (20)       41 2023-03-01 06:51:46.000000 joonmyung-1.3.9/joonmyung/meta_data/__init__.py
--rw-r--r--   0 joonmyung   (501) staff       (20)    45491 2023-02-22 17:22:56.000000 joonmyung-1.3.9/joonmyung/meta_data/label.py
--rw-r--r--   0 joonmyung   (501) staff       (20)     2277 2023-03-01 06:32:47.000000 joonmyung-1.3.9/joonmyung/meta_data/utils.py
--rw-r--r--   0 joonmyung   (501) staff       (20)     6030 2023-03-04 10:44:55.000000 joonmyung-1.3.9/joonmyung/metric.py
--rw-r--r--   0 joonmyung   (501) staff       (20)     2912 2023-03-04 09:54:14.000000 joonmyung-1.3.9/joonmyung/script.py
--rw-r--r--   0 joonmyung   (501) staff       (20)     1487 2023-03-01 13:25:20.000000 joonmyung-1.3.9/joonmyung/status.py
--rw-r--r--   0 joonmyung   (501) staff       (20)     3969 2023-02-26 13:32:34.000000 joonmyung-1.3.9/joonmyung/utils.py
-drwxr-xr-x   0 joonmyung   (501) staff       (20)        0 2023-03-08 20:12:53.000000 joonmyung-1.3.9/joonmyung.egg-info/
--rw-r--r--   0 joonmyung   (501) staff       (20)      241 2023-03-08 20:12:53.000000 joonmyung-1.3.9/joonmyung.egg-info/PKG-INFO
--rw-r--r--   0 joonmyung   (501) staff       (20)      465 2023-03-08 20:12:53.000000 joonmyung-1.3.9/joonmyung.egg-info/SOURCES.txt
--rw-r--r--   0 joonmyung   (501) staff       (20)        1 2023-03-08 20:12:53.000000 joonmyung-1.3.9/joonmyung.egg-info/dependency_links.txt
--rw-r--r--   0 joonmyung   (501) staff       (20)        1 2023-03-08 20:12:53.000000 joonmyung-1.3.9/joonmyung.egg-info/not-zip-safe
--rw-r--r--   0 joonmyung   (501) staff       (20)       10 2023-03-08 20:12:53.000000 joonmyung-1.3.9/joonmyung.egg-info/top_level.txt
--rw-r--r--   0 joonmyung   (501) staff       (20)       38 2023-03-08 20:12:53.000000 joonmyung-1.3.9/setup.cfg
--rw-r--r--   0 joonmyung   (501) staff       (20)      805 2023-03-08 20:12:28.000000 joonmyung-1.3.9/setup.py
+drwxr-xr-x   0 joonmyung   (501) staff       (20)        0 2023-04-06 05:36:56.000000 joonmyung-1.4.0/
+-rw-r--r--   0 joonmyung   (501) staff       (20)      241 2023-04-06 05:36:56.000000 joonmyung-1.4.0/PKG-INFO
+-rw-r--r--   0 joonmyung   (501) staff       (20)     1001 2023-04-06 05:35:59.000000 joonmyung-1.4.0/README.md
+drwxr-xr-x   0 joonmyung   (501) staff       (20)        0 2023-04-06 05:36:56.000000 joonmyung-1.4.0/joonmyung/
+-rw-r--r--   0 joonmyung   (501) staff       (20)       15 2023-02-22 17:22:56.000000 joonmyung-1.4.0/joonmyung/__init__.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)     6700 2023-04-03 12:26:27.000000 joonmyung-1.4.0/joonmyung/app.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)      695 2023-02-24 17:07:52.000000 joonmyung-1.4.0/joonmyung/data.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)    13286 2023-03-06 13:16:50.000000 joonmyung-1.4.0/joonmyung/draw.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)       29 2023-04-03 12:26:27.000000 joonmyung-1.4.0/joonmyung/dummy.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)     2755 2023-02-22 17:22:56.000000 joonmyung-1.4.0/joonmyung/file.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)      920 2023-02-22 17:22:56.000000 joonmyung-1.4.0/joonmyung/gradcam.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)     4922 2023-04-06 05:34:25.000000 joonmyung-1.4.0/joonmyung/log.py
+drwxr-xr-x   0 joonmyung   (501) staff       (20)        0 2023-04-06 05:36:56.000000 joonmyung-1.4.0/joonmyung/meta_data/
+-rw-r--r--   0 joonmyung   (501) staff       (20)       41 2023-03-01 06:51:46.000000 joonmyung-1.4.0/joonmyung/meta_data/__init__.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)    45491 2023-02-22 17:22:56.000000 joonmyung-1.4.0/joonmyung/meta_data/label.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)     2277 2023-03-01 06:32:47.000000 joonmyung-1.4.0/joonmyung/meta_data/utils.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)     6030 2023-03-04 10:44:55.000000 joonmyung-1.4.0/joonmyung/metric.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)     3214 2023-03-30 15:51:49.000000 joonmyung-1.4.0/joonmyung/script.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)     1487 2023-03-01 13:25:20.000000 joonmyung-1.4.0/joonmyung/status.py
+-rw-r--r--   0 joonmyung   (501) staff       (20)     3969 2023-04-05 01:40:34.000000 joonmyung-1.4.0/joonmyung/utils.py
+drwxr-xr-x   0 joonmyung   (501) staff       (20)        0 2023-04-06 05:36:56.000000 joonmyung-1.4.0/joonmyung.egg-info/
+-rw-r--r--   0 joonmyung   (501) staff       (20)      241 2023-04-06 05:36:56.000000 joonmyung-1.4.0/joonmyung.egg-info/PKG-INFO
+-rw-r--r--   0 joonmyung   (501) staff       (20)      501 2023-04-06 05:36:56.000000 joonmyung-1.4.0/joonmyung.egg-info/SOURCES.txt
+-rw-r--r--   0 joonmyung   (501) staff       (20)        1 2023-04-06 05:36:56.000000 joonmyung-1.4.0/joonmyung.egg-info/dependency_links.txt
+-rw-r--r--   0 joonmyung   (501) staff       (20)        1 2023-03-08 20:12:53.000000 joonmyung-1.4.0/joonmyung.egg-info/not-zip-safe
+-rw-r--r--   0 joonmyung   (501) staff       (20)       10 2023-04-06 05:36:56.000000 joonmyung-1.4.0/joonmyung.egg-info/top_level.txt
+-rw-r--r--   0 joonmyung   (501) staff       (20)       38 2023-04-06 05:36:56.000000 joonmyung-1.4.0/setup.cfg
+-rw-r--r--   0 joonmyung   (501) staff       (20)      781 2023-04-06 05:34:32.000000 joonmyung-1.4.0/setup.py
```

### Comparing `joonmyung-1.3.9/README.md` & `joonmyung-1.4.0/README.md`

 * *Files 16% similar despite different names*

```diff
@@ -10,14 +10,20 @@
 2. joonmyung/draw 
  - [ ] LinePlot 수정
  
 ### b. Playground
 
 
 # 3. Previous
+## Version 1.4.0
+1. joonmyung/app.py
+ - [X] 실험 도중 스크립트 추가 기능
+2. joonmyung/log
+ - [X] 모델, 코드 저장 기능
+
 ## Version 1.3.2
 1. joonmyung/Logger
  - [X] wandb_id 작업
 
 ## Version 1.3.2
 1. joonmyung/Script
  - [X] Multi-GPU 적용
```

### Comparing `joonmyung-1.3.9/joonmyung/data.py` & `joonmyung-1.4.0/joonmyung/data.py`

 * *Files identical despite different names*

### Comparing `joonmyung-1.3.9/joonmyung/draw.py` & `joonmyung-1.4.0/joonmyung/draw.py`

 * *Files identical despite different names*

### Comparing `joonmyung-1.3.9/joonmyung/file.py` & `joonmyung-1.4.0/joonmyung/file.py`

 * *Files identical despite different names*

### Comparing `joonmyung-1.3.9/joonmyung/gradcam.py` & `joonmyung-1.4.0/joonmyung/gradcam.py`

 * *Files identical despite different names*

### Comparing `joonmyung-1.3.9/joonmyung/log.py` & `joonmyung-1.4.0/joonmyung/log.py`

 * *Files 13% similar despite different names*

```diff
@@ -38,26 +38,28 @@
               f'loss {losses.val:.4f} ({losses.avg:.4f})\t' \n\
               f'acc {avg_score.val:.4f} ({avg_score.avg:.4f})')"
 
 
 class Logger():
     loggers = {}
     def __init__(self, use_wandb=True, wandb_entity=None, wandb_project=None, wandb_name=None
-                 , wandb_watch=False, main_process=True, wandb_id=None
-                 , args=None, model=False
-                 , save=True):
+                 , wandb_watch=False, main_process=True, wandb_id=None, wandb_dir='./'
+                 , args=None, model=False):
         self.use_wandb = use_wandb and main_process
 
         if self.use_wandb:
-            wandb.init(entity=wandb_entity, project=wandb_project, name=wandb_name, resume="allow",
-                       config=args, id = wandb_id)
-
-            if args: args.wandb_id = wandb.config.id = wandb.run.id
+            wandb.init(entity=wandb_entity, project=wandb_project, name=wandb_name
+                       , save_code=True, resume="allow", id = wandb_id, dir=wandb_dir
+                       , config=args, settings=wandb.Settings(code_dir="."))
+
+            if args:
+                args.wandb_id = wandb.config.id = wandb.run.id
+                torch.save(args, os.path.join(wandb.run.dir, "args.pt"))
             if wandb_watch and model: wandb.watch(model, log='all')
-            if save and args: torch.save({'args': args, }, os.path.join(wandb.run.dir, "args.pt"))
+
 
     def getLog(self, k, return_type =None):
         if return_type == "avg":
             return self.loggers[k].avg
         elif return_type == "val":
             return self.loggers[k].val
         else:
@@ -87,37 +89,47 @@
                     self.loggers[k].add_data(str(epoch), str(mae_task_type), *[wandb.Image(to_np(data2PIL(v[1][k][idx]))) if len(v[1][k].shape) == 4 else to_np(v[1][k])[idx] for k in columns])
         return True
 
     def getPath(self):
         return wandb.run.dir
 
     def logWandb(self):
-        if self.use_wandb:
-            wandb.log({k:v.avg if type(v) == AverageMeter else v for k, v in self.loggers.items()})
+        if self.validation():
+            wandb.log({k: v.avg if type(v) == AverageMeter else v for k, v in self.loggers.items()})
             self.resetLog()
-        else:
-            print("Wandb is not Working Now")
-
+        #
     def finish(self):
         wandb.finish()
 
+    def save(self, file, name):
+        if self.validation():
+            path = os.path.join(wandb.run.dir, f"{name}.pt")
+            torch.save(file, path)
+            wandb.save(path, wandb.run.dir)
+
+    def validation(self):
+        return True if self.use_wandb else False
+
 if __name__ == "__main__":
     from playground.analysis.lib_import import *
     dataset_name, server, device = "imagenet", "148", "cuda"
     data_path, _ = data2path(server, dataset_name)
     data_num = [[5, 1],
                 [5, 2],
                 [5, 3],
                 [5, 4]]
     dataset = JDataset(data_path, dataset_name, device=device)
     samples, targets, imgs, label_names = dataset.getItems(data_num)
+    model = torch.hub.load('facebookresearch/deit:main', "deit_tiny_patch16_224", pretrained=True)
 
     logger = Logger(use_wandb=True, wandb_entity="joonmyung", wandb_project="test", wandb_name="AAPP",
-                    wandb_watch=False)
+                    wandb_watch=False, wandb_dir="./")
 
     logger.addLog({ "sample A": [0, 4],
                     "sample B": [0, 3],
                     "sample C": [0, 2],
                     "table  B": [2, {"image" :     samples, "prediction": targets}]})
-    logger.logWandb()
 
+
+    logger.save(model.state_dict(), "checkpoint_best.pt")
+    logger.logWandb()
     logger.finish()
```

### Comparing `joonmyung-1.3.9/joonmyung/meta_data/label.py` & `joonmyung-1.4.0/joonmyung/meta_data/label.py`

 * *Files identical despite different names*

### Comparing `joonmyung-1.3.9/joonmyung/meta_data/utils.py` & `joonmyung-1.4.0/joonmyung/meta_data/utils.py`

 * *Files identical despite different names*

### Comparing `joonmyung-1.3.9/joonmyung/metric.py` & `joonmyung-1.4.0/joonmyung/metric.py`

 * *Files identical despite different names*

### Comparing `joonmyung-1.3.9/joonmyung/script.py` & `joonmyung-1.4.0/joonmyung/script.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,53 +1,57 @@
 from joonmyung.utils import time2str
 from tqdm import tqdm
 import subprocess
 import time
 import pynvml
 
-
-
 class GPU_Worker():
-    def __init__(self, gpus = [], waitTimeInit = 30, waitTime = 60,
-                 checkType = 0, need_gpu=1, reversed=False, p = True):
+    def __init__(self, gpus = [], waitTimeInit = 30, waitTime = 60, count = 0,
+                 checkType:int = 0, utilRatio:int = 50, need_gpu=1, reversed=False, p = True):
         self.activate  = False
         self.gpus      = gpus
         self.waitTimeInit = waitTimeInit
         self.waitTime = waitTime
         self.checkType = checkType
         self.need_gpu = int(need_gpu)
 
         self.reversed  = reversed
+        self.utilRatio = utilRatio
         self.p = p
+        self.count = count
 
         self.availGPUs = []
 
+    def getFreeRatio(self, id):
+        handle = pynvml.nvmlDeviceGetHandleByIndex(id)
+        use = pynvml.nvmlDeviceGetUtilizationRates(handle)
+        ratio = 0.5 * (float(use.gpu + float(use.memory)))
+        # ratio = float(use.memory)
+        # ratio = float(use.gpu)
+        return ratio
+
     def setGPU(self):
         if self.activate: time.sleep(self.waitTimeInit)
         else: self.activate = True
 
-        count = 0
+        count = self.count
         pynvml.nvmlInit()
         while True:
             availGPUs = []
             count += 1
             for gpu in self.gpus:
-                handle = pynvml.nvmlDeviceGetHandleByIndex(gpu)
+                handle = pynvml.nvmlDeviceGetHandleByIndex(int(gpu))
 
                 # 1. 아무것도 돌지 않는 경우
                 if self.checkType == 0 and len(pynvml.nvmlDeviceGetComputeRunningProcesses(handle)) == 0:
                     availGPUs.append(str(gpu))
 
-                # # 2. 70% 이하를 사용하는 경우
-                # elif self.checkType == 1 and self.getFreeRatio(gpu) < 70:
-                #     availGPUs.append(gpu)
-
-
-            # for proc in pynvml.nvmlDeviceGetComputeRunningProcesses(handle):
-            #     result[gpu] = [proc.pid, proc.usedGpuMemory]
+                # 2. n% 이하를 사용하고 있는 경우
+                elif self.checkType == 1 and self.getFreeRatio(int(gpu)) < self.utilRatio:
+                    availGPUs.append(str(gpu))
 
             if len(availGPUs) < self.need_gpu:
                 if self.p: print("{} : Wait for finish".format(count))
                 time.sleep(self.waitTime)
             else:
                 break
         self.availGPUs = availGPUs
@@ -77,9 +81,9 @@
     print("Training Time :  : {} ------".format(time2str(end - start)))
 
 
 
 if __name__ == '__main__':
     # Wokring Sample
     processes = [1,2,3,4,5]
-    gpuWorker = GPU_Worker([0,1,2,3,4,5,6,7], 30, 120, need_gpu=4)
+    gpuWorker = GPU_Worker([0,1,2,3], 30, 120, checkType=1, utilRatio=50, need_gpu=4)
     Process_Worker(processes, gpuWorker)
```

### Comparing `joonmyung-1.3.9/joonmyung/status.py` & `joonmyung-1.4.0/joonmyung/status.py`

 * *Files identical despite different names*

### Comparing `joonmyung-1.3.9/joonmyung/utils.py` & `joonmyung-1.4.0/joonmyung/utils.py`

 * *Files identical despite different names*

### Comparing `joonmyung-1.3.9/setup.py` & `joonmyung-1.4.0/setup.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 import setuptools
 from setuptools import find_packages
 setuptools.setup(
     name="joonmyung",
-    version="1.3.9",
+    version="1.4.0",
     author="JoonMyung Choi",
     author_email="pizard@korea.ac.kr",
     description="JoonMyung's Library",
     url="https://github.com/pizard/JoonMyung.git",
     license="MIT",
     packages=find_packages(exclude=["playground",
                                     "playground.*",
@@ -20,10 +20,9 @@
 )
 
 # git add .
 # git commit
 # git push
 # Remove *.egg-info
 #
-# python setup.py sdist
-# python -m twine upload dist/*     # Remove All File
-# ID:JoonmyungChoi
+# python setup.py sdist; python -m twine upload dist/*
+# ID:JoonmyungChoi
```

