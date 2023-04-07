# Comparing `tmp/sysall-1.1.0.tar.gz` & `tmp/sysall-1.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sysall-1.1.0.tar", last modified: Thu Apr  6 14:47:34 2023, max compression
+gzip compressed data, was "sysall-1.1.1.tar", last modified: Fri Apr  7 08:24:46 2023, max compression
```

## Comparing `sysall-1.1.0.tar` & `sysall-1.1.1.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 14:47:34.484825 sysall-1.1.0/
--rw-rw-rw-   0        0        0     1067 2023-04-04 19:25:31.000000 sysall-1.1.0/LICENSE
--rw-rw-rw-   0        0        0     4135 2023-04-06 14:47:34.483319 sysall-1.1.0/PKG-INFO
--rw-rw-rw-   0        0        0     3587 2023-04-06 14:47:11.000000 sysall-1.1.0/README.md
--rw-rw-rw-   0        0        0      716 2023-04-06 14:44:20.000000 sysall-1.1.0/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 14:47:34.484825 sysall-1.1.0/setup.cfg
--rw-rw-rw-   0        0        0      170 2023-04-06 08:37:31.000000 sysall-1.1.0/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-06 14:47:34.443313 sysall-1.1.0/src/
-drwxrwxrwx   0        0        0        0 2023-04-06 14:47:34.462513 sysall-1.1.0/src/sysall/
--rw-rw-rw-   0        0        0    12527 2023-04-06 14:47:02.000000 sysall-1.1.0/src/sysall/SysAll.py
--rw-rw-rw-   0        0        0       21 2023-04-04 19:51:38.000000 sysall-1.1.0/src/sysall/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-06 14:47:34.481295 sysall-1.1.0/src/sysall.egg-info/
--rw-rw-rw-   0        0        0     4135 2023-04-06 14:47:34.000000 sysall-1.1.0/src/sysall.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      254 2023-04-06 14:47:34.000000 sysall-1.1.0/src/sysall.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 14:47:34.000000 sysall-1.1.0/src/sysall.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       38 2023-04-06 14:47:34.000000 sysall-1.1.0/src/sysall.egg-info/requires.txt
--rw-rw-rw-   0        0        0        7 2023-04-06 14:47:34.000000 sysall-1.1.0/src/sysall.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 08:24:46.947938 sysall-1.1.1/
+-rw-rw-rw-   0        0        0     1067 2023-04-04 19:25:31.000000 sysall-1.1.1/LICENSE
+-rw-rw-rw-   0        0        0     4198 2023-04-07 08:24:46.946926 sysall-1.1.1/PKG-INFO
+-rw-rw-rw-   0        0        0     3650 2023-04-07 08:24:25.000000 sysall-1.1.1/README.md
+-rw-rw-rw-   0        0        0      716 2023-04-07 08:24:13.000000 sysall-1.1.1/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 08:24:46.948950 sysall-1.1.1/setup.cfg
+-rw-rw-rw-   0        0        0      170 2023-04-06 08:37:31.000000 sysall-1.1.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:24:46.906418 sysall-1.1.1/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 08:24:46.922733 sysall-1.1.1/src/sysall/
+-rw-rw-rw-   0        0        0    13200 2023-04-07 08:24:18.000000 sysall-1.1.1/src/sysall/SysAll.py
+-rw-rw-rw-   0        0        0       21 2023-04-04 19:51:38.000000 sysall-1.1.1/src/sysall/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:24:46.945920 sysall-1.1.1/src/sysall.egg-info/
+-rw-rw-rw-   0        0        0     4198 2023-04-07 08:24:46.000000 sysall-1.1.1/src/sysall.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      254 2023-04-07 08:24:46.000000 sysall-1.1.1/src/sysall.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 08:24:46.000000 sysall-1.1.1/src/sysall.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       38 2023-04-07 08:24:46.000000 sysall-1.1.1/src/sysall.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        7 2023-04-07 08:24:46.000000 sysall-1.1.1/src/sysall.egg-info/top_level.txt
```

### Comparing `sysall-1.1.0/LICENSE` & `sysall-1.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `sysall-1.1.0/PKG-INFO` & `sysall-1.1.1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,26 +1,26 @@
 Metadata-Version: 2.1
 Name: sysall
-Version: 1.1.0
+Version: 1.1.1
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
 
 [![Downloads](https://static.pepy.tech/personalized-badge/sysall?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/sysall)
-[![sysall Version](https://img.shields.io/pypi/v/sysall)](https://pypi.org/project/sysall/)
-[![sysall Python Version](https://img.shields.io/pypi/pyversions/sysall)](https://pypi.org/project/sysall/)
+[![Version](https://img.shields.io/pypi/v/sysall)](https://pypi.org/project/sysall/)
+[![Python Version](https://img.shields.io/pypi/pyversions/sysall)](https://pypi.org/project/sysall/)
 
 SysAll is a library that aims to make it easier for python developers,
 to use/manipulate data from the Windows environment.
 
 With this tool, you will be able to access many system and network features. 
 All this with functions that can be modified at will and in a single library.
 
@@ -179,7 +179,13 @@
 ~~~   
 
             
 Returns main DNS suffix
 ~~~python
 get_main_DNS_suffix()
 ~~~    
+
+
+Returns Autoconfiguration status
+~~~python
+get_automtic_config()
+~~~
```

### Comparing `sysall-1.1.0/README.md` & `sysall-1.1.1/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # SysAll
 
 [![Downloads](https://static.pepy.tech/personalized-badge/sysall?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/sysall)
-[![sysall Version](https://img.shields.io/pypi/v/sysall)](https://pypi.org/project/sysall/)
-[![sysall Python Version](https://img.shields.io/pypi/pyversions/sysall)](https://pypi.org/project/sysall/)
+[![Version](https://img.shields.io/pypi/v/sysall)](https://pypi.org/project/sysall/)
+[![Python Version](https://img.shields.io/pypi/pyversions/sysall)](https://pypi.org/project/sysall/)
 
 SysAll is a library that aims to make it easier for python developers,
 to use/manipulate data from the Windows environment.
 
 With this tool, you will be able to access many system and network features. 
 All this with functions that can be modified at will and in a single library.
 
@@ -164,8 +164,14 @@
 get_IP_routing_status()
 ~~~   
 
             
 Returns main DNS suffix
 ~~~python
 get_main_DNS_suffix()
-~~~    
+~~~    
+
+
+Returns Autoconfiguration status
+~~~python
+get_automtic_config()
+~~~
```

### Comparing `sysall-1.1.0/pyproject.toml` & `sysall-1.1.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,15 @@
     "py-cpuinfo",
     "requests"
 ]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "sysall"
-version = "1.1.0"
+version = "1.1.1"
 authors = [
   { name="LixNew", email="lixnew2@gmail.com" },
 ]
 description = "Tools to facilitate the use/manipulation of data in the Windows environment"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `sysall-1.1.0/src/sysall/SysAll.py` & `sysall-1.1.1/src/sysall/SysAll.py`

 * *Files 3% similar despite different names*

```diff
@@ -24,15 +24,15 @@
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
 """
 
-__version__ = '1.1.0'
+__version__ = '1.1.1'
 __title__ = 'SysAll'
 __description__ = "Tools to facilitate the use/manipulation of data in the Windows environment"
 __autor__ = 'LixNew'
 __twitter__ = '@LixNew2'
 __url__ = "https://github.com/LixNew2/SysAll"
 
 #Import
@@ -174,15 +174,15 @@
     _gpus = _wmi_obj.Win32_VideoController()
     
     #Dictionary that saves the returned information
     gpu_infos = {}
     
     #For all GPU in GPUS get info
     for _gpu in _gpus:
-        AMOUNT+=1
+        _AMOUNT+=1
         #If name (True) add name in gpu_infos
         if name:
             gpu_infos[f"Name GPU{_AMOUNT}"] = _gpu.Name
         #If ram (True) add ram in gpu_infos    
         if ram:
             gpu_infos[f"RAM GPU{_AMOUNT}"] = _gpu.AdapterRAM
         #If driver_version (True) add driver_version in gpu_infos
@@ -353,8 +353,25 @@
 def get_main_DNS_suffix(net=_network_infos()) -> str:
     """Returns main DNS status"""
     
     for _line in net.split(b'\r\n'):
         if b'Priamry Dns Suffix' in _line or b'Suffixe DNS principal' in _line:
             suffix_dns = _line.split(b':')[1].decode('utf-8').strip()
             if suffix_dns != "":
-                return suffix_dns
+                return suffix_dns
+
+def get_automtic_config(net=_network_infos()) -> str:
+    """Returns Autoconfiguration status
+    
+    If the function returns "True" it means that Autoconfiguration is enabled.
+    On the contrary, if the function returns "False", it means that Autoconfiguration is disabled.
+    """
+    
+    for _line in net.split(b'\r\n'):
+        if b'Autoconfiguration Enabled' in _line or b'Configuration automatique activ' in _line:
+            _auto_conf = _line.split(b':')[1].decode('utf-8').strip()
+            if _auto_conf == "Yes" or _auto_conf == "Oui":
+                return True
+            else:
+                return False
+            
+
```

### Comparing `sysall-1.1.0/src/sysall.egg-info/PKG-INFO` & `sysall-1.1.1/src/sysall.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,26 +1,26 @@
 Metadata-Version: 2.1
 Name: sysall
-Version: 1.1.0
+Version: 1.1.1
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
 
 [![Downloads](https://static.pepy.tech/personalized-badge/sysall?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/sysall)
-[![sysall Version](https://img.shields.io/pypi/v/sysall)](https://pypi.org/project/sysall/)
-[![sysall Python Version](https://img.shields.io/pypi/pyversions/sysall)](https://pypi.org/project/sysall/)
+[![Version](https://img.shields.io/pypi/v/sysall)](https://pypi.org/project/sysall/)
+[![Python Version](https://img.shields.io/pypi/pyversions/sysall)](https://pypi.org/project/sysall/)
 
 SysAll is a library that aims to make it easier for python developers,
 to use/manipulate data from the Windows environment.
 
 With this tool, you will be able to access many system and network features. 
 All this with functions that can be modified at will and in a single library.
 
@@ -179,7 +179,13 @@
 ~~~   
 
             
 Returns main DNS suffix
 ~~~python
 get_main_DNS_suffix()
 ~~~    
+
+
+Returns Autoconfiguration status
+~~~python
+get_automtic_config()
+~~~
```

