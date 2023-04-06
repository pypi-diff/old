# Comparing `tmp/fps_resource_usage-0.0.50.tar.gz` & `tmp/fps_resource_usage-0.1.2.tar.gz`

## Comparing `fps_resource_usage-0.0.50.tar` & `fps_resource_usage-0.1.2.tar`

### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0       23 2020-02-02 00:00:00.000000 fps_resource_usage-0.0.50/fps_resource_usage/__init__.py
--rw-r--r--   0        0        0      496 2020-02-02 00:00:00.000000 fps_resource_usage-0.0.50/fps_resource_usage/config.py
--rw-r--r--   0        0        0     2021 2020-02-02 00:00:00.000000 fps_resource_usage-0.0.50/fps_resource_usage/routes.py
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_resource_usage-0.0.50/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_resource_usage-0.0.50/COPYING.md
--rw-r--r--   0        0        0       64 2020-02-02 00:00:00.000000 fps_resource_usage-0.0.50/README.md
--rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 fps_resource_usage-0.0.50/pyproject.toml
--rw-r--r--   0        0        0      536 2020-02-02 00:00:00.000000 fps_resource_usage-0.0.50/PKG-INFO
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/fps_resource_usage/__init__.py
+-rw-r--r--   0        0        0      695 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/fps_resource_usage/main.py
+-rw-r--r--   0        0        0     2620 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/fps_resource_usage/routes.py
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/COPYING.md
+-rw-r--r--   0        0        0       64 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/README.md
+-rw-r--r--   0        0        0      998 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0      559 2020-02-02 00:00:00.000000 fps_resource_usage-0.1.2/PKG-INFO
```

### Comparing `fps_resource_usage-0.0.50/fps_resource_usage/routes.py` & `fps_resource_usage-0.1.2/fps_resource_usage/routes.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,65 +1,74 @@
-import psutil  # type: ignore
+import psutil
 from anyio import to_thread
-from fastapi import APIRouter, Depends  # type: ignore
-from fps.hooks import register_router  # type: ignore
-from fps_auth_base import User, current_user  # type: ignore
-
-from .config import get_resource_usage_config
-
-router = APIRouter()
-
-
-@router.get("/api/metrics/v1")
-async def get_content(
-    user: User = Depends(current_user(permissions={"contents": ["read"]})),
-    config=Depends(get_resource_usage_config),
-):
-    cur_process = psutil.Process()
-    all_processes = [cur_process] + cur_process.children(recursive=True)
-
-    # Get memory information
-    rss = 0
-    for p in all_processes:
-        try:
-            rss += p.memory_info().rss
-        except (psutil.NoSuchProcess, psutil.AccessDenied):
-            pass
-
-    mem_limit = config.mem_limit
-
-    limits = {"memory": {"rss": mem_limit}}
-    if config.mem_limit and config.mem_warning_threshold:
-        limits["memory"]["warn"] = (mem_limit - rss) < (mem_limit * config.mem_warning_threshold)
-
-    metrics = {"rss": rss, "limits": limits}
-
-    # Optionally get CPU information
-    if config.track_cpu_percent:
-        cpu_count = psutil.cpu_count()
-        cpu_percent = await to_thread.run_sync(_get_cpu_percent, all_processes)
-
-        if config.cpu_limit:
-            limits["cpu"] = {"cpu": config.cpu_limit}
-            if config.cpu_warning_threshold:
-                limits["cpu"]["warn"] = (config.cpu_limit - cpu_percent) < (
-                    config.cpu_limit * config.cpu_warning_threshold
+from fastapi import APIRouter, Depends
+from jupyverse_api.app import App
+from jupyverse_api.auth import Auth, User
+from jupyverse_api.resource_usage import ResourceUsage, ResourceUsageConfig
+
+
+class _ResourceUsage(ResourceUsage):
+    def __init__(
+        self,
+        app: App,
+        auth: Auth,
+        resource_usage_config: ResourceUsageConfig,
+    ):
+        super().__init__(app)
+
+        router = APIRouter()
+
+        @router.get("/api/metrics/v1")
+        async def get_metrics(
+            user: User = Depends(auth.current_user(permissions={"contents": ["read"]})),
+        ):
+            cur_process = psutil.Process()
+            all_processes = [cur_process] + cur_process.children(recursive=True)
+
+            # Get memory information
+            rss = 0
+            for p in all_processes:
+                try:
+                    rss += p.memory_info().rss
+                except (psutil.NoSuchProcess, psutil.AccessDenied):
+                    pass
+
+            mem_limit = resource_usage_config.mem_limit
+
+            limits = {"memory": {"rss": mem_limit}}
+            if resource_usage_config.mem_limit and resource_usage_config.mem_warning_threshold:
+                limits["memory"]["warn"] = (mem_limit - rss) < (
+                    mem_limit * resource_usage_config.mem_warning_threshold
                 )
 
-        metrics.update(cpu_percent=cpu_percent, cpu_count=cpu_count)
+            metrics = {"rss": rss, "limits": limits}
+
+            # Optionally get CPU information
+            if resource_usage_config.track_cpu_percent:
+                cpu_count = psutil.cpu_count()
+                cpu_percent = await to_thread.run_sync(_get_cpu_percent, all_processes)
+
+                if resource_usage_config.cpu_limit:
+                    limits["cpu"] = {"cpu": resource_usage_config.cpu_limit}
+                    if resource_usage_config.cpu_warning_threshold:
+                        limits["cpu"]["warn"] = (resource_usage_config.cpu_limit - cpu_percent) < (
+                            resource_usage_config.cpu_limit
+                            * resource_usage_config.cpu_warning_threshold
+                        )
+
+                metrics.update(cpu_percent=cpu_percent, cpu_count=cpu_count)
 
-    return metrics
+            return metrics
+
+        self.include_router(router)
 
 
 def _get_cpu_percent(all_processes):
     def get_cpu_percent(p):
         try:
             return p.cpu_percent(interval=0.05)
         # Avoid littering logs with stack traces complaining
         # about dead processes having no CPU usage
         except BaseException:
             return 0
 
     return sum([get_cpu_percent(p) for p in all_processes])
-
-
-r = register_router(router)
```

### Comparing `fps_resource_usage-0.0.50/.gitignore` & `fps_resource_usage-0.1.2/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_resource_usage-0.0.50/COPYING.md` & `fps_resource_usage-0.1.2/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_resource_usage-0.0.50/PKG-INFO` & `fps_resource_usage-0.1.2/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,18 +1,19 @@
 Metadata-Version: 2.1
 Name: fps_resource_usage
-Version: 0.0.50
+Version: 0.1.2
 Summary: An FPS plugin for the resource usage API
 Project-URL: Homepage, https://jupyter.org
 Author-email: Jupyter Development Team <jupyter@googlegroups.com>
 License: BSD 3-Clause License
 License-File: COPYING.md
-Keywords: fastapi,jupyter,pluggy,plugins,server
+Keywords: fastapi,jupyter,plugins,server
 Requires-Python: >=3.8
 Requires-Dist: anyio>=3.6.2
-Requires-Dist: fps>=0.0.8
+Requires-Dist: jupyverse-api
 Requires-Dist: psutil>=5.9.4
+Requires-Dist: types-psutil
 Description-Content-Type: text/markdown
 
 # fps-resource-usage
 
 An FPS plugin for the resource usage API.
```

