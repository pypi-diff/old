# Comparing `tmp/zbxtool-cfomp-0.9.8.tar.gz` & `tmp/zbxtool-cfomp-0.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/zbxtool-cfomp-0.9.8.tar", last modified: Mon Dec 12 10:17:12 2022, max compression
+gzip compressed data, was "dist/zbxtool-cfomp-0.9.9.tar", last modified: Mon Dec 12 10:24:53 2022, max compression
```

## Comparing `zbxtool-cfomp-0.9.8.tar` & `zbxtool-cfomp-0.9.9.tar`

### file list

```diff
@@ -1,50 +1,50 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/lib/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/lib/commands/
--rw-r--r--   0 root         (0) root         (0)        0 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7135 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/discovery.py
--rw-r--r--   0 root         (0) root         (0)     5571 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/es_index_zbxhost.py
--rw-r--r--   0 root         (0) root         (0)     4391 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/fs_calc.py
--rw-r--r--   0 root         (0) root         (0)    47901 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/gen_analaysis_report.py
--rw-r--r--   0 root         (0) root         (0)     7843 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/hostgrp_aggr_item.py
--rw-r--r--   0 root         (0) root         (0)     1550 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/hosttpl.py
--rw-r--r--   0 root         (0) root         (0)     4289 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/inventory_supplementary.py
--rw-r--r--   0 root         (0) root         (0)     3577 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/ldap_usergrp.py
--rw-r--r--   0 root         (0) root         (0)     8778 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/multi_interfaces.py
--rw-r--r--   0 root         (0) root         (0)     5283 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/oob.py
--rw-r--r--   0 root         (0) root         (0)     3083 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/send_to_all_users.py
--rw-r--r--   0 root         (0) root         (0)     4113 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/service_tree.py
--rw-r--r--   0 root         (0) root         (0)     2408 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/sync_wework_media.py
--rw-r--r--   0 root         (0) root         (0)     4965 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/update_hostgrp_poc.py
--rw-r--r--   0 root         (0) root         (0)     1208 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/update_hostname.py
--rw-r--r--   0 root         (0) root         (0)     7276 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/commands/vmware_host_inventory.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/lib/utils/
--rw-r--r--   0 root         (0) root         (0)     2601 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/utils/LdapTool.py
--rw-r--r--   0 root         (0) root         (0)     2085 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/utils/TemplateBaseTool.py
--rw-r--r--   0 root         (0) root         (0)     2533 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/utils/TemplateTool.py
--rw-r--r--   0 root         (0) root         (0)        0 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/utils/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1744 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/utils/inventory_tag.py
--rw-r--r--   0 root         (0) root         (0)    10473 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/utils/wework.py
--rw-r--r--   0 root         (0) root         (0)        0 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1331 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/lib/cli.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/test/
--rw-r--r--   0 root         (0) root         (0)     1422 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/test/test_inventory_tag.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/zbxtool_cfomp.egg-info/
--rw-r--r--   0 root         (0) root         (0)      187 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/zbxtool_cfomp.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1085 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/zbxtool_cfomp.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/zbxtool_cfomp.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       42 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/zbxtool_cfomp.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)      299 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/zbxtool_cfomp.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        4 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/zbxtool_cfomp.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/zbxtool_cfomp.egg-info/zip-safe
--rw-r--r--   0 root         (0) root         (0)     2096 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/.gitignore
--rw-r--r--   0 root         (0) root         (0)     1061 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/CHANGELOG
--rw-r--r--   0 root         (0) root         (0)     1351 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/Jenkinsfile
--rw-r--r--   0 root         (0) root         (0)        8 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/LICENSE
--rw-r--r--   0 root         (0) root         (0)     4723 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/README.md
--rw-r--r--   0 root         (0) root         (0)     5804 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/ip_range.json
--rw-r--r--   0 root         (0) root         (0)      152 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/pytest.ini
--rw-r--r--   0 root         (0) root         (0)      299 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/requirements.txt
--rw-r--r--   0 root         (0) root         (0)      695 2022-12-12 10:16:53.000000 zbxtool-cfomp-0.9.8/setup.py
--rw-r--r--   0 root         (0) root         (0)      187 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       38 2022-12-12 10:17:12.000000 zbxtool-cfomp-0.9.8/setup.cfg
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/lib/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/lib/commands/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7135 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/discovery.py
+-rw-r--r--   0 root         (0) root         (0)     5571 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/es_index_zbxhost.py
+-rw-r--r--   0 root         (0) root         (0)     4391 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/fs_calc.py
+-rw-r--r--   0 root         (0) root         (0)    47901 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/gen_analaysis_report.py
+-rw-r--r--   0 root         (0) root         (0)     7843 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/hostgrp_aggr_item.py
+-rw-r--r--   0 root         (0) root         (0)     1550 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/hosttpl.py
+-rw-r--r--   0 root         (0) root         (0)     4289 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/inventory_supplementary.py
+-rw-r--r--   0 root         (0) root         (0)     3577 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/ldap_usergrp.py
+-rw-r--r--   0 root         (0) root         (0)     8778 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/multi_interfaces.py
+-rw-r--r--   0 root         (0) root         (0)     5283 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/oob.py
+-rw-r--r--   0 root         (0) root         (0)     3027 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/send_to_all_users.py
+-rw-r--r--   0 root         (0) root         (0)     4113 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/service_tree.py
+-rw-r--r--   0 root         (0) root         (0)     2408 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/sync_wework_media.py
+-rw-r--r--   0 root         (0) root         (0)     4965 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/update_hostgrp_poc.py
+-rw-r--r--   0 root         (0) root         (0)     1208 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/update_hostname.py
+-rw-r--r--   0 root         (0) root         (0)     7276 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/commands/vmware_host_inventory.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/lib/utils/
+-rw-r--r--   0 root         (0) root         (0)     2601 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/utils/LdapTool.py
+-rw-r--r--   0 root         (0) root         (0)     2085 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/utils/TemplateBaseTool.py
+-rw-r--r--   0 root         (0) root         (0)     2533 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/utils/TemplateTool.py
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/utils/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1744 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/utils/inventory_tag.py
+-rw-r--r--   0 root         (0) root         (0)    10473 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/utils/wework.py
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1331 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/lib/cli.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/test/
+-rw-r--r--   0 root         (0) root         (0)     1422 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/test/test_inventory_tag.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/zbxtool_cfomp.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      187 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/zbxtool_cfomp.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1085 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/zbxtool_cfomp.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/zbxtool_cfomp.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       42 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/zbxtool_cfomp.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)      299 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/zbxtool_cfomp.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        4 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/zbxtool_cfomp.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/zbxtool_cfomp.egg-info/zip-safe
+-rw-r--r--   0 root         (0) root         (0)     2096 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/.gitignore
+-rw-r--r--   0 root         (0) root         (0)     1061 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/CHANGELOG
+-rw-r--r--   0 root         (0) root         (0)     1351 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/Jenkinsfile
+-rw-r--r--   0 root         (0) root         (0)        8 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     4723 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/README.md
+-rw-r--r--   0 root         (0) root         (0)     5804 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/ip_range.json
+-rw-r--r--   0 root         (0) root         (0)      152 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/pytest.ini
+-rw-r--r--   0 root         (0) root         (0)      299 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/requirements.txt
+-rw-r--r--   0 root         (0) root         (0)      695 2022-12-12 10:24:33.000000 zbxtool-cfomp-0.9.9/setup.py
+-rw-r--r--   0 root         (0) root         (0)      187 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)       38 2022-12-12 10:24:53.000000 zbxtool-cfomp-0.9.9/setup.cfg
```

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/discovery.py` & `zbxtool-cfomp-0.9.9/lib/commands/discovery.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/es_index_zbxhost.py` & `zbxtool-cfomp-0.9.9/lib/commands/es_index_zbxhost.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/fs_calc.py` & `zbxtool-cfomp-0.9.9/lib/commands/fs_calc.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/gen_analaysis_report.py` & `zbxtool-cfomp-0.9.9/lib/commands/gen_analaysis_report.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/hostgrp_aggr_item.py` & `zbxtool-cfomp-0.9.9/lib/commands/hostgrp_aggr_item.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/hosttpl.py` & `zbxtool-cfomp-0.9.9/lib/commands/hosttpl.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/inventory_supplementary.py` & `zbxtool-cfomp-0.9.9/lib/commands/inventory_supplementary.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/ldap_usergrp.py` & `zbxtool-cfomp-0.9.9/lib/commands/ldap_usergrp.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/multi_interfaces.py` & `zbxtool-cfomp-0.9.9/lib/commands/multi_interfaces.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/oob.py` & `zbxtool-cfomp-0.9.9/lib/commands/oob.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/send_to_all_users.py` & `zbxtool-cfomp-0.9.9/lib/commands/send_to_all_users.py`

 * *Files 2% similar despite different names*

```diff
@@ -25,15 +25,15 @@
             4. 再比对 "send to users" 列表和根据 Media 名称获取的用户列表；
             5. 最后追加不在原有 "send to users" 列表里的用户信息。
     :param zapi:
     :param media_name:
     :param action_name:
     :return:
     """
-    zapi.login(user="zhanggao", password="zhanggao711A")
+
     medias = zapi.mediatype.get(
         {
             "filter": {"name": media_name},
             "selectUsers": ["userid"],
             "output": ["users"]
         }
     )
```

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/service_tree.py` & `zbxtool-cfomp-0.9.9/lib/commands/service_tree.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/sync_wework_media.py` & `zbxtool-cfomp-0.9.9/lib/commands/sync_wework_media.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/update_hostgrp_poc.py` & `zbxtool-cfomp-0.9.9/lib/commands/update_hostgrp_poc.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/update_hostname.py` & `zbxtool-cfomp-0.9.9/lib/commands/update_hostname.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/commands/vmware_host_inventory.py` & `zbxtool-cfomp-0.9.9/lib/commands/vmware_host_inventory.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/utils/LdapTool.py` & `zbxtool-cfomp-0.9.9/lib/utils/LdapTool.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/utils/TemplateBaseTool.py` & `zbxtool-cfomp-0.9.9/lib/utils/TemplateBaseTool.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/utils/TemplateTool.py` & `zbxtool-cfomp-0.9.9/lib/utils/TemplateTool.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/utils/inventory_tag.py` & `zbxtool-cfomp-0.9.9/lib/utils/inventory_tag.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/utils/wework.py` & `zbxtool-cfomp-0.9.9/lib/utils/wework.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/lib/cli.py` & `zbxtool-cfomp-0.9.9/lib/cli.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/test/test_inventory_tag.py` & `zbxtool-cfomp-0.9.9/test/test_inventory_tag.py`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/zbxtool_cfomp.egg-info/SOURCES.txt` & `zbxtool-cfomp-0.9.9/zbxtool_cfomp.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/.gitignore` & `zbxtool-cfomp-0.9.9/.gitignore`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/CHANGELOG` & `zbxtool-cfomp-0.9.9/CHANGELOG`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/Jenkinsfile` & `zbxtool-cfomp-0.9.9/Jenkinsfile`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/README.md` & `zbxtool-cfomp-0.9.9/README.md`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/ip_range.json` & `zbxtool-cfomp-0.9.9/ip_range.json`

 * *Files identical despite different names*

### Comparing `zbxtool-cfomp-0.9.8/setup.py` & `zbxtool-cfomp-0.9.9/setup.py`

 * *Files identical despite different names*

