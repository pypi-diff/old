# Comparing `tmp/djangoldp_needle-0.1.8.tar.gz` & `tmp/djangoldp_needle-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/djangoldp_needle-0.1.8.tar", last modified: Thu Jan  5 14:05:04 2023, max compression
+gzip compressed data, was "dist/djangoldp_needle-0.1.9.tar", last modified: Thu Jan  5 15:11:29 2023, max compression
```

## Comparing `djangoldp_needle-0.1.8.tar` & `djangoldp_needle-0.1.9.tar`

### file list

```diff
@@ -1,62 +1,63 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 14:05:04.000000 djangoldp_needle-0.1.8/
--rw-rw-rw-   0 root         (0) root         (0)      194 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 14:05:04.000000 djangoldp_needle-0.1.8/djangoldp_needle/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 14:05:04.000000 djangoldp_needle-0.1.8/djangoldp_needle/tests/
--rw-rw-rw-   0 root         (0) root         (0)     4967 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/tests/test_annotation_add.py
--rw-rw-rw-   0 root         (0) root         (0)      876 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/tests/test_first_annotation_on_user_creation.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/tests/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     7084 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/tests/test_annotation_target_add.py
--rw-rw-rw-   0 root         (0) root         (0)    10736 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/tests/test_annotation_activity.py
--rw-rw-rw-   0 root         (0) root         (0)     1233 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/tests/runner.py
--rw-rw-rw-   0 root         (0) root         (0)       33 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/admin.py
--rw-rw-rw-   0 root         (0) root         (0)      782 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/djangoldp_urls.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2023-01-05 14:05:01.000000 djangoldp_needle-0.1.8/djangoldp_needle/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 14:05:04.000000 djangoldp_needle-0.1.8/djangoldp_needle/request_parser/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 14:05:04.000000 djangoldp_needle-0.1.8/djangoldp_needle/request_parser/parsers/
--rw-rw-rw-   0 root         (0) root         (0)      893 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/request_parser/parsers/opengraph.py
--rw-rw-rw-   0 root         (0) root         (0)       76 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/request_parser/parsers/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      185 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/request_parser/parsers/abstract_parser.py
--rw-rw-rw-   0 root         (0) root         (0)       42 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/request_parser/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      685 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/request_parser/request_parser.py
--rw-rw-rw-   0 root         (0) root         (0)      106 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/apps.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 14:05:04.000000 djangoldp_needle-0.1.8/djangoldp_needle/views/
--rw-rw-rw-   0 root         (0) root         (0)     1696 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/views/annotation_target_intersection.py
--rw-rw-rw-   0 root         (0) root         (0)     3392 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/views/annotation.py
--rw-rw-rw-   0 root         (0) root         (0)      314 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/views/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)       93 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/views/needle_user_profile.py
--rw-rw-rw-   0 root         (0) root         (0)      570 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/views/needle_activity.py
--rw-rw-rw-   0 root         (0) root         (0)     2216 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/views/annotation_target.py
--rw-rw-rw-   0 root         (0) root         (0)      156 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/views/tag.py
--rw-rw-rw-   0 root         (0) root         (0)      262 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/djangoldp_settings.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 14:05:04.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/
--rw-rw-rw-   0 root         (0) root         (0)      413 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0004_annotationtarget_image.py
--rw-rw-rw-   0 root         (0) root         (0)      422 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0012_needleactivity_activity_type.py
--rw-rw-rw-   0 root         (0) root         (0)     2622 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0001_initial.py
--rw-rw-rw-   0 root         (0) root         (0)     1852 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0013_needleuserprofile.py
--rw-rw-rw-   0 root         (0) root         (0)      402 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0009_activity_subtitle.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      404 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0006_auto_20221101_1846.py
--rw-rw-rw-   0 root         (0) root         (0)     1543 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0002_tag.py
--rw-rw-rw-   0 root         (0) root         (0)      584 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0007_auto_20221114_1643.py
--rw-rw-rw-   0 root         (0) root         (0)     1854 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0011_auto_20221125_1015.py
--rw-rw-rw-   0 root         (0) root         (0)      399 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0003_annotation_tags.py
--rw-rw-rw-   0 root         (0) root         (0)      420 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0005_annotationtarget_title.py
--rw-rw-rw-   0 root         (0) root         (0)     1635 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0008_activity.py
--rw-rw-rw-   0 root         (0) root         (0)      396 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/migrations/0010_activity_read.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 14:05:04.000000 djangoldp_needle-0.1.8/djangoldp_needle/models/
--rw-rw-rw-   0 root         (0) root         (0)      980 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/models/annotation.py
--rw-rw-rw-   0 root         (0) root         (0)     3641 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/models/activity_signal_receiver.py
--rw-rw-rw-   0 root         (0) root         (0)      253 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/models/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      803 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/models/needle_user_profile.py
--rw-rw-rw-   0 root         (0) root         (0)     1106 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/models/needle_activity.py
--rw-rw-rw-   0 root         (0) root         (0)      509 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/models/annotation_target.py
--rw-rw-rw-   0 root         (0) root         (0)      624 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/djangoldp_needle/models/tag.py
--rw-rw-rw-   0 root         (0) root         (0)       81 2023-01-05 14:04:46.000000 djangoldp_needle-0.1.8/setup.py
--rw-rw-rw-   0 root         (0) root         (0)      571 2023-01-05 14:05:04.000000 djangoldp_needle-0.1.8/setup.cfg
--rw-r--r--   0 root         (0) root         (0)      399 2023-01-05 14:05:04.000000 djangoldp_needle-0.1.8/PKG-INFO
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 14:05:04.000000 djangoldp_needle-0.1.8/djangoldp_needle.egg-info/
--rw-r--r--   0 root         (0) root         (0)      399 2023-01-05 14:05:03.000000 djangoldp_needle-0.1.8/djangoldp_needle.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)        1 2023-01-05 14:05:03.000000 djangoldp_needle-0.1.8/djangoldp_needle.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)     2232 2023-01-05 14:05:03.000000 djangoldp_needle-0.1.8/djangoldp_needle.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)       17 2023-01-05 14:05:03.000000 djangoldp_needle-0.1.8/djangoldp_needle.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       78 2023-01-05 14:05:03.000000 djangoldp_needle-0.1.8/djangoldp_needle.egg-info/requires.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/
+-rw-rw-rw-   0 root         (0) root         (0)      194 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle/tests/
+-rw-rw-rw-   0 root         (0) root         (0)     4967 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/tests/test_annotation_add.py
+-rw-rw-rw-   0 root         (0) root         (0)      876 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/tests/test_first_annotation_on_user_creation.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/tests/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     7084 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/tests/test_annotation_target_add.py
+-rw-rw-rw-   0 root         (0) root         (0)    10736 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/tests/test_annotation_activity.py
+-rw-rw-rw-   0 root         (0) root         (0)     1233 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/tests/runner.py
+-rw-rw-rw-   0 root         (0) root         (0)       33 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/admin.py
+-rw-rw-rw-   0 root         (0) root         (0)      782 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/djangoldp_urls.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2023-01-05 15:11:27.000000 djangoldp_needle-0.1.9/djangoldp_needle/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle/request_parser/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle/request_parser/parsers/
+-rw-rw-rw-   0 root         (0) root         (0)      893 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/request_parser/parsers/opengraph.py
+-rw-rw-rw-   0 root         (0) root         (0)       76 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/request_parser/parsers/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      185 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/request_parser/parsers/abstract_parser.py
+-rw-rw-rw-   0 root         (0) root         (0)       42 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/request_parser/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      685 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/request_parser/request_parser.py
+-rw-rw-rw-   0 root         (0) root         (0)      106 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/apps.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle/views/
+-rw-rw-rw-   0 root         (0) root         (0)     1696 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/views/annotation_target_intersection.py
+-rw-rw-rw-   0 root         (0) root         (0)     3392 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/views/annotation.py
+-rw-rw-rw-   0 root         (0) root         (0)      314 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/views/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)       93 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/views/needle_user_profile.py
+-rw-rw-rw-   0 root         (0) root         (0)      570 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/views/needle_activity.py
+-rw-rw-rw-   0 root         (0) root         (0)     2216 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/views/annotation_target.py
+-rw-rw-rw-   0 root         (0) root         (0)      156 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/views/tag.py
+-rw-rw-rw-   0 root         (0) root         (0)      262 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/djangoldp_settings.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/
+-rw-rw-rw-   0 root         (0) root         (0)      413 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0004_annotationtarget_image.py
+-rw-rw-rw-   0 root         (0) root         (0)      422 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0012_needleactivity_activity_type.py
+-rw-rw-rw-   0 root         (0) root         (0)     2622 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0001_initial.py
+-rw-rw-rw-   0 root         (0) root         (0)     1852 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0013_needleuserprofile.py
+-rw-rw-rw-   0 root         (0) root         (0)      402 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0009_activity_subtitle.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      404 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0006_auto_20221101_1846.py
+-rw-rw-rw-   0 root         (0) root         (0)     1543 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0002_tag.py
+-rw-rw-rw-   0 root         (0) root         (0)      543 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0014_auto_20230105_1238.py
+-rw-rw-rw-   0 root         (0) root         (0)      584 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0007_auto_20221114_1643.py
+-rw-rw-rw-   0 root         (0) root         (0)     1854 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0011_auto_20221125_1015.py
+-rw-rw-rw-   0 root         (0) root         (0)      399 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0003_annotation_tags.py
+-rw-rw-rw-   0 root         (0) root         (0)      420 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0005_annotationtarget_title.py
+-rw-rw-rw-   0 root         (0) root         (0)     1635 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0008_activity.py
+-rw-rw-rw-   0 root         (0) root         (0)      396 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/migrations/0010_activity_read.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle/models/
+-rw-rw-rw-   0 root         (0) root         (0)      980 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/models/annotation.py
+-rw-rw-rw-   0 root         (0) root         (0)     3641 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/models/activity_signal_receiver.py
+-rw-rw-rw-   0 root         (0) root         (0)      253 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/models/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      803 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/models/needle_user_profile.py
+-rw-rw-rw-   0 root         (0) root         (0)     1106 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/models/needle_activity.py
+-rw-rw-rw-   0 root         (0) root         (0)      509 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/models/annotation_target.py
+-rw-rw-rw-   0 root         (0) root         (0)      624 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/djangoldp_needle/models/tag.py
+-rw-rw-rw-   0 root         (0) root         (0)       81 2023-01-05 15:11:12.000000 djangoldp_needle-0.1.9/setup.py
+-rw-rw-rw-   0 root         (0) root         (0)      571 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)      399 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      399 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)        1 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)     2287 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)       17 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       78 2023-01-05 15:11:29.000000 djangoldp_needle-0.1.9/djangoldp_needle.egg-info/requires.txt
```

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/tests/test_annotation_add.py` & `djangoldp_needle-0.1.9/djangoldp_needle/tests/test_annotation_add.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/tests/test_first_annotation_on_user_creation.py` & `djangoldp_needle-0.1.9/djangoldp_needle/tests/test_first_annotation_on_user_creation.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/tests/test_annotation_target_add.py` & `djangoldp_needle-0.1.9/djangoldp_needle/tests/test_annotation_target_add.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/tests/test_annotation_activity.py` & `djangoldp_needle-0.1.9/djangoldp_needle/tests/test_annotation_activity.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/tests/runner.py` & `djangoldp_needle-0.1.9/djangoldp_needle/tests/runner.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/djangoldp_urls.py` & `djangoldp_needle-0.1.9/djangoldp_needle/djangoldp_urls.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/request_parser/parsers/opengraph.py` & `djangoldp_needle-0.1.9/djangoldp_needle/request_parser/parsers/opengraph.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/request_parser/request_parser.py` & `djangoldp_needle-0.1.9/djangoldp_needle/request_parser/request_parser.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/views/annotation_target_intersection.py` & `djangoldp_needle-0.1.9/djangoldp_needle/views/annotation_target_intersection.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/views/annotation.py` & `djangoldp_needle-0.1.9/djangoldp_needle/views/annotation.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/views/needle_activity.py` & `djangoldp_needle-0.1.9/djangoldp_needle/views/needle_activity.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/views/annotation_target.py` & `djangoldp_needle-0.1.9/djangoldp_needle/views/annotation_target.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/migrations/0001_initial.py` & `djangoldp_needle-0.1.9/djangoldp_needle/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/migrations/0013_needleuserprofile.py` & `djangoldp_needle-0.1.9/djangoldp_needle/migrations/0013_needleuserprofile.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/migrations/0002_tag.py` & `djangoldp_needle-0.1.9/djangoldp_needle/migrations/0002_tag.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/migrations/0007_auto_20221114_1643.py` & `djangoldp_needle-0.1.9/djangoldp_needle/migrations/0007_auto_20221114_1643.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/migrations/0011_auto_20221125_1015.py` & `djangoldp_needle-0.1.9/djangoldp_needle/migrations/0011_auto_20221125_1015.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/migrations/0008_activity.py` & `djangoldp_needle-0.1.9/djangoldp_needle/migrations/0008_activity.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/models/annotation.py` & `djangoldp_needle-0.1.9/djangoldp_needle/models/annotation.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/models/activity_signal_receiver.py` & `djangoldp_needle-0.1.9/djangoldp_needle/models/activity_signal_receiver.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/models/needle_user_profile.py` & `djangoldp_needle-0.1.9/djangoldp_needle/models/needle_user_profile.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/models/needle_activity.py` & `djangoldp_needle-0.1.9/djangoldp_needle/models/needle_activity.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle/models/tag.py` & `djangoldp_needle-0.1.9/djangoldp_needle/models/tag.py`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/setup.cfg` & `djangoldp_needle-0.1.9/setup.cfg`

 * *Files identical despite different names*

### Comparing `djangoldp_needle-0.1.8/djangoldp_needle.egg-info/SOURCES.txt` & `djangoldp_needle-0.1.9/djangoldp_needle.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -20,14 +20,15 @@
 djangoldp_needle/migrations/0007_auto_20221114_1643.py
 djangoldp_needle/migrations/0008_activity.py
 djangoldp_needle/migrations/0009_activity_subtitle.py
 djangoldp_needle/migrations/0010_activity_read.py
 djangoldp_needle/migrations/0011_auto_20221125_1015.py
 djangoldp_needle/migrations/0012_needleactivity_activity_type.py
 djangoldp_needle/migrations/0013_needleuserprofile.py
+djangoldp_needle/migrations/0014_auto_20230105_1238.py
 djangoldp_needle/migrations/__init__.py
 djangoldp_needle/models/__init__.py
 djangoldp_needle/models/activity_signal_receiver.py
 djangoldp_needle/models/annotation.py
 djangoldp_needle/models/annotation_target.py
 djangoldp_needle/models/needle_activity.py
 djangoldp_needle/models/needle_user_profile.py
```

