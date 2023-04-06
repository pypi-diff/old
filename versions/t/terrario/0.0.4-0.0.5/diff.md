# Comparing `tmp/terrario-0.0.4.tar.gz` & `tmp/terrario-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "terrario-0.0.4.tar", last modified: Thu Apr  6 18:53:34 2023, max compression
+gzip compressed data, was "terrario-0.0.5.tar", last modified: Thu Apr  6 19:06:47 2023, max compression
```

## Comparing `terrario-0.0.4.tar` & `terrario-0.0.5.tar`

### file list

```diff
@@ -1,84 +1,84 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 18:53:34.935574 terrario-0.0.4/
--rw-rw-rw-   0        0        0        0 2023-04-06 17:58:29.000000 terrario-0.0.4/LICENSE
--rw-rw-rw-   0        0        0      178 2023-04-06 18:52:26.000000 terrario-0.0.4/MANIFEST.in
--rw-rw-rw-   0        0        0     1341 2023-04-06 18:53:34.935574 terrario-0.0.4/PKG-INFO
--rw-rw-rw-   0        0        0      762 2023-04-06 18:04:01.000000 terrario-0.0.4/README.md
--rw-rw-rw-   0        0        0      152 2023-04-06 18:50:16.000000 terrario-0.0.4/pyproject.toml
--rw-rw-rw-   0        0        0      854 2023-04-06 18:53:34.936574 terrario-0.0.4/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-04-06 18:53:34.845442 terrario-0.0.4/src/
-drwxrwxrwx   0        0        0        0 2023-04-06 18:53:34.857447 terrario-0.0.4/src/terrario/
-drwxrwxrwx   0        0        0        0 2023-04-06 18:53:34.871450 terrario-0.0.4/src/terrario/Classes/
--rw-rw-rw-   0        0        0     1742 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Classes/game.py
--rw-rw-rw-   0        0        0    10385 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Classes/map.py
--rw-rw-rw-   0        0        0     4230 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Classes/player.py
--rw-rw-rw-   0        0        0     6621 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Classes/props.py
--rw-rw-rw-   0        0        0     4721 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Classes/tile.py
-drwxrwxrwx   0        0        0        0 2023-04-06 18:53:34.848442 terrario-0.0.4/src/terrario/Images/
-drwxrwxrwx   0        0        0        0 2023-04-06 18:53:34.882561 terrario-0.0.4/src/terrario/Images/Player/
--rw-rw-rw-   0        0        0      217 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Player/DrillTip_down.png
--rw-rw-rw-   0        0        0      213 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Player/DrillTip_left.png
--rw-rw-rw-   0        0        0      211 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Player/DrillTip_right.png
--rw-rw-rw-   0        0        0      217 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Player/DrillTip_up.png
--rw-rw-rw-   0        0        0      250 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Player/Drill_down.png
--rw-rw-rw-   0        0        0      243 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Player/Drill_left.png
--rw-rw-rw-   0        0        0      241 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Player/Drill_right.png
--rw-rw-rw-   0        0        0      251 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Player/Drill_up.png
--rw-rw-rw-   0        0        0      258 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Player/Parachute.png
-drwxrwxrwx   0        0        0        0 2023-04-06 18:53:34.932573 terrario-0.0.4/src/terrario/Images/Tiles/
--rw-rw-rw-   0        0        0      120 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Air.png
--rw-rw-rw-   0        0        0      209 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Brown_mushroom.png
--rw-rw-rw-   0        0        0      211 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Cactus.png
--rw-rw-rw-   0        0        0      224 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Cactus_top.png
--rw-rw-rw-   0        0        0      222 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Coal_ore.png
--rw-rw-rw-   0        0        0      235 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Dead_weed.png
--rw-rw-rw-   0        0        0     1826 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Dirt.png
--rw-rw-rw-   0        0        0      656 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Fir_dark_leaves.png
--rw-rw-rw-   0        0        0      546 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Fir_dark_leaves_covered_trunk.png
--rw-rw-rw-   0        0        0      240 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Fir_leaves_covered_trunk.png
--rw-rw-rw-   0        0        0      257 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Fir_snow_covered_leaves.png
--rw-rw-rw-   0        0        0      172 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Fir_trunk.png
--rw-rw-rw-   0        0        0     1568 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Gold_ore.png
--rw-rw-rw-   0        0        0     1440 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Grass.png
--rw-rw-rw-   0        0        0      166 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Ice.png
--rw-rw-rw-   0        0        0      210 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Iron_ore.png
--rw-rw-rw-   0        0        0      178 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Loess.png
--rw-rw-rw-   0        0        0     3204 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Mossy_stone.png
--rw-rw-rw-   0        0        0     3207 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Mycelium.png
--rw-rw-rw-   0        0        0      194 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Oak_branch.png
--rw-rw-rw-   0        0        0      728 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Oak_dark_leaves.png
--rw-rw-rw-   0        0        0      266 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Oak_leaves.png
--rw-rw-rw-   0        0        0      457 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Oak_leaves_covered_trunk.png
--rw-rw-rw-   0        0        0      172 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Oak_trunk.png
--rw-rw-rw-   0        0        0      231 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Red_mushroom.png
--rw-rw-rw-   0        0        0     1422 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Sand.png
--rw-rw-rw-   0        0        0     1526 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Sandstone.png
--rw-rw-rw-   0        0        0     3241 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Scaffolding.png
--rw-rw-rw-   0        0        0      207 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Shale.png
--rw-rw-rw-   0        0        0      190 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Snowman_belly.png
--rw-rw-rw-   0        0        0      236 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Snowman_head.png
--rw-rw-rw-   0        0        0      173 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Snowman_left_arm.png
--rw-rw-rw-   0        0        0      161 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Snowman_right_arm.png
--rw-rw-rw-   0        0        0      254 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Snowman_torso.png
--rw-rw-rw-   0        0        0     1936 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Snowy_dirt.png
--rw-rw-rw-   0        0        0     1525 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Snowy_grass.png
--rw-rw-rw-   0        0        0      250 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Snowy_weed.png
--rw-rw-rw-   0        0        0      212 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Stalagmite_base.png
--rw-rw-rw-   0        0        0      212 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Stalagmite_middle.png
--rw-rw-rw-   0        0        0      199 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Stalagmite_tip.png
--rw-rw-rw-   0        0        0      207 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Stalagmite_upper_middle.png
--rw-rw-rw-   0        0        0     3179 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Stone.png
--rw-rw-rw-   0        0        0      135 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/Water.png
--rw-rw-rw-   0        0        0      252 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/fir_leaves.png
--rw-rw-rw-   0        0        0      217 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/tulip.png
--rw-rw-rw-   0        0        0      235 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Images/Tiles/weed.png
-drwxrwxrwx   0        0        0        0 2023-04-06 18:53:34.934573 terrario-0.0.4/src/terrario/Props/
--rw-rw-rw-   0        0        0      720 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Props/fir.csv
--rw-rw-rw-   0        0        0      326 2023-04-06 18:06:15.000000 terrario-0.0.4/src/terrario/Props/oak_tree.csv
--rw-rw-rw-   0        0        0       58 2023-04-06 18:41:40.000000 terrario-0.0.4/src/terrario/__init__.py
--rw-rw-rw-   0        0        0       71 2023-04-06 18:07:13.000000 terrario-0.0.4/src/terrario/__main__.py
-drwxrwxrwx   0        0        0        0 2023-04-06 18:53:34.862447 terrario-0.0.4/src/terrario.egg-info/
--rw-rw-rw-   0        0        0     1341 2023-04-06 18:53:34.000000 terrario-0.0.4/src/terrario.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     2813 2023-04-06 18:53:34.000000 terrario-0.0.4/src/terrario.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 18:53:34.000000 terrario-0.0.4/src/terrario.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       81 2023-04-06 18:53:34.000000 terrario-0.0.4/src/terrario.egg-info/requires.txt
--rw-rw-rw-   0        0        0        9 2023-04-06 18:53:34.000000 terrario-0.0.4/src/terrario.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 19:06:47.505917 terrario-0.0.5/
+-rw-rw-rw-   0        0        0        0 2023-04-06 17:58:29.000000 terrario-0.0.5/LICENSE
+-rw-rw-rw-   0        0        0      178 2023-04-06 18:52:26.000000 terrario-0.0.5/MANIFEST.in
+-rw-rw-rw-   0        0        0     1341 2023-04-06 19:06:47.506918 terrario-0.0.5/PKG-INFO
+-rw-rw-rw-   0        0        0      762 2023-04-06 18:04:01.000000 terrario-0.0.5/README.md
+-rw-rw-rw-   0        0        0      152 2023-04-06 18:50:16.000000 terrario-0.0.5/pyproject.toml
+-rw-rw-rw-   0        0        0      901 2023-04-06 19:06:47.506918 terrario-0.0.5/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-06 19:06:47.428901 terrario-0.0.5/src/
+drwxrwxrwx   0        0        0        0 2023-04-06 19:06:47.436902 terrario-0.0.5/src/terrario/
+drwxrwxrwx   0        0        0        0 2023-04-06 19:06:47.446905 terrario-0.0.5/src/terrario/Classes/
+-rw-rw-rw-   0        0        0     1742 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Classes/game.py
+-rw-rw-rw-   0        0        0    10385 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Classes/map.py
+-rw-rw-rw-   0        0        0     4230 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Classes/player.py
+-rw-rw-rw-   0        0        0     6621 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Classes/props.py
+-rw-rw-rw-   0        0        0     4721 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Classes/tile.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:06:47.429900 terrario-0.0.5/src/terrario/Images/
+drwxrwxrwx   0        0        0        0 2023-04-06 19:06:47.455906 terrario-0.0.5/src/terrario/Images/Player/
+-rw-rw-rw-   0        0        0      217 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Player/DrillTip_down.png
+-rw-rw-rw-   0        0        0      213 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Player/DrillTip_left.png
+-rw-rw-rw-   0        0        0      211 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Player/DrillTip_right.png
+-rw-rw-rw-   0        0        0      217 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Player/DrillTip_up.png
+-rw-rw-rw-   0        0        0      250 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Player/Drill_down.png
+-rw-rw-rw-   0        0        0      243 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Player/Drill_left.png
+-rw-rw-rw-   0        0        0      241 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Player/Drill_right.png
+-rw-rw-rw-   0        0        0      251 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Player/Drill_up.png
+-rw-rw-rw-   0        0        0      258 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Player/Parachute.png
+drwxrwxrwx   0        0        0        0 2023-04-06 19:06:47.502917 terrario-0.0.5/src/terrario/Images/Tiles/
+-rw-rw-rw-   0        0        0      120 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Air.png
+-rw-rw-rw-   0        0        0      209 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Brown_mushroom.png
+-rw-rw-rw-   0        0        0      211 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Cactus.png
+-rw-rw-rw-   0        0        0      224 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Cactus_top.png
+-rw-rw-rw-   0        0        0      222 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Coal_ore.png
+-rw-rw-rw-   0        0        0      235 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Dead_weed.png
+-rw-rw-rw-   0        0        0     1826 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Dirt.png
+-rw-rw-rw-   0        0        0      656 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Fir_dark_leaves.png
+-rw-rw-rw-   0        0        0      546 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Fir_dark_leaves_covered_trunk.png
+-rw-rw-rw-   0        0        0      240 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Fir_leaves_covered_trunk.png
+-rw-rw-rw-   0        0        0      257 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Fir_snow_covered_leaves.png
+-rw-rw-rw-   0        0        0      172 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Fir_trunk.png
+-rw-rw-rw-   0        0        0     1568 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Gold_ore.png
+-rw-rw-rw-   0        0        0     1440 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Grass.png
+-rw-rw-rw-   0        0        0      166 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Ice.png
+-rw-rw-rw-   0        0        0      210 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Iron_ore.png
+-rw-rw-rw-   0        0        0      178 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Loess.png
+-rw-rw-rw-   0        0        0     3204 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Mossy_stone.png
+-rw-rw-rw-   0        0        0     3207 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Mycelium.png
+-rw-rw-rw-   0        0        0      194 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Oak_branch.png
+-rw-rw-rw-   0        0        0      728 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Oak_dark_leaves.png
+-rw-rw-rw-   0        0        0      266 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Oak_leaves.png
+-rw-rw-rw-   0        0        0      457 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Oak_leaves_covered_trunk.png
+-rw-rw-rw-   0        0        0      172 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Oak_trunk.png
+-rw-rw-rw-   0        0        0      231 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Red_mushroom.png
+-rw-rw-rw-   0        0        0     1422 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Sand.png
+-rw-rw-rw-   0        0        0     1526 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Sandstone.png
+-rw-rw-rw-   0        0        0     3241 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Scaffolding.png
+-rw-rw-rw-   0        0        0      207 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Shale.png
+-rw-rw-rw-   0        0        0      190 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Snowman_belly.png
+-rw-rw-rw-   0        0        0      236 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Snowman_head.png
+-rw-rw-rw-   0        0        0      173 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Snowman_left_arm.png
+-rw-rw-rw-   0        0        0      161 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Snowman_right_arm.png
+-rw-rw-rw-   0        0        0      254 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Snowman_torso.png
+-rw-rw-rw-   0        0        0     1936 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Snowy_dirt.png
+-rw-rw-rw-   0        0        0     1525 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Snowy_grass.png
+-rw-rw-rw-   0        0        0      250 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Snowy_weed.png
+-rw-rw-rw-   0        0        0      212 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Stalagmite_base.png
+-rw-rw-rw-   0        0        0      212 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Stalagmite_middle.png
+-rw-rw-rw-   0        0        0      199 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Stalagmite_tip.png
+-rw-rw-rw-   0        0        0      207 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Stalagmite_upper_middle.png
+-rw-rw-rw-   0        0        0     3179 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Stone.png
+-rw-rw-rw-   0        0        0      135 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/Water.png
+-rw-rw-rw-   0        0        0      252 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/fir_leaves.png
+-rw-rw-rw-   0        0        0      217 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/tulip.png
+-rw-rw-rw-   0        0        0      235 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Images/Tiles/weed.png
+drwxrwxrwx   0        0        0        0 2023-04-06 19:06:47.504917 terrario-0.0.5/src/terrario/Props/
+-rw-rw-rw-   0        0        0      720 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Props/fir.csv
+-rw-rw-rw-   0        0        0      326 2023-04-06 18:06:15.000000 terrario-0.0.5/src/terrario/Props/oak_tree.csv
+-rw-rw-rw-   0        0        0       58 2023-04-06 18:41:40.000000 terrario-0.0.5/src/terrario/__init__.py
+-rw-rw-rw-   0        0        0       71 2023-04-06 19:06:20.000000 terrario-0.0.5/src/terrario/__main__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:06:47.441902 terrario-0.0.5/src/terrario.egg-info/
+-rw-rw-rw-   0        0        0     1341 2023-04-06 19:06:47.000000 terrario-0.0.5/src/terrario.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     2813 2023-04-06 19:06:47.000000 terrario-0.0.5/src/terrario.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 19:06:47.000000 terrario-0.0.5/src/terrario.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       81 2023-04-06 19:06:47.000000 terrario-0.0.5/src/terrario.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        9 2023-04-06 19:06:47.000000 terrario-0.0.5/src/terrario.egg-info/top_level.txt
```

### Comparing `terrario-0.0.4/PKG-INFO` & `terrario-0.0.5/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: terrario
-Version: 0.0.4
+Version: 0.0.5
 Summary: A 2D mining game made with Pygame.
 Home-page: https://github.com/MaitreRenard18/Terrario-2
 Author: MaitreRenard18, Wagister
 Author-email: maitre.renardowo@gmail.com
 Project-URL: Bug Tracker, https://github.com/MaitreRenard18/Terrario-2/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
```

### Comparing `terrario-0.0.4/README.md` & `terrario-0.0.5/README.md`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Classes/game.py` & `terrario-0.0.5/src/terrario/Classes/game.py`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Classes/map.py` & `terrario-0.0.5/src/terrario/Classes/map.py`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Classes/player.py` & `terrario-0.0.5/src/terrario/Classes/player.py`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Classes/props.py` & `terrario-0.0.5/src/terrario/Classes/props.py`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Classes/tile.py` & `terrario-0.0.5/src/terrario/Classes/tile.py`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Dirt.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Dirt.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Fir_dark_leaves.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Fir_dark_leaves.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Fir_dark_leaves_covered_trunk.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Fir_dark_leaves_covered_trunk.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Gold_ore.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Gold_ore.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Grass.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Grass.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Mossy_stone.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Mossy_stone.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Mycelium.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Mycelium.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Oak_dark_leaves.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Oak_dark_leaves.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Sand.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Sand.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Sandstone.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Sandstone.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Scaffolding.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Scaffolding.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Snowy_dirt.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Snowy_dirt.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Snowy_grass.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Snowy_grass.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Images/Tiles/Stone.png` & `terrario-0.0.5/src/terrario/Images/Tiles/Stone.png`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario/Props/fir.csv` & `terrario-0.0.5/src/terrario/Props/fir.csv`

 * *Files identical despite different names*

### Comparing `terrario-0.0.4/src/terrario.egg-info/PKG-INFO` & `terrario-0.0.5/src/terrario.egg-info/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: terrario
-Version: 0.0.4
+Version: 0.0.5
 Summary: A 2D mining game made with Pygame.
 Home-page: https://github.com/MaitreRenard18/Terrario-2
 Author: MaitreRenard18, Wagister
 Author-email: maitre.renardowo@gmail.com
 Project-URL: Bug Tracker, https://github.com/MaitreRenard18/Terrario-2/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
```

### Comparing `terrario-0.0.4/src/terrario.egg-info/SOURCES.txt` & `terrario-0.0.5/src/terrario.egg-info/SOURCES.txt`

 * *Files identical despite different names*
