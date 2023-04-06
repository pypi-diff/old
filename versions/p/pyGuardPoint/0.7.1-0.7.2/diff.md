# Comparing `tmp/pyGuardPoint-0.7.1.tar.gz` & `tmp/pyGuardPoint-0.7.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyGuardPoint-0.7.1.tar", last modified: Wed Apr  5 13:20:15 2023, max compression
+gzip compressed data, was "pyGuardPoint-0.7.2.tar", last modified: Thu Apr  6 11:06:38 2023, max compression
```

## Comparing `pyGuardPoint-0.7.1.tar` & `pyGuardPoint-0.7.2.tar`

### file list

```diff
@@ -1,29 +1,29 @@
-drwxrwxrwx   0        0        0        0 2023-04-05 13:20:15.266958 pyGuardPoint-0.7.1/
--rw-rw-rw-   0        0        0    11558 2022-09-27 13:07:38.000000 pyGuardPoint-0.7.1/LICENSE.txt
--rw-rw-rw-   0        0        0      199 2023-04-05 13:20:15.265936 pyGuardPoint-0.7.1/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-05 13:20:15.254937 pyGuardPoint-0.7.1/pyGuardPoint/
--rw-rw-rw-   0        0        0      250 2023-03-30 08:56:57.000000 pyGuardPoint-0.7.1/pyGuardPoint/__init__.py
--rw-rw-rw-   0        0        0      997 2023-03-03 10:58:18.000000 pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_areas.py
--rw-rw-rw-   0        0        0    11137 2023-04-05 12:23:31.000000 pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_cardholders.py
--rw-rw-rw-   0        0        0     6687 2023-04-05 13:08:15.000000 pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_cards.py
--rw-rw-rw-   0        0        0     1170 2023-03-16 16:56:01.000000 pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_customizedfields.py
--rw-rw-rw-   0        0        0     1175 2023-03-16 16:56:01.000000 pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_personaldetails.py
--rw-rw-rw-   0        0        0     2462 2023-03-17 15:44:40.000000 pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_scheduledmags.py
--rw-rw-rw-   0        0        0     1314 2023-03-17 12:07:11.000000 pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_securitygroups.py
--rw-rw-rw-   0        0        0     4902 2023-04-05 10:42:09.000000 pyGuardPoint-0.7.1/pyGuardPoint/_odata_filter.py
--rw-rw-rw-   0        0        0     1636 2023-03-31 09:30:04.000000 pyGuardPoint-0.7.1/pyGuardPoint/_str_match_algo.py
--rw-rw-rw-   0        0        0     2393 2023-04-03 15:05:33.000000 pyGuardPoint-0.7.1/pyGuardPoint/guardpoint.py
--rw-rw-rw-   0        0        0     4058 2023-04-05 09:36:31.000000 pyGuardPoint-0.7.1/pyGuardPoint/guardpoint_async.py
--rw-rw-rw-   0        0        0     5799 2023-04-05 10:41:13.000000 pyGuardPoint-0.7.1/pyGuardPoint/guardpoint_connection.py
--rw-rw-rw-   0        0        0    16810 2023-04-05 12:41:37.000000 pyGuardPoint-0.7.1/pyGuardPoint/guardpoint_dataclasses.py
--rw-rw-rw-   0        0        0       49 2023-03-21 15:31:43.000000 pyGuardPoint-0.7.1/pyGuardPoint/guardpoint_error.py
--rw-rw-rw-   0        0        0     2885 2023-04-03 15:08:05.000000 pyGuardPoint-0.7.1/pyGuardPoint/guardpoint_utils.py
-drwxrwxrwx   0        0        0        0 2023-04-05 13:20:15.264933 pyGuardPoint-0.7.1/pyGuardPoint.egg-info/
--rw-rw-rw-   0        0        0      199 2023-04-05 13:20:15.000000 pyGuardPoint-0.7.1/pyGuardPoint.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      806 2023-04-05 13:20:15.000000 pyGuardPoint-0.7.1/pyGuardPoint.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-05 13:20:15.000000 pyGuardPoint-0.7.1/pyGuardPoint.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2022-09-30 14:14:07.000000 pyGuardPoint-0.7.1/pyGuardPoint.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0       34 2023-04-05 13:20:15.000000 pyGuardPoint-0.7.1/pyGuardPoint.egg-info/requires.txt
--rw-rw-rw-   0        0        0       13 2023-04-05 13:20:15.000000 pyGuardPoint-0.7.1/pyGuardPoint.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-05 13:20:15.266958 pyGuardPoint-0.7.1/setup.cfg
--rw-rw-rw-   0        0        0      382 2023-04-05 13:19:52.000000 pyGuardPoint-0.7.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 11:06:38.092190 pyGuardPoint-0.7.2/
+-rw-rw-rw-   0        0        0    11558 2022-09-27 13:07:38.000000 pyGuardPoint-0.7.2/LICENSE.txt
+-rw-rw-rw-   0        0        0      199 2023-04-06 11:06:38.091190 pyGuardPoint-0.7.2/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-06 11:06:38.078181 pyGuardPoint-0.7.2/pyGuardPoint/
+-rw-rw-rw-   0        0        0      250 2023-03-30 08:56:57.000000 pyGuardPoint-0.7.2/pyGuardPoint/__init__.py
+-rw-rw-rw-   0        0        0      997 2023-03-03 10:58:18.000000 pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_areas.py
+-rw-rw-rw-   0        0        0    11137 2023-04-05 12:23:31.000000 pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_cardholders.py
+-rw-rw-rw-   0        0        0     6687 2023-04-05 13:08:15.000000 pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_cards.py
+-rw-rw-rw-   0        0        0     1170 2023-03-16 16:56:01.000000 pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_customizedfields.py
+-rw-rw-rw-   0        0        0     1175 2023-03-16 16:56:01.000000 pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_personaldetails.py
+-rw-rw-rw-   0        0        0     2462 2023-03-17 15:44:40.000000 pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_scheduledmags.py
+-rw-rw-rw-   0        0        0     1314 2023-03-17 12:07:11.000000 pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_securitygroups.py
+-rw-rw-rw-   0        0        0     4902 2023-04-05 10:42:09.000000 pyGuardPoint-0.7.2/pyGuardPoint/_odata_filter.py
+-rw-rw-rw-   0        0        0     1636 2023-03-31 09:30:04.000000 pyGuardPoint-0.7.2/pyGuardPoint/_str_match_algo.py
+-rw-rw-rw-   0        0        0     2393 2023-04-03 15:05:33.000000 pyGuardPoint-0.7.2/pyGuardPoint/guardpoint.py
+-rw-rw-rw-   0        0        0     4058 2023-04-05 09:36:31.000000 pyGuardPoint-0.7.2/pyGuardPoint/guardpoint_async.py
+-rw-rw-rw-   0        0        0     5799 2023-04-05 10:41:13.000000 pyGuardPoint-0.7.2/pyGuardPoint/guardpoint_connection.py
+-rw-rw-rw-   0        0        0    16977 2023-04-06 11:06:08.000000 pyGuardPoint-0.7.2/pyGuardPoint/guardpoint_dataclasses.py
+-rw-rw-rw-   0        0        0       49 2023-03-21 15:31:43.000000 pyGuardPoint-0.7.2/pyGuardPoint/guardpoint_error.py
+-rw-rw-rw-   0        0        0     2885 2023-04-03 15:08:05.000000 pyGuardPoint-0.7.2/pyGuardPoint/guardpoint_utils.py
+drwxrwxrwx   0        0        0        0 2023-04-06 11:06:38.090187 pyGuardPoint-0.7.2/pyGuardPoint.egg-info/
+-rw-rw-rw-   0        0        0      199 2023-04-06 11:06:37.000000 pyGuardPoint-0.7.2/pyGuardPoint.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      806 2023-04-06 11:06:37.000000 pyGuardPoint-0.7.2/pyGuardPoint.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 11:06:37.000000 pyGuardPoint-0.7.2/pyGuardPoint.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2022-09-30 14:14:07.000000 pyGuardPoint-0.7.2/pyGuardPoint.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0       34 2023-04-06 11:06:37.000000 pyGuardPoint-0.7.2/pyGuardPoint.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       13 2023-04-06 11:06:37.000000 pyGuardPoint-0.7.2/pyGuardPoint.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 11:06:38.092190 pyGuardPoint-0.7.2/setup.cfg
+-rw-rw-rw-   0        0        0      382 2023-04-06 11:06:18.000000 pyGuardPoint-0.7.2/setup.py
```

### Comparing `pyGuardPoint-0.7.1/LICENSE.txt` & `pyGuardPoint-0.7.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_areas.py` & `pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_areas.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_cardholders.py` & `pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_cardholders.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_cards.py` & `pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_cards.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_customizedfields.py` & `pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_customizedfields.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_personaldetails.py` & `pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_personaldetails.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_scheduledmags.py` & `pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_scheduledmags.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/_guardpoint_securitygroups.py` & `pyGuardPoint-0.7.2/pyGuardPoint/_guardpoint_securitygroups.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/_odata_filter.py` & `pyGuardPoint-0.7.2/pyGuardPoint/_odata_filter.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/_str_match_algo.py` & `pyGuardPoint-0.7.2/pyGuardPoint/_str_match_algo.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/guardpoint.py` & `pyGuardPoint-0.7.2/pyGuardPoint/guardpoint.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/guardpoint_async.py` & `pyGuardPoint-0.7.2/pyGuardPoint/guardpoint_async.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/guardpoint_connection.py` & `pyGuardPoint-0.7.2/pyGuardPoint/guardpoint_connection.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/guardpoint_dataclasses.py` & `pyGuardPoint-0.7.2/pyGuardPoint/guardpoint_dataclasses.py`

 * *Files 1% similar despite different names*

```diff
@@ -393,15 +393,14 @@
                 setattr(self, property_name, cardholder_dict[property_name])
 
         # Monitor Changes
         for k, v in asdict(self).items():
             if isinstance(v, (str, type(None), bool, int)):
                 self.add_observer(k)
 
-
     def to_search_pattern(self):
         pattern = ""
         if self.firstName:
             pattern += self.firstName + " "
         if self.lastName:
             pattern += self.lastName + " "
         if self.cardholderPersonalDetail:
@@ -422,23 +421,27 @@
                     print(f"\t{str(attribute)}")
                 elif hasattr(attribute, '__dict__'):
                     print(f"{attribute_name}:")
                     obj.pretty_print(attribute)
                 else:
                     print(f"\t{attribute_name:<25}" + str(attribute))
 
-    def dict(self, editable_only=False, changed_only=False):
+    def dict(self, editable_only=False, changed_only=False, non_empty_only=False):
         ch = dict()
         for k, v in asdict(self).items():
             if isinstance(v, (list, dict, bool, int)):
                 ch[k] = v
             elif isinstance(v, type(None)):
-                ch[k] = None
+                if not non_empty_only:
+                    ch[k] = None
             elif isinstance(v, str):
-                if len(v) > 0:
+                if non_empty_only:
+                    if len(v) > 0:
+                        ch[k] = str(v)
+                else:
                     ch[k] = str(v)
             else:
                 pass
 
         if editable_only:
             ch = self._remove_non_editable(ch)
```

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint/guardpoint_utils.py` & `pyGuardPoint-0.7.2/pyGuardPoint/guardpoint_utils.py`

 * *Files identical despite different names*

### Comparing `pyGuardPoint-0.7.1/pyGuardPoint.egg-info/SOURCES.txt` & `pyGuardPoint-0.7.2/pyGuardPoint.egg-info/SOURCES.txt`

 * *Files identical despite different names*

