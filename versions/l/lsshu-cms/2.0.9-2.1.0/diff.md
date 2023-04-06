# Comparing `tmp/lsshu-cms-2.0.9.tar.gz` & `tmp/lsshu-cms-2.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/lsshu-cms-2.0.9.tar", last modified: Mon Oct 31 02:23:24 2022, max compression
+gzip compressed data, was "lsshu-cms-2.1.0.tar", last modified: Thu Apr  6 10:00:32 2023, max compression
```

## Comparing `lsshu-cms-2.0.9.tar` & `lsshu-cms-2.1.0.tar`

### file list

```diff
@@ -1,54 +1,56 @@
-drwxr-xr-x   0 lsshu      (501) admin       (80)        0 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/
--rw-r--r--   0 lsshu      (501) admin       (80)    12447 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/PKG-INFO
--rw-r--r--   0 lsshu      (501) admin       (80)    12048 2022-10-31 01:27:24.000000 lsshu-cms-2.0.9/README.md
-drwxr-xr-x   0 lsshu      (501) admin       (80)        0 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/lsshu/
--rw-r--r--   0 lsshu      (501) admin       (80)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/__init__.py
--rw-r--r--   0 lsshu      (501) admin       (80)     2208 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/config-template.py
-drwxr-xr-x   0 lsshu      (501) admin       (80)        0 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/lsshu/demo/
--rw-r--r--   0 lsshu      (501) admin       (80)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/demo/__init__.py
--rw-r--r--   0 lsshu      (501) admin       (80)      147 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/demo/crud.py
--rw-r--r--   0 lsshu      (501) admin       (80)     4952 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/demo/main.py
--rw-r--r--   0 lsshu      (501) admin       (80)      428 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/demo/model.py
--rw-r--r--   0 lsshu      (501) admin       (80)      593 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/demo/schema.py
--rw-r--r--   0 lsshu      (501) admin       (80)      504 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/init-template.py
-drwxr-xr-x   0 lsshu      (501) admin       (80)        0 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/lsshu/internal/
--rw-r--r--   0 lsshu      (501) admin       (80)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/internal/__init__.py
--rw-r--r--   0 lsshu      (501) admin       (80)    19558 2022-10-24 08:14:51.000000 lsshu-cms-2.0.9/lsshu/internal/crud.py
--rw-r--r--   0 lsshu      (501) admin       (80)     1314 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/internal/db.py
--rw-r--r--   0 lsshu      (501) admin       (80)     2342 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/internal/depends.py
--rw-r--r--   0 lsshu      (501) admin       (80)     5640 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/internal/helpers.py
--rw-r--r--   0 lsshu      (501) admin       (80)     7640 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/internal/method.py
--rw-r--r--   0 lsshu      (501) admin       (80)     1829 2022-10-18 06:28:51.000000 lsshu-cms-2.0.9/lsshu/internal/model.py
--rw-r--r--   0 lsshu      (501) admin       (80)     1158 2022-10-24 08:14:42.000000 lsshu-cms-2.0.9/lsshu/internal/schema.py
-drwxr-xr-x   0 lsshu      (501) admin       (80)        0 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/lsshu/oauth/
--rw-r--r--   0 lsshu      (501) admin       (80)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/__init__.py
-drwxr-xr-x   0 lsshu      (501) admin       (80)        0 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/lsshu/oauth/annex/
--rw-r--r--   0 lsshu      (501) admin       (80)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/annex/__init__.py
--rw-r--r--   0 lsshu      (501) admin       (80)      169 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/annex/crud.py
--rw-r--r--   0 lsshu      (501) admin       (80)     5673 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/annex/main.py
--rw-r--r--   0 lsshu      (501) admin       (80)      798 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/annex/schema.py
--rw-r--r--   0 lsshu      (501) admin       (80)      498 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/main.py
--rw-r--r--   0 lsshu      (501) admin       (80)     3367 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/model.py
-drwxr-xr-x   0 lsshu      (501) admin       (80)        0 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/lsshu/oauth/permission/
--rw-r--r--   0 lsshu      (501) admin       (80)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/permission/__init__.py
--rw-r--r--   0 lsshu      (501) admin       (80)      199 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/permission/crud.py
--rw-r--r--   0 lsshu      (501) admin       (80)     9966 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/permission/main.py
--rw-r--r--   0 lsshu      (501) admin       (80)     1855 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/permission/schema.py
-drwxr-xr-x   0 lsshu      (501) admin       (80)        0 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/lsshu/oauth/role/
--rw-r--r--   0 lsshu      (501) admin       (80)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/role/__init__.py
--rw-r--r--   0 lsshu      (501) admin       (80)     1289 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/role/crud.py
--rw-r--r--   0 lsshu      (501) admin       (80)     5649 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/role/main.py
--rw-r--r--   0 lsshu      (501) admin       (80)      885 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/role/schema.py
-drwxr-xr-x   0 lsshu      (501) admin       (80)        0 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/lsshu/oauth/user/
--rw-r--r--   0 lsshu      (501) admin       (80)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/user/__init__.py
--rw-r--r--   0 lsshu      (501) admin       (80)     1197 2022-10-09 02:41:15.000000 lsshu-cms-2.0.9/lsshu/oauth/user/crud.py
--rw-r--r--   0 lsshu      (501) admin       (80)     9355 2022-10-31 01:41:49.000000 lsshu-cms-2.0.9/lsshu/oauth/user/main.py
--rw-r--r--   0 lsshu      (501) admin       (80)     2500 2022-10-14 06:56:58.000000 lsshu-cms-2.0.9/lsshu/oauth/user/schema.py
-drwxr-xr-x   0 lsshu      (501) admin       (80)        0 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/lsshu_cms.egg-info/
--rw-r--r--   0 lsshu      (501) admin       (80)    12447 2022-10-31 02:23:23.000000 lsshu-cms-2.0.9/lsshu_cms.egg-info/PKG-INFO
--rw-r--r--   0 lsshu      (501) admin       (80)     1064 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/lsshu_cms.egg-info/SOURCES.txt
--rw-r--r--   0 lsshu      (501) admin       (80)        1 2022-10-31 02:23:23.000000 lsshu-cms-2.0.9/lsshu_cms.egg-info/dependency_links.txt
--rw-r--r--   0 lsshu      (501) admin       (80)      135 2022-10-31 02:23:23.000000 lsshu-cms-2.0.9/lsshu_cms.egg-info/requires.txt
--rw-r--r--   0 lsshu      (501) admin       (80)        6 2022-10-31 02:23:23.000000 lsshu-cms-2.0.9/lsshu_cms.egg-info/top_level.txt
--rw-r--r--   0 lsshu      (501) admin       (80)       38 2022-10-31 02:23:24.000000 lsshu-cms-2.0.9/setup.cfg
--rw-r--r--   0 lsshu      (501) admin       (80)      982 2022-10-31 02:14:38.000000 lsshu-cms-2.0.9/setup.py
+drwxr-xr-x   0 ke         (501) wheel        (0)        0 2023-04-06 10:00:32.974353 lsshu-cms-2.1.0/
+-rw-r--r--   0 ke         (501) wheel        (0)    12447 2023-04-06 10:00:32.974181 lsshu-cms-2.1.0/PKG-INFO
+-rw-r--r--   0 ke         (501) wheel        (0)    12048 2023-04-06 09:44:18.000000 lsshu-cms-2.1.0/README.md
+drwxr-xr-x   0 ke         (501) wheel        (0)        0 2023-04-06 10:00:32.967853 lsshu-cms-2.1.0/lsshu/
+-rw-r--r--   0 ke         (501) wheel        (0)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/__init__.py
+-rw-r--r--   0 ke         (501) wheel        (0)     2208 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/config-template.py
+drwxr-xr-x   0 ke         (501) wheel        (0)        0 2023-04-06 10:00:32.968583 lsshu-cms-2.1.0/lsshu/demo/
+-rw-r--r--   0 ke         (501) wheel        (0)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/demo/__init__.py
+-rw-r--r--   0 ke         (501) wheel        (0)      147 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/demo/crud.py
+-rw-r--r--   0 ke         (501) wheel        (0)     4952 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/demo/main.py
+-rw-r--r--   0 ke         (501) wheel        (0)      428 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/demo/model.py
+-rw-r--r--   0 ke         (501) wheel        (0)      593 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/demo/schema.py
+-rw-r--r--   0 ke         (501) wheel        (0)      504 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/init-template.py
+drwxr-xr-x   0 ke         (501) wheel        (0)        0 2023-04-06 10:00:32.970404 lsshu-cms-2.1.0/lsshu/internal/
+-rw-r--r--   0 ke         (501) wheel        (0)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/internal/__init__.py
+-rw-r--r--   0 ke         (501) wheel        (0)    20195 2023-04-06 07:26:24.000000 lsshu-cms-2.1.0/lsshu/internal/crud.py
+-rw-r--r--   0 ke         (501) wheel        (0)     1314 2023-01-31 04:02:21.000000 lsshu-cms-2.1.0/lsshu/internal/db.py
+-rw-r--r--   0 ke         (501) wheel        (0)     3369 2023-03-21 06:12:11.000000 lsshu-cms-2.1.0/lsshu/internal/depends.py
+-rw-r--r--   0 ke         (501) wheel        (0)     5686 2022-11-22 07:14:07.000000 lsshu-cms-2.1.0/lsshu/internal/helpers.py
+-rw-r--r--   0 ke         (501) wheel        (0)     7640 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/internal/method.py
+-rw-r--r--   0 ke         (501) wheel        (0)     1829 2022-10-18 06:28:51.000000 lsshu-cms-2.1.0/lsshu/internal/model.py
+-rw-r--r--   0 ke         (501) wheel        (0)     5758 2022-12-12 08:49:30.000000 lsshu-cms-2.1.0/lsshu/internal/redis.py
+-rw-r--r--   0 ke         (501) wheel        (0)     1466 2023-04-02 07:34:20.000000 lsshu-cms-2.1.0/lsshu/internal/schema.py
+-rw-r--r--   0 ke         (501) wheel        (0)     2940 2022-12-12 09:30:03.000000 lsshu-cms-2.1.0/lsshu/internal/socket.py
+drwxr-xr-x   0 ke         (501) wheel        (0)        0 2023-04-06 10:00:32.970834 lsshu-cms-2.1.0/lsshu/oauth/
+-rw-r--r--   0 ke         (501) wheel        (0)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/oauth/__init__.py
+drwxr-xr-x   0 ke         (501) wheel        (0)        0 2023-04-06 10:00:32.971414 lsshu-cms-2.1.0/lsshu/oauth/annex/
+-rw-r--r--   0 ke         (501) wheel        (0)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/oauth/annex/__init__.py
+-rw-r--r--   0 ke         (501) wheel        (0)      169 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/oauth/annex/crud.py
+-rw-r--r--   0 ke         (501) wheel        (0)     5673 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/oauth/annex/main.py
+-rw-r--r--   0 ke         (501) wheel        (0)      798 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/oauth/annex/schema.py
+-rw-r--r--   0 ke         (501) wheel        (0)      498 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/oauth/main.py
+-rw-r--r--   0 ke         (501) wheel        (0)     3425 2023-04-06 07:32:23.000000 lsshu-cms-2.1.0/lsshu/oauth/model.py
+drwxr-xr-x   0 ke         (501) wheel        (0)        0 2023-04-06 10:00:32.972098 lsshu-cms-2.1.0/lsshu/oauth/permission/
+-rw-r--r--   0 ke         (501) wheel        (0)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/oauth/permission/__init__.py
+-rw-r--r--   0 ke         (501) wheel        (0)      199 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/oauth/permission/crud.py
+-rw-r--r--   0 ke         (501) wheel        (0)     9966 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/oauth/permission/main.py
+-rw-r--r--   0 ke         (501) wheel        (0)     2020 2022-11-16 02:33:09.000000 lsshu-cms-2.1.0/lsshu/oauth/permission/schema.py
+drwxr-xr-x   0 ke         (501) wheel        (0)        0 2023-04-06 10:00:32.972612 lsshu-cms-2.1.0/lsshu/oauth/role/
+-rw-r--r--   0 ke         (501) wheel        (0)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/oauth/role/__init__.py
+-rw-r--r--   0 ke         (501) wheel        (0)     1289 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/oauth/role/crud.py
+-rw-r--r--   0 ke         (501) wheel        (0)     5649 2022-11-16 02:31:15.000000 lsshu-cms-2.1.0/lsshu/oauth/role/main.py
+-rw-r--r--   0 ke         (501) wheel        (0)      893 2022-11-16 02:33:21.000000 lsshu-cms-2.1.0/lsshu/oauth/role/schema.py
+drwxr-xr-x   0 ke         (501) wheel        (0)        0 2023-04-06 10:00:32.973310 lsshu-cms-2.1.0/lsshu/oauth/user/
+-rw-r--r--   0 ke         (501) wheel        (0)        0 2022-10-09 02:41:15.000000 lsshu-cms-2.1.0/lsshu/oauth/user/__init__.py
+-rw-r--r--   0 ke         (501) wheel        (0)     1355 2023-04-06 07:41:33.000000 lsshu-cms-2.1.0/lsshu/oauth/user/crud.py
+-rw-r--r--   0 ke         (501) wheel        (0)    10286 2023-04-06 07:23:34.000000 lsshu-cms-2.1.0/lsshu/oauth/user/main.py
+-rw-r--r--   0 ke         (501) wheel        (0)     2977 2023-04-06 07:28:28.000000 lsshu-cms-2.1.0/lsshu/oauth/user/schema.py
+drwxr-xr-x   0 ke         (501) wheel        (0)        0 2023-04-06 10:00:32.974000 lsshu-cms-2.1.0/lsshu_cms.egg-info/
+-rw-r--r--   0 ke         (501) wheel        (0)    12447 2023-04-06 10:00:32.000000 lsshu-cms-2.1.0/lsshu_cms.egg-info/PKG-INFO
+-rw-r--r--   0 ke         (501) wheel        (0)     1113 2023-04-06 10:00:32.000000 lsshu-cms-2.1.0/lsshu_cms.egg-info/SOURCES.txt
+-rw-r--r--   0 ke         (501) wheel        (0)        1 2023-04-06 10:00:32.000000 lsshu-cms-2.1.0/lsshu_cms.egg-info/dependency_links.txt
+-rw-r--r--   0 ke         (501) wheel        (0)      174 2023-04-06 10:00:32.000000 lsshu-cms-2.1.0/lsshu_cms.egg-info/requires.txt
+-rw-r--r--   0 ke         (501) wheel        (0)        6 2023-04-06 10:00:32.000000 lsshu-cms-2.1.0/lsshu_cms.egg-info/top_level.txt
+-rw-r--r--   0 ke         (501) wheel        (0)       38 2023-04-06 10:00:32.974394 lsshu-cms-2.1.0/setup.cfg
+-rw-r--r--   0 ke         (501) wheel        (0)     1199 2023-04-06 09:54:48.000000 lsshu-cms-2.1.0/setup.py
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `lsshu-cms-2.0.9/PKG-INFO` & `lsshu-cms-2.1.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 Metadata-Version: 2.1
 Name: lsshu-cms
-Version: 2.0.9
+Version: 2.1.0
 Summary: FastAPI 开发的CMS
 Home-page: https://github.com/lsshu/fastapi-cms
 Author: Lsshu
 Author-email: admin@lsshu.cn
 License: GPLv3
-Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Development Status :: 3 - Alpha
-Requires-Python: >=3.8
+Requires-Python: >=3.9
 Description-Content-Type: text/markdown
 
 # Lsshu 
 _admin@lsshu.cn_
 
 ## 安装
 ```shell
```

### Comparing `lsshu-cms-2.0.9/README.md` & `lsshu-cms-2.1.0/README.md`

 * *Files identical despite different names*

### Comparing `lsshu-cms-2.0.9/lsshu/config-template.py` & `lsshu-cms-2.1.0/lsshu/config-template.py`

 * *Files identical despite different names*

### Comparing `lsshu-cms-2.0.9/lsshu/demo/main.py` & `lsshu-cms-2.1.0/lsshu/demo/main.py`

 * *Files identical despite different names*

### Comparing `lsshu-cms-2.0.9/lsshu/demo/schema.py` & `lsshu-cms-2.1.0/lsshu/demo/schema.py`

 * *Files identical despite different names*

### Comparing `lsshu-cms-2.0.9/lsshu/internal/crud.py` & `lsshu-cms-2.1.0/lsshu/internal/crud.py`

 * *Files 5% similar despite different names*

```diff
@@ -193,15 +193,15 @@
             for (relation, relation_class) in cls.params_relationship.items():
                 _obj = cls.first(db=db, **kwargs)
                 if hasattr(item, relation) and bool(getattr(item, relation)):
                     _relation = BaseCRUD.all(db=db, model=relation_class, where=(
                         "id", 'in_', getattr(item, relation)))
                     setattr(_obj, relation, _relation)
                     db.add(_obj), db.commit(), db.close()
-                elif hasattr(item, relation):
+                elif hasattr(item, relation) and relation in item.dict(exclude_unset=True):
                     [getattr(_obj, relation).remove(rela) for rela in getattr(_obj, relation)]
                 delattr(item, relation)
         return item
 
     @classmethod
     def delete(cls, **kwargs):
         """
@@ -326,75 +326,90 @@
         :param where:
         :param model:
         :return:
         """
         query = cls.params_query
         params_model = cls.params_model if not model else model
         if bool(where) and (type(where) == tuple or type(where) == list):
-            if len(where) == 2:
-                """('content', '西')"""
-                query = query.filter(getattr(params_model, where[0]) == where[1])
-            elif len(where) == 3:
-                if where[1] == "==" or where[1] == "=" or where[1] == "eq":
-                    """('content', '==', '西')"""
-                    query = query.filter(getattr(params_model, where[0]) == where[2])
-                elif where[1] == "!=" or where[1] == "<>" or where[1] == "><" or where[1] == "neq" or where[1] == "ne":
-                    """('content', '!=', '西')"""
-                    query = query.filter(getattr(params_model, where[0]) != where[2])
-                elif where[1] == ">" or where[1] == "gt":
-                    """('content', '>', '西')"""
-                    query = query.filter(getattr(params_model, where[0]) > where[2])
-                elif where[1] == ">=" or where[1] == "ge":
-                    """('content', '>=', '西')"""
-                    query = query.filter(getattr(params_model, where[0]) >= where[2])
-                elif where[1] == "<" or where[1] == "lt":
-                    """('content', '<', '西')"""
-                    query = query.filter(getattr(params_model, where[0]) < where[2])
-                elif where[1] == "<=" or where[1] == "le":
-                    """('content', '<=', '西')"""
-                    query = query.filter(getattr(params_model, where[0]) <= where[2])
-                elif where[1] in ["like", "ilike"]:
-                    if not where[2] is None:
-                        """('content', 'like', '西')"""
-                        query = query.filter(
-                            getattr(getattr(params_model, where[0]), where[1])("%" + where[2] + "%")
-                        )
-                elif where[1] in ["or"]:
-                    if type(where[0]) == tuple or type(where[0]) == list:
-                        """(['name','content'], 'or', '西')"""
-                        _filters = [(getattr(params_model, fil) == where[2]) for fil in where[0]]
-                        query = query.filter(or_(*_filters))
-
-                    if type(where[0]) == str and (type(where[2]) == tuple or type(where[2]) == list):
-                        """('name', 'or', ['西', '西'])"""
-                        _filters = [(getattr(params_model, where[0]) == fil) for fil in where[2]]
-                        query = query.filter(or_(*_filters))
-                elif where[1] in ["or_like", "or_ilike"]:
-                    if type(where[0]) == tuple or type(where[0]) == list:
-                        """(['name','content'], 'or_like', '西')"""
-                        _filters = [(getattr(getattr(params_model, fil), where[1][3:])("%" + where[2] + "%")) for
-                                    fil in
-                                    where[0]]
-                        query = query.filter(or_(*_filters))
-                    if type(where[0]) == str and (type(where[2]) == tuple or type(where[2]) == list):
-                        """('name', 'or_like', ['西', '西'])"""
-                        _filters = [(getattr(getattr(params_model, where[0]), where[1][3:])("%" + fil + "%")) for
-                                    fil in
-                                    where[2]]
-                        query = query.filter(or_(*_filters))
-                elif where[1] in ["between"] and type(where[2]) in [list, tuple] and len(where[2]) == 2:
-                    query = query.filter(getattr(getattr(params_model, where[0]), where[1])(where[2][0], where[2][1]))
-                elif where[1] in ["in"] and type(where[2]) in [list, tuple]:
-                    query = query.filter(getattr(getattr(params_model, where[0]), "in_")(where[2]))
-                else:
-                    query = query.filter(getattr(getattr(params_model, where[0]), where[1])(where[2]))
+            if len(where) == 2 and (type(where[0]) is list or type(where[0]) is tuple) and where[1] == "or":
+                """([('content',"==", '东'),('content','==', '西')], 'or')"""
+                _filters = [cls.filter_item(params_model, fil) for fil in where[0]]
+                query = query.filter(or_(*_filters))
+            else:
+                query = query.filter(cls.filter_item(params_model, where))
         cls.params_query = query
         return cls
 
     @classmethod
+    def filter_item(cls, model, where):
+        if len(where) == 2:
+            """('content', '西')"""
+            if type(where[0]) is str:
+                return getattr(model, where[0]) == where[1]
+        elif len(where) == 3:
+            if where[1] == "==" or where[1] == "=" or where[1] == "eq":
+                """('content', '==', '西')"""
+                return getattr(model, where[0]) == where[2]
+            elif where[1] == "!=" or where[1] == "<>" or where[1] == "><" or where[1] == "neq" or where[1] == "ne":
+                """('content', '!=', '西')"""
+                return getattr(model, where[0]) != where[2]
+            elif where[1] == ">" or where[1] == "gt":
+                """('content', '>', '西')"""
+                return getattr(model, where[0]) > where[2]
+            elif where[1] == ">=" or where[1] == "ge":
+                """('content', '>=', '西')"""
+                return getattr(model, where[0]) >= where[2]
+            elif where[1] == "<" or where[1] == "lt":
+                """('content', '<', '西')"""
+                return getattr(model, where[0]) < where[2]
+            elif where[1] == "<=" or where[1] == "le":
+                """('content', '<=', '西')"""
+                return getattr(model, where[0]) <= where[2]
+            elif where[1] in ["like", "ilike"]:
+                if not where[2] is None:
+                    """('content', 'like', '西')"""
+                    return getattr(getattr(model, where[0]), where[1])("%" + where[2] + "%")
+            elif where[1] in ["or"]:
+                if type(where[0]) == tuple or type(where[0]) == list:
+                    """(['name','content'], 'or', '西')"""
+                    _filters = [(getattr(model, fil) == where[2]) for fil in where[0]]
+                    return or_(*_filters)
+
+                if type(where[0]) == str and (type(where[2]) == tuple or type(where[2]) == list):
+                    """('name', 'or', ['西', '西'])"""
+                    _filters = [(getattr(model, where[0]) == fil) for fil in where[2]]
+                    return or_(*_filters)
+            elif where[1] in ["or_like", "or_ilike"]:
+                if type(where[0]) == tuple or type(where[0]) == list:
+                    """(['name','content'], 'or_like', '西')"""
+                    _filters = [(getattr(getattr(model, fil), where[1][3:])("%" + where[2] + "%")) for
+                                fil in
+                                where[0]]
+                    return or_(*_filters)
+                if type(where[0]) == str and (type(where[2]) == tuple or type(where[2]) == list):
+                    """('name', 'or_like', ['西', '西'])"""
+                    _filters = [(getattr(getattr(model, where[0]), where[1][3:])("%" + fil + "%")) for
+                                fil in
+                                where[2]]
+                    return or_(*_filters)
+            elif where[1] in ["between"] and type(where[2]) in [list, tuple] and len(where[2]) == 2:
+                return getattr(getattr(model, where[0]), where[1])(where[2][0], where[2][1])
+            elif where[1] in ["datebetween"] and type(where[2]) in [list, tuple] and len(where[2]) == 2:
+                return getattr(getattr(model, where[0]), 'between')(where[2][0], where[2][1])
+            elif where[1] in ["datetimebetween"] and type(where[2]) in [list, tuple] and len(where[2]) == 2:
+                return getattr(getattr(model, where[0]), 'between')("%s 00:00:00" % where[2][0], "%s 23:59:59" % where[2][1])
+            elif where[1] in ["in"] and type(where[2]) in [list, tuple]:
+                return getattr(getattr(model, where[0]), "in_")(where[2])
+            elif where[1] in ["notin"] and type(where[2]) in [list, tuple]:
+                return getattr(getattr(model, where[0]), "notin_")(where[2])
+            else:
+                return getattr(getattr(model, where[0]), where[1])(where[2])
+        return
+
+    @classmethod
     def order(cls, order: Union[List[tuple], List[list], Tuple[tuple], Tuple[list], list, tuple]):
         """
         排序
         :param order:
         :return:
         """
         if bool(order):
@@ -520,14 +535,16 @@
         """
         更新或者创建
         :param kwargs:
         :return:
         """
         instance = cls.first(**kwargs)
         if instance:
+            if "where" in kwargs:
+                del kwargs['where']
             return cls.update(**kwargs, pk=getattr(instance, cls.params_pk), exclude_unset=True)
         else:
             del kwargs['where']
             return cls.store(**kwargs)
 
     @classmethod
     def find_or_store_model(cls, **kwargs):
```

### Comparing `lsshu-cms-2.0.9/lsshu/internal/db.py` & `lsshu-cms-2.1.0/lsshu/internal/db.py`

 * *Files identical despite different names*

### Comparing `lsshu-cms-2.0.9/lsshu/internal/depends.py` & `lsshu-cms-2.1.0/lsshu/internal/depends.py`

 * *Files 19% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 from fastapi import Depends, Security
 from fastapi.security import SecurityScopes, OAuth2PasswordBearer
 from sqlalchemy.orm import Session
 
 from config import OAUTH_TOKEN_URL, OAUTH_TOKEN_SCOPES, OAUTH_SECRET_KEY, OAUTH_ALGORITHM, OAUTH_LOGIN_SCOPES
 from lsshu.internal.db import dbs
 from lsshu.internal.helpers import token_payload
-from lsshu.internal.schema import ModelScreenParams
+from lsshu.internal.schema import ModelScreenParams, ModelScreenParamsForAll
 from lsshu.oauth.user.crud import CRUDOAuthUser
 from lsshu.oauth.user.schema import SchemasOAuthUser, SchemasOAuthScopes
 
 
 def model_screen_params(page: Optional[int] = 1, limit: Optional[int] = 25, quest_data: Optional[str] = None):
     """列表筛选参数"""
     order, where = [], []
@@ -24,16 +24,34 @@
 
 
 def model_post_screen_params(data: ModelScreenParams = None):
     """列表筛选参数"""
     order = []
     [order.extend(list(s.items())) for s in data.order]
     data.order = order
-    where = [(w['key'], w['condition'], w['value']) for w in data.where if 'value' in w and (w['value'] or w['value'] is False or w['value'] is 0)]
+    where = [(w['key'], w['condition'], w['value']) for w in data.where if
+             ('value' in w and (w['value'] or w['value'] is False or w['value'] == 0)) and (not "join" in w or "join" in w and not w['join'])]
+    join = [(w['join'], [(w['key'], w['condition'], w['value'])], 'join') for w in data.where if
+            ('value' in w and (w['value'] or w['value'] is False or w['value'] == 0)) and ("join" in w and w['join'])]
     data.where = where
+    data.join = join
+    return data
+
+
+def model_post_screen_params_for_all(data: ModelScreenParamsForAll = None):
+    """列表筛选参数"""
+    order = []
+    [order.extend(list(s.items())) for s in data.order]
+    data.order = order
+    where = [(w['key'], w['condition'], w['value']) for w in data.where if
+             ('value' in w and (w['value'] or w['value'] is False or w['value'] == 0)) and (not "join" in w or "join" in w and not w['join'])]
+    join = [(w['join'], [(w['key'], w['condition'], w['value'])], 'join') for w in data.where if
+            ('value' in w and (w['value'] or w['value'] is False or w['value'] == 0)) and ("join" in w and w['join'])]
+    data.where = where
+    data.join = join
     return data
 
 
 oauth2_scheme = OAuth2PasswordBearer(tokenUrl=OAUTH_TOKEN_URL, scopes=OAUTH_TOKEN_SCOPES)
 
 
 async def current_user_security(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
```

### Comparing `lsshu-cms-2.0.9/lsshu/internal/helpers.py` & `lsshu-cms-2.1.0/lsshu/internal/helpers.py`

 * *Files 2% similar despite different names*

```diff
@@ -30,15 +30,15 @@
     :param algorithm: 加密 算法
     :param expires_delta: 有效期 类型 timedelta
     :return: token
     """
     from datetime import datetime, timedelta
     from jose import jwt
     to_encode = data.copy()
-    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
+    expire = datetime.now() + (expires_delta if expires_delta else timedelta(minutes=15))
     to_encode.update({"exp": expire})
     encoded_jwt = jwt.encode(claims=to_encode, key=key, algorithm=algorithm)
     return encoded_jwt
 
 
 def token_payload(security_scopes, token, key, algorithm):
     """
@@ -102,14 +102,15 @@
     from lsshu.oauth.permission.schema import SchemasOAuthPermissionStoreUpdate
     ACTION_ITEMS = [
         {"name": "列表", "scope": "list"},
         {"name": "详情", "scope": "get"},
         {"name": "创建", "scope": "store"},
         {"name": "更新", "scope": "update"},
         {"name": "删除", "scope": "delete"},
+        {"name": "导出", "scope": "download"},
     ]
     if not db:
         from lsshu.internal.db import SessionLocal
         db = SessionLocal()
     for permission in permissions:
         _scope = permission.get('scope')
         _name = permission.get('name')
```

### Comparing `lsshu-cms-2.0.9/lsshu/internal/method.py` & `lsshu-cms-2.1.0/lsshu/internal/method.py`

 * *Files identical despite different names*

### Comparing `lsshu-cms-2.0.9/lsshu/internal/model.py` & `lsshu-cms-2.1.0/lsshu/internal/model.py`

 * *Files identical despite different names*

### Comparing `lsshu-cms-2.0.9/lsshu/oauth/annex/main.py` & `lsshu-cms-2.1.0/lsshu/oauth/annex/main.py`

 * *Files identical despite different names*

### Comparing `lsshu-cms-2.0.9/lsshu/oauth/annex/schema.py` & `lsshu-cms-2.1.0/lsshu/oauth/annex/schema.py`

 * *Files identical despite different names*

### Comparing `lsshu-cms-2.0.9/lsshu/oauth/model.py` & `lsshu-cms-2.1.0/lsshu/oauth/model.py`

 * *Files 5% similar despite different names*

```diff
@@ -42,14 +42,15 @@
     ))
     roles = relationship('ModelOAuthRoles', backref='auth_users', secondary=Table(
         "%s_user_has_roles" % _table_name,
         Model.metadata,
         Column('rol_id', Integer, ForeignKey("%s.id" % role_table_name), primary_key=True, comment="角色"),
         Column('use_id', Integer, ForeignKey("%s.id" % user_table_name), primary_key=True, comment="用户"),
     ))
+    sort = Column(Integer, default=999, comment="排序")
 
 
 class ModelOAuthRoles(_ModelOAuthRoles):
     """角色"""
     __tablename__ = role_table_name
     permissions = relationship('ModelOAuthPermissions', backref='roles', lazy="joined", secondary=Table(
         "%s_role_has_permissions" % _table_name,
```

### Comparing `lsshu-cms-2.0.9/lsshu/oauth/permission/main.py` & `lsshu-cms-2.1.0/lsshu/oauth/permission/main.py`

 * *Files identical despite different names*

### Comparing `lsshu-cms-2.0.9/lsshu/oauth/permission/schema.py` & `lsshu-cms-2.1.0/lsshu/oauth/permission/schema.py`

 * *Files 8% similar despite different names*

```diff
@@ -19,14 +19,23 @@
     created_at: Optional[datetime] = None
     updated_at: Optional[datetime] = None
 
     class Config:
         orm_mode = True
 
 
+class SchemasOAuthPermissionThinResponse(BaseModel):
+    """权限 返回"""
+    id: int
+    name: Optional[str] = None
+
+    class Config:
+        orm_mode = True
+
+
 class SchemasOAuthPermissionPaginateItem(SchemasPaginate):
     items: List[SchemasOAuthPermissionResponse]
 
 
 class SchemasOAuthPermissionStoreUpdate(BaseModel):
     """授权角色 提交"""
     name: Optional[str] = None
```

### Comparing `lsshu-cms-2.0.9/lsshu/oauth/role/crud.py` & `lsshu-cms-2.1.0/lsshu/oauth/role/crud.py`

 * *Files identical despite different names*

### Comparing `lsshu-cms-2.0.9/lsshu/oauth/role/main.py` & `lsshu-cms-2.1.0/lsshu/oauth/role/main.py`

 * *Files identical despite different names*

### Comparing `lsshu-cms-2.0.9/lsshu/oauth/role/schema.py` & `lsshu-cms-2.1.0/lsshu/oauth/role/schema.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,20 +1,20 @@
 from datetime import datetime
 from typing import Optional, List
 from pydantic import BaseModel
 
 from lsshu.internal.schema import SchemasPaginate
-from lsshu.oauth.permission.schema import SchemasOAuthPermissionResponse
+from lsshu.oauth.permission.schema import SchemasOAuthPermissionThinResponse
 
 
 class SchemasOAuthRoleResponse(BaseModel):
     """角色 返回"""
     id: int
     name: Optional[str] = None
-    permissions: Optional[List[SchemasOAuthPermissionResponse]] = None
+    permissions: Optional[List[SchemasOAuthPermissionThinResponse]] = None
     created_at: Optional[datetime] = None
     updated_at: Optional[datetime] = None
 
     class Config:
         orm_mode = True
```

### Comparing `lsshu-cms-2.0.9/lsshu/oauth/user/crud.py` & `lsshu-cms-2.1.0/lsshu/oauth/user/crud.py`

 * *Files 24% similar despite different names*

```diff
@@ -24,8 +24,15 @@
     def update(cls, db: Session, pk: int, item: SchemasOAuthUserStoreUpdate, **kwargs):
         if hasattr(item, "password") and item.password:
             item.password = token_get_password_hash(item.password)
         else:
             if hasattr(item, "password"):
                 delattr(item, "password")
 
-        return super(CRUDOAuthUser, cls).update(db=db, pk=pk, item=item, **kwargs)
+        return super(CRUDOAuthUser, cls).update(db=db, pk=pk, item=item, **kwargs)
+
+    @classmethod
+    def all(cls, **kwargs):
+        kwargs.update({
+            "order": [("sort", "asc")]
+        })
+        return super().all(**kwargs)
```

### Comparing `lsshu-cms-2.0.9/lsshu/oauth/user/main.py` & `lsshu-cms-2.1.0/lsshu/oauth/user/main.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from typing import List
+from typing import List, Optional
 
 from fastapi import APIRouter, Depends, Security, HTTPException, status
 from fastapi.security import OAuth2PasswordRequestForm
 from sqlalchemy.orm import Session
 
 from config import OAUTH_DEFAULT_TAGS, OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES, OAUTH_LOGIN_SCOPES, OAUTH_ADMIN_USERS, OAUTH_SECRET_KEY, OAUTH_ALGORITHM, \
     OAUTH_TOKEN_URI, OAUTH_SCOPES_URI, OAUTH_ME_URI
@@ -67,29 +67,55 @@
         data={"sub": user.username, "user_id": user.id, "scopes": list(set(scopes))},
         key=OAUTH_SECRET_KEY,
         algorithm=OAUTH_ALGORITHM,
         expires_delta=access_token_expires
     )
 
 
+from fastapi.param_functions import Form
+
+
+class _OAuth2PasswordRequestForm(OAuth2PasswordRequestForm):
+    def __init__(
+            self,
+            grant_type: str = Form(default=None, regex="password"),
+            username: str = Form(),
+            password: str = Form(),
+            scope: str = Form(default=""),
+            client_id: Optional[str] = Form(default=None),
+            client_secret: Optional[str] = Form(default=None),
+            verification_username: Optional[str] = Form(default=None),
+            verification_code: Optional[str] = Form(default=None),
+    ):
+        self.grant_type = grant_type
+        self.username = username
+        self.password = password
+        self.scopes = scope.split()
+        self.client_id = client_id
+        self.client_secret = client_secret
+        self.verification_username = verification_username
+        self.verification_code = verification_code
+
+
 @router.post(OAUTH_TOKEN_URI)
-async def login_for_access_token(db: Session = Depends(dbs), form_data: OAuth2PasswordRequestForm = Depends()):
+async def login_for_access_token(db: Session = Depends(dbs), form_data: _OAuth2PasswordRequestForm = Depends()):
     """
     获取登录授权:
     - **form_data**: 登录数据
     """
     access_token = token_authenticate_access_token(
         db=db,
         username=form_data.username,
         password=form_data.password,
         scopes=form_data.scopes
     )
     return SchemasLoginResponse(data=SchemasLogin(access_token=access_token, token_type="bearer"))
 
 
+
 @router.get(OAUTH_SCOPES_URI)
 async def get_scopes(auth: SchemasOAuthScopes = Security(auth_user)):
     """
     获取登录授权:
     """
     return SchemasOAuthUserMeStatusResponse(data={"user": auth.user, "scopes": auth.scopes})
```

### Comparing `lsshu-cms-2.0.9/lsshu/oauth/user/schema.py` & `lsshu-cms-2.1.0/lsshu/oauth/user/schema.py`

 * *Files 21% similar despite different names*

```diff
@@ -4,22 +4,36 @@
 from pydantic import BaseModel
 
 from lsshu.internal.schema import Schemas, SchemasPaginate
 from lsshu.oauth.permission.schema import SchemasOAuthPermissionResponse
 from lsshu.oauth.role.schema import SchemasOAuthRoleResponse
 
 
+class SchemasOAuthRole(BaseModel):
+    """角色 返回"""
+    id: int
+    name: Optional[str] = None
+    created_at: Optional[datetime] = None
+    updated_at: Optional[datetime] = None
+
+    class Config:
+        orm_mode = True
+
+
 class SchemasOAuthUserResponse(BaseModel):
     """授权用户 返回"""
     id: int
     username: Optional[str] = None
     user_phone: Optional[str] = None
     permissions: Optional[List[SchemasOAuthPermissionResponse]] = None
-    roles: Optional[List[SchemasOAuthRoleResponse]] = None
+    roles: Optional[List[SchemasOAuthRole]] = None
     available: Optional[bool] = True
+    remarks: Optional[str] = None  # 备注
+    sort: Optional[int] = None  # 排序
+    status: Optional[bool] = None  # 状态
     created_at: Optional[datetime] = None
     updated_at: Optional[datetime] = None
 
     class Config:
         orm_mode = True
 
 
@@ -63,14 +77,18 @@
     username: Optional[str] = None
     password: Optional[str] = None
     user_phone: Optional[str] = None
     available: Optional[bool] = True
     permissions: Optional[List[int]] = None
     roles: Optional[List[int]] = None
 
+    remarks: Optional[str] = None  # 备注
+    sort: Optional[int] = None  # 排序
+    status: Optional[bool] = None  # 状态
+
 
 class SchemasOAuthUser(BaseModel):
     """解析加密字段"""
     sub: Optional[str] = None
     user_id: Optional[int] = 0
     exp: Optional[int] = 0
     scopes: List[str] = []
@@ -80,16 +98,19 @@
     """验证授权后"""
     user: SchemasOAuthUserResponse
     scopes: List[str] = []
 
 
 class SchemasParams(BaseModel):
     """参数"""
-    roles: List[SchemasOAuthRoleResponse]
+    roles: List[SchemasOAuthRole]
     permissions: List[SchemasOAuthPermissionResponse]
 
 
 class SchemasOAuthUserMeUpdate(BaseModel):
     """授权用户修改自己信息 提交"""
     username: Optional[str] = None
     password: Optional[str] = None
     user_phone: Optional[str] = None
+
+
+
```

### Comparing `lsshu-cms-2.0.9/lsshu_cms.egg-info/PKG-INFO` & `lsshu-cms-2.1.0/lsshu_cms.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 Metadata-Version: 2.1
 Name: lsshu-cms
-Version: 2.0.9
+Version: 2.1.0
 Summary: FastAPI 开发的CMS
 Home-page: https://github.com/lsshu/fastapi-cms
 Author: Lsshu
 Author-email: admin@lsshu.cn
 License: GPLv3
-Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Development Status :: 3 - Alpha
-Requires-Python: >=3.8
+Requires-Python: >=3.9
 Description-Content-Type: text/markdown
 
 # Lsshu 
 _admin@lsshu.cn_
 
 ## 安装
 ```shell
```

### Comparing `lsshu-cms-2.0.9/lsshu_cms.egg-info/SOURCES.txt` & `lsshu-cms-2.1.0/lsshu_cms.egg-info/SOURCES.txt`

 * *Files 6% similar despite different names*

```diff
@@ -11,15 +11,17 @@
 lsshu/internal/__init__.py
 lsshu/internal/crud.py
 lsshu/internal/db.py
 lsshu/internal/depends.py
 lsshu/internal/helpers.py
 lsshu/internal/method.py
 lsshu/internal/model.py
+lsshu/internal/redis.py
 lsshu/internal/schema.py
+lsshu/internal/socket.py
 lsshu/oauth/__init__.py
 lsshu/oauth/main.py
 lsshu/oauth/model.py
 lsshu/oauth/annex/__init__.py
 lsshu/oauth/annex/crud.py
 lsshu/oauth/annex/main.py
 lsshu/oauth/annex/schema.py
```

### Comparing `lsshu-cms-2.0.9/setup.py` & `lsshu-cms-2.1.0/setup.py`

 * *Files 27% similar despite different names*

```diff
@@ -6,19 +6,40 @@
 @Project ：lsshu-cms
 """
 from setuptools import setup, find_packages
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
-setup(name="lsshu-cms", version="2.0.9", description="FastAPI 开发的CMS", python_requires=">=3.8",
-      author="Lsshu", author_email="admin@lsshu.cn", url="https://github.com/lsshu/fastapi-cms",
-      packages=find_packages(), long_description=long_description,
-      long_description_content_type="text/markdown", license="GPLv3",
+setup(name="lsshu-cms",
+      version="2.1.0",
+      description="FastAPI 开发的CMS",
+      python_requires=">=3.9",
+      author="Lsshu",
+      author_email="admin@lsshu.cn",
+      url="https://github.com/lsshu/fastapi-cms",
+      packages=find_packages(),
+      long_description=long_description,
+      long_description_content_type="text/markdown",
+      license="GPLv3",
       classifiers=[
-          "Programming Language :: Python :: 3.8",
+          "Programming Language :: Python :: 3.9",
           "License :: OSI Approved :: MIT License",
           "Development Status :: 3 - Alpha",
       ],
-      install_requires=["uvicorn[standard]", "fastapi", "sqlalchemy", "sqlalchemy_mptt", "python-multipart", "hashids", "passlib[bcrypt]", "python-jose[cryptography]", "Pillow",
-                        "PyMySQL"]
+      install_requires=[
+          "hashids",
+          "fastapi[all]",
+          "python-jose[cryptography]",
+          "passlib[bcrypt]",
+          "SQLAlchemy==1.4.46",
+          "Pillow",
+          "pymysql",
+          "sqlalchemy-mptt",
+          "user-agents",
+          "requests",
+          "openpyxl",
+          "aioredis",
+          "filetype",
+          "pycryptodome"
+      ]
       )
```

