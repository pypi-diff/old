# Comparing `tmp/ruiwen_data_all-1.0.1.tar.gz` & `tmp/ruiwen_data_all-1.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ruiwen_data_all-1.0.1.tar", last modified: Fri Apr  7 09:28:24 2023, max compression
+gzip compressed data, was "ruiwen_data_all-1.0.2.tar", last modified: Fri Apr  7 11:31:40 2023, max compression
```

## Comparing `ruiwen_data_all-1.0.1.tar` & `ruiwen_data_all-1.0.2.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxr-xr-x   0 xiaochuan   (501) staff       (20)        0 2023-04-07 09:28:24.111767 ruiwen_data_all-1.0.1/
--rw-r--r--   0 xiaochuan   (501) staff       (20)       59 2023-04-07 09:28:24.109751 ruiwen_data_all-1.0.1/PKG-INFO
--rw-r--r--   0 xiaochuan   (501) staff       (20)      546 2023-04-07 09:28:10.000000 ruiwen_data_all-1.0.1/pyproject.toml
-drwxr-xr-x   0 xiaochuan   (501) staff       (20)        0 2023-04-07 09:28:24.103923 ruiwen_data_all-1.0.1/ruiwen_data_all/
--rw-r--r--   0 xiaochuan   (501) staff       (20)    36692 2023-04-07 09:28:10.000000 ruiwen_data_all-1.0.1/ruiwen_data_all/__init__.py
-drwxr-xr-x   0 xiaochuan   (501) staff       (20)        0 2023-04-07 09:28:24.108270 ruiwen_data_all-1.0.1/ruiwen_data_all.egg-info/
--rw-r--r--   0 xiaochuan   (501) staff       (20)       59 2023-04-07 09:28:24.000000 ruiwen_data_all-1.0.1/ruiwen_data_all.egg-info/PKG-INFO
--rw-r--r--   0 xiaochuan   (501) staff       (20)      236 2023-04-07 09:28:24.000000 ruiwen_data_all-1.0.1/ruiwen_data_all.egg-info/SOURCES.txt
--rw-r--r--   0 xiaochuan   (501) staff       (20)        1 2023-04-07 09:28:24.000000 ruiwen_data_all-1.0.1/ruiwen_data_all.egg-info/dependency_links.txt
--rw-r--r--   0 xiaochuan   (501) staff       (20)       53 2023-04-07 09:28:24.000000 ruiwen_data_all-1.0.1/ruiwen_data_all.egg-info/requires.txt
--rw-r--r--   0 xiaochuan   (501) staff       (20)       16 2023-04-07 09:28:24.000000 ruiwen_data_all-1.0.1/ruiwen_data_all.egg-info/top_level.txt
--rw-r--r--   0 xiaochuan   (501) staff       (20)       38 2023-04-07 09:28:24.112663 ruiwen_data_all-1.0.1/setup.cfg
+drwxr-xr-x   0 xiaochuan   (501) staff       (20)        0 2023-04-07 11:31:40.150240 ruiwen_data_all-1.0.2/
+-rw-r--r--   0 xiaochuan   (501) staff       (20)       59 2023-04-07 11:31:40.149146 ruiwen_data_all-1.0.2/PKG-INFO
+-rw-r--r--   0 xiaochuan   (501) staff       (20)      673 2023-04-07 11:31:28.000000 ruiwen_data_all-1.0.2/pyproject.toml
+drwxr-xr-x   0 xiaochuan   (501) staff       (20)        0 2023-04-07 11:31:40.139846 ruiwen_data_all-1.0.2/ruiwen_data_all/
+-rw-r--r--   0 xiaochuan   (501) staff       (20)    36688 2023-04-07 11:31:28.000000 ruiwen_data_all-1.0.2/ruiwen_data_all/__init__.py
+drwxr-xr-x   0 xiaochuan   (501) staff       (20)        0 2023-04-07 11:31:40.146010 ruiwen_data_all-1.0.2/ruiwen_data_all.egg-info/
+-rw-r--r--   0 xiaochuan   (501) staff       (20)       59 2023-04-07 11:31:40.000000 ruiwen_data_all-1.0.2/ruiwen_data_all.egg-info/PKG-INFO
+-rw-r--r--   0 xiaochuan   (501) staff       (20)      236 2023-04-07 11:31:40.000000 ruiwen_data_all-1.0.2/ruiwen_data_all.egg-info/SOURCES.txt
+-rw-r--r--   0 xiaochuan   (501) staff       (20)        1 2023-04-07 11:31:40.000000 ruiwen_data_all-1.0.2/ruiwen_data_all.egg-info/dependency_links.txt
+-rw-r--r--   0 xiaochuan   (501) staff       (20)       53 2023-04-07 11:31:40.000000 ruiwen_data_all-1.0.2/ruiwen_data_all.egg-info/requires.txt
+-rw-r--r--   0 xiaochuan   (501) staff       (20)       16 2023-04-07 11:31:40.000000 ruiwen_data_all-1.0.2/ruiwen_data_all.egg-info/top_level.txt
+-rw-r--r--   0 xiaochuan   (501) staff       (20)       38 2023-04-07 11:31:40.150828 ruiwen_data_all-1.0.2/setup.cfg
```

### Comparing `ruiwen_data_all-1.0.1/ruiwen_data_all/__init__.py` & `ruiwen_data_all-1.0.2/ruiwen_data_all/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -689,15 +689,15 @@
         warnings.simplefilter('ignore', DeprecationWarning)
         pool = redis.ConnectionPool(host=self.ip_all, port=self.redis_port, password=self.redis_password, db=self.redis_db,
                                     decode_responses=True)
         self.redis_sql = redis.Redis(connection_pool=pool)
         self.mongodb_port = int(self.redis_sql.get('mongodb_port'))
         self.mongodb_password = str(self.redis_sql.get('mongodb_password'))
         self.daili_no = str(self.redis_sql.get('daili_no'))
-        self.daili_name = str(self.redis_sql.get('daili_password'))
+        self.daili_name = str(self.redis_sql.get('daili_name'))
         self.daili_password = str(self.redis_sql.get('daili_password'))
         self.dali_host = str(self.redis_sql.get('dali_host'))
         self.daili_port = int(self.redis_sql.get('daili_port'))
         self.emall_fsz = str(self.redis_sql.get('emall_fsz'))
         self.emall_name = str(self.redis_sql.get('emall_name'))
         self.emall_password = str(self.redis_sql.get('emall_password'))
         self.emall_sjr = str(self.redis_sql.get('emall_sjr'))
```

