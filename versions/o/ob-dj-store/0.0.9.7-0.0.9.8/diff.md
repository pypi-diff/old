# Comparing `tmp/ob-dj-store-0.0.9.7.tar.gz` & `tmp/ob-dj-store-0.0.9.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ob-dj-store-0.0.9.7.tar", last modified: Tue Sep 20 10:27:15 2022, max compression
+gzip compressed data, was "ob-dj-store-0.0.9.8.tar", last modified: Thu Sep 22 11:37:48 2022, max compression
```

## Comparing `ob-dj-store-0.0.9.7.tar` & `ob-dj-store-0.0.9.8.tar`

### file list

```diff
@@ -1,151 +1,151 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.735739 ob-dj-store-0.0.9.7/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.727739 ob-dj-store-0.0.9.7/.github/
--rw-r--r--   0 runner    (1001) docker     (121)      273 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/.github/dependabot.yml
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.727739 ob-dj-store-0.0.9.7/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (121)      947 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/.github/workflows/docs.yml
--rw-r--r--   0 runner    (1001) docker     (121)     1348 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/.github/workflows/pre-release.yml
--rw-r--r--   0 runner    (1001) docker     (121)     1953 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/.github/workflows/release.yml
--rw-r--r--   0 runner    (1001) docker     (121)      948 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/.github/workflows/test-build.yml
--rw-r--r--   0 runner    (1001) docker     (121)      186 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/.gitignore
--rw-r--r--   0 runner    (1001) docker     (121)      242 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/.isort.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1322 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (121)     1195 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/Dockerfile
--rw-r--r--   0 runner    (1001) docker     (121)       30 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     2456 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/Makefile
--rw-r--r--   0 runner    (1001) docker     (121)     2639 2022-09-20 10:27:15.735739 ob-dj-store-0.0.9.7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1263 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/Pipfile
--rw-r--r--   0 runner    (1001) docker     (121)    85388 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/Pipfile.lock
--rw-r--r--   0 runner    (1001) docker     (121)     1832 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.727739 ob-dj-store-0.0.9.7/config/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12535 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/config/settings.py
--rw-r--r--   0 runner    (1001) docker     (121)      759 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/config/urls.py
--rw-r--r--   0 runner    (1001) docker     (121)      387 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/config/wsgi.py
--rw-r--r--   0 runner    (1001) docker     (121)       97 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/docker-compose.env
--rw-r--r--   0 runner    (1001) docker     (121)      876 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/docker-compose.yml
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.727739 ob-dj-store-0.0.9.7/docs/
--rw-r--r--   0 runner    (1001) docker     (121)      637 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/docs/Makefile
--rw-r--r--   0 runner    (1001) docker     (121)      763 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/docs/make.bat
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.727739 ob-dj-store-0.0.9.7/docs/source/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/docs/source/admin.rst
--rw-r--r--   0 runner    (1001) docker     (121)     1211 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/docs/source/conf.py
--rw-r--r--   0 runner    (1001) docker     (121)      321 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/docs/source/index.rst
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/docs/source/installation.rst
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/docs/source/models.rst
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/docs/source/rest_endpoints.rst
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.727739 ob-dj-store-0.0.9.7/fixtures/
--rw-r--r--   0 runner    (1001) docker     (121)      407 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/fixtures/initial_users.yaml
--rw-r--r--   0 runner    (1001) docker     (121)      890 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/fixtures/stores.yaml
--rwxr-xr-x   0 runner    (1001) docker     (121)     1028 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/manage.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.727739 ob-dj-store-0.0.9.7/ob_dj_store/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.727739 ob-dj-store-0.0.9.7/ob_dj_store/apis/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/apis/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.727739 ob-dj-store-0.0.9.7/ob_dj_store/apis/stores/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/apis/stores/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3135 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/apis/stores/filters.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.723739 ob-dj-store-0.0.9.7/ob_dj_store/apis/stores/rest/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.731739 ob-dj-store-0.0.9.7/ob_dj_store/apis/stores/rest/serializers/
--rw-r--r--   0 runner    (1001) docker     (121)    23720 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/apis/stores/rest/serializers/serializers.py
--rw-r--r--   0 runner    (1001) docker     (121)     1425 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/apis/stores/urls.py
--rw-r--r--   0 runner    (1001) docker     (121)    19873 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/apis/stores/views.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.731739 ob-dj-store-0.0.9.7/ob_dj_store/apis/tap/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/apis/tap/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1080 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/apis/tap/serializers.py
--rw-r--r--   0 runner    (1001) docker     (121)      367 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/apis/tap/urls.py
--rw-r--r--   0 runner    (1001) docker     (121)     2666 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/apis/tap/views.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.731739 ob-dj-store-0.0.9.7/ob_dj_store/core/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.731739 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/
--rw-r--r--   0 runner    (1001) docker     (121)       65 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9147 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/admin.py
--rw-r--r--   0 runner    (1001) docker     (121)      434 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/apps.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.731739 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.731739 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/
--rw-r--r--   0 runner    (1001) docker     (121)       40 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      384 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/admin.py
--rw-r--r--   0 runner    (1001) docker     (121)      212 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/apps.py
--rw-r--r--   0 runner    (1001) docker     (121)      830 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/managers.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.731739 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/migrations/
--rw-r--r--   0 runner    (1001) docker     (121)     4808 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/migrations/0001_initial.py
--rw-r--r--   0 runner    (1001) docker     (121)      674 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/migrations/0002_auto_20220815_1610.py
--rw-r--r--   0 runner    (1001) docker     (121)      598 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/migrations/0003_auto_20220818_1938.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/migrations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3449 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/models.py
--rw-r--r--   0 runner    (1001) docker     (121)     2427 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/utils.py
--rw-r--r--   0 runner    (1001) docker     (121)     5641 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/managers.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.735739 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/
--rwxr-xr-x   0 runner    (1001) docker     (121)     2154 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0001_initial.py
--rwxr-xr-x   0 runner    (1001) docker     (121)      382 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0002_auto_20220422_0205.py
--rw-r--r--   0 runner    (1001) docker     (121)     1901 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0003_openinghours.py
--rw-r--r--   0 runner    (1001) docker     (121)      379 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0004_auto_20220422_2326.py
--rw-r--r--   0 runner    (1001) docker     (121)     1334 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0005_auto_20220425_2119.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     1049 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0005_auto_20220427_1729.py
--rw-r--r--   0 runner    (1001) docker     (121)    10941 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0006_auto_20220428_0100.py
--rw-r--r--   0 runner    (1001) docker     (121)     5587 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0007_cart_cartitem_order_orderitem.py
--rw-r--r--   0 runner    (1001) docker     (121)      870 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0008_order_status.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     1846 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0009_auto_20220508_2142.py
--rwxr-xr-x   0 runner    (1001) docker     (121)      893 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0010_auto_20220509_1633.py
--rw-r--r--   0 runner    (1001) docker     (121)     1841 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0011_favorite.py
--rw-r--r--   0 runner    (1001) docker     (121)     5640 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0012_auto_20220514_0633.py
--rw-r--r--   0 runner    (1001) docker     (121)     3098 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0013_auto_20220518_1539.py
--rw-r--r--   0 runner    (1001) docker     (121)     2888 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0014_auto_20220519_0018.py
--rw-r--r--   0 runner    (1001) docker     (121)     4368 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0015_inventory_inventoryoperations.py
--rw-r--r--   0 runner    (1001) docker     (121)      521 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0016_productvariant_preparation_time.py
--rw-r--r--   0 runner    (1001) docker     (121)     2860 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0017_auto_20220524_0912.py
--rwxr-xr-x   0 runner    (1001) docker     (121)      552 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0018_auto_20220524_1613.py
--rwxr-xr-x   0 runner    (1001) docker     (121)      393 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0019_product_is_featured.py
--rw-r--r--   0 runner    (1001) docker     (121)     1947 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0020_orderhistory.py
--rw-r--r--   0 runner    (1001) docker     (121)     1726 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0021_auto_20220531_1849.py
--rw-r--r--   0 runner    (1001) docker     (121)      425 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0022_order_pickup_time.py
--rw-r--r--   0 runner    (1001) docker     (121)     4025 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0023_feedback_feedbackattribute_feedbackconfig.py
--rw-r--r--   0 runner    (1001) docker     (121)      984 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0024_auto_20220609_1552.py
--rw-r--r--   0 runner    (1001) docker     (121)      399 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0025_productvariant_is_primary.py
--rw-r--r--   0 runner    (1001) docker     (121)     2934 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0026_auto_20220630_1913.py
--rw-r--r--   0 runner    (1001) docker     (121)      986 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0027_auto_20220713_1759.py
--rw-r--r--   0 runner    (1001) docker     (121)     1762 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0028_phonecontact.py
--rw-r--r--   0 runner    (1001) docker     (121)      691 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0029_auto_20220726_1750.py
--rw-r--r--   0 runner    (1001) docker     (121)      620 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0030_category_parent.py
--rw-r--r--   0 runner    (1001) docker     (121)     1252 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0031_auto_20220811_1733.py
--rw-r--r--   0 runner    (1001) docker     (121)     1079 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0032_auto_20220812_1951.py
--rw-r--r--   0 runner    (1001) docker     (121)     1587 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0033_auto_20220815_0133.py
--rw-r--r--   0 runner    (1001) docker     (121)      745 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0034_auto_20220815_1528.py
--rw-r--r--   0 runner    (1001) docker     (121)      805 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0035_auto_20220818_1938.py
--rw-r--r--   0 runner    (1001) docker     (121)      403 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0036_productattribute_is_mandatory.py
--rw-r--r--   0 runner    (1001) docker     (121)     2432 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0037_auto_20220825_1736.py
--rw-r--r--   0 runner    (1001) docker     (121)      399 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0038_cartitem_extra_infos.py
--rw-r--r--   0 runner    (1001) docker     (121)      770 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0039_auto_20220831_1521.py
--rw-r--r--   0 runner    (1001) docker     (121)      640 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0040_auto_20220902_1806.py
--rw-r--r--   0 runner    (1001) docker     (121)     1476 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0041_auto_20220912_1506.py
--rw-r--r--   0 runner    (1001) docker     (121)     2623 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0042_wallet_wallettransaction.py
--rw-r--r--   0 runner    (1001) docker     (121)     1016 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0043_auto_20220919_1854.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.735739 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/
--rw-r--r--   0 runner    (1001) docker     (121)     1532 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1661 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_address.py
--rw-r--r--   0 runner    (1001) docker     (121)     3911 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_cart.py
--rw-r--r--   0 runner    (1001) docker     (121)     1535 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_favorite.py
--rw-r--r--   0 runner    (1001) docker     (121)     1472 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_feedback.py
--rw-r--r--   0 runner    (1001) docker     (121)     3577 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_inventory.py
--rw-r--r--   0 runner    (1001) docker     (121)     7541 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_order.py
--rw-r--r--   0 runner    (1001) docker     (121)     4463 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_payment.py
--rw-r--r--   0 runner    (1001) docker     (121)     8528 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_product.py
--rw-r--r--   0 runner    (1001) docker     (121)     6364 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_store.py
--rw-r--r--   0 runner    (1001) docker     (121)     2285 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_wallet.py
--rw-r--r--   0 runner    (1001) docker     (121)      849 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/receivers.py
--rw-r--r--   0 runner    (1001) docker     (121)      327 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/settings_validation.py
--rw-r--r--   0 runner    (1001) docker     (121)     1143 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/core/stores/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.735739 ob-dj-store-0.0.9.7/ob_dj_store/utils/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      842 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/utils/helpers.py
--rw-r--r--   0 runner    (1001) docker     (121)      303 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/ob_dj_store/utils/model.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 10:27:15.727739 ob-dj-store-0.0.9.7/ob_dj_store.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2639 2022-09-20 10:27:15.000000 ob-dj-store-0.0.9.7/ob_dj_store.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     5411 2022-09-20 10:27:15.000000 ob-dj-store-0.0.9.7/ob_dj_store.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-20 10:27:15.000000 ob-dj-store-0.0.9.7/ob_dj_store.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       97 2022-09-20 10:27:15.000000 ob-dj-store-0.0.9.7/ob_dj_store.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       12 2022-09-20 10:27:15.000000 ob-dj-store-0.0.9.7/ob_dj_store.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      160 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/pytest.ini
--rw-r--r--   0 runner    (1001) docker     (121)      847 2022-09-20 10:27:15.739739 ob-dj-store-0.0.9.7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)      551 2022-09-20 10:26:56.000000 ob-dj-store-0.0.9.7/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.322634 ob-dj-store-0.0.9.8/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.310634 ob-dj-store-0.0.9.8/.github/
+-rw-r--r--   0 runner    (1001) docker     (121)      273 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/.github/dependabot.yml
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.310634 ob-dj-store-0.0.9.8/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (121)      947 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/.github/workflows/docs.yml
+-rw-r--r--   0 runner    (1001) docker     (121)     1348 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/.github/workflows/pre-release.yml
+-rw-r--r--   0 runner    (1001) docker     (121)     1953 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/.github/workflows/release.yml
+-rw-r--r--   0 runner    (1001) docker     (121)      948 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/.github/workflows/test-build.yml
+-rw-r--r--   0 runner    (1001) docker     (121)      186 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (121)      242 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/.isort.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1322 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/.pre-commit-config.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)     1195 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/Dockerfile
+-rw-r--r--   0 runner    (1001) docker     (121)       30 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     2456 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/Makefile
+-rw-r--r--   0 runner    (1001) docker     (121)     2639 2022-09-22 11:37:48.322634 ob-dj-store-0.0.9.8/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1263 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/Pipfile
+-rw-r--r--   0 runner    (1001) docker     (121)    85388 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/Pipfile.lock
+-rw-r--r--   0 runner    (1001) docker     (121)     1832 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.310634 ob-dj-store-0.0.9.8/config/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12535 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/config/settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)      759 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/config/urls.py
+-rw-r--r--   0 runner    (1001) docker     (121)      387 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/config/wsgi.py
+-rw-r--r--   0 runner    (1001) docker     (121)       97 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/docker-compose.env
+-rw-r--r--   0 runner    (1001) docker     (121)      876 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/docker-compose.yml
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.310634 ob-dj-store-0.0.9.8/docs/
+-rw-r--r--   0 runner    (1001) docker     (121)      637 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/docs/Makefile
+-rw-r--r--   0 runner    (1001) docker     (121)      763 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/docs/make.bat
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.310634 ob-dj-store-0.0.9.8/docs/source/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/docs/source/admin.rst
+-rw-r--r--   0 runner    (1001) docker     (121)     1211 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/docs/source/conf.py
+-rw-r--r--   0 runner    (1001) docker     (121)      321 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/docs/source/index.rst
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/docs/source/installation.rst
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/docs/source/models.rst
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/docs/source/rest_endpoints.rst
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.310634 ob-dj-store-0.0.9.8/fixtures/
+-rw-r--r--   0 runner    (1001) docker     (121)      407 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/fixtures/initial_users.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)      890 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/fixtures/stores.yaml
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1028 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/manage.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.310634 ob-dj-store-0.0.9.8/ob_dj_store/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.310634 ob-dj-store-0.0.9.8/ob_dj_store/apis/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/apis/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.314634 ob-dj-store-0.0.9.8/ob_dj_store/apis/stores/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/apis/stores/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3135 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/apis/stores/filters.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.306634 ob-dj-store-0.0.9.8/ob_dj_store/apis/stores/rest/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.314634 ob-dj-store-0.0.9.8/ob_dj_store/apis/stores/rest/serializers/
+-rw-r--r--   0 runner    (1001) docker     (121)    23992 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/apis/stores/rest/serializers/serializers.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1425 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/apis/stores/urls.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19873 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/apis/stores/views.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.314634 ob-dj-store-0.0.9.8/ob_dj_store/apis/tap/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/apis/tap/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1080 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/apis/tap/serializers.py
+-rw-r--r--   0 runner    (1001) docker     (121)      367 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/apis/tap/urls.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2666 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/apis/tap/views.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.314634 ob-dj-store-0.0.9.8/ob_dj_store/core/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.314634 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/
+-rw-r--r--   0 runner    (1001) docker     (121)       65 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9147 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/admin.py
+-rw-r--r--   0 runner    (1001) docker     (121)      434 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/apps.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.314634 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.314634 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/
+-rw-r--r--   0 runner    (1001) docker     (121)       40 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      384 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/admin.py
+-rw-r--r--   0 runner    (1001) docker     (121)      212 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/apps.py
+-rw-r--r--   0 runner    (1001) docker     (121)      830 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/managers.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.314634 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/migrations/
+-rw-r--r--   0 runner    (1001) docker     (121)     4808 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/migrations/0001_initial.py
+-rw-r--r--   0 runner    (1001) docker     (121)      674 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/migrations/0002_auto_20220815_1610.py
+-rw-r--r--   0 runner    (1001) docker     (121)      598 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/migrations/0003_auto_20220818_1938.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/migrations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3449 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/models.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2427 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5641 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/managers.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.318634 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2154 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0001_initial.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)      382 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0002_auto_20220422_0205.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1901 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0003_openinghours.py
+-rw-r--r--   0 runner    (1001) docker     (121)      379 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0004_auto_20220422_2326.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1334 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0005_auto_20220425_2119.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1049 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0005_auto_20220427_1729.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10941 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0006_auto_20220428_0100.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5587 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0007_cart_cartitem_order_orderitem.py
+-rw-r--r--   0 runner    (1001) docker     (121)      870 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0008_order_status.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1846 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0009_auto_20220508_2142.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)      893 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0010_auto_20220509_1633.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1841 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0011_favorite.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5640 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0012_auto_20220514_0633.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3098 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0013_auto_20220518_1539.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2888 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0014_auto_20220519_0018.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4368 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0015_inventory_inventoryoperations.py
+-rw-r--r--   0 runner    (1001) docker     (121)      521 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0016_productvariant_preparation_time.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2860 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0017_auto_20220524_0912.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)      552 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0018_auto_20220524_1613.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)      393 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0019_product_is_featured.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1947 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0020_orderhistory.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1726 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0021_auto_20220531_1849.py
+-rw-r--r--   0 runner    (1001) docker     (121)      425 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0022_order_pickup_time.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4025 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0023_feedback_feedbackattribute_feedbackconfig.py
+-rw-r--r--   0 runner    (1001) docker     (121)      984 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0024_auto_20220609_1552.py
+-rw-r--r--   0 runner    (1001) docker     (121)      399 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0025_productvariant_is_primary.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2934 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0026_auto_20220630_1913.py
+-rw-r--r--   0 runner    (1001) docker     (121)      986 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0027_auto_20220713_1759.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1762 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0028_phonecontact.py
+-rw-r--r--   0 runner    (1001) docker     (121)      691 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0029_auto_20220726_1750.py
+-rw-r--r--   0 runner    (1001) docker     (121)      620 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0030_category_parent.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1252 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0031_auto_20220811_1733.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1079 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0032_auto_20220812_1951.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1587 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0033_auto_20220815_0133.py
+-rw-r--r--   0 runner    (1001) docker     (121)      745 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0034_auto_20220815_1528.py
+-rw-r--r--   0 runner    (1001) docker     (121)      805 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0035_auto_20220818_1938.py
+-rw-r--r--   0 runner    (1001) docker     (121)      403 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0036_productattribute_is_mandatory.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2432 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0037_auto_20220825_1736.py
+-rw-r--r--   0 runner    (1001) docker     (121)      399 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0038_cartitem_extra_infos.py
+-rw-r--r--   0 runner    (1001) docker     (121)      770 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0039_auto_20220831_1521.py
+-rw-r--r--   0 runner    (1001) docker     (121)      640 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0040_auto_20220902_1806.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1476 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0041_auto_20220912_1506.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2623 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0042_wallet_wallettransaction.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1016 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0043_auto_20220919_1854.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.318634 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/
+-rw-r--r--   0 runner    (1001) docker     (121)     1532 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1661 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_address.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3911 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_cart.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1535 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_favorite.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1472 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_feedback.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3577 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_inventory.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7541 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_order.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4463 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_payment.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8528 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_product.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6364 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_store.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2285 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_wallet.py
+-rw-r--r--   0 runner    (1001) docker     (121)      849 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/receivers.py
+-rw-r--r--   0 runner    (1001) docker     (121)      327 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/settings_validation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1143 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/core/stores/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.318634 ob-dj-store-0.0.9.8/ob_dj_store/utils/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      842 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/utils/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (121)      303 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/ob_dj_store/utils/model.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 11:37:48.310634 ob-dj-store-0.0.9.8/ob_dj_store.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     2639 2022-09-22 11:37:48.000000 ob-dj-store-0.0.9.8/ob_dj_store.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     5411 2022-09-22 11:37:48.000000 ob-dj-store-0.0.9.8/ob_dj_store.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-22 11:37:48.000000 ob-dj-store-0.0.9.8/ob_dj_store.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       97 2022-09-22 11:37:48.000000 ob-dj-store-0.0.9.8/ob_dj_store.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       12 2022-09-22 11:37:48.000000 ob-dj-store-0.0.9.8/ob_dj_store.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      160 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/pytest.ini
+-rw-r--r--   0 runner    (1001) docker     (121)      847 2022-09-22 11:37:48.322634 ob-dj-store-0.0.9.8/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)      551 2022-09-22 11:37:36.000000 ob-dj-store-0.0.9.8/setup.py
```

### Comparing `ob-dj-store-0.0.9.7/.github/workflows/docs.yml` & `ob-dj-store-0.0.9.8/.github/workflows/docs.yml`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/.github/workflows/pre-release.yml` & `ob-dj-store-0.0.9.8/.github/workflows/pre-release.yml`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/.github/workflows/release.yml` & `ob-dj-store-0.0.9.8/.github/workflows/release.yml`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/.github/workflows/test-build.yml` & `ob-dj-store-0.0.9.8/.github/workflows/test-build.yml`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/.pre-commit-config.yaml` & `ob-dj-store-0.0.9.8/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/Dockerfile` & `ob-dj-store-0.0.9.8/Dockerfile`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/Makefile` & `ob-dj-store-0.0.9.8/Makefile`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/PKG-INFO` & `ob-dj-store-0.0.9.8/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ob-dj-store
-Version: 0.0.9.7
+Version: 0.0.9.8
 Summary: OBytes django application for managing ecommerce stores.
 Home-page: https://www.obytes.com/
 Author: OBytes
 Author-email: hello@obytes.com
 License: BSD-3-Clause
 Classifier: Environment :: Web Environment
 Classifier: Framework :: Django
```

### Comparing `ob-dj-store-0.0.9.7/Pipfile` & `ob-dj-store-0.0.9.8/Pipfile`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/Pipfile.lock` & `ob-dj-store-0.0.9.8/Pipfile.lock`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/README.md` & `ob-dj-store-0.0.9.8/README.md`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/config/settings.py` & `ob-dj-store-0.0.9.8/config/settings.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/config/urls.py` & `ob-dj-store-0.0.9.8/config/urls.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/docker-compose.yml` & `ob-dj-store-0.0.9.8/docker-compose.yml`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/docs/Makefile` & `ob-dj-store-0.0.9.8/docs/Makefile`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/docs/make.bat` & `ob-dj-store-0.0.9.8/docs/make.bat`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/docs/source/conf.py` & `ob-dj-store-0.0.9.8/docs/source/conf.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/fixtures/stores.yaml` & `ob-dj-store-0.0.9.8/fixtures/stores.yaml`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/manage.py` & `ob-dj-store-0.0.9.8/manage.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/apis/stores/filters.py` & `ob-dj-store-0.0.9.8/ob_dj_store/apis/stores/filters.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/apis/stores/rest/serializers/serializers.py` & `ob-dj-store-0.0.9.8/ob_dj_store/apis/stores/rest/serializers/serializers.py`

 * *Files 2% similar despite different names*

```diff
@@ -340,27 +340,30 @@
         if obj.inventories.filter(is_active=True).exists():
             return obj.inventories.filter(is_active=True).values(
                 "price", "store", "discount_percent"
             )
 
 
 class CartItemSerializer(InventoryValidationMixin, serializers.ModelSerializer):
+    image = serializers.SerializerMethodField()
+
     class Meta:
         model = CartItem
         fields = (
             "id",
             "product_variant",
             "quantity",
             "store",
             "unit_price",
             "total_price",
             "notes",
             "attribute_choices",
             "extra_infos",
             "attribute_choices_total_price",
+            "image",
         )
 
     def validate(self, attrs: typing.Dict) -> typing.Dict:
         """
         When creating a Cartitem for physical product variant, we create an instance with the fields (product_variant,quantity, notes,store)
         so in case of digital product variant we need to add json field e.g: extra_infos containing the base infos of the giftee.
         """
@@ -383,14 +386,21 @@
                 for key in settings.DIGITAL_PRODUCTS_REQUIRED_KEYS:
                     if not (key in data.keys() and len(str(data.get(key)))):
                         errors.append({key: "This field should be filled."})
                 if len(errors) > 0:
                     raise serializers.ValidationError(errors)
         return super(CartItemSerializer, self).validate(attrs)
 
+    def get_image(self, obj):
+        qs = ProductMedia.objects.filter(product=obj.product_variant.product)
+        if qs:
+            return qs.first().image.url
+        else:
+            return None
+
     def to_representation(self, instance: CartItem):
         data = super().to_representation(instance)
         data["product_variant"] = ProductVariantSerializer(
             instance=instance.product_variant
         ).data
         data["product_name"] = instance.product_variant.product.name
         data["attribute_choices"] = AttributeChoiceSerializer(
```

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/apis/stores/urls.py` & `ob-dj-store-0.0.9.8/ob_dj_store/apis/stores/urls.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/apis/stores/views.py` & `ob-dj-store-0.0.9.8/ob_dj_store/apis/stores/views.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/apis/tap/serializers.py` & `ob-dj-store-0.0.9.8/ob_dj_store/apis/tap/serializers.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/apis/tap/views.py` & `ob-dj-store-0.0.9.8/ob_dj_store/apis/tap/views.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/admin.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/admin.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/managers.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/managers.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/migrations/0001_initial.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/migrations/0002_auto_20220815_1610.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/migrations/0002_auto_20220815_1610.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/migrations/0003_auto_20220818_1938.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/migrations/0003_auto_20220818_1938.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/models.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/models.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/gateway/tap/utils.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/gateway/tap/utils.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/managers.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/managers.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0001_initial.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0003_openinghours.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0003_openinghours.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0005_auto_20220425_2119.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0005_auto_20220425_2119.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0005_auto_20220427_1729.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0005_auto_20220427_1729.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0006_auto_20220428_0100.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0006_auto_20220428_0100.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0007_cart_cartitem_order_orderitem.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0007_cart_cartitem_order_orderitem.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0008_order_status.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0008_order_status.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0009_auto_20220508_2142.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0009_auto_20220508_2142.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0010_auto_20220509_1633.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0010_auto_20220509_1633.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0011_favorite.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0011_favorite.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0012_auto_20220514_0633.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0012_auto_20220514_0633.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0013_auto_20220518_1539.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0013_auto_20220518_1539.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0014_auto_20220519_0018.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0014_auto_20220519_0018.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0015_inventory_inventoryoperations.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0015_inventory_inventoryoperations.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0016_productvariant_preparation_time.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0016_productvariant_preparation_time.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0017_auto_20220524_0912.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0017_auto_20220524_0912.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0018_auto_20220524_1613.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0018_auto_20220524_1613.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0020_orderhistory.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0020_orderhistory.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0021_auto_20220531_1849.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0021_auto_20220531_1849.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0023_feedback_feedbackattribute_feedbackconfig.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0023_feedback_feedbackattribute_feedbackconfig.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0024_auto_20220609_1552.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0024_auto_20220609_1552.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0026_auto_20220630_1913.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0026_auto_20220630_1913.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0027_auto_20220713_1759.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0027_auto_20220713_1759.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0028_phonecontact.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0028_phonecontact.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0029_auto_20220726_1750.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0029_auto_20220726_1750.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0030_category_parent.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0030_category_parent.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0031_auto_20220811_1733.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0031_auto_20220811_1733.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0032_auto_20220812_1951.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0032_auto_20220812_1951.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0033_auto_20220815_0133.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0033_auto_20220815_0133.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0034_auto_20220815_1528.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0034_auto_20220815_1528.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0035_auto_20220818_1938.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0035_auto_20220818_1938.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0037_auto_20220825_1736.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0037_auto_20220825_1736.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0039_auto_20220831_1521.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0039_auto_20220831_1521.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0040_auto_20220902_1806.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0040_auto_20220902_1806.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0041_auto_20220912_1506.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0041_auto_20220912_1506.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0042_wallet_wallettransaction.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0042_wallet_wallettransaction.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/migrations/0043_auto_20220919_1854.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/migrations/0043_auto_20220919_1854.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/__init__.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/__init__.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_address.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_address.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_cart.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_cart.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_favorite.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_favorite.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_feedback.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_feedback.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_inventory.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_inventory.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_order.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_order.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_payment.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_payment.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_product.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_product.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_store.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_store.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/models/_wallet.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/models/_wallet.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/receivers.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/receivers.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/core/stores/utils.py` & `ob-dj-store-0.0.9.8/ob_dj_store/core/stores/utils.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store/utils/helpers.py` & `ob-dj-store-0.0.9.8/ob_dj_store/utils/helpers.py`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store.egg-info/PKG-INFO` & `ob-dj-store-0.0.9.8/ob_dj_store.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ob-dj-store
-Version: 0.0.9.7
+Version: 0.0.9.8
 Summary: OBytes django application for managing ecommerce stores.
 Home-page: https://www.obytes.com/
 Author: OBytes
 Author-email: hello@obytes.com
 License: BSD-3-Clause
 Classifier: Environment :: Web Environment
 Classifier: Framework :: Django
```

### Comparing `ob-dj-store-0.0.9.7/ob_dj_store.egg-info/SOURCES.txt` & `ob-dj-store-0.0.9.8/ob_dj_store.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/setup.cfg` & `ob-dj-store-0.0.9.8/setup.cfg`

 * *Files identical despite different names*

### Comparing `ob-dj-store-0.0.9.7/setup.py` & `ob-dj-store-0.0.9.8/setup.py`

 * *Files identical despite different names*

