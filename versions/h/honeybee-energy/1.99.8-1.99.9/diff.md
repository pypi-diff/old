# Comparing `tmp/honeybee-energy-1.99.8.tar.gz` & `tmp/honeybee-energy-1.99.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/honeybee-energy-1.99.8.tar", last modified: Sat Feb 25 16:38:02 2023, max compression
+gzip compressed data, was "dist/honeybee-energy-1.99.9.tar", last modified: Tue Feb 28 21:50:50 2023, max compression
```

## Comparing `honeybee-energy-1.99.8.tar` & `honeybee-energy-1.99.9.tar`

### file list

```diff
@@ -1,186 +1,186 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/CODE_OF_CONDUCT.md
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/CONTRIBUTING.md
--rw-r--r--   0 runner    (1001) docker     (123)    34523 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      600 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2616 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1990 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      811 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/dev-requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/
--rw-r--r--   0 runner    (1001) docker     (123)      802 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       80 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4683 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/_extend_honeybee.py
--rw-r--r--   0 runner    (1001) docker     (123)      576 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/altnumber.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    27352 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/create.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/data/
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1558 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/data/constructions.csv
--rw-r--r--   0 runner    (1001) docker     (123)      267 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/data/fen_ratios.csv
--rw-r--r--   0 runner    (1001) docker     (123)      362 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/data/lpd_building.csv
--rw-r--r--   0 runner    (1001) docker     (123)     2272 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/data/pci_2016.csv
--rw-r--r--   0 runner    (1001) docker     (123)     2253 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/data/pci_2019.csv
--rw-r--r--   0 runner    (1001) docker     (123)     2312 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/data/pci_2022.csv
--rw-r--r--   0 runner    (1001) docker     (123)      410 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/data/shw.csv
--rw-r--r--   0 runner    (1001) docker     (123)    25217 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/pci.py
--rw-r--r--   0 runner    (1001) docker     (123)    17047 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/baseline/result.py
--rw-r--r--   0 runner    (1001) docker     (123)     4970 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/boundarycondition.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/cli/
--rw-r--r--   0 runner    (1001) docker     (123)     2484 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    24345 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/cli/baseline.py
--rw-r--r--   0 runner    (1001) docker     (123)    12021 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/cli/edit.py
--rw-r--r--   0 runner    (1001) docker     (123)    28228 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/cli/lib.py
--rw-r--r--   0 runner    (1001) docker     (123)    33329 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/cli/result.py
--rw-r--r--   0 runner    (1001) docker     (123)     3815 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/cli/setconfig.py
--rw-r--r--   0 runner    (1001) docker     (123)    28623 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/cli/settings.py
--rw-r--r--   0 runner    (1001) docker     (123)    19200 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/cli/simulate.py
--rw-r--r--   0 runner    (1001) docker     (123)    33290 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/cli/translate.py
--rw-r--r--   0 runner    (1001) docker     (123)     9339 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/cli/validate.py
--rw-r--r--   0 runner    (1001) docker     (123)      344 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/config.json
--rw-r--r--   0 runner    (1001) docker     (123)    35402 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/construction/
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/construction/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14321 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/construction/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)    11804 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/construction/air.py
--rw-r--r--   0 runner    (1001) docker     (123)     4334 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/construction/dictutil.py
--rw-r--r--   0 runner    (1001) docker     (123)    22389 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/construction/dynamic.py
--rw-r--r--   0 runner    (1001) docker     (123)    17577 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/construction/opaque.py
--rw-r--r--   0 runner    (1001) docker     (123)    11907 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/construction/shade.py
--rw-r--r--   0 runner    (1001) docker     (123)    48081 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/construction/window.py
--rw-r--r--   0 runner    (1001) docker     (123)    33830 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/construction/windowshade.py
--rw-r--r--   0 runner    (1001) docker     (123)    71467 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/constructionset.py
--rw-r--r--   0 runner    (1001) docker     (123)     2457 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/dictutil.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/
--rw-r--r--   0 runner    (1001) docker     (123)      886 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4359 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     9944 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/_template.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/allair/
--rw-r--r--   0 runner    (1001) docker     (123)     1129 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/allair/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14887 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/allair/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     6589 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/allair/furnace.py
--rw-r--r--   0 runner    (1001) docker     (123)     4671 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/allair/psz.py
--rw-r--r--   0 runner    (1001) docker     (123)     6013 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/allair/ptac.py
--rw-r--r--   0 runner    (1001) docker     (123)     4230 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/allair/pvav.py
--rw-r--r--   0 runner    (1001) docker     (123)     4818 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/allair/vav.py
--rw-r--r--   0 runner    (1001) docker     (123)     7760 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/detailed.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/doas/
--rw-r--r--   0 runner    (1001) docker     (123)     1539 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/doas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15467 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/doas/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     5411 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/doas/fcu.py
--rw-r--r--   0 runner    (1001) docker     (123)    14830 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/doas/radiant.py
--rw-r--r--   0 runner    (1001) docker     (123)     3456 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/doas/vrf.py
--rw-r--r--   0 runner    (1001) docker     (123)     3875 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/doas/wshp.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/
--rw-r--r--   0 runner    (1001) docker     (123)     1168 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7023 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/baseboard.py
--rw-r--r--   0 runner    (1001) docker     (123)     2529 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/evapcool.py
--rw-r--r--   0 runner    (1001) docker     (123)     2997 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/fcu.py
--rw-r--r--   0 runner    (1001) docker     (123)     1595 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/gasunit.py
--rw-r--r--   0 runner    (1001) docker     (123)    10710 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/radiant.py
--rw-r--r--   0 runner    (1001) docker     (123)     2745 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/residential.py
--rw-r--r--   0 runner    (1001) docker     (123)     1729 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/vrf.py
--rw-r--r--   0 runner    (1001) docker     (123)     2291 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/windowac.py
--rw-r--r--   0 runner    (1001) docker     (123)     1950 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/wshp.py
--rw-r--r--   0 runner    (1001) docker     (123)    30175 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/hvac/idealair.py
--rw-r--r--   0 runner    (1001) docker     (123)    11769 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/internalmass.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/lib/
--rw-r--r--   0 runner    (1001) docker     (123)       71 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7944 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/_loadconstructions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3744 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/_loadconstructionsets.py
--rw-r--r--   0 runner    (1001) docker     (123)     3251 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/_loadmaterials.py
--rw-r--r--   0 runner    (1001) docker     (123)     4021 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/_loadprogramtypes.py
--rw-r--r--   0 runner    (1001) docker     (123)     3379 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/_loadschedules.py
--rw-r--r--   0 runner    (1001) docker     (123)     2682 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/_loadtypelimits.py
--rw-r--r--   0 runner    (1001) docker     (123)     7048 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/constructions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2439 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/constructionsets.py
--rw-r--r--   0 runner    (1001) docker     (123)     3002 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/materials.py
--rw-r--r--   0 runner    (1001) docker     (123)     3927 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/programtypes.py
--rw-r--r--   0 runner    (1001) docker     (123)     1872 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/schedules.py
--rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/lib/scheduletypelimits.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/load/
--rw-r--r--   0 runner    (1001) docker     (123)       40 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/load/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6813 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/load/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)    15522 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/load/daylight.py
--rw-r--r--   0 runner    (1001) docker     (123)     1918 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/load/dictutil.py
--rw-r--r--   0 runner    (1001) docker     (123)    35187 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/load/equipment.py
--rw-r--r--   0 runner    (1001) docker     (123)    25881 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/load/hotwater.py
--rw-r--r--   0 runner    (1001) docker     (123)    21275 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/load/infiltration.py
--rw-r--r--   0 runner    (1001) docker     (123)    21938 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/load/lighting.py
--rw-r--r--   0 runner    (1001) docker     (123)    23149 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/load/people.py
--rw-r--r--   0 runner    (1001) docker     (123)    18642 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/load/process.py
--rw-r--r--   0 runner    (1001) docker     (123)    31076 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/load/setpoint.py
--rw-r--r--   0 runner    (1001) docker     (123)    19749 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/load/ventilation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/material/
--rw-r--r--   0 runner    (1001) docker     (123)       33 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/material/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5467 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/material/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2747 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/material/dictutil.py
--rw-r--r--   0 runner    (1001) docker     (123)    14432 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/material/frame.py
--rw-r--r--   0 runner    (1001) docker     (123)    44498 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/material/gas.py
--rw-r--r--   0 runner    (1001) docker     (123)    33657 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/material/glazing.py
--rw-r--r--   0 runner    (1001) docker     (123)    53627 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/material/opaque.py
--rw-r--r--   0 runner    (1001) docker     (123)    62083 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/material/shade.py
--rw-r--r--   0 runner    (1001) docker     (123)    16930 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/measure.py
--rw-r--r--   0 runner    (1001) docker     (123)    34222 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/programtype.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/properties/
--rw-r--r--   0 runner    (1001) docker     (123)       34 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/properties/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15369 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/properties/aperture.py
--rw-r--r--   0 runner    (1001) docker     (123)    15544 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/properties/door.py
--rw-r--r--   0 runner    (1001) docker     (123)     6886 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/properties/extension.py
--rw-r--r--   0 runner    (1001) docker     (123)    11132 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/properties/face.py
--rw-r--r--   0 runner    (1001) docker     (123)    80680 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/properties/model.py
--rw-r--r--   0 runner    (1001) docker     (123)    75701 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/properties/room.py
--rw-r--r--   0 runner    (1001) docker     (123)    12419 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/properties/shade.py
--rw-r--r--   0 runner    (1001) docker     (123)     1856 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/reader.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/result/
--rw-r--r--   0 runner    (1001) docker     (123)       43 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/result/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    27428 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/result/colorobj.py
--rw-r--r--   0 runner    (1001) docker     (123)    12415 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/result/emissions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3312 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/result/err.py
--rw-r--r--   0 runner    (1001) docker     (123)     3943 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/result/eui.py
--rw-r--r--   0 runner    (1001) docker     (123)    32402 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/result/loadbalance.py
--rw-r--r--   0 runner    (1001) docker     (123)     7464 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/result/match.py
--rw-r--r--   0 runner    (1001) docker     (123)     2672 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/result/osw.py
--rw-r--r--   0 runner    (1001) docker     (123)     1873 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/result/rdd.py
--rw-r--r--   0 runner    (1001) docker     (123)     7532 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/result/zsz.py
--rw-r--r--   0 runner    (1001) docker     (123)    42915 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/run.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/schedule/
--rw-r--r--   0 runner    (1001) docker     (123)       33 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/schedule/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    27426 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/schedule/day.py
--rw-r--r--   0 runner    (1001) docker     (123)     2550 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/schedule/dictutil.py
--rw-r--r--   0 runner    (1001) docker     (123)    41584 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/schedule/fixedinterval.py
--rw-r--r--   0 runner    (1001) docker     (123)    24814 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/schedule/rule.py
--rw-r--r--   0 runner    (1001) docker     (123)    84172 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/schedule/ruleset.py
--rw-r--r--   0 runner    (1001) docker     (123)    11870 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/schedule/typelimit.py
--rw-r--r--   0 runner    (1001) docker     (123)    12726 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/shw.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/simulation/
--rw-r--r--   0 runner    (1001) docker     (123)       43 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/simulation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7911 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/simulation/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     6650 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/simulation/daylightsaving.py
--rw-r--r--   0 runner    (1001) docker     (123)     2252 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/simulation/dictutil.py
--rw-r--r--   0 runner    (1001) docker     (123)    26353 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/simulation/output.py
--rw-r--r--   0 runner    (1001) docker     (123)    22528 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/simulation/parameter.py
--rw-r--r--   0 runner    (1001) docker     (123)    17217 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/simulation/runperiod.py
--rw-r--r--   0 runner    (1001) docker     (123)    11264 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/simulation/shadowcalculation.py
--rw-r--r--   0 runner    (1001) docker     (123)    19627 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/simulation/sizing.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy/ventcool/
--rw-r--r--   0 runner    (1001) docker     (123)      173 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/ventcool/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2798 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/ventcool/_crack_data.py
--rw-r--r--   0 runner    (1001) docker     (123)    14531 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/ventcool/afn.py
--rw-r--r--   0 runner    (1001) docker     (123)    11987 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/ventcool/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     4565 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/ventcool/crack.py
--rw-r--r--   0 runner    (1001) docker     (123)    16355 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/ventcool/opening.py
--rw-r--r--   0 runner    (1001) docker     (123)    14423 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/ventcool/simulation.py
--rw-r--r--   0 runner    (1001) docker     (123)    35841 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/honeybee_energy/writer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2616 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5746 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       63 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       95 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/honeybee_energy.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      181 2023-02-25 16:38:02.000000 honeybee-energy-1.99.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1445 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/setup.py
--rw-r--r--   0 runner    (1001) docker     (123)       33 2023-02-25 16:36:43.000000 honeybee-energy-1.99.8/standards-requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/CODE_OF_CONDUCT.md
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/CONTRIBUTING.md
+-rw-r--r--   0 runner    (1001) docker     (123)    34523 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      600 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2616 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1990 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      811 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/dev-requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/
+-rw-r--r--   0 runner    (1001) docker     (123)      802 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       80 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4683 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/_extend_honeybee.py
+-rw-r--r--   0 runner    (1001) docker     (123)      576 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/altnumber.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27352 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/create.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/data/
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1558 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/data/constructions.csv
+-rw-r--r--   0 runner    (1001) docker     (123)      267 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/data/fen_ratios.csv
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/data/lpd_building.csv
+-rw-r--r--   0 runner    (1001) docker     (123)     2272 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/data/pci_2016.csv
+-rw-r--r--   0 runner    (1001) docker     (123)     2253 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/data/pci_2019.csv
+-rw-r--r--   0 runner    (1001) docker     (123)     2312 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/data/pci_2022.csv
+-rw-r--r--   0 runner    (1001) docker     (123)      410 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/data/shw.csv
+-rw-r--r--   0 runner    (1001) docker     (123)    25217 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/pci.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17047 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/baseline/result.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4970 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/boundarycondition.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)     2484 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24345 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/cli/baseline.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12021 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/cli/edit.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28228 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/cli/lib.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33329 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/cli/result.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3815 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/cli/setconfig.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28623 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/cli/settings.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19200 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/cli/simulate.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33290 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/cli/translate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9339 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/cli/validate.py
+-rw-r--r--   0 runner    (1001) docker     (123)      344 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/config.json
+-rw-r--r--   0 runner    (1001) docker     (123)    35402 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/construction/
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/construction/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14321 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/construction/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11804 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/construction/air.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4334 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/construction/dictutil.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22389 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/construction/dynamic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17577 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/construction/opaque.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11907 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/construction/shade.py
+-rw-r--r--   0 runner    (1001) docker     (123)    48081 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/construction/window.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33830 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/construction/windowshade.py
+-rw-r--r--   0 runner    (1001) docker     (123)    71467 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/constructionset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2457 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/dictutil.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/
+-rw-r--r--   0 runner    (1001) docker     (123)      886 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4359 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9944 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/_template.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/allair/
+-rw-r--r--   0 runner    (1001) docker     (123)     1129 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/allair/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14887 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/allair/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6589 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/allair/furnace.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4671 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/allair/psz.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6013 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/allair/ptac.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4230 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/allair/pvav.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4818 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/allair/vav.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7760 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/detailed.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/doas/
+-rw-r--r--   0 runner    (1001) docker     (123)     1539 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/doas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15467 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/doas/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5411 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/doas/fcu.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14830 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/doas/radiant.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3456 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/doas/vrf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3875 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/doas/wshp.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/
+-rw-r--r--   0 runner    (1001) docker     (123)     1168 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7023 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/baseboard.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2529 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/evapcool.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2997 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/fcu.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1595 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/gasunit.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10710 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/radiant.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2745 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/residential.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1729 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/vrf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2291 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/windowac.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1950 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/wshp.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30175 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/hvac/idealair.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11769 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/internalmass.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/lib/
+-rw-r--r--   0 runner    (1001) docker     (123)       71 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7944 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/_loadconstructions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3744 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/_loadconstructionsets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3251 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/_loadmaterials.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4021 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/_loadprogramtypes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3379 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/_loadschedules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2682 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/_loadtypelimits.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7048 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/constructions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2439 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/constructionsets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3002 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/materials.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3927 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/programtypes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1872 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/schedules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/lib/scheduletypelimits.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/load/
+-rw-r--r--   0 runner    (1001) docker     (123)       40 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/load/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6813 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/load/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15522 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/load/daylight.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1918 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/load/dictutil.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35187 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/load/equipment.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25881 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/load/hotwater.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21275 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/load/infiltration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21938 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/load/lighting.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23149 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/load/people.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18642 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/load/process.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31076 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/load/setpoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19749 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/load/ventilation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/material/
+-rw-r--r--   0 runner    (1001) docker     (123)       33 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/material/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5467 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/material/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2747 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/material/dictutil.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14432 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/material/frame.py
+-rw-r--r--   0 runner    (1001) docker     (123)    44498 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/material/gas.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33657 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/material/glazing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    53627 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/material/opaque.py
+-rw-r--r--   0 runner    (1001) docker     (123)    62083 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/material/shade.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16930 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/measure.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34222 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/programtype.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/properties/
+-rw-r--r--   0 runner    (1001) docker     (123)       34 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/properties/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15369 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/properties/aperture.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15544 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/properties/door.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6886 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/properties/extension.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11132 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/properties/face.py
+-rw-r--r--   0 runner    (1001) docker     (123)    80680 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/properties/model.py
+-rw-r--r--   0 runner    (1001) docker     (123)    77265 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/properties/room.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12419 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/properties/shade.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1856 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/reader.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/result/
+-rw-r--r--   0 runner    (1001) docker     (123)       43 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/result/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27428 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/result/colorobj.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12415 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/result/emissions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3312 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/result/err.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3943 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/result/eui.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32402 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/result/loadbalance.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7464 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/result/match.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2672 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/result/osw.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1873 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/result/rdd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7532 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/result/zsz.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42915 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/run.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/schedule/
+-rw-r--r--   0 runner    (1001) docker     (123)       33 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/schedule/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27426 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/schedule/day.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2550 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/schedule/dictutil.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41584 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/schedule/fixedinterval.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24814 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/schedule/rule.py
+-rw-r--r--   0 runner    (1001) docker     (123)    84172 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/schedule/ruleset.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11870 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/schedule/typelimit.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12726 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/shw.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/simulation/
+-rw-r--r--   0 runner    (1001) docker     (123)       43 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/simulation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7911 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/simulation/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6650 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/simulation/daylightsaving.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2252 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/simulation/dictutil.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26353 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/simulation/output.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22528 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/simulation/parameter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17217 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/simulation/runperiod.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11264 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/simulation/shadowcalculation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19627 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/simulation/sizing.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy/ventcool/
+-rw-r--r--   0 runner    (1001) docker     (123)      173 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/ventcool/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2798 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/ventcool/_crack_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14531 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/ventcool/afn.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11987 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/ventcool/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4565 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/ventcool/crack.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16355 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/ventcool/opening.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14423 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/ventcool/simulation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35841 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/honeybee_energy/writer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2616 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5746 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       63 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       95 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/honeybee_energy.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      181 2023-02-28 21:50:49.000000 honeybee-energy-1.99.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1445 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)       33 2023-02-28 21:49:30.000000 honeybee-energy-1.99.9/standards-requirements.txt
```

### Comparing `honeybee-energy-1.99.8/LICENSE` & `honeybee-energy-1.99.9/LICENSE`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/MANIFEST.in` & `honeybee-energy-1.99.9/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/PKG-INFO` & `honeybee-energy-1.99.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: honeybee-energy
-Version: 1.99.8
+Version: 1.99.9
 Summary: Energy simulation library for honeybee.
 Home-page: https://github.com/ladybug-tools/honeybee-energy
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: AGPL-3.0
 Classifier: Programming Language :: Python :: 2.7
 Classifier: Programming Language :: Python :: 3.7
```

### Comparing `honeybee-energy-1.99.8/README.md` & `honeybee-energy-1.99.9/README.md`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/dev-requirements.txt` & `honeybee-energy-1.99.9/dev-requirements.txt`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/__init__.py` & `honeybee-energy-1.99.9/honeybee_energy/__init__.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/_extend_honeybee.py` & `honeybee-energy-1.99.9/honeybee_energy/_extend_honeybee.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/altnumber.py` & `honeybee-energy-1.99.9/honeybee_energy/altnumber.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/baseline/create.py` & `honeybee-energy-1.99.9/honeybee_energy/baseline/create.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/baseline/data/constructions.csv` & `honeybee-energy-1.99.9/honeybee_energy/baseline/data/constructions.csv`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/baseline/data/pci_2016.csv` & `honeybee-energy-1.99.9/honeybee_energy/baseline/data/pci_2016.csv`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/baseline/data/pci_2019.csv` & `honeybee-energy-1.99.9/honeybee_energy/baseline/data/pci_2019.csv`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/baseline/data/pci_2022.csv` & `honeybee-energy-1.99.9/honeybee_energy/baseline/data/pci_2022.csv`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/baseline/pci.py` & `honeybee-energy-1.99.9/honeybee_energy/baseline/pci.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/baseline/result.py` & `honeybee-energy-1.99.9/honeybee_energy/baseline/result.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/boundarycondition.py` & `honeybee-energy-1.99.9/honeybee_energy/boundarycondition.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/cli/__init__.py` & `honeybee-energy-1.99.9/honeybee_energy/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/cli/baseline.py` & `honeybee-energy-1.99.9/honeybee_energy/cli/baseline.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/cli/edit.py` & `honeybee-energy-1.99.9/honeybee_energy/cli/edit.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/cli/lib.py` & `honeybee-energy-1.99.9/honeybee_energy/cli/lib.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/cli/result.py` & `honeybee-energy-1.99.9/honeybee_energy/cli/result.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/cli/setconfig.py` & `honeybee-energy-1.99.9/honeybee_energy/cli/setconfig.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/cli/settings.py` & `honeybee-energy-1.99.9/honeybee_energy/cli/settings.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/cli/simulate.py` & `honeybee-energy-1.99.9/honeybee_energy/cli/simulate.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/cli/translate.py` & `honeybee-energy-1.99.9/honeybee_energy/cli/translate.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/cli/validate.py` & `honeybee-energy-1.99.9/honeybee_energy/cli/validate.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/config.py` & `honeybee-energy-1.99.9/honeybee_energy/config.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/construction/_base.py` & `honeybee-energy-1.99.9/honeybee_energy/construction/_base.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/construction/air.py` & `honeybee-energy-1.99.9/honeybee_energy/construction/air.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/construction/dictutil.py` & `honeybee-energy-1.99.9/honeybee_energy/construction/dictutil.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/construction/dynamic.py` & `honeybee-energy-1.99.9/honeybee_energy/construction/dynamic.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/construction/opaque.py` & `honeybee-energy-1.99.9/honeybee_energy/construction/opaque.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/construction/shade.py` & `honeybee-energy-1.99.9/honeybee_energy/construction/shade.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/construction/window.py` & `honeybee-energy-1.99.9/honeybee_energy/construction/window.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/construction/windowshade.py` & `honeybee-energy-1.99.9/honeybee_energy/construction/windowshade.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/constructionset.py` & `honeybee-energy-1.99.9/honeybee_energy/constructionset.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/dictutil.py` & `honeybee-energy-1.99.9/honeybee_energy/dictutil.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/__init__.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/__init__.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/_base.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/_base.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/_template.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/_template.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/allair/__init__.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/allair/__init__.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/allair/_base.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/allair/_base.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/allair/furnace.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/allair/furnace.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/allair/psz.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/allair/psz.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/allair/ptac.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/allair/ptac.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/allair/pvav.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/allair/pvav.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/allair/vav.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/allair/vav.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/detailed.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/detailed.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/doas/__init__.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/doas/__init__.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/doas/_base.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/doas/_base.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/doas/fcu.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/doas/fcu.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/doas/radiant.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/doas/radiant.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/doas/vrf.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/doas/vrf.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/doas/wshp.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/doas/wshp.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/__init__.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/__init__.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/_base.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/_base.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/baseboard.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/baseboard.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/evapcool.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/evapcool.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/fcu.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/fcu.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/gasunit.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/gasunit.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/radiant.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/radiant.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/residential.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/residential.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/vrf.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/vrf.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/windowac.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/windowac.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/heatcool/wshp.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/heatcool/wshp.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/hvac/idealair.py` & `honeybee-energy-1.99.9/honeybee_energy/hvac/idealair.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/internalmass.py` & `honeybee-energy-1.99.9/honeybee_energy/internalmass.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/lib/_loadconstructions.py` & `honeybee-energy-1.99.9/honeybee_energy/lib/_loadconstructions.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/lib/_loadconstructionsets.py` & `honeybee-energy-1.99.9/honeybee_energy/lib/_loadconstructionsets.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/lib/_loadmaterials.py` & `honeybee-energy-1.99.9/honeybee_energy/lib/_loadmaterials.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/lib/_loadprogramtypes.py` & `honeybee-energy-1.99.9/honeybee_energy/lib/_loadprogramtypes.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/lib/_loadschedules.py` & `honeybee-energy-1.99.9/honeybee_energy/lib/_loadschedules.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/lib/_loadtypelimits.py` & `honeybee-energy-1.99.9/honeybee_energy/lib/_loadtypelimits.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/lib/constructions.py` & `honeybee-energy-1.99.9/honeybee_energy/lib/constructions.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/lib/constructionsets.py` & `honeybee-energy-1.99.9/honeybee_energy/lib/constructionsets.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/lib/materials.py` & `honeybee-energy-1.99.9/honeybee_energy/lib/materials.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/lib/programtypes.py` & `honeybee-energy-1.99.9/honeybee_energy/lib/programtypes.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/lib/schedules.py` & `honeybee-energy-1.99.9/honeybee_energy/lib/schedules.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/lib/scheduletypelimits.py` & `honeybee-energy-1.99.9/honeybee_energy/lib/scheduletypelimits.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/load/_base.py` & `honeybee-energy-1.99.9/honeybee_energy/load/_base.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/load/daylight.py` & `honeybee-energy-1.99.9/honeybee_energy/load/daylight.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/load/dictutil.py` & `honeybee-energy-1.99.9/honeybee_energy/load/dictutil.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/load/equipment.py` & `honeybee-energy-1.99.9/honeybee_energy/load/equipment.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/load/hotwater.py` & `honeybee-energy-1.99.9/honeybee_energy/load/hotwater.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/load/infiltration.py` & `honeybee-energy-1.99.9/honeybee_energy/load/infiltration.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/load/lighting.py` & `honeybee-energy-1.99.9/honeybee_energy/load/lighting.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/load/people.py` & `honeybee-energy-1.99.9/honeybee_energy/load/people.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/load/process.py` & `honeybee-energy-1.99.9/honeybee_energy/load/process.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/load/setpoint.py` & `honeybee-energy-1.99.9/honeybee_energy/load/setpoint.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/load/ventilation.py` & `honeybee-energy-1.99.9/honeybee_energy/load/ventilation.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/material/_base.py` & `honeybee-energy-1.99.9/honeybee_energy/material/_base.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/material/dictutil.py` & `honeybee-energy-1.99.9/honeybee_energy/material/dictutil.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/material/frame.py` & `honeybee-energy-1.99.9/honeybee_energy/material/frame.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/material/gas.py` & `honeybee-energy-1.99.9/honeybee_energy/material/gas.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/material/glazing.py` & `honeybee-energy-1.99.9/honeybee_energy/material/glazing.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/material/opaque.py` & `honeybee-energy-1.99.9/honeybee_energy/material/opaque.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/material/shade.py` & `honeybee-energy-1.99.9/honeybee_energy/material/shade.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/measure.py` & `honeybee-energy-1.99.9/honeybee_energy/measure.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/programtype.py` & `honeybee-energy-1.99.9/honeybee_energy/programtype.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/properties/aperture.py` & `honeybee-energy-1.99.9/honeybee_energy/properties/aperture.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/properties/door.py` & `honeybee-energy-1.99.9/honeybee_energy/properties/door.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/properties/extension.py` & `honeybee-energy-1.99.9/honeybee_energy/properties/extension.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/properties/face.py` & `honeybee-energy-1.99.9/honeybee_energy/properties/face.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/properties/model.py` & `honeybee-energy-1.99.9/honeybee_energy/properties/model.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/properties/room.py` & `honeybee-energy-1.99.9/honeybee_energy/properties/room.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # coding=utf-8
 """Room Energy Properties."""
 # import honeybee-core and ladybug-geometry modules
-from ladybug_geometry.geometry2d.pointvector import Vector2D
-from ladybug_geometry.geometry3d.pointvector import Point3D
+from ladybug_geometry.geometry2d import Vector2D
+from ladybug_geometry.geometry3d import Vector3D, Point3D, Polyline3D, Face3D, Polyface3D
 from honeybee.checkdup import is_equivalent
 from honeybee.boundarycondition import Outdoors, Ground, Surface, boundary_conditions
 from honeybee.facetype import Wall, RoofCeiling, Floor, AirBoundary
 from honeybee.units import conversion_factor_to_meters
 from honeybee.aperture import Aperture
 
 # import the main types of assignable objects
@@ -713,20 +713,23 @@
                 new_vent = self.ventilation.duplicate()
                 new_vent.schedule = self.hvac.doas_availability_schedule
                 self.ventilation = new_vent
         self.hvac = i_sys
 
     def add_daylight_control_to_center(
             self, distance_from_floor, illuminance_setpoint=300, control_fraction=1,
-            min_power_input=0.3, min_light_output=0.2, off_at_minimum=False):
+            min_power_input=0.3, min_light_output=0.2, off_at_minimum=False,
+            tolerance=0.01):
         """Try to assign a DaylightingControl object to the center of the Room.
 
         If the Room is too concave and the center point does not lie within the
-        Room volume, this method wil return None and no daylighting control will
-        be assigned.
+        Room volume, the pole of inaccessibility across the floor geometry will
+        be used. If the concave Room has no floors or the pole of inaccessibility
+        does not exist inside the Room, this method wil return None and no
+        daylighting control will be assigned.
 
         Args:
             distance_from_floor: A number for the distance that the daylight sensor
                 is from the floor. Typical values are around 0.8 meters.
             illuminance_setpoint: A number for the illuminance setpoint in lux
                 beyond which electric lights are dimmed if there is sufficient
                 daylight. (Default: 300 lux).
@@ -741,28 +744,53 @@
                 lighting system can dim down to, expressed as a fraction of maximum
                 input power. (Default: 0.3).
             min_light_output: A number between 0 and 1 the lowest lighting output the
                 lighting system can dim down to, expressed as a fraction of maximum
                 light output. (Default: 0.2).
             off_at_minimum: Boolean to note whether lights should switch off completely
                 when they get to the minimum power input. (Default: False).
+            tolerance: The maximum difference between x, y, and z values at which
+                vertices are considered equivalent. (Default: 0.01, suitable for
+                objects in meters).
 
         Returns:
             A DaylightingControl object if the sensor was successfully assigned
-            to the center of the Room. Will be None if the zone was so concave
-            that a sensor would not be assigned.
+            to the Room. Will be None if the Room was too short or so concave
+            that a sensor could not be assigned.
         """
-        cen_pt, min_pt = self.host.geometry.center, self.host.geometry.min
+        # first compute the Room center point and check the distance_from_floor
+        r_geo = self.host.geometry
+        cen_pt, min_pt, max_pt = r_geo.center, r_geo.min, r_geo.max
+        if max_pt.z - min_pt.z < distance_from_floor:
+            return None
         sensor_pt = Point3D(cen_pt.x, cen_pt.y, min_pt.z + distance_from_floor)
-        if self.host.geometry.is_point_inside(sensor_pt):
-            dl_control = DaylightingControl(
-                sensor_pt, illuminance_setpoint, control_fraction,
-                min_power_input, min_light_output, off_at_minimum)
-            self.daylighting_control = dl_control
-            return dl_control
+        # if the point is not inside the room, try checking the pole of inaccessibility
+        if not r_geo.is_point_inside(sensor_pt):
+            floor_faces = [face.geometry for face in self.host.faces
+                           if isinstance(face.type, Floor)]
+            if len(floor_faces) == 0:
+                return None
+            if len(floor_faces) == 1:
+                flr_geo = floor_faces[0]
+            else:
+                flr_pf = Polyface3D.from_faces(floor_faces, tolerance)
+                flr_outline = Polyline3D.join_segments(flr_pf.naked_edges, tolerance)[0]
+                flr_geo = Face3D(flr_outline.vertices[:-1])
+            min_dim = min((max_pt.x - min_pt.x, max_pt.y - min_pt.y))
+            p_tol = min_dim / 100
+            sensor_pt = flr_geo.pole_of_inaccessibility(p_tol)
+            sensor_pt = sensor_pt.move(Vector3D(0, 0, distance_from_floor))
+            if not r_geo.is_point_inside(sensor_pt):
+                return None
+        # create the daylight control sensor at the point
+        dl_control = DaylightingControl(
+            sensor_pt, illuminance_setpoint, control_fraction,
+            min_power_input, min_light_output, off_at_minimum)
+        self.daylighting_control = dl_control
+        return dl_control
 
     def assign_ventilation_opening(self, vent_opening):
         """Assign a VentilationOpening object to all operable Apertures on this Room.
 
         This method will handle the duplication of the VentilationOpening object to
         ensure that each aperture gets a unique object that can export the correct
         area and height properties of its parent.
```

### Comparing `honeybee-energy-1.99.8/honeybee_energy/properties/shade.py` & `honeybee-energy-1.99.9/honeybee_energy/properties/shade.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/reader.py` & `honeybee-energy-1.99.9/honeybee_energy/reader.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/result/colorobj.py` & `honeybee-energy-1.99.9/honeybee_energy/result/colorobj.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/result/emissions.py` & `honeybee-energy-1.99.9/honeybee_energy/result/emissions.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/result/err.py` & `honeybee-energy-1.99.9/honeybee_energy/result/err.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/result/eui.py` & `honeybee-energy-1.99.9/honeybee_energy/result/eui.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/result/loadbalance.py` & `honeybee-energy-1.99.9/honeybee_energy/result/loadbalance.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/result/match.py` & `honeybee-energy-1.99.9/honeybee_energy/result/match.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/result/osw.py` & `honeybee-energy-1.99.9/honeybee_energy/result/osw.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/result/rdd.py` & `honeybee-energy-1.99.9/honeybee_energy/result/rdd.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/result/zsz.py` & `honeybee-energy-1.99.9/honeybee_energy/result/zsz.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/run.py` & `honeybee-energy-1.99.9/honeybee_energy/run.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/schedule/day.py` & `honeybee-energy-1.99.9/honeybee_energy/schedule/day.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/schedule/dictutil.py` & `honeybee-energy-1.99.9/honeybee_energy/schedule/dictutil.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/schedule/fixedinterval.py` & `honeybee-energy-1.99.9/honeybee_energy/schedule/fixedinterval.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/schedule/rule.py` & `honeybee-energy-1.99.9/honeybee_energy/schedule/rule.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/schedule/ruleset.py` & `honeybee-energy-1.99.9/honeybee_energy/schedule/ruleset.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/schedule/typelimit.py` & `honeybee-energy-1.99.9/honeybee_energy/schedule/typelimit.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/shw.py` & `honeybee-energy-1.99.9/honeybee_energy/shw.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/simulation/control.py` & `honeybee-energy-1.99.9/honeybee_energy/simulation/control.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/simulation/daylightsaving.py` & `honeybee-energy-1.99.9/honeybee_energy/simulation/daylightsaving.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/simulation/dictutil.py` & `honeybee-energy-1.99.9/honeybee_energy/simulation/dictutil.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/simulation/output.py` & `honeybee-energy-1.99.9/honeybee_energy/simulation/output.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/simulation/parameter.py` & `honeybee-energy-1.99.9/honeybee_energy/simulation/parameter.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/simulation/runperiod.py` & `honeybee-energy-1.99.9/honeybee_energy/simulation/runperiod.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/simulation/shadowcalculation.py` & `honeybee-energy-1.99.9/honeybee_energy/simulation/shadowcalculation.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/simulation/sizing.py` & `honeybee-energy-1.99.9/honeybee_energy/simulation/sizing.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/ventcool/_crack_data.py` & `honeybee-energy-1.99.9/honeybee_energy/ventcool/_crack_data.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/ventcool/afn.py` & `honeybee-energy-1.99.9/honeybee_energy/ventcool/afn.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/ventcool/control.py` & `honeybee-energy-1.99.9/honeybee_energy/ventcool/control.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/ventcool/crack.py` & `honeybee-energy-1.99.9/honeybee_energy/ventcool/crack.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/ventcool/opening.py` & `honeybee-energy-1.99.9/honeybee_energy/ventcool/opening.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/ventcool/simulation.py` & `honeybee-energy-1.99.9/honeybee_energy/ventcool/simulation.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy/writer.py` & `honeybee-energy-1.99.9/honeybee_energy/writer.py`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/honeybee_energy.egg-info/PKG-INFO` & `honeybee-energy-1.99.9/honeybee_energy.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: honeybee-energy
-Version: 1.99.8
+Version: 1.99.9
 Summary: Energy simulation library for honeybee.
 Home-page: https://github.com/ladybug-tools/honeybee-energy
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: AGPL-3.0
 Classifier: Programming Language :: Python :: 2.7
 Classifier: Programming Language :: Python :: 3.7
```

### Comparing `honeybee-energy-1.99.8/honeybee_energy.egg-info/SOURCES.txt` & `honeybee-energy-1.99.9/honeybee_energy.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `honeybee-energy-1.99.8/setup.py` & `honeybee-energy-1.99.9/setup.py`

 * *Files identical despite different names*

