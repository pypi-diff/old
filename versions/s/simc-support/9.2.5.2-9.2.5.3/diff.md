# Comparing `tmp/simc_support-9.2.5.2.tar.gz` & `tmp/simc_support-9.2.5.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "simc_support-9.2.5.2.tar", last modified: Sat Aug  6 16:53:43 2022, max compression
+gzip compressed data, was "simc_support-9.2.5.3.tar", last modified: Wed Aug 17 17:13:19 2022, max compression
```

## Comparing `simc_support-9.2.5.2.tar` & `simc_support-9.2.5.3.tar`

### file list

```diff
@@ -1,50 +1,50 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-06 16:53:43.483070 simc_support-9.2.5.2/
--rw-r--r--   0 runner    (1001) docker     (121)    35141 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     1571 2022-08-06 16:53:43.483070 simc_support-9.2.5.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      944 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      613 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)      822 2022-08-06 16:53:43.483070 simc_support-9.2.5.2/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-06 16:53:43.471069 simc_support-9.2.5.2/simc_support/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-06 16:53:43.479069 simc_support-9.2.5.2/simc_support/game_data/
--rw-r--r--   0 runner    (1001) docker     (121)     3964 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/Conduit.py
--rw-r--r--   0 runner    (1001) docker     (121)     1949 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/Covenant.py
--rw-r--r--   0 runner    (1001) docker     (121)     2038 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/DominationShard.py
--rw-r--r--   0 runner    (1001) docker     (121)      482 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/Faction.py
--rw-r--r--   0 runner    (1001) docker     (121)     2262 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/ItemLevel.py
--rw-r--r--   0 runner    (1001) docker     (121)     3094 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/Language.py
--rw-r--r--   0 runner    (1001) docker     (121)     3966 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/Legendary.py
--rw-r--r--   0 runner    (1001) docker     (121)    11333 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/Race.py
--rw-r--r--   0 runner    (1001) docker     (121)       91 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/RaidRole.py
--rw-r--r--   0 runner    (1001) docker     (121)       79 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/Role.py
--rw-r--r--   0 runner    (1001) docker     (121)     1109 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/SimcObject.py
--rw-r--r--   0 runner    (1001) docker     (121)    10172 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/SoulBind.py
--rw-r--r--   0 runner    (1001) docker     (121)      377 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/Source.py
--rw-r--r--   0 runner    (1001) docker     (121)      100 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/Stat.py
--rw-r--r--   0 runner    (1001) docker     (121)     3216 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/Talent.py
--rw-r--r--   0 runner    (1001) docker     (121)    18499 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/Trinket.py
--rw-r--r--   0 runner    (1001) docker     (121)     5837 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/WowClass.py
--rw-r--r--   0 runner    (1001) docker     (121)    18421 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/WowSpec.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-06 16:53:43.483070 simc_support-9.2.5.2/simc_support/game_data/data_files/
--rw-r--r--   0 runner    (1001) docker     (121)   147887 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/data_files/conduits.json
--rw-r--r--   0 runner    (1001) docker     (121)     2410 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/data_files/covenants.json
--rw-r--r--   0 runner    (1001) docker     (121)        2 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/data_files/damnation_shards.json
--rw-r--r--   0 runner    (1001) docker     (121)    31715 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/data_files/domination_shards.json
--rw-r--r--   0 runner    (1001) docker     (121)   154887 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/data_files/legendaries.json
--rw-r--r--   0 runner    (1001) docker     (121)   170782 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/data_files/soul_binds.json
--rw-r--r--   0 runner    (1001) docker     (121)   305279 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/data_files/talents.json
--rw-r--r--   0 runner    (1001) docker     (121)  2398504 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/data_files/trinkets.json
--rw-r--r--   0 runner    (1001) docker     (121)    20184 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/game_data/data_files/wow_classes.json
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/py.typed
--rw-r--r--   0 runner    (1001) docker     (121)    32498 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/self_update.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-06 16:53:43.483070 simc_support-9.2.5.2/simc_support/simc_data/
--rw-r--r--   0 runner    (1001) docker     (121)      494 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/simc_data/FightStyle.py
--rw-r--r--   0 runner    (1001) docker     (121)       94 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/simc_data/Tier.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/simc_data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1407 2022-08-06 16:53:26.000000 simc_support-9.2.5.2/simc_support/trinket_export.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-06 16:53:43.471069 simc_support-9.2.5.2/simc_support.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     1571 2022-08-06 16:53:43.000000 simc_support-9.2.5.2/simc_support.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1508 2022-08-06 16:53:43.000000 simc_support-9.2.5.2/simc_support.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-06 16:53:43.000000 simc_support-9.2.5.2/simc_support.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       13 2022-08-06 16:53:43.000000 simc_support-9.2.5.2/simc_support.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-17 17:13:19.566961 simc_support-9.2.5.3/
+-rw-r--r--   0 runner    (1001) docker     (121)    35141 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)     1571 2022-08-17 17:13:19.566961 simc_support-9.2.5.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      944 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      613 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)      822 2022-08-17 17:13:19.566961 simc_support-9.2.5.3/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-17 17:13:19.558961 simc_support-9.2.5.3/simc_support/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-17 17:13:19.562961 simc_support-9.2.5.3/simc_support/game_data/
+-rw-r--r--   0 runner    (1001) docker     (121)     3964 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/Conduit.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1949 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/Covenant.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2038 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/DominationShard.py
+-rw-r--r--   0 runner    (1001) docker     (121)      482 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/Faction.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2373 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/ItemLevel.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3094 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/Language.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3966 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/Legendary.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11333 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/Race.py
+-rw-r--r--   0 runner    (1001) docker     (121)       91 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/RaidRole.py
+-rw-r--r--   0 runner    (1001) docker     (121)       79 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/Role.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1109 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/SimcObject.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10172 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/SoulBind.py
+-rw-r--r--   0 runner    (1001) docker     (121)      377 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/Source.py
+-rw-r--r--   0 runner    (1001) docker     (121)      100 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/Stat.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3216 2022-08-17 17:13:04.000000 simc_support-9.2.5.3/simc_support/game_data/Talent.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18492 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/Trinket.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5837 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/WowClass.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18421 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/WowSpec.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-17 17:13:19.566961 simc_support-9.2.5.3/simc_support/game_data/data_files/
+-rw-r--r--   0 runner    (1001) docker     (121)   147887 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/data_files/conduits.json
+-rw-r--r--   0 runner    (1001) docker     (121)     2410 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/data_files/covenants.json
+-rw-r--r--   0 runner    (1001) docker     (121)        2 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/data_files/damnation_shards.json
+-rw-r--r--   0 runner    (1001) docker     (121)    31715 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/data_files/domination_shards.json
+-rw-r--r--   0 runner    (1001) docker     (121)   154887 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/data_files/legendaries.json
+-rw-r--r--   0 runner    (1001) docker     (121)   170782 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/data_files/soul_binds.json
+-rw-r--r--   0 runner    (1001) docker     (121)   305279 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/data_files/talents.json
+-rw-r--r--   0 runner    (1001) docker     (121)  2398504 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/data_files/trinkets.json
+-rw-r--r--   0 runner    (1001) docker     (121)    20184 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/game_data/data_files/wow_classes.json
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/py.typed
+-rw-r--r--   0 runner    (1001) docker     (121)    32498 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/self_update.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-17 17:13:19.566961 simc_support-9.2.5.3/simc_support/simc_data/
+-rw-r--r--   0 runner    (1001) docker     (121)      494 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/simc_data/FightStyle.py
+-rw-r--r--   0 runner    (1001) docker     (121)       94 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/simc_data/Tier.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/simc_data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1407 2022-08-17 17:13:05.000000 simc_support-9.2.5.3/simc_support/trinket_export.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-17 17:13:19.562961 simc_support-9.2.5.3/simc_support.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     1571 2022-08-17 17:13:19.000000 simc_support-9.2.5.3/simc_support.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1508 2022-08-17 17:13:19.000000 simc_support-9.2.5.3/simc_support.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-17 17:13:19.000000 simc_support-9.2.5.3/simc_support.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       13 2022-08-17 17:13:19.000000 simc_support-9.2.5.3/simc_support.egg-info/top_level.txt
```

### Comparing `simc_support-9.2.5.2/LICENSE` & `simc_support-9.2.5.3/LICENSE`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/PKG-INFO` & `simc_support-9.2.5.3/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: simc_support
-Version: 9.2.5.2
+Version: 9.2.5.3
 Summary: Data to support simulations for World of Warcraft with SimulationCraft.
 Home-page: https://github.com/Bloodmallet/simc_support
 Author: Bloodmallet(EU)
 Author-email: bloodmalleteu@gmail.com
 License: GNU GENERAL PUBLIC LICENSE
 Project-URL: Bug Tracker, https://github.com/Bloodmallet/simc_support/issues
 Classifier: Programming Language :: Python :: 3
```

### Comparing `simc_support-9.2.5.2/README.md` & `simc_support-9.2.5.3/README.md`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/pyproject.toml` & `simc_support-9.2.5.3/pyproject.toml`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/setup.cfg` & `simc_support-9.2.5.3/setup.cfg`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/Conduit.py` & `simc_support-9.2.5.3/simc_support/game_data/Conduit.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/Covenant.py` & `simc_support-9.2.5.3/simc_support/game_data/Covenant.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/DominationShard.py` & `simc_support-9.2.5.3/simc_support/game_data/DominationShard.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/ItemLevel.py` & `simc_support-9.2.5.3/simc_support/game_data/ItemLevel.py`

 * *Files 12% similar despite different names*

```diff
@@ -79,21 +79,32 @@
     288,  # + weekly
     291,  # weekly
     294,  # weekly
     298,  # weekly
     301,  # weekly
     304,  # weekly
 ]
+SEASON_4_VALOR_UPGRADES = [
+    272,
+    275,
+    278,
+    281,
+    285,
+    288,
+    291,
+    294,
+    298,
+]
 TAZAVESH = [226, 233]
 WORLD_BOSS_CHAINS_OF_DEVASTATION = 233
 WORLD_BOSS_ZERETH_MORTIS = 259
 
 # raids
 SEASON_4_RAID = [265, 278, 291, 304]
-SEASON_4_RAID_ENDBOSSES = [272, 285, 297, 311]
+SEASON_4_RAID_ENDBOSSES = [272, 285, 298, 311]
 
 CASTLE_NATHRIA = SEASON_4_RAID
 CASTLE_NATHRIA_ENDBOSSES = SEASON_4_RAID_ENDBOSSES
 
 SANCTUM_OF_DOMINATION = SEASON_4_RAID
 SANCTUM_OF_DOMINATION_ENDBOSSES = SEASON_4_RAID_ENDBOSSES
```

### Comparing `simc_support-9.2.5.2/simc_support/game_data/Language.py` & `simc_support-9.2.5.3/simc_support/game_data/Language.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/Legendary.py` & `simc_support-9.2.5.3/simc_support/game_data/Legendary.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/Race.py` & `simc_support-9.2.5.3/simc_support/game_data/Race.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/SimcObject.py` & `simc_support-9.2.5.3/simc_support/game_data/SimcObject.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/SoulBind.py` & `simc_support-9.2.5.3/simc_support/game_data/SoulBind.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/Talent.py` & `simc_support-9.2.5.3/simc_support/game_data/Talent.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/Trinket.py` & `simc_support-9.2.5.3/simc_support/game_data/Trinket.py`

 * *Files 2% similar despite different names*

```diff
@@ -169,16 +169,17 @@
                 262,
             ]
 
         # Tazavesh Dungeon m+ specific itemlevel
         if item["id_journal_instance"] == 1194:
             return ItemLevel.DUNGEON
 
+        # Legion
         if item["id_expansion"] == 6 and source == Source.DUNGEON:
-            combined_list = ItemLevel.DUNGEON_MYTHIC_DROPS + ItemLevel.VALOR_UPGRADES
+            combined_list = ItemLevel.SEASON_4_VALOR_UPGRADES
             unique_set = set(combined_list)
             sorted_list = sorted(list(unique_set))
             return sorted_list
 
         if source == Source.DUNGEON or item["id"] == 190958:
             return ItemLevel.DUNGEON
```

### Comparing `simc_support-9.2.5.2/simc_support/game_data/WowClass.py` & `simc_support-9.2.5.3/simc_support/game_data/WowClass.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/WowSpec.py` & `simc_support-9.2.5.3/simc_support/game_data/WowSpec.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/data_files/conduits.json` & `simc_support-9.2.5.3/simc_support/game_data/data_files/conduits.json`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/data_files/covenants.json` & `simc_support-9.2.5.3/simc_support/game_data/data_files/covenants.json`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/data_files/domination_shards.json` & `simc_support-9.2.5.3/simc_support/game_data/data_files/domination_shards.json`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/data_files/legendaries.json` & `simc_support-9.2.5.3/simc_support/game_data/data_files/legendaries.json`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/data_files/soul_binds.json` & `simc_support-9.2.5.3/simc_support/game_data/data_files/soul_binds.json`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/data_files/talents.json` & `simc_support-9.2.5.3/simc_support/game_data/data_files/talents.json`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/data_files/trinkets.json` & `simc_support-9.2.5.3/simc_support/game_data/data_files/trinkets.json`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/game_data/data_files/wow_classes.json` & `simc_support-9.2.5.3/simc_support/game_data/data_files/wow_classes.json`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/self_update.py` & `simc_support-9.2.5.3/simc_support/self_update.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support/trinket_export.py` & `simc_support-9.2.5.3/simc_support/trinket_export.py`

 * *Files identical despite different names*

### Comparing `simc_support-9.2.5.2/simc_support.egg-info/PKG-INFO` & `simc_support-9.2.5.3/simc_support.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: simc-support
-Version: 9.2.5.2
+Version: 9.2.5.3
 Summary: Data to support simulations for World of Warcraft with SimulationCraft.
 Home-page: https://github.com/Bloodmallet/simc_support
 Author: Bloodmallet(EU)
 Author-email: bloodmalleteu@gmail.com
 License: GNU GENERAL PUBLIC LICENSE
 Project-URL: Bug Tracker, https://github.com/Bloodmallet/simc_support/issues
 Classifier: Programming Language :: Python :: 3
```

### Comparing `simc_support-9.2.5.2/simc_support.egg-info/SOURCES.txt` & `simc_support-9.2.5.3/simc_support.egg-info/SOURCES.txt`

 * *Files identical despite different names*

