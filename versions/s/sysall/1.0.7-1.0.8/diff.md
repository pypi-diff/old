# Comparing `tmp/sysall-1.0.7.tar.gz` & `tmp/sysall-1.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sysall-1.0.7.tar", last modified: Wed Apr  5 14:59:07 2023, max compression
+gzip compressed data, was "sysall-1.0.8.tar", last modified: Thu Apr  6 10:40:31 2023, max compression
```

## Comparing `sysall-1.0.7.tar` & `sysall-1.0.8.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxrwxrwx   0        0        0        0 2023-04-05 14:59:07.627605 sysall-1.0.7/
--rw-rw-rw-   0        0        0     1067 2023-04-04 19:25:31.000000 sysall-1.0.7/LICENSE
--rw-rw-rw-   0        0        0     3578 2023-04-05 14:59:07.625036 sysall-1.0.7/PKG-INFO
--rw-rw-rw-   0        0        0     3033 2023-04-05 14:46:18.000000 sysall-1.0.7/README.md
--rw-rw-rw-   0        0        0      713 2023-04-05 14:58:40.000000 sysall-1.0.7/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-05 14:59:07.627605 sysall-1.0.7/setup.cfg
--rw-rw-rw-   0        0        0      170 2023-04-05 11:42:42.000000 sysall-1.0.7/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-05 14:59:07.584883 sysall-1.0.7/src/
-drwxrwxrwx   0        0        0        0 2023-04-05 14:59:07.601276 sysall-1.0.7/src/sysall/
--rw-rw-rw-   0        0        0     7489 2023-04-05 14:58:49.000000 sysall-1.0.7/src/sysall/SysAll.py
--rw-rw-rw-   0        0        0       21 2023-04-04 19:51:38.000000 sysall-1.0.7/src/sysall/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-05 14:59:07.623954 sysall-1.0.7/src/sysall.egg-info/
--rw-rw-rw-   0        0        0     3578 2023-04-05 14:59:07.000000 sysall-1.0.7/src/sysall.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      254 2023-04-05 14:59:07.000000 sysall-1.0.7/src/sysall.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-05 14:59:07.000000 sysall-1.0.7/src/sysall.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       38 2023-04-05 14:59:07.000000 sysall-1.0.7/src/sysall.egg-info/requires.txt
--rw-rw-rw-   0        0        0        7 2023-04-05 14:59:07.000000 sysall-1.0.7/src/sysall.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 10:40:31.666973 sysall-1.0.8/
+-rw-rw-rw-   0        0        0     1067 2023-04-04 19:25:31.000000 sysall-1.0.8/LICENSE
+-rw-rw-rw-   0        0        0     3907 2023-04-06 10:40:31.664964 sysall-1.0.8/PKG-INFO
+-rw-rw-rw-   0        0        0     3362 2023-04-06 10:38:31.000000 sysall-1.0.8/README.md
+-rw-rw-rw-   0        0        0      713 2023-04-06 10:40:12.000000 sysall-1.0.8/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-06 10:40:31.666973 sysall-1.0.8/setup.cfg
+-rw-rw-rw-   0        0        0      170 2023-04-06 08:37:31.000000 sysall-1.0.8/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:40:31.629108 sysall-1.0.8/src/
+drwxrwxrwx   0        0        0        0 2023-04-06 10:40:31.645142 sysall-1.0.8/src/sysall/
+-rw-rw-rw-   0        0        0     9546 2023-04-06 10:40:16.000000 sysall-1.0.8/src/sysall/SysAll.py
+-rw-rw-rw-   0        0        0       21 2023-04-04 19:51:38.000000 sysall-1.0.8/src/sysall/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:40:31.663954 sysall-1.0.8/src/sysall.egg-info/
+-rw-rw-rw-   0        0        0     3907 2023-04-06 10:40:31.000000 sysall-1.0.8/src/sysall.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      254 2023-04-06 10:40:31.000000 sysall-1.0.8/src/sysall.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 10:40:31.000000 sysall-1.0.8/src/sysall.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       38 2023-04-06 10:40:31.000000 sysall-1.0.8/src/sysall.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        7 2023-04-06 10:40:31.000000 sysall-1.0.8/src/sysall.egg-info/top_level.txt
```

### Comparing `sysall-1.0.7/LICENSE` & `sysall-1.0.8/LICENSE`

 * *Files identical despite different names*

### Comparing `sysall-1.0.7/PKG-INFO` & `sysall-1.0.8/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,59 +1,65 @@
 Metadata-Version: 2.1
 Name: sysall
-Version: 1.0.7
+Version: 1.0.8
 Summary: Tool to easily retrieve information from the environment and the network
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
 
-[![sysall Downloads](https://img.shields.io/pypi/dm/sysall)](https://pypi.org/project/sysall/)
+[![Downloads](https://static.pepy.tech/personalized-badge/sysall?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/sysall)
 [![sysall Version](https://img.shields.io/pypi/v/sysall)](https://pypi.org/project/sysall/)
 [![sysall Python Version](https://img.shields.io/pypi/pyversions/sysall)](https://pypi.org/project/sysall/)
 
 SysAll is a tool that allows you to retrieve information about the environment, 
 such as the name of the operating system, processor, RAM, IP address, MAC address of the machine.
 
 It gathers the functionalities of several libraries such as 
 wmi, psutil, platform, getmac, socket in one to facilitate the use/manipulation of environment data
 for Python programmers.
 
-## Installs
+## Set up
 ----
+### Install
 
 ~~~python
 pip install sysall
 ~~~
 
+### Upgrade
+~~~~python
+pip install --upgrade sysall
+~~~~
+
 ## Support
 
 If you want to contact me for questions, bugs, or problems or other : lixnew2@gmail.com
 
-## Getting started
-
-### Python version
+## Python version
 
 Sysall was written for python 3.
 
-### Functions
+## Functions
 
+
+### System
 Returns operating system name, version, release.
 ~~~python
 get_os()
 # You can use the arguments of the function to return or not certain elements. By default they are all on True.
 # If you put them all on False, the function will return 'None'.
-args = name : bool = True, version : bool = True, release : bool = True
+args = name, version, release
 ~~~
 
 
 Returns device name
 ~~~python
 get_device_name()
 ~~~
@@ -66,60 +72,91 @@
 
 
 Returns appdata hostname and path
 ~~~python
 get_appdata()
 # You can use the arguments of the function to return or not certain elements. By default they are all on True.
 # If you put them all on False, the function will return 'None'.
-args = hostname : bool = True, appdata_path : bool = True
+args = hostname, appdata_path
 ~~~
 
 
 Returns the memory size : Mo
 ~~~python
 get_memory()
 ~~~
 
 
-Return the processor brand (Intel, AMD), frequency and cores.
+Returns the processor brand (Intel, AMD), frequency and cores.
 ~~~python
 get_cpu_info()
 # You can use the arguments of the function to return or not certain elements. By default they are all on True.
 # If you put them all on False, the function will return 'None'.
-args = brand: bool = True , cpu_frequency: bool = True, cores: bool = True
+args = brand, cpu_frequency, cores
 ~~~
 
 
 Returns the type of the graphics card
 ~~~python
 get_gpu_info()
 # You can use the arguments of the function to return or not certain elements. By default they are all on True.
 # If you put them all on False, the function will return 'None'.
-args = name: bool = True, ram: bool = True, driver_version: bool = True
+args = name, ram, driver_version
 ~~~
 
 
+Returns the informations of the disk : total free, used
+~~~python
+get_disk_infos()
+# You can use the arguments of the function to return or not certain elements. By default they are all on True.
+# If you put them all on False, the function will return 'None'.
+args = path, total, free, used
+~~~
+
+### Network
+
 Returns the IPv4 address
 ~~~python
 get_IPv4()
 ~~~
 
 
 Returns the MAC address
 ~~~python
 get_MAC()
 ~~~
 
 
-Return the public address
+Returns the public address
 ~~~python
 get_public_ip()
 ~~~
 
 
-Return the informations of the disk : total free, used
+Returns the default gateway address
 ~~~python
-get_disk_infos()
-# You can use the arguments of the function to return or not certain elements. By default they are all on True.
-# If you put them all on False, the function will return 'None'.
-args = path: str = 'C', total : bool = True, free: bool = True, used: bool = True
+get_gateway()
+~~~
+
+
+Returns the address of the sub-mask
+~~~python
+get_submask()
+~~~
+
+
+Returns the address of the DNS server
+~~~python
+get_DNS()
+~~~
+
+
+Returns the DHCP status
+~~~python
+get_DHCP_status()
+~~~
+
+
+Returns the address of the DHCP server
+~~~python
+get_DHCP()
 ~~~
```

### Comparing `sysall-1.0.7/README.md` & `sysall-1.0.8/README.md`

 * *Files 20% similar despite different names*

```diff
@@ -1,45 +1,51 @@
 # SysAll
 
-[![sysall Downloads](https://img.shields.io/pypi/dm/sysall)](https://pypi.org/project/sysall/)
+[![Downloads](https://static.pepy.tech/personalized-badge/sysall?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/sysall)
 [![sysall Version](https://img.shields.io/pypi/v/sysall)](https://pypi.org/project/sysall/)
 [![sysall Python Version](https://img.shields.io/pypi/pyversions/sysall)](https://pypi.org/project/sysall/)
 
 SysAll is a tool that allows you to retrieve information about the environment, 
 such as the name of the operating system, processor, RAM, IP address, MAC address of the machine.
 
 It gathers the functionalities of several libraries such as 
 wmi, psutil, platform, getmac, socket in one to facilitate the use/manipulation of environment data
 for Python programmers.
 
-## Installs
+## Set up
 ----
+### Install
 
 ~~~python
 pip install sysall
 ~~~
 
+### Upgrade
+~~~~python
+pip install --upgrade sysall
+~~~~
+
 ## Support
 
 If you want to contact me for questions, bugs, or problems or other : lixnew2@gmail.com
 
-## Getting started
-
-### Python version
+## Python version
 
 Sysall was written for python 3.
 
-### Functions
+## Functions
 
+
+### System
 Returns operating system name, version, release.
 ~~~python
 get_os()
 # You can use the arguments of the function to return or not certain elements. By default they are all on True.
 # If you put them all on False, the function will return 'None'.
-args = name : bool = True, version : bool = True, release : bool = True
+args = name, version, release
 ~~~
 
 
 Returns device name
 ~~~python
 get_device_name()
 ~~~
@@ -52,60 +58,91 @@
 
 
 Returns appdata hostname and path
 ~~~python
 get_appdata()
 # You can use the arguments of the function to return or not certain elements. By default they are all on True.
 # If you put them all on False, the function will return 'None'.
-args = hostname : bool = True, appdata_path : bool = True
+args = hostname, appdata_path
 ~~~
 
 
 Returns the memory size : Mo
 ~~~python
 get_memory()
 ~~~
 
 
-Return the processor brand (Intel, AMD), frequency and cores.
+Returns the processor brand (Intel, AMD), frequency and cores.
 ~~~python
 get_cpu_info()
 # You can use the arguments of the function to return or not certain elements. By default they are all on True.
 # If you put them all on False, the function will return 'None'.
-args = brand: bool = True , cpu_frequency: bool = True, cores: bool = True
+args = brand, cpu_frequency, cores
 ~~~
 
 
 Returns the type of the graphics card
 ~~~python
 get_gpu_info()
 # You can use the arguments of the function to return or not certain elements. By default they are all on True.
 # If you put them all on False, the function will return 'None'.
-args = name: bool = True, ram: bool = True, driver_version: bool = True
+args = name, ram, driver_version
 ~~~
 
 
+Returns the informations of the disk : total free, used
+~~~python
+get_disk_infos()
+# You can use the arguments of the function to return or not certain elements. By default they are all on True.
+# If you put them all on False, the function will return 'None'.
+args = path, total, free, used
+~~~
+
+### Network
+
 Returns the IPv4 address
 ~~~python
 get_IPv4()
 ~~~
 
 
 Returns the MAC address
 ~~~python
 get_MAC()
 ~~~
 
 
-Return the public address
+Returns the public address
 ~~~python
 get_public_ip()
 ~~~
 
 
-Return the informations of the disk : total free, used
+Returns the default gateway address
 ~~~python
-get_disk_infos()
-# You can use the arguments of the function to return or not certain elements. By default they are all on True.
-# If you put them all on False, the function will return 'None'.
-args = path: str = 'C', total : bool = True, free: bool = True, used: bool = True
+get_gateway()
+~~~
+
+
+Returns the address of the sub-mask
+~~~python
+get_submask()
+~~~
+
+
+Returns the address of the DNS server
+~~~python
+get_DNS()
+~~~
+
+
+Returns the DHCP status
+~~~python
+get_DHCP_status()
+~~~
+
+
+Returns the address of the DHCP server
+~~~python
+get_DHCP()
 ~~~
```

### Comparing `sysall-1.0.7/pyproject.toml` & `sysall-1.0.8/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -7,15 +7,15 @@
     "py-cpuinfo",
     "requests"
 ]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "sysall"
-version = "1.0.7"
+version = "1.0.8"
 authors = [
   { name="LixNew", email="lixnew2@gmail.com" },
 ]
 description = "Tool to easily retrieve information from the environment and the network"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `sysall-1.0.7/src/sysall/SysAll.py` & `sysall-1.0.8/src/sysall/SysAll.py`

 * *Files 22% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 such as the name of the operating system, processor, RAM, IP address, MAC address of the machine.
 
 It gathers the functionalities of several libraries such as 
 wmi, psutil, platform, getmac, socket in one to facilitate the use/manipulation of environment data
 for Python programmers.
 """
 
-__version__ = '1.0.7'
+__version__ = '1.0.8'
 __title__ = 'SysAll'
 __description__ = "Tool to easily retrieve information from the environment and the network"
 __autor__ = 'LixNew'
 __twitter__ = '@LixNew2'
 __url__ = "https://github.com/LixNew2/SysAll"
 
 #Import
@@ -21,22 +21,23 @@
 import psutil
 import socket
 import getmac
 import wmi
 import requests
 import multiprocessing
 import ctypes
+import subprocess
 
 
-
+#System
 
 #Functions
 def get_os(name : bool = True, version : bool = True, release : bool = True) -> dict:
     """
-    Return operating system name (Window, Linux, MacOS)
+    Returns operating system name (Window, Linux, MacOS)
     
     Args:
         name (bool): To return os name. Defaults to True.
         version (bool): To return os version. Defaults to True.
         release (bool): To return os release. Defaults to True.
     """
     
@@ -49,32 +50,32 @@
     #If version (True) add version in os_infos
     if version:
         os_infos['version'] = platform.version()
     #If release (True) add release in os_infos
     if release:
         os_infos['release'] = platform.release()
     
-    #If one or more (True) return os_infos
+    #If one or more (True) returns os_infos
     if (name or version or release):
         return os_infos
     else:
-        #Return None
+        #Returns None
         return None
 
 def get_device_name() -> str:
-    """Return device name"""
+    """Returns device name"""
     return socket.gethostname()
 
 def get_hostname() -> str:
     """Returns the name of the account currently connected to the operating system."""
     return os.getlogin()
 
 def get_appdata(hostname : bool = True, appdata_path : bool = True) -> dict:
     """
-    Return appdata hostname
+    Returns appdata hostname
     
     Args:
         hostname (bool) : To return appdata hostname. Defautls to True.
         appdata_path (bool): To return appdata path. Defaults to True.
     """
     
     #Dictionary that saves the returned information
@@ -93,15 +94,15 @@
     if (hostname or appdata_path):  
         return appdata_infos
     else:
         #Return None
         return None
 
 def get_memory() -> float:
-    """Return the memory size : Mo"""
+    """Returns the memory size : Mo"""
     
     memory_size = psutil.virtual_memory().total
     memory_size = memory_size / (1024**2)
     
     return memory_size
 
 def get_cpu_info(brand: bool = True, cpu_frequency: bool = True, cores : bool = True) -> dict:
@@ -122,19 +123,19 @@
     #If cpu_frequency (True) add cpu_frequency in processor_infos
     if cpu_frequency:
         processor_infos["frequency"] = cpuinfo.get_cpu_info()['hz_actual_friendly']
         #If cores (True) add number of processor cores in processor_infos
     if cores:
         processor_infos["cores"] = multiprocessing.cpu_count()
         
-    #If one or more (True) return processor _infos
+    #If one or more (True) returns processor _infos
     if (brand or cpu_frequency or cores):
         return processor_infos
     else:
-        #Return None
+        #Returns None
         return None
             
 def get_gpu_info(name: bool = True, ram: bool = True, driver_version: bool = True) -> dict:
     """
     Returns the informations of the graphics card.
 
     Args:
@@ -164,37 +165,24 @@
         #If ram (True) add ram in gpu_infos    
         if ram:
             gpu_infos[f"RAM GPU{AMOUNT}"] = gpu.AdapterRAM
         #If driver_version (True) add driver_version in gpu_infos
         if driver_version:
             gpu_infos[f"Driver_Version GPU{AMOUNT}"] = gpu.DriverVersion
     
-    #If one or more (True) return gpu_infos
+    #If one or more (True) returns gpu_infos
     if (name or ram or driver_version):         
         return gpu_infos
     else:
-        #Return None
+        #Returns None
         return None
 
-def get_IPv4() ->str:
-    """Return the IPv4 address"""
-    return socket.gethostbyname(socket.gethostname())
-
-def get_MAC() -> str:
-    """Return the MAC address"""
-    return getmac.get_mac_address()
-
-def get_public_ip():
-    """Return the public address"""
-    ip = requests.get('https://api64.ipify.org').text
-    return ip
-
 def get_disk_infos(path: str = 'C', total : bool = True, free: bool = True, used: bool = True):
     """
-    Return the informations of the disk : total free, used
+    Returns the informations of the disk : total free, used
 
     Args:
         path (str): Reader's letter. Defaults to 'C'.
         total (bool, optional): To return full size of the disk. Defaults to True.
         free (bool, optional): To return free size of the disk. Defaults to True.
         used (bool, optional): To return used size of the disk. Defaults to True.
 
@@ -226,8 +214,80 @@
         disk_infos['used'] =  f"{used_space / (1024**3):.2f}"
     
     #If one or more (True) return gpu_infos
     if (total or free or used):
         return disk_infos
     else:
         #Return None
-        return None
+        return None
+    
+#Network
+
+def get_IPv4() ->str:
+    """Returns the IPv4 address"""
+    return socket.gethostbyname(socket.gethostname())
+
+def get_MAC() -> str:
+    """Returns the MAC address"""
+    return getmac.get_mac_address()
+
+def get_public_ip():
+    """Returns the public address"""
+    ip = requests.get('https://api64.ipify.org').text
+    return ip
+
+def _network_infos():
+    """Do not call"""
+    
+    net = subprocess.check_output('ipconfig /all')
+
+    return net
+
+def get_gateway(net=_network_infos()) -> str:
+    """Returns the default gateway address"""
+    
+    for line in net.split(b'\r\n'):
+        if b'Default Gateway' in line or b'Passerelle par d' in line:
+            gateway = line.split(b':')[1].decode('utf-8').strip()
+            if gateway != "":
+                return gateway
+            
+def get_submask(net=_network_infos()) -> str:
+    """Returns the address of the sub-mask"""
+    
+    for line in net.split(b'\r\n'):
+        if b'Subnet Mask' in line or b'Masque de sous-r' in line:
+            submask = line.split(b':')[1].decode('utf-8').strip()
+            return submask
+    
+def get_DNS(net=_network_infos()) -> str:
+    """Returns the address of the DNS server"""
+    
+    for line in net.split(b'\r\n'):
+        if b'DNS Servers' in line or b'Serveurs DNS' in line:
+            dns = line.split(b':')[1].decode('utf-8').strip()
+            if dns != "fec0":
+                return dns
+            
+def get_DHCP_status(net=_network_infos()) -> str:
+    """Returns the DHCP status
+    
+    If the function returns "True" it means that DHCP is enabled.
+    On the contrary, if the function returns "False", it means that DHCP is disabled.
+    """
+    
+    for line in net.split(b'\r\n'):
+        if b'DHCP Enabled' in line or b'DHCP activ' in line:
+            dhcp_st = line.split(b':')[1].decode('utf-8').strip()
+            if dhcp_st == "Yes" or dhcp_st == "Oui":
+                return True
+            else:
+                return False  
+    
+def get_DHCP(net=_network_infos()) -> str:
+    """Returns the address of the DNS server"""
+    
+    for line in net.split(b'\r\n'):
+        if b'DHCP Server' in line or b'Serveur DHCP' in line:
+            dhcp = line.split(b':')[1].decode('utf-8').strip()
+            if dhcp != "":
+                return dhcp
```

### Comparing `sysall-1.0.7/src/sysall.egg-info/PKG-INFO` & `sysall-1.0.8/src/sysall.egg-info/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,59 +1,65 @@
 Metadata-Version: 2.1
 Name: sysall
-Version: 1.0.7
+Version: 1.0.8
 Summary: Tool to easily retrieve information from the environment and the network
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
 
-[![sysall Downloads](https://img.shields.io/pypi/dm/sysall)](https://pypi.org/project/sysall/)
+[![Downloads](https://static.pepy.tech/personalized-badge/sysall?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/sysall)
 [![sysall Version](https://img.shields.io/pypi/v/sysall)](https://pypi.org/project/sysall/)
 [![sysall Python Version](https://img.shields.io/pypi/pyversions/sysall)](https://pypi.org/project/sysall/)
 
 SysAll is a tool that allows you to retrieve information about the environment, 
 such as the name of the operating system, processor, RAM, IP address, MAC address of the machine.
 
 It gathers the functionalities of several libraries such as 
 wmi, psutil, platform, getmac, socket in one to facilitate the use/manipulation of environment data
 for Python programmers.
 
-## Installs
+## Set up
 ----
+### Install
 
 ~~~python
 pip install sysall
 ~~~
 
+### Upgrade
+~~~~python
+pip install --upgrade sysall
+~~~~
+
 ## Support
 
 If you want to contact me for questions, bugs, or problems or other : lixnew2@gmail.com
 
-## Getting started
-
-### Python version
+## Python version
 
 Sysall was written for python 3.
 
-### Functions
+## Functions
 
+
+### System
 Returns operating system name, version, release.
 ~~~python
 get_os()
 # You can use the arguments of the function to return or not certain elements. By default they are all on True.
 # If you put them all on False, the function will return 'None'.
-args = name : bool = True, version : bool = True, release : bool = True
+args = name, version, release
 ~~~
 
 
 Returns device name
 ~~~python
 get_device_name()
 ~~~
@@ -66,60 +72,91 @@
 
 
 Returns appdata hostname and path
 ~~~python
 get_appdata()
 # You can use the arguments of the function to return or not certain elements. By default they are all on True.
 # If you put them all on False, the function will return 'None'.
-args = hostname : bool = True, appdata_path : bool = True
+args = hostname, appdata_path
 ~~~
 
 
 Returns the memory size : Mo
 ~~~python
 get_memory()
 ~~~
 
 
-Return the processor brand (Intel, AMD), frequency and cores.
+Returns the processor brand (Intel, AMD), frequency and cores.
 ~~~python
 get_cpu_info()
 # You can use the arguments of the function to return or not certain elements. By default they are all on True.
 # If you put them all on False, the function will return 'None'.
-args = brand: bool = True , cpu_frequency: bool = True, cores: bool = True
+args = brand, cpu_frequency, cores
 ~~~
 
 
 Returns the type of the graphics card
 ~~~python
 get_gpu_info()
 # You can use the arguments of the function to return or not certain elements. By default they are all on True.
 # If you put them all on False, the function will return 'None'.
-args = name: bool = True, ram: bool = True, driver_version: bool = True
+args = name, ram, driver_version
 ~~~
 
 
+Returns the informations of the disk : total free, used
+~~~python
+get_disk_infos()
+# You can use the arguments of the function to return or not certain elements. By default they are all on True.
+# If you put them all on False, the function will return 'None'.
+args = path, total, free, used
+~~~
+
+### Network
+
 Returns the IPv4 address
 ~~~python
 get_IPv4()
 ~~~
 
 
 Returns the MAC address
 ~~~python
 get_MAC()
 ~~~
 
 
-Return the public address
+Returns the public address
 ~~~python
 get_public_ip()
 ~~~
 
 
-Return the informations of the disk : total free, used
+Returns the default gateway address
 ~~~python
-get_disk_infos()
-# You can use the arguments of the function to return or not certain elements. By default they are all on True.
-# If you put them all on False, the function will return 'None'.
-args = path: str = 'C', total : bool = True, free: bool = True, used: bool = True
+get_gateway()
+~~~
+
+
+Returns the address of the sub-mask
+~~~python
+get_submask()
+~~~
+
+
+Returns the address of the DNS server
+~~~python
+get_DNS()
+~~~
+
+
+Returns the DHCP status
+~~~python
+get_DHCP_status()
+~~~
+
+
+Returns the address of the DHCP server
+~~~python
+get_DHCP()
 ~~~
```

