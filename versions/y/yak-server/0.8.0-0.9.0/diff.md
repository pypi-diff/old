# Comparing `tmp/yak_server-0.8.0.tar.gz` & `tmp/yak_server-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "yak_server-0.8.0.tar", max compression
+gzip compressed data, was "yak_server-0.9.0.tar", max compression
```

## Comparing `yak_server-0.8.0.tar` & `yak_server-0.9.0.tar`

### file list

```diff
@@ -1,55 +1,55 @@
--rw-r--r--   0        0        0     1074 2023-03-19 23:32:53.409026 yak_server-0.8.0/LICENSE
--rw-r--r--   0        0        0     2630 2023-03-19 23:32:53.409026 yak_server-0.8.0/README.md
--rw-r--r--   0        0        0     2526 2023-03-19 23:32:53.409026 yak_server-0.8.0/pyproject.toml
--rw-r--r--   0        0        0     2476 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/__init__.py
--rw-r--r--   0        0        0     1309 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/cli/__init__.py
--rw-r--r--   0        0        0     5132 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/cli/database.py
--rw-r--r--   0        0        0     2712 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/config_file.py
--rw-r--r--   0        0        0      226 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/data/world_cup_2022/config.ini
--rw-r--r--   0        0        0     1713 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/data/world_cup_2022/finale_phase_config.json
--rw-r--r--   0        0        0     1600 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/data/world_cup_2022/groups.json
--rw-r--r--   0        0        0     7659 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/data/world_cup_2022/matches.json
--rw-r--r--   0        0        0      199 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/data/world_cup_2022/phases.json
--rw-r--r--   0        0        0     5231 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/data/world_cup_2022/teams.json
--rw-r--r--   0        0        0        0 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/__init__.py
--rw-r--r--   0        0        0       41 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/migrations/README
--rw-r--r--   0        0        0        0 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/migrations/__init__.py
--rw-r--r--   0        0        0     1109 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/migrations/alembic.ini
--rw-r--r--   0        0        0     3061 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/migrations/env.py
--rw-r--r--   0        0        0      494 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/migrations/script.py.mako
--rw-r--r--   0        0        0     1572 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/migrations/versions/9f8e020eeced_add_group_position_table.py
--rw-r--r--   0        0        0        0 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/migrations/versions/__init__.py
--rw-r--r--   0        0        0      946 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/migrations/versions/b36763d4cb42_add_bet_type_from_match.py
--rw-r--r--   0        0        0     1249 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/migrations/versions/c2ecfb568236_remove_locked_column_from_score_bet_and_.py
--rw-r--r--   0        0        0      941 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/migrations/versions/d75e76959af8_remove_played_column_compute_played_.py
--rw-r--r--   0        0        0      853 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/migrations/versions/e0f551c7766c_add_group_rank_need_recomputation_column.py
--rw-r--r--   0        0        0     5177 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/migrations/versions/f33dc66104ad_initial_migration.py
--rw-r--r--   0        0        0    12927 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/models.py
--rw-r--r--   0        0        0     1843 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/database/query.py
--rw-r--r--   0        0        0        0 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/helpers/__init__.py
--rw-r--r--   0        0        0      539 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/helpers/authentification.py
--rw-r--r--   0        0        0     2843 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/helpers/group_position.py
--rw-r--r--   0        0        0     1184 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/helpers/logging.py
--rw-r--r--   0        0        0        0 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/__init__.py
--rw-r--r--   0        0        0     3527 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/auth.py
--rw-r--r--   0        0        0    20336 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/bets.py
--rw-r--r--   0        0        0     1893 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/groups.py
--rw-r--r--   0        0        0      895 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/phase.py
--rw-r--r--   0        0        0     8300 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/results.py
--rw-r--r--   0        0        0     1267 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/teams.py
--rw-r--r--   0        0        0        0 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/utils/__init__.py
--rw-r--r--   0        0        0     1489 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/utils/auth_utils.py
--rw-r--r--   0        0        0       39 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/utils/constants.py
--rw-r--r--   0        0        0     3951 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/utils/errors.py
--rw-r--r--   0        0        0      490 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/utils/flask_utils.py
--rw-r--r--   0        0        0     4866 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/utils/schemas.py
--rw-r--r--   0        0        0      894 2023-03-19 23:32:53.413026 yak_server-0.8.0/yak_server/v1/utils/validation.py
--rw-r--r--   0        0        0      406 2023-03-19 23:32:53.417027 yak_server-0.8.0/yak_server/v2/__init__.py
--rw-r--r--   0        0        0     1400 2023-03-19 23:32:53.417027 yak_server-0.8.0/yak_server/v2/bearer_authenfication.py
--rw-r--r--   0        0        0     6060 2023-03-19 23:32:53.417027 yak_server-0.8.0/yak_server/v2/mutation.py
--rw-r--r--   0        0        0     7651 2023-03-19 23:32:53.417027 yak_server-0.8.0/yak_server/v2/query.py
--rw-r--r--   0        0        0     6437 2023-03-19 23:32:53.417027 yak_server-0.8.0/yak_server/v2/result.py
--rw-r--r--   0        0        0    12391 2023-03-19 23:32:53.417027 yak_server-0.8.0/yak_server/v2/schema.py
--rw-r--r--   0        0        0        0 2023-03-19 23:32:53.417027 yak_server-0.8.0/yak_server/v2/utils/__init__.py
--rw-r--r--   0        0        0       39 2023-03-19 23:32:53.417027 yak_server-0.8.0/yak_server/v2/utils/constants.py
--rw-r--r--   0        0        0     3637 1970-01-01 00:00:00.000000 yak_server-0.8.0/PKG-INFO
+-rw-r--r--   0        0        0     1074 2023-03-20 00:04:07.063132 yak_server-0.9.0/LICENSE
+-rw-r--r--   0        0        0     2837 2023-03-20 00:04:07.063132 yak_server-0.9.0/README.md
+-rw-r--r--   0        0        0     2526 2023-03-20 00:04:07.063132 yak_server-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0     2476 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/__init__.py
+-rw-r--r--   0        0        0     1309 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/cli/__init__.py
+-rw-r--r--   0        0        0     5132 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/cli/database.py
+-rw-r--r--   0        0        0     2712 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/config_file.py
+-rw-r--r--   0        0        0      226 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/data/world_cup_2022/config.ini
+-rw-r--r--   0        0        0     1713 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/data/world_cup_2022/finale_phase_config.json
+-rw-r--r--   0        0        0     1600 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/data/world_cup_2022/groups.json
+-rw-r--r--   0        0        0     7659 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/data/world_cup_2022/matches.json
+-rw-r--r--   0        0        0      199 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/data/world_cup_2022/phases.json
+-rw-r--r--   0        0        0     5231 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/data/world_cup_2022/teams.json
+-rw-r--r--   0        0        0        0 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/__init__.py
+-rw-r--r--   0        0        0       41 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/migrations/README
+-rw-r--r--   0        0        0        0 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/migrations/__init__.py
+-rw-r--r--   0        0        0     1109 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/migrations/alembic.ini
+-rw-r--r--   0        0        0     3061 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/migrations/env.py
+-rw-r--r--   0        0        0      494 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/migrations/script.py.mako
+-rw-r--r--   0        0        0     1572 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/migrations/versions/9f8e020eeced_add_group_position_table.py
+-rw-r--r--   0        0        0        0 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/migrations/versions/__init__.py
+-rw-r--r--   0        0        0      946 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/migrations/versions/b36763d4cb42_add_bet_type_from_match.py
+-rw-r--r--   0        0        0     1249 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/migrations/versions/c2ecfb568236_remove_locked_column_from_score_bet_and_.py
+-rw-r--r--   0        0        0      941 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/migrations/versions/d75e76959af8_remove_played_column_compute_played_.py
+-rw-r--r--   0        0        0      853 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/migrations/versions/e0f551c7766c_add_group_rank_need_recomputation_column.py
+-rw-r--r--   0        0        0     5177 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/migrations/versions/f33dc66104ad_initial_migration.py
+-rw-r--r--   0        0        0    12927 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/models.py
+-rw-r--r--   0        0        0     1843 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/database/query.py
+-rw-r--r--   0        0        0        0 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/helpers/__init__.py
+-rw-r--r--   0        0        0      539 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/helpers/authentification.py
+-rw-r--r--   0        0        0     2843 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/helpers/group_position.py
+-rw-r--r--   0        0        0     1184 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/helpers/logging.py
+-rw-r--r--   0        0        0        0 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/__init__.py
+-rw-r--r--   0        0        0     3527 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/auth.py
+-rw-r--r--   0        0        0    20336 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/bets.py
+-rw-r--r--   0        0        0     1893 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/groups.py
+-rw-r--r--   0        0        0      895 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/phase.py
+-rw-r--r--   0        0        0     8300 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/results.py
+-rw-r--r--   0        0        0     1267 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/teams.py
+-rw-r--r--   0        0        0        0 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/utils/__init__.py
+-rw-r--r--   0        0        0     1489 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/utils/auth_utils.py
+-rw-r--r--   0        0        0       39 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/utils/constants.py
+-rw-r--r--   0        0        0     3951 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/utils/errors.py
+-rw-r--r--   0        0        0      490 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/utils/flask_utils.py
+-rw-r--r--   0        0        0     4866 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/utils/schemas.py
+-rw-r--r--   0        0        0      894 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v1/utils/validation.py
+-rw-r--r--   0        0        0      406 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v2/__init__.py
+-rw-r--r--   0        0        0     1400 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v2/bearer_authenfication.py
+-rw-r--r--   0        0        0     6060 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v2/mutation.py
+-rw-r--r--   0        0        0     7651 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v2/query.py
+-rw-r--r--   0        0        0     6437 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v2/result.py
+-rw-r--r--   0        0        0    12391 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v2/schema.py
+-rw-r--r--   0        0        0        0 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v2/utils/__init__.py
+-rw-r--r--   0        0        0       39 2023-03-20 00:04:07.067132 yak_server-0.9.0/yak_server/v2/utils/constants.py
+-rw-r--r--   0        0        0     3844 1970-01-01 00:00:00.000000 yak_server-0.9.0/PKG-INFO
```

### Comparing `yak_server-0.8.0/LICENSE` & `yak_server-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/README.md` & `yak_server-0.9.0/README.md`

 * *Files 11% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 # Yak-toto
 
-[![PyPI](https://img.shields.io/pypi/v/yak-server?logo=pypi&logoColor=white&style=for-the-badge)](https://pypi.org/project/yak-server/)
+[![PyPI](https://img.shields.io/pypi/v/yak-server?label=stable)](https://pypi.org/project/yak-server/)
+[![Python Versions](https://img.shields.io/pypi/pyversions/yak-server)](https://pypi.org/project/yak-server/)
+[![codecov](https://codecov.io/gh/yak-toto/yak-server/branch/master/graph/badge.svg?token=EZZK5SY5BL)](https://codecov.io/gh/yak-toto/yak-server)
 
 ## Requisites
 
 - Ubuntu 22.04
-- Python 3.10.4
 - MySQL 8.0.30
 
 ## How to build the project
 
 ### Database
 
 Install and start mysql server on port 3306. Add a database named `yak_toto`. In root folder, create a dotenv file named `.flaskenv` and fill your MySQL user name, password and database. When backend start, this configuration is automaticaly loaded.
```

### Comparing `yak_server-0.8.0/pyproject.toml` & `yak_server-0.9.0/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 [tool.poetry]
 name = "yak-server"
 packages = [ { include = "yak_server" } ]
-version = "0.8.0"
+version = "0.9.0"
 description = "Football bet rest/graphql server"
 authors = ["Guillaume Le Pape <gui.lepape25@gmail.com>"]
 license = "MIT"
 readme = "README.md"
 keywords = ["mysql", "api", "rest", "graphql"]
 
 repository = "https://github.com/yak-toto/yak-server"
```

### Comparing `yak_server-0.8.0/yak_server/__init__.py` & `yak_server-0.9.0/yak_server/__init__.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/cli/__init__.py` & `yak_server-0.9.0/yak_server/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/cli/database.py` & `yak_server-0.9.0/yak_server/cli/database.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/config_file.py` & `yak_server-0.9.0/yak_server/config_file.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/data/world_cup_2022/finale_phase_config.json` & `yak_server-0.9.0/yak_server/data/world_cup_2022/finale_phase_config.json`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/data/world_cup_2022/groups.json` & `yak_server-0.9.0/yak_server/data/world_cup_2022/groups.json`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/data/world_cup_2022/matches.json` & `yak_server-0.9.0/yak_server/data/world_cup_2022/matches.json`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/data/world_cup_2022/teams.json` & `yak_server-0.9.0/yak_server/data/world_cup_2022/teams.json`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/database/migrations/alembic.ini` & `yak_server-0.9.0/yak_server/database/migrations/alembic.ini`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/database/migrations/env.py` & `yak_server-0.9.0/yak_server/database/migrations/env.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/database/migrations/versions/9f8e020eeced_add_group_position_table.py` & `yak_server-0.9.0/yak_server/database/migrations/versions/9f8e020eeced_add_group_position_table.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/database/migrations/versions/b36763d4cb42_add_bet_type_from_match.py` & `yak_server-0.9.0/yak_server/database/migrations/versions/b36763d4cb42_add_bet_type_from_match.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/database/migrations/versions/c2ecfb568236_remove_locked_column_from_score_bet_and_.py` & `yak_server-0.9.0/yak_server/database/migrations/versions/c2ecfb568236_remove_locked_column_from_score_bet_and_.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/database/migrations/versions/d75e76959af8_remove_played_column_compute_played_.py` & `yak_server-0.9.0/yak_server/database/migrations/versions/d75e76959af8_remove_played_column_compute_played_.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/database/migrations/versions/e0f551c7766c_add_group_rank_need_recomputation_column.py` & `yak_server-0.9.0/yak_server/database/migrations/versions/e0f551c7766c_add_group_rank_need_recomputation_column.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/database/migrations/versions/f33dc66104ad_initial_migration.py` & `yak_server-0.9.0/yak_server/database/migrations/versions/f33dc66104ad_initial_migration.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/database/models.py` & `yak_server-0.9.0/yak_server/database/models.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/database/query.py` & `yak_server-0.9.0/yak_server/database/query.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/helpers/authentification.py` & `yak_server-0.9.0/yak_server/helpers/authentification.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/helpers/group_position.py` & `yak_server-0.9.0/yak_server/helpers/group_position.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/helpers/logging.py` & `yak_server-0.9.0/yak_server/helpers/logging.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v1/auth.py` & `yak_server-0.9.0/yak_server/v1/auth.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v1/bets.py` & `yak_server-0.9.0/yak_server/v1/bets.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v1/groups.py` & `yak_server-0.9.0/yak_server/v1/groups.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v1/phase.py` & `yak_server-0.9.0/yak_server/v1/phase.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v1/results.py` & `yak_server-0.9.0/yak_server/v1/results.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v1/teams.py` & `yak_server-0.9.0/yak_server/v1/teams.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v1/utils/auth_utils.py` & `yak_server-0.9.0/yak_server/v1/utils/auth_utils.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v1/utils/errors.py` & `yak_server-0.9.0/yak_server/v1/utils/errors.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v1/utils/schemas.py` & `yak_server-0.9.0/yak_server/v1/utils/schemas.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v1/utils/validation.py` & `yak_server-0.9.0/yak_server/v1/utils/validation.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v2/bearer_authenfication.py` & `yak_server-0.9.0/yak_server/v2/bearer_authenfication.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v2/mutation.py` & `yak_server-0.9.0/yak_server/v2/mutation.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v2/query.py` & `yak_server-0.9.0/yak_server/v2/query.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v2/result.py` & `yak_server-0.9.0/yak_server/v2/result.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/yak_server/v2/schema.py` & `yak_server-0.9.0/yak_server/v2/schema.py`

 * *Files identical despite different names*

### Comparing `yak_server-0.8.0/PKG-INFO` & `yak_server-0.9.0/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: yak-server
-Version: 0.8.0
+Version: 0.9.0
 Summary: Football bet rest/graphql server
 Home-page: https://github.com/yak-toto/yak-server
 License: MIT
 Keywords: mysql,api,rest,graphql
 Author: Guillaume Le Pape
 Author-email: gui.lepape25@gmail.com
 Requires-Python: >=3.9,<4.0
@@ -22,20 +22,21 @@
 Requires-Dist: python-dotenv (>=1.0.0,<2.0.0)
 Requires-Dist: strawberry-graphql (>=0.165.0,<0.166.0)
 Project-URL: Repository, https://github.com/yak-toto/yak-server
 Description-Content-Type: text/markdown
 
 # Yak-toto
 
-[![PyPI](https://img.shields.io/pypi/v/yak-server?logo=pypi&logoColor=white&style=for-the-badge)](https://pypi.org/project/yak-server/)
+[![PyPI](https://img.shields.io/pypi/v/yak-server?label=stable)](https://pypi.org/project/yak-server/)
+[![Python Versions](https://img.shields.io/pypi/pyversions/yak-server)](https://pypi.org/project/yak-server/)
+[![codecov](https://codecov.io/gh/yak-toto/yak-server/branch/master/graph/badge.svg?token=EZZK5SY5BL)](https://codecov.io/gh/yak-toto/yak-server)
 
 ## Requisites
 
 - Ubuntu 22.04
-- Python 3.10.4
 - MySQL 8.0.30
 
 ## How to build the project
 
 ### Database
 
 Install and start mysql server on port 3306. Add a database named `yak_toto`. In root folder, create a dotenv file named `.flaskenv` and fill your MySQL user name, password and database. When backend start, this configuration is automaticaly loaded.
```

