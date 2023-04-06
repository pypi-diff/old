# Comparing `tmp/fps_retrolab-0.0.50.tar.gz` & `tmp/fps_retrolab-0.1.2.tar.gz`

## Comparing `fps_retrolab-0.0.50.tar` & `fps_retrolab-0.1.2.tar`

### file list

```diff
@@ -1,9 +1,9 @@
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_retrolab-0.0.50/MANIFEST.in
--rw-r--r--   0        0        0       23 2020-02-02 00:00:00.000000 fps_retrolab-0.0.50/fps_retrolab/__init__.py
--rw-r--r--   0        0        0      264 2020-02-02 00:00:00.000000 fps_retrolab-0.0.50/fps_retrolab/config.py
--rw-r--r--   0        0        0     6288 2020-02-02 00:00:00.000000 fps_retrolab-0.0.50/fps_retrolab/routes.py
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_retrolab-0.0.50/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_retrolab-0.0.50/COPYING.md
--rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 fps_retrolab-0.0.50/README.md
--rw-r--r--   0        0        0      912 2020-02-02 00:00:00.000000 fps_retrolab-0.0.50/pyproject.toml
--rw-r--r--   0        0        0      559 2020-02-02 00:00:00.000000 fps_retrolab-0.0.50/PKG-INFO
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/MANIFEST.in
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/fps_retrolab/__init__.py
+-rw-r--r--   0        0        0      738 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/fps_retrolab/main.py
+-rw-r--r--   0        0        0     6717 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/fps_retrolab/routes.py
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/COPYING.md
+-rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/README.md
+-rw-r--r--   0        0        0      899 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0      474 2020-02-02 00:00:00.000000 fps_retrolab-0.1.2/PKG-INFO
```

### Comparing `fps_retrolab-0.0.50/fps_retrolab/routes.py` & `fps_retrolab-0.1.2/fps_retrolab/routes.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,151 +1,147 @@
 import json
 from pathlib import Path
 
 import retrolab  # type: ignore
 from fastapi import APIRouter, Depends
 from fastapi.responses import HTMLResponse
 from fastapi.staticfiles import StaticFiles
-from fps.hooks import register_router  # type: ignore
-from fps_auth_base import User, current_user  # type: ignore
-from fps_frontend.config import get_frontend_config  # type: ignore
-from fps_lab.config import get_lab_config  # type: ignore
-from fps_lab.routes import init_router  # type: ignore
-from fps_lab.utils import get_federated_extensions  # type: ignore
-
-router = APIRouter()
-prefix_dir, federated_extensions = init_router(router, "retro/tree")
-retrolab_dir = Path(retrolab.__file__).parent
-
-router.mount(
-    "/static/retro",
-    StaticFiles(directory=retrolab_dir / "static"),
-    name="static",
-)
-
-router.mount(
-    "/lab/extensions/@retrolab/lab-extension/static",
-    StaticFiles(directory=retrolab_dir / "labextension" / "static"),
-    name="labextension/static",
-)
-
-for path in (retrolab_dir / "labextension" / "static").glob("remoteEntry.*.js"):
-    load = f"static/{path.name}"
-    break
-retro_federated_extensions = [
-    {
-        "extension": "./extension",
-        "load": load,
-        "name": "@retrolab/lab-extension",
-        "style": "./style",
-    }
-]
-
-
-@router.get("/retro/tree", response_class=HTMLResponse)
-async def get_tree(
-    user: User = Depends(current_user()),
-    frontend_config=Depends(get_frontend_config),
-    lab_config=Depends(get_lab_config),
-):
-    return get_index("Tree", "tree", lab_config.collaborative, frontend_config.base_url)
-
-
-@router.get("/retro/notebooks/{path:path}", response_class=HTMLResponse)
-async def get_notebook(
-    path,
-    user: User = Depends(current_user()),
-    frontend_config=Depends(get_frontend_config),
-    lab_config=Depends(get_lab_config),
-):
-    return get_index(path, "notebooks", lab_config.collaborative, frontend_config.base_url)
-
-
-@router.get("/retro/edit/{path:path}", response_class=HTMLResponse)
-async def edit_file(
-    path,
-    user: User = Depends(current_user()),
-    frontend_config=Depends(get_frontend_config),
-    lab_config=Depends(get_lab_config),
-):
-    return get_index(path, "edit", lab_config.collaborative, frontend_config.base_url)
-
-
-@router.get("/retro/consoles/{path:path}", response_class=HTMLResponse)
-async def get_console(
-    path,
-    user: User = Depends(current_user()),
-    frontend_config=Depends(get_frontend_config),
-    lab_config=Depends(get_lab_config),
-):
-    return get_index(path, "consoles", lab_config.collaborative, frontend_config.base_url)
-
-
-@router.get("/retro/terminals/{name}", response_class=HTMLResponse)
-async def get_terminal(
-    name: str,
-    user: User = Depends(current_user()),
-    frontend_config=Depends(get_frontend_config),
-    lab_config=Depends(get_lab_config),
-):
-    return get_index(name, "terminals", lab_config.collaborative, frontend_config.base_url)
-
-
-def get_index(doc_name, retro_page, collaborative, base_url="/"):
-    extensions_dir = prefix_dir / "share" / "jupyter" / "labextensions"
-    federated_extensions, disabled_extension = get_federated_extensions(extensions_dir)
-    page_config = {
-        "appName": "RetroLab",
-        "appNamespace": "retro",
-        "appSettingsDir": (prefix_dir / "share" / "jupyter" / "lab" / "settings").as_posix(),
-        "appUrl": "/lab",
-        "appVersion": retrolab.__version__,
-        "baseUrl": base_url,
-        "cacheFiles": True,
-        "collaborative": collaborative,
-        "disabledExtensions": disabled_extension,
-        "extraLabextensionsPath": [],
-        "federated_extensions": retro_federated_extensions + federated_extensions,
-        "frontendUrl": "/retro/",
-        "fullAppUrl": f"{base_url}lab",
-        "fullLabextensionsUrl": f"{base_url}lab/extensions",
-        "fullLicensesUrl": f"{base_url}lab/api/licenses",
-        "fullListingsUrl": f"{base_url}lab/api/listings",
-        "fullMathjaxUrl": f"{base_url}static/notebook/components/MathJax/MathJax.js",
-        "fullSettingsUrl": f"{base_url}lab/api/settings",
-        "fullStaticUrl": f"{base_url}static/retro",
-        "fullThemesUrl": f"{base_url}lab/api/themes",
-        "fullTranslationsApiUrl": f"{base_url}lab/api/translations",
-        "fullTreeUrl": f"{base_url}lab/tree",
-        "fullWorkspacesApiUrl": f"{base_url}lab/api/workspaces",
-        "labextensionsPath": [(prefix_dir / "share" / "jupyter" / "labextensions").as_posix()],
-        "labextensionsUrl": "/lab/extensions",
-        "licensesUrl": "/lab/api/licenses",
-        "listingsUrl": "/lab/api/listings",
-        "mathjaxConfig": "TeX-AMS-MML_HTMLorMML-full,Safe",
-        "retroLogo": False,
-        "retroPage": retro_page,
-        "schemasDir": (prefix_dir / "share" / "jupyter" / "lab" / "schemas").as_posix(),
-        "settingsUrl": "/lab/api/settings",
-        "staticDir": (retrolab_dir / "static").as_posix(),
-        "templatesDir": (retrolab_dir / "templates").as_posix(),
-        "terminalsAvailable": True,
-        "themesDir": (prefix_dir / "share" / "jupyter" / "lab" / "themes").as_posix(),
-        "themesUrl": "/lab/api/themes",
-        "translationsApiUrl": "/lab/api/translations",
-        "treeUrl": "/lab/tree",
-        "workspacesApiUrl": "/lab/api/workspaces",
-        "wsUrl": "",
-    }
-    index = (
-        INDEX_HTML.replace("PAGE_CONFIG", json.dumps(page_config))
-        .replace("DOC_NAME", doc_name)
-        .replace("BASE_URL", base_url)
-    )
-    return index
+from jupyverse_api.app import App
+from jupyverse_api.auth import Auth, User
+from jupyverse_api.frontend import FrontendConfig
+from jupyverse_api.lab import Lab
+from jupyverse_api.retrolab import RetroLab
+
+
+class _RetroLab(RetroLab):
+    def __init__(self, app: App, auth: Auth, frontend_config: FrontendConfig, lab: Lab) -> None:
+        super().__init__(app)
+
+        router = APIRouter()
+        prefix_dir, federated_extensions = lab.init_router(router, "retro/tree")
+        retrolab_dir = Path(retrolab.__file__).parent
+
+        self.mount(
+            "/static/retro",
+            StaticFiles(directory=retrolab_dir / "static"),
+            name="static",
+        )
+
+        for path in (retrolab_dir / "labextension" / "static").glob("remoteEntry.*.js"):
+            load = f"static/{path.name}"
+            break
+        retro_federated_extensions = [
+            {
+                "extension": "./extension",
+                "load": load,
+                "name": "@retrolab/lab-extension",
+                "style": "./style",
+            }
+        ]
+
+        @router.get("/retro/tree", response_class=HTMLResponse)
+        async def get_tree(
+            user: User = Depends(auth.current_user()),
+        ):
+            return get_index(
+                "Tree", "tree", frontend_config.collaborative, frontend_config.base_url
+            )
+
+        @router.get("/retro/notebooks/{path:path}", response_class=HTMLResponse)
+        async def get_notebook(
+            path,
+            user: User = Depends(auth.current_user()),
+        ):
+            return get_index(
+                path, "notebooks", frontend_config.collaborative, frontend_config.base_url
+            )
+
+        @router.get("/retro/edit/{path:path}", response_class=HTMLResponse)
+        async def edit_file(
+            path,
+            user: User = Depends(auth.current_user()),
+        ):
+            return get_index(path, "edit", frontend_config.collaborative, frontend_config.base_url)
+
+        @router.get("/retro/consoles/{path:path}", response_class=HTMLResponse)
+        async def get_console(
+            path,
+            user: User = Depends(auth.current_user()),
+        ):
+            return get_index(
+                path, "consoles", frontend_config.collaborative, frontend_config.base_url
+            )
+
+        @router.get("/retro/terminals/{name}", response_class=HTMLResponse)
+        async def get_terminal(
+            name: str,
+            user: User = Depends(auth.current_user()),
+        ):
+            return get_index(
+                name, "terminals", frontend_config.collaborative, frontend_config.base_url
+            )
+
+        def get_index(doc_name, retro_page, collaborative, base_url="/"):
+            extensions_dir = prefix_dir / "share" / "jupyter" / "labextensions"
+            federated_extensions, disabled_extension = lab.get_federated_extensions(extensions_dir)
+            page_config = {
+                "appName": "RetroLab",
+                "appNamespace": "retro",
+                "appSettingsDir": (
+                    prefix_dir / "share" / "jupyter" / "lab" / "settings"
+                ).as_posix(),
+                "appUrl": "/lab",
+                "appVersion": retrolab.__version__,
+                "baseUrl": base_url,
+                "cacheFiles": True,
+                "collaborative": collaborative,
+                "disabledExtensions": disabled_extension,
+                "extraLabextensionsPath": [],
+                "federated_extensions": retro_federated_extensions + federated_extensions,
+                "frontendUrl": "/retro/",
+                "fullAppUrl": f"{base_url}lab",
+                "fullLabextensionsUrl": f"{base_url}lab/extensions",
+                "fullLicensesUrl": f"{base_url}lab/api/licenses",
+                "fullListingsUrl": f"{base_url}lab/api/listings",
+                "fullMathjaxUrl": f"{base_url}static/notebook/components/MathJax/MathJax.js",
+                "fullSettingsUrl": f"{base_url}lab/api/settings",
+                "fullStaticUrl": f"{base_url}static/retro",
+                "fullThemesUrl": f"{base_url}lab/api/themes",
+                "fullTranslationsApiUrl": f"{base_url}lab/api/translations",
+                "fullTreeUrl": f"{base_url}lab/tree",
+                "fullWorkspacesApiUrl": f"{base_url}lab/api/workspaces",
+                "labextensionsPath": [
+                    (prefix_dir / "share" / "jupyter" / "labextensions").as_posix()
+                ],
+                "labextensionsUrl": "/lab/extensions",
+                "licensesUrl": "/lab/api/licenses",
+                "listingsUrl": "/lab/api/listings",
+                "mathjaxConfig": "TeX-AMS-MML_HTMLorMML-full,Safe",
+                "retroLogo": False,
+                "retroPage": retro_page,
+                "schemasDir": (prefix_dir / "share" / "jupyter" / "lab" / "schemas").as_posix(),
+                "settingsUrl": "/lab/api/settings",
+                "staticDir": (retrolab_dir / "static").as_posix(),
+                "templatesDir": (retrolab_dir / "templates").as_posix(),
+                "terminalsAvailable": True,
+                "themesDir": (prefix_dir / "share" / "jupyter" / "lab" / "themes").as_posix(),
+                "themesUrl": "/lab/api/themes",
+                "translationsApiUrl": "/lab/api/translations",
+                "treeUrl": "/lab/tree",
+                "workspacesApiUrl": "/lab/api/workspaces",
+                "wsUrl": "",
+            }
+            index = (
+                INDEX_HTML.replace("PAGE_CONFIG", json.dumps(page_config))
+                .replace("DOC_NAME", doc_name)
+                .replace("BASE_URL", base_url)
+            )
+            return index
+
+        self.include_router(router)
 
 
 INDEX_HTML = """\
 <!DOCTYPE html>
 <html>
 <head>
   <meta charset="utf-8">
@@ -168,9 +164,7 @@
         window.history.replaceState({ }, '', parsedUrl.href);
       }
     })();
   </script>
 </body>
 </html>
 """
-
-r = register_router(router)
```

### Comparing `fps_retrolab-0.0.50/.gitignore` & `fps_retrolab-0.1.2/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_retrolab-0.0.50/COPYING.md` & `fps_retrolab-0.1.2/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_retrolab-0.0.50/pyproject.toml` & `fps_retrolab-0.1.2/pyproject.toml`

 * *Files 18% similar despite different names*

```diff
@@ -1,17 +1,20 @@
 [build-system]
 requires = [ "hatchling",]
 build-backend = "hatchling.build"
 
 [project]
 name = "fps_retrolab"
 description = "An FPS plugin for the RetroLab API"
-keywords = [ "jupyter", "server", "fastapi", "pluggy", "plugins",]
+keywords = ["jupyter", "server", "fastapi", "plugins"]
 requires-python = ">=3.8"
-dependencies = [ "fps >=0.0.8", "fps-auth-base", "fps-frontend", "fps-lab", "retrolab",]
+dependencies = [
+    "retrolab",
+    "jupyverse-api",
+]
 dynamic = [ "version",]
 [[project.authors]]
 name = "Jupyter Development Team"
 email = "jupyter@googlegroups.com"
 
 [project.readme]
 file = "README.md"
@@ -25,15 +28,13 @@
 
 [tool.check-manifest]
 ignore = [ ".*",]
 
 [tool.jupyter-releaser]
 skip = [ "check-links",]
 
-[project.entry-points.fps_router]
-fps-retrolab = "fps_retrolab.routes"
-
-[project.entry-points.fps_config]
-fps-retrolab = "fps_retrolab.config"
+[project.entry-points]
+"asphalt.components"   = {retrolab = "fps_retrolab.main:RetroLabComponent"}
+"jupyverse.components" = {retrolab = "fps_retrolab.main:RetroLabComponent"}
 
 [tool.hatch.version]
 path = "fps_retrolab/__init__.py"
```

