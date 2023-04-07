# Comparing `tmp/socha-1.0.5.tar.gz` & `tmp/socha-1.0.6.tar.gz`

## Comparing `socha-1.0.5.tar` & `socha-1.0.6.tar`

### file list

```diff
@@ -1,27 +1,27 @@
--rw-r--r--   0        0        0     2196 2020-02-02 00:00:00.000000 socha-1.0.5/changes.md
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 socha-1.0.5/requirements.txt
--rw-r--r--   0        0        0      747 2020-02-02 00:00:00.000000 socha-1.0.5/start.sh
--rw-r--r--   0        0        0      586 2020-02-02 00:00:00.000000 socha-1.0.5/socha/__init__.py
--rw-r--r--   0        0        0     6251 2020-02-02 00:00:00.000000 socha-1.0.5/socha/starter.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/__init__.py
--rw-r--r--   0        0        0       85 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/networking/__init__.py
--rw-r--r--   0        0        0    12752 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/networking/game_client.py
--rw-r--r--   0        0        0     3047 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/networking/network_socket.py
--rw-r--r--   0        0        0     5966 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/networking/xml_protocol_interface.py
--rw-r--r--   0        0        0       78 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/plugin/__init__.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/plugin/penguins/__init__.py
--rw-r--r--   0        0        0    14995 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/plugin/penguins/board.py
--rw-r--r--   0        0        0     9243 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/plugin/penguins/coordinate.py
--rw-r--r--   0        0        0     7111 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/plugin/penguins/game_state.py
--rw-r--r--   0        0        0     4945 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/plugin/penguins/team.py
--rw-r--r--   0        0        0      262 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/protocol/__init__.py
--rw-r--r--   0        0        0    17852 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/protocol/protocol.py
--rw-r--r--   0        0        0      173 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/protocol/protocol_packet.py
--rw-r--r--   0        0        0      346 2020-02-02 00:00:00.000000 socha-1.0.5/socha/api/protocol/room_message.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 socha-1.0.5/socha/utils/__init__.py
--rw-r--r--   0        0        0     6558 2020-02-02 00:00:00.000000 socha-1.0.5/socha/utils/package_builder.py
--rw-r--r--   0        0        0     1376 2020-02-02 00:00:00.000000 socha-1.0.5/.gitignore
--rw-r--r--   0        0        0     1066 2020-02-02 00:00:00.000000 socha-1.0.5/LICENSE
--rw-r--r--   0        0        0    10021 2020-02-02 00:00:00.000000 socha-1.0.5/README.md
--rw-r--r--   0        0        0     1304 2020-02-02 00:00:00.000000 socha-1.0.5/pyproject.toml
--rw-r--r--   0        0        0    10966 2020-02-02 00:00:00.000000 socha-1.0.5/PKG-INFO
+-rw-r--r--   0        0        0     2196 2020-02-02 00:00:00.000000 socha-1.0.6/changes.md
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 socha-1.0.6/requirements.txt
+-rw-r--r--   0        0        0      747 2020-02-02 00:00:00.000000 socha-1.0.6/start.sh
+-rw-r--r--   0        0        0      586 2020-02-02 00:00:00.000000 socha-1.0.6/socha/__init__.py
+-rw-r--r--   0        0        0     6251 2020-02-02 00:00:00.000000 socha-1.0.6/socha/starter.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/__init__.py
+-rw-r--r--   0        0        0       85 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/networking/__init__.py
+-rw-r--r--   0        0        0    12752 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/networking/game_client.py
+-rw-r--r--   0        0        0     3047 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/networking/network_socket.py
+-rw-r--r--   0        0        0     5966 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/networking/xml_protocol_interface.py
+-rw-r--r--   0        0        0       78 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/plugin/__init__.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/plugin/penguins/__init__.py
+-rw-r--r--   0        0        0    14995 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/plugin/penguins/board.py
+-rw-r--r--   0        0        0     9243 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/plugin/penguins/coordinate.py
+-rw-r--r--   0        0        0     7111 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/plugin/penguins/game_state.py
+-rw-r--r--   0        0        0     4945 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/plugin/penguins/team.py
+-rw-r--r--   0        0        0      262 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/protocol/__init__.py
+-rw-r--r--   0        0        0    17852 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/protocol/protocol.py
+-rw-r--r--   0        0        0      173 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/protocol/protocol_packet.py
+-rw-r--r--   0        0        0      346 2020-02-02 00:00:00.000000 socha-1.0.6/socha/api/protocol/room_message.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 socha-1.0.6/socha/utils/__init__.py
+-rw-r--r--   0        0        0     8375 2020-02-02 00:00:00.000000 socha-1.0.6/socha/utils/package_builder.py
+-rw-r--r--   0        0        0     1376 2020-02-02 00:00:00.000000 socha-1.0.6/.gitignore
+-rw-r--r--   0        0        0     1066 2020-02-02 00:00:00.000000 socha-1.0.6/LICENSE
+-rw-r--r--   0        0        0    10021 2020-02-02 00:00:00.000000 socha-1.0.6/README.md
+-rw-r--r--   0        0        0     1304 2020-02-02 00:00:00.000000 socha-1.0.6/pyproject.toml
+-rw-r--r--   0        0        0    10966 2020-02-02 00:00:00.000000 socha-1.0.6/PKG-INFO
```

### Comparing `socha-1.0.5/changes.md` & `socha-1.0.6/changes.md`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/start.sh` & `socha-1.0.6/start.sh`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/socha/__init__.py` & `socha-1.0.6/socha/__init__.py`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/socha/starter.py` & `socha-1.0.6/socha/starter.py`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/socha/api/networking/game_client.py` & `socha-1.0.6/socha/api/networking/game_client.py`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/socha/api/networking/network_socket.py` & `socha-1.0.6/socha/api/networking/network_socket.py`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/socha/api/networking/xml_protocol_interface.py` & `socha-1.0.6/socha/api/networking/xml_protocol_interface.py`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/socha/api/plugin/penguins/board.py` & `socha-1.0.6/socha/api/plugin/penguins/board.py`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/socha/api/plugin/penguins/coordinate.py` & `socha-1.0.6/socha/api/plugin/penguins/coordinate.py`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/socha/api/plugin/penguins/game_state.py` & `socha-1.0.6/socha/api/plugin/penguins/game_state.py`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/socha/api/plugin/penguins/team.py` & `socha-1.0.6/socha/api/plugin/penguins/team.py`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/socha/api/protocol/protocol.py` & `socha-1.0.6/socha/api/protocol/protocol.py`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/.gitignore` & `socha-1.0.6/.gitignore`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/LICENSE` & `socha-1.0.6/LICENSE`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/README.md` & `socha-1.0.6/README.md`

 * *Files identical despite different names*

### Comparing `socha-1.0.5/pyproject.toml` & `socha-1.0.6/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "socha"
-version = "1.0.5"
+version = "1.0.6"
 authors = [
     { name = "FalconsSky", email = "stu222782@mail.uni-kiel.de" },
 ]
 description = "This is the package for the Software-Challenge Germany 2023. This Season the game will be 'Hey, danke für den Fisch' a.k.a. 'Penguins' in short."
 readme = "README.md"
 requires-python = ">=3.6"
 dependencies = [
```

### Comparing `socha-1.0.5/PKG-INFO` & `socha-1.0.6/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: socha
-Version: 1.0.5
+Version: 1.0.6
 Summary: This is the package for the Software-Challenge Germany 2023. This Season the game will be 'Hey, danke für den Fisch' a.k.a. 'Penguins' in short.
 Project-URL: Bug Tracker, https://github.com/FalconsSky/Software-Challenge-Python-Client/issues
 Author-email: FalconsSky <stu222782@mail.uni-kiel.de>
 License-File: LICENSE
 Classifier: License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
```

