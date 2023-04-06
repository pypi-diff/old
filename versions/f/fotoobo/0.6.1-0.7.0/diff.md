# Comparing `tmp/fotoobo-0.6.1.tar.gz` & `tmp/fotoobo-0.7.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "fotoobo-0.6.1.tar", max compression
+gzip compressed data, was "fotoobo-0.7.0.tar", max compression
```

## Comparing `fotoobo-0.6.1.tar` & `fotoobo-0.7.0.tar`

### file list

```diff
@@ -1,64 +1,64 @@
--rw-r--r--   0        0        0     7633 2023-03-23 10:22:10.140868 fotoobo-0.6.1/LICENSE
--rw-r--r--   0        0        0     2797 2023-03-23 10:22:10.140868 fotoobo-0.6.1/README.md
--rw-r--r--   0        0        0      256 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/__init__.py
--rw-r--r--   0        0        0      206 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/__init__.py
--rw-r--r--   0        0        0     1516 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/convert.py
--rw-r--r--   0        0        0       20 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/ems/__init__.py
--rw-r--r--   0        0        0     1431 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/ems/get_commands.py
--rw-r--r--   0        0        0      717 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/ems/main.py
--rw-r--r--   0        0        0     7665 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/ems/monitor.py
--rw-r--r--   0        0        0       20 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/faz/__init__.py
--rw-r--r--   0        0        0      944 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/faz/get_commands.py
--rw-r--r--   0        0        0      593 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/faz/main.py
--rw-r--r--   0        0        0       20 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/fgt/__init__.py
--rw-r--r--   0        0        0     1553 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/fgt/check_commands.py
--rw-r--r--   0        0        0      570 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/fgt/config_commands.py
--rw-r--r--   0        0        0     1147 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/fgt/get_commands.py
--rw-r--r--   0        0        0     1465 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/fgt/main.py
--rw-r--r--   0        0        0       20 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/fmg/__init__.py
--rw-r--r--   0        0        0     2620 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/fmg/get_commands.py
--rw-r--r--   0        0        0     1948 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/fmg/main.py
--rw-r--r--   0        0        0      948 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/get.py
--rw-r--r--   0        0        0     4081 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/cli/main.py
--rw-r--r--   0        0        0      196 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/exceptions/__init__.py
--rw-r--r--   0        0        0     1966 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/exceptions/exceptions.py
--rw-r--r--   0        0        0      190 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/fortinet/__init__.py
--rw-r--r--   0        0        0    13955 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/fortinet/convert.py
--rw-r--r--   0        0        0     1023 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/fortinet/fortianalyzer.py
--rw-r--r--   0        0        0     5431 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/fortinet/forticlientems.py
--rw-r--r--   0        0        0     2878 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/fortinet/fortigate.py
--rw-r--r--   0        0        0    11342 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/fortinet/fortigate_config.py
--rw-r--r--   0        0        0     8668 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/fortinet/fortigate_config_check.py
--rw-r--r--   0        0        0      584 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/fortinet/fortigate_info.py
--rw-r--r--   0        0        0    10419 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/fortinet/fortimanager.py
--rw-r--r--   0        0        0     6468 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/fortinet/fortinet.py
--rw-r--r--   0        0        0      322 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/helpers/__init__.py
--rw-r--r--   0        0        0     1227 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/helpers/cli.py
--rw-r--r--   0        0        0     3543 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/helpers/config.py
--rw-r--r--   0        0        0     6322 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/helpers/files.py
--rw-r--r--   0        0        0    10407 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/helpers/log.py
--rw-r--r--   0        0        0     9300 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/helpers/output.py
--rw-r--r--   0        0        0      128 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/inventory/__init__.py
--rw-r--r--   0        0        0      568 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/inventory/generic.py
--rw-r--r--   0        0        0     4296 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/inventory/inventory.py
--rwxr-xr-x   0        0        0     1359 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/main.py
--rw-r--r--   0        0        0      440 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/__init__.py
--rw-r--r--   0        0        0     1153 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/convert.py
--rw-r--r--   0        0        0       92 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/ems/__init__.py
--rw-r--r--   0        0        0     1518 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/ems/get.py
--rw-r--r--   0        0        0     7725 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/ems/monitor.py
--rw-r--r--   0        0        0       56 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/faz/__init__.py
--rw-r--r--   0        0        0      779 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/faz/get.py
--rw-r--r--   0        0        0      125 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/fgt/__init__.py
--rw-r--r--   0        0        0     4583 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/fgt/check.py
--rw-r--r--   0        0        0     2411 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/fgt/config.py
--rw-r--r--   0        0        0     1114 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/fgt/get.py
--rw-r--r--   0        0        0     3311 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/fgt/main.py
--rw-r--r--   0        0        0      140 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/fmg/__init__.py
--rw-r--r--   0        0        0     4271 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/fmg/get.py
--rw-r--r--   0        0        0     2569 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/fmg/main.py
--rw-r--r--   0        0        0     1093 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/fmg/set_.py
--rw-r--r--   0        0        0     2035 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/get.py
--rw-r--r--   0        0        0     1306 2023-03-23 10:22:10.144868 fotoobo-0.6.1/fotoobo/utils/greet.py
--rw-r--r--   0        0        0     3730 2023-03-23 10:22:10.148868 fotoobo-0.6.1/pyproject.toml
--rw-r--r--   0        0        0     3504 1970-01-01 00:00:00.000000 fotoobo-0.6.1/PKG-INFO
+-rw-r--r--   0        0        0     7633 2023-04-06 11:48:01.689492 fotoobo-0.7.0/LICENSE
+-rw-r--r--   0        0        0     2797 2023-04-06 11:48:01.689492 fotoobo-0.7.0/README.md
+-rw-r--r--   0        0        0      256 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/__init__.py
+-rw-r--r--   0        0        0      206 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/__init__.py
+-rw-r--r--   0        0        0     1516 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/convert.py
+-rw-r--r--   0        0        0       20 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/ems/__init__.py
+-rw-r--r--   0        0        0     1431 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/ems/get_commands.py
+-rw-r--r--   0        0        0      717 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/ems/main.py
+-rw-r--r--   0        0        0     7665 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/ems/monitor.py
+-rw-r--r--   0        0        0       20 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/faz/__init__.py
+-rw-r--r--   0        0        0      944 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/faz/get_commands.py
+-rw-r--r--   0        0        0      593 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/faz/main.py
+-rw-r--r--   0        0        0       20 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/fgt/__init__.py
+-rw-r--r--   0        0        0     1553 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/fgt/check_commands.py
+-rw-r--r--   0        0        0     1303 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/fgt/config_commands.py
+-rw-r--r--   0        0        0     1147 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/fgt/get_commands.py
+-rw-r--r--   0        0        0     1759 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/fgt/main.py
+-rw-r--r--   0        0        0       20 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/fmg/__init__.py
+-rw-r--r--   0        0        0     2620 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/fmg/get_commands.py
+-rw-r--r--   0        0        0     1948 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/fmg/main.py
+-rw-r--r--   0        0        0      948 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/get.py
+-rw-r--r--   0        0        0     4081 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/cli/main.py
+-rw-r--r--   0        0        0      196 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/exceptions/__init__.py
+-rw-r--r--   0        0        0     1966 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/exceptions/exceptions.py
+-rw-r--r--   0        0        0      190 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/fortinet/__init__.py
+-rw-r--r--   0        0        0    13955 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/fortinet/convert.py
+-rw-r--r--   0        0        0     1023 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/fortinet/fortianalyzer.py
+-rw-r--r--   0        0        0     5431 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/fortinet/forticlientems.py
+-rw-r--r--   0        0        0     2878 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/fortinet/fortigate.py
+-rw-r--r--   0        0        0    11342 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/fortinet/fortigate_config.py
+-rw-r--r--   0        0        0     8668 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/fortinet/fortigate_config_check.py
+-rw-r--r--   0        0        0      584 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/fortinet/fortigate_info.py
+-rw-r--r--   0        0        0    10419 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/fortinet/fortimanager.py
+-rw-r--r--   0        0        0     6468 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/fortinet/fortinet.py
+-rw-r--r--   0        0        0      322 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/helpers/__init__.py
+-rw-r--r--   0        0        0     1227 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/helpers/cli.py
+-rw-r--r--   0        0        0     3435 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/helpers/config.py
+-rw-r--r--   0        0        0     6414 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/helpers/files.py
+-rw-r--r--   0        0        0    10407 2023-04-06 11:48:01.693492 fotoobo-0.7.0/fotoobo/helpers/log.py
+-rw-r--r--   0        0        0     9300 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/helpers/output.py
+-rw-r--r--   0        0        0      128 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/inventory/__init__.py
+-rw-r--r--   0        0        0      568 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/inventory/generic.py
+-rw-r--r--   0        0        0     4296 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/inventory/inventory.py
+-rwxr-xr-x   0        0        0     1359 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/main.py
+-rw-r--r--   0        0        0      440 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/__init__.py
+-rw-r--r--   0        0        0     1153 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/convert.py
+-rw-r--r--   0        0        0       92 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/ems/__init__.py
+-rw-r--r--   0        0        0     1518 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/ems/get.py
+-rw-r--r--   0        0        0     7725 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/ems/monitor.py
+-rw-r--r--   0        0        0       56 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/faz/__init__.py
+-rw-r--r--   0        0        0      779 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/faz/get.py
+-rw-r--r--   0        0        0      125 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/fgt/__init__.py
+-rw-r--r--   0        0        0     4583 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/fgt/check.py
+-rw-r--r--   0        0        0     3423 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/fgt/config.py
+-rw-r--r--   0        0        0     1114 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/fgt/get.py
+-rw-r--r--   0        0        0     3286 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/fgt/main.py
+-rw-r--r--   0        0        0      140 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/fmg/__init__.py
+-rw-r--r--   0        0        0     4271 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/fmg/get.py
+-rw-r--r--   0        0        0     2569 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/fmg/main.py
+-rw-r--r--   0        0        0     1093 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/fmg/set_.py
+-rw-r--r--   0        0        0     2035 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/get.py
+-rw-r--r--   0        0        0     1306 2023-04-06 11:48:01.697492 fotoobo-0.7.0/fotoobo/utils/greet.py
+-rw-r--r--   0        0        0     3730 2023-04-06 11:48:01.697492 fotoobo-0.7.0/pyproject.toml
+-rw-r--r--   0        0        0     3504 1970-01-01 00:00:00.000000 fotoobo-0.7.0/PKG-INFO
```

### Comparing `fotoobo-0.6.1/LICENSE` & `fotoobo-0.7.0/LICENSE`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/README.md` & `fotoobo-0.7.0/README.md`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/cli/convert.py` & `fotoobo-0.7.0/fotoobo/cli/convert.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/cli/ems/get_commands.py` & `fotoobo-0.7.0/fotoobo/cli/ems/get_commands.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/cli/ems/main.py` & `fotoobo-0.7.0/fotoobo/cli/ems/main.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/cli/ems/monitor.py` & `fotoobo-0.7.0/fotoobo/cli/ems/monitor.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/cli/faz/get_commands.py` & `fotoobo-0.7.0/fotoobo/cli/faz/get_commands.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/cli/faz/main.py` & `fotoobo-0.7.0/fotoobo/cli/faz/main.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/cli/fgt/check_commands.py` & `fotoobo-0.7.0/fotoobo/cli/fgt/check_commands.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/cli/fgt/get_commands.py` & `fotoobo-0.7.0/fotoobo/cli/fgt/get_commands.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/cli/fgt/main.py` & `fotoobo-0.7.0/fotoobo/cli/fgt/main.py`

 * *Files 11% similar despite different names*

```diff
@@ -32,22 +32,30 @@
 app.add_typer(config.app, name="config", help="FortiGate config file commands")
 
 
 @app.command()
 def backup(
     host: str = typer.Argument(
         "",
-        help="The FortiGate hostname to access (must be defined in inventory)",
+        help="The FortiGate to backup (must be defined in inventory). Backups all if left empty.",
         show_default=False,
         metavar="[host]",
     ),
+    backup_dir: str = typer.Option(
+        None,
+        "--backup-dir",
+        "-b",
+        help="The directory to save the backup(s) to. Default is the current working directory.",
+        show_default=False,
+        metavar="backup_dir",
+    ),
     ftp_server: str = typer.Option(
-        None, "--ftp", help="the ftp configuration from the inventory", metavar="server"
+        None, "--ftp", "-f", help="the ftp configuration from the inventory", metavar="server"
     ),
     smtp_server: str = typer.Option(
-        None, "--smtp", help="the smtp configuration from the inventory", metavar="server"
+        None, "--smtp", "-s", help="the smtp configuration from the inventory", metavar="server"
     ),
 ) -> None:
     """
     Backup one or more FortiGate(s)
     """
-    utils.fgt.backup(host, ftp_server, smtp_server)
+    utils.fgt.backup(host, backup_dir, ftp_server, smtp_server)
```

### Comparing `fotoobo-0.6.1/fotoobo/cli/fmg/get_commands.py` & `fotoobo-0.7.0/fotoobo/cli/fmg/get_commands.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/cli/fmg/main.py` & `fotoobo-0.7.0/fotoobo/cli/fmg/main.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/cli/get.py` & `fotoobo-0.7.0/fotoobo/cli/get.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/cli/main.py` & `fotoobo-0.7.0/fotoobo/cli/main.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/exceptions/exceptions.py` & `fotoobo-0.7.0/fotoobo/exceptions/exceptions.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/fortinet/convert.py` & `fotoobo-0.7.0/fotoobo/fortinet/convert.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/fortinet/fortianalyzer.py` & `fotoobo-0.7.0/fotoobo/fortinet/fortianalyzer.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/fortinet/forticlientems.py` & `fotoobo-0.7.0/fotoobo/fortinet/forticlientems.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/fortinet/fortigate.py` & `fotoobo-0.7.0/fotoobo/fortinet/fortigate.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/fortinet/fortigate_config.py` & `fotoobo-0.7.0/fotoobo/fortinet/fortigate_config.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/fortinet/fortigate_config_check.py` & `fotoobo-0.7.0/fotoobo/fortinet/fortigate_config_check.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/fortinet/fortigate_info.py` & `fotoobo-0.7.0/fotoobo/fortinet/fortigate_info.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/fortinet/fortimanager.py` & `fotoobo-0.7.0/fotoobo/fortinet/fortimanager.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/fortinet/fortinet.py` & `fotoobo-0.7.0/fotoobo/fortinet/fortinet.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/helpers/cli.py` & `fotoobo-0.7.0/fotoobo/helpers/cli.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/helpers/config.py` & `fotoobo-0.7.0/fotoobo/helpers/config.py`

 * *Files 14% similar despite different names*

```diff
@@ -18,15 +18,14 @@
     """
     This is the configuration dataclass for the global configuration options.
     First all the configuration options must be initialized.
     If an option is not defined here it is not guaranteed that it may be used later in the code.
     """
 
     # set default values
-    backup_dir: str = ""
     inventory_file: str = "inventory.yaml"
     logging: Union[Dict[str, Any], None] = None
     audit_logging: Union[Dict[str, Any], None] = None
     no_logo: bool = False
     snmp_community: str = ""
     cli_info: Dict[str, Any] = field(default_factory=dict)
 
@@ -63,15 +62,14 @@
 
         if config_file:
             if loaded_config := load_yaml_file(config_file):
                 # We need a dict here
                 loaded_config = dict(loaded_config)
 
                 # then set the config options from file if set in file
-                self.backup_dir = loaded_config.get("backup_dir", self.backup_dir)
                 self.inventory_file = loaded_config.get("inventory", self.inventory_file)
 
                 if loaded_config.get("logging"):
                     self.logging = loaded_config["logging"]
 
                 if loaded_config.get("audit_logging"):
                     self.audit_logging = loaded_config["audit_logging"]
```

### Comparing `fotoobo-0.6.1/fotoobo/helpers/files.py` & `fotoobo-0.7.0/fotoobo/helpers/files.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 """
 Some helper functions for file manipulation.
 """
-
 import json
 import logging
 import os
 import re
 from ftplib import FTP, FTP_TLS
+from pathlib import Path
 from typing import Any, Dict, List, Union
 from zipfile import ZIP_DEFLATED, ZipFile
 
 import jinja2
 import yaml
 
 from fotoobo.exceptions import GeneralError
@@ -58,25 +58,27 @@
         if hasattr(server, "protocol"):
             protocol = server.protocol
         else:
             protocol = "sftp"
 
         if protocol == "sftp":
             with FTP_TLS(server.hostname) as ftp:
+                log.debug("SFTP transfer for '%s'", server.hostname)
                 ftp.sendcmd(f"USER {server.username}")
                 ftp.sendcmd(f"PASS {server.password}")
                 ftp.cwd(server.directory)
                 with open(file, "rb") as ftp_file:
                     response = ftp.storbinary(f"STOR {os.path.basename(file)}", ftp_file)
                     if response != "226 Transfer complete.":
                         if code := re.search(r"^([0-9]{0,3})\s", response):
                             retcode = int(code[1])
 
         elif protocol == "ftp":
             with FTP(server.hostname, server.username, server.password) as ftp:
+                log.debug("FTP transfer for '%s'", server.hostname)
                 ftp.cwd(server.directory)
                 with open(file, "rb") as ftp_file:
                     response = ftp.storbinary(f"STOR {os.path.basename(file)}", ftp_file)
                     if response != "226 Transfer complete.":
                         if code := re.search(r"^([0-9]{0,3})\s", response):
                             retcode = int(code[1])
 
@@ -173,22 +175,23 @@
     Saves a data structure to a file with a given Jinja2 template. The data structure and the
     variables you can use in the template file depend on the utility the data comes from. See the
     docs of the used utility to see what variables you're intended to use.
 
     Args:
         data (Dict[Any, Any]): The data used in the template
 
-        template_file (str): Filename of the Jinja2 template file. The path to the template_file
-        is always a relative path (at the moment). Absolute paths are not supported.
+        template_file (str): Filename of the Jinja2 template file
 
         output_file (str): The file to write the output to
     """
     log.debug("template_file is: %s", template_file)
-    template_env = jinja2.Environment(loader=jinja2.FileSystemLoader("./"), trim_blocks=True)
-    template = template_env.get_template(template_file)
+    template_env = jinja2.Environment(
+        loader=jinja2.FileSystemLoader(Path(template_file).parent), trim_blocks=True
+    )
+    template = template_env.get_template(Path(template_file).name)
     output = template.render(data)
     with open(output_file, "w", encoding="UTF-8") as file:
         file.write(output)
 
 
 def save_yaml_file(filename: str, data: Union[List[Any], Dict[str, Any]]) -> bool:
     """
```

### Comparing `fotoobo-0.6.1/fotoobo/helpers/log.py` & `fotoobo-0.7.0/fotoobo/helpers/log.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -75,16 +75,16 @@
 
         return (
             " ".join(
                 [
                     # Syslog header parts
                     f"<{prival}>1",
                     timestamp,
-                    "fotoobo",
                     f"{self.hostname}",
+                    "fotoobo",
                     f"{record.process}",
                     msg_id,
                     "-",
                     # Syslog message parts
                     f"username={self.user}",
                 ]
             )
```

### Comparing `fotoobo-0.6.1/fotoobo/helpers/output.py` & `fotoobo-0.7.0/fotoobo/helpers/output.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/inventory/generic.py` & `fotoobo-0.7.0/fotoobo/inventory/generic.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/inventory/inventory.py` & `fotoobo-0.7.0/fotoobo/inventory/inventory.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/main.py` & `fotoobo-0.7.0/fotoobo/main.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/utils/convert.py` & `fotoobo-0.7.0/fotoobo/utils/convert.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/utils/ems/get.py` & `fotoobo-0.7.0/fotoobo/utils/ems/get.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/utils/ems/monitor.py` & `fotoobo-0.7.0/fotoobo/utils/ems/monitor.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/utils/faz/get.py` & `fotoobo-0.7.0/fotoobo/utils/faz/get.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/utils/fgt/check.py` & `fotoobo-0.7.0/fotoobo/utils/fgt/check.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/utils/fgt/get.py` & `fotoobo-0.7.0/fotoobo/utils/fgt/get.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/utils/fgt/main.py` & `fotoobo-0.7.0/fotoobo/utils/fgt/main.py`

 * *Files 15% similar despite different names*

```diff
@@ -13,55 +13,61 @@
 from fotoobo.helpers.output import Output
 from fotoobo.inventory import Inventory
 
 log = logging.getLogger("fotoobo")
 
 
 def backup(  # pylint: disable=too-many-locals, too-many-branches
-    host: str, ftp_server: Optional[str] = None, smtp_server: Optional[str] = None
+    host: str,
+    backup_dir: str = "",
+    ftp_server: Optional[str] = None,
+    smtp_server: Optional[str] = None,
 ) -> None:
     """
     Create a FortiGate configuration backup into a file and optionally upload it to an FTP server.
 
     Args:
-        host (str):  the host from the inventory to get the backup. If no host is given all
-                     FortiGate devices in the inventory are backed up.
-        ftp_server:  the FTP server from the inventory to upload the backup to. You may omit this
-                     argument to only safe the backup to a file. This argument also compresses
-                     the configuration file into a zip file.
-        smtp_server: the SMTP server from the inventory to send mail messages if errors occur
+        host (str):         The host from the inventory to get the backup. If no host is given all
+                            FortiGate devices in the inventory are backed up.
+        backup_dir (str):   The directory to save tha backup(s) to
+        ftp_server (str):   The FTP server from the inventory to upload the backup to. You may omit
+                            this argument to only safe the backup to a file. This argument also
+                            compresses the configuration file into a zip file.
+        smtp_server (str):  The SMTP server from the inventory to send mail messages if errors occur
     """
-    for option in ["backup_dir"]:
-        if not getattr(config, option, None):
-            raise GeneralError(f"mandatory option '{option}' not set")
+    output = Output()
     inventory = Inventory(config.inventory_file)
     fgts = inventory.get(host, "fortigate")
+    if not backup_dir:
+        backup_dir = os.getcwd()
 
-    create_dir(config.backup_dir)
-
-    output = Output()
+    create_dir(backup_dir)
 
     # backup every FortiGate
     for name, fgt in fgts.items():
         log.debug("backup FortiGate '%s'", name)
-        config_file = os.path.join(config.backup_dir, name + ".conf")
+        config_file = os.path.join(backup_dir, name + ".conf")
+
         if os.path.isfile(config_file):
             os.remove(config_file)
 
         try:
             data: str = fgt.backup()
+
         except GeneralError as err:
             output.add(err.message)
             continue
+
         except APIError as err:
             output.add(f"{name} returned {err.message}")
             continue
 
         if data.startswith("#config-version"):
             log.info("backup '%s' succeeded", name)
+
         else:
             data_json = json.loads(data)
             log.error("backup '%s' failed with error '%s'", name, data_json["http_status"])
             continue
 
         with open(config_file, "w", encoding="UTF-8") as file:
             file.writelines(data)
@@ -71,18 +77,18 @@
             continue
 
         if ftp_server:
             if ftp_server in inventory.assets:
                 server = inventory.assets[ftp_server]
                 log.debug("compressing configuration '%s'", name)
                 time: str = datetime.datetime.now().strftime("%Y%m%d-%H%M")
-                zip_file = os.path.join(config.backup_dir, name + "-" + time + ".conf.zip")
+                zip_file = os.path.join(backup_dir, name + "-" + time + ".conf.zip")
                 file_to_zip(config_file, zip_file)
-                log.debug("FTP transfer for '%s'", name)
                 file_to_ftp(zip_file, server)
                 os.remove(zip_file)
+
             else:
                 raise GeneralWarning(f"ftp server '{ftp_server}' not found in inventory")
 
     if smtp_server:
         if smtp_server in inventory.assets:
             output.send_mail(inventory.assets[smtp_server])
```

### Comparing `fotoobo-0.6.1/fotoobo/utils/fmg/get.py` & `fotoobo-0.7.0/fotoobo/utils/fmg/get.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/utils/fmg/main.py` & `fotoobo-0.7.0/fotoobo/utils/fmg/main.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/utils/fmg/set_.py` & `fotoobo-0.7.0/fotoobo/utils/fmg/set_.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/utils/get.py` & `fotoobo-0.7.0/fotoobo/utils/get.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/fotoobo/utils/greet.py` & `fotoobo-0.7.0/fotoobo/utils/greet.py`

 * *Files identical despite different names*

### Comparing `fotoobo-0.6.1/pyproject.toml` & `fotoobo-0.7.0/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry]
 name = "fotoobo"
-version = "0.6.1"
+version = "0.7.0"
 description = "The awesome Fortinet Toolbox"
 authors = ["Patrik Spiess <patrik.spiess@mgb.ch>", "Lukas Murer-Jäckle <lukas.murer@mgb.ch>"]
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = ">=3.8.0, <3.12"
 typer = "~0.6.0"
```

### Comparing `fotoobo-0.6.1/PKG-INFO` & `fotoobo-0.7.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fotoobo
-Version: 0.6.1
+Version: 0.7.0
 Summary: The awesome Fortinet Toolbox
 Author: Patrik Spiess
 Author-email: patrik.spiess@mgb.ch
 Requires-Python: >=3.8.0,<3.12
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

