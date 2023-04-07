# Comparing `tmp/sysall-1.1.1.tar.gz` & `tmp/sysall-1.1.11.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sysall-1.1.1.tar", last modified: Fri Apr  7 08:24:46 2023, max compression
+gzip compressed data, was "sysall-1.1.11.tar", last modified: Fri Apr  7 10:06:03 2023, max compression
```

## Comparing `sysall-1.1.1.tar` & `sysall-1.1.11.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 08:24:46.947938 sysall-1.1.1/
--rw-rw-rw-   0        0        0     1067 2023-04-04 19:25:31.000000 sysall-1.1.1/LICENSE
--rw-rw-rw-   0        0        0     4198 2023-04-07 08:24:46.946926 sysall-1.1.1/PKG-INFO
--rw-rw-rw-   0        0        0     3650 2023-04-07 08:24:25.000000 sysall-1.1.1/README.md
--rw-rw-rw-   0        0        0      716 2023-04-07 08:24:13.000000 sysall-1.1.1/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-07 08:24:46.948950 sysall-1.1.1/setup.cfg
--rw-rw-rw-   0        0        0      170 2023-04-06 08:37:31.000000 sysall-1.1.1/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-07 08:24:46.906418 sysall-1.1.1/src/
-drwxrwxrwx   0        0        0        0 2023-04-07 08:24:46.922733 sysall-1.1.1/src/sysall/
--rw-rw-rw-   0        0        0    13200 2023-04-07 08:24:18.000000 sysall-1.1.1/src/sysall/SysAll.py
--rw-rw-rw-   0        0        0       21 2023-04-04 19:51:38.000000 sysall-1.1.1/src/sysall/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-07 08:24:46.945920 sysall-1.1.1/src/sysall.egg-info/
--rw-rw-rw-   0        0        0     4198 2023-04-07 08:24:46.000000 sysall-1.1.1/src/sysall.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      254 2023-04-07 08:24:46.000000 sysall-1.1.1/src/sysall.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 08:24:46.000000 sysall-1.1.1/src/sysall.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       38 2023-04-07 08:24:46.000000 sysall-1.1.1/src/sysall.egg-info/requires.txt
--rw-rw-rw-   0        0        0        7 2023-04-07 08:24:46.000000 sysall-1.1.1/src/sysall.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 10:06:03.739719 sysall-1.1.11/
+-rw-rw-rw-   0        0        0     1067 2023-04-04 19:25:31.000000 sysall-1.1.11/LICENSE
+-rw-rw-rw-   0        0        0     4093 2023-04-07 10:06:03.738598 sysall-1.1.11/PKG-INFO
+-rw-rw-rw-   0        0        0     3544 2023-04-07 10:03:54.000000 sysall-1.1.11/README.md
+-rw-rw-rw-   0        0        0      717 2023-04-07 10:05:44.000000 sysall-1.1.11/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 10:06:03.739719 sysall-1.1.11/setup.cfg
+-rw-rw-rw-   0        0        0      170 2023-04-06 08:37:31.000000 sysall-1.1.11/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 10:06:03.695932 sysall-1.1.11/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 10:06:03.713453 sysall-1.1.11/src/sysall/
+-rw-rw-rw-   0        0        0    13201 2023-04-07 10:05:39.000000 sysall-1.1.11/src/sysall/SysAll.py
+-rw-rw-rw-   0        0        0       21 2023-04-04 19:51:38.000000 sysall-1.1.11/src/sysall/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 10:06:03.736419 sysall-1.1.11/src/sysall.egg-info/
+-rw-rw-rw-   0        0        0     4093 2023-04-07 10:06:03.000000 sysall-1.1.11/src/sysall.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      254 2023-04-07 10:06:03.000000 sysall-1.1.11/src/sysall.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 10:06:03.000000 sysall-1.1.11/src/sysall.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       38 2023-04-07 10:06:03.000000 sysall-1.1.11/src/sysall.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        7 2023-04-07 10:06:03.000000 sysall-1.1.11/src/sysall.egg-info/top_level.txt
```

### Comparing `sysall-1.1.1/LICENSE` & `sysall-1.1.11/LICENSE`

 * *Files identical despite different names*

### Comparing `sysall-1.1.1/PKG-INFO` & `sysall-1.1.11/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 Metadata-Version: 2.1
 Name: sysall
-Version: 1.1.1
+Version: 1.1.11
 Summary: Tools to facilitate the use/manipulation of data in the Windows environment
 Author-email: LixNew <lixnew2@gmail.com>
 Project-URL: Homepage, https://github.com/LixNew2/SysAll
 Project-URL: Bug Tracker, https://github.com/LixNew2/SysAll/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # SysAll
 
-[![Downloads](https://static.pepy.tech/personalized-badge/sysall?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/sysall)
+[![Downloads](https://static.pepy.tech/badge/sysall)](https://pepy.tech/project/sysall)
 [![Version](https://img.shields.io/pypi/v/sysall)](https://pypi.org/project/sysall/)
 [![Python Version](https://img.shields.io/pypi/pyversions/sysall)](https://pypi.org/project/sysall/)
 
 SysAll is a library that aims to make it easier for python developers,
 to use/manipulate data from the Windows environment.
 
 With this tool, you will be able to access many system and network features.
```

### Comparing `sysall-1.1.1/README.md` & `sysall-1.1.11/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # SysAll
 
-[![Downloads](https://static.pepy.tech/personalized-badge/sysall?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/sysall)
+[![Downloads](https://static.pepy.tech/badge/sysall)](https://pepy.tech/project/sysall)
 [![Version](https://img.shields.io/pypi/v/sysall)](https://pypi.org/project/sysall/)
 [![Python Version](https://img.shields.io/pypi/pyversions/sysall)](https://pypi.org/project/sysall/)
 
 SysAll is a library that aims to make it easier for python developers,
 to use/manipulate data from the Windows environment.
 
 With this tool, you will be able to access many system and network features.
```

### Comparing `sysall-1.1.1/pyproject.toml` & `sysall-1.1.11/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,15 @@
     "py-cpuinfo",
     "requests"
 ]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "sysall"
-version = "1.1.1"
+version = "1.1.11"
 authors = [
   { name="LixNew", email="lixnew2@gmail.com" },
 ]
 description = "Tools to facilitate the use/manipulation of data in the Windows environment"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `sysall-1.1.1/src/sysall/SysAll.py` & `sysall-1.1.11/src/sysall/SysAll.py`

 * *Files 0% similar despite different names*

```diff
@@ -24,15 +24,15 @@
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
 """
 
-__version__ = '1.1.1'
+__version__ = '1.1.11'
 __title__ = 'SysAll'
 __description__ = "Tools to facilitate the use/manipulation of data in the Windows environment"
 __autor__ = 'LixNew'
 __twitter__ = '@LixNew2'
 __url__ = "https://github.com/LixNew2/SysAll"
 
 #Import
```

### Comparing `sysall-1.1.1/src/sysall.egg-info/PKG-INFO` & `sysall-1.1.11/src/sysall.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 Metadata-Version: 2.1
 Name: sysall
-Version: 1.1.1
+Version: 1.1.11
 Summary: Tools to facilitate the use/manipulation of data in the Windows environment
 Author-email: LixNew <lixnew2@gmail.com>
 Project-URL: Homepage, https://github.com/LixNew2/SysAll
 Project-URL: Bug Tracker, https://github.com/LixNew2/SysAll/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # SysAll
 
-[![Downloads](https://static.pepy.tech/personalized-badge/sysall?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/sysall)
+[![Downloads](https://static.pepy.tech/badge/sysall)](https://pepy.tech/project/sysall)
 [![Version](https://img.shields.io/pypi/v/sysall)](https://pypi.org/project/sysall/)
 [![Python Version](https://img.shields.io/pypi/pyversions/sysall)](https://pypi.org/project/sysall/)
 
 SysAll is a library that aims to make it easier for python developers,
 to use/manipulate data from the Windows environment.
 
 With this tool, you will be able to access many system and network features.
```

