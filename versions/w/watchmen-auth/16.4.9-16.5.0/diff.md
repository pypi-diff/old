# Comparing `tmp/watchmen_auth-16.4.9.tar.gz` & `tmp/watchmen_auth-16.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_auth-16.4.9.tar", max compression
+gzip compressed data, was "watchmen_auth-16.5.0.tar", max compression
```

## Comparing `watchmen_auth-16.4.9.tar` & `watchmen_auth-16.5.0.tar`

### file list

```diff
@@ -1,10 +1,9 @@
--rw-r--r--   0        0        0     1061 2023-02-23 10:23:45.968775 watchmen_auth-16.4.9/LICENSE
--rw-r--r--   0        0        0      418 2023-02-23 10:23:45.972775 watchmen_auth-16.4.9/pyproject.toml
--rw-r--r--   0        0        0      362 2023-02-23 10:23:45.972775 watchmen_auth-16.4.9/src/watchmen_auth/__init__.py
--rw-r--r--   0        0        0      755 2023-02-23 10:23:45.972775 watchmen_auth-16.4.9/src/watchmen_auth/auth_helper.py
--rw-r--r--   0        0        0     1569 2023-02-23 10:23:45.972775 watchmen_auth-16.4.9/src/watchmen_auth/authentication.py
--rw-r--r--   0        0        0     1212 2023-02-23 10:23:45.972775 watchmen_auth-16.4.9/src/watchmen_auth/authorization.py
--rw-r--r--   0        0        0      742 2023-02-23 10:23:45.972775 watchmen_auth-16.4.9/src/watchmen_auth/fake_principal_service.py
--rw-r--r--   0        0        0      816 2023-02-23 10:23:45.972775 watchmen_auth-16.4.9/src/watchmen_auth/principal_service.py
--rw-r--r--   0        0        0      689 1970-01-01 00:00:00.000000 watchmen_auth-16.4.9/setup.py
--rw-r--r--   0        0        0      478 1970-01-01 00:00:00.000000 watchmen_auth-16.4.9/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-04-06 09:13:10.376010 watchmen_auth-16.5.0/LICENSE
+-rw-r--r--   0        0        0      418 2023-04-06 09:13:10.376010 watchmen_auth-16.5.0/pyproject.toml
+-rw-r--r--   0        0        0      362 2023-04-06 09:13:10.376010 watchmen_auth-16.5.0/src/watchmen_auth/__init__.py
+-rw-r--r--   0        0        0      755 2023-04-06 09:13:10.376010 watchmen_auth-16.5.0/src/watchmen_auth/auth_helper.py
+-rw-r--r--   0        0        0     1569 2023-04-06 09:13:10.376010 watchmen_auth-16.5.0/src/watchmen_auth/authentication.py
+-rw-r--r--   0        0        0     1212 2023-04-06 09:13:10.376010 watchmen_auth-16.5.0/src/watchmen_auth/authorization.py
+-rw-r--r--   0        0        0      742 2023-04-06 09:13:10.376010 watchmen_auth-16.5.0/src/watchmen_auth/fake_principal_service.py
+-rw-r--r--   0        0        0      816 2023-04-06 09:13:10.376010 watchmen_auth-16.5.0/src/watchmen_auth/principal_service.py
+-rw-r--r--   0        0        0      478 1970-01-01 00:00:00.000000 watchmen_auth-16.5.0/PKG-INFO
```

### Comparing `watchmen_auth-16.4.9/LICENSE` & `watchmen_auth-16.5.0/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_auth-16.4.9/src/watchmen_auth/auth_helper.py` & `watchmen_auth-16.5.0/src/watchmen_auth/auth_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_auth-16.4.9/src/watchmen_auth/authentication.py` & `watchmen_auth-16.5.0/src/watchmen_auth/authentication.py`

 * *Files identical despite different names*

### Comparing `watchmen_auth-16.4.9/src/watchmen_auth/authorization.py` & `watchmen_auth-16.5.0/src/watchmen_auth/authorization.py`

 * *Files identical despite different names*

### Comparing `watchmen_auth-16.4.9/src/watchmen_auth/fake_principal_service.py` & `watchmen_auth-16.5.0/src/watchmen_auth/fake_principal_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_auth-16.4.9/src/watchmen_auth/principal_service.py` & `watchmen_auth-16.5.0/src/watchmen_auth/principal_service.py`

 * *Files identical despite different names*

