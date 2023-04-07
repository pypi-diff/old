# Comparing `tmp/policyengine-api-1.0.0.tar.gz` & `tmp/policyengine-api-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "policyengine-api-1.0.0.tar", last modified: Fri Apr  7 09:22:18 2023, max compression
+gzip compressed data, was "policyengine-api-1.0.1.tar", last modified: Fri Apr  7 12:08:21 2023, max compression
```

## Comparing `policyengine-api-1.0.0.tar` & `policyengine-api-1.0.1.tar`

### file list

```diff
@@ -1,68 +1,78 @@
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.298777 policyengine-api-1.0.0/
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.292861 policyengine-api-1.0.0/.github/
--rw-r--r--   0 nikhil     (501) staff       (20)      267 2022-12-19 15:37:36.000000 policyengine-api-1.0.0/.github/changelog_template.md
--rwxr-xr-x   0 nikhil     (501) staff       (20)      122 2022-12-19 15:37:36.000000 policyengine-api-1.0.0/.github/get-changelog-diff.sh
--rwxr-xr-x   0 nikhil     (501) staff       (20)      642 2022-12-19 15:37:36.000000 policyengine-api-1.0.0/.github/has-functional-changes.sh
--rwxr-xr-x   0 nikhil     (501) staff       (20)     1013 2022-12-19 15:37:36.000000 policyengine-api-1.0.0/.github/is-version-number-acceptable.sh
--rwxr-xr-x   0 nikhil     (501) staff       (20)      115 2022-12-19 15:37:36.000000 policyengine-api-1.0.0/.github/publish-git-tag.sh
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.293139 policyengine-api-1.0.0/.github/workflows/
--rw-r--r--   0 nikhil     (501) staff       (20)     2048 2023-03-28 23:54:13.000000 policyengine-api-1.0.0/.github/workflows/pr.yml
--rw-r--r--   0 nikhil     (501) staff       (20)     3411 2023-03-28 23:54:32.000000 policyengine-api-1.0.0/.github/workflows/push.yml
--rw-r--r--   0 nikhil     (501) staff       (20)      142 2023-04-06 09:46:03.000000 policyengine-api-1.0.0/.gitignore
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.293273 policyengine-api-1.0.0/.vscode/
--rw-r--r--   0 nikhil     (501) staff       (20)      692 2022-11-22 22:32:04.000000 policyengine-api-1.0.0/.vscode/launch.json
--rw-r--r--   0 nikhil     (501) staff       (20)    28729 2023-04-04 09:47:38.000000 policyengine-api-1.0.0/CHANGELOG.md
--rw-r--r--   0 nikhil     (501) staff       (20)    34523 2022-12-06 22:08:46.000000 policyengine-api-1.0.0/LICENSE
--rw-r--r--   0 nikhil     (501) staff       (20)     1285 2023-03-22 21:37:20.000000 policyengine-api-1.0.0/Makefile
--rw-r--r--   0 nikhil     (501) staff       (20)      211 2023-04-07 09:22:18.298528 policyengine-api-1.0.0/PKG-INFO
--rw-r--r--   0 nikhil     (501) staff       (20)      229 2023-03-20 18:59:41.000000 policyengine-api-1.0.0/README.md
--rw-r--r--   0 nikhil     (501) staff       (20)    18299 2023-04-04 09:47:38.000000 policyengine-api-1.0.0/changelog.yaml
--rw-r--r--   0 nikhil     (501) staff       (20)        0 2023-04-03 21:42:12.000000 policyengine-api-1.0.0/changelog_entry.yaml
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.293406 policyengine-api-1.0.0/dashboard/
--rw-r--r--   0 nikhil     (501) staff       (20)     1990 2023-01-11 13:17:41.000000 policyengine-api-1.0.0/dashboard/app.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.293673 policyengine-api-1.0.0/dashboard/experiments/
--rw-r--r--   0 nikhil     (501) staff       (20)     4252 2023-04-03 21:42:12.000000 policyengine-api-1.0.0/dashboard/experiments/gpt4_api_user.py
--rw-r--r--   0 nikhil     (501) staff       (20)       41 2023-04-03 21:42:12.000000 policyengine-api-1.0.0/dashboard/experiments/requirements.txt
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.294315 policyengine-api-1.0.0/gcp/
--rw-r--r--   0 nikhil     (501) staff       (20)      640 2023-04-07 09:21:58.000000 policyengine-api-1.0.0/gcp/Dockerfile
--rw-r--r--   0 nikhil     (501) staff       (20)      693 2023-03-25 19:25:34.000000 policyengine-api-1.0.0/gcp/README.md
--rw-r--r--   0 nikhil     (501) staff       (20)     2715 2023-01-20 17:20:59.000000 policyengine-api-1.0.0/gcp/bump_country_package.py
--rw-r--r--   0 nikhil     (501) staff       (20)      133 2022-12-08 00:06:30.000000 policyengine-api-1.0.0/gcp/dispatch.yaml
--rw-r--r--   0 nikhil     (501) staff       (20)     1163 2023-03-28 23:54:13.000000 policyengine-api-1.0.0/gcp/export.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.294582 policyengine-api-1.0.0/gcp/policyengine_api/
--rw-r--r--   0 nikhil     (501) staff       (20)      350 2023-04-07 09:19:01.000000 policyengine-api-1.0.0/gcp/policyengine_api/Dockerfile
--rw-r--r--   0 nikhil     (501) staff       (20)      327 2023-04-07 09:16:29.000000 policyengine-api-1.0.0/gcp/policyengine_api/app.yaml
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.295117 policyengine-api-1.0.0/policyengine_api/
--rw-r--r--   0 nikhil     (501) staff       (20)     1721 2023-04-07 09:15:07.000000 policyengine-api-1.0.0/policyengine_api/api.py
--rw-r--r--   0 nikhil     (501) staff       (20)      611 2023-04-07 09:22:09.000000 policyengine-api-1.0.0/policyengine_api/constants.py
--rw-r--r--   0 nikhil     (501) staff       (20)    17717 2023-04-06 16:41:27.000000 policyengine-api-1.0.0/policyengine_api/country.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.296463 policyengine-api-1.0.0/policyengine_api/data/
--rw-r--r--   0 nikhil     (501) staff       (20)     2003 2023-04-04 11:36:53.000000 policyengine-api-1.0.0/policyengine_api/data/README.md
--rw-r--r--   0 nikhil     (501) staff       (20)       65 2023-04-06 11:50:46.000000 policyengine-api-1.0.0/policyengine_api/data/__init__.py
--rw-r--r--   0 nikhil     (501) staff       (20)     4413 2023-04-06 14:21:15.000000 policyengine-api-1.0.0/policyengine_api/data/data.py
--rw-r--r--   0 nikhil     (501) staff       (20)     1922 2023-04-04 11:36:53.000000 policyengine-api-1.0.0/policyengine_api/data/initialise.sql
--rw-r--r--   0 nikhil     (501) staff       (20)     2043 2023-04-06 16:57:17.000000 policyengine-api-1.0.0/policyengine_api/data/initialise_local.sql
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.297110 policyengine-api-1.0.0/policyengine_api/endpoints/
--rw-r--r--   0 nikhil     (501) staff       (20)      296 2023-04-06 16:50:25.000000 policyengine-api-1.0.0/policyengine_api/endpoints/__init__.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.297989 policyengine-api-1.0.0/policyengine_api/endpoints/economy/
--rw-r--r--   0 nikhil     (501) staff       (20)       40 2023-04-04 22:53:20.000000 policyengine-api-1.0.0/policyengine_api/endpoints/economy/__init__.py
--rw-r--r--   0 nikhil     (501) staff       (20)    13764 2023-04-04 20:02:12.000000 policyengine-api-1.0.0/policyengine_api/endpoints/economy/compare.py
--rw-r--r--   0 nikhil     (501) staff       (20)     5662 2023-04-06 16:56:29.000000 policyengine-api-1.0.0/policyengine_api/endpoints/economy/economy.py
--rw-r--r--   0 nikhil     (501) staff       (20)     8241 2023-04-06 20:27:43.000000 policyengine-api-1.0.0/policyengine_api/endpoints/economy/reform_impact.py
--rw-r--r--   0 nikhil     (501) staff       (20)     5846 2023-04-06 16:41:03.000000 policyengine-api-1.0.0/policyengine_api/endpoints/economy/single_economy.py
--rw-r--r--   0 nikhil     (501) staff       (20)      260 2023-04-04 12:21:57.000000 policyengine-api-1.0.0/policyengine_api/endpoints/home.py
--rw-r--r--   0 nikhil     (501) staff       (20)     7166 2023-04-04 14:34:04.000000 policyengine-api-1.0.0/policyengine_api/endpoints/household.py
--rw-r--r--   0 nikhil     (501) staff       (20)      361 2023-04-04 12:02:24.000000 policyengine-api-1.0.0/policyengine_api/endpoints/metadata.py
--rw-r--r--   0 nikhil     (501) staff       (20)     3686 2023-04-04 12:42:53.000000 policyengine-api-1.0.0/policyengine_api/endpoints/policy.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.298278 policyengine-api-1.0.0/policyengine_api/utils/
--rw-r--r--   0 nikhil     (501) staff       (20)       20 2023-04-04 11:26:24.000000 policyengine-api-1.0.0/policyengine_api/utils/__init__.py
--rw-r--r--   0 nikhil     (501) staff       (20)      979 2023-04-05 09:46:36.000000 policyengine-api-1.0.0/policyengine_api/utils/json.py
--rw-r--r--   0 nikhil     (501) staff       (20)      281 2023-04-07 08:49:36.000000 policyengine-api-1.0.0/policyengine_api/worker.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.295787 policyengine-api-1.0.0/policyengine_api.egg-info/
--rw-r--r--   0 nikhil     (501) staff       (20)      211 2023-04-07 09:22:17.000000 policyengine-api-1.0.0/policyengine_api.egg-info/PKG-INFO
--rw-r--r--   0 nikhil     (501) staff       (20)     1558 2023-04-07 09:22:18.000000 policyengine-api-1.0.0/policyengine_api.egg-info/SOURCES.txt
--rw-r--r--   0 nikhil     (501) staff       (20)        1 2023-04-07 09:22:17.000000 policyengine-api-1.0.0/policyengine_api.egg-info/dependency_links.txt
--rw-r--r--   0 nikhil     (501) staff       (20)      278 2023-04-07 09:22:18.000000 policyengine-api-1.0.0/policyengine_api.egg-info/requires.txt
--rw-r--r--   0 nikhil     (501) staff       (20)        1 2023-04-07 09:22:18.000000 policyengine-api-1.0.0/policyengine_api.egg-info/top_level.txt
--rw-r--r--   0 nikhil     (501) staff       (20)       38 2023-04-07 09:22:18.298832 policyengine-api-1.0.0/setup.cfg
--rw-r--r--   0 nikhil     (501) staff       (20)      790 2023-04-07 09:18:56.000000 policyengine-api-1.0.0/setup.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.998529 policyengine-api-1.0.1/
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.988125 policyengine-api-1.0.1/.github/
+-rw-r--r--   0 nikhil     (501) staff       (20)      267 2022-12-19 15:37:36.000000 policyengine-api-1.0.1/.github/changelog_template.md
+-rwxr-xr-x   0 nikhil     (501) staff       (20)      122 2022-12-19 15:37:36.000000 policyengine-api-1.0.1/.github/get-changelog-diff.sh
+-rwxr-xr-x   0 nikhil     (501) staff       (20)      642 2022-12-19 15:37:36.000000 policyengine-api-1.0.1/.github/has-functional-changes.sh
+-rwxr-xr-x   0 nikhil     (501) staff       (20)     1013 2022-12-19 15:37:36.000000 policyengine-api-1.0.1/.github/is-version-number-acceptable.sh
+-rwxr-xr-x   0 nikhil     (501) staff       (20)      115 2022-12-19 15:37:36.000000 policyengine-api-1.0.1/.github/publish-git-tag.sh
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.988623 policyengine-api-1.0.1/.github/workflows/
+-rw-r--r--   0 nikhil     (501) staff       (20)     1729 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/.github/workflows/pr.yml
+-rw-r--r--   0 nikhil     (501) staff       (20)     2395 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/.github/workflows/push.yml
+-rw-r--r--   0 nikhil     (501) staff       (20)      142 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/.gitignore
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.989002 policyengine-api-1.0.1/.vscode/
+-rw-r--r--   0 nikhil     (501) staff       (20)      692 2022-11-22 22:32:04.000000 policyengine-api-1.0.1/.vscode/launch.json
+-rw-r--r--   0 nikhil     (501) staff       (20)    30179 2023-04-07 12:06:14.000000 policyengine-api-1.0.1/CHANGELOG.md
+-rw-r--r--   0 nikhil     (501) staff       (20)    34523 2022-12-06 22:08:46.000000 policyengine-api-1.0.1/LICENSE
+-rw-r--r--   0 nikhil     (501) staff       (20)      826 2023-04-07 11:35:57.000000 policyengine-api-1.0.1/Makefile
+-rw-r--r--   0 nikhil     (501) staff       (20)      211 2023-04-07 12:08:21.998283 policyengine-api-1.0.1/PKG-INFO
+-rw-r--r--   0 nikhil     (501) staff       (20)      391 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/README.md
+-rw-r--r--   0 nikhil     (501) staff       (20)    19239 2023-04-07 12:06:13.000000 policyengine-api-1.0.1/changelog.yaml
+-rw-r--r--   0 nikhil     (501) staff       (20)        0 2023-04-07 12:06:14.000000 policyengine-api-1.0.1/changelog_entry.yaml
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.989164 policyengine-api-1.0.1/dashboard/
+-rw-r--r--   0 nikhil     (501) staff       (20)     1990 2023-01-11 13:17:41.000000 policyengine-api-1.0.1/dashboard/app.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.989489 policyengine-api-1.0.1/dashboard/experiments/
+-rw-r--r--   0 nikhil     (501) staff       (20)     4252 2023-04-03 21:42:12.000000 policyengine-api-1.0.1/dashboard/experiments/gpt4_api_user.py
+-rw-r--r--   0 nikhil     (501) staff       (20)       41 2023-04-03 21:42:12.000000 policyengine-api-1.0.1/dashboard/experiments/requirements.txt
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.990760 policyengine-api-1.0.1/gcp/
+-rw-r--r--   0 nikhil     (501) staff       (20)      640 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/gcp/Dockerfile
+-rw-r--r--   0 nikhil     (501) staff       (20)      697 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/gcp/README.md
+-rw-r--r--   0 nikhil     (501) staff       (20)     2906 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/gcp/bump_country_package.py
+-rw-r--r--   0 nikhil     (501) staff       (20)      133 2022-12-08 00:06:30.000000 policyengine-api-1.0.1/gcp/dispatch.yaml
+-rw-r--r--   0 nikhil     (501) staff       (20)     1129 2023-04-07 11:37:10.000000 policyengine-api-1.0.1/gcp/export.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.991466 policyengine-api-1.0.1/gcp/policyengine_api/
+-rw-r--r--   0 nikhil     (501) staff       (20)      295 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/gcp/policyengine_api/Dockerfile
+-rw-r--r--   0 nikhil     (501) staff       (20)      358 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/gcp/policyengine_api/app.yaml
+-rw-r--r--   0 nikhil     (501) staff       (20)      177 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/gcp/policyengine_api/start.sh
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.992384 policyengine-api-1.0.1/policyengine_api/
+-rw-r--r--   0 nikhil     (501) staff       (20)     1783 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/api.py
+-rw-r--r--   0 nikhil     (501) staff       (20)      611 2023-04-07 12:06:14.000000 policyengine-api-1.0.1/policyengine_api/constants.py
+-rw-r--r--   0 nikhil     (501) staff       (20)    17718 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/country.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.994545 policyengine-api-1.0.1/policyengine_api/data/
+-rw-r--r--   0 nikhil     (501) staff       (20)     2003 2023-04-04 11:36:53.000000 policyengine-api-1.0.1/policyengine_api/data/README.md
+-rw-r--r--   0 nikhil     (501) staff       (20)       65 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/data/__init__.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     4488 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/data/data.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     1922 2023-04-04 11:36:53.000000 policyengine-api-1.0.1/policyengine_api/data/initialise.sql
+-rw-r--r--   0 nikhil     (501) staff       (20)     2043 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/data/initialise_local.sql
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.995413 policyengine-api-1.0.1/policyengine_api/endpoints/
+-rw-r--r--   0 nikhil     (501) staff       (20)      317 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/endpoints/__init__.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     3229 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/endpoints/analysis.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.996203 policyengine-api-1.0.1/policyengine_api/endpoints/economy/
+-rw-r--r--   0 nikhil     (501) staff       (20)       41 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/endpoints/economy/__init__.py
+-rw-r--r--   0 nikhil     (501) staff       (20)    13764 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/endpoints/economy/compare.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     6275 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/endpoints/economy/economy.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     8300 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/endpoints/economy/reform_impact.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     5846 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/endpoints/economy/single_economy.py
+-rw-r--r--   0 nikhil     (501) staff       (20)      258 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/endpoints/home.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     7379 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/endpoints/household.py
+-rw-r--r--   0 nikhil     (501) staff       (20)      359 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/endpoints/metadata.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     3769 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/endpoints/policy.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.996477 policyengine-api-1.0.1/policyengine_api/utils/
+-rw-r--r--   0 nikhil     (501) staff       (20)       20 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/utils/__init__.py
+-rw-r--r--   0 nikhil     (501) staff       (20)      979 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/utils/json.py
+-rw-r--r--   0 nikhil     (501) staff       (20)      282 2023-04-07 11:35:54.000000 policyengine-api-1.0.1/policyengine_api/worker.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.993431 policyengine-api-1.0.1/policyengine_api.egg-info/
+-rw-r--r--   0 nikhil     (501) staff       (20)      211 2023-04-07 12:08:21.000000 policyengine-api-1.0.1/policyengine_api.egg-info/PKG-INFO
+-rw-r--r--   0 nikhil     (501) staff       (20)     1811 2023-04-07 12:08:21.000000 policyengine-api-1.0.1/policyengine_api.egg-info/SOURCES.txt
+-rw-r--r--   0 nikhil     (501) staff       (20)        1 2023-04-07 12:08:21.000000 policyengine-api-1.0.1/policyengine_api.egg-info/dependency_links.txt
+-rw-r--r--   0 nikhil     (501) staff       (20)      284 2023-04-07 12:08:21.000000 policyengine-api-1.0.1/policyengine_api.egg-info/requires.txt
+-rw-r--r--   0 nikhil     (501) staff       (20)        1 2023-04-07 12:08:21.000000 policyengine-api-1.0.1/policyengine_api.egg-info/top_level.txt
+-rw-r--r--   0 nikhil     (501) staff       (20)       38 2023-04-07 12:08:21.998592 policyengine-api-1.0.1/setup.cfg
+-rw-r--r--   0 nikhil     (501) staff       (20)      807 2023-04-07 12:06:14.000000 policyengine-api-1.0.1/setup.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.985626 policyengine-api-1.0.1/tests/
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 12:08:21.997939 policyengine-api-1.0.1/tests/api/
+-rw-r--r--   0 nikhil     (501) staff       (20)     2332 2023-03-22 20:58:23.000000 policyengine-api-1.0.1/tests/api/test_api.py
+-rw-r--r--   0 nikhil     (501) staff       (20)       54 2022-12-08 00:06:30.000000 policyengine-api-1.0.1/tests/api/test_hello_world.yaml
+-rw-r--r--   0 nikhil     (501) staff       (20)       65 2023-03-23 00:33:05.000000 policyengine-api-1.0.1/tests/api/test_liveness.yaml
+-rw-r--r--   0 nikhil     (501) staff       (20)       67 2023-03-23 00:33:13.000000 policyengine-api-1.0.1/tests/api/test_readiness.yaml
+-rw-r--r--   0 nikhil     (501) staff       (20)      154 2023-03-22 18:03:54.000000 policyengine-api-1.0.1/tests/api/test_uk_baseline_policy.yaml
+-rw-r--r--   0 nikhil     (501) staff       (20)       65 2022-12-08 00:06:30.000000 policyengine-api-1.0.1/tests/api/test_uk_metadata.yaml
```

### Comparing `policyengine-api-1.0.0/.github/has-functional-changes.sh` & `policyengine-api-1.0.1/.github/has-functional-changes.sh`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/.github/is-version-number-acceptable.sh` & `policyengine-api-1.0.1/.github/is-version-number-acceptable.sh`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/.github/workflows/pr.yml` & `policyengine-api-1.0.1/.github/workflows/pr.yml`

 * *Files 25% similar despite different names*

```diff
@@ -49,13 +49,7 @@
         run: make install
       - name: Test the main API
         run: make test
         env:
           POLICYENGINE_DB_PASSWORD: ${{ secrets.POLICYENGINE_DB_PASSWORD }}
           POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN: ${{ secrets.POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN }}
           OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
-      - name: Test the compute API
-        run: make test-compute
-        env:
-          POLICYENGINE_DB_PASSWORD: ${{ secrets.POLICYENGINE_DB_PASSWORD }}
-          POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN: ${{ secrets.POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN }}
-          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

### Comparing `policyengine-api-1.0.0/.github/workflows/push.yml` & `policyengine-api-1.0.1/.github/workflows/push.yml`

 * *Files 18% similar despite different names*

```diff
@@ -61,40 +61,13 @@
       - name: GCP authentication
         uses: 'google-github-actions/auth@v1'
         with:
           credentials_json: '${{ secrets.GCP_SA_KEY }}'
       - name: Set up GCloud
         uses: 'google-github-actions/setup-gcloud@v1'
       - name: Deploy
-        run: make deploy-api
+        run: make deploy
         env:
           POLICYENGINE_DB_PASSWORD: ${{ secrets.POLICYENGINE_DB_PASSWORD }}
           GOOGLE_APPLICATION_CREDENTIALS: ${{ secrets.GCP_SA_KEY }}
           POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN: ${{ secrets.POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN }}
           OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
-  deploy_compute:
-    name: Deploy compute API
-    runs-on: ubuntu-latest
-    if: |
-      (github.repository == 'PolicyEngine/policyengine-api')
-      && (github.event.head_commit.message == 'Update PolicyEngine API')
-    steps:
-      - name: Checkout repo
-        uses: actions/checkout@v2
-      - name: Setup Python
-        uses: actions/setup-python@v2
-        with:
-          python-version: 3.9
-      - name: GCP authentication
-        uses: 'google-github-actions/auth@v1'
-        with:
-          credentials_json: '${{ secrets.GCP_SA_KEY }}'
-      - name: Set up GCloud
-        uses: 'google-github-actions/setup-gcloud@v1'
-      - name: Deploy
-        run: make deploy-compute-api
-        env:
-          POLICYENGINE_DB_PASSWORD: ${{ secrets.POLICYENGINE_DB_PASSWORD }}
-          GOOGLE_APPLICATION_CREDENTIALS: ${{ secrets.GCP_SA_KEY }}
-          POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN: ${{ secrets.POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN }}
-          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
-
```

### Comparing `policyengine-api-1.0.0/.vscode/launch.json` & `policyengine-api-1.0.1/.vscode/launch.json`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/CHANGELOG.md` & `policyengine-api-1.0.1/CHANGELOG.md`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,63 @@
 # Changelog
 
 All notable changes to this project will be documented in this file.
 
 The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), 
 and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
 
+## [1.0.1] - 2023-04-07 13:06:13
+
+### Added
+
+- Added missing `redis` Python dependency.
+
+## [1.0.0] - 2023-04-07 11:34:18
+
+### Changed
+
+- Use redis server workers to process jobs in a more standardised way.
+- Combine main and compute servers into a single server.
+
+## [0.13.25] - 2023-04-06 18:42:39
+
+### Changed
+
+- Bump policyengine-us to 0.278.0
+
+## [0.13.24] - 2023-04-06 14:19:38
+
+### Changed
+
+- Bump policyengine-us to 0.277.0
+
+## [0.13.23] - 2023-04-06 04:17:45
+
+### Changed
+
+- Bump policyengine-canada to 0.45.0
+
+## [0.13.22] - 2023-04-05 17:17:50
+
+### Changed
+
+- Bump policyengine-us to 0.276.0
+
+## [0.13.21] - 2023-04-05 03:28:24
+
+### Changed
+
+- Bump policyengine-us to 0.275.0
+
+## [0.13.20] - 2023-04-04 14:37:18
+
+### Changed
+
+- Bump policyengine-us to 0.273.0
+
 ## [0.13.19] - 2023-04-04 04:49:17
 
 ### Changed
 
 - Bump policyengine-us to 0.271.0
 
 ## [0.13.18] - 2023-04-03 17:43:08
@@ -1026,14 +1075,22 @@
 
 ### Added
 
 - Initial API.
 
 
 
+[1.0.1]: https://github.com/PolicyEngine/policyengine-api/compare/1.0.0...1.0.1
+[1.0.0]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.25...1.0.0
+[0.13.25]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.24...0.13.25
+[0.13.24]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.23...0.13.24
+[0.13.23]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.22...0.13.23
+[0.13.22]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.21...0.13.22
+[0.13.21]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.20...0.13.21
+[0.13.20]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.19...0.13.20
 [0.13.19]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.18...0.13.19
 [0.13.18]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.17...0.13.18
 [0.13.17]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.16...0.13.17
 [0.13.16]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.15...0.13.16
 [0.13.15]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.14...0.13.15
 [0.13.14]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.13...0.13.14
 [0.13.13]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.12...0.13.13
```

### Comparing `policyengine-api-1.0.0/LICENSE` & `policyengine-api-1.0.1/LICENSE`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/changelog.yaml` & `policyengine-api-1.0.1/changelog.yaml`

 * *Files 1% similar despite different names*

```diff
@@ -851,7 +851,48 @@
     - Bump policyengine-us to 0.268.0
   date: 2023-04-03 17:43:08
 - bump: patch
   changes:
     changed:
     - Bump policyengine-us to 0.271.0
   date: 2023-04-04 04:49:17
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.273.0
+  date: 2023-04-04 14:37:18
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.275.0
+  date: 2023-04-05 03:28:24
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.276.0
+  date: 2023-04-05 17:17:50
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-canada to 0.45.0
+  date: 2023-04-06 04:17:45
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.277.0
+  date: 2023-04-06 14:19:38
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.278.0
+  date: 2023-04-06 18:42:39
+- bump: major
+  changes:
+    changed:
+    - Use redis server workers to process jobs in a more standardised way.
+    - Combine main and compute servers into a single server.
+  date: 2023-04-07 11:34:18
+- bump: patch
+  changes:
+    added:
+    - Added missing `redis` Python dependency.
+  date: 2023-04-07 13:06:13
```

### Comparing `policyengine-api-1.0.0/dashboard/app.py` & `policyengine-api-1.0.1/dashboard/app.py`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/dashboard/experiments/gpt4_api_user.py` & `policyengine-api-1.0.1/dashboard/experiments/gpt4_api_user.py`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/gcp/Dockerfile` & `policyengine-api-1.0.1/gcp/Dockerfile`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/gcp/README.md` & `policyengine-api-1.0.1/gcp/README.md`

 * *Files 17% similar despite different names*

```diff
@@ -4,9 +4,9 @@
 
 To update the starter image:
 * `python setup.py sdist` to build the python package
 * `twine upload dist/*` to upload the package to pypi as `policyengine-api`
 * `cd gcp`
 * `docker build .`
 * `docker images` to get the image id (the most recent one should be the one you just built)
-* `docker tag <image id> policyengine/policyengine-api`
-* `docker push policyengine/policyengine-api`
+* `docker tag <image id> nikhilwoodruff/policyengine-api`
+* `docker push nikhilwoodruff/policyengine-api`
```

### Comparing `policyengine-api-1.0.0/gcp/bump_country_package.py` & `policyengine-api-1.0.1/gcp/bump_country_package.py`

 * *Files 10% similar despite different names*

```diff
@@ -40,15 +40,19 @@
     if match:
         new_line = f"{country_package_name}=={version}"
     setup_py = setup_py.replace(match.group(0), new_line)
     # Write setup_py to setup.py
     with open(setup_py_path, "w") as f:
         f.write(setup_py)
 
-    changelog_yaml = f"""- bump: patch\n  changes:\n    changed:\n    - Bump {country} to {version}\n"""
+    country_package_full_name = country.replace(
+        "policyengine", "PolicyEngine"
+    ).replace("-", " ")
+
+    changelog_yaml = f"""- bump: patch\n  changes:\n    changed:\n    - Update {country_package_full_name} to {version}\n"""
     # Write changelog_yaml to changelog.yaml
     with open("changelog_entry.yaml", "w") as f:
         f.write(changelog_yaml)
 
     # Commit the change and push to a branch
     branch_name = f"bump-{country}-to-{version}"
     # Checkout a new branch locally, add all the files, commit, and push using the GitHub CLI only
@@ -56,18 +60,18 @@
     # First, create a new branch off master
     os.system(f"git checkout -b {branch_name}")
     # Add all the files
     os.system("git add -A")
     # Commit the change
     os.system(f"git config --global user.name 'PolicyEngine[bot]'")
     os.system(f"git config --global user.email 'hello@policyengine.org'")
-    os.system(f'git commit -m "Bump {country} to {version}"')
+    os.system(f'git commit -m "Bump {country_package_full_name} to {version}"')
     # Push the branch to GitHub, using the personal access token stored in GITHUB_TOKEN
     os.system(f"git push -u origin {branch_name} -f")
     # Create a pull request using the GitHub CLI
     os.system(
-        f"gh pr create --title 'Bump {country} to {version}' --body 'Bump {country} to {version}' --base master --head {branch_name}"
+        f"gh pr create --title 'Update {country_package_full_name} to {version}' --body 'Update {country_package_full_name} to {version}' --base master --head {branch_name}"
     )
 
 
 if __name__ == "__main__":
     main()
```

### Comparing `policyengine-api-1.0.0/gcp/export.py` & `policyengine-api-1.0.1/gcp/export.py`

 * *Files 24% similar despite different names*

```diff
@@ -19,15 +19,14 @@
     f.write(GAE)
 
 with open(".dbpw", "w") as f:
     f.write(DB_PD)
 
 # in gcp/compute_api/Dockerfile, replace .github_microdata_token with the contents of the file
 for dockerfile_location in [
-    "gcp/compute_api/Dockerfile",
     "gcp/policyengine_api/Dockerfile",
 ]:
     with open(dockerfile_location, "r") as f:
         dockerfile = f.read()
         dockerfile = dockerfile.replace(
             ".github_microdata_token", GITHUB_MICRODATA_TOKEN
         )
```

### Comparing `policyengine-api-1.0.0/policyengine_api/api.py` & `policyengine-api-1.0.1/policyengine_api/api.py`

 * *Files 8% similar despite different names*

```diff
@@ -5,15 +5,27 @@
 print(f"Initialising API...")
 
 import flask
 from flask_cors import CORS
 
 # Endpoints
 
-from .endpoints import get_home, get_metadata, get_household, post_household, get_policy, set_policy, get_policy_search, get_household_under_policy, get_calculate, get_economic_impact, get_analysis
+from .endpoints import (
+    get_home,
+    get_metadata,
+    get_household,
+    post_household,
+    get_policy,
+    set_policy,
+    get_policy_search,
+    get_household_under_policy,
+    get_calculate,
+    get_economic_impact,
+    get_analysis,
+)
 
 app = application = flask.Flask(__name__)
 
 CORS(app)
 
 app.route("/", methods=["GET"])(get_home)
 
@@ -28,30 +40,30 @@
 app.route("/<country_id>/policy/<policy_id>", methods=["GET"])(get_policy)
 
 app.route("/<country_id>/policy", methods=["POST"])(set_policy)
 
 app.route("/<country_id>/policies", methods=["GET"])(get_policy_search)
 
 app.route(
-    "/<country_id>/household/<household_id>/policy/<policy_id>", methods=["GET"]
+    "/<country_id>/household/<household_id>/policy/<policy_id>",
+    methods=["GET"],
 )(get_household_under_policy)
 
-app.route(
-    "/<country_id>/calculate", methods=["POST"]
-)(get_calculate)
+app.route("/<country_id>/calculate", methods=["POST"])(get_calculate)
 
 app.route(
-    "/<country_id>/economy/<policy_id>/over/<baseline_policy_id>", methods=["GET"]
+    "/<country_id>/economy/<policy_id>/over/<baseline_policy_id>",
+    methods=["GET"],
 )(get_economic_impact)
 
-app.route(
-    "/<country_id>/analysis", methods=["POST"]
-)(app.route(
-    "/<country_id>/analysis/<prompt_id>", methods=["GET"]
-)(get_analysis))
+app.route("/<country_id>/analysis", methods=["POST"])(
+    app.route("/<country_id>/analysis/<prompt_id>", methods=["GET"])(
+        get_analysis
+    )
+)
 
 
 @app.route("/liveness_check", methods=["GET"])
 def liveness_check():
     return flask.Response(
         "OK", status=200, headers={"Content-Type": "text/plain"}
     )
@@ -60,8 +72,8 @@
 @app.route("/readiness_check", methods=["GET"])
 def readiness_check():
     return flask.Response(
         "OK", status=200, headers={"Content-Type": "text/plain"}
     )
 
 
-print(f"API initialised.")
+print(f"API initialised.")
```

### Comparing `policyengine-api-1.0.0/policyengine_api/constants.py` & `policyengine-api-1.0.1/policyengine_api/constants.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 import pkg_resources
 
 REPO = Path(__file__).parents[1]
 GET = "GET"
 POST = "POST"
 UPDATE = "UPDATE"
 LIST = "LIST"
-VERSION = "1.0.0"
+VERSION = "1.0.1"
 COUNTRIES = ("uk", "us", "ca", "ng")
 COUNTRY_PACKAGE_NAMES = (
     "policyengine_uk",
     "policyengine_us",
     "policyengine_canada",
     "policyengine_ng",
 )
```

### Comparing `policyengine-api-1.0.0/policyengine_api/country.py` & `policyengine-api-1.0.1/policyengine_api/country.py`

 * *Files 2% similar despite different names*

```diff
@@ -51,18 +51,16 @@
                 basicInputs=self.tax_benefit_system.basic_inputs,
                 modelled_policies=self.tax_benefit_system.modelled_policies,
                 version=pkg_resources.get_distribution(
                     self.country_package_name
                 ).version,
             ),
         )
-    
-    def build_microsimulation_options(
-        self
-    ) -> dict:
+
+    def build_microsimulation_options(self) -> dict:
         # { region: [{ name: "uk", label: "the UK" }], time_period: [{ name: 2022, label: "2022", ... }] }
         options = dict()
         if self.country_id == "uk":
             region = [
                 dict(name="uk", label="the UK"),
                 dict(name="eng", label="England"),
                 dict(name="scot", label="Scotland"),
@@ -147,15 +145,14 @@
             time_period = [
                 dict(name=2023, label="2023"),
             ]
             options["region"] = region
             options["time_period"] = time_period
         return options
 
-
     def build_variables(self) -> dict:
         variables = self.tax_benefit_system.variables
         variable_data = {}
         for variable_name, variable in variables.items():
             variable_data[variable_name] = {
                 "documentation": variable.documentation,
                 "entity": variable.entity.key,
@@ -181,15 +178,14 @@
                     for value in variable.possible_values
                 ]
                 variable_data[variable_name][
                     "defaultValue"
                 ] = variable.default_value.name
         return variable_data
 
-
     def build_parameters(self) -> dict:
         parameters = self.tax_benefit_system.parameters
         parameter_data = {}
         for parameter in parameters.get_descendants():
             if "gov" != parameter.name[:3]:
                 continue
             end_name = parameter.name.split(".")[-1]
@@ -242,15 +238,14 @@
                         "label", end_name.replace("_", " ")
                     ),
                     "economy": parameter.metadata.get("economy", True),
                     "household": parameter.metadata.get("household", True),
                 }
         return parameter_data
 
-
     def build_entities(self) -> dict:
         data = {}
         for entity in self.tax_benefit_system.entities:
             entity_data = {
                 "plural": entity.plural,
                 "label": entity.label,
                 "doc": entity.doc,
@@ -266,24 +261,24 @@
                     }
                     for role in entity.roles
                 }
             else:
                 entity_data["roles"] = {}
             data[entity.key] = entity_data
         return data
-    
-    def calculate(
-        self, household: dict, reform: dict
-    ) -> dict:
+
+    def calculate(self, household: dict, reform: dict) -> dict:
         if len(reform.keys()) > 0:
             system = self.tax_benefit_system.clone()
             for parameter_name in reform:
                 for time_period, value in reform[parameter_name].items():
                     start_instant, end_instant = time_period.split(".")
-                    parameter = get_parameter(system.parameters, parameter_name)
+                    parameter = get_parameter(
+                        system.parameters, parameter_name
+                    )
                     node_type = type(parameter.values_list[-1].value)
                     if node_type == int:
                         node_type = float
                     try:
                         value = float(value)
                     except:
                         pass
@@ -359,15 +354,14 @@
                 else:
                     household[entity_plural][entity_id][variable_name][
                         period
                     ] = None
 
         return household
 
-    
 
 def create_policy_reform(policy_data: dict) -> dict:
     """
     Create a policy reform.
 
     Args:
         policy_data (dict): The policy data.
@@ -401,14 +395,15 @@
 
     class reform(Reform):
         def apply(self):
             self.modify_parameters(modify_parameters)
 
     return reform
 
+
 def get_requested_computations(household: dict):
     requested_computations = dpath.util.search(
         household,
         "*/*/*/*",
         afilter=lambda t: t is None,
         yielded=True,
     )
@@ -420,15 +415,14 @@
         requested_computation_data.append(
             (entity_plural, entity_id, variable_name, period)
         )
 
     return requested_computation_data
 
 
-
 COUNTRIES = {
     "uk": PolicyEngineCountry("policyengine_uk", "uk"),
     "us": PolicyEngineCountry("policyengine_us", "us"),
     "ca": PolicyEngineCountry("policyengine_canada", "ca"),
     "ng": PolicyEngineCountry("policyengine_ng", "ng"),
 }
 
@@ -445,8 +439,7 @@
     if country_id not in COUNTRIES:
         body = dict(
             status="error",
             message=f"Country {country_id} not found. Available countries are: {', '.join(COUNTRIES.keys())}",
         )
         return Response(json.dumps(body), status=404)
     return None
-
```

### Comparing `policyengine-api-1.0.0/policyengine_api/data/README.md` & `policyengine-api-1.0.1/policyengine_api/data/README.md`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/policyengine_api/data/data.py` & `policyengine-api-1.0.1/policyengine_api/data/data.py`

 * *Files 6% similar despite different names*

```diff
@@ -54,35 +54,38 @@
             user=db_user,
             password=db_pass,
         )
         self.pool = sqlalchemy.create_engine(
             "mysql+pymysql://",
             creator=lambda: conn,
         )
-    
+
     def _close_pool(self):
         try:
             self.pool.dispose()
             self.connector.close()
         except:
             pass
-    
+
     def query(self, *query):
         if self.local:
             with sqlite3.connect(self.db_url) as conn:
                 return conn.execute(*query)
         else:
             query = list(query)
             main_query = query[0]
             main_query = main_query.replace("?", "%s")
             query[0] = main_query
             try:
                 return self.pool.execute(*query)
             # Except InterfaceError and OperationalError, which are thrown when the connection is lost.
-            except (sqlalchemy.exc.InterfaceError, sqlalchemy.exc.OperationalError) as e:
+            except (
+                sqlalchemy.exc.InterfaceError,
+                sqlalchemy.exc.OperationalError,
+            ) as e:
                 try:
                     self._close_pool()
                     self._create_pool()
                     return self.pool.execute(*query)
                 except Exception as e:
                     raise e
 
@@ -109,23 +112,26 @@
             # Split the query into individual queries.
             queries = full_query.split(";")
             for query in queries:
                 # Execute each query.
                 self.query(query)
 
         # Insert the UK, US and Canadian 'current law' policies. e.g. the UK policy table must have a row with id=1, country_id="uk", label="Current law", api_version=COUNTRY_PACKAGE_VERSIONS["uk"], policy_json="{}", policy_hash=hash_object({})
-        for country_id, policy_id in zip(COUNTRY_PACKAGE_VERSIONS.keys(), range(1, 1 + len(COUNTRY_PACKAGE_VERSIONS))):
+        for country_id, policy_id in zip(
+            COUNTRY_PACKAGE_VERSIONS.keys(),
+            range(1, 1 + len(COUNTRY_PACKAGE_VERSIONS)),
+        ):
             self.query(
                 f"INSERT INTO policy (id, country_id, label, api_version, policy_json, policy_hash) VALUES (?, ?, ?, ?, ?, ?)",
                 (
                     policy_id,
                     country_id,
                     "Current law",
                     COUNTRY_PACKAGE_VERSIONS[country_id],
                     json.dumps({}),
                     hash_object({}),
                 ),
             )
 
 
 database = PolicyEngineDatabase(local=False, initialize=False)
-local_database = PolicyEngineDatabase(local=True, initialize=False)
+local_database = PolicyEngineDatabase(local=True, initialize=False)
```

### Comparing `policyengine-api-1.0.0/policyengine_api/data/initialise.sql` & `policyengine-api-1.0.1/policyengine_api/data/initialise.sql`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/policyengine_api/data/initialise_local.sql` & `policyengine-api-1.0.1/policyengine_api/data/initialise_local.sql`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/policyengine_api/endpoints/economy/compare.py` & `policyengine-api-1.0.1/policyengine_api/endpoints/economy/compare.py`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/policyengine_api/endpoints/economy/economy.py` & `policyengine-api-1.0.1/policyengine_api/endpoints/economy/economy.py`

 * *Files 8% similar despite different names*

```diff
@@ -9,15 +9,18 @@
 from rq import Queue
 from rq.job import Job
 from redis import Redis
 import datetime
 
 queue = Queue(connection=Redis())
 
-def get_economic_impact(country_id: str, policy_id: str, baseline_policy_id: str = None):
+
+def get_economic_impact(
+    country_id: str, policy_id: str, baseline_policy_id: str = None
+):
     """Calculate the economic impact of a policy.
 
     Args:
         country_id (str): The country ID.
         policy_id (str): The policy ID.
         baseline_policy_id (str): The baseline policy ID.
 
@@ -27,31 +30,47 @@
     invalid_country = validate_country(country_id)
     if invalid_country:
         return invalid_country
 
     country = COUNTRIES.get(country_id)
 
     policy_id = int(policy_id or get_current_law_policy_id(country_id))
-    baseline_policy_id = int(baseline_policy_id or get_current_law_policy_id(country_id))
-
-    default_region = country.metadata["result"]["economy_options"]["region"][0]["name"]
-    default_time_period = country.metadata["result"]["economy_options"]["time_period"][0]["name"]
+    baseline_policy_id = int(
+        baseline_policy_id or get_current_law_policy_id(country_id)
+    )
+
+    default_region = country.metadata["result"]["economy_options"]["region"][
+        0
+    ]["name"]
+    default_time_period = country.metadata["result"]["economy_options"][
+        "time_period"
+    ][0]["name"]
 
     query_parameters = request.args
     options = dict(query_parameters)
     options = json.loads(json.dumps(options))
     region = options.pop("region", default_region)
     time_period = options.pop("time_period", default_time_period)
-    api_version = options.pop("version", COUNTRY_PACKAGE_VERSIONS.get(country_id))
+    api_version = options.pop(
+        "version", COUNTRY_PACKAGE_VERSIONS.get(country_id)
+    )
     options_hash = json.dumps(options, sort_keys=True)
 
     # First, check if already calculated
     result = local_database.query(
         f"SELECT reform_impact_json, status, start_time FROM reform_impact WHERE country_id = ? AND reform_policy_id = ? AND baseline_policy_id = ? AND region = ? AND time_period = ? AND options_hash = ? AND api_version = ?",
-        (country_id, policy_id, baseline_policy_id, region, time_period, options_hash, api_version),
+        (
+            country_id,
+            policy_id,
+            baseline_policy_id,
+            region,
+            time_period,
+            options_hash,
+            api_version,
+        ),
     ).fetchall()
 
     # If there is a computing record which started more than 2 minutes ago, restart the job
     result = [
         dict(
             reform_impact_json=r[0],
             status=r[1],
@@ -59,32 +78,58 @@
         )
         for r in result
     ]
     computing_results = [r for r in result if r["status"] == "computing"]
     restarting = False
     if len(computing_results) > 0:
         computing_result = computing_results[0]
-        start_date = datetime.datetime.strptime(computing_result["start_time"], "%Y-%m-%d %H:%M:%S.%f")
-        seconds_elapsed = (datetime.datetime.now() - start_date).total_seconds()
+        start_date = datetime.datetime.strptime(
+            computing_result["start_time"], "%Y-%m-%d %H:%M:%S.%f"
+        )
+        seconds_elapsed = (
+            datetime.datetime.now() - start_date
+        ).total_seconds()
         if seconds_elapsed > 120:
-            print(f"Restarting computing job because it started {seconds_elapsed} seconds ago")
+            print(
+                f"Restarting computing job because it started {seconds_elapsed} seconds ago"
+            )
             restarting = True
             # Delete the computing record
             local_database.query(
                 f"DELETE FROM reform_impact WHERE country_id = ? AND reform_policy_id = ? AND baseline_policy_id = ? AND region = ? AND time_period = ? AND options_hash = ? AND api_version = ?",
-                (country_id, policy_id, baseline_policy_id, region, time_period, options_hash, api_version),
+                (
+                    country_id,
+                    policy_id,
+                    baseline_policy_id,
+                    region,
+                    time_period,
+                    options_hash,
+                    api_version,
+                ),
             )
 
     job_id = f"reform_impact_{country_id}_{policy_id}_{baseline_policy_id}_{region}_{time_period}_{options_hash}_{api_version}"
 
     if len(result) == 0 or restarting:
         # First, add a 'computing' record
         local_database.query(
             f"INSERT INTO reform_impact (country_id, reform_policy_id, baseline_policy_id, region, time_period, options_json, options_hash, status, api_version, reform_impact_json, start_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
-            (country_id, policy_id, baseline_policy_id, region, time_period, json.dumps(options), options_hash, "computing", api_version, json.dumps({}), datetime.datetime.now()),
+            (
+                country_id,
+                policy_id,
+                baseline_policy_id,
+                region,
+                time_period,
+                json.dumps(options),
+                options_hash,
+                "computing",
+                api_version,
+                json.dumps({}),
+                datetime.datetime.now(),
+            ),
         )
         baseline_policy = database.query(
             "SELECT policy_json FROM policy WHERE country_id = ? AND id = ?",
             (country_id, baseline_policy_id),
         ).fetchone()[0]
         reform_policy = database.query(
             "SELECT policy_json FROM policy WHERE country_id = ? AND id = ?",
@@ -109,21 +154,23 @@
         )
     else:
         # If there is one with status "ok" or "error", return that one
         ok_results = [r for r in result if r["status"] in ["ok", "error"]]
         if len(ok_results) > 0:
             result = ok_results[0]
             result = dict(result)
-            result["reform_impact_json"] = json.loads(result["reform_impact_json"])
+            result["reform_impact_json"] = json.loads(
+                result["reform_impact_json"]
+            )
             return dict(
                 status=result["status"],
                 message=None,
                 result=result["reform_impact_json"],
             )
         # Otherwise, return the first one
         result = result[0]
         job = Job.fetch(job_id, connection=queue.connection)
         return dict(
             status=result["status"],
             message=f"Your position in the queue is {job.get_position()}.",
             result=result["reform_impact_json"],
-        )
+        )
```

### Comparing `policyengine-api-1.0.0/policyengine_api/endpoints/economy/reform_impact.py` & `policyengine-api-1.0.1/policyengine_api/endpoints/economy/reform_impact.py`

 * *Files 8% similar despite different names*

```diff
@@ -9,27 +9,35 @@
 )
 from policyengine_api.data import PolicyEngineDatabase, local_database
 from .compare import compare_economic_outputs
 from .single_economy import compute_economy
 from policyengine_api.utils import hash_object
 from datetime import datetime
 
+
 def ensure_economy_computed(
     country_id: str,
     policy_id: str,
     region: str,
     time_period: str,
     options: dict,
     policy_json: dict,
 ):
     options_hash = hash_object(json.dumps(options))
     api_version = COUNTRY_PACKAGE_VERSIONS[country_id]
     economy = local_database.query(
         f"SELECT policy_id FROM economy WHERE country_id = ? AND policy_id = ? AND region = ? AND time_period = ? AND options_hash = ? AND api_version = ?",
-        (country_id, policy_id, region, time_period, options_hash, api_version),
+        (
+            country_id,
+            policy_id,
+            region,
+            time_period,
+            options_hash,
+            api_version,
+        ),
     ).fetchone()
     if economy is None:
         try:
             economy_result = compute_economy(
                 country_id,
                 policy_id,
                 region=region,
@@ -71,15 +79,15 @@
                     json.dumps(options),
                     country_id,
                     policy_id,
                     region,
                     time_period,
                     options_hash,
                     api_version,
-                )
+                ),
             )
             return dict(
                 policy_id=policy_id,
                 country_id=country_id,
                 region=region,
                 time_period=time_period,
                 options_hash=options_hash,
@@ -88,15 +96,22 @@
                 status="error",
                 message=str(e)[:250],
             )
     else:
         # Now get the total object now we know it exists
         economy = local_database.query(
             f"SELECT * FROM economy WHERE country_id = ? AND policy_id = ? AND region = ? AND time_period = ? AND options_hash = ? AND api_version = ?",
-            (country_id, policy_id, region, time_period, options_hash, api_version),
+            (
+                country_id,
+                policy_id,
+                region,
+                time_period,
+                options_hash,
+                api_version,
+            ),
         ).fetchone()
         economy = dict(
             economy_id=economy[0],
             policy_id=economy[1],
             country_id=economy[2],
             region=economy[3],
             time_period=economy[4],
@@ -133,36 +148,31 @@
         region (str): The region to filter on.
         time_period (str): The time period, e.g. 2024.
         options (dict): Any additional options.
     """
     options_hash = json.dumps(options, sort_keys=True)
     baseline_policy_id = int(baseline_policy_id)
     policy_id = int(policy_id)
-    print("Computing baseline economy")
     baseline_economy = ensure_economy_computed(
         country_id,
         baseline_policy_id,
         region,
         time_period,
         options,
         baseline_policy,
     )
-    print("Computing reform economy")
     reform_economy = ensure_economy_computed(
         country_id,
         policy_id,
         region,
         time_period,
         options,
         reform_policy,
     )
-    if (
-        baseline_economy["status"] != "ok"
-        or reform_economy["status"] != "ok"
-    ):
+    if baseline_economy["status"] != "ok" or reform_economy["status"] != "ok":
         local_database.query(
             "UPDATE reform_impact SET status = ?, message = ?, reform_impact_json = ? WHERE country_id = ? AND reform_policy_id = ? AND baseline_policy_id = ? AND region = ? AND time_period = ? AND options_hash = ?",
             (
                 "error",
                 "Error computing baseline or reform economy.",
                 json.dumps(
                     dict(
@@ -181,15 +191,14 @@
                 time_period,
                 options_hash,
             ),
         )
     else:
         baseline_economy = baseline_economy["economy_json"]
         reform_economy = reform_economy["economy_json"]
-        print("Comparing economies")
         impact = compare_economic_outputs(baseline_economy, reform_economy)
         # Delete all reform impact rows with the same baseline and reform policy IDs
 
         query = (
             "DELETE FROM reform_impact WHERE country_id = ? AND "
             "reform_policy_id = ? AND baseline_policy_id = ? AND "
             "region = ? AND time_period = ? AND options_hash = ? AND "
@@ -201,15 +210,15 @@
             (
                 country_id,
                 policy_id,
                 baseline_policy_id,
                 region,
                 time_period,
                 options_hash,
-            )
+            ),
         )
 
         # Insert into table
 
         query = (
             "INSERT INTO reform_impact (country_id, reform_policy_id, "
             "baseline_policy_id, region, time_period, options_hash, "
@@ -227,9 +236,9 @@
                 time_period,
                 options_hash,
                 json.dumps(options),
                 json.dumps(impact),
                 "ok",
                 datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S.%f"),
                 COUNTRY_PACKAGE_VERSIONS[country_id],
-            )
+            ),
         )
```

### Comparing `policyengine-api-1.0.0/policyengine_api/endpoints/economy/single_economy.py` & `policyengine-api-1.0.1/policyengine_api/endpoints/economy/single_economy.py`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/policyengine_api/endpoints/household.py` & `policyengine-api-1.0.1/policyengine_api/endpoints/household.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,12 @@
-from policyengine_api.country import COUNTRIES, validate_country, PolicyEngineCountry
+from policyengine_api.country import (
+    COUNTRIES,
+    validate_country,
+    PolicyEngineCountry,
+)
 from policyengine_api.data import database
 import json
 from flask import Response, request
 from policyengine_api.utils import hash_object
 from policyengine_api.constants import COUNTRY_PACKAGE_VERSIONS
 import sqlalchemy.exc
 from policyengine_api.constants import COUNTRY_PACKAGE_VERSIONS
@@ -11,14 +15,15 @@
 from policyengine_core.enums import Enum
 from policyengine_api.country import PolicyEngineCountry, COUNTRIES
 import json
 import dpath
 import math
 import logging
 
+
 def get_household(country_id: str, household_id: str) -> dict:
     """Get a household's input data with a given ID.
 
     Args:
         country_id (str): The country ID.
         household_id (str): The household ID.
     """
@@ -48,35 +53,41 @@
         )
         return Response(
             json.dumps(response_body),
             status=404,
             mimetype="application/json",
         )
 
-        
+
 def post_household(country_id: str) -> dict:
     """Set a household's input data.
 
     Args:
         country_id (str): The country ID.
     """
     country_not_found = validate_country(country_id)
     if country_not_found:
         return country_not_found
-    
+
     payload = request.json
     label = payload.get("label")
     household_json = payload.get("data")
     household_hash = hash_object(household_json)
     api_version = COUNTRY_PACKAGE_VERSIONS.get(country_id)
 
     try:
         database.query(
             f"INSERT INTO household (country_id, household_json, household_hash, label, api_version) VALUES (?, ?, ?, ?, ?)",
-            (country_id, json.dumps(household_json), household_hash, label, api_version),
+            (
+                country_id,
+                json.dumps(household_json),
+                household_hash,
+                label,
+                api_version,
+            ),
         )
     except sqlalchemy.exc.IntegrityError:
         pass
 
     household_id = database.query(
         f"SELECT id FROM household WHERE country_id = ? AND household_hash = ?",
         (country_id, household_hash),
@@ -86,26 +97,29 @@
         status="ok",
         message=None,
         result=dict(
             household_id=household_id,
         ),
     )
 
-def get_household_under_policy(country_id: str, household_id: str, policy_id: str):
+
+def get_household_under_policy(
+    country_id: str, household_id: str, policy_id: str
+):
     """Get a household's output data under a given policy.
 
     Args:
         country_id (str): The country ID.
         household_id (str): The household ID.
         policy_id (str): The policy ID.
     """
     invalid_country = validate_country(country_id)
     if invalid_country:
         return invalid_country
-    
+
     api_version = COUNTRY_PACKAGE_VERSIONS.get(country_id)
 
     # Look in computed_households to see if already computed
 
     row = database.query(
         f"SELECT * FROM computed_household WHERE household_id = ? AND policy_id = ? AND api_version = ?",
         (household_id, policy_id, api_version),
@@ -116,15 +130,14 @@
         result["result"] = json.loads(result["computed_household_json"])
         return dict(
             status="ok",
             message=None,
             result=result,
         )
 
-
     # Retrieve from the household table
 
     row = database.query(
         f"SELECT * FROM household WHERE id = ? AND country_id = ?",
         (household_id, country_id),
     ).fetchone()
 
@@ -137,15 +150,15 @@
             message=f"Household #{household_id} not found.",
         )
         return Response(
             json.dumps(response_body),
             status=404,
             mimetype="application/json",
         )
-    
+
     # Retrieve from the policy table
 
     row = database.query(
         f"SELECT * FROM policy WHERE id = ? AND country_id = ?",
         (policy_id, country_id),
     ).fetchone()
 
@@ -162,48 +175,56 @@
             status=404,
             mimetype="application/json",
         )
 
     country = COUNTRIES.get(country_id)
 
     try:
-        result = country.calculate(household["household_json"], policy["policy_json"])
+        result = country.calculate(
+            household["household_json"], policy["policy_json"]
+        )
     except Exception as e:
         logging.exception(e)
         response_body = dict(
             status="error",
             message=f"Error calculating household #{household_id} under policy #{policy_id}: {e}",
         )
         return Response(
             json.dumps(response_body),
             status=500,
             mimetype="application/json",
         )
-    
-    # Store the result in the computed_household table
 
+    # Store the result in the computed_household table
 
     try:
         database.query(
             f"INSERT INTO computed_household (country_id, household_id, policy_id, computed_household_json, api_version) VALUES (?, ?, ?, ?, ?)",
-            (country_id, household_id, policy_id, json.dumps(result), api_version),
+            (
+                country_id,
+                household_id,
+                policy_id,
+                json.dumps(result),
+                api_version,
+            ),
         )
     except sqlalchemy.exc.IntegrityError:
         # Update the result if it already exists
         database.query(
             f"UPDATE computed_household SET computed_household_json = ? WHERE country_id = ? AND household_id = ? AND policy_id = ?",
             (json.dumps(result), country_id, household_id, policy_id),
         )
 
     return dict(
         status="ok",
         message=None,
         result=result,
     )
 
+
 def get_calculate(country_id: str) -> dict:
     """Lightweight endpoint for passing in household and policy JSON objects and calculating without storing data.
 
     Args:
         country_id (str): The country ID.
     """
 
@@ -231,8 +252,8 @@
             mimetype="application/json",
         )
 
     return dict(
         status="ok",
         message=None,
         result=result,
-    )
+    )
```

### Comparing `policyengine-api-1.0.0/policyengine_api/endpoints/policy.py` & `policyengine-api-1.0.1/policyengine_api/endpoints/policy.py`

 * *Files 2% similar despite different names*

```diff
@@ -6,17 +6,15 @@
 from policyengine_core.parameters import ParameterNode, Parameter
 from policyengine_core.periods import instant
 import json
 from flask import Response, request
 import sqlalchemy.exc
 
 
-def get_policy(
-    country_id: str, policy_id: int
-) -> dict:
+def get_policy(country_id: str, policy_id: int) -> dict:
     """
     Get policy data for a given country and policy ID.
 
     Args:
         country_id (str): The country ID.
         policy_id (int): The policy ID.
 
@@ -58,25 +56,31 @@
 
     Args:
         country_id (str): The country ID.
     """
     country_not_found = validate_country(country_id)
     if country_not_found:
         return country_not_found
-    
+
     payload = request.json
     label = payload.pop("label", None)
     policy_json = payload.pop("data", None)
     policy_hash = hash_object(policy_json)
     api_version = COUNTRY_PACKAGE_VERSIONS.get(country_id)
 
     try:
         database.query(
             f"INSERT INTO policy (country_id, policy_json, policy_hash, label, api_version) VALUES (?, ?, ?, ?, ?)",
-            (country_id, json.dumps(policy_json), policy_hash, label, api_version),
+            (
+                country_id,
+                json.dumps(policy_json),
+                policy_hash,
+                label,
+                api_version,
+            ),
         )
     except sqlalchemy.exc.IntegrityError:
         pass
 
     policy_id = database.query(
         f"SELECT id FROM policy WHERE country_id = ? AND policy_hash = ?",
         (country_id, policy_hash),
@@ -87,16 +91,14 @@
         message=None,
         result=dict(
             policy_id=policy_id,
         ),
     )
 
 
-
-
 def get_policy_search(country_id: str) -> list:
     """
     Search for policies.
 
     Args:
         country_id (str): The country ID.
         query (str): The search query.
```

### Comparing `policyengine-api-1.0.0/policyengine_api/utils/json.py` & `policyengine-api-1.0.1/policyengine_api/utils/json.py`

 * *Files identical despite different names*

### Comparing `policyengine-api-1.0.0/policyengine_api.egg-info/SOURCES.txt` & `policyengine-api-1.0.1/policyengine_api.egg-info/SOURCES.txt`

 * *Files 9% similar despite different names*

```diff
@@ -20,14 +20,15 @@
 gcp/Dockerfile
 gcp/README.md
 gcp/bump_country_package.py
 gcp/dispatch.yaml
 gcp/export.py
 gcp/policyengine_api/Dockerfile
 gcp/policyengine_api/app.yaml
+gcp/policyengine_api/start.sh
 policyengine_api/api.py
 policyengine_api/constants.py
 policyengine_api/country.py
 policyengine_api/worker.py
 policyengine_api.egg-info/PKG-INFO
 policyengine_api.egg-info/SOURCES.txt
 policyengine_api.egg-info/dependency_links.txt
@@ -35,18 +36,25 @@
 policyengine_api.egg-info/top_level.txt
 policyengine_api/data/README.md
 policyengine_api/data/__init__.py
 policyengine_api/data/data.py
 policyengine_api/data/initialise.sql
 policyengine_api/data/initialise_local.sql
 policyengine_api/endpoints/__init__.py
+policyengine_api/endpoints/analysis.py
 policyengine_api/endpoints/home.py
 policyengine_api/endpoints/household.py
 policyengine_api/endpoints/metadata.py
 policyengine_api/endpoints/policy.py
 policyengine_api/endpoints/economy/__init__.py
 policyengine_api/endpoints/economy/compare.py
 policyengine_api/endpoints/economy/economy.py
 policyengine_api/endpoints/economy/reform_impact.py
 policyengine_api/endpoints/economy/single_economy.py
 policyengine_api/utils/__init__.py
-policyengine_api/utils/json.py
+policyengine_api/utils/json.py
+tests/api/test_api.py
+tests/api/test_hello_world.yaml
+tests/api/test_liveness.yaml
+tests/api/test_readiness.yaml
+tests/api/test_uk_baseline_policy.yaml
+tests/api/test_uk_metadata.yaml
```

### Comparing `policyengine-api-1.0.0/setup.py` & `policyengine-api-1.0.1/setup.py`

 * *Files 18% similar despite different names*

```diff
@@ -10,21 +10,22 @@
     packages=find_packages(),
     install_requires=[
         "click>=8",
         "flask>=1",
         "flask-cors>=3",
         "PolicyEngine-Core>=2,<3",
         "policyengine_uk==0.45.0",
-        "policyengine_us==0.271.0",
-        "policyengine_canada==0.44.0",
+        "policyengine_us==0.278.0",
+        "policyengine_canada==0.45.0",
         "policyengine-ng==0.4.2",
         "gunicorn",
         "cloud-sql-python-connector",
         "google-cloud-logging",
         "pymysql",
         "sqlalchemy>=1.4,<2",
         "streamlit",
         "markupsafe==2.0.1",
         "openai",
         "rq",
+        "redis",
     ],
 )
```

