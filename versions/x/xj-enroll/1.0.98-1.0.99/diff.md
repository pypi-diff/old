# Comparing `tmp/xj_enroll-1.0.98.tar.gz` & `tmp/xj_enroll-1.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\xj_enroll-1.0.98.tar", last modified: Tue Feb  7 13:58:36 2023, max compression
+gzip compressed data, was "dist\xj_enroll-1.0.99.tar", last modified: Tue Feb  7 14:02:40 2023, max compression
```

## Comparing `xj_enroll-1.0.98.tar` & `xj_enroll-1.0.99.tar`

### file list

```diff
@@ -1,62 +1,62 @@
-drwxrwxrwx   0        0        0        0 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/
--rw-rw-rw-   0        0        0     1968 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/PKG-INFO
--rw-rw-rw-   0        0        0     1353 2022-09-14 03:26:13.000000 xj_enroll-1.0.98/README.md
--rw-rw-rw-   0        0        0       42 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/setup.cfg
--rw-rw-rw-   0        0        0      893 2023-02-07 13:58:30.000000 xj_enroll-1.0.98/setup.py
-drwxrwxrwx   0        0        0        0 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/xj_enroll/
--rw-rw-rw-   0        0        0        0 2023-01-12 06:01:27.000000 xj_enroll-1.0.98/xj_enroll/__init__.py
--rw-rw-rw-   0        0        0     6163 2022-11-13 07:07:22.000000 xj_enroll-1.0.98/xj_enroll/admin.py
-drwxrwxrwx   0        0        0        0 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/xj_enroll/api/
--rw-rw-rw-   0        0        0     2215 2022-09-20 07:01:02.000000 xj_enroll-1.0.98/xj_enroll/api/[category_apis_del][del_by_sky].py
--rw-rw-rw-   0        0        0     2224 2022-09-20 04:02:23.000000 xj_enroll-1.0.98/xj_enroll/api/[classify_apis_del][del_by_sky].py
--rw-rw-rw-   0        0        0      148 2022-09-23 01:24:10.000000 xj_enroll-1.0.98/xj_enroll/api/__init__.py
--rw-rw-rw-   0        0        0    22384 2023-02-06 09:03:25.000000 xj_enroll-1.0.98/xj_enroll/api/enroll_apis.py
--rw-rw-rw-   0        0        0     1642 2022-11-03 06:34:39.000000 xj_enroll-1.0.98/xj_enroll/api/enroll_statistics_apis.py
--rw-rw-rw-   0        0        0     1364 2022-12-05 04:21:39.000000 xj_enroll-1.0.98/xj_enroll/api/enroll_status_code_api.py
--rw-rw-rw-   0        0        0      466 2022-10-14 06:26:57.000000 xj_enroll-1.0.98/xj_enroll/api/rarely_data_list_api.py
--rw-rw-rw-   0        0        0     5258 2023-02-07 13:21:31.000000 xj_enroll-1.0.98/xj_enroll/api/record_apis.py
--rw-rw-rw-   0        0        0     2723 2022-11-03 01:49:16.000000 xj_enroll-1.0.98/xj_enroll/api/rule_apis.py
--rw-rw-rw-   0        0        0     5663 2022-11-03 02:00:45.000000 xj_enroll-1.0.98/xj_enroll/api/subitem_apis.py
--rw-rw-rw-   0        0        0     2696 2022-10-30 06:12:38.000000 xj_enroll-1.0.98/xj_enroll/api/subitem_record_apis.py
--rw-rw-rw-   0        0        0     3585 2023-02-07 08:22:30.000000 xj_enroll-1.0.98/xj_enroll/api/valuation_api.py
--rw-rw-rw-   0        0        0      206 2023-01-12 06:06:58.000000 xj_enroll-1.0.98/xj_enroll/apps.py
--rw-rw-rw-   0        0        0      660 2022-09-26 08:18:26.000000 xj_enroll-1.0.98/xj_enroll/join_list.py
--rw-rw-rw-   0        0        0    26654 2023-01-12 07:21:10.000000 xj_enroll-1.0.98/xj_enroll/models.py
--rw-rw-rw-   0        0        0     2262 2023-02-06 09:40:00.000000 xj_enroll-1.0.98/xj_enroll/serializers.py
-drwxrwxrwx   0        0        0        0 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/xj_enroll/service/
--rw-rw-rw-   0        0        0     2265 2022-10-12 06:42:25.000000 xj_enroll-1.0.98/xj_enroll/service/[category_service][del_by_sky].py
--rw-rw-rw-   0        0        0     2452 2022-10-12 06:42:25.000000 xj_enroll-1.0.98/xj_enroll/service/[classify_service_del][del_by_sky].py
--rw-rw-rw-   0        0        0      148 2022-09-23 01:24:20.000000 xj_enroll-1.0.98/xj_enroll/service/__init__.py
--rw-rw-rw-   0        0        0     6866 2022-11-03 02:04:14.000000 xj_enroll-1.0.98/xj_enroll/service/clock_service.py
--rw-rw-rw-   0        0        0    15778 2023-02-07 10:10:03.000000 xj_enroll-1.0.98/xj_enroll/service/enroll_record_serivce.py
--rw-rw-rw-   0        0        0    17666 2023-02-07 13:58:18.000000 xj_enroll-1.0.98/xj_enroll/service/enroll_services.py
--rw-rw-rw-   0        0        0     6189 2022-11-03 07:25:50.000000 xj_enroll-1.0.98/xj_enroll/service/enroll_statistics_service.py
--rw-rw-rw-   0        0        0     1864 2022-11-13 10:15:21.000000 xj_enroll-1.0.98/xj_enroll/service/enroll_status_code_service.py
--rw-rw-rw-   0        0        0     5838 2023-02-07 07:53:52.000000 xj_enroll-1.0.98/xj_enroll/service/enroll_subitem_record_service.py
--rw-rw-rw-   0        0        0    10496 2022-10-17 02:22:11.000000 xj_enroll-1.0.98/xj_enroll/service/excel_exporter_service.py
--rw-rw-rw-   0        0        0     3058 2023-02-06 06:40:18.000000 xj_enroll-1.0.98/xj_enroll/service/rule_service.py
--rw-rw-rw-   0        0        0     2284 2022-10-31 07:35:09.000000 xj_enroll-1.0.98/xj_enroll/service/subitem_extend_service.py
--rw-rw-rw-   0        0        0     8260 2023-02-07 08:01:58.000000 xj_enroll-1.0.98/xj_enroll/service/subitem_service.py
--rw-rw-rw-   0        0        0     4796 2023-02-07 13:21:39.000000 xj_enroll-1.0.98/xj_enroll/service/valuation_service.py
--rw-rw-rw-   0        0        0      841 2023-02-03 07:02:42.000000 xj_enroll-1.0.98/xj_enroll/service_register.py
--rw-rw-rw-   0        0        0     3640 2023-02-01 00:48:31.000000 xj_enroll-1.0.98/xj_enroll/urls.py
-drwxrwxrwx   0        0        0        0 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/xj_enroll/utils/
--rw-rw-rw-   0        0        0      148 2022-09-23 01:24:35.000000 xj_enroll-1.0.98/xj_enroll/utils/__init__.py
--rw-rw-rw-   0        0        0     1345 2022-10-29 05:40:12.000000 xj_enroll-1.0.98/xj_enroll/utils/custom_response.py
--rw-rw-rw-   0        0        0     7796 2023-02-03 08:42:49.000000 xj_enroll-1.0.98/xj_enroll/utils/custom_tool.py
--rw-rw-rw-   0        0        0      988 2023-01-04 07:56:02.000000 xj_enroll-1.0.98/xj_enroll/utils/j_config.py
--rw-rw-rw-   0        0        0      429 2022-08-27 10:02:03.000000 xj_enroll-1.0.98/xj_enroll/utils/j_dict.py
--rw-rw-rw-   0        0        0     8089 2023-02-07 12:53:59.000000 xj_enroll-1.0.98/xj_enroll/utils/j_valuation.py
--rw-rw-rw-   0        0        0      660 2022-09-07 09:11:23.000000 xj_enroll-1.0.98/xj_enroll/utils/join_list.py
--rw-rw-rw-   0        0        0     2932 2022-09-20 03:29:30.000000 xj_enroll-1.0.98/xj_enroll/utils/validator.py
-drwxrwxrwx   0        0        0        0 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/xj_enroll/validator/
--rw-rw-rw-   0        0        0      146 2022-09-23 01:24:49.000000 xj_enroll-1.0.98/xj_enroll/validator/__init__.py
--rw-rw-rw-   0        0        0      639 2022-09-20 03:28:13.000000 xj_enroll-1.0.98/xj_enroll/validator/category_validator.py
--rw-rw-rw-   0        0        0     2685 2022-09-17 09:04:36.000000 xj_enroll-1.0.98/xj_enroll/validator/enroll_validator.py
--rw-rw-rw-   0        0        0      634 2022-10-13 03:01:47.000000 xj_enroll-1.0.98/xj_enroll/validator/record_validator.py
--rw-rw-rw-   0        0        0      969 2022-09-20 05:29:39.000000 xj_enroll-1.0.98/xj_enroll/validator/rule_validator.py
-drwxrwxrwx   0        0        0        0 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/xj_enroll.egg-info/
--rw-rw-rw-   0        0        0     1968 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/xj_enroll.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     1776 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/xj_enroll.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/xj_enroll.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       10 2023-02-07 13:58:36.000000 xj_enroll-1.0.98/xj_enroll.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/
+-rw-rw-rw-   0        0        0     1968 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/PKG-INFO
+-rw-rw-rw-   0        0        0     1353 2022-09-14 03:26:13.000000 xj_enroll-1.0.99/README.md
+-rw-rw-rw-   0        0        0       42 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/setup.cfg
+-rw-rw-rw-   0        0        0      893 2023-02-07 14:02:33.000000 xj_enroll-1.0.99/setup.py
+drwxrwxrwx   0        0        0        0 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/xj_enroll/
+-rw-rw-rw-   0        0        0        0 2023-01-12 06:01:27.000000 xj_enroll-1.0.99/xj_enroll/__init__.py
+-rw-rw-rw-   0        0        0     6163 2022-11-13 07:07:22.000000 xj_enroll-1.0.99/xj_enroll/admin.py
+drwxrwxrwx   0        0        0        0 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/xj_enroll/api/
+-rw-rw-rw-   0        0        0     2215 2022-09-20 07:01:02.000000 xj_enroll-1.0.99/xj_enroll/api/[category_apis_del][del_by_sky].py
+-rw-rw-rw-   0        0        0     2224 2022-09-20 04:02:23.000000 xj_enroll-1.0.99/xj_enroll/api/[classify_apis_del][del_by_sky].py
+-rw-rw-rw-   0        0        0      148 2022-09-23 01:24:10.000000 xj_enroll-1.0.99/xj_enroll/api/__init__.py
+-rw-rw-rw-   0        0        0    22384 2023-02-06 09:03:25.000000 xj_enroll-1.0.99/xj_enroll/api/enroll_apis.py
+-rw-rw-rw-   0        0        0     1642 2022-11-03 06:34:39.000000 xj_enroll-1.0.99/xj_enroll/api/enroll_statistics_apis.py
+-rw-rw-rw-   0        0        0     1364 2022-12-05 04:21:39.000000 xj_enroll-1.0.99/xj_enroll/api/enroll_status_code_api.py
+-rw-rw-rw-   0        0        0      466 2022-10-14 06:26:57.000000 xj_enroll-1.0.99/xj_enroll/api/rarely_data_list_api.py
+-rw-rw-rw-   0        0        0     5258 2023-02-07 13:21:31.000000 xj_enroll-1.0.99/xj_enroll/api/record_apis.py
+-rw-rw-rw-   0        0        0     2723 2022-11-03 01:49:16.000000 xj_enroll-1.0.99/xj_enroll/api/rule_apis.py
+-rw-rw-rw-   0        0        0     5663 2022-11-03 02:00:45.000000 xj_enroll-1.0.99/xj_enroll/api/subitem_apis.py
+-rw-rw-rw-   0        0        0     2696 2022-10-30 06:12:38.000000 xj_enroll-1.0.99/xj_enroll/api/subitem_record_apis.py
+-rw-rw-rw-   0        0        0     3585 2023-02-07 08:22:30.000000 xj_enroll-1.0.99/xj_enroll/api/valuation_api.py
+-rw-rw-rw-   0        0        0      206 2023-01-12 06:06:58.000000 xj_enroll-1.0.99/xj_enroll/apps.py
+-rw-rw-rw-   0        0        0      660 2022-09-26 08:18:26.000000 xj_enroll-1.0.99/xj_enroll/join_list.py
+-rw-rw-rw-   0        0        0    26654 2023-01-12 07:21:10.000000 xj_enroll-1.0.99/xj_enroll/models.py
+-rw-rw-rw-   0        0        0     2262 2023-02-06 09:40:00.000000 xj_enroll-1.0.99/xj_enroll/serializers.py
+drwxrwxrwx   0        0        0        0 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/xj_enroll/service/
+-rw-rw-rw-   0        0        0     2265 2022-10-12 06:42:25.000000 xj_enroll-1.0.99/xj_enroll/service/[category_service][del_by_sky].py
+-rw-rw-rw-   0        0        0     2452 2022-10-12 06:42:25.000000 xj_enroll-1.0.99/xj_enroll/service/[classify_service_del][del_by_sky].py
+-rw-rw-rw-   0        0        0      148 2022-09-23 01:24:20.000000 xj_enroll-1.0.99/xj_enroll/service/__init__.py
+-rw-rw-rw-   0        0        0     6866 2022-11-03 02:04:14.000000 xj_enroll-1.0.99/xj_enroll/service/clock_service.py
+-rw-rw-rw-   0        0        0    15778 2023-02-07 10:10:03.000000 xj_enroll-1.0.99/xj_enroll/service/enroll_record_serivce.py
+-rw-rw-rw-   0        0        0    17854 2023-02-07 14:02:16.000000 xj_enroll-1.0.99/xj_enroll/service/enroll_services.py
+-rw-rw-rw-   0        0        0     6189 2022-11-03 07:25:50.000000 xj_enroll-1.0.99/xj_enroll/service/enroll_statistics_service.py
+-rw-rw-rw-   0        0        0     1864 2022-11-13 10:15:21.000000 xj_enroll-1.0.99/xj_enroll/service/enroll_status_code_service.py
+-rw-rw-rw-   0        0        0     5838 2023-02-07 07:53:52.000000 xj_enroll-1.0.99/xj_enroll/service/enroll_subitem_record_service.py
+-rw-rw-rw-   0        0        0    10496 2022-10-17 02:22:11.000000 xj_enroll-1.0.99/xj_enroll/service/excel_exporter_service.py
+-rw-rw-rw-   0        0        0     3058 2023-02-06 06:40:18.000000 xj_enroll-1.0.99/xj_enroll/service/rule_service.py
+-rw-rw-rw-   0        0        0     2284 2022-10-31 07:35:09.000000 xj_enroll-1.0.99/xj_enroll/service/subitem_extend_service.py
+-rw-rw-rw-   0        0        0     8260 2023-02-07 08:01:58.000000 xj_enroll-1.0.99/xj_enroll/service/subitem_service.py
+-rw-rw-rw-   0        0        0     4796 2023-02-07 13:21:39.000000 xj_enroll-1.0.99/xj_enroll/service/valuation_service.py
+-rw-rw-rw-   0        0        0      841 2023-02-03 07:02:42.000000 xj_enroll-1.0.99/xj_enroll/service_register.py
+-rw-rw-rw-   0        0        0     3640 2023-02-01 00:48:31.000000 xj_enroll-1.0.99/xj_enroll/urls.py
+drwxrwxrwx   0        0        0        0 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/xj_enroll/utils/
+-rw-rw-rw-   0        0        0      148 2022-09-23 01:24:35.000000 xj_enroll-1.0.99/xj_enroll/utils/__init__.py
+-rw-rw-rw-   0        0        0     1345 2022-10-29 05:40:12.000000 xj_enroll-1.0.99/xj_enroll/utils/custom_response.py
+-rw-rw-rw-   0        0        0     7796 2023-02-03 08:42:49.000000 xj_enroll-1.0.99/xj_enroll/utils/custom_tool.py
+-rw-rw-rw-   0        0        0      988 2023-01-04 07:56:02.000000 xj_enroll-1.0.99/xj_enroll/utils/j_config.py
+-rw-rw-rw-   0        0        0      429 2022-08-27 10:02:03.000000 xj_enroll-1.0.99/xj_enroll/utils/j_dict.py
+-rw-rw-rw-   0        0        0     8089 2023-02-07 12:53:59.000000 xj_enroll-1.0.99/xj_enroll/utils/j_valuation.py
+-rw-rw-rw-   0        0        0      660 2022-09-07 09:11:23.000000 xj_enroll-1.0.99/xj_enroll/utils/join_list.py
+-rw-rw-rw-   0        0        0     2932 2022-09-20 03:29:30.000000 xj_enroll-1.0.99/xj_enroll/utils/validator.py
+drwxrwxrwx   0        0        0        0 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/xj_enroll/validator/
+-rw-rw-rw-   0        0        0      146 2022-09-23 01:24:49.000000 xj_enroll-1.0.99/xj_enroll/validator/__init__.py
+-rw-rw-rw-   0        0        0      639 2022-09-20 03:28:13.000000 xj_enroll-1.0.99/xj_enroll/validator/category_validator.py
+-rw-rw-rw-   0        0        0     2685 2022-09-17 09:04:36.000000 xj_enroll-1.0.99/xj_enroll/validator/enroll_validator.py
+-rw-rw-rw-   0        0        0      634 2022-10-13 03:01:47.000000 xj_enroll-1.0.99/xj_enroll/validator/record_validator.py
+-rw-rw-rw-   0        0        0      969 2022-09-20 05:29:39.000000 xj_enroll-1.0.99/xj_enroll/validator/rule_validator.py
+drwxrwxrwx   0        0        0        0 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/xj_enroll.egg-info/
+-rw-rw-rw-   0        0        0     1968 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/xj_enroll.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1776 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/xj_enroll.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/xj_enroll.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       10 2023-02-07 14:02:40.000000 xj_enroll-1.0.99/xj_enroll.egg-info/top_level.txt
```

### Comparing `xj_enroll-1.0.98/PKG-INFO` & `xj_enroll-1.0.99/xj_enroll.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: xj_enroll
-Version: 1.0.98
+Name: xj-enroll
+Version: 1.0.99
 Summary: 报名模块
 Home-page: UNKNOWN
 Author: 赵向明
 Author-email: sieyoo@163.com
 Maintainer: 孙楷炎
 Maintainer-email: sky4834@163.com
 License: apache 3.0
```

### Comparing `xj_enroll-1.0.98/README.md` & `xj_enroll-1.0.99/README.md`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/setup.py` & `xj_enroll-1.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 from setuptools import setup, find_packages
 
 with open('README.md', 'r', encoding='utf8') as fp:
     log_desc = fp.read()
 
 setup(
     name='xj_enroll',  # 模块名称
-    version='1.0.98',  # 模块版本
+    version='1.0.99',  # 模块版本
     description='报名模块',  # 项目 摘要描述
     long_description=log_desc,  # 项目描述
     long_description_content_type="text/markdown",  # md文件，markdown格式
     author='赵向明',  # 作者
     author_email='sieyoo@163.com',  # 作者邮箱
     maintainer="孙楷炎",  # 维护者
     maintainer_email="sky4834@163.com",  # 维护者的邮箱地址
```

### Comparing `xj_enroll-1.0.98/xj_enroll/admin.py` & `xj_enroll-1.0.99/xj_enroll/admin.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/api/[category_apis_del][del_by_sky].py` & `xj_enroll-1.0.99/xj_enroll/api/[category_apis_del][del_by_sky].py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/api/[classify_apis_del][del_by_sky].py` & `xj_enroll-1.0.99/xj_enroll/api/[classify_apis_del][del_by_sky].py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/api/enroll_apis.py` & `xj_enroll-1.0.99/xj_enroll/api/enroll_apis.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/api/enroll_statistics_apis.py` & `xj_enroll-1.0.99/xj_enroll/api/enroll_statistics_apis.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/api/enroll_status_code_api.py` & `xj_enroll-1.0.99/xj_enroll/api/enroll_status_code_api.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/api/record_apis.py` & `xj_enroll-1.0.99/xj_enroll/api/record_apis.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/api/rule_apis.py` & `xj_enroll-1.0.99/xj_enroll/api/rule_apis.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/api/subitem_apis.py` & `xj_enroll-1.0.99/xj_enroll/api/subitem_apis.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/api/subitem_record_apis.py` & `xj_enroll-1.0.99/xj_enroll/api/subitem_record_apis.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/api/valuation_api.py` & `xj_enroll-1.0.99/xj_enroll/api/valuation_api.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/join_list.py` & `xj_enroll-1.0.99/xj_enroll/join_list.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/models.py` & `xj_enroll-1.0.99/xj_enroll/models.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/serializers.py` & `xj_enroll-1.0.99/xj_enroll/serializers.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service/[category_service][del_by_sky].py` & `xj_enroll-1.0.99/xj_enroll/service/[category_service][del_by_sky].py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service/[classify_service_del][del_by_sky].py` & `xj_enroll-1.0.99/xj_enroll/service/[classify_service_del][del_by_sky].py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service/clock_service.py` & `xj_enroll-1.0.99/xj_enroll/service/clock_service.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service/enroll_record_serivce.py` & `xj_enroll-1.0.99/xj_enroll/service/enroll_record_serivce.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service/enroll_services.py` & `xj_enroll-1.0.99/xj_enroll/service/enroll_services.py`

 * *Files 1% similar despite different names*

```diff
@@ -329,25 +329,29 @@
         情况2：（报名并指派后）用户支付差价，订单开始。进入上传状态。
         扩展逻辑：分销逻辑，资金逻辑。
 
         2023-2-6 回调逻辑：第一种代补差价付款成功后，直接进入已接单待上传，第二种：付完首付款后直接进入报名中
         :param order_no: 订单号
         :return: response
         """
+        print("资金模块回调")
         finance_transact_data, err = FinanceTransactsService.detail(order_no=order_no)
         if err:
+            print("err", err)
             return None, err
         try:
             user_id = finance_transact_data.get("account_id", None)
             enroll_id = finance_transact_data.get("enroll_id", None)
+            print("enroll_id", enroll_id, "account_id", user_id)
             outgo = finance_transact_data.get("outgo", 0)
             # print("支付回调报名", "user_id:", user_id, "enroll_id:", enroll_id, "order_no", order_no)
             enroll_obj = Enroll.objects.filter(id=enroll_id, user_id=user_id)
             enroll_set = enroll_obj.first()
             if not enroll_set:
+                print("不是一个有效的报名")
                 return None, None
             paid_amount = (enroll_set.paid_amount or 0) + (outgo or 0)
             # print(paid_amount, enroll_set.enroll_status_code)
             if int(enroll_set.enroll_status_code) == 243:
                 enroll_obj.update(paid_amount=paid_amount, unpaid_amount=0, enroll_status_code=356)
                 EnrollSubitem.objects.filter(enroll_id=enroll_id).update(enroll_subitem_status_code=356)
             else:
```

### Comparing `xj_enroll-1.0.98/xj_enroll/service/enroll_statistics_service.py` & `xj_enroll-1.0.99/xj_enroll/service/enroll_statistics_service.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service/enroll_status_code_service.py` & `xj_enroll-1.0.99/xj_enroll/service/enroll_status_code_service.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service/enroll_subitem_record_service.py` & `xj_enroll-1.0.99/xj_enroll/service/enroll_subitem_record_service.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service/excel_exporter_service.py` & `xj_enroll-1.0.99/xj_enroll/service/excel_exporter_service.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service/rule_service.py` & `xj_enroll-1.0.99/xj_enroll/service/rule_service.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service/subitem_extend_service.py` & `xj_enroll-1.0.99/xj_enroll/service/subitem_extend_service.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service/subitem_service.py` & `xj_enroll-1.0.99/xj_enroll/service/subitem_service.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service/valuation_service.py` & `xj_enroll-1.0.99/xj_enroll/service/valuation_service.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/service_register.py` & `xj_enroll-1.0.99/xj_enroll/service_register.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/urls.py` & `xj_enroll-1.0.99/xj_enroll/urls.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/utils/custom_response.py` & `xj_enroll-1.0.99/xj_enroll/utils/custom_response.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/utils/custom_tool.py` & `xj_enroll-1.0.99/xj_enroll/utils/custom_tool.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/utils/j_config.py` & `xj_enroll-1.0.99/xj_enroll/utils/j_config.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/utils/j_valuation.py` & `xj_enroll-1.0.99/xj_enroll/utils/j_valuation.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/utils/join_list.py` & `xj_enroll-1.0.99/xj_enroll/utils/join_list.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/utils/validator.py` & `xj_enroll-1.0.99/xj_enroll/utils/validator.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/validator/category_validator.py` & `xj_enroll-1.0.99/xj_enroll/validator/category_validator.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/validator/enroll_validator.py` & `xj_enroll-1.0.99/xj_enroll/validator/enroll_validator.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/validator/record_validator.py` & `xj_enroll-1.0.99/xj_enroll/validator/record_validator.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll/validator/rule_validator.py` & `xj_enroll-1.0.99/xj_enroll/validator/rule_validator.py`

 * *Files identical despite different names*

### Comparing `xj_enroll-1.0.98/xj_enroll.egg-info/PKG-INFO` & `xj_enroll-1.0.99/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: xj-enroll
-Version: 1.0.98
+Name: xj_enroll
+Version: 1.0.99
 Summary: 报名模块
 Home-page: UNKNOWN
 Author: 赵向明
 Author-email: sieyoo@163.com
 Maintainer: 孙楷炎
 Maintainer-email: sky4834@163.com
 License: apache 3.0
```

### Comparing `xj_enroll-1.0.98/xj_enroll.egg-info/SOURCES.txt` & `xj_enroll-1.0.99/xj_enroll.egg-info/SOURCES.txt`

 * *Files identical despite different names*

