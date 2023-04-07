# Comparing `tmp/superinference-1.0.4.tar.gz` & `tmp/superinference-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "superinference-1.0.4.tar", last modified: Fri Apr  7 03:53:22 2023, max compression
+gzip compressed data, was "superinference-1.0.9.tar", last modified: Tue Mar 21 09:44:20 2023, max compression
```

## Comparing `superinference-1.0.4.tar` & `superinference-1.0.9.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 03:53:22.542507 superinference-1.0.4/
--rw-rw-rw-   0        0        0     1069 2023-03-21 13:42:01.000000 superinference-1.0.4/LICENSE.txt
--rw-rw-rw-   0        0        0     5394 2023-04-07 03:53:22.542507 superinference-1.0.4/PKG-INFO
--rw-rw-rw-   0        0        0     3953 2023-03-28 10:18:49.000000 superinference-1.0.4/README.md
--rw-rw-rw-   0        0        0       97 2023-03-21 13:42:01.000000 superinference-1.0.4/pyproject.toml
--rw-rw-rw-   0        0        0      531 2023-04-07 03:53:22.548134 superinference-1.0.4/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-04-07 03:53:22.490267 superinference-1.0.4/src/
-drwxrwxrwx   0        0        0        0 2023-04-07 03:53:22.522439 superinference-1.0.4/src/superinference/
--rw-rw-rw-   0        0        0        0 2023-03-21 09:18:24.000000 superinference-1.0.4/src/superinference/__init__.py
--rw-rw-rw-   0        0        0     1095 2023-03-22 03:35:34.000000 superinference-1.0.4/src/superinference/devto.py
--rw-rw-rw-   0        0        0    24904 2023-04-07 02:51:30.000000 superinference-1.0.4/src/superinference/github.py
-drwxrwxrwx   0        0        0        0 2023-04-07 03:53:22.540509 superinference-1.0.4/src/superinference.egg-info/
--rw-rw-rw-   0        0        0     5394 2023-04-07 03:53:22.000000 superinference-1.0.4/src/superinference.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      314 2023-04-07 03:53:22.000000 superinference-1.0.4/src/superinference.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 03:53:22.000000 superinference-1.0.4/src/superinference.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       15 2023-04-07 03:53:22.000000 superinference-1.0.4/src/superinference.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-03-21 09:44:20.244631 superinference-1.0.9/
+-rw-rw-rw-   0        0        0     1069 2023-03-21 06:25:25.000000 superinference-1.0.9/LICENSE.txt
+-rw-rw-rw-   0        0        0     2258 2023-03-21 09:44:20.244631 superinference-1.0.9/PKG-INFO
+-rw-rw-rw-   0        0        0      817 2023-03-21 06:24:53.000000 superinference-1.0.9/README.md
+-rw-rw-rw-   0        0        0       97 2023-03-09 12:43:33.000000 superinference-1.0.9/pyproject.toml
+-rw-rw-rw-   0        0        0      531 2023-03-21 09:44:20.250065 superinference-1.0.9/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-03-21 09:44:20.184084 superinference-1.0.9/src/
+drwxrwxrwx   0        0        0        0 2023-03-21 09:44:20.221953 superinference-1.0.9/src/superinference/
+-rw-rw-rw-   0        0        0        0 2023-03-21 09:18:24.000000 superinference-1.0.9/src/superinference/__init__.py
+-rw-rw-rw-   0        0        0      886 2023-03-21 07:59:16.000000 superinference-1.0.9/src/superinference/devto.py
+-rw-rw-rw-   0        0        0    17354 2023-03-21 08:30:27.000000 superinference-1.0.9/src/superinference/github.py
+drwxrwxrwx   0        0        0        0 2023-03-21 09:44:20.242126 superinference-1.0.9/src/superinference.egg-info/
+-rw-rw-rw-   0        0        0     2258 2023-03-21 09:44:20.000000 superinference-1.0.9/src/superinference.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      314 2023-03-21 09:44:20.000000 superinference-1.0.9/src/superinference.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-21 09:44:20.000000 superinference-1.0.9/src/superinference.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       15 2023-03-21 09:44:20.000000 superinference-1.0.9/src/superinference.egg-info/top_level.txt
```

### Comparing `superinference-1.0.4/LICENSE.txt` & `superinference-1.0.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `superinference-1.0.4/setup.cfg` & `superinference-1.0.9/setup.cfg`

 * *Files 18% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 00000000: 5b6d 6574 6164 6174 615d 0d0a 6e61 6d65  [metadata]..name
 00000010: 203d 2073 7570 6572 696e 6665 7265 6e63   = superinferenc
 00000020: 650d 0a76 6572 7369 6f6e 203d 2031 2e30  e..version = 1.0
-00000030: 2e34 0d0a 6465 7363 7269 7074 696f 6e20  .4..description 
+00000030: 2e39 0d0a 6465 7363 7269 7074 696f 6e20  .9..description 
 00000040: 3d20 5375 7065 7269 6e66 6572 656e 6365  = Superinference
 00000050: 2069 7320 6120 6c69 6272 6172 7920 7468   is a library th
 00000060: 6174 2069 6e66 6572 7320 616e 616c 7973  at infers analys
 00000070: 6973 2d72 6561 6479 2061 7474 7269 6275  is-ready attribu
 00000080: 7465 7320 6672 6f6d 2061 2070 6572 736f  tes from a perso
 00000090: 6e27 2773 2073 6f63 6961 6c20 6d65 6469  n''s social medi
 000000a0: 6120 7573 6572 6e61 6d65 206f 7220 756e  a username or un
```

### Comparing `superinference-1.0.4/src/superinference/devto.py` & `superinference-1.0.9/src/superinference/devto.py`

 * *Files 19% similar despite different names*

```diff
@@ -2,32 +2,24 @@
 from rich.console import Console
 from rich.theme import Theme
 
 console = Console(theme=Theme({"repr.str":"#54A24B", "repr.number": "#FF7F0E", "repr.none":"#808080"}))
 
 class DevtoProfile:
     def __init__(self, username):
-        """Dev.to profile inference class
-
-        Args:
-            username (str): Dev.to username
-        """
         self.username = username
-        self.inference = None
-        self._api_url = "https://dev.to/api"
+        self.api_url = "https://dev.to/api"
 
     def perform_inference(self):
-        """Performs inference on the Dev.to profile
-        
-        Returns:
-            dict: Dev.to profile data
-        """
-        url = f"{self._api_url}/users/by_username?url={self.username}"
+        url = f"{self.api_url}/users/by_username?url={self.username}"
         response = requests.get(url)
         if response.status_code == 200:
-            self.inference = response.json()
-            console.print(self.inference)
+            data = response.json()
+            return data
         elif response.status_code == 404:
             raise Exception("Invalid Dev.to username inputted.")
         else:
             raise Exception(f"Error with status code of: {response.status_code}")
-    
+    
+    def pprint_inference(self):
+        data = self.perform_inference()
+        console.print(data)
```

