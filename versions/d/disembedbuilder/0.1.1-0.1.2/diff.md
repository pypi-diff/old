# Comparing `tmp/disembedbuilder-0.1.1.tar.gz` & `tmp/disembedbuilder-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "disembedbuilder-0.1.1.tar", last modified: Fri Mar 17 14:31:23 2023, max compression
+gzip compressed data, was "disembedbuilder-0.1.2.tar", last modified: Thu Apr  6 15:33:14 2023, max compression
```

## Comparing `disembedbuilder-0.1.1.tar` & `disembedbuilder-0.1.2.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxrwx   0        0        0        0 2023-03-17 14:31:23.319306 disembedbuilder-0.1.1/
--rw-rw-rw-   0        0        0     1069 2023-03-17 14:25:29.000000 disembedbuilder-0.1.1/LICENSE
--rw-rw-rw-   0        0        0      620 2023-03-17 14:31:23.319306 disembedbuilder-0.1.1/PKG-INFO
--rw-rw-rw-   0        0        0      110 2022-09-01 15:27:20.000000 disembedbuilder-0.1.1/README.md
--rw-rw-rw-   0        0        0      108 2023-03-17 14:25:40.000000 disembedbuilder-0.1.1/pyproject.toml
--rw-rw-rw-   0        0        0      643 2023-03-17 14:31:23.320306 disembedbuilder-0.1.1/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-03-17 14:31:23.309343 disembedbuilder-0.1.1/src/
-drwxrwxrwx   0        0        0        0 2023-03-17 14:31:23.315306 disembedbuilder-0.1.1/src/disembedbuilder/
--rw-rw-rw-   0        0        0       32 2023-03-17 09:52:50.000000 disembedbuilder-0.1.1/src/disembedbuilder/__init__.py
--rw-rw-rw-   0        0        0    23254 2023-03-17 14:21:57.000000 disembedbuilder-0.1.1/src/disembedbuilder/disembedbuilder.py
--rw-rw-rw-   0        0        0      698 2023-03-17 13:35:56.000000 disembedbuilder-0.1.1/src/disembedbuilder/preembeds.py
-drwxrwxrwx   0        0        0        0 2023-03-17 14:31:23.318307 disembedbuilder-0.1.1/src/disembedbuilder.egg-info/
--rw-rw-rw-   0        0        0      620 2023-03-17 14:31:23.000000 disembedbuilder-0.1.1/src/disembedbuilder.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      318 2023-03-17 14:31:23.000000 disembedbuilder-0.1.1/src/disembedbuilder.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-17 14:31:23.000000 disembedbuilder-0.1.1/src/disembedbuilder.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       16 2023-03-17 14:31:23.000000 disembedbuilder-0.1.1/src/disembedbuilder.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 15:33:14.720127 disembedbuilder-0.1.2/
+-rw-rw-rw-   0        0        0     1069 2023-03-17 14:25:29.000000 disembedbuilder-0.1.2/LICENSE
+-rw-rw-rw-   0        0        0      620 2023-04-06 15:33:14.720127 disembedbuilder-0.1.2/PKG-INFO
+-rw-rw-rw-   0        0        0      110 2022-09-01 15:27:20.000000 disembedbuilder-0.1.2/README.md
+-rw-rw-rw-   0        0        0      108 2023-03-17 14:25:40.000000 disembedbuilder-0.1.2/pyproject.toml
+-rw-rw-rw-   0        0        0      643 2023-04-06 15:33:14.721127 disembedbuilder-0.1.2/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-06 15:33:14.710125 disembedbuilder-0.1.2/src/
+drwxrwxrwx   0        0        0        0 2023-04-06 15:33:14.716126 disembedbuilder-0.1.2/src/disembedbuilder/
+-rw-rw-rw-   0        0        0       32 2023-03-17 09:52:50.000000 disembedbuilder-0.1.2/src/disembedbuilder/__init__.py
+-rw-rw-rw-   0        0        0    23270 2023-04-06 15:30:03.000000 disembedbuilder-0.1.2/src/disembedbuilder/disembedbuilder.py
+-rw-rw-rw-   0        0        0      698 2023-03-17 13:35:56.000000 disembedbuilder-0.1.2/src/disembedbuilder/preembeds.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:33:14.719127 disembedbuilder-0.1.2/src/disembedbuilder.egg-info/
+-rw-rw-rw-   0        0        0      620 2023-04-06 15:33:14.000000 disembedbuilder-0.1.2/src/disembedbuilder.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      318 2023-04-06 15:33:14.000000 disembedbuilder-0.1.2/src/disembedbuilder.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 15:33:14.000000 disembedbuilder-0.1.2/src/disembedbuilder.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       16 2023-04-06 15:33:14.000000 disembedbuilder-0.1.2/src/disembedbuilder.egg-info/top_level.txt
```

### Comparing `disembedbuilder-0.1.1/LICENSE` & `disembedbuilder-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `disembedbuilder-0.1.1/PKG-INFO` & `disembedbuilder-0.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: disembedbuilder
-Version: 0.1.1
+Version: 0.1.2
 Summary: Simple embed builder made with modals and buttons.
 Home-page: https://github.com/Fadix47/disembedbuilder
 Author: Fadix Meier
 Author-email: fadix18123@gmail.com
 Project-URL: Bug Tracker, https://github.com/Fadix47/disembedbuilder/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `disembedbuilder-0.1.1/setup.cfg` & `disembedbuilder-0.1.2/setup.cfg`

 * *Files 20% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 00000000: 5b6d 6574 6164 6174 615d 0d0a 6e61 6d65  [metadata]..name
 00000010: 203d 2064 6973 656d 6265 6462 7569 6c64   = disembedbuild
 00000020: 6572 0d0a 7665 7273 696f 6e20 3d20 302e  er..version = 0.
-00000030: 312e 310d 0a61 7574 686f 7220 3d20 4661  1.1..author = Fa
+00000030: 312e 320d 0a61 7574 686f 7220 3d20 4661  1.2..author = Fa
 00000040: 6469 7820 4d65 6965 720d 0a61 7574 686f  dix Meier..autho
 00000050: 725f 656d 6169 6c20 3d20 6661 6469 7831  r_email = fadix1
 00000060: 3831 3233 4067 6d61 696c 2e63 6f6d 0d0a  8123@gmail.com..
 00000070: 6465 7363 7269 7074 696f 6e20 3d20 5369  description = Si
 00000080: 6d70 6c65 2065 6d62 6564 2062 7569 6c64  mple embed build
 00000090: 6572 206d 6164 6520 7769 7468 206d 6f64  er made with mod
 000000a0: 616c 7320 616e 6420 6275 7474 6f6e 732e  als and buttons.
```

### Comparing `disembedbuilder-0.1.1/src/disembedbuilder/disembedbuilder.py` & `disembedbuilder-0.1.2/src/disembedbuilder/disembedbuilder.py`

 * *Files 0% similar despite different names*

```diff
@@ -395,9 +395,9 @@
     async def on_timeout(self) -> None:
         for child in self.children:
             child.disabled = True
         self.message.edit(embed=self.embed, view=self)
         self.stop()
 
     async def on_check_failure(self, interaction: Interaction) -> None:
-        await interaction.response.send_message(embed=error_embed(f"{interaction.user.mention}, you cannot interact with this menu!"))
+        await interaction.response.send_message(embed=error_embed(f"{interaction.user.mention}, you cannot interact with this menu!"), ephemeral=True)
```

### Comparing `disembedbuilder-0.1.1/src/disembedbuilder/preembeds.py` & `disembedbuilder-0.1.2/src/disembedbuilder/preembeds.py`

 * *Files identical despite different names*

### Comparing `disembedbuilder-0.1.1/src/disembedbuilder.egg-info/PKG-INFO` & `disembedbuilder-0.1.2/src/disembedbuilder.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: disembedbuilder
-Version: 0.1.1
+Version: 0.1.2
 Summary: Simple embed builder made with modals and buttons.
 Home-page: https://github.com/Fadix47/disembedbuilder
 Author: Fadix Meier
 Author-email: fadix18123@gmail.com
 Project-URL: Bug Tracker, https://github.com/Fadix47/disembedbuilder/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

