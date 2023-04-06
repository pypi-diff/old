# Comparing `tmp/hopla-cli-0.0.32a0.tar.gz` & `tmp/hopla-cli-0.0.33a0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "hopla-cli-0.0.32a0.tar", last modified: Tue Feb 14 16:25:02 2023, max compression
+gzip compressed data, was "hopla-cli-0.0.33a0.tar", last modified: Thu Apr  6 19:21:21 2023, max compression
```

## Comparing `hopla-cli-0.0.32a0.tar` & `hopla-cli-0.0.33a0.tar`

### file list

```diff
@@ -1,164 +1,164 @@
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/
--rw-------   0 m         (1000) m         (1000)     7118 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/PKG-INFO
--rw-------   0 m         (1000) m         (1000)     5804 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/README.md
--rw-------   0 m         (1000) m         (1000)      272 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/pyproject.toml
--rw-------   0 m         (1000) m         (1000)     1508 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/setup.cfg
--rw-------   0 m         (1000) m         (1000)      352 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/setup.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.778755 hopla-cli-0.0.32a0/src/
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.778755 hopla-cli-0.0.32a0/src/hopla/
--rwx------   0 m         (1000) m         (1000)      880 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/__init__.py
--rwx------   0 m         (1000) m         (1000)      267 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/__main__.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.778755 hopla-cli-0.0.32a0/src/hopla/cli/
--rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/cli/__init__.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.778755 hopla-cli-0.0.32a0/src/hopla/cli/add/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/cli/add/__init__.py
--rw-------   0 m         (1000) m         (1000)     6904 2021-10-04 19:13:15.000000 hopla-cli-0.0.32a0/src/hopla/cli/add/todo.py
--rw-------   0 m         (1000) m         (1000)     1652 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/cli/authenticate.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.778755 hopla-cli-0.0.32a0/src/hopla/cli/buy/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/cli/buy/__init__.py
--rw-------   0 m         (1000) m         (1000)     4576 2021-10-10 18:40:43.000000 hopla-cli-0.0.32a0/src/hopla/cli/buy/enchanted_armoire.py
--rw-------   0 m         (1000) m         (1000)     2609 2021-10-10 16:57:22.000000 hopla-cli-0.0.32a0/src/hopla/cli/cast.py
--rw-------   0 m         (1000) m         (1000)     8373 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/cli/complete.py
--rw-------   0 m         (1000) m         (1000)     3440 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/cli/config.py
--rw-------   0 m         (1000) m         (1000)     7559 2021-10-10 10:56:10.000000 hopla-cli-0.0.32a0/src/hopla/cli/feed.py
--rw-------   0 m         (1000) m         (1000)     3776 2022-04-13 17:07:04.000000 hopla-cli-0.0.32a0/src/hopla/cli/feed_all.py
--rw-------   0 m         (1000) m         (1000)     2442 2022-10-03 20:13:25.000000 hopla-cli-0.0.32a0/src/hopla/cli/get_group.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.782755 hopla-cli-0.0.32a0/src/hopla/cli/get_user/
--rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/cli/get_user/__init__.py
--rw-------   0 m         (1000) m         (1000)     2050 2023-02-01 16:39:39.000000 hopla-cli-0.0.32a0/src/hopla/cli/get_user/auth.py
--rw-------   0 m         (1000) m         (1000)     2673 2023-02-01 16:39:39.000000 hopla-cli-0.0.32a0/src/hopla/cli/get_user/info.py
--rw-------   0 m         (1000) m         (1000)     1960 2023-02-01 16:39:39.000000 hopla-cli-0.0.32a0/src/hopla/cli/get_user/inventory.py
--rw-------   0 m         (1000) m         (1000)     2270 2023-02-01 16:39:39.000000 hopla-cli-0.0.32a0/src/hopla/cli/get_user/stats.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.782755 hopla-cli-0.0.32a0/src/hopla/cli/groupcmds/
--rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/cli/groupcmds/__init__.py
--rw-------   0 m         (1000) m         (1000)      208 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/cli/groupcmds/add.py
--rw-------   0 m         (1000) m         (1000)     3747 2022-10-03 20:13:25.000000 hopla-cli-0.0.32a0/src/hopla/cli/groupcmds/api.py
--rw-------   0 m         (1000) m         (1000)      160 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/cli/groupcmds/buy.py
--rw-------   0 m         (1000) m         (1000)      609 2021-10-02 17:13:58.000000 hopla-cli-0.0.32a0/src/hopla/cli/groupcmds/get_user.py
--rw-------   0 m         (1000) m         (1000)      873 2021-10-03 17:04:03.000000 hopla-cli-0.0.32a0/src/hopla/cli/groupcmds/hatch.py
--rw-------   0 m         (1000) m         (1000)     1950 2022-10-03 20:13:25.000000 hopla-cli-0.0.32a0/src/hopla/cli/groupcmds/set.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.782755 hopla-cli-0.0.32a0/src/hopla/cli/hatch/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 15:11:29.000000 hopla-cli-0.0.32a0/src/hopla/cli/hatch/__init__.py
--rw-------   0 m         (1000) m         (1000)     1128 2022-04-13 16:39:26.000000 hopla-cli-0.0.32a0/src/hopla/cli/hatch/quest_egg.py
--rw-------   0 m         (1000) m         (1000)     1425 2022-04-13 16:40:23.000000 hopla-cli-0.0.32a0/src/hopla/cli/hatch/standard_egg.py
--rw-------   0 m         (1000) m         (1000)     4075 2021-10-12 08:45:19.000000 hopla-cli-0.0.32a0/src/hopla/cli/hatch_all.py
--rw-------   0 m         (1000) m         (1000)     5590 2021-10-11 17:29:51.000000 hopla-cli-0.0.32a0/src/hopla/cli/request.py
--rw-------   0 m         (1000) m         (1000)     1889 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/cli/support_development.py
--rw-------   0 m         (1000) m         (1000)      369 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/cli/version.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.782755 hopla-cli-0.0.32a0/src/hopla/hoplalib/
--rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/__init__.py
--rw-------   0 m         (1000) m         (1000)     6111 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/authorization.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.782755 hopla-cli-0.0.32a0/src/hopla/hoplalib/buy/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-10 18:40:43.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/buy/__init__.py
--rw-------   0 m         (1000) m         (1000)     1252 2022-10-03 20:13:25.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/buy/buy_controllers.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.782755 hopla-cli-0.0.32a0/src/hopla/hoplalib/cast/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/cast/__init__.py
--rw-------   0 m         (1000) m         (1000)      888 2022-10-03 20:13:25.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/cast/castcontroller.py
--rw-------   0 m         (1000) m         (1000)     2820 2021-10-10 16:57:22.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/cast/spellmodel.py
--rw-------   0 m         (1000) m         (1000)     2033 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/common.py
--rw-------   0 m         (1000) m         (1000)     6874 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/configuration.py
--rw-------   0 m         (1000) m         (1000)     1116 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/errors.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.782755 hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 15:11:29.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/__init__.py
--rw-------   0 m         (1000) m         (1000)     1281 2022-04-13 16:56:16.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/egg_data.py
--rw-------   0 m         (1000) m         (1000)     3750 2022-04-13 16:38:45.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/eggmodels.py
--rw-------   0 m         (1000) m         (1000)     5386 2021-10-04 18:58:52.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/hatchalgorithms.py
--rw-------   0 m         (1000) m         (1000)      962 2022-10-03 20:13:25.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/hatchcontroller.py
--rw-------   0 m         (1000) m         (1000)     1755 2023-02-14 16:19:52.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/hatchpotion_data.py
--rw-------   0 m         (1000) m         (1000)     3179 2022-04-13 16:41:13.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/hatchpotionmodels.py
--rw-------   0 m         (1000) m         (1000)      534 2021-10-11 11:57:30.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/hopla_option.py
--rw-------   0 m         (1000) m         (1000)     1536 2023-02-14 16:23:22.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/hoplaversion.py
--rw-------   0 m         (1000) m         (1000)     2617 2022-10-03 20:13:25.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/http.py
--rw-------   0 m         (1000) m         (1000)      566 2021-10-11 17:29:51.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/outputformatter.py
--rw-------   0 m         (1000) m         (1000)     1024 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/requests_helper.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.782755 hopla-cli-0.0.32a0/src/hopla/hoplalib/tasks/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/tasks/__init__.py
--rw-------   0 m         (1000) m         (1000)      908 2022-10-03 20:13:25.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/tasks/taskcontroller.py
--rw-------   0 m         (1000) m         (1000)     3475 2021-10-04 19:13:15.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/tasks/taskmodel.py
--rw-------   0 m         (1000) m         (1000)     7190 2021-10-12 12:10:10.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/throttling.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.782755 hopla-cli-0.0.32a0/src/hopla/hoplalib/user/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 17:13:58.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/user/__init__.py
--rw-------   0 m         (1000) m         (1000)     1141 2022-10-03 20:13:25.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/user/usercontroller.py
--rw-------   0 m         (1000) m         (1000)     3508 2021-11-24 10:10:57.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/user/usermodels.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.782755 hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/
--rw-------   0 m         (1000) m         (1000)      176 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/__init__.py
--rw-------   0 m         (1000) m         (1000)      860 2021-10-03 17:04:03.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/feed_clickhelper.py
--rw-------   0 m         (1000) m         (1000)     1569 2021-10-03 17:04:03.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/fooddata.py
--rw-------   0 m         (1000) m         (1000)     7592 2021-10-03 17:04:03.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/foodmodels.py
--rw-------   0 m         (1000) m         (1000)     2273 2022-10-03 20:13:25.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/petcontroller.py
--rw-------   0 m         (1000) m         (1000)     3894 2023-02-01 16:39:39.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/petdata.py
--rw-------   0 m         (1000) m         (1000)     8924 2022-04-13 16:41:17.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/petmodels.py
--rw-------   0 m         (1000) m         (1000)     4635 2021-10-12 10:34:43.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/zoofeed_algorithms.py
--rw-------   0 m         (1000) m         (1000)     3584 2021-10-03 17:04:03.000000 hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/zoomodels.py
--rw-------   0 m         (1000) m         (1000)     4449 2023-02-01 16:39:39.000000 hopla-cli-0.0.32a0/src/hopla/kickstart.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.782755 hopla-cli-0.0.32a0/src/hopla_cli.egg-info/
--rw-------   0 m         (1000) m         (1000)     7118 2023-02-14 16:25:02.000000 hopla-cli-0.0.32a0/src/hopla_cli.egg-info/PKG-INFO
--rw-------   0 m         (1000) m         (1000)     4601 2023-02-14 16:25:02.000000 hopla-cli-0.0.32a0/src/hopla_cli.egg-info/SOURCES.txt
--rw-------   0 m         (1000) m         (1000)        1 2023-02-14 16:25:02.000000 hopla-cli-0.0.32a0/src/hopla_cli.egg-info/dependency_links.txt
--rw-------   0 m         (1000) m         (1000)       56 2023-02-14 16:25:02.000000 hopla-cli-0.0.32a0/src/hopla_cli.egg-info/entry_points.txt
--rw-------   0 m         (1000) m         (1000)       15 2023-02-14 16:25:02.000000 hopla-cli-0.0.32a0/src/hopla_cli.egg-info/requires.txt
--rw-------   0 m         (1000) m         (1000)       12 2023-02-14 16:25:02.000000 hopla-cli-0.0.32a0/src/hopla_cli.egg-info/top_level.txt
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/
--rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/__init__.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/cli/
--rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/cli/__init__.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/cli/add/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-04 19:13:15.000000 hopla-cli-0.0.32a0/src/tests/cli/add/__init__.py
--rw-------   0 m         (1000) m         (1000)     5572 2021-10-04 19:13:15.000000 hopla-cli-0.0.32a0/src/tests/cli/add/test_todo.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/cli/buy/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/cli/buy/__init__.py
--rw-------   0 m         (1000) m         (1000)     3854 2021-10-10 18:40:43.000000 hopla-cli-0.0.32a0/src/tests/cli/buy/test_enchanted_armoire.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/cli/get_user/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/cli/get_user/__init__.py
--rw-------   0 m         (1000) m         (1000)    27891 2021-10-03 17:04:03.000000 hopla-cli-0.0.32a0/src/tests/cli/get_user/test_info.py
--rw-------   0 m         (1000) m         (1000)     1722 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/cli/get_user/test_stats.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/cli/groupcmds/
--rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/cli/groupcmds/__init__.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/cli/hatch/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 15:11:29.000000 hopla-cli-0.0.32a0/src/tests/cli/hatch/__init__.py
--rw-------   0 m         (1000) m         (1000)     2175 2021-10-03 16:37:42.000000 hopla-cli-0.0.32a0/src/tests/cli/hatch/test_quest_egg.py
--rw-------   0 m         (1000) m         (1000)     2293 2021-10-03 16:37:42.000000 hopla-cli-0.0.32a0/src/tests/cli/hatch/test_standard_egg.py
--rw-------   0 m         (1000) m         (1000)     5677 2021-10-10 16:57:22.000000 hopla-cli-0.0.32a0/src/tests/cli/test_cast.py
--rw-------   0 m         (1000) m         (1000)      630 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/cli/test_complete.py
--rw-------   0 m         (1000) m         (1000)    12615 2021-10-03 17:04:03.000000 hopla-cli-0.0.32a0/src/tests/cli/test_feed.py
--rw-------   0 m         (1000) m         (1000)     6852 2021-10-12 10:34:43.000000 hopla-cli-0.0.32a0/src/tests/cli/test_feed_all.py
--rw-------   0 m         (1000) m         (1000)     9272 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/cli/test_get_group.py
--rw-------   0 m         (1000) m         (1000)     6379 2021-10-12 08:45:19.000000 hopla-cli-0.0.32a0/src/tests/cli/test_hatch_all.py
--rw-------   0 m         (1000) m         (1000)     5163 2021-10-11 17:29:51.000000 hopla-cli-0.0.32a0/src/tests/cli/test_request.py
--rw-------   0 m         (1000) m         (1000)    10113 2021-10-12 12:10:10.000000 hopla-cli-0.0.32a0/src/tests/cli/test_throttling.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/hoplalib/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/__init__.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/hoplalib/buy/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-10 18:40:43.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/buy/__init__.py
--rw-------   0 m         (1000) m         (1000)      316 2021-10-10 18:40:43.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/buy/test_buy_controllers.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/hoplalib/cast/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/cast/__init__.py
--rw-------   0 m         (1000) m         (1000)      504 2021-10-10 14:28:50.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/cast/test_castcontroller.py
--rw-------   0 m         (1000) m         (1000)      244 2021-10-10 16:57:22.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/cast/test_classmodels.py
--rw-------   0 m         (1000) m         (1000)     2142 2021-10-10 16:57:22.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/cast/test_spellmodel.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/hoplalib/hatchery/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 15:11:29.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/hatchery/__init__.py
--rw-------   0 m         (1000) m         (1000)     8761 2022-04-13 16:42:07.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/hatchery/test_eggmodels.py
--rw-------   0 m         (1000) m         (1000)    14510 2022-04-13 16:40:08.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/hatchery/test_hatchalgorithm.py
--rw-------   0 m         (1000) m         (1000)      581 2021-10-03 17:04:03.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/hatchery/test_hatchcontroller.py
--rw-------   0 m         (1000) m         (1000)     7842 2022-04-13 16:41:53.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/hatchery/test_hatchpotionmodels.py
--rw-------   0 m         (1000) m         (1000)     1022 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/test_errors.py
--rw-------   0 m         (1000) m         (1000)      264 2021-10-11 11:57:30.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/test_hopla_option.py
--rw-------   0 m         (1000) m         (1000)     1767 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/test_hoplaversion.py
--rw-------   0 m         (1000) m         (1000)     1066 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/test_outputformatter.py
--rw-------   0 m         (1000) m         (1000)     1257 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/test_requests_helper.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/hoplalib/user/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 17:13:58.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/user/__init__.py
--rw-------   0 m         (1000) m         (1000)     3780 2021-10-03 17:04:03.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/user/test_usermodels.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/__init__.py
--rw-------   0 m         (1000) m         (1000)    11033 2021-10-03 17:04:03.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/test_foodmodels.py
--rw-------   0 m         (1000) m         (1000)     2596 2022-10-03 20:13:25.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/test_petcontroller.py
--rw-------   0 m         (1000) m         (1000)     4253 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/test_petdata.py
--rw-------   0 m         (1000) m         (1000)    18786 2021-10-03 17:04:03.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/test_petmodels.py
--rw-------   0 m         (1000) m         (1000)     9102 2021-10-12 10:34:43.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/test_zoofeeding_algorithms.py
--rw-------   0 m         (1000) m         (1000)     5948 2021-10-03 17:04:03.000000 hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/test_zoomodels.py
--rw-------   0 m         (1000) m         (1000)     2026 2021-10-04 17:22:17.000000 hopla-cli-0.0.32a0/src/tests/test_kickstarter.py
-drwx------   0 m         (1000) m         (1000)        0 2023-02-14 16:25:02.786756 hopla-cli-0.0.32a0/src/tests/testutils/
--rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/testutils/__init__.py
--rw-------   0 m         (1000) m         (1000)      856 2021-10-02 13:16:33.000000 hopla-cli-0.0.32a0/src/tests/testutils/user_test_utils.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.989050 hopla-cli-0.0.33a0/
+-rw-------   0 m         (1000) m         (1000)     7118 2023-04-06 19:21:21.989050 hopla-cli-0.0.33a0/PKG-INFO
+-rw-------   0 m         (1000) m         (1000)     5804 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/README.md
+-rw-------   0 m         (1000) m         (1000)      272 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/pyproject.toml
+-rw-------   0 m         (1000) m         (1000)     1508 2023-04-06 19:21:21.989050 hopla-cli-0.0.33a0/setup.cfg
+-rw-------   0 m         (1000) m         (1000)      352 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/setup.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.977051 hopla-cli-0.0.33a0/src/
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.981051 hopla-cli-0.0.33a0/src/hopla/
+-rwx------   0 m         (1000) m         (1000)      880 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/__init__.py
+-rwx------   0 m         (1000) m         (1000)      267 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/__main__.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.981051 hopla-cli-0.0.33a0/src/hopla/cli/
+-rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/cli/__init__.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.981051 hopla-cli-0.0.33a0/src/hopla/cli/add/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/cli/add/__init__.py
+-rw-------   0 m         (1000) m         (1000)     6904 2021-10-04 19:13:15.000000 hopla-cli-0.0.33a0/src/hopla/cli/add/todo.py
+-rw-------   0 m         (1000) m         (1000)     1652 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/cli/authenticate.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.981051 hopla-cli-0.0.33a0/src/hopla/cli/buy/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/cli/buy/__init__.py
+-rw-------   0 m         (1000) m         (1000)     4576 2021-10-10 18:40:43.000000 hopla-cli-0.0.33a0/src/hopla/cli/buy/enchanted_armoire.py
+-rw-------   0 m         (1000) m         (1000)     2609 2021-10-10 16:57:22.000000 hopla-cli-0.0.33a0/src/hopla/cli/cast.py
+-rw-------   0 m         (1000) m         (1000)     8373 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/cli/complete.py
+-rw-------   0 m         (1000) m         (1000)     3440 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/cli/config.py
+-rw-------   0 m         (1000) m         (1000)     7559 2021-10-10 10:56:10.000000 hopla-cli-0.0.33a0/src/hopla/cli/feed.py
+-rw-------   0 m         (1000) m         (1000)     3776 2022-04-13 17:07:04.000000 hopla-cli-0.0.33a0/src/hopla/cli/feed_all.py
+-rw-------   0 m         (1000) m         (1000)     2442 2022-10-03 20:13:25.000000 hopla-cli-0.0.33a0/src/hopla/cli/get_group.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.981051 hopla-cli-0.0.33a0/src/hopla/cli/get_user/
+-rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/cli/get_user/__init__.py
+-rw-------   0 m         (1000) m         (1000)     2050 2023-02-01 16:39:39.000000 hopla-cli-0.0.33a0/src/hopla/cli/get_user/auth.py
+-rw-------   0 m         (1000) m         (1000)     2673 2023-02-01 16:39:39.000000 hopla-cli-0.0.33a0/src/hopla/cli/get_user/info.py
+-rw-------   0 m         (1000) m         (1000)     1960 2023-02-01 16:39:39.000000 hopla-cli-0.0.33a0/src/hopla/cli/get_user/inventory.py
+-rw-------   0 m         (1000) m         (1000)     2270 2023-02-01 16:39:39.000000 hopla-cli-0.0.33a0/src/hopla/cli/get_user/stats.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.981051 hopla-cli-0.0.33a0/src/hopla/cli/groupcmds/
+-rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/cli/groupcmds/__init__.py
+-rw-------   0 m         (1000) m         (1000)      208 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/cli/groupcmds/add.py
+-rw-------   0 m         (1000) m         (1000)     3747 2022-10-03 20:13:25.000000 hopla-cli-0.0.33a0/src/hopla/cli/groupcmds/api.py
+-rw-------   0 m         (1000) m         (1000)      160 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/cli/groupcmds/buy.py
+-rw-------   0 m         (1000) m         (1000)      609 2021-10-02 17:13:58.000000 hopla-cli-0.0.33a0/src/hopla/cli/groupcmds/get_user.py
+-rw-------   0 m         (1000) m         (1000)      873 2021-10-03 17:04:03.000000 hopla-cli-0.0.33a0/src/hopla/cli/groupcmds/hatch.py
+-rw-------   0 m         (1000) m         (1000)     1950 2022-10-03 20:13:25.000000 hopla-cli-0.0.33a0/src/hopla/cli/groupcmds/set.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.981051 hopla-cli-0.0.33a0/src/hopla/cli/hatch/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 15:11:29.000000 hopla-cli-0.0.33a0/src/hopla/cli/hatch/__init__.py
+-rw-------   0 m         (1000) m         (1000)     1128 2022-04-13 16:39:26.000000 hopla-cli-0.0.33a0/src/hopla/cli/hatch/quest_egg.py
+-rw-------   0 m         (1000) m         (1000)     1425 2022-04-13 16:40:23.000000 hopla-cli-0.0.33a0/src/hopla/cli/hatch/standard_egg.py
+-rw-------   0 m         (1000) m         (1000)     4075 2021-10-12 08:45:19.000000 hopla-cli-0.0.33a0/src/hopla/cli/hatch_all.py
+-rw-------   0 m         (1000) m         (1000)     5590 2021-10-11 17:29:51.000000 hopla-cli-0.0.33a0/src/hopla/cli/request.py
+-rw-------   0 m         (1000) m         (1000)     1889 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/cli/support_development.py
+-rw-------   0 m         (1000) m         (1000)      369 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/cli/version.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.981051 hopla-cli-0.0.33a0/src/hopla/hoplalib/
+-rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/__init__.py
+-rw-------   0 m         (1000) m         (1000)     6111 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/authorization.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/hopla/hoplalib/buy/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-10 18:40:43.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/buy/__init__.py
+-rw-------   0 m         (1000) m         (1000)     1252 2022-10-03 20:13:25.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/buy/buy_controllers.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/hopla/hoplalib/cast/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/cast/__init__.py
+-rw-------   0 m         (1000) m         (1000)      888 2022-10-03 20:13:25.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/cast/castcontroller.py
+-rw-------   0 m         (1000) m         (1000)     2820 2021-10-10 16:57:22.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/cast/spellmodel.py
+-rw-------   0 m         (1000) m         (1000)     2033 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/common.py
+-rw-------   0 m         (1000) m         (1000)     6874 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/configuration.py
+-rw-------   0 m         (1000) m         (1000)     1116 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/errors.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 15:11:29.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/__init__.py
+-rw-------   0 m         (1000) m         (1000)     1281 2022-04-13 16:56:16.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/egg_data.py
+-rw-------   0 m         (1000) m         (1000)     3750 2022-04-13 16:38:45.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/eggmodels.py
+-rw-------   0 m         (1000) m         (1000)     5386 2021-10-04 18:58:52.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/hatchalgorithms.py
+-rw-------   0 m         (1000) m         (1000)      962 2022-10-03 20:13:25.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/hatchcontroller.py
+-rw-------   0 m         (1000) m         (1000)     1771 2023-04-06 19:18:42.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/hatchpotion_data.py
+-rw-------   0 m         (1000) m         (1000)     3179 2022-04-13 16:41:13.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/hatchpotionmodels.py
+-rw-------   0 m         (1000) m         (1000)      534 2021-10-11 11:57:30.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/hopla_option.py
+-rw-------   0 m         (1000) m         (1000)     1536 2023-04-06 19:20:15.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/hoplaversion.py
+-rw-------   0 m         (1000) m         (1000)     2617 2022-10-03 20:13:25.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/http.py
+-rw-------   0 m         (1000) m         (1000)      566 2021-10-11 17:29:51.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/outputformatter.py
+-rw-------   0 m         (1000) m         (1000)     1024 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/requests_helper.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/hopla/hoplalib/tasks/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/tasks/__init__.py
+-rw-------   0 m         (1000) m         (1000)      908 2022-10-03 20:13:25.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/tasks/taskcontroller.py
+-rw-------   0 m         (1000) m         (1000)     3475 2021-10-04 19:13:15.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/tasks/taskmodel.py
+-rw-------   0 m         (1000) m         (1000)     7190 2021-10-12 12:10:10.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/throttling.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/hopla/hoplalib/user/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 17:13:58.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/user/__init__.py
+-rw-------   0 m         (1000) m         (1000)     1141 2022-10-03 20:13:25.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/user/usercontroller.py
+-rw-------   0 m         (1000) m         (1000)     3508 2021-11-24 10:10:57.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/user/usermodels.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/
+-rw-------   0 m         (1000) m         (1000)      176 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/__init__.py
+-rw-------   0 m         (1000) m         (1000)      860 2021-10-03 17:04:03.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/feed_clickhelper.py
+-rw-------   0 m         (1000) m         (1000)     1569 2021-10-03 17:04:03.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/fooddata.py
+-rw-------   0 m         (1000) m         (1000)     7592 2021-10-03 17:04:03.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/foodmodels.py
+-rw-------   0 m         (1000) m         (1000)     2273 2022-10-03 20:13:25.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/petcontroller.py
+-rw-------   0 m         (1000) m         (1000)     3894 2023-02-01 16:39:39.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/petdata.py
+-rw-------   0 m         (1000) m         (1000)     8924 2022-04-13 16:41:17.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/petmodels.py
+-rw-------   0 m         (1000) m         (1000)     4635 2021-10-12 10:34:43.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/zoofeed_algorithms.py
+-rw-------   0 m         (1000) m         (1000)     3584 2021-10-03 17:04:03.000000 hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/zoomodels.py
+-rw-------   0 m         (1000) m         (1000)     4449 2023-02-01 16:39:39.000000 hopla-cli-0.0.33a0/src/hopla/kickstart.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/hopla_cli.egg-info/
+-rw-------   0 m         (1000) m         (1000)     7118 2023-04-06 19:21:21.000000 hopla-cli-0.0.33a0/src/hopla_cli.egg-info/PKG-INFO
+-rw-------   0 m         (1000) m         (1000)     4601 2023-04-06 19:21:21.000000 hopla-cli-0.0.33a0/src/hopla_cli.egg-info/SOURCES.txt
+-rw-------   0 m         (1000) m         (1000)        1 2023-04-06 19:21:21.000000 hopla-cli-0.0.33a0/src/hopla_cli.egg-info/dependency_links.txt
+-rw-------   0 m         (1000) m         (1000)       56 2023-04-06 19:21:21.000000 hopla-cli-0.0.33a0/src/hopla_cli.egg-info/entry_points.txt
+-rw-------   0 m         (1000) m         (1000)       15 2023-04-06 19:21:21.000000 hopla-cli-0.0.33a0/src/hopla_cli.egg-info/requires.txt
+-rw-------   0 m         (1000) m         (1000)       12 2023-04-06 19:21:21.000000 hopla-cli-0.0.33a0/src/hopla_cli.egg-info/top_level.txt
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/tests/
+-rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/__init__.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/tests/cli/
+-rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/cli/__init__.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/tests/cli/add/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-04 19:13:15.000000 hopla-cli-0.0.33a0/src/tests/cli/add/__init__.py
+-rw-------   0 m         (1000) m         (1000)     5572 2021-10-04 19:13:15.000000 hopla-cli-0.0.33a0/src/tests/cli/add/test_todo.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/tests/cli/buy/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/cli/buy/__init__.py
+-rw-------   0 m         (1000) m         (1000)     3854 2021-10-10 18:40:43.000000 hopla-cli-0.0.33a0/src/tests/cli/buy/test_enchanted_armoire.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/tests/cli/get_user/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/cli/get_user/__init__.py
+-rw-------   0 m         (1000) m         (1000)    27891 2021-10-03 17:04:03.000000 hopla-cli-0.0.33a0/src/tests/cli/get_user/test_info.py
+-rw-------   0 m         (1000) m         (1000)     1722 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/cli/get_user/test_stats.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.985051 hopla-cli-0.0.33a0/src/tests/cli/groupcmds/
+-rw-------   0 m         (1000) m         (1000)        0 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/cli/groupcmds/__init__.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.989050 hopla-cli-0.0.33a0/src/tests/cli/hatch/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 15:11:29.000000 hopla-cli-0.0.33a0/src/tests/cli/hatch/__init__.py
+-rw-------   0 m         (1000) m         (1000)     2175 2021-10-03 16:37:42.000000 hopla-cli-0.0.33a0/src/tests/cli/hatch/test_quest_egg.py
+-rw-------   0 m         (1000) m         (1000)     2293 2021-10-03 16:37:42.000000 hopla-cli-0.0.33a0/src/tests/cli/hatch/test_standard_egg.py
+-rw-------   0 m         (1000) m         (1000)     5677 2021-10-10 16:57:22.000000 hopla-cli-0.0.33a0/src/tests/cli/test_cast.py
+-rw-------   0 m         (1000) m         (1000)      630 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/cli/test_complete.py
+-rw-------   0 m         (1000) m         (1000)    12615 2021-10-03 17:04:03.000000 hopla-cli-0.0.33a0/src/tests/cli/test_feed.py
+-rw-------   0 m         (1000) m         (1000)     6852 2021-10-12 10:34:43.000000 hopla-cli-0.0.33a0/src/tests/cli/test_feed_all.py
+-rw-------   0 m         (1000) m         (1000)     9272 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/cli/test_get_group.py
+-rw-------   0 m         (1000) m         (1000)     6379 2021-10-12 08:45:19.000000 hopla-cli-0.0.33a0/src/tests/cli/test_hatch_all.py
+-rw-------   0 m         (1000) m         (1000)     5163 2021-10-11 17:29:51.000000 hopla-cli-0.0.33a0/src/tests/cli/test_request.py
+-rw-------   0 m         (1000) m         (1000)    10113 2021-10-12 12:10:10.000000 hopla-cli-0.0.33a0/src/tests/cli/test_throttling.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.989050 hopla-cli-0.0.33a0/src/tests/hoplalib/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/__init__.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.989050 hopla-cli-0.0.33a0/src/tests/hoplalib/buy/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-10 18:40:43.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/buy/__init__.py
+-rw-------   0 m         (1000) m         (1000)      316 2021-10-10 18:40:43.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/buy/test_buy_controllers.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.989050 hopla-cli-0.0.33a0/src/tests/hoplalib/cast/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/cast/__init__.py
+-rw-------   0 m         (1000) m         (1000)      504 2021-10-10 14:28:50.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/cast/test_castcontroller.py
+-rw-------   0 m         (1000) m         (1000)      244 2021-10-10 16:57:22.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/cast/test_classmodels.py
+-rw-------   0 m         (1000) m         (1000)     2142 2021-10-10 16:57:22.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/cast/test_spellmodel.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.989050 hopla-cli-0.0.33a0/src/tests/hoplalib/hatchery/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 15:11:29.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/hatchery/__init__.py
+-rw-------   0 m         (1000) m         (1000)     8761 2022-04-13 16:42:07.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/hatchery/test_eggmodels.py
+-rw-------   0 m         (1000) m         (1000)    14510 2022-04-13 16:40:08.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/hatchery/test_hatchalgorithm.py
+-rw-------   0 m         (1000) m         (1000)      581 2021-10-03 17:04:03.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/hatchery/test_hatchcontroller.py
+-rw-------   0 m         (1000) m         (1000)     7842 2022-04-13 16:41:53.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/hatchery/test_hatchpotionmodels.py
+-rw-------   0 m         (1000) m         (1000)     1022 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/test_errors.py
+-rw-------   0 m         (1000) m         (1000)      264 2021-10-11 11:57:30.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/test_hopla_option.py
+-rw-------   0 m         (1000) m         (1000)     1767 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/test_hoplaversion.py
+-rw-------   0 m         (1000) m         (1000)     1066 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/test_outputformatter.py
+-rw-------   0 m         (1000) m         (1000)     1257 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/test_requests_helper.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.989050 hopla-cli-0.0.33a0/src/tests/hoplalib/user/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 17:13:58.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/user/__init__.py
+-rw-------   0 m         (1000) m         (1000)     3780 2021-10-03 17:04:03.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/user/test_usermodels.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.989050 hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/__init__.py
+-rw-------   0 m         (1000) m         (1000)    11033 2021-10-03 17:04:03.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/test_foodmodels.py
+-rw-------   0 m         (1000) m         (1000)     2596 2022-10-03 20:13:25.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/test_petcontroller.py
+-rw-------   0 m         (1000) m         (1000)     4253 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/test_petdata.py
+-rw-------   0 m         (1000) m         (1000)    18786 2021-10-03 17:04:03.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/test_petmodels.py
+-rw-------   0 m         (1000) m         (1000)     9102 2021-10-12 10:34:43.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/test_zoofeeding_algorithms.py
+-rw-------   0 m         (1000) m         (1000)     5948 2021-10-03 17:04:03.000000 hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/test_zoomodels.py
+-rw-------   0 m         (1000) m         (1000)     2026 2021-10-04 17:22:17.000000 hopla-cli-0.0.33a0/src/tests/test_kickstarter.py
+drwx------   0 m         (1000) m         (1000)        0 2023-04-06 19:21:21.989050 hopla-cli-0.0.33a0/src/tests/testutils/
+-rw-------   0 m         (1000) m         (1000)       23 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/testutils/__init__.py
+-rw-------   0 m         (1000) m         (1000)      856 2021-10-02 13:16:33.000000 hopla-cli-0.0.33a0/src/tests/testutils/user_test_utils.py
```

### Comparing `hopla-cli-0.0.32a0/PKG-INFO` & `hopla-cli-0.0.33a0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hopla-cli
-Version: 0.0.32a0
+Version: 0.0.33a0
 Summary: Hopla is a CLI to interact with the habitica.com API
 Home-page: https://github.com/melvio/hopla
 Author: melvio
 Author-email: hopla.pypi@gmail.com
 License: Apache-2.0
 Project-URL: Source, https://github.com/melvio/hopla/
 Project-URL: Readme, https://github.com/melvio/hopla/blob/main/README.md
```

### Comparing `hopla-cli-0.0.32a0/README.md` & `hopla-cli-0.0.33a0/README.md`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/setup.cfg` & `hopla-cli-0.0.33a0/setup.cfg`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/__init__.py` & `hopla-cli-0.0.33a0/src/hopla/__init__.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/add/todo.py` & `hopla-cli-0.0.33a0/src/hopla/cli/add/todo.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/authenticate.py` & `hopla-cli-0.0.33a0/src/hopla/cli/authenticate.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/buy/enchanted_armoire.py` & `hopla-cli-0.0.33a0/src/hopla/cli/buy/enchanted_armoire.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/cast.py` & `hopla-cli-0.0.33a0/src/hopla/cli/cast.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/complete.py` & `hopla-cli-0.0.33a0/src/hopla/cli/complete.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/config.py` & `hopla-cli-0.0.33a0/src/hopla/cli/config.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/feed.py` & `hopla-cli-0.0.33a0/src/hopla/cli/feed.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/feed_all.py` & `hopla-cli-0.0.33a0/src/hopla/cli/feed_all.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/get_group.py` & `hopla-cli-0.0.33a0/src/hopla/cli/get_group.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/get_user/auth.py` & `hopla-cli-0.0.33a0/src/hopla/cli/get_user/auth.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/get_user/info.py` & `hopla-cli-0.0.33a0/src/hopla/cli/get_user/info.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/get_user/inventory.py` & `hopla-cli-0.0.33a0/src/hopla/cli/get_user/inventory.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/get_user/stats.py` & `hopla-cli-0.0.33a0/src/hopla/cli/get_user/stats.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/groupcmds/api.py` & `hopla-cli-0.0.33a0/src/hopla/cli/groupcmds/api.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/groupcmds/get_user.py` & `hopla-cli-0.0.33a0/src/hopla/cli/groupcmds/get_user.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/groupcmds/hatch.py` & `hopla-cli-0.0.33a0/src/hopla/cli/groupcmds/hatch.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/groupcmds/set.py` & `hopla-cli-0.0.33a0/src/hopla/cli/groupcmds/set.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/hatch/quest_egg.py` & `hopla-cli-0.0.33a0/src/hopla/cli/hatch/quest_egg.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/hatch/standard_egg.py` & `hopla-cli-0.0.33a0/src/hopla/cli/hatch/standard_egg.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/hatch_all.py` & `hopla-cli-0.0.33a0/src/hopla/cli/hatch_all.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/request.py` & `hopla-cli-0.0.33a0/src/hopla/cli/request.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/cli/support_development.py` & `hopla-cli-0.0.33a0/src/hopla/cli/support_development.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/authorization.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/authorization.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/buy/buy_controllers.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/buy/buy_controllers.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/cast/castcontroller.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/cast/castcontroller.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/cast/spellmodel.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/cast/spellmodel.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/common.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/common.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/configuration.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/configuration.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/errors.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/errors.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/egg_data.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/egg_data.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/eggmodels.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/eggmodels.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/hatchalgorithms.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/hatchalgorithms.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/hatchcontroller.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/hatchcontroller.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/hatchpotion_data.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/hatchpotion_data.py`

 * *Files 3% similar despite different names*

```diff
@@ -10,15 +10,15 @@
     drop_hatch_potion_names = [
         "Base", "CottonCandyBlue", "CottonCandyPink", "Desert", "Golden",
         "Red", "Shade", "Skeleton", "White", "Zombie"
     ]
     """
     Drop hatching potions. Also known as 1st gen potions.
     This list was retrieved by using:
-    hopla api content | jq .dropHatchingPotions | jq keys
+        hopla api content | jq .dropHatchingPotions | jq keys
     """
 
     magic_hatch_potion_names = [
         "Amber", "Aquatic", "Aurora", "AutumnLeaf",
         "BirchBark", "BlackPearl", "Bronze",
         "Celestial", "Cupid", "Ember",
         "Fairy", "Floral", "Fluorite", "Frost",
@@ -28,21 +28,21 @@
         "Rainbow", "RoseQuartz", "RoyalPurple", "Ruby",
         "SandSculpture", "Shadow", "Shimmer", "Silver", "SolarSystem",
         "Spooky", "StainedGlass", "StarryNight", "Sunset", "Sunshine",
         "Thunderstorm", "Turquoise", "Vampire", "Watery", "Windup"
     ]
     """
     Magic hatching potions. This list was retrieved by using:
-    hopla api content | jq .premiumHatchingPotions | jq keys
+        hopla api content | jq .premiumHatchingPotions | jq keys
     """
 
-    wacky_hatch_potion_names = ["Dessert", "Veggie", "VirtualPet"]
+    wacky_hatch_potion_names = ["Dessert", "TeaShop", "Veggie", "VirtualPet"]
     """
     Wacky hatching potions. This list was retrieved by using:
-           hopla api content | jq '.wackyHatchingPotions|keys'
+        hopla api content | jq '.wackyHatchingPotions|keys'
     """
 
     non_drop_hatch_potion_names: List[str] = (
             magic_hatch_potion_names
             + wacky_hatch_potion_names
     )
```

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/hatchery/hatchpotionmodels.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/hatchery/hatchpotionmodels.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/hopla_option.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/hopla_option.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/hoplaversion.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/hoplaversion.py`

 * *Files 0% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 Module with hopla versioning logic.
 """
 from dataclasses import dataclass
 from typing import Final, Optional
 
 MAJOR_VERSION: Final[int] = 0
 MINOR_VERSION: Final[int] = 0
-PATCH_VERSION: Final[int] = 32
+PATCH_VERSION: Final[int] = 33
 PRE_RELEASE: Final[Optional[str]] = "alpha"
 
 
 @dataclass
 class HoplaVersion:
     """Class with HoplaVersion constants."""
```

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/http.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/http.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/outputformatter.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/outputformatter.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/requests_helper.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/requests_helper.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/tasks/taskcontroller.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/tasks/taskcontroller.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/tasks/taskmodel.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/tasks/taskmodel.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/throttling.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/throttling.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/user/usercontroller.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/user/usercontroller.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/user/usermodels.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/user/usermodels.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/feed_clickhelper.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/feed_clickhelper.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/fooddata.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/fooddata.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/foodmodels.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/foodmodels.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/petcontroller.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/petcontroller.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/petdata.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/petdata.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/petmodels.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/petmodels.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/zoofeed_algorithms.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/zoofeed_algorithms.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/hoplalib/zoo/zoomodels.py` & `hopla-cli-0.0.33a0/src/hopla/hoplalib/zoo/zoomodels.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla/kickstart.py` & `hopla-cli-0.0.33a0/src/hopla/kickstart.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/hopla_cli.egg-info/PKG-INFO` & `hopla-cli-0.0.33a0/src/hopla_cli.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hopla-cli
-Version: 0.0.32a0
+Version: 0.0.33a0
 Summary: Hopla is a CLI to interact with the habitica.com API
 Home-page: https://github.com/melvio/hopla
 Author: melvio
 Author-email: hopla.pypi@gmail.com
 License: Apache-2.0
 Project-URL: Source, https://github.com/melvio/hopla/
 Project-URL: Readme, https://github.com/melvio/hopla/blob/main/README.md
```

### Comparing `hopla-cli-0.0.32a0/src/hopla_cli.egg-info/SOURCES.txt` & `hopla-cli-0.0.33a0/src/hopla_cli.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/add/test_todo.py` & `hopla-cli-0.0.33a0/src/tests/cli/add/test_todo.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/buy/test_enchanted_armoire.py` & `hopla-cli-0.0.33a0/src/tests/cli/buy/test_enchanted_armoire.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/get_user/test_info.py` & `hopla-cli-0.0.33a0/src/tests/cli/get_user/test_info.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/get_user/test_stats.py` & `hopla-cli-0.0.33a0/src/tests/cli/get_user/test_stats.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/hatch/test_quest_egg.py` & `hopla-cli-0.0.33a0/src/tests/cli/hatch/test_quest_egg.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/hatch/test_standard_egg.py` & `hopla-cli-0.0.33a0/src/tests/cli/hatch/test_standard_egg.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/test_cast.py` & `hopla-cli-0.0.33a0/src/tests/cli/test_cast.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/test_complete.py` & `hopla-cli-0.0.33a0/src/tests/cli/test_complete.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/test_feed.py` & `hopla-cli-0.0.33a0/src/tests/cli/test_feed.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/test_feed_all.py` & `hopla-cli-0.0.33a0/src/tests/cli/test_feed_all.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/test_get_group.py` & `hopla-cli-0.0.33a0/src/tests/cli/test_get_group.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/test_hatch_all.py` & `hopla-cli-0.0.33a0/src/tests/cli/test_hatch_all.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/test_request.py` & `hopla-cli-0.0.33a0/src/tests/cli/test_request.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/cli/test_throttling.py` & `hopla-cli-0.0.33a0/src/tests/cli/test_throttling.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/cast/test_spellmodel.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/cast/test_spellmodel.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/hatchery/test_eggmodels.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/hatchery/test_eggmodels.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/hatchery/test_hatchalgorithm.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/hatchery/test_hatchalgorithm.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/hatchery/test_hatchcontroller.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/hatchery/test_hatchcontroller.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/hatchery/test_hatchpotionmodels.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/hatchery/test_hatchpotionmodels.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/test_errors.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/test_errors.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/test_hoplaversion.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/test_hoplaversion.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/test_outputformatter.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/test_outputformatter.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/test_requests_helper.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/test_requests_helper.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/user/test_usermodels.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/user/test_usermodels.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/test_foodmodels.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/test_foodmodels.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/test_petcontroller.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/test_petcontroller.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/test_petdata.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/test_petdata.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/test_petmodels.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/test_petmodels.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/test_zoofeeding_algorithms.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/test_zoofeeding_algorithms.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/hoplalib/zoo/test_zoomodels.py` & `hopla-cli-0.0.33a0/src/tests/hoplalib/zoo/test_zoomodels.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/test_kickstarter.py` & `hopla-cli-0.0.33a0/src/tests/test_kickstarter.py`

 * *Files identical despite different names*

### Comparing `hopla-cli-0.0.32a0/src/tests/testutils/user_test_utils.py` & `hopla-cli-0.0.33a0/src/tests/testutils/user_test_utils.py`

 * *Files identical despite different names*

