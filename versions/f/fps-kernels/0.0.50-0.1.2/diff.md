# Comparing `tmp/fps_kernels-0.0.50.tar.gz` & `tmp/fps_kernels-0.1.2.tar.gz`

## Comparing `fps_kernels-0.0.50.tar` & `fps_kernels-0.1.2.tar`

### file list

```diff
@@ -1,19 +1,18 @@
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/MANIFEST.in
--rw-r--r--   0        0        0       23 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/__init__.py
--rw-r--r--   0        0        0      374 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/config.py
--rw-r--r--   0        0        0      622 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/models.py
--rw-r--r--   0        0        0    12033 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/routes.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/kernel_driver/__init__.py
--rw-r--r--   0        0        0     2987 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/kernel_driver/connect.py
--rw-r--r--   0        0        0     8664 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/kernel_driver/driver.py
--rw-r--r--   0        0        0     1900 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/kernel_driver/kernelspec.py
--rw-r--r--   0        0        0     4094 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/kernel_driver/message.py
--rw-r--r--   0        0        0     2916 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/kernel_driver/paths.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/kernel_server/__init__.py
--rw-r--r--   0        0        0     2731 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/kernel_server/message.py
--rw-r--r--   0        0        0    11550 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/fps_kernels/kernel_server/server.py
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/COPYING.md
--rw-r--r--   0        0        0       50 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/README.md
--rw-r--r--   0        0        0      960 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/pyproject.toml
--rw-r--r--   0        0        0      646 2020-02-02 00:00:00.000000 fps_kernels-0.0.50/PKG-INFO
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/MANIFEST.in
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/__init__.py
+-rw-r--r--   0        0        0     1582 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/main.py
+-rw-r--r--   0        0        0    15262 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/routes.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_driver/__init__.py
+-rw-r--r--   0        0        0     2987 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_driver/connect.py
+-rw-r--r--   0        0        0     8632 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_driver/driver.py
+-rw-r--r--   0        0        0     1900 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_driver/kernelspec.py
+-rw-r--r--   0        0        0     4078 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_driver/message.py
+-rw-r--r--   0        0        0     2916 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_driver/paths.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_server/__init__.py
+-rw-r--r--   0        0        0     2731 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_server/message.py
+-rw-r--r--   0        0        0    11591 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/fps_kernels/kernel_server/server.py
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/COPYING.md
+-rw-r--r--   0        0        0       50 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/README.md
+-rw-r--r--   0        0        0      987 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0      598 2020-02-02 00:00:00.000000 fps_kernels-0.1.2/PKG-INFO
```

### Comparing `fps_kernels-0.0.50/fps_kernels/routes.py` & `fps_kernels-0.1.2/fps_kernels/routes.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,339 +1,364 @@
-import asyncio
 import json
 import sys
 import uuid
 from http import HTTPStatus
 from pathlib import Path
 from typing import Dict, List, Set, Tuple
 
 from fastapi import APIRouter, Depends, HTTPException, Response
 from fastapi.responses import FileResponse
-from fps.hooks import register_router  # type: ignore
-from fps_auth_base import User, current_user, websocket_auth  # type: ignore
-from fps_frontend.config import get_frontend_config  # type: ignore
-from fps_yjs.routes import YDocWebSocketHandler  # type: ignore
-from starlette.requests import Request  # type: ignore
+from starlette.requests import Request
 from watchfiles import Change, awatch
+from jupyverse_api.auth import Auth, User
+from jupyverse_api.kernels import Kernels, KernelsConfig
+from jupyverse_api.kernels.models import CreateSession, Execution, Kernel, Notebook, Session
+from jupyverse_api.frontend import FrontendConfig
+from jupyverse_api.yjs import Yjs
+from jupyverse_api.app import App
 
-from .config import get_kernel_config
-from .kernel_driver.driver import KernelDriver  # type: ignore
+from .kernel_driver.driver import KernelDriver
 from .kernel_driver.kernelspec import find_kernelspec, kernelspec_dirs
-from .kernel_server.server import (  # type: ignore
+from .kernel_server.server import (
     AcceptedWebSocket,
     KernelServer,
     kernels,
 )
-from .models import CreateSession, Execution, Session
 
-router = APIRouter()
-
-kernelspecs: dict = {}
-kernel_id_to_connection_file: Dict[str, str] = {}
-sessions: dict = {}
-prefix_dir: Path = Path(sys.prefix)
-
-
-async def process_connection_files(changes: Set[Tuple[Change, str]]):
-    # get rid of "simultaneously" added/deleted files
-    file_changes: Dict[str, List[Change]] = {}
-    for c in changes:
-        change, path = c
-        if path not in file_changes:
-            file_changes[path] = []
-        file_changes[path].append(change)
-    to_delete: List[str] = []
-    for p, cs in file_changes.items():
-        if Change.added in cs and Change.deleted in cs:
-            cs.remove(Change.added)
-            cs.remove(Change.deleted)
-            if not cs:
-                to_delete.append(p)
-    for p in to_delete:
-        del file_changes[p]
-    # process file changes
-    for path, cs in file_changes.items():
-        for change in cs:
-            if change == Change.deleted:
-                if path in kernels:
-                    kernel_id = list(kernel_id_to_connection_file.keys())[
-                        list(kernel_id_to_connection_file.values()).index(path)
-                    ]
-                    del kernels[kernel_id]
-            elif change == Change.added:
-                try:
-                    data = json.loads(Path(path).read_text())
-                except BaseException:
-                    continue
-                if "kernel_name" not in data or "key" not in data:
-                    continue
-                # looks like a kernel connection file
-                kernel_id = str(uuid.uuid4())
-                kernel_id_to_connection_file[kernel_id] = path
-                kernels[kernel_id] = {"name": data["kernel_name"], "server": None, "driver": None}
-
-
-async def watch_connection_files(path: Path):
-    # first time scan, treat everything as added files
-    initial_changes = {(Change.added, str(p)) for p in path.iterdir()}
-    await process_connection_files(initial_changes)
-    # then, on every change
-    async for changes in awatch(path):
-        await process_connection_files(changes)
-
-
-@router.on_event("startup")
-async def startup():
-    kernel_config = get_kernel_config()
-    if kernel_config.connection_path is not None:
-        path = Path(kernel_config.connection_path)
-        asyncio.create_task(watch_connection_files(path))
-
-
-@router.on_event("shutdown")
-async def stop_kernels():
-    for kernel in kernels.values():
-        await kernel["server"].stop()
-
-
-@router.get("/api/kernelspecs")
-async def get_kernelspecs(
-    frontend_config=Depends(get_frontend_config),
-    kernel_config=Depends(get_kernel_config),
-    user: User = Depends(current_user(permissions={"kernelspecs": ["read"]})),
-):
-    for search_path in kernelspec_dirs():
-        for path in Path(search_path).glob("*/kernel.json"):
-            with open(path) as f:
-                spec = json.load(f)
-            name = path.parent.name
-            resources = {
-                f.stem: f"{frontend_config.base_url}kernelspecs/{name}/{f.name}"
-                for f in path.parent.iterdir()
-                if f.is_file() and f.name != "kernel.json"
-            }
-            kernelspecs[name] = {"name": name, "spec": spec, "resources": resources}
-    return {"default": kernel_config.default_kernel, "kernelspecs": kernelspecs}
-
-
-@router.get("/kernelspecs/{kernel_name}/{file_name}")
-async def get_kernelspec(
-    kernel_name,
-    file_name,
-    user: User = Depends(current_user()),
-):
-    for search_path in kernelspec_dirs():
-        file_path = Path(search_path) / kernel_name / file_name
-        if file_path.exists():
-            return FileResponse(file_path)
-    raise HTTPException(status_code=404, detail=f"Kernelspec {kernel_name}/{file_name} not found")
-
-
-@router.get("/api/kernels")
-async def get_kernels(
-    user: User = Depends(current_user(permissions={"kernels": ["read"]})),
-):
-    results = []
-    for kernel_id, kernel in kernels.items():
-        if kernel["server"]:
-            connections = kernel["server"].connections
-            last_activity = kernel["server"].last_activity["date"]
-            execution_state = kernel["server"].last_activity["execution_state"]
-        else:
-            connections = 0
-            last_activity = ""
-            execution_state = "idle"
-        results.append(
-            {
-                "id": kernel_id,
-                "name": kernel["name"],
-                "connections": connections,
-                "last_activity": last_activity,
-                "execution_state": execution_state,
-            }
-        )
-    return results
 
+class _Kernels(Kernels):
+    def __init__(
+        self,
+        app: App,
+        kernels_config: KernelsConfig,
+        auth: Auth,
+        frontend_config: FrontendConfig,
+        yjs: Yjs,
+    ) -> None:
+        super().__init__(app)
+
+        router = APIRouter()
+
+        kernelspecs: dict = {}
+        self.kernel_id_to_connection_file: Dict[str, str] = {}
+        sessions: Dict[str, Session] = {}
+        Path(sys.prefix)
+
+        @router.get("/api/kernelspecs")
+        async def get_kernelspecs(
+            user: User = Depends(auth.current_user(permissions={"kernelspecs": ["read"]})),
+        ):
+            for search_path in kernelspec_dirs():
+                for path in Path(search_path).glob("*/kernel.json"):
+                    with open(path) as f:
+                        spec = json.load(f)
+                    name = path.parent.name
+                    resources = {
+                        f.stem: f"{frontend_config.base_url}kernelspecs/{name}/{f.name}"
+                        for f in path.parent.iterdir()
+                        if f.is_file() and f.name != "kernel.json"
+                    }
+                    kernelspecs[name] = {"name": name, "spec": spec, "resources": resources}
+            return {"default": kernels_config.default_kernel, "kernelspecs": kernelspecs}
+
+        @router.get("/kernelspecs/{kernel_name}/{file_name}")
+        async def get_kernelspec(
+            kernel_name,
+            file_name,
+            user: User = Depends(auth.current_user()),
+        ):
+            for search_path in kernelspec_dirs():
+                file_path = Path(search_path) / kernel_name / file_name
+                if file_path.exists():
+                    return FileResponse(file_path)
+            raise HTTPException(
+                status_code=404, detail=f"Kernelspec {kernel_name}/{file_name} not found"
+            )
 
-@router.delete("/api/sessions/{session_id}", status_code=204)
-async def delete_session(
-    session_id: str,
-    user: User = Depends(current_user(permissions={"sessions": ["write"]})),
-):
-    kernel_id = sessions[session_id]["kernel"]["id"]
-    kernel_server = kernels[kernel_id]["server"]
-    await kernel_server.stop()
-    del kernels[kernel_id]
-    if kernel_id in kernel_id_to_connection_file:
-        del kernel_id_to_connection_file[kernel_id]
-    del sessions[session_id]
-    return Response(status_code=HTTPStatus.NO_CONTENT.value)
-
-
-@router.patch("/api/sessions/{session_id}")
-async def rename_session(
-    request: Request,
-    user: User = Depends(current_user(permissions={"sessions": ["write"]})),
-):
-    rename_session = await request.json()
-    session_id = rename_session.pop("id")
-    for key, value in rename_session.items():
-        sessions[session_id][key] = value
-    return Session(**sessions[session_id])
-
-
-@router.get("/api/sessions")
-async def get_sessions(
-    user: User = Depends(current_user(permissions={"sessions": ["read"]})),
-):
-    for session in sessions.values():
-        kernel_id = session["kernel"]["id"]
-        kernel_server = kernels[kernel_id]["server"]
-        session["kernel"]["last_activity"] = kernel_server.last_activity["date"]
-        session["kernel"]["execution_state"] = kernel_server.last_activity["execution_state"]
-    return list(sessions.values())
-
-
-@router.post(
-    "/api/sessions",
-    status_code=201,
-    response_model=Session,
-)
-async def create_session(
-    request: Request,
-    user: User = Depends(current_user(permissions={"sessions": ["write"]})),
-):
-    create_session = CreateSession(**(await request.json()))
-    kernel_id = create_session.kernel.id
-    kernel_name = create_session.kernel.name
-    if kernel_name is not None:
-        # launch a new ("internal") kernel
-        kernel_server = KernelServer(
-            kernelspec_path=Path(find_kernelspec(kernel_name)).as_posix(),
-            kernel_cwd=str(Path(create_session.path).parent),
+        @router.get("/api/kernels")
+        async def get_kernels(
+            user: User = Depends(auth.current_user(permissions={"kernels": ["read"]})),
+        ):
+            results = []
+            for kernel_id, kernel in kernels.items():
+                if kernel["server"]:
+                    connections = kernel["server"].connections
+                    last_activity = kernel["server"].last_activity["date"]
+                    execution_state = kernel["server"].last_activity["execution_state"]
+                else:
+                    connections = 0
+                    last_activity = ""
+                    execution_state = "idle"
+                results.append(
+                    {
+                        "id": kernel_id,
+                        "name": kernel["name"],
+                        "connections": connections,
+                        "last_activity": last_activity,
+                        "execution_state": execution_state,
+                    }
+                )
+            return results
+
+        @router.delete("/api/sessions/{session_id}", status_code=204)
+        async def delete_session(
+            session_id: str,
+            user: User = Depends(auth.current_user(permissions={"sessions": ["write"]})),
+        ):
+            kernel_id = sessions[session_id].kernel.id
+            kernel_server = kernels[kernel_id]["server"]
+            await kernel_server.stop()
+            del kernels[kernel_id]
+            if kernel_id in self.kernel_id_to_connection_file:
+                del self.kernel_id_to_connection_file[kernel_id]
+            del sessions[session_id]
+            return Response(status_code=HTTPStatus.NO_CONTENT.value)
+
+        @router.patch("/api/sessions/{session_id}")
+        async def rename_session(
+            request: Request,
+            user: User = Depends(auth.current_user(permissions={"sessions": ["write"]})),
+        ):
+            rename_session = await request.json()
+            session_id = rename_session.pop("id")
+            for key, value in rename_session.items():
+                setattr(sessions[session_id], key, value)
+            return sessions[session_id]
+
+        @router.get("/api/sessions")
+        async def get_sessions(
+            user: User = Depends(auth.current_user(permissions={"sessions": ["read"]})),
+        ):
+            for session in sessions.values():
+                kernel_id = session.kernel.id
+                kernel_server = kernels[kernel_id]["server"]
+                session.kernel.last_activity = kernel_server.last_activity["date"]
+                session.kernel.execution_state = kernel_server.last_activity["execution_state"]
+            return list(sessions.values())
+
+        @router.post(
+            "/api/sessions",
+            status_code=201,
+            response_model=Session,
         )
-        kernel_id = str(uuid.uuid4())
-        kernels[kernel_id] = {"name": kernel_name, "server": kernel_server, "driver": None}
-        await kernel_server.start()
-    elif kernel_id is not None:
-        # external kernel
-        kernel_name = kernels[kernel_id]["name"]
-        kernel_server = KernelServer(
-            connection_file=kernel_id_to_connection_file[kernel_id],
-            write_connection_file=False,
-        )
-        kernels[kernel_id]["server"] = kernel_server
-        await kernel_server.start(launch_kernel=False)
-    else:
-        return
-    session_id = str(uuid.uuid4())
-    session = {
-        "id": session_id,
-        "path": create_session.path,
-        "name": create_session.name,
-        "type": create_session.type,
-        "kernel": {
-            "id": kernel_id,
-            "name": kernel_name,
-            "connections": kernel_server.connections,
-            "last_activity": kernel_server.last_activity["date"],
-            "execution_state": kernel_server.last_activity["execution_state"],
-        },
-        "notebook": {"path": create_session.path, "name": create_session.name},
-    }
-    sessions[session_id] = session
-    return Session(**session)
-
-
-@router.post("/api/kernels/{kernel_id}/restart")
-async def restart_kernel(
-    kernel_id,
-    user: User = Depends(current_user(permissions={"kernels": ["write"]})),
-):
-    if kernel_id in kernels:
-        kernel = kernels[kernel_id]
-        await kernel["server"].restart()
-        result = {
-            "id": kernel_id,
-            "name": kernel["name"],
-            "connections": kernel["server"].connections,
-            "last_activity": kernel["server"].last_activity["date"],
-            "execution_state": kernel["server"].last_activity["execution_state"],
-        }
-        return result
-
-
-@router.post("/api/kernels/{kernel_id}/execute")
-async def execute_cell(
-    request: Request,
-    kernel_id,
-    user: User = Depends(current_user(permissions={"kernels": ["write"]})),
-):
-    r = await request.json()
-    execution = Execution(**r)
-    if kernel_id in kernels:
-        ynotebook = YDocWebSocketHandler.websocket_server.get_room(execution.document_id).document
-        cell = ynotebook.get_cell(execution.cell_idx)
-        cell["outputs"] = []
-
-        kernel = kernels[kernel_id]
-        if not kernel["driver"]:
-            kernel["driver"] = driver = KernelDriver(
-                kernelspec_path=Path(find_kernelspec(kernel["name"])).as_posix(),
-                write_connection_file=False,
-                connection_file=kernel["server"].connection_file_path,
+        async def create_session(
+            request: Request,
+            user: User = Depends(auth.current_user(permissions={"sessions": ["write"]})),
+        ):
+            create_session = CreateSession(**(await request.json()))
+            kernel_id = create_session.kernel.id
+            kernel_name = create_session.kernel.name
+            if kernel_name is not None:
+                # launch a new ("internal") kernel
+                kernel_server = KernelServer(
+                    kernelspec_path=Path(find_kernelspec(kernel_name)).as_posix(),
+                    kernel_cwd=str(Path(create_session.path).parent),
+                )
+                kernel_id = str(uuid.uuid4())
+                kernels[kernel_id] = {"name": kernel_name, "server": kernel_server, "driver": None}
+                await kernel_server.start()
+            elif kernel_id is not None:
+                # external kernel
+                kernel_name = kernels[kernel_id]["name"]
+                kernel_server = KernelServer(
+                    connection_file=self.kernel_id_to_connection_file[kernel_id],
+                    write_connection_file=False,
+                )
+                kernels[kernel_id]["server"] = kernel_server
+                await kernel_server.start(launch_kernel=False)
+            else:
+                return
+            session_id = str(uuid.uuid4())
+            session = Session(
+                id=session_id,
+                path=create_session.path,
+                name=create_session.name,
+                type=create_session.type,
+                kernel=Kernel(
+                    id=kernel_id,
+                    name=kernel_name,
+                    connections=kernel_server.connections,
+                    last_activity=kernel_server.last_activity["date"],
+                    execution_state=kernel_server.last_activity["execution_state"],
+                ),
+                notebook=Notebook(
+                    path=create_session.path,
+                    name=create_session.name,
+                ),
             )
-            await driver.connect()
-        driver = kernel["driver"]
-
-        await driver.execute(cell)
-        ynotebook.set_cell(execution.cell_idx, cell)
+            sessions[session_id] = session
+            return session
 
-
-@router.get("/api/kernels/{kernel_id}")
-async def get_kernel(
-    kernel_id,
-    user: User = Depends(current_user(permissions={"kernels": ["read"]})),
-):
-    if kernel_id in kernels:
-        kernel = kernels[kernel_id]
-        result = {
-            "id": kernel_id,
-            "name": kernel["name"],
-            "connections": kernel["server"].connections,
-            "last_activity": kernel["server"].last_activity["date"],
-            "execution_state": kernel["server"].last_activity["execution_state"],
-        }
-        return result
-
-
-@router.websocket("/api/kernels/{kernel_id}/channels")
-async def kernel_channels(
-    kernel_id,
-    session_id,
-    websocket_permissions=Depends(websocket_auth(permissions={"kernels": ["execute"]})),
-):
-    if websocket_permissions is None:
-        return
-    websocket, permissions = websocket_permissions
-    subprotocol = (
-        "v1.kernel.websocket.jupyter.org"
-        if "v1.kernel.websocket.jupyter.org" in websocket["subprotocols"]
-        else None
-    )
-    await websocket.accept(subprotocol=subprotocol)
-    accepted_websocket = AcceptedWebSocket(websocket, subprotocol)
-    if kernel_id in kernels:
-        kernel_server = kernels[kernel_id]["server"]
-        if kernel_server is None:
-            # this is an external kernel
-            # kernel is already launched, just start a kernel server
-            kernel_server = KernelServer(
-                connection_file=kernel_id,
-                write_connection_file=False,
+        @router.post("/api/kernels/{kernel_id}/interrupt")
+        async def interrupt_kernel(
+            kernel_id,
+            user: User = Depends(auth.current_user(permissions={"kernels": ["write"]})),
+        ):
+            if kernel_id in kernels:
+                kernel = kernels[kernel_id]
+                kernel["server"].interrupt()
+                result = {
+                    "id": kernel_id,
+                    "name": kernel["name"],
+                    "connections": kernel["server"].connections,
+                    "last_activity": kernel["server"].last_activity["date"],
+                    "execution_state": kernel["server"].last_activity["execution_state"],
+                }
+                return result
+
+        @router.post("/api/kernels/{kernel_id}/restart")
+        async def restart_kernel(
+            kernel_id,
+            user: User = Depends(auth.current_user(permissions={"kernels": ["write"]})),
+        ):
+            if kernel_id in kernels:
+                kernel = kernels[kernel_id]
+                await kernel["server"].restart()
+                result = {
+                    "id": kernel_id,
+                    "name": kernel["name"],
+                    "connections": kernel["server"].connections,
+                    "last_activity": kernel["server"].last_activity["date"],
+                    "execution_state": kernel["server"].last_activity["execution_state"],
+                }
+                return result
+
+        @router.post("/api/kernels/{kernel_id}/execute")
+        async def execute_cell(
+            request: Request,
+            kernel_id,
+            user: User = Depends(auth.current_user(permissions={"kernels": ["write"]})),
+        ):
+            r = await request.json()
+            execution = Execution(**r)
+            if kernel_id in kernels:
+                ynotebook = yjs.YDocWebSocketHandler.websocket_server.get_room(
+                    execution.document_id
+                ).document
+                cell = ynotebook.get_cell(execution.cell_idx)
+                cell["outputs"] = []
+
+                kernel = kernels[kernel_id]
+                if not kernel["driver"]:
+                    kernel["driver"] = driver = KernelDriver(
+                        kernelspec_path=Path(find_kernelspec(kernel["name"])).as_posix(),
+                        write_connection_file=False,
+                        connection_file=kernel["server"].connection_file_path,
+                    )
+                    await driver.connect()
+                driver = kernel["driver"]
+
+                await driver.execute(cell)
+                ynotebook.set_cell(execution.cell_idx, cell)
+
+        @router.get("/api/kernels/{kernel_id}")
+        async def get_kernel(
+            kernel_id,
+            user: User = Depends(auth.current_user(permissions={"kernels": ["read"]})),
+        ):
+            if kernel_id in kernels:
+                kernel = kernels[kernel_id]
+                result = {
+                    "id": kernel_id,
+                    "name": kernel["name"],
+                    "connections": kernel["server"].connections,
+                    "last_activity": kernel["server"].last_activity["date"],
+                    "execution_state": kernel["server"].last_activity["execution_state"],
+                }
+                return result
+
+        @router.delete("/api/kernels/{kernel_id}", status_code=204)
+        async def shutdown_kernel(
+            kernel_id,
+            user: User = Depends(auth.current_user(permissions={"kernels": ["write"]})),
+        ):
+            if kernel_id in kernels:
+                await kernels[kernel_id]["server"].stop()
+                del kernels[kernel_id]
+            for session_id in [k for k, v in sessions.items() if v.kernel.id == kernel_id]:
+                del sessions[session_id]
+            return Response(status_code=HTTPStatus.NO_CONTENT.value)
+
+        @router.websocket("/api/kernels/{kernel_id}/channels")
+        async def kernel_channels(
+            kernel_id,
+            session_id,
+            websocket_permissions=Depends(
+                auth.websocket_auth(permissions={"kernels": ["execute"]})
+            ),
+        ):
+            if websocket_permissions is None:
+                return
+            websocket, permissions = websocket_permissions
+            subprotocol = (
+                "v1.kernel.websocket.jupyter.org"
+                if "v1.kernel.websocket.jupyter.org" in websocket["subprotocols"]
+                else None
             )
-            await kernel_server.start(launch_kernel=False)
-            kernels[kernel_id]["server"] = kernel_server
-        await kernel_server.serve(accepted_websocket, session_id, permissions)
-
-
-r = register_router(router)
+            await websocket.accept(subprotocol=subprotocol)
+            accepted_websocket = AcceptedWebSocket(websocket, subprotocol)
+            if kernel_id in kernels:
+                kernel_server = kernels[kernel_id]["server"]
+                if kernel_server is None:
+                    # this is an external kernel
+                    # kernel is already launched, just start a kernel server
+                    kernel_server = KernelServer(
+                        connection_file=kernel_id,
+                        write_connection_file=False,
+                    )
+                    await kernel_server.start(launch_kernel=False)
+                    kernels[kernel_id]["server"] = kernel_server
+                await kernel_server.serve(accepted_websocket, session_id, permissions)
+
+        self.include_router(router)
+
+        self.kernels = kernels
+
+    async def watch_connection_files(self, path: Path) -> None:
+        # first time scan, treat everything as added files
+        initial_changes = {(Change.added, str(p)) for p in path.iterdir()}
+        await self.process_connection_files(initial_changes)
+        # then, on every change
+        async for changes in awatch(path):
+            await self.process_connection_files(changes)
+
+    async def process_connection_files(self, changes: Set[Tuple[Change, str]]):
+        # get rid of "simultaneously" added/deleted files
+        file_changes: Dict[str, List[Change]] = {}
+        for c in changes:
+            change, path = c
+            if path not in file_changes:
+                file_changes[path] = []
+            file_changes[path].append(change)
+        to_delete: List[str] = []
+        for p, cs in file_changes.items():
+            if Change.added in cs and Change.deleted in cs:
+                cs.remove(Change.added)
+                cs.remove(Change.deleted)
+                if not cs:
+                    to_delete.append(p)
+        for p in to_delete:
+            del file_changes[p]
+        # process file changes
+        for path, cs in file_changes.items():
+            for change in cs:
+                if change == Change.deleted:
+                    if path in kernels:
+                        kernel_id = list(self.kernel_id_to_connection_file.keys())[
+                            list(self.kernel_id_to_connection_file.values()).index(path)
+                        ]
+                        del kernels[kernel_id]
+                elif change == Change.added:
+                    try:
+                        data = json.loads(Path(path).read_text())
+                    except BaseException:
+                        continue
+                    if "kernel_name" not in data or "key" not in data:
+                        continue
+                    # looks like a kernel connection file
+                    kernel_id = str(uuid.uuid4())
+                    self.kernel_id_to_connection_file[kernel_id] = path
+                    kernels[kernel_id] = {
+                        "name": data["kernel_name"],
+                        "server": None,
+                        "driver": None,
+                    }
```

### Comparing `fps_kernels-0.0.50/fps_kernels/kernel_driver/connect.py` & `fps_kernels-0.1.2/fps_kernels/kernel_driver/connect.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.0.50/fps_kernels/kernel_driver/driver.py` & `fps_kernels-0.1.2/fps_kernels/kernel_driver/driver.py`

 * *Files 1% similar despite different names*

```diff
@@ -85,22 +85,22 @@
         await self.kernel_process.wait()
         os.remove(self.connection_file_path)
         for task in self.channel_tasks:
             task.cancel()
 
     async def listen_iopub(self):
         while True:
-            msg = await receive_message(self.iopub_channel, change_str_to_date=True)  # type: ignore
+            msg = await receive_message(self.iopub_channel, change_str_to_date=True)
             msg_id = msg["parent_header"].get("msg_id")
             if msg_id in self.execute_requests.keys():
                 self.execute_requests[msg_id]["iopub_msg"].set_result(msg)
 
     async def listen_shell(self):
         while True:
-            msg = await receive_message(self.shell_channel, change_str_to_date=True)  # type: ignore
+            msg = await receive_message(self.shell_channel, change_str_to_date=True)
             msg_id = msg["parent_header"].get("msg_id")
             if msg_id in self.execute_requests.keys():
                 self.execute_requests[msg_id]["shell_msg"].set_result(msg)
 
     async def execute(
         self,
         cell: Dict[str, Any],
```

### Comparing `fps_kernels-0.0.50/fps_kernels/kernel_driver/kernelspec.py` & `fps_kernels-0.1.2/fps_kernels/kernel_driver/kernelspec.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.0.50/fps_kernels/kernel_driver/message.py` & `fps_kernels-0.1.2/fps_kernels/kernel_driver/message.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import hashlib
 import hmac
 from datetime import datetime, timezone
 from typing import Any, Dict, List, Optional, Tuple, cast
 from uuid import uuid4
 
-from dateutil.parser import parse as dateutil_parse  # type: ignore
+from dateutil.parser import parse as dateutil_parse
 from zmq.asyncio import Socket
 from zmq.utils import jsonapi
 
 protocol_version_info = (5, 3)
 protocol_version = "%i.%i" % protocol_version_info
 
 DELIM = b"<IDS|MSG>"
```

### Comparing `fps_kernels-0.0.50/fps_kernels/kernel_driver/paths.py` & `fps_kernels-0.1.2/fps_kernels/kernel_driver/paths.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.0.50/fps_kernels/kernel_server/message.py` & `fps_kernels-0.1.2/fps_kernels/kernel_server/message.py`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.0.50/fps_kernels/kernel_server/server.py` & `fps_kernels-0.1.2/fps_kernels/kernel_server/server.py`

 * *Files 5% similar despite different names*

```diff
@@ -2,25 +2,25 @@
 import json
 import os
 import signal
 import uuid
 from datetime import datetime
 from typing import Dict, Iterable, List, Optional, cast
 
-from fastapi import WebSocket, WebSocketDisconnect  # type: ignore
+from fastapi import WebSocket, WebSocketDisconnect
 from starlette.websockets import WebSocketState
 
 from ..kernel_driver.connect import cfg_t, connect_channel
 from ..kernel_driver.connect import launch_kernel as _launch_kernel
 from ..kernel_driver.connect import read_connection_file
 from ..kernel_driver.connect import (
-    write_connection_file as _write_connection_file,  # type: ignore
+    write_connection_file as _write_connection_file,
 )
 from ..kernel_driver.message import create_message, receive_message, send_message
-from .message import (  # type: ignore
+from .message import (
     deserialize_msg_from_ws_v1,
     from_binary,
     get_msg_from_parts,
     get_parent_header,
     get_zmq_parts,
     send_raw_message,
     serialize_msg_to_ws_v1,
@@ -146,14 +146,17 @@
                 os.remove(self.connection_file_path)
             except BaseException:
                 pass
         for task in self.channel_tasks:
             task.cancel()
         self.channel_tasks = []
 
+    def interrupt(self) -> None:
+        self.kernel_process.send_signal(signal.SIGINT)
+
     async def restart(self) -> None:
         await self.stop()
         self.setup_connection_file()
         await self.start()
 
     async def serve(
         self,
```

### Comparing `fps_kernels-0.0.50/.gitignore` & `fps_kernels-0.1.2/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.0.50/COPYING.md` & `fps_kernels-0.1.2/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_kernels-0.0.50/pyproject.toml` & `fps_kernels-0.1.2/pyproject.toml`

 * *Files 24% similar despite different names*

```diff
@@ -1,17 +1,24 @@
 [build-system]
 requires = [ "hatchling",]
 build-backend = "hatchling.build"
 
 [project]
 name = "fps_kernels"
 description = "An FPS plugin for the kernels API"
-keywords = [ "jupyter", "server", "fastapi", "pluggy", "plugins",]
+keywords = ["jupyter", "server", "fastapi", "plugins"]
 requires-python = ">=3.8"
-dependencies = [ "fps >=0.0.8", "fps-auth-base", "fps-frontend", "fps-yjs", "pyzmq", "websockets", "python-dateutil", "watchfiles >=0.16.1,<1"]
+dependencies = [
+    "pyzmq",
+    "websockets",
+    "python-dateutil",
+    "types-python-dateutil",
+    "watchfiles >=0.16.1,<1",
+    "jupyverse-api",
+]
 dynamic = [ "version",]
 [[project.authors]]
 name = "Jupyter Development Team"
 email = "jupyter@googlegroups.com"
 
 [project.readme]
 file = "README.md"
@@ -25,15 +32,13 @@
 
 [tool.check-manifest]
 ignore = [ ".*",]
 
 [tool.jupyter-releaser]
 skip = [ "check-links",]
 
-[project.entry-points.fps_router]
-fps-kernels = "fps_kernels.routes"
-
-[project.entry-points.fps_config]
-fps-kernels = "fps_kernels.config"
+[project.entry-points]
+"asphalt.components"   = {kernels = "fps_kernels.main:KernelsComponent"}
+"jupyverse.components" = {kernels = "fps_kernels.main:KernelsComponent"}
 
 [tool.hatch.version]
 path = "fps_kernels/__init__.py"
```

### Comparing `fps_kernels-0.0.50/PKG-INFO` & `fps_kernels-0.1.2/PKG-INFO`

 * *Files 27% similar despite different names*

```diff
@@ -1,23 +1,21 @@
 Metadata-Version: 2.1
 Name: fps_kernels
-Version: 0.0.50
+Version: 0.1.2
 Summary: An FPS plugin for the kernels API
 Project-URL: Homepage, https://jupyter.org
 Author-email: Jupyter Development Team <jupyter@googlegroups.com>
 License: BSD 3-Clause License
 License-File: COPYING.md
-Keywords: fastapi,jupyter,pluggy,plugins,server
+Keywords: fastapi,jupyter,plugins,server
 Requires-Python: >=3.8
-Requires-Dist: fps-auth-base
-Requires-Dist: fps-frontend
-Requires-Dist: fps-yjs
-Requires-Dist: fps>=0.0.8
+Requires-Dist: jupyverse-api
 Requires-Dist: python-dateutil
 Requires-Dist: pyzmq
+Requires-Dist: types-python-dateutil
 Requires-Dist: watchfiles<1,>=0.16.1
 Requires-Dist: websockets
 Description-Content-Type: text/markdown
 
 # fps-kernels
 
 An FPS plugin for the kernels API.
```

