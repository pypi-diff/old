# Comparing `tmp/hdxcli-1.0rc8.tar.gz` & `tmp/hdxcli-1.0rc9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "hdxcli-1.0rc8.tar", max compression
+gzip compressed data, was "hdxcli-1.0rc9.tar", max compression
```

## Comparing `hdxcli-1.0rc8.tar` & `hdxcli-1.0rc9.tar`

### file list

```diff
@@ -1,39 +1,42 @@
--rw-r--r--   0        0        0     3773 2022-11-14 15:05:49.242866 hdxcli-1.0rc8/README.md
--rw-r--r--   0        0        0     1032 2022-11-14 15:06:38.619871 hdxcli-1.0rc8/pyproject.toml
--rw-r--r--   0        0        0        1 2022-11-02 19:10:24.848710 hdxcli-1.0rc8/src/hdx_cli/__init__.py
--rw-r--r--   0        0        0        1 2022-11-03 12:18:25.102930 hdxcli-1.0rc8/src/hdx_cli/cli_interface/__init__.py
--rw-r--r--   0        0        0        1 2022-11-02 19:10:24.849096 hdxcli-1.0rc8/src/hdx_cli/cli_interface/common/__init__.py
--rw-r--r--   0        0        0     3870 2022-11-11 12:29:57.201019 hdxcli-1.0rc8/src/hdx_cli/cli_interface/common/cached_operations.py
--rw-r--r--   0        0        0     9441 2022-11-11 12:27:18.949810 hdxcli-1.0rc8/src/hdx_cli/cli_interface/common/misc_operations.py
--rw-r--r--   0        0        0     6969 2022-11-10 19:27:42.237649 hdxcli-1.0rc8/src/hdx_cli/cli_interface/common/rest_operations.py
--rw-r--r--   0        0        0     1778 2022-11-10 18:55:17.041358 hdxcli-1.0rc8/src/hdx_cli/cli_interface/dictionary/commands.py
--rw-r--r--   0        0        0     1957 2022-11-02 19:10:24.850232 hdxcli-1.0rc8/src/hdx_cli/cli_interface/function/commands.py
--rw-r--r--   0        0        0     7433 2022-11-14 15:07:13.018631 hdxcli-1.0rc8/src/hdx_cli/cli_interface/job/commands.py
--rw-r--r--   0        0        0     1395 2022-11-03 13:08:35.449835 hdxcli-1.0rc8/src/hdx_cli/cli_interface/profile/commands.py
--rw-r--r--   0        0        0        0 2022-11-02 19:10:24.850567 hdxcli-1.0rc8/src/hdx_cli/cli_interface/project/__init__.py
--rw-r--r--   0        0        0     1273 2022-11-02 19:10:24.850839 hdxcli-1.0rc8/src/hdx_cli/cli_interface/project/commands.py
--rw-r--r--   0        0        0     1963 2022-11-08 11:14:36.318805 hdxcli-1.0rc8/src/hdx_cli/cli_interface/set/commands.py
--rw-r--r--   0        0        0        0 2022-11-02 19:10:24.851143 hdxcli-1.0rc8/src/hdx_cli/cli_interface/table/__init__.py
--rw-r--r--   0        0        0     2079 2022-11-09 10:34:28.007755 hdxcli-1.0rc8/src/hdx_cli/cli_interface/table/commands.py
--rw-r--r--   0        0        0        0 2022-11-02 19:10:24.851493 hdxcli-1.0rc8/src/hdx_cli/cli_interface/transform/__init__.py
--rw-r--r--   0        0        0     3240 2022-11-09 10:38:47.669910 hdxcli-1.0rc8/src/hdx_cli/cli_interface/transform/commands.py
--rw-r--r--   0        0        0        1 2022-11-02 19:10:24.853107 hdxcli-1.0rc8/src/hdx_cli/library_api/__init__.py
--rw-r--r--   0        0        0        0 2022-11-02 19:10:24.853196 hdxcli-1.0rc8/src/hdx_cli/library_api/common/__init__.py
--rw-r--r--   0        0        0     3599 2022-11-08 11:13:09.969489 hdxcli-1.0rc8/src/hdx_cli/library_api/common/auth.py
--rw-r--r--   0        0        0     1208 2022-11-02 19:10:24.853697 hdxcli-1.0rc8/src/hdx_cli/library_api/common/cache.py
--rw-r--r--   0        0        0      238 2022-11-03 10:38:11.894462 hdxcli-1.0rc8/src/hdx_cli/library_api/common/config_constants.py
--rw-r--r--   0        0        0     1180 2022-11-10 19:18:31.648532 hdxcli-1.0rc8/src/hdx_cli/library_api/common/context.py
--rw-r--r--   0        0        0      275 2022-11-02 19:10:24.854341 hdxcli-1.0rc8/src/hdx_cli/library_api/common/dates.py
--rw-r--r--   0        0        0      996 2022-11-02 19:10:24.854549 hdxcli-1.0rc8/src/hdx_cli/library_api/common/exceptions.py
--rw-r--r--   0        0        0      238 2022-11-08 16:21:24.918673 hdxcli-1.0rc8/src/hdx_cli/library_api/common/first_use.py
--rw-r--r--   0        0        0     1834 2022-11-02 19:10:24.854984 hdxcli-1.0rc8/src/hdx_cli/library_api/common/generic_resource.py
--rw-r--r--   0        0        0     2487 2022-11-02 19:10:24.855200 hdxcli-1.0rc8/src/hdx_cli/library_api/common/login.py
--rw-r--r--   0        0        0     2926 2022-11-11 12:41:46.913874 hdxcli-1.0rc8/src/hdx_cli/library_api/common/rest_operations.py
--rw-r--r--   0        0        0        0 2022-11-02 19:10:24.855494 hdxcli-1.0rc8/src/hdx_cli/library_api/userdata/__init__.py
--rw-r--r--   0        0        0      193 2022-11-02 19:10:24.855758 hdxcli-1.0rc8/src/hdx_cli/library_api/userdata/token.py
--rw-r--r--   0        0        0        0 2022-11-02 19:10:24.855842 hdxcli-1.0rc8/src/hdx_cli/library_api/utility/__init__.py
--rw-r--r--   0        0        0     3012 2022-11-08 14:36:09.561152 hdxcli-1.0rc8/src/hdx_cli/library_api/utility/decorators.py
--rw-r--r--   0        0        0      334 2022-11-02 19:10:24.856332 hdxcli-1.0rc8/src/hdx_cli/library_api/utility/json_util.py
--rw-r--r--   0        0        0    11132 2022-11-14 15:07:23.561076 hdxcli-1.0rc8/src/hdx_cli/main.py
--rw-r--r--   0        0        0     5344 2022-11-14 15:21:00.689825 hdxcli-1.0rc8/setup.py
--rw-r--r--   0        0        0     4526 2022-11-14 15:21:00.690106 hdxcli-1.0rc8/PKG-INFO
+-rw-r--r--   0        0        0     3773 2022-11-14 15:05:49.242866 hdxcli-1.0rc9/README.md
+-rw-r--r--   0        0        0     1032 2022-11-15 10:58:07.343615 hdxcli-1.0rc9/pyproject.toml
+-rw-r--r--   0        0        0        1 2022-11-02 19:10:24.848710 hdxcli-1.0rc9/src/hdx_cli/__init__.py
+-rw-r--r--   0        0        0        1 2022-11-03 12:18:25.102930 hdxcli-1.0rc9/src/hdx_cli/cli_interface/__init__.py
+-rw-r--r--   0        0        0        1 2022-11-02 19:10:24.849096 hdxcli-1.0rc9/src/hdx_cli/cli_interface/common/__init__.py
+-rw-r--r--   0        0        0     3870 2022-11-11 12:29:57.201019 hdxcli-1.0rc9/src/hdx_cli/cli_interface/common/cached_operations.py
+-rw-r--r--   0        0        0     9441 2022-11-11 12:27:18.949810 hdxcli-1.0rc9/src/hdx_cli/cli_interface/common/misc_operations.py
+-rw-r--r--   0        0        0     6949 2022-11-15 10:50:25.862786 hdxcli-1.0rc9/src/hdx_cli/cli_interface/common/rest_operations.py
+-rw-r--r--   0        0        0     1778 2022-11-10 18:55:17.041358 hdxcli-1.0rc9/src/hdx_cli/cli_interface/dictionary/commands.py
+-rw-r--r--   0        0        0     1957 2022-11-02 19:10:24.850232 hdxcli-1.0rc9/src/hdx_cli/cli_interface/function/commands.py
+-rw-r--r--   0        0        0     7433 2022-11-14 15:07:13.018631 hdxcli-1.0rc9/src/hdx_cli/cli_interface/job/commands.py
+-rw-r--r--   0        0        0     1395 2022-11-03 13:08:35.449835 hdxcli-1.0rc9/src/hdx_cli/cli_interface/profile/commands.py
+-rw-r--r--   0        0        0        0 2022-11-02 19:10:24.850567 hdxcli-1.0rc9/src/hdx_cli/cli_interface/project/__init__.py
+-rw-r--r--   0        0        0     1273 2022-11-02 19:10:24.850839 hdxcli-1.0rc9/src/hdx_cli/cli_interface/project/commands.py
+-rw-r--r--   0        0        0     1963 2022-11-08 11:14:36.318805 hdxcli-1.0rc9/src/hdx_cli/cli_interface/set/commands.py
+-rw-r--r--   0        0        0     2299 2022-11-15 10:41:08.999519 hdxcli-1.0rc9/src/hdx_cli/cli_interface/sources/commands.py
+-rw-r--r--   0        0        0     1165 2022-11-15 10:50:42.890361 hdxcli-1.0rc9/src/hdx_cli/cli_interface/sources/kafka.py
+-rw-r--r--   0        0        0        1 2022-11-15 10:18:32.577688 hdxcli-1.0rc9/src/hdx_cli/cli_interface/sources/kinesis.py
+-rw-r--r--   0        0        0        0 2022-11-02 19:10:24.851143 hdxcli-1.0rc9/src/hdx_cli/cli_interface/table/__init__.py
+-rw-r--r--   0        0        0     2079 2022-11-09 10:34:28.007755 hdxcli-1.0rc9/src/hdx_cli/cli_interface/table/commands.py
+-rw-r--r--   0        0        0        0 2022-11-02 19:10:24.851493 hdxcli-1.0rc9/src/hdx_cli/cli_interface/transform/__init__.py
+-rw-r--r--   0        0        0     3240 2022-11-15 10:36:50.997037 hdxcli-1.0rc9/src/hdx_cli/cli_interface/transform/commands.py
+-rw-r--r--   0        0        0        1 2022-11-02 19:10:24.853107 hdxcli-1.0rc9/src/hdx_cli/library_api/__init__.py
+-rw-r--r--   0        0        0        0 2022-11-02 19:10:24.853196 hdxcli-1.0rc9/src/hdx_cli/library_api/common/__init__.py
+-rw-r--r--   0        0        0     3599 2022-11-08 11:13:09.969489 hdxcli-1.0rc9/src/hdx_cli/library_api/common/auth.py
+-rw-r--r--   0        0        0     1208 2022-11-02 19:10:24.853697 hdxcli-1.0rc9/src/hdx_cli/library_api/common/cache.py
+-rw-r--r--   0        0        0      238 2022-11-03 10:38:11.894462 hdxcli-1.0rc9/src/hdx_cli/library_api/common/config_constants.py
+-rw-r--r--   0        0        0     1180 2022-11-10 19:18:31.648532 hdxcli-1.0rc9/src/hdx_cli/library_api/common/context.py
+-rw-r--r--   0        0        0      275 2022-11-02 19:10:24.854341 hdxcli-1.0rc9/src/hdx_cli/library_api/common/dates.py
+-rw-r--r--   0        0        0      996 2022-11-02 19:10:24.854549 hdxcli-1.0rc9/src/hdx_cli/library_api/common/exceptions.py
+-rw-r--r--   0        0        0      238 2022-11-08 16:21:24.918673 hdxcli-1.0rc9/src/hdx_cli/library_api/common/first_use.py
+-rw-r--r--   0        0        0     1834 2022-11-02 19:10:24.854984 hdxcli-1.0rc9/src/hdx_cli/library_api/common/generic_resource.py
+-rw-r--r--   0        0        0     2487 2022-11-02 19:10:24.855200 hdxcli-1.0rc9/src/hdx_cli/library_api/common/login.py
+-rw-r--r--   0        0        0     2926 2022-11-11 12:41:46.913874 hdxcli-1.0rc9/src/hdx_cli/library_api/common/rest_operations.py
+-rw-r--r--   0        0        0        0 2022-11-02 19:10:24.855494 hdxcli-1.0rc9/src/hdx_cli/library_api/userdata/__init__.py
+-rw-r--r--   0        0        0      193 2022-11-02 19:10:24.855758 hdxcli-1.0rc9/src/hdx_cli/library_api/userdata/token.py
+-rw-r--r--   0        0        0        0 2022-11-02 19:10:24.855842 hdxcli-1.0rc9/src/hdx_cli/library_api/utility/__init__.py
+-rw-r--r--   0        0        0     3012 2022-11-08 14:36:09.561152 hdxcli-1.0rc9/src/hdx_cli/library_api/utility/decorators.py
+-rw-r--r--   0        0        0      334 2022-11-02 19:10:24.856332 hdxcli-1.0rc9/src/hdx_cli/library_api/utility/json_util.py
+-rw-r--r--   0        0        0    11310 2022-11-15 10:58:43.389326 hdxcli-1.0rc9/src/hdx_cli/main.py
+-rw-r--r--   0        0        0     5384 1970-01-01 00:00:00.000000 hdxcli-1.0rc9/setup.py
+-rw-r--r--   0        0        0     4526 1970-01-01 00:00:00.000000 hdxcli-1.0rc9/PKG-INFO
```

### Comparing `hdxcli-1.0rc8/README.md` & `hdxcli-1.0rc9/README.md`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/pyproject.toml` & `hdxcli-1.0rc9/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [project]
 maintainers = [{name = "German Diago Gomez", email = "german@hydrolix.io"}]
 
 
 [tool.poetry]
 name = "hdxcli"
-version = "1.0-rc8"
+version = "1.0-rc9"
 description = "Hydrolix command line utility to do CRUD operations on projects, tables, transforms and other resources in Hydrolix clusters"
 authors = ["German Diago Gomez <german@hydrolix.io>"]
 license = "MIT license"
 keywords = ["database", "bigdata", "hydrolix"]
 classifiers = ["Development Status :: 3 - Alpha",
                "Topic :: Database",
                "Topic :: Database :: Front-Ends"]
```

### Comparing `hdxcli-1.0rc8/src/hdx_cli/cli_interface/common/cached_operations.py` & `hdxcli-1.0rc9/src/hdx_cli/cli_interface/common/cached_operations.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/cli_interface/common/misc_operations.py` & `hdxcli-1.0rc9/src/hdx_cli/cli_interface/common/misc_operations.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/cli_interface/common/rest_operations.py` & `hdxcli-1.0rc9/src/hdx_cli/cli_interface/common/rest_operations.py`

 * *Files 1% similar despite different names*

```diff
@@ -104,15 +104,14 @@
 @click.pass_context
 @report_error_and_exit(exctype=HdxCliException)
 def list(ctx: click.Context):
     resource_path = ctx.parent.obj['resource_path']
     profile = ctx.parent.obj['usercontext']
     hostname = profile.hostname
     list_url = f'https://{hostname}{resource_path}'
-    print(list_url)
     auth_info : AuthInfo = profile.auth
     headers = {'Authorization': f'{auth_info.token_type} {auth_info.token}',
                'Accept': 'application/json'}
     resources = rest_ops.list(list_url, headers=headers)
     for resource in resources:
         print(resource['name'], end='')
         if (settings := resource.get('settings')) and settings.get('is_default'):
```

### Comparing `hdxcli-1.0rc8/src/hdx_cli/cli_interface/dictionary/commands.py` & `hdxcli-1.0rc9/src/hdx_cli/cli_interface/dictionary/commands.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/cli_interface/function/commands.py` & `hdxcli-1.0rc9/src/hdx_cli/cli_interface/function/commands.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/cli_interface/job/commands.py` & `hdxcli-1.0rc9/src/hdx_cli/cli_interface/job/commands.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/cli_interface/profile/commands.py` & `hdxcli-1.0rc9/src/hdx_cli/cli_interface/profile/commands.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/cli_interface/project/commands.py` & `hdxcli-1.0rc9/src/hdx_cli/cli_interface/project/commands.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/cli_interface/set/commands.py` & `hdxcli-1.0rc9/src/hdx_cli/cli_interface/set/commands.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/cli_interface/table/commands.py` & `hdxcli-1.0rc9/src/hdx_cli/cli_interface/table/commands.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/cli_interface/transform/commands.py` & `hdxcli-1.0rc9/src/hdx_cli/cli_interface/transform/commands.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/library_api/common/auth.py` & `hdxcli-1.0rc9/src/hdx_cli/library_api/common/auth.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/library_api/common/cache.py` & `hdxcli-1.0rc9/src/hdx_cli/library_api/common/cache.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/library_api/common/context.py` & `hdxcli-1.0rc9/src/hdx_cli/library_api/common/context.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/library_api/common/exceptions.py` & `hdxcli-1.0rc9/src/hdx_cli/library_api/common/exceptions.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/library_api/common/generic_resource.py` & `hdxcli-1.0rc9/src/hdx_cli/library_api/common/generic_resource.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/library_api/common/login.py` & `hdxcli-1.0rc9/src/hdx_cli/library_api/common/login.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/library_api/common/rest_operations.py` & `hdxcli-1.0rc9/src/hdx_cli/library_api/common/rest_operations.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/library_api/utility/decorators.py` & `hdxcli-1.0rc9/src/hdx_cli/library_api/utility/decorators.py`

 * *Files identical despite different names*

### Comparing `hdxcli-1.0rc8/src/hdx_cli/main.py` & `hdxcli-1.0rc9/src/hdx_cli/main.py`

 * *Files 1% similar despite different names*

```diff
@@ -12,14 +12,15 @@
 from hdx_cli.cli_interface.project import commands as project_
 from hdx_cli.cli_interface.table import commands as table_
 from hdx_cli.cli_interface.transform import commands as transform_
 from hdx_cli.cli_interface.job import commands as job_
 from hdx_cli.cli_interface.function import commands as function_
 from hdx_cli.cli_interface.dictionary import commands as dictionary_
 from hdx_cli.cli_interface.profile import commands as profile_
+from hdx_cli.cli_interface.sources import commands as sources_
 
 
 from hdx_cli.library_api.utility.decorators import report_error_and_exit
 from hdx_cli.library_api.common.cache import CacheDict
 from hdx_cli.library_api.common.context import ProfileUserContext, ProfileLoadContext
 from hdx_cli.library_api.common.exceptions import HdxCliException, TokenExpiredException
 from hdx_cli.library_api.common.config_constants import HDX_CLI_HOME_DIR, PROFILE_CONFIG_FILE
@@ -29,15 +30,15 @@
 from hdx_cli.library_api.common.auth import (
     load_profile,
     try_load_profile_from_cache_data)
 
 from hdx_cli.cli_interface.set import commands as set_commands
 from hdx_cli.library_api.common.login import login
 
-VERSION = '1.0rc8'
+VERSION = '1.0rc9'
 
 def _is_valid_username(username):
     return not username[0].isdigit()
 
 
 def _is_valid_hostname(hostname):
     # Credits to https://stackoverflow.com/questions/2532053/validate-a-hostname-string
@@ -66,17 +67,18 @@
                 print('Invalid host name.')
         good_username = False
         username = None
         while not good_username:
             username = input('Please, type the user name of your cluster: ')
             good_username = _is_valid_username(username)
         config_data = {'default': {'username': username, 'hostname': hostname}}
-        with open(profile_config_file, 'w', encoding='utf-8') as config_file:
+        os.makedirs(Path(profile_config_file).parent, exist_ok=True)
+        with open(profile_config_file, 'w+', encoding='utf-8') as config_file:
             toml.dump(config_data, config_file)
-        print('Your configuration with profile [default] has been created at {profile_config_file}')
+        print(f'\nYour configuration with profile [default] has been created at {profile_config_file}')
         print('This will be the profile used to perform commands against by default')
         print('You can start working with hdx-cli now')
         sys.exit(0)
     except KeyboardInterrupt:
         sys.exit(-1)
 
 
@@ -167,25 +169,25 @@
               metavar='PROJECTNAME', default=None)
 @click.option('--table', help="Perform operation with a different profile. (Default profile is 'default')",
               metavar='TABLENAME', default=None)
 @click.option('--transform',
               help="Explicitly pass the transform name. If none is given, the default transform for the used table is used.",
               metavar='TRANSFORMNAME', default=None)
 @click.option('--job',
-              help="Perform operation on the passed jobname",
+              help="Perform operation on the passed jobname.",
               metavar='JOBNAME', default=None)
 @click.option('--function',
-              help="Perform operation on the passed function",
+              help="Perform operation on the passed function.",
               metavar='FUNCTIONNAME', default=None)
 @click.option('--dictionary',
-              help="Perform operation on the passed dictionary",
+              help="Perform operation on the passed dictionary.",
               metavar='DICTIONARYNAME', default=None)
 @click.option('--password', help="Login password. If provided and the access token is expired, it will be used.",
               metavar='PASSWORD', default=None)
-@click.option('--profile-config-file', hidden=True, help='Used only for testing',
+@click.option('--profile-config-file', hidden=True, help='Used only for testing.',
               default=None)
 @click.pass_context
 @report_error_and_exit(exctype=HdxCliException)
 # pylint: enable=line-too-long
 def hdx_cli(ctx, profile,
             project,
             table,
@@ -260,14 +262,15 @@
 hdx_cli.add_command(set_commands.set)
 hdx_cli.add_command(set_commands.unset)
 hdx_cli.add_command(job_.job)
 hdx_cli.add_command(function_.function)
 hdx_cli.add_command(job_.purgejobs)
 hdx_cli.add_command(dictionary_.dictionary)
 hdx_cli.add_command(profile_.profile)
+hdx_cli.add_command(sources_.sources)
 hdx_cli.add_command(version)
 
 
 def main():
     hdx_cli() # pylint: disable=no-value-for-parameter
```

### Comparing `hdxcli-1.0rc8/setup.py` & `hdxcli-1.0rc9/setup.py`

 * *Files 3% similar despite different names*

```diff
@@ -10,14 +10,15 @@
  'hdx_cli.cli_interface.common',
  'hdx_cli.cli_interface.dictionary',
  'hdx_cli.cli_interface.function',
  'hdx_cli.cli_interface.job',
  'hdx_cli.cli_interface.profile',
  'hdx_cli.cli_interface.project',
  'hdx_cli.cli_interface.set',
+ 'hdx_cli.cli_interface.sources',
  'hdx_cli.cli_interface.table',
  'hdx_cli.cli_interface.transform',
  'hdx_cli.library_api',
  'hdx_cli.library_api.common',
  'hdx_cli.library_api.userdata',
  'hdx_cli.library_api.utility']
 
@@ -28,22 +29,22 @@
 ['click>=8.1.3,<9.0.0', 'requests>=2.28.1,<3.0.0', 'toml>=0.10.2,<0.11.0']
 
 entry_points = \
 {'console_scripts': ['hdxcli = hdx_cli.main:main']}
 
 setup_kwargs = {
     'name': 'hdxcli',
-    'version': '1.0rc8',
+    'version': '1.0rc9',
     'description': 'Hydrolix command line utility to do CRUD operations on projects, tables, transforms and other resources in Hydrolix clusters',
     'long_description': '[![](images/hdxcli.png)](https://github.com/hydrolix/hdx-cli)\n\n\n`hdxcli` is a command-line tool to work with hydrolix projects and tables\ninteractively.\n\nCommon operations such as CRUD operations on projects/tables/transforms \nand others  can be performed.\n\n# Hdx-cli installation\n\nYou can install `hdxcli` from pip:\n\n```shell\npip install hdxcli\n```\n\n# Using hdxcli command-line program\n\n`hdxcli` supports multiple profiles. You can use a default profile or\nuse the `--profile` option to operate on a non-default profile.\n\nWhen trying to invoke a command, if a login to the server is necessary, \na prompt will be shown and the token will be cached.\n\n\n# Command-line tool organization\n\nThe tool is organized, mostly with the general invocation form of:\n\n```shell\nhdxcli <resource> [<subresource...] <verb> [<resource_name>]\n```\n\nTable and project resources have defaults that depend on the profile you are working with,\nso they can be omitted if you used the `set` command.\n\nFor all other resources, you can use `--transform`, `--dictionary`, etc. Please see the\ncommand line help for more information.\n\n## Projects, tables and transforms\n\nThe basic operations you can do with these resources are:\n\n- list them\n- create a new resource\n- delete an existing resource\n- modify an existing resource\n- show a resource in raw json format\n- show settings from a resource\n- write a setting\n- show a single setting\n\n## Working with transforms and batch jobs\n\nIn order to use a transforms, you need to:\n\n1. create a transform\n\n\n``` shell\nhdxcli transform create -f atransform.json atransform\n```\n\nWhere atransform.json is a local file and atransform is the \nname for the transform that will be uploaded to the cluster. \nRemember that a transform is applied to a table in a project, \nso whatever you `set` with the \ncommand-line tool will be the target of your transform.\n\nIf you want to override it, do:\n\n``` shell\nhdxcli --project <the-project> --table <the-table> transform create -f atransform.json atransform\n```\n\n\n2. ingest a batch job\n\n``` shell\nhdxcli job batch ingest <job-name> <job-url>\n```\n\nThe job-name is the job name you will see if you list the job batch. job url can be either a local url or a url\nto a bucket *for which the cluster has at lease read access to*.\n\n\n## Listing and showing your profiles \n\nListing profiles:\n\n\n``` shell\nhdxcli profile list\n```\n\nShogin default profile\n\n``` shell\nhdxcli profile show\n```\n\n\n\n## FAQ: Common operations\n\n### Showing help \n\nIn order to see what you can do with the tool:\n\n``` shell\nhdxcli --help\n```\n\n### Listing resources\n\nTo list projects:\n\n``` shell\nhdxcli project list\n```\n\nTo list resources on a project:\n\n``` shell\nhdxcli --project <project-name> table list\n```\n\n\nYou can avoid repeating the project and table name by using the `set` command:\n\n\n### Set/unset project and table\n\n``` shell\nhdxcli set <your-project> <your-table>\n```\n\nSubsequent operations will be applied to the project and table. If you want to `unset`\nit, just do:\n\n``` shell\nhdxcli unset\n```\n\n\n### Creating resources\n\n``` shell\nhdxcli project create <project-name>\n```\n\n\n### Peforming operations against another server\n\nIf you want to use `hdxcli` against another server, use `--profile` option:\n\n\n### Working with resource settings\n\nShow settings for a resource:\n\n``` shell\nhdxcli project <myprojectname> settings\n```\n\n``` shell\nhdxcli table <mytablename> settings\n```\n\n``` shell\nhdxcli --transform <mytransform transform settings\n```\n\n\nModify a setting:\n\n``` shell\nhdxcli table <mytablename> settings key value\n```\n\nShow a single setting:\n\n``` shell\nhdxcli table <mytablename> settings key value\n```\n\n\n\n### Getting help for subcommands\n\nCheck which commands are available for each resource by typing:\n\n\n```\nhdxcli [<resource>...] [<verb>] --help\n```\n',
     'author': 'German Diago Gomez',
     'author_email': 'german@hydrolix.io',
-    'maintainer': None,
-    'maintainer_email': None,
-    'url': None,
+    'maintainer': 'None',
+    'maintainer_email': 'None',
+    'url': 'None',
     'package_dir': package_dir,
     'packages': packages,
     'package_data': package_data,
     'install_requires': install_requires,
     'entry_points': entry_points,
     'python_requires': '>=3.10,<3.11',
 }
```

### Comparing `hdxcli-1.0rc8/PKG-INFO` & `hdxcli-1.0rc9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hdxcli
-Version: 1.0rc8
+Version: 1.0rc9
 Summary: Hydrolix command line utility to do CRUD operations on projects, tables, transforms and other resources in Hydrolix clusters
 License: MIT
 Keywords: database,bigdata,hydrolix
 Author: German Diago Gomez
 Author-email: german@hydrolix.io
 Requires-Python: >=3.10,<3.11
 Classifier: Development Status :: 3 - Alpha
```

