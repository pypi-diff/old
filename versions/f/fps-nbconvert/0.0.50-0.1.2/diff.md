# Comparing `tmp/fps_nbconvert-0.0.50.tar.gz` & `tmp/fps_nbconvert-0.1.2.tar.gz`

## Comparing `fps_nbconvert-0.0.50.tar` & `fps_nbconvert-0.1.2.tar`

### file list

```diff
@@ -1,8 +1,9 @@
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_nbconvert-0.0.50/MANIFEST.in
--rw-r--r--   0        0        0       23 2020-02-02 00:00:00.000000 fps_nbconvert-0.0.50/fps_nbconvert/__init__.py
--rw-r--r--   0        0        0     1224 2020-02-02 00:00:00.000000 fps_nbconvert-0.0.50/fps_nbconvert/routes.py
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_nbconvert-0.0.50/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_nbconvert-0.0.50/COPYING.md
--rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 fps_nbconvert-0.0.50/README.md
--rw-r--r--   0        0        0      819 2020-02-02 00:00:00.000000 fps_nbconvert-0.0.50/pyproject.toml
--rw-r--r--   0        0        0      513 2020-02-02 00:00:00.000000 fps_nbconvert-0.0.50/PKG-INFO
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/MANIFEST.in
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/fps_nbconvert/__init__.py
+-rw-r--r--   0        0        0      509 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/fps_nbconvert/main.py
+-rw-r--r--   0        0        0     1563 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/fps_nbconvert/routes.py
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/COPYING.md
+-rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/README.md
+-rw-r--r--   0        0        0      909 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0      479 2020-02-02 00:00:00.000000 fps_nbconvert-0.1.2/PKG-INFO
```

### Comparing `fps_nbconvert-0.0.50/fps_nbconvert/routes.py` & `fps_nbconvert-0.1.2/fps_nbconvert/routes.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,40 +1,47 @@
 import tempfile
 from pathlib import Path
 
-import nbconvert  # type: ignore
+import nbconvert
 from fastapi import APIRouter, Depends
 from fastapi.responses import FileResponse
-from fps.hooks import register_router  # type: ignore
-from fps_auth_base import User, current_user  # type: ignore
+from jupyverse_api.app import App
+from jupyverse_api.auth import Auth, User
+from jupyverse_api.nbconvert import Nbconvert
+
+
+class _Nbconvert(Nbconvert):
+    def __init__(
+        self,
+        app: App,
+        auth: Auth,
+    ) -> None:
+        super().__init__(app)
+
+        router = APIRouter()
+
+        @router.get("/api/nbconvert")
+        async def get_nbconvert_formats():
+            return {
+                name: {"output_mimetype": nbconvert.exporters.get_exporter(name).output_mimetype}
+                for name in nbconvert.exporters.get_export_names()
+            }
+
+        @router.get("/nbconvert/{format}/{path}")
+        async def get_nbconvert_document(
+            format: str,
+            path: str,
+            download: bool,
+            user: User = Depends(auth.current_user(permissions={"nbconvert": ["read"]})),
+        ):
+            exporter = nbconvert.exporters.get_exporter(format)
+            if download:
+                media_type = "application/octet-stream"
+            else:
+                media_type = exporter.output_mimetype
+            tmp_dir = Path(tempfile.mkdtemp())
+            tmp_path = tmp_dir / (Path(path).stem + exporter().file_extension)
+            with open(tmp_path, "wt") as f:
+                f.write(exporter().from_filename(path)[0])
+            return FileResponse(tmp_path, media_type=media_type, filename=tmp_path.name)
 
-router = APIRouter()
-
-
-@router.get("/api/nbconvert")
-async def get_nbconvert_formats():
-    return {
-        name: {"output_mimetype": nbconvert.exporters.get_exporter(name).output_mimetype}
-        for name in nbconvert.exporters.get_export_names()
-    }
-
-
-@router.get("/nbconvert/{format}/{path}")
-async def get_nbconvert_document(
-    format: str,
-    path: str,
-    download: bool,
-    user: User = Depends(current_user(permissions={"nbconvert": ["read"]})),
-):
-    exporter = nbconvert.exporters.get_exporter(format)
-    if download:
-        media_type = "application/octet-stream"
-    else:
-        media_type = exporter.output_mimetype
-    tmp_dir = Path(tempfile.mkdtemp())
-    tmp_path = tmp_dir / (Path(path).stem + exporter().file_extension)
-    with open(tmp_path, "wt") as f:
-        f.write(exporter().from_filename(path)[0])
-    return FileResponse(tmp_path, media_type=media_type, filename=tmp_path.name)
-
-
-r = register_router(router)
+        self.include_router(router)
```

### Comparing `fps_nbconvert-0.0.50/.gitignore` & `fps_nbconvert-0.1.2/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_nbconvert-0.0.50/COPYING.md` & `fps_nbconvert-0.1.2/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_nbconvert-0.0.50/pyproject.toml` & `fps_nbconvert-0.1.2/pyproject.toml`

 * *Files 25% similar despite different names*

```diff
@@ -1,17 +1,20 @@
 [build-system]
 requires = [ "hatchling",]
 build-backend = "hatchling.build"
 
 [project]
 name = "fps_nbconvert"
 description = "An FPS plugin for the nbconvert API"
-keywords = [ "jupyter", "server", "fastapi", "pluggy", "plugins",]
+keywords = ["jupyter", "server", "fastapi", "plugins"]
 requires-python = ">=3.8"
-dependencies = [ "fps >=0.0.8", "fps-auth-base", "nbconvert",]
+dependencies = [
+    "nbconvert",
+    "jupyverse-api",
+]
 dynamic = [ "version",]
 [[project.authors]]
 name = "Jupyter Development Team"
 email = "jupyter@googlegroups.com"
 
 [project.readme]
 file = "README.md"
@@ -25,12 +28,13 @@
 
 [tool.check-manifest]
 ignore = [ ".*",]
 
 [tool.jupyter-releaser]
 skip = [ "check-links",]
 
-[project.entry-points.fps_router]
-fps-nbconvert = "fps_nbconvert.routes"
+[project.entry-points]
+"asphalt.components"   = {nbconvert = "fps_nbconvert.main:NbconvertComponent"}
+"jupyverse.components" = {nbconvert = "fps_nbconvert.main:NbconvertComponent"}
 
 [tool.hatch.version]
 path = "fps_nbconvert/__init__.py"
```

