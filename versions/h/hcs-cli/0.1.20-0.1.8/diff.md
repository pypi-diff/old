# Comparing `tmp/hcs-cli-0.1.20.tar.gz` & `tmp/hcs-cli-0.1.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "hcs-cli-0.1.20.tar", last modified: Thu Apr  6 22:15:29 2023, max compression
+gzip compressed data, was "hcs-cli-0.1.8.tar", last modified: Thu Apr  6 01:53:41 2023, max compression
```

## Comparing `hcs-cli-0.1.20.tar` & `hcs-cli-0.1.8.tar`

### file list

```diff
@@ -1,93 +1,92 @@
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.348966 hcs-cli-0.1.20/
--rw-r--r--   0 nanw       (501) staff       (20)     2820 2023-01-11 22:10:27.000000 hcs-cli-0.1.20/.gitignore
--rw-r--r--   0 nanw       (501) staff       (20)      151 2023-04-06 22:15:29.337848 hcs-cli-0.1.20/PKG-INFO
--rw-r--r--   0 nanw       (501) staff       (20)     1194 2023-04-06 16:09:03.000000 hcs-cli-0.1.20/README.md
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.117456 hcs-cli-0.1.20/hcs_cli.egg-info/
--rw-r--r--   0 nanw       (501) staff       (20)      151 2023-04-06 22:15:28.000000 hcs-cli-0.1.20/hcs_cli.egg-info/PKG-INFO
--rw-r--r--   0 nanw       (501) staff       (20)     2081 2023-04-06 22:15:28.000000 hcs-cli-0.1.20/hcs_cli.egg-info/SOURCES.txt
--rw-r--r--   0 nanw       (501) staff       (20)        1 2023-04-06 22:15:28.000000 hcs-cli-0.1.20/hcs_cli.egg-info/dependency_links.txt
--rw-r--r--   0 nanw       (501) staff       (20)       42 2023-04-06 22:15:28.000000 hcs-cli-0.1.20/hcs_cli.egg-info/entry_points.txt
--rw-r--r--   0 nanw       (501) staff       (20)      106 2023-04-06 22:15:28.000000 hcs-cli-0.1.20/hcs_cli.egg-info/requires.txt
--rw-r--r--   0 nanw       (501) staff       (20)        5 2023-04-06 22:15:28.000000 hcs-cli-0.1.20/hcs_cli.egg-info/top_level.txt
--rw-r--r--   0 nanw       (501) staff       (20)      297 2023-01-11 22:10:27.000000 hcs-cli-0.1.20/pyproject.toml
--rw-r--r--   0 nanw       (501) staff       (20)      106 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/requirements.txt
--rw-r--r--   0 nanw       (501) staff       (20)       38 2023-04-06 22:15:29.350164 hcs-cli-0.1.20/setup.cfg
--rw-r--r--   0 nanw       (501) staff       (20)      753 2023-04-06 22:15:10.000000 hcs-cli-0.1.20/setup.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.141575 hcs-cli-0.1.20/vhcs/
--rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 21:25:27.000000 hcs-cli-0.1.20/vhcs/__init__.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.144945 hcs-cli-0.1.20/vhcs/cli/
--rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/cli/__init__.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.151208 hcs-cli-0.1.20/vhcs/cli/cmds/
--rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/cli/cmds/__init__.py
--rw-r--r--   0 nanw       (501) staff       (20)      486 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/cli/cmds/auth.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.154379 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/
--rw-r--r--   0 nanw       (501) staff       (20)       31 2023-04-06 17:42:33.000000 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/__init__.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.161940 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/provider/
--rw-r--r--   0 nanw       (501) staff       (20)       28 2023-04-06 17:42:33.000000 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/provider/__init__.py
--rw-r--r--   0 nanw       (501) staff       (20)      294 2023-04-06 22:10:53.000000 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/provider/delete.py
--rw-r--r--   0 nanw       (501) staff       (20)      285 2023-04-06 22:13:28.000000 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/provider/get.py
--rw-r--r--   0 nanw       (501) staff       (20)      225 2023-04-06 22:11:04.000000 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/provider/list.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.173360 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/template/
--rw-r--r--   0 nanw       (501) staff       (20)       28 2023-04-06 17:42:33.000000 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/template/__init__.py
--rw-r--r--   0 nanw       (501) staff       (20)      760 2023-04-06 22:11:12.000000 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/template/create.py
--rw-r--r--   0 nanw       (501) staff       (20)      450 2023-04-06 22:11:17.000000 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/template/delete.py
--rw-r--r--   0 nanw       (501) staff       (20)      285 2023-04-06 22:11:23.000000 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/template/get.py
--rw-r--r--   0 nanw       (501) staff       (20)      225 2023-04-06 22:11:29.000000 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/template/list.py
--rw-r--r--   0 nanw       (501) staff       (20)      154 2023-04-06 22:11:36.000000 hcs-cli-0.1.20/vhcs/cli/cmds/lcm/test.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.199169 hcs-cli-0.1.20/vhcs/cli/cmds/pki/
--rw-r--r--   0 nanw       (501) staff       (20)       31 2023-04-06 17:42:33.000000 hcs-cli-0.1.20/vhcs/cli/cmds/pki/__init__.py
--rw-r--r--   0 nanw       (501) staff       (20)      623 2023-04-06 22:11:46.000000 hcs-cli-0.1.20/vhcs/cli/cmds/pki/delete-org-cert.py
--rw-r--r--   0 nanw       (501) staff       (20)      262 2023-04-06 22:11:57.000000 hcs-cli-0.1.20/vhcs/cli/cmds/pki/get-root-ca.py
--rw-r--r--   0 nanw       (501) staff       (20)      398 2023-04-06 22:11:51.000000 hcs-cli-0.1.20/vhcs/cli/cmds/pki/get_org_cert.py
--rw-r--r--   0 nanw       (501) staff       (20)     1220 2023-04-06 22:12:04.000000 hcs-cli-0.1.20/vhcs/cli/cmds/pki/sign-resource-cert.py
--rw-r--r--   0 nanw       (501) staff       (20)      154 2023-04-06 22:12:12.000000 hcs-cli-0.1.20/vhcs/cli/cmds/pki/test.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.203512 hcs-cli-0.1.20/vhcs/cli/cmds/profile/
--rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/cli/cmds/profile/__init__.py
--rw-r--r--   0 nanw       (501) staff       (20)     3765 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/cli/cmds/profile/init.py
--rw-r--r--   0 nanw       (501) staff       (20)      213 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/cli/cmds/upgrade.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.221691 hcs-cli-0.1.20/vhcs/cli/cmds/vmhub/
--rw-r--r--   0 nanw       (501) staff       (20)       33 2023-04-06 17:42:33.000000 hcs-cli-0.1.20/vhcs/cli/cmds/vmhub/__init__.py
--rw-r--r--   0 nanw       (501) staff       (20)      748 2023-04-06 22:12:30.000000 hcs-cli-0.1.20/vhcs/cli/cmds/vmhub/redeem-otp.py
--rw-r--r--   0 nanw       (501) staff       (20)      616 2023-04-06 22:12:37.000000 hcs-cli-0.1.20/vhcs/cli/cmds/vmhub/request-otp.py
--rw-r--r--   0 nanw       (501) staff       (20)      158 2023-04-06 22:12:43.000000 hcs-cli-0.1.20/vhcs/cli/cmds/vmhub/test.py
--rwxr-xr-x   0 nanw       (501) staff       (20)     1068 2023-04-06 20:42:36.000000 hcs-cli-0.1.20/vhcs/cli/main.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.223580 hcs-cli-0.1.20/vhcs/common/
--rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/__init__.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.266086 hcs-cli-0.1.20/vhcs/common/ctxp/
--rw-r--r--   0 nanw       (501) staff       (20)     1839 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/README.md
--rw-r--r--   0 nanw       (501) staff       (20)      152 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/__init__.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.277873 hcs-cli-0.1.20/vhcs/common/ctxp/built_in_cmds/
--rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/built_in_cmds/__init__.py
--rw-r--r--   0 nanw       (501) staff       (20)     1258 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/built_in_cmds/context.py
--rw-r--r--   0 nanw       (501) staff       (20)     1302 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/built_in_cmds/profile.py
--rw-r--r--   0 nanw       (501) staff       (20)     3407 2023-04-06 22:00:23.000000 hcs-cli-0.1.20/vhcs/common/ctxp/cli_processor.py
--rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/cli_state.py
--rw-r--r--   0 nanw       (501) staff       (20)      398 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/config.py
--rw-r--r--   0 nanw       (501) staff       (20)     1706 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/context.py
--rw-r--r--   0 nanw       (501) staff       (20)     5681 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/fstore.py
--rw-r--r--   0 nanw       (501) staff       (20)      473 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/init.py
--rw-r--r--   0 nanw       (501) staff       (20)     2128 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/jsondot.py
--rw-r--r--   0 nanw       (501) staff       (20)       55 2023-04-06 21:51:19.000000 hcs-cli-0.1.20/vhcs/common/ctxp/lazy_group.py
--rw-r--r--   0 nanw       (501) staff       (20)     4008 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/logutil.py
--rw-r--r--   0 nanw       (501) staff       (20)     3702 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/profile.py
--rw-r--r--   0 nanw       (501) staff       (20)      915 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/util.py
--rw-r--r--   0 nanw       (501) staff       (20)     2666 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/ctxp/var_template.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.298289 hcs-cli-0.1.20/vhcs/common/sglib/
--rw-r--r--   0 nanw       (501) staff       (20)       54 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/sglib/__init__.py
--rw-r--r--   0 nanw       (501) staff       (20)     2492 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/sglib/auth.py
--rw-r--r--   0 nanw       (501) staff       (20)     3589 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/sglib/csp.py
--rw-r--r--   0 nanw       (501) staff       (20)     3793 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/sglib/ez_client.py
--rw-r--r--   0 nanw       (501) staff       (20)      500 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/sglib/hcs_client.py
--rw-r--r--   0 nanw       (501) staff       (20)      358 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/common/sglib/util.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.308992 hcs-cli-0.1.20/vhcs/config/
--rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/config/__init__.py
--rw-r--r--   0 nanw       (501) staff       (20)     7327 2023-04-06 17:22:27.000000 hcs-cli-0.1.20/vhcs/config/hcs-deployments.yaml
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.324244 hcs-cli-0.1.20/vhcs/service/
--rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/service/__init__.py
--rw-r--r--   0 nanw       (501) staff       (20)     2138 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/service/lcm.py
--rw-r--r--   0 nanw       (501) staff       (20)      790 2023-04-06 22:13:28.000000 hcs-cli-0.1.20/vhcs/service/pki.py
--rw-r--r--   0 nanw       (501) staff       (20)     1545 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/service/vmhub.py
-drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 22:15:29.332459 hcs-cli-0.1.20/vhcs/util/
--rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/util/__init__.py
--rw-r--r--   0 nanw       (501) staff       (20)     4699 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/util/pki_util.py
--rw-r--r--   0 nanw       (501) staff       (20)      221 2023-04-06 02:05:21.000000 hcs-cli-0.1.20/vhcs/util/shell.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.069747 hcs-cli-0.1.8/
+-rw-r--r--   0 nanw       (501) staff       (20)      150 2023-04-06 01:53:41.069302 hcs-cli-0.1.8/PKG-INFO
+-rw-r--r--   0 nanw       (501) staff       (20)      497 2023-04-06 00:54:00.000000 hcs-cli-0.1.8/README.md
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.012883 hcs-cli-0.1.8/hcs_cli.egg-info/
+-rw-r--r--   0 nanw       (501) staff       (20)      150 2023-04-06 01:53:40.000000 hcs-cli-0.1.8/hcs_cli.egg-info/PKG-INFO
+-rw-r--r--   0 nanw       (501) staff       (20)     2109 2023-04-06 01:53:40.000000 hcs-cli-0.1.8/hcs_cli.egg-info/SOURCES.txt
+-rw-r--r--   0 nanw       (501) staff       (20)        1 2023-04-06 01:53:40.000000 hcs-cli-0.1.8/hcs_cli.egg-info/dependency_links.txt
+-rw-r--r--   0 nanw       (501) staff       (20)       42 2023-04-06 01:53:40.000000 hcs-cli-0.1.8/hcs_cli.egg-info/entry_points.txt
+-rw-r--r--   0 nanw       (501) staff       (20)      105 2023-04-06 01:53:40.000000 hcs-cli-0.1.8/hcs_cli.egg-info/requires.txt
+-rw-r--r--   0 nanw       (501) staff       (20)        5 2023-04-06 01:53:40.000000 hcs-cli-0.1.8/hcs_cli.egg-info/top_level.txt
+-rw-r--r--   0 nanw       (501) staff       (20)      297 2023-01-11 22:10:27.000000 hcs-cli-0.1.8/pyproject.toml
+-rw-r--r--   0 nanw       (501) staff       (20)       38 2023-04-06 01:53:41.069862 hcs-cli-0.1.8/setup.cfg
+-rw-r--r--   0 nanw       (501) staff       (20)      625 2023-04-06 01:53:20.000000 hcs-cli-0.1.8/setup.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.013777 hcs-cli-0.1.8/vhcs/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 01:41:05.000000 hcs-cli-0.1.8/vhcs/__init__.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.015123 hcs-cli-0.1.8/vhcs/cli/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 00:22:16.000000 hcs-cli-0.1.8/vhcs/cli/__init__.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.017819 hcs-cli-0.1.8/vhcs/cli/cmds/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 00:22:19.000000 hcs-cli-0.1.8/vhcs/cli/cmds/__init__.py
+-rw-r--r--   0 nanw       (501) staff       (20)      486 2023-04-06 01:28:45.000000 hcs-cli-0.1.8/vhcs/cli/cmds/auth.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.021094 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 01:41:52.000000 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/__init__.py
+-rw-r--r--   0 nanw       (501) staff       (20)       27 2023-04-06 01:21:03.000000 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/meta.yaml
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.024633 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/provider/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 01:48:57.000000 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/provider/__init__.py
+-rw-r--r--   0 nanw       (501) staff       (20)      310 2023-04-06 01:28:44.000000 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/provider/delete.py
+-rw-r--r--   0 nanw       (501) staff       (20)      301 2023-04-06 01:28:44.000000 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/provider/get.py
+-rw-r--r--   0 nanw       (501) staff       (20)      241 2023-04-06 01:28:44.000000 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/provider/list.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.028630 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/template/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 01:48:55.000000 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/template/__init__.py
+-rw-r--r--   0 nanw       (501) staff       (20)      776 2023-04-06 01:28:44.000000 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/template/create.py
+-rw-r--r--   0 nanw       (501) staff       (20)      466 2023-04-06 01:28:44.000000 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/template/delete.py
+-rw-r--r--   0 nanw       (501) staff       (20)      301 2023-04-06 01:28:44.000000 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/template/get.py
+-rw-r--r--   0 nanw       (501) staff       (20)      241 2023-04-06 01:28:44.000000 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/template/list.py
+-rw-r--r--   0 nanw       (501) staff       (20)      170 2023-04-06 01:28:44.000000 hcs-cli-0.1.8/vhcs/cli/cmds/lcm/test.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.035617 hcs-cli-0.1.8/vhcs/cli/cmds/pki/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 01:41:50.000000 hcs-cli-0.1.8/vhcs/cli/cmds/pki/__init__.py
+-rw-r--r--   0 nanw       (501) staff       (20)      639 2023-04-06 01:28:46.000000 hcs-cli-0.1.8/vhcs/cli/cmds/pki/delete-org-cert.py
+-rw-r--r--   0 nanw       (501) staff       (20)      278 2023-04-06 01:28:46.000000 hcs-cli-0.1.8/vhcs/cli/cmds/pki/get-root-ca.py
+-rw-r--r--   0 nanw       (501) staff       (20)      414 2023-04-06 01:28:46.000000 hcs-cli-0.1.8/vhcs/cli/cmds/pki/get_org_cert.py
+-rw-r--r--   0 nanw       (501) staff       (20)       27 2023-04-06 01:21:13.000000 hcs-cli-0.1.8/vhcs/cli/cmds/pki/meta.yaml
+-rw-r--r--   0 nanw       (501) staff       (20)     1236 2023-04-06 01:28:46.000000 hcs-cli-0.1.8/vhcs/cli/cmds/pki/sign-resource-cert.py
+-rw-r--r--   0 nanw       (501) staff       (20)      170 2023-04-06 01:28:44.000000 hcs-cli-0.1.8/vhcs/cli/cmds/pki/test.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.037333 hcs-cli-0.1.8/vhcs/cli/cmds/profile/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 01:41:49.000000 hcs-cli-0.1.8/vhcs/cli/cmds/profile/__init__.py
+-rw-r--r--   0 nanw       (501) staff       (20)     3765 2023-04-06 01:28:45.000000 hcs-cli-0.1.8/vhcs/cli/cmds/profile/init.py
+-rw-r--r--   0 nanw       (501) staff       (20)      213 2023-04-06 01:32:08.000000 hcs-cli-0.1.8/vhcs/cli/cmds/upgrade.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.041814 hcs-cli-0.1.8/vhcs/cli/cmds/vmhub/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 01:41:46.000000 hcs-cli-0.1.8/vhcs/cli/cmds/vmhub/__init__.py
+-rw-r--r--   0 nanw       (501) staff       (20)       29 2023-04-06 01:21:24.000000 hcs-cli-0.1.8/vhcs/cli/cmds/vmhub/meta.yaml
+-rw-r--r--   0 nanw       (501) staff       (20)      767 2023-04-06 01:28:44.000000 hcs-cli-0.1.8/vhcs/cli/cmds/vmhub/redeem-otp.py
+-rw-r--r--   0 nanw       (501) staff       (20)      635 2023-04-06 01:28:44.000000 hcs-cli-0.1.8/vhcs/cli/cmds/vmhub/request-otp.py
+-rw-r--r--   0 nanw       (501) staff       (20)      176 2023-04-06 01:28:46.000000 hcs-cli-0.1.8/vhcs/cli/cmds/vmhub/test.py
+-rwxr-xr-x   0 nanw       (501) staff       (20)     1002 2023-04-06 01:28:45.000000 hcs-cli-0.1.8/vhcs/cli/main.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.042953 hcs-cli-0.1.8/vhcs/common/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 00:22:13.000000 hcs-cli-0.1.8/vhcs/common/__init__.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.052588 hcs-cli-0.1.8/vhcs/common/ctxp/
+-rw-r--r--   0 nanw       (501) staff       (20)      152 2023-01-11 23:02:40.000000 hcs-cli-0.1.8/vhcs/common/ctxp/__init__.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.055302 hcs-cli-0.1.8/vhcs/common/ctxp/built_in_cmds/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 00:37:37.000000 hcs-cli-0.1.8/vhcs/common/ctxp/built_in_cmds/__init__.py
+-rw-r--r--   0 nanw       (501) staff       (20)     1258 2023-04-06 01:28:46.000000 hcs-cli-0.1.8/vhcs/common/ctxp/built_in_cmds/context.py
+-rw-r--r--   0 nanw       (501) staff       (20)     1302 2023-04-06 01:28:45.000000 hcs-cli-0.1.8/vhcs/common/ctxp/built_in_cmds/profile.py
+-rw-r--r--   0 nanw       (501) staff       (20)     2901 2023-04-06 01:52:59.000000 hcs-cli-0.1.8/vhcs/common/ctxp/cli_processor.py
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-01-20 23:17:41.000000 hcs-cli-0.1.8/vhcs/common/ctxp/cli_state.py
+-rw-r--r--   0 nanw       (501) staff       (20)      398 2023-01-11 23:02:40.000000 hcs-cli-0.1.8/vhcs/common/ctxp/config.py
+-rw-r--r--   0 nanw       (501) staff       (20)     1706 2023-01-11 23:02:40.000000 hcs-cli-0.1.8/vhcs/common/ctxp/context.py
+-rw-r--r--   0 nanw       (501) staff       (20)     5681 2023-04-06 01:32:09.000000 hcs-cli-0.1.8/vhcs/common/ctxp/fstore.py
+-rw-r--r--   0 nanw       (501) staff       (20)      473 2023-04-06 01:32:08.000000 hcs-cli-0.1.8/vhcs/common/ctxp/init.py
+-rw-r--r--   0 nanw       (501) staff       (20)     2128 2023-04-06 01:32:09.000000 hcs-cli-0.1.8/vhcs/common/ctxp/jsondot.py
+-rw-r--r--   0 nanw       (501) staff       (20)     4008 2023-04-06 01:32:09.000000 hcs-cli-0.1.8/vhcs/common/ctxp/logutil.py
+-rw-r--r--   0 nanw       (501) staff       (20)     3702 2023-04-06 01:32:09.000000 hcs-cli-0.1.8/vhcs/common/ctxp/profile.py
+-rw-r--r--   0 nanw       (501) staff       (20)      915 2023-04-06 01:28:45.000000 hcs-cli-0.1.8/vhcs/common/ctxp/util.py
+-rw-r--r--   0 nanw       (501) staff       (20)     2666 2023-01-11 23:02:40.000000 hcs-cli-0.1.8/vhcs/common/ctxp/var_template.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.060524 hcs-cli-0.1.8/vhcs/common/sglib/
+-rw-r--r--   0 nanw       (501) staff       (20)       54 2023-01-11 23:02:40.000000 hcs-cli-0.1.8/vhcs/common/sglib/__init__.py
+-rw-r--r--   0 nanw       (501) staff       (20)     2492 2023-04-06 01:28:47.000000 hcs-cli-0.1.8/vhcs/common/sglib/auth.py
+-rw-r--r--   0 nanw       (501) staff       (20)     3589 2023-04-06 01:28:46.000000 hcs-cli-0.1.8/vhcs/common/sglib/csp.py
+-rw-r--r--   0 nanw       (501) staff       (20)     3793 2023-04-06 01:28:46.000000 hcs-cli-0.1.8/vhcs/common/sglib/ez_client.py
+-rw-r--r--   0 nanw       (501) staff       (20)      500 2023-04-06 01:28:46.000000 hcs-cli-0.1.8/vhcs/common/sglib/hcs_client.py
+-rw-r--r--   0 nanw       (501) staff       (20)      358 2023-01-12 04:20:06.000000 hcs-cli-0.1.8/vhcs/common/sglib/util.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.062419 hcs-cli-0.1.8/vhcs/config/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 01:41:22.000000 hcs-cli-0.1.8/vhcs/config/__init__.py
+-rw-r--r--   0 nanw       (501) staff       (20)     7327 2023-01-20 22:06:46.000000 hcs-cli-0.1.8/vhcs/config/hcs-deployments.yaml
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.065644 hcs-cli-0.1.8/vhcs/service_facade/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-01-11 22:10:27.000000 hcs-cli-0.1.8/vhcs/service_facade/__init__.py
+-rw-r--r--   0 nanw       (501) staff       (20)     2138 2023-04-06 01:28:46.000000 hcs-cli-0.1.8/vhcs/service_facade/lcm.py
+-rw-r--r--   0 nanw       (501) staff       (20)      804 2023-04-06 01:28:45.000000 hcs-cli-0.1.8/vhcs/service_facade/pki.py
+-rw-r--r--   0 nanw       (501) staff       (20)     1545 2023-04-06 01:28:45.000000 hcs-cli-0.1.8/vhcs/service_facade/vmhub.py
+drwxr-xr-x   0 nanw       (501) staff       (20)        0 2023-04-06 01:53:41.068543 hcs-cli-0.1.8/vhcs/util/
+-rw-r--r--   0 nanw       (501) staff       (20)        0 2023-04-06 01:41:21.000000 hcs-cli-0.1.8/vhcs/util/__init__.py
+-rw-r--r--   0 nanw       (501) staff       (20)     4699 2023-04-06 01:32:09.000000 hcs-cli-0.1.8/vhcs/util/pki_util.py
+-rw-r--r--   0 nanw       (501) staff       (20)      195 2023-04-06 01:32:08.000000 hcs-cli-0.1.8/vhcs/util/shell.py
```

### Comparing `hcs-cli-0.1.20/hcs_cli.egg-info/SOURCES.txt` & `hcs-cli-0.1.8/hcs_cli.egg-info/SOURCES.txt`

 * *Files 7% similar despite different names*

```diff
@@ -1,58 +1,57 @@
-.gitignore
 README.md
 pyproject.toml
-requirements.txt
 setup.py
 hcs_cli.egg-info/PKG-INFO
 hcs_cli.egg-info/SOURCES.txt
 hcs_cli.egg-info/dependency_links.txt
 hcs_cli.egg-info/entry_points.txt
 hcs_cli.egg-info/requires.txt
 hcs_cli.egg-info/top_level.txt
 vhcs/__init__.py
 vhcs/cli/__init__.py
 vhcs/cli/main.py
 vhcs/cli/cmds/__init__.py
 vhcs/cli/cmds/auth.py
 vhcs/cli/cmds/upgrade.py
 vhcs/cli/cmds/lcm/__init__.py
+vhcs/cli/cmds/lcm/meta.yaml
 vhcs/cli/cmds/lcm/test.py
 vhcs/cli/cmds/lcm/provider/__init__.py
 vhcs/cli/cmds/lcm/provider/delete.py
 vhcs/cli/cmds/lcm/provider/get.py
 vhcs/cli/cmds/lcm/provider/list.py
 vhcs/cli/cmds/lcm/template/__init__.py
 vhcs/cli/cmds/lcm/template/create.py
 vhcs/cli/cmds/lcm/template/delete.py
 vhcs/cli/cmds/lcm/template/get.py
 vhcs/cli/cmds/lcm/template/list.py
 vhcs/cli/cmds/pki/__init__.py
 vhcs/cli/cmds/pki/delete-org-cert.py
 vhcs/cli/cmds/pki/get-root-ca.py
 vhcs/cli/cmds/pki/get_org_cert.py
+vhcs/cli/cmds/pki/meta.yaml
 vhcs/cli/cmds/pki/sign-resource-cert.py
 vhcs/cli/cmds/pki/test.py
 vhcs/cli/cmds/profile/__init__.py
 vhcs/cli/cmds/profile/init.py
 vhcs/cli/cmds/vmhub/__init__.py
+vhcs/cli/cmds/vmhub/meta.yaml
 vhcs/cli/cmds/vmhub/redeem-otp.py
 vhcs/cli/cmds/vmhub/request-otp.py
 vhcs/cli/cmds/vmhub/test.py
 vhcs/common/__init__.py
-vhcs/common/ctxp/README.md
 vhcs/common/ctxp/__init__.py
 vhcs/common/ctxp/cli_processor.py
 vhcs/common/ctxp/cli_state.py
 vhcs/common/ctxp/config.py
 vhcs/common/ctxp/context.py
 vhcs/common/ctxp/fstore.py
 vhcs/common/ctxp/init.py
 vhcs/common/ctxp/jsondot.py
-vhcs/common/ctxp/lazy_group.py
 vhcs/common/ctxp/logutil.py
 vhcs/common/ctxp/profile.py
 vhcs/common/ctxp/util.py
 vhcs/common/ctxp/var_template.py
 vhcs/common/ctxp/built_in_cmds/__init__.py
 vhcs/common/ctxp/built_in_cmds/context.py
 vhcs/common/ctxp/built_in_cmds/profile.py
@@ -60,14 +59,14 @@
 vhcs/common/sglib/auth.py
 vhcs/common/sglib/csp.py
 vhcs/common/sglib/ez_client.py
 vhcs/common/sglib/hcs_client.py
 vhcs/common/sglib/util.py
 vhcs/config/__init__.py
 vhcs/config/hcs-deployments.yaml
-vhcs/service/__init__.py
-vhcs/service/lcm.py
-vhcs/service/pki.py
-vhcs/service/vmhub.py
+vhcs/service_facade/__init__.py
+vhcs/service_facade/lcm.py
+vhcs/service_facade/pki.py
+vhcs/service_facade/vmhub.py
 vhcs/util/__init__.py
 vhcs/util/pki_util.py
 vhcs/util/shell.py
```

### Comparing `hcs-cli-0.1.20/setup.py` & `hcs-cli-0.1.8/setup.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,34 +1,27 @@
 from setuptools import setup, find_packages
 
-from setuptools_scm import get_version
-import os
-
-with open("requirements.txt") as f:
-    requirements = f.read().splitlines()
-
-
-def get_version():
-    version = "0.1.20"
-    local_version = os.environ.get("SCM_REV")
-    if local_version:
-        version += "+" + local_version
-    return version
-
-
 setup(
     name="hcs-cli",
-    version=get_version(),
+    version="0.1.8",
     author="Nan Wang",
     author_email="nanw1103@gmail.com",
     description="A CLI command for Horizon Cloud Service",
     packages=find_packages(),
-    install_requires=requirements,
+    install_requires=[
+        "click==8.1.3",
+        "cryptography==40.0.1",
+        "httpx==0.23.3",
+        "PyJWT==2.6.0",
+        "pyOpenSSL==23.1.1",
+        "PyYAML==6.0",
+        "black==23.3.0",
+    ],
     entry_points="""
         [console_scripts]
         hcs=vhcs.cli.main:cli
     """,
     package_data={
-        "": ["*.yaml"],
+        '': ['*.yaml'],
     },
     include_package_data=True,
 )
```

### Comparing `hcs-cli-0.1.20/vhcs/cli/cmds/lcm/template/create.py` & `hcs-cli-0.1.8/vhcs/cli/cmds/lcm/template/create.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from sys import stdin
 import click
 from vhcs.common.ctxp import option_output, show
-from vhcs.service import lcm
+from vhcs.service_facade import lcm as _lcm
 
 
 @click.command()
 @click.option(
     "--file",
     "-f",
     type=click.File("r"),
@@ -20,9 +20,9 @@
     # if file:
     #     with open(file, "r", encoding="utf-8") as file:
     #         payload = file.read()
     # else:
     #     payload = stdin.read()
     with file:
         payload = file.read()
-    ret = lcm.template.create(payload, type)
+    ret = _lcm.template.create(payload, type)
     show(ret, output)
```

### Comparing `hcs-cli-0.1.20/vhcs/cli/cmds/pki/delete-org-cert.py` & `hcs-cli-0.1.8/vhcs/cli/cmds/pki/delete-org-cert.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 import click
 from vhcs.common.ctxp import option_output, show, panic
-from vhcs.service import pki
+from vhcs.service_facade import pki as _pki
 from vhcs.common.sglib.util import option_org_id, get_org_id
 
 
 @click.command()
 @option_org_id
 @click.option("--confirm/--no-confirm", default=False)
 @option_output
 def delete_org_cert(org: str, confirm: bool, output: str):
     """Delete the signing certificate of a specific org"""
 
     if not confirm:
         panic('Delete an org certificate will impact some service. Specify "--confirm" to perform the deletion.')
     org_id = get_org_id(org)
-    ret = pki.delete_org_cert(org_id)
+    ret = _pki.delete_org_cert(org_id)
     show(ret, output)
```

### Comparing `hcs-cli-0.1.20/vhcs/cli/cmds/pki/sign-resource-cert.py` & `hcs-cli-0.1.8/vhcs/cli/cmds/pki/sign-resource-cert.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 import click
 from vhcs.common.ctxp import profile
-from vhcs.service import pki
+from vhcs.service_facade import pki as _pki
 from vhcs.util import pki_util
 from vhcs.common.sglib.util import option_org_id, get_org_id
 
 
 def _write_file(file_path: str, text: str):
     with open(file_path, "w") as file:
         file.write(text)
@@ -20,15 +20,15 @@
     help="Private key length",
 )
 @option_org_id
 def sign_resource_cert(resource_name: str, key_length: int, org: str):
     """Get the certificate for a specific resource"""
     org_id = get_org_id(org)
     csr_pem, private_key_pem = pki_util.generate_CSR(resource_name, key_length=key_length)
-    ret = pki.sign_resource_cert(org_id, csr_pem)
+    ret = _pki.sign_resource_cert(org_id, csr_pem)
 
     long_name = f"{profile.name()}-{org_id}-{resource_name}"
     key_file = resource_name + ".key"
     print("Private key (generated by CLI): " + key_file)
     _write_file(key_file, private_key_pem)
 
     client_cert_chain_file = long_name + ".crt"
```

### Comparing `hcs-cli-0.1.20/vhcs/cli/cmds/profile/init.py` & `hcs-cli-0.1.8/vhcs/cli/cmds/profile/init.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/cli/cmds/vmhub/redeem-otp.py` & `hcs-cli-0.1.8/vhcs/cli/cmds/vmhub/redeem-otp.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 import click
 from vhcs.common.ctxp import option_output, show
-from vhcs.service import vmhub
+from vhcs.service_facade import vmhub as _vmhub
 from vhcs.util import pki_util
 
 
 @click.command()
 @click.option(
     "--region",
     type=str,
@@ -14,13 +14,13 @@
 )
 @click.argument("resource-name", type=str, required=True)
 @click.argument("otp", type=str, required=True)
 @option_output
 def redeem_otp(region: str, resource_name: str, otp: str, output: str):
     """Redeem OTP with CSR, receive resource cert."""
 
-    vmhub.use_region(region)
+    _vmhub.use_region(region)
     csr_pem, private_key_pem = pki_util.generate_CSR(resource_name)
 
-    ret = vmhub.redeem_otp(resource_name, otp, csr_pem)
+    ret = _vmhub.redeem_otp(resource_name, otp, csr_pem)
     ret.private_key = private_key_pem
     show(ret, output)
```

### Comparing `hcs-cli-0.1.20/vhcs/cli/cmds/vmhub/request-otp.py` & `hcs-cli-0.1.8/vhcs/cli/cmds/vmhub/request-otp.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import click
 from vhcs.common.ctxp import show
 from vhcs.common.sglib.util import option_org_id, get_org_id
-from vhcs.service import vmhub
+from vhcs.service_facade import vmhub as _vmhub
 
 
 @click.command()
 @option_org_id
 @click.option(
     "--region",
     type=str,
@@ -13,10 +13,10 @@
     required=False,
     help="Specify region name",
 )
 @click.argument("resource-name", type=str, required=True)
 def request_otp(org: str, region: str, resource_name: str):
     """Request an one-time password for a specific resource"""
     org_id = get_org_id(org)
-    vmhub.use_region(region)
-    ret = vmhub.request_otp(org_id, resource_name)
+    _vmhub.use_region(region)
+    ret = _vmhub.request_otp(org_id, resource_name)
     show(ret)
```

### Comparing `hcs-cli-0.1.20/vhcs/cli/main.py` & `hcs-cli-0.1.8/vhcs/cli/main.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,16 +1,15 @@
 #!/usr/bin/env -S python3 -W ignore
 
 import sys
 import logging
 import os.path as path
 
 _script_dir = path.abspath(path.join(path.dirname(path.realpath(__file__)), "."))
-_module_dir = path.dirname(_script_dir)
-_cli_dir = path.dirname(_module_dir)
+_cli_dir = path.dirname(_script_dir)
 sys.path.append(_cli_dir)
 
 import vhcs.common.ctxp as ctxp
 
 # -----------------------------------------------------------
 # Setup logger
 ctxp.logutil.setup()
@@ -20,17 +19,16 @@
 logging.getLogger("init").setLevel(logging.WARN)
 logging.getLogger("profile").setLevel(logging.WARN)
 # -----------------------------------------------------------
 
 
 def cli():
     try:
-        commands_dir = path.join(_module_dir, "cli/cmds")
-        config_path = path.join(_module_dir, "config")
+        commands_dir = path.join(_cli_dir, "cli/cmds")
+        config_path = path.join(_cli_dir, "config")
         ctxp.init(cli_name="hcs", commands_dir=commands_dir, config_path=config_path)
     except ctxp.CtxpException as e:
         ctxp.panic(e)
 
 
 if __name__ == "__main__":
-    print(sys.argv)
     cli()
```

### Comparing `hcs-cli-0.1.20/vhcs/common/ctxp/built_in_cmds/context.py` & `hcs-cli-0.1.8/vhcs/common/ctxp/built_in_cmds/context.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/common/ctxp/built_in_cmds/profile.py` & `hcs-cli-0.1.8/vhcs/common/ctxp/built_in_cmds/profile.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/common/ctxp/cli_processor.py` & `hcs-cli-0.1.8/vhcs/common/ctxp/cli_processor.py`

 * *Files 14% similar despite different names*

```diff
@@ -18,78 +18,62 @@
 
 
 @_cli.result_callback()
 def _process_result(result, **kwargs):
     pass
 
 
-class LazyGroup(click.Group):
-    def __init__(self, mod_path: Path, *args, **kwargs):
-        super().__init__(*args, **kwargs)
-        self.mod_path = mod_path
-
-    def list_commands(self, ctx):
-        self._lazy_ensure_subcommands()
-        return super().list_commands(ctx)
-
-    def get_command(self, ctx, cmd_name):
-        self._lazy_ensure_subcommands()
-        return super().get_command(ctx, cmd_name)
-
-    def _lazy_ensure_subcommands(self):
-        if not self.commands:
-            _add_subcommands(self.mod_path.absolute(), self)
-
-
 def _add_built_in_commands(group: Group):
     script_dir = path.abspath(path.join(path.dirname(path.realpath(__file__)), "."))
     build_in_cmds_dir = path.join(script_dir, "built_in_cmds")
     _add_subcommands(build_in_cmds_dir, group)
 
 
-def _ensure_sub_group(current: Group, mod_path: Path):
-    name = mod_path.name
-    help = _read_group_meta(mod_path).get("help")
+def _create_group(current: Group, name: str, help: str):
     subgroup = current.commands.get(name)
     if subgroup and isinstance(subgroup, Group):
         return subgroup
 
-    subgroup = LazyGroup(name=name, help=help, mod_path=mod_path)
+    subgroup = click.core.Group(name=name, help=help)
     current.add_command(subgroup)
     return subgroup
 
 
 def _read_group_meta(mod_path: Path) -> dict:
     meta_file = mod_path.absolute().joinpath("meta.yaml")
     if not meta_file.exists():
         return {}
     with open(meta_file, "r") as f:
         return yaml.safe_load(f)
 
-
-_excluded_names = ["__pycache__", "__init__.py", ".DS_Store"]
-
+_excluded_names = [
+    "__pycache__",
+    "__init__.py",
+    "meta.yaml",
+    ".DS_Store"
+]
 
 def _add_subcommands(commands_dir: str, group: Group):
     for mod_path in Path(commands_dir).glob("*"):
         if mod_path.name in _excluded_names:
             continue
         if mod_path.is_dir():
-            _ensure_sub_group(group, mod_path)
+            help = _read_group_meta(mod_path).get("help")
+            subgroup = _create_group(group, mod_path.name, help)
+            _add_subcommands(mod_path.absolute(), subgroup)
         elif mod_path.name.endswith(".py"):
             _import_cmd_file(mod_path, group)
         else:
             pass
-            # print("Unrecognized sub cmd: " + mod_path.name)
+            #print("Unrecognized sub cmd: " + mod_path.name)
     return
 
 
 def _import_cmd_file(mod_path: Path, parent: click.core.Group):
     mod_name = f"ctxp#{mod_path}"
-    # print("Loading ---> ", mod_name)
 
     spec = importlib.util.spec_from_file_location(mod_name, mod_path)
     mod = importlib.util.module_from_spec(spec)
     spec.loader.exec_module(mod)
 
     # mod = importlib.import_module(mod_name)
     # filter out any things that aren't a click Command
```

### Comparing `hcs-cli-0.1.20/vhcs/common/ctxp/context.py` & `hcs-cli-0.1.8/vhcs/common/ctxp/context.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/common/ctxp/fstore.py` & `hcs-cli-0.1.8/vhcs/common/ctxp/fstore.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/common/ctxp/jsondot.py` & `hcs-cli-0.1.8/vhcs/common/ctxp/jsondot.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/common/ctxp/logutil.py` & `hcs-cli-0.1.8/vhcs/common/ctxp/logutil.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/common/ctxp/profile.py` & `hcs-cli-0.1.8/vhcs/common/ctxp/profile.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/common/ctxp/util.py` & `hcs-cli-0.1.8/vhcs/common/ctxp/util.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/common/ctxp/var_template.py` & `hcs-cli-0.1.8/vhcs/common/ctxp/var_template.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/common/sglib/auth.py` & `hcs-cli-0.1.8/vhcs/common/sglib/auth.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/common/sglib/csp.py` & `hcs-cli-0.1.8/vhcs/common/sglib/csp.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/common/sglib/ez_client.py` & `hcs-cli-0.1.8/vhcs/common/sglib/ez_client.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/config/hcs-deployments.yaml` & `hcs-cli-0.1.8/vhcs/config/hcs-deployments.yaml`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/service/lcm.py` & `hcs-cli-0.1.8/vhcs/service_facade/lcm.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/service/pki.py` & `hcs-cli-0.1.8/vhcs/service_facade/pki.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,7 +1,8 @@
+import base64
 from vhcs.common.ctxp import profile
 from vhcs.common.sglib import hcs_client
 
 
 def _client():
     url = profile.current().hcs.url
     if not url.endswith("/"):
```

### Comparing `hcs-cli-0.1.20/vhcs/service/vmhub.py` & `hcs-cli-0.1.8/vhcs/service_facade/vmhub.py`

 * *Files identical despite different names*

### Comparing `hcs-cli-0.1.20/vhcs/util/pki_util.py` & `hcs-cli-0.1.8/vhcs/util/pki_util.py`

 * *Files identical despite different names*

