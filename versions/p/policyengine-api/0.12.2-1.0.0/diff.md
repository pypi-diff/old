# Comparing `tmp/policyengine-api-0.12.2.tar.gz` & `tmp/policyengine-api-1.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "policyengine-api-0.12.2.tar", last modified: Sun Mar 26 00:27:50 2023, max compression
+gzip compressed data, was "policyengine-api-1.0.0.tar", last modified: Fri Apr  7 09:22:18 2023, max compression
```

## Comparing `policyengine-api-0.12.2.tar` & `policyengine-api-1.0.0.tar`

### file list

```diff
@@ -1,82 +1,68 @@
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.868715 policyengine-api-0.12.2/
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.853778 policyengine-api-0.12.2/.github/
--rw-r--r--   0 nikhil     (501) staff       (20)      267 2022-12-19 15:37:36.000000 policyengine-api-0.12.2/.github/changelog_template.md
--rwxr-xr-x   0 nikhil     (501) staff       (20)      122 2022-12-19 15:37:36.000000 policyengine-api-0.12.2/.github/get-changelog-diff.sh
--rwxr-xr-x   0 nikhil     (501) staff       (20)      642 2022-12-19 15:37:36.000000 policyengine-api-0.12.2/.github/has-functional-changes.sh
--rwxr-xr-x   0 nikhil     (501) staff       (20)     1013 2022-12-19 15:37:36.000000 policyengine-api-0.12.2/.github/is-version-number-acceptable.sh
--rwxr-xr-x   0 nikhil     (501) staff       (20)      115 2022-12-19 15:37:36.000000 policyengine-api-0.12.2/.github/publish-git-tag.sh
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.854252 policyengine-api-0.12.2/.github/workflows/
--rw-r--r--   0 nikhil     (501) staff       (20)     1723 2023-03-25 23:38:54.000000 policyengine-api-0.12.2/.github/workflows/pr.yml
--rw-r--r--   0 nikhil     (501) staff       (20)     3299 2023-03-25 23:38:12.000000 policyengine-api-0.12.2/.github/workflows/push.yml
--rw-r--r--   0 nikhil     (501) staff       (20)      133 2023-03-26 00:08:11.000000 policyengine-api-0.12.2/.gitignore
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.854510 policyengine-api-0.12.2/.vscode/
--rw-r--r--   0 nikhil     (501) staff       (20)      692 2022-11-22 22:32:04.000000 policyengine-api-0.12.2/.vscode/launch.json
--rw-r--r--   0 nikhil     (501) staff       (20)    24859 2023-03-26 00:21:42.000000 policyengine-api-0.12.2/CHANGELOG.md
--rw-r--r--   0 nikhil     (501) staff       (20)    34523 2022-12-06 22:08:46.000000 policyengine-api-0.12.2/LICENSE
--rw-r--r--   0 nikhil     (501) staff       (20)     1285 2023-03-22 21:37:20.000000 policyengine-api-0.12.2/Makefile
--rw-r--r--   0 nikhil     (501) staff       (20)      212 2023-03-26 00:27:50.868481 policyengine-api-0.12.2/PKG-INFO
--rw-r--r--   0 nikhil     (501) staff       (20)      229 2023-03-20 18:59:41.000000 policyengine-api-0.12.2/README.md
--rw-r--r--   0 nikhil     (501) staff       (20)    15894 2023-03-26 00:21:42.000000 policyengine-api-0.12.2/changelog.yaml
--rw-r--r--   0 nikhil     (501) staff       (20)       60 2023-03-26 00:22:04.000000 policyengine-api-0.12.2/changelog_entry.yaml
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.854798 policyengine-api-0.12.2/dashboard/
--rw-r--r--   0 nikhil     (501) staff       (20)     1990 2023-01-11 13:17:41.000000 policyengine-api-0.12.2/dashboard/app.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.856278 policyengine-api-0.12.2/gcp/
--rw-r--r--   0 nikhil     (501) staff       (20)      583 2023-03-26 00:14:23.000000 policyengine-api-0.12.2/gcp/Dockerfile
--rw-r--r--   0 nikhil     (501) staff       (20)      693 2023-03-25 19:25:34.000000 policyengine-api-0.12.2/gcp/README.md
--rw-r--r--   0 nikhil     (501) staff       (20)     2715 2023-01-20 17:20:59.000000 policyengine-api-0.12.2/gcp/bump_country_package.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.857007 policyengine-api-0.12.2/gcp/compute_api/
--rw-r--r--   0 nikhil     (501) staff       (20)      349 2023-03-25 23:33:00.000000 policyengine-api-0.12.2/gcp/compute_api/Dockerfile
--rw-r--r--   0 nikhil     (501) staff       (20)      361 2023-03-25 12:36:55.000000 policyengine-api-0.12.2/gcp/compute_api/app.yaml
--rw-r--r--   0 nikhil     (501) staff       (20)      133 2022-12-08 00:06:30.000000 policyengine-api-0.12.2/gcp/dispatch.yaml
--rw-r--r--   0 nikhil     (501) staff       (20)      662 2023-03-25 23:32:26.000000 policyengine-api-0.12.2/gcp/export.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.857571 policyengine-api-0.12.2/gcp/policyengine_api/
--rw-r--r--   0 nikhil     (501) staff       (20)      332 2023-03-25 23:32:56.000000 policyengine-api-0.12.2/gcp/policyengine_api/Dockerfile
--rw-r--r--   0 nikhil     (501) staff       (20)      327 2023-03-25 12:36:40.000000 policyengine-api-0.12.2/gcp/policyengine_api/app.yaml
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.860037 policyengine-api-0.12.2/policyengine_api/
--rw-r--r--   0 nikhil     (501) staff       (20)    12707 2023-03-25 19:19:20.000000 policyengine-api-0.12.2/policyengine_api/api.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.862299 policyengine-api-0.12.2/policyengine_api/compute_api/
--rw-r--r--   0 nikhil     (501) staff       (20)      205 2022-12-08 00:06:30.000000 policyengine-api-0.12.2/policyengine_api/compute_api/README.md
--rw-r--r--   0 nikhil     (501) staff       (20)       42 2022-12-08 00:06:30.000000 policyengine-api-0.12.2/policyengine_api/compute_api/__init__.py
--rw-r--r--   0 nikhil     (501) staff       (20)    13764 2023-03-08 18:08:40.000000 policyengine-api-0.12.2/policyengine_api/compute_api/compare.py
--rw-r--r--   0 nikhil     (501) staff       (20)    10287 2023-03-25 19:19:20.000000 policyengine-api-0.12.2/policyengine_api/compute_api/compute_api.py
--rw-r--r--   0 nikhil     (501) staff       (20)     6088 2023-03-09 00:46:05.000000 policyengine-api-0.12.2/policyengine_api/compute_api/economy.py
--rw-r--r--   0 nikhil     (501) staff       (20)      612 2023-03-26 00:27:43.000000 policyengine-api-0.12.2/policyengine_api/constants.py
--rw-r--r--   0 nikhil     (501) staff       (20)     1005 2023-03-25 19:19:20.000000 policyengine-api-0.12.2/policyengine_api/country.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.863897 policyengine-api-0.12.2/policyengine_api/data/
--rw-r--r--   0 nikhil     (501) staff       (20)     2003 2022-11-20 15:05:48.000000 policyengine-api-0.12.2/policyengine_api/data/README.md
--rw-r--r--   0 nikhil     (501) staff       (20)       49 2022-11-22 18:52:22.000000 policyengine-api-0.12.2/policyengine_api/data/__init__.py
--rw-r--r--   0 nikhil     (501) staff       (20)    10675 2023-03-25 12:36:07.000000 policyengine-api-0.12.2/policyengine_api/data/data.py
--rw-r--r--   0 nikhil     (501) staff       (20)     1783 2023-01-12 01:27:08.000000 policyengine-api-0.12.2/policyengine_api/data/initialise.sql
--rw-r--r--   0 nikhil     (501) staff       (20)     1682 2022-12-25 20:13:53.000000 policyengine-api-0.12.2/policyengine_api/data/initialise_local.sql
--rw-r--r--   0 nikhil     (501) staff       (20)       75 2022-11-30 19:47:16.000000 policyengine-api-0.12.2/policyengine_api/debug.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.865281 policyengine-api-0.12.2/policyengine_api/endpoints/
--rw-r--r--   0 nikhil     (501) staff       (20)      363 2022-11-23 01:57:19.000000 policyengine-api-0.12.2/policyengine_api/endpoints/__init__.py
--rw-r--r--   0 nikhil     (501) staff       (20)     6845 2023-03-10 11:44:08.000000 policyengine-api-0.12.2/policyengine_api/endpoints/computed_household.py
--rw-r--r--   0 nikhil     (501) staff       (20)     4312 2023-03-10 11:44:08.000000 policyengine-api-0.12.2/policyengine_api/endpoints/household.py
--rw-r--r--   0 nikhil     (501) staff       (20)    10313 2023-03-25 19:19:20.000000 policyengine-api-0.12.2/policyengine_api/endpoints/metadata.py
--rw-r--r--   0 nikhil     (501) staff       (20)     6831 2023-03-10 11:44:08.000000 policyengine-api-0.12.2/policyengine_api/endpoints/policy.py
--rw-r--r--   0 nikhil     (501) staff       (20)      423 2022-12-28 11:57:21.000000 policyengine-api-0.12.2/policyengine_api/logging.py
--rw-r--r--   0 nikhil     (501) staff       (20)     1256 2023-03-22 21:06:50.000000 policyengine-api-0.12.2/policyengine_api/testing.py
--rw-r--r--   0 nikhil     (501) staff       (20)     2081 2023-03-22 21:06:50.000000 policyengine-api-0.12.2/policyengine_api/utils.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.861065 policyengine-api-0.12.2/policyengine_api.egg-info/
--rw-r--r--   0 nikhil     (501) staff       (20)      212 2023-03-26 00:27:50.000000 policyengine-api-0.12.2/policyengine_api.egg-info/PKG-INFO
--rw-r--r--   0 nikhil     (501) staff       (20)     1894 2023-03-26 00:27:50.000000 policyengine-api-0.12.2/policyengine_api.egg-info/SOURCES.txt
--rw-r--r--   0 nikhil     (501) staff       (20)        1 2023-03-26 00:27:50.000000 policyengine-api-0.12.2/policyengine_api.egg-info/dependency_links.txt
--rw-r--r--   0 nikhil     (501) staff       (20)      268 2023-03-26 00:27:50.000000 policyengine-api-0.12.2/policyengine_api.egg-info/requires.txt
--rw-r--r--   0 nikhil     (501) staff       (20)        1 2023-03-26 00:27:50.000000 policyengine-api-0.12.2/policyengine_api.egg-info/top_level.txt
--rw-r--r--   0 nikhil     (501) staff       (20)       38 2023-03-26 00:27:50.868773 policyengine-api-0.12.2/setup.cfg
--rw-r--r--   0 nikhil     (501) staff       (20)      758 2023-03-26 00:21:42.000000 policyengine-api-0.12.2/setup.py
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.849964 policyengine-api-0.12.2/tests/
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.866881 policyengine-api-0.12.2/tests/api/
--rw-r--r--   0 nikhil     (501) staff       (20)     2332 2023-03-22 20:58:23.000000 policyengine-api-0.12.2/tests/api/test_api.py
--rw-r--r--   0 nikhil     (501) staff       (20)       54 2022-12-08 00:06:30.000000 policyengine-api-0.12.2/tests/api/test_hello_world.yaml
--rw-r--r--   0 nikhil     (501) staff       (20)       65 2023-03-23 00:33:05.000000 policyengine-api-0.12.2/tests/api/test_liveness.yaml
--rw-r--r--   0 nikhil     (501) staff       (20)       67 2023-03-23 00:33:13.000000 policyengine-api-0.12.2/tests/api/test_readiness.yaml
--rw-r--r--   0 nikhil     (501) staff       (20)      154 2023-03-22 18:03:54.000000 policyengine-api-0.12.2/tests/api/test_uk_baseline_policy.yaml
--rw-r--r--   0 nikhil     (501) staff       (20)       65 2022-12-08 00:06:30.000000 policyengine-api-0.12.2/tests/api/test_uk_metadata.yaml
-drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-03-26 00:27:50.868107 policyengine-api-0.12.2/tests/compute_api/
--rw-r--r--   0 nikhil     (501) staff       (20)     2321 2022-12-08 00:06:30.000000 policyengine-api-0.12.2/tests/compute_api/test_compute_api.py
--rw-r--r--   0 nikhil     (501) staff       (20)       54 2022-12-08 00:06:30.000000 policyengine-api-0.12.2/tests/compute_api/test_hello_world.yaml
--rw-r--r--   0 nikhil     (501) staff       (20)       65 2023-03-23 00:33:13.000000 policyengine-api-0.12.2/tests/compute_api/test_liveness.yaml
--rw-r--r--   0 nikhil     (501) staff       (20)      144 2023-03-26 00:09:44.000000 policyengine-api-0.12.2/tests/compute_api/test_microdata.py
--rw-r--r--   0 nikhil     (501) staff       (20)       67 2023-03-23 00:33:13.000000 policyengine-api-0.12.2/tests/compute_api/test_readiness.yaml
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.298777 policyengine-api-1.0.0/
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.292861 policyengine-api-1.0.0/.github/
+-rw-r--r--   0 nikhil     (501) staff       (20)      267 2022-12-19 15:37:36.000000 policyengine-api-1.0.0/.github/changelog_template.md
+-rwxr-xr-x   0 nikhil     (501) staff       (20)      122 2022-12-19 15:37:36.000000 policyengine-api-1.0.0/.github/get-changelog-diff.sh
+-rwxr-xr-x   0 nikhil     (501) staff       (20)      642 2022-12-19 15:37:36.000000 policyengine-api-1.0.0/.github/has-functional-changes.sh
+-rwxr-xr-x   0 nikhil     (501) staff       (20)     1013 2022-12-19 15:37:36.000000 policyengine-api-1.0.0/.github/is-version-number-acceptable.sh
+-rwxr-xr-x   0 nikhil     (501) staff       (20)      115 2022-12-19 15:37:36.000000 policyengine-api-1.0.0/.github/publish-git-tag.sh
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.293139 policyengine-api-1.0.0/.github/workflows/
+-rw-r--r--   0 nikhil     (501) staff       (20)     2048 2023-03-28 23:54:13.000000 policyengine-api-1.0.0/.github/workflows/pr.yml
+-rw-r--r--   0 nikhil     (501) staff       (20)     3411 2023-03-28 23:54:32.000000 policyengine-api-1.0.0/.github/workflows/push.yml
+-rw-r--r--   0 nikhil     (501) staff       (20)      142 2023-04-06 09:46:03.000000 policyengine-api-1.0.0/.gitignore
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.293273 policyengine-api-1.0.0/.vscode/
+-rw-r--r--   0 nikhil     (501) staff       (20)      692 2022-11-22 22:32:04.000000 policyengine-api-1.0.0/.vscode/launch.json
+-rw-r--r--   0 nikhil     (501) staff       (20)    28729 2023-04-04 09:47:38.000000 policyengine-api-1.0.0/CHANGELOG.md
+-rw-r--r--   0 nikhil     (501) staff       (20)    34523 2022-12-06 22:08:46.000000 policyengine-api-1.0.0/LICENSE
+-rw-r--r--   0 nikhil     (501) staff       (20)     1285 2023-03-22 21:37:20.000000 policyengine-api-1.0.0/Makefile
+-rw-r--r--   0 nikhil     (501) staff       (20)      211 2023-04-07 09:22:18.298528 policyengine-api-1.0.0/PKG-INFO
+-rw-r--r--   0 nikhil     (501) staff       (20)      229 2023-03-20 18:59:41.000000 policyengine-api-1.0.0/README.md
+-rw-r--r--   0 nikhil     (501) staff       (20)    18299 2023-04-04 09:47:38.000000 policyengine-api-1.0.0/changelog.yaml
+-rw-r--r--   0 nikhil     (501) staff       (20)        0 2023-04-03 21:42:12.000000 policyengine-api-1.0.0/changelog_entry.yaml
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.293406 policyengine-api-1.0.0/dashboard/
+-rw-r--r--   0 nikhil     (501) staff       (20)     1990 2023-01-11 13:17:41.000000 policyengine-api-1.0.0/dashboard/app.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.293673 policyengine-api-1.0.0/dashboard/experiments/
+-rw-r--r--   0 nikhil     (501) staff       (20)     4252 2023-04-03 21:42:12.000000 policyengine-api-1.0.0/dashboard/experiments/gpt4_api_user.py
+-rw-r--r--   0 nikhil     (501) staff       (20)       41 2023-04-03 21:42:12.000000 policyengine-api-1.0.0/dashboard/experiments/requirements.txt
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.294315 policyengine-api-1.0.0/gcp/
+-rw-r--r--   0 nikhil     (501) staff       (20)      640 2023-04-07 09:21:58.000000 policyengine-api-1.0.0/gcp/Dockerfile
+-rw-r--r--   0 nikhil     (501) staff       (20)      693 2023-03-25 19:25:34.000000 policyengine-api-1.0.0/gcp/README.md
+-rw-r--r--   0 nikhil     (501) staff       (20)     2715 2023-01-20 17:20:59.000000 policyengine-api-1.0.0/gcp/bump_country_package.py
+-rw-r--r--   0 nikhil     (501) staff       (20)      133 2022-12-08 00:06:30.000000 policyengine-api-1.0.0/gcp/dispatch.yaml
+-rw-r--r--   0 nikhil     (501) staff       (20)     1163 2023-03-28 23:54:13.000000 policyengine-api-1.0.0/gcp/export.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.294582 policyengine-api-1.0.0/gcp/policyengine_api/
+-rw-r--r--   0 nikhil     (501) staff       (20)      350 2023-04-07 09:19:01.000000 policyengine-api-1.0.0/gcp/policyengine_api/Dockerfile
+-rw-r--r--   0 nikhil     (501) staff       (20)      327 2023-04-07 09:16:29.000000 policyengine-api-1.0.0/gcp/policyengine_api/app.yaml
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.295117 policyengine-api-1.0.0/policyengine_api/
+-rw-r--r--   0 nikhil     (501) staff       (20)     1721 2023-04-07 09:15:07.000000 policyengine-api-1.0.0/policyengine_api/api.py
+-rw-r--r--   0 nikhil     (501) staff       (20)      611 2023-04-07 09:22:09.000000 policyengine-api-1.0.0/policyengine_api/constants.py
+-rw-r--r--   0 nikhil     (501) staff       (20)    17717 2023-04-06 16:41:27.000000 policyengine-api-1.0.0/policyengine_api/country.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.296463 policyengine-api-1.0.0/policyengine_api/data/
+-rw-r--r--   0 nikhil     (501) staff       (20)     2003 2023-04-04 11:36:53.000000 policyengine-api-1.0.0/policyengine_api/data/README.md
+-rw-r--r--   0 nikhil     (501) staff       (20)       65 2023-04-06 11:50:46.000000 policyengine-api-1.0.0/policyengine_api/data/__init__.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     4413 2023-04-06 14:21:15.000000 policyengine-api-1.0.0/policyengine_api/data/data.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     1922 2023-04-04 11:36:53.000000 policyengine-api-1.0.0/policyengine_api/data/initialise.sql
+-rw-r--r--   0 nikhil     (501) staff       (20)     2043 2023-04-06 16:57:17.000000 policyengine-api-1.0.0/policyengine_api/data/initialise_local.sql
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.297110 policyengine-api-1.0.0/policyengine_api/endpoints/
+-rw-r--r--   0 nikhil     (501) staff       (20)      296 2023-04-06 16:50:25.000000 policyengine-api-1.0.0/policyengine_api/endpoints/__init__.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.297989 policyengine-api-1.0.0/policyengine_api/endpoints/economy/
+-rw-r--r--   0 nikhil     (501) staff       (20)       40 2023-04-04 22:53:20.000000 policyengine-api-1.0.0/policyengine_api/endpoints/economy/__init__.py
+-rw-r--r--   0 nikhil     (501) staff       (20)    13764 2023-04-04 20:02:12.000000 policyengine-api-1.0.0/policyengine_api/endpoints/economy/compare.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     5662 2023-04-06 16:56:29.000000 policyengine-api-1.0.0/policyengine_api/endpoints/economy/economy.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     8241 2023-04-06 20:27:43.000000 policyengine-api-1.0.0/policyengine_api/endpoints/economy/reform_impact.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     5846 2023-04-06 16:41:03.000000 policyengine-api-1.0.0/policyengine_api/endpoints/economy/single_economy.py
+-rw-r--r--   0 nikhil     (501) staff       (20)      260 2023-04-04 12:21:57.000000 policyengine-api-1.0.0/policyengine_api/endpoints/home.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     7166 2023-04-04 14:34:04.000000 policyengine-api-1.0.0/policyengine_api/endpoints/household.py
+-rw-r--r--   0 nikhil     (501) staff       (20)      361 2023-04-04 12:02:24.000000 policyengine-api-1.0.0/policyengine_api/endpoints/metadata.py
+-rw-r--r--   0 nikhil     (501) staff       (20)     3686 2023-04-04 12:42:53.000000 policyengine-api-1.0.0/policyengine_api/endpoints/policy.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.298278 policyengine-api-1.0.0/policyengine_api/utils/
+-rw-r--r--   0 nikhil     (501) staff       (20)       20 2023-04-04 11:26:24.000000 policyengine-api-1.0.0/policyengine_api/utils/__init__.py
+-rw-r--r--   0 nikhil     (501) staff       (20)      979 2023-04-05 09:46:36.000000 policyengine-api-1.0.0/policyengine_api/utils/json.py
+-rw-r--r--   0 nikhil     (501) staff       (20)      281 2023-04-07 08:49:36.000000 policyengine-api-1.0.0/policyengine_api/worker.py
+drwxr-xr-x   0 nikhil     (501) staff       (20)        0 2023-04-07 09:22:18.295787 policyengine-api-1.0.0/policyengine_api.egg-info/
+-rw-r--r--   0 nikhil     (501) staff       (20)      211 2023-04-07 09:22:17.000000 policyengine-api-1.0.0/policyengine_api.egg-info/PKG-INFO
+-rw-r--r--   0 nikhil     (501) staff       (20)     1558 2023-04-07 09:22:18.000000 policyengine-api-1.0.0/policyengine_api.egg-info/SOURCES.txt
+-rw-r--r--   0 nikhil     (501) staff       (20)        1 2023-04-07 09:22:17.000000 policyengine-api-1.0.0/policyengine_api.egg-info/dependency_links.txt
+-rw-r--r--   0 nikhil     (501) staff       (20)      278 2023-04-07 09:22:18.000000 policyengine-api-1.0.0/policyengine_api.egg-info/requires.txt
+-rw-r--r--   0 nikhil     (501) staff       (20)        1 2023-04-07 09:22:18.000000 policyengine-api-1.0.0/policyengine_api.egg-info/top_level.txt
+-rw-r--r--   0 nikhil     (501) staff       (20)       38 2023-04-07 09:22:18.298832 policyengine-api-1.0.0/setup.cfg
+-rw-r--r--   0 nikhil     (501) staff       (20)      790 2023-04-07 09:18:56.000000 policyengine-api-1.0.0/setup.py
```

### Comparing `policyengine-api-0.12.2/.github/has-functional-changes.sh` & `policyengine-api-1.0.0/.github/has-functional-changes.sh`

 * *Files identical despite different names*

### Comparing `policyengine-api-0.12.2/.github/is-version-number-acceptable.sh` & `policyengine-api-1.0.0/.github/is-version-number-acceptable.sh`

 * *Files identical despite different names*

### Comparing `policyengine-api-0.12.2/.github/workflows/pr.yml` & `policyengine-api-1.0.0/.github/workflows/pr.yml`

 * *Files 22% similar despite different names*

```diff
@@ -30,27 +30,32 @@
       - name: Preview changelog update
         run: ".github/get-changelog-diff.sh"
       - name: Check version number has been properly updated
         run: ".github/is-version-number-acceptable.sh"
   test:
     name: Test
     runs-on: ubuntu-latest
+    container:
+      image: nikhilwoodruff/policyengine-api
     steps:
       - name: Checkout repo
         uses: actions/checkout@v2
-      - name: Setup Python
-        uses: actions/setup-python@v2
-        with:
-          python-version: 3.9
       - name: Set up Cloud SDK
         uses: google-github-actions/setup-gcloud@v0
         with:
           project_id: policyengine-api
           service_account_key: ${{ secrets.GCP_SA_KEY }}
           export_default_credentials: true
       - name: Install dependencies
         run: make install
-      - name: Run the main tests
+      - name: Test the main API
         run: make test
         env:
           POLICYENGINE_DB_PASSWORD: ${{ secrets.POLICYENGINE_DB_PASSWORD }}
           POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN: ${{ secrets.POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN }}
+          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
+      - name: Test the compute API
+        run: make test-compute
+        env:
+          POLICYENGINE_DB_PASSWORD: ${{ secrets.POLICYENGINE_DB_PASSWORD }}
+          POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN: ${{ secrets.POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN }}
+          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

### Comparing `policyengine-api-0.12.2/.github/workflows/push.yml` & `policyengine-api-1.0.0/.github/workflows/push.yml`

 * *Files 6% similar despite different names*

```diff
@@ -66,14 +66,15 @@
         uses: 'google-github-actions/setup-gcloud@v1'
       - name: Deploy
         run: make deploy-api
         env:
           POLICYENGINE_DB_PASSWORD: ${{ secrets.POLICYENGINE_DB_PASSWORD }}
           GOOGLE_APPLICATION_CREDENTIALS: ${{ secrets.GCP_SA_KEY }}
           POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN: ${{ secrets.POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN }}
+          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
   deploy_compute:
     name: Deploy compute API
     runs-on: ubuntu-latest
     if: |
       (github.repository == 'PolicyEngine/policyengine-api')
       && (github.event.head_commit.message == 'Update PolicyEngine API')
     steps:
@@ -91,8 +92,9 @@
         uses: 'google-github-actions/setup-gcloud@v1'
       - name: Deploy
         run: make deploy-compute-api
         env:
           POLICYENGINE_DB_PASSWORD: ${{ secrets.POLICYENGINE_DB_PASSWORD }}
           GOOGLE_APPLICATION_CREDENTIALS: ${{ secrets.GCP_SA_KEY }}
           POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN: ${{ secrets.POLICYENGINE_GITHUB_MICRODATA_AUTH_TOKEN }}
+          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

### Comparing `policyengine-api-0.12.2/.vscode/launch.json` & `policyengine-api-1.0.0/.vscode/launch.json`

 * *Files identical despite different names*

### Comparing `policyengine-api-0.12.2/CHANGELOG.md` & `policyengine-api-1.0.0/CHANGELOG.md`

 * *Files 8% similar despite different names*

```diff
@@ -1,14 +1,152 @@
 # Changelog
 
 All notable changes to this project will be documented in this file.
 
 The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), 
 and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
 
+## [0.13.19] - 2023-04-04 04:49:17
+
+### Changed
+
+- Bump policyengine-us to 0.271.0
+
+## [0.13.18] - 2023-04-03 17:43:08
+
+### Changed
+
+- Bump policyengine-us to 0.268.0
+
+## [0.13.17] - 2023-04-03 16:26:44
+
+### Changed
+
+- Bump policyengine-us to 0.267.0
+
+## [0.13.16] - 2023-04-02 20:56:40
+
+### Changed
+
+- Bump policyengine-us to 0.266.0
+
+## [0.13.15] - 2023-04-02 02:42:16
+
+### Changed
+
+- Bump policyengine-us to 0.264.0
+
+## [0.13.14] - 2023-04-01 15:35:04
+
+### Changed
+
+- Bump policyengine-us to 0.263.5
+
+## [0.13.13] - 2023-04-01 09:51:26
+
+### Changed
+
+- Bump policyengine-uk to 0.45.0
+
+## [0.13.12] - 2023-03-31 06:50:42
+
+### Changed
+
+- Bump policyengine-us to 0.263.4
+
+## [0.13.11] - 2023-03-30 21:54:35
+
+### Changed
+
+- Bump policyengine-us to 0.263.3
+
+## [0.13.10] - 2023-03-30 18:23:20
+
+### Changed
+
+- Bump policyengine-us to 0.263.2
+
+## [0.13.9] - 2023-03-30 15:00:19
+
+### Changed
+
+- Bump policyengine-uk to 0.44.3
+
+## [0.13.8] - 2023-03-30 05:26:32
+
+### Changed
+
+- Bump policyengine-us to 0.263.1
+
+## [0.13.7] - 2023-03-30 04:29:37
+
+### Changed
+
+- Bump policyengine-us to 0.263.0
+
+## [0.13.6] - 2023-03-30 02:39:15
+
+### Changed
+
+- Bump policyengine-us to 0.262.0
+
+## [0.13.5] - 2023-03-30 01:38:20
+
+### Changed
+
+- Bump policyengine-canada to 0.44.0
+
+## [0.13.4] - 2023-03-29 23:53:23
+
+### Changed
+
+- Bump policyengine-us to 0.261.1
+
+## [0.13.3] - 2023-03-29 12:36:32
+
+### Changed
+
+- Bump policyengine-uk to 0.44.2
+
+## [0.13.2] - 2023-03-29 04:43:52
+
+### Changed
+
+- Bump policyengine-us to 0.260.0
+
+## [0.13.1] - 2023-03-28 23:06:53
+
+### Fixed
+
+- OpenAI API key included in API environments.
+
+## [0.13.0] - 2023-03-28 22:25:38
+
+### Added
+
+- /analysis endpoint for policy analyses by GPT-4.
+
+## [0.12.4] - 2023-03-28 03:57:32
+
+### Changed
+
+- Bump policyengine-canada to 0.43.0
+
+## [0.12.3] - 2023-03-27 21:43:16
+
+### Changed
+
+- Bump policyengine-us to 0.259.0
+
+## [0.12.2] - 2023-03-26 00:58:55
+
+### Fixed
+
+- Bumped UK system.
+
 ## [0.12.1] - 2023-03-26 00:21:42
 
 ### Fixed
 
 - UK microsimulation runs download the correct data.
 
 ## [0.12.0] - 2023-03-25 16:34:24
@@ -888,14 +1026,37 @@
 
 ### Added
 
 - Initial API.
 
 
 
+[0.13.19]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.18...0.13.19
+[0.13.18]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.17...0.13.18
+[0.13.17]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.16...0.13.17
+[0.13.16]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.15...0.13.16
+[0.13.15]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.14...0.13.15
+[0.13.14]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.13...0.13.14
+[0.13.13]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.12...0.13.13
+[0.13.12]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.11...0.13.12
+[0.13.11]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.10...0.13.11
+[0.13.10]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.9...0.13.10
+[0.13.9]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.8...0.13.9
+[0.13.8]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.7...0.13.8
+[0.13.7]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.6...0.13.7
+[0.13.6]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.5...0.13.6
+[0.13.5]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.4...0.13.5
+[0.13.4]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.3...0.13.4
+[0.13.3]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.2...0.13.3
+[0.13.2]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.1...0.13.2
+[0.13.1]: https://github.com/PolicyEngine/policyengine-api/compare/0.13.0...0.13.1
+[0.13.0]: https://github.com/PolicyEngine/policyengine-api/compare/0.12.4...0.13.0
+[0.12.4]: https://github.com/PolicyEngine/policyengine-api/compare/0.12.3...0.12.4
+[0.12.3]: https://github.com/PolicyEngine/policyengine-api/compare/0.12.2...0.12.3
+[0.12.2]: https://github.com/PolicyEngine/policyengine-api/compare/0.12.1...0.12.2
 [0.12.1]: https://github.com/PolicyEngine/policyengine-api/compare/0.12.0...0.12.1
 [0.12.0]: https://github.com/PolicyEngine/policyengine-api/compare/0.11.18...0.12.0
 [0.11.18]: https://github.com/PolicyEngine/policyengine-api/compare/0.11.17...0.11.18
 [0.11.17]: https://github.com/PolicyEngine/policyengine-api/compare/0.11.16...0.11.17
 [0.11.16]: https://github.com/PolicyEngine/policyengine-api/compare/0.11.15...0.11.16
 [0.11.15]: https://github.com/PolicyEngine/policyengine-api/compare/0.11.14...0.11.15
 [0.11.14]: https://github.com/PolicyEngine/policyengine-api/compare/0.11.13...0.11.14
```

### Comparing `policyengine-api-0.12.2/LICENSE` & `policyengine-api-1.0.0/LICENSE`

 * *Files identical despite different names*

### Comparing `policyengine-api-0.12.2/Makefile` & `policyengine-api-1.0.0/Makefile`

 * *Files identical despite different names*

### Comparing `policyengine-api-0.12.2/changelog.yaml` & `policyengine-api-1.0.0/changelog.yaml`

 * *Files 9% similar despite different names*

```diff
@@ -736,7 +736,122 @@
     - Country packages updated.
   date: 2023-03-25 16:34:24
 - bump: patch
   changes:
     fixed:
     - UK microsimulation runs download the correct data.
   date: 2023-03-26 00:21:42
+- bump: patch
+  changes:
+    fixed:
+    - Bumped UK system.
+  date: 2023-03-26 00:58:55
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.259.0
+  date: 2023-03-27 21:43:16
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-canada to 0.43.0
+  date: 2023-03-28 03:57:32
+- bump: minor
+  changes:
+    added:
+    - /analysis endpoint for policy analyses by GPT-4.
+  date: 2023-03-28 22:25:38
+- bump: patch
+  changes:
+    fixed:
+    - OpenAI API key included in API environments.
+  date: 2023-03-28 23:06:53
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.260.0
+  date: 2023-03-29 04:43:52
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-uk to 0.44.2
+  date: 2023-03-29 12:36:32
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.261.1
+  date: 2023-03-29 23:53:23
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-canada to 0.44.0
+  date: 2023-03-30 01:38:20
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.262.0
+  date: 2023-03-30 02:39:15
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.263.0
+  date: 2023-03-30 04:29:37
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.263.1
+  date: 2023-03-30 05:26:32
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-uk to 0.44.3
+  date: 2023-03-30 15:00:19
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.263.2
+  date: 2023-03-30 18:23:20
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.263.3
+  date: 2023-03-30 21:54:35
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.263.4
+  date: 2023-03-31 06:50:42
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-uk to 0.45.0
+  date: 2023-04-01 09:51:26
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.263.5
+  date: 2023-04-01 15:35:04
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.264.0
+  date: 2023-04-02 02:42:16
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.266.0
+  date: 2023-04-02 20:56:40
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.267.0
+  date: 2023-04-03 16:26:44
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.268.0
+  date: 2023-04-03 17:43:08
+- bump: patch
+  changes:
+    changed:
+    - Bump policyengine-us to 0.271.0
+  date: 2023-04-04 04:49:17
```

### Comparing `policyengine-api-0.12.2/dashboard/app.py` & `policyengine-api-1.0.0/dashboard/app.py`

 * *Files identical despite different names*

### Comparing `policyengine-api-0.12.2/gcp/README.md` & `policyengine-api-1.0.0/gcp/README.md`

 * *Files identical despite different names*

### Comparing `policyengine-api-0.12.2/gcp/bump_country_package.py` & `policyengine-api-1.0.0/gcp/bump_country_package.py`

 * *Files identical despite different names*

### Comparing `policyengine-api-0.12.2/policyengine_api/compute_api/compare.py` & `policyengine-api-1.0.0/policyengine_api/endpoints/economy/compare.py`

 * *Files identical despite different names*

### Comparing `policyengine-api-0.12.2/policyengine_api/compute_api/economy.py` & `policyengine-api-1.0.0/policyengine_api/endpoints/economy/single_economy.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,8 @@
-from policyengine_api.country import COUNTRIES
-from policyengine_api.data import database
-from policyengine_api.endpoints.policy import create_policy_reform
+from policyengine_api.country import COUNTRIES, create_policy_reform
 from policyengine_core.simulations import Microsimulation
 from policyengine_core.experimental import MemoryConfig
 import json
 
 
 def compute_general_economy(simulation: Microsimulation) -> dict:
     total_tax = simulation.calculate("household_tax").sum()
@@ -106,35 +104,32 @@
 
 def compute_economy(
     country_id: str,
     policy_id: str,
     region: str,
     time_period: str,
     options: dict,
+    policy_json: dict,
 ):
     country = COUNTRIES.get(country_id)
-    policy_json = database.get_in_table(
-        "policy", country_id=country_id, id=policy_id
-    )["policy_json"]
     policy_data = json.loads(policy_json)
     if country_id == "us":
         us_modelled_states = country.tax_benefit_system.modelled_policies[
             "filtered"
         ]["state_name"].keys()
         us_modelled_states = [state.lower() for state in us_modelled_states]
         if (region == "us") or (region.lower() not in us_modelled_states):
             policy_data["simulation.reported_state_income_tax"] = {
                 "2010-01-01.2030-01-01": True
             }
-    reform = create_policy_reform(country_id, policy_data)
+    reform = create_policy_reform(policy_data)
 
     simulation: Microsimulation = country.country_package.Microsimulation(
         reform=reform,
     )
-    simulation.memory_config = MemoryConfig(0.4)
     simulation.default_calculation_period = time_period
 
     original_household_weight = simulation.calculate("household_weight").values
 
     if country_id == "uk":
         if region != "uk":
             region_values = simulation.calculate("country").values
```

### Comparing `policyengine-api-0.12.2/policyengine_api/constants.py` & `policyengine-api-1.0.0/policyengine_api/constants.py`

 * *Files 3% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 import pkg_resources
 
 REPO = Path(__file__).parents[1]
 GET = "GET"
 POST = "POST"
 UPDATE = "UPDATE"
 LIST = "LIST"
-VERSION = "0.12.2"
+VERSION = "1.0.0"
 COUNTRIES = ("uk", "us", "ca", "ng")
 COUNTRY_PACKAGE_NAMES = (
     "policyengine_uk",
     "policyengine_us",
     "policyengine_canada",
     "policyengine_ng",
 )
```

### Comparing `policyengine-api-0.12.2/policyengine_api/data/README.md` & `policyengine-api-1.0.0/policyengine_api/data/README.md`

 * *Files identical despite different names*

### Comparing `policyengine-api-0.12.2/policyengine_api/data/initialise.sql` & `policyengine-api-1.0.0/policyengine_api/data/initialise.sql`

 * *Files 3% similar despite different names*

```diff
@@ -1,9 +1,7 @@
-DROP TABLE IF EXISTS reform_impact;
-
 CREATE TABLE IF NOT EXISTS household (
     id INTEGER PRIMARY KEY AUTO_INCREMENT,
     country_id VARCHAR(3) NOT NULL,
     label VARCHAR(255),
     api_version VARCHAR(255) NOT NULL,
     household_json JSON NOT NULL,
     household_hash VARCHAR(255) NOT NULL
@@ -53,8 +51,15 @@
     options_json JSON,
     options_hash VARCHAR(255),
     api_version VARCHAR(10) NOT NULL,
     reform_impact_json JSON NOT NULL,
     status VARCHAR(32) NOT NULL,
     message VARCHAR(255),
     start_time DATETIME
-)
+);
+
+CREATE TABLE IF NOT EXISTS analysis (
+    prompt_id INTEGER PRIMARY KEY AUTO_INCREMENT,
+    prompt LONGTEXT NOT NULL,
+    analysis LONGTEXT,
+    status VARCHAR(32) NOT NULL
+)
```

### Comparing `policyengine-api-0.12.2/policyengine_api/data/initialise_local.sql` & `policyengine-api-1.0.0/policyengine_api/data/initialise_local.sql`

 * *Files 8% similar despite different names*

```diff
@@ -1,106 +1,128 @@
-00000000: 4352 4541 5445 2054 4142 4c45 2049 4620  CREATE TABLE IF 
-00000010: 4e4f 5420 4558 4953 5453 2068 6f75 7365  NOT EXISTS house
-00000020: 686f 6c64 2028 0a20 2020 2069 6420 494e  hold (.    id IN
-00000030: 5445 4745 5220 5052 494d 4152 5920 4b45  TEGER PRIMARY KE
-00000040: 592c 0a20 2020 2063 6f75 6e74 7279 5f69  Y,.    country_i
-00000050: 6420 5641 5243 4841 5228 3329 204e 4f54  d VARCHAR(3) NOT
-00000060: 204e 554c 4c2c 0a20 2020 206c 6162 656c   NULL,.    label
-00000070: 2056 4152 4348 4152 2832 3535 292c 0a20   VARCHAR(255),. 
-00000080: 2020 2061 7069 5f76 6572 7369 6f6e 2056     api_version V
-00000090: 4152 4348 4152 2832 3535 2920 4e4f 5420  ARCHAR(255) NOT 
-000000a0: 4e55 4c4c 2c0a 2020 2020 686f 7573 6568  NULL,.    househ
-000000b0: 6f6c 645f 6a73 6f6e 204a 534f 4e42 204e  old_json JSONB N
-000000c0: 4f54 204e 554c 4c2c 0a20 2020 2068 6f75  OT NULL,.    hou
-000000d0: 7365 686f 6c64 5f68 6173 6820 5641 5243  sehold_hash VARC
-000000e0: 4841 5228 3235 3529 204e 4f54 204e 554c  HAR(255) NOT NUL
-000000f0: 4c0a 293b 0a0a 4352 4541 5445 2054 4142  L.);..CREATE TAB
-00000100: 4c45 2049 4620 4e4f 5420 4558 4953 5453  LE IF NOT EXISTS
-00000110: 2063 6f6d 7075 7465 645f 686f 7573 6568   computed_househ
-00000120: 6f6c 6420 280a 2020 2020 686f 7573 6568  old (.    househ
-00000130: 6f6c 645f 6964 2049 4e54 204e 4f54 204e  old_id INT NOT N
-00000140: 554c 4c2c 0a20 2020 2070 6f6c 6963 795f  ULL,.    policy_
-00000150: 6964 2049 4e54 204e 4f54 204e 554c 4c2c  id INT NOT NULL,
-00000160: 0a20 2020 2063 6f75 6e74 7279 5f69 6420  .    country_id 
-00000170: 5641 5243 4841 5228 3329 204e 4f54 204e  VARCHAR(3) NOT N
-00000180: 554c 4c2c 0a20 2020 2061 7069 5f76 6572  ULL,.    api_ver
-00000190: 7369 6f6e 2056 4152 4348 4152 2831 3029  sion VARCHAR(10)
-000001a0: 204e 4f54 204e 554c 4c2c 0a20 2020 2063   NOT NULL,.    c
-000001b0: 6f6d 7075 7465 645f 686f 7573 6568 6f6c  omputed_househol
-000001c0: 645f 6a73 6f6e 204a 534f 4e42 204e 4f54  d_json JSONB NOT
-000001d0: 204e 554c 4c2c 0a20 2020 2073 7461 7475   NULL,.    statu
-000001e0: 7320 5641 5243 4841 5228 3332 292c 0a20  s VARCHAR(32),. 
-000001f0: 2020 2050 5249 4d41 5259 204b 4559 2028     PRIMARY KEY (
-00000200: 686f 7573 6568 6f6c 645f 6964 2c20 706f  household_id, po
-00000210: 6c69 6379 5f69 642c 2063 6f75 6e74 7279  licy_id, country
-00000220: 5f69 6429 0a29 3b0a 0a43 5245 4154 4520  _id).);..CREATE 
-00000230: 5441 424c 4520 4946 204e 4f54 2045 5849  TABLE IF NOT EXI
-00000240: 5354 5320 706f 6c69 6379 2028 0a20 2020  STS policy (.   
-00000250: 2069 6420 494e 5445 4745 5220 5052 494d   id INTEGER PRIM
-00000260: 4152 5920 4b45 592c 0a20 2020 2063 6f75  ARY KEY,.    cou
-00000270: 6e74 7279 5f69 6420 5641 5243 4841 5228  ntry_id VARCHAR(
-00000280: 3329 204e 4f54 204e 554c 4c2c 0a20 2020  3) NOT NULL,.   
-00000290: 206c 6162 656c 2056 4152 4348 4152 2832   label VARCHAR(2
-000002a0: 3535 292c 0a20 2020 2061 7069 5f76 6572  55),.    api_ver
-000002b0: 7369 6f6e 2056 4152 4348 4152 2831 3029  sion VARCHAR(10)
-000002c0: 204e 4f54 204e 554c 4c2c 0a20 2020 2070   NOT NULL,.    p
-000002d0: 6f6c 6963 795f 6a73 6f6e 204a 534f 4e42  olicy_json JSONB
-000002e0: 204e 4f54 204e 554c 4c2c 0a20 2020 2070   NOT NULL,.    p
-000002f0: 6f6c 6963 795f 6861 7368 2056 4152 4348  olicy_hash VARCH
-00000300: 4152 2832 3535 2920 4e4f 5420 4e55 4c4c  AR(255) NOT NULL
-00000310: 0a29 3b0a 0a43 5245 4154 4520 5441 424c  .);..CREATE TABL
-00000320: 4520 4946 204e 4f54 2045 5849 5354 5320  E IF NOT EXISTS 
-00000330: 6563 6f6e 6f6d 7920 280a 2020 2020 6563  economy (.    ec
-00000340: 6f6e 6f6d 795f 6964 2049 4e54 4547 4552  onomy_id INTEGER
-00000350: 2050 5249 4d41 5259 204b 4559 2c0a 2020   PRIMARY KEY,.  
-00000360: 2020 706f 6c69 6379 5f69 6420 494e 5420    policy_id INT 
-00000370: 4e4f 5420 4e55 4c4c 2c0a 2020 2020 636f  NOT NULL,.    co
-00000380: 756e 7472 795f 6964 2056 4152 4348 4152  untry_id VARCHAR
-00000390: 2833 2920 4e4f 5420 4e55 4c4c 2c0a 2020  (3) NOT NULL,.  
-000003a0: 2020 7265 6769 6f6e 2056 4152 4348 4152    region VARCHAR
-000003b0: 2833 3229 2c0a 2020 2020 7469 6d65 5f70  (32),.    time_p
-000003c0: 6572 696f 6420 5641 5243 4841 5228 3332  eriod VARCHAR(32
-000003d0: 292c 0a20 2020 206f 7074 696f 6e73 5f6a  ),.    options_j
-000003e0: 736f 6e20 4a53 4f4e 204e 4f54 204e 554c  son JSON NOT NUL
-000003f0: 4c2c 0a20 2020 206f 7074 696f 6e73 5f68  L,.    options_h
-00000400: 6173 6820 5641 5243 4841 5228 3235 3529  ash VARCHAR(255)
-00000410: 204e 4f54 204e 554c 4c2c 0a20 2020 2061   NOT NULL,.    a
-00000420: 7069 5f76 6572 7369 6f6e 2056 4152 4348  pi_version VARCH
-00000430: 4152 2831 3029 204e 4f54 204e 554c 4c2c  AR(10) NOT NULL,
-00000440: 0a20 2020 2065 636f 6e6f 6d79 5f6a 736f  .    economy_jso
-00000450: 6e20 4a53 4f4e 2c0a 2020 2020 7374 6174  n JSON,.    stat
-00000460: 7573 2056 4152 4348 4152 2833 3229 204e  us VARCHAR(32) N
-00000470: 4f54 204e 554c 4c2c 0a20 2020 206d 6573  OT NULL,.    mes
-00000480: 7361 6765 2056 4152 4348 4152 2832 3535  sage VARCHAR(255
-00000490: 290a 293b 0a0a 4352 4541 5445 2054 4142  ).);..CREATE TAB
-000004a0: 4c45 2049 4620 4e4f 5420 4558 4953 5453  LE IF NOT EXISTS
-000004b0: 2072 6566 6f72 6d5f 696d 7061 6374 2028   reform_impact (
-000004c0: 0a20 2020 2072 6566 6f72 6d5f 696d 7061  .    reform_impa
-000004d0: 6374 5f69 6420 494e 5445 4745 5220 5052  ct_id INTEGER PR
-000004e0: 494d 4152 5920 4b45 592c 0a20 2020 2062  IMARY KEY,.    b
-000004f0: 6173 656c 696e 655f 706f 6c69 6379 5f69  aseline_policy_i
-00000500: 6420 494e 5420 4e4f 5420 4e55 4c4c 2c0a  d INT NOT NULL,.
-00000510: 2020 2020 7265 666f 726d 5f70 6f6c 6963      reform_polic
-00000520: 795f 6964 2049 4e54 204e 4f54 204e 554c  y_id INT NOT NUL
-00000530: 4c2c 200a 2020 2020 636f 756e 7472 795f  L, .    country_
-00000540: 6964 2056 4152 4348 4152 2833 2920 4e4f  id VARCHAR(3) NO
-00000550: 5420 4e55 4c4c 2c0a 2020 2020 7265 6769  T NULL,.    regi
-00000560: 6f6e 2056 4152 4348 4152 2833 3229 204e  on VARCHAR(32) N
-00000570: 4f54 204e 554c 4c2c 0a20 2020 2074 696d  OT NULL,.    tim
-00000580: 655f 7065 7269 6f64 2056 4152 4348 4152  e_period VARCHAR
-00000590: 2833 3229 204e 4f54 204e 554c 4c2c 0a20  (32) NOT NULL,. 
-000005a0: 2020 206f 7074 696f 6e73 5f6a 736f 6e20     options_json 
-000005b0: 4a53 4f4e 204e 4f54 204e 554c 4c2c 0a20  JSON NOT NULL,. 
-000005c0: 2020 206f 7074 696f 6e73 5f68 6173 6820     options_hash 
-000005d0: 5641 5243 4841 5228 3235 3529 204e 4f54  VARCHAR(255) NOT
-000005e0: 204e 554c 4c2c 0a20 2020 2061 7069 5f76   NULL,.    api_v
-000005f0: 6572 7369 6f6e 2056 4152 4348 4152 2831  ersion VARCHAR(1
-00000600: 3029 204e 4f54 204e 554c 4c2c 0a20 2020  0) NOT NULL,.   
-00000610: 2072 6566 6f72 6d5f 696d 7061 6374 5f6a   reform_impact_j
-00000620: 736f 6e20 4a53 4f4e 204e 4f54 204e 554c  son JSON NOT NUL
-00000630: 4c2c 0a20 2020 2073 7461 7475 7320 5641  L,.    status VA
-00000640: 5243 4841 5228 3332 2920 4e4f 5420 4e55  RCHAR(32) NOT NU
-00000650: 4c4c 2c0a 2020 2020 6d65 7373 6167 6520  LL,.    message 
-00000660: 5641 5243 4841 5228 3235 3529 2c0a 2020  VARCHAR(255),.  
-00000670: 2020 7374 6172 745f 7469 6d65 2044 4154    start_time DAT
-00000680: 4554 494d 4520 4e4f 5420 4e55 4c4c 0a29  ETIME NOT NULL.)
-00000690: 3b0a                                     ;.
+00000000: 4452 4f50 2054 4142 4c45 2049 4620 4558  DROP TABLE IF EX
+00000010: 4953 5453 2068 6f75 7365 686f 6c64 3b0a  ISTS household;.
+00000020: 4452 4f50 2054 4142 4c45 2049 4620 4558  DROP TABLE IF EX
+00000030: 4953 5453 2063 6f6d 7075 7465 645f 686f  ISTS computed_ho
+00000040: 7573 6568 6f6c 643b 0a44 524f 5020 5441  usehold;.DROP TA
+00000050: 424c 4520 4946 2045 5849 5354 5320 706f  BLE IF EXISTS po
+00000060: 6c69 6379 3b0a 4452 4f50 2054 4142 4c45  licy;.DROP TABLE
+00000070: 2049 4620 4558 4953 5453 2065 636f 6e6f   IF EXISTS econo
+00000080: 6d79 3b0a 4452 4f50 2054 4142 4c45 2049  my;.DROP TABLE I
+00000090: 4620 4558 4953 5453 2072 6566 6f72 6d5f  F EXISTS reform_
+000000a0: 696d 7061 6374 3b0a 4452 4f50 2054 4142  impact;.DROP TAB
+000000b0: 4c45 2049 4620 4558 4953 5453 2061 6e61  LE IF EXISTS ana
+000000c0: 6c79 7369 733b 0a0a 4352 4541 5445 2054  lysis;..CREATE T
+000000d0: 4142 4c45 2049 4620 4e4f 5420 4558 4953  ABLE IF NOT EXIS
+000000e0: 5453 2068 6f75 7365 686f 6c64 2028 0a20  TS household (. 
+000000f0: 2020 2069 6420 494e 5445 4745 5220 5052     id INTEGER PR
+00000100: 494d 4152 5920 4b45 592c 0a20 2020 2063  IMARY KEY,.    c
+00000110: 6f75 6e74 7279 5f69 6420 5641 5243 4841  ountry_id VARCHA
+00000120: 5228 3329 204e 4f54 204e 554c 4c2c 0a20  R(3) NOT NULL,. 
+00000130: 2020 206c 6162 656c 2056 4152 4348 4152     label VARCHAR
+00000140: 2832 3535 292c 0a20 2020 2061 7069 5f76  (255),.    api_v
+00000150: 6572 7369 6f6e 2056 4152 4348 4152 2832  ersion VARCHAR(2
+00000160: 3535 2920 4e4f 5420 4e55 4c4c 2c0a 2020  55) NOT NULL,.  
+00000170: 2020 686f 7573 6568 6f6c 645f 6a73 6f6e    household_json
+00000180: 204a 534f 4e42 204e 4f54 204e 554c 4c2c   JSONB NOT NULL,
+00000190: 0a20 2020 2068 6f75 7365 686f 6c64 5f68  .    household_h
+000001a0: 6173 6820 5641 5243 4841 5228 3235 3529  ash VARCHAR(255)
+000001b0: 204e 4f54 204e 554c 4c0a 293b 0a0a 4352   NOT NULL.);..CR
+000001c0: 4541 5445 2054 4142 4c45 2049 4620 4e4f  EATE TABLE IF NO
+000001d0: 5420 4558 4953 5453 2063 6f6d 7075 7465  T EXISTS compute
+000001e0: 645f 686f 7573 6568 6f6c 6420 280a 2020  d_household (.  
+000001f0: 2020 686f 7573 6568 6f6c 645f 6964 2049    household_id I
+00000200: 4e54 204e 4f54 204e 554c 4c2c 0a20 2020  NT NOT NULL,.   
+00000210: 2070 6f6c 6963 795f 6964 2049 4e54 204e   policy_id INT N
+00000220: 4f54 204e 554c 4c2c 0a20 2020 2063 6f75  OT NULL,.    cou
+00000230: 6e74 7279 5f69 6420 5641 5243 4841 5228  ntry_id VARCHAR(
+00000240: 3329 204e 4f54 204e 554c 4c2c 0a20 2020  3) NOT NULL,.   
+00000250: 2061 7069 5f76 6572 7369 6f6e 2056 4152   api_version VAR
+00000260: 4348 4152 2831 3029 204e 4f54 204e 554c  CHAR(10) NOT NUL
+00000270: 4c2c 0a20 2020 2063 6f6d 7075 7465 645f  L,.    computed_
+00000280: 686f 7573 6568 6f6c 645f 6a73 6f6e 204a  household_json J
+00000290: 534f 4e42 204e 4f54 204e 554c 4c2c 0a20  SONB NOT NULL,. 
+000002a0: 2020 2073 7461 7475 7320 5641 5243 4841     status VARCHA
+000002b0: 5228 3332 292c 0a20 2020 2050 5249 4d41  R(32),.    PRIMA
+000002c0: 5259 204b 4559 2028 686f 7573 6568 6f6c  RY KEY (househol
+000002d0: 645f 6964 2c20 706f 6c69 6379 5f69 642c  d_id, policy_id,
+000002e0: 2063 6f75 6e74 7279 5f69 6429 0a29 3b0a   country_id).);.
+000002f0: 0a43 5245 4154 4520 5441 424c 4520 4946  .CREATE TABLE IF
+00000300: 204e 4f54 2045 5849 5354 5320 706f 6c69   NOT EXISTS poli
+00000310: 6379 2028 0a20 2020 2069 6420 494e 5445  cy (.    id INTE
+00000320: 4745 5220 5052 494d 4152 5920 4b45 592c  GER PRIMARY KEY,
+00000330: 0a20 2020 2063 6f75 6e74 7279 5f69 6420  .    country_id 
+00000340: 5641 5243 4841 5228 3329 204e 4f54 204e  VARCHAR(3) NOT N
+00000350: 554c 4c2c 0a20 2020 206c 6162 656c 2056  ULL,.    label V
+00000360: 4152 4348 4152 2832 3535 292c 0a20 2020  ARCHAR(255),.   
+00000370: 2061 7069 5f76 6572 7369 6f6e 2056 4152   api_version VAR
+00000380: 4348 4152 2831 3029 204e 4f54 204e 554c  CHAR(10) NOT NUL
+00000390: 4c2c 0a20 2020 2070 6f6c 6963 795f 6a73  L,.    policy_js
+000003a0: 6f6e 204a 534f 4e42 204e 4f54 204e 554c  on JSONB NOT NUL
+000003b0: 4c2c 0a20 2020 2070 6f6c 6963 795f 6861  L,.    policy_ha
+000003c0: 7368 2056 4152 4348 4152 2832 3535 2920  sh VARCHAR(255) 
+000003d0: 4e4f 5420 4e55 4c4c 0a29 3b0a 0a43 5245  NOT NULL.);..CRE
+000003e0: 4154 4520 5441 424c 4520 4946 204e 4f54  ATE TABLE IF NOT
+000003f0: 2045 5849 5354 5320 6563 6f6e 6f6d 7920   EXISTS economy 
+00000400: 280a 2020 2020 6563 6f6e 6f6d 795f 6964  (.    economy_id
+00000410: 2049 4e54 4547 4552 2050 5249 4d41 5259   INTEGER PRIMARY
+00000420: 204b 4559 2c0a 2020 2020 706f 6c69 6379   KEY,.    policy
+00000430: 5f69 6420 494e 5420 4e4f 5420 4e55 4c4c  _id INT NOT NULL
+00000440: 2c0a 2020 2020 636f 756e 7472 795f 6964  ,.    country_id
+00000450: 2056 4152 4348 4152 2833 2920 4e4f 5420   VARCHAR(3) NOT 
+00000460: 4e55 4c4c 2c0a 2020 2020 7265 6769 6f6e  NULL,.    region
+00000470: 2056 4152 4348 4152 2833 3229 2c0a 2020   VARCHAR(32),.  
+00000480: 2020 7469 6d65 5f70 6572 696f 6420 5641    time_period VA
+00000490: 5243 4841 5228 3332 292c 0a20 2020 206f  RCHAR(32),.    o
+000004a0: 7074 696f 6e73 5f6a 736f 6e20 4a53 4f4e  ptions_json JSON
+000004b0: 204e 4f54 204e 554c 4c2c 0a20 2020 206f   NOT NULL,.    o
+000004c0: 7074 696f 6e73 5f68 6173 6820 5641 5243  ptions_hash VARC
+000004d0: 4841 5228 3235 3529 204e 4f54 204e 554c  HAR(255) NOT NUL
+000004e0: 4c2c 0a20 2020 2061 7069 5f76 6572 7369  L,.    api_versi
+000004f0: 6f6e 2056 4152 4348 4152 2831 3029 204e  on VARCHAR(10) N
+00000500: 4f54 204e 554c 4c2c 0a20 2020 2065 636f  OT NULL,.    eco
+00000510: 6e6f 6d79 5f6a 736f 6e20 4a53 4f4e 2c0a  nomy_json JSON,.
+00000520: 2020 2020 7374 6174 7573 2056 4152 4348      status VARCH
+00000530: 4152 2833 3229 204e 4f54 204e 554c 4c2c  AR(32) NOT NULL,
+00000540: 0a20 2020 206d 6573 7361 6765 2056 4152  .    message VAR
+00000550: 4348 4152 2832 3535 290a 293b 0a0a 4352  CHAR(255).);..CR
+00000560: 4541 5445 2054 4142 4c45 2049 4620 4e4f  EATE TABLE IF NO
+00000570: 5420 4558 4953 5453 2072 6566 6f72 6d5f  T EXISTS reform_
+00000580: 696d 7061 6374 2028 0a20 2020 2072 6566  impact (.    ref
+00000590: 6f72 6d5f 696d 7061 6374 5f69 6420 494e  orm_impact_id IN
+000005a0: 5445 4745 5220 5052 494d 4152 5920 4b45  TEGER PRIMARY KE
+000005b0: 592c 0a20 2020 2062 6173 656c 696e 655f  Y,.    baseline_
+000005c0: 706f 6c69 6379 5f69 6420 494e 5420 4e4f  policy_id INT NO
+000005d0: 5420 4e55 4c4c 2c0a 2020 2020 7265 666f  T NULL,.    refo
+000005e0: 726d 5f70 6f6c 6963 795f 6964 2049 4e54  rm_policy_id INT
+000005f0: 204e 4f54 204e 554c 4c2c 200a 2020 2020   NOT NULL, .    
+00000600: 636f 756e 7472 795f 6964 2056 4152 4348  country_id VARCH
+00000610: 4152 2833 2920 4e4f 5420 4e55 4c4c 2c0a  AR(3) NOT NULL,.
+00000620: 2020 2020 7265 6769 6f6e 2056 4152 4348      region VARCH
+00000630: 4152 2833 3229 204e 4f54 204e 554c 4c2c  AR(32) NOT NULL,
+00000640: 0a20 2020 2074 696d 655f 7065 7269 6f64  .    time_period
+00000650: 2056 4152 4348 4152 2833 3229 204e 4f54   VARCHAR(32) NOT
+00000660: 204e 554c 4c2c 0a20 2020 206f 7074 696f   NULL,.    optio
+00000670: 6e73 5f6a 736f 6e20 4a53 4f4e 204e 4f54  ns_json JSON NOT
+00000680: 204e 554c 4c2c 0a20 2020 206f 7074 696f   NULL,.    optio
+00000690: 6e73 5f68 6173 6820 5641 5243 4841 5228  ns_hash VARCHAR(
+000006a0: 3235 3529 204e 4f54 204e 554c 4c2c 0a20  255) NOT NULL,. 
+000006b0: 2020 2061 7069 5f76 6572 7369 6f6e 2056     api_version V
+000006c0: 4152 4348 4152 2831 3029 204e 4f54 204e  ARCHAR(10) NOT N
+000006d0: 554c 4c2c 0a20 2020 2072 6566 6f72 6d5f  ULL,.    reform_
+000006e0: 696d 7061 6374 5f6a 736f 6e20 4a53 4f4e  impact_json JSON
+000006f0: 204e 4f54 204e 554c 4c2c 0a20 2020 2073   NOT NULL,.    s
+00000700: 7461 7475 7320 5641 5243 4841 5228 3332  tatus VARCHAR(32
+00000710: 2920 4e4f 5420 4e55 4c4c 2c0a 2020 2020  ) NOT NULL,.    
+00000720: 6d65 7373 6167 6520 5641 5243 4841 5228  message VARCHAR(
+00000730: 3235 3529 2c0a 2020 2020 7374 6172 745f  255),.    start_
+00000740: 7469 6d65 2044 4154 4554 494d 4520 4e4f  time DATETIME NO
+00000750: 5420 4e55 4c4c 0a29 3b0a 0a43 5245 4154  T NULL.);..CREAT
+00000760: 4520 5441 424c 4520 4946 204e 4f54 2045  E TABLE IF NOT E
+00000770: 5849 5354 5320 616e 616c 7973 6973 2028  XISTS analysis (
+00000780: 0a20 2020 2070 726f 6d70 745f 6964 2049  .    prompt_id I
+00000790: 4e54 4547 4552 2050 5249 4d41 5259 204b  NTEGER PRIMARY K
+000007a0: 4559 2c0a 2020 2020 7072 6f6d 7074 204c  EY,.    prompt L
+000007b0: 4f4e 4754 4558 5420 4e4f 5420 4e55 4c4c  ONGTEXT NOT NULL
+000007c0: 2c0a 2020 2020 616e 616c 7973 6973 204c  ,.    analysis L
+000007d0: 4f4e 4754 4558 542c 0a20 2020 2073 7461  ONGTEXT,.    sta
+000007e0: 7475 7320 5641 5243 4841 5228 3332 2920  tus VARCHAR(32) 
+000007f0: 4e4f 5420 4e55 4c4c 0a29 3b              NOT NULL.);
```

### Comparing `policyengine-api-0.12.2/policyengine_api/endpoints/policy.py` & `policyengine-api-1.0.0/policyengine_api/endpoints/household.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,215 +1,238 @@
-from policyengine_api.country import COUNTRIES, validate_country
+from policyengine_api.country import COUNTRIES, validate_country, PolicyEngineCountry
 from policyengine_api.data import database
+import json
+from flask import Response, request
 from policyengine_api.utils import hash_object
-from policyengine_api.constants import VERSION, COUNTRY_PACKAGE_VERSIONS
-from policyengine_core.reforms import Reform
-from policyengine_core.parameters import ParameterNode, Parameter
+from policyengine_api.constants import COUNTRY_PACKAGE_VERSIONS
+import sqlalchemy.exc
+from policyengine_api.constants import COUNTRY_PACKAGE_VERSIONS
+from policyengine_core.parameters import get_parameter
 from policyengine_core.periods import instant
+from policyengine_core.enums import Enum
+from policyengine_api.country import PolicyEngineCountry, COUNTRIES
 import json
+import dpath
+import math
+import logging
 
-
-def get_policy(
-    country_id: str, policy_id: int = None, policy_data: dict = None
-) -> dict:
-    """
-    Get policy data for a given country and policy ID, or get the full record for a given policy from its data.
+def get_household(country_id: str, household_id: str) -> dict:
+    """Get a household's input data with a given ID.
 
     Args:
         country_id (str): The country ID.
-        policy_id (int, optional): The policy ID. Defaults to None.
-        policy_data (dict, optional): The policy data. Defaults to None.
-
-    Returns:
-        dict: The policy record.
+        household_id (str): The household ID.
     """
-    country_not_found = validate_country(country_id)
-    if country_not_found:
-        return country_not_found
-
-    policy = None
-    if policy_id is not None:
-        # Get the policy record for a given policy ID.
-        policy = database.get_in_table(
-            "policy", country_id=country_id, id=policy_id
-        )
-        if policy is None:
-            return dict(
-                status="error",
-                message=f"Policy {policy_id} not found in {country_id}",
-            )
-    elif policy_data is not None:
-        # Get the policy record for a given policy data object.
-        policy = database.get_in_table(
-            "policy",
-            country_id=country_id,
-            policy_hash=hash_object(policy_data),
-        )
-        if policy is None:
-            return dict(
-                status="error",
-                message=f"Policy not found in {country_id}",
-            )
-    else:
+    invalid_country = validate_country(country_id)
+    if invalid_country:
+        return invalid_country
+
+    # Retrieve from the household table
+
+    row = database.query(
+        f"SELECT * FROM household WHERE id = ? AND country_id = ?",
+        (household_id, country_id),
+    ).fetchone()
+
+    if row is not None:
+        household = dict(row)
+        household["household_json"] = json.loads(household["household_json"])
         return dict(
+            status="ok",
+            message=None,
+            result=household,
+        )
+    else:
+        response_body = dict(
             status="error",
-            message=f"Must provide either policy_id or policy_data",
+            message=f"Household #{household_id} not found.",
+        )
+        return Response(
+            json.dumps(response_body),
+            status=404,
+            mimetype="application/json",
         )
-    policy = dict(policy)
-    policy["policy_json"] = json.loads(policy["policy_json"])
-    return dict(
-        status="ok",
-        message=None,
-        result=policy,
-    )
-
 
-def set_policy(
-    country_id: str, policy_id: str, policy_json: dict, label: str = None
-) -> dict:
-    """
-    Set policy data for a given country and policy ID.
+        
+def post_household(country_id: str) -> dict:
+    """Set a household's input data.
 
     Args:
         country_id (str): The country ID.
-        policy_json (dict): The policy data.
-        policy_id (str, optional): The policy ID. Defaults to None.
-        label (str, optional): The policy label. Defaults to None.
     """
     country_not_found = validate_country(country_id)
     if country_not_found:
         return country_not_found
-
-    policy_hash = hash_object(policy_json)
-    match = dict(policy_hash=policy_hash)
-    if policy_id is not None:
-        match["id"] = policy_id
-    # Don't allow changes to policies with IDs 1, 2, or 3.
-    if policy_id in [1, 2, 3]:
-        return dict(
-            status="error",
-            message=f"Cannot change policy with ID {policy_id}",
+    
+    payload = request.json
+    label = payload.get("label")
+    household_json = payload.get("data")
+    household_hash = hash_object(household_json)
+    api_version = COUNTRY_PACKAGE_VERSIONS.get(country_id)
+
+    try:
+        database.query(
+            f"INSERT INTO household (country_id, household_json, household_hash, label, api_version) VALUES (?, ?, ?, ?, ?)",
+            (country_id, json.dumps(household_json), household_hash, label, api_version),
         )
-    # Check if the policy already exists and has a label.
-    existing_policy = database.get_in_table(
-        "policy", country_id=country_id, policy_hash=policy_hash
-    )
-    if existing_policy is not None:
-        if existing_policy["label"] is not None:
-            # If the submitted policy JSON contains a label, check that it matches the existing label.
-            if label is not None and label != existing_policy["label"]:
-                return dict(
-                    status="error",
-                    message=f"Policy already exists with label {existing_policy['label']}. Once a policy has a label, it cannot be changed.",
-                )
-        else:
-            policy_id = existing_policy["id"]
-    database.set_in_table(
-        "policy",
-        match,
-        dict(
-            country_id=country_id,
-            policy_json=json.dumps(policy_json),
-            label=label,
-            api_version=COUNTRY_PACKAGE_VERSIONS[country_id],
-        ),
-        auto_increment="id",
-    )
+    except sqlalchemy.exc.IntegrityError:
+        pass
+
+    household_id = database.query(
+        f"SELECT id FROM household WHERE country_id = ? AND household_hash = ?",
+        (country_id, household_hash),
+    ).fetchone()["id"]
 
-    policy_id = database.get_in_table(
-        "policy", country_id=country_id, policy_hash=policy_hash
-    )["id"]
     return dict(
         status="ok",
         message=None,
         result=dict(
-            policy_id=policy_id,
+            household_id=household_id,
         ),
     )
 
-
-def create_policy_reform(country_id: str, policy_data: dict) -> dict:
-    """
-    Create a policy reform.
+def get_household_under_policy(country_id: str, household_id: str, policy_id: str):
+    """Get a household's output data under a given policy.
 
     Args:
         country_id (str): The country ID.
-        policy_data (dict): The policy data.
-
-    Returns:
-        dict: The reform.
+        household_id (str): The household ID.
+        policy_id (str): The policy ID.
     """
-    country_not_found = validate_country(country_id)
-    if country_not_found:
-        return country_not_found
+    invalid_country = validate_country(country_id)
+    if invalid_country:
+        return invalid_country
+    
+    api_version = COUNTRY_PACKAGE_VERSIONS.get(country_id)
+
+    # Look in computed_households to see if already computed
+
+    row = database.query(
+        f"SELECT * FROM computed_household WHERE household_id = ? AND policy_id = ? AND api_version = ?",
+        (household_id, policy_id, api_version),
+    ).fetchone()
+
+    if row is not None:
+        result = dict(row)
+        result["result"] = json.loads(result["computed_household_json"])
+        return dict(
+            status="ok",
+            message=None,
+            result=result,
+        )
 
-    def modify_parameters(parameters: ParameterNode) -> ParameterNode:
-        for path, values in policy_data.items():
-            node = parameters
-            for step in path.split("."):
-                if "[" in step:
-                    step, index = step.split("[")
-                    index = int(index[:-1])
-                    node = node.children[step].brackets[index]
-                else:
-                    node = node.children[step]
-            for period, value in values.items():
-                start, end = period.split(".")
-                node_type = type(node.values_list[-1].value)
-                if node_type == int:
-                    node_type = float  # '0' is of type int by default, but usually we want to cast to float.
-                node.update(
-                    start=instant(start),
-                    stop=instant(end),
-                    value=node_type(value),
-                )
-
-        return parameters
-
-    class reform(Reform):
-        def apply(self):
-            self.modify_parameters(modify_parameters)
 
-    return reform
+    # Retrieve from the household table
 
+    row = database.query(
+        f"SELECT * FROM household WHERE id = ? AND country_id = ?",
+        (household_id, country_id),
+    ).fetchone()
+
+    if row is not None:
+        household = dict(row)
+        household["household_json"] = json.loads(household["household_json"])
+    else:
+        response_body = dict(
+            status="error",
+            message=f"Household #{household_id} not found.",
+        )
+        return Response(
+            json.dumps(response_body),
+            status=404,
+            mimetype="application/json",
+        )
+    
+    # Retrieve from the policy table
 
-def search_policies(country_id: str, query: str) -> list:
-    """
-    Search for policies.
+    row = database.query(
+        f"SELECT * FROM policy WHERE id = ? AND country_id = ?",
+        (policy_id, country_id),
+    ).fetchone()
+
+    if row is not None:
+        policy = dict(row)
+        policy["policy_json"] = json.loads(policy["policy_json"])
+    else:
+        response_body = dict(
+            status="error",
+            message=f"Policy #{policy_id} not found.",
+        )
+        return Response(
+            json.dumps(response_body),
+            status=404,
+            mimetype="application/json",
+        )
+
+    country = COUNTRIES.get(country_id)
+
+    try:
+        result = country.calculate(household["household_json"], policy["policy_json"])
+    except Exception as e:
+        logging.exception(e)
+        response_body = dict(
+            status="error",
+            message=f"Error calculating household #{household_id} under policy #{policy_id}: {e}",
+        )
+        return Response(
+            json.dumps(response_body),
+            status=500,
+            mimetype="application/json",
+        )
+    
+    # Store the result in the computed_household table
+
+
+    try:
+        database.query(
+            f"INSERT INTO computed_household (country_id, household_id, policy_id, computed_household_json, api_version) VALUES (?, ?, ?, ?, ?)",
+            (country_id, household_id, policy_id, json.dumps(result), api_version),
+        )
+    except sqlalchemy.exc.IntegrityError:
+        # Update the result if it already exists
+        database.query(
+            f"UPDATE computed_household SET computed_household_json = ? WHERE country_id = ? AND household_id = ? AND policy_id = ?",
+            (json.dumps(result), country_id, household_id, policy_id),
+        )
+
+    return dict(
+        status="ok",
+        message=None,
+        result=result,
+    )
+
+def get_calculate(country_id: str) -> dict:
+    """Lightweight endpoint for passing in household and policy JSON objects and calculating without storing data.
 
     Args:
         country_id (str): The country ID.
-        query (str): The search query.
-
-    Returns:
-        list: The search results.
     """
+
     country_not_found = validate_country(country_id)
     if country_not_found:
         return country_not_found
 
-    results = database.query(
-        "SELECT id, label FROM policy WHERE country_id = ? AND label LIKE ?",
-        (country_id, f"%{query}%"),
-    )
-    if results is None:
-        return dict(
+    payload = request.json
+    household_json = payload.get("household", {})
+    policy_json = payload.get("policy", {})
+
+    country = COUNTRIES.get(country_id)
+
+    try:
+        result = country.calculate(household_json, policy_json)
+    except Exception as e:
+        logging.exception(e)
+        response_body = dict(
             status="error",
-            message=f"Policy not found in {country_id}",
+            message=f"Error calculating household under policy: {e}",
         )
-    else:
-        results = results.fetchall()
-    # Format into: [{ id: 1, label: "My policy" }, ...]
-    policies = [dict(id=result[0], label=result[1]) for result in results]
+        return Response(
+            json.dumps(response_body),
+            status=500,
+            mimetype="application/json",
+        )
+
     return dict(
         status="ok",
         message=None,
-        result=policies,
-    )
-
-
-def get_current_law_policy_id(country_id: str) -> int:
-    policy_hash = hash_object({})
-    return database.query(
-        "SELECT id FROM policy WHERE country_id = ? AND policy_hash = ?",
-        (country_id, policy_hash),
-    ).fetchone()[0]
+        result=result,
+    )
```

### Comparing `policyengine-api-0.12.2/setup.py` & `policyengine-api-1.0.0/setup.py`

 * *Files 16% similar despite different names*

```diff
@@ -9,20 +9,22 @@
     description="PolicyEngine API",
     packages=find_packages(),
     install_requires=[
         "click>=8",
         "flask>=1",
         "flask-cors>=3",
         "PolicyEngine-Core>=2,<3",
-        "policyengine_uk==0.44.2",
-        "policyengine_us==0.254.1",
-        "policyengine_canada==0.42.3",
+        "policyengine_uk==0.45.0",
+        "policyengine_us==0.271.0",
+        "policyengine_canada==0.44.0",
         "policyengine-ng==0.4.2",
         "gunicorn",
         "cloud-sql-python-connector",
         "google-cloud-logging",
         "pymysql",
         "sqlalchemy>=1.4,<2",
         "streamlit",
         "markupsafe==2.0.1",
+        "openai",
+        "rq",
     ],
 )
```

