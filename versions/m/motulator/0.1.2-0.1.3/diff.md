# Comparing `tmp/motulator-0.1.2.tar.gz` & `tmp/motulator-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "motulator-0.1.2.tar", last modified: Thu Nov 17 19:23:05 2022, max compression
+gzip compressed data, was "motulator-0.1.3.tar", last modified: Thu Apr  6 21:26:08 2023, max compression
```

## Comparing `motulator-0.1.2.tar` & `motulator-0.1.3.tar`

### file list

```diff
@@ -1,36 +1,36 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-17 19:23:05.682012 motulator-0.1.2/
--rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-11-17 19:22:49.000000 motulator-0.1.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     7874 2022-11-17 19:23:05.682012 motulator-0.1.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     7339 2022-11-17 19:22:49.000000 motulator-0.1.2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-17 19:23:05.682012 motulator-0.1.2/motulator/
--rw-r--r--   0 runner    (1001) docker     (121)     2074 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-17 19:23:05.682012 motulator-0.1.2/motulator/control/
--rw-r--r--   0 runner    (1001) docker     (121)       99 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/control/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9521 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/control/common.py
--rw-r--r--   0 runner    (1001) docker     (121)     8336 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/control/im_obs_vhz.py
--rw-r--r--   0 runner    (1001) docker     (121)    16011 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/control/im_vector.py
--rw-r--r--   0 runner    (1001) docker     (121)     5733 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/control/im_vhz.py
--rw-r--r--   0 runner    (1001) docker     (121)    10678 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/control/sm_flux_vector.py
--rw-r--r--   0 runner    (1001) docker     (121)     8048 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/control/sm_obs_vhz.py
--rw-r--r--   0 runner    (1001) docker     (121)     7080 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/control/sm_signal_inj.py
--rw-r--r--   0 runner    (1001) docker     (121)    21407 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/control/sm_torque.py
--rw-r--r--   0 runner    (1001) docker     (121)    14229 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/control/sm_vector.py
--rw-r--r--   0 runner    (1001) docker     (121)     6802 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/helpers.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-17 19:23:05.682012 motulator-0.1.2/motulator/model/
--rw-r--r--   0 runner    (1001) docker     (121)      109 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/model/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4092 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/model/converter.py
--rw-r--r--   0 runner    (1001) docker     (121)     6801 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/model/im.py
--rw-r--r--   0 runner    (1001) docker     (121)     9400 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/model/im_drive.py
--rw-r--r--   0 runner    (1001) docker     (121)     4955 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/model/mech.py
--rw-r--r--   0 runner    (1001) docker     (121)    10082 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/model/sm.py
--rw-r--r--   0 runner    (1001) docker     (121)     6241 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/model/sm_drive.py
--rw-r--r--   0 runner    (1001) docker     (121)     8088 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/model/sm_flux_maps.py
--rw-r--r--   0 runner    (1001) docker     (121)     7546 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/plots.py
--rw-r--r--   0 runner    (1001) docker     (121)     8377 2022-11-17 19:22:49.000000 motulator-0.1.2/motulator/simulation.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-17 19:23:05.682012 motulator-0.1.2/motulator.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     7874 2022-11-17 19:23:05.000000 motulator-0.1.2/motulator.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      787 2022-11-17 19:23:05.000000 motulator-0.1.2/motulator.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-17 19:23:05.000000 motulator-0.1.2/motulator.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       10 2022-11-17 19:23:05.000000 motulator-0.1.2/motulator.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      379 2022-11-17 19:22:49.000000 motulator-0.1.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)      601 2022-11-17 19:23:05.682012 motulator-0.1.2/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:08.271854 motulator-0.1.3/
+-rw-r--r--   0 runner    (1001) docker     (123)     1078 2023-04-06 21:25:53.000000 motulator-0.1.3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     8471 2023-04-06 21:26:08.275854 motulator-0.1.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     7936 2023-04-06 21:25:53.000000 motulator-0.1.3/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:08.271854 motulator-0.1.3/motulator/
+-rw-r--r--   0 runner    (1001) docker     (123)     2074 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:08.271854 motulator-0.1.3/motulator/control/
+-rw-r--r--   0 runner    (1001) docker     (123)       99 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/control/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10014 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/control/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8143 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/control/im_obs_vhz.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15938 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/control/im_vector.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5664 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/control/im_vhz.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7263 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/control/sm_flux_vector.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9447 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/control/sm_obs_vhz.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7021 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/control/sm_signal_inj.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19488 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/control/sm_torque.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13687 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/control/sm_vector.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6772 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/helpers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:08.271854 motulator-0.1.3/motulator/model/
+-rw-r--r--   0 runner    (1001) docker     (123)      109 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/model/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4071 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/model/converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6881 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/model/im.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9364 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/model/im_drive.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4992 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/model/mech.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10079 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/model/sm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6194 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/model/sm_drive.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8057 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/model/sm_flux_maps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7514 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/plots.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8255 2023-04-06 21:25:53.000000 motulator-0.1.3/motulator/simulation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:26:08.271854 motulator-0.1.3/motulator.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     8471 2023-04-06 21:26:08.000000 motulator-0.1.3/motulator.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      787 2023-04-06 21:26:08.000000 motulator-0.1.3/motulator.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 21:26:08.000000 motulator-0.1.3/motulator.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 21:26:08.000000 motulator-0.1.3/motulator.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      377 2023-04-06 21:25:53.000000 motulator-0.1.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      601 2023-04-06 21:26:08.275854 motulator-0.1.3/setup.cfg
```

### Comparing `motulator-0.1.2/LICENSE` & `motulator-0.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `motulator-0.1.2/PKG-INFO` & `motulator-0.1.3/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: motulator
-Version: 0.1.2
+Version: 0.1.3
 Summary: Motor Drive Simulator in Python
 Home-page: https://github.com/Aalto-Electric-Drives/motulator
 Author: Marko Hinkkanen
 Author-email: marko.hinkkanen@aalto.fi
 Project-URL: Bug Tracker, https://github.com/Aalto-Electric-Drives/motulator/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
@@ -71,26 +71,27 @@
 
 <!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
 <!-- prettier-ignore-start -->
 <!-- markdownlint-disable -->
 <table>
   <tbody>
     <tr>
-      <td align="center"><a href="https://github.com/lauritapio"><img src="https://avatars.githubusercontent.com/u/85596019?v=4?s=50" width="50px;" alt="Lauri Tiitinen"/><br /><sub><b>Lauri Tiitinen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=lauritapio" title="Code">💻</a> <a href="#ideas-lauritapio" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-lauritapio" title="Examples">💡</a> <a href="#mentoring-lauritapio" title="Mentoring">🧑‍🏫</a></td>
-      <td align="center"><a href="https://github.com/HannuHar"><img src="https://avatars.githubusercontent.com/u/96597650?v=4?s=50" width="50px;" alt="HannuHar"/><br /><sub><b>HannuHar</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=HannuHar" title="Code">💻</a> <a href="https://github.com/Aalto-Electric-Drives/motulator/issues?q=author%3AHannuHar" title="Bug reports">🐛</a></td>
-      <td align="center"><a href="https://research.aalto.fi/en/persons/marko-hinkkanen"><img src="https://avatars.githubusercontent.com/u/76600872?v=4?s=50" width="50px;" alt="Marko Hinkkanen"/><br /><sub><b>Marko Hinkkanen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=mhinkkan" title="Code">💻</a> <a href="#ideas-mhinkkan" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-mhinkkan" title="Examples">💡</a></td>
-      <td align="center"><a href="https://github.com/silundbe"><img src="https://avatars.githubusercontent.com/u/81169347?v=4?s=50" width="50px;" alt="silundbe"/><br /><sub><b>silundbe</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=silundbe" title="Code">💻</a> <a href="#example-silundbe" title="Examples">💡</a></td>
-      <td align="center"><a href="https://github.com/JoonaKukkonen"><img src="https://avatars.githubusercontent.com/u/85099403?v=4?s=50" width="50px;" alt="JoonaKukkonen"/><br /><sub><b>JoonaKukkonen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=JoonaKukkonen" title="Code">💻</a> <a href="#infra-JoonaKukkonen" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
-      <td align="center"><a href="https://github.com/jarno-k"><img src="https://avatars.githubusercontent.com/u/84438313?v=4?s=50" width="50px;" alt="jarno-k"/><br /><sub><b>jarno-k</b></sub></a><br /><a href="#ideas-jarno-k" title="Ideas, Planning, & Feedback">🤔</a></td>
-      <td align="center"><a href="https://github.com/angelicaiaderosa"><img src="https://avatars.githubusercontent.com/u/112799415?v=4?s=50" width="50px;" alt="angelicaiaderosa"/><br /><sub><b>angelicaiaderosa</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=angelicaiaderosa" title="Code">💻</a> <a href="#example-angelicaiaderosa" title="Examples">💡</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lauritapio"><img src="https://avatars.githubusercontent.com/u/85596019?v=4?s=50" width="50px;" alt="Lauri Tiitinen"/><br /><sub><b>Lauri Tiitinen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=lauritapio" title="Code">💻</a> <a href="#ideas-lauritapio" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-lauritapio" title="Examples">💡</a> <a href="#mentoring-lauritapio" title="Mentoring">🧑‍🏫</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/HannuHar"><img src="https://avatars.githubusercontent.com/u/96597650?v=4?s=50" width="50px;" alt="HannuHar"/><br /><sub><b>HannuHar</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=HannuHar" title="Code">💻</a> <a href="https://github.com/Aalto-Electric-Drives/motulator/issues?q=author%3AHannuHar" title="Bug reports">🐛</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://research.aalto.fi/en/persons/marko-hinkkanen"><img src="https://avatars.githubusercontent.com/u/76600872?v=4?s=50" width="50px;" alt="Marko Hinkkanen"/><br /><sub><b>Marko Hinkkanen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=mhinkkan" title="Code">💻</a> <a href="#ideas-mhinkkan" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-mhinkkan" title="Examples">💡</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/silundbe"><img src="https://avatars.githubusercontent.com/u/81169347?v=4?s=50" width="50px;" alt="silundbe"/><br /><sub><b>silundbe</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=silundbe" title="Code">💻</a> <a href="#example-silundbe" title="Examples">💡</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/JoonaKukkonen"><img src="https://avatars.githubusercontent.com/u/85099403?v=4?s=50" width="50px;" alt="JoonaKukkonen"/><br /><sub><b>JoonaKukkonen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=JoonaKukkonen" title="Code">💻</a> <a href="#infra-JoonaKukkonen" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jarno-k"><img src="https://avatars.githubusercontent.com/u/84438313?v=4?s=50" width="50px;" alt="jarno-k"/><br /><sub><b>jarno-k</b></sub></a><br /><a href="#ideas-jarno-k" title="Ideas, Planning, & Feedback">🤔</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/angelicaiaderosa"><img src="https://avatars.githubusercontent.com/u/112799415?v=4?s=50" width="50px;" alt="angelicaiaderosa"/><br /><sub><b>angelicaiaderosa</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=angelicaiaderosa" title="Code">💻</a> <a href="#example-angelicaiaderosa" title="Examples">💡</a></td>
     </tr>
     <tr>
-      <td align="center"><a href="https://www.kth.se/profile/lucap"><img src="https://avatars.githubusercontent.com/u/64190518?v=4?s=50" width="50px;" alt="Luca Peretti"/><br /><sub><b>Luca Peretti</b></sub></a><br /><a href="#ideas-lucaperetti" title="Ideas, Planning, & Feedback">🤔</a> <a href="#promotion-lucaperetti" title="Promotion">📣</a></td>
-      <td align="center"><a href="https://github.com/GianmarioPellegrinoPolito"><img src="https://avatars.githubusercontent.com/u/70333484?v=4?s=50" width="50px;" alt="GianmarioPellegrinoPolito"/><br /><sub><b>GianmarioPellegrinoPolito</b></sub></a><br /><a href="#data-GianmarioPellegrinoPolito" title="Data">🔣</a></td>
-      <td align="center"><a href="https://github.com/SimFerr"><img src="https://avatars.githubusercontent.com/u/67151973?v=4?s=50" width="50px;" alt="Simone Ferrari"/><br /><sub><b>Simone Ferrari</b></sub></a><br /><a href="#data-SimFerr" title="Data">🔣</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://www.kth.se/profile/lucap"><img src="https://avatars.githubusercontent.com/u/64190518?v=4?s=50" width="50px;" alt="Luca Peretti"/><br /><sub><b>Luca Peretti</b></sub></a><br /><a href="#ideas-lucaperetti" title="Ideas, Planning, & Feedback">🤔</a> <a href="#promotion-lucaperetti" title="Promotion">📣</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/GianmarioPellegrinoPolito"><img src="https://avatars.githubusercontent.com/u/70333484?v=4?s=50" width="50px;" alt="GianmarioPellegrinoPolito"/><br /><sub><b>GianmarioPellegrinoPolito</b></sub></a><br /><a href="#data-GianmarioPellegrinoPolito" title="Data">🔣</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/SimFerr"><img src="https://avatars.githubusercontent.com/u/67151973?v=4?s=50" width="50px;" alt="Simone Ferrari"/><br /><sub><b>Simone Ferrari</b></sub></a><br /><a href="#data-SimFerr" title="Data">🔣</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Jialed0303"><img src="https://avatars.githubusercontent.com/u/118135952?v=4?s=50" width="50px;" alt="Jialed0303"/><br /><sub><b>Jialed0303</b></sub></a><br /><a href="#ideas-Jialed0303" title="Ideas, Planning, & Feedback">🤔</a></td>
     </tr>
   </tbody>
 </table>
 
 <!-- markdownlint-restore -->
 <!-- prettier-ignore-end -->
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: motulator Version: 0.1.2 Summary: Motor Drive
+Metadata-Version: 2.1 Name: motulator Version: 0.1.3 Summary: Motor Drive
 Simulator in Python Home-page: https://github.com/Aalto-Electric-Drives/
 motulator Author: Marko Hinkkanen Author-email: marko.hinkkanen@aalto.fi
 Project-URL: Bug Tracker, https://github.com/Aalto-Electric-Drives/motulator/
 issues Classifier: Programming Language :: Python :: 3 Classifier: License ::
 OSI Approved :: MIT License Classifier: Operating System :: OS Independent
 Requires-Python: >=3.6 Description-Content-Type: text/markdown License-File:
 LICENSE # *motulator:* Motor Drive Simulator in Python [![Build Status](https:/
@@ -40,17 +40,17 @@
 have a look at these [guidelines](https://github.com/Aalto-Electric-Drives/
 motulator/blob/main/CONTRIBUTING.md) first. Contributors ------------ Thanks go
 to these wonderful people:
                 [Lauri_Tiitinen]                          [HannuHar]              [Marko_Hinkkanen]         [silundbe]      [JoonaKukkonen]  [jarno-  [angelicaiaderosa]
                  Lauri_Tiitinen                            HannuHar                Marko_Hinkkanen           silundbe        JoonaKukkonen      k]     angelicaiaderosa
            ð» ð¤ ð¡ ð§â         ð» ð        ð» ð¤ ð�    ð» ð�    ð» ð�jarno-k      ð» ð¡
                                                                                                                                                ð¤
-                       [Luca_Peretti]             [GianmarioPellegrinoPolito]        [Simone_Ferrari]
-                        Luca_Peretti               GianmarioPellegrinoPolito          Simone_Ferrari
-                          ð¤ ð£                  ð£                      ð£
+                       [Luca_Peretti]             [GianmarioPellegrinoPolito]        [Simone_Ferrari]       [Jialed0303]
+                        Luca_Peretti               GianmarioPellegrinoPolito          Simone_Ferrari         Jialed0303
+                          ð¤ ð£                  ð£                      ð£             ð¤
    This project follows the [all-contributors](https://github.com/all-
 contributors/all-contributors) specification. Contributions of any kind
 welcome! Acknowledgement --------------- This project has been sponsored by ABB
 Oy and by the Academy of Finland *Centre of Excellence in High-Speed
 Electromechanical Energy Conversion Systems*. The example control methods
 included in this repository are based on published algorithms (available in
 textbooks and scientific articles). They do not present any proprietary control
```

### Comparing `motulator-0.1.2/README.md` & `motulator-0.1.3/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -56,26 +56,27 @@
 
 <!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
 <!-- prettier-ignore-start -->
 <!-- markdownlint-disable -->
 <table>
   <tbody>
     <tr>
-      <td align="center"><a href="https://github.com/lauritapio"><img src="https://avatars.githubusercontent.com/u/85596019?v=4?s=50" width="50px;" alt="Lauri Tiitinen"/><br /><sub><b>Lauri Tiitinen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=lauritapio" title="Code">💻</a> <a href="#ideas-lauritapio" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-lauritapio" title="Examples">💡</a> <a href="#mentoring-lauritapio" title="Mentoring">🧑‍🏫</a></td>
-      <td align="center"><a href="https://github.com/HannuHar"><img src="https://avatars.githubusercontent.com/u/96597650?v=4?s=50" width="50px;" alt="HannuHar"/><br /><sub><b>HannuHar</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=HannuHar" title="Code">💻</a> <a href="https://github.com/Aalto-Electric-Drives/motulator/issues?q=author%3AHannuHar" title="Bug reports">🐛</a></td>
-      <td align="center"><a href="https://research.aalto.fi/en/persons/marko-hinkkanen"><img src="https://avatars.githubusercontent.com/u/76600872?v=4?s=50" width="50px;" alt="Marko Hinkkanen"/><br /><sub><b>Marko Hinkkanen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=mhinkkan" title="Code">💻</a> <a href="#ideas-mhinkkan" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-mhinkkan" title="Examples">💡</a></td>
-      <td align="center"><a href="https://github.com/silundbe"><img src="https://avatars.githubusercontent.com/u/81169347?v=4?s=50" width="50px;" alt="silundbe"/><br /><sub><b>silundbe</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=silundbe" title="Code">💻</a> <a href="#example-silundbe" title="Examples">💡</a></td>
-      <td align="center"><a href="https://github.com/JoonaKukkonen"><img src="https://avatars.githubusercontent.com/u/85099403?v=4?s=50" width="50px;" alt="JoonaKukkonen"/><br /><sub><b>JoonaKukkonen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=JoonaKukkonen" title="Code">💻</a> <a href="#infra-JoonaKukkonen" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
-      <td align="center"><a href="https://github.com/jarno-k"><img src="https://avatars.githubusercontent.com/u/84438313?v=4?s=50" width="50px;" alt="jarno-k"/><br /><sub><b>jarno-k</b></sub></a><br /><a href="#ideas-jarno-k" title="Ideas, Planning, & Feedback">🤔</a></td>
-      <td align="center"><a href="https://github.com/angelicaiaderosa"><img src="https://avatars.githubusercontent.com/u/112799415?v=4?s=50" width="50px;" alt="angelicaiaderosa"/><br /><sub><b>angelicaiaderosa</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=angelicaiaderosa" title="Code">💻</a> <a href="#example-angelicaiaderosa" title="Examples">💡</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lauritapio"><img src="https://avatars.githubusercontent.com/u/85596019?v=4?s=50" width="50px;" alt="Lauri Tiitinen"/><br /><sub><b>Lauri Tiitinen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=lauritapio" title="Code">💻</a> <a href="#ideas-lauritapio" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-lauritapio" title="Examples">💡</a> <a href="#mentoring-lauritapio" title="Mentoring">🧑‍🏫</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/HannuHar"><img src="https://avatars.githubusercontent.com/u/96597650?v=4?s=50" width="50px;" alt="HannuHar"/><br /><sub><b>HannuHar</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=HannuHar" title="Code">💻</a> <a href="https://github.com/Aalto-Electric-Drives/motulator/issues?q=author%3AHannuHar" title="Bug reports">🐛</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://research.aalto.fi/en/persons/marko-hinkkanen"><img src="https://avatars.githubusercontent.com/u/76600872?v=4?s=50" width="50px;" alt="Marko Hinkkanen"/><br /><sub><b>Marko Hinkkanen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=mhinkkan" title="Code">💻</a> <a href="#ideas-mhinkkan" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-mhinkkan" title="Examples">💡</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/silundbe"><img src="https://avatars.githubusercontent.com/u/81169347?v=4?s=50" width="50px;" alt="silundbe"/><br /><sub><b>silundbe</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=silundbe" title="Code">💻</a> <a href="#example-silundbe" title="Examples">💡</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/JoonaKukkonen"><img src="https://avatars.githubusercontent.com/u/85099403?v=4?s=50" width="50px;" alt="JoonaKukkonen"/><br /><sub><b>JoonaKukkonen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=JoonaKukkonen" title="Code">💻</a> <a href="#infra-JoonaKukkonen" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jarno-k"><img src="https://avatars.githubusercontent.com/u/84438313?v=4?s=50" width="50px;" alt="jarno-k"/><br /><sub><b>jarno-k</b></sub></a><br /><a href="#ideas-jarno-k" title="Ideas, Planning, & Feedback">🤔</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/angelicaiaderosa"><img src="https://avatars.githubusercontent.com/u/112799415?v=4?s=50" width="50px;" alt="angelicaiaderosa"/><br /><sub><b>angelicaiaderosa</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=angelicaiaderosa" title="Code">💻</a> <a href="#example-angelicaiaderosa" title="Examples">💡</a></td>
     </tr>
     <tr>
-      <td align="center"><a href="https://www.kth.se/profile/lucap"><img src="https://avatars.githubusercontent.com/u/64190518?v=4?s=50" width="50px;" alt="Luca Peretti"/><br /><sub><b>Luca Peretti</b></sub></a><br /><a href="#ideas-lucaperetti" title="Ideas, Planning, & Feedback">🤔</a> <a href="#promotion-lucaperetti" title="Promotion">📣</a></td>
-      <td align="center"><a href="https://github.com/GianmarioPellegrinoPolito"><img src="https://avatars.githubusercontent.com/u/70333484?v=4?s=50" width="50px;" alt="GianmarioPellegrinoPolito"/><br /><sub><b>GianmarioPellegrinoPolito</b></sub></a><br /><a href="#data-GianmarioPellegrinoPolito" title="Data">🔣</a></td>
-      <td align="center"><a href="https://github.com/SimFerr"><img src="https://avatars.githubusercontent.com/u/67151973?v=4?s=50" width="50px;" alt="Simone Ferrari"/><br /><sub><b>Simone Ferrari</b></sub></a><br /><a href="#data-SimFerr" title="Data">🔣</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://www.kth.se/profile/lucap"><img src="https://avatars.githubusercontent.com/u/64190518?v=4?s=50" width="50px;" alt="Luca Peretti"/><br /><sub><b>Luca Peretti</b></sub></a><br /><a href="#ideas-lucaperetti" title="Ideas, Planning, & Feedback">🤔</a> <a href="#promotion-lucaperetti" title="Promotion">📣</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/GianmarioPellegrinoPolito"><img src="https://avatars.githubusercontent.com/u/70333484?v=4?s=50" width="50px;" alt="GianmarioPellegrinoPolito"/><br /><sub><b>GianmarioPellegrinoPolito</b></sub></a><br /><a href="#data-GianmarioPellegrinoPolito" title="Data">🔣</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/SimFerr"><img src="https://avatars.githubusercontent.com/u/67151973?v=4?s=50" width="50px;" alt="Simone Ferrari"/><br /><sub><b>Simone Ferrari</b></sub></a><br /><a href="#data-SimFerr" title="Data">🔣</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Jialed0303"><img src="https://avatars.githubusercontent.com/u/118135952?v=4?s=50" width="50px;" alt="Jialed0303"/><br /><sub><b>Jialed0303</b></sub></a><br /><a href="#ideas-Jialed0303" title="Ideas, Planning, & Feedback">🤔</a></td>
     </tr>
   </tbody>
 </table>
 
 <!-- markdownlint-restore -->
 <!-- prettier-ignore-end -->
```

#### html2text {}

```diff
@@ -33,17 +33,17 @@
 have a look at these [guidelines](https://github.com/Aalto-Electric-Drives/
 motulator/blob/main/CONTRIBUTING.md) first. Contributors ------------ Thanks go
 to these wonderful people:
                 [Lauri_Tiitinen]                          [HannuHar]              [Marko_Hinkkanen]         [silundbe]      [JoonaKukkonen]  [jarno-  [angelicaiaderosa]
                  Lauri_Tiitinen                            HannuHar                Marko_Hinkkanen           silundbe        JoonaKukkonen      k]     angelicaiaderosa
            ð» ð¤ ð¡ ð§â         ð» ð        ð» ð¤ ð�    ð» ð�    ð» ð�jarno-k      ð» ð¡
                                                                                                                                                ð¤
-                       [Luca_Peretti]             [GianmarioPellegrinoPolito]        [Simone_Ferrari]
-                        Luca_Peretti               GianmarioPellegrinoPolito          Simone_Ferrari
-                          ð¤ ð£                  ð£                      ð£
+                       [Luca_Peretti]             [GianmarioPellegrinoPolito]        [Simone_Ferrari]       [Jialed0303]
+                        Luca_Peretti               GianmarioPellegrinoPolito          Simone_Ferrari         Jialed0303
+                          ð¤ ð£                  ð£                      ð£             ð¤
    This project follows the [all-contributors](https://github.com/all-
 contributors/all-contributors) specification. Contributions of any kind
 welcome! Acknowledgement --------------- This project has been sponsored by ABB
 Oy and by the Academy of Finland *Centre of Excellence in High-Speed
 Electromechanical Energy Conversion Systems*. The example control methods
 included in this repository are based on published algorithms (available in
 textbooks and scientific articles). They do not present any proprietary control
```

### Comparing `motulator-0.1.2/motulator/__init__.py` & `motulator-0.1.3/motulator/__init__.py`

 * *Files identical despite different names*

### Comparing `motulator-0.1.2/motulator/control/common.py` & `motulator-0.1.3/motulator/control/common.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,7 @@
-# pylint: disable=invalid-name
 """Common control functions and classes."""
 
 import numpy as np
 
 from motulator.helpers import abc2complex, complex2abc, Bunch
 
 
@@ -196,21 +195,35 @@
     pars : data object
         Control parameters.
 
     """
 
     def __init__(self, pars):
         self.T_s = pars.T_s
-        self.alpha_s = pars.alpha_s
-        self.tau_M_max = pars.tau_M_max
-        self.J = pars.J
-        # Gain
-        self.k = pars.alpha_s*pars.J
+        try:
+            self.tau_M_max = pars.tau_M_max
+        except AttributeError:
+            # No maximum torque limit
+            self.tau_M_max = np.inf
+        try:
+            # Gains for the 2DOF PI controller
+            self.alpha = pars.alpha_s
+            self.k_t = pars.alpha_s*pars.J
+            self.k_p = 2*pars.alpha_s*pars.J
+        except AttributeError:
+            # alpha_s or J not defined, try to use k_t, k_p, k_i
+            try:
+                self.k_t = pars.k_t
+                self.k_p = pars.k_p
+                self.alpha = pars.k_i/pars.k_t
+            except AttributeError:
+                print('No speed controller gains found.')
+
         # Integral state
-        self.tau_l = 0
+        self.tau_i = 0
         # Load torque estimate (stored for the update method)
         self.tau_L = 0
 
     def output(self, w_M_ref, w_M):
         """
         Compute the torque reference and the load torque estimate.
 
@@ -223,16 +236,16 @@
 
         Returns
         -------
         tau_M_ref : float
             Torque reference.
 
         """
-        self.tau_L = self.tau_l - self.alpha_s*self.J*w_M
-        tau_M_ref = self.k*(w_M_ref - w_M) + self.tau_L
+        self.tau_L = self.tau_i - (self.k_p - self.k_t)*w_M
+        tau_M_ref = self.k_t*(w_M_ref - w_M) + self.tau_L
 
         if np.abs(tau_M_ref) > self.tau_M_max:
             tau_M_ref = np.sign(tau_M_ref)*self.tau_M_max
 
         return tau_M_ref
 
     def update(self, tau_M_ref_lim):
@@ -241,15 +254,15 @@
 
         Parameters
         ----------
         tau_M_ref_lim : float
             Realized (limited) torque reference.
 
         """
-        self.tau_l += self.T_s*self.alpha_s*(tau_M_ref_lim - self.tau_L)
+        self.tau_i += self.T_s*self.alpha*(tau_M_ref_lim - self.tau_L)
 
 
 # %%
 class RateLimiter:
     """
     Rate limiter.
```

### Comparing `motulator-0.1.2/motulator/control/im_obs_vhz.py` & `motulator-0.1.3/motulator/control/im_obs_vhz.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,28 +1,25 @@
-# pylint: disable=invalid-name
 """
 Observer-based V/Hz control for induction motor drives.
 
 This implements the observer-based V/Hz control method described in [1]_. The
 state-feedback control law is in the alternative form which uses an
 intermediate stator current reference.
 
 References
 ----------
 .. [1] Tiitinen, Hinkkanen, Harnefors, "Stable and passive observer-based V/Hz
-    control for induction motors," in Proc. IEEE ECCE, Detroit, MI, Oct. 2022.
+    control for induction motors," Proc. IEEE ECCE, Detroit, MI, Oct. 2022.
 
 """
 
 # %%
-from __future__ import annotations
-from collections.abc import Callable
+from typing import Callable
 from dataclasses import dataclass, field
 import numpy as np
-
 from motulator.control.common import Ctrl, PWM, RateLimiter
 from motulator.helpers import abc2complex, Bunch
 
 
 # %%
 @dataclass
 class InductionMotorObsVHzCtrlPars:
@@ -52,15 +49,15 @@
     zeta_inf: float = .7
 
     # Motor parameter estimates (inverse-Γ model)
     R_s: float = 3.7
     R_R: float = 2.1
     L_sgm: float = .021
     L_M: float = .224
-    p: int = 2
+    n_p: int = 2
 
 
 # %%
 class InductionMotorVHzObsCtrl(Ctrl):
     """
     Observer-based V/Hz control for induction motors.
 
@@ -82,15 +79,15 @@
         self.w_m_ref = pars.w_m_ref
         self.psi_s_ref = pars.psi_s_nom
         # Control Parameters
         self.T_s = pars.T_s
         self.alpha_f = pars.alpha_f
         self.alpha_r = pars.alpha_r
         self.alpha_psi = pars.alpha_psi
-        self.p = pars.p
+        self.n_p = pars.n_p
         self.k_tau = pars.k_tau
         self.i_s_max = pars.i_s_max
         self.slip_compensation = pars.slip_compensation
         # Motor parameters
         self.R_s = pars.R_s
         self.R_R = pars.R_R
         self.L_sgm = pars.L_sgm
@@ -128,33 +125,33 @@
         # Get the states
         u_s = self.pwm.realized_voltage
         psi_R = self.observer.psi_R
         tau_M_ref = self.tau_M_ref
         w_r_ref = self.w_r_ref
 
         # Torque estimate (11c)
-        tau_M = 1.5*self.p*np.imag(i_s*np.conj(psi_R))
+        tau_M = 1.5*self.n_p*np.imag(i_s*np.conj(psi_R))
 
         # Slip frequency compensation (if enabled) for the low-pass filter.
         # Note, could also be based on the low-pass filtered torque.
         psi_R_sqr = np.abs(psi_R)**2
         if self.slip_compensation and psi_R_sqr > 0:
-            w_r = self.R_R*tau_M/(1.5*self.p*psi_R_sqr)
+            w_r = self.R_R*tau_M/(1.5*self.n_p*psi_R_sqr)
         else:
             w_r = 0
 
         # Slip compensation (9). Uses the low-pass filtered slip estimate
         # w_r_ref. Note if slip compensation disabled w_r_ref == 0.
         w_s_ref = w_m_ref + w_r_ref
 
         # Dynamic frequency (7a)
         w_s = w_s_ref - self.k_tau*(tau_M - tau_M_ref)
 
         # State feedback
-        u_s_ref, i_s_ref = self.state_feedback(i_s, psi_R, w_s)
+        u_s_ref = self.state_feedback(i_s, psi_R, w_s)
 
         # Duty ratios
         d_abc_ref, u_s_ref_lim = self.pwm.output(
             u_s_ref, u_dc, self.theta_s, w_s)
 
         # Data logging
         data = Bunch(
@@ -190,15 +187,15 @@
         # Limit the reference
         if np.abs(i_s_ref) > self.i_s_max:
             i_s_ref = self.i_s_max*i_s_ref/np.abs(i_s_ref)
         # State feedback (6a)
         u_s_ref = (
             self.R_s*i_s_ref + 1j*w_s*self.psi_s_ref +
             self.L_sgm*self.alpha_psi*(i_s_ref - i_s))
-        return u_s_ref, i_s_ref
+        return u_s_ref
 
 
 # %%
 class SensorlessFluxObserver:
     """
     Sensorless reduced-order flux observer.
 
@@ -217,15 +214,15 @@
     .. [1] Hinkkanen, Harnefors, Luomi, "Reduced-order flux observers with
        stator-resistance adaptation for speed-sensorless induction motor
        drives," IEEE Trans. Power Electron., 2010,
        https://doi.org/10.1109/TPEL.2009.2039650
 
     """
 
-    # pylint: disable=too-many-instance-attributes, too-few-public-methods
+    # pylint: disable=too-many-instance-attributes
     def __init__(self, pars):
         self.T_s = pars.T_s
         self.R_s = pars.R_s
         self.R_R = pars.R_R
         self.L_sgm = pars.L_sgm
         self.alpha = pars.R_R/pars.L_M
         self.alpha_o = pars.alpha_o
@@ -247,27 +244,26 @@
             Angular frequency of the reference frame.
 
         """
         # Decay rate
         lambd = self.zeta_inf*np.abs(w_s) + .5*self.alpha
         # Observer gain (without the orthogonal projection which is
         # embedded into the state update)
-        g_o = 2*lambd*(self.alpha + 1j*self.w_m)/(self.alpha**2 + self.w_m**2)
+        g_o = 2*lambd/(self.alpha - 1j*self.w_m)
 
         # Time derivative of the stator current
         di_s = (i_s - self.i_s_old)/self.T_s
 
         # Error voltage
         e = (
             self.L_sgm*(di_s + 1j*w_s*i_s) + (self.R_s + self.R_R)*i_s -
             (self.alpha - 1j*self.w_m)*self.psi_R - u_s)
 
         # Error signal
-        psi_R_sqr = np.abs(self.psi_R)**2
-        err = e*np.conj(self.psi_R)/psi_R_sqr if psi_R_sqr > 0 else 0
+        err = e/self.psi_R if np.abs(self.psi_R) > 0 else 0
 
         # Update the states
         self.w_m -= self.T_s*self.alpha_o*err.imag
         self.psi_R += self.T_s*(
             u_s - self.R_s*i_s - self.L_sgm*di_s - 1j*w_s*
             (self.psi_R + self.L_sgm*i_s) + g_o*self.psi_R*err.real)
         self.i_s_old = i_s
```

### Comparing `motulator-0.1.2/motulator/control/im_vector.py` & `motulator-0.1.3/motulator/control/im_vector.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,16 +1,14 @@
-# pylint: disable=C0103
 """
 Vector control methods for induction motor drives.
 
 The algorithms are written based on the inverse-Γ model.
 
 """
-from __future__ import annotations
-from collections.abc import Callable
+from typing import Callable
 from dataclasses import dataclass, field
 import numpy as np
 
 from motulator.helpers import abc2complex, Bunch
 from motulator.control.common import Ctrl, SpeedCtrl, PWM
 
 
@@ -40,15 +38,15 @@
     psi_R_nom: float = .9
     u_dc_nom: float = 540
     # Motor parameter estimates (inverse-Γ model)
     R_s: float = 3.7
     R_R: float = 2.1
     L_sgm: float = .021
     L_M: float = .224
-    p: int = 2
+    n_p: int = 2
     J: float = .015
 
 
 # %%
 class InductionMotorVectorCtrl(Ctrl):
     """
     Vector control for an induction motor drive.
@@ -65,15 +63,15 @@
 
     # pylint: disable=too-many-instance-attributes
     def __init__(self, pars):
         super().__init__()
         self.T_s = pars.T_s
         self.w_m_ref = pars.w_m_ref
         self.sensorless = pars.sensorless
-        self.p = pars.p
+        self.n_p = pars.n_p
         self.speed_ctrl = SpeedCtrl(pars)
         self.current_ref = CurrentRef(pars)
         self.current_ctrl = CurrentCtrl(pars)
         if self.sensorless:
             self.observer = SensorlessObserver(pars)
         else:
             self.observer = Observer(pars)
@@ -101,28 +99,28 @@
         w_m_ref = self.w_m_ref(self.t)
 
         # Measure the feedback signals
         i_s_abc = mdl.motor.meas_currents()  # Phase currents
         u_dc = mdl.conv.meas_dc_voltage()  # DC-bus voltage
 
         if not self.sensorless:
-            w_m = self.p*mdl.mech.meas_speed()  # Rotor speed
+            w_m = self.n_p*mdl.mech.meas_speed()  # Rotor speed
         else:
             w_m = self.observer.w_m  # Get the estimated speed
 
         # Get the states
         u_s = self.pwm.realized_voltage
         psi_R = self.observer.psi_R
         theta_s = self.observer.theta_s
 
         # Space vector and coordinate transformation
         i_s = np.exp(-1j*theta_s)*abc2complex(i_s_abc)
 
         # Outputs
-        tau_M_ref = self.speed_ctrl.output(w_m_ref/self.p, w_m/self.p)
+        tau_M_ref = self.speed_ctrl.output(w_m_ref/self.n_p, w_m/self.n_p)
         i_s_ref, tau_M_ref_lim = self.current_ref.output(tau_M_ref, psi_R)
         w_s = self.observer.output(u_s, i_s, w_m)  # w_m not used if sensorless
         u_s_ref = self.current_ctrl.output(i_s_ref, i_s)
         d_abc_ref, u_s_ref_lim = self.pwm.output(u_s_ref, u_dc, theta_s, w_s)
 
         # Save data
         data = Bunch(
@@ -177,15 +175,15 @@
 
     """
 
     def __init__(self, pars):
         self.T_s = pars.T_s
         self.i_s_max = pars.i_s_max
         self.L_sgm = pars.L_sgm
-        self.p = pars.p
+        self.n_p = pars.n_p
         # Local parameters for initializing the constants
         psi_R_nom = pars.psi_R_nom
         L_M = pars.L_M
         R_R = pars.R_R
         u_dc_nom = pars.u_dc_nom
         # Nominal d-axis current
         self.i_sd_nom = psi_R_nom/L_M
@@ -220,26 +218,26 @@
             # Breakdown torque limit
             i_sq_max2 = psi_R/self.L_sgm + i_sd_ref
             # q-axis current limit
             i_sq_max = np.min([i_sq_max1, i_sq_max2])
             return i_sq_max
 
         # q-axis current reference
-        i_sq_ref = tau_M_ref/(1.5*self.p*psi_R) if psi_R > 0 else 0
+        i_sq_ref = tau_M_ref/(1.5*self.n_p*psi_R) if psi_R > 0 else 0
 
         # Limit the current
         i_sq_max = q_axis_current_limit(self.i_sd_ref, psi_R)
         if np.abs(i_sq_ref) > i_sq_max:
             i_sq_ref = np.sign(i_sq_ref)*i_sq_max
 
         # Current reference
         i_s_ref = self.i_sd_ref + 1j*i_sq_ref
 
         # Limited torque (for the speed controller)
-        tau_M_ref_lim = 1.5*self.p*psi_R*i_sq_ref
+        tau_M_ref_lim = 1.5*self.n_p*psi_R*i_sq_ref
 
         return i_s_ref, tau_M_ref_lim
 
     def update(self, u_s_ref, u_dc):
         """
         Field-weakening based on the unlimited reference voltage.
 
@@ -403,15 +401,15 @@
 
         """
         alpha = self.R_R/self.L_M
 
         # Observer gain (17) with c = w_s**2 (without the orthogonal projection
         # which is embedded into the state update)
         b = alpha + 2*self.zeta_inf*np.abs(self.w_m)
-        g = b*(alpha + 1j*self.w_m)/(alpha**2 + self.w_m**2)
+        g = b/(alpha - 1j*self.w_m)
 
         # Induced voltage from stator quantities, cf. (7)
         e_s = u_s - self.R_s*i_s - self.L_sgm*(i_s - self.i_s_old)/self.T_s
         # Induced voltage (8) from the rotor quantities
         e_r = self.R_R*i_s - (alpha - 1j*self.w_m)*self.psi_R
 
         # Angular frequency of the rotor flux vector
```

### Comparing `motulator-0.1.2/motulator/control/im_vhz.py` & `motulator-0.1.3/motulator/control/im_vhz.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,7 @@
-# pylint: disable=C0103
 """
 V/Hz control for induction motor drives.
 
 The method is similar to [1]_. Open-loop V/Hz control can be obtained as a
 special case by choosing::
 
     R_s, R_R = 0, 0
@@ -18,19 +17,17 @@
 ----------
 .. [1] Hinkkanen, Tiitinen, Mölsä, Harnefors, "On the stability of
    volts-per-hertz control for induction motors," IEEE J. Emerg. Sel. Topics
    Power Electron., 2022, https://doi.org/10.1109/JESTPE.2021.3060583
 
 """
 # %%
-from __future__ import annotations
-from collections.abc import Callable
+from typing import Callable
 from dataclasses import dataclass, field
 import numpy as np
-
 from motulator.control.common import Ctrl, PWM, RateLimiter
 from motulator.helpers import abc2complex, Bunch
 
 
 # %%
 @dataclass
 class InductionMotorVHzCtrlPars:
```

### Comparing `motulator-0.1.2/motulator/control/sm_flux_vector.py` & `motulator-0.1.3/motulator/control/sm_obs_vhz.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,113 +1,100 @@
-# pylint: disable=invalid-name
 """
-Flux-vector control for synchronous motor drives.
+Observer-based V/Hz control for synchronous motor drives.
 
-This implements a simplified version of stator-flux-vector control [1]_. The
-rotor coordinates are used in this implementation [2]_. One control variable is
-the stator-flux magnitude and another is the electromagnetic torque. The latter
-choice differs from [1]_ and [2]_, where the torque-producing current component
-is used. Furthermore, here proportional control is used for simplicity. The
-magnetic saturation is not considered in this implementation.
+This method is based on [1]_.
 
 References
 ----------
-.. [1] Pellegrino, Armando, Guglielmi, “Direct flux field-oriented control of
-   IPM drives with variable DC link in the field-weakening region,” IEEE Trans.
-   Ind. Appl., 2009, https://doi.org/10.1109/TIA.2009.2027167
-
-.. [2] Awan, Hinkkanen, Bojoi, Pellegrino, "Stator-flux-oriented control of
-   synchronous motors: A systematic design procedure," IEEE Trans. Ind. Appl.,
-   2019, https://doi.org/10.1109/TIA.2019.2927316
+.. [1] Tiitinen, Hinkkanen, Kukkola, Routimo, Pellegrino, Harnefors, "Stable
+    and passive observer-based V/Hz control for synchronous Motors," Proc.
+    IEEE ECCE, Detroit, MI, Oct. 2022.
 
 """
-from __future__ import annotations
-from collections.abc import Callable
+
+from typing import Callable
 from dataclasses import dataclass, field
 import numpy as np
-
 from motulator.helpers import abc2complex, Bunch
-from motulator.control.common import Ctrl, SpeedCtrl, PWM
+from motulator.control.common import Ctrl, PWM, RateLimiter
 from motulator.control.sm_torque import TorqueCharacteristics
-from motulator.control.sm_vector import SensorlessObserver
 
 
 # %%
 @dataclass
-class SynchronousMotorFluxVectorCtrlPars:
-    """Control parameters: flux-vector control for synchronous motor drives."""
+class SynchronousMotorVHzObsCtrlPars:
+    """Control parameters."""
 
     # pylint: disable=too-many-instance-attributes
     # Speed reference (in electrical rad/s)
     w_m_ref: Callable[[float], float] = field(
         repr=False, default=lambda t: (t > .2)*(2*np.pi*75))
-    # Mode
-    sensorless: bool = True
-    # Sampling period
+
+    # Control
     T_s: float = 250e-6
-    # Nominal flux
-    psi_s_nom: float = np.sqrt(2/3)*370/(2*np.pi*75)
-    # Maximum flux
-    psi_s_max: float = np.sqrt(2/3)*370/(2*np.pi*75)
-    # Minimum flux
-    psi_s_min: float = .5*np.sqrt(2/3)*370/(2*np.pi*75)
-    # Voltage marginal
-    k_u: float = .9
-    # Bandwidths
-    alpha_psi: float = 2*np.pi*100
-    alpha_tau_max: float = 2*np.pi*400
-    alpha_s: float = 2*np.pi*4
-    # Maximum values
-    tau_M_max: float = 1.5*14
-    i_s_max: float = 1.5*np.sqrt(2)*5.
+    psi_s_max: float = None
+    psi_s_min: float = None
+    rate_limit: float = np.inf
+    i_s_max: float = 1.5*np.sqrt(2)*5
+    alpha_psi: float = 2*np.pi*50
+    alpha_tau: float = 2*np.pi*50
+    alpha_f: float = 2*np.pi*1
+    k_u: float = 1
+
+    # Observer
+    alpha_o: float = 2*np.pi*20
+    zeta_inf: float = .2
+
     # Motor parameter estimates
     R_s: float = 3.6
     L_d: float = .036
     L_q: float = .051
     psi_f: float = .545
-    p: int = 3
-    J: float = .015
-    # Sensorless observer (used only in the sensorless mode)
-    w_o: float = 2*np.pi*40
-    zeta_inf: float = .2
-    # Sensored observer (used only in the sensored mode)
-    g: float = 2*np.pi*15
+    n_p: int = 3
 
 
 # %%
-class SynchronousMotorFluxVectorCtrl(Ctrl):
+class SynchronousMotorVHzObsCtrl(Ctrl):
     """
-    Flux-vector control for synchronous motor drives.
-
-    This class interconnects the subsystems of the control system and
-    provides the interface to the solver.
+    Observer-based V/Hz control for synchronous motors.
 
     Parameters
     ----------
-    pars : SynchronousMotoroFluxVectorCtrlPars
+    pars : SynchronousMotorVHzObsCtrlPars
         Control parameters.
 
     """
 
     # pylint: disable=too-many-instance-attributes
     def __init__(self, pars):
         super().__init__()
-        self.T_s = pars.T_s
-        self.w_m_ref = pars.w_m_ref
-        self.p = pars.p
-        self.L_d, self.L_q, self.psi_f = pars.L_d, pars.L_q, pars.psi_f
-        self.sensorless = pars.sensorless
-        self.flux_torque_ctrl = FluxTorqueCtrl(pars)
-        self.speed_ctrl = SpeedCtrl(pars)
+        # Instantiate classes
+        self.observer = SensorlessFluxObserver(pars)
         self.pwm = PWM(pars)
-        if pars.sensorless:
-            self.observer = SensorlessObserver(pars)
-        else:
-            self.observer = Observer(pars)
+        self.rate_limiter = RateLimiter(pars)
         self.flux_torque_ref = FluxTorqueRef(pars)
+        # Reference
+        self.w_m_ref = pars.w_m_ref
+        # Motor parameters
+        self.R_s = pars.R_s
+        self.n_p = pars.n_p
+        # Controller parameters
+        self.T_s = pars.T_s
+        self.alpha_f = pars.alpha_f
+        self.alpha_psi = pars.alpha_psi
+        # Gain k_tau
+        G = (pars.L_d - pars.L_q)/(pars.L_d*pars.L_q)
+        psi_s0 = pars.psi_f if pars.psi_f > 0 else pars.psi_s_min
+        if pars.psi_f > 0:  # PMSM or PM-SyRM
+            c_delta0 = 1.5*pars.n_p*(pars.psi_f*psi_s0/pars.L_d - G*psi_s0**2)
+        else:  # SyRM
+            c_delta0 = 1.5*pars.n_p*G*psi_s0**2
+        self.k_tau = pars.alpha_tau/c_delta0
+        # Initial states
+        self.theta_s, self.tau_M_ref = 0, 0
 
     def __call__(self, mdl):
         """
         Run the main control loop.
 
         Parameters
         ----------
@@ -120,151 +107,87 @@
         T_s : float
             Sampling period.
         d_abc_ref : ndarray, shape (3,)
             Duty ratio references.
 
         """
         # Get the speed reference
-        w_m_ref = self.w_m_ref(self.t)
+        w_m_ref = self.rate_limiter(self.w_m_ref(self.t))
 
-        # Feedback signals
+        # Measure the feedback signals
         i_s_abc = mdl.motor.meas_currents()  # Phase currents
         u_dc = mdl.conv.meas_dc_voltage()  # DC-bus voltage
-        u_s = self.pwm.realized_voltage  # Realized voltage from PWM
 
-        if self.sensorless:
-            # Get the rotor speed and position estimates
-            w_m, theta_m = self.observer.w_m, self.observer.theta_m
-        else:
-            # Measure the rotor speed
-            w_m = self.p*mdl.mech.meas_speed()
-            # Limit the electrical rotor position into [-pi, pi)
-            theta_m = np.mod(
-                self.p*mdl.mech.meas_position() + np.pi, 2*np.pi) - np.pi
+        # Space vector and coordinate transformation
+        i_s = np.exp(-1j*self.theta_s)*abc2complex(i_s_abc)
 
-        # Current vector in estimated rotor coordinates
-        i_s = np.exp(-1j*theta_m)*abc2complex(i_s_abc)
-
-        # Flux and torque estimates
+        # Get the states
+        u_s = self.pwm.realized_voltage
         psi_s = self.observer.psi_s
+        tau_M_ref = self.tau_M_ref
+
+        # Limited flux and torque references
+        psi_s_ref, _ = self.flux_torque_ref(tau_M_ref, w_m_ref, u_dc)
+
+        # Electromagnetic torque (7d)
+        tau_M = 1.5*self.n_p*np.imag(i_s*np.conj(psi_s))
+
+        # Dynamic frequency (5a)
+        w_s = w_m_ref - self.k_tau*(tau_M - tau_M_ref)
 
-        # Outputs
-        tau_M_ref = self.speed_ctrl.output(w_m_ref/self.p, w_m/self.p)
-        psi_s_ref, tau_M_ref_lim = self.flux_torque_ref(tau_M_ref, w_m, u_dc)
-        u_s_ref = self.flux_torque_ctrl(
-            psi_s_ref, tau_M_ref_lim, psi_s, i_s, w_m, u_dc)
-        d_abc_ref, u_s_ref_lim = self.pwm.output(u_s_ref, u_dc, theta_m, w_m)
+        # Voltage reference (4)
+        err = psi_s_ref - psi_s
+        u_s_ref = self.R_s*i_s + 1j*w_s*psi_s_ref + self.alpha_psi*err
+
+        # Duty ratios
+        d_abc_ref, u_s_ref_lim = self.pwm.output(
+            u_s_ref, u_dc, self.theta_s, w_s)
 
         # Data logging
         data = Bunch(
             i_s=i_s,
             psi_s=psi_s,
             psi_s_ref=psi_s_ref,
             t=self.t,
-            tau_M_ref_lim=tau_M_ref_lim,
-            theta_m=theta_m,
+            theta_s=self.theta_s,
             u_dc=u_dc,
             u_s=u_s,
-            w_m=w_m,
             w_m_ref=w_m_ref,
+            w_s=w_s,
+            tau_M=tau_M,
         )
         self.save(data)
 
-        # Update states
-        self.observer.update(u_s, i_s, w_m)
-        self.speed_ctrl.update(tau_M_ref_lim)
+        # Update the states
         self.pwm.update(u_s_ref_lim)
+        self.observer.update(u_s, i_s, w_s)
+        self.tau_M_ref += self.T_s*self.alpha_f*(tau_M - self.tau_M_ref)
+        self.theta_s += self.T_s*w_s  # Next line: limit into [-pi, pi)
+        self.theta_s = np.mod(self.theta_s + np.pi, 2*np.pi) - np.pi
         self.update_clock(self.T_s)
 
         return self.T_s, d_abc_ref
 
 
 # %%
-class FluxTorqueCtrl:
-    """
-    Stator flux and torque controller.
-
-    Parameters
-    ----------
-    pars : SynchronousMotoroFluxVectorCtrlPars
-        Control parameters.
-
-    """
-
-    # pylint: disable=too-few-public-methods
-    def __init__(self, pars):
-        self.T_s = pars.T_s
-        self.R_s = pars.R_s
-        self.p = pars.p
-        self.alpha_psi = pars.alpha_psi
-        G = (pars.L_d - pars.L_q)/(pars.L_d*pars.L_q)
-        c_delta_max = 1.5*pars.p*(
-            pars.psi_f*pars.psi_s_nom/pars.L_d + G*pars.psi_s_nom**2)
-        self.k_tau = pars.alpha_tau_max/c_delta_max
-
-    def __call__(self, psi_s_ref, tau_M_ref, psi_s, i_s, w_m, u_dc):
-        """
-        Compute the unlimited voltage reference.
-
-        Parameters
-        ----------
-        psi_s_ref : float
-            Stator flux reference (magnitude).
-        tau_M_ref : float
-            Torque reference.
-        psi_s : complex
-            Stator flux estimate.
-        i_s : complex
-            Stator current.
-        w_m : float
-            Rotor speed (in electrical rad/s).
-        u_dc : float
-            DC-bus voltage.
-
-        Returns
-        -------
-        u_s_ref : complex
-            Unlimited voltage reference.
-
-        """
-        # Torque estimate
-        tau_M = 1.5*self.p*np.imag(i_s*np.conj(psi_s))
-
-        # Stator frequency
-        w_s = w_m + self.k_tau*(tau_M_ref - tau_M)
-
-        # Voltage reference
-        e_psi = psi_s_ref - np.abs(psi_s)
-        delta = np.angle(psi_s)
-        u_s_ref = (
-            self.R_s*i_s + 1j*w_s*psi_s +
-            self.alpha_psi*e_psi*np.exp(1j*delta))
-
-        return u_s_ref
-
-
-# %%
 class FluxTorqueRef:
     """
     Flux and torque references.
 
     Parameters
     ----------
-    pars : SynchronousMotoroFluxVectorCtrlPars
+    pars : SynchronousMotorVHzObsCtrlPars
         Control parameters.
 
     """
 
-    # pylint: disable=too-few-public-methods
     def __init__(self, pars):
-        self.psi_s_min = pars.psi_s_min
-        try:
-            self.psi_s_max = pars.psi_s_max
-        except AttributeError:
-            self.psi_s_max = np.inf
+        self.psi_s_min = (
+            pars.psi_f if pars.psi_s_min is None else pars.psi_s_min)
+        self.psi_s_max = np.inf if pars.psi_s_max is None else pars.psi_s_max
         self.k_u = pars.k_u
         # Merged MTPV and current limits
         tq = TorqueCharacteristics(pars)
         lims = tq.mtpv_and_current_limits(i_s_max=pars.i_s_max)
         self.tau_M_lim = lims.tau_M_vs_abs_psi_s
         # MTPA locus
         mtpa = tq.mtpa_locus(i_s_max=pars.i_s_max)
@@ -275,86 +198,116 @@
         Calculate the stator flux reference and limit the torque reference.
 
         Parameters
         ----------
         tau_M_ref : float
             Unlimited torque reference.
         w_m : float
-            Rotor speed (in electrical rad/s).
+            Rotor speed or its reference (in electrical rad/s).
         u_dc : float
             DC-bus voltage.
 
         Returns
         -------
         psi_s_ref : float
             Stator flux reference.
         tau_M_ref_lim : float
             Limited torque reference.
 
         """
         # Get the MTPA flux
         psi_s_mtpa = self.psi_s_mtpa(np.abs(tau_M_ref))
-        # Limit the MTPA flux for sensorless drives
-        psi_s_mtpa = np.max([psi_s_mtpa, self.psi_s_min])
-        # Limit the MTPA flux to avoid magnetic saturation
-        psi_s_mtpa = np.min([psi_s_mtpa, self.psi_s_max])
+        np.clip(psi_s_mtpa, self.psi_s_min, self.psi_s_max, out=psi_s_mtpa)
 
         # Field weakening
-        if np.abs(w_m) > 0:
-            psi_s_max = self.k_u*u_dc/np.sqrt(3)/np.abs(w_m)
-        else:
-            psi_s_max = np.inf
+        u_s_max = self.k_u*u_dc/np.sqrt(3)
+        psi_s_max = u_s_max/np.abs(w_m) if np.abs(w_m) > 0 else np.inf
 
         # Flux reference
         psi_s_ref = np.min([psi_s_max, psi_s_mtpa])
 
         # Limit the torque reference according to the MTPV and current limits
         tau_M_lim = self.tau_M_lim(psi_s_ref)
         tau_M_ref_lim = np.min([tau_M_lim, np.abs(tau_M_ref)
                                 ])*np.sign(tau_M_ref)
 
         return psi_s_ref, tau_M_ref_lim
 
 
 # %%
-class Observer:
+class SensorlessFluxObserver:
     """
-    Sensored observer.
+    Sensorless stator flux observer.
+
+    This observer is a variant of [1]_. The observer gain decouples the
+    electrical and mechanical dynamics and allows placing the poles of the
+    corresponding linearized estimation error dynamics. For simplicity, the
+    current model is here implemented in rotor coordinates, however this is
+    mathematically equivalent to controller coordinates implementation in [2]_.
 
     Parameters
     ----------
-    pars : SynchronousMotoroFluxVectorCtrlPars
+    pars : SynchronousMotorObsVHzCtrlPars
         Control parameters.
 
+    References
+    ----------
+    .. [1] Hinkkanen, Saarakkala, Awan, Mölsä, Tuovinen, "Observers for
+        sensorless synchronous motor drives: Framework for design and
+        analysis," IEEE Trans. Ind. Appl., 2018,
+        https://doi.org/10.1109/TIA.2018.2858753
+    .. [2] Tiitinen, Hinkkanen, Kukkola, Routimo, Pellegrino, Harnefors,
+        "Stable and passive observer-based V/Hz control for synchronous
+        Motors," Proc. IEEE ECCE, Detroit, MI, Oct. 2022.
+
     """
 
-    # pylint: disable=too-few-public-methods
     def __init__(self, pars):
         self.T_s = pars.T_s
         self.R_s = pars.R_s
         self.L_d = pars.L_d
         self.L_q = pars.L_q
         self.psi_f = pars.psi_f
-        self.g = pars.g
-        # Initial state
-        self.psi_s = pars.psi_f
+        self.alpha_o = pars.alpha_o
+        self.b_p = .5*pars.R_s*(pars.L_d + pars.L_q)/(pars.L_d*pars.L_q)
+        self.zeta_inf = pars.zeta_inf
+        # Initial states
+        self.delta, self.psi_s = 0, pars.psi_f
 
-    def update(self, u_s, i_s, w_m):
+    def update(self, u_s, i_s, w_s):
         """
         Update the states for the next sampling period.
 
         Parameters
         ----------
         u_s : complex
-            Stator voltage in estimated rotor coordinates.
+            Stator voltage.
         i_s : complex
-            Stator current in estimated rotor coordinates.
-        w_m : float
-            Rotor speed (in electrical rad/s).
+            Stator current.
+        w_s : float
+            Stator angular frequency.
 
         """
-        # Estimation error
-        e = self.L_d*i_s.real + 1j*self.L_q*i_s.imag + self.psi_f - self.psi_s
+        # Transformations to rotor coordinates
+        i_sr = i_s*np.exp(1j*self.delta)
+        psi_sr = self.psi_s*np.exp(1j*self.delta)
+
+        # Auxiliary flux and estimation error in rotor coordinates
+        psi_ar = self.psi_f + (self.L_d - self.L_q)*np.conj(i_sr)
+        e_r = self.L_d*i_sr.real + 1j*self.L_q*i_sr.imag + self.psi_f - psi_sr
+
+        # Auxiliary flux in controller coordinates
+        psi_a = np.exp(-1j*self.delta)*psi_ar
+
+        g_o = self.b_p + 2*self.zeta_inf*np.abs(w_s)
+
+        if np.abs(psi_ar) > 0:
+            # Correction voltage in controller coordinates
+            v = g_o*psi_a*np.real(e_r/psi_ar)
+            # Error signal
+            w_delta = self.alpha_o*np.imag(e_r/psi_ar)
+        else:
+            v, w_delta = 0, 0
 
-        # Update the state
-        self.psi_s += self.T_s*(
-            u_s - self.R_s*i_s - 1j*w_m*self.psi_s + self.g*e)
+        # Update the states
+        self.psi_s += self.T_s*(u_s - self.R_s*i_s - 1j*w_s*self.psi_s + v)
+        self.delta += self.T_s*w_delta
```

### Comparing `motulator-0.1.2/motulator/control/sm_obs_vhz.py` & `motulator-0.1.3/motulator/control/sm_flux_vector.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,113 +1,111 @@
-# pylint: disable=invalid-name
 """
-Observer-based V/Hz control for synchronous motor drives.
+Flux-vector control for synchronous motor drives.
 
-This method is based on [1]_.
+This implements a version of stator-flux-vector control [1]_. Rotor coordinates 
+as well as decoupling between the stator flux and torque channels are used [2]_. 
+Here, the stator flux magnitude and the electromagnetic torque are selected as
+controllable variables. Proportional controllers are used for simplicity. The 
+magnetic saturation is not considered in this implementation.
 
 References
 ----------
-.. [1] Tiitinen, Hinkkanen, Kukkola, Routimo, Pellegrino, Harnefors, "Stable
-    and passive observer-based V/Hz control for synchronous Motors," in Proc.
-    IEEE ECCE, Detroit, MI, Oct. 2022.
+.. [1] Pellegrino, Armando, Guglielmi, “Direct flux field-oriented control of
+   IPM drives with variable DC link in the field-weakening region,” IEEE Trans.
+   Ind. Appl., 2009, https://doi.org/10.1109/TIA.2009.2027167
+
+.. [2] Awan, Hinkkanen, Bojoi, Pellegrino, "Stator-flux-oriented control of
+   synchronous motors: A systematic design procedure," IEEE Trans. Ind. Appl.,
+   2019, https://doi.org/10.1109/TIA.2019.2927316
 
 """
-
 from typing import Callable
 from dataclasses import dataclass, field
 import numpy as np
-
 from motulator.helpers import abc2complex, Bunch
-from motulator.control.common import Ctrl, PWM, RateLimiter
-from motulator.control.sm_torque import TorqueCharacteristics
+from motulator.control.common import Ctrl, SpeedCtrl, PWM
+from motulator.control.sm_vector import SensorlessObserver
+from motulator.control.sm_obs_vhz import FluxTorqueRef
 
 
 # %%
 @dataclass
-class SynchronousMotorVHzObsCtrlPars:
-    """Control parameters."""
+class SynchronousMotorFluxVectorCtrlPars:
+    """Control parameters: flux-vector control for synchronous motor drives."""
 
     # pylint: disable=too-many-instance-attributes
     # Speed reference (in electrical rad/s)
     w_m_ref: Callable[[float], float] = field(
         repr=False, default=lambda t: (t > .2)*(2*np.pi*75))
-
-    # Control
+    # Mode
+    sensorless: bool = True
+    # Sampling period
     T_s: float = 250e-6
-    psi_s_max: float = np.sqrt(2/3)*370/(2*np.pi*75)
-    psi_s_min: float = .5*np.sqrt(2/3)*370/(2*np.pi*75)
-    rate_limit: float = np.inf
-    i_s_max: float = 1.5*np.sqrt(2)*5
-    alpha_psi: float = 2*np.pi*50
-    alpha_tau_max: float = 2*np.pi*50
-    alpha_f: float = 2*np.pi*1
-
-    # Observer
-    alpha_o: float = 2*np.pi*20
-    zeta_inf: float = .7
-
+    # Flux reference limits
+    psi_s_min: float = None
+    psi_s_max: float = None
+    # Voltage marginal
+    k_u: float = .9
+    # Bandwidths
+    alpha_psi: float = 2*np.pi*150
+    alpha_tau: float = 2*np.pi*50
+    alpha_s: float = 2*np.pi*4
+    # Maximum values
+    tau_M_max: float = 1.5*14
+    i_s_max: float = 1.5*np.sqrt(2)*5.
     # Motor parameter estimates
     R_s: float = 3.6
     L_d: float = .036
     L_q: float = .051
     psi_f: float = .545
-    p: int = 3
+    n_p: int = 3
+    J: float = .015
+    # Sensorless observer (used only in the sensorless mode)
+    w_o: float = 2*np.pi*100
+    zeta_inf: float = .2
+    # Sensored observer (used only in the sensored mode)
+    g: float = 2*np.pi*15
 
 
 # %%
-class SynchronousMotorVHzObsCtrl(Ctrl):
+class SynchronousMotorFluxVectorCtrl(Ctrl):
     """
-    Observer-based V/Hz control for synchronous motors.
+    Flux-vector control for synchronous motor drives.
+
+    This class interconnects the subsystems of the control system and
+    provides the interface to the solver.
 
     Parameters
     ----------
-    pars : SynchronousMotorVHzObsCtrlPars
+    pars : SynchronousMotoroFluxVectorCtrlPars
         Control parameters.
 
     """
 
     # pylint: disable=too-many-instance-attributes
     def __init__(self, pars):
         super().__init__()
-        # Instantiate classes
-        self.observer = SensorlessFluxObserver(pars)
-        self.pwm = PWM(pars)
-        self.rate_limiter = RateLimiter(pars)
-        # Reference
-        self.w_m_ref = pars.w_m_ref
-        # Motor parameters
-        self.R_s = pars.R_s
-        self.p = pars.p
-        # Controller parameters
         self.T_s = pars.T_s
-        self.alpha_f = pars.alpha_f
+        self.w_m_ref = pars.w_m_ref
+        self.sensorless = pars.sensorless
+        self.speed_ctrl = SpeedCtrl(pars)
+        self.pwm = PWM(pars)
+        if pars.sensorless:
+            self.observer = SensorlessObserver(pars)
+        else:
+            self.observer = Observer(pars)
+        self.flux_torque_ref = FluxTorqueRef(pars)
+        # Bandwidths
         self.alpha_psi = pars.alpha_psi
-        # MTPA
-        tq = TorqueCharacteristics(pars)
-        mtpa = tq.mtpa_locus(i_s_max=pars.i_s_max)
-        self.abs_psi_s_mtpa = mtpa.abs_psi_s_vs_tau_M
-        try:
-            self.psi_s_min = pars.psi_s_min
-        except AttributeError:
-            self.psi_s_min = 0
-        try:
-            self.psi_s_max = pars.psi_s_max
-        except AttributeError:
-            self.psi_s_max = np.inf
-        # Gain k_tau
-        abs_psi_s_mtpa0 = self.abs_psi_s_mtpa(0)
-        G = (pars.L_d - pars.L_q)/(pars.L_d*pars.L_q)
-        if pars.psi_f > 0:  # PMSM or PM-SyRM
-            c_delta_max = 1.5*pars.p*(
-                pars.psi_f*abs_psi_s_mtpa0/pars.L_d - G*abs_psi_s_mtpa0**2)
-        else:  # SyRM
-            c_delta_max = 1.5*pars.p*G*abs_psi_s_mtpa0**2
-        self.k_tau = pars.alpha_tau_max/c_delta_max
-        # Initial states
-        self.theta_s, self.tau_M_ref = 0, 0
+        self.alpha_tau = pars.alpha_tau
+        # Motor parameter estimates
+        self.R_s = pars.R_s
+        self.L_d = pars.L_d
+        self.L_q = pars.L_q
+        self.n_p = pars.n_p
 
     def __call__(self, mdl):
         """
         Run the main control loop.
 
         Parameters
         ----------
@@ -120,144 +118,121 @@
         T_s : float
             Sampling period.
         d_abc_ref : ndarray, shape (3,)
             Duty ratio references.
 
         """
         # Get the speed reference
-        w_m_ref = self.rate_limiter(self.w_m_ref(self.t))
+        w_m_ref = self.w_m_ref(self.t)
 
-        # Measure the feedback signals
+        # Feedback signals
         i_s_abc = mdl.motor.meas_currents()  # Phase currents
         u_dc = mdl.conv.meas_dc_voltage()  # DC-bus voltage
+        u_s = self.pwm.realized_voltage  # Realized voltage from PWM
+
+        if self.sensorless:
+            # Get the rotor speed and position estimates
+            w_m, theta_m = self.observer.w_m, self.observer.theta_m
+        else:
+            # Measure the rotor speed
+            w_m = self.n_p*mdl.mech.meas_speed()
+            # Limit the electrical rotor position into [-pi, pi)
+            theta_m = np.mod(
+                self.n_p*mdl.mech.meas_position() + np.pi, 2*np.pi) - np.pi
 
-        # Space vector and coordinate transformation
-        i_s = np.exp(-1j*self.theta_s)*abc2complex(i_s_abc)
+        # Current vector in estimated rotor coordinates
+        i_s = np.exp(-1j*theta_m)*abc2complex(i_s_abc)
 
-        # Get the states
-        u_s = self.pwm.realized_voltage
+        # Flux and torque estimates
         psi_s = self.observer.psi_s
-        tau_M_ref = self.tau_M_ref
+        tau_M = 1.5*self.n_p*np.imag(i_s*np.conj(psi_s))
 
-        # Electromagnetic torque (7d)
-        tau_M = 1.5*self.p*np.imag(i_s*np.conj(psi_s))
+        # Outputs
+        tau_M_ref = self.speed_ctrl.output(w_m_ref/self.n_p, w_m/self.n_p)
+        psi_s_ref, tau_M_ref_lim = self.flux_torque_ref(tau_M_ref, w_m, u_dc)
+
+        # Auxiliary current
+        i_a = psi_s.real/self.L_q + 1j*psi_s.imag/self.L_d - i_s
+
+        # Torque-production factor (c_tau = 0 corresponds to the MTPV condition)
+        c_tau = np.real(i_a*np.conj(psi_s))
+
+        # References for the flux and torque controllers
+        v_psi = self.alpha_psi*(psi_s_ref - np.abs(psi_s))
+        v_tau = self.alpha_tau*(tau_M_ref_lim - tau_M)
+        if c_tau > 0:
+            v = (np.abs(psi_s)*i_a*v_psi + 1j*psi_s*v_tau)/c_tau
+        else:
+            v = v_psi
 
-        # Dynamic frequency (5a)
-        w_s = w_m_ref - self.k_tau*(tau_M - tau_M_ref)
+        # Stator voltage reference
+        u_s_ref = self.R_s*i_s + 1j*w_m*psi_s + v
 
-        # Flux reference
-        psi_s_ref = self.abs_psi_s_mtpa(np.abs(tau_M_ref))
-        psi_s_ref = np.max([psi_s_ref, self.psi_s_min])
-        psi_s_ref = np.min([psi_s_ref, self.psi_s_max])
-
-        # Voltage reference (4)
-        err = psi_s_ref - psi_s
-        u_s_ref = self.R_s*i_s + 1j*w_s*psi_s_ref + self.alpha_psi*err
-
-        # Duty ratios
-        d_abc_ref, u_s_ref_lim = self.pwm.output(
-            u_s_ref, u_dc, self.theta_s, w_s)
+        # PWM output
+        d_abc_ref, u_s_ref_lim = self.pwm.output(u_s_ref, u_dc, theta_m, w_m)
 
         # Data logging
         data = Bunch(
             i_s=i_s,
             psi_s=psi_s,
             psi_s_ref=psi_s_ref,
             t=self.t,
-            theta_s=self.theta_s,
+            tau_M_ref_lim=tau_M_ref_lim,
+            theta_m=theta_m,
             u_dc=u_dc,
             u_s=u_s,
+            w_m=w_m,
             w_m_ref=w_m_ref,
-            w_s=w_s,
-            tau_M=tau_M,
         )
         self.save(data)
 
-        # Update the states
+        # Update states
+        self.observer.update(u_s, i_s, w_m)
+        self.speed_ctrl.update(tau_M_ref_lim)
         self.pwm.update(u_s_ref_lim)
-        self.observer.update(u_s, i_s, w_s)
-        self.tau_M_ref += self.T_s*self.alpha_f*(tau_M - self.tau_M_ref)
-        self.theta_s += self.T_s*w_s  # Next line: limit into [-pi, pi)
-        self.theta_s = np.mod(self.theta_s + np.pi, 2*np.pi) - np.pi
         self.update_clock(self.T_s)
 
         return self.T_s, d_abc_ref
 
 
 # %%
-class SensorlessFluxObserver:
+class Observer:
     """
-    Sensorless stator flux observer.
-
-    This observer is a variant of [1]_. The observer gain decouples the
-    electrical and mechanical dynamics and allows placing the poles of the
-    corresponding linearized estimation error dynamics. For simplicity, the
-    current model is here implemented in rotor coordinates, however this is
-    mathematically equivalent to controller coordinates implementation in [2]_.
+    Sensored observer.
 
     Parameters
     ----------
-    pars : SynchronousMotorObsVHzCtrlPars
+    pars : SynchronousMotoroFluxVectorCtrlPars
         Control parameters.
 
-    References
-    ----------
-    .. [1] Hinkkanen, Saarakkala, Awan, Mölsä, Tuovinen, "Observers for
-        sensorless synchronous motor drives: Framework for design and
-        analysis," IEEE Trans. Ind. Appl., 2018,
-        https://doi.org/10.1109/TIA.2018.2858753
-    .. [2] Tiitinen, Hinkkanen, Kukkola, Routimo, Pellegrino, Harnefors,
-        "Stable and passive observer-based V/Hz control for synchronous
-        Motors," in Proc. IEEE ECCE, Detroit, MI, Oct. 2022.
-
     """
 
     def __init__(self, pars):
         self.T_s = pars.T_s
         self.R_s = pars.R_s
         self.L_d = pars.L_d
         self.L_q = pars.L_q
         self.psi_f = pars.psi_f
-        self.alpha_o = pars.alpha_o
-        self.b_p = .5*pars.R_s*(pars.L_d + pars.L_q)/(pars.L_d*pars.L_q)
-        self.zeta_inf = pars.zeta_inf
-        # Initial states
-        self.delta, self.psi_s = 0, pars.psi_f
+        self.g = pars.g
+        # Initial state
+        self.psi_s = pars.psi_f
 
-    def update(self, u_s, i_s, w_s):
+    def update(self, u_s, i_s, w_m):
         """
         Update the states for the next sampling period.
 
         Parameters
         ----------
         u_s : complex
-            Stator voltage.
+            Stator voltage in estimated rotor coordinates.
         i_s : complex
-            Stator current.
-        w_s : float
-            Stator angular frequency.
+            Stator current in estimated rotor coordinates.
+        w_m : float
+            Rotor speed (in electrical rad/s).
 
         """
-        # Transformations to rotor coordinates
-        i_sr = i_s*np.exp(1j*self.delta)
-        psi_sr = self.psi_s*np.exp(1j*self.delta)
-
-        # Auxiliary flux and estimation error in rotor coordinates
-        psi_ar = self.psi_f + (self.L_d - self.L_q)*np.conj(i_sr)
-        e_r = self.L_d*i_sr.real + 1j*self.L_q*i_sr.imag + self.psi_f - psi_sr
-
-        # Auxiliary flux in controller coordinates
-        psi_a = np.exp(-1j*self.delta)*psi_ar
-
-        g_o = self.b_p + 2*self.zeta_inf*np.abs(w_s)
-
-        if np.abs(psi_ar) > 0:
-            # Correction voltage in controller coordinates
-            v = g_o*psi_a*np.real(e_r/psi_ar)
-            # Error signal
-            w_delta = self.alpha_o*np.imag(e_r/psi_ar)
-        else:
-            v, w_delta = 0, 0
+        # Estimation error
+        e = self.L_d*i_s.real + 1j*self.L_q*i_s.imag + self.psi_f - self.psi_s
 
-        # Update the states
-        self.psi_s += self.T_s*(u_s - self.R_s*i_s - 1j*w_s*self.psi_s + v)
-        self.delta += self.T_s*w_delta
+        # Update the state
+        self.psi_s += self.T_s*(
+            u_s - self.R_s*i_s - 1j*w_m*self.psi_s + self.g*e)
```

### Comparing `motulator-0.1.2/motulator/control/sm_signal_inj.py` & `motulator-0.1.3/motulator/control/sm_signal_inj.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,23 +1,20 @@
-# pylint: disable=invalid-name
 """
 Sensorless control with signal injection for synchronous motor drives.
 
 This module contains a simple example of square-wave signal injection for low-
 speed operation. A phase-locked loop is used to track the rotor position. For
 a wider speed range, signal injection could be combined to a model-based
 observer. The effects of magnetic saturation are not compensated for in this
 version.
 
 """
 
-from __future__ import annotations
 from dataclasses import dataclass
 import numpy as np
-
 from motulator.helpers import abc2complex, Bunch
 from motulator.control.common import Ctrl, SpeedCtrl, PWM
 from motulator.control.sm_vector import (
     CurrentCtrl, CurrentRef, SynchronousMotorVectorCtrlPars)
 
 
 # %%
@@ -44,15 +41,15 @@
     """
 
     # pylint: disable=too-many-instance-attributes
     def __init__(self, pars):
         super().__init__()
         self.T_s = pars.T_s
         self.w_m_ref = pars.w_m_ref
-        self.p = pars.p
+        self.n_p = pars.n_p
         self.current_ctrl = CurrentCtrl(pars)
         self.speed_ctrl = SpeedCtrl(pars)
         self.current_ref = CurrentRef(pars)
         self.pwm = PWM(pars)
         self.pll = PhaseLockedLoop(pars)
         self.signal_inj = SignalInjection(pars)
 
@@ -87,15 +84,15 @@
         # Current vector in estimated rotor coordinates
         i_s = np.exp(-1j*theta_m)*abc2complex(i_s_abc)
 
         # Filter the current measurement for the current controller
         i_s_filt = self.signal_inj.filter_current(i_s)
 
         # Outputs
-        tau_M_ref = self.speed_ctrl.output(w_m_ref/self.p, w_m/self.p)
+        tau_M_ref = self.speed_ctrl.output(w_m_ref/self.n_p, w_m/self.n_p)
         i_s_ref, tau_M_ref_lim = self.current_ref.output(tau_M_ref, w_m, u_dc)
         err = self.signal_inj.output(i_s.imag)
         # Superimpose the excitation voltage on the d-axis
         u_s_ref = self.current_ctrl.output(
             i_s_ref, i_s_filt) + self.signal_inj.u_sd_inj
         d_abc_ref, u_s_ref_lim = self.pwm.output(u_s_ref, u_dc, theta_m, w_m)
```

### Comparing `motulator-0.1.2/motulator/control/sm_torque.py` & `motulator-0.1.3/motulator/control/sm_torque.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,23 +1,28 @@
-# pylint: disable=C0103
 """
 Torque characteristics for synchronous machines.
 
 This contains computation and plotting of torque characteristics for
-synchronous machines, including the MTPA and MTPV loci. The methods can be used
-to define look-up tables for control as well as to analyze the characteristics.
+synchronous machines, including the MTPA and MTPV loci [1]_. The methods can be
+used to define look-up tables for control and to analyze the characteristics.
 In this version, the magnetic saturation is omitted.
 
+References
+----------
+.. [1] Morimoto, Takeda, Hirasa, Taniguchi, "Expansion of operating limits for
+   permanent magnet motor by current vector control considering inverter
+   capacity," IEEE Trans. Ind. Appl., 1990,
+   https://doi.org/10.1109/28.60058
+
 """
 from sys import float_info
 import numpy as np
 from scipy.interpolate import interp1d
 import matplotlib.pyplot as plt
 from cycler import cycler
-
 from motulator.helpers import Bunch
 
 plt.rcParams['axes.prop_cycle'] = cycler(color='brgcmyk')
 plt.rcParams['lines.linewidth'] = 1.
 plt.rcParams.update({"text.usetex": False})  # Disable LaTeX in plots
 
 
@@ -32,15 +37,15 @@
     ----------
     pars : data object
         Motor parameters.
 
     """
 
     def __init__(self, pars):
-        self.p = pars.p
+        self.n_p = pars.n_p
         self.L_d = pars.L_d
         self.L_q = pars.L_q
         self.psi_f = pars.psi_f
         try:
             self.psi_s_min = pars.psi_s_min
         except AttributeError:
             self.psi_s_min = None
@@ -61,15 +66,15 @@
         Returns
         -------
         tau_M : float
             Electromagnetic torque.
 
         """
         i_s = self.current(psi_s)
-        tau_M = 1.5*self.p*np.imag(i_s*np.conj(psi_s))
+        tau_M = 1.5*self.n_p*np.imag(i_s*np.conj(psi_s))
 
         return tau_M
 
     def current(self, psi_s):
         """
         Compute the stator current as a function of the stator flux linkage.
 
@@ -269,16 +274,16 @@
 
         psi_s = self.flux(i_s)
         tau_M = self.torque(psi_s)
 
         # Create an interpolant that can be used as a look-up table. If needed,
         # more interpolants can be easily added.
         abs_psi_s_vs_tau_M = interp1d(
-            tau_M, np.abs(psi_s), fill_value="extrapolate")
-        i_sd_vs_tau_M = interp1d(tau_M, i_s.real, fill_value="extrapolate")
+            tau_M, np.abs(psi_s), fill_value='extrapolate')
+        i_sd_vs_tau_M = interp1d(tau_M, i_s.real, fill_value='extrapolate')
 
         # Return the result as a bunch object
         return Bunch(
             psi_s=psi_s,
             i_s=i_s,
             tau_M=tau_M,
             abs_psi_s_vs_tau_M=abs_psi_s_vs_tau_M,
@@ -432,52 +437,20 @@
 
         # Create an interpolant that can be used as a look-up table
         tau_M_vs_abs_psi_s = interp1d(
             np.abs(psi_s),
             tau_M,
             bounds_error=False,
             fill_value=(tau_M[0], tau_M[-1]))
-        i_sd_vs_tau_M = interp1d(tau_M, i_sd, fill_value="extrapolate")
+        i_sd_vs_tau_M = interp1d(tau_M, i_sd, fill_value='extrapolate')
 
         # Return the result as a bunch object
         return Bunch(
             tau_M_vs_abs_psi_s=tau_M_vs_abs_psi_s, i_sd_vs_tau_M=i_sd_vs_tau_M)
 
-    def delta_at_zero_torque(self, abs_psi_s):
-        """
-        Compute the load angle value at the zero torque.
-
-        This computes the "nontrivial" load angle value corresponding to the
-        zero electromagnetic torque.
-
-        Parameters
-        ----------
-        abs_psi_s : float
-            Stator flux magnitude.
-
-        Returns
-        -------
-        delta : float
-            Load angle at the zero torque.
-
-        """
-        if self.psi_f > 0:
-            c = ((self.L_q - self.L_d)/self.L_q*abs_psi_s/self.psi_f)**2 - 1
-            if c > 0:
-                if self.L_q > self.L_d:
-                    delta = np.arctan((np.sqrt(c)))
-                else:
-                    delta = np.pi - np.arctan((np.sqrt(c)))
-            else:
-                delta = 0
-        else:
-            delta = 0
-
-        return delta
-
     def plot_flux_loci(self, i_s_max, base, N=20):
         """
         Plot the stator flux linkage loci.
 
         Per-unit quantities are used.
 
         Parameters
@@ -656,46 +629,7 @@
         except AttributeError:
             pass
         ax.plot(np.abs(clim.psi_s)/base.psi, clim.tau_M/base.tau)
 
         ax.legend(['MTPA', 'MTPV', 'Const current'])
         ax.set_xlabel(r'$\psi_\mathrm{s}$ (p.u.)')
         ax.set_ylabel(r'$\tau_\mathrm{m}$ (p.u.)')
-
-    def plot_angle_torque(self, abs_psi_s, base, N=100):
-        """
-        Plot the electromagnetic torque as a function of the load angle.
-
-        Per-unit quantities are used.
-
-        Parameters
-        ----------
-        abs_psi_s : float
-            Stator flux magnitude.
-        base : object
-            Base values.
-        N : int, optional
-            Amount of points to be evaluated. The default is 100.
-
-        """
-        delta = np.linspace(-np.pi, np.pi, N)
-        psi_s = abs_psi_s*np.exp(1j*delta)
-        tau_M = self.torque(psi_s)
-
-        delta_mtpv = self.mtpv(abs_psi_s)
-        psi_s_mtpv = abs_psi_s*np.exp(1j*delta_mtpv)
-        tau_M_mtpv = self.torque(psi_s_mtpv)
-
-        delta0 = self.delta_at_zero_torque(abs_psi_s)
-        psi_s0 = abs_psi_s*np.exp(1j*delta0)
-        tau_M0 = self.torque(psi_s0)
-
-        _, ax = plt.subplots()
-        ax.plot(180*delta/np.pi, tau_M/base.tau)
-        ax.plot(180*delta_mtpv/np.pi, tau_M_mtpv/base.tau, 'o')
-        ax.plot(180*delta0/np.pi, tau_M0/base.tau, 'x')
-
-        ax.set_xlim([-180, 180])
-        ax.set_xticks([-180, -135, -90, -45, 0, 45, 90, 135, 180])
-        ax.set_xlabel(r'$\delta$ (deg)')
-        ax.set_ylabel(r'$\tau_\mathrm{m}$ (p.u.)')
-        ax.set_title(r'$\psi_\mathrm{s}=$ %1.2f p.u.' % (abs_psi_s/base.psi))
```

### Comparing `motulator-0.1.2/motulator/control/sm_vector.py` & `motulator-0.1.3/motulator/control/sm_vector.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,15 +1,12 @@
-# pylint: disable=invalid-name
 """Current vector control for synchronous motor drives."""
 
-from __future__ import annotations
-from collections.abc import Callable
+from typing import Callable
 from dataclasses import dataclass, field
 import numpy as np
-
 from motulator.helpers import abc2complex, Bunch
 from motulator.control.common import Ctrl, SpeedCtrl, PWM
 from motulator.control.sm_torque import TorqueCharacteristics
 
 
 # %%
 @dataclass
@@ -27,46 +24,30 @@
     # Bandwidths
     alpha_c: float = 2*np.pi*200
     alpha_fw: float = 2*np.pi*20
     alpha_s: float = 2*np.pi*4
     # Maximum values
     tau_M_max: float = 2*14
     i_s_max: float = 1.5*np.sqrt(2)*5
-    psi_s_min: float = 0
+    psi_s_min: float = None
     # Voltage margin
     k_u: float = .95
     # Nominal values
     w_nom: float = 2*np.pi*75
     # Motor parameter estimates
     R_s: float = 3.6
     L_d: float = .036
     L_q: float = .051
     psi_f: float = .545
-    p: int = 3
+    n_p: int = 3
     J: float = .015
     # Sensorless observer
     w_o: float = 2*np.pi*40  # Used only in the sensorless mode
     zeta_inf: float = .2
 
-    def plot_luts(self, base):
-        """
-        Plot control look-up tables.
-
-        Parameters
-        ----------
-        base : BaseValues
-            Base values for scaling the plots.
-
-        """
-        tq = TorqueCharacteristics(self)
-        tq.plot_current_loci(self.i_s_max, base)
-        tq.plot_torque_flux(self.i_s_max, base)
-        tq.plot_torque_current(self.i_s_max, base)
-        # tq.plot_flux_loci(self.i_s_max, base)
-
 
 # %%
 class SynchronousMotorVectorCtrl(Ctrl):
     """
     Vector control for a synchronous motor drive.
 
     This class interconnects the subsystems of the control system and
@@ -80,15 +61,15 @@
     """
 
     # pylint: disable=too-many-instance-attributes
     def __init__(self, pars):
         super().__init__()
         self.T_s = pars.T_s
         self.w_m_ref = pars.w_m_ref
-        self.p = pars.p
+        self.n_p = pars.n_p
         self.sensorless = pars.sensorless
         self.current_ctrl = CurrentCtrl(pars)
         self.speed_ctrl = SpeedCtrl(pars)
         self.current_ref = CurrentRef(pars)
         self.pwm = PWM(pars)
         if pars.sensorless:
             self.observer = SensorlessObserver(pars)
@@ -118,30 +99,30 @@
 
         # Measure the feedback signals
         i_s_abc = mdl.motor.meas_currents()  # Phase currents
         u_dc = mdl.conv.meas_dc_voltage()  # DC-bus voltage
 
         if not self.sensorless:
             # Measure the rotor speed
-            w_m = self.p*mdl.mech.meas_speed()
+            w_m = self.n_p*mdl.mech.meas_speed()
             # Limit the electrical rotor position into [-pi, pi)
             theta_m = np.mod(
-                self.p*mdl.mech.meas_position() + np.pi, 2*np.pi) - np.pi
+                self.n_p*mdl.mech.meas_position() + np.pi, 2*np.pi) - np.pi
         else:
             # Get the rotor speed and position estimates
             w_m, theta_m = self.observer.w_m, self.observer.theta_m
 
         # Get the realized voltage from the PWM method
         u_s = self.pwm.realized_voltage
 
         # Current vector in estimated rotor coordinates
         i_s = np.exp(-1j*theta_m)*abc2complex(i_s_abc)
 
         # Outputs
-        tau_M_ref = self.speed_ctrl.output(w_m_ref/self.p, w_m/self.p)
+        tau_M_ref = self.speed_ctrl.output(w_m_ref/self.n_p, w_m/self.n_p)
         i_s_ref, tau_M_ref_lim = self.current_ref.output(tau_M_ref, w_m, u_dc)
         u_s_ref = self.current_ctrl.output(i_s_ref, i_s)
         d_abc_ref, u_s_ref_lim = self.pwm.output(u_s_ref, u_dc, theta_m, w_m)
 
         # Data logging
         data = Bunch(
             i_s=i_s,
@@ -193,15 +174,14 @@
     .. [1] Awan, Saarakkala, Hinkkanen, "Flux-linkage-based current control of
        saturated synchronous motors," IEEE Trans. Ind. Appl. 2019,
        https://doi.org/10.1109/TIA.2019.2919258
 
     """
 
     def __init__(self, pars):
-
         self.T_s = pars.T_s
         self.L_d = pars.L_d
         self.L_q = pars.L_q
         self.alpha_c = pars.alpha_c
         # Integral state
         self.u_i = 0
         # Memory for the update method
@@ -283,18 +263,17 @@
        accurate torque regulation," IEEE Trans. Ind. Appl., 2020,
        https://doi.org/10.1109/TIA.2019.2942807
 
     """
 
     # pylint: disable=too-many-instance-attributes
     def __init__(self, pars):
-
         self.T_s = pars.T_s
         self.i_s_max = pars.i_s_max
-        self.p = pars.p
+        self.n_p = pars.n_p
         self.L_d = pars.L_d
         self.L_q = pars.L_q
         self.psi_f = pars.psi_f
         self.k = pars.alpha_fw/(pars.w_nom*self.L_d)
         self.k_u = pars.k_u
         # Generate LUTs
         tq = TorqueCharacteristics(pars)
@@ -343,30 +322,30 @@
             return tau_M_ref
 
         # Limit the torque reference according to MTPV and current limits
         tau_M_ref = limit_torque(tau_M_ref, w_m, u_dc)
 
         # q-axis current reference
         psi_t = self.psi_f + (self.L_d - self.L_q)*self.i_sd_ref
-        i_sq_ref = tau_M_ref/(1.5*self.p*psi_t) if psi_t != 0 else 0
+        i_sq_ref = tau_M_ref/(1.5*self.n_p*psi_t) if psi_t != 0 else 0
 
         # Limit the q-axis current reference
         i_sd_mtpa = self.i_sd_mtpa(np.abs(tau_M_ref))
         i_sq_max = np.min([
             np.sqrt(self.i_s_max**2 - self.i_sd_ref**2),
             np.sqrt(self.i_s_max**2 - i_sd_mtpa**2)
         ])
         if np.abs(i_sq_ref) > i_sq_max:
             i_sq_ref = np.sign(i_sq_ref)*i_sq_max
 
         # Current reference
         i_s_ref = self.i_sd_ref + 1j*i_sq_ref
 
         # Limited torque (for the speed controller)
-        tau_M_ref_lim = 1.5*self.p*psi_t*i_sq_ref
+        tau_M_ref_lim = 1.5*self.n_p*psi_t*i_sq_ref
 
         return i_s_ref, tau_M_ref_lim
 
     def update(self, tau_M_ref_lim, u_s_ref, u_dc):
         """
         Field-weakening based on the unlimited reference voltage.
 
@@ -413,17 +392,15 @@
     .. [3] Hinkkanen, Saarakkala, Awan, Mölsä, Tuovinen, "Observers for
        sensorless synchronous motor drives: Framework for design and analysis,"
        IEEE Trans. Ind. Appl., 2018, https://doi.org/10.1109/TIA.2018.2858753
 
     """
 
     # pylint: disable=too-many-instance-attributes
-    # pylint: disable=too-few-public-methods
     def __init__(self, pars):
-
         self.T_s = pars.T_s
         self.R_s = pars.R_s
         self.L_d = pars.L_d
         self.L_q = pars.L_q
         self.psi_f = pars.psi_f
         self.k_p = 2*pars.w_o
         self.k_i = pars.w_o**2
```

### Comparing `motulator-0.1.2/motulator/helpers.py` & `motulator-0.1.3/motulator/helpers.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,12 +1,10 @@
-# pylint: disable=invalid-name
 """Helper functions and classes."""
 
 # %%
-from __future__ import annotations
 from dataclasses import dataclass
 import numpy as np
 
 
 # %%
 def abc2complex(u):
     """
@@ -70,31 +68,32 @@
 
     Base values are computed from the nominal values and the number of pole
     pairs. They can be used, e.g., for scaling the plotted waveforms.
 
     """
 
     # pylint: disable=too-many-instance-attributes
-    U_nom: float
-    I_nom: float
-    f_nom: float
-    P_nom: float
-    tau_nom: float
-    p: int
+    # Nominal values
+    U_nom: float  # Voltage (rms, line-line)
+    I_nom: float  # Current (rms)
+    f_nom: float  # Frequency
+    P_nom: float  # Power
+    tau_nom: float  # Torque
+    n_p: int  # Number of pole pairs
 
     def __post_init__(self):
         """Compute the base values."""
         self.u = np.sqrt(2/3)*self.U_nom
         self.i = np.sqrt(2)*self.I_nom
         self.w = 2*np.pi*self.f_nom
         self.psi = self.u/self.w
-        self.P = 1.5*self.u*self.i
+        self.p = 1.5*self.u*self.i
         self.Z = self.u/self.i
         self.L = self.Z/self.w
-        self.tau = self.p*self.P/self.w
+        self.tau = self.n_p*self.p/self.w
 
 
 # %%
 class Sequence:
     """
     Sequence generator.
 
@@ -108,15 +107,14 @@
     values : ndarray
         Output values.
     periodic : bool, optional
         Enables periodicity. The default is False.
 
     """
 
-    # pylint: disable=too-few-public-methods
     def __init__(self, times, values, periodic=False):
         self.times = times
         self.values = values
         if periodic is True:
             self._period = times[-1] - times[0]
         else:
             self._period = None
@@ -139,15 +137,14 @@
         return np.interp(t, self.times, self.values, period=self._period)
 
 
 # %%
 class Step:
     """Step function."""
 
-    # pylint: disable=too-few-public-methods
     def __init__(self, step_time, step_value, initial_value=0):
         self.step_time = step_time
         self.step_value = step_value
         self.initial_value = initial_value
 
     def __call__(self, t):
         """
```

### Comparing `motulator-0.1.2/motulator/model/converter.py` & `motulator-0.1.3/motulator/model/converter.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,7 @@
-# pylint: disable=invalid-name
 """
 Power converter models.
 
 An inverter with constant DC-bus voltage and a frequency converter with a diode
 front-end rectifier are modeled. Complex space vectors are used also for duty
 ratios and switching states, wherever applicable. In this module, all space
 vectors are in stationary coordinates. The default values correspond to a
@@ -162,15 +161,15 @@
         list, length 2
             Time derivative of the state vector, [du_dc, d_iL]
 
         """
         # Grid phase voltages
         u_g_abc = self.grid_voltages(t)
         # Output voltage of the diode bridge
-        u_di = np.amax(u_g_abc, 0) - np.amin(u_g_abc, 0)
+        u_di = np.amax(u_g_abc, axis=0) - np.amin(u_g_abc, axis=0)
         # State derivatives
         du_dc = (i_L - i_dc)/self.C
         di_L = (u_di - u_dc)/self.L
         # The inductor current cannot be negative due to the diode bridge
         if i_L < 0 and di_L < 0:
             di_L = 0
         return [du_dc, di_L]
```

### Comparing `motulator-0.1.2/motulator/model/im.py` & `motulator-0.1.3/motulator/model/im.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,33 +1,31 @@
-# pylint: disable=invalid-name
 """
 Continuous-time models for induction motors.
 
 Peak-valued complex space vectors are used. The space vector models are
 implemented in stator coordinates. The default values correspond to a 2.2-kW
 induction motor.
 
 """
 import numpy as np
-
 from motulator.helpers import complex2abc
 
 
 # %%
 class InductionMotor:
     """
     Γ-equivalent model of an induction motor.
 
     An induction motor is modeled using the Γ-equivalent model [1]_. The model
     is implemented in stator coordinates. The flux linkages are used as state
     variables.
 
     Parameters
     ----------
-    p : int
+    n_p : int
         Number of pole pairs.
     R_s : float
         Stator resistance.
     R_r : float
         Rotor resistance.
     L_ell : float
         Leakage inductance.
@@ -44,17 +42,17 @@
     References
     ----------
     .. [1] Slemon, "Modelling of induction machines for electric drives," IEEE
        Trans. Ind. Appl., 1989, https://doi.org/10.1109/28.44251.
 
     """
 
-    def __init__(self, p=2, R_s=3.7, R_r=2.5, L_ell=.023, L_s=.245):
+    def __init__(self, n_p=2, R_s=3.7, R_r=2.5, L_ell=.023, L_s=.245):
         # pylint: disable=too-many-arguments
-        self.p = p
+        self.n_p = n_p
         self.R_s, self.R_r = R_s, R_r
         self.L_ell, self.L_s = L_ell, L_s
         # Initial values
         self.psi_ss0, self.psi_rs0 = 0j, 0j
 
     def currents(self, psi_ss, psi_rs):
         """
@@ -98,15 +96,15 @@
         i_rs : complex
             Rotor current.
         tau_M : float
             Electromagnetic torque.
 
         """
         i_ss, i_rs = self.currents(psi_ss, psi_rs)
-        tau_M = 1.5*self.p*np.imag(i_ss*np.conj(psi_ss))
+        tau_M = 1.5*self.n_p*np.imag(i_ss*np.conj(psi_ss))
 
         return i_ss, i_rs, tau_M
 
     def f(self, psi_ss, psi_rs, u_ss, w_M):
         """
         Compute the state derivatives.
 
@@ -136,15 +134,15 @@
         output signals (stator current `i_ss` and torque `tau_M`) needed for
         interconnection with other subsystems. This avoids overlapping
         computation in simulation.
 
         """
         i_ss, i_rs, tau_M = self.magnetic(psi_ss, psi_rs)
         dpsi_ss = u_ss - self.R_s*i_ss
-        dpsi_rs = -self.R_r*i_rs + 1j*self.p*w_M*psi_rs
+        dpsi_rs = -self.R_r*i_rs + 1j*self.n_p*w_M*psi_rs
 
         return [dpsi_ss, dpsi_rs], i_ss, tau_M
 
     def meas_currents(self):
         """
         Measure the phase currents at the end of the sampling period.
 
@@ -169,15 +167,15 @@
     This extends the InductionMotor class with a main-flux magnetic saturation
     model [2]_::
 
         L_s(psi_ss) = L_su/(1 + (beta*abs(psi_ss)**S)
 
     Parameters
     ----------
-    p : int
+    n_p : int
         Number of pole pairs.
     R_s : float
         Stator resistance.
     R_r : float
         Rotor resistance.
     L_ell : float
         Leakage inductance.
@@ -193,17 +191,24 @@
     .. [2] Qu, Ranta, Hinkkanen, Luomi, "Loss-minimizing flux level control of
        induction motor drives," IEEE Trans. Ind. Appl., 2012,
        https://doi.org/10.1109/TIA.2012.2190818
 
     """
 
     def __init__(
-            self, p=2, R_s=3.7, R_r=2.5, L_ell=.023, L_su=.34, beta=.84, S=7):
+            self,
+            n_p=2,
+            R_s=3.7,
+            R_r=2.5,
+            L_ell=.023,
+            L_su=.34,
+            beta=.84,
+            S=7):
         # pylint: disable=too-many-arguments
-        super().__init__(p=p, R_s=R_s, R_r=R_r, L_ell=L_ell)
+        super().__init__(n_p=n_p, R_s=R_s, R_r=R_r, L_ell=L_ell)
         # Saturation model
         self.L_s = lambda psi: L_su/(1. + (beta*np.abs(psi))**S)
 
     def currents(self, psi_ss, psi_rs):
         """Override the base class method."""
         # Saturated value of the stator inductance.
         L_s = self.L_s(psi_ss)
@@ -220,32 +225,32 @@
 
     This extends the InductionMotor class (based on the Γ model) by providing
     an interface for the inverse-Γ model parameters. Linear magnetics are
     assumed. If magnetic saturation is to be modeled, the Γ model is preferred.
 
     Parameters
     ----------
-    p : int
+    n_p : int
         Number of pole pairs.
     R_s : float
         Stator resistance.
     R_R : float
         Rotor resistance.
     L_sgm : float
         Leakage inductance.
     L_M : float
         Magnetizing inductance.
 
     """
 
-    def __init__(self, p=2, R_s=3.7, R_R=2.1, L_sgm=.021, L_M=.224):
+    def __init__(self, n_p=2, R_s=3.7, R_R=2.1, L_sgm=.021, L_M=.224):
         # pylint: disable=too-many-arguments, disable=super-init-not-called
         # Convert the inverse-Γ parameters to the Γ parameters
         gamma = L_M/(L_M + L_sgm)  # Magnetic coupling factor
-        self.p = p
+        self.n_p = n_p
         self.R_s = R_s
         self.L_s = L_M + L_sgm
         self.L_ell = L_sgm/gamma
         self.R_r = R_R/gamma**2
         # Initial values
         self.psi_ss0 = 0j
         self.psi_rs0 = 0j  # self.psi_rs0 = self.psi_Rs0/gamma
```

### Comparing `motulator-0.1.2/motulator/model/im_drive.py` & `motulator-0.1.3/motulator/model/im_drive.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,7 @@
-# pylint: disable=invalid-name
 """
 Continuous-time models for induction motor drives.
 
 Peak-valued complex space vectors are used. The space vector models are
 implemented in stator coordinates. The default values correspond to a 2.2-kW
 induction motor.
 
@@ -131,16 +130,16 @@
 
         # Some useful variables
         self.data.i_ss, _, self.data.tau_M = self.motor.magnetic(
             self.data.psi_ss, self.data.psi_rs)
         self.data.theta_M = np.mod(  # Limit into [-pi, pi)
             self.data.theta_M + np.pi, 2*np.pi) - np.pi
         self.data.theta_m = np.mod(  # Limit into [-pi, pi)
-            self.motor.p*self.data.theta_M + np.pi, 2*np.pi) - np.pi
-        self.data.w_m = self.motor.p*self.data.w_M
+            self.motor.n_p*self.data.theta_M + np.pi, 2*np.pi) - np.pi
+        self.data.w_m = self.motor.n_p*self.data.w_M
         self.data.tau_L = (
             self.mech.tau_L_t(self.data.t) + self.mech.tau_L_w(self.data.w_M))
         self.data.u_ss = self.conv.ac_voltage(self.data.q, self.conv.u_dc0)
 
         # Compute the inverse-Γ rotor flux
         try:
             # Saturable stator inductance
@@ -217,18 +216,18 @@
         self.data.i_L = np.asarray(self.data.i_L)
         # Some useful variables
         self.data.u_ss = self.conv.ac_voltage(self.data.q, self.data.u_dc)
         self.data.i_dc = self.conv.dc_current(self.data.q, self.data.i_ss)
         u_g_abc = self.conv.grid_voltages(self.data.t)
         self.data.u_g = abc2complex(u_g_abc)
         # Voltage at the output of the diode bridge
-        self.data.u_di = np.amax(u_g_abc, 0) - np.amin(u_g_abc, 0)
+        self.data.u_di = np.amax(u_g_abc, axis=0) - np.amin(u_g_abc, axis=0)
         # Diode briddge switching states (-1, 0, 1)
-        q_g_abc = ((np.amax(u_g_abc, 0) == u_g_abc).astype(int) -
-                   (np.amin(u_g_abc, 0) == u_g_abc).astype(int))
+        q_g_abc = ((np.amax(u_g_abc, axis=0) == u_g_abc).astype(int) -
+                   (np.amin(u_g_abc, axis=0) == u_g_abc).astype(int))
         # Grid current space vector
         self.data.i_g = abc2complex(q_g_abc)*self.data.i_L
 
 
 # %%
 class InductionMotorDriveTwoMass(InductionMotorDrive):
     """
@@ -250,28 +249,29 @@
 
     def __init__(self, motor=None, mech=None, conv=None):
         super().__init__(motor=motor, mech=mech, conv=conv)
         self.data.w_L, self.data.theta_ML = [], []
 
     def get_initial_values(self):
         """Extend the base class."""
-        x0 = super().get_initial_values() + [self.mech.w_L0,
-                                             self.mech.theta_ML0]
+        x0 = super().get_initial_values() + [
+            self.mech.w_L0, self.mech.theta_ML0
+        ]
         return x0
 
     def set_initial_values(self, t0, x0):
         """Extend the base class."""
         super().set_initial_values(t0, x0[0:4])
         self.mech.w_L0 = x0[4].real
         self.mech.theta_ML0 = np.mod(x0[5].real + np.pi, 2*np.pi) - np.pi
 
     def f(self, t, x):
         """Override the base class."""
         # Unpack the states
-        psi_ss, psi_rs, w_M, theta_M, w_L, theta_ML = x
+        psi_ss, psi_rs, w_M, _, w_L, theta_ML = x
         # Interconnections: outputs for computing the state derivatives
         u_ss = self.conv.ac_voltage(self.conv.q, self.conv.u_dc0)
         # State derivatives plus the outputs for interconnections
         motor_f, _, tau_M = self.motor.f(psi_ss, psi_rs, u_ss, w_M)
         mech_f = self.mech.f(t, w_M, w_L, theta_ML, tau_M)
         # List of state derivatives
         return motor_f + mech_f
```

### Comparing `motulator-0.1.2/motulator/model/mech.py` & `motulator-0.1.3/motulator/model/mech.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,7 @@
-# pylint: disable=invalid-name
 """Continuous-time models for mechanical subsystems."""
 
 
 # %%
 class Mechanics:
     """
     Mechanics subsystem.
@@ -107,16 +106,22 @@
         tau_L_w = b*w_L, where b is the viscous friction coefficient.
     tau_L_t : function
         Load torque as a function of time, `tau_L_t(t)`.
 
     """
 
     # pylint: disable=too-many-instance-attributes
-    def __init__(self, J_M=.005, J_L=.005, K_S=700., C_S=.13,
-                 tau_L_w=lambda w_M: 0, tau_L_t=lambda t: 0):
+    def __init__(
+            self,
+            J_M=.005,
+            J_L=.005,
+            K_S=700.,
+            C_S=.13,
+            tau_L_w=lambda w_M: 0,
+            tau_L_t=lambda t: 0):
         # pylint: disable=too-many-arguments
         # pylint: disable=super-init-not-called
         self.J_M = J_M
         self.J_L = J_L
         self.K_S = K_S
         self.C_S = C_S
         self.tau_L_t = tau_L_t
```

### Comparing `motulator-0.1.2/motulator/model/sm.py` & `motulator-0.1.3/motulator/model/sm.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,8 +1,7 @@
-# pylint: disable=invalid-name
 """
 Continuous-time models for synchronous motors.
 
 The motor models can be parametrized to represent permanent-magnet synchronous
 motors and synchronous reluctance motors. Peak-valued complex space vectors are
 used.
 
@@ -20,15 +19,15 @@
 
     This models a synchronous motor in rotor coordinates. The stator flux
     linkage is the state variable. The default values correspond to a 2.2-kW
     permanent-magnet synchronous motor.
 
     Parameters
     ----------
-    p : int
+    n_p : int
         Number of pole pairs.
     R_s : float
         Stator resistance.
     L_d : float
         d-axis inductance.
     L_q : float
         q-axis inductance.
@@ -37,17 +36,17 @@
     mech : Mechanics
         Model of the mechanical subsystem, needed only for the coordinate
         transformation in the measure_currents method.
 
     """
 
     def __init__(
-            self, p=3, R_s=3.6, L_d=.036, L_q=.051, psi_f=.545, mech=None):
+            self, n_p=3, R_s=3.6, L_d=.036, L_q=.051, psi_f=.545, mech=None):
         # pylint: disable=too-many-arguments
-        self.p, self.R_s = p, R_s
+        self.n_p, self.R_s = n_p, R_s
         self.L_d, self.L_q, self.psi_f = L_d, L_q, psi_f
         # Initial value
         self.psi_s0 = self.psi_f + 0j
         # For the coordinate transformation
         self._mech = mech
 
     def current(self, psi_s):
@@ -82,15 +81,15 @@
         i_s : complex
             Stator current.
         tau_M : float
             Electromagnetic torque.
 
         """
         i_s = self.current(psi_s)
-        tau_M = 1.5*self.p*np.imag(i_s*np.conj(psi_s))
+        tau_M = 1.5*self.n_p*np.imag(i_s*np.conj(psi_s))
         return i_s, tau_M
 
     def f(self, psi_s, u_s, w_M):
         """
         Compute the state derivative.
 
         Parameters
@@ -116,29 +115,29 @@
         In addition to the state derivative, this method also returns the
         output signals (stator current `i_ss` and torque `tau_M`) needed for
         interconnection with other subsystems. This avoids overlapping
         computation in simulation.
 
         """
         i_s, tau_M = self.magnetic(psi_s)
-        dpsi_s = u_s - self.R_s*i_s - 1j*self.p*w_M*psi_s
+        dpsi_s = u_s - self.R_s*i_s - 1j*self.n_p*w_M*psi_s
         return [dpsi_s], i_s, tau_M
 
     def meas_currents(self):
         """
         Measure the phase currents at the end of the sampling period.
 
         Returns
         -------
         i_s_abc : 3-tuple of floats
             Phase currents.
 
         """
         i_s0 = self.current(self.psi_s0)
-        theta_m0 = self.p*self._mech.theta_M0
+        theta_m0 = self.n_p*self._mech.theta_M0
         i_s_abc = complex2abc(np.exp(1j*theta_m0)*i_s0)
         return i_s_abc
 
 
 # %%
 class SynchronousMotorSaturated(SynchronousMotor):
     """
@@ -147,15 +146,15 @@
     This extends the SynchronousMotor class with an analytical saturation
     model [1]_, [2]_. The permanent magnets (PMs) are assumed to be along the
     d-axis. The default values correspond to a 6.7-kW synchronous reluctance
     motor.
 
     Parameters
     ----------
-    p : int
+    n_p : int
         Number of pole pairs.
     R_s : float
         Stator resistance.
     i_f : float
         Constant current corresponding to the magnetomotive force (MMF) of PMs.
         In the magnetically linear case, `i_f = psi_f/L_d`.
     a_d0 : float
@@ -213,42 +212,43 @@
        Appl., 2009, https://doi.org/10.1109/TIA.2008.2009493
 
     """
 
     # pylint: disable=too-many-instance-attributes
     def __init__(
         self,
-        p=2,
+        n_p=2,
         R_s=.54,
         i_f=0,
         a_d0=17.4,
         a_q0=52.1,
         a_dd=373.,
         a_qq=658.,
         a_dq=1120.,
         S=5,
         T=1,
         U=1,
         V=0,
         mech=None,
     ):
         # pylint: disable=too-many-arguments, disable=super-init-not-called
-        self.p, self.R_s = p, R_s
+        self.n_p, self.R_s = n_p, R_s
         self.i_f, self.a_d0, self.a_q0 = i_f, a_d0, a_q0
         self.a_dd, self.a_qq, self.a_dq = a_dd, a_qq, a_dq
         self.S, self.T, self.U, self.V = S, T, U, V
 
         # Initial value of the stator flux
         if i_f == 0:
             # No magnets
             self.psi_s0 = 0j
         else:
             # Solve the stator flux caused by the magnets @ i_s = 0
             res = minimize_scalar(
-                lambda psi_d: np.abs((a_d0 + a_dd*np.abs(psi_d)**S)*psi_d - i_f))
+                lambda psi_d: np.abs(
+                    (a_d0 + a_dd*np.abs(psi_d)**S)*psi_d - i_f))
             self.psi_s0 = complex(res.x)
             print(self.psi_s0)
 
         # For the coordinate transformation
         self._mech = mech
 
     def current(self, psi_s):
@@ -276,15 +276,15 @@
     This extends the SynchronousMotor class with a saturation model, where the
     stator current depends on the stator flux linkage. The coordinates assume
     the PMSM convention, i.e., that the PM flux is along the d-axis.
     Unstructured flux map data can be used.
 
     Parameters
     ----------
-    p : int
+    n_p : int
         Number of pole pairs.
     R_s : float
         Stator resistance.
     psi_s_data : ndarray of complex
         Stator flux data points for creating the interpolant.
     i_s_data : ndarray of complex
         Stator current data values for creating the interpolant.
@@ -292,26 +292,27 @@
         Model of the mechanical subsystem, needed only for the coordinate
         transformation in the measure_currents method.
 
     """
 
     # pylint: disable=too-many-arguments, disable=super-init-not-called
     def __init__(
-            self, p=2, R_s=.20, psi_s_data=None, i_s_data=None, mech=None):
+            self, n_p=2, R_s=.20, psi_s_data=None, i_s_data=None, mech=None):
 
-        self.p, self.R_s = p, R_s
+        self.n_p, self.R_s = n_p, R_s
 
         # Create the interpolant
         self.i_s = LinearNDInterpolator(
             list(zip(psi_s_data.real, psi_s_data.imag)), i_s_data)
 
         # Solve the PM flux for the initial value of the stator flux
-        res = minimize_scalar(lambda psi_d: np.abs(self.i_s(psi_d, 0)),
-                              bounds=(0, np.max(psi_s_data.real)),
-                              method='bounded')
+        res = minimize_scalar(
+            lambda psi_d: np.abs(self.i_s(psi_d, 0)),
+            bounds=(0, np.max(psi_s_data.real)),
+            method='bounded')
         self.psi_s0 = complex(res.x)
 
         # For the coordinate transformation
         self._mech = mech
 
     def current(self, psi_s):
         """Override the base class method."""
```

### Comparing `motulator-0.1.2/motulator/model/sm_drive.py` & `motulator-0.1.3/motulator/model/sm_drive.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,17 +1,15 @@
-# pylint: disable=invalid-name
 """
 Continuous-time models for synchronous motor drives.
 
 Peak-valued complex space vectors are used. The default values correspond to a
 2.2-kW permanent-magnet synchronous motor.
 
 """
 import numpy as np
-
 from motulator.helpers import Bunch
 
 
 # %%
 class SynchronousMotorDrive:
     """
     Continuous-time model for a synchronous motor drive.
@@ -47,15 +45,15 @@
 
     def get_initial_values(self):
         """
         Get the initial values.
 
         Returns
         -------
-        x0 : complex list, length 2
+        x0 : complex list, length 3
             Initial values of the state variables.
 
         """
         x0 = [
             self.motor.psi_s0,
             self.mech.w_M0,
             self.mech.theta_M0,
@@ -94,15 +92,15 @@
         -------
         complex list
             State derivatives.
 
         """
         # Unpack the states
         psi_s, w_M, theta_M = x
-        theta_m = self.motor.p*theta_M
+        theta_m = self.motor.n_p*theta_M
 
         # Interconnections: outputs for computing the state derivatives
         u_ss = self.conv.ac_voltage(self.conv.q, self.conv.u_dc0)
         u_s = np.exp(-1j*theta_m)*u_ss  # Stator voltage in rotor coordinates
 
         # State derivatives
         motor_f, _, tau_M = self.motor.f(psi_s, u_s, w_M)
@@ -131,22 +129,22 @@
         """Transform the lists to the ndarray format and post-process them."""
         # From lists to the ndarray
         for key in self.data:
             self.data[key] = np.asarray(self.data[key])
 
         # Compute some useful quantities
         self.data.i_s, self.data.tau_M = self.motor.magnetic(self.data.psi_s)
-        self.data.w_m = self.motor.p*self.data.w_M
+        self.data.w_m = self.motor.n_p*self.data.w_M
         self.data.tau_L = (
             self.mech.tau_L_t(self.data.t) + self.mech.tau_L_w(self.data.w_M))
         self.data.u_ss = self.conv.ac_voltage(self.data.q, self.conv.u_dc0)
         self.data.theta_M = np.mod(  # Limit into [-pi, pi)
             self.data.theta_M + np.pi, 2*np.pi) - np.pi
         self.data.theta_m = np.mod(  # Limit into [-pi, pi)
-            self.motor.p*self.data.theta_M + np.pi, 2*np.pi) - np.pi
+            self.motor.n_p*self.data.theta_M + np.pi, 2*np.pi) - np.pi
         self.data.i_ss = self.data.i_s*np.exp(1j*self.data.theta_m)
 
 
 # %%
 class SynchronousMotorDriveTwoMass(SynchronousMotorDrive):
     """
     Synchronous motor drive with two-mass mechanics.
@@ -167,29 +165,30 @@
 
     def __init__(self, motor=None, mech=None, conv=None):
         super().__init__(motor=motor, mech=mech, conv=conv)
         self.data.w_L, self.data.theta_ML = [], []
 
     def get_initial_values(self):
         """Extend the base class."""
-        x0 = super().get_initial_values() + [self.mech.w_L0,
-                                             self.mech.theta_ML0]
+        x0 = super().get_initial_values() + [
+            self.mech.w_L0, self.mech.theta_ML0
+        ]
         return x0
 
     def set_initial_values(self, t0, x0):
         """Extend the base class."""
         super().set_initial_values(t0, x0[0:3])
         self.mech.w_L0 = x0[3].real
         self.mech.theta_ML0 = np.mod(x0[4].real + np.pi, 2*np.pi) - np.pi
 
     def f(self, t, x):
         """Override the base class."""
         # Unpack the states
         psi_s, w_M, theta_M, w_L, theta_ML = x
-        theta_m = self.motor.p*theta_M
+        theta_m = self.motor.n_p*theta_M
         # Interconnections: outputs for computing the state derivatives
         u_ss = self.conv.ac_voltage(self.conv.q, self.conv.u_dc0)
         u_s = np.exp(-1j*theta_m)*u_ss  # Stator voltage in rotor coordinates
         # State derivatives plus the outputs for interconnections
         motor_f, _, tau_M = self.motor.f(psi_s, u_s, w_M)
         mech_f = self.mech.f(t, w_M, w_L, theta_ML, tau_M)
         # List of state derivatives
```

### Comparing `motulator-0.1.2/motulator/model/sm_flux_maps.py` & `motulator-0.1.3/motulator/model/sm_flux_maps.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,23 +1,22 @@
-# pylint: disable=invalid-name
 """Import and plot flux maps from the SyR-e project."""
 
 # %%
 import numpy as np
 import matplotlib.pyplot as plt
 from cycler import cycler
 from scipy.io import loadmat
 from scipy.interpolate import griddata
 from motulator.helpers import Bunch
 
 # Plotting parameters
 plt.rcParams['axes.prop_cycle'] = cycler(color='brgcmyk')
 plt.rcParams['lines.linewidth'] = 1.
 plt.rcParams['axes.grid'] = True
-plt.rcParams.update({"text.usetex": False})
+plt.rcParams.update({'text.usetex': False})
 
 
 # %%
 def import_syre_data(fname='THOR.mat', add_negative_q_axis=True):
     """
     Import a flux map from the MATLAB data file in the SyR-e format.
```

### Comparing `motulator-0.1.2/motulator/plots.py` & `motulator-0.1.3/motulator/plots.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,13 @@
-# pylint: disable=invalid-name
 """Example plotting scripts."""
 
 # %%
 import numpy as np
 import matplotlib.pyplot as plt
 from cycler import cycler
-
 from motulator.helpers import Bunch, complex2abc
 
 # Plotting parameters
 plt.rcParams['axes.prop_cycle'] = cycler(color='brgcmyk')
 plt.rcParams['lines.linewidth'] = 1.
 plt.rcParams['axes.grid'] = True
 plt.rcParams.update({"text.usetex": False})
```

### Comparing `motulator-0.1.2/motulator/simulation.py` & `motulator-0.1.3/motulator/simulation.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,12 @@
-# pylint: disable=invalid-name
 """Simulation environment."""
 
 import numpy as np
 from scipy.integrate import solve_ivp
 from scipy.io import savemat
-
 from motulator.helpers import abc2complex
 
 
 # %%
 class Delay:
     """
     Computational delay.
@@ -18,15 +16,14 @@
     Parameters
     ----------
     length : int, optional
         Length of the buffer in samples. The default is 1.
 
     """
 
-    # pylint: disable=too-few-public-methods
     def __init__(self, length=1, elem=3):
         self.data = length*[elem*[0]]  # Creates a zero list
 
     def __call__(self, u):
         """
         Delay the input.
 
@@ -100,15 +97,14 @@
     array([[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1]])
 
     """
 
-    # pylint: disable=too-few-public-methods
     def __init__(self, N=2**12, return_complex=True):
         self.N = N
         self.return_complex = return_complex
         self.rising_edge = True  # Stores the carrier direction
 
     def __call__(self, T_s, d_abc):
         """
@@ -229,15 +225,15 @@
         Other options of solve_ivp could be easily changed if needed, but, for
         simplicity, only max_step is included as an option of this method.
 
         """
         try:
             self.simulation_loop(t_stop, max_step)
         except FloatingPointError:
-            print('Invalid value encountered at %.2f seconds.' % self.mdl.t0)
+            print(f'Invalid value encountered at {self.mdl.t0:.2f} seconds.')
         # Call the post-processing functions
         self.mdl.post_process()
         self.ctrl.post_process()
 
     @np.errstate(invalid='raise')
     def simulation_loop(self, t_stop, max_step):
         """Run the main simulation loop."""
```

### Comparing `motulator-0.1.2/motulator.egg-info/PKG-INFO` & `motulator-0.1.3/motulator.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: motulator
-Version: 0.1.2
+Version: 0.1.3
 Summary: Motor Drive Simulator in Python
 Home-page: https://github.com/Aalto-Electric-Drives/motulator
 Author: Marko Hinkkanen
 Author-email: marko.hinkkanen@aalto.fi
 Project-URL: Bug Tracker, https://github.com/Aalto-Electric-Drives/motulator/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
@@ -71,26 +71,27 @@
 
 <!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
 <!-- prettier-ignore-start -->
 <!-- markdownlint-disable -->
 <table>
   <tbody>
     <tr>
-      <td align="center"><a href="https://github.com/lauritapio"><img src="https://avatars.githubusercontent.com/u/85596019?v=4?s=50" width="50px;" alt="Lauri Tiitinen"/><br /><sub><b>Lauri Tiitinen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=lauritapio" title="Code">💻</a> <a href="#ideas-lauritapio" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-lauritapio" title="Examples">💡</a> <a href="#mentoring-lauritapio" title="Mentoring">🧑‍🏫</a></td>
-      <td align="center"><a href="https://github.com/HannuHar"><img src="https://avatars.githubusercontent.com/u/96597650?v=4?s=50" width="50px;" alt="HannuHar"/><br /><sub><b>HannuHar</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=HannuHar" title="Code">💻</a> <a href="https://github.com/Aalto-Electric-Drives/motulator/issues?q=author%3AHannuHar" title="Bug reports">🐛</a></td>
-      <td align="center"><a href="https://research.aalto.fi/en/persons/marko-hinkkanen"><img src="https://avatars.githubusercontent.com/u/76600872?v=4?s=50" width="50px;" alt="Marko Hinkkanen"/><br /><sub><b>Marko Hinkkanen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=mhinkkan" title="Code">💻</a> <a href="#ideas-mhinkkan" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-mhinkkan" title="Examples">💡</a></td>
-      <td align="center"><a href="https://github.com/silundbe"><img src="https://avatars.githubusercontent.com/u/81169347?v=4?s=50" width="50px;" alt="silundbe"/><br /><sub><b>silundbe</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=silundbe" title="Code">💻</a> <a href="#example-silundbe" title="Examples">💡</a></td>
-      <td align="center"><a href="https://github.com/JoonaKukkonen"><img src="https://avatars.githubusercontent.com/u/85099403?v=4?s=50" width="50px;" alt="JoonaKukkonen"/><br /><sub><b>JoonaKukkonen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=JoonaKukkonen" title="Code">💻</a> <a href="#infra-JoonaKukkonen" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
-      <td align="center"><a href="https://github.com/jarno-k"><img src="https://avatars.githubusercontent.com/u/84438313?v=4?s=50" width="50px;" alt="jarno-k"/><br /><sub><b>jarno-k</b></sub></a><br /><a href="#ideas-jarno-k" title="Ideas, Planning, & Feedback">🤔</a></td>
-      <td align="center"><a href="https://github.com/angelicaiaderosa"><img src="https://avatars.githubusercontent.com/u/112799415?v=4?s=50" width="50px;" alt="angelicaiaderosa"/><br /><sub><b>angelicaiaderosa</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=angelicaiaderosa" title="Code">💻</a> <a href="#example-angelicaiaderosa" title="Examples">💡</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lauritapio"><img src="https://avatars.githubusercontent.com/u/85596019?v=4?s=50" width="50px;" alt="Lauri Tiitinen"/><br /><sub><b>Lauri Tiitinen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=lauritapio" title="Code">💻</a> <a href="#ideas-lauritapio" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-lauritapio" title="Examples">💡</a> <a href="#mentoring-lauritapio" title="Mentoring">🧑‍🏫</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/HannuHar"><img src="https://avatars.githubusercontent.com/u/96597650?v=4?s=50" width="50px;" alt="HannuHar"/><br /><sub><b>HannuHar</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=HannuHar" title="Code">💻</a> <a href="https://github.com/Aalto-Electric-Drives/motulator/issues?q=author%3AHannuHar" title="Bug reports">🐛</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://research.aalto.fi/en/persons/marko-hinkkanen"><img src="https://avatars.githubusercontent.com/u/76600872?v=4?s=50" width="50px;" alt="Marko Hinkkanen"/><br /><sub><b>Marko Hinkkanen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=mhinkkan" title="Code">💻</a> <a href="#ideas-mhinkkan" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-mhinkkan" title="Examples">💡</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/silundbe"><img src="https://avatars.githubusercontent.com/u/81169347?v=4?s=50" width="50px;" alt="silundbe"/><br /><sub><b>silundbe</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=silundbe" title="Code">💻</a> <a href="#example-silundbe" title="Examples">💡</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/JoonaKukkonen"><img src="https://avatars.githubusercontent.com/u/85099403?v=4?s=50" width="50px;" alt="JoonaKukkonen"/><br /><sub><b>JoonaKukkonen</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=JoonaKukkonen" title="Code">💻</a> <a href="#infra-JoonaKukkonen" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jarno-k"><img src="https://avatars.githubusercontent.com/u/84438313?v=4?s=50" width="50px;" alt="jarno-k"/><br /><sub><b>jarno-k</b></sub></a><br /><a href="#ideas-jarno-k" title="Ideas, Planning, & Feedback">🤔</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/angelicaiaderosa"><img src="https://avatars.githubusercontent.com/u/112799415?v=4?s=50" width="50px;" alt="angelicaiaderosa"/><br /><sub><b>angelicaiaderosa</b></sub></a><br /><a href="https://github.com/Aalto-Electric-Drives/motulator/commits?author=angelicaiaderosa" title="Code">💻</a> <a href="#example-angelicaiaderosa" title="Examples">💡</a></td>
     </tr>
     <tr>
-      <td align="center"><a href="https://www.kth.se/profile/lucap"><img src="https://avatars.githubusercontent.com/u/64190518?v=4?s=50" width="50px;" alt="Luca Peretti"/><br /><sub><b>Luca Peretti</b></sub></a><br /><a href="#ideas-lucaperetti" title="Ideas, Planning, & Feedback">🤔</a> <a href="#promotion-lucaperetti" title="Promotion">📣</a></td>
-      <td align="center"><a href="https://github.com/GianmarioPellegrinoPolito"><img src="https://avatars.githubusercontent.com/u/70333484?v=4?s=50" width="50px;" alt="GianmarioPellegrinoPolito"/><br /><sub><b>GianmarioPellegrinoPolito</b></sub></a><br /><a href="#data-GianmarioPellegrinoPolito" title="Data">🔣</a></td>
-      <td align="center"><a href="https://github.com/SimFerr"><img src="https://avatars.githubusercontent.com/u/67151973?v=4?s=50" width="50px;" alt="Simone Ferrari"/><br /><sub><b>Simone Ferrari</b></sub></a><br /><a href="#data-SimFerr" title="Data">🔣</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://www.kth.se/profile/lucap"><img src="https://avatars.githubusercontent.com/u/64190518?v=4?s=50" width="50px;" alt="Luca Peretti"/><br /><sub><b>Luca Peretti</b></sub></a><br /><a href="#ideas-lucaperetti" title="Ideas, Planning, & Feedback">🤔</a> <a href="#promotion-lucaperetti" title="Promotion">📣</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/GianmarioPellegrinoPolito"><img src="https://avatars.githubusercontent.com/u/70333484?v=4?s=50" width="50px;" alt="GianmarioPellegrinoPolito"/><br /><sub><b>GianmarioPellegrinoPolito</b></sub></a><br /><a href="#data-GianmarioPellegrinoPolito" title="Data">🔣</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/SimFerr"><img src="https://avatars.githubusercontent.com/u/67151973?v=4?s=50" width="50px;" alt="Simone Ferrari"/><br /><sub><b>Simone Ferrari</b></sub></a><br /><a href="#data-SimFerr" title="Data">🔣</a></td>
+      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Jialed0303"><img src="https://avatars.githubusercontent.com/u/118135952?v=4?s=50" width="50px;" alt="Jialed0303"/><br /><sub><b>Jialed0303</b></sub></a><br /><a href="#ideas-Jialed0303" title="Ideas, Planning, & Feedback">🤔</a></td>
     </tr>
   </tbody>
 </table>
 
 <!-- markdownlint-restore -->
 <!-- prettier-ignore-end -->
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: motulator Version: 0.1.2 Summary: Motor Drive
+Metadata-Version: 2.1 Name: motulator Version: 0.1.3 Summary: Motor Drive
 Simulator in Python Home-page: https://github.com/Aalto-Electric-Drives/
 motulator Author: Marko Hinkkanen Author-email: marko.hinkkanen@aalto.fi
 Project-URL: Bug Tracker, https://github.com/Aalto-Electric-Drives/motulator/
 issues Classifier: Programming Language :: Python :: 3 Classifier: License ::
 OSI Approved :: MIT License Classifier: Operating System :: OS Independent
 Requires-Python: >=3.6 Description-Content-Type: text/markdown License-File:
 LICENSE # *motulator:* Motor Drive Simulator in Python [![Build Status](https:/
@@ -40,17 +40,17 @@
 have a look at these [guidelines](https://github.com/Aalto-Electric-Drives/
 motulator/blob/main/CONTRIBUTING.md) first. Contributors ------------ Thanks go
 to these wonderful people:
                 [Lauri_Tiitinen]                          [HannuHar]              [Marko_Hinkkanen]         [silundbe]      [JoonaKukkonen]  [jarno-  [angelicaiaderosa]
                  Lauri_Tiitinen                            HannuHar                Marko_Hinkkanen           silundbe        JoonaKukkonen      k]     angelicaiaderosa
            ð» ð¤ ð¡ ð§â         ð» ð        ð» ð¤ ð�    ð» ð�    ð» ð�jarno-k      ð» ð¡
                                                                                                                                                ð¤
-                       [Luca_Peretti]             [GianmarioPellegrinoPolito]        [Simone_Ferrari]
-                        Luca_Peretti               GianmarioPellegrinoPolito          Simone_Ferrari
-                          ð¤ ð£                  ð£                      ð£
+                       [Luca_Peretti]             [GianmarioPellegrinoPolito]        [Simone_Ferrari]       [Jialed0303]
+                        Luca_Peretti               GianmarioPellegrinoPolito          Simone_Ferrari         Jialed0303
+                          ð¤ ð£                  ð£                      ð£             ð¤
    This project follows the [all-contributors](https://github.com/all-
 contributors/all-contributors) specification. Contributions of any kind
 welcome! Acknowledgement --------------- This project has been sponsored by ABB
 Oy and by the Academy of Finland *Centre of Excellence in High-Speed
 Electromechanical Energy Conversion Systems*. The example control methods
 included in this repository are based on published algorithms (available in
 textbooks and scientific articles). They do not present any proprietary control
```

### Comparing `motulator-0.1.2/motulator.egg-info/SOURCES.txt` & `motulator-0.1.3/motulator.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `motulator-0.1.2/setup.cfg` & `motulator-0.1.3/setup.cfg`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = motulator
-version = 0.1.2
+version = 0.1.3
 author = Marko Hinkkanen
 author_email = marko.hinkkanen@aalto.fi
 description = Motor Drive Simulator in Python
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/Aalto-Electric-Drives/motulator
 project_urls =
```

