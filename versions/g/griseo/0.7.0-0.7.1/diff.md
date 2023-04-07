# Comparing `tmp/griseo-0.7.0.tar.gz` & `tmp/griseo-0.7.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "griseo-0.7.0.tar", max compression
+gzip compressed data, was "griseo-0.7.1.tar", max compression
```

## Comparing `griseo-0.7.0.tar` & `griseo-0.7.1.tar`

### file list

```diff
@@ -1,6 +1,6 @@
--rw-r--r--   0        0        0    11357 2023-03-31 00:48:44.258133 griseo-0.7.0/LICENSE
--rw-r--r--   0        0        0      280 2023-04-07 09:26:25.990781 griseo-0.7.0/README.md
--rw-r--r--   0        0        0     3191 2023-04-07 09:51:38.914570 griseo-0.7.0/griseo/__init__.py
--rw-r--r--   0        0        0      653 2023-03-31 01:58:54.505124 griseo-0.7.0/griseo/__main__.py
--rw-r--r--   0        0        0     1193 2023-04-07 09:53:24.837658 griseo-0.7.0/pyproject.toml
--rw-r--r--   0        0        0     1115 1970-01-01 00:00:00.000000 griseo-0.7.0/PKG-INFO
+-rw-r--r--   0        0        0    11357 2023-04-07 10:04:49.268262 griseo-0.7.1/LICENSE
+-rw-r--r--   0        0        0      280 2023-04-07 10:04:49.268262 griseo-0.7.1/README.md
+-rw-r--r--   0        0        0     3191 2023-04-07 10:04:49.268262 griseo-0.7.1/griseo/__init__.py
+-rw-r--r--   0        0        0      653 2023-04-07 10:04:49.268262 griseo-0.7.1/griseo/__main__.py
+-rw-r--r--   0        0        0     1193 2023-04-07 10:04:49.268262 griseo-0.7.1/pyproject.toml
+-rw-r--r--   0        0        0     1115 1970-01-01 00:00:00.000000 griseo-0.7.1/PKG-INFO
```

### Comparing `griseo-0.7.0/LICENSE` & `griseo-0.7.1/LICENSE`

 * *Files identical despite different names*

### Comparing `griseo-0.7.0/griseo/__init__.py` & `griseo-0.7.1/griseo/__init__.py`

 * *Files identical despite different names*

### Comparing `griseo-0.7.0/griseo/__main__.py` & `griseo-0.7.1/griseo/__main__.py`

 * *Files identical despite different names*

### Comparing `griseo-0.7.0/pyproject.toml` & `griseo-0.7.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 [tool.poetry]
 name = "griseo"
-version = "0.7.0"
+version = "0.7.1"
 description = "Chat with OpenAI in the Hacker way."
 authors = ["tison <wander4096@gmail.com>"]
 license = "Apache-2.0"
 readme = "README.md"
 homepage = "https://github.com/korandoru/griseo"
 repository = "https://github.com/korandoru/griseo"
 documentation = "https://github.com/korandoru/griseo"
```

### Comparing `griseo-0.7.0/PKG-INFO` & `griseo-0.7.1/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: griseo
-Version: 0.7.0
+Version: 0.7.1
 Summary: Chat with OpenAI in the Hacker way.
 Home-page: https://github.com/korandoru/griseo
 License: Apache-2.0
 Keywords: chatgpt,cli,openai
 Author: tison
 Author-email: wander4096@gmail.com
 Requires-Python: >=3.8,<4.0
```

