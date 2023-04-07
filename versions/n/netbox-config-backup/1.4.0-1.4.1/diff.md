# Comparing `tmp/netbox_config_backup-1.4.0.tar.gz` & `tmp/netbox_config_backup-1.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "netbox_config_backup-1.4.0.tar", last modified: Sat Dec 31 02:20:50 2022, max compression
+gzip compressed data, was "netbox_config_backup-1.4.1.tar", last modified: Fri Apr  7 02:31:44 2023, max compression
```

## Comparing `netbox_config_backup-1.4.0.tar` & `netbox_config_backup-1.4.1.tar`

### file list

```diff
@@ -1,70 +1,75 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:50.231495 netbox_config_backup-1.4.0/
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      132 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)      539 2022-12-31 02:20:50.231495 netbox_config_backup-1.4.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2287 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:50.223495 netbox_config_backup-1.4.0/netbox_config_backup/
--rw-r--r--   0 runner    (1001) docker     (123)      759 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      443 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/choices.py
--rw-r--r--   0 runner    (1001) docker     (123)     1011 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/filtersets.py
--rw-r--r--   0 runner    (1001) docker     (123)     1482 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/forms.py
--rw-r--r--   0 runner    (1001) docker     (123)     5947 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/git.py
--rw-r--r--   0 runner    (1001) docker     (123)      388 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/helpers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:50.227495 netbox_config_backup-1.4.0/netbox_config_backup/management/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/management/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:50.227495 netbox_config_backup-1.4.0/netbox_config_backup/management/commands/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/management/commands/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      407 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/management/commands/enqueue_if_needed.py
--rw-r--r--   0 runner    (1001) docker     (123)     3313 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/management/commands/fix_missing.py
--rw-r--r--   0 runner    (1001) docker     (123)     3456 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/management/commands/rebuild.py
--rw-r--r--   0 runner    (1001) docker     (123)      562 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/management/commands/runbackup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:50.227495 netbox_config_backup-1.4.0/netbox_config_backup/migrations/
--rw-r--r--   0 runner    (1001) docker     (123)     2171 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/migrations/0001_initial.py
--rw-r--r--   0 runner    (1001) docker     (123)     2699 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/migrations/0002_git_models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1110 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/migrations/0003_primary_model_to_bigid.py
--rw-r--r--   0 runner    (1001) docker     (123)      480 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/migrations/0004_custom_constraints.py
--rw-r--r--   0 runner    (1001) docker     (123)      405 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/migrations/0005_commit_add_time_field.py
--rw-r--r--   0 runner    (1001) docker     (123)      542 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/migrations/0006_backup_add_commit_last_time.py
--rw-r--r--   0 runner    (1001) docker     (123)      520 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/migrations/0007_backup_job_add_scheduled.py
--rw-r--r--   0 runner    (1001) docker     (123)      423 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/migrations/0008_backupjob_scheduled_nullable.py
--rw-r--r--   0 runner    (1001) docker     (123)     4859 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/migrations/0009_bctc_file_model_backup_fk_restructure.py
--rw-r--r--   0 runner    (1001) docker     (123)      569 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/migrations/0010_backup_ip.py
--rw-r--r--   0 runner    (1001) docker     (123)      402 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/migrations/0011_alter_backup_name.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/migrations/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:50.227495 netbox_config_backup-1.4.0/netbox_config_backup/models/
--rw-r--r--   0 runner    (1001) docker     (123)      308 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      150 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/models/abstract.py
--rw-r--r--   0 runner    (1001) docker     (123)     7928 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/models/backups.py
--rw-r--r--   0 runner    (1001) docker     (123)     3637 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/models/jobs.py
--rw-r--r--   0 runner    (1001) docker     (123)      623 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/navigation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1971 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/tables.py
--rw-r--r--   0 runner    (1001) docker     (123)     5682 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/tasks.py
--rw-r--r--   0 runner    (1001) docker     (123)     1050 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/template_content.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:50.223495 netbox_config_backup-1.4.0/netbox_config_backup/templates/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:50.227495 netbox_config_backup-1.4.0/netbox_config_backup/templates/netbox_config_backup/
--rw-r--r--   0 runner    (1001) docker     (123)      971 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/templates/netbox_config_backup/base.html
--rw-r--r--   0 runner    (1001) docker     (123)      395 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/templates/netbox_config_backup/config.html
--rw-r--r--   0 runner    (1001) docker     (123)     2726 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/templates/netbox_config_backup/device.html
--rw-r--r--   0 runner    (1001) docker     (123)     1072 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/templates/netbox_config_backup/diff.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:50.227495 netbox_config_backup-1.4.0/netbox_config_backup/templates/netbox_config_backup/inc/
--rw-r--r--   0 runner    (1001) docker     (123)     1250 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/templates/netbox_config_backup/inc/backup_tables.html
--rw-r--r--   0 runner    (1001) docker     (123)       83 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/templates/netbox_config_backup/repository.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:50.227495 netbox_config_backup-1.4.0/netbox_config_backup/templatetags/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/templatetags/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/templatetags/ncb_split.py
--rw-r--r--   0 runner    (1001) docker     (123)      784 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:50.231495 netbox_config_backup-1.4.0/netbox_config_backup/utils/
--rw-r--r--   0 runner    (1001) docker     (123)      369 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1025 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/utils/backups.py
--rw-r--r--   0 runner    (1001) docker     (123)      519 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/utils/git.py
--rw-r--r--   0 runner    (1001) docker     (123)     6634 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/utils/rq.py
--rw-r--r--   0 runner    (1001) docker     (123)     4525 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/netbox_config_backup/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-31 02:20:50.227495 netbox_config_backup-1.4.0/netbox_config_backup.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      539 2022-12-31 02:20:50.000000 netbox_config_backup-1.4.0/netbox_config_backup.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2509 2022-12-31 02:20:50.000000 netbox_config_backup-1.4.0/netbox_config_backup.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-31 02:20:50.000000 netbox_config_backup-1.4.0/netbox_config_backup.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-31 02:20:50.000000 netbox_config_backup-1.4.0/netbox_config_backup.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       49 2022-12-31 02:20:50.000000 netbox_config_backup-1.4.0/netbox_config_backup.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       21 2022-12-31 02:20:50.000000 netbox_config_backup-1.4.0/netbox_config_backup.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-31 02:20:50.231495 netbox_config_backup-1.4.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      905 2022-12-31 02:20:42.000000 netbox_config_backup-1.4.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.027744 netbox_config_backup-1.4.1/
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)      539 2023-04-07 02:31:44.027744 netbox_config_backup-1.4.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2287 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.019744 netbox_config_backup-1.4.1/netbox_config_backup/
+-rw-r--r--   0 runner    (1001) docker     (123)      759 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      635 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/choices.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2455 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/filtersets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2073 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/forms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5947 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/git.py
+-rw-r--r--   0 runner    (1001) docker     (123)      388 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/helpers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.023744 netbox_config_backup-1.4.1/netbox_config_backup/management/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/management/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.023744 netbox_config_backup-1.4.1/netbox_config_backup/management/commands/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/management/commands/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      407 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/management/commands/enqueue_if_needed.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3313 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/management/commands/fix_missing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3456 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/management/commands/rebuild.py
+-rw-r--r--   0 runner    (1001) docker     (123)      562 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/management/commands/runbackup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.023744 netbox_config_backup-1.4.1/netbox_config_backup/migrations/
+-rw-r--r--   0 runner    (1001) docker     (123)     2171 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/0001_initial.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2699 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/0002_git_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1110 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/0003_primary_model_to_bigid.py
+-rw-r--r--   0 runner    (1001) docker     (123)      480 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/0004_custom_constraints.py
+-rw-r--r--   0 runner    (1001) docker     (123)      405 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/0005_commit_add_time_field.py
+-rw-r--r--   0 runner    (1001) docker     (123)      542 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/0006_backup_add_commit_last_time.py
+-rw-r--r--   0 runner    (1001) docker     (123)      520 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/0007_backup_job_add_scheduled.py
+-rw-r--r--   0 runner    (1001) docker     (123)      423 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/0008_backupjob_scheduled_nullable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4859 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/0009_bctc_file_model_backup_fk_restructure.py
+-rw-r--r--   0 runner    (1001) docker     (123)      569 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/0010_backup_ip.py
+-rw-r--r--   0 runner    (1001) docker     (123)      402 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/0011_alter_backup_name.py
+-rw-r--r--   0 runner    (1001) docker     (123)      414 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/0012_backup_status.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/migrations/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.023744 netbox_config_backup-1.4.1/netbox_config_backup/models/
+-rw-r--r--   0 runner    (1001) docker     (123)      308 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      150 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/models/abstract.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8278 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/models/backups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3637 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/models/jobs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      623 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/navigation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2299 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/tables.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5582 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/tasks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1755 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/template_content.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.019744 netbox_config_backup-1.4.1/netbox_config_backup/templates/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.027744 netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/
+-rw-r--r--   0 runner    (1001) docker     (123)     2712 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/backup.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1235 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/backups.html
+-rw-r--r--   0 runner    (1001) docker     (123)      971 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/base.html
+-rw-r--r--   0 runner    (1001) docker     (123)      395 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/config.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1316 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/diff.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.027744 netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/inc/
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/inc/backup_tables.html
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/repository.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.019744 netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/switch_templates/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.027744 netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/switch_templates/cisco_iosxe/
+-rw-r--r--   0 runner    (1001) docker     (123)     1223 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/switch_templates/cisco_iosxe/interface.tpl
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.027744 netbox_config_backup-1.4.1/netbox_config_backup/templatetags/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/templatetags/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/templatetags/ncb_split.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1051 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.027744 netbox_config_backup-1.4.1/netbox_config_backup/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      369 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1170 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/utils/backups.py
+-rw-r--r--   0 runner    (1001) docker     (123)      519 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/utils/git.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7000 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/utils/rq.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7982 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/netbox_config_backup/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 02:31:44.023744 netbox_config_backup-1.4.1/netbox_config_backup.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      539 2023-04-07 02:31:44.000000 netbox_config_backup-1.4.1/netbox_config_backup.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2723 2023-04-07 02:31:44.000000 netbox_config_backup-1.4.1/netbox_config_backup.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 02:31:44.000000 netbox_config_backup-1.4.1/netbox_config_backup.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 02:31:44.000000 netbox_config_backup-1.4.1/netbox_config_backup.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-07 02:31:44.000000 netbox_config_backup-1.4.1/netbox_config_backup.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       21 2023-04-07 02:31:44.000000 netbox_config_backup-1.4.1/netbox_config_backup.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 02:31:44.027744 netbox_config_backup-1.4.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      905 2023-04-07 02:31:38.000000 netbox_config_backup-1.4.1/setup.py
```

### Comparing `netbox_config_backup-1.4.0/LICENSE` & `netbox_config_backup-1.4.1/LICENSE`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/PKG-INFO` & `netbox_config_backup-1.4.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: netbox_config_backup
-Version: 1.4.0
+Version: 1.4.1
 Summary: NetBox Configuration Backup
 Home-page: https://github.com/dansheps/netbox-config-backup/
 Download-URL: https://github.com/dansheps/netbox-config-backup/
 Author: Daniel Sheppard
 Author-email: dans@dansheps.com
 Maintainer: Daniel Sheppard
 Maintainer-email: dans@dansheps.com
```

### Comparing `netbox_config_backup-1.4.0/README.md` & `netbox_config_backup-1.4.1/README.md`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/__init__.py` & `netbox_config_backup-1.4.1/netbox_config_backup/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -9,15 +9,15 @@
     verbose_name = metadata.get('Summary')
     description = metadata.get('Description')
     version = metadata.get('Version')
     author = metadata.get('Author')
     author_email = metadata.get('Author-email')
     base_url = 'configbackup'
     min_version = '3.2.0'
-    max_version = '3.4.99'
+    max_version = '3.5.99'
     required_settings = [
         'repository',
         'committer',
         'author',
     ]
     default_settings = {
         # Frequency in seconds
```

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/forms.py` & `netbox_config_backup-1.4.1/netbox_config_backup/forms.py`

 * *Files 10% similar despite different names*

```diff
@@ -2,19 +2,19 @@
 from django.forms import CharField
 from django.utils.translation import gettext as _
 
 from dcim.choices import DeviceStatusChoices
 from dcim.models import Device
 from ipam.models import IPAddress
 from netbox_config_backup.models import Backup
-from utilities.forms import BootstrapMixin, DynamicModelChoiceField
+from utilities.forms import BootstrapMixin, DynamicModelChoiceField, DynamicModelMultipleChoiceField
 
-__all = (
-    'VirtualCircuitForm',
-    'VirtualCircuitInterfaceForm',
+__all__ = (
+    'BackupForm',
+    'BackupFilterSetForm',
 )
 
 
 class BackupForm(BootstrapMixin, forms.ModelForm):
     device = DynamicModelChoiceField(
         label='Device',
         required=False,
@@ -31,27 +31,47 @@
         queryset=IPAddress.objects.all(),
         query_params={
             'device_id': '$device'
         }
     )
     class Meta:
         model = Backup
-        fields = ('name', 'device', 'ip')
+        fields = ('name', 'device', 'status', 'ip')
 
     def clean(self):
         super().clean()
         if self.cleaned_data.get('device', None) == None:
             self.cleaned_data['ip'] = None
 
 
-class BackupFiltersetForm(BootstrapMixin, forms.Form):
+class BackupFilterSetForm(BootstrapMixin, forms.Form):
     model = Backup
     field_order = [
-        'q', 'name', 'device'
+        'q', 'name', 'device_id', 'ip'
     ]
     q = forms.CharField(
         required=False,
         widget=forms.TextInput(attrs={'placeholder': _('All Fields')}),
         label=_('Search')
     )
+    device_id = DynamicModelMultipleChoiceField(
+        queryset=Device.objects.all(),
+        required=False,
+        label=_('Device'),
+        fetch_trigger='open',
+        query_params={
+            'status': [DeviceStatusChoices.STATUS_ACTIVE],
+            'platform__napalm__ne': None,
+            'has_primary_ip': True,
+        }
+    )
+    ip = forms.CharField(
+        required=False,
+        widget=forms.TextInput(
+            attrs={
+                'placeholder': 'IP Address',
+            }
+        ),
+        label=_('IP Address')
+    )
```

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/git.py` & `netbox_config_backup-1.4.1/netbox_config_backup/git.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/management/commands/fix_missing.py` & `netbox_config_backup-1.4.1/netbox_config_backup/management/commands/fix_missing.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/management/commands/rebuild.py` & `netbox_config_backup-1.4.1/netbox_config_backup/management/commands/rebuild.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/management/commands/runbackup.py` & `netbox_config_backup-1.4.1/netbox_config_backup/management/commands/runbackup.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/migrations/0001_initial.py` & `netbox_config_backup-1.4.1/netbox_config_backup/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/migrations/0002_git_models.py` & `netbox_config_backup-1.4.1/netbox_config_backup/migrations/0002_git_models.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/migrations/0003_primary_model_to_bigid.py` & `netbox_config_backup-1.4.1/netbox_config_backup/migrations/0003_primary_model_to_bigid.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/migrations/0006_backup_add_commit_last_time.py` & `netbox_config_backup-1.4.1/netbox_config_backup/migrations/0006_backup_add_commit_last_time.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/migrations/0007_backup_job_add_scheduled.py` & `netbox_config_backup-1.4.1/netbox_config_backup/migrations/0007_backup_job_add_scheduled.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/migrations/0009_bctc_file_model_backup_fk_restructure.py` & `netbox_config_backup-1.4.1/netbox_config_backup/migrations/0009_bctc_file_model_backup_fk_restructure.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/migrations/0010_backup_ip.py` & `netbox_config_backup-1.4.1/netbox_config_backup/migrations/0010_backup_ip.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/models/backups.py` & `netbox_config_backup-1.4.1/netbox_config_backup/models/backups.py`

 * *Files 5% similar despite different names*

```diff
@@ -5,29 +5,35 @@
 from django.db import models
 from django.urls import reverse
 
 from django_rq import get_queue
 
 from dcim.models import Device
 from extras.choices import JobResultStatusChoices
+from netbox.models import NetBoxModel
 
-from netbox_config_backup.choices import FileTypeChoices, CommitTreeChangeTypeChoices
+from netbox_config_backup.choices import FileTypeChoices, CommitTreeChangeTypeChoices, StatusChoices
 from netbox_config_backup.helpers import get_repository_dir
 from utilities.querysets import RestrictedQuerySet
 
 from .abstract import BigIDModel
 from netbox_config_backup.utils.rq import remove_queued
 from ..utils import Differ
 
 logger = logging.getLogger(f"netbox_config_backup")
 
 
 class Backup(BigIDModel):
     name = models.CharField(max_length=255, unique=True)
     uuid = models.UUIDField(default=uuid.uuid4, editable=False)
+    status = models.CharField(
+        max_length=50,
+        choices=StatusChoices,
+        default=StatusChoices.STATUS_ACTIVE
+    )
     device = models.ForeignKey(
         to=Device,
         on_delete=models.SET_NULL,
         blank=True,
         null=True
     )
     ip = models.ForeignKey(
@@ -197,15 +203,15 @@
     backup = models.ForeignKey(to=Backup, on_delete=models.CASCADE, null=False, blank=False, related_name='files')
     type = models.CharField(max_length=10, choices=FileTypeChoices, null=False, blank=False)
 
     class Meta:
         unique_together = ['backup', 'type']
 
     def __str__(self):
-        return f'{self.sha}'
+        return f'{self.name}.{self.type}'
 
     @property
     def name(self):
         return f'{self.backup.uuid}'
 
     @property
     def path(self):
@@ -222,7 +228,11 @@
     new = models.ForeignKey(to=BackupObject, on_delete=models.PROTECT, related_name='changes', null=True)
 
     def __str__(self):
         return f'{self.commit.sha}-{self.type}'
 
     def filename(self):
         return f'{self.backup.uuid}.{self.type}'
+
+    @property
+    def previous(self):
+        return self.backup.changes.filter(file__type=self.file.type, commit__time__lt=self.commit.time).last()
```

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/models/jobs.py` & `netbox_config_backup-1.4.1/netbox_config_backup/models/jobs.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/navigation.py` & `netbox_config_backup-1.4.1/netbox_config_backup/navigation.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/tables.py` & `netbox_config_backup-1.4.1/netbox_config_backup/tables.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 import django_tables2 as tables
 from django_tables2.utils import Accessor
 
-from netbox_config_backup.models import Backup
+from netbox_config_backup.models import Backup, BackupCommitTreeChange
 from netbox.tables import columns, BaseTable
 
 
 class ActionButtonsColumn(tables.TemplateColumn):
     attrs = {'td': {'class': 'text-end text-nowrap noprint min-width'}}
     template_code = """
-    <a href="{% url 'plugins:netbox_config_backup:backup_config' pk=record.pk current=record.current.pk %}" class="btn btn-sm btn-outline-dark" title="View">
+    <a href="{% url 'plugins:netbox_config_backup:backup_config' pk=record.backup.pk current=record.pk %}" class="btn btn-sm btn-outline-dark" title="View">
         <i class="mdi mdi-cloud-download"></i>
     </a>
     {% if record.previous %}
-        <a href="{% url 'plugins:netbox_config_backup:backup_diff' pk=record.pk current=record.current.pk previous=record.previous.pk %}" class="btn btn-outline-dark btn-sm" title="Diff">
+        <a href="{% url 'plugins:netbox_config_backup:backup_diff' pk=record.backup.pk current=record.pk previous=record.previous.pk %}" class="btn btn-outline-dark btn-sm" title="Diff">
             <i class="mdi mdi-file-compare"></i>
         </a>
     {% else %}
         
     {% endif %}
     """
 
@@ -52,16 +52,28 @@
             'pk', 'name', 'device', 'last_backup', 'next_attempt', 'backup_count'
         )
         default_columns = (
             'pk', 'name', 'device', 'last_backup', 'next_attempt', 'backup_count'
         )
 
 
-class BackupsTable(tables.Table):
-    date = tables.Column()
+class BackupsTable(BaseTable):
+    date = tables.Column(
+        accessor='commit__time'
+    )
+    type = tables.Column(
+        accessor='file__type'
+    )
     actions = ActionButtonsColumn()
 
     class Meta:
+        model = BackupCommitTreeChange
+        fields = (
+            'date', 'type', 'backup', 'commit', 'file', 'actions'
+        )
+        default_columns = (
+            'date', 'type', 'actions'
+        )
         attrs = {
             'class': 'table table-hover object-list',
         }
         order_by = ['-date']
```

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/tasks.py` & `netbox_config_backup-1.4.1/netbox_config_backup/tasks.py`

 * *Files 2% similar despite different names*

```diff
@@ -104,21 +104,19 @@
         logger.info(f'{backup}: No IP set')
 
     return commit
 
 
 def backup_job(pk):
     import netmiko
-    #logger.debug(f'[{pk}] Starting backup run')
     try:
         job_result = BackupJob.objects.get(pk=pk)
-        #logger.debug(f'[{pk}] Found existing job')
     except BackupJob.DoesNotExist:
         logger.error(f'Cannot locate job (Id: {pk}) in DB')
-        raise Exception('Cannot locate job (Id: {pk}) in DB')
+        raise Exception(f'Cannot locate job (Id: {pk}) in DB')
     backup = job_result.backup
     delay = timedelta(seconds=settings.PLUGINS_CONFIG.get('netbox_config_backup', {}).get('frequency'))
 
     job_result.started = timezone.now()
     job_result.status = JobResultStatusChoices.STATUS_RUNNING
     job_result.save()
     try:
```

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/template_content.py` & `netbox_config_backup-1.4.1/netbox_config_backup/template_content.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,33 +1,53 @@
 import logging
 
 from extras.plugins import PluginTemplateExtension
 
-from netbox_config_backup.models import Backup, BackupJob
+from netbox_config_backup.models import Backup, BackupJob, BackupCommitTreeChange
+from netbox_config_backup.tables import BackupsTable
 from netbox_config_backup.utils.backups import get_backup_tables
+from utilities.htmx import is_htmx
 
 logger = logging.getLogger(f"netbox_config_backup")
 
 
 class DeviceBackups(PluginTemplateExtension):
     model = 'dcim.device'
 
     def full_width_page(self):
+        request = self.context.get('request')
+        def build_table(instance):
+            bctc = BackupCommitTreeChange.objects.filter(
+                backup=instance,
+                file__isnull=False
+            )
+            table = BackupsTable(bctc, user=request.user)
+            table.configure(request)
+
+            return table
+
         device = self.context.get('object', None)
         devices = Backup.objects.filter(device=device) if device is not None else Backup.objects.none()
         if devices.count() > 0:
             instance = devices.first()
-            tables = get_backup_tables(instance)
+            table = build_table(instance)
 
             if BackupJob.is_queued(instance) is False:
                 logger.debug(f'{instance}: Queuing Job')
                 BackupJob.enqueue(instance)
 
+            if is_htmx(request):
+                return self.render('htmx/table.html', extra_context={
+                    'object': instance,
+                    'table': table,
+                    'preferences': {},
+                })
             return self.render('netbox_config_backup/inc/backup_tables.html', extra_context={
-                'running': tables.get('running'),
-                'startup': tables.get('startup'),
+                'object': instance,
+                'table': table,
+                'preferences': request.user.config,
             })
 
         return ''
 
 
 template_extensions = [DeviceBackups]
```

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/templates/netbox_config_backup/base.html` & `netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/base.html`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/templates/netbox_config_backup/device.html` & `netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/backup.html`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,14 @@
 {% extends 'netbox_config_backup/base.html' %}
 {% load helpers %}
 
+{% block subtitle %}
+  <div class="object-subtitle"></div>
+{% endblock %}
+
 {% block content %}
 <div class="row">
 	<div class="col col-md-6">
         <div class="card">
             <h5 class="card-header">
                 Backup Attributes
             </h5>
@@ -62,11 +66,8 @@
                 </table>
             </div>
         </div>
 	</div>
 	<div class="col col-md-6">
     </div>
 </div>
-<div class="row">
-    {% include 'netbox_config_backup/inc/backup_tables.html' %}
-</div>
 {% endblock %}
```

#### html2text {}

```diff
@@ -1,15 +1,15 @@
 {% extends 'netbox_config_backup/base.html' %} {% load helpers %} {% block
-content %}
+subtitle %}
+{% endblock %} {% block content %}
 ** Backup Attributes **
 Name       {{ object.name|placeholder }}
 UUID       {{ object.uuid }}
 Device     {{_object.device|placeholder_}} {{ object.device|placeholder }}
 IP Address {{_object.ip|placeholder_}}     {{ object.ip|placeholder }}
 ** Status **
 Scheduled    {{ status.scheduled | placeholder }}{% if status.scheduled %} ({
              {status.next_attempt}}){% endif %}
 Last Job     {{ status.last_job.completed | placeholder }}
 Last Success {{ status.last_success | placeholder }}
 Last Change  {{ status.last_change | placeholder }}
-{% include 'netbox_config_backup/inc/backup_tables.html' %}
 {% endblock %}
```

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/templates/netbox_config_backup/diff.html` & `netbox_config_backup-1.4.1/netbox_config_backup/templates/netbox_config_backup/diff.html`

 * *Files 16% similar despite different names*

```diff
@@ -1,8 +1,17 @@
 {% extends 'netbox_config_backup/base.html' %}
+{% load helpers %}
+
+{% block subtitle %}
+  <div class="object-subtitle">
+    <span>{{ current.commit.time }}</span>
+    <span class="separator">&middot;&middot;&middot;</span>
+    <span>{{ previous.commit.time }}</span>
+  </div>
+{% endblock %}
 
 {% block content %}
 <div class="row">
 	<div class="col col-md-12">
         <div class="card">
             <h5 class="card-header">
                 Diff
```

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/urls.py` & `netbox_config_backup-1.4.1/netbox_config_backup/urls.py`

 * *Files 19% similar despite different names*

```diff
@@ -3,11 +3,14 @@
 
 urlpatterns = [
     path('devices/', views.BackupListView.as_view(), name='backup_list'),
     path('devices/add/', views.BackupEditView.as_view(), name='backup_add'),
     path('devices/<int:pk>/', views.BackupView.as_view(), name='backup'),
     path('devices/<int:pk>/edit/', views.BackupEditView.as_view(), name='backup_edit'),
     path('devices/<int:pk>/delete/', views.BackupDeleteView.as_view(), name='backup_delete'),
+    path('devices/<int:pk>/backups/', views.BackupBackupsView.as_view(), name='backup_backups'),
+    path('devices/<int:pk>/config/', views.ConfigView.as_view(), name='backup_config'),
     path('devices/<int:pk>/config/<int:current>/', views.ConfigView.as_view(), name='backup_config'),
+    path('devices/<int:pk>/diff/', views.DiffView.as_view(), name='backup_diff'),
     path('devices/<int:pk>/diff/<int:current>/', views.DiffView.as_view(), name='backup_diff'),
     path('devices/<int:pk>/diff/<int:current>/<int:previous>/', views.DiffView.as_view(), name='backup_diff'),
 ]
```

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/utils/git.py` & `netbox_config_backup-1.4.1/netbox_config_backup/utils/git.py`

 * *Files identical despite different names*

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup/utils/rq.py` & `netbox_config_backup-1.4.1/netbox_config_backup/utils/rq.py`

 * *Files 15% similar despite different names*

```diff
@@ -3,14 +3,15 @@
 import uuid
 from django.utils import timezone
 from django_rq import get_queue
 from rq.registry import ScheduledJobRegistry
 
 from dcim.choices import DeviceStatusChoices
 from extras.choices import JobResultStatusChoices
+from netbox_config_backup.choices import StatusChoices
 from netbox_config_backup.models.jobs import BackupJob
 
 logger = logging.getLogger(f"netbox_config_backup")
 
 
 def enqueue(backup, delay=None):
     from netbox_config_backup.models import BackupJob
@@ -62,29 +63,29 @@
 
     scheduled_jobs = scheduled.get_job_ids()
     started_jobs = started.get_job_ids()
 
     if backup.device is None:
         print(f'No device for {backup}')
         return False
-
-    if backup.device.status in [DeviceStatusChoices.STATUS_OFFLINE,
+    elif backup.status == StatusChoices.STATUS_DISABLED:
+        print(f'Backup disabled for {backup}')
+        return False
+    elif backup.device.status in [DeviceStatusChoices.STATUS_OFFLINE,
                                 DeviceStatusChoices.STATUS_FAILED,
                                 DeviceStatusChoices.STATUS_INVENTORY,
                                 DeviceStatusChoices.STATUS_PLANNED]:
-        print('Status')
+        print(f'Backup disabled for {backup} due to device status ({backup.device.status})')
         return False
-
-    if (backup.ip is None and backup.device.primary_ip is None) or backup.device.platform is None or \
+    elif (backup.ip is None and backup.device.primary_ip is None) or backup.device.platform is None or \
             backup.device.platform.napalm_driver == '' or backup.device.platform.napalm_driver is None:
-        print('Napalm')
+        print(f'Backup disabled for {backup} due to napalm drive or no primary IP ({backup.device.status})')
         return False
-
-    if is_queued(backup, job_id):
-        print('Queued')
+    elif is_queued(backup, job_id):
+        print(f'Backup already queued for {backup}')
         return False
 
     return True
 
 
 def is_running(backup, job_id=None):
     queue = get_queue('netbox_config_backup.jobs')
```

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup.egg-info/PKG-INFO` & `netbox_config_backup-1.4.1/netbox_config_backup.egg-info/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: netbox-config-backup
-Version: 1.4.0
+Version: 1.4.1
 Summary: NetBox Configuration Backup
 Home-page: https://github.com/dansheps/netbox-config-backup/
 Download-URL: https://github.com/dansheps/netbox-config-backup/
 Author: Daniel Sheppard
 Author-email: dans@dansheps.com
 Maintainer: Daniel Sheppard
 Maintainer-email: dans@dansheps.com
```

### Comparing `netbox_config_backup-1.4.0/netbox_config_backup.egg-info/SOURCES.txt` & `netbox_config_backup-1.4.1/netbox_config_backup.egg-info/SOURCES.txt`

 * *Files 5% similar despite different names*

```diff
@@ -33,24 +33,27 @@
 netbox_config_backup/migrations/0005_commit_add_time_field.py
 netbox_config_backup/migrations/0006_backup_add_commit_last_time.py
 netbox_config_backup/migrations/0007_backup_job_add_scheduled.py
 netbox_config_backup/migrations/0008_backupjob_scheduled_nullable.py
 netbox_config_backup/migrations/0009_bctc_file_model_backup_fk_restructure.py
 netbox_config_backup/migrations/0010_backup_ip.py
 netbox_config_backup/migrations/0011_alter_backup_name.py
+netbox_config_backup/migrations/0012_backup_status.py
 netbox_config_backup/migrations/__init__.py
 netbox_config_backup/models/__init__.py
 netbox_config_backup/models/abstract.py
 netbox_config_backup/models/backups.py
 netbox_config_backup/models/jobs.py
+netbox_config_backup/templates/netbox_config_backup/backup.html
+netbox_config_backup/templates/netbox_config_backup/backups.html
 netbox_config_backup/templates/netbox_config_backup/base.html
 netbox_config_backup/templates/netbox_config_backup/config.html
-netbox_config_backup/templates/netbox_config_backup/device.html
 netbox_config_backup/templates/netbox_config_backup/diff.html
 netbox_config_backup/templates/netbox_config_backup/repository.html
 netbox_config_backup/templates/netbox_config_backup/inc/backup_tables.html
+netbox_config_backup/templates/netbox_config_backup/switch_templates/cisco_iosxe/interface.tpl
 netbox_config_backup/templatetags/__init__.py
 netbox_config_backup/templatetags/ncb_split.py
 netbox_config_backup/utils/__init__.py
 netbox_config_backup/utils/backups.py
 netbox_config_backup/utils/git.py
 netbox_config_backup/utils/rq.py
```

### Comparing `netbox_config_backup-1.4.0/setup.py` & `netbox_config_backup-1.4.1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import find_packages, setup
 
 setup(
     name='netbox_config_backup',
-    version='1.4.0',
+    version='1.4.1',
     description='NetBox Configuration Backup',
     long_description='Plugin to backup device configuration',
     url='https://github.com/dansheps/netbox-config-backup/',
     download_url='https://github.com/dansheps/netbox-config-backup/',
     author='Daniel Sheppard',
     author_email='dans@dansheps.com',
     maintainer='Daniel Sheppard',
```

