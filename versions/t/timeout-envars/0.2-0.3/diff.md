# Comparing `tmp/timeout-envars-0.2.tar.gz` & `tmp/timeout-envars-0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "timeout-envars-0.2.tar", last modified: Tue Apr  4 00:12:27 2023, max compression
+gzip compressed data, was "timeout-envars-0.3.tar", last modified: Thu Apr  6 15:14:59 2023, max compression
```

## Comparing `timeout-envars-0.2.tar` & `timeout-envars-0.3.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 00:12:27.339250 timeout-envars-0.2/
--rw-r--r--   0 runner    (1001) docker     (123)      175 2023-04-04 00:12:27.339250 timeout-envars-0.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1344 2023-04-04 00:12:10.000000 timeout-envars-0.2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 00:12:27.335250 timeout-envars-0.2/envars/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 00:12:10.000000 timeout-envars-0.2/envars/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     9893 2023-04-04 00:12:10.000000 timeout-envars-0.2/envars/envars.py
--rw-r--r--   0 runner    (1001) docker     (123)     1484 2023-04-04 00:12:10.000000 timeout-envars-0.2/envars/kms.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     9043 2023-04-04 00:12:10.000000 timeout-envars-0.2/envars/models.py
--rw-r--r--   0 runner    (1001) docker     (123)      870 2023-04-04 00:12:10.000000 timeout-envars-0.2/envars/ssm.py
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-04-04 00:12:27.339250 timeout-envars-0.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-04-04 00:12:10.000000 timeout-envars-0.2/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 00:12:27.335250 timeout-envars-0.2/tests/
--rw-r--r--   0 runner    (1001) docker     (123)    11445 2023-04-04 00:12:10.000000 timeout-envars-0.2/tests/test_cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 00:12:27.339250 timeout-envars-0.2/timeout_envars.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      175 2023-04-04 00:12:27.000000 timeout-envars-0.2/timeout_envars.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-04-04 00:12:27.000000 timeout-envars-0.2/timeout_envars.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-04 00:12:27.000000 timeout-envars-0.2/timeout_envars.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       46 2023-04-04 00:12:27.000000 timeout-envars-0.2/timeout_envars.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       29 2023-04-04 00:12:27.000000 timeout-envars-0.2/timeout_envars.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-04 00:12:27.000000 timeout-envars-0.2/timeout_envars.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:14:59.369855 timeout-envars-0.3/
+-rw-r--r--   0 runner    (1001) docker     (123)      175 2023-04-06 15:14:59.369855 timeout-envars-0.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1344 2023-04-06 15:14:50.000000 timeout-envars-0.3/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:14:59.365855 timeout-envars-0.3/envars/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 15:14:50.000000 timeout-envars-0.3/envars/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    10159 2023-04-06 15:14:50.000000 timeout-envars-0.3/envars/envars.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1484 2023-04-06 15:14:50.000000 timeout-envars-0.3/envars/kms.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     9102 2023-04-06 15:14:50.000000 timeout-envars-0.3/envars/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)      870 2023-04-06 15:14:50.000000 timeout-envars-0.3/envars/ssm.py
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-04-06 15:14:59.369855 timeout-envars-0.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      484 2023-04-06 15:14:50.000000 timeout-envars-0.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:14:59.365855 timeout-envars-0.3/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)    11445 2023-04-06 15:14:50.000000 timeout-envars-0.3/tests/test_cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:14:59.369855 timeout-envars-0.3/timeout_envars.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      175 2023-04-06 15:14:59.000000 timeout-envars-0.3/timeout_envars.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-04-06 15:14:59.000000 timeout-envars-0.3/timeout_envars.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:14:59.000000 timeout-envars-0.3/timeout_envars.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       46 2023-04-06 15:14:59.000000 timeout-envars-0.3/timeout_envars.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       29 2023-04-06 15:14:59.000000 timeout-envars-0.3/timeout_envars.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-06 15:14:59.000000 timeout-envars-0.3/timeout_envars.egg-info/top_level.txt
```

### Comparing `timeout-envars-0.2/README.md` & `timeout-envars-0.3/README.md`

 * *Files identical despite different names*

### Comparing `timeout-envars-0.2/envars/envars.py` & `timeout-envars-0.3/envars/envars.py`

 * *Files 2% similar despite different names*

```diff
@@ -112,14 +112,21 @@
     parser_print.add_argument(
         '-d',
         '--decrypt',
         required=False,
         action='store_true',
     )
     parser_print.add_argument(
+        '-n',
+        '--no-templating',
+        required=False,
+        default=False,
+        action='store_true',
+    )
+    parser_print.add_argument(
         '-e',
         '--env',
         required=False,
     )
     parser_print.add_argument(
         '-t',
         '--template-var',
@@ -372,25 +379,27 @@
             return (
                 yaml.dump(
                     {'envars': envars.build_env(
                         args.env,
                         account,
                         decrypt=args.decrypt,
                         template_vars=template_vars,
+                        no_templating=args.no_templating,
                     )},
                     default_flow_style=False
                 )
             )
         else:
             env_vars = []
             for name, value in envars.build_env(
                     args.env,
                     account,
                     decrypt=args.decrypt,
-                    template_vars=template_vars).items():
+                    template_vars=template_vars,
+                    no_templating=args.no_templating).items():
                 if args.quote:
                     env_vars.append(f"{name}='{value}'")
                 else:
                     env_vars.append(f'{name}={value}')
 
             return env_vars
     else:
```

### Comparing `timeout-envars-0.2/envars/kms.py` & `timeout-envars-0.3/envars/kms.py`

 * *Files identical despite different names*

### Comparing `timeout-envars-0.2/envars/models.py` & `timeout-envars-0.3/envars/models.py`

 * *Files 3% similar despite different names*

```diff
@@ -206,15 +206,15 @@
         return envars
 
     def get_var(self, var, env, account):
         for v in self.envars:
             if v.name == var:
                 return {v.name: v.get_value(env, account, fetch_pstore=True)}
 
-    def build_env(self, env, account, decrypt=False, template_vars=None):
+    def build_env(self, env, account, decrypt=False, template_vars=None, no_templating=False):
         logging.debug(f'build_env({env}, {account})')
         envars = {}
         if env != 'default' and env not in self.envs:
             raise (Exception(f'Unknown Env: "{env}"'))
 
         template_vars['STAGE'] = env
         # fetch all the non secret values
@@ -224,16 +224,17 @@
                 if v.name not in template_vars.keys():
                     template_vars[v.name] = value
                 envars[v.name] = value
 
         jenv = jinja2.Environment()
 
         # process jinja templates
-        for var in envars:
-            envars[var] = jenv.from_string(envars[var]).render(template_vars)
+        if not no_templating:
+            for var in envars:
+                envars[var] = jenv.from_string(envars[var]).render(template_vars)
 
         # fetch secrets
         for v in self.envars:
             value = v.get_value(env, account, decrypt)
             if value:
                 if v.name not in envars:
                     envars[v.name] = value
```

### Comparing `timeout-envars-0.2/envars/ssm.py` & `timeout-envars-0.3/envars/ssm.py`

 * *Files identical despite different names*

### Comparing `timeout-envars-0.2/tests/test_cli.py` & `timeout-envars-0.3/tests/test_cli.py`

 * *Files identical despite different names*

