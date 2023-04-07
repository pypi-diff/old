# Comparing `tmp/robot-soccer-kit-2.0.0.tar.gz` & `tmp/robot-soccer-kit-2.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "robot-soccer-kit-2.0.0.tar", last modified: Fri Apr  7 11:09:46 2023, max compression
+gzip compressed data, was "robot-soccer-kit-2.0.1.tar", last modified: Fri Apr  7 11:54:43 2023, max compression
```

## Comparing `robot-soccer-kit-2.0.0.tar` & `robot-soccer-kit-2.0.1.tar`

### file list

```diff
@@ -1,162 +1,162 @@
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.604168 robot-soccer-kit-2.0.0/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      262 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/LICENSE
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1157 2023-04-07 11:09:46.604168 robot-soccer-kit-2.0.0/PKG-INFO
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      588 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/README.md
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.580168 robot-soccer-kit-2.0.0/robot_soccer_kit.egg-info/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1157 2023-04-07 11:09:46.000000 robot-soccer-kit-2.0.0/robot_soccer_kit.egg-info/PKG-INFO
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     4847 2023-04-07 11:09:46.000000 robot-soccer-kit-2.0.0/robot_soccer_kit.egg-info/SOURCES.txt
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)        1 2023-04-07 11:09:46.000000 robot-soccer-kit-2.0.0/robot_soccer_kit.egg-info/dependency_links.txt
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       86 2023-04-07 11:09:46.000000 robot-soccer-kit-2.0.0/robot_soccer_kit.egg-info/requires.txt
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)        4 2023-04-07 11:09:46.000000 robot-soccer-kit-2.0.0/robot_soccer_kit.egg-info/top_level.txt
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.580168 robot-soccer-kit-2.0.0/rsk/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      102 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/__init__.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      571 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/api.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     5422 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/backend.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    10948 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/client.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      277 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/config.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     3225 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/constants.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    13513 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/control.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       35 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/debug.sh
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    17821 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/detection.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1058 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/dumb_ia.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      571 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/dump_referee.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       73 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/em.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    10173 2022-11-27 19:47:15.000000 robot-soccer-kit-2.0.0/rsk/field.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2379 2023-04-07 11:09:06.000000 robot-soccer-kit-2.0.0/rsk/game_controller.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2462 2023-04-07 11:09:06.000000 robot-soccer-kit-2.0.0/rsk/kinematics.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      445 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/logger.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      602 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/place.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    23541 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/referee.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2362 2023-04-07 11:09:06.000000 robot-soccer-kit-2.0.0/rsk/robot.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    11752 2023-04-07 11:09:07.000000 robot-soccer-kit-2.0.0/rsk/robot_serial.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     6030 2023-04-07 11:09:06.000000 robot-soccer-kit-2.0.0/rsk/robots.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    10228 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/simulator.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2317 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/state.py
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.580168 robot-soccer-kit-2.0.0/rsk/static/
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.580168 robot-soccer-kit-2.0.0/rsk/static/bootstrap/
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.588168 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    75616 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   226018 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    56464 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.min.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   142342 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.min.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    75690 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.rtl.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   226022 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.rtl.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    56539 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.rtl.min.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   142419 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.rtl.min.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    11735 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   126626 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     9817 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.min.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    51406 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.min.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    11728 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.rtl.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   126641 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.rtl.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     9889 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.rtl.min.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    63643 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.rtl.min.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    96254 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   250681 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    74887 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.min.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   163881 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.min.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    96121 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.rtl.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   250622 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.rtl.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    74815 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.rtl.min.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   163716 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.rtl.min.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   267476 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   658460 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   220780 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.min.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   568408 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.min.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   267055 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.rtl.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   658305 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.rtl.css.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   220887 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.rtl.min.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   567947 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.rtl.min.css.map
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.588168 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   208288 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.bundle.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   448884 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.bundle.js.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    80599 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.bundle.min.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   333974 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.bundle.min.js.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   136243 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.esm.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   305274 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.esm.js.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    74135 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.esm.min.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   222070 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.esm.min.js.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   145819 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   306458 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.js.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    60554 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.min.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   217885 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.min.js.map
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      215 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/camera-setting.html
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.588168 robot-soccer-kit-2.0.0/rsk/static/css/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2566 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/css/app.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1150 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/favicon.ico
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.596168 robot-soccer-kit-2.0.0/rsk/static/icons/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      376 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.browserslistrc
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      167 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.editorconfig
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       40 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.eslintignore
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      375 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.eslintrc.json
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      922 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.fantasticonrc.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       43 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.gitattributes
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.596168 robot-soccer-kit-2.0.0/rsk/static/icons/.github/
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.596168 robot-soccer-kit-2.0.0/rsk/static/icons/.github/ISSUE_TEMPLATE/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      583 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.github/ISSUE_TEMPLATE/bug_report.md
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      122 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.github/ISSUE_TEMPLATE/icon-request.md
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      433 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.github/dependabot.yml
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   248086 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.github/preview.png
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      572 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.github/release-drafter.yml
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.596168 robot-soccer-kit-2.0.0/rsk/static/icons/.github/workflows/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      662 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.github/workflows/codeql.yml
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1190 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.github/workflows/deploy.yml
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      243 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.github/workflows/release-notes.yml
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      575 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.github/workflows/test.yml
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       63 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.gitignore
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      125 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/.stylelintrc
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1093 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/LICENSE.md
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     3312 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/README.md
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   881772 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/bootstrap-icons.svg
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      425 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/composer.json
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2052 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/config.yml
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.596168 robot-soccer-kit-2.0.0/rsk/static/icons/font/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    80510 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/font/bootstrap-icons.css
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    42897 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/font/bootstrap-icons.json
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.600168 robot-soccer-kit-2.0.0/rsk/static/icons/font/fonts/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   137124 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/font/fonts/bootstrap-icons.woff
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   102536 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/font/fonts/bootstrap-icons.woff2
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   200995 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/font/index.html
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   643115 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/package-lock.json
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     3152 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/package.json
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     3085 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/svg-sprite.json
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      654 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/icons/svgo.config.js
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.604168 robot-soccer-kit-2.0.0/rsk/static/imgs/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     3287 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/ball.png
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1251 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/ball_16x16.png
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1856 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/ball_24x24.png
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    43069 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/ball_256x256.png
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2654 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/ball_32x32.png
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     4470 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/ball_48x48.png
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    19402 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/field.png
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    17815 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/field.svg
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   249649 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/robot.svg
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   507520 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/robotblue1.svg
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   524385 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/robotblue2.svg
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   498488 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/robotgreen1.svg
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   522425 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/imgs/robotgreen2.svg
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    26782 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/index.html
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.604168 robot-soccer-kit-2.0.0/rsk/static/jquery/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   288580 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/jquery/jquery.js
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.604168 robot-soccer-kit-2.0.0/rsk/static/js/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1614 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/js/app.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1567 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/js/control.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    24620 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/js/referee.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     6005 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/js/robots.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      426 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/js/tabs.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      329 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/js/utils.js
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     6015 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/js/video.js
-drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:09:46.604168 robot-soccer-kit-2.0.0/rsk/static/markers/
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     6021 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/markers/blue1.svg
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     6023 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/markers/blue2.svg
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     6009 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/markers/green1.svg
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     5098 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/markers/green2.svg
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      337 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/referee_event_neutral.html
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      632 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/referee_event_team.html
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1029 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/static/robot.html
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      569 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.0/rsk/static/team.html
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     3865 2022-11-27 19:47:15.000000 robot-soccer-kit-2.0.0/rsk/tasks.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     4154 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/utils.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     9469 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.0/rsk/video.py
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       38 2023-04-07 11:09:46.604168 robot-soccer-kit-2.0.0/setup.cfg
--rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1395 2023-04-07 11:09:35.000000 robot-soccer-kit-2.0.0/setup.py
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.256201 robot-soccer-kit-2.0.1/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      262 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/LICENSE
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1157 2023-04-07 11:54:43.256201 robot-soccer-kit-2.0.1/PKG-INFO
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      588 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/README.md
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.240201 robot-soccer-kit-2.0.1/robot_soccer_kit.egg-info/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1157 2023-04-07 11:54:43.000000 robot-soccer-kit-2.0.1/robot_soccer_kit.egg-info/PKG-INFO
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     4847 2023-04-07 11:54:43.000000 robot-soccer-kit-2.0.1/robot_soccer_kit.egg-info/SOURCES.txt
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)        1 2023-04-07 11:54:43.000000 robot-soccer-kit-2.0.1/robot_soccer_kit.egg-info/dependency_links.txt
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       86 2023-04-07 11:54:43.000000 robot-soccer-kit-2.0.1/robot_soccer_kit.egg-info/requires.txt
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)        4 2023-04-07 11:54:43.000000 robot-soccer-kit-2.0.1/robot_soccer_kit.egg-info/top_level.txt
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.244201 robot-soccer-kit-2.0.1/rsk/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      102 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/__init__.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      571 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/api.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     5422 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/backend.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    10948 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/client.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      277 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/config.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     3225 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/constants.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    13513 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/control.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       35 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/debug.sh
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    17821 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/detection.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1058 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/dumb_ia.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      571 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/dump_referee.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       73 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/em.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    10173 2022-11-27 19:47:15.000000 robot-soccer-kit-2.0.1/rsk/field.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2379 2023-04-07 11:09:06.000000 robot-soccer-kit-2.0.1/rsk/game_controller.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2462 2023-04-07 11:09:06.000000 robot-soccer-kit-2.0.1/rsk/kinematics.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      445 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/logger.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      602 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/place.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    23541 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/referee.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2362 2023-04-07 11:09:06.000000 robot-soccer-kit-2.0.1/rsk/robot.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    11752 2023-04-07 11:09:07.000000 robot-soccer-kit-2.0.1/rsk/robot_serial.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     6030 2023-04-07 11:09:06.000000 robot-soccer-kit-2.0.1/rsk/robots.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    10231 2023-04-07 11:17:58.000000 robot-soccer-kit-2.0.1/rsk/simulator.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2317 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/state.py
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.244201 robot-soccer-kit-2.0.1/rsk/static/
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.240201 robot-soccer-kit-2.0.1/rsk/static/bootstrap/
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.248201 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    75616 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   226018 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    56464 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.min.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   142342 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.min.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    75690 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.rtl.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   226022 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.rtl.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    56539 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.rtl.min.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   142419 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.rtl.min.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    11735 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   126626 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     9817 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.min.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    51406 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.min.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    11728 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.rtl.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   126641 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.rtl.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     9889 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.rtl.min.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    63643 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.rtl.min.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    96254 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   250681 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    74887 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.min.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   163881 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.min.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    96121 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.rtl.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   250622 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.rtl.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    74815 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.rtl.min.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   163716 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.rtl.min.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   267476 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   658460 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   220780 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.min.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   568408 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.min.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   267055 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.rtl.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   658305 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.rtl.css.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   220887 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.rtl.min.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   567947 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.rtl.min.css.map
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.252201 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   208288 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.bundle.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   448884 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.bundle.js.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    80599 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.bundle.min.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   333974 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.bundle.min.js.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   136243 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.esm.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   305274 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.esm.js.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    74135 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.esm.min.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   222070 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.esm.min.js.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   145819 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   306458 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.js.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    60554 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.min.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   217885 2023-04-07 08:27:16.000000 robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.min.js.map
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      215 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/camera-setting.html
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.252201 robot-soccer-kit-2.0.1/rsk/static/css/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2566 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/css/app.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1150 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/favicon.ico
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.252201 robot-soccer-kit-2.0.1/rsk/static/icons/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      376 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.browserslistrc
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      167 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.editorconfig
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       40 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.eslintignore
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      375 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.eslintrc.json
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      922 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.fantasticonrc.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       43 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.gitattributes
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.252201 robot-soccer-kit-2.0.1/rsk/static/icons/.github/
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.252201 robot-soccer-kit-2.0.1/rsk/static/icons/.github/ISSUE_TEMPLATE/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      583 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.github/ISSUE_TEMPLATE/bug_report.md
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      122 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.github/ISSUE_TEMPLATE/icon-request.md
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      433 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.github/dependabot.yml
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   248086 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.github/preview.png
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      572 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.github/release-drafter.yml
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.252201 robot-soccer-kit-2.0.1/rsk/static/icons/.github/workflows/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      662 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.github/workflows/codeql.yml
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1190 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.github/workflows/deploy.yml
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      243 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.github/workflows/release-notes.yml
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      575 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.github/workflows/test.yml
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       63 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.gitignore
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      125 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/.stylelintrc
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1093 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/LICENSE.md
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     3312 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/README.md
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   881772 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/bootstrap-icons.svg
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      425 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/composer.json
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2052 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/config.yml
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.252201 robot-soccer-kit-2.0.1/rsk/static/icons/font/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    80510 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/font/bootstrap-icons.css
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    42897 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/font/bootstrap-icons.json
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.252201 robot-soccer-kit-2.0.1/rsk/static/icons/font/fonts/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   137124 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/font/fonts/bootstrap-icons.woff
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   102536 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/font/fonts/bootstrap-icons.woff2
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   200995 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/font/index.html
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   643115 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/package-lock.json
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     3152 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/package.json
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     3085 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/svg-sprite.json
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      654 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/icons/svgo.config.js
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.256201 robot-soccer-kit-2.0.1/rsk/static/imgs/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     3287 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/ball.png
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1251 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/ball_16x16.png
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1856 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/ball_24x24.png
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    43069 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/ball_256x256.png
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     2654 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/ball_32x32.png
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     4470 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/ball_48x48.png
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    19402 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/field.png
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    17815 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/field.svg
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   249649 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/robot.svg
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   507520 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/robotblue1.svg
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   524385 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/robotblue2.svg
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   498488 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/robotgreen1.svg
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   522425 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/imgs/robotgreen2.svg
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    26782 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/index.html
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.256201 robot-soccer-kit-2.0.1/rsk/static/jquery/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)   288580 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/jquery/jquery.js
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.256201 robot-soccer-kit-2.0.1/rsk/static/js/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1614 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/js/app.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1567 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/js/control.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)    24620 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/js/referee.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     6005 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/js/robots.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      426 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/js/tabs.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      329 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/js/utils.js
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     6015 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/js/video.js
+drwxrwxr-x   0 gregwar   (1000) gregwar   (1000)        0 2023-04-07 11:54:43.256201 robot-soccer-kit-2.0.1/rsk/static/markers/
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     6021 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/markers/blue1.svg
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     6023 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/markers/blue2.svg
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     6009 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/markers/green1.svg
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     5098 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/markers/green2.svg
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      337 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/referee_event_neutral.html
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      632 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/referee_event_team.html
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1029 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/static/robot.html
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)      569 2022-09-27 10:59:02.000000 robot-soccer-kit-2.0.1/rsk/static/team.html
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     3865 2022-11-27 19:47:15.000000 robot-soccer-kit-2.0.1/rsk/tasks.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     4154 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/utils.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     9469 2023-04-07 11:08:46.000000 robot-soccer-kit-2.0.1/rsk/video.py
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)       38 2023-04-07 11:54:43.256201 robot-soccer-kit-2.0.1/setup.cfg
+-rw-rw-r--   0 gregwar   (1000) gregwar   (1000)     1395 2023-04-07 11:54:31.000000 robot-soccer-kit-2.0.1/setup.py
```

### Comparing `robot-soccer-kit-2.0.0/PKG-INFO` & `robot-soccer-kit-2.0.1/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: robot-soccer-kit
-Version: 2.0.0
+Version: 2.0.1
 Summary: Robot Soccer Kit
 Home-page: https://github.com/rhoban/robot-soccer-kit/
 Author: Rhoban team
 Author-email: team@rhoban.com
 License: UNKNOWN
 Keywords: robot holonomic omniwheel ssl robocup junior soccer standard localized tracking
 Platform: UNKNOWN
```

### Comparing `robot-soccer-kit-2.0.0/README.md` & `robot-soccer-kit-2.0.1/README.md`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/robot_soccer_kit.egg-info/PKG-INFO` & `robot-soccer-kit-2.0.1/robot_soccer_kit.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: robot-soccer-kit
-Version: 2.0.0
+Version: 2.0.1
 Summary: Robot Soccer Kit
 Home-page: https://github.com/rhoban/robot-soccer-kit/
 Author: Rhoban team
 Author-email: team@rhoban.com
 License: UNKNOWN
 Keywords: robot holonomic omniwheel ssl robocup junior soccer standard localized tracking
 Platform: UNKNOWN
```

### Comparing `robot-soccer-kit-2.0.0/robot_soccer_kit.egg-info/SOURCES.txt` & `robot-soccer-kit-2.0.1/robot_soccer_kit.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/api.py` & `robot-soccer-kit-2.0.1/rsk/api.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/backend.py` & `robot-soccer-kit-2.0.1/rsk/backend.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/client.py` & `robot-soccer-kit-2.0.1/rsk/client.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/constants.py` & `robot-soccer-kit-2.0.1/rsk/constants.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/control.py` & `robot-soccer-kit-2.0.1/rsk/control.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/detection.py` & `robot-soccer-kit-2.0.1/rsk/detection.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/dumb_ia.py` & `robot-soccer-kit-2.0.1/rsk/dumb_ia.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/dump_referee.py` & `robot-soccer-kit-2.0.1/rsk/dump_referee.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/field.py` & `robot-soccer-kit-2.0.1/rsk/field.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/game_controller.py` & `robot-soccer-kit-2.0.1/rsk/game_controller.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/kinematics.py` & `robot-soccer-kit-2.0.1/rsk/kinematics.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/place.py` & `robot-soccer-kit-2.0.1/rsk/place.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/referee.py` & `robot-soccer-kit-2.0.1/rsk/referee.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/robot.py` & `robot-soccer-kit-2.0.1/rsk/robot.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/robot_serial.py` & `robot-soccer-kit-2.0.1/rsk/robot_serial.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/robots.py` & `robot-soccer-kit-2.0.1/rsk/robots.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/simulator.py` & `robot-soccer-kit-2.0.1/rsk/simulator.py`

 * *Files 1% similar despite different names*

```diff
@@ -197,15 +197,15 @@
     def thread(self) -> None:
         last_time = time.time()
         while self.run:
             self.dt = -last_time + (last_time := time.time())
             self.loop(self.dt)
 
             while (self.fps_limit is not None) and (time.time() - last_time < 1 / self.fps_limit):
-                time.sleep(0)
+                time.sleep(1e-3)
 
     def loop(self, dt):
         # Simulator proceed in two steps:
         # 1) We handle future collisions as elastic collisions and change the velocity vectors
         #    accordingly.
         # 2) We apply the object velocities, removing all the components in the velocities that would
         #    create collision.
```

### Comparing `robot-soccer-kit-2.0.0/rsk/state.py` & `robot-soccer-kit-2.0.1/rsk/state.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.min.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.min.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.min.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.min.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.rtl.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.rtl.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.rtl.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.rtl.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.rtl.min.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.rtl.min.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-grid.rtl.min.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-grid.rtl.min.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.min.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.min.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.min.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.min.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.rtl.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.rtl.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.rtl.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.rtl.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.rtl.min.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.rtl.min.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-reboot.rtl.min.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-reboot.rtl.min.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.min.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.min.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.min.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.min.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.rtl.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.rtl.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.rtl.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.rtl.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.rtl.min.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.rtl.min.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap-utilities.rtl.min.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap-utilities.rtl.min.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.min.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.min.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.min.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.min.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.rtl.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.rtl.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.rtl.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.rtl.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.rtl.min.css` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.rtl.min.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/css/bootstrap.rtl.min.css.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/css/bootstrap.rtl.min.css.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.bundle.js` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.bundle.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.bundle.js.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.bundle.js.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.bundle.min.js` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.bundle.min.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.bundle.min.js.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.bundle.min.js.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.esm.js` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.esm.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.esm.js.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.esm.js.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.esm.min.js` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.esm.min.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.esm.min.js.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.esm.min.js.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.js` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.js.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.js.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.min.js` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.min.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/bootstrap/js/bootstrap.min.js.map` & `robot-soccer-kit-2.0.1/rsk/static/bootstrap/js/bootstrap.min.js.map`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/css/app.css` & `robot-soccer-kit-2.0.1/rsk/static/css/app.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/favicon.ico` & `robot-soccer-kit-2.0.1/rsk/static/favicon.ico`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/.fantasticonrc.js` & `robot-soccer-kit-2.0.1/rsk/static/icons/.fantasticonrc.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/.github/ISSUE_TEMPLATE/bug_report.md` & `robot-soccer-kit-2.0.1/rsk/static/icons/.github/ISSUE_TEMPLATE/bug_report.md`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/.github/preview.png` & `robot-soccer-kit-2.0.1/rsk/static/icons/.github/preview.png`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/.github/release-drafter.yml` & `robot-soccer-kit-2.0.1/rsk/static/icons/.github/release-drafter.yml`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/.github/workflows/codeql.yml` & `robot-soccer-kit-2.0.1/rsk/static/icons/.github/workflows/codeql.yml`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/.github/workflows/deploy.yml` & `robot-soccer-kit-2.0.1/rsk/static/icons/.github/workflows/deploy.yml`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/.github/workflows/test.yml` & `robot-soccer-kit-2.0.1/rsk/static/icons/.github/workflows/test.yml`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/LICENSE.md` & `robot-soccer-kit-2.0.1/rsk/static/icons/LICENSE.md`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/README.md` & `robot-soccer-kit-2.0.1/rsk/static/icons/README.md`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/bootstrap-icons.svg` & `robot-soccer-kit-2.0.1/rsk/static/icons/bootstrap-icons.svg`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/config.yml` & `robot-soccer-kit-2.0.1/rsk/static/icons/config.yml`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/font/bootstrap-icons.css` & `robot-soccer-kit-2.0.1/rsk/static/icons/font/bootstrap-icons.css`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/font/bootstrap-icons.json` & `robot-soccer-kit-2.0.1/rsk/static/icons/font/bootstrap-icons.json`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/font/fonts/bootstrap-icons.woff` & `robot-soccer-kit-2.0.1/rsk/static/icons/font/fonts/bootstrap-icons.woff`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/font/fonts/bootstrap-icons.woff2` & `robot-soccer-kit-2.0.1/rsk/static/icons/font/fonts/bootstrap-icons.woff2`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/font/index.html` & `robot-soccer-kit-2.0.1/rsk/static/icons/font/index.html`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/package-lock.json` & `robot-soccer-kit-2.0.1/rsk/static/icons/package-lock.json`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/package.json` & `robot-soccer-kit-2.0.1/rsk/static/icons/package.json`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/svg-sprite.json` & `robot-soccer-kit-2.0.1/rsk/static/icons/svg-sprite.json`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/icons/svgo.config.js` & `robot-soccer-kit-2.0.1/rsk/static/icons/svgo.config.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/ball.png` & `robot-soccer-kit-2.0.1/rsk/static/imgs/ball.png`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/ball_16x16.png` & `robot-soccer-kit-2.0.1/rsk/static/imgs/ball_16x16.png`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/ball_24x24.png` & `robot-soccer-kit-2.0.1/rsk/static/imgs/ball_24x24.png`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/ball_256x256.png` & `robot-soccer-kit-2.0.1/rsk/static/imgs/ball_256x256.png`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/ball_32x32.png` & `robot-soccer-kit-2.0.1/rsk/static/imgs/ball_32x32.png`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/ball_48x48.png` & `robot-soccer-kit-2.0.1/rsk/static/imgs/ball_48x48.png`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/field.png` & `robot-soccer-kit-2.0.1/rsk/static/imgs/field.png`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/field.svg` & `robot-soccer-kit-2.0.1/rsk/static/imgs/field.svg`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/robot.svg` & `robot-soccer-kit-2.0.1/rsk/static/imgs/robot.svg`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/robotblue1.svg` & `robot-soccer-kit-2.0.1/rsk/static/imgs/robotblue1.svg`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/robotblue2.svg` & `robot-soccer-kit-2.0.1/rsk/static/imgs/robotblue2.svg`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/robotgreen1.svg` & `robot-soccer-kit-2.0.1/rsk/static/imgs/robotgreen1.svg`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/imgs/robotgreen2.svg` & `robot-soccer-kit-2.0.1/rsk/static/imgs/robotgreen2.svg`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/index.html` & `robot-soccer-kit-2.0.1/rsk/static/index.html`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/jquery/jquery.js` & `robot-soccer-kit-2.0.1/rsk/static/jquery/jquery.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/js/app.js` & `robot-soccer-kit-2.0.1/rsk/static/js/app.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/js/control.js` & `robot-soccer-kit-2.0.1/rsk/static/js/control.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/js/referee.js` & `robot-soccer-kit-2.0.1/rsk/static/js/referee.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/js/robots.js` & `robot-soccer-kit-2.0.1/rsk/static/js/robots.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/js/video.js` & `robot-soccer-kit-2.0.1/rsk/static/js/video.js`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/markers/blue1.svg` & `robot-soccer-kit-2.0.1/rsk/static/markers/blue1.svg`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/markers/blue2.svg` & `robot-soccer-kit-2.0.1/rsk/static/markers/blue2.svg`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/markers/green1.svg` & `robot-soccer-kit-2.0.1/rsk/static/markers/green1.svg`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/markers/green2.svg` & `robot-soccer-kit-2.0.1/rsk/static/markers/green2.svg`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/referee_event_team.html` & `robot-soccer-kit-2.0.1/rsk/static/referee_event_team.html`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/robot.html` & `robot-soccer-kit-2.0.1/rsk/static/robot.html`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/static/team.html` & `robot-soccer-kit-2.0.1/rsk/static/team.html`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/tasks.py` & `robot-soccer-kit-2.0.1/rsk/tasks.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/utils.py` & `robot-soccer-kit-2.0.1/rsk/utils.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/rsk/video.py` & `robot-soccer-kit-2.0.1/rsk/video.py`

 * *Files identical despite different names*

### Comparing `robot-soccer-kit-2.0.0/setup.py` & `robot-soccer-kit-2.0.1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -10,15 +10,15 @@
         for filename in filenames:
             if '__pycache__' not in path:
                 paths.append(os.path.join('..', path, filename))
     return paths
 
 setuptools.setup(
     name="robot-soccer-kit",
-    version="2.0.0",
+    version="2.0.1",
     author="Rhoban team",
     author_email="team@rhoban.com",
     description="Robot Soccer Kit",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/rhoban/robot-soccer-kit/",
     packages=setuptools.find_packages(),
```

