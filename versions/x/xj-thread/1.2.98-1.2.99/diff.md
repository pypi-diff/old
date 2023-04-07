# Comparing `tmp/xj_thread-1.2.98.tar.gz` & `tmp/xj_thread-1.2.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\xj_thread-1.2.98.tar", last modified: Wed Mar 29 10:20:20 2023, max compression
+gzip compressed data, was "dist\xj_thread-1.2.99.tar", last modified: Wed Mar 29 10:52:02 2023, max compression
```

## Comparing `xj_thread-1.2.98.tar` & `xj_thread-1.2.99.tar`

### file list

```diff
@@ -1,61 +1,61 @@
-drwxrwxrwx   0        0        0        0 2023-03-29 10:20:20.000000 xj_thread-1.2.98/
--rw-rw-rw-   0        0        0    24709 2023-03-29 10:20:20.000000 xj_thread-1.2.98/PKG-INFO
--rw-rw-rw-   0        0        0    21225 2022-08-03 08:57:06.000000 xj_thread-1.2.98/README.md
--rw-rw-rw-   0        0        0       42 2023-03-29 10:20:20.000000 xj_thread-1.2.98/setup.cfg
--rw-rw-rw-   0        0        0     1942 2023-03-29 10:20:01.000000 xj_thread-1.2.98/setup.py
-drwxrwxrwx   0        0        0        0 2023-03-29 10:20:19.000000 xj_thread-1.2.98/xj_thread/
--rw-rw-rw-   0        0        0        0 2022-08-23 09:09:46.000000 xj_thread-1.2.98/xj_thread/__init__.py
--rw-rw-rw-   0        0        0     6764 2023-03-07 02:17:28.000000 xj_thread-1.2.98/xj_thread/admin.py
-drwxrwxrwx   0        0        0        0 2023-03-29 10:20:19.000000 xj_thread-1.2.98/xj_thread/apis/
--rw-rw-rw-   0        0        0      134 2022-08-03 09:04:37.000000 xj_thread-1.2.98/xj_thread/apis/__init__.py
--rw-rw-rw-   0        0        0     1341 2022-10-27 08:44:15.000000 xj_thread-1.2.98/xj_thread/apis/thread_add.py
--rw-rw-rw-   0        0        0     2130 2023-03-28 07:47:36.000000 xj_thread-1.2.98/xj_thread/apis/thread_category_apis.py
--rw-rw-rw-   0        0        0     1943 2023-02-14 02:04:01.000000 xj_thread-1.2.98/xj_thread/apis/thread_category_tree.py
--rw-rw-rw-   0        0        0     2241 2023-03-28 08:00:45.000000 xj_thread-1.2.98/xj_thread/apis/thread_classify_apis.py
--rw-rw-rw-   0        0        0     1497 2022-10-27 08:45:06.000000 xj_thread-1.2.98/xj_thread/apis/thread_classify_tree.py
--rw-rw-rw-   0        0        0     2012 2022-11-09 08:58:16.000000 xj_thread-1.2.98/xj_thread/apis/thread_item.py
--rw-rw-rw-   0        0        0     4387 2023-03-29 10:17:13.000000 xj_thread-1.2.98/xj_thread/apis/thread_list.py
--rw-rw-rw-   0        0        0     7243 2023-03-07 01:49:05.000000 xj_thread-1.2.98/xj_thread/apis/thread_list[del ].py
--rw-rw-rw-   0        0        0     2649 2023-03-16 09:15:12.000000 xj_thread-1.2.98/xj_thread/apis/thread_other_list.py
--rw-rw-rw-   0        0        0     1755 2022-10-27 08:45:57.000000 xj_thread-1.2.98/xj_thread/apis/thread_statistic.py
--rw-rw-rw-   0        0        0      206 2022-09-06 01:51:47.000000 xj_thread-1.2.98/xj_thread/apps.py
--rw-rw-rw-   0        0        0      367 2022-06-04 04:47:05.000000 xj_thread-1.2.98/xj_thread/forms.py
--rw-rw-rw-   0        0        0    29726 2023-03-29 08:11:05.000000 xj_thread-1.2.98/xj_thread/models.py
--rw-rw-rw-   0        0        0     9810 2023-03-07 07:59:19.000000 xj_thread-1.2.98/xj_thread/serializers.py
-drwxrwxrwx   0        0        0        0 2023-03-29 10:20:20.000000 xj_thread-1.2.98/xj_thread/services/
--rw-rw-rw-   0        0        0      134 2022-08-03 09:04:22.000000 xj_thread-1.2.98/xj_thread/services/__init__.py
--rw-rw-rw-   0        0        0     5478 2023-03-29 03:28:57.000000 xj_thread-1.2.98/xj_thread/services/thread_category_service.py
--rw-rw-rw-   0        0        0     3324 2022-10-08 03:32:47.000000 xj_thread-1.2.98/xj_thread/services/thread_category_tree_service [backup].py
--rw-rw-rw-   0        0        0     3956 2023-03-29 10:18:29.000000 xj_thread-1.2.98/xj_thread/services/thread_category_tree_service.py
--rw-rw-rw-   0        0        0     5471 2023-03-28 08:01:26.000000 xj_thread-1.2.98/xj_thread/services/thread_classify_service.py
--rw-rw-rw-   0        0        0     2807 2022-12-31 09:12:26.000000 xj_thread-1.2.98/xj_thread/services/thread_classify_tree_service.py
--rw-rw-rw-   0        0        0     6311 2023-03-07 09:12:49.000000 xj_thread-1.2.98/xj_thread/services/thread_extend_service.py
--rw-rw-rw-   0        0        0     6120 2023-03-07 09:15:33.000000 xj_thread-1.2.98/xj_thread/services/thread_item_service.py
--rw-rw-rw-   0        0        0     9761 2023-03-29 08:11:58.000000 xj_thread-1.2.98/xj_thread/services/thread_list_service.py
--rw-rw-rw-   0        0        0     6497 2023-03-16 09:13:45.000000 xj_thread-1.2.98/xj_thread/services/thread_other_list_service.py
--rw-rw-rw-   0        0        0     2423 2023-03-14 07:10:59.000000 xj_thread-1.2.98/xj_thread/services/thread_statistic_service.py
--rw-rw-rw-   0        0        0     3025 2023-03-28 07:54:45.000000 xj_thread-1.2.98/xj_thread/urls.py
-drwxrwxrwx   0        0        0        0 2023-03-29 10:20:20.000000 xj_thread-1.2.98/xj_thread/utils/
--rw-rw-rw-   0        0        0      134 2022-08-03 09:04:51.000000 xj_thread-1.2.98/xj_thread/utils/__init__.py
--rw-rw-rw-   0        0        0      635 2022-08-02 02:23:40.000000 xj_thread-1.2.98/xj_thread/utils/custom_authentication_wrapper.py
--rw-rw-rw-   0        0        0     1524 2022-08-02 07:03:31.000000 xj_thread-1.2.98/xj_thread/utils/custom_authorization.py
--rw-rw-rw-   0        0        0     1551 2022-04-22 01:16:10.000000 xj_thread-1.2.98/xj_thread/utils/custom_exception.py
--rw-rw-rw-   0        0        0      881 2022-04-22 01:16:10.000000 xj_thread-1.2.98/xj_thread/utils/custom_pagination.py
--rw-rw-rw-   0        0        0     1749 2023-03-07 06:35:37.000000 xj_thread-1.2.98/xj_thread/utils/custom_response.py
--rw-rw-rw-   0        0        0    18541 2023-03-20 01:56:43.000000 xj_thread-1.2.98/xj_thread/utils/custom_tool.py
--rw-rw-rw-   0        0        0      429 2022-08-27 10:02:03.000000 xj_thread-1.2.98/xj_thread/utils/j_dict.py
--rw-rw-rw-   0        0        0     7614 2023-03-29 10:15:38.000000 xj_thread-1.2.98/xj_thread/utils/j_recur.py
--rw-rw-rw-   0        0        0      769 2022-10-08 03:32:47.000000 xj_thread-1.2.98/xj_thread/utils/j_type.py
--rw-rw-rw-   0        0        0      660 2022-09-07 09:11:23.000000 xj_thread-1.2.98/xj_thread/utils/join_list.py
--rw-rw-rw-   0        0        0     4194 2023-02-14 01:48:07.000000 xj_thread-1.2.98/xj_thread/utils/user_wrapper.py
--rw-rw-rw-   0        0        0     3885 2022-06-20 06:19:26.000000 xj_thread-1.2.98/xj_thread/utils/util.py
--rw-rw-rw-   0        0        0     2682 2022-07-29 14:44:11.000000 xj_thread-1.2.98/xj_thread/utils/validator.py
--rw-rw-rw-   0        0        0      789 2022-09-07 09:21:20.000000 xj_thread-1.2.98/xj_thread/utils/x_get_params.py
--rw-rw-rw-   0        0        0     1606 2022-10-25 09:22:04.000000 xj_thread-1.2.98/xj_thread/validator.py
--rw-rw-rw-   0        0        0     6699 2022-07-31 11:32:37.000000 xj_thread-1.2.98/xj_thread/views.py
-drwxrwxrwx   0        0        0        0 2023-03-29 10:20:19.000000 xj_thread-1.2.98/xj_thread.egg-info/
--rw-rw-rw-   0        0        0    24709 2023-03-29 10:20:19.000000 xj_thread-1.2.98/xj_thread.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     1733 2023-03-29 10:20:19.000000 xj_thread-1.2.98/xj_thread.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-29 10:20:19.000000 xj_thread-1.2.98/xj_thread.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       16 2023-03-29 10:20:19.000000 xj_thread-1.2.98/xj_thread.egg-info/requires.txt
--rw-rw-rw-   0        0        0       10 2023-03-29 10:20:19.000000 xj_thread-1.2.98/xj_thread.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-03-29 10:52:02.000000 xj_thread-1.2.99/
+-rw-rw-rw-   0        0        0    24709 2023-03-29 10:52:02.000000 xj_thread-1.2.99/PKG-INFO
+-rw-rw-rw-   0        0        0    21225 2022-08-03 08:57:06.000000 xj_thread-1.2.99/README.md
+-rw-rw-rw-   0        0        0       42 2023-03-29 10:52:02.000000 xj_thread-1.2.99/setup.cfg
+-rw-rw-rw-   0        0        0     1942 2023-03-29 10:51:52.000000 xj_thread-1.2.99/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-29 10:52:02.000000 xj_thread-1.2.99/xj_thread/
+-rw-rw-rw-   0        0        0        0 2022-08-23 09:09:46.000000 xj_thread-1.2.99/xj_thread/__init__.py
+-rw-rw-rw-   0        0        0     6764 2023-03-07 02:17:28.000000 xj_thread-1.2.99/xj_thread/admin.py
+drwxrwxrwx   0        0        0        0 2023-03-29 10:52:02.000000 xj_thread-1.2.99/xj_thread/apis/
+-rw-rw-rw-   0        0        0      134 2022-08-03 09:04:37.000000 xj_thread-1.2.99/xj_thread/apis/__init__.py
+-rw-rw-rw-   0        0        0     1341 2022-10-27 08:44:15.000000 xj_thread-1.2.99/xj_thread/apis/thread_add.py
+-rw-rw-rw-   0        0        0     2130 2023-03-28 07:47:36.000000 xj_thread-1.2.99/xj_thread/apis/thread_category_apis.py
+-rw-rw-rw-   0        0        0     1943 2023-02-14 02:04:01.000000 xj_thread-1.2.99/xj_thread/apis/thread_category_tree.py
+-rw-rw-rw-   0        0        0     2241 2023-03-28 08:00:45.000000 xj_thread-1.2.99/xj_thread/apis/thread_classify_apis.py
+-rw-rw-rw-   0        0        0     1497 2022-10-27 08:45:06.000000 xj_thread-1.2.99/xj_thread/apis/thread_classify_tree.py
+-rw-rw-rw-   0        0        0     2012 2022-11-09 08:58:16.000000 xj_thread-1.2.99/xj_thread/apis/thread_item.py
+-rw-rw-rw-   0        0        0     4389 2023-03-29 10:21:53.000000 xj_thread-1.2.99/xj_thread/apis/thread_list.py
+-rw-rw-rw-   0        0        0     7243 2023-03-07 01:49:05.000000 xj_thread-1.2.99/xj_thread/apis/thread_list[del ].py
+-rw-rw-rw-   0        0        0     2649 2023-03-16 09:15:12.000000 xj_thread-1.2.99/xj_thread/apis/thread_other_list.py
+-rw-rw-rw-   0        0        0     1755 2022-10-27 08:45:57.000000 xj_thread-1.2.99/xj_thread/apis/thread_statistic.py
+-rw-rw-rw-   0        0        0      206 2022-09-06 01:51:47.000000 xj_thread-1.2.99/xj_thread/apps.py
+-rw-rw-rw-   0        0        0      367 2022-06-04 04:47:05.000000 xj_thread-1.2.99/xj_thread/forms.py
+-rw-rw-rw-   0        0        0    29726 2023-03-29 08:11:05.000000 xj_thread-1.2.99/xj_thread/models.py
+-rw-rw-rw-   0        0        0     9810 2023-03-07 07:59:19.000000 xj_thread-1.2.99/xj_thread/serializers.py
+drwxrwxrwx   0        0        0        0 2023-03-29 10:52:02.000000 xj_thread-1.2.99/xj_thread/services/
+-rw-rw-rw-   0        0        0      134 2022-08-03 09:04:22.000000 xj_thread-1.2.99/xj_thread/services/__init__.py
+-rw-rw-rw-   0        0        0     5478 2023-03-29 03:28:57.000000 xj_thread-1.2.99/xj_thread/services/thread_category_service.py
+-rw-rw-rw-   0        0        0     3324 2022-10-08 03:32:47.000000 xj_thread-1.2.99/xj_thread/services/thread_category_tree_service [backup].py
+-rw-rw-rw-   0        0        0     3956 2023-03-29 10:18:29.000000 xj_thread-1.2.99/xj_thread/services/thread_category_tree_service.py
+-rw-rw-rw-   0        0        0     5471 2023-03-28 08:01:26.000000 xj_thread-1.2.99/xj_thread/services/thread_classify_service.py
+-rw-rw-rw-   0        0        0     2807 2022-12-31 09:12:26.000000 xj_thread-1.2.99/xj_thread/services/thread_classify_tree_service.py
+-rw-rw-rw-   0        0        0     6311 2023-03-07 09:12:49.000000 xj_thread-1.2.99/xj_thread/services/thread_extend_service.py
+-rw-rw-rw-   0        0        0     6120 2023-03-07 09:15:33.000000 xj_thread-1.2.99/xj_thread/services/thread_item_service.py
+-rw-rw-rw-   0        0        0    10266 2023-03-29 10:41:30.000000 xj_thread-1.2.99/xj_thread/services/thread_list_service.py
+-rw-rw-rw-   0        0        0     6497 2023-03-16 09:13:45.000000 xj_thread-1.2.99/xj_thread/services/thread_other_list_service.py
+-rw-rw-rw-   0        0        0     2423 2023-03-14 07:10:59.000000 xj_thread-1.2.99/xj_thread/services/thread_statistic_service.py
+-rw-rw-rw-   0        0        0     3025 2023-03-28 07:54:45.000000 xj_thread-1.2.99/xj_thread/urls.py
+drwxrwxrwx   0        0        0        0 2023-03-29 10:52:02.000000 xj_thread-1.2.99/xj_thread/utils/
+-rw-rw-rw-   0        0        0      134 2022-08-03 09:04:51.000000 xj_thread-1.2.99/xj_thread/utils/__init__.py
+-rw-rw-rw-   0        0        0      635 2022-08-02 02:23:40.000000 xj_thread-1.2.99/xj_thread/utils/custom_authentication_wrapper.py
+-rw-rw-rw-   0        0        0     1524 2022-08-02 07:03:31.000000 xj_thread-1.2.99/xj_thread/utils/custom_authorization.py
+-rw-rw-rw-   0        0        0     1551 2022-04-22 01:16:10.000000 xj_thread-1.2.99/xj_thread/utils/custom_exception.py
+-rw-rw-rw-   0        0        0      881 2022-04-22 01:16:10.000000 xj_thread-1.2.99/xj_thread/utils/custom_pagination.py
+-rw-rw-rw-   0        0        0     1749 2023-03-07 06:35:37.000000 xj_thread-1.2.99/xj_thread/utils/custom_response.py
+-rw-rw-rw-   0        0        0    18541 2023-03-20 01:56:43.000000 xj_thread-1.2.99/xj_thread/utils/custom_tool.py
+-rw-rw-rw-   0        0        0      429 2022-08-27 10:02:03.000000 xj_thread-1.2.99/xj_thread/utils/j_dict.py
+-rw-rw-rw-   0        0        0     7614 2023-03-29 10:15:38.000000 xj_thread-1.2.99/xj_thread/utils/j_recur.py
+-rw-rw-rw-   0        0        0      769 2022-10-08 03:32:47.000000 xj_thread-1.2.99/xj_thread/utils/j_type.py
+-rw-rw-rw-   0        0        0      660 2022-09-07 09:11:23.000000 xj_thread-1.2.99/xj_thread/utils/join_list.py
+-rw-rw-rw-   0        0        0     4194 2023-02-14 01:48:07.000000 xj_thread-1.2.99/xj_thread/utils/user_wrapper.py
+-rw-rw-rw-   0        0        0     3885 2022-06-20 06:19:26.000000 xj_thread-1.2.99/xj_thread/utils/util.py
+-rw-rw-rw-   0        0        0     2682 2022-07-29 14:44:11.000000 xj_thread-1.2.99/xj_thread/utils/validator.py
+-rw-rw-rw-   0        0        0      789 2022-09-07 09:21:20.000000 xj_thread-1.2.99/xj_thread/utils/x_get_params.py
+-rw-rw-rw-   0        0        0     1606 2022-10-25 09:22:04.000000 xj_thread-1.2.99/xj_thread/validator.py
+-rw-rw-rw-   0        0        0     6699 2022-07-31 11:32:37.000000 xj_thread-1.2.99/xj_thread/views.py
+drwxrwxrwx   0        0        0        0 2023-03-29 10:52:02.000000 xj_thread-1.2.99/xj_thread.egg-info/
+-rw-rw-rw-   0        0        0    24709 2023-03-29 10:52:01.000000 xj_thread-1.2.99/xj_thread.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1733 2023-03-29 10:52:01.000000 xj_thread-1.2.99/xj_thread.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-29 10:52:01.000000 xj_thread-1.2.99/xj_thread.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       16 2023-03-29 10:52:01.000000 xj_thread-1.2.99/xj_thread.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       10 2023-03-29 10:52:01.000000 xj_thread-1.2.99/xj_thread.egg-info/top_level.txt
```

### Comparing `xj_thread-1.2.98/PKG-INFO` & `xj_thread-1.2.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: xj_thread
-Version: 1.2.98
+Version: 1.2.99
 Summary: 信息模块
 Home-page: UNKNOWN
 License: apache 3.0
 Description: <<<<<<< HEAD
         # sql
         
         ```mysql
```

### Comparing `xj_thread-1.2.98/README.md` & `xj_thread-1.2.99/README.md`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/setup.py` & `xj_thread-1.2.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 from setuptools import setup, find_packages
 
 with open('README.md', 'r', encoding='utf8') as fp:
     log_desc = fp.read()
 
 setup(
     name='xj_thread',  # 模块名称
-    version='1.2.98',  # 模块版本
+    version='1.2.99',  # 模块版本
     description='信息模块',  # 项目 摘要描述
     long_description=log_desc,  # 项目描述
     long_description_content_type="text/markdown",  # md文件，markdown格式
     packages=find_packages(),  # 系统自动从当前目录开始找包
     # packages=['xj_user'],  # 系指定安装模块
     license="apache 3.0",
```

### Comparing `xj_thread-1.2.98/xj_thread/admin.py` & `xj_thread-1.2.99/xj_thread/admin.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/apis/thread_add.py` & `xj_thread-1.2.99/xj_thread/apis/thread_add.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/apis/thread_category_apis.py` & `xj_thread-1.2.99/xj_thread/apis/thread_category_apis.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/apis/thread_category_tree.py` & `xj_thread-1.2.99/xj_thread/apis/thread_category_tree.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/apis/thread_classify_apis.py` & `xj_thread-1.2.99/xj_thread/apis/thread_classify_apis.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/apis/thread_classify_tree.py` & `xj_thread-1.2.99/xj_thread/apis/thread_classify_tree.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/apis/thread_item.py` & `xj_thread-1.2.99/xj_thread/apis/thread_item.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/apis/thread_list.py` & `xj_thread-1.2.99/xj_thread/apis/thread_list.py`

 * *Files 0% similar despite different names*

```diff
@@ -39,14 +39,15 @@
             category_ids, category_tree_err = ThreadCategoryTreeServices.get_child_ids(
                 category_id=request_params.pop("category_id", None),
                 category_value=request_params.pop("category_value", None)
             )
             if category_tree_err:
                 return util_response(err=1000, msg="获取字数节点错误：" + category_tree_err)
             request_params.setdefault("category_id_list", category_ids)
+
         # 检查时间格式
         try:
             if request_params.get('create_time_start'):
                 datetime.datetime.strptime(request_params.get('create_time_start'), "%Y-%m-%d %H:%M:%S")
             if request_params.get('create_time_end'):
                 datetime.datetime.strptime(request_params.get('create_time_end'), "%Y-%m-%d %H:%M:%S")
         except ValueError:
```

### Comparing `xj_thread-1.2.98/xj_thread/apis/thread_list[del ].py` & `xj_thread-1.2.99/xj_thread/apis/thread_list[del ].py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/apis/thread_other_list.py` & `xj_thread-1.2.99/xj_thread/apis/thread_other_list.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/apis/thread_statistic.py` & `xj_thread-1.2.99/xj_thread/apis/thread_statistic.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/models.py` & `xj_thread-1.2.99/xj_thread/models.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/serializers.py` & `xj_thread-1.2.99/xj_thread/serializers.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/services/thread_category_service.py` & `xj_thread-1.2.99/xj_thread/services/thread_category_service.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/services/thread_category_tree_service [backup].py` & `xj_thread-1.2.99/xj_thread/services/thread_category_tree_service [backup].py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/services/thread_category_tree_service.py` & `xj_thread-1.2.99/xj_thread/services/thread_category_tree_service.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/services/thread_classify_service.py` & `xj_thread-1.2.99/xj_thread/services/thread_classify_service.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/services/thread_classify_tree_service.py` & `xj_thread-1.2.99/xj_thread/services/thread_classify_tree_service.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/services/thread_extend_service.py` & `xj_thread-1.2.99/xj_thread/services/thread_extend_service.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/services/thread_item_service.py` & `xj_thread-1.2.99/xj_thread/services/thread_item_service.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/services/thread_list_service.py` & `xj_thread-1.2.99/xj_thread/services/thread_list_service.py`

 * *Files 4% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 @Email: sky4834@163.com
 @synopsis:
 @created_time: 2022/7/29 15:11
 """
 import logging
 
 from django.core.paginator import Paginator
-from django.db.models import F, Q
+from django.db.models import F
 
 from xj_thread.services.thread_extend_service import ThreadExtendOutPutService
 from ..models import Thread, ThreadTagMapping
 from ..utils.custom_tool import filter_result_field, format_params_handle
 
 log = logging.getLogger()
 
@@ -121,24 +121,31 @@
         """
         if not id_list:
             return [], None
         thread_set = Thread.objects.filter(id__in=id_list)
         # 开始按过滤条件
         try:
             thread_set = thread_set \
+                .annotate(thread_category_value=F("category_id__value")) \
+                .annotate(thread_category_name=F("category_id__name")) \
                 .annotate(category_value=F("category_id__value")) \
                 .annotate(category_name=F("category_id__name")) \
                 .annotate(need_auth=F("category_id__need_auth")) \
-                .annotate(classify_value=F("classify_id__value")) \
+                .annotate(thread_classify_value=F("classify_id__value")) \
                 .annotate(thread_classify_name=F("classify_id__name")) \
+                .annotate(classify_value=F("classify_id__value")) \
+                .annotate(classify_name=F("classify_id__name")) \
                 .annotate(show_value=F("show_id__value"))
 
             thread_set = thread_set.filter(is_deleted=0)
+            # TODO 后期迭代计划：删除调thread前缀，与前端沟通一致 2023/3/29
             thread_set = thread_set.values(
-                'thread_category_value', 'thread_category_name', 'thread_classify_value', 'thread_classify_name', "id", "is_deleted", "category_id", "classify_id",
+                'thread_category_value', 'thread_category_name', 'thread_classify_value', 'thread_classify_name',
+                'category_value', 'category_name', 'classify_value', 'classify_name', "show_value",
+                "id", "is_deleted", "category_id", "classify_id",
                 "show", "user_id", "with_user_id", "title", "subtitle", "content", "summary",
                 "access_level", "author", "ip", "has_enroll", "has_fee", "has_comment", "has_location",
                 "cover", "photos", "video", "files", "price", "is_original", "link", "create_time",
                 "update_time", "logs", "more", "sort", "language_code",
             )
         except Exception as e:
             return None, "err:" + e.__str__()
```

### Comparing `xj_thread-1.2.98/xj_thread/services/thread_other_list_service.py` & `xj_thread-1.2.99/xj_thread/services/thread_other_list_service.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/services/thread_statistic_service.py` & `xj_thread-1.2.99/xj_thread/services/thread_statistic_service.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/urls.py` & `xj_thread-1.2.99/xj_thread/urls.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/custom_authentication_wrapper.py` & `xj_thread-1.2.99/xj_thread/utils/custom_authentication_wrapper.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/custom_authorization.py` & `xj_thread-1.2.99/xj_thread/utils/custom_authorization.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/custom_exception.py` & `xj_thread-1.2.99/xj_thread/utils/custom_exception.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/custom_pagination.py` & `xj_thread-1.2.99/xj_thread/utils/custom_pagination.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/custom_response.py` & `xj_thread-1.2.99/xj_thread/utils/custom_response.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/custom_tool.py` & `xj_thread-1.2.99/xj_thread/utils/custom_tool.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/j_recur.py` & `xj_thread-1.2.99/xj_thread/utils/j_recur.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/j_type.py` & `xj_thread-1.2.99/xj_thread/utils/j_type.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/join_list.py` & `xj_thread-1.2.99/xj_thread/utils/join_list.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/user_wrapper.py` & `xj_thread-1.2.99/xj_thread/utils/user_wrapper.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/util.py` & `xj_thread-1.2.99/xj_thread/utils/util.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/validator.py` & `xj_thread-1.2.99/xj_thread/utils/validator.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/utils/x_get_params.py` & `xj_thread-1.2.99/xj_thread/utils/x_get_params.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/validator.py` & `xj_thread-1.2.99/xj_thread/validator.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread/views.py` & `xj_thread-1.2.99/xj_thread/views.py`

 * *Files identical despite different names*

### Comparing `xj_thread-1.2.98/xj_thread.egg-info/PKG-INFO` & `xj_thread-1.2.99/xj_thread.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: xj-thread
-Version: 1.2.98
+Version: 1.2.99
 Summary: 信息模块
 Home-page: UNKNOWN
 License: apache 3.0
 Description: <<<<<<< HEAD
         # sql
         
         ```mysql
```

### Comparing `xj_thread-1.2.98/xj_thread.egg-info/SOURCES.txt` & `xj_thread-1.2.99/xj_thread.egg-info/SOURCES.txt`

 * *Files identical despite different names*

