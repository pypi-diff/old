# Comparing `tmp/pandaspublisher-0.1.0.tar.gz` & `tmp/pandaspublisher-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pandaspublisher-0.1.0.tar", last modified: Fri Apr  7 01:03:58 2023, max compression
+gzip compressed data, was "pandaspublisher-0.1.1.tar", last modified: Fri Apr  7 01:07:45 2023, max compression
```

## Comparing `pandaspublisher-0.1.0.tar` & `pandaspublisher-0.1.1.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 jasonflittner   (501) staff       (20)        0 2023-04-07 01:03:58.561662 pandaspublisher-0.1.0/
--rw-r--r--   0 jasonflittner   (501) staff       (20)     1799 2023-04-05 14:27:48.000000 pandaspublisher-0.1.0/.gitignore
--rw-r--r--   0 jasonflittner   (501) staff       (20)    11357 2023-04-05 14:27:48.000000 pandaspublisher-0.1.0/LICENSE
--rw-r--r--   0 jasonflittner   (501) staff       (20)    16377 2023-04-07 01:03:58.561203 pandaspublisher-0.1.0/PKG-INFO
--rw-r--r--   0 jasonflittner   (501) staff       (20)     3082 2023-04-07 01:01:28.000000 pandaspublisher-0.1.0/README.md
-drwxr-xr-x   0 jasonflittner   (501) staff       (20)        0 2023-04-07 01:03:58.556356 pandaspublisher-0.1.0/examples/
--rw-r--r--   0 jasonflittner   (501) staff       (20)      844 2023-04-05 14:32:38.000000 pandaspublisher-0.1.0/examples/example_usage.py
-drwxr-xr-x   0 jasonflittner   (501) staff       (20)        0 2023-04-07 01:03:58.557317 pandaspublisher-0.1.0/examples/templates/
--rw-r--r--   0 jasonflittner   (501) staff       (20)     1445 2023-04-05 02:19:39.000000 pandaspublisher-0.1.0/examples/templates/sample_template.html
-drwxr-xr-x   0 jasonflittner   (501) staff       (20)        0 2023-04-07 01:03:58.558158 pandaspublisher-0.1.0/pandaspublisher/
--rw-r--r--   0 jasonflittner   (501) staff       (20)        0 2023-04-05 02:19:39.000000 pandaspublisher-0.1.0/pandaspublisher/__init__.py
--rw-r--r--   0 jasonflittner   (501) staff       (20)     1992 2023-04-05 13:49:23.000000 pandaspublisher-0.1.0/pandaspublisher/generate.py
-drwxr-xr-x   0 jasonflittner   (501) staff       (20)        0 2023-04-07 01:03:58.560510 pandaspublisher-0.1.0/pandaspublisher.egg-info/
--rw-r--r--   0 jasonflittner   (501) staff       (20)    16377 2023-04-07 01:03:58.000000 pandaspublisher-0.1.0/pandaspublisher.egg-info/PKG-INFO
--rw-r--r--   0 jasonflittner   (501) staff       (20)      359 2023-04-07 01:03:58.000000 pandaspublisher-0.1.0/pandaspublisher.egg-info/SOURCES.txt
--rw-r--r--   0 jasonflittner   (501) staff       (20)        1 2023-04-07 01:03:58.000000 pandaspublisher-0.1.0/pandaspublisher.egg-info/dependency_links.txt
--rw-r--r--   0 jasonflittner   (501) staff       (20)       25 2023-04-07 01:03:58.000000 pandaspublisher-0.1.0/pandaspublisher.egg-info/requires.txt
--rw-r--r--   0 jasonflittner   (501) staff       (20)       16 2023-04-07 01:03:58.000000 pandaspublisher-0.1.0/pandaspublisher.egg-info/top_level.txt
--rw-r--r--   0 jasonflittner   (501) staff       (20)      499 2023-04-05 14:43:52.000000 pandaspublisher-0.1.0/pyproject.toml
--rw-r--r--   0 jasonflittner   (501) staff       (20)       38 2023-04-07 01:03:58.561778 pandaspublisher-0.1.0/setup.cfg
+drwxr-xr-x   0 jasonflittner   (501) staff       (20)        0 2023-04-07 01:07:45.295575 pandaspublisher-0.1.1/
+-rw-r--r--   0 jasonflittner   (501) staff       (20)     1799 2023-04-05 14:27:48.000000 pandaspublisher-0.1.1/.gitignore
+-rw-r--r--   0 jasonflittner   (501) staff       (20)    11357 2023-04-05 14:27:48.000000 pandaspublisher-0.1.1/LICENSE
+-rw-r--r--   0 jasonflittner   (501) staff       (20)    16523 2023-04-07 01:07:45.295100 pandaspublisher-0.1.1/PKG-INFO
+-rw-r--r--   0 jasonflittner   (501) staff       (20)     3082 2023-04-07 01:01:28.000000 pandaspublisher-0.1.1/README.md
+drwxr-xr-x   0 jasonflittner   (501) staff       (20)        0 2023-04-07 01:07:45.291595 pandaspublisher-0.1.1/examples/
+-rw-r--r--   0 jasonflittner   (501) staff       (20)      844 2023-04-05 14:32:38.000000 pandaspublisher-0.1.1/examples/example_usage.py
+drwxr-xr-x   0 jasonflittner   (501) staff       (20)        0 2023-04-07 01:07:45.291884 pandaspublisher-0.1.1/examples/templates/
+-rw-r--r--   0 jasonflittner   (501) staff       (20)     1445 2023-04-05 02:19:39.000000 pandaspublisher-0.1.1/examples/templates/sample_template.html
+drwxr-xr-x   0 jasonflittner   (501) staff       (20)        0 2023-04-07 01:07:45.292690 pandaspublisher-0.1.1/pandaspublisher/
+-rw-r--r--   0 jasonflittner   (501) staff       (20)        0 2023-04-05 02:19:39.000000 pandaspublisher-0.1.1/pandaspublisher/__init__.py
+-rw-r--r--   0 jasonflittner   (501) staff       (20)     1992 2023-04-05 13:49:23.000000 pandaspublisher-0.1.1/pandaspublisher/generate.py
+drwxr-xr-x   0 jasonflittner   (501) staff       (20)        0 2023-04-07 01:07:45.294589 pandaspublisher-0.1.1/pandaspublisher.egg-info/
+-rw-r--r--   0 jasonflittner   (501) staff       (20)    16523 2023-04-07 01:07:45.000000 pandaspublisher-0.1.1/pandaspublisher.egg-info/PKG-INFO
+-rw-r--r--   0 jasonflittner   (501) staff       (20)      359 2023-04-07 01:07:45.000000 pandaspublisher-0.1.1/pandaspublisher.egg-info/SOURCES.txt
+-rw-r--r--   0 jasonflittner   (501) staff       (20)        1 2023-04-07 01:07:45.000000 pandaspublisher-0.1.1/pandaspublisher.egg-info/dependency_links.txt
+-rw-r--r--   0 jasonflittner   (501) staff       (20)       25 2023-04-07 01:07:45.000000 pandaspublisher-0.1.1/pandaspublisher.egg-info/requires.txt
+-rw-r--r--   0 jasonflittner   (501) staff       (20)       16 2023-04-07 01:07:45.000000 pandaspublisher-0.1.1/pandaspublisher.egg-info/top_level.txt
+-rw-r--r--   0 jasonflittner   (501) staff       (20)      645 2023-04-07 01:07:33.000000 pandaspublisher-0.1.1/pyproject.toml
+-rw-r--r--   0 jasonflittner   (501) staff       (20)       38 2023-04-07 01:07:45.295659 pandaspublisher-0.1.1/setup.cfg
```

### Comparing `pandaspublisher-0.1.0/.gitignore` & `pandaspublisher-0.1.1/.gitignore`

 * *Files identical despite different names*

### Comparing `pandaspublisher-0.1.0/LICENSE` & `pandaspublisher-0.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `pandaspublisher-0.1.0/PKG-INFO` & `pandaspublisher-0.1.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pandaspublisher
-Version: 0.1.0
+Version: 0.1.1
 Summary: A Python package for generating customizable HTML and PDF reports from Pandas DataFrames and Jinja2 templates
 Author-email: Jason Flittner <jason.flittner@gmail.com>
 License:                                  Apache License
                                    Version 2.0, January 2004
                                 http://www.apache.org/licenses/
         
            TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
@@ -201,14 +201,16 @@
         
            Unless required by applicable law or agreed to in writing, software
            distributed under the License is distributed on an "AS IS" BASIS,
            WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
            See the License for the specific language governing permissions and
            limitations under the License.
         
+Project-URL: Homepage, https://github.com/jflittner/PandasPublisher
+Project-URL: Bug Tracker, https://github.com/jflittner/PandasPublisher/issues
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # Pandas Publisher
 
 Pandas Publisher allows you to generate HTML and PDF reports using Jinja2 templates and Pandas dataframes. The generated reports can be saved as HTML, PDF, or returned as an HTML string.
```

### Comparing `pandaspublisher-0.1.0/README.md` & `pandaspublisher-0.1.1/README.md`

 * *Files identical despite different names*

### Comparing `pandaspublisher-0.1.0/examples/example_usage.py` & `pandaspublisher-0.1.1/examples/example_usage.py`

 * *Files identical despite different names*

### Comparing `pandaspublisher-0.1.0/examples/templates/sample_template.html` & `pandaspublisher-0.1.1/examples/templates/sample_template.html`

 * *Files identical despite different names*

### Comparing `pandaspublisher-0.1.0/pandaspublisher/generate.py` & `pandaspublisher-0.1.1/pandaspublisher/generate.py`

 * *Files identical despite different names*

### Comparing `pandaspublisher-0.1.0/pandaspublisher.egg-info/PKG-INFO` & `pandaspublisher-0.1.1/pandaspublisher.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pandaspublisher
-Version: 0.1.0
+Version: 0.1.1
 Summary: A Python package for generating customizable HTML and PDF reports from Pandas DataFrames and Jinja2 templates
 Author-email: Jason Flittner <jason.flittner@gmail.com>
 License:                                  Apache License
                                    Version 2.0, January 2004
                                 http://www.apache.org/licenses/
         
            TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
@@ -201,14 +201,16 @@
         
            Unless required by applicable law or agreed to in writing, software
            distributed under the License is distributed on an "AS IS" BASIS,
            WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
            See the License for the specific language governing permissions and
            limitations under the License.
         
+Project-URL: Homepage, https://github.com/jflittner/PandasPublisher
+Project-URL: Bug Tracker, https://github.com/jflittner/PandasPublisher/issues
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # Pandas Publisher
 
 Pandas Publisher allows you to generate HTML and PDF reports using Jinja2 templates and Pandas dataframes. The generated reports can be saved as HTML, PDF, or returned as an HTML string.
```

