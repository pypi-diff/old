# Comparing `tmp/vt2m-0.1.8.tar.gz` & `tmp/vt2m-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "vt2m-0.1.8.tar", max compression
+gzip compressed data, was "vt2m-0.1.9.tar", max compression
```

## Comparing `vt2m-0.1.8.tar` & `vt2m-0.1.9.tar`

### file list

```diff
@@ -1,13 +1,13 @@
--rw-r--r--   0        0        0    88975 2022-03-28 09:00:26.878409 vt2m-0.1.8/.github/screenshots/graph.png
--rw-r--r--   0        0        0     1069 2022-03-16 22:14:15.011518 vt2m-0.1.8/LICENSE
--rw-r--r--   0        0        0     2414 2022-03-31 10:09:58.807120 vt2m-0.1.8/README.md
--rw-r--r--   0        0        0     1189 2023-02-15 15:36:07.964413 vt2m-0.1.8/pyproject.toml
--rw-r--r--   0        0        0        0 2022-03-16 21:54:37.189203 vt2m-0.1.8/vt2m/__init__.py
--rw-r--r--   0        0        0        0 2022-05-16 13:46:45.695509 vt2m-0.1.8/vt2m/lib/__init__.py
--rw-r--r--   0        0        0    26174 2023-02-15 15:36:07.964807 vt2m-0.1.8/vt2m/lib/lib.py
--rw-r--r--   0        0        0     1759 2022-05-16 13:46:45.697447 vt2m-0.1.8/vt2m/lib/output.py
--rw-r--r--   0        0        0     3462 2023-02-15 15:36:07.965118 vt2m-0.1.8/vt2m/main.py
--rw-r--r--   0        0        0     4251 2022-05-16 13:46:45.697978 vt2m-0.1.8/vt2m/subcommands/notifications.py
--rw-r--r--   0        0        0     4147 2022-05-16 13:46:45.698193 vt2m-0.1.8/vt2m/subcommands/retrohunts.py
--rw-r--r--   0        0        0     3336 1970-01-01 00:00:00.000000 vt2m-0.1.8/setup.py
--rw-r--r--   0        0        0     3770 1970-01-01 00:00:00.000000 vt2m-0.1.8/PKG-INFO
+-rw-r--r--   0        0        0    88975 2022-03-28 09:00:26.878409 vt2m-0.1.9/.github/screenshots/graph.png
+-rw-r--r--   0        0        0     1069 2022-03-16 22:14:15.011518 vt2m-0.1.9/LICENSE
+-rw-r--r--   0        0        0     2414 2022-03-31 10:09:58.807120 vt2m-0.1.9/README.md
+-rw-r--r--   0        0        0     1189 2023-03-20 14:42:05.782872 vt2m-0.1.9/pyproject.toml
+-rw-r--r--   0        0        0        0 2022-03-16 21:54:37.189203 vt2m-0.1.9/vt2m/__init__.py
+-rw-r--r--   0        0        0        0 2022-05-16 13:46:45.695509 vt2m-0.1.9/vt2m/lib/__init__.py
+-rw-r--r--   0        0        0    28279 2023-03-20 14:42:05.783424 vt2m-0.1.9/vt2m/lib/lib.py
+-rw-r--r--   0        0        0     1759 2022-05-16 13:46:45.697447 vt2m-0.1.9/vt2m/lib/output.py
+-rw-r--r--   0        0        0     4494 2023-03-20 14:42:05.784104 vt2m-0.1.9/vt2m/main.py
+-rw-r--r--   0        0        0     4304 2023-03-20 14:42:05.785402 vt2m-0.1.9/vt2m/subcommands/notifications.py
+-rw-r--r--   0        0        0     4528 2023-03-20 14:42:05.786398 vt2m-0.1.9/vt2m/subcommands/retrohunts.py
+-rw-r--r--   0        0        0     3336 1970-01-01 00:00:00.000000 vt2m-0.1.9/setup.py
+-rw-r--r--   0        0        0     3770 1970-01-01 00:00:00.000000 vt2m-0.1.9/PKG-INFO
```

### Comparing `vt2m-0.1.8/.github/screenshots/graph.png` & `vt2m-0.1.9/.github/screenshots/graph.png`

 * *Files identical despite different names*

### Comparing `vt2m-0.1.8/LICENSE` & `vt2m-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `vt2m-0.1.8/README.md` & `vt2m-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `vt2m-0.1.8/pyproject.toml` & `vt2m-0.1.9/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "vt2m"
-version = "0.1.8"
+version = "0.1.9"
 description = "Automatically import results from VirusTotal queries into MISP objects"
 authors = ["3c7 <3c7@posteo.de>"]
 license = "MIT"
 readme = "README.md"
 homepage = "https://github.com/3c7/vt2m"
 repository = "https://github.com/3c7/vt2m"
 classifiers = [
```

### Comparing `vt2m-0.1.8/vt2m/lib/lib.py` & `vt2m-0.1.9/vt2m/lib/lib.py`

 * *Files 2% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 from datetime import datetime
 from typing import Generator, Union, List, Optional, Dict
 from urllib.parse import quote_plus, urlparse
 
 import requests
 import typer
 from pymisp import MISPEvent, MISPObject
-from vt import Client as VTClient, ClientResponse
+from vt import Client as VTClient
 
 from vt2m.lib.output import print, print_err
 
 file_relations = ["execution_parents", "compressed_parents", "bundled_files", "dropped_files"]
 url_relations = ["contacted_urls", "embedded_urls", "itw_urls"]
 domain_relations = ["contacted_domains", "embedded_domains", "itw_domains"]
 ip_relations = ["contacted_ips", "embedded_ips", "itw_ips"]
@@ -499,14 +499,56 @@
     """Loops over given relationships and returns true if any relationship references the given uuid and type."""
     for ref in obj.references:
         if ref.referenced_uuid == referenced_uuid and ref.relationship_type == relationship_type:
             return True
     return False
 
 
+def pivot_from_hash(
+        *,
+        api_key: str,
+        sha256_hash: str,
+        rel: str,
+        limit: int = 40,
+        disable_output: bool = False
+):
+    """Pivots from a hash and retrieves file objects in 'rel' relation. Returns a list of VT dictionary objects."""
+    if not disable_output:
+        print(f"[PIV] Pivot to {rel} from {sha256_hash}.")
+
+    data = []
+    with VTClient(api_key) as client:
+        cursor = ""
+        while limit > 0:
+            query_limit = limit if limit <= 40 else 40
+            limit -= limit if limit <= 40 else 40
+            url = f"/files/{sha256_hash}/{rel}?limit={query_limit}"
+            if cursor != "":
+                url += f"&cursor={cursor}"
+            res = client.get(url).json()
+
+            if "error" in res:
+                print_err(f"[PIV] Error during receiving related objects: {res['error']}.")
+                return []
+
+            data.extend(res["data"])
+
+            meta = res.get("meta", {})
+            if "cursor" in meta:
+                cursor = meta["cursor"]
+            else:
+                # Reset cursor and set limit to 0 in order to exit the loop
+                cursor = ""
+                limit = 0
+    if not disable_output:
+        for d in data:
+            print(f"[PIV] Got {d['attributes']['sha256']}.")
+    return data
+
+
 def get_related_objects(
         *, api_key: str, obj: MISPObject, rel: str, limit: int = 40, disable_output: bool = False
 ) -> List[Dict]:
     """Gets related objects from VT."""
     if obj.name == "file":
         vt_id = obj.get_attributes_by_relation("sha256")[0].value
     elif obj.name == "domain-ip":
@@ -556,23 +598,46 @@
 
 def get_vt_notifications(
         vt_key: str,
         filter: Optional[str] = None,
         limit: int = 10
 ) -> List:
     """Requests notifications from VT API. Applies an optional filter."""
+    max_limit = limit
+    if max_limit > 40:
+        max_limit -= 40
+        limit = 40
     url = f"https://www.virustotal.com/api/v3/intelligence/hunting_notification_files?limit={limit}"
     if filter:
         url += f"&filter={quote_plus(filter)}"
 
     data = vt_request(api_key=vt_key, url=url)
     if "error" in data:
         print_err(f"[ERR] Error occured during receiving notifications: {data['error']}")
         return []
-    return data["data"]
+
+    results = data.get("data", [])
+    while "cursor" in data.get("meta", {}) and max_limit:
+        if max_limit > 40:
+            max_limit -= 40
+            limit = 40
+        else:
+            limit = max_limit
+            max_limit = 0
+        url = f"https://www.virustotal.com/api/v3/intelligence/hunting_notification_files?limit={limit}" \
+              f"&cursor={data['meta']['cursor']}"
+        if filter:
+            url += f"&filter={quote_plus(filter)}"
+
+        data = vt_request(api_key=vt_key, url=url)
+        if "error" in data:
+            print_err(f"[ERR] Error occured during receiving notifications: {data['error']}")
+            break
+        results.extend(data.get("data", []))
+    return results
 
 
 def create_domain_from_url(event: MISPEvent, domain: str, u_obj: MISPObject, disable_output: bool = False):
     """Creates domain object from url object and adds a relation."""
     if domain and len(domain) > 0:
         if re.fullmatch(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", domain):
             attribute_type = "ip"
@@ -627,15 +692,15 @@
     data = vt_request(api_key=vt_key, url=url)
     if "error" in data:
         print_err(f"[ERR] Error occured during receiving notifications: {data['error']}")
         return []
     return data["data"]
 
 
-def get_retrohunt_rules(r: Dict) -> List[str]:
+def get_retrohunt_rule_names(r: Dict) -> List[str]:
     """Extracts rules used within a retrohunt."""
     rules = []
     for line in r.get("attributes", {}).get("rules", "").splitlines():
         line = line.strip()
         if "rule" in line[:4]:
             line = line.split("{")[0]
             line = line.split(":")[0]
```

### Comparing `vt2m-0.1.8/vt2m/lib/output.py` & `vt2m-0.1.9/vt2m/lib/output.py`

 * *Files identical despite different names*

### Comparing `vt2m-0.1.8/vt2m/subcommands/notifications.py` & `vt2m-0.1.9/vt2m/subcommands/notifications.py`

 * *Files 2% similar despite different names*

```diff
@@ -8,17 +8,17 @@
 from vt2m.lib.output import print_file_object
 
 app = typer.Typer(help="Query and process VT notifications")
 
 
 @app.command("list")
 def list_notifications(
-        vt_key: str = typer.Option(None, help="VT API Key - can also be set via VT_KEY env"),
-        filter: str = typer.Option("", help="Filter to be used for filtering notifications"),
-        limit: int = typer.Option(10, help="Amount of notifications to grab"),
+        vt_key: str = typer.Option(None, "-k", "--vt-key", help="VT API Key - can also be set via VT_KEY env"),
+        filter: str = typer.Option("", "-f", "--filter", help="Filter to be used for filtering notifications"),
+        limit: int = typer.Option(10, "-l", "--limit", help="Amount of notifications to grab"),
         sha256: bool = typer.Option(False, "-s", "--sha256", help="Only show sha256 hashes")
 ):
     """List currently available VirusTotal notifications"""
     if not vt_key:
         vt_key = os.getenv("VT_KEY")
 
     if not all([vt_key]):
```

### Comparing `vt2m-0.1.8/vt2m/subcommands/retrohunts.py` & `vt2m-0.1.9/vt2m/subcommands/retrohunts.py`

 * *Files 15% similar despite different names*

```diff
@@ -2,30 +2,31 @@
 from typing import List
 
 import typer
 from pymisp import PyMISP
 
 from vt2m.lib.lib import (
     get_vt_retrohunts,
-    get_retrohunt_rules,
+    get_retrohunt_rule_names,
     get_vt_retrohunt_files,
     process_results,
     process_relations
 )
 from vt2m.lib.output import print, print_err, print_file_object
 
 app = typer.Typer(help="Query for retrohunt results.")
 
 
 @app.command("list")
 def list_retrohunts(
         vt_key: str = typer.Option(None, help="VT API Key - can also be set via VT_KEY env"),
         limit: int = typer.Option(40, help="Limit of retrohunts to return"),
         filter: str = typer.Option("", help="Text filter to apply"),
-        rules: bool = typer.Option(False, help="Show rules")
+        rules: bool = typer.Option(False, "-r", "--rules", help="Show rulenames"),
+        full_rules: bool = typer.Option(False, "-R", "--full-rules", help="Show full rules")
 ):
     """Lists available retrohunts"""
     if not vt_key:
         vt_key = os.getenv("VT_KEY", None)
 
     if not vt_key:
         print_err("[ERR] VirusTotal key must be given.")
@@ -41,15 +42,19 @@
         raise typer.Exit(-1)
 
     print(f"{'ID':<25}{'Status':<15}{'Finished Date':<25}Matches")
     for item in retrohunts:
         print_file_object(item, "id,25", "attributes.status,15", "attributes.finish_date,25", "attributes.num_matches")
         if rules:
             print("Rules: ", nl=False)
-            print(", ".join(get_retrohunt_rules(item)))
+            print(", ".join(get_retrohunt_rule_names(item)))
+        elif full_rules:
+            print("----------------------------------------------------------------------")
+            print(item["attributes"]["rules"])
+            print("----------------------------------------------------------------------")
 
 
 @app.command("import")
 def import_retrohunt(
         rid: str = typer.Argument(..., help="Retrohunt ID"),
         vt_key: str = typer.Option(None, help="VT API Key - can also be set via VT_KEY env"),
         uuid: str = typer.Option(..., "--uuid", "-u", help="MISP event UUID"),
```

### Comparing `vt2m-0.1.8/setup.py` & `vt2m-0.1.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -14,15 +14,15 @@
  'vt-py>=0.17.4,<0.18.0']
 
 entry_points = \
 {'console_scripts': ['vt2m = vt2m.main:app']}
 
 setup_kwargs = {
     'name': 'vt2m',
-    'version': '0.1.8',
+    'version': '0.1.9',
     'description': 'Automatically import results from VirusTotal queries into MISP objects',
     'long_description': '# VirusTotal Query to MISP Objects (vt2m)\n\nWhile there are multiple Python projects which implement the object creation based on single VirusTotal objects, this\nproject aims to enable users to directly convert VirusTotal search queries to MISP objects.\n**This is work in progress.** Future release will implement handling URLs, Domain and IP objects, too. Right now, only\nfile objects are implemented.\n\n## Installation\n\n```\npip install vt2m\n```\n\n## Usage\n\nIf you use the script frequently, passing the arguments as environment variables (`MISP_URL`, `MISP_KEY`, `VT_KEY`)\ncan be useful to save some time. For example, this can be achieved through creating a shell script which passes the\nenvironment variables and executes the command with spaces in front, so it does not show up in the shell history.\n\nVia `--relations` VirusTotal relations can be resolved and added as MISP objects with the specific relations, e.g. the\nfollowing graph was created using vt2m:\n![MISP Graph](.github/screenshots/graph.png)\n*Graph created via `vt2m --uuid <UUID> --limit 5 --relations dropped_files,execution_parents "behaviour_processes:\\"ping -n 70\\""`*\n\n### Params\n```\nusage: vt2m [-h] --uuid UUID [--url URL] [--key KEY] [--vt-key VT_KEY] [--comment COMMENT] [--limit LIMIT] [--relations RELATIONS] [--quiet]\n            [--detections DETECTIONS]\n            query\n\npositional arguments:\n  query                 VT query\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --uuid UUID, -u UUID  MISP event uuid\n  --url URL, -U URL     MISP URL - can also be given as env MISP_URL\n  --key KEY, -k KEY     MISP API key - can also be given as env MISP_KEY\n  --vt-key VT_KEY, -K VT_KEY\n                        VT API key - can also be given as env VT_KEY\n  --comment COMMENT, -c COMMENT\n                        Comment to add to MISP objects\n  --limit LIMIT, -l LIMIT\n                        Limit results of VT query - default is 100\n  --relations RELATIONS, -r RELATIONS\n                        Comma-seperated list of relations to request PER result (if type fits). This can burn your API credits. Currently\n                        implemented: dropped_files, executing_parents, bundled_files\n  --quiet, -q           Disable output. Stderr will still be printed.\n  --detections DETECTIONS, -d DETECTIONS\n                        Only consider related entities with at least X malicious detections.\n```\n',
     'author': '3c7',
     'author_email': '3c7@posteo.de',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://github.com/3c7/vt2m',
```

### Comparing `vt2m-0.1.8/PKG-INFO` & `vt2m-0.1.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vt2m
-Version: 0.1.8
+Version: 0.1.9
 Summary: Automatically import results from VirusTotal queries into MISP objects
 Home-page: https://github.com/3c7/vt2m
 License: MIT
 Author: 3c7
 Author-email: 3c7@posteo.de
 Requires-Python: >=3.8,<4.0
 Classifier: Development Status :: 4 - Beta
```

