# Comparing `tmp/appian-locust-1.8.2.tar.gz` & `tmp/appian-locust-1.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/appian-locust-1.8.2.tar", last modified: Fri Feb 12 14:30:26 2021, max compression
+gzip compressed data, was "dist/appian-locust-1.9.0.tar", last modified: Mon Feb 15 20:42:47 2021, max compression
```

## Comparing `appian-locust-1.8.2.tar` & `appian-locust-1.9.0.tar`

### file list

```diff
@@ -1,36 +1,37 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-02-12 14:30:26.000000 appian-locust-1.8.2/
--rw-r--r--   0 root         (0) root         (0)     5955 2021-02-12 14:30:26.000000 appian-locust-1.8.2/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     4454 2021-02-12 14:30:15.000000 appian-locust-1.8.2/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-02-12 14:30:26.000000 appian-locust-1.8.2/appian_locust/
--rw-rw-rw-   0 root         (0) root         (0)      332 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     8478 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_actions.py
--rw-rw-rw-   0 root         (0) root         (0)      892 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_admin.py
--rw-rw-rw-   0 root         (0) root         (0)     2786 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_app_importer.py
--rw-rw-rw-   0 root         (0) root         (0)     2401 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_base.py
--rw-rw-rw-   0 root         (0) root         (0)     4022 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_design.py
--rw-rw-rw-   0 root         (0) root         (0)     1792 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_feature_flag.py
--rw-rw-rw-   0 root         (0) root         (0)     5462 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_feature_toggle_helper.py
--rw-rw-rw-   0 root         (0) root         (0)     5945 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_grid_interactor.py
--rw-rw-rw-   0 root         (0) root         (0)    41805 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_interactor.py
--rw-rw-rw-   0 root         (0) root         (0)     7434 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_news.py
--rw-rw-rw-   0 root         (0) root         (0)    18060 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_records.py
--rw-rw-rw-   0 root         (0) root         (0)     5893 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_reports.py
--rw-rw-rw-   0 root         (0) root         (0)     2824 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_save_request_builder.py
--rw-rw-rw-   0 root         (0) root         (0)    11866 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_sites.py
--rw-rw-rw-   0 root         (0) root         (0)     7921 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_tasks.py
--rw-rw-rw-   0 root         (0) root         (0)     2365 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/_ui_reconciler.py
--rw-rw-rw-   0 root         (0) root         (0)    14651 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/appianclient.py
--rw-rw-rw-   0 root         (0) root         (0)      669 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/exceptions.py
--rw-rw-rw-   0 root         (0) root         (0)    12212 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/helper.py
--rwxrwxrwx   0 root         (0) root         (0)     1143 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/loadDriverUtils.py
--rw-rw-rw-   0 root         (0) root         (0)      824 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/logger.py
--rw-rw-rw-   0 root         (0) root         (0)     3771 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/records_helper.py
--rw-rw-rw-   0 root         (0) root         (0)    55996 2021-02-12 14:30:15.000000 appian-locust-1.8.2/appian_locust/uiform.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-02-12 14:30:26.000000 appian-locust-1.8.2/appian_locust.egg-info/
--rw-r--r--   0 root         (0) root         (0)     5955 2021-02-12 14:30:26.000000 appian-locust-1.8.2/appian_locust.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      891 2021-02-12 14:30:26.000000 appian-locust-1.8.2/appian_locust.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2021-02-12 14:30:26.000000 appian-locust-1.8.2/appian_locust.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       14 2021-02-12 14:30:26.000000 appian-locust-1.8.2/appian_locust.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       14 2021-02-12 14:30:26.000000 appian-locust-1.8.2/appian_locust.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)      627 2021-02-12 14:30:26.000000 appian-locust-1.8.2/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)     1085 2021-02-12 14:30:15.000000 appian-locust-1.8.2/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-02-15 20:42:47.000000 appian-locust-1.9.0/
+-rw-r--r--   0 root         (0) root         (0)     5955 2021-02-15 20:42:47.000000 appian-locust-1.9.0/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     4454 2021-02-15 20:42:37.000000 appian-locust-1.9.0/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-02-15 20:42:47.000000 appian-locust-1.9.0/appian_locust/
+-rw-rw-rw-   0 root         (0) root         (0)      332 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     8478 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_actions.py
+-rw-rw-rw-   0 root         (0) root         (0)      892 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_admin.py
+-rw-rw-rw-   0 root         (0) root         (0)     2786 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_app_importer.py
+-rw-rw-rw-   0 root         (0) root         (0)     2401 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_base.py
+-rw-rw-rw-   0 root         (0) root         (0)     4022 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_design.py
+-rw-rw-rw-   0 root         (0) root         (0)     1792 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_feature_flag.py
+-rw-rw-rw-   0 root         (0) root         (0)     5462 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_feature_toggle_helper.py
+-rw-rw-rw-   0 root         (0) root         (0)     5945 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_grid_interactor.py
+-rw-rw-rw-   0 root         (0) root         (0)    41805 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_interactor.py
+-rw-rw-rw-   0 root         (0) root         (0)     7434 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_news.py
+-rw-rw-rw-   0 root         (0) root         (0)    18060 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_records.py
+-rw-rw-rw-   0 root         (0) root         (0)     5893 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_reports.py
+-rw-rw-rw-   0 root         (0) root         (0)     2824 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_save_request_builder.py
+-rw-rw-rw-   0 root         (0) root         (0)    11866 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_sites.py
+-rw-rw-rw-   0 root         (0) root         (0)     4193 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_task_opener.py
+-rw-rw-rw-   0 root         (0) root         (0)     5748 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_tasks.py
+-rw-rw-rw-   0 root         (0) root         (0)     2365 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/_ui_reconciler.py
+-rw-rw-rw-   0 root         (0) root         (0)    14651 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/appianclient.py
+-rw-rw-rw-   0 root         (0) root         (0)      669 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/exceptions.py
+-rw-rw-rw-   0 root         (0) root         (0)    12212 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/helper.py
+-rwxrwxrwx   0 root         (0) root         (0)     1143 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/loadDriverUtils.py
+-rw-rw-rw-   0 root         (0) root         (0)      824 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/logger.py
+-rw-rw-rw-   0 root         (0) root         (0)     3771 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/records_helper.py
+-rw-rw-rw-   0 root         (0) root         (0)    60967 2021-02-15 20:42:37.000000 appian-locust-1.9.0/appian_locust/uiform.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-02-15 20:42:47.000000 appian-locust-1.9.0/appian_locust.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     5955 2021-02-15 20:42:47.000000 appian-locust-1.9.0/appian_locust.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      921 2021-02-15 20:42:47.000000 appian-locust-1.9.0/appian_locust.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2021-02-15 20:42:47.000000 appian-locust-1.9.0/appian_locust.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       14 2021-02-15 20:42:47.000000 appian-locust-1.9.0/appian_locust.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       14 2021-02-15 20:42:47.000000 appian-locust-1.9.0/appian_locust.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)      627 2021-02-15 20:42:47.000000 appian-locust-1.9.0/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)     1085 2021-02-15 20:42:37.000000 appian-locust-1.9.0/setup.py
```

### Comparing `appian-locust-1.8.2/PKG-INFO` & `appian-locust-1.9.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: appian-locust
-Version: 1.8.2
+Version: 1.9.0
 Summary: Tools and functions to make testing Appian with Locust easier
 Home-page: https://gitlab.com/appian-oss/appian-locust
 Author: Appian Performance & Reliability Engineering Squad
 License: Apache 2.0
 Description: .. what_is_appian_locust-inclusion-begin-do-not-remove
         
         #######################################
```

### Comparing `appian-locust-1.8.2/README.rst` & `appian-locust-1.9.0/README.rst`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_actions.py` & `appian-locust-1.9.0/appian_locust/_actions.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_admin.py` & `appian-locust-1.9.0/appian_locust/_admin.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_app_importer.py` & `appian-locust-1.9.0/appian_locust/_app_importer.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_base.py` & `appian-locust-1.9.0/appian_locust/_base.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_design.py` & `appian-locust-1.9.0/appian_locust/_design.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_feature_flag.py` & `appian-locust-1.9.0/appian_locust/_feature_flag.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_feature_toggle_helper.py` & `appian-locust-1.9.0/appian_locust/_feature_toggle_helper.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_grid_interactor.py` & `appian-locust-1.9.0/appian_locust/_grid_interactor.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_interactor.py` & `appian-locust-1.9.0/appian_locust/_interactor.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_news.py` & `appian-locust-1.9.0/appian_locust/_news.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_records.py` & `appian-locust-1.9.0/appian_locust/_records.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_reports.py` & `appian-locust-1.9.0/appian_locust/_reports.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_save_request_builder.py` & `appian-locust-1.9.0/appian_locust/_save_request_builder.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_sites.py` & `appian-locust-1.9.0/appian_locust/_sites.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/_ui_reconciler.py` & `appian-locust-1.9.0/appian_locust/_ui_reconciler.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/appianclient.py` & `appian-locust-1.9.0/appian_locust/appianclient.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/exceptions.py` & `appian-locust-1.9.0/appian_locust/exceptions.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/helper.py` & `appian-locust-1.9.0/appian_locust/helper.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/loadDriverUtils.py` & `appian-locust-1.9.0/appian_locust/loadDriverUtils.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/logger.py` & `appian-locust-1.9.0/appian_locust/logger.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/records_helper.py` & `appian-locust-1.9.0/appian_locust/records_helper.py`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/appian_locust/uiform.py` & `appian-locust-1.9.0/appian_locust/uiform.py`

 * *Files 3% similar despite different names*

```diff
@@ -10,23 +10,26 @@
 from urllib.parse import quote, urlparse
 
 from appian_locust.records_helper import _is_grid
 
 from . import logger
 from ._grid_interactor import GridInteractor
 from ._interactor import _Interactor
+from ._task_opener import _TaskOpener
 from ._ui_reconciler import UiReconciler
 from .helper import (extract_all_by_label, find_component_by_attribute_in_dict,
                      find_component_by_index_in_dict,
                      find_component_by_label_and_type_dict, log_locust_error)
 from .records_helper import (get_record_header_response,
                              get_record_summary_view_response)
 
 KEY_UUID = "uuid"
 KEY_CONTEXT = "context"
+START_PROCESS_LINK_TYPE = 'StartProcessLink'
+PROCESS_TASK_LINK_TYPE = 'ProcessTaskLink'
 COMPONENTS_THAT_CAN_BE_FILLED = ["ParagraphField", "TextField"]
 
 log = logger.getLogger(__name__)
 
 
 class ClientMode(enum.Enum):
     TEMPO = 'TEMPO'
@@ -56,14 +59,15 @@
             state: JSON representation of the initial form
             latest_state: JSON representation of the last to the the form
             url: Url to make updates to the form
             breadcrumbs: Path used to create locust labels
 
         """
         self.interactor: _Interactor = interactor
+        self.task_opener: _TaskOpener = _TaskOpener(self.interactor)
         self.state: Dict[str, Any] = state
         self.form_url = url
         if any(key not in self.state for key in (KEY_CONTEXT, KEY_UUID)):
             return None
         self.context: dict = self.state[KEY_CONTEXT]
         self.uuid: str = self.state[KEY_UUID]
         self.grid_interactor: GridInteractor = GridInteractor()
@@ -300,14 +304,18 @@
 
     @raises_locust_error("uiform.py/click()")
     def click(self, label: str, is_test_label: bool = False, locust_request_label: str = "") -> 'SailUiForm':
         """
         Clicks on a component on the form, if there is one present with the following label (case sensitive)
         Otherwise throws a NotFoundException
 
+        Can also be called as 'click_link' or 'click_button' to convey intent
+
+        This can also click StartProcessLinks or ProcessTaskLinks
+
         Args:
             label(str): Label of the component to click
             is_test_label(bool): If you are clicking a button or link via a test label instead of a label, set this boolean to true
 
         Keyword Args:
             locust_request_label(str): Label used to identify the request for locust statistics
 
@@ -315,32 +323,86 @@
 
         Examples:
 
             >>> form.click('Submit')
             >>> form.click('SampleTestLabel', is_test_label = True)
 
         """
+        locust_label = locust_request_label or f"{self.breadcrumb}.Click.{label}"
+        return self._click(label, is_test_label=is_test_label, locust_request_label=locust_label)
+
+    @raises_locust_error("uiform.py/click_button()")
+    def click_button(self, label: str, is_test_label: bool = False, locust_request_label: str = "") -> 'SailUiForm':
+        """
+        Clicks on a component on the form, if there is one present with the following label (case sensitive)
+        Otherwise throws a NotFoundException
+
+        This can also click StartProcessLinks or ProcessTaskLinks
+
+        Args:
+            label(str): Label of the component to click
+            is_test_label(bool): If you are clicking a button via a test label instead of a label, set this boolean to true
+
+        Keyword Args:
+            locust_request_label(str): Label used to identify the request for locust statistics
+
+        Returns (SailUiForm): The latest state of the UiForm
+
+        Examples:
+
+            >>> form.click_button('Save')
+            >>> form.click_link('Update')
+
+        """
+        locust_label = locust_request_label or f"{self.breadcrumb}.ClickButton.{label}"
+        return self._click(label, is_test_label=is_test_label, locust_request_label=locust_label)
+
+    @raises_locust_error("uiform.py/click_link()")
+    def click_link(self, label: str, is_test_label: bool = False, locust_request_label: str = "") -> 'SailUiForm':
+        """
+        Clicks on a component on the form, if there is one present with the following label (case sensitive)
+        Otherwise throws a NotFoundException
+
+        This can also click StartProcessLinks or ProcessTaskLinks
+
+        Args:
+            label(str): Label of the component to click
+            is_test_label(bool): If you are clicking a link via a test label instead of a label, set this boolean to true
+
+        Keyword Args:
+            locust_request_label(str): Label used to identify the request for locust statistics
+
+        Returns (SailUiForm): The latest state of the UiForm
+
+        Examples:
+
+            >>> form.click_link('Update')
+
+        """
+        locust_label = locust_request_label or f"{self.breadcrumb}.ClickLink.{label}"
+        return self._click(label, is_test_label=is_test_label, locust_request_label=locust_label)
+
+    def _click(self, label: str, is_test_label: bool = False, locust_request_label: str = "") -> 'SailUiForm':
+        """
+        Internal function wrapped by various click methods
+        """
         attribute_to_find = 'testLabel' if is_test_label else 'label'
-        component = find_component_by_attribute_in_dict(
-            attribute_to_find, label, self.state)
+
+        component = find_component_by_attribute_in_dict(attribute_to_find, label, self.state)
+
         self._validate_component_found(component, label)
 
         locust_label = locust_request_label or f"{self.breadcrumb}.Click.{label}"
         reeval_url = self._get_update_url_for_reeval(self.state)
-        new_state = self.interactor.click_component(
-            reeval_url, component, self.context, self.uuid, label=locust_label)
+        new_state = self._dispatch_click(component=component, locust_label=locust_label)
 
         if not new_state:
             raise Exception(f"No response returned when trying to click button with label '{label}'")
         return self._reconcile_state(new_state, form_url=reeval_url)
 
-    # Aliases for click() function
-    click_button = click
-    click_link = click
-
     @raises_locust_error("uiform.py/click_card_layout_by_index()")
     def click_card_layout_by_index(self, index: int, locust_request_label: str = "") -> 'SailUiForm':
         """
         Clicks a card layout link by index.
         This method will find the CardLayout component on the UI by index and then perform
         the click behavior on its Link component.
 
@@ -358,21 +420,19 @@
             no need to call click_start_process_link() when it is on a CardLayout.
 
             >>> form.click_card_layout_by_index(2)
 
         """
         component = find_component_by_index_in_dict("CardLayout", index, self.state)
 
-        if "link" in component and component["link"]:
-            link_component = component["link"]
-        else:
+        if not component.get("link"):
             raise Exception(f"CardLayout found at index: {index} does not have a link on it")
 
+        link_component = component.get('link')
         locust_label = locust_request_label or f"{self.breadcrumb}.ClickCardLayout.Index.{index}"
-
         if link_component["#t"] == "StartProcessLink":
             site_name = link_component["siteUrlStub"] or "D6JMim"
             page_name = link_component["sitePageUrlStub"]
             new_state = self._click_start_process_link(site_name, page_name, False, link_component, locust_request_label=locust_label)
         else:
             new_state = self.interactor.click_component(self.form_url, link_component, self.context, self.uuid, label=locust_label)
 
@@ -424,15 +484,15 @@
         Returns (SailUiForm): The latest state of the UiForm
 
         Examples:
             >>> form.click_start_process_link('Request upgrade')
 
         """
 
-        component = find_component_by_label_and_type_dict('label', label, 'StartProcessLink', self.state)
+        component = find_component_by_label_and_type_dict('label', label, START_PROCESS_LINK_TYPE, self.state)
         self._validate_component_found(component, label)
 
         locust_label = locust_request_label or f"{self.breadcrumb}.ClickStartProcessLink.{label}"
         new_state = self._click_start_process_link(site_name, page_name, is_mobile, component, locust_request_label=locust_label)
 
         # get the re-eval URI from links object of the response (new_state)
         reeval_url = self._get_update_url_for_reeval(new_state)
@@ -475,14 +535,57 @@
         elif not cache_key:
             raise Exception(f"StartProcessLink component does not have cache key set.")
 
         return self.interactor.click_start_process_link(component=component, process_model_opaque_id=process_model_opaque_id,
                                                         cache_key=cache_key, site_name=site_name, page_name=page_name, is_mobile=is_mobile,
                                                         locust_request_label=locust_request_label)
 
+    def _dispatch_click(self, component: Dict[str, Any], locust_label: str) -> Dict[str, Any]:
+        """
+        Dispatches the appropriate link interaction based on the link type if appropriate
+
+        Args:
+            link_component (Dict[str, Any]): Link component to interact with
+            locust_label (str): Label used to identify the request for locust statistics
+
+        Returns:
+            Dict[str, Any]: State returned by the interaction
+        """
+        component_type = component.get('#t')
+        # Check if component is already a supported link
+        if component_type in [START_PROCESS_LINK_TYPE, PROCESS_TASK_LINK_TYPE]:
+            link_component = component
+            link_type = component_type
+        else:
+            link_component = component.get('link', {})
+            link_type = link_component.get('#t')
+
+        if link_type == START_PROCESS_LINK_TYPE:
+            site_name = link_component["siteUrlStub"] or "D6JMim"
+            page_name = link_component["sitePageUrlStub"]
+            new_state = self._click_start_process_link(site_name, page_name, False, link_component, locust_request_label=locust_label)
+        elif link_type == PROCESS_TASK_LINK_TYPE:
+            task_name = link_component.get('label') or 'Unnammed Task'
+            task_id = link_component.get('opaqueTaskId')
+            if not task_id:
+                raise Exception(f"No task id found for task with name '{task_name}'")
+            site_name = link_component.get("siteUrlStub") or "D6JMim"
+            page_name = link_component.get("sitePageUrlStub")
+            headers = {
+                'X-Site-UrlStub': site_name,
+                'X-Page-UrlStub': page_name,
+                'X-Client-Mode': 'SITES'
+            }
+            new_state = self.task_opener.visit_by_task_id(task_name, task_id, extra_headers=headers)
+        elif link_component:
+            new_state = self.interactor.click_component(self.form_url, link_component, self.context, self.uuid, label=locust_label)
+        else:
+            new_state = self.interactor.click_component(self.form_url, component, self.context, self.uuid, label=locust_label)
+        return new_state
+
     @raises_locust_error("uiform.py/click_related_action_link()")
     def click_related_action(self, label: str, locust_request_label: str = "") -> 'SailUiForm':
         """
         Clicks a related action (either a related action button or link) on the form by label
         If no link is found, throws a ComponentNotFoundException
 
         Args:
@@ -1166,14 +1269,16 @@
             raise Exception(f"At least one validation was found in the form {self.breadcrumb}")
         return self
 
     def _reconcile_state(self, new_state: dict, form_url: str = "") -> 'SailUiForm':
         self.interactor.datatype_cache.cache(new_state)
         self.state = self.reconciler.reconcile_ui(self.state, new_state)
         self.form_url = form_url or self.form_url
+        self.uuid = self.state.get(KEY_UUID) or self.uuid
+        self.context = self.state.get(KEY_CONTEXT) or self.context
         return self
 
     def _validate_component_found(self, component: Optional[Dict[str, Any]], label: str, type: Optional[str] = None) -> None:
         if not component:
             optional_type_info = f" of type '{type}'" if type else ''
             msg = f"Could not find the component with label '{label}'{optional_type_info} in the provided form"
             raise ComponentNotFoundException(msg)
```

### Comparing `appian-locust-1.8.2/appian_locust.egg-info/PKG-INFO` & `appian-locust-1.9.0/appian_locust.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: appian-locust
-Version: 1.8.2
+Version: 1.9.0
 Summary: Tools and functions to make testing Appian with Locust easier
 Home-page: https://gitlab.com/appian-oss/appian-locust
 Author: Appian Performance & Reliability Engineering Squad
 License: Apache 2.0
 Description: .. what_is_appian_locust-inclusion-begin-do-not-remove
         
         #######################################
```

### Comparing `appian-locust-1.8.2/appian_locust.egg-info/SOURCES.txt` & `appian-locust-1.9.0/appian_locust.egg-info/SOURCES.txt`

 * *Files 5% similar despite different names*

```diff
@@ -12,14 +12,15 @@
 appian_locust/_grid_interactor.py
 appian_locust/_interactor.py
 appian_locust/_news.py
 appian_locust/_records.py
 appian_locust/_reports.py
 appian_locust/_save_request_builder.py
 appian_locust/_sites.py
+appian_locust/_task_opener.py
 appian_locust/_tasks.py
 appian_locust/_ui_reconciler.py
 appian_locust/appianclient.py
 appian_locust/exceptions.py
 appian_locust/helper.py
 appian_locust/loadDriverUtils.py
 appian_locust/logger.py
```

### Comparing `appian-locust-1.8.2/setup.cfg` & `appian-locust-1.9.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `appian-locust-1.8.2/setup.py` & `appian-locust-1.9.0/setup.py`

 * *Files identical despite different names*

