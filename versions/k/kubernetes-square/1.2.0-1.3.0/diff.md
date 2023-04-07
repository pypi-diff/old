# Comparing `tmp/kubernetes-square-1.2.0.tar.gz` & `tmp/kubernetes-square-1.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kubernetes-square-1.2.0.tar", max compression
+gzip compressed data, was "kubernetes-square-1.3.0.tar", max compression
```

## Comparing `kubernetes-square-1.2.0.tar` & `kubernetes-square-1.3.0.tar`

### file list

```diff
@@ -1,14 +1,14 @@
--rw-r--r--   0        0        0    11357 2022-02-01 06:59:37.801997 kubernetes-square-1.2.0/LICENSE
--rw-r--r--   0        0        0      816 2022-02-23 05:36:54.591061 kubernetes-square-1.2.0/pyproject.toml
--rw-r--r--   0        0        0     3531 2022-02-01 06:59:37.801997 kubernetes-square-1.2.0/resources/defaultconfig.yaml
--rw-r--r--   0        0        0     1382 2022-02-23 05:36:54.591061 kubernetes-square-1.2.0/square/__init__.py
--rw-r--r--   0        0        0      203 2022-02-01 06:59:37.801997 kubernetes-square-1.2.0/square/__main__.py
--rw-r--r--   0        0        0     4805 2022-02-01 06:59:37.801997 kubernetes-square-1.2.0/square/cfgfile.py
--rw-r--r--   0        0        0     1851 2022-02-01 06:59:37.801997 kubernetes-square-1.2.0/square/dotdict.py
--rw-r--r--   0        0        0     6750 2022-02-23 05:28:06.835122 kubernetes-square-1.2.0/square/dtypes.py
--rw-r--r--   0        0        0    33546 2022-02-18 07:27:09.254404 kubernetes-square-1.2.0/square/k8s.py
--rw-r--r--   0        0        0    14906 2022-02-23 05:28:06.835122 kubernetes-square-1.2.0/square/main.py
--rw-r--r--   0        0        0    39369 2022-02-23 05:28:06.835122 kubernetes-square-1.2.0/square/manio.py
--rw-r--r--   0        0        0    29731 2022-02-23 05:28:06.835122 kubernetes-square-1.2.0/square/square.py
--rw-r--r--   0        0        0      897 2022-02-23 05:37:17.411600 kubernetes-square-1.2.0/setup.py
--rw-r--r--   0        0        0      756 2022-02-23 05:37:17.411784 kubernetes-square-1.2.0/PKG-INFO
+-rw-r--r--   0        0        0    11357 2019-10-19 08:56:49.000000 kubernetes-square-1.3.0/LICENSE
+-rw-r--r--   0        0        0      816 2023-04-07 04:24:51.071471 kubernetes-square-1.3.0/pyproject.toml
+-rw-r--r--   0        0        0     3531 2021-09-06 17:16:58.000000 kubernetes-square-1.3.0/resources/defaultconfig.yaml
+-rw-r--r--   0        0        0     1382 2023-04-07 04:24:51.071471 kubernetes-square-1.3.0/square/__init__.py
+-rw-r--r--   0        0        0      203 2021-09-06 17:16:58.000000 kubernetes-square-1.3.0/square/__main__.py
+-rw-r--r--   0        0        0     5095 2023-03-16 06:14:23.918379 kubernetes-square-1.3.0/square/cfgfile.py
+-rw-r--r--   0        0        0     1851 2021-09-06 17:16:58.000000 kubernetes-square-1.3.0/square/dotdict.py
+-rw-r--r--   0        0        0     6867 2023-03-22 01:24:34.210365 kubernetes-square-1.3.0/square/dtypes.py
+-rw-r--r--   0        0        0    33744 2023-03-22 01:24:34.210365 kubernetes-square-1.3.0/square/k8s.py
+-rw-r--r--   0        0        0    14924 2023-03-16 06:14:23.918379 kubernetes-square-1.3.0/square/main.py
+-rw-r--r--   0        0        0    39403 2023-03-16 06:14:23.918379 kubernetes-square-1.3.0/square/manio.py
+-rw-r--r--   0        0        0    29840 2023-03-16 06:14:23.918379 kubernetes-square-1.3.0/square/square.py
+-rw-r--r--   0        0        0      901 2023-04-07 05:06:46.609230 kubernetes-square-1.3.0/setup.py
+-rw-r--r--   0        0        0      610 2023-04-07 05:06:46.609397 kubernetes-square-1.3.0/PKG-INFO
```

### Comparing `kubernetes-square-1.2.0/LICENSE` & `kubernetes-square-1.3.0/LICENSE`

 * *Files identical despite different names*

### Comparing `kubernetes-square-1.2.0/pyproject.toml` & `kubernetes-square-1.3.0/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,37 +1,37 @@
 [tool.poetry]
 name = "kubernetes-square"
-version = "1.2.0"
+version = "1.3.0"
 description = ""
 authors = ["Oliver Nagy <olitheolix@gmail.com>"]
 packages = [
     { include = "square" },
 ]
 include = ["resources/defaultconfig.yaml"]
 
 
 [tool.poetry.dependencies]
 colorama = "^0.4.1"
 google = "^2.0"
 google-api-python-client = "^1.7"
 jsonpatch = "^1.24"
-python = "^3.7"
+python = "^3.10"
 pyyaml = "^5.1"
 requests = "^2.22"
 colorlog = "^4.0"
-pydantic = "=1.5.1"
+pydantic = "^1.8"
 backoff = "^1.10.0"
 
 [tool.poetry.dev-dependencies]
 bumpversion = "^0.5.3"
 flake8 = "^3.7"
 flake8-isort = "^2.7"
-ipython = "^7.8"
+ipython = "^8.10"
 isort = "^4.3"
-pytest = "^3.0"
+pytest = "^7.2"
 pytest-cov = "^2.7"
 pytest-dotenv = "^0.4.0"
 pytest-flake8 = "^1.0"
 requests-mock = "^1.7"
 sh = "^1.12"
 
 [tool.poetry.scripts]
```

### Comparing `kubernetes-square-1.2.0/resources/defaultconfig.yaml` & `kubernetes-square-1.3.0/resources/defaultconfig.yaml`

 * *Files identical despite different names*

### Comparing `kubernetes-square-1.2.0/square/__init__.py` & `kubernetes-square-1.3.0/square/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import pathlib
 import sys
 
 from . import square
 from .cfgfile import load
 
-__version__ = '1.2.0'
+__version__ = '1.3.0'
 
 
 # ---------------------------------------------------------------------------
 # Global Runtime Constants
 # ---------------------------------------------------------------------------
 # Determine the base folder. This is usually the folder of this very file, but
 # will be different if we run inside a bundle produced by PyInstaller.
```

### Comparing `kubernetes-square-1.2.0/square/cfgfile.py` & `kubernetes-square-1.3.0/square/cfgfile.py`

 * *Files 4% similar despite different names*

```diff
@@ -5,27 +5,33 @@
 dangerous, for Square to compute diffs on such field or patch them.
 
 This module defines utility functions to define these filters.
 
 """
 import copy
 import logging
+import typing
 from types import SimpleNamespace
-from typing import List, Tuple, Union
+from typing import List, Tuple
 
 import pydantic
 import yaml
 
 from square.dtypes import Config, Filepath
 
 # Convenience.
 logit = logging.getLogger("square")
 
 
-def valid(filters: List[Union[dict, list, str]]) -> bool:
+# Need to disable MyPy type checking because it would otherwise report the
+# first `if` statement as unreachable code. That warning is justified but
+# ignores the recursive nature of the function where one of the nested elements
+# may not adhere to the requirement.
+@typing.no_type_check
+def valid(filters: List[dict | list | str]) -> bool:
     """Return `True` iff `filters` is valid."""
     if not isinstance(filters, list):
         logit.error(f"<{filters}> must be a list")
         return False
 
     # Iterate over all fields of all K8s resource type.
     for el in filters:
```

### Comparing `kubernetes-square-1.2.0/square/dotdict.py` & `kubernetes-square-1.3.0/square/dotdict.py`

 * *Files identical despite different names*

### Comparing `kubernetes-square-1.2.0/square/dtypes.py` & `kubernetes-square-1.3.0/square/dtypes.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,18 +1,17 @@
+import dataclasses
 import pathlib
 from typing import (
     TYPE_CHECKING, Any, Callable, Collection, Dict, List, NamedTuple, Optional,
-    Set, Tuple, Union,
+    Set, Tuple,
 )
 
 if TYPE_CHECKING:
     from dataclasses import dataclass
 else:
-    import dataclasses
-
     from pydantic.dataclasses import dataclass
 
 # All files in Square have this type.
 Filepath = pathlib.Path
 
 # Square will first save/deploy the resources in this list in this order.
 # Afterwards it will move on to all those resources not in this list. The order
@@ -58,16 +57,18 @@
     The primary purpose of this tuple is to provide an immutable UUID that
     we can use as keys in dictionaries and sets.
 
     """
     apiVersion: str
     kind: str
     namespace: Optional[str]
-    name: str
 
+    # Every resource must have a name except for Namespaces, which encode their
+    # name in the `namespace` field.
+    name: str | None
 
 class K8sResource(NamedTuple):
     """Describe a specific K8s resource kind."""
     apiVersion: str   # "batch/v1beta1" or "extensions/v1beta1".
     kind: str         # "Deployment" (as specified in manifest)
     name: str         # "deployment" (usually lower case version of above)
     namespaced: bool  # Whether or not the resource is namespaced.
@@ -109,15 +110,15 @@
 # -----------------------------------------------------------------------------
 class JsonPatch(NamedTuple):
     """The URL for the patches as well as the patch payloads themselves."""
     # Send the patch to https://1.2.3.4/api/v1/namespace/foo/services
     url: str
 
     # The list of JSON patches.
-    ops: Collection[str]
+    ops: Collection[Dict[str, str]]
 
 
 class DeltaCreate(NamedTuple):
     meta: MetaManifest
     url: str
     manifest: Dict[str, Any]
 
@@ -193,15 +194,15 @@
     # Sort the manifest in this order, or alphabetically at the end if not in the list.
     priorities: List[str] = _factory(list(DEFAULT_PRIORITIES))
 
     # How to structure the folder directory when syncing manifests.
     groupby: GroupBy = GroupBy()
 
     # Define which fields to skip for which resource.
-    filters: Dict[str, List[Union[str, dict]]] = _factory({})
+    filters: Dict[str, List[str | dict]] = _factory({})
 
     # Callable: will be invoked for every local/server manifest that requires
     # patching before the actual patch will be computed.
     patch_callback: Optional[Callable] = None
 
     version: str = ""
```

### Comparing `kubernetes-square-1.2.0/square/k8s.py` & `kubernetes-square-1.3.0/square/k8s.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 import os
 import pathlib
 import re
 import subprocess
 import tempfile
 import warnings
 from collections import defaultdict
-from typing import Dict, List, Optional, Set, Tuple
+from typing import Collection, Dict, List, Optional, Set, Tuple
 
 import backoff
 import google.auth
 import google.auth.exceptions
 import google.auth.transport.requests
 import requests
 import yaml
@@ -32,18 +32,18 @@
 def load_kubeconfig(fname: Filepath,
                     context: Optional[str]) -> Tuple[str, dict, dict, bool]:
     """Return user name and user- and cluster information.
 
     Return None on error.
 
     Inputs:
-        fname: str
+        fname: Filepath
             Path to kubeconfig file, eg "~/.kube/config.yaml"
-        context: str
-            Kubeconf context. Use `None` to use default context.
+        context: Optional[str]
+            Kubeconf context. Use `None` to get the default context.
 
     Returns:
         name, user info, cluster info
 
     """
     # Load `kubeconfig`.
     try:
@@ -149,15 +149,15 @@
             Whether or not do disable GCloud warnings.
 
     Returns:
         Config
 
     """
     # Parse the kubeconfig file.
-    name, user, cluster, err = load_kubeconfig(fname, context)
+    _, _, cluster, err = load_kubeconfig(fname, context)
     if err:
         return (K8sConfig(), True)
 
     # Unpack the self signed certificate (Google does not register the K8s API
     # server certificate with a public CA).
     try:
         ssl_ca_cert_data = base64.b64decode(cluster["certificate-authority-data"])
@@ -170,57 +170,58 @@
     # cannot just pass it the content.
     _, tmp = tempfile.mkstemp(text=False)
     ssl_ca_cert = Filepath(tmp)
     ssl_ca_cert.write_bytes(ssl_ca_cert_data)
 
     with warnings.catch_warnings(record=disable_warnings):
         try:
-            cred, project_id = google.auth.default(
+            cred, _ = google.auth.default(
                 scopes=['https://www.googleapis.com/auth/cloud-platform']
             )
             cred.refresh(google.auth.transport.requests.Request())
             token = cred.token
         except google.auth.exceptions.DefaultCredentialsError as e:
             logit.error(str(e))
             return (K8sConfig(), True)
 
     # Return the config data.
     logit.info("Assuming GKE cluster.")
     return K8sConfig(
         url=cluster["server"],
-        token=token,
+        token=token,            # type: ignore
         ca_cert=ssl_ca_cert,
         client_cert=None,
         version="",
         name=cluster["name"],
     ), False
 
 
 def load_eks_config(
         fname: Filepath,
         context: Optional[str],
-        disable_warnings: bool = False) -> Tuple[K8sConfig, bool]:
+        _: bool = False) -> Tuple[K8sConfig, bool]:
     """Return K8s access config for EKS cluster described in `kubeconfig`.
 
     Returns None if `kubeconfig` does not exist or could not be parsed.
 
     Inputs:
         fname: Filepath
             Kubeconfig file.
         context: str
             Kubeconf context. Use `None` to use default context.
-        disable_warnings: bool
-            Whether or not do disable GCloud warnings.
+        disable_warnings: bool (unused)
+            Not used. It only exists for consistency with `load_gke_config` to
+            make those functions generic.
 
     Returns:
         Config
 
     """
     # Parse the kubeconfig file.
-    name, user, cluster, err = load_kubeconfig(fname, context)
+    user, cluster, err = load_kubeconfig(fname, context)[1:]
     if err:
         return (K8sConfig(), True)
 
     # Get a copy of all env vars. We will pass that one along to the
     # sub-process, plus the env vars specified in the kubeconfig file.
     env = os.environ.copy()
 
@@ -237,15 +238,15 @@
 
     # Convert a None value (valid value in YAML) to an empty list of env vars.
     env_kubeconf = env_kubeconf if env_kubeconf else []
 
     # Save the certificate to a temporary file. This is only necessary because
     # the Requests library will need a path to the CA file - unfortunately, we
     # cannot just pass it the content.
-    _, tmp = tempfile.mkstemp(text=False)
+    tmp = tempfile.mkstemp(text=False)[1]
     ssl_ca_cert = Filepath(tmp)
     ssl_ca_cert.write_bytes(ssl_ca_cert_data)
 
     # Compile the name, arguments and env vars for the command specified in kubeconf.
     cmd_args = [cmd] + args
     env_kubeconf = {_["name"]: _["value"] for _ in env_kubeconf}
     env.update(env_kubeconf)
@@ -287,42 +288,42 @@
 def load_minikube_config(fname: Filepath,
                          context: Optional[str]) -> Tuple[K8sConfig, bool]:
     """Load minikube configuration from `fname`.
 
     Return None on error.
 
     Inputs:
-        kubconfig: str
+        fname: Filepath
             Path to kubeconfig file, eg "~/.kube/config.yaml"
         context: str
-            Kubeconf context. Use `None` to use default context.
+            Kubeconf context. Use `None` to select default context.
 
     Returns:
         Config
 
     """
     # Parse the kubeconfig file.
-    name, user, cluster, err = load_kubeconfig(fname, context)
+    _, user, cluster, err = load_kubeconfig(fname, context)
     if err:
         return (K8sConfig(), True)
 
     # Minikube uses client certificates to authenticate. We need to pass those
     # to the HTTP client of our choice when we create the session.
     try:
         client_cert = K8sClientCert(
-            crt=user["client-certificate"],
-            key=user["client-key"],
+            crt=Filepath(user["client-certificate"]),
+            key=Filepath(user["client-key"]),
         )
 
         # Return the config data.
         logit.info("Assuming Minikube cluster.")
         return K8sConfig(
             url=cluster["server"],
             token="",
-            ca_cert=cluster["certificate-authority"],
+            ca_cert=Filepath(cluster["certificate-authority"]),
             client_cert=client_cert,
             version="",
             name=cluster["name"],
         ), False
     except KeyError:
         logit.debug(f"Context {context} in <{fname}> is not a Minikube config")
         return (K8sConfig(), True)
@@ -346,15 +347,15 @@
             Kubeconf context. Use `None` to use default context.
 
     Returns:
         Config
 
     """
     # Parse the kubeconfig file.
-    name, user, cluster, err = load_kubeconfig(fname, context)
+    _, user, cluster, err = load_kubeconfig(fname, context)
     if err:
         return (K8sConfig(), True)
 
     # Kind and Minikube use client certificates to authenticate. We need to
     # pass those to the HTTP client of our choice when we create the session.
     try:
         client_crt = base64.b64decode(user["client-certificate-data"]).decode()
@@ -581,16 +582,16 @@
     because the irregular intervals are irritating in an interactive tool.
     """
     @backoff.on_exception(backoff.constant, web_exceptions,
                           max_tries=max_tries,
                           interval=3,
                           max_time=20,
                           on_backoff=on_backoff,
-                          logger=None,
-                          jitter=None,
+                          logger=None,  # type: ignore
+                          jitter=None,  # type: ignore
                           )
     def _call(*args, **kwargs):
         return client.request(method, url, json=payload, headers=headers, timeout=30)
 
     # Make the web request via our backoff/retry handler.
     try:
         ret = _call()
@@ -632,18 +633,18 @@
     resp, code = request(client, 'GET', url, payload=None, headers=None)
     err = (code != 200)
     if err:
         logit.error(f"{code} - GET - {url} - {resp}")
     return (resp, err)
 
 
-def patch(client, url: str, payload: dict) -> Tuple[dict, bool]:
+def patch(client, url: str, payload: Collection[Dict[str, str]]) -> Tuple[dict, bool]:
     """Make PATCH requests to K8s (see `request`)."""
     headers = {'Content-Type': 'application/json-patch+json'}
-    resp, code = request(client, 'PATCH', url, payload, headers)
+    resp, code = request(client, 'PATCH', url, payload, headers)  # type: ignore
     err = (code != 200)
     if err:
         logit.error(f"{code} - PATCH - {url} - {resp}")
     return (resp, err)
 
 
 def post(client, url: str, payload: dict) -> Tuple[dict, bool]:
```

### Comparing `kubernetes-square-1.2.0/square/main.py` & `kubernetes-square-1.3.0/square/main.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 import logging
 import os
 from typing import Optional, Tuple
 
 import colorama
 
 import square
+import square.k8s
 import square.square
 from square import DEFAULT_CONFIG_FILE, __version__
 from square.dtypes import Config, Filepath, GroupBy, Selectors
 
 # Convenience: global logger instance to avoid repetitive code.
 logit = logging.getLogger("square")
```

### Comparing `kubernetes-square-1.2.0/square/manio.py` & `kubernetes-square-1.3.0/square/manio.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,14 +4,15 @@
 import logging
 import multiprocessing
 import pathlib
 from typing import (
     Collection, DefaultDict, Dict, Iterable, List, Optional, Tuple,
 )
 
+import yaml.parser
 import yaml.scanner
 
 import square.cfgfile
 import square.dotdict
 import square.k8s
 from square.dtypes import (
     Config, Filepath, GroupBy, K8sConfig, K8sResource, LocalManifestLists,
@@ -235,15 +236,14 @@
     with multiprocessing.Pool() as pool:
         # Compile the arguments for the worker processes that we will use to
         # load the YAML files.
         funargs = sorted(file_yaml.items())
         fnames = sorted(list(file_yaml))
 
         # Parse the YAMLs in a process pool.
-        ret: Collection[Tuple[MetaManifest, dict]]
         for fname, (manifests, err) in zip(fnames, pool.starmap(_parse_worker, funargs)):
             if err:
                 return ({}, err)
 
             # Remove all empty manifests. This typically happens when the YAML
             # file ends with a "---" string.
             manifests = [_ for _ in manifests if _ is not None]
@@ -498,20 +498,21 @@
             See tests for examples
 
     Returns:
         dict, dict: (stripped manifest, removed keys).
 
     """
     # Convenience: default return value if an error occurs.
-    ret_err: Tuple[DotDict, dict, bool] = (square.dotdict.make({}), {}, True)
+    ret_err: Tuple[DotDict, dict, bool] = (
+        square.dotdict.make({}), {}, True) # type: ignore
 
     # Parse the manifest.
     try:
         meta = make_meta(manifest)
-        resource, err = square.k8s.resource(k8sconfig, meta)
+        _, err = square.k8s.resource(k8sconfig, meta)
         assert not err
     except KeyError as e:
         logit.error(f"Manifest is missing the <{e.args[0]}> key.")
         return ret_err
     except AssertionError:
         return ret_err
 
@@ -571,21 +572,21 @@
     filters = manifest_filters.get(
         kind,
         square.DEFAULT_CONFIG.filters.get(
             kind,
             square.DEFAULT_CONFIG.filters["_common_"]
         )
     )
-    if not square.cfgfile.valid(filters):
+    if not square.cfgfile.valid(filters):  # type: ignore
         return ret_err
 
     # Remove the keys from the `manifest` according to `filters`.
     manifest = copy.deepcopy(manifest)
     removed = _update(filters, manifest)
-    return (square.dotdict.make(manifest), removed, False)
+    return (square.dotdict.make(manifest), removed, False)  # type: ignore
 
 
 def align_serviceaccount(
         local_manifests: ServerManifests,
         server_manifests: ServerManifests) -> Tuple[ServerManifests, bool]:
     """Insert the token secret from `server_manifest` into `local_manifest`.
 
@@ -676,15 +677,15 @@
     server_meta = set(server_manifests.keys()).intersection(local_meta)
 
     # Iterate over all ServiceAccount manifests and insert the secret token
     # from the cluster into the local manifest.
     for meta in server_meta:
         # Find the service account token in the local/cluster manifest.
         loc_token, loc_secrets, err1 = _get_token(meta, local_manifests)
-        srv_token, srv_secrets, err2 = _get_token(meta, server_manifests)
+        srv_token, _, err2 = _get_token(meta, server_manifests)
 
         # Ignore the manifest if there was an error. Typically this means the
         # local or cluster manifest defined multiple service account secrets.
         # If that happens then something is probably seriously wrong with the
         # cluster.
         if err1 or err2:
             continue
@@ -863,15 +864,15 @@
 
     """
     # Sort the manifests in each file.
     out: Dict[Filepath, Collection[MetaManifest]] = {}
     for fname, manifests in file_manifests.items():
         # Group the manifests by their "kind" in order of `priority` and sort
         # each group alphabetically.
-        man_sorted: List[dict] = []
+        man_sorted: list = []
         for kind in priority:
             # Partition the manifest list into the current `kind` and the rest.
             tmp = [_ for _ in manifests if _[0].kind == kind]
             manifests = [_ for _ in manifests if _[0].kind != kind]
 
             # Append the manifests ordered by their MetaManifest.
             man_sorted += sorted(tmp, key=lambda _: _[0])
@@ -931,14 +932,15 @@
     del out_nonempty
 
     # Ignore all hidden files.
     out_clean = {k: v for k, v in out_clean.items() if not k.name.startswith(".")}
 
     # Convert all manifest dicts into YAML strings.
     out_final: Dict[Filepath, str] = {}
+    fname: Filepath = Filepath()
     try:
         for fname, v in out_clean.items():
             out_final[fname] = yaml.dump_all(v, default_flow_style=False,
                                              Dumper=Dumper)
     except yaml.YAMLError as e:
         logit.error(
             f"YAML error. Cannot create <{fname}>: {e.args[0]} <{str(e.args[1])}>"
```

### Comparing `kubernetes-square-1.2.0/square/square.py` & `kubernetes-square-1.3.0/square/square.py`

 * *Files 1% similar despite different names*

```diff
@@ -293,40 +293,40 @@
     """
     err_resp = (DeploymentPlan(tuple(), tuple(), tuple()), True)
 
     # Abort unless all local manifests reference valid K8s resource kinds.
     if any([k8s.resource(k8sconfig, meta)[1] for meta in local]):
         return err_resp
 
-    # Replace the server resources fetched from the K8s preferred endpoint with
-    # those fetched from the endpoint used by the local manifest.
+    # Replace the server resources fetched from K8s' preferred endpoint with
+    # those from the endpoint declared in the local manifest.
     server, err = match_api_version(k8sconfig, local, server)
     assert not err
 
     # Apply the filters to all local and server manifests before we compute patches.
     server = {
         meta: manio.strip(k8sconfig, man, config.filters)
         for meta, man in server.items()
-    }
+    }                           # type: ignore
     local = {
         meta: manio.strip(k8sconfig, man, config.filters)
         for meta, man in local.items()
-    }
+    }                           # type: ignore
 
     # Abort if any of the manifests could not be stripped.
     err_srv = {_[2] for _ in server.values()}
     err_loc = {_[2] for _ in local.values()}
     if True in err_srv or True in err_loc:
         logit.error("Could not strip all manifests.")
         return err_resp
 
     # Unpack the stripped manifests (first element in the tuple returned from
     # `manio.strip`).
-    server = {k: dotdict.undo(v[0]) for k, v in server.items()}
-    local = {k: dotdict.undo(v[0]) for k, v in local.items()}
+    server = {k: dotdict.undo(v[0]) for k, v in server.items()}  # type: ignore
+    local = {k: dotdict.undo(v[0]) for k, v in local.items()}    # type: ignore
 
     # Partition the set of meta manifests into create/delete/patch groups.
     plan, err = partition_manifests(local, server)
     if err:
         logit.error("Could not partition the manifests for the plan.")
         return err_resp
```

### Comparing `kubernetes-square-1.2.0/setup.py` & `kubernetes-square-1.3.0/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -10,33 +10,33 @@
 install_requires = \
 ['backoff>=1.10.0,<2.0.0',
  'colorama>=0.4.1,<0.5.0',
  'colorlog>=4.0,<5.0',
  'google-api-python-client>=1.7,<2.0',
  'google>=2.0,<3.0',
  'jsonpatch>=1.24,<2.0',
- 'pydantic==1.5.1',
+ 'pydantic>=1.8,<2.0',
  'pyyaml>=5.1,<6.0',
  'requests>=2.22,<3.0']
 
 entry_points = \
 {'console_scripts': ['square = square.main:main']}
 
 setup_kwargs = {
     'name': 'kubernetes-square',
-    'version': '1.2.0',
+    'version': '1.3.0',
     'description': '',
     'long_description': None,
     'author': 'Oliver Nagy',
     'author_email': 'olitheolix@gmail.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': None,
     'packages': packages,
     'package_data': package_data,
     'install_requires': install_requires,
     'entry_points': entry_points,
-    'python_requires': '>=3.7,<4.0',
+    'python_requires': '>=3.10,<4.0',
 }
 
 
 setup(**setup_kwargs)
```

### Comparing `kubernetes-square-1.2.0/PKG-INFO` & `kubernetes-square-1.3.0/PKG-INFO`

 * *Files 21% similar despite different names*

```diff
@@ -1,21 +1,18 @@
 Metadata-Version: 2.1
 Name: kubernetes-square
-Version: 1.2.0
+Version: 1.3.0
 Summary: 
 Author: Oliver Nagy
 Author-email: olitheolix@gmail.com
-Requires-Python: >=3.7,<4.0
+Requires-Python: >=3.10,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
 Requires-Dist: backoff (>=1.10.0,<2.0.0)
 Requires-Dist: colorama (>=0.4.1,<0.5.0)
 Requires-Dist: colorlog (>=4.0,<5.0)
 Requires-Dist: google (>=2.0,<3.0)
 Requires-Dist: google-api-python-client (>=1.7,<2.0)
 Requires-Dist: jsonpatch (>=1.24,<2.0)
-Requires-Dist: pydantic (==1.5.1)
+Requires-Dist: pydantic (>=1.8,<2.0)
 Requires-Dist: pyyaml (>=5.1,<6.0)
 Requires-Dist: requests (>=2.22,<3.0)
```

