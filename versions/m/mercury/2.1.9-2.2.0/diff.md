# Comparing `tmp/mercury-2.1.9.tar.gz` & `tmp/mercury-2.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mercury-2.1.9.tar", last modified: Mon Apr  3 10:44:35 2023, max compression
+gzip compressed data, was "mercury-2.2.0.tar", last modified: Fri Apr  7 10:49:44 2023, max compression
```

## Comparing `mercury-2.1.9.tar` & `mercury-2.2.0.tar`

### file list

```diff
@@ -1,205 +1,211 @@
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.283555 mercury-2.1.9/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      149 2022-04-19 12:37:24.000000 mercury-2.1.9/MANIFEST.in
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     5674 2023-04-03 10:44:35.283555 mercury-2.1.9/PKG-INFO
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     4214 2023-02-15 10:26:45.000000 mercury-2.1.9/README.md
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.267555 mercury-2.1.9/mercury/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)       54 2023-04-03 10:43:22.000000 mercury-2.1.9/mercury/__init__.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.267555 mercury-2.1.9/mercury/apps/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/apps/__init__.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.267555 mercury-2.1.9/mercury/apps/accounts/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-01 11:11:00.000000 mercury-2.1.9/mercury/apps/accounts/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      459 2023-03-17 11:37:23.000000 mercury-2.1.9/mercury/apps/accounts/admin.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      153 2023-03-01 11:11:00.000000 mercury-2.1.9/mercury/apps/accounts/apps.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      801 2023-03-01 11:11:00.000000 mercury-2.1.9/mercury/apps/accounts/fields.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.267555 mercury-2.1.9/mercury/apps/accounts/migrations/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     9132 2023-03-29 09:06:05.000000 mercury-2.1.9/mercury/apps/accounts/migrations/0001_initial.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-01 11:11:00.000000 mercury-2.1.9/mercury/apps/accounts/migrations/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     4715 2023-03-28 08:49:03.000000 mercury-2.1.9/mercury/apps/accounts/models.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1812 2023-03-27 06:19:51.000000 mercury-2.1.9/mercury/apps/accounts/serializers.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2937 2023-03-27 12:26:01.000000 mercury-2.1.9/mercury/apps/accounts/tasks.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/accounts/tests/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-16 13:27:44.000000 mercury-2.1.9/mercury/apps/accounts/tests/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     7289 2023-03-29 09:06:05.000000 mercury-2.1.9/mercury/apps/accounts/tests/test_accounts.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     5543 2023-03-31 10:36:11.000000 mercury-2.1.9/mercury/apps/accounts/tests/test_invitations.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     4137 2023-03-17 09:13:31.000000 mercury-2.1.9/mercury/apps/accounts/tests/test_secrets.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)    11402 2023-03-31 10:52:58.000000 mercury-2.1.9/mercury/apps/accounts/tests/test_sites.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3426 2023-03-29 09:06:05.000000 mercury-2.1.9/mercury/apps/accounts/tests/test_subscription.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2650 2023-03-24 11:47:32.000000 mercury-2.1.9/mercury/apps/accounts/urls.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/accounts/views/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-17 08:20:29.000000 mercury-2.1.9/mercury/apps/accounts/views/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2006 2023-03-27 08:34:35.000000 mercury-2.1.9/mercury/apps/accounts/views/accounts.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     4308 2023-03-31 10:36:11.000000 mercury-2.1.9/mercury/apps/accounts/views/invitations.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      789 2023-03-24 08:45:58.000000 mercury-2.1.9/mercury/apps/accounts/views/permissions.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2893 2023-03-17 13:01:54.000000 mercury-2.1.9/mercury/apps/accounts/views/secrets.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     6372 2023-03-31 10:52:58.000000 mercury-2.1.9/mercury/apps/accounts/views/sites.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     4152 2023-03-29 09:06:05.000000 mercury-2.1.9/mercury/apps/accounts/views/subscription.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      436 2023-03-24 08:45:58.000000 mercury-2.1.9/mercury/apps/accounts/views/utils.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/nb/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/nb/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3794 2023-02-21 07:28:26.000000 mercury-2.1.9/mercury/apps/nb/exporter.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     4004 2023-02-21 07:28:26.000000 mercury-2.1.9/mercury/apps/nb/nbrun.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1265 2023-03-17 12:41:34.000000 mercury-2.1.9/mercury/apps/nb/tests.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      403 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/nb/utils.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/nbworker/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/nbworker/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1719 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/apps/nbworker/__main__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)    16991 2023-03-31 13:20:13.000000 mercury-2.1.9/mercury/apps/nbworker/nb.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     7059 2023-03-28 13:59:09.000000 mercury-2.1.9/mercury/apps/nbworker/rest.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     4864 2023-03-17 08:55:41.000000 mercury-2.1.9/mercury/apps/nbworker/tests.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      701 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/apps/nbworker/utils.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2976 2023-03-31 09:54:03.000000 mercury-2.1.9/mercury/apps/nbworker/ws.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/notebooks/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/apps/notebooks/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      277 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/apps/notebooks/admin.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      155 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/apps/notebooks/apps.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/notebooks/management/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/apps/notebooks/management/__init__.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/notebooks/management/commands/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/apps/notebooks/management/commands/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1279 2022-03-09 11:06:47.000000 mercury-2.1.9/mercury/apps/notebooks/management/commands/add.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      864 2022-03-09 11:06:47.000000 mercury-2.1.9/mercury/apps/notebooks/management/commands/delete.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      545 2022-03-09 11:06:47.000000 mercury-2.1.9/mercury/apps/notebooks/management/commands/list.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3702 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/notebooks/management/commands/watch.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/notebooks/migrations/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2300 2023-03-29 09:06:05.000000 mercury-2.1.9/mercury/apps/notebooks/migrations/0001_initial.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/apps/notebooks/migrations/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1067 2023-03-27 08:29:11.000000 mercury-2.1.9/mercury/apps/notebooks/models.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      617 2023-03-17 11:38:01.000000 mercury-2.1.9/mercury/apps/notebooks/serializers.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     4093 2022-05-18 10:19:32.000000 mercury-2.1.9/mercury/apps/notebooks/slides_themes.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)    11349 2023-03-29 09:06:05.000000 mercury-2.1.9/mercury/apps/notebooks/tasks.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        1 2023-03-01 11:11:00.000000 mercury-2.1.9/mercury/apps/notebooks/tests.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      567 2023-03-17 12:41:34.000000 mercury-2.1.9/mercury/apps/notebooks/urls.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3755 2023-03-17 08:55:41.000000 mercury-2.1.9/mercury/apps/notebooks/views.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/storage/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/storage/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)       63 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/storage/admin.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      151 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/storage/apps.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/storage/migrations/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2949 2023-03-29 09:06:05.000000 mercury-2.1.9/mercury/apps/storage/migrations/0001_initial.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1404 2023-03-31 09:54:03.000000 mercury-2.1.9/mercury/apps/storage/migrations/0002_useruploadedfile.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/storage/migrations/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1787 2023-03-29 09:06:05.000000 mercury-2.1.9/mercury/apps/storage/models.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3540 2023-03-31 09:54:03.000000 mercury-2.1.9/mercury/apps/storage/s3utils.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      469 2023-03-31 14:19:15.000000 mercury-2.1.9/mercury/apps/storage/serializers.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)    11397 2023-03-31 09:54:03.000000 mercury-2.1.9/mercury/apps/storage/storage.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3158 2023-03-17 08:55:41.000000 mercury-2.1.9/mercury/apps/storage/tests.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2132 2023-03-29 09:56:45.000000 mercury-2.1.9/mercury/apps/storage/urls.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      445 2023-03-31 09:54:03.000000 mercury-2.1.9/mercury/apps/storage/utils.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/storage/views/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-31 12:45:08.000000 mercury-2.1.9/mercury/apps/storage/views/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     6182 2023-03-31 11:42:07.000000 mercury-2.1.9/mercury/apps/storage/views/dashboardfiles.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     4935 2023-03-31 11:42:07.000000 mercury-2.1.9/mercury/apps/storage/views/notebookfiles.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3737 2023-03-31 11:42:07.000000 mercury-2.1.9/mercury/apps/storage/views/workerfiles.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/tasks/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/apps/tasks/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      287 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/apps/tasks/admin.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      153 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/apps/tasks/apps.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      412 2022-03-09 11:06:47.000000 mercury-2.1.9/mercury/apps/tasks/clean_service.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3840 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/apps/tasks/export_pdf.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/tasks/migrations/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1328 2023-03-29 09:06:05.000000 mercury-2.1.9/mercury/apps/tasks/migrations/0001_initial.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/apps/tasks/migrations/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      762 2022-05-18 10:19:32.000000 mercury-2.1.9/mercury/apps/tasks/models.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3659 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/tasks/notify.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      433 2022-03-09 11:06:47.000000 mercury-2.1.9/mercury/apps/tasks/serializers.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)    15223 2023-02-23 14:52:12.000000 mercury-2.1.9/mercury/apps/tasks/tasks.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1314 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/tasks/tasks_export.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      571 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/apps/tasks/tests.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1401 2023-03-17 12:41:34.000000 mercury-2.1.9/mercury/apps/tasks/urls.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     8619 2023-03-17 08:55:41.000000 mercury-2.1.9/mercury/apps/tasks/views.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/workers/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/apps/workers/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)       63 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/apps/workers/admin.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      151 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/apps/workers/apps.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.271555 mercury-2.1.9/mercury/apps/workers/migrations/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1286 2023-03-29 09:06:05.000000 mercury-2.1.9/mercury/apps/workers/migrations/0001_initial.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/apps/workers/migrations/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      798 2023-03-29 09:06:05.000000 mercury-2.1.9/mercury/apps/workers/models.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      296 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/apps/workers/serializers.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)       60 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/apps/workers/tests.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1053 2023-03-17 12:41:34.000000 mercury-2.1.9/mercury/apps/workers/urls.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3881 2023-03-31 09:54:03.000000 mercury-2.1.9/mercury/apps/workers/views.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.275555 mercury-2.1.9/mercury/apps/ws/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/ws/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      141 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/ws/apps.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     5760 2023-03-31 09:54:03.000000 mercury-2.1.9/mercury/apps/ws/client.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      947 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/apps/ws/middleware.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.275555 mercury-2.1.9/mercury/apps/ws/migrations/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/apps/ws/migrations/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      386 2023-02-28 13:59:46.000000 mercury-2.1.9/mercury/apps/ws/routing.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1185 2023-03-29 09:06:05.000000 mercury-2.1.9/mercury/apps/ws/tasks.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      137 2023-03-01 11:07:38.000000 mercury-2.1.9/mercury/apps/ws/tests.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     4801 2023-04-03 08:19:03.000000 mercury-2.1.9/mercury/apps/ws/utils.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1754 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/apps/ws/worker.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     7191 2023-03-31 14:11:10.000000 mercury-2.1.9/mercury/demo.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.275555 mercury-2.1.9/mercury/frontend-dist/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1158 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/asset-manifest.json
--rw-rw-r--   0 piotr     (1000) piotr     (1000)    15406 2023-04-03 10:44:18.000000 mercury-2.1.9/mercury/frontend-dist/favicon-old.ico
--rw-rw-r--   0 piotr     (1000) piotr     (1000)    15086 2023-04-03 10:44:18.000000 mercury-2.1.9/mercury/frontend-dist/favicon.ico
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3086 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/index.html
--rw-rw-r--   0 piotr     (1000) piotr     (1000)    17406 2023-04-03 10:44:18.000000 mercury-2.1.9/mercury/frontend-dist/jupyter-additional.css
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     4539 2023-04-03 10:44:18.000000 mercury-2.1.9/mercury/frontend-dist/jupyter-syntax.css
--rw-rw-r--   0 piotr     (1000) piotr     (1000)   580386 2023-04-03 10:44:18.000000 mercury-2.1.9/mercury/frontend-dist/jupyter-theme-light.css
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      324 2023-04-03 10:44:18.000000 mercury-2.1.9/mercury/frontend-dist/manifest.json
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     6237 2023-04-03 10:44:18.000000 mercury-2.1.9/mercury/frontend-dist/mercury_black_logo.svg
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     6997 2023-04-03 10:44:18.000000 mercury-2.1.9/mercury/frontend-dist/mercury_logo.svg
--rw-rw-r--   0 piotr     (1000) piotr     (1000)       67 2023-04-03 10:44:18.000000 mercury-2.1.9/mercury/frontend-dist/robots.txt
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.267555 mercury-2.1.9/mercury/frontend-dist/static/
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.275555 mercury-2.1.9/mercury/frontend-dist/static/css/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)   229115 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/css/2.c6cf5ff9.chunk.css
--rw-rw-r--   0 piotr     (1000) piotr     (1000)   612316 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/css/2.c6cf5ff9.chunk.css.map
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2831 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/css/main.26f96620.chunk.css
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     5260 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/css/main.26f96620.chunk.css.map
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.279555 mercury-2.1.9/mercury/frontend-dist/static/js/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)  1311795 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/js/2.20950ecb.chunk.js
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3383 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/js/2.20950ecb.chunk.js.LICENSE.txt
--rw-rw-r--   0 piotr     (1000) piotr     (1000)  4973512 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/js/2.20950ecb.chunk.js.map
--rw-rw-r--   0 piotr     (1000) piotr     (1000)    78134 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/js/main.b729f6a0.chunk.js
--rw-rw-r--   0 piotr     (1000) piotr     (1000)   248569 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/js/main.b729f6a0.chunk.js.map
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1557 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/js/runtime-main.248907bc.js
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     8276 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/js/runtime-main.248907bc.js.map
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.279555 mercury-2.1.9/mercury/frontend-dist/static/media/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)   165548 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/media/fontawesome-webfont.1e59d233.ttf
--rw-rw-r--   0 piotr     (1000) piotr     (1000)    77160 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/media/fontawesome-webfont.20fd1704.woff2
--rw-rw-r--   0 piotr     (1000) piotr     (1000)   165742 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/media/fontawesome-webfont.8b43027f.eot
--rw-rw-r--   0 piotr     (1000) piotr     (1000)   444379 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/media/fontawesome-webfont.c1e38fd9.svg
--rw-rw-r--   0 piotr     (1000) piotr     (1000)    98024 2023-04-03 10:44:34.000000 mercury-2.1.9/mercury/frontend-dist/static/media/fontawesome-webfont.f691f37e.woff
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      684 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/manage.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     8306 2023-03-24 08:33:01.000000 mercury-2.1.9/mercury/mercury.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      543 2023-03-30 08:36:26.000000 mercury-2.1.9/mercury/requirements.txt
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.279555 mercury-2.1.9/mercury/server/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)       68 2022-03-09 11:04:20.000000 mercury-2.1.9/mercury/server/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      837 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/server/asgi.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2771 2023-03-24 08:43:00.000000 mercury-2.1.9/mercury/server/celery.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     9798 2023-03-28 14:27:07.000000 mercury-2.1.9/mercury/server/settings.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1572 2023-03-14 07:49:44.000000 mercury-2.1.9/mercury/server/urls.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1645 2023-03-01 12:07:40.000000 mercury-2.1.9/mercury/server/views.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      405 2022-05-18 11:03:41.000000 mercury-2.1.9/mercury/server/wsgi.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.283555 mercury-2.1.9/mercury/widgets/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.1.9/mercury/widgets/__init__.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2029 2023-03-17 11:39:55.000000 mercury-2.1.9/mercury/widgets/app.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2263 2023-04-03 09:20:35.000000 mercury-2.1.9/mercury/widgets/button.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2077 2023-04-03 09:20:46.000000 mercury-2.1.9/mercury/widgets/checkbox.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     3413 2023-04-03 09:20:52.000000 mercury-2.1.9/mercury/widgets/file.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     4828 2023-02-21 07:28:26.000000 mercury-2.1.9/mercury/widgets/json.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     6895 2023-04-03 09:33:26.000000 mercury-2.1.9/mercury/widgets/manager.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      104 2023-02-21 07:28:26.000000 mercury-2.1.9/mercury/widgets/md.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2629 2023-04-03 09:21:01.000000 mercury-2.1.9/mercury/widgets/multiselect.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1219 2023-02-21 07:48:36.000000 mercury-2.1.9/mercury/widgets/note.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2935 2023-04-03 09:21:09.000000 mercury-2.1.9/mercury/widgets/numeric.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1255 2023-02-21 07:48:36.000000 mercury-2.1.9/mercury/widgets/outputdir.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2944 2023-04-03 09:21:15.000000 mercury-2.1.9/mercury/widgets/range.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2355 2023-04-03 09:21:24.000000 mercury-2.1.9/mercury/widgets/select.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     2868 2023-04-03 09:21:30.000000 mercury-2.1.9/mercury/widgets/slider.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      222 2023-02-21 07:28:26.000000 mercury-2.1.9/mercury/widgets/stop.py
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1994 2023-04-03 09:21:37.000000 mercury-2.1.9/mercury/widgets/text.py
-drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-03 10:44:35.267555 mercury-2.1.9/mercury.egg-info/
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     5674 2023-04-03 10:44:35.000000 mercury-2.1.9/mercury.egg-info/PKG-INFO
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     6130 2023-04-03 10:44:35.000000 mercury-2.1.9/mercury.egg-info/SOURCES.txt
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        1 2023-04-03 10:44:35.000000 mercury-2.1.9/mercury.egg-info/dependency_links.txt
--rw-rw-r--   0 piotr     (1000) piotr     (1000)       50 2023-04-03 10:44:35.000000 mercury-2.1.9/mercury.egg-info/entry_points.txt
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      491 2023-04-03 10:44:35.000000 mercury-2.1.9/mercury.egg-info/requires.txt
--rw-rw-r--   0 piotr     (1000) piotr     (1000)        8 2023-04-03 10:44:35.000000 mercury-2.1.9/mercury.egg-info/top_level.txt
--rw-rw-r--   0 piotr     (1000) piotr     (1000)      106 2022-03-09 11:04:20.000000 mercury-2.1.9/pyproject.toml
--rw-rw-r--   0 piotr     (1000) piotr     (1000)       38 2023-04-03 10:44:35.283555 mercury-2.1.9/setup.cfg
--rw-rw-r--   0 piotr     (1000) piotr     (1000)     1163 2023-04-03 10:43:15.000000 mercury-2.1.9/setup.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.263627 mercury-2.2.0/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      149 2022-04-19 12:37:24.000000 mercury-2.2.0/MANIFEST.in
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     5674 2023-04-07 10:49:44.263627 mercury-2.2.0/PKG-INFO
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     4214 2023-02-15 10:26:45.000000 mercury-2.2.0/README.md
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.251627 mercury-2.2.0/mercury/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)       54 2023-04-07 10:48:43.000000 mercury-2.2.0/mercury/__init__.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.251627 mercury-2.2.0/mercury/apps/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/apps/__init__.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.251627 mercury-2.2.0/mercury/apps/accounts/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-01 11:11:00.000000 mercury-2.2.0/mercury/apps/accounts/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      459 2023-03-17 11:37:23.000000 mercury-2.2.0/mercury/apps/accounts/admin.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      153 2023-03-01 11:11:00.000000 mercury-2.2.0/mercury/apps/accounts/apps.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      801 2023-03-01 11:11:00.000000 mercury-2.2.0/mercury/apps/accounts/fields.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.251627 mercury-2.2.0/mercury/apps/accounts/migrations/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     9132 2023-03-29 09:06:05.000000 mercury-2.2.0/mercury/apps/accounts/migrations/0001_initial.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-01 11:11:00.000000 mercury-2.2.0/mercury/apps/accounts/migrations/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     4715 2023-03-28 08:49:03.000000 mercury-2.2.0/mercury/apps/accounts/models.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2086 2023-04-06 13:33:42.000000 mercury-2.2.0/mercury/apps/accounts/serializers.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2937 2023-03-27 12:26:01.000000 mercury-2.2.0/mercury/apps/accounts/tasks.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.251627 mercury-2.2.0/mercury/apps/accounts/tests/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-16 13:27:44.000000 mercury-2.2.0/mercury/apps/accounts/tests/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     7289 2023-03-29 09:06:05.000000 mercury-2.2.0/mercury/apps/accounts/tests/test_accounts.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     5543 2023-03-31 10:36:11.000000 mercury-2.2.0/mercury/apps/accounts/tests/test_invitations.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     6078 2023-04-06 13:49:54.000000 mercury-2.2.0/mercury/apps/accounts/tests/test_secrets.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)    11402 2023-03-31 10:52:58.000000 mercury-2.2.0/mercury/apps/accounts/tests/test_sites.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3426 2023-03-29 09:06:05.000000 mercury-2.2.0/mercury/apps/accounts/tests/test_subscription.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2650 2023-03-24 11:47:32.000000 mercury-2.2.0/mercury/apps/accounts/urls.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.251627 mercury-2.2.0/mercury/apps/accounts/views/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-17 08:20:29.000000 mercury-2.2.0/mercury/apps/accounts/views/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2006 2023-03-27 08:34:35.000000 mercury-2.2.0/mercury/apps/accounts/views/accounts.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     4308 2023-03-31 10:36:11.000000 mercury-2.2.0/mercury/apps/accounts/views/invitations.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      789 2023-03-24 08:45:58.000000 mercury-2.2.0/mercury/apps/accounts/views/permissions.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2922 2023-04-06 14:49:43.000000 mercury-2.2.0/mercury/apps/accounts/views/secrets.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     6372 2023-03-31 10:52:58.000000 mercury-2.2.0/mercury/apps/accounts/views/sites.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     4152 2023-03-29 09:06:05.000000 mercury-2.2.0/mercury/apps/accounts/views/subscription.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      436 2023-03-24 08:45:58.000000 mercury-2.2.0/mercury/apps/accounts/views/utils.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.251627 mercury-2.2.0/mercury/apps/nb/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/nb/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     5845 2023-04-06 13:49:54.000000 mercury-2.2.0/mercury/apps/nb/exporter.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     4086 2023-04-06 13:49:54.000000 mercury-2.2.0/mercury/apps/nb/nbrun.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.251627 mercury-2.2.0/mercury/apps/nb/tests/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-04-05 08:19:32.000000 mercury-2.2.0/mercury/apps/nb/tests/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      854 2023-04-06 13:49:54.000000 mercury-2.2.0/mercury/apps/nb/tests/test_nbrun.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1265 2023-03-17 12:41:34.000000 mercury-2.2.0/mercury/apps/nb/tests.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      403 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/nb/utils.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.251627 mercury-2.2.0/mercury/apps/nbworker/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/nbworker/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1719 2023-04-05 10:59:50.000000 mercury-2.2.0/mercury/apps/nbworker/__main__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)    17398 2023-04-06 14:49:56.000000 mercury-2.2.0/mercury/apps/nbworker/nb.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     7485 2023-04-06 14:49:56.000000 mercury-2.2.0/mercury/apps/nbworker/rest.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     4864 2023-03-17 08:55:41.000000 mercury-2.2.0/mercury/apps/nbworker/tests.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      701 2023-03-14 07:49:44.000000 mercury-2.2.0/mercury/apps/nbworker/utils.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2976 2023-03-31 09:54:03.000000 mercury-2.2.0/mercury/apps/nbworker/ws.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/notebooks/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/apps/notebooks/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      277 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/apps/notebooks/admin.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      155 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/apps/notebooks/apps.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/notebooks/management/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/apps/notebooks/management/__init__.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/notebooks/management/commands/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/apps/notebooks/management/commands/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1279 2022-03-09 11:06:47.000000 mercury-2.2.0/mercury/apps/notebooks/management/commands/add.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      864 2022-03-09 11:06:47.000000 mercury-2.2.0/mercury/apps/notebooks/management/commands/delete.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      545 2022-03-09 11:06:47.000000 mercury-2.2.0/mercury/apps/notebooks/management/commands/list.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3702 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/notebooks/management/commands/watch.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/notebooks/migrations/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2300 2023-03-29 09:06:05.000000 mercury-2.2.0/mercury/apps/notebooks/migrations/0001_initial.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/apps/notebooks/migrations/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1067 2023-03-27 08:29:11.000000 mercury-2.2.0/mercury/apps/notebooks/models.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      617 2023-03-17 11:38:01.000000 mercury-2.2.0/mercury/apps/notebooks/serializers.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     4093 2022-05-18 10:19:32.000000 mercury-2.2.0/mercury/apps/notebooks/slides_themes.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)    11689 2023-04-03 14:44:43.000000 mercury-2.2.0/mercury/apps/notebooks/tasks.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        1 2023-03-01 11:11:00.000000 mercury-2.2.0/mercury/apps/notebooks/tests.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      567 2023-03-17 12:41:34.000000 mercury-2.2.0/mercury/apps/notebooks/urls.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3755 2023-03-17 08:55:41.000000 mercury-2.2.0/mercury/apps/notebooks/views.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/storage/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/storage/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)       63 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/storage/admin.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      151 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/storage/apps.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/storage/migrations/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2949 2023-03-29 09:06:05.000000 mercury-2.2.0/mercury/apps/storage/migrations/0001_initial.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1404 2023-03-31 09:54:03.000000 mercury-2.2.0/mercury/apps/storage/migrations/0002_useruploadedfile.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/storage/migrations/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1787 2023-03-29 09:06:05.000000 mercury-2.2.0/mercury/apps/storage/models.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3540 2023-03-31 09:54:03.000000 mercury-2.2.0/mercury/apps/storage/s3utils.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      469 2023-03-31 14:19:15.000000 mercury-2.2.0/mercury/apps/storage/serializers.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)    11397 2023-03-31 09:54:03.000000 mercury-2.2.0/mercury/apps/storage/storage.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3158 2023-03-17 08:55:41.000000 mercury-2.2.0/mercury/apps/storage/tests.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2132 2023-03-29 09:56:45.000000 mercury-2.2.0/mercury/apps/storage/urls.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      445 2023-03-31 09:54:03.000000 mercury-2.2.0/mercury/apps/storage/utils.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/storage/views/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-31 12:45:08.000000 mercury-2.2.0/mercury/apps/storage/views/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     6182 2023-03-31 11:42:07.000000 mercury-2.2.0/mercury/apps/storage/views/dashboardfiles.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     4935 2023-03-31 11:42:07.000000 mercury-2.2.0/mercury/apps/storage/views/notebookfiles.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3737 2023-03-31 11:42:07.000000 mercury-2.2.0/mercury/apps/storage/views/workerfiles.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/tasks/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/apps/tasks/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      287 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/apps/tasks/admin.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      153 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/apps/tasks/apps.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      412 2022-03-09 11:06:47.000000 mercury-2.2.0/mercury/apps/tasks/clean_service.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3840 2023-04-03 14:18:32.000000 mercury-2.2.0/mercury/apps/tasks/export_pdf.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3805 2023-04-06 13:49:54.000000 mercury-2.2.0/mercury/apps/tasks/export_png.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/tasks/migrations/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1328 2023-03-29 09:06:05.000000 mercury-2.2.0/mercury/apps/tasks/migrations/0001_initial.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/apps/tasks/migrations/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      762 2022-05-18 10:19:32.000000 mercury-2.2.0/mercury/apps/tasks/models.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3659 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/tasks/notify.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      433 2022-03-09 11:06:47.000000 mercury-2.2.0/mercury/apps/tasks/serializers.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)    15223 2023-02-23 14:52:12.000000 mercury-2.2.0/mercury/apps/tasks/tasks.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1314 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/tasks/tasks_export.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      571 2023-03-14 07:49:44.000000 mercury-2.2.0/mercury/apps/tasks/tests.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1401 2023-03-17 12:41:34.000000 mercury-2.2.0/mercury/apps/tasks/urls.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     8619 2023-03-17 08:55:41.000000 mercury-2.2.0/mercury/apps/tasks/views.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/workers/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-14 07:49:44.000000 mercury-2.2.0/mercury/apps/workers/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)       63 2023-03-14 07:49:44.000000 mercury-2.2.0/mercury/apps/workers/admin.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      151 2023-03-14 07:49:44.000000 mercury-2.2.0/mercury/apps/workers/apps.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/workers/migrations/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1286 2023-03-29 09:06:05.000000 mercury-2.2.0/mercury/apps/workers/migrations/0001_initial.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-03-14 07:49:44.000000 mercury-2.2.0/mercury/apps/workers/migrations/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      798 2023-03-29 09:06:05.000000 mercury-2.2.0/mercury/apps/workers/models.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      296 2023-03-14 07:49:44.000000 mercury-2.2.0/mercury/apps/workers/serializers.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)       60 2023-03-14 07:49:44.000000 mercury-2.2.0/mercury/apps/workers/tests.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1053 2023-03-17 12:41:34.000000 mercury-2.2.0/mercury/apps/workers/urls.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3881 2023-03-31 09:54:03.000000 mercury-2.2.0/mercury/apps/workers/views.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/ws/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/ws/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      141 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/ws/apps.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     6162 2023-04-06 13:49:54.000000 mercury-2.2.0/mercury/apps/ws/client.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      947 2023-03-14 07:49:44.000000 mercury-2.2.0/mercury/apps/ws/middleware.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.255627 mercury-2.2.0/mercury/apps/ws/migrations/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/apps/ws/migrations/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      386 2023-02-28 13:59:46.000000 mercury-2.2.0/mercury/apps/ws/routing.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2495 2023-04-06 13:49:54.000000 mercury-2.2.0/mercury/apps/ws/tasks.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      137 2023-03-01 11:07:38.000000 mercury-2.2.0/mercury/apps/ws/tests.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     5106 2023-04-06 13:49:54.000000 mercury-2.2.0/mercury/apps/ws/utils.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1754 2023-03-14 07:49:44.000000 mercury-2.2.0/mercury/apps/ws/worker.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     7191 2023-03-31 14:11:10.000000 mercury-2.2.0/mercury/demo.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.259627 mercury-2.2.0/mercury/frontend-dist/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1158 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/asset-manifest.json
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)    15406 2023-04-07 10:49:28.000000 mercury-2.2.0/mercury/frontend-dist/favicon-old.ico
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)    15086 2023-04-07 10:49:28.000000 mercury-2.2.0/mercury/frontend-dist/favicon.ico
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3086 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/index.html
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)    17406 2023-04-07 10:49:28.000000 mercury-2.2.0/mercury/frontend-dist/jupyter-additional.css
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     4539 2023-04-07 10:49:28.000000 mercury-2.2.0/mercury/frontend-dist/jupyter-syntax.css
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)   580386 2023-04-07 10:49:28.000000 mercury-2.2.0/mercury/frontend-dist/jupyter-theme-light.css
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      324 2023-04-07 10:49:28.000000 mercury-2.2.0/mercury/frontend-dist/manifest.json
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     6237 2023-04-07 10:49:28.000000 mercury-2.2.0/mercury/frontend-dist/mercury_black_logo.svg
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     6997 2023-04-07 10:49:28.000000 mercury-2.2.0/mercury/frontend-dist/mercury_logo.svg
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)       67 2023-04-07 10:49:28.000000 mercury-2.2.0/mercury/frontend-dist/robots.txt
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.251627 mercury-2.2.0/mercury/frontend-dist/static/
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.259627 mercury-2.2.0/mercury/frontend-dist/static/css/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)   229115 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/css/2.c6cf5ff9.chunk.css
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)   612316 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/css/2.c6cf5ff9.chunk.css.map
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2831 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/css/main.26f96620.chunk.css
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     5260 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/css/main.26f96620.chunk.css.map
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.263627 mercury-2.2.0/mercury/frontend-dist/static/js/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)  1311795 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/js/2.20950ecb.chunk.js
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3383 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/js/2.20950ecb.chunk.js.LICENSE.txt
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)  4973512 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/js/2.20950ecb.chunk.js.map
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)    83606 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/js/main.717ee96a.chunk.js
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)   258957 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/js/main.717ee96a.chunk.js.map
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1557 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/js/runtime-main.248907bc.js
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     8276 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/js/runtime-main.248907bc.js.map
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.263627 mercury-2.2.0/mercury/frontend-dist/static/media/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)   165548 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/media/fontawesome-webfont.1e59d233.ttf
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)    77160 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/media/fontawesome-webfont.20fd1704.woff2
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)   165742 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/media/fontawesome-webfont.8b43027f.eot
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)   444379 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/media/fontawesome-webfont.c1e38fd9.svg
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)    98024 2023-04-07 10:49:43.000000 mercury-2.2.0/mercury/frontend-dist/static/media/fontawesome-webfont.f691f37e.woff
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      684 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/manage.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     8376 2023-04-07 10:38:38.000000 mercury-2.2.0/mercury/mercury.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      543 2023-03-30 08:36:26.000000 mercury-2.2.0/mercury/requirements.txt
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.263627 mercury-2.2.0/mercury/server/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)       68 2022-03-09 11:04:20.000000 mercury-2.2.0/mercury/server/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      837 2023-03-14 07:49:44.000000 mercury-2.2.0/mercury/server/asgi.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2771 2023-03-24 08:43:00.000000 mercury-2.2.0/mercury/server/celery.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     9844 2023-04-05 13:16:51.000000 mercury-2.2.0/mercury/server/settings.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1572 2023-03-14 07:49:44.000000 mercury-2.2.0/mercury/server/urls.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1645 2023-03-01 12:07:40.000000 mercury-2.2.0/mercury/server/views.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      405 2022-05-18 11:03:41.000000 mercury-2.2.0/mercury/server/wsgi.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.263627 mercury-2.2.0/mercury/widgets/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        0 2023-02-13 14:05:12.000000 mercury-2.2.0/mercury/widgets/__init__.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2029 2023-03-17 11:39:55.000000 mercury-2.2.0/mercury/widgets/app.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2294 2023-04-07 10:30:37.000000 mercury-2.2.0/mercury/widgets/button.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      826 2023-04-07 10:43:02.000000 mercury-2.2.0/mercury/widgets/chat.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2127 2023-04-07 10:30:37.000000 mercury-2.2.0/mercury/widgets/checkbox.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      408 2023-04-07 10:32:14.000000 mercury-2.2.0/mercury/widgets/confetti.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3393 2023-04-07 10:30:37.000000 mercury-2.2.0/mercury/widgets/file.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     4828 2023-02-21 07:28:26.000000 mercury-2.2.0/mercury/widgets/json.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     6894 2023-04-07 10:30:37.000000 mercury-2.2.0/mercury/widgets/manager.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      104 2023-02-21 07:28:26.000000 mercury-2.2.0/mercury/widgets/md.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2690 2023-04-07 10:30:37.000000 mercury-2.2.0/mercury/widgets/multiselect.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1219 2023-02-21 07:48:36.000000 mercury-2.2.0/mercury/widgets/note.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3016 2023-04-07 10:30:37.000000 mercury-2.2.0/mercury/widgets/numeric.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1255 2023-02-21 07:48:36.000000 mercury-2.2.0/mercury/widgets/outputdir.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     3025 2023-04-07 10:30:37.000000 mercury-2.2.0/mercury/widgets/range.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2403 2023-04-07 10:30:37.000000 mercury-2.2.0/mercury/widgets/select.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2949 2023-04-07 10:30:37.000000 mercury-2.2.0/mercury/widgets/slider.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      222 2023-02-21 07:28:26.000000 mercury-2.2.0/mercury/widgets/stop.py
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     2039 2023-04-07 10:30:37.000000 mercury-2.2.0/mercury/widgets/text.py
+drwxrwxr-x   0 piotr     (1000) piotr     (1000)        0 2023-04-07 10:49:44.251627 mercury-2.2.0/mercury.egg-info/
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     5674 2023-04-07 10:49:44.000000 mercury-2.2.0/mercury.egg-info/PKG-INFO
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     6285 2023-04-07 10:49:44.000000 mercury-2.2.0/mercury.egg-info/SOURCES.txt
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        1 2023-04-07 10:49:44.000000 mercury-2.2.0/mercury.egg-info/dependency_links.txt
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)       50 2023-04-07 10:49:44.000000 mercury-2.2.0/mercury.egg-info/entry_points.txt
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      491 2023-04-07 10:49:44.000000 mercury-2.2.0/mercury.egg-info/requires.txt
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)        8 2023-04-07 10:49:44.000000 mercury-2.2.0/mercury.egg-info/top_level.txt
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)      106 2022-03-09 11:04:20.000000 mercury-2.2.0/pyproject.toml
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)       38 2023-04-07 10:49:44.263627 mercury-2.2.0/setup.cfg
+-rw-rw-r--   0 piotr     (1000) piotr     (1000)     1163 2023-04-07 10:49:15.000000 mercury-2.2.0/setup.py
```

### Comparing `mercury-2.1.9/PKG-INFO` & `mercury-2.2.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mercury
-Version: 2.1.9
+Version: 2.2.0
 Summary: Turn Jupyter Notebook to Web App and share with non-technical users
 Home-page: https://github.com/mljar/mercury
 Maintainer: MLJAR Sp. z o.o.
 Maintainer-email: contact@mljar.com
 License: UNKNOWN
 Description:
```

### Comparing `mercury-2.1.9/README.md` & `mercury-2.2.0/README.md`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/fields.py` & `mercury-2.2.0/mercury/apps/accounts/fields.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/migrations/0001_initial.py` & `mercury-2.2.0/mercury/apps/accounts/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/models.py` & `mercury-2.2.0/mercury/apps/accounts/models.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/serializers.py` & `mercury-2.2.0/mercury/apps/accounts/serializers.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from dj_rest_auth.serializers import UserDetailsSerializer
 from rest_framework import serializers
 
-from apps.accounts.models import Invitation, Membership, Site, UserProfile
+from apps.accounts.models import Invitation, Membership, Secret, Site, UserProfile
 
 
 class UserProfileSerializer(serializers.ModelSerializer):
     class Meta:
         model = UserProfile
         fields = ("info",)
 
@@ -60,7 +60,16 @@
 class InvitationSerializer(serializers.ModelSerializer):
     created_by = UserDetailsSerializer(many=False, read_only=True)
 
     class Meta:
         model = Invitation
         read_only_fields = ("id", "invited", "created_at", "created_by", "rights")
         fields = read_only_fields
+
+
+class SecretSerializer(serializers.ModelSerializer):
+    created_by = UserDetailsSerializer(many=False, read_only=True)
+
+    class Meta:
+        model = Secret
+        read_only_fields = ("id", "name", "created_at", "created_by")
+        fields = read_only_fields
```

### Comparing `mercury-2.1.9/mercury/apps/accounts/tasks.py` & `mercury-2.2.0/mercury/apps/accounts/tasks.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/tests/test_accounts.py` & `mercury-2.2.0/mercury/apps/accounts/tests/test_accounts.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/tests/test_invitations.py` & `mercury-2.2.0/mercury/apps/accounts/tests/test_invitations.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/tests/test_secrets.py` & `mercury-2.2.0/mercury/apps/accounts/tests/test_secrets.py`

 * *Files 19% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 from datetime import datetime
 
 from allauth.account.admin import EmailAddress
 from django.contrib.auth.models import User
 from django.utils.timezone import make_aware
 from rest_framework.test import APITestCase
 
-from apps.accounts.models import Secret, Site
+from apps.accounts.models import Membership, Secret, Site
 from apps.notebooks.models import Notebook
 from apps.workers.models import Worker
 
 
 class SecretsTestCase(APITestCase):
     register_url = "/api/v1/auth/register/"
     login_url = "/api/v1/auth/login/"
@@ -55,15 +55,15 @@
 
         response = self.client.get(
             self.list_secrets_url.format(self.site.id), **headers
         )
         self.assertEqual(response.status_code, 200)
         data = response.json()
         self.assertEqual(len(data), 1)
-        self.assertEqual(data[0], new_data["name"])
+        self.assertEqual(data[0]["name"], new_data["name"])
 
     def test_list_worker_secrets(self):
         # login
         response = self.client.post(self.login_url, self.user1_params)
         token = response.json()["key"]
         headers = {"HTTP_AUTHORIZATION": "Token " + token}
         new_data = {"name": "MY_SECRET", "secret": "super-secret"}
@@ -104,7 +104,60 @@
 
         response = self.client.delete(
             self.delete_secret_url.format(self.site.id, 1), **headers
         )
         self.assertEqual(response.status_code, 204)
         secrets = Secret.objects.all()
         self.assertEqual(len(secrets), 0)
+
+    def test_list_secrets_by_user(self):
+        # login
+        response = self.client.post(self.login_url, self.user1_params)
+        token = response.json()["key"]
+        headers = {"HTTP_AUTHORIZATION": "Token " + token}
+        new_data = {"name": "MY_SECRET", "secret": "super-secret"}
+        response = self.client.post(
+            self.add_secret_url.format(self.site.id), new_data, **headers
+        )
+
+        # get worker secrets
+        url = f"/api/v1/{self.site.id}/list-secrets"
+        response = self.client.get(url, **headers)
+        self.assertTrue(len(response.json()), 1)
+
+        user2_params = {
+            "username": "user2",  # it is optional to pass username
+            "email": "piotr2@example.com",
+            "password": "verysecret2",
+        }
+        user2 = User.objects.create_user(
+            username=user2_params["username"],
+            email=user2_params["email"],
+            password=user2_params["password"],
+        )
+        EmailAddress.objects.create(
+            user=user2, email=user2.email, verified=True, primary=True
+        )
+
+        response = self.client.post(self.login_url, user2_params)
+        token = response.json()["key"]
+        headers = {"HTTP_AUTHORIZATION": "Token " + token}
+
+        url = f"/api/v1/{self.site.id}/list-secrets"
+        response = self.client.get(url, **headers)
+        self.assertTrue(len(response.json()), 0)
+
+        # invite
+        m = Membership.objects.create(
+            user=user2, host=self.site, rights=Membership.VIEW, created_by=self.user
+        )
+
+        url = f"/api/v1/{self.site.id}/list-secrets"
+        response = self.client.get(url, **headers)
+        self.assertTrue(len(response.json()), 0)
+
+        m.rights = Membership.EDIT
+        m.save()
+
+        url = f"/api/v1/{self.site.id}/list-secrets"
+        response = self.client.get(url, **headers)
+        self.assertTrue(len(response.json()), 1)
```

### Comparing `mercury-2.1.9/mercury/apps/accounts/tests/test_sites.py` & `mercury-2.2.0/mercury/apps/accounts/tests/test_sites.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/tests/test_subscription.py` & `mercury-2.2.0/mercury/apps/accounts/tests/test_subscription.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/urls.py` & `mercury-2.2.0/mercury/apps/accounts/urls.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/views/accounts.py` & `mercury-2.2.0/mercury/apps/accounts/views/accounts.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/views/invitations.py` & `mercury-2.2.0/mercury/apps/accounts/views/invitations.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/views/permissions.py` & `mercury-2.2.0/mercury/apps/accounts/views/permissions.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/views/secrets.py` & `mercury-2.2.0/mercury/apps/accounts/views/secrets.py`

 * *Files 8% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 from rest_framework.response import Response
 from rest_framework.views import APIView
 
 from apps.accounts.models import Secret, Site
 from apps.accounts.views.permissions import HasEditRights
 from apps.notebooks.models import Notebook
 from apps.workers.models import Worker
+from apps.accounts.serializers import SecretSerializer
 
 
 class AddSecret(APIView):
     permission_classes = [permissions.IsAuthenticated, HasEditRights]
 
     def post(self, request, site_id, format=None):
         site = Site.objects.get(pk=site_id)
@@ -41,20 +42,17 @@
 
 class ListSecrets(APIView):
     permission_classes = [permissions.IsAuthenticated, HasEditRights]
 
     def get(self, request, site_id, format=None):
         secrets = Secret.objects.filter(hosted_on__id=site_id)
 
-        data = []
-
-        for secret in secrets:
-            data += [secret.name]
-
-        return Response(data, status=status.HTTP_200_OK)
+        return Response(
+            SecretSerializer(secrets, many=True).data, status=status.HTTP_200_OK
+        )
 
 
 class WorkerListSecrets(APIView):
     def get(self, request, session_id, worker_id, notebook_id, format=None):
         try:
             w = Worker.objects.get(
                 pk=worker_id, session_id=session_id, notebook__id=notebook_id
```

### Comparing `mercury-2.1.9/mercury/apps/accounts/views/sites.py` & `mercury-2.2.0/mercury/apps/accounts/views/sites.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/accounts/views/subscription.py` & `mercury-2.2.0/mercury/apps/accounts/views/subscription.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/nb/nbrun.py` & `mercury-2.2.0/mercury/apps/nb/nbrun.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,20 +1,19 @@
-import json
 import os
 import sys
+import copy
 
 import nbformat
 from execnb.nbio import nb2dict, nb2str, read_nb, write_nb
 from execnb.shell import CaptureShell
 
 CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 BACKEND_DIR = os.path.join(CURRENT_DIR, "..")
 sys.path.insert(0, BACKEND_DIR)
 
-import copy
 
 from execnb.nbio import _dict2obj, dict2nb
 
 from apps.nb.exporter import Exporter
 from apps.nb.utils import one_cell_notebook, test_notebook
 
 
@@ -61,19 +60,23 @@
 
             cell.outputs = []
             self.shell.cell(cell)
 
             if counter is not None:
                 cell.execution_count = counter
 
-            for output in cell.outputs:
-                if output.get(
-                    "output_type", ""
-                ) == "error" and "StopExecution" in output.get("ename", ""):
-                    return False
+            try:
+                for output in cell.outputs:
+                    if output.get(
+                        "output_type", ""
+                    ) == "error" and "StopExecution" in output.get("ename", ""):
+                        return False
+            except Exception as e:
+                pass
+
         return True
 
     def run_notebook(self, nb, start=0):
         #
         # nb is fastai format
         #
         counter = start + 1
```

### Comparing `mercury-2.1.9/mercury/apps/nb/tests.py` & `mercury-2.2.0/mercury/apps/nb/tests.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/nbworker/__main__.py` & `mercury-2.2.0/mercury/apps/nbworker/__main__.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/nbworker/nb.py` & `mercury-2.2.0/mercury/apps/nbworker/nb.py`

 * *Files 6% similar despite different names*

```diff
@@ -285,14 +285,25 @@
         if "127.0.0.1" not in self.ws_address and "localhost" not in self.ws_address:
             fname = "requirements.txt"
             if os.path.exists(fname):
                 log.debug(f"Install new packages from requirements.txt")
                 cmd = f"pip install -r {fname}"
                 self.nbrun.run_code(cmd)
 
+    def provision_secrets(self):
+        secrets = self.list_secrets()
+        if secrets:
+            cmd = "import os\n"
+            for s in secrets:
+                name = s.get("name", "")
+                secret = s.get("secret", "")
+                cmd += f'os.environ["{name}"] = "{secret}"'
+            log.debug("Set secrets")
+            self.nbrun.run_code(cmd)
+
     def init_notebook(self):
         log.debug(f"Init notebook, show_code={self.show_code()}")
 
         self.sm.provision_uploaded_files()
 
         self.prev_nb = None
         self.prev_widgets = {}
@@ -304,14 +315,15 @@
             show_code=self.show_code(),
             show_prompt=self.show_prompt(),
             is_presentation=self.is_presentation(),
             reveal_theme=self.reveal_theme(),
         )
 
         self.install_new_packages()
+        self.provision_secrets()
 
         # we need to initialize the output dir always
         # even if there is no OutputDir in the notebook
         self.initialize_outputdir()
 
         self.nb_original = read_nb(self.notebook.path)
```

### Comparing `mercury-2.1.9/mercury/apps/nbworker/rest.py` & `mercury-2.2.0/mercury/apps/nbworker/rest.py`

 * *Files 8% similar despite different names*

```diff
@@ -188,7 +188,18 @@
             return True
 
         except Exception:
             log.exception(
                 f"Exception when check if worker id={self.worker_id} is stale"
             )
         return True
+
+    def list_secrets(self):
+        try:
+            response = requests.get(
+                f"{self.server_url}/api/v1/worker/{self.session_id}/{self.worker_id}/{self.notebook_id}/worker-secrets",
+            )
+            if response.status_code == 200:
+                return response.json()
+        except Exception:
+            log.exception(f"Exception when list worker id={self.worker_id} secrets")
+        return []
```

### Comparing `mercury-2.1.9/mercury/apps/nbworker/tests.py` & `mercury-2.2.0/mercury/apps/nbworker/tests.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/nbworker/utils.py` & `mercury-2.2.0/mercury/apps/nbworker/utils.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/nbworker/ws.py` & `mercury-2.2.0/mercury/apps/nbworker/ws.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/notebooks/management/commands/add.py` & `mercury-2.2.0/mercury/apps/notebooks/management/commands/add.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/notebooks/management/commands/delete.py` & `mercury-2.2.0/mercury/apps/notebooks/management/commands/delete.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/notebooks/management/commands/list.py` & `mercury-2.2.0/mercury/apps/notebooks/management/commands/list.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/notebooks/management/commands/watch.py` & `mercury-2.2.0/mercury/apps/notebooks/management/commands/watch.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/notebooks/migrations/0001_initial.py` & `mercury-2.2.0/mercury/apps/notebooks/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/notebooks/models.py` & `mercury-2.2.0/mercury/apps/notebooks/models.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/notebooks/serializers.py` & `mercury-2.2.0/mercury/apps/notebooks/serializers.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/notebooks/slides_themes.py` & `mercury-2.2.0/mercury/apps/notebooks/slides_themes.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/notebooks/tasks.py` & `mercury-2.2.0/mercury/apps/notebooks/tasks.py`

 * *Files 10% similar despite different names*

```diff
@@ -23,14 +23,16 @@
 from apps.nb.exporter import Exporter
 from apps.notebooks.models import Notebook
 from apps.storage.s3utils import S3
 from apps.tasks.models import Task
 from apps.tasks.notify import validate_notify
 from apps.ws.utils import parse_params
 
+# from apps.tasks.export_png import to_png
+
 log = logging.getLogger(__name__)
 
 
 def process_nbconvert_errors(error_msg):
     known_warnings = [
         "warn(",
         "UserWarning",
@@ -265,14 +267,21 @@
                 format=json.dumps(notebook_format),
                 schedule=notebook_schedule,
                 notify=json.dumps(notebook_notify),
                 errors=parse_errors,
                 created_by=user,
                 hosted_on=site,
             )
+
+            # html_file = os.path.join(settings.MEDIA_ROOT, f"{notebook_output_file}.html")
+            # png_file = os.path.join(settings.MEDIA_ROOT, f"{notebook_output_file}.png")
+            # print(html_file)
+            # print(png_file)
+            # to_png(html_file, png_file)
+
         else:
             notebook = Notebook.objects.get(pk=notebook_id)
             notebook.title = notebook_title
             notebook.slug = notebook_slug
             notebook.path = os.path.abspath(notebook_path)
             notebook.state = "WATCH_READY" if is_watch_mode else "READY"
             notebook.params = json.dumps(params)
```

### Comparing `mercury-2.1.9/mercury/apps/notebooks/urls.py` & `mercury-2.2.0/mercury/apps/notebooks/urls.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/notebooks/views.py` & `mercury-2.2.0/mercury/apps/notebooks/views.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/storage/migrations/0001_initial.py` & `mercury-2.2.0/mercury/apps/storage/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/storage/migrations/0002_useruploadedfile.py` & `mercury-2.2.0/mercury/apps/storage/migrations/0002_useruploadedfile.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/storage/models.py` & `mercury-2.2.0/mercury/apps/storage/models.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/storage/s3utils.py` & `mercury-2.2.0/mercury/apps/storage/s3utils.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/storage/storage.py` & `mercury-2.2.0/mercury/apps/storage/storage.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/storage/tests.py` & `mercury-2.2.0/mercury/apps/storage/tests.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/storage/urls.py` & `mercury-2.2.0/mercury/apps/storage/urls.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/storage/views/dashboardfiles.py` & `mercury-2.2.0/mercury/apps/storage/views/dashboardfiles.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/storage/views/notebookfiles.py` & `mercury-2.2.0/mercury/apps/storage/views/notebookfiles.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/storage/views/workerfiles.py` & `mercury-2.2.0/mercury/apps/storage/views/workerfiles.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/tasks/export_pdf.py` & `mercury-2.2.0/mercury/apps/tasks/export_pdf.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/tasks/migrations/0001_initial.py` & `mercury-2.2.0/mercury/apps/tasks/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/tasks/models.py` & `mercury-2.2.0/mercury/apps/tasks/models.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/tasks/notify.py` & `mercury-2.2.0/mercury/apps/tasks/notify.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/tasks/tasks.py` & `mercury-2.2.0/mercury/apps/tasks/tasks.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/tasks/tasks_export.py` & `mercury-2.2.0/mercury/apps/tasks/tasks_export.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/tasks/tests.py` & `mercury-2.2.0/mercury/apps/tasks/tests.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/tasks/urls.py` & `mercury-2.2.0/mercury/apps/tasks/urls.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/tasks/views.py` & `mercury-2.2.0/mercury/apps/tasks/views.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/workers/migrations/0001_initial.py` & `mercury-2.2.0/mercury/apps/workers/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/workers/models.py` & `mercury-2.2.0/mercury/apps/workers/models.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/workers/urls.py` & `mercury-2.2.0/mercury/apps/workers/urls.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/workers/views.py` & `mercury-2.2.0/mercury/apps/workers/views.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/ws/client.py` & `mercury-2.2.0/mercury/apps/ws/client.py`

 * *Files 4% similar despite different names*

```diff
@@ -107,14 +107,26 @@
     def broadcast_message(self, event):
         payload = event["payload"]
         self.send(text_data=json.dumps(payload))
 
     def need_worker(self):
         if self.server_address is None:
             return
+
+        # usage = json.loads(self.site_owner.profile.usage).get("usage", 0)
+        # log.debug(f"Current usage {usage} seconds")
+
+        # async_to_sync(self.channel_layer.group_send)(
+        #     self.client_group,
+        #     {
+        #         "type": "broadcast_message",
+        #         "payload": {"purpose": "worker-state", "state": "UsageLimitReached"},
+        #     },
+        # )
+
         with transaction.atomic():
             log.debug("Create worker in db")
             worker = Worker(
                 session_id=self.session_id,
                 notebook_id=self.notebook_id,
                 state="Queued",
             )
```

### Comparing `mercury-2.1.9/mercury/apps/ws/middleware.py` & `mercury-2.2.0/mercury/apps/ws/middleware.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/apps/ws/utils.py` & `mercury-2.2.0/mercury/apps/ws/utils.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,23 +1,34 @@
+import os
 import json
 import logging
 import platform
-
+import requests
 import nbformat
 
 from widgets.manager import WidgetsManager
 
 log = logging.getLogger(__name__)
 
 
 CLIENT_SITE = "client"
 WORKER_SITE = "worker"
 
 
+my_ip = None
+
+
 def machine_uuid():
+    global my_ip
+    if my_ip is not None:
+        return my_ip
+    if os.environ.get("USE_WORKER_IP") is not None:
+        response = requests.get("https://api.ipify.org?format=json")
+        my_ip = response.json().get("ip", platform.node())
+        return my_ip
     return platform.node()
 
 
 def client_group(notebook_id, session_id):
     return f"{CLIENT_SITE}-{notebook_id}-{session_id}"
```

### Comparing `mercury-2.1.9/mercury/apps/ws/worker.py` & `mercury-2.2.0/mercury/apps/ws/worker.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/demo.py` & `mercury-2.2.0/mercury/demo.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/asset-manifest.json` & `mercury-2.2.0/mercury/frontend-dist/asset-manifest.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8974358974358974%*

 * *Differences: {"'entrypoints'": "{insert: [(4, 'static/js/main.717ee96a.chunk.js')], delete: [4]}",*

 * * "'files'": "{'main.js': '/static/js/main.717ee96a.chunk.js', 'main.js.map': "*

 * *            "'/static/js/main.717ee96a.chunk.js.map'}"}*

```diff
@@ -1,20 +1,20 @@
 {
     "entrypoints": [
         "static/js/runtime-main.248907bc.js",
         "static/css/2.c6cf5ff9.chunk.css",
         "static/js/2.20950ecb.chunk.js",
         "static/css/main.26f96620.chunk.css",
-        "static/js/main.b729f6a0.chunk.js"
+        "static/js/main.717ee96a.chunk.js"
     ],
     "files": {
         "index.html": "/index.html",
         "main.css": "/static/css/main.26f96620.chunk.css",
-        "main.js": "/static/js/main.b729f6a0.chunk.js",
-        "main.js.map": "/static/js/main.b729f6a0.chunk.js.map",
+        "main.js": "/static/js/main.717ee96a.chunk.js",
+        "main.js.map": "/static/js/main.717ee96a.chunk.js.map",
         "runtime-main.js": "/static/js/runtime-main.248907bc.js",
         "runtime-main.js.map": "/static/js/runtime-main.248907bc.js.map",
         "static/css/2.c6cf5ff9.chunk.css": "/static/css/2.c6cf5ff9.chunk.css",
         "static/css/2.c6cf5ff9.chunk.css.map": "/static/css/2.c6cf5ff9.chunk.css.map",
         "static/css/main.26f96620.chunk.css.map": "/static/css/main.26f96620.chunk.css.map",
         "static/js/2.20950ecb.chunk.js": "/static/js/2.20950ecb.chunk.js",
         "static/js/2.20950ecb.chunk.js.LICENSE.txt": "/static/js/2.20950ecb.chunk.js.LICENSE.txt",
```

### Comparing `mercury-2.1.9/mercury/frontend-dist/favicon-old.ico` & `mercury-2.2.0/mercury/frontend-dist/favicon-old.ico`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/favicon.ico` & `mercury-2.2.0/mercury/frontend-dist/favicon.ico`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/index.html` & `mercury-2.2.0/mercury/frontend-dist/index.html`

 * *Files 3% similar despite different names*

```diff
@@ -1 +1 @@
-<!doctype html><html lang="en"><head><meta charset="utf-8"/><link rel="icon" href="/static/favicon.ico"/><meta name="viewport" content="width=device-width,initial-scale=1"/><meta name="theme-color" content="#000000"/><meta name="description" content="Mercury: Easily share your Python notebooks"/><link rel="manifest" href="/static/manifest.json"/><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script><link rel="stylesheet" href="/static/jupyter-syntax.css"/><link rel="stylesheet" href="/static/jupyter-additional.css"/><link rel="stylesheet" href="/static/jupyter-theme-light.css"/><title>Mercury - Turn Jupyter Notebook to Web App</title><script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"></script><script>init_mathjax=function(){window.MathJax&&(MathJax.Hub.Config({showProcessingMessages:!1,TeX:{equationNumbers:{autoNumber:"AMS",useLabelIds:!0}},tex2jax:{inlineMath:[["$","$"],["\\(","\\)"]],displayMath:[["$$","$$"],["\\[","\\]"]],processEscapes:!0,processEnvironments:!0},displayAlign:"center",CommonHTML:{linebreaks:{automatic:!0}}}),MathJax.Hub.Queue(["Typeset",MathJax.Hub]))},init_mathjax()</script><link href="/static/css/2.c6cf5ff9.chunk.css" rel="stylesheet"><link href="/static/css/main.26f96620.chunk.css" rel="stylesheet"></head><body><noscript>You need to enable JavaScript to run this app.</noscript><div id="root"></div><script>!function(e){function r(r){for(var n,f,l=r[0],i=r[1],a=r[2],c=0,s=[];c<l.length;c++)f=l[c],Object.prototype.hasOwnProperty.call(o,f)&&o[f]&&s.push(o[f][0]),o[f]=0;for(n in i)Object.prototype.hasOwnProperty.call(i,n)&&(e[n]=i[n]);for(p&&p(r);s.length;)s.shift()();return u.push.apply(u,a||[]),t()}function t(){for(var e,r=0;r<u.length;r++){for(var t=u[r],n=!0,l=1;l<t.length;l++){var i=t[l];0!==o[i]&&(n=!1)}n&&(u.splice(r--,1),e=f(f.s=t[0]))}return e}var n={},o={1:0},u=[];function f(r){if(n[r])return n[r].exports;var t=n[r]={i:r,l:!1,exports:{}};return e[r].call(t.exports,t,t.exports,f),t.l=!0,t.exports}f.m=e,f.c=n,f.d=function(e,r,t){f.o(e,r)||Object.defineProperty(e,r,{enumerable:!0,get:t})},f.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},f.t=function(e,r){if(1&r&&(e=f(e)),8&r)return e;if(4&r&&"object"==typeof e&&e&&e.__esModule)return e;var t=Object.create(null);if(f.r(t),Object.defineProperty(t,"default",{enumerable:!0,value:e}),2&r&&"string"!=typeof e)for(var n in e)f.d(t,n,function(r){return e[r]}.bind(null,n));return t},f.n=function(e){var r=e&&e.__esModule?function(){return e.default}:function(){return e};return f.d(r,"a",r),r},f.o=function(e,r){return Object.prototype.hasOwnProperty.call(e,r)},f.p="/";var l=this.webpackJsonpfrontend=this.webpackJsonpfrontend||[],i=l.push.bind(l);l.push=r,l=l.slice();for(var a=0;a<l.length;a++)r(l[a]);var p=i;t()}([])</script><script src="/static/js/2.20950ecb.chunk.js"></script><script src="/static/js/main.b729f6a0.chunk.js"></script></body></html>
+<!doctype html><html lang="en"><head><meta charset="utf-8"/><link rel="icon" href="/static/favicon.ico"/><meta name="viewport" content="width=device-width,initial-scale=1"/><meta name="theme-color" content="#000000"/><meta name="description" content="Mercury: Easily share your Python notebooks"/><link rel="manifest" href="/static/manifest.json"/><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script><link rel="stylesheet" href="/static/jupyter-syntax.css"/><link rel="stylesheet" href="/static/jupyter-additional.css"/><link rel="stylesheet" href="/static/jupyter-theme-light.css"/><title>Mercury - Turn Jupyter Notebook to Web App</title><script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"></script><script>init_mathjax=function(){window.MathJax&&(MathJax.Hub.Config({showProcessingMessages:!1,TeX:{equationNumbers:{autoNumber:"AMS",useLabelIds:!0}},tex2jax:{inlineMath:[["$","$"],["\\(","\\)"]],displayMath:[["$$","$$"],["\\[","\\]"]],processEscapes:!0,processEnvironments:!0},displayAlign:"center",CommonHTML:{linebreaks:{automatic:!0}}}),MathJax.Hub.Queue(["Typeset",MathJax.Hub]))},init_mathjax()</script><link href="/static/css/2.c6cf5ff9.chunk.css" rel="stylesheet"><link href="/static/css/main.26f96620.chunk.css" rel="stylesheet"></head><body><noscript>You need to enable JavaScript to run this app.</noscript><div id="root"></div><script>!function(e){function r(r){for(var n,f,l=r[0],i=r[1],a=r[2],c=0,s=[];c<l.length;c++)f=l[c],Object.prototype.hasOwnProperty.call(o,f)&&o[f]&&s.push(o[f][0]),o[f]=0;for(n in i)Object.prototype.hasOwnProperty.call(i,n)&&(e[n]=i[n]);for(p&&p(r);s.length;)s.shift()();return u.push.apply(u,a||[]),t()}function t(){for(var e,r=0;r<u.length;r++){for(var t=u[r],n=!0,l=1;l<t.length;l++){var i=t[l];0!==o[i]&&(n=!1)}n&&(u.splice(r--,1),e=f(f.s=t[0]))}return e}var n={},o={1:0},u=[];function f(r){if(n[r])return n[r].exports;var t=n[r]={i:r,l:!1,exports:{}};return e[r].call(t.exports,t,t.exports,f),t.l=!0,t.exports}f.m=e,f.c=n,f.d=function(e,r,t){f.o(e,r)||Object.defineProperty(e,r,{enumerable:!0,get:t})},f.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},f.t=function(e,r){if(1&r&&(e=f(e)),8&r)return e;if(4&r&&"object"==typeof e&&e&&e.__esModule)return e;var t=Object.create(null);if(f.r(t),Object.defineProperty(t,"default",{enumerable:!0,value:e}),2&r&&"string"!=typeof e)for(var n in e)f.d(t,n,function(r){return e[r]}.bind(null,n));return t},f.n=function(e){var r=e&&e.__esModule?function(){return e.default}:function(){return e};return f.d(r,"a",r),r},f.o=function(e,r){return Object.prototype.hasOwnProperty.call(e,r)},f.p="/";var l=this.webpackJsonpfrontend=this.webpackJsonpfrontend||[],i=l.push.bind(l);l.push=r,l=l.slice();for(var a=0;a<l.length;a++)r(l[a]);var p=i;t()}([])</script><script src="/static/js/2.20950ecb.chunk.js"></script><script src="/static/js/main.717ee96a.chunk.js"></script></body></html>
```

### Comparing `mercury-2.1.9/mercury/frontend-dist/jupyter-additional.css` & `mercury-2.2.0/mercury/frontend-dist/jupyter-additional.css`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/jupyter-syntax.css` & `mercury-2.2.0/mercury/frontend-dist/jupyter-syntax.css`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/jupyter-theme-light.css` & `mercury-2.2.0/mercury/frontend-dist/jupyter-theme-light.css`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/mercury_black_logo.svg` & `mercury-2.2.0/mercury/frontend-dist/mercury_black_logo.svg`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/mercury_logo.svg` & `mercury-2.2.0/mercury/frontend-dist/mercury_logo.svg`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/css/2.c6cf5ff9.chunk.css` & `mercury-2.2.0/mercury/frontend-dist/static/css/2.c6cf5ff9.chunk.css`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/css/2.c6cf5ff9.chunk.css.map` & `mercury-2.2.0/mercury/frontend-dist/static/css/2.c6cf5ff9.chunk.css.map`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/css/main.26f96620.chunk.css` & `mercury-2.2.0/mercury/frontend-dist/static/css/main.26f96620.chunk.css`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/css/main.26f96620.chunk.css.map` & `mercury-2.2.0/mercury/frontend-dist/static/css/main.26f96620.chunk.css.map`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/js/2.20950ecb.chunk.js` & `mercury-2.2.0/mercury/frontend-dist/static/js/2.20950ecb.chunk.js`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/js/2.20950ecb.chunk.js.LICENSE.txt` & `mercury-2.2.0/mercury/frontend-dist/static/js/2.20950ecb.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/js/2.20950ecb.chunk.js.map` & `mercury-2.2.0/mercury/frontend-dist/static/js/2.20950ecb.chunk.js.map`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/js/main.b729f6a0.chunk.js` & `mercury-2.2.0/mercury/frontend-dist/static/js/main.717ee96a.chunk.js`

 * *Files 16% similar despite different names*

#### js-beautify {}

```diff
@@ -4,16 +4,16 @@
         293: function(e, t, a) {},
         295: function(e, t, a) {
             "use strict";
             a.r(t);
             var n = a(1),
                 o = a(39),
                 s = a(313),
-                r = a(5),
-                i = a(11),
+                i = a(5),
+                r = a(11),
                 c = a(20),
                 l = a(6),
                 d = a.n(l),
                 u = a(13),
                 b = a(25),
                 p = a(22),
                 j = a(126),
@@ -68,77 +68,77 @@
                 P = k.setUserInfo,
                 C = function(e) {
                     return e.auth.token
                 },
                 T = function(e) {
                     return e.auth.username
                 },
-                E = function(e) {
+                _ = function(e) {
                     return e.auth.user
                 },
                 R = a(9),
-                _ = (a(193), a(0));
+                E = (a(193), a(0));
 
             function F() {
-                return Object(_.jsx)("div", {
+                return Object(E.jsx)("div", {
                     style: {
                         color: "white",
                         padding: "5px",
                         float: "right"
                     },
-                    children: Object(_.jsxs)(c.b, {
+                    children: Object(E.jsxs)(c.b, {
                         to: "/login",
                         className: "btn btn-primary btn-sm ",
-                        children: [Object(_.jsx)("i", {
+                        children: [Object(E.jsx)("i", {
                             className: "fa fa-sign-in",
                             "aria-hidden": "true"
                         }), " Log in"]
                     })
                 })
             }
 
             function A(e) {
                 var t = e.username,
-                    a = Object(r.b)(),
-                    n = Object(i.o)();
-                return Object(_.jsx)("div", {
-                    children: Object(_.jsxs)("div", {
+                    a = Object(i.b)(),
+                    n = Object(r.o)();
+                return Object(E.jsx)("div", {
+                    children: Object(E.jsxs)("div", {
                         className: "dropdown",
                         style: {
                             float: "right"
                         },
-                        children: [Object(_.jsx)("a", {
+                        children: [Object(E.jsx)("a", {
                             className: "btn btn-secondary btn-sm dropdown-toggle",
                             style: {
                                 margin: "5px"
                             },
                             href: "#",
                             role: "button",
                             id: "dropdownMenuLink",
                             "data-bs-toggle": "dropdown",
                             "aria-expanded": "false",
                             children: t
-                        }), Object(_.jsxs)("ul", {
+                        }), Object(E.jsxs)("ul", {
                             className: "dropdown-menu dropdown-menu-end",
                             "aria-labelledby": "dropdownMenuLink",
-                            children: [Object(_.jsx)("li", {
-                                children: Object(_.jsxs)("a", {
+                            children: [Object(E.jsx)("li", {
+                                children: Object(E.jsxs)("a", {
                                     className: "dropdown-item",
                                     href: "/account",
-                                    children: [Object(_.jsx)("i", {
+                                    children: [Object(E.jsx)("i", {
                                         className: "fa fa-user",
                                         "aria-hidden": "true"
                                     }), " Account"]
                                 })
-                            }), Object(_.jsx)("li", {
-                                children: Object(_.jsx)("hr", {
+                            }), Object(E.jsx)("li", {
+                                children: Object(E.jsx)("hr", {
                                     className: "dropdown-divider"
                                 })
-                            }), Object(_.jsx)("li", {
-                                children: Object(_.jsxs)("a", {
+                            }), Object(E.jsx)("li", {
+                                children: Object(E.jsxs)("a", {
                                     className: "dropdown-item",
                                     onClick: function() {
                                         return a(function(e) {
                                             return function() {
                                                 var t = Object(u.a)(d.a.mark((function t(a) {
                                                     return d.a.wrap((function(t) {
                                                         for (;;) switch (t.prev = t.next) {
@@ -159,49 +159,49 @@
                                                 })));
                                                 return function(e) {
                                                     return t.apply(this, arguments)
                                                 }
                                             }()
                                         }(n))
                                     },
-                                    children: [Object(_.jsx)("i", {
+                                    children: [Object(E.jsx)("i", {
                                         className: "fa fa-sign-out",
                                         "aria-hidden": "true"
                                     }), " Log out"]
                                 })
                             })]
                         })]
                     })
                 })
             }
 
-            function I(e) {
+            function M(e) {
                 var t = e.isSitePublic,
                     a = e.username;
-                return Object(_.jsxs)("header", {
+                return Object(E.jsxs)("header", {
                     className: "navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0",
-                    children: [Object(_.jsx)(c.b, {
+                    children: [Object(E.jsx)(c.b, {
                         className: "navbar-brand col-md-3 col-lg-3 me-0 px-3",
                         to: "/",
-                        children: Object(_.jsx)("img", {
+                        children: Object(E.jsx)("img", {
                             alt: "Mercury",
                             src: "/static/mercury_logo.svg",
                             style: {
                                 height: "28px",
                                 paddingLeft: "10px"
                             }
                         })
-                    }), !t && "" === a && Object(_.jsx)(F, {}), "" !== a && Object(_.jsx)(A, {
+                    }), !t && "" === a && Object(E.jsx)(F, {}), "" !== a && Object(E.jsx)(A, {
                         username: a
                     })]
                 })
             }
             var D = a(14),
-                W = a(27),
-                M = Object(b.b)({
+                I = a(27),
+                L = Object(b.b)({
                     name: "app",
                     initialState: {
                         view: "app",
                         files: [],
                         filesState: "unknown",
                         showSideBar: !0,
                         storageType: "media"
@@ -223,21 +223,21 @@
                             e.showSideBar = !e.showSideBar
                         },
                         setStorageType: function(e, t) {
                             e.storageType = t.payload
                         }
                     }
                 }),
-                U = M.reducer,
-                L = M.actions,
-                H = L.setView,
-                z = L.setFilesState,
-                B = L.setFiles,
-                V = L.setShowSideBar,
-                J = (L.toggleShowSideBar, L.setStorageType),
+                U = L.reducer,
+                W = L.actions,
+                H = W.setView,
+                z = W.setFilesState,
+                B = W.setFiles,
+                V = W.setShowSideBar,
+                J = (W.toggleShowSideBar, W.setStorageType),
                 K = function(e) {
                     return e.app.view
                 },
                 q = function(e) {
                     return e.app.filesState
                 },
                 Y = function(e) {
@@ -248,23 +248,23 @@
                 },
                 Q = function(e) {
                     return e.app.storageType
                 },
                 Z = function(e, t, a) {
                     return function() {
                         var n = Object(u.a)(d.a.mark((function n(o) {
-                            var r;
+                            var i;
                             return d.a.wrap((function(n) {
                                 for (;;) switch (n.prev = n.next) {
                                     case 0:
-                                        return n.prev = 0, r = {
+                                        return n.prev = 0, i = {
                                             site_id: e,
                                             session_id: t,
                                             filename: a
-                                        }, "/api/v1/nb-delete-file", n.next = 5, s.a.post("/api/v1/nb-delete-file", r);
+                                        }, "/api/v1/nb-delete-file", n.next = 5, s.a.post("/api/v1/nb-delete-file", i);
                                     case 5:
                                         n.next = 10;
                                         break;
                                     case 7:
                                         n.prev = 7, n.t0 = n.catch(0), console.error("Problem with file upload. ".concat(n.t0));
                                     case 10:
                                     case "end":
@@ -308,19 +308,19 @@
                 return "text" === e.input
             }
 
             function se(e) {
                 return "dir" === e.output
             }
 
-            function re(e) {
+            function ie(e) {
                 return "markdown" === e.output
             }
 
-            function ie(e) {
+            function re(e) {
                 return "button" === e.input
             }
 
             function ce() {
                 var e = window;
                 return {
                     width: e.innerWidth,
@@ -375,49 +375,49 @@
                         setLoadingStateSelected: function(e, t) {
                             e.loadingStateSelected = t.payload
                         },
                         setSlidesHash: function(e, t) {
                             e.slidesHash = t.payload
                         },
                         updateWidgetsParams: function(e, t) {
-                            for (var a = t.payload.widgetKey, n = !1, o = !0, s = 0, r = Object.keys(e.selectedNotebook.params.params); s < r.length; s++) {
-                                var i = r[s];
-                                if (i === a) {
+                            for (var a = t.payload.widgetKey, n = !1, o = !0, s = 0, i = Object.keys(e.selectedNotebook.params.params); s < i.length; s++) {
+                                var r = i[s];
+                                if (r === a) {
                                     o = !1;
                                     var c = Object(D.a)({}, e.selectedNotebook.params.params[a]);
-                                    ae(c) ? (c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[i] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[i] = t.payload.value, n = !0), c.min !== t.payload.min && (c.min = t.payload.min, e.widgets[i] = t.payload.value, n = !0), c.max !== t.payload.max && (c.max = t.payload.max, e.widgets[i] = t.payload.value, n = !0), c.step !== t.payload.step && (c.step = t.payload.step, e.widgets[i] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)) : oe(c) ? (c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[i] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[i] = t.payload.value, n = !0), c.rows !== t.payload.rows && (c.rows = t.payload.rows, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)) : te(c) ? (c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[i] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[i] = t.payload.value, n = !0), c.min !== t.payload.min && (c.min = t.payload.min, e.widgets[i] = t.payload.value, n = !0), c.max !== t.payload.max && (c.max = t.payload.max, e.widgets[i] = t.payload.value, n = !0), c.step !== t.payload.step && (c.step = t.payload.step, e.widgets[i] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)) : X(c) ? (c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[i] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[i] = t.payload.value, n = !0), c.choices.toString() !== t.payload.choices.toString() && (c.choices = t.payload.choices, e.widgets[i] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)) : $(c) ? (c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[i] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[i] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)) : ee(c) ? (c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[i] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[i] = t.payload.value, n = !0), c.min !== t.payload.min && (c.min = t.payload.min, e.widgets[i] = t.payload.value, n = !0), c.max !== t.payload.max && (c.max = t.payload.max, e.widgets[i] = t.payload.value, n = !0), c.step !== t.payload.step && (c.step = t.payload.step, e.widgets[i] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)) : re(c) ? c.value !== t.payload.value && (c.value = t.payload.value, n = !0) : ie(c) ? (e.widgets[i] = t.payload.value, c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[i] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[i] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0), c.style !== t.payload.style && (c.style = t.payload.style, n = !0)) : ne(c) && (e.widgets[i] = t.payload.value, c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[i] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[i] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)), n && (e.selectedNotebook.params.params[a] = c)
+                                    ae(c) ? (c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[r] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[r] = t.payload.value, n = !0), c.min !== t.payload.min && (c.min = t.payload.min, e.widgets[r] = t.payload.value, n = !0), c.max !== t.payload.max && (c.max = t.payload.max, e.widgets[r] = t.payload.value, n = !0), c.step !== t.payload.step && (c.step = t.payload.step, e.widgets[r] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)) : oe(c) ? (c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[r] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[r] = t.payload.value, n = !0), c.rows !== t.payload.rows && (c.rows = t.payload.rows, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)) : te(c) ? (c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[r] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[r] = t.payload.value, n = !0), c.min !== t.payload.min && (c.min = t.payload.min, e.widgets[r] = t.payload.value, n = !0), c.max !== t.payload.max && (c.max = t.payload.max, e.widgets[r] = t.payload.value, n = !0), c.step !== t.payload.step && (c.step = t.payload.step, e.widgets[r] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)) : X(c) ? (c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[r] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[r] = t.payload.value, n = !0), c.choices.toString() !== t.payload.choices.toString() && (c.choices = t.payload.choices, e.widgets[r] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)) : $(c) ? (c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[r] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[r] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)) : ee(c) ? (c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[r] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[r] = t.payload.value, n = !0), c.min !== t.payload.min && (c.min = t.payload.min, e.widgets[r] = t.payload.value, n = !0), c.max !== t.payload.max && (c.max = t.payload.max, e.widgets[r] = t.payload.value, n = !0), c.step !== t.payload.step && (c.step = t.payload.step, e.widgets[r] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)) : ie(c) ? c.value !== t.payload.value && (c.value = t.payload.value, n = !0) : re(c) ? (e.widgets[r] = t.payload.value, c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[r] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[r] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0), c.style !== t.payload.style && (c.style = t.payload.style, n = !0)) : ne(c) && (e.widgets[r] = t.payload.value, c.disabled !== t.payload.disabled && (c.disabled = t.payload.disabled, e.widgets[r] = t.payload.value, n = !0), c.hidden !== t.payload.hidden && (c.hidden = t.payload.hidden, e.widgets[r] = t.payload.value, n = !0), c.label !== t.payload.label && (c.label = t.payload.label, n = !0)), n && (e.selectedNotebook.params.params[a] = c)
                                 }
                             }
                             o && (e.selectedNotebook.params.params[a] = t.payload)
                         },
                         hideWidgets: function(e, t) {
                             var a, n = t.payload.keys,
-                                o = Object(W.a)(n);
+                                o = Object(I.a)(n);
                             try {
                                 for (o.s(); !(a = o.n()).done;) {
                                     var s = a.value;
                                     s in e.selectedNotebook.params.params && delete e.selectedNotebook.params.params[s]
                                 }
-                            } catch (r) {
-                                o.e(r)
+                            } catch (i) {
+                                o.e(i)
                             } finally {
                                 o.f()
                             }
                         },
                         initWidgets: function(e, t) {
                             var a = t.payload.widgets;
                             e.selectedNotebook.params.params = {}, e.widgets = {};
-                            var n, o = Object(W.a)(a);
+                            var n, o = Object(I.a)(a);
                             try {
                                 for (o.s(); !(n = o.n()).done;) {
                                     var s = n.value;
                                     e.selectedNotebook.params.params[s.widgetKey] = s, e.widgets[s.widgetKey] = s.value
                                 }
-                            } catch (r) {
-                                o.e(r)
+                            } catch (i) {
+                                o.e(i)
                             } finally {
                                 o.f()
                             }
                         },
                         updateTitle: function(e, t) {
                             e.selectedNotebook.title = t.payload
                         },
@@ -454,40 +454,40 @@
                 Pe = be.setUrlValuesUsed,
                 Ce = function(e) {
                     return e.notebooks.notebooks
                 },
                 Te = function(e) {
                     return e.notebooks.loadingState
                 },
-                Ee = function(e) {
+                _e = function(e) {
                     return e.notebooks.selectedNotebook
                 },
                 Re = function(e) {
                     return e.notebooks.selectedNotebookId
                 },
-                _e = function(e) {
+                Ee = function(e) {
                     var t, a, n = null === (t = e.notebooks.selectedNotebook) || void 0 === t || null === (a = t.params) || void 0 === a ? void 0 : a.static_notebook;
                     return void 0 !== n && n
                 },
                 Fe = function(e) {
                     return e.notebooks.loadingStateSelected
                 },
                 Ae = function(e) {
                     return e.notebooks.slidesHash
                 },
-                Ie = function(e) {
+                Me = function(e) {
                     return e.notebooks.widgets
                 },
                 De = function(e) {
                     return e.notebooks.widgetsUrlValues
                 },
-                We = function(e) {
+                Ie = function(e) {
                     return e.notebooks.widgetsInitialized
                 },
-                Me = function(e) {
+                Le = function(e) {
                     return e.notebooks.urlValuesUsed
                 },
                 Ue = Object(b.b)({
                     name: "tasks",
                     initialState: {
                         currentTask: {},
                         historicTask: {},
@@ -533,15 +533,15 @@
                             e.executionHistory = t.payload
                         },
                         clearExecutionHistory: function(e) {
                             e.executionHistory = []
                         }
                     }
                 }),
-                Le = Ue.reducer,
+                We = Ue.reducer,
                 He = Ue.actions,
                 ze = (He.setShowCurrent, He.setCurrentTask, He.setHistoricTask, He.setPreviousTask, He.copyCurrentToPreviousTask, He.setExportingToPDF),
                 Be = He.setExportToPDFJobId,
                 Ve = He.resetExportToPDFCounter,
                 Je = He.increaseExportToPDFCounter,
                 Ke = He.stopPDFExport,
                 qe = (He.setExecutionHistory, He.clearExecutionHistory),
@@ -573,18 +573,18 @@
                 };
 
             function tt(e) {
                 var t = e.widgetKey,
                     a = e.label,
                     o = e.value,
                     s = e.disabled,
-                    i = e.hidden,
+                    r = e.hidden,
                     l = e.runNb,
                     d = e.url_key,
-                    u = Object(r.b)(),
+                    u = Object(i.b)(),
                     b = Object(n.useState)(!1),
                     p = Object(R.a)(b, 2),
                     j = p[0],
                     h = p[1],
                     v = Object(c.c)(),
                     f = Object(R.a)(v, 1)[0];
                 return Object(n.useEffect)((function() {
@@ -593,32 +593,32 @@
                         j || void 0 === a || "true" !== a && "false" !== a || (u(ge({
                             key: t,
                             value: "true" === a
                         })), u(Pe(!0)))
                     }
                 }), [u, f, j, d, t]), Object(n.useEffect)((function() {
                     j && l()
-                }), [o]), Object(_.jsxs)("div", {
+                }), [o]), Object(E.jsxs)("div", {
                     className: "form-group form-check form-switch mb-3",
                     style: {
-                        display: i ? "none" : ""
+                        display: r ? "none" : ""
                     },
-                    children: [Object(_.jsx)("input", {
+                    children: [Object(E.jsx)("input", {
                         className: "form-check-input",
                         type: "checkbox",
                         id: "checkbox-".concat(a),
                         disabled: s,
                         onChange: function() {
                             h(!0), u(Oe({
                                 key: t,
                                 value: !o
                             }))
                         },
                         checked: null != o && o
-                    }), Object(_.jsx)("label", {
+                    }), Object(E.jsx)("label", {
                         className: "form-check-label",
                         htmlFor: "checkbox-".concat(a),
                         style: {
                             color: s ? "#555" : "#212529"
                         },
                         children: a
                     })]
@@ -626,97 +626,97 @@
             }
 
             function at(e) {
                 var t = e.widgetKey,
                     a = e.label,
                     o = e.value,
                     s = e.min,
-                    i = e.max,
+                    r = e.max,
                     l = e.step,
                     d = e.disabled,
                     u = e.hidden,
                     b = e.runNb,
                     p = e.continuousUpdate,
                     j = e.url_key,
-                    h = Object(r.b)(),
+                    h = Object(i.b)(),
                     v = Object(n.useState)(!1),
                     f = Object(R.a)(v, 2),
                     m = f[0],
                     x = f[1],
                     O = Object(n.useState)(!1),
                     g = Object(R.a)(O, 2),
                     y = g[0],
                     w = g[1],
                     k = 0,
                     N = 10,
                     S = 1;
-                null !== s && (k = s), null !== i && (N = i), null !== l && (S = l);
+                null !== s && (k = s), null !== r && (N = r), null !== l && (S = l);
                 var P = null !== o && void 0 !== o ? o : 0,
                     C = Object(c.c)(),
                     T = Object(R.a)(C, 1)[0];
                 Object(n.useEffect)((function() {
                     if (void 0 !== j && "" !== j) {
                         var e = T.get(j);
                         !y && void 0 !== e && null !== e && !isNaN(parseFloat(e)) && parseFloat(e) >= k && parseFloat(e) <= N && (h(ge({
                             key: t,
                             value: parseFloat(e)
                         })), h(Pe(!0)))
                     }
                 }), [h, N, k, T, y, j, t]);
-                var E = function() {
+                var _ = function() {
                     null !== s && null !== o && o < s && h(Oe({
                         key: t,
                         value: s
-                    })), null !== i && null !== o && o > i && h(Oe({
+                    })), null !== r && null !== o && o > r && h(Oe({
                         key: t,
-                        value: i
+                        value: r
                     }))
                 };
-                return Object(_.jsxs)("div", {
+                return Object(E.jsxs)("div", {
                     className: "form-group mb-3",
                     style: {
                         display: u ? "none" : ""
                     },
-                    children: [Object(_.jsx)("label", {
+                    children: [Object(E.jsx)("label", {
                         htmlFor: "checkbox-".concat(a),
                         style: {
                             color: d ? "#555" : "#212529"
                         },
                         children: a
-                    }), Object(_.jsx)("input", {
+                    }), Object(E.jsx)("input", {
                         className: "form-control",
                         type: "number",
                         value: P,
                         onChange: function(e) {
                             w(!0), x(!0), h(Oe({
                                 key: t,
                                 value: e.target.value
                             }))
                         },
                         onBlur: function(e) {
-                            E()
+                            _()
                         },
                         onKeyPress: function(e) {
-                            "Enter" === e.key && (E(), b(), x(!1), e.preventDefault())
+                            "Enter" === e.key && (_(), b(), x(!1), e.preventDefault())
                         },
                         min: k,
                         max: N,
                         step: S,
                         disabled: d
-                    }), m && p && Object(_.jsx)("div", {
+                    }), m && p && Object(E.jsx)("div", {
                         style: {
                             float: "right",
                             position: "relative",
                             top: "0px",
                             left: "0px"
                         },
-                        children: Object(_.jsx)("button", {
+                        children: Object(E.jsx)("button", {
                             className: "btn btn-sm btn-outline-primary",
                             onClick: function(e) {
-                                E(), b(), x(!1), e.preventDefault()
+                                _(), b(), x(!1), e.preventDefault()
                             },
                             style: {
                                 fontSize: "0.7em",
                                 border: "none"
                             },
                             children: "Press enter or click to apply"
                         })
@@ -726,25 +726,25 @@
             var nt = a(58);
 
             function ot(e) {
                 var t = e.widgetKey,
                     a = e.label,
                     o = e.value,
                     s = e.min,
-                    i = e.max,
+                    r = e.max,
                     l = e.step,
                     d = (e.vertical, e.disabled),
                     u = e.hidden,
                     b = e.runNb,
                     p = e.url_key,
                     j = 0,
                     h = 100,
                     v = 1;
-                s && (j = s), i && (h = i), l && (v = l);
-                var f = Object(r.b)(),
+                s && (j = s), r && (h = r), l && (v = l);
+                var f = Object(i.b)(),
                     m = Object(n.useState)(!1),
                     x = Object(R.a)(m, 2),
                     O = x[0],
                     g = x[1],
                     y = Object(c.c)(),
                     w = Object(R.a)(y, 1)[0];
                 Object(n.useEffect)((function() {
@@ -755,33 +755,33 @@
                         !O && void 0 !== a && 2 === a.length && void 0 !== a[0] && !isNaN(a[0]) && void 0 !== a[1] && !isNaN(a[1]) && a[0] <= a[1] && a[0] >= j && a[1] <= h && (f(ge({
                             key: t,
                             value: a
                         })), f(Pe(!0)))
                     }
                 }), [f, h, j, w, O, p, t]);
                 var k = null != o && void 0 !== o && 2 === o.length ? o : [j, h];
-                return Object(_.jsxs)("div", {
+                return Object(E.jsxs)("div", {
                     className: "form-group mb-3",
                     style: {
                         display: u ? "none" : ""
                     },
-                    children: [Object(_.jsx)("label", {
+                    children: [Object(E.jsx)("label", {
                         htmlFor: "range-slider-".concat(a),
                         style: {
                             color: d ? "#555" : "#212529"
                         },
                         children: a
-                    }), Object(_.jsx)("div", {
+                    }), Object(E.jsx)("div", {
                         style: {
                             paddingTop: "12px",
                             display: "flex",
                             justifyContent: "center",
                             flexWrap: "wrap"
                         },
-                        children: Object(_.jsx)(nt.Range, {
+                        children: Object(E.jsx)(nt.Range, {
                             disabled: d,
                             values: k,
                             step: v,
                             min: j,
                             max: h,
                             onChange: function(e) {
                                 g(!0), f(ye()), f(Oe({
@@ -791,114 +791,114 @@
                             },
                             onFinalChange: function(e) {
                                 b()
                             },
                             renderTrack: function(e) {
                                 var t = e.props,
                                     a = e.children;
-                                return Object(_.jsx)("div", {
+                                return Object(E.jsx)("div", {
                                     onMouseDown: t.onMouseDown,
                                     onTouchStart: t.onTouchStart,
                                     style: Object(D.a)(Object(D.a)({}, t.style), {}, {
                                         height: "36px",
                                         display: "flex",
                                         width: "100%"
                                     }),
-                                    children: Object(_.jsxs)("div", {
+                                    children: Object(E.jsxs)("div", {
                                         ref: t.ref,
                                         style: {
                                             height: "5px",
                                             width: "100%",
                                             borderRadius: "4px",
                                             background: Object(nt.getTrackBackground)({
                                                 values: k,
                                                 colors: ["#ccc", d ? "rgba(0, 0, 0, 0.3)" : "#2684ff", "#ccc"],
                                                 min: j,
                                                 max: h
                                             }),
                                             alignSelf: "center"
                                         },
-                                        children: [a, Object(_.jsxs)("div", {
+                                        children: [a, Object(E.jsxs)("div", {
                                             style: {
                                                 display: "inline-block",
                                                 width: "100%",
                                                 fontSize: "12px",
                                                 paddingTop: "13px"
                                             },
-                                            children: [Object(_.jsx)("div", {
+                                            children: [Object(E.jsx)("div", {
                                                 style: {
                                                     float: "left"
                                                 },
                                                 children: j
-                                            }), Object(_.jsx)("div", {
+                                            }), Object(E.jsx)("div", {
                                                 style: {
                                                     float: "right"
                                                 },
                                                 children: h
                                             })]
                                         })]
                                     })
                                 })
                             },
                             renderThumb: function(e) {
                                 var t = e.index,
                                     a = e.props,
                                     n = e.isDragged;
-                                return Object(_.jsxs)("div", Object(D.a)(Object(D.a)({}, a), {}, {
+                                return Object(E.jsxs)("div", Object(D.a)(Object(D.a)({}, a), {}, {
                                     style: Object(D.a)(Object(D.a)({}, a.style), {}, {
                                         height: "18px",
                                         width: "18px",
                                         border: "None !important",
                                         borderRadius: "4px",
                                         backgroundColor: "#FFF",
                                         display: "flex",
                                         justifyContent: "center",
                                         alignItems: "center",
                                         boxShadow: "0px 2px 6px #AAA",
                                         outline: "none"
                                     }),
-                                    children: [Object(_.jsx)("div", {
+                                    children: [Object(E.jsx)("div", {
                                         style: {
                                             position: "absolute",
                                             top: "-24px",
                                             color: "#fff",
                                             fontWeight: "bold",
                                             fontSize: "12px",
                                             fontFamily: "Arial,Helvetica Neue,Helvetica,sans-serif",
                                             padding: "2px",
                                             borderRadius: "3px",
                                             backgroundColor: d ? "rgba(0, 0, 0, 0.3)" : "#2684ff"
                                         },
                                         children: k[t]
-                                    }), Object(_.jsx)("div", {
+                                    }), Object(E.jsx)("div", {
                                         style: {
                                             height: "12px",
                                             width: "3px",
                                             backgroundColor: n ? "#2684ff" : "#CCC"
                                         }
                                     })]
                                 }))
                             }
                         })
                     })]
                 })
             }
             var st = a(172);
 
-            function rt(e) {
+            function it(e) {
                 var t = e.widgetKey,
                     a = e.label,
                     o = e.value,
                     s = e.choices,
-                    i = e.multi,
+                    r = e.multi,
                     l = e.disabled,
                     d = e.hidden,
                     u = e.runNb,
                     b = e.url_key,
-                    p = Object(r.b)(),
+                    p = Object(i.b)(),
                     j = Object(n.useState)(!1),
                     h = Object(R.a)(j, 2),
                     v = h[0],
                     f = h[1],
                     m = {
                         menu: function(e) {
                             return Object(D.a)(Object(D.a)({}, e), {}, {
@@ -908,74 +908,74 @@
                     },
                     x = Object(c.c)(),
                     O = Object(R.a)(x, 1)[0];
                 Object(n.useEffect)((function() {
                     if (void 0 !== b && "" !== b) {
                         var e = O.get(b);
                         if (!v && void 0 !== e && null !== e)
-                            if (i) {
+                            if (r) {
                                 var a = e.split(",");
                                 a && (p(ge({
                                     key: t,
                                     value: a.filter((function(e) {
                                         return s.includes(e)
                                     }))
                                 })), p(Pe(!0)))
                             } else s.includes(e) && (p(ge({
                                 key: t,
                                 value: e
                             })), p(Pe(!0)))
                     }
-                }), [s, p, i, O, v, b, t]);
+                }), [s, p, r, O, v, b, t]);
                 var g = {
                         value: "",
                         label: ""
                     },
                     y = [{
                         value: "",
                         label: ""
                     }],
                     w = s.map((function(e) {
-                        return o && e === o && !i && (g = {
+                        return o && e === o && !r && (g = {
                             value: e,
                             label: e
                         }), {
                             value: e,
                             label: e
                         }
                     }));
-                return i && (y = [], s.map((function(e) {
-                    return o && o.includes(e) && i && y.push({
+                return r && (y = [], s.map((function(e) {
+                    return o && o.includes(e) && r && y.push({
                         value: e,
                         label: e
                     }), {
                         value: e,
                         label: e
                     }
                 }))), Object(n.useEffect)((function() {
                     v && u()
-                }), [o]), Object(_.jsxs)("div", {
+                }), [o]), Object(E.jsxs)("div", {
                     className: "form-group mb-3",
                     style: {
                         display: d ? "none" : ""
                     },
-                    children: [Object(_.jsx)("label", {
+                    children: [Object(E.jsx)("label", {
                         htmlFor: "select-".concat(a),
                         style: {
                             color: l ? "#555" : "#212529"
                         },
                         children: a
-                    }), Object(_.jsx)(st.a, {
+                    }), Object(E.jsx)(st.a, {
                         id: "select-".concat(a),
                         isDisabled: l,
                         name: a || "Select",
                         styles: m,
-                        value: i ? y : g,
+                        value: r ? y : g,
                         options: w,
-                        isMulti: i,
+                        isMulti: r,
                         onChange: function(e) {
                             if (e)
                                 if (f(!0), function(e) {
                                         return void 0 !== e.value
                                     }(e)) p(Oe({
                                     key: t,
                                     value: e.value
@@ -992,65 +992,65 @@
                                     }))
                                 }
                         }
                     })]
                 })
             }
 
-            function it(e) {
+            function rt(e) {
                 var t = e.widgetKey,
                     a = e.label,
                     o = e.value,
                     s = e.min,
-                    i = e.max,
+                    r = e.max,
                     l = e.step,
                     d = (e.vertical, e.disabled),
                     u = e.hidden,
                     b = e.runNb,
                     p = e.url_key,
-                    j = Object(r.b)(),
+                    j = Object(i.b)(),
                     h = Object(n.useState)(!1),
                     v = Object(R.a)(h, 2),
                     f = v[0],
                     m = v[1],
                     x = 0,
                     O = 100,
                     g = 1;
-                s && (x = s), i && (O = i), l && (g = l);
+                s && (x = s), r && (O = r), l && (g = l);
                 var y = Object(c.c)(),
                     w = Object(R.a)(y, 1)[0];
                 Object(n.useEffect)((function() {
                     if (void 0 !== p && "" !== p) {
                         var e = w.get(p);
                         !f && void 0 !== e && null !== e && !isNaN(parseFloat(e)) && parseFloat(e) >= x && parseFloat(e) <= O && (j(ge({
                             key: t,
                             value: parseFloat(e)
                         })), j(Pe(!0)))
                     }
                 }), [j, O, x, w, f, p, t]);
                 var k = [null !== o ? o : O];
-                return Object(_.jsxs)("div", {
+                return Object(E.jsxs)("div", {
                     className: "form-group mb-3",
                     style: {
                         display: u ? "none" : ""
                     },
-                    children: [Object(_.jsx)("label", {
+                    children: [Object(E.jsx)("label", {
                         htmlFor: "slider-".concat(a),
                         style: {
                             color: d ? "#555" : "#212529"
                         },
                         children: a
-                    }), Object(_.jsx)("div", {
+                    }), Object(E.jsx)("div", {
                         style: {
                             paddingTop: "12px",
                             display: "flex",
                             justifyContent: "center",
                             flexWrap: "wrap"
                         },
-                        children: Object(_.jsx)(nt.Range, {
+                        children: Object(E.jsx)(nt.Range, {
                             disabled: d,
                             values: k,
                             step: g,
                             min: x,
                             max: O,
                             onChange: function(e) {
                                 m(!0), j(Oe({
@@ -1060,88 +1060,88 @@
                             },
                             onFinalChange: function(e) {
                                 b()
                             },
                             renderTrack: function(e) {
                                 var t = e.props,
                                     a = e.children;
-                                return Object(_.jsx)("div", {
+                                return Object(E.jsx)("div", {
                                     onMouseDown: t.onMouseDown,
                                     onTouchStart: t.onTouchStart,
                                     style: Object(D.a)(Object(D.a)({}, t.style), {}, {
                                         height: "36px",
                                         display: "flex",
                                         width: "100%"
                                     }),
-                                    children: Object(_.jsxs)("div", {
+                                    children: Object(E.jsxs)("div", {
                                         ref: t.ref,
                                         style: {
                                             height: "5px",
                                             width: "100%",
                                             borderRadius: "4px",
                                             background: Object(nt.getTrackBackground)({
                                                 values: k,
                                                 colors: [d ? "rgba(0, 0, 0, 0.3)" : "#2684ff", "#ccc"],
                                                 min: x,
                                                 max: O
                                             }),
                                             alignSelf: "center"
                                         },
-                                        children: [a, Object(_.jsxs)("div", {
+                                        children: [a, Object(E.jsxs)("div", {
                                             style: {
                                                 display: "inline-block",
                                                 width: "100%",
                                                 fontSize: "12px",
                                                 paddingTop: "13px"
                                             },
-                                            children: [Object(_.jsx)("div", {
+                                            children: [Object(E.jsx)("div", {
                                                 style: {
                                                     float: "left"
                                                 },
                                                 children: x
-                                            }), Object(_.jsx)("div", {
+                                            }), Object(E.jsx)("div", {
                                                 style: {
                                                     float: "right"
                                                 },
                                                 children: O
                                             })]
                                         })]
                                     })
                                 })
                             },
                             renderThumb: function(e) {
                                 var t = e.props,
                                     a = e.isDragged;
-                                return Object(_.jsxs)("div", Object(D.a)(Object(D.a)({}, t), {}, {
+                                return Object(E.jsxs)("div", Object(D.a)(Object(D.a)({}, t), {}, {
                                     style: Object(D.a)(Object(D.a)({}, t.style), {}, {
                                         height: "18px",
                                         width: "18px",
                                         border: "None",
                                         borderRadius: "4px",
                                         backgroundColor: "#FFF",
                                         display: "flex",
                                         justifyContent: "center",
                                         alignItems: "center",
                                         boxShadow: "0px 2px 6px #AAA",
                                         outline: "none"
                                     }),
-                                    children: [Object(_.jsx)("div", {
+                                    children: [Object(E.jsx)("div", {
                                         style: {
                                             position: "absolute",
                                             top: "-24px",
                                             color: "#fff",
                                             fontWeight: "bold",
                                             fontSize: "12px",
                                             fontFamily: "Arial,Helvetica Neue,Helvetica,sans-serif",
                                             padding: "2px",
                                             borderRadius: "3px",
                                             backgroundColor: d ? "rgba(0, 0, 0, 0.3)" : "#2684ff"
                                         },
                                         children: k[0]
-                                    }), Object(_.jsx)("div", {
+                                    }), Object(E.jsx)("div", {
                                         style: {
                                             height: "12px",
                                             width: "3px",
                                             backgroundColor: a ? "#2684ff" : "#CCC"
                                         }
                                     })]
                                 }))
@@ -1191,24 +1191,24 @@
                 },
                 Nt = function(e) {
                     return "PUBLIC" === e.sites.site.share
                 },
                 St = function() {
                     return function() {
                         var e = Object(u.a)(d.a.mark((function e(t) {
-                            var a, n, o, r, i;
+                            var a, n, o, i, r;
                             return d.a.wrap((function(e) {
                                 for (;;) switch (e.prev = e.next) {
                                     case 0:
                                         return e.prev = 0, t(Ot({})), t(gt(ct.Unknown)), a = "single-site", a = window.location.host.split(":")[0], n = "/api/v1/get-site/".concat(a, "/"), e.next = 8, s.a.get(n);
                                     case 8:
-                                        o = e.sent, r = o.data, t(Ot(r)), "Ready" !== (null === r || void 0 === r ? void 0 : r.status) ? t(gt(ct.NotReady)) : t(gt(ct.Loaded)), e.next = 19;
+                                        o = e.sent, i = o.data, t(Ot(i)), "Ready" !== (null === i || void 0 === i ? void 0 : i.status) ? t(gt(ct.NotReady)) : t(gt(ct.Loaded)), e.next = 19;
                                         break;
                                     case 14:
-                                        e.prev = 14, e.t0 = e.catch(0), i = e.t0, console.log(i.message), "Network Error" === (null === i || void 0 === i ? void 0 : i.message) ? t(gt(ct.NetworkError)) : 403 === i.response.status ? t(gt(ct.AccessForbidden)) : 404 === i.response.status ? t(gt(ct.NotFound)) : 401 === i.response.status ? (t(N("")), t(S("")), t(gt(ct.PleaseRefresh))) : console.error("Problem during loading site information. ".concat(e.t0));
+                                        e.prev = 14, e.t0 = e.catch(0), r = e.t0, console.log(r.message), "Network Error" === (null === r || void 0 === r ? void 0 : r.message) ? t(gt(ct.NetworkError)) : 403 === r.response.status ? t(gt(ct.AccessForbidden)) : 404 === r.response.status ? t(gt(ct.NotFound)) : 401 === r.response.status ? (t(N("")), t(S("")), t(gt(ct.PleaseRefresh))) : console.error("Problem during loading site information. ".concat(e.t0));
                                     case 19:
                                     case "end":
                                         return e.stop()
                                 }
                             }), e, null, [
                                 [0, 14]
                             ])
@@ -1219,26 +1219,26 @@
                     }()
                 };
 
             function Pt(e) {
                 var t = e.widgetKey,
                     a = e.label,
                     o = e.maxFileSize,
-                    i = e.disabled,
+                    r = e.disabled,
                     c = e.hidden,
                     l = e.value,
                     b = e.runNb,
-                    j = Object(r.b)(),
+                    j = Object(i.b)(),
                     h = Object(n.useState)(!1),
                     v = Object(R.a)(h, 2),
                     m = v[0],
                     x = v[1],
-                    O = Object(r.c)(Q),
-                    g = Object(r.c)(wt),
-                    y = Object(r.c)(f),
+                    O = Object(i.c)(Q),
+                    g = Object(i.c)(wt),
+                    y = Object(i.c)(f),
                     w = "100MB";
                 o && (w = o), Object(n.useEffect)((function() {
                     m && void 0 !== l && 2 === l.length && b()
                 }), [l]), Object(n.useEffect)((function() {
                     j(function() {
                         var e = Object(u.a)(d.a.mark((function e(t) {
                             var a, n;
@@ -1293,44 +1293,44 @@
                             })));
                             return function(t, a, n) {
                                 return e.apply(this, arguments)
                             }
                         }()
                     },
                     N = {
-                        process: function(e, t, a, n, o, r, i) {
+                        process: function(e, t, a, n, o, i, r) {
                             var c = new AbortController;
                             return s.a.get("/api/v1/nb-file-put/".concat(g, "/").concat(y, "/").concat(t.name, "/").concat(t.size)).then((function(e) {
                                 var a = e.data.url,
                                     o = s.a.defaults.headers.common.Authorization;
                                 delete s.a.defaults.headers.common.Authorization;
-                                var i = {
+                                var r = {
                                     onUploadProgress: function(e) {
-                                        r(void 0 !== e.total, e.loaded, e.total)
+                                        i(void 0 !== e.total, e.loaded, e.total)
                                     }
                                 };
                                 s.a.put(a, t, {
                                     headers: {
                                         "Content-Type": ""
                                     },
-                                    onUploadProgress: i.onUploadProgress,
+                                    onUploadProgress: r.onUploadProgress,
                                     signal: c.signal
                                 }).then((function(e) {
                                     n(t.name), void 0 !== g && j(function(e, t, a) {
                                         return function() {
                                             var n = Object(u.a)(d.a.mark((function n(o) {
-                                                var r;
+                                                var i;
                                                 return d.a.wrap((function(n) {
                                                     for (;;) switch (n.prev = n.next) {
                                                         case 0:
-                                                            return n.prev = 0, r = {
+                                                            return n.prev = 0, i = {
                                                                 site_id: e,
                                                                 session_id: t,
                                                                 filename: a
-                                                            }, n.next = 5, s.a.post("/api/v1/nb-file-uploaded", r);
+                                                            }, n.next = 5, s.a.post("/api/v1/nb-file-uploaded", i);
                                                         case 5:
                                                             n.next = 10;
                                                             break;
                                                         case 7:
                                                             n.prev = 7, n.t0 = n.catch(0), console.error("Problem with file upload. ".concat(n.t0));
                                                         case 10:
                                                         case "end":
@@ -1348,15 +1348,15 @@
                                 })).catch((function(e) {
                                     p.b.error("Error when uploading new files")
                                 })), s.a.defaults.headers.common.Authorization = o
                             })).catch((function(e) {
                                 p.b.error("Cant upload new files")
                             })), {
                                 abort: function() {
-                                    c.abort(), i()
+                                    c.abort(), r()
                                 }
                             }
                         },
                         revert: function() {
                             var e = Object(u.a)(d.a.mark((function e(t, a, n) {
                                 return d.a.wrap((function(e) {
                                     for (;;) switch (e.prev = e.next) {
@@ -1373,28 +1373,28 @@
                                 }), e)
                             })));
                             return function(t, a, n) {
                                 return e.apply(this, arguments)
                             }
                         }()
                     };
-                return Object(_.jsxs)("div", {
+                return Object(E.jsxs)("div", {
                     className: "form-group mb-3",
                     style: {
                         display: c ? "none" : ""
                     },
-                    children: [Object(_.jsx)("label", {
+                    children: [Object(E.jsx)("label", {
                         htmlFor: "file-".concat(a),
                         style: {
-                            color: i ? "#555" : "#212529"
+                            color: r ? "#555" : "#212529"
                         },
                         children: a
-                    }), Object(_.jsx)("div", {
-                        children: Object(_.jsx)(lt.FilePond, {
-                            disabled: i,
+                    }), Object(E.jsx)("div", {
+                        children: Object(E.jsx)(lt.FilePond, {
+                            disabled: r,
                             maxFileSize: w,
                             onprocessfile: function(e, a) {
                                 x(!0), j(Oe({
                                     key: t,
                                     value: [a.filename, a.serverId]
                                 }))
                             },
@@ -1406,20 +1406,20 @@
             }
 
             function Ct(e) {
                 var t = e.widgetKey,
                     a = e.label,
                     o = e.value,
                     s = e.rows,
-                    i = e.disabled,
+                    r = e.disabled,
                     l = e.hidden,
                     d = e.runNb,
                     u = e.continuousUpdate,
                     b = e.url_key,
-                    p = Object(r.b)(),
+                    p = Object(i.b)(),
                     j = Object(n.useState)(!1),
                     h = Object(R.a)(j, 2),
                     v = h[0],
                     f = h[1],
                     m = Object(n.useState)(!1),
                     x = Object(R.a)(m, 2),
                     O = x[0],
@@ -1434,127 +1434,127 @@
                     if (void 0 !== b && "" !== b) {
                         var e = N.get(b);
                         O || void 0 === e || null === e || (p(ge({
                             key: t,
                             value: e
                         })), p(Pe(!0)))
                     }
-                }), [p, N, O, b, t]), Object(_.jsxs)("div", {
+                }), [p, N, O, b, t]), Object(E.jsxs)("div", {
                     className: "form-group mb-3",
                     style: {
                         display: l ? "none" : ""
                     },
-                    children: [Object(_.jsx)("label", {
+                    children: [Object(E.jsx)("label", {
                         htmlFor: "textarea-".concat(a),
                         style: {
-                            color: i ? "#555" : "#212529"
+                            color: r ? "#555" : "#212529"
                         },
                         children: a
-                    }), 1 === y && Object(_.jsx)("input", {
+                    }), 1 === y && Object(E.jsx)("input", {
                         className: "form-control",
                         type: "text",
                         id: "text-".concat(a),
                         value: o || "",
                         onChange: function(e) {
                             g(!0), f(!0), p(Oe({
                                 key: t,
                                 value: w(e.target.value)
                             }))
                         },
                         onKeyPress: function(e) {
                             "Enter" === e.key && (d(), f(!1), e.preventDefault())
                         },
-                        disabled: i
-                    }), y > 1 && Object(_.jsx)("textarea", {
+                        disabled: r
+                    }), y > 1 && Object(E.jsx)("textarea", {
                         className: "form-control",
                         id: "text-area-".concat(a),
                         rows: y,
                         value: o || "",
                         onChange: function(e) {
                             g(!0), f(!0), p(Oe({
                                 key: t,
                                 value: w(e.target.value)
                             }))
                         },
-                        disabled: i
-                    }), v && u && 1 === y && Object(_.jsx)("div", {
+                        disabled: r
+                    }), v && u && 1 === y && Object(E.jsx)("div", {
                         style: {
                             float: "right",
                             position: "relative",
                             top: "2px",
                             left: "0px"
                         },
-                        children: Object(_.jsx)("button", {
+                        children: Object(E.jsx)("button", {
                             className: "btn btn-sm btn-outline-primary",
                             onClick: function(e) {
                                 d(), f(!1), e.preventDefault()
                             },
                             style: {
                                 fontSize: "0.7em",
                                 border: "none"
                             },
                             children: "Press enter or click to apply"
                         })
-                    }), v && u && y > 1 && Object(_.jsx)("div", {
+                    }), v && u && y > 1 && Object(E.jsx)("div", {
                         style: {
                             float: "right",
                             position: "relative",
                             top: "2px",
                             left: "0px"
                         },
-                        children: Object(_.jsx)("button", {
+                        children: Object(E.jsx)("button", {
                             className: "btn btn-sm btn-outline-primary",
                             onClick: function(e) {
                                 d(), f(!1), e.preventDefault()
                             },
                             style: {
                                 fontSize: "0.7em",
                                 border: "none"
                             },
                             children: "Apply"
                         })
                     })]
                 })
             }
             Object(lt.registerPlugin)(ut.a, pt.a, ht.a);
-            var Tt, Et, Rt = a(312),
-                _t = a(314),
+            var Tt, _t, Rt = a(312),
+                Et = a(314),
                 Ft = a(87),
                 At = a(90),
-                It = a(88);
+                Mt = a(88);
 
             function Dt(e) {
                 var t = e.value,
                     a = e.disabled;
-                return Object(_.jsx)("div", {
+                return Object(E.jsx)("div", {
                     className: "form-group mb-3",
                     style: {
                         color: a ? "#555" : "#212529"
                     },
-                    children: Object(_.jsx)(Rt.a, {
-                        rehypePlugins: [Ft.a, _t.a, At.a, It.a],
+                    children: Object(E.jsx)(Rt.a, {
+                        rehypePlugins: [Ft.a, Et.a, At.a, Mt.a],
                         children: t
                     })
                 })
             }! function(e) {
                 e.Connecting = "Connecting", e.Connected = "Connected", e.Unknown = "Unknown", e.Disconnected = "Disconnected"
             }(Tt || (Tt = {})),
             function(e) {
-                e.Unknown = "Unknown", e.Starting = "Starting", e.Running = "Running", e.Missing = "Missing", e.Busy = "Busy", e.Queued = "Queued", e.MaxRunTimeReached = "MaxRunTimeReached", e.MaxIdleTimeReached = "MaxIdleTimeReached"
-            }(Et || (Et = {}));
-            var Wt = {
+                e.Unknown = "Unknown", e.Starting = "Starting", e.Running = "Running", e.Missing = "Missing", e.Busy = "Busy", e.Queued = "Queued", e.MaxRunTimeReached = "MaxRunTimeReached", e.MaxIdleTimeReached = "MaxIdleTimeReached", e.UsageLimitReached = "UsageLimitReached"
+            }(_t || (_t = {}));
+            var It = {
                     webSocketState: Tt.Unknown,
-                    workerState: Et.Unknown,
+                    workerState: _t.Unknown,
                     workerId: void 0,
                     notebookSrc: "",
                     tryConnectCount: 0
                 },
-                Mt = Object(b.b)({
+                Lt = Object(b.b)({
                     name: "ws",
-                    initialState: Wt,
+                    initialState: It,
                     reducers: {
                         setWebSocketState: function(e, t) {
                             e.webSocketState = t.payload
                         },
                         setWorkerState: function(e, t) {
                             e.workerState = t.payload
                         },
@@ -1568,22 +1568,22 @@
                             e.tryConnectCount += 1
                         },
                         resetTryConnectCount: function(e) {
                             e.tryConnectCount = 0
                         }
                     }
                 }),
-                Ut = Mt.reducer,
-                Lt = Mt.actions,
-                Ht = Lt.setWebSocketState,
-                zt = Lt.setWorkerState,
-                Bt = Lt.setWorkerId,
-                Vt = Lt.setNotebookSrc,
-                Jt = Lt.increaseTryConnectCount,
-                Kt = Lt.resetTryConnectCount,
+                Ut = Lt.reducer,
+                Wt = Lt.actions,
+                Ht = Wt.setWebSocketState,
+                zt = Wt.setWorkerState,
+                Bt = Wt.setWorkerId,
+                Vt = Wt.setNotebookSrc,
+                Jt = Wt.increaseTryConnectCount,
+                Kt = Wt.resetTryConnectCount,
                 qt = function(e) {
                     return e.ws.webSocketState
                 },
                 Yt = function(e) {
                     return e.ws.workerState
                 },
                 Gt = function(e) {
@@ -1607,19 +1607,19 @@
             ea = "ws://localhost:8000", ta = !1;
             var aa = 0,
                 na = void 0;
 
             function oa(e) {
                 var t = e.children;
                 console.log("WebSocketProvider");
-                var a = Object(r.b)(),
-                    o = Object(r.c)(wt),
-                    i = Object(r.c)(Re),
-                    c = Object(r.c)(C),
-                    l = Object(r.c)(_e),
+                var a = Object(i.b)(),
+                    o = Object(i.c)(wt),
+                    r = Object(i.c)(Re),
+                    c = Object(i.c)(C),
+                    l = Object(i.c)(Ee),
                     b = void 0,
                     p = "Unknown";
                 Object(n.useEffect)((function() {
                     return aa = 0,
                         function() {
                             var e;
                             aa = 6, null === (e = na) || void 0 === e || e.close()
@@ -1634,23 +1634,23 @@
                         purpose: "server-address",
                         address: ea
                     })), a(Ht(Tt.Connected)), g()
                 }
 
                 function v(e) {
                     var t, n = JSON.parse(e.data);
-                    "purpose" in n && ("worker-state" === n.purpose ? (console.log("worker-state", n.state), p = n.state, a(zt(n.state)), a(Bt(n.workerId)), (p === Et.MaxIdleTimeReached || p === Et.MaxRunTimeReached) && (null === (t = b) || void 0 === t || t.close())) : "executed-notebook" === n.purpose ? ((null === n || void 0 === n ? void 0 : n.reloadNotebook) && void 0 !== i && a(function(e, t) {
+                    "purpose" in n && ("worker-state" === n.purpose ? (console.log("worker-state", n.state), p = n.state, a(zt(n.state)), a(Bt(n.workerId)), (p === _t.MaxIdleTimeReached || p === _t.MaxRunTimeReached) && (null === (t = b) || void 0 === t || t.close())) : "executed-notebook" === n.purpose ? ((null === n || void 0 === n ? void 0 : n.reloadNotebook) && void 0 !== r && a(function(e, t) {
                         var a = arguments.length > 2 && void 0 !== arguments[2] && arguments[2];
                         return function() {
                             var n = Object(u.a)(d.a.mark((function n(o) {
-                                var r, i, c, l, u, b;
+                                var i, r, c, l, u, b;
                                 return d.a.wrap((function(n) {
                                     for (;;) switch (n.prev = n.next) {
                                         case 0:
-                                            return n.prev = 0, a || (o(fe("")), o(qe())), r = ce(), i = r.width, o(V(i > 992)), a || o(ve("loading")), c = "/api/v1/".concat(e, "/notebooks/").concat(t, "/"), n.next = 8, s.a.get(c);
+                                            return n.prev = 0, a || (o(fe("")), o(qe())), i = ce(), r = i.width, o(V(r > 992)), a || o(ve("loading")), c = "/api/v1/".concat(e, "/notebooks/").concat(t, "/"), n.next = 8, s.a.get(c);
                                         case 8:
                                             l = n.sent, u = l.data, b = JSON.parse(u.params), o(he(Object(D.a)(Object(D.a)({}, u), {}, {
                                                 params: b
                                             }))), a || o(ve("loaded")), null !== (null === b || void 0 === b ? void 0 : b.show_sidebar) && void 0 !== (null === b || void 0 === b ? void 0 : b.show_sidebar) && o(V(null === b || void 0 === b ? void 0 : b.show_sidebar)), n.next = 20;
                                             break;
                                         case 16:
                                             n.prev = 16, n.t0 = n.catch(0), a || o(ve("error")), console.error("Problem during loading selected notebook (".concat(t, "). ").concat(n.t0));
@@ -1662,594 +1662,830 @@
                                     [0, 16]
                                 ])
                             })));
                             return function(e) {
                                 return n.apply(this, arguments)
                             }
                         }()
-                    }(o, i)), a(Vt(n.body))) : "update-widgets" === n.purpose ? a(me(n)) : "hide-widgets" === n.purpose ? a(xe(n)) : "init-widgets" === n.purpose ? (a(we(n)), a(Se(!0))) : "update-title" === n.purpose ? a(ke(n.title)) : "update-show-code" === n.purpose ? a(Ne(n.showCode)) : "download-html" !== n.purpose && "download-pdf" !== n.purpose || n.url && n.filename && (a(ze(!1)), x(n.url, n.filename)))
+                    }(o, r)), a(Vt(n.body))) : "update-widgets" === n.purpose ? a(me(n)) : "hide-widgets" === n.purpose ? a(xe(n)) : "init-widgets" === n.purpose ? (a(we(n)), a(Se(!0))) : "update-title" === n.purpose ? a(ke(n.title)) : "update-show-code" === n.purpose ? a(Ne(n.showCode)) : "download-html" !== n.purpose && "download-pdf" !== n.purpose || n.url && n.filename && (a(ze(!1)), x(n.url, n.filename)))
                 }
 
                 function m(e) {
-                    a(Ht(Tt.Disconnected)), a(zt(Et.Unknown))
+                    a(Ht(Tt.Disconnected)), a(zt(_t.Unknown))
                 }
 
                 function O(e) {
-                    a(Ht(Tt.Disconnected)), b = void 0, p !== Et.MaxIdleTimeReached && p !== Et.MaxRunTimeReached && (a(zt(Et.Unknown)), a(Bt(void 0)), aa < 5 && setTimeout((function() {
+                    a(Ht(Tt.Disconnected)), b = void 0, p !== _t.MaxIdleTimeReached && p !== _t.MaxRunTimeReached && (a(zt(_t.Unknown)), a(Bt(void 0)), aa < 5 && setTimeout((function() {
                         return y()
                     }), 5e3))
                 }
 
                 function g() {
                     j(JSON.stringify({
                         purpose: "worker-ping"
                     })), void 0 !== b && b.readyState === b.OPEN && setTimeout((function() {
                         return g()
                     }), 1e4)
                 }
 
                 function y() {
-                    if ((ta || !l) && void 0 !== i && void 0 === b && p !== Et.MaxIdleTimeReached && p !== Et.MaxRunTimeReached && aa < 5) {
+                    if ((ta || !l) && void 0 !== r && void 0 === b && p !== _t.MaxIdleTimeReached && p !== _t.MaxRunTimeReached && aa < 5) {
                         console.log("WS connect ..." + p + " " + aa), a(Jt());
-                        var e = "".concat(ea, "/ws/client/").concat(i, "/").concat(f(), "/");
+                        var e = "".concat(ea, "/ws/client/").concat(r, "/").concat(f(), "/");
                         void 0 !== c && null !== c && "" !== c && (e += "?token=".concat(c)), (b = new WebSocket(e)).onopen = h, b.onmessage = v, b.onerror = m, b.onclose = O, na = b, (aa += 1) >= 5 && a(gt(ct.NetworkError))
                     }
                 }
                 y();
                 var w = {
                     sendMessage: j
                 };
-                return Object(_.jsx)($t.Provider, {
+                return Object(E.jsx)($t.Provider, {
                     value: w,
                     children: t
                 })
             }
 
-            function sa() {
-                var e = Object(r.b)(),
-                    t = Object(r.c)(qt),
-                    a = Object(r.c)(Yt),
-                    o = Object(r.c)(Zt);
+            function sa(e) {
+                var t = e.allowDownload,
+                    a = e.waiting,
+                    o = (e.continuousUpdate, e.staticNotebook),
+                    r = e.notebookId,
+                    c = e.notebookPath,
+                    l = e.notebookTitle,
+                    b = e.runDownloadHTML,
+                    j = e.runDownloadPDF,
+                    h = e.widgetsValues,
+                    v = e.widgetsParams,
+                    m = Object(i.b)(),
+                    O = Object(n.useState)(!1),
+                    g = Object(R.a)(O, 2),
+                    y = g[0],
+                    w = g[1],
+                    k = Object(i.c)(qt),
+                    N = Object(i.c)(Yt),
+                    S = Object(i.c)(Zt);
                 Object(n.useEffect)((function() {
-                    o >= 5 && e(gt(ct.LostConnection))
-                }), [e, o]);
-                var s = "orange";
-                t === Tt.Connected ? s = "green" : t !== Tt.Disconnected && t !== Tt.Unknown || (s = "red");
-                var i = "orange";
-                return a === Et.Running || a === Et.Busy ? i = "green" : a !== Et.Missing && a !== Et.Unknown || (i = "red"), Object(_.jsxs)("div", {
-                    children: [Object(_.jsx)("span", {
-                        title: "WebSocket: ".concat(t),
-                        children: Object(_.jsxs)("svg", {
-                            xmlns: "http://www.w3.org/2000/svg",
-                            width: "16",
-                            height: "16",
-                            fill: s,
-                            className: "bi bi-wifi",
-                            viewBox: "0 0 16 16",
-                            children: [Object(_.jsx)("path", {
-                                d: "M15.384 6.115a.485.485 0 0 0-.047-.736A12.444 12.444 0 0 0 8 3C5.259 3 2.723 3.882.663 5.379a.485.485 0 0 0-.048.736.518.518 0 0 0 .668.05A11.448 11.448 0 0 1 8 4c2.507 0 4.827.802 6.716 2.164.205.148.49.13.668-.049z"
-                            }), Object(_.jsx)("path", {
-                                d: "M13.229 8.271a.482.482 0 0 0-.063-.745A9.455 9.455 0 0 0 8 6c-1.905 0-3.68.56-5.166 1.526a.48.48 0 0 0-.063.745.525.525 0 0 0 .652.065A8.46 8.46 0 0 1 8 7a8.46 8.46 0 0 1 4.576 1.336c.206.132.48.108.653-.065zm-2.183 2.183c.226-.226.185-.605-.1-.75A6.473 6.473 0 0 0 8 9c-1.06 0-2.062.254-2.946.704-.285.145-.326.524-.1.75l.015.015c.16.16.407.19.611.09A5.478 5.478 0 0 1 8 10c.868 0 1.69.201 2.42.56.203.1.45.07.61-.091l.016-.015zM9.06 12.44c.196-.196.198-.52-.04-.66A1.99 1.99 0 0 0 8 11.5a1.99 1.99 0 0 0-1.02.28c-.238.14-.236.464-.04.66l.706.706a.5.5 0 0 0 .707 0l.707-.707z"
-                            })]
-                        })
-                    }), " ", Object(_.jsx)("span", {
-                        title: "Worker: ".concat(a, "\nSession Id: ").concat(f()),
-                        children: Object(_.jsx)("svg", {
-                            xmlns: "http://www.w3.org/2000/svg",
-                            width: "16",
-                            height: "16",
-                            fill: i,
-                            className: "bi bi-cpu",
-                            viewBox: "0 0 16 16",
-                            children: Object(_.jsx)("path", {
-                                d: "M5 0a.5.5 0 0 1 .5.5V2h1V.5a.5.5 0 0 1 1 0V2h1V.5a.5.5 0 0 1 1 0V2h1V.5a.5.5 0 0 1 1 0V2A2.5 2.5 0 0 1 14 4.5h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14a2.5 2.5 0 0 1-2.5 2.5v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14A2.5 2.5 0 0 1 2 11.5H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2A2.5 2.5 0 0 1 4.5 2V.5A.5.5 0 0 1 5 0zm-.5 3A1.5 1.5 0 0 0 3 4.5v7A1.5 1.5 0 0 0 4.5 13h7a1.5 1.5 0 0 0 1.5-1.5v-7A1.5 1.5 0 0 0 11.5 3h-7zM5 6.5A1.5 1.5 0 0 1 6.5 5h3A1.5 1.5 0 0 1 11 6.5v3A1.5 1.5 0 0 1 9.5 11h-3A1.5 1.5 0 0 1 5 9.5v-3zM6.5 6a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5h-3z"
+                    S >= 5 && m(gt(ct.LostConnection))
+                }), [m, S]);
+                var P = "orange";
+                k === Tt.Connected ? P = "green" : k !== Tt.Disconnected && k !== Tt.Unknown || (P = "red");
+                var C = "orange";
+                N === _t.Running || N === _t.Busy ? C = "green" : N !== _t.Missing && N !== _t.Unknown || (C = "red");
+                var T = !0,
+                    _ = "?";
+                if (void 0 !== v && null !== v && void 0 !== h && null !== h) {
+                    for (var F = 0, A = Object.entries(v); F < A.length; F++) {
+                        var M = Object(R.a)(A[F], 2),
+                            D = M[0],
+                            I = M[1];
+                        if (void 0 !== h[D]) {
+                            if (($(I) || ee(I) || ae(I) || X(I) || te(I) || oe(I)) && null !== (null === I || void 0 === I ? void 0 : I.url_key) && "" !== (null === I || void 0 === I ? void 0 : I.url_key) && (T = !1), ($(I) || ee(I) || te(I) || oe(I)) && null !== (null === I || void 0 === I ? void 0 : I.url_key) && "" !== (null === I || void 0 === I ? void 0 : I.url_key) && (_ += "".concat(null === I || void 0 === I ? void 0 : I.url_key, "=").concat(h[D], "&")), ae(I) && null !== (null === I || void 0 === I ? void 0 : I.url_key) && "" !== (null === I || void 0 === I ? void 0 : I.url_key)) {
+                                var L = h[D];
+                                _ += "".concat(null === I || void 0 === I ? void 0 : I.url_key, "=").concat(L[0], ",").concat(L[1], "&")
+                            }
+                            if (X(I) && null !== (null === I || void 0 === I ? void 0 : I.url_key) && "" !== (null === I || void 0 === I ? void 0 : I.url_key))
+                                if (null === I || void 0 === I ? void 0 : I.multi) {
+                                    var U = h[D];
+                                    _ += "".concat(null === I || void 0 === I ? void 0 : I.url_key, "=").concat(U.join(","), "&")
+                                } else {
+                                    var W = h[D];
+                                    _ += "".concat(null === I || void 0 === I ? void 0 : I.url_key, "=").concat(W, "&")
+                                }
+                        }
+                    }
+                    "?" !== _ && (_ = _.slice(0, _.length - 1))
+                }
+                return Object(E.jsxs)("div", {
+                    style: {
+                        paddingBottom: "25px"
+                    },
+                    children: [void 0 !== r && !o && Object(E.jsxs)(E.Fragment, {
+                        children: [Object(E.jsx)("span", {
+                            title: "WebSocket: ".concat(k),
+                            children: Object(E.jsxs)("svg", {
+                                xmlns: "http://www.w3.org/2000/svg",
+                                width: "16",
+                                height: "16",
+                                fill: P,
+                                className: "bi bi-wifi",
+                                viewBox: "0 0 16 16",
+                                children: [Object(E.jsx)("path", {
+                                    d: "M15.384 6.115a.485.485 0 0 0-.047-.736A12.444 12.444 0 0 0 8 3C5.259 3 2.723 3.882.663 5.379a.485.485 0 0 0-.048.736.518.518 0 0 0 .668.05A11.448 11.448 0 0 1 8 4c2.507 0 4.827.802 6.716 2.164.205.148.49.13.668-.049z"
+                                }), Object(E.jsx)("path", {
+                                    d: "M13.229 8.271a.482.482 0 0 0-.063-.745A9.455 9.455 0 0 0 8 6c-1.905 0-3.68.56-5.166 1.526a.48.48 0 0 0-.063.745.525.525 0 0 0 .652.065A8.46 8.46 0 0 1 8 7a8.46 8.46 0 0 1 4.576 1.336c.206.132.48.108.653-.065zm-2.183 2.183c.226-.226.185-.605-.1-.75A6.473 6.473 0 0 0 8 9c-1.06 0-2.062.254-2.946.704-.285.145-.326.524-.1.75l.015.015c.16.16.407.19.611.09A5.478 5.478 0 0 1 8 10c.868 0 1.69.201 2.42.56.203.1.45.07.61-.091l.016-.015zM9.06 12.44c.196-.196.198-.52-.04-.66A1.99 1.99 0 0 0 8 11.5a1.99 1.99 0 0 0-1.02.28c-.238.14-.236.464-.04.66l.706.706a.5.5 0 0 0 .707 0l.707-.707z"
+                                })]
                             })
-                        })
-                    }), a === Et.Busy && Object(_.jsxs)("span", {
+                        }), " ", Object(E.jsx)("span", {
+                            title: "Worker: ".concat(N, "\nSession Id: ").concat(f()),
+                            children: Object(E.jsx)("svg", {
+                                xmlns: "http://www.w3.org/2000/svg",
+                                width: "16",
+                                height: "16",
+                                fill: C,
+                                className: "bi bi-cpu",
+                                viewBox: "0 0 16 16",
+                                children: Object(E.jsx)("path", {
+                                    d: "M5 0a.5.5 0 0 1 .5.5V2h1V.5a.5.5 0 0 1 1 0V2h1V.5a.5.5 0 0 1 1 0V2h1V.5a.5.5 0 0 1 1 0V2A2.5 2.5 0 0 1 14 4.5h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14a2.5 2.5 0 0 1-2.5 2.5v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14A2.5 2.5 0 0 1 2 11.5H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2A2.5 2.5 0 0 1 4.5 2V.5A.5.5 0 0 1 5 0zm-.5 3A1.5 1.5 0 0 0 3 4.5v7A1.5 1.5 0 0 0 4.5 13h7a1.5 1.5 0 0 0 1.5-1.5v-7A1.5 1.5 0 0 0 11.5 3h-7zM5 6.5A1.5 1.5 0 0 1 6.5 5h3A1.5 1.5 0 0 1 11 6.5v3A1.5 1.5 0 0 1 9.5 11h-3A1.5 1.5 0 0 1 5 9.5v-3zM6.5 6a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5h-3z"
+                                })
+                            })
+                        })]
+                    }), N === _t.Busy && Object(E.jsxs)("span", {
                         title: "Worker is busy",
-                        children: [" ", Object(_.jsx)("svg", {
+                        children: [" ", Object(E.jsx)("svg", {
                             xmlns: "http://www.w3.org/2000/svg",
                             width: "16",
                             height: "16",
                             fill: "green",
                             className: "bi bi-activity",
                             viewBox: "0 0 16 16",
-                            children: Object(_.jsx)("path", {
+                            children: Object(E.jsx)("path", {
                                 fillRule: "evenodd",
                                 d: "M6 2a.5.5 0 0 1 .47.33L10 12.036l1.53-4.208A.5.5 0 0 1 12 7.5h3.5a.5.5 0 0 1 0 1h-3.15l-1.88 5.17a.5.5 0 0 1-.94 0L6 3.964 4.47 8.171A.5.5 0 0 1 4 8.5H.5a.5.5 0 0 1 0-1h3.15l1.88-5.17A.5.5 0 0 1 6 2Z"
                             })
-                        }), " ", "Busy"]
+                        })]
+                    }), Object(E.jsxs)("div", {
+                        style: {
+                            float: "right"
+                        },
+                        children: [t && Object(E.jsxs)("div", {
+                            className: "dropdown mx-2 btn-group",
+                            style: {
+                                display: "inline"
+                            },
+                            children: [Object(E.jsxs)("button", {
+                                className: "btn btn-sm btn-primary dropdown-toggle",
+                                type: "button",
+                                "data-bs-toggle": "dropdown",
+                                disabled: a,
+                                children: [Object(E.jsxs)("svg", {
+                                    xmlns: "http://www.w3.org/2000/svg",
+                                    width: "14",
+                                    height: "14",
+                                    viewBox: "0 0 24 24",
+                                    strokeWidth: "2",
+                                    stroke: "currentColor",
+                                    fill: "none",
+                                    strokeLinecap: "round",
+                                    strokeLinejoin: "round",
+                                    style: {
+                                        paddingBottom: "1px"
+                                    },
+                                    children: [Object(E.jsx)("path", {
+                                        stroke: "none",
+                                        d: "M0 0h24v24H0z",
+                                        fill: "none"
+                                    }), Object(E.jsx)("path", {
+                                        d: "M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-2"
+                                    }), Object(E.jsx)("path", {
+                                        d: "M7 11l5 5l5 -5"
+                                    }), Object(E.jsx)("path", {
+                                        d: "M12 4l0 12"
+                                    })]
+                                }), " ", "Download"]
+                            }), Object(E.jsxs)("ul", {
+                                className: "dropdown-menu my-2",
+                                children: [Object(E.jsx)("li", {
+                                    children: Object(E.jsxs)("button", {
+                                        type: "button",
+                                        style: {
+                                            cursor: "pointer"
+                                        },
+                                        className: "dropdown-item",
+                                        onClick: function() {
+                                            o ? x("".concat(s.a.defaults.baseURL).concat(c), "".concat(l, ".html")) : b()
+                                        },
+                                        children: [Object(E.jsx)("i", {
+                                            className: "fa fa-file-code-o",
+                                            "aria-hidden": "true"
+                                        }), " ", "Download as HTML"]
+                                    })
+                                }), Object(E.jsx)("li", {
+                                    children: Object(E.jsx)("hr", {
+                                        className: "dropdown-divider"
+                                    })
+                                }), Object(E.jsx)("li", {
+                                    children: Object(E.jsxs)("button", {
+                                        type: "button",
+                                        className: "dropdown-item",
+                                        onClick: function() {
+                                            o ? m(function(e, t) {
+                                                return function() {
+                                                    var a = Object(u.a)(d.a.mark((function a(n) {
+                                                        var o, i, r, c;
+                                                        return d.a.wrap((function(a) {
+                                                            for (;;) switch (a.prev = a.next) {
+                                                                case 0:
+                                                                    return a.prev = 0, n(ze(!0)), n(Ve()), n(Be("")), o = f(), i = {
+                                                                        session_id: o,
+                                                                        notebook_id: e,
+                                                                        notebook_path: t
+                                                                    }, a.next = 9, s.a.post("/api/v1/export_pdf/", i);
+                                                                case 9:
+                                                                    r = a.sent, c = r.data, n(Be(c.job_id)), a.next = 18;
+                                                                    break;
+                                                                case 14:
+                                                                    a.prev = 14, a.t0 = a.catch(0), p.b.error("The error occured during PDF export. ".concat(a.t0)), n(Ke());
+                                                                case 18:
+                                                                case "end":
+                                                                    return a.stop()
+                                                            }
+                                                        }), a, null, [
+                                                            [0, 14]
+                                                        ])
+                                                    })));
+                                                    return function(e) {
+                                                        return a.apply(this, arguments)
+                                                    }
+                                                }()
+                                            }(r, c)) : (m(ze(!0)), j())
+                                        },
+                                        children: [Object(E.jsx)("i", {
+                                            className: "fa fa-file-pdf-o",
+                                            "aria-hidden": "true"
+                                        }), " ", "Download as PDF"]
+                                    })
+                                })]
+                            })]
+                        }), Object(E.jsxs)("button", {
+                            className: "btn btn-sm btn-primary",
+                            onClick: function() {
+                                return w(!y)
+                            },
+                            disabled: a,
+                            children: [Object(E.jsxs)("svg", {
+                                xmlns: "http://www.w3.org/2000/svg",
+                                width: "14",
+                                height: "14",
+                                viewBox: "0 0 24 24",
+                                strokeWidth: "2",
+                                stroke: "currentColor",
+                                fill: "none",
+                                strokeLinecap: "round",
+                                strokeLinejoin: "round",
+                                children: [Object(E.jsx)("path", {
+                                    stroke: "none",
+                                    d: "M0 0h24v24H0z",
+                                    fill: "none"
+                                }), Object(E.jsx)("path", {
+                                    d: "M6 12m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"
+                                }), Object(E.jsx)("path", {
+                                    d: "M18 6m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"
+                                }), Object(E.jsx)("path", {
+                                    d: "M18 18m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"
+                                }), Object(E.jsx)("path", {
+                                    d: "M8.7 10.7l6.6 -3.4"
+                                }), Object(E.jsx)("path", {
+                                    d: "M8.7 13.3l6.6 3.4"
+                                })]
+                            }), " ", "Share"]
+                        })]
+                    }), Object(E.jsx)("div", {
+                        className: "",
+                        style: {
+                            position: "fixed",
+                            top: "0",
+                            left: "0",
+                            width: "100%",
+                            height: "100%",
+                            background: "rgba(0, 0, 0, 0.6)",
+                            display: y ? "block" : "none"
+                        },
+                        children: Object(E.jsx)("section", {
+                            className: "",
+                            style: {
+                                position: "fixed",
+                                width: "100%",
+                                height: "auto",
+                                top: "50%",
+                                left: "50%",
+                                transform: "translate(-50%,-50%)"
+                            },
+                            children: Object(E.jsx)("div", {
+                                className: "modal-dialog",
+                                children: Object(E.jsxs)("div", {
+                                    className: "modal-content",
+                                    children: [Object(E.jsxs)("div", {
+                                        className: "modal-header",
+                                        children: [Object(E.jsxs)("h3", {
+                                            className: "modal-title",
+                                            children: [Object(E.jsxs)("svg", {
+                                                xmlns: "http://www.w3.org/2000/svg",
+                                                width: "24",
+                                                height: "24",
+                                                viewBox: "0 0 24 24",
+                                                strokeWidth: "2",
+                                                stroke: "currentColor",
+                                                fill: "none",
+                                                strokeLinecap: "round",
+                                                strokeLinejoin: "round",
+                                                children: [Object(E.jsx)("path", {
+                                                    stroke: "none",
+                                                    d: "M0 0h24v24H0z",
+                                                    fill: "none"
+                                                }), Object(E.jsx)("path", {
+                                                    d: "M6 12m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"
+                                                }), Object(E.jsx)("path", {
+                                                    d: "M18 6m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"
+                                                }), Object(E.jsx)("path", {
+                                                    d: "M18 18m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"
+                                                }), Object(E.jsx)("path", {
+                                                    d: "M8.7 10.7l6.6 -3.4"
+                                                }), Object(E.jsx)("path", {
+                                                    d: "M8.7 13.3l6.6 3.4"
+                                                })]
+                                            }), " ", "Share"]
+                                        }), Object(E.jsx)("button", {
+                                            type: "button",
+                                            className: "btn-close",
+                                            "aria-label": "Close",
+                                            onClick: function() {
+                                                return w(!1)
+                                            }
+                                        })]
+                                    }), Object(E.jsxs)("div", {
+                                        className: "modal-body",
+                                        children: [Object(E.jsxs)("div", {
+                                            className: "py-2",
+                                            children: [Object(E.jsx)("label", {
+                                                children: "App address"
+                                            }), Object(E.jsx)("input", {
+                                                type: "text",
+                                                className: "form-control",
+                                                disabled: !0,
+                                                value: window.location.href
+                                            })]
+                                        }), !T && Object(E.jsxs)("div", {
+                                            className: "py-2",
+                                            children: [Object(E.jsx)("label", {
+                                                children: "App address with current paramters"
+                                            }), Object(E.jsx)("textarea", {
+                                                rows: 5,
+                                                className: "form-control",
+                                                disabled: !0,
+                                                value: window.location.href + _
+                                            })]
+                                        }), T && Object(E.jsxs)("div", {
+                                            className: "py-2",
+                                            children: ["There are no ", Object(E.jsx)("code", {
+                                                children: "url_key"
+                                            }), " defined for any widget. You can easily share URL to your notebook with preset values by using ", Object(E.jsx)("code", {
+                                                children: "url_key"
+                                            }), " in the widget. Please check", " ", Object(E.jsx)("a", {
+                                                href: "https://runmercury.com/docs/input-widgets/",
+                                                target: "_blank",
+                                                rel: "noreferrer",
+                                                children: "documentation"
+                                            }), "."]
+                                        }), Object(E.jsx)("div", {
+                                            className: "py-2"
+                                        })]
+                                    }), Object(E.jsx)("div", {
+                                        className: "modal-footer",
+                                        children: Object(E.jsx)("button", {
+                                            type: "button",
+                                            className: "btn btn-secondary",
+                                            onClick: function() {
+                                                return w(!1)
+                                            },
+                                            children: "Close"
+                                        })
+                                    })]
+                                })
+                            })
+                        })
                     })]
                 })
             }
 
-            function ra(e) {
+            function ia(e) {
                 var t = e.widgetKey,
                     a = e.label,
                     o = e.style,
                     s = e.value,
-                    i = e.disabled,
+                    r = e.disabled,
                     c = e.hidden,
                     l = e.runNb,
-                    d = Object(r.b)(),
+                    d = Object(i.b)(),
                     u = "btn-primary";
                 return "success" === o ? u = "btn-success" : "danger" === o ? u = "btn-danger" : "info" === o ? u = "btn-info" : "warning" === o && (u = "btn-warning"), Object(n.useEffect)((function() {
                     s && l()
-                }), [s]), Object(_.jsx)("div", {
+                }), [s]), Object(E.jsx)("div", {
                     className: "form-group mb-3",
                     style: {
                         display: c ? "none" : ""
                     },
-                    children: Object(_.jsx)("button", {
+                    children: Object(E.jsx)("button", {
                         type: "button",
                         className: "btn ".concat(u),
                         style: {
                             marginRight: "10px",
                             width: "47%"
                         },
                         onClick: function() {
                             d(Oe({
                                 key: t,
                                 value: !0
                             }))
                         },
-                        disabled: i,
+                        disabled: r,
                         children: a
                     })
                 })
             }
 
-            function ia(e) {
+            function ra(e) {
                 var t = e.runNb,
                     a = e.waiting,
                     n = e.workerState;
-                return Object(_.jsxs)("button", {
+                return Object(E.jsxs)("button", {
                     type: "button",
                     className: "btn btn-success",
                     style: {
                         marginRight: "10px",
-                        width: "47%"
+                        width: "100%"
                     },
                     onClick: function() {
                         t()
                     },
-                    disabled: a || n !== Et.Running,
-                    children: [n === Et.Running && Object(_.jsxs)("span", {
-                        children: [Object(_.jsx)("i", {
+                    disabled: a || n !== _t.Running,
+                    children: [n === _t.Running && Object(E.jsxs)("span", {
+                        children: [Object(E.jsx)("i", {
                             className: "fa fa-play",
                             "aria-hidden": "true"
                         }), " Run"]
-                    }), n === Et.Busy && Object(_.jsxs)("span", {
-                        children: [Object(_.jsx)("svg", {
+                    }), n === _t.Busy && Object(E.jsxs)("span", {
+                        children: [Object(E.jsx)("svg", {
                             xmlns: "http://www.w3.org/2000/svg",
                             width: "16",
                             height: "16",
                             fill: "white",
                             className: "bi bi-activity",
                             viewBox: "0 0 16 16",
-                            children: Object(_.jsx)("path", {
+                            children: Object(E.jsx)("path", {
                                 fillRule: "evenodd",
                                 d: "M6 2a.5.5 0 0 1 .47.33L10 12.036l1.53-4.208A.5.5 0 0 1 12 7.5h3.5a.5.5 0 0 1 0 1h-3.15l-1.88 5.17a.5.5 0 0 1-.94 0L6 3.964 4.47 8.171A.5.5 0 0 1 4 8.5H.5a.5.5 0 0 1 0-1h3.15l1.88-5.17A.5.5 0 0 1 6 2Z"
                             })
                         }), " ", "Busy"]
-                    }), n !== Et.Busy && n !== Et.Running && Object(_.jsx)("span", {
+                    }), n !== _t.Busy && n !== _t.Running && Object(E.jsx)("span", {
                         children: "Waiting ..."
                     })]
                 })
             }
             var ca = a(49);
 
             function la(e) {
                 var t = e.notebookTitle,
                     a = e.notebookId,
                     o = (e.notebookSchedule, e.taskCreatedAt, e.loadingState, e.waiting),
-                    i = e.widgetsParams,
-                    c = e.watchMode,
-                    l = e.notebookPath,
-                    b = e.displayEmbed,
-                    j = e.showFiles,
-                    h = e.isPresentation,
-                    v = (e.notebookParseErrors, e.continuousUpdate),
-                    m = e.staticNotebook,
-                    O = e.allowDownload,
-                    g = Object(r.b)(),
-                    y = Object(r.c)(Ie),
-                    w = Object(r.c)(De),
-                    k = Object(r.c)(Yt),
-                    N = Object(r.c)(We),
-                    S = Object(r.c)(Me),
-                    P = Object(n.useContext)($t),
-                    C = function() {
-                        v && T()
+                    s = e.widgetsParams,
+                    r = e.watchMode,
+                    c = e.notebookPath,
+                    l = e.displayEmbed,
+                    d = e.showFiles,
+                    u = e.isPresentation,
+                    b = (e.notebookParseErrors, e.continuousUpdate),
+                    p = e.staticNotebook,
+                    j = e.allowDownload,
+                    h = Object(i.b)(),
+                    v = Object(i.c)(Me),
+                    f = Object(i.c)(De),
+                    m = Object(i.c)(Yt),
+                    x = Object(i.c)(Ie),
+                    O = Object(i.c)(Le),
+                    g = Object(n.useContext)($t),
+                    y = function() {
+                        b && w()
                     },
-                    T = function() {
+                    w = function() {
                         var e = et();
-                        if (g(fe(e)), w) {
-                            for (var t = {}, a = 0, n = Object.entries(i); a < n.length; a++) {
+                        if (h(fe(e)), f) {
+                            for (var t = {}, a = 0, n = Object.entries(s); a < n.length; a++) {
                                 var o = Object(R.a)(n[a], 2),
-                                    s = o[0];
+                                    i = o[0];
                                 o[1];
-                                s in w ? (t[s] = w[s], g(Oe({
-                                    key: s,
-                                    value: t[s]
-                                }))) : s in y && (t[s] = y[s])
+                                i in f ? (t[i] = f[i], h(Oe({
+                                    key: i,
+                                    value: t[i]
+                                }))) : i in v && (t[i] = v[i])
                             }
-                            P.sendMessage(JSON.stringify(Xt(JSON.stringify(t)))), g(ye())
-                        } else P.sendMessage(JSON.stringify(Xt(JSON.stringify(y))))
+                            g.sendMessage(JSON.stringify(Xt(JSON.stringify(t)))), h(ye())
+                        } else g.sendMessage(JSON.stringify(Xt(JSON.stringify(v))))
                     };
                 Object(n.useEffect)((function() {
-                    N && S && (T(), g(Pe(!1)), g(Se(!1)))
-                }), [N, S]);
+                    x && O && (w(), h(Pe(!1)), h(Se(!1)))
+                }), [x, O]);
                 Object(n.useEffect)((function() {
-                    if (i)
-                        for (var e = 0, t = Object.entries(i); e < t.length; e++) {
+                    if (s)
+                        for (var e = 0, t = Object.entries(s); e < t.length; e++) {
                             var a = Object(R.a)(t[e], 2),
                                 n = a[0],
                                 o = a[1];
-                            n in y || ("file" === o.input ? g(Oe({
+                            n in v || ("file" === o.input ? h(Oe({
                                 key: n,
                                 value: []
-                            })) : "text" === o.input ? g(Oe({
+                            })) : "text" === o.input ? h(Oe({
                                 key: n,
                                 value: o.value ? o.value : ""
-                            })) : re(o) || (se(o) ? g(Oe({
+                            })) : ie(o) || (se(o) ? h(Oe({
                                 key: n,
                                 value: "output-dir"
-                            })) : g(Oe({
+                            })) : h(Oe({
                                 key: n,
                                 value: o.value
                             }))))
                         }
-                }), [g, i, y]);
-                var E = [],
-                    F = [];
-                if (i && !m) {
-                    for (var A = [], I = 0, W = Object.keys(i); I < W.length; I++) {
-                        var M = W[I],
-                            U = M.split(".");
-                        A.push([M, parseFloat("".concat(U[1], ".").concat(U[2]))])
+                }), [h, s, v]);
+                var k = [],
+                    N = [];
+                if (s && !p) {
+                    for (var S = [], P = 0, C = Object.keys(s); P < C.length; P++) {
+                        var T = C[P],
+                            _ = T.split(".");
+                        S.push([T, parseFloat("".concat(_[1], ".").concat(_[2]))])
                     }
-                    A.sort((function(e, t) {
+                    S.sort((function(e, t) {
                         return e[1] - t[1]
                     }));
-                    for (var L = 0, z = A; L < z.length; L++) {
-                        var B = z[L][0],
-                            J = i[B];
-                        X(J) ? E.push(Object(_.jsx)(rt, {
-                            widgetKey: B,
-                            disabled: o || (null === J || void 0 === J ? void 0 : J.disabled),
-                            hidden: null === J || void 0 === J ? void 0 : J.hidden,
-                            label: null === J || void 0 === J ? void 0 : J.label,
-                            value: y[B],
-                            choices: null === J || void 0 === J ? void 0 : J.choices,
-                            multi: null === J || void 0 === J ? void 0 : J.multi,
-                            runNb: C,
-                            url_key: null === J || void 0 === J ? void 0 : J.url_key
-                        }, B)) : $(J) ? E.push(Object(_.jsx)(tt, {
-                            widgetKey: B,
-                            disabled: o || (null === J || void 0 === J ? void 0 : J.disabled),
-                            hidden: null === J || void 0 === J ? void 0 : J.hidden,
-                            label: null === J || void 0 === J ? void 0 : J.label,
-                            value: y[B],
-                            runNb: C,
-                            url_key: null === J || void 0 === J ? void 0 : J.url_key
-                        }, B)) : ee(J) ? E.push(Object(_.jsx)(at, {
-                            widgetKey: B,
-                            disabled: o || (null === J || void 0 === J ? void 0 : J.disabled),
-                            hidden: null === J || void 0 === J ? void 0 : J.hidden,
-                            label: null === J || void 0 === J ? void 0 : J.label,
-                            value: y[B],
-                            min: null === J || void 0 === J ? void 0 : J.min,
-                            max: null === J || void 0 === J ? void 0 : J.max,
-                            step: null === J || void 0 === J ? void 0 : J.step,
-                            runNb: C,
-                            continuousUpdate: v,
-                            url_key: null === J || void 0 === J ? void 0 : J.url_key
-                        }, B)) : te(J) ? E.push(Object(_.jsx)(it, {
-                            widgetKey: B,
-                            disabled: o || (null === J || void 0 === J ? void 0 : J.disabled),
-                            hidden: null === J || void 0 === J ? void 0 : J.hidden,
-                            label: null === J || void 0 === J ? void 0 : J.label,
-                            value: y[B],
-                            min: null === J || void 0 === J ? void 0 : J.min,
-                            max: null === J || void 0 === J ? void 0 : J.max,
-                            step: null === J || void 0 === J ? void 0 : J.step,
-                            vertical: null === J || void 0 === J ? void 0 : J.vertical,
-                            runNb: C,
-                            url_key: null === J || void 0 === J ? void 0 : J.url_key
-                        }, B)) : ae(J) ? E.push(Object(_.jsx)(ot, {
-                            widgetKey: B,
-                            disabled: o || (null === J || void 0 === J ? void 0 : J.disabled),
-                            hidden: null === J || void 0 === J ? void 0 : J.hidden,
-                            label: null === J || void 0 === J ? void 0 : J.label,
-                            value: y[B],
-                            min: null === J || void 0 === J ? void 0 : J.min,
-                            max: null === J || void 0 === J ? void 0 : J.max,
-                            step: null === J || void 0 === J ? void 0 : J.step,
-                            vertical: null === J || void 0 === J ? void 0 : J.vertical,
-                            runNb: C,
-                            url_key: J.url_key
-                        }, B)) : ne(J) ? (E.push(Object(_.jsx)(Pt, {
-                            widgetKey: B,
-                            disabled: o || (null === J || void 0 === J ? void 0 : J.disabled),
-                            hidden: null === J || void 0 === J ? void 0 : J.hidden,
-                            label: null === J || void 0 === J ? void 0 : J.label,
-                            maxFileSize: null === J || void 0 === J ? void 0 : J.maxFileSize,
-                            value: y[B],
-                            runNb: C
-                        }, B)), F.push(B)) : oe(J) ? E.push(Object(_.jsx)(Ct, {
-                            widgetKey: B,
-                            disabled: o || (null === J || void 0 === J ? void 0 : J.disabled),
-                            hidden: null === J || void 0 === J ? void 0 : J.hidden,
-                            label: null === J || void 0 === J ? void 0 : J.label,
-                            value: y[B],
-                            rows: null === J || void 0 === J ? void 0 : J.rows,
-                            runNb: C,
-                            continuousUpdate: v,
-                            url_key: null === J || void 0 === J ? void 0 : J.url_key
-                        }, B)) : re(J) ? E.push(Object(_.jsx)(Dt, {
-                            value: J.value,
+                    for (var F = 0, A = S; F < A.length; F++) {
+                        var M = A[F][0],
+                            I = s[M];
+                        X(I) ? k.push(Object(E.jsx)(it, {
+                            widgetKey: M,
+                            disabled: o || (null === I || void 0 === I ? void 0 : I.disabled),
+                            hidden: null === I || void 0 === I ? void 0 : I.hidden,
+                            label: null === I || void 0 === I ? void 0 : I.label,
+                            value: v[M],
+                            choices: null === I || void 0 === I ? void 0 : I.choices,
+                            multi: null === I || void 0 === I ? void 0 : I.multi,
+                            runNb: y,
+                            url_key: null === I || void 0 === I ? void 0 : I.url_key
+                        }, M)) : $(I) ? k.push(Object(E.jsx)(tt, {
+                            widgetKey: M,
+                            disabled: o || (null === I || void 0 === I ? void 0 : I.disabled),
+                            hidden: null === I || void 0 === I ? void 0 : I.hidden,
+                            label: null === I || void 0 === I ? void 0 : I.label,
+                            value: v[M],
+                            runNb: y,
+                            url_key: null === I || void 0 === I ? void 0 : I.url_key
+                        }, M)) : ee(I) ? k.push(Object(E.jsx)(at, {
+                            widgetKey: M,
+                            disabled: o || (null === I || void 0 === I ? void 0 : I.disabled),
+                            hidden: null === I || void 0 === I ? void 0 : I.hidden,
+                            label: null === I || void 0 === I ? void 0 : I.label,
+                            value: v[M],
+                            min: null === I || void 0 === I ? void 0 : I.min,
+                            max: null === I || void 0 === I ? void 0 : I.max,
+                            step: null === I || void 0 === I ? void 0 : I.step,
+                            runNb: y,
+                            continuousUpdate: b,
+                            url_key: null === I || void 0 === I ? void 0 : I.url_key
+                        }, M)) : te(I) ? k.push(Object(E.jsx)(rt, {
+                            widgetKey: M,
+                            disabled: o || (null === I || void 0 === I ? void 0 : I.disabled),
+                            hidden: null === I || void 0 === I ? void 0 : I.hidden,
+                            label: null === I || void 0 === I ? void 0 : I.label,
+                            value: v[M],
+                            min: null === I || void 0 === I ? void 0 : I.min,
+                            max: null === I || void 0 === I ? void 0 : I.max,
+                            step: null === I || void 0 === I ? void 0 : I.step,
+                            vertical: null === I || void 0 === I ? void 0 : I.vertical,
+                            runNb: y,
+                            url_key: null === I || void 0 === I ? void 0 : I.url_key
+                        }, M)) : ae(I) ? k.push(Object(E.jsx)(ot, {
+                            widgetKey: M,
+                            disabled: o || (null === I || void 0 === I ? void 0 : I.disabled),
+                            hidden: null === I || void 0 === I ? void 0 : I.hidden,
+                            label: null === I || void 0 === I ? void 0 : I.label,
+                            value: v[M],
+                            min: null === I || void 0 === I ? void 0 : I.min,
+                            max: null === I || void 0 === I ? void 0 : I.max,
+                            step: null === I || void 0 === I ? void 0 : I.step,
+                            vertical: null === I || void 0 === I ? void 0 : I.vertical,
+                            runNb: y,
+                            url_key: I.url_key
+                        }, M)) : ne(I) ? (k.push(Object(E.jsx)(Pt, {
+                            widgetKey: M,
+                            disabled: o || (null === I || void 0 === I ? void 0 : I.disabled),
+                            hidden: null === I || void 0 === I ? void 0 : I.hidden,
+                            label: null === I || void 0 === I ? void 0 : I.label,
+                            maxFileSize: null === I || void 0 === I ? void 0 : I.maxFileSize,
+                            value: v[M],
+                            runNb: y
+                        }, M)), N.push(M)) : oe(I) ? k.push(Object(E.jsx)(Ct, {
+                            widgetKey: M,
+                            disabled: o || (null === I || void 0 === I ? void 0 : I.disabled),
+                            hidden: null === I || void 0 === I ? void 0 : I.hidden,
+                            label: null === I || void 0 === I ? void 0 : I.label,
+                            value: v[M],
+                            rows: null === I || void 0 === I ? void 0 : I.rows,
+                            runNb: y,
+                            continuousUpdate: b,
+                            url_key: null === I || void 0 === I ? void 0 : I.url_key
+                        }, M)) : ie(I) ? k.push(Object(E.jsx)(Dt, {
+                            value: I.value,
                             disabled: o
-                        }, B)) : ie(J) ? E.push(Object(_.jsx)(ra, {
-                            widgetKey: B,
-                            disabled: o || (null === J || void 0 === J ? void 0 : J.disabled),
-                            hidden: null === J || void 0 === J ? void 0 : J.hidden,
-                            label: null === J || void 0 === J ? void 0 : J.label,
-                            value: y[B],
-                            style: null === J || void 0 === J ? void 0 : J.style,
-                            runNb: C
-                        }, B)) : se(J) || console.log("Unknown widget type", J)
+                        }, M)) : re(I) ? k.push(Object(E.jsx)(ia, {
+                            widgetKey: M,
+                            disabled: o || (null === I || void 0 === I ? void 0 : I.disabled),
+                            hidden: null === I || void 0 === I ? void 0 : I.hidden,
+                            label: null === I || void 0 === I ? void 0 : I.label,
+                            value: v[M],
+                            style: null === I || void 0 === I ? void 0 : I.style,
+                            runNb: y
+                        }, M)) : se(I) || console.log("Unknown widget type", I)
                     }
                 }
-                var K = {};
-                b && (K = {
+                var L = {};
+                l && (L = {
                     padding: "0px"
                 });
-                var q = void 0 === t || null === t || "" === t;
-                return Object(_.jsx)("nav", {
+                var U = void 0 === t || null === t || "" === t;
+                return Object(E.jsx)("nav", {
                     id: "sidebarMenu",
                     className: "col-lg-3 d-md-block bg-light sidebar",
-                    style: Object(D.a)(Object(D.a)({}, K), {}, {
+                    style: Object(D.a)(Object(D.a)({}, L), {}, {
                         overflowY: "auto"
                     }),
-                    children: Object(_.jsx)(ca.a, {
+                    children: Object(E.jsx)(ca.a, {
                         blocking: !1,
                         message: "",
-                        children: Object(_.jsxs)("div", {
+                        children: Object(E.jsxs)("div", {
                             className: "position-sticky p-3",
-                            children: [Object(_.jsxs)("h4", {
-                                children: [t, Object(_.jsx)("button", {
+                            children: [Object(E.jsxs)("h4", {
+                                children: [t, Object(E.jsx)("button", {
                                     className: "btn btn-sm  btn-outline-primary",
                                     type: "button",
                                     style: {
                                         float: "right",
                                         zIndex: "101"
                                     },
                                     onClick: function() {
-                                        return g(V(!1))
+                                        return h(V(!1))
                                     },
                                     "data-toggle": "tooltip",
                                     "data-placement": "right",
                                     title: "Hide sidebar",
-                                    children: Object(_.jsx)("i", {
+                                    children: Object(E.jsx)("i", {
                                         className: "fa fa-chevron-left",
                                         "aria-hidden": "true"
                                     })
                                 })]
-                            }), Object(_.jsx)("div", {
+                            }), Object(E.jsx)("div", {
                                 style: {
                                     padding: "0px"
                                 },
-                                children: Object(_.jsxs)("form", {
-                                    children: [E, q && Object(_.jsx)("div", {
+                                children: Object(E.jsxs)("form", {
+                                    children: [k, U && Object(E.jsx)("div", {
                                         style: {
                                             padding: "15px"
                                         }
-                                    }), Object(_.jsxs)("div", {
+                                    }), Object(E.jsx)("div", {
                                         className: "form-group mb-3 pb-1 pt-2",
-                                        children: [!v && Object(_.jsx)(ia, {
-                                            runNb: T,
+                                        children: !b && Object(E.jsx)(ra, {
+                                            runNb: w,
                                             waiting: o,
-                                            workerState: k
-                                        }), O && Object(_.jsxs)("div", {
-                                            className: "dropdown",
-                                            style: {
-                                                width: "47%",
-                                                float: v ? "left" : "right"
-                                            },
-                                            children: [Object(_.jsx)("button", {
-                                                className: "btn btn-primary dropdown-toggle",
-                                                style: {
-                                                    margin: "0px",
-                                                    width: "100%"
-                                                },
-                                                type: "button",
-                                                "data-bs-toggle": "dropdown",
-                                                disabled: o,
-                                                children: "Download"
-                                            }), Object(_.jsxs)("ul", {
-                                                className: "dropdown-menu dropdown-menu-end",
-                                                children: [Object(_.jsx)("li", {
-                                                    children: Object(_.jsxs)("a", {
-                                                        style: {
-                                                            cursor: "pointer"
-                                                        },
-                                                        className: "dropdown-item",
-                                                        onClick: function() {
-                                                            m ? x("".concat(s.a.defaults.baseURL).concat(l), "".concat(t, ".html")) : m || P.sendMessage(JSON.stringify({
-                                                                purpose: "download-html"
-                                                            }))
-                                                        },
-                                                        children: [Object(_.jsx)("i", {
-                                                            className: "fa fa-file-code-o",
-                                                            "aria-hidden": "true"
-                                                        }), " ", "Download as HTML"]
-                                                    })
-                                                }), Object(_.jsx)("li", {
-                                                    children: Object(_.jsx)("hr", {
-                                                        className: "dropdown-divider"
-                                                    })
-                                                }), Object(_.jsx)("li", {
-                                                    children: Object(_.jsxs)("button", {
-                                                        type: "button",
-                                                        className: "dropdown-item",
-                                                        onClick: function() {
-                                                            m ? g(function(e, t) {
-                                                                return function() {
-                                                                    var a = Object(u.a)(d.a.mark((function a(n) {
-                                                                        var o, r, i, c;
-                                                                        return d.a.wrap((function(a) {
-                                                                            for (;;) switch (a.prev = a.next) {
-                                                                                case 0:
-                                                                                    return a.prev = 0, n(ze(!0)), n(Ve()), n(Be("")), o = f(), r = {
-                                                                                        session_id: o,
-                                                                                        notebook_id: e,
-                                                                                        notebook_path: t
-                                                                                    }, a.next = 9, s.a.post("/api/v1/export_pdf/", r);
-                                                                                case 9:
-                                                                                    i = a.sent, c = i.data, n(Be(c.job_id)), a.next = 18;
-                                                                                    break;
-                                                                                case 14:
-                                                                                    a.prev = 14, a.t0 = a.catch(0), p.b.error("The error occured during PDF export. ".concat(a.t0)), n(Ke());
-                                                                                case 18:
-                                                                                case "end":
-                                                                                    return a.stop()
-                                                                            }
-                                                                        }), a, null, [
-                                                                            [0, 14]
-                                                                        ])
-                                                                    })));
-                                                                    return function(e) {
-                                                                        return a.apply(this, arguments)
-                                                                    }
-                                                                }()
-                                                            }(a, l)) : (g(ze(!0)), m || P.sendMessage(JSON.stringify({
-                                                                purpose: "download-pdf"
-                                                            })))
-                                                        },
-                                                        children: [Object(_.jsx)("i", {
-                                                            className: "fa fa-file-pdf-o",
-                                                            "aria-hidden": "true"
-                                                        }), " ", "Download as PDF"]
-                                                    })
-                                                })]
-                                            })]
-                                        })]
-                                    }), v && Object(_.jsx)("div", {
-                                        children: Object(_.jsx)("br", {})
-                                    }), k === Et.MaxIdleTimeReached && Object(_.jsxs)("div", {
+                                            workerState: m
+                                        })
+                                    }), m === _t.UsageLimitReached && Object(E.jsxs)("div", {
+                                        className: "alert alert-info mb-3 mt-3",
+                                        role: "alert",
+                                        children: [Object(E.jsx)("i", {
+                                            className: "fa fa-info-circle",
+                                            "aria-hidden": "true"
+                                        }), " Usage limit was reached. Please upgrade the plan."]
+                                    }), m === _t.MaxIdleTimeReached && Object(E.jsxs)("div", {
                                         className: "alert alert-info mb-3 mt-3",
                                         role: "alert",
-                                        children: [Object(_.jsx)("i", {
+                                        children: [Object(E.jsx)("i", {
                                             className: "fa fa-info-circle",
                                             "aria-hidden": "true"
-                                        }), " Your worker was idle for too long, that's why we have stopped it. Do you need a worker?", Object(_.jsx)("br", {}), Object(_.jsx)("button", {
+                                        }), " Your worker was idle for too long, that's why we have stopped it. Do you need a worker?", Object(E.jsx)("br", {}), Object(E.jsx)("button", {
                                             className: "btn btn-sm btn-primary my-2",
                                             onClick: function() {
                                                 return window.location.reload()
                                             },
                                             children: "Restart worker"
                                         })]
-                                    }), k === Et.MaxRunTimeReached && Object(_.jsxs)("div", {
+                                    }), m === _t.MaxRunTimeReached && Object(E.jsxs)("div", {
                                         className: "alert alert-info mb-3 mt-3",
                                         role: "alert",
-                                        children: [Object(_.jsx)("i", {
+                                        children: [Object(E.jsx)("i", {
                                             className: "fa fa-info-circle",
                                             "aria-hidden": "true"
-                                        }), " Your worker was running for too long, that's why we have stopped it. Do you need a worker?", Object(_.jsx)("br", {}), Object(_.jsx)("button", {
+                                        }), " Your worker was running for too long, that's why we have stopped it. Do you need a worker?", Object(E.jsx)("br", {}), Object(E.jsx)("button", {
                                             className: "btn btn-sm btn-primary my-2",
                                             onClick: function() {
                                                 return window.location.reload()
                                             },
                                             children: "Restart worker"
                                         })]
-                                    }), o && (k === Et.Unknown || k === Et.Queued) && Object(_.jsxs)("div", {
+                                    }), o && (m === _t.Unknown || m === _t.Queued) && Object(E.jsxs)("div", {
                                         className: "alert alert-warning mb-3 mt-3",
                                         role: "alert",
-                                        children: [Object(_.jsx)("i", {
+                                        children: [Object(E.jsx)("i", {
                                             className: "fa fa-cogs",
                                             "aria-hidden": "true"
                                         }), " Waiting for worker ..."]
-                                    }), o && k === Et.Starting && Object(_.jsxs)("div", {
+                                    }), o && m === _t.Starting && Object(E.jsxs)("div", {
                                         className: "alert alert-success mb-3 mt-3",
                                         role: "alert",
-                                        children: [Object(_.jsx)("i", {
+                                        children: [Object(E.jsx)("i", {
                                             className: "fa fa-cogs",
                                             "aria-hidden": "true"
                                         }), " Initializing worker ..."]
-                                    }), c && Object(_.jsxs)("div", {
+                                    }), r && Object(E.jsxs)("div", {
                                         className: "alert alert-secondary mb-3 mt-3",
                                         role: "alert",
-                                        children: [Object(_.jsx)("i", {
+                                        children: [Object(E.jsx)("i", {
                                             className: "fa fa-refresh",
                                             "aria-hidden": "true"
                                         }), " Notebook in watch mode. All changes to Notebook will be automatically visible in Mercury."]
-                                    }), h && Object(_.jsxs)("div", {
+                                    }), u && Object(E.jsxs)("div", {
                                         className: "alert alert-primary mb-3",
                                         role: "alert",
-                                        children: [Object(_.jsx)("i", {
+                                        children: [Object(E.jsx)("i", {
                                             className: "fa fa-television",
                                             "aria-hidden": "true"
-                                        }), " Click on presentation and press ", Object(_.jsx)("b", {
+                                        }), " Click on presentation and press ", Object(E.jsx)("b", {
                                             children: "F"
-                                        }), " for full screen. Press", " ", Object(_.jsx)("b", {
+                                        }), " for full screen. Press", " ", Object(E.jsx)("b", {
                                             children: "Esc"
-                                        }), " to quit.", Object(_.jsx)("br", {}), Object(_.jsx)("br", {}), Object(_.jsx)("i", {
+                                        }), " to quit.", Object(E.jsx)("br", {}), Object(E.jsx)("br", {}), Object(E.jsx)("i", {
                                             className: "fa fa-arrows",
                                             "aria-hidden": "true"
-                                        }), " Click on presentation and press ", Object(_.jsx)("b", {
+                                        }), " Click on presentation and press ", Object(E.jsx)("b", {
                                             children: "Esc"
                                         }), " to navigate slides."]
                                     })]
                                 })
-                            }), j && Object(_.jsxs)("div", {
-                                children: [Object(_.jsx)("hr", {}), Object(_.jsxs)("button", {
+                            }), d && Object(E.jsxs)("div", {
+                                children: [Object(E.jsx)("hr", {}), Object(E.jsxs)("button", {
                                     className: "btn btn-sm btn-outline-secondary",
                                     style: {
                                         border: "none"
                                     },
                                     onClick: function() {
-                                        g(H("app"))
+                                        h(H("app"))
                                     },
-                                    children: [Object(_.jsx)("i", {
+                                    children: [Object(E.jsx)("i", {
                                         className: "fa fa-laptop",
                                         "aria-hidden": "true"
                                     }), " App"]
-                                }), Object(_.jsxs)("button", {
+                                }), Object(E.jsxs)("button", {
                                     className: "btn btn-sm btn-outline-secondary",
                                     style: {
                                         border: "none"
                                     },
                                     onClick: function() {
-                                        g(H("files"))
+                                        h(H("files"))
                                     },
-                                    children: [Object(_.jsx)("i", {
+                                    children: [Object(E.jsx)("i", {
                                         className: "fa fa-folder-open-o",
                                         "aria-hidden": "true"
                                     }), " ", "Output Files"]
                                 })]
-                            }), void 0 !== a && !m && Object(_.jsxs)("div", {
-                                children: [Object(_.jsx)("hr", {}), Object(_.jsxs)("div", {
+                            }), Object(E.jsxs)("div", {
+                                children: [Object(E.jsx)("hr", {}), Object(E.jsxs)("div", {
                                     style: {
                                         paddingLeft: "10px"
                                     },
-                                    children: [Object(_.jsx)(sa, {}), " "]
+                                    children: [Object(E.jsx)(sa, {
+                                        notebookId: a,
+                                        notebookPath: c,
+                                        notebookTitle: t,
+                                        staticNotebook: p,
+                                        allowDownload: j,
+                                        waiting: o,
+                                        continuousUpdate: b,
+                                        runDownloadHTML: function() {
+                                            p || g.sendMessage(JSON.stringify({
+                                                purpose: "download-html"
+                                            }))
+                                        },
+                                        runDownloadPDF: function() {
+                                            p || g.sendMessage(JSON.stringify({
+                                                purpose: "download-pdf"
+                                            }))
+                                        },
+                                        widgetsValues: v,
+                                        widgetsParams: s
+                                    }), " "]
                                 })]
                             })]
                         })
                     })
                 })
             }
             var da = a(170);
 
             function ua(e) {
                 var t = e.appView,
                     a = e.loadingState,
                     o = e.notebookPath,
-                    i = e.waiting,
+                    r = e.waiting,
                     c = e.errorMsg,
                     l = e.watchMode,
                     d = e.displayEmbed,
                     u = e.username,
                     b = e.slidesHash,
                     p = e.columnsWidth,
                     j = e.isPresentation,
@@ -2266,17 +2502,17 @@
                             return window.addEventListener("resize", e),
                                 function() {
                                     return window.removeEventListener("resize", e)
                                 }
                         }), []), a
                     }().height,
                     f = d ? v - 10 : v - 58,
-                    m = Object(r.b)(),
-                    x = Object(r.c)(Ee),
-                    O = Object(r.c)(Qt),
+                    m = Object(i.b)(),
+                    x = Object(i.c)(_e),
+                    O = Object(i.c)(Qt),
                     g = !1;
                 if (void 0 !== x && void 0 !== x.params && void 0 !== x.params["show-code"] && null !== x.params["show-code"] && (g = x.params["show-code"]), "" !== O && !j && (O = "<script>init_mathjax();<\/script>" + O, !g)) {
                     O = '<style type="text/css">\n      .jp-mod-noOutputs {\n          padding: 0px; \n      }\n      .jp-mod-noInput {\n        padding-top: 0px;\n        padding-bottom: 0px;\n      }\n      </style>' + O
                 }
                 if ("" !== O && j && "" !== b && -1 === O.indexOf("Reveal.slide(")) {
                     var y = b.split("/"),
                         w = "";
@@ -2294,194 +2530,194 @@
                         paddingLeft: h ? "12px" : "0px",
                         display: "files" === t ? "none" : "block"
                     },
                     N = {};
                 return h || (N = {
                     maxWidth: "1140px",
                     margin: "auto"
-                }), Object(_.jsx)("main", {
+                }), Object(E.jsx)("main", {
                     className: "ms-sm-auto col-".concat(p),
                     style: k,
-                    children: Object(_.jsx)(ca.a, {
+                    children: Object(E.jsx)(ca.a, {
                         tag: "div",
-                        blocking: i,
-                        children: Object(_.jsxs)("div", {
+                        blocking: r,
+                        children: Object(E.jsxs)("div", {
                             style: N,
-                            children: ["loading" === a && !l && Object(_.jsx)("p", {
+                            children: ["loading" === a && !l && Object(E.jsx)("p", {
                                 children: "Loading notebook. Please wait ..."
-                            }), "error" === a && Object(_.jsx)("p", {
+                            }), "error" === a && Object(E.jsx)("p", {
                                 style: {
                                     margin: "20px"
                                 },
                                 children: "Problem while loading notebook. Please try again later or contact Mercury administrator."
-                            }), "error" === a && "" === u && Object(_.jsxs)("p", {
+                            }), "error" === a && "" === u && Object(E.jsxs)("p", {
                                 style: {
                                     margin: "20px"
                                 },
-                                children: [Object(_.jsx)("h5", {
+                                children: [Object(E.jsx)("h5", {
                                     children: "Please log in to see the notebook"
-                                }), Object(_.jsxs)("a", {
+                                }), Object(E.jsxs)("a", {
                                     href: "/login",
                                     className: "btn btn-primary btn-sm ",
-                                    children: [Object(_.jsx)("i", {
+                                    children: [Object(E.jsx)("i", {
                                         className: "fa fa-sign-in",
                                         "aria-hidden": "true"
                                     }), " Log in"]
                                 })]
-                            }), c && Object(_.jsxs)("div", {
+                            }), c && Object(E.jsxs)("div", {
                                 className: "alert alert-danger mb-3",
                                 role: "alert",
-                                children: [Object(_.jsx)("b", {
+                                children: [Object(E.jsx)("b", {
                                     children: "Notebook is executed with errors."
-                                }), Object(_.jsx)("p", {
+                                }), Object(E.jsx)("p", {
                                     children: c
                                 })]
-                            }), "" === c && "loading" !== a && j && "" !== O && Object(_.jsx)("iframe", {
+                            }), "" === c && "loading" !== a && j && "" !== O && Object(E.jsx)("iframe", {
                                 width: "100%",
                                 height: f,
                                 srcDoc: O,
                                 title: "display",
                                 id: "main-iframe",
                                 onError: function() {
                                     console.log("iframe error")
                                 }
-                            }, o), "" !== O && !j && Object(_.jsx)(da.a, {
+                            }, o), "" !== O && !j && Object(E.jsx)(da.a, {
                                 html: O
                             })]
                         })
                     })
                 })
             }
 
             function ba(e) {
                 var t = e.files,
                     a = e.filesState,
                     n = e.waiting,
-                    o = Object(r.b)();
+                    o = Object(i.b)();
                 console.log(t);
-                var i, c = [],
-                    l = Object(W.a)(t);
+                var r, c = [],
+                    l = Object(I.a)(t);
                 try {
                     var d = function() {
-                        var e, t = i.value,
+                        var e, t = r.value,
                             a = t.split("/").pop();
                         if (a = null === (e = a) || void 0 === e ? void 0 : e.split("?")[0], t && a) {
                             var n = "".concat(s.a.defaults.baseURL).concat(t);
-                            t.includes("s3.amazonaws.com") && (n = t), c.push(Object(_.jsxs)("div", {
-                                children: [Object(_.jsx)("i", {
+                            t.includes("s3.amazonaws.com") && (n = t), c.push(Object(E.jsxs)("div", {
+                                children: [Object(E.jsx)("i", {
                                     className: "fa fa-file-text-o",
                                     "aria-hidden": "true",
                                     style: {
                                         paddingRight: "5px"
                                     }
-                                }), " ", Object(_.jsx)("b", {
+                                }), " ", Object(E.jsx)("b", {
                                     children: a
-                                }), Object(_.jsxs)("button", {
+                                }), Object(E.jsxs)("button", {
                                     style: {
                                         float: "right"
                                     },
                                     type: "button",
                                     className: "btn btn-primary",
                                     onClick: function() {
                                         return e = n, t = a, void s.a.get(e, {
                                             responseType: "blob"
                                         }).then((function(e) {
                                             v()(e.data, t)
                                         }));
                                         var e, t
                                     },
-                                    children: [Object(_.jsx)("i", {
+                                    children: [Object(E.jsx)("i", {
                                         className: "fa fa-download",
                                         "aria-hidden": "true"
                                     }), " Download"]
-                                }), Object(_.jsx)("hr", {})]
+                                }), Object(E.jsx)("hr", {})]
                             }, t))
                         }
                     };
-                    for (l.s(); !(i = l.n()).done;) d()
+                    for (l.s(); !(r = l.n()).done;) d()
                 } catch (u) {
                     l.e(u)
                 } finally {
                     l.f()
                 }
-                return Object(_.jsxs)("main", {
+                return Object(E.jsxs)("main", {
                     className: "col-md-9 ms-sm-auto col-lg-9",
                     style: {
                         padding: "20px"
                     },
-                    children: [Object(_.jsxs)("div", {
+                    children: [Object(E.jsxs)("div", {
                         className: "col-8",
-                        children: [Object(_.jsxs)("h3", {
+                        children: [Object(E.jsxs)("h3", {
                             style: {
                                 paddingBottom: "10px"
                             },
-                            children: [Object(_.jsx)("i", {
+                            children: [Object(E.jsx)("i", {
                                 className: "fa fa-folder-open-o",
                                 "aria-hidden": "true"
                             }), " Output Files"]
-                        }), Object(_.jsx)(ca.a, {
+                        }), Object(E.jsx)(ca.a, {
                             tag: "div",
                             blocking: n,
-                            children: Object(_.jsxs)("div", {
-                                children: ["loaded" === a && c, "unknown" === a && Object(_.jsx)("p", {
+                            children: Object(E.jsxs)("div", {
+                                children: ["loaded" === a && c, "unknown" === a && Object(E.jsx)("p", {
                                     children: "Please run the notebook to produce output files ..."
-                                }), "loading" === a && Object(_.jsx)("p", {
+                                }), "loading" === a && Object(E.jsx)("p", {
                                     children: "Loading files please wait ..."
-                                }), "error" === a && Object(_.jsx)("div", {
+                                }), "error" === a && Object(E.jsx)("div", {
                                     className: "alert alert-danger mb-3",
                                     role: "alert",
                                     children: "There was an error during loading files. Please try to run the app again or contact the administrator."
                                 })]
                             })
                         })]
-                    }), Object(_.jsxs)("button", {
+                    }), Object(E.jsxs)("button", {
                         className: "btn btn-secondary btn-sm",
                         onClick: function() {
                             o(H("app"))
                         },
-                        children: [Object(_.jsx)("i", {
+                        children: [Object(E.jsx)("i", {
                             className: "fa fa-arrow-left",
                             "aria-hidden": "true"
                         }), " Back to App"]
                     })]
                 })
             }
 
             function pa() {
-                return Object(_.jsx)("a", {
+                return Object(E.jsx)("a", {
                     href: "https://runmercury.com",
                     target: "_blank",
                     rel: "noreferrer",
-                    children: Object(_.jsxs)("div", {
+                    children: Object(E.jsxs)("div", {
                         className: "poweredby",
-                        children: [Object(_.jsxs)("div", {
+                        children: [Object(E.jsxs)("div", {
                             className: "text-center",
-                            children: [" ", Object(_.jsx)("b", {
+                            children: [" ", Object(E.jsx)("b", {
                                 style: {
                                     fontSize: "0.9em"
                                 },
                                 children: "created with"
                             }), " "]
-                        }), Object(_.jsx)("div", {
-                            children: Object(_.jsx)("img", {
+                        }), Object(E.jsx)("div", {
+                            children: Object(E.jsx)("img", {
                                 alt: "Mercury",
                                 src: "/static/mercury_black_logo.svg",
                                 style: {
                                     height: "27px"
                                 }
                             })
                         })]
                     })
                 })
             }
 
             function ja(e) {
-                for (var t = e.slug, a = e.widgetsParams, o = e.notebookPath, i = e.columnsWidth, c = e.taskSessionId, l = Object(n.useState)(JSON.stringify({
+                for (var t = e.slug, a = e.widgetsParams, o = e.notebookPath, r = e.columnsWidth, c = e.taskSessionId, l = Object(n.useState)(JSON.stringify({
                         msg: "Example output"
-                    })), b = Object(R.a)(l, 2), p = b[0], j = b[1], h = Object(r.c)(Ie), v = {}, f = 0, m = Object.entries(a); f < m.length; f++) {
+                    })), b = Object(R.a)(l, 2), p = b[0], j = b[1], h = Object(i.c)(Me), v = {}, f = 0, m = Object.entries(a); f < m.length; f++) {
                     var x = Object(R.a)(m[f], 2),
                         O = x[0];
                     x[1].input && (v[O] = h[O])
                 }
 
                 function g() {
                     return (g = Object(u.a)(d.a.mark((function e() {
@@ -2508,84 +2744,84 @@
                     c && function() {
                         g.apply(this, arguments)
                     }()
                 }), [c, o]);
                 var y = "id-with-some-random-string";
                 c && (y = c);
                 var w = 'curl -X POST -H "Content-Type: application/json" -d \''.concat(JSON.stringify(v), "' ").concat(s.a.defaults.baseURL, "/run/").concat(t);
-                return Object(_.jsxs)("div", {
-                    className: "ms-sm-auto col-lg-".concat(i),
+                return Object(E.jsxs)("div", {
+                    className: "ms-sm-auto col-lg-".concat(r),
                     style: {
                         border: "none",
                         paddingTop: "0px",
                         paddingRight: "0px",
                         paddingLeft: "0px",
                         padding: "10px"
                     },
-                    children: [Object(_.jsx)("h4", {
+                    children: [Object(E.jsx)("h4", {
                         children: "Notebook as REST API"
-                    }), Object(_.jsx)("p", {
+                    }), Object(E.jsx)("p", {
                         children: "This notebook can be executed as REST API. Please see the examples below on how to access the notebook."
-                    }), Object(_.jsxs)("div", {
+                    }), Object(E.jsxs)("div", {
                         className: "alert alert-secondary",
                         role: "alert",
-                        children: [Object(_.jsx)("h5", {
+                        children: [Object(E.jsx)("h5", {
                             children: "POST request to execute the notebook"
-                        }), Object(_.jsx)("textarea", {
+                        }), Object(E.jsx)("textarea", {
                             disabled: !0,
                             style: {
                                 width: "100%"
                             },
                             rows: 3,
                             value: w
-                        }), "The above request should return a JSON with `id`. The `id` should be used in the GET request to fetch the result.", Object(_.jsx)("br", {}), "Example response:", Object(_.jsx)("pre", {
+                        }), "The above request should return a JSON with `id`. The `id` should be used in the GET request to fetch the result.", Object(E.jsx)("br", {}), "Example response:", Object(E.jsx)("pre", {
                             children: '{"id": "'.concat(y, '"}')
                         })]
-                    }), Object(_.jsxs)("div", {
+                    }), Object(E.jsxs)("div", {
                         className: "alert alert-secondary",
                         role: "alert",
-                        children: [Object(_.jsx)("h5", {
+                        children: [Object(E.jsx)("h5", {
                             children: "GET request to get execution result in JSON"
-                        }), Object(_.jsx)("textarea", {
+                        }), Object(E.jsx)("textarea", {
                             disabled: !0,
                             style: {
                                 width: "100%"
                             },
                             rows: 1,
                             value: "curl ".concat(s.a.defaults.baseURL, "/get/").concat(y)
                         })]
-                    }), Object(_.jsxs)("div", {
+                    }), Object(E.jsxs)("div", {
                         className: "alert alert-primary",
                         role: "alert",
-                        children: [Object(_.jsx)("h5", {
+                        children: [Object(E.jsx)("h5", {
                             children: "Response"
-                        }), Object(_.jsx)("pre", {
+                        }), Object(E.jsx)("pre", {
                             children: p
                         })]
                     })]
                 })
             }
 
             function ha() {
-                var e = Object(r.b)(),
-                    t = Object(r.c)($e),
-                    a = Object(r.c)(Xe),
-                    o = Object(r.c)(Ze);
+                var e = Object(i.b)(),
+                    t = Object(i.c)($e),
+                    a = Object(i.c)(Xe),
+                    o = Object(i.c)(Ze);
                 return Object(n.useEffect)((function() {
                     "" !== a && o && (t < 120 ? setTimeout((function() {
                         e(function(e) {
                             return function() {
                                 var t = Object(u.a)(d.a.mark((function t(a) {
-                                    var n, o, r;
+                                    var n, o, i;
                                     return d.a.wrap((function(t) {
                                         for (;;) switch (t.prev = t.next) {
                                             case 0:
                                                 return t.prev = 0, n = "/api/v1/get_pdf/".concat(e, "/"), t.next = 4, s.a.get(n);
                                             case 4:
-                                                o = t.sent, (r = o.data).ready ? (a(Ke()), "" !== r.error ? p.b.error(r.error) : x("".concat(s.a.defaults.baseURL).concat(r.url), "".concat(r.title))) : a(Je()), t.next = 13;
+                                                o = t.sent, (i = o.data).ready ? (a(Ke()), "" !== i.error ? p.b.error(i.error) : x("".concat(s.a.defaults.baseURL).concat(i.url), "".concat(i.title))) : a(Je()), t.next = 13;
                                                 break;
                                             case 9:
                                                 t.prev = 9, t.t0 = t.catch(0), p.b.error("The error occured during PDF export. ".concat(t.t0)), a(Ke());
                                             case 13:
                                             case "end":
                                                 return t.stop()
                                         }
@@ -2597,55 +2833,55 @@
                                     return t.apply(this, arguments)
                                 }
                             }()
                         }(a))
                     }), 1e3) : (e(Ke()), p.b.error("Problem with PDF export. Please try again later or ask your admin for help.", {
                         autoClose: 6e3
                     })))
-                }), [e, t, a, o]), Object(_.jsx)("div", {})
+                }), [e, t, a, o]), Object(E.jsx)("div", {})
             }
             var va = function(e) {
                 e.isSingleApp;
-                var t, a, o, i, c, l = e.notebookSlug,
+                var t, a, o, r, c, l = e.notebookSlug,
                     b = e.displayEmbed,
-                    p = Object(r.b)(),
-                    j = Object(r.c)(Ee),
-                    h = Object(r.c)(Fe),
-                    v = Object(r.c)(Ye),
-                    m = Object(r.c)(Ge),
-                    x = Object(r.c)(Qe),
-                    O = Object(r.c)(K),
-                    g = Object(r.c)(Y),
-                    y = Object(r.c)(q),
-                    w = Object(r.c)(T),
-                    k = Object(r.c)(C),
-                    N = Object(r.c)(Ae),
-                    S = Object(r.c)(G),
-                    P = Object(r.c)(Ze),
-                    E = Object(r.c)(Gt),
-                    F = Object(r.c)(Yt),
-                    A = Object(r.c)(wt),
-                    W = Object(r.c)(Nt),
-                    M = function() {
+                    p = Object(i.b)(),
+                    j = Object(i.c)(_e),
+                    h = Object(i.c)(Fe),
+                    v = Object(i.c)(Ye),
+                    m = Object(i.c)(Ge),
+                    x = Object(i.c)(Qe),
+                    O = Object(i.c)(K),
+                    g = Object(i.c)(Y),
+                    y = Object(i.c)(q),
+                    w = Object(i.c)(T),
+                    k = Object(i.c)(C),
+                    N = Object(i.c)(Ae),
+                    S = Object(i.c)(G),
+                    P = Object(i.c)(Ze),
+                    _ = Object(i.c)(Gt),
+                    F = Object(i.c)(Yt),
+                    A = Object(i.c)(wt),
+                    I = Object(i.c)(Nt),
+                    L = function() {
                         var e;
-                        return !(null === j || void 0 === j || null === (e = j.params) || void 0 === e ? void 0 : e.static_notebook) && F !== Et.Running
+                        return !(null === j || void 0 === j || null === (e = j.params) || void 0 === e ? void 0 : e.static_notebook) && (F !== _t.UsageLimitReached && F !== _t.MaxIdleTimeReached && F !== _t.MaxRunTimeReached && F !== _t.Running)
                     },
                     U = function() {
                         return "WATCH_READY" === j.state || "WATCH_WAIT" === j.state || "WATCH_ERROR" === j.state
                     };
                 Object(n.useEffect)((function() {
                     void 0 !== A && p(function(e, t) {
                         var a = arguments.length > 2 && void 0 !== arguments[2] && arguments[2];
                         return function() {
                             var n = Object(u.a)(d.a.mark((function n(o) {
-                                var r, i, c, l, u, b;
+                                var i, r, c, l, u, b;
                                 return d.a.wrap((function(n) {
                                     for (;;) switch (n.prev = n.next) {
                                         case 0:
-                                            return n.prev = 0, a || (o(fe("")), o(qe())), r = ce(), i = r.width, o(V(i > 992)), a || o(ve("loading")), c = "/api/v1/".concat(e, "/getnb/").concat(t, "/"), n.next = 8, s.a.get(c);
+                                            return n.prev = 0, a || (o(fe("")), o(qe())), i = ce(), r = i.width, o(V(r > 992)), a || o(ve("loading")), c = "/api/v1/".concat(e, "/getnb/").concat(t, "/"), n.next = 8, s.a.get(c);
                                         case 8:
                                             l = n.sent, u = l.data, b = JSON.parse(u.params), o(he(Object(D.a)(Object(D.a)({}, u), {}, {
                                                 params: b
                                             }))), a || o(ve("loaded")), null !== (null === b || void 0 === b ? void 0 : b.show_sidebar) && void 0 !== (null === b || void 0 === b ? void 0 : b.show_sidebar) && o(V(null === b || void 0 === b ? void 0 : b.show_sidebar)), n.next = 20;
                                             break;
                                         case 16:
                                             n.prev = 16, n.t0 = n.catch(0), a || o(ve("error")), console.error("Problem during loading selected notebook (".concat(t, "). ").concat(n.t0));
@@ -2660,24 +2896,24 @@
                             return function(e) {
                                 return n.apply(this, arguments)
                             }
                         }()
                     }(A, l))
                 }), [p, A, l, k]), Object(n.useEffect)((function() {
                     var e;
-                    "files" === O && "2" === (null === j || void 0 === j || null === (e = j.params) || void 0 === e ? void 0 : e.version) && void 0 !== E && void 0 !== j.id && p(function(e, t) {
+                    "files" === O && "2" === (null === j || void 0 === j || null === (e = j.params) || void 0 === e ? void 0 : e.version) && void 0 !== _ && void 0 !== j.id && p(function(e, t) {
                         return function() {
                             var a = Object(u.a)(d.a.mark((function a(n) {
-                                var o, r, i, c;
+                                var o, i, r, c;
                                 return d.a.wrap((function(a) {
                                     for (;;) switch (a.prev = a.next) {
                                         case 0:
-                                            return a.prev = 0, n(z("loading")), n(B([])), o = f(), r = "/api/v1/worker-output-files/".concat(o, "/").concat(e, "/").concat(t, "/"), a.next = 7, s.a.get(r);
+                                            return a.prev = 0, n(z("loading")), n(B([])), o = f(), i = "/api/v1/worker-output-files/".concat(o, "/").concat(e, "/").concat(t, "/"), a.next = 7, s.a.get(i);
                                         case 7:
-                                            i = a.sent, c = i.data, n(B(c)), n(z("loaded")), a.next = 17;
+                                            r = a.sent, c = r.data, n(B(c)), n(z("loaded")), a.next = 17;
                                             break;
                                         case 13:
                                             a.prev = 13, a.t0 = a.catch(0), n(z("error")), console.error("Problem during loading worker output files. ".concat(a.t0));
                                         case 17:
                                         case "end":
                                             return a.stop()
                                     }
@@ -2685,234 +2921,234 @@
                                     [0, 13]
                                 ])
                             })));
                             return function(e) {
                                 return a.apply(this, arguments)
                             }
                         }()
-                    }(E, j.id))
-                }), [p, O, j, E]);
-                var L = j.default_view_path;
-                v.state && "DONE" === v.state && v.result && (L = v.result);
+                    }(_, j.id))
+                }), [p, O, j, _]);
+                var W = j.default_view_path;
+                v.state && "DONE" === v.state && v.result && (W = v.result);
                 var H = "";
-                v.state && v.result && "ERROR" === v.state && (H = v.result), m.state && "DONE" === m.state && m.result && (L = m.result), m.state && m.result && "ERROR" === m.state && (H = m.result), L === j.default_view_path && x.state && "DONE" === x.state && x.result && (L = x.result);
+                v.state && v.result && "ERROR" === v.state && (H = v.result), m.state && "DONE" === m.state && m.result && (W = m.result), m.state && m.result && "ERROR" === m.state && (H = m.result), W === j.default_view_path && x.state && "DONE" === x.state && x.result && (W = x.result);
                 var J = !1;
-                return j.output && j.output.toLowerCase().startsWith("rest") && (J = !0), Object(_.jsxs)("div", {
+                return j.output && j.output.toLowerCase().startsWith("rest") && (J = !0), Object(E.jsxs)("div", {
                     className: "App",
-                    children: [!b && Object(_.jsx)(I, {
-                        isSitePublic: W,
+                    children: [!b && Object(E.jsx)(M, {
+                        isSitePublic: I,
                         username: w
-                    }), Object(_.jsxs)(ca.a, {
+                    }), Object(E.jsxs)(ca.a, {
                         blocking: P,
                         message: "Exporting to PDF. Please wait ...",
-                        children: [P && Object(_.jsx)(ha, {}), Object(_.jsx)("div", {
+                        children: [P && Object(E.jsx)(ha, {}), Object(E.jsx)("div", {
                             className: "container-fluid",
-                            children: Object(_.jsxs)("div", {
+                            children: Object(E.jsxs)("div", {
                                 className: "row",
-                                children: [S && Object(_.jsx)(la, {
+                                children: [S && Object(E.jsx)(la, {
                                     notebookTitle: j.title,
                                     notebookId: j.id,
                                     notebookSchedule: j.schedule,
                                     taskCreatedAt: v.created_at,
                                     loadingState: h,
-                                    waiting: M(),
+                                    waiting: L(),
                                     widgetsParams: null === j || void 0 === j || null === (t = j.params) || void 0 === t ? void 0 : t.params,
                                     watchMode: U(),
-                                    notebookPath: L,
+                                    notebookPath: W,
                                     displayEmbed: b,
                                     showFiles: function(e) {
                                         if (e)
                                             for (var t = 0, a = Object.entries(e); t < a.length; t++) {
                                                 if (se(Object(R.a)(a[t], 2)[1])) return !0
                                             }
                                         return !1
                                     }(null === j || void 0 === j || null === (a = j.params) || void 0 === a ? void 0 : a.params),
                                     isPresentation: void 0 !== j.output && "slides" === j.output,
                                     notebookParseErrors: j.errors,
                                     continuousUpdate: null === j || void 0 === j || null === (o = j.params) || void 0 === o ? void 0 : o.continuous_update,
-                                    staticNotebook: null === j || void 0 === j || null === (i = j.params) || void 0 === i ? void 0 : i.static_notebook,
+                                    staticNotebook: null === j || void 0 === j || null === (r = j.params) || void 0 === r ? void 0 : r.static_notebook,
                                     allowDownload: function() {
                                         var e, t;
                                         return void 0 === j || null === j || (void 0 === (null === j || void 0 === j || null === (e = j.params) || void 0 === e ? void 0 : e.allow_download) || null === (null === j || void 0 === j || null === (t = j.params) || void 0 === t ? void 0 : t.allow_download) || j.params.allow_download)
                                     }()
-                                }), !S && Object(_.jsx)("div", {
-                                    children: Object(_.jsx)("button", {
+                                }), !S && Object(E.jsx)("div", {
+                                    children: Object(E.jsx)("button", {
                                         className: "btn btn-sm  btn-outline-primary",
                                         type: "button",
                                         style: {
                                             position: "absolute",
                                             top: b ? "5px" : "50px",
                                             left: "5px",
                                             zIndex: "100"
                                         },
                                         onClick: function() {
                                             return p(V(!0))
                                         },
                                         "data-toggle": "tooltip",
                                         "data-placement": "right",
                                         title: "Show sidebar",
-                                        children: Object(_.jsx)("i", {
+                                        children: Object(E.jsx)("i", {
                                             className: "fa fa-chevron-right",
                                             "aria-hidden": "true"
                                         })
                                     })
-                                }), J && Object(_.jsx)(ja, {
+                                }), J && Object(E.jsx)(ja, {
                                     slug: j.slug,
                                     widgetsParams: null === j || void 0 === j || null === (c = j.params) || void 0 === c ? void 0 : c.params,
-                                    notebookPath: L,
+                                    notebookPath: W,
                                     columnsWidth: S ? 9 : 12,
                                     taskSessionId: v.session_id
-                                }), Object(_.jsx)(ua, {
+                                }), Object(E.jsx)(ua, {
                                     appView: O,
                                     loadingState: h,
-                                    notebookPath: L,
+                                    notebookPath: W,
                                     errorMsg: H,
-                                    waiting: M(),
+                                    waiting: L(),
                                     watchMode: U(),
                                     displayEmbed: b,
                                     username: w,
                                     slidesHash: N,
                                     columnsWidth: S ? 9 : 12,
                                     isPresentation: void 0 !== j.output && "slides" === j.output,
                                     fullScreen: function() {
                                         var e, t;
                                         return void 0 === j || null === j || (void 0 === (null === j || void 0 === j || null === (e = j.params) || void 0 === e ? void 0 : e.full_screen) || null === (null === j || void 0 === j || null === (t = j.params) || void 0 === t ? void 0 : t.full_screen) || j.params.full_screen)
                                     }()
-                                }), "files" === O && Object(_.jsx)(ba, {
+                                }), "files" === O && Object(E.jsx)(ba, {
                                     files: g,
                                     filesState: y,
-                                    waiting: M()
+                                    waiting: L()
                                 })]
                             })
                         })]
-                    }), b && Object(_.jsx)(pa, {})]
+                    }), b && Object(E.jsx)(pa, {})]
                 })
             };
 
             function fa() {
-                var e = Object(i.q)().slug,
-                    t = Object(i.q)().embed,
+                var e = Object(r.q)().slug,
+                    t = Object(r.q)().embed,
                     a = !(!t || "embed" !== t);
-                return Object(_.jsx)(oa, {
-                    children: Object(_.jsx)(va, {
+                return Object(E.jsx)(oa, {
+                    children: Object(E.jsx)(va, {
                         isSingleApp: !1,
                         notebookSlug: e,
                         displayEmbed: a
                     })
                 })
             }
 
             function ma() {
-                return Object(_.jsx)("footer", {
+                return Object(E.jsx)("footer", {
                     className: "footer",
                     style: {
                         position: "absolute",
                         bottom: "0",
                         width: "100%",
                         height: "40px",
                         lineHeight: "40px",
                         backgroundColor: "#f5f5f5",
                         borderTop: "1px solid #e5e5e5"
                     },
-                    children: Object(_.jsxs)("div", {
+                    children: Object(E.jsxs)("div", {
                         className: "container",
-                        children: [Object(_.jsxs)("span", {
+                        children: [Object(E.jsxs)("span", {
                             className: "text-muted",
                             style: {
                                 color: "gray"
                             },
-                            children: ["Mercury \xa9", " ", Object(_.jsx)("a", {
+                            children: ["Mercury \xa9", " ", Object(E.jsx)("a", {
                                 style: {
                                     textDecoration: "none",
                                     color: "gray"
                                 },
                                 href: "https://mljar.com",
                                 target: "_blank",
                                 rel: "noreferrer",
                                 children: "MLJAR"
                             })]
-                        }), Object(_.jsxs)("span", {
+                        }), Object(E.jsxs)("span", {
                             className: "text-muted",
                             style: {
                                 float: "right"
                             },
-                            children: [Object(_.jsx)("a", {
+                            children: [Object(E.jsx)("a", {
                                 style: {
                                     textDecoration: "none",
                                     color: "gray"
                                 },
                                 href: "https://github.com/mljar/mercury",
                                 target: "_blank",
                                 rel: "noreferrer",
                                 children: "Mercury"
-                            }), " ", Object(_.jsx)("i", {
+                            }), " ", Object(E.jsx)("i", {
                                 className: "fa fa-github",
                                 "aria-hidden": "true"
                             })]
                         })]
                     })
                 })
             }
 
             function xa(e) {
                 var t = e.isSitePublic,
                     a = e.username;
-                return Object(_.jsx)("header", {
+                return Object(E.jsx)("header", {
                     className: "navbar navbar-dark sticky-top bg-dark p-0",
-                    children: Object(_.jsxs)("div", {
+                    children: Object(E.jsxs)("div", {
                         className: "row",
                         style: {
                             width: "100%",
                             paddingRight: "0px"
                         },
-                        children: [Object(_.jsx)("div", {
+                        children: [Object(E.jsx)("div", {
                             className: "col-4"
-                        }), Object(_.jsx)("div", {
+                        }), Object(E.jsx)("div", {
                             className: "col-4 text-center",
-                            children: Object(_.jsx)("a", {
+                            children: Object(E.jsx)("a", {
                                 href: "/",
-                                children: Object(_.jsx)("img", {
+                                children: Object(E.jsx)("img", {
                                     alt: "Mercury",
                                     src: "/static/mercury_logo.svg",
                                     style: {
                                         height: "40px"
                                     }
                                 })
                             })
-                        }), Object(_.jsxs)("div", {
+                        }), Object(E.jsxs)("div", {
                             className: "col-4",
                             style: {
                                 marginRight: "0px",
                                 paddingRight: "0px"
                             },
-                            children: [!t && "" === a && Object(_.jsx)(F, {}), "" !== a && Object(_.jsx)(A, {
+                            children: [!t && "" === a && Object(E.jsx)(F, {}), "" !== a && Object(E.jsx)(A, {
                                 username: a
                             })]
                         })]
                     })
                 })
             }
 
             function Oa() {
-                var e = Object(r.b)(),
+                var e = Object(i.b)(),
                     t = Object(n.useState)(""),
                     a = Object(R.a)(t, 2),
                     o = a[0],
-                    i = a[1],
+                    r = a[1],
                     c = Object(n.useState)(""),
                     l = Object(R.a)(c, 2),
                     b = l[0],
                     j = l[1],
                     h = Object(n.useState)(""),
                     v = Object(R.a)(h, 2),
                     f = v[0],
                     m = v[1],
-                    x = Object(r.c)(T),
-                    O = Object(r.c)(E),
-                    g = Object(r.c)(Nt);
+                    x = Object(i.c)(T),
+                    O = Object(i.c)(_),
+                    g = Object(i.c)(Nt);
                 return document.body.style.backgroundColor = "white", Object(n.useEffect)((function() {
                     e(function() {
                         var e = Object(u.a)(d.a.mark((function e(t) {
                             var a, n;
                             return d.a.wrap((function(e) {
                                 for (;;) switch (e.prev = e.next) {
                                     case 0:
@@ -2930,132 +3166,132 @@
                                 [0, 9]
                             ])
                         })));
                         return function(t) {
                             return e.apply(this, arguments)
                         }
                     }())
-                }), [e]), Object(_.jsxs)("div", {
+                }), [e]), Object(E.jsxs)("div", {
                     className: "App",
-                    children: [Object(_.jsx)(xa, {
+                    children: [Object(E.jsx)(xa, {
                         isSitePublic: g,
                         username: x
-                    }), Object(_.jsx)("div", {
+                    }), Object(E.jsx)("div", {
                         className: "container",
-                        children: Object(_.jsxs)("div", {
+                        children: Object(E.jsxs)("div", {
                             className: "mx-auto",
                             style: {
                                 width: "700px"
                             },
-                            children: [Object(_.jsxs)("div", {
+                            children: [Object(E.jsxs)("div", {
                                 className: "row",
                                 style: {
                                     marginTop: "40px"
                                 },
-                                children: [Object(_.jsxs)("h2", {
-                                    children: [Object(_.jsx)("i", {
+                                children: [Object(E.jsxs)("h2", {
+                                    children: [Object(E.jsx)("i", {
                                         className: "fa fa-user",
                                         "aria-hidden": "true"
                                     }), " Account"]
-                                }), Object(_.jsxs)("form", {
-                                    children: [Object(_.jsxs)("div", {
+                                }), Object(E.jsxs)("form", {
+                                    children: [Object(E.jsxs)("div", {
                                         className: "mb-3",
-                                        children: [Object(_.jsx)("label", {
+                                        children: [Object(E.jsx)("label", {
                                             className: "form-label",
                                             children: "Username"
-                                        }), Object(_.jsx)("input", {
+                                        }), Object(E.jsx)("input", {
                                             className: "form-control",
                                             value: O.username,
                                             disabled: !0
                                         })]
-                                    }), Object(_.jsxs)("div", {
+                                    }), Object(E.jsxs)("div", {
                                         className: "mb-3",
-                                        children: [Object(_.jsx)("label", {
+                                        children: [Object(E.jsx)("label", {
                                             className: "form-label",
                                             children: "First name"
-                                        }), Object(_.jsx)("input", {
+                                        }), Object(E.jsx)("input", {
                                             className: "form-control",
                                             value: O.first_name,
                                             disabled: !0
                                         })]
-                                    }), Object(_.jsxs)("div", {
+                                    }), Object(E.jsxs)("div", {
                                         className: "mb-3",
-                                        children: [Object(_.jsx)("label", {
+                                        children: [Object(E.jsx)("label", {
                                             className: "form-label",
                                             children: "Last name"
-                                        }), Object(_.jsx)("input", {
+                                        }), Object(E.jsx)("input", {
                                             className: "form-control",
                                             value: O.last_name,
                                             disabled: !0
                                         })]
-                                    }), Object(_.jsxs)("div", {
+                                    }), Object(E.jsxs)("div", {
                                         className: "mb-3",
-                                        children: [Object(_.jsx)("label", {
+                                        children: [Object(E.jsx)("label", {
                                             className: "form-label",
                                             children: "Email address"
-                                        }), Object(_.jsx)("input", {
+                                        }), Object(E.jsx)("input", {
                                             className: "form-control",
                                             value: O.email,
                                             disabled: !0
                                         })]
                                     })]
                                 })]
-                            }), Object(_.jsx)("hr", {}), Object(_.jsxs)("div", {
+                            }), Object(E.jsx)("hr", {}), Object(E.jsxs)("div", {
                                 className: "row",
-                                children: [Object(_.jsxs)("h2", {
-                                    children: [Object(_.jsx)("i", {
+                                children: [Object(E.jsxs)("h2", {
+                                    children: [Object(E.jsx)("i", {
                                         className: "fa fa-key",
                                         "aria-hidden": "true"
                                     }), " Change password"]
-                                }), Object(_.jsxs)("div", {
-                                    children: [Object(_.jsxs)("div", {
+                                }), Object(E.jsxs)("div", {
+                                    children: [Object(E.jsxs)("div", {
                                         className: "mb-3",
-                                        children: [Object(_.jsx)("label", {
+                                        children: [Object(E.jsx)("label", {
                                             className: "form-label",
                                             children: "Old password"
-                                        }), Object(_.jsx)("input", {
+                                        }), Object(E.jsx)("input", {
                                             type: "password",
                                             className: "form-control",
                                             value: o,
                                             onChange: function(e) {
-                                                return i(e.target.value)
+                                                return r(e.target.value)
                                             }
                                         })]
-                                    }), Object(_.jsxs)("div", {
+                                    }), Object(E.jsxs)("div", {
                                         className: "mb-3",
-                                        children: [Object(_.jsx)("label", {
+                                        children: [Object(E.jsx)("label", {
                                             className: "form-label",
                                             children: "New password"
-                                        }), Object(_.jsx)("input", {
+                                        }), Object(E.jsx)("input", {
                                             type: "password",
                                             className: "form-control",
                                             value: b,
                                             onChange: function(e) {
                                                 return j(e.target.value)
                                             }
                                         })]
-                                    }), Object(_.jsxs)("div", {
+                                    }), Object(E.jsxs)("div", {
                                         className: "mb-3",
-                                        children: [Object(_.jsx)("label", {
+                                        children: [Object(E.jsx)("label", {
                                             className: "form-label",
                                             children: "Repeat new password"
-                                        }), Object(_.jsx)("input", {
+                                        }), Object(E.jsx)("input", {
                                             type: "password",
                                             className: "form-control",
                                             value: f,
                                             onChange: function(e) {
                                                 return m(e.target.value)
                                             }
                                         })]
-                                    }), Object(_.jsx)("div", {
+                                    }), Object(E.jsx)("div", {
                                         className: "mb-3",
                                         style: {
                                             paddingBottom: "50px"
                                         },
-                                        children: Object(_.jsx)("button", {
+                                        children: Object(E.jsx)("button", {
                                             className: "btn btn-primary",
                                             onClick: function() {
                                                 return e(function(e, t, a) {
                                                     return function() {
                                                         var n = Object(u.a)(d.a.mark((function n(o) {
                                                             return d.a.wrap((function(n) {
                                                                 for (;;) switch (n.prev = n.next) {
@@ -3087,15 +3323,15 @@
                                             disabled: "" === o || "" === b || "" === f,
                                             children: "Change password"
                                         })
                                     })]
                                 })]
                             })]
                         })
-                    }), Object(_.jsx)(ma, {})]
+                    }), Object(E.jsx)(ma, {})]
                 })
             }
             var ga = Object(b.b)({
                     name: "version",
                     initialState: {
                         fetchingIsPro: !0,
                         isPro: !1,
@@ -3115,43 +3351,43 @@
                 wa = ga.actions,
                 ka = (wa.setVersion, wa.setWelcome),
                 Na = function(e) {
                     return e.version.welcome
                 };
 
             function Sa() {
-                var e = Object(r.b)(),
-                    t = Object(r.c)(Ce),
-                    a = Object(r.c)(Te),
-                    o = Object(r.c)(Na),
-                    i = Object(r.c)(T),
-                    c = Object(r.c)(C),
+                var e = Object(i.b)(),
+                    t = Object(i.c)(Ce),
+                    a = Object(i.c)(Te),
+                    o = Object(i.c)(Na),
+                    r = Object(i.c)(T),
+                    c = Object(i.c)(C),
                     l = Object(n.useState)(""),
                     b = Object(R.a)(l, 2),
                     p = b[0],
                     j = b[1],
-                    h = Object(r.c)(wt),
-                    v = Object(r.c)(Nt),
-                    f = Object(r.c)(kt);
+                    h = Object(i.c)(wt),
+                    v = Object(i.c)(Nt),
+                    f = Object(i.c)(kt);
                 Object(n.useEffect)((function() {
                     void 0 !== h && (e(function(e) {
                         return function() {
                             var t = Object(u.a)(d.a.mark((function t(a) {
-                                var n, o, r, i;
+                                var n, o, i, r;
                                 return d.a.wrap((function(t) {
                                     for (;;) switch (t.prev = t.next) {
                                         case 0:
                                             return t.prev = 0, a(fe("")), a(je("loading")), a(qe()), n = "/api/v1/".concat(e, "/notebooks/"), t.next = 7, s.a.get(n);
                                         case 7:
-                                            o = t.sent, r = o.data, i = r.map((function(e) {
+                                            o = t.sent, i = o.data, r = i.map((function(e) {
                                                 var t = JSON.parse(e.params);
                                                 return Object(D.a)(Object(D.a)({}, e), {}, {
                                                     params: t
                                                 })
-                                            })), a(pe(i)), a(je("loaded")), t.next = 18;
+                                            })), a(pe(r)), a(je("loaded")), t.next = 18;
                                             break;
                                         case 14:
                                             t.prev = 14, t.t0 = t.catch(0), a(je("error")), console.error("Problem during loading recent notebooks. ".concat(t.t0));
                                         case 18:
                                         case "end":
                                             return t.stop()
                                     }
@@ -3162,21 +3398,21 @@
                             return function(e) {
                                 return t.apply(this, arguments)
                             }
                         }()
                     }(h)), void 0 !== f && "" !== f || e(function(e) {
                         return function() {
                             var t = Object(u.a)(d.a.mark((function t(a) {
-                                var n, o, r;
+                                var n, o, i;
                                 return d.a.wrap((function(t) {
                                     for (;;) switch (t.prev = t.next) {
                                         case 0:
                                             return t.prev = 0, n = "/api/v1/".concat(e, "/welcome/"), t.next = 4, s.a.get(n);
                                         case 4:
-                                            o = t.sent, r = o.data, a(ka(r.msg)), t.next = 12;
+                                            o = t.sent, i = o.data, a(ka(i.msg)), t.next = 12;
                                             break;
                                         case 9:
                                             t.prev = 9, t.t0 = t.catch(0), console.log("Problem during loading Mercury welcome message. ".concat(t.t0));
                                         case 12:
                                         case "end":
                                             return t.stop()
                                     }
@@ -3190,170 +3426,170 @@
                         }()
                     }(h)))
                 }), [e, h, c, f]);
                 var m = function(e, t) {
                         return null !== e && void 0 !== e ? e.slice(0, t) + (e.length > t ? " ..." : "") : ""
                     },
                     x = t.map((function(e, t) {
-                        return Object(_.jsx)("div", {
+                        return Object(E.jsx)("div", {
                             className: "col-md-4",
                             style: {
                                 paddingBottom: "20px"
                             },
-                            children: Object(_.jsxs)("div", {
+                            children: Object(E.jsxs)("div", {
                                 className: "card",
-                                children: [Object(_.jsx)("div", {
+                                children: [Object(E.jsx)("div", {
                                     style: {
                                         height: "200px",
                                         width: "100%",
                                         padding: "1px",
                                         overflow: "hidden"
                                     },
-                                    children: Object(_.jsx)("iframe", {
+                                    children: Object(E.jsx)("iframe", {
                                         className: "thumbnailIframe",
                                         width: "200%",
                                         height: 800,
                                         src: "".concat(e.default_view_path),
                                         title: "display",
                                         scrolling: "no"
                                     })
-                                }), Object(_.jsxs)("a", {
+                                }), Object(E.jsxs)("a", {
                                     href: "/app/".concat(e.slug),
                                     style: {
                                         textDecoration: "none",
                                         color: "black"
                                     },
                                     className: "title-card",
                                     onMouseEnter: function() {
                                         j(e.slug)
                                     },
                                     onMouseLeave: function() {
                                         j("")
                                     },
-                                    children: [Object(_.jsxs)("div", {
+                                    children: [Object(E.jsxs)("div", {
                                         className: "card-body",
                                         style: {
                                             borderTop: "1px solid rgba(0,0,0,0.1)",
                                             height: "110px"
                                         },
-                                        children: [Object(_.jsx)("h5", {
+                                        children: [Object(E.jsx)("h5", {
                                             className: "card-title",
                                             children: m(e.title, 40)
-                                        }), Object(_.jsx)("p", {
+                                        }), Object(E.jsx)("p", {
                                             className: "card-text",
                                             children: m(e.params.description, 100)
                                         })]
-                                    }), p === e.slug && Object(_.jsx)("button", {
+                                    }), p === e.slug && Object(E.jsx)("button", {
                                         className: "btn btn-outline-primary",
                                         type: "button",
                                         style: {
                                             zIndex: "101",
                                             border: "none",
                                             margin: "5px",
                                             position: "absolute",
                                             right: "0px",
                                             bottom: "0px"
                                         },
                                         "data-toggle": "tooltip",
                                         "data-placement": "right",
                                         title: "Open ".concat(e.title),
-                                        children: Object(_.jsx)("i", {
+                                        children: Object(E.jsx)("i", {
                                             className: "fa fa-chevron-right",
                                             "aria-hidden": "true"
                                         })
                                     })]
                                 })]
                             })
                         }, "notebook-".concat(e.id, "}"))
                     }));
                 document.body.style.backgroundColor = "white";
                 var O = f;
-                return void 0 !== O && "" !== O || (O = o), Object(_.jsxs)("div", {
+                return void 0 !== O && "" !== O || (O = o), Object(E.jsxs)("div", {
                     className: "App",
-                    children: [Object(_.jsx)(xa, {
+                    children: [Object(E.jsx)(xa, {
                         isSitePublic: v,
-                        username: i
-                    }), Object(_.jsxs)("div", {
+                        username: r
+                    }), Object(E.jsxs)("div", {
                         className: "container",
                         style: {
                             paddingBottom: "50px"
                         },
-                        children: ["" === O && Object(_.jsx)("h1", {
+                        children: ["" === O && Object(E.jsx)("h1", {
                             style: {
                                 padding: "30px",
                                 textAlign: "center"
                             },
                             children: "Welcome!"
-                        }), "" !== O && Object(_.jsx)("div", {
+                        }), "" !== O && Object(E.jsx)("div", {
                             style: {
                                 paddingTop: "20px",
                                 paddingBottom: "10px"
                             },
-                            children: Object(_.jsx)(Rt.a, {
-                                rehypePlugins: [Ft.a, _t.a, At.a, It.a],
+                            children: Object(E.jsx)(Rt.a, {
+                                rehypePlugins: [Ft.a, Et.a, At.a, Mt.a],
                                 children: O
                             })
-                        }), Object(_.jsxs)("div", {
+                        }), Object(E.jsxs)("div", {
                             className: "row",
-                            children: ["loading" === a && Object(_.jsx)("p", {
+                            children: ["loading" === a && Object(E.jsx)("p", {
                                 children: "Loading notebooks. Please wait ..."
-                            }), "loaded" === a && 0 === t.length && Object(_.jsx)("div", {
-                                children: Object(_.jsx)("p", {
+                            }), "loaded" === a && 0 === t.length && Object(E.jsx)("div", {
+                                children: Object(E.jsx)("p", {
                                     children: "There are no notebooks available."
                                 })
-                            }), "error" === a && Object(_.jsx)("p", {
+                            }), "error" === a && Object(E.jsx)("p", {
                                 children: "Problem while loading notebooks. Please try again later or contact Mercury administrator."
                             }), x]
                         })]
-                    }), Object(_.jsx)(ma, {})]
+                    }), Object(E.jsx)(ma, {})]
                 })
             }
 
             function Pa() {
-                var e = Object(r.b)(),
-                    t = Object(i.o)(),
+                var e = Object(i.b)(),
+                    t = Object(r.o)(),
                     a = Object(n.useState)(""),
                     o = Object(R.a)(a, 2),
                     c = o[0],
                     l = o[1],
                     b = Object(n.useState)(""),
                     j = Object(R.a)(b, 2),
                     h = j[0],
                     v = j[1],
-                    f = Object(r.c)(Nt);
+                    f = Object(i.c)(Nt);
                 document.body.style.backgroundColor = "#f5f5f5";
                 var m = "/",
-                    x = Object(i.m)();
+                    x = Object(r.m)();
                 if (x && x.state) {
                     var O = x.state.from;
                     m = O.pathname
                 }
-                return Object(_.jsxs)("div", {
+                return Object(E.jsxs)("div", {
                     className: "App",
-                    children: [Object(_.jsx)(xa, {
+                    children: [Object(E.jsx)(xa, {
                         isSitePublic: f,
                         username: ""
-                    }), Object(_.jsxs)("div", {
+                    }), Object(E.jsxs)("div", {
                         className: "div-signin text-center",
-                        children: [Object(_.jsxs)("form", {
+                        children: [Object(E.jsxs)("form", {
                             className: "form-signin",
                             onSubmit: function(a) {
                                 a.preventDefault(), a.stopPropagation(), e(function(e, t, a, n) {
                                     return function() {
-                                        var o = Object(u.a)(d.a.mark((function o(r) {
-                                            var i, c, l, u, b, j;
+                                        var o = Object(u.a)(d.a.mark((function o(i) {
+                                            var r, c, l, u, b, j;
                                             return d.a.wrap((function(o) {
                                                 for (;;) switch (o.prev = o.next) {
                                                     case 0:
                                                         return o.prev = 0, o.next = 4, s.a.post("/api/v1/auth/login/", {
                                                             email: e,
                                                             password: t
                                                         });
                                                     case 4:
-                                                        i = o.sent, c = i.data, r(N(c.key)), r(S(e.split("@")[0])), p.b.success("Log in successfull"), n(a), o.next = 16;
+                                                        r = o.sent, c = r.data, i(N(c.key)), i(S(e.split("@")[0])), p.b.success("Log in successfull"), n(a), o.next = 16;
                                                         break;
                                                     case 12:
                                                         o.prev = 12, o.t0 = o.catch(0), "Network Error" === (null === (l = o.t0) || void 0 === l ? void 0 : l.message) ? p.b.info("Problem with server connection") : (b = null === (u = l.response) || void 0 === u ? void 0 : u.data, j = "Problem during authentication. ", void 0 !== b.non_field_errors && (j += b.non_field_errors), p.b.error(j));
                                                     case 16:
                                                     case "end":
                                                         return o.stop()
                                                 }
@@ -3363,328 +3599,328 @@
                                         })));
                                         return function(e) {
                                             return o.apply(this, arguments)
                                         }
                                     }()
                                 }(c, h, m, t))
                             },
-                            children: [Object(_.jsx)("h3", {
+                            children: [Object(E.jsx)("h3", {
                                 className: "h3 mb-3 font-weight-normal",
                                 children: "Please sign in"
-                            }), Object(_.jsx)("label", {
+                            }), Object(E.jsx)("label", {
                                 className: "sr-only",
                                 children: "Email"
-                            }), Object(_.jsx)("input", {
+                            }), Object(E.jsx)("input", {
                                 type: "email",
                                 id: "inputEmail",
                                 className: "form-control",
                                 placeholder: "Email",
                                 value: c,
                                 onChange: function(e) {
                                     l(e.target.value)
                                 },
                                 required: !0
-                            }), Object(_.jsx)("label", {
+                            }), Object(E.jsx)("label", {
                                 className: "sr-only",
                                 children: "Password"
-                            }), Object(_.jsx)("input", {
+                            }), Object(E.jsx)("input", {
                                 type: "password",
                                 id: "inputPassword",
                                 className: "form-control",
                                 placeholder: "Password",
                                 value: h,
                                 onChange: function(e) {
                                     v(e.target.value)
                                 },
                                 required: !0
-                            }), Object(_.jsxs)("button", {
+                            }), Object(E.jsxs)("button", {
                                 className: "btn btn-lg btn-primary btn-block",
                                 type: "submit",
                                 style: {
                                     margin: "5px"
                                 },
                                 disabled: "" === c || "" === h,
-                                children: [Object(_.jsx)("i", {
+                                children: [Object(E.jsx)("i", {
                                     className: "fa fa-sign-in",
                                     "aria-hidden": "true"
                                 }), " Log in"]
                             })]
-                        }), Object(_.jsx)("div", {
+                        }), Object(E.jsx)("div", {
                             className: "mx-auto",
                             style: {
                                 width: "400px",
                                 marginTop: "40px"
                             },
-                            children: Object(_.jsxs)("p", {
+                            children: Object(E.jsxs)("p", {
                                 className: "text-muted",
-                                children: ["No account? ", Object(_.jsx)("br", {}), " Please contact administrator to create account for you."]
+                                children: ["No account? ", Object(E.jsx)("br", {}), " Please contact administrator to create account for you."]
                             })
                         })]
-                    }), Object(_.jsx)(ma, {})]
+                    }), Object(E.jsx)(ma, {})]
                 })
             }
 
             function Ca() {
-                return Object(_.jsxs)("div", {
+                return Object(E.jsxs)("div", {
                     className: "App",
-                    children: [Object(_.jsx)(xa, {
+                    children: [Object(E.jsx)(xa, {
                         isSitePublic: !0,
                         username: ""
-                    }), Object(_.jsxs)("div", {
+                    }), Object(E.jsxs)("div", {
                         style: {
                             width: "100%",
                             maxWidth: "500px",
                             padding: "15px",
                             margin: "0 auto"
                         },
-                        children: [Object(_.jsx)("h3", {
+                        children: [Object(E.jsx)("h3", {
                             children: "Lost connection"
-                        }), Object(_.jsx)("p", {
+                        }), Object(E.jsx)("p", {
                             children: "App lost connection to the server. Please try again in a moment or contact administrator."
                         })]
-                    }), Object(_.jsx)(ma, {})]
+                    }), Object(E.jsx)(ma, {})]
                 })
             }
 
             function Ta() {
-                return Object(_.jsxs)("div", {
+                return Object(E.jsxs)("div", {
                     className: "App",
-                    children: [Object(_.jsx)(xa, {
+                    children: [Object(E.jsx)(xa, {
                         isSitePublic: !0,
                         username: ""
-                    }), Object(_.jsxs)("div", {
+                    }), Object(E.jsxs)("div", {
                         style: {
                             width: "100%",
                             maxWidth: "500px",
                             padding: "15px",
                             margin: "0 auto"
                         },
-                        children: [Object(_.jsx)("h3", {
+                        children: [Object(E.jsx)("h3", {
                             children: "Access forbidden"
-                        }), Object(_.jsxs)("p", {
-                            children: ["Please ", Object(_.jsx)(c.b, {
+                        }), Object(E.jsxs)("p", {
+                            children: ["Please ", Object(E.jsx)(c.b, {
                                 to: "/login",
                                 children: "login"
                             }), " to access site."]
                         })]
-                    }), Object(_.jsx)(ma, {})]
+                    }), Object(E.jsx)(ma, {})]
                 })
             }
 
-            function Ea() {
-                return Object(_.jsxs)("div", {
+            function _a() {
+                return Object(E.jsxs)("div", {
                     className: "App",
-                    children: [Object(_.jsx)(xa, {
+                    children: [Object(E.jsx)(xa, {
                         isSitePublic: !0,
                         username: ""
-                    }), Object(_.jsx)("div", {
+                    }), Object(E.jsx)("div", {
                         style: {
                             width: "100%",
                             maxWidth: "500px",
                             padding: "15px",
                             margin: "0 auto"
                         },
-                        children: Object(_.jsx)("p", {
+                        children: Object(E.jsx)("p", {
                             style: {
                                 color: "gray"
                             },
                             children: "Please wait. Loading site ..."
                         })
-                    }), Object(_.jsx)(ma, {})]
+                    }), Object(E.jsx)(ma, {})]
                 })
             }
 
             function Ra() {
-                return Object(_.jsxs)("div", {
+                return Object(E.jsxs)("div", {
                     className: "App",
-                    children: [Object(_.jsx)(xa, {
+                    children: [Object(E.jsx)(xa, {
                         isSitePublic: !0,
                         username: ""
-                    }), Object(_.jsxs)("div", {
+                    }), Object(E.jsxs)("div", {
                         style: {
                             width: "100%",
                             maxWidth: "500px",
                             padding: "15px",
                             margin: "0 auto"
                         },
-                        children: [Object(_.jsx)("h3", {
+                        children: [Object(E.jsx)("h3", {
                             children: "Network Error"
-                        }), Object(_.jsx)("p", {
+                        }), Object(E.jsx)("p", {
                             children: "Please check if you have internet connection and server is running. In case of problems, please contact administrator."
                         })]
-                    }), Object(_.jsx)(ma, {})]
+                    }), Object(E.jsx)(ma, {})]
                 })
             }
 
-            function _a() {
-                return Object(_.jsxs)("div", {
+            function Ea() {
+                return Object(E.jsxs)("div", {
                     className: "App",
-                    children: [Object(_.jsx)(xa, {
+                    children: [Object(E.jsx)(xa, {
                         isSitePublic: !0,
                         username: ""
-                    }), Object(_.jsxs)("div", {
+                    }), Object(E.jsxs)("div", {
                         style: {
                             width: "100%",
                             maxWidth: "500px",
                             padding: "15px",
                             margin: "0 auto"
                         },
-                        children: [Object(_.jsx)("h3", {
+                        children: [Object(E.jsx)("h3", {
                             children: "Site does not exist"
-                        }), Object(_.jsx)("p", {
+                        }), Object(E.jsx)("p", {
                             children: "We can't find site you are looking for. Please make sure that URL address is correct."
                         })]
-                    }), Object(_.jsx)(ma, {})]
+                    }), Object(E.jsx)(ma, {})]
                 })
             }
 
             function Fa() {
-                return Object(_.jsxs)("div", {
+                return Object(E.jsxs)("div", {
                     className: "App",
-                    children: [Object(_.jsx)(xa, {
+                    children: [Object(E.jsx)(xa, {
                         isSitePublic: !0,
                         username: ""
-                    }), Object(_.jsxs)("div", {
+                    }), Object(E.jsxs)("div", {
                         style: {
                             width: "100%",
                             maxWidth: "500px",
                             padding: "15px",
                             margin: "0 auto"
                         },
-                        children: [Object(_.jsx)("h3", {
+                        children: [Object(E.jsx)("h3", {
                             children: "Please refresh"
-                        }), Object(_.jsx)("p", {
+                        }), Object(E.jsx)("p", {
                             children: "Please try to refresh the website ..."
                         })]
-                    }), Object(_.jsx)(ma, {})]
+                    }), Object(E.jsx)(ma, {})]
                 })
             }
 
             function Aa() {
-                return Object(_.jsxs)("div", {
+                return Object(E.jsxs)("div", {
                     className: "App",
-                    children: [Object(_.jsx)(xa, {
+                    children: [Object(E.jsx)(xa, {
                         isSitePublic: !0,
                         username: ""
-                    }), Object(_.jsxs)("div", {
+                    }), Object(E.jsxs)("div", {
                         style: {
                             width: "100%",
                             maxWidth: "500px",
                             padding: "15px",
                             margin: "0 auto"
                         },
-                        children: [Object(_.jsx)("h3", {
+                        children: [Object(E.jsx)("h3", {
                             children: "Site not ready"
-                        }), Object(_.jsx)("p", {
+                        }), Object(E.jsx)("p", {
                             children: "Your site is not ready yet. Please refresh page in a while or check the dashboard."
-                        }), Object(_.jsx)("button", {
+                        }), Object(E.jsx)("button", {
                             className: "btn btn-success",
                             onClick: function() {
                                 return window.location.reload()
                             },
                             children: "Refresh"
                         })]
-                    }), Object(_.jsx)(ma, {})]
+                    }), Object(E.jsx)(ma, {})]
                 })
             }
 
-            function Ia(e) {
+            function Ma(e) {
                 var t = e.children,
-                    a = Object(r.c)(C),
-                    o = Object(r.c)(Nt),
-                    s = Object(i.m)(),
-                    c = Object(r.b)(),
-                    l = Object(r.c)(yt);
+                    a = Object(i.c)(C),
+                    o = Object(i.c)(Nt),
+                    s = Object(r.m)(),
+                    c = Object(i.b)(),
+                    l = Object(i.c)(yt);
                 return Object(n.useEffect)((function() {
                     c(St())
-                }), [c]), l === ct.Unknown ? Object(_.jsx)(Ea, {}) : l === ct.NotFound ? Object(_.jsx)(_a, {}) : l === ct.NotReady ? Object(_.jsx)(Aa, {}) : l === ct.AccessForbidden ? Object(_.jsx)(Ta, {}) : l === ct.NetworkError ? Object(_.jsx)(Ra, {}) : l === ct.PleaseRefresh ? Object(_.jsx)(Fa, {}) : l === ct.LostConnection ? (window.location.reload(), Object(_.jsx)(Ca, {})) : o || a ? t : Object(_.jsx)(i.a, {
+                }), [c]), l === ct.Unknown ? Object(E.jsx)(_a, {}) : l === ct.NotFound ? Object(E.jsx)(Ea, {}) : l === ct.NotReady ? Object(E.jsx)(Aa, {}) : l === ct.AccessForbidden ? Object(E.jsx)(Ta, {}) : l === ct.NetworkError ? Object(E.jsx)(Ra, {}) : l === ct.PleaseRefresh ? Object(E.jsx)(Fa, {}) : l === ct.LostConnection ? (window.location.reload(), Object(E.jsx)(Ca, {})) : o || a ? t : Object(E.jsx)(r.a, {
                     to: "/login",
                     state: {
                         from: s
                     },
                     replace: !0
                 })
             }
 
             function Da(e) {
                 var t = e.children;
-                return Object(_.jsx)(_.Fragment, {
+                return Object(E.jsx)(E.Fragment, {
                     children: t
                 })
             }
 
-            function Wa() {
-                return Object(_.jsx)(Ia, {
-                    children: Object(_.jsx)(_.Fragment, {
-                        children: Object(_.jsx)(i.b, {})
+            function Ia() {
+                return Object(E.jsx)(Ma, {
+                    children: Object(E.jsx)(E.Fragment, {
+                        children: Object(E.jsx)(r.b, {})
                     })
                 })
             }
 
-            function Ma() {
-                var e = Object(r.b)();
+            function La() {
+                var e = Object(i.b)();
                 return Object(n.useEffect)((function() {
                     f(), localStorage.getItem("token") && e(N(localStorage.getItem("token"))), localStorage.getItem("username") && e(S(localStorage.getItem("username"))), e(St())
-                }), []), Object(_.jsx)(c.a, {
-                    children: Object(_.jsx)(Da, {
-                        children: Object(_.jsxs)(i.e, {
-                            children: [Object(_.jsxs)(i.c, {
+                }), []), Object(E.jsx)(c.a, {
+                    children: Object(E.jsx)(Da, {
+                        children: Object(E.jsxs)(r.e, {
+                            children: [Object(E.jsxs)(r.c, {
                                 path: "/",
-                                element: Object(_.jsx)(Wa, {}),
-                                children: [Object(_.jsx)(i.c, {
+                                element: Object(E.jsx)(Ia, {}),
+                                children: [Object(E.jsx)(r.c, {
                                     path: "/",
-                                    element: Object(_.jsx)(Sa, {})
-                                }), Object(_.jsx)(i.c, {
+                                    element: Object(E.jsx)(Sa, {})
+                                }), Object(E.jsx)(r.c, {
                                     path: "/app/:slug/:embed?",
-                                    element: Object(_.jsx)(fa, {})
-                                }), Object(_.jsx)(i.c, {
+                                    element: Object(E.jsx)(fa, {})
+                                }), Object(E.jsx)(r.c, {
                                     path: "/account",
-                                    element: Object(_.jsx)(Oa, {})
+                                    element: Object(E.jsx)(Oa, {})
                                 })]
-                            }), Object(_.jsx)(i.c, {
+                            }), Object(E.jsx)(r.c, {
                                 path: "/login",
-                                element: Object(_.jsx)(Pa, {})
+                                element: Object(E.jsx)(Pa, {})
                             })]
                         })
                     })
                 })
             }
             var Ua = function(e) {
                     var t = e.store;
                     e.history;
-                    return Object(_.jsx)(r.a, {
+                    return Object(E.jsx)(i.a, {
                         store: t,
-                        children: Object(_.jsx)(Ma, {})
+                        children: Object(E.jsx)(La, {})
                     })
                 },
-                La = a(15),
+                Wa = a(15),
                 Ha = a(171),
                 za = a(32);
             var Ba, Va = Object(Ha.a)(),
                 Ja = Object(za.b)({
                     notebooks: ue,
-                    tasks: Le,
+                    tasks: We,
                     version: ya,
                     app: U,
                     auth: w,
                     ws: Ut,
                     sites: mt
                 }),
-                Ka = Object(La.a)(Object(b.c)()),
+                Ka = Object(Wa.a)(Object(b.c)()),
                 qa = (a(285), a(286), a(288), a(289), a(290), a(291), a(292), a(293), Object(b.a)({
                     reducer: Ja,
                     middleware: Ka,
                     preloadedState: Ba
                 }));
             s.a.defaults.baseURL = "http://127.0.0.1:8000", document.addEventListener("DOMContentLoaded", (function() {
-                return Object(o.render)(Object(_.jsxs)("div", {
-                    children: [Object(_.jsx)(Ua, {
+                return Object(o.render)(Object(E.jsxs)("div", {
+                    children: [Object(E.jsx)(Ua, {
                         store: qa,
                         history: Va
-                    }), Object(_.jsx)(p.a, {
+                    }), Object(E.jsx)(p.a, {
                         position: "top-right",
                         autoClose: 3e3,
                         hideProgressBar: !0,
                         newestOnTop: !0,
                         closeOnClick: !0,
                         pauseOnHover: !0
                     })]
@@ -3692,8 +3928,8 @@
             }))
         }
     },
     [
         [295, 1, 2]
     ]
 ]);
-//# sourceMappingURL=main.b729f6a0.chunk.js.map
+//# sourceMappingURL=main.717ee96a.chunk.js.map
```

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/js/main.b729f6a0.chunk.js.map` & `mercury-2.2.0/mercury/frontend-dist/static/js/main.717ee96a.chunk.js.map`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8342272257023924%*

 * *Differences: {"'file'": "'static/js/main.717ee96a.chunk.js'",*

 * * "'mappings'": "'8QAIaA,EAAe,WACxB,IAAIC,EAAYC,eAAeC,QAAQ,aAKvC,OAJiB,MAAbF,IACAA,EAAYG,eACZF,eAAeG,QAAQ,YAAaJ,IAEjCA,GAGEK,EAAoB,SAACC,GACT,qBAAVA,GAAyBA,EAEhCC,IAAMC,SAASC,QAAQC,OAAvB,cAAiD,SAAWJ,SAGrDC,IAAMC,SAASC,QAAQC,OAAvB,eAIFC,EAAiB,SAACC,EAAaC,GACxCN,IACKO,IAAIF,EAAK,CACNG,aAAc,SAEjBC,MAAK,SAACC,GACHC,IAAaD,EAAIE,KAAMN,OCf/BO,EAAY,KACZC,aAAanB,QAAQ,WACvBkB,EAAYC,aAAanB,QAAQ,SACjCG,EAAkBe,IAWpB,IAAME,EAAe,CACnBhB,MAAOc,EACPG,SAAU,GACVC,KAAM,CACJC,GAAI […]*

```diff
@@ -1,10 +1,10 @@
 {
-    "file": "static/js/main.b729f6a0.chunk.js",
-    "mappings": "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",
+    "file": "static/js/main.717ee96a.chunk.js",
+    "mappings": "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",
     "names": [
         "getSessionId",
         "sessionId",
         "sessionStorage",
         "getItem",
         "uuidv4",
         "setItem",
@@ -452,66 +452,84 @@
         "WebSocket",
         "onopen",
         "onmessage",
         "onerror",
         "onclose",
         "Provider",
         "StatusBar",
+        "allowDownload",
+        "waiting",
+        "staticNotebook",
+        "notebookId",
+        "notebookPath",
+        "notebookTitle",
+        "runDownloadHTML",
+        "runDownloadPDF",
+        "widgetsValues",
+        "widgetsParams",
+        "showShareModal",
+        "setShowShareModal",
         "wsStatus",
         "LostConnection",
         "wifiColor",
         "workerColor",
         "Running",
         "Busy",
         "Missing",
+        "noUrlKeys",
+        "urlParams",
+        "entries",
+        "widgetParams",
+        "v",
+        "join",
+        "slice",
+        "paddingBottom",
         "xmlns",
         "fill",
         "viewBox",
         "d",
         "fillRule",
+        "strokeWidth",
+        "stroke",
+        "strokeLinecap",
+        "strokeLinejoin",
+        "cursor",
+        "notebook_id",
+        "notebook_path",
+        "job_id",
+        "exportToPDF",
+        "transform",
+        "aria-label",
+        "rel",
         "ButtonWidget",
         "selectedClass",
         "marginRight",
         "RunButton",
-        "waiting",
         "SideBar",
-        "notebookTitle",
-        "notebookId",
         "notebookSchedule",
         "taskCreatedAt",
-        "widgetsParams",
         "watchMode",
-        "notebookPath",
         "displayEmbed",
         "showFiles",
         "isPresentation",
         "notebookParseErrors",
-        "staticNotebook",
-        "allowDownload",
-        "widgetsValues",
         "useContext",
         "execNb",
-        "entries",
-        "widgetParams",
         "fileKeys",
         "widgetKeys",
         "parts",
         "sort",
         "b",
         "additionalStyle",
         "addSpaceInsteadTitle",
         "overflowY",
         "blocking",
         "data-toggle",
         "data-placement",
-        "cursor",
-        "notebook_id",
-        "notebook_path",
-        "job_id",
-        "exportToPDF",
+        "UsageLimitReached",
         "reload",
         "Queued",
         "Starting",
         "MainView",
         "appView",
         "errorMsg",
         "columnsWidth",
@@ -537,17 +555,15 @@
         "html",
         "FilesView",
         "filesLinks",
         "f",
         "fname",
         "pop",
         "downloadLink",
-        "paddingBottom",
         "MadeWithDiv",
-        "rel",
         "RestAPIView",
         "slug",
         "taskSessionId",
         "msg",
         "setResponse",
         "examplePostData",
         "fetchResponse",
@@ -615,15 +631,14 @@
         "siteWelcome",
         "parsedNotebooks",
         "fetchNotebooks",
         "fetchWelcome",
         "firstLetters",
         "text",
         "count",
-        "slice",
         "notebookItems",
         "overflow",
         "scrolling",
         "onMouseEnter",
         "onMouseLeave",
         "description",
         "right",
@@ -699,15 +714,15 @@
         "widgets/Slider.tsx",
         "slices/sitesSlice.ts",
         "widgets/File.tsx",
         "widgets/Text.tsx",
         "slices/wsSlice.tsx",
         "widgets/Markdown.tsx",
         "websocket/Provider.tsx",
-        "websocket/StatusBar.tsx",
+        "components/StatusBar.tsx",
         "widgets/Button.tsx",
         "components/RunButton.tsx",
         "components/SideBar.tsx",
         "components/MainView.tsx",
         "components/FilesView.tsx",
         "components/MadeWithDiv.tsx",
         "components/RestAPIView.tsx",
@@ -749,33 +764,33 @@
         "import React, { useEffect, useState } from \"react\";\nimport { useDispatch } from \"react-redux\";\nimport { useSearchParams } from \"react-router-dom\";\nimport {\n  setUrlValuesUsed,\n  setWidgetUrlValue,\n  setWidgetValue,\n} from \"../slices/notebooksSlice\";\n\ntype NumericProps = {\n  widgetKey: string;\n  label: string | null;\n  value: number | null;\n  min: number | null;\n  max: number | null;\n  step: number | null;\n  disabled: boolean;\n  hidden: boolean;\n  runNb: () => void;\n  continuousUpdate: boolean;\n  url_key: string;\n};\n\nexport default function NumericWidget({\n  widgetKey,\n  label,\n  value,\n  min,\n  max,\n  step,\n  disabled,\n  hidden,\n  runNb,\n  continuousUpdate,\n  url_key,\n}: NumericProps) {\n  const dispatch = useDispatch();\n  const [apply, showApply] = useState(false);\n  const [updated, userInteraction] = useState(false);\n\n  let minValue = 0;\n  let maxValue = 10;\n  let stepValue = 1;\n  if (min !== null) {\n    minValue = min;\n  }\n  if (max !== null) {\n    maxValue = max;\n  }\n  if (step !== null) {\n    stepValue = step;\n  }\n  let displayValue = value !== null && value !== undefined ? value : 0;\n\n  const [searchParams] = useSearchParams();\n  useEffect(() => {\n    if (url_key !== undefined && url_key !== \"\") {\n      const urlValue = searchParams.get(url_key);\n      if (\n        !updated &&\n        urlValue !== undefined &&\n        urlValue !== null &&\n        !isNaN(parseFloat(urlValue)) &&\n        parseFloat(urlValue) >= minValue &&\n        parseFloat(urlValue) <= maxValue\n      ) {\n        dispatch(\n          setWidgetUrlValue({\n            key: widgetKey,\n            value: parseFloat(urlValue),\n          })\n        );\n        dispatch(setUrlValuesUsed(true));\n      }\n    }\n  }, [dispatch, maxValue, minValue, searchParams, updated, url_key, widgetKey]);\n\n  const validateValue = () => {\n    if (min !== null && value !== null && value < min) {\n      dispatch(setWidgetValue({ key: widgetKey, value: min }));\n    }\n    if (max !== null && value !== null && value > max) {\n      dispatch(setWidgetValue({ key: widgetKey, value: max }));\n    }\n  };\n\n  return (\n    <div className=\"form-group mb-3\" style={{ display: hidden ? \"none\" : \"\" }}>\n      <label\n        htmlFor={`checkbox-${label}`}\n        style={{ color: disabled ? \"#555\" : \"#212529\" }}\n      >\n        {label}\n      </label>\n      <input\n        className=\"form-control\"\n        type=\"number\"\n        value={displayValue} // {displayValue as number | string}\n        onChange={(e) => {\n          userInteraction(true);\n          showApply(true);\n          dispatch(setWidgetValue({ key: widgetKey, value: e.target.value }));\n        }}\n        onBlur={(e) => {\n          validateValue();\n        }}\n        onKeyPress={(e) => {\n          if (e.key === \"Enter\") {\n            validateValue();\n            runNb();\n            showApply(false);\n            e.preventDefault();\n          }\n        }}\n        min={minValue}\n        max={maxValue}\n        step={stepValue}\n        disabled={disabled}\n      />\n      {apply && continuousUpdate && (\n        <div\n          style={{\n            float: \"right\",\n            position: \"relative\",\n            top: \"0px\",\n            left: \"0px\",\n          }}\n        >\n          <button\n            className=\"btn btn-sm btn-outline-primary\"\n            onClick={(e) => {\n              validateValue();\n              runNb();\n              showApply(false);\n              e.preventDefault();\n            }}\n            style={{\n              fontSize: \"0.7em\",\n              border: \"none\",\n            }}\n          >\n            Press enter or click to apply\n          </button>\n        </div>\n      )}\n    </div>\n  );\n}\n",
         "import React, { useEffect, useState } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\nimport {\n  clearWidgetsUrlValues,\n  getWidgetsInitialized,\n  setUrlValuesUsed,\n  setWidgetUrlValue,\n  setWidgetValue,\n} from \"../slices/notebooksSlice\";\nimport { Range, getTrackBackground } from \"react-range\";\nimport { useSearchParams } from \"react-router-dom\";\n\ntype RangeProps = {\n  widgetKey: string;\n  label: string | null;\n  value: [number, number] | null;\n  min: number | null;\n  max: number | null;\n  step: number | null;\n  vertical: boolean | null;\n  disabled: boolean;\n  hidden: boolean;\n  runNb: () => void;\n  url_key: string;\n};\n\nexport default function RangeWidget({\n  widgetKey,\n  label,\n  value,\n  min,\n  max,\n  step,\n  vertical,\n  disabled,\n  hidden,\n  runNb,\n  url_key,\n}: RangeProps) {\n  let minValue = 0;\n  let maxValue = 100;\n  let stepValue = 1;\n  if (min) {\n    minValue = min;\n  }\n  if (max) {\n    maxValue = max;\n  }\n  if (step) {\n    stepValue = step;\n  }\n\n  const dispatch = useDispatch();\n  const [updated, userInteraction] = useState(false);\n  const [searchParams] = useSearchParams();\n\n  useEffect(() => {\n    if (url_key !== undefined && url_key !== \"\") {\n      const urlValue = searchParams\n        .get(url_key)\n        ?.split(\",\")\n        .map((i) => parseFloat(i));\n      if (\n        !updated &&\n        urlValue !== undefined &&\n        urlValue.length === 2 &&\n        urlValue[0] !== undefined &&\n        !isNaN(urlValue[0]) &&\n        urlValue[1] !== undefined &&\n        !isNaN(urlValue[1]) &&\n        urlValue[0] <= urlValue[1] &&\n        urlValue[0] >= minValue &&\n        urlValue[1] <= maxValue\n      ) {\n        dispatch(\n          setWidgetUrlValue({\n            key: widgetKey,\n            value: urlValue as [number, number],\n          })\n        );\n        dispatch(setUrlValuesUsed(true));\n      }\n    }\n  }, [dispatch, maxValue, minValue, searchParams, updated, url_key, widgetKey]);\n\n  const values =\n    value != null && value !== undefined && value.length === 2\n      ? value\n      : [minValue, maxValue];\n\n  return (\n    <div className=\"form-group mb-3\" style={{ display: hidden ? \"none\" : \"\" }}>\n      <label\n        htmlFor={`range-slider-${label}`}\n        style={{ color: disabled ? \"#555\" : \"#212529\" }}\n      >\n        {label}\n      </label>\n\n      <div\n        style={{\n          paddingTop: \"12px\",\n          display: \"flex\",\n          justifyContent: \"center\",\n          flexWrap: \"wrap\",\n        }}\n      >\n        <Range\n          disabled={disabled}\n          values={values}\n          step={stepValue}\n          min={minValue}\n          max={maxValue}\n          onChange={(values) => {\n            userInteraction(true);\n            dispatch(clearWidgetsUrlValues());\n            dispatch(\n              setWidgetValue({\n                key: widgetKey,\n                value: values as [number, number],\n              })\n            );\n          }}\n          onFinalChange={(values) => {\n            runNb();\n          }}\n          renderTrack={({ props, children }) => (\n            <div\n              onMouseDown={props.onMouseDown}\n              onTouchStart={props.onTouchStart}\n              style={{\n                ...props.style,\n                height: \"36px\",\n                display: \"flex\",\n                width: \"100%\",\n              }}\n            >\n              <div\n                ref={props.ref}\n                style={{\n                  height: \"5px\",\n                  width: \"100%\",\n                  borderRadius: \"4px\",\n                  background: getTrackBackground({\n                    values,\n                    colors: [\n                      \"#ccc\",\n                      disabled ? \"rgba(0, 0, 0, 0.3)\" : \"#2684ff\",\n                      \"#ccc\",\n                    ],\n                    min: minValue,\n                    max: maxValue,\n                  }),\n                  alignSelf: \"center\",\n                }}\n              >\n                {children}\n\n                <div\n                  style={{\n                    display: \"inline-block\",\n                    width: \"100%\",\n                    fontSize: \"12px\",\n                    paddingTop: \"13px\",\n                  }}\n                >\n                  <div style={{ float: \"left\" }}>{minValue}</div>\n                  <div style={{ float: \"right\" }}>{maxValue}</div>\n                </div>\n              </div>\n            </div>\n          )}\n          renderThumb={({ index, props, isDragged }) => (\n            <div\n              {...props}\n              style={{\n                ...props.style,\n                height: \"18px\",\n                width: \"18px\",\n                border: \"None !important\",\n                borderRadius: \"4px\",\n                backgroundColor: \"#FFF\",\n                display: \"flex\",\n                justifyContent: \"center\",\n                alignItems: \"center\",\n                boxShadow: \"0px 2px 6px #AAA\",\n                outline: \"none\",\n              }}\n            >\n              <div\n                style={{\n                  position: \"absolute\",\n                  top: \"-24px\",\n                  color: \"#fff\",\n                  fontWeight: \"bold\",\n                  fontSize: \"12px\",\n                  fontFamily: \"Arial,Helvetica Neue,Helvetica,sans-serif\",\n                  padding: \"2px\",\n                  borderRadius: \"3px\",\n                  backgroundColor: disabled ? \"rgba(0, 0, 0, 0.3)\" : \"#2684ff\",\n                }}\n              >\n                {values[index]}\n              </div>\n              <div\n                style={{\n                  height: \"12px\",\n                  width: \"3px\",\n                  backgroundColor: isDragged ? \"#2684ff\" : \"#CCC\",\n                }}\n              />\n            </div>\n          )}\n        />\n      </div>\n    </div>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React, { useEffect, useState } from \"react\";\nimport { useDispatch } from \"react-redux\";\nimport { useSearchParams } from \"react-router-dom\";\nimport Select, { MultiValue } from \"react-select\";\nimport {\n  setUrlValuesUsed,\n  setWidgetUrlValue,\n  setWidgetValue,\n} from \"../slices/notebooksSlice\";\n\ntype SingleOption = { value: string; label: string };\ntype MultiOption = MultiValue<{ value: string; label: string } | undefined>;\n\nexport function isSingleOption(\n  options: SingleOption | MultiOption\n): options is SingleOption {\n  return (options as SingleOption).value !== undefined;\n}\n\ntype SelectProps = {\n  widgetKey: string;\n  label: string | null;\n  value: string | string[] | null;\n  choices: string[];\n  multi: boolean | undefined;\n  disabled: boolean;\n  hidden: boolean;\n  runNb: () => void;\n  url_key: string;\n};\n\nexport default function SelectWidget({\n  widgetKey,\n  label,\n  value,\n  choices,\n  multi,\n  disabled,\n  hidden,\n  runNb,\n  url_key,\n}: SelectProps) {\n  const dispatch = useDispatch();\n  const [updated, userInteraction] = useState(false);\n\n  const selectStyles = {\n    menu: (base: any) => ({\n      ...base,\n      zIndex: 100,\n    }),\n  };\n\n  const [searchParams] = useSearchParams();\n  useEffect(() => {\n    if (url_key !== undefined && url_key !== \"\") {\n      const urlValue = searchParams.get(url_key);\n      if (!updated && urlValue !== undefined && urlValue !== null) {\n        if (multi) {\n          const arr = urlValue.split(\",\");\n          if (arr) {\n            dispatch(\n              setWidgetUrlValue({\n                key: widgetKey,\n                value: arr.filter((a) => choices.includes(a)),\n              })\n            );\n            dispatch(setUrlValuesUsed(true));\n          }\n        } else {\n          if (choices.includes(urlValue)) {\n            dispatch(\n              setWidgetUrlValue({\n                key: widgetKey,\n                value: urlValue,\n              })\n            );\n            dispatch(setUrlValuesUsed(true));\n          }\n        }\n      }\n    }\n  }, [choices, dispatch, multi, searchParams, updated, url_key, widgetKey]);\n\n  let selectedValue: SingleOption = { value: \"\", label: \"\" };\n  let selectedValues: SingleOption[] = [{ value: \"\", label: \"\" }];\n\n  let options: { value: string; label: string }[] = choices.map((choice) => {\n    if (value && choice === value && !multi) {\n      selectedValue = { value: choice, label: choice };\n    }\n    return { value: choice, label: choice };\n  });\n\n  if (multi) {\n    selectedValues = [];\n    choices.map((choice) => {\n      if (value && value.includes(choice) && multi) {\n        selectedValues.push({ value: choice, label: choice });\n      }\n      return { value: choice, label: choice };\n    });\n  }\n\n  useEffect(() => {\n    if (!updated) return;\n    runNb();\n    // const timeOutId = setTimeout(() => {\n    //   // console.log(\"run from select\");\n    //   runNb();\n    // }, RUN_DELAY_FAST);\n    // return () => clearTimeout(timeOutId);\n    // eslint-disable-next-line react-hooks/exhaustive-deps\n  }, [value]);\n\n  return (\n    <div className=\"form-group mb-3\" style={{ display: hidden ? \"none\" : \"\" }}>\n      <label\n        htmlFor={`select-${label}`}\n        style={{ color: disabled ? \"#555\" : \"#212529\" }}\n      >\n        {label}\n      </label>\n      <Select\n        id={`select-${label}`}\n        isDisabled={disabled}\n        name={label ? label : \"Select\"}\n        styles={selectStyles}\n        value={multi ? selectedValues : selectedValue}\n        options={options}\n        isMulti={multi}\n        onChange={(e) => {\n          if (e) {\n            userInteraction(true);\n            if (isSingleOption(e)) {\n              dispatch(setWidgetValue({ key: widgetKey, value: e.value }));\n            } else {\n              // console.log({ msg: \"values\", values: e.values() });\n              const vs = Array.from(e.values()).filter(\n                (i) => i !== undefined\n              ) as { label: string; value: string }[];\n              // console.log({\n              //   key: widgetKey,\n              // });\n              dispatch(\n                setWidgetValue({\n                  key: widgetKey,\n                  value: vs.map((i) => i.value) as string[],\n                })\n              );\n            }\n          }\n        }}\n      />\n    </div>\n  );\n}\n",
         "import React, { useEffect, useState } from \"react\";\nimport { useDispatch } from \"react-redux\";\nimport {\n  setUrlValuesUsed,\n  setWidgetUrlValue,\n  setWidgetValue,\n} from \"../slices/notebooksSlice\";\nimport { Range, getTrackBackground } from \"react-range\";\nimport { useSearchParams } from \"react-router-dom\";\n\ntype SliderProps = {\n  widgetKey: string;\n  label: string | null;\n  value: number | null;\n  min: number | null;\n  max: number | null;\n  step: number | null;\n  vertical: boolean | null;\n  disabled: boolean;\n  hidden: boolean;\n  runNb: () => void;\n  url_key: string;\n};\n\nexport default function SliderWidget({\n  widgetKey,\n  label,\n  value,\n  min,\n  max,\n  step,\n  vertical,\n  disabled,\n  hidden,\n  runNb,\n  url_key,\n}: SliderProps) {\n  const dispatch = useDispatch();\n  const [updated, userInteraction] = useState(false);\n\n  let minValue = 0;\n  let maxValue = 100;\n  let stepValue = 1;\n  if (min) {\n    minValue = min;\n  }\n  if (max) {\n    maxValue = max;\n  }\n  if (step) {\n    stepValue = step;\n  }\n  const [searchParams] = useSearchParams();\n  useEffect(() => {\n    if (url_key !== undefined && url_key !== \"\") {\n      const urlValue = searchParams.get(url_key);\n      if (\n        !updated &&\n        urlValue !== undefined &&\n        urlValue !== null &&\n        !isNaN(parseFloat(urlValue)) &&\n        parseFloat(urlValue) >= minValue &&\n        parseFloat(urlValue) <= maxValue\n      ) {\n        dispatch(\n          setWidgetUrlValue({\n            key: widgetKey,\n            value: parseFloat(urlValue),\n          })\n        );\n        dispatch(setUrlValuesUsed(true));\n      }\n    }\n  }, [dispatch, maxValue, minValue, searchParams, updated, url_key, widgetKey]);\n\n  const vals: number[] = [value !== null ? value : maxValue];\n\n  return (\n    <div className=\"form-group mb-3\" style={{ display: hidden ? \"none\" : \"\" }}>\n      <label\n        htmlFor={`slider-${label}`}\n        style={{ color: disabled ? \"#555\" : \"#212529\" }}\n      >\n        {label}\n      </label>\n\n      <div\n        style={{\n          paddingTop: \"12px\",\n          display: \"flex\",\n          justifyContent: \"center\",\n          flexWrap: \"wrap\",\n        }}\n      >\n        <Range\n          disabled={disabled}\n          values={vals}\n          step={stepValue}\n          min={minValue}\n          max={maxValue}\n          onChange={(values) => {\n            userInteraction(true);\n            dispatch(setWidgetValue({ key: widgetKey, value: values[0] }));\n          }}\n          onFinalChange={(values) => {\n            runNb();\n          }}\n          renderTrack={({ props, children }) => (\n            <div\n              onMouseDown={props.onMouseDown}\n              onTouchStart={props.onTouchStart}\n              style={{\n                ...props.style,\n                height: \"36px\",\n                display: \"flex\",\n                width: \"100%\",\n              }}\n            >\n              <div\n                ref={props.ref}\n                style={{\n                  height: \"5px\",\n                  width: \"100%\",\n                  borderRadius: \"4px\",\n                  background: getTrackBackground({\n                    values: vals,\n                    colors: [\n                      disabled ? \"rgba(0, 0, 0, 0.3)\" : \"#2684ff\", // \"#548BF4\",\n                      \"#ccc\",\n                    ],\n                    min: minValue,\n                    max: maxValue,\n                  }),\n                  alignSelf: \"center\",\n                }}\n              >\n                {children}\n\n                <div\n                  style={{\n                    display: \"inline-block\",\n                    width: \"100%\",\n                    fontSize: \"12px\",\n                    paddingTop: \"13px\",\n                  }}\n                >\n                  <div style={{ float: \"left\" }}>{minValue}</div>\n                  <div style={{ float: \"right\" }}>{maxValue}</div>\n                </div>\n              </div>\n            </div>\n          )}\n          renderThumb={({ props, isDragged }) => (\n            <div\n              {...props}\n              style={{\n                ...props.style,\n                height: \"18px\",\n                width: \"18px\",\n                border: \"None\",\n                borderRadius: \"4px\",\n                backgroundColor: \"#FFF\",\n                display: \"flex\",\n                justifyContent: \"center\",\n                alignItems: \"center\",\n                boxShadow: \"0px 2px 6px #AAA\",\n                outline: \"none\",\n              }}\n            >\n              <div\n                style={{\n                  position: \"absolute\",\n                  top: \"-24px\",\n                  color: \"#fff\",\n                  fontWeight: \"bold\",\n                  fontSize: \"12px\",\n                  fontFamily: \"Arial,Helvetica Neue,Helvetica,sans-serif\",\n                  padding: \"2px\",\n                  borderRadius: \"3px\",\n                  backgroundColor: disabled ? \"rgba(0, 0, 0, 0.3)\" : \"#2684ff\",\n                }}\n              >\n                {vals[0]}\n              </div>\n              <div\n                style={{\n                  height: \"12px\",\n                  width: \"3px\",\n                  backgroundColor: isDragged ? \"#2684ff\" : \"#CCC\",\n                }}\n              />\n            </div>\n          )}\n        />\n      </div>\n    </div>\n  );\n}\n",
         "/* eslint-disable import/no-cycle */\r\nimport {\r\n  createSlice,\r\n  PayloadAction,\r\n  AnyAction,\r\n  Dispatch,\r\n} from \"@reduxjs/toolkit\";\r\nimport axios, { AxiosError } from \"axios\";\r\n\r\nimport { RootState } from \"../store\";\r\nimport { setToken, setUsername } from \"./authSlice\";\r\n\r\n\r\nexport const SITE_PUBLIC = \"PUBLIC\";\r\nexport const SITE_PRIVATE = \"PRIVATE\";\r\n\r\nexport interface Site {\r\n  id: number;\r\n  title: string;\r\n  slug: string;\r\n  share: string;\r\n  welcome: string;\r\n  active: boolean;\r\n  version: string;\r\n  created_at: Date;\r\n  updated_at: Date;\r\n  created_by: number;\r\n}\r\n\r\nexport enum SiteStatus {\r\n  Unknown = \"Unknown\",\r\n  Loaded = \"Loaded\",\r\n  NotFound = \"Not found\",\r\n  AccessForbidden = \"Access forbidden\",\r\n  NetworkError = \"Network Error\",\r\n  PleaseRefresh = \"Please refresh\",\r\n  LostConnection = \"Lost connection\",\r\n  NotReady = \"Not Ready\"\r\n}\r\n\r\nconst initialState = {\r\n  site: {} as Site,\r\n  siteStatus: SiteStatus.Unknown,\r\n};\r\n\r\nconst sitesSlice = createSlice({\r\n  name: \"sites\",\r\n  initialState,\r\n  reducers: {\r\n    setSite(state, action: PayloadAction<Site>) {\r\n      state.site = action.payload;\r\n    },\r\n    setSiteStatus(state, action: PayloadAction<SiteStatus>) {\r\n      state.siteStatus = action.payload;\r\n    }\r\n  },\r\n});\r\n\r\nexport default sitesSlice.reducer;\r\n\r\nexport const { setSite, setSiteStatus } = sitesSlice.actions;\r\n\r\nexport const getSite = (state: RootState) => state.sites.site;\r\nexport const getSiteStatus = (state: RootState) => state.sites.siteStatus;\r\nexport const getSiteId = (state: RootState) => state.sites.site.id;\r\nexport const getSiteWelcome = (state: RootState) => state.sites.site.welcome;\r\nexport const isPublic = (state: RootState) => {\r\n  return state.sites.site.share === SITE_PUBLIC;\r\n};\r\nexport const fetchSite = () => async (dispatch: Dispatch<AnyAction>) => {\r\n  try {\r\n    dispatch(setSite({} as Site));\r\n    dispatch(setSiteStatus(SiteStatus.Unknown));\r\n\r\n    let siteSlug = \"single-site\";\r\n    if(process.env.REACT_APP_SERVER_URL) {\r\n      siteSlug = window.location.host.split(':')[0]\r\n    }\r\n\r\n    const url = `/api/v1/get-site/${siteSlug}/`;\r\n    const { data } = await axios.get(url);\r\n\r\n    dispatch(setSite(data as Site));\r\n    if(data?.status !== \"Ready\") {\r\n      dispatch(setSiteStatus(SiteStatus.NotReady));  \r\n    } else {\r\n      dispatch(setSiteStatus(SiteStatus.Loaded));\r\n    }\r\n  } catch (error) {\r\n    const err = error as AxiosError;\r\n    console.log(err.message)\r\n    if (err?.message === \"Network Error\") {\r\n      dispatch(setSiteStatus(SiteStatus.NetworkError));\r\n    } else if (err.response!.status === 403) {\r\n      dispatch(setSiteStatus(SiteStatus.AccessForbidden));\r\n    } else if (err.response!.status === 404) {\r\n      dispatch(setSiteStatus(SiteStatus.NotFound));\r\n    } else if (err.response!.status === 401) {\r\n      // invalid token, clear token ...\r\n      dispatch(setToken(\"\"));\r\n      dispatch(setUsername(\"\"));\r\n      dispatch(setSiteStatus(SiteStatus.PleaseRefresh));\r\n    } else {\r\n      console.error(`Problem during loading site information. ${error}`);\r\n    }\r\n  }\r\n};\r\n",
         "import React, { useEffect, useState } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\n\nimport axios, { AxiosProgressEvent } from \"axios\";\n\nimport { setWidgetValue } from \"../slices/notebooksSlice\";\n\nimport { FilePond, registerPlugin } from \"react-filepond\";\nimport FilePondPluginImageExifOrientation from \"filepond-plugin-image-exif-orientation\";\nimport FilePondPluginImagePreview from \"filepond-plugin-image-preview\";\nimport FilePondPluginFileValidateSize from \"filepond-plugin-file-validate-size\";\nimport {\n  deleteUserFileUploaded,\n  fetchStorageType,\n  getStorageType,\n  userFileUploaded,\n} from \"../slices/appSlice\";\nimport { toast } from \"react-toastify\";\nimport { getSiteId } from \"../slices/sitesSlice\";\nimport { getSessionId } from \"../utils\";\n\nregisterPlugin(\n  FilePondPluginImageExifOrientation,\n  FilePondPluginImagePreview,\n  FilePondPluginFileValidateSize\n);\n\ntype FileProps = {\n  widgetKey: string;\n  label: string | null;\n  maxFileSize: string | null;\n  disabled: boolean;\n  hidden: boolean;\n  value: string[];\n  runNb: () => void;\n};\n\nexport default function FileWidget({\n  widgetKey,\n  label,\n  maxFileSize,\n  disabled,\n  hidden,\n  value,\n  runNb,\n}: FileProps) {\n  const dispatch = useDispatch();\n  const [updated, userInteraction] = useState(false);\n  const storageType = useSelector(getStorageType);\n  const siteId = useSelector(getSiteId);\n  const sessionId = useSelector(getSessionId);\n\n  let fileSizeLimit = \"100MB\";\n  if (maxFileSize) {\n    fileSizeLimit = maxFileSize;\n  }\n  useEffect(() => {\n    if (updated && value !== undefined && value.length === 2) {\n      //console.log(\"run from file\");\n      runNb();\n    }\n    // eslint-disable-next-line react-hooks/exhaustive-deps\n  }, [value]);\n\n  useEffect(() => {\n    dispatch(fetchStorageType());\n  }, [dispatch]);\n\n  console.log(storageType);\n\n  const mediaServerActions = {\n    url: `${axios.defaults.baseURL}/api/v1/fp`,\n    process: \"/process/\",\n    revert: async (\n      uniqueFileId: any,\n      load: () => void,\n      error: (arg0: string) => void\n    ) => {\n      try {\n        await axios.delete(`${axios.defaults.baseURL}/api/v1/fp/revert`, {\n          data: uniqueFileId,\n        });\n        dispatch(setWidgetValue({ key: widgetKey, value: [] }));\n        // Should call the load method when done, no parameters required\n        load();\n      } catch (e) {\n        // Can call the error method if something is wrong, should exit after\n        error(\"Problem with uploaded file removal\");\n      }\n    },\n  };\n  const s3ServerActions = {\n    process: (\n      fieldName: string,\n      file: { name: any; size: any },\n      metadata: any,\n      load: (arg0: any) => void,\n      error: any,\n      progress: (arg0: boolean, arg1: any, arg2: number) => void,\n      abort: () => void\n    ) => {\n      const abortController = new AbortController();\n\n      axios\n        .get(\n          `/api/v1/nb-file-put/${siteId}/${sessionId}/${file.name}/${file.size}`\n        )\n        .then((response) => {\n          const { url } = response.data;\n\n          let token = axios.defaults.headers.common[\"Authorization\"];\n\n          delete axios.defaults.headers.common[\"Authorization\"];\n\n          const config = {\n            onUploadProgress: (progressEvent: AxiosProgressEvent) => {\n              progress(\n                progressEvent.total !== undefined,\n                progressEvent.loaded,\n                progressEvent.total as number\n              );\n            },\n          };\n\n          axios\n            .put(url, file, {\n              headers: {\n                \"Content-Type\": \"\",\n              },\n              onUploadProgress: config.onUploadProgress,\n              signal: abortController.signal,\n            })\n            .then((response) => {\n              // file uploaded\n              // set it as uploaded in filepond\n              load(file.name);\n              // save it in database\n              if (siteId !== undefined) {\n                dispatch(userFileUploaded(siteId, sessionId, file.name));\n              }\n            })\n            .catch((error) => {\n              toast.error(\"Error when uploading new files\");\n            });\n\n          axios.defaults.headers.common[\"Authorization\"] = token;\n        })\n        .catch((error) => {\n          toast.error(\"Cant upload new files\");\n        });\n\n      // Should expose an abort method so the request can be cancelled\n      return {\n        abort: () => {\n          // This function is entered if the user has tapped the cancel button\n          abortController.abort();\n          // Let FilePond know the request has been cancelled\n          abort();\n        },\n      };\n    },\n    revert: async (\n      uniqueFileId: any,\n      load: () => void,\n      error: (arg0: string) => void\n    ) => {\n      try {\n        if (siteId !== undefined) {\n          dispatch(deleteUserFileUploaded(siteId, sessionId, uniqueFileId));\n        }\n        // Should call the load method when done, no parameters required\n        load();\n      } catch (e) {\n        // Can call the error method if something is wrong, should exit after\n        error(\"Problem with uploaded file removal\");\n      }\n    },\n  };\n\n  return (\n    <div className=\"form-group mb-3\" style={{ display: hidden ? \"none\" : \"\" }}>\n      <label\n        htmlFor={`file-${label}`}\n        style={{ color: disabled ? \"#555\" : \"#212529\" }}\n      >\n        {label}\n      </label>\n      <div>\n        <FilePond\n          disabled={disabled}\n          maxFileSize={fileSizeLimit}\n          onprocessfile={(error, file) => {\n            userInteraction(true);\n            dispatch(\n              setWidgetValue({\n                key: widgetKey,\n                value: [file.filename, file.serverId],\n              })\n            );\n          }}\n          server={\n            storageType === \"media\" ? mediaServerActions : s3ServerActions\n          }\n          labelIdle='Drag & Drop your file or <span class=\"filepond--label-action\">Browse</span>'\n        />\n      </div>\n    </div>\n  );\n}\n",
         "import React, { useEffect, useState } from \"react\";\nimport { useDispatch } from \"react-redux\";\nimport { useSearchParams } from \"react-router-dom\";\nimport { setUrlValuesUsed, setWidgetUrlValue, setWidgetValue } from \"../slices/notebooksSlice\";\n\ntype TextProps = {\n  widgetKey: string;\n  label: string | null;\n  value: string | undefined;\n  rows: number | null;\n  disabled: boolean;\n  hidden: boolean;\n  runNb: () => void;\n  continuousUpdate: boolean;\n  url_key: string;\n};\n\nexport default function TextWidget({\n  widgetKey,\n  label,\n  value,\n  rows,\n  disabled,\n  hidden,\n  runNb,\n  continuousUpdate,\n  url_key,\n}: TextProps) {\n  const dispatch = useDispatch();\n  const [apply, showApply] = useState(false);\n  const [updated, userInteraction] = useState(false);\n  let rowsValue: number = rows ? rows : 1;\n\n  const sanitizeString = (input_string: string) => {\n    return input_string.replace(/[\"'(){}[\\]`^]/gim, \"\");\n  };\n\n  const [searchParams] = useSearchParams();\n  useEffect(() => {\n    if (url_key !== undefined && url_key !== \"\") {\n      const urlValue = searchParams.get(url_key);\n      if (!updated && urlValue !== undefined && urlValue !== null) {\n        dispatch(\n          setWidgetUrlValue({\n            key: widgetKey,\n            value: urlValue,\n          })\n        );\n        dispatch(setUrlValuesUsed(true));\n      }\n    }\n  }, [dispatch, searchParams, updated, url_key, widgetKey]);\n\n  return (\n    <div className=\"form-group mb-3\" style={{ display: hidden ? \"none\" : \"\" }}>\n      <label\n        htmlFor={`textarea-${label}`}\n        style={{ color: disabled ? \"#555\" : \"#212529\" }}\n      >\n        {label}\n      </label>\n      {rowsValue === 1 && (\n        <input\n          className=\"form-control\"\n          type=\"text\"\n          id={`text-${label}`}\n          value={value ? value : \"\"}\n          onChange={(e) => {\n            userInteraction(true);\n            showApply(true);\n            dispatch(\n              setWidgetValue({\n                key: widgetKey,\n                value: sanitizeString(e.target.value),\n              })\n            );\n          }}\n          onKeyPress={(e) => {\n            if (e.key === \"Enter\") {\n              runNb();\n              showApply(false);\n              e.preventDefault();\n            }\n          }}\n          disabled={disabled}\n        />\n      )}\n      {rowsValue > 1 && (\n        <textarea\n          className=\"form-control\"\n          id={`text-area-${label}`}\n          rows={rowsValue}\n          value={value ? value : \"\"}\n          onChange={(e) => {\n            userInteraction(true);\n            showApply(true);\n            dispatch(\n              setWidgetValue({\n                key: widgetKey,\n                value: sanitizeString(e.target.value),\n              })\n            );\n          }}\n          disabled={disabled}\n        />\n      )}\n\n      {apply && continuousUpdate && rowsValue === 1 && (\n        // <div\n        //   style={{\n        //     fontSize: \"0.7em\",\n        //     float: \"right\",\n        //     position: \"relative\",\n        //     top: \"0px\",\n        //     left: \"-5px\",\n        //     color: \"#2684ff\",\n        //   }}\n        // >\n        //   Press enter to apply\n        // </div>\n\n        <div\n          style={{\n            float: \"right\",\n            position: \"relative\",\n            top: \"2px\",\n            left: \"0px\",\n          }}\n        >\n          <button\n            className=\"btn btn-sm btn-outline-primary\"\n            onClick={(e) => {\n              runNb();\n              showApply(false);\n              e.preventDefault();\n            }}\n            style={{\n              fontSize: \"0.7em\",\n              border: \"none\",\n            }}\n          >\n            Press enter or click to apply\n          </button>\n        </div>\n      )}\n      {apply && continuousUpdate && rowsValue > 1 && (\n        <div\n          style={{\n            float: \"right\",\n            position: \"relative\",\n            top: \"2px\",\n            left: \"0px\",\n          }}\n        >\n          <button\n            className=\"btn btn-sm btn-outline-primary\"\n            onClick={(e) => {\n              runNb();\n              showApply(false);\n              e.preventDefault();\n            }}\n            style={{\n              fontSize: \"0.7em\",\n              border: \"none\",\n            }}\n          >\n            Apply\n          </button>\n        </div>\n      )}\n    </div>\n  );\n}\n",
-        "/* eslint-disable import/no-cycle */\nimport { createSlice, PayloadAction } from \"@reduxjs/toolkit\";\nimport { RootState } from \"../store\";\n\nexport enum WebSocketState {\n  Connecting = \"Connecting\",\n  Connected = \"Connected\",\n  Unknown = \"Unknown\",\n  Disconnected = \"Disconnected\",\n}\n\nexport enum WorkerState {\n  Unknown = \"Unknown\",\n  Starting = \"Starting\",\n  Running = \"Running\",\n  Missing = \"Missing\",\n  Busy = \"Busy\",\n  Queued = \"Queued\",\n  MaxRunTimeReached = \"MaxRunTimeReached\",\n  MaxIdleTimeReached = \"MaxIdleTimeReached\",\n  //InstallPackages = \"InstallPackages\",\n}\n\nconst initialState = {\n  webSocketState: WebSocketState.Unknown,\n  workerState: WorkerState.Unknown,\n  workerId: undefined as undefined | number,\n  notebookSrc: \"\",\n  tryConnectCount: 0,\n};\n\nconst wsSlice = createSlice({\n  name: \"ws\",\n  initialState,\n  reducers: {\n    setWebSocketState(state, action: PayloadAction<WebSocketState>) {\n      state.webSocketState = action.payload;\n    },\n    setWorkerState(state, action: PayloadAction<WorkerState>) {\n      state.workerState = action.payload;\n    },\n    setWorkerId(state, action: PayloadAction<undefined | number>) {\n      state.workerId = action.payload;\n    },\n    setNotebookSrc(state, action: PayloadAction<string>) {\n      state.notebookSrc = action.payload;\n    },\n    increaseTryConnectCount(state) {\n      state.tryConnectCount += 1;\n    },\n    resetTryConnectCount(state) {\n      state.tryConnectCount = 0;\n    },\n  },\n});\n\nexport default wsSlice.reducer;\n\nexport const {\n  setWebSocketState,\n  setWorkerState,\n  setWorkerId,\n  setNotebookSrc,\n  increaseTryConnectCount,\n  resetTryConnectCount,\n} = wsSlice.actions;\n\nexport const getWebSocketState = (state: RootState) => state.ws.webSocketState;\nexport const getWorkerState = (state: RootState) => state.ws.workerState;\nexport const getWorkerId = (state: RootState) => state.ws.workerId;\nexport const getNotebookSrc = (state: RootState) => state.ws.notebookSrc;\nexport const getTryConnectCount = (state: RootState) =>\n  state.ws.tryConnectCount;\n\nexport const runNotebook = (widgets_params: string) => {\n  return {\n    purpose: \"run-notebook\",\n    widgets: widgets_params,\n  };\n};\n\nexport const saveNotebook = () => {\n  return {\n    purpose: \"save-notebook\",\n  };\n};\n\nexport const displayNotebook = (taskId: number) => {\n  return {\n    purpose: \"display-notebook\",\n    taskId,\n  };\n};\n\nexport const downloadHTML = () => {\n  return {\n    purpose: \"download-html\",\n  };\n};\n\nexport const downloadPDF = () => {\n  return {\n    purpose: \"download-pdf\",\n  };\n};\n",
+        "/* eslint-disable import/no-cycle */\nimport { createSlice, PayloadAction } from \"@reduxjs/toolkit\";\nimport { RootState } from \"../store\";\n\nexport enum WebSocketState {\n  Connecting = \"Connecting\",\n  Connected = \"Connected\",\n  Unknown = \"Unknown\",\n  Disconnected = \"Disconnected\",\n}\n\nexport enum WorkerState {\n  Unknown = \"Unknown\",\n  Starting = \"Starting\",\n  Running = \"Running\",\n  Missing = \"Missing\",\n  Busy = \"Busy\",\n  Queued = \"Queued\",\n  MaxRunTimeReached = \"MaxRunTimeReached\",\n  MaxIdleTimeReached = \"MaxIdleTimeReached\",\n  UsageLimitReached = \"UsageLimitReached\",\n  //InstallPackages = \"InstallPackages\",\n}\n\nconst initialState = {\n  webSocketState: WebSocketState.Unknown,\n  workerState: WorkerState.Unknown,\n  workerId: undefined as undefined | number,\n  notebookSrc: \"\",\n  tryConnectCount: 0,\n};\n\nconst wsSlice = createSlice({\n  name: \"ws\",\n  initialState,\n  reducers: {\n    setWebSocketState(state, action: PayloadAction<WebSocketState>) {\n      state.webSocketState = action.payload;\n    },\n    setWorkerState(state, action: PayloadAction<WorkerState>) {\n      state.workerState = action.payload;\n    },\n    setWorkerId(state, action: PayloadAction<undefined | number>) {\n      state.workerId = action.payload;\n    },\n    setNotebookSrc(state, action: PayloadAction<string>) {\n      state.notebookSrc = action.payload;\n    },\n    increaseTryConnectCount(state) {\n      state.tryConnectCount += 1;\n    },\n    resetTryConnectCount(state) {\n      state.tryConnectCount = 0;\n    },\n  },\n});\n\nexport default wsSlice.reducer;\n\nexport const {\n  setWebSocketState,\n  setWorkerState,\n  setWorkerId,\n  setNotebookSrc,\n  increaseTryConnectCount,\n  resetTryConnectCount,\n} = wsSlice.actions;\n\nexport const getWebSocketState = (state: RootState) => state.ws.webSocketState;\nexport const getWorkerState = (state: RootState) => state.ws.workerState;\nexport const getWorkerId = (state: RootState) => state.ws.workerId;\nexport const getNotebookSrc = (state: RootState) => state.ws.notebookSrc;\nexport const getTryConnectCount = (state: RootState) =>\n  state.ws.tryConnectCount;\n\nexport const runNotebook = (widgets_params: string) => {\n  return {\n    purpose: \"run-notebook\",\n    widgets: widgets_params,\n  };\n};\n\nexport const saveNotebook = () => {\n  return {\n    purpose: \"save-notebook\",\n  };\n};\n\nexport const displayNotebook = (taskId: number) => {\n  return {\n    purpose: \"display-notebook\",\n    taskId,\n  };\n};\n\nexport const downloadHTML = () => {\n  return {\n    purpose: \"download-html\",\n  };\n};\n\nexport const downloadPDF = () => {\n  return {\n    purpose: \"download-pdf\",\n  };\n};\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React from \"react\";\n\nimport ReactMarkdown from \"react-markdown\";\nimport rehypeHighlight from \"rehype-highlight\";\nimport remarkGfm from \"remark-gfm\";\nimport emoji from \"remark-emoji\";\nimport rehypeRaw from \"rehype-raw\";\n\ntype MarkdownProps = {\n  value: string;\n  disabled: boolean;\n};\n\nexport default function MarkdownWidget({ value, disabled }: MarkdownProps) {\n  return (\n    <div\n      className=\"form-group mb-3\"\n      style={{ color: disabled ? \"#555\" : \"#212529\" }}\n    >\n      <ReactMarkdown\n        rehypePlugins={[remarkGfm, rehypeHighlight, emoji, rehypeRaw]}\n      >\n        {value}\n      </ReactMarkdown>\n    </div>\n  );\n}\n",
         "import React, { createContext, useEffect } from \"react\";\nimport { useDispatch } from \"react-redux\";\nimport {\n  getSelectedNotebookId,\n  hideWidgets,\n  isStaticNotebook,\n  updateWidgetsParams,\n  initWidgets,\n  fetchNotebook,\n  updateTitle,\n  updateShowCode,\n  setWidgetsInitialized,\n} from \"../slices/notebooksSlice\";\nimport {\n  setNotebookSrc,\n  setWebSocketState,\n  setWorkerState,\n  setWorkerId,\n  WebSocketState,\n  WorkerState,\n  resetTryConnectCount,\n  increaseTryConnectCount,\n} from \"../slices/wsSlice\";\n\nimport { useSelector } from \"react-redux\";\nimport { getSessionId, handleDownload } from \"../utils\";\nimport { setExportingToPDF } from \"../slices/tasksSlice\";\nimport { getSiteId, setSiteStatus, SiteStatus } from \"../slices/sitesSlice\";\nimport { getToken } from \"../slices/authSlice\";\n\nconst WebSocketContext = createContext(undefined as any);\n\nexport { WebSocketContext };\n\nlet wsServer = \"ws://127.0.0.1:8000\";\nlet localServer = true;\nif (process.env.REACT_APP_SERVER_WS) {\n  wsServer = process.env.REACT_APP_SERVER_WS;\n  localServer = false;\n} else {\n  if (window.location.origin === \"http://localhost:3000\") {\n    wsServer = \"ws://127.0.0.1:8000\";\n    localServer = true;\n  } else {\n    wsServer = window.location.origin\n      .replace(\"http://\", \"ws://\")\n      .replace(\"https://\", \"wss://\");\n    localServer = false;\n  }\n}\n\nconst MAX_CONNECT_COUNT = 5;\nlet connectCounter = 0;\nlet globalConnection: WebSocket | undefined = undefined;\n\nexport default function WebSocketProvider({\n  children,\n}: {\n  children: JSX.Element;\n}) {\n  console.log(\"WebSocketProvider\");\n\n  const dispatch = useDispatch();\n  const siteId = useSelector(getSiteId);\n  const selectedNotebookId = useSelector(getSelectedNotebookId);\n  const token = useSelector(getToken);\n  const isStatic = useSelector(isStaticNotebook);\n  \n\n  let connection: WebSocket | undefined = undefined;\n  let workerState = \"Unknown\" as WorkerState;\n\n  useEffect(() => {\n    connectCounter = 0;\n    // returned function will be called on component unmount\n    return () => {\n      connectCounter = MAX_CONNECT_COUNT + 1;\n      globalConnection?.close();\n    };\n    // eslint-disable-next-line react-hooks/exhaustive-deps\n  }, []);\n\n  const sendMessage = (payload: string) => {\n    if (connection !== undefined && connection.readyState === connection.OPEN) {\n      connection.send(payload);\n    }\n  };\n\n  function onOpen(event: any): void {\n    dispatch(resetTryConnectCount());\n    sendMessage(\n      JSON.stringify({\n        purpose: \"server-address\",\n        address: wsServer,\n      })\n    );\n    dispatch(setWebSocketState(WebSocketState.Connected));\n    ping();\n  }\n\n  function onMessage(event: any): void {\n    // console.log(\"reveived from server\", event.data);\n\n    const response = JSON.parse(event.data);\n    if (\"purpose\" in response) {\n      if (response.purpose === \"worker-state\") {\n        console.log(\"worker-state\", response.state);\n        workerState = response.state;\n\n        dispatch(setWorkerState(response.state));\n        dispatch(setWorkerId(response.workerId));\n\n        if (\n          workerState === WorkerState.MaxIdleTimeReached ||\n          workerState === WorkerState.MaxRunTimeReached\n        ) {\n          connection?.close();\n        }\n      } else if (response.purpose === \"executed-notebook\") {\n        //console.log(response?.reloadNotebook, selectedNotebookId);\n        if (response?.reloadNotebook && selectedNotebookId !== undefined) {\n          //console.log(\"reload notebook ...........................\");\n          dispatch(fetchNotebook(siteId, selectedNotebookId));\n        }\n        dispatch(setNotebookSrc(response.body));\n        // } else if (response.purpose === \"saved-notebook\") {\n        //   if (selectedNotebookId !== undefined) {\n        //     dispatch(fetchExecutionHistory(selectedNotebookId, false));\n        //   }\n      } else if (response.purpose === \"update-widgets\") {\n        dispatch(updateWidgetsParams(response));\n      } else if (response.purpose === \"hide-widgets\") {\n        dispatch(hideWidgets(response));\n      } else if (response.purpose === \"init-widgets\") {\n        dispatch(initWidgets(response));\n        dispatch(setWidgetsInitialized(true));\n      } else if (response.purpose === \"update-title\") {\n        dispatch(updateTitle(response.title));\n      } else if (response.purpose === \"update-show-code\") {\n        dispatch(updateShowCode(response.showCode));\n      } else if (\n        response.purpose === \"download-html\" ||\n        response.purpose === \"download-pdf\"\n      ) {\n        if (response.url && response.filename) {\n          dispatch(setExportingToPDF(false));\n          handleDownload(response.url, response.filename);\n        }\n      }\n    }\n  }\n\n  function onError(event: any): void {\n    dispatch(setWebSocketState(WebSocketState.Disconnected));\n    dispatch(setWorkerState(WorkerState.Unknown));\n  }\n\n  function onClose(event: any): void {\n    dispatch(setWebSocketState(WebSocketState.Disconnected));\n    connection = undefined;\n    if (\n      workerState !== WorkerState.MaxIdleTimeReached &&\n      workerState !== WorkerState.MaxRunTimeReached\n    ) {\n      dispatch(setWorkerState(WorkerState.Unknown));\n      dispatch(setWorkerId(undefined));\n      if (connectCounter < MAX_CONNECT_COUNT) {\n        setTimeout(() => connect(), 5000);\n      }\n    }\n  }\n\n  function ping(): void {\n    sendMessage(\n      JSON.stringify({\n        purpose: \"worker-ping\",\n      })\n    );\n    if (connection !== undefined && connection.readyState === connection.OPEN) {\n      setTimeout(() => ping(), 10000);\n    }\n  }\n\n  function connect() {\n    if (\n      (localServer || !isStatic) &&\n      selectedNotebookId !== undefined &&\n      connection === undefined &&\n      workerState !== WorkerState.MaxIdleTimeReached &&\n      workerState !== WorkerState.MaxRunTimeReached &&\n      connectCounter < MAX_CONNECT_COUNT\n    ) {\n      console.log(\"WS connect ...\" + workerState + \" \" + connectCounter);\n      dispatch(increaseTryConnectCount());\n      let url = `${wsServer}/ws/client/${selectedNotebookId}/${getSessionId()}/`;\n      if (token !== undefined && token !== null && token !== \"\") {\n        url += `?token=${token}`;\n      }\n      connection = new WebSocket(url);\n      connection.onopen = onOpen;\n      connection.onmessage = onMessage;\n      connection.onerror = onError;\n      connection.onclose = onClose;\n      connectCounter += 1;\n\n      globalConnection = connection;\n      if (connectCounter >= MAX_CONNECT_COUNT) {\n        dispatch(setSiteStatus(SiteStatus.NetworkError));\n      }\n    }\n  }\n  connect();\n\n  const ws = {\n    sendMessage,\n  };\n\n  return (\n    <WebSocketContext.Provider value={ws}>{children}</WebSocketContext.Provider>\n  );\n}\n",
-        "import React, { useEffect } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\nimport { getSessionId } from \"../utils\";\nimport {\n  WorkerState,\n  WebSocketState,\n  getWebSocketState,\n  getWorkerState,\n  getTryConnectCount,\n} from \"../slices/wsSlice\";\nimport { setSiteStatus, SiteStatus } from \"../slices/sitesSlice\";\n\nexport default function StatusBar() {\n  const dispatch = useDispatch();\n  const wsStatus = useSelector(getWebSocketState);\n  const workerState = useSelector(getWorkerState);\n  const tryConnectCount = useSelector(getTryConnectCount);\n\n  useEffect(() => {\n    if (tryConnectCount >= 5) {\n      dispatch(setSiteStatus(SiteStatus.LostConnection));\n    }\n  }, [dispatch, tryConnectCount]);\n\n  let wifiColor = \"orange\";\n  if (wsStatus === WebSocketState.Connected) {\n    wifiColor = \"green\";\n  } else if (\n    wsStatus === WebSocketState.Disconnected ||\n    wsStatus === WebSocketState.Unknown\n  ) {\n    wifiColor = \"red\";\n  }\n\n  let workerColor = \"orange\";\n  if (workerState === WorkerState.Running || workerState === WorkerState.Busy) {\n    workerColor = \"green\";\n  } else if (\n    workerState === WorkerState.Missing ||\n    workerState === WorkerState.Unknown\n  ) {\n    workerColor = \"red\";\n  }\n\n  return (\n    <div>\n      <span title={`WebSocket: ${wsStatus}`}>\n        <svg\n          xmlns=\"http://www.w3.org/2000/svg\"\n          width=\"16\"\n          height=\"16\"\n          fill={wifiColor}\n          className=\"bi bi-wifi\"\n          viewBox=\"0 0 16 16\"\n        >\n          <path d=\"M15.384 6.115a.485.485 0 0 0-.047-.736A12.444 12.444 0 0 0 8 3C5.259 3 2.723 3.882.663 5.379a.485.485 0 0 0-.048.736.518.518 0 0 0 .668.05A11.448 11.448 0 0 1 8 4c2.507 0 4.827.802 6.716 2.164.205.148.49.13.668-.049z\" />\n          <path d=\"M13.229 8.271a.482.482 0 0 0-.063-.745A9.455 9.455 0 0 0 8 6c-1.905 0-3.68.56-5.166 1.526a.48.48 0 0 0-.063.745.525.525 0 0 0 .652.065A8.46 8.46 0 0 1 8 7a8.46 8.46 0 0 1 4.576 1.336c.206.132.48.108.653-.065zm-2.183 2.183c.226-.226.185-.605-.1-.75A6.473 6.473 0 0 0 8 9c-1.06 0-2.062.254-2.946.704-.285.145-.326.524-.1.75l.015.015c.16.16.407.19.611.09A5.478 5.478 0 0 1 8 10c.868 0 1.69.201 2.42.56.203.1.45.07.61-.091l.016-.015zM9.06 12.44c.196-.196.198-.52-.04-.66A1.99 1.99 0 0 0 8 11.5a1.99 1.99 0 0 0-1.02.28c-.238.14-.236.464-.04.66l.706.706a.5.5 0 0 0 .707 0l.707-.707z\" />\n        </svg>\n      </span>{\" \"}\n      <span title={`Worker: ${workerState}\\nSession Id: ${getSessionId()}`}>\n        <svg\n          xmlns=\"http://www.w3.org/2000/svg\"\n          width=\"16\"\n          height=\"16\"\n          fill={workerColor}\n          className=\"bi bi-cpu\"\n          viewBox=\"0 0 16 16\"\n        >\n          <path d=\"M5 0a.5.5 0 0 1 .5.5V2h1V.5a.5.5 0 0 1 1 0V2h1V.5a.5.5 0 0 1 1 0V2h1V.5a.5.5 0 0 1 1 0V2A2.5 2.5 0 0 1 14 4.5h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14a2.5 2.5 0 0 1-2.5 2.5v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14A2.5 2.5 0 0 1 2 11.5H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2A2.5 2.5 0 0 1 4.5 2V.5A.5.5 0 0 1 5 0zm-.5 3A1.5 1.5 0 0 0 3 4.5v7A1.5 1.5 0 0 0 4.5 13h7a1.5 1.5 0 0 0 1.5-1.5v-7A1.5 1.5 0 0 0 11.5 3h-7zM5 6.5A1.5 1.5 0 0 1 6.5 5h3A1.5 1.5 0 0 1 11 6.5v3A1.5 1.5 0 0 1 9.5 11h-3A1.5 1.5 0 0 1 5 9.5v-3zM6.5 6a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5h-3z\" />\n        </svg>\n      </span>\n      {workerState === WorkerState.Busy && (\n        <span title=\"Worker is busy\">\n          {\" \"}\n          <svg\n            xmlns=\"http://www.w3.org/2000/svg\"\n            width=\"16\"\n            height=\"16\"\n            fill=\"green\"\n            className=\"bi bi-activity\"\n            viewBox=\"0 0 16 16\"\n          >\n            <path\n              fillRule=\"evenodd\"\n              d=\"M6 2a.5.5 0 0 1 .47.33L10 12.036l1.53-4.208A.5.5 0 0 1 12 7.5h3.5a.5.5 0 0 1 0 1h-3.15l-1.88 5.17a.5.5 0 0 1-.94 0L6 3.964 4.47 8.171A.5.5 0 0 1 4 8.5H.5a.5.5 0 0 1 0-1h3.15l1.88-5.17A.5.5 0 0 1 6 2Z\"\n            />\n          </svg>{\" \"}\n          Busy\n        </span>\n      )}\n    </div>\n  );\n}\n",
+        "import React, { useEffect, useState } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\nimport { getSessionId, handleDownload } from \"../utils\";\nimport {\n  WorkerState,\n  WebSocketState,\n  getWebSocketState,\n  getWorkerState,\n  getTryConnectCount,\n} from \"../slices/wsSlice\";\nimport { setSiteStatus, SiteStatus } from \"../slices/sitesSlice\";\nimport axios from \"axios\";\nimport { exportToPDF, setExportingToPDF } from \"../slices/tasksSlice\";\nimport {\n  isCheckboxWidget,\n  isFileWidget,\n  isNumericWidget,\n  isRangeWidget,\n  isSelectWidget,\n  isSliderWidget,\n  isTextWidget,\n  IWidget,\n} from \"../widgets/Types\";\nimport { WidgetValueType } from \"../slices/notebooksSlice\";\n\ntype Props = {\n  allowDownload: boolean;\n  waiting: boolean;\n  continuousUpdate: boolean;\n  staticNotebook: boolean;\n  notebookId: number;\n  notebookPath: string;\n  notebookTitle: string;\n  runDownloadHTML: () => void;\n  runDownloadPDF: () => void;\n  widgetsValues: Record<string, WidgetValueType>;\n  widgetsParams: Record<string, IWidget>;\n};\n\nexport default function StatusBar({\n  allowDownload,\n  waiting,\n  continuousUpdate,\n  staticNotebook,\n  notebookId,\n  notebookPath,\n  notebookTitle,\n  runDownloadHTML,\n  runDownloadPDF,\n  widgetsValues,\n  widgetsParams,\n}: Props) {\n  const dispatch = useDispatch();\n  const [showShareModal, setShowShareModal] = useState(false);\n  const wsStatus = useSelector(getWebSocketState);\n  const workerState = useSelector(getWorkerState);\n  const tryConnectCount = useSelector(getTryConnectCount);\n\n  useEffect(() => {\n    if (tryConnectCount >= 5) {\n      dispatch(setSiteStatus(SiteStatus.LostConnection));\n    }\n  }, [dispatch, tryConnectCount]);\n\n  let wifiColor = \"orange\";\n  if (wsStatus === WebSocketState.Connected) {\n    wifiColor = \"green\";\n  } else if (\n    wsStatus === WebSocketState.Disconnected ||\n    wsStatus === WebSocketState.Unknown\n  ) {\n    wifiColor = \"red\";\n  }\n\n  let workerColor = \"orange\";\n  if (workerState === WorkerState.Running || workerState === WorkerState.Busy) {\n    workerColor = \"green\";\n  } else if (\n    workerState === WorkerState.Missing ||\n    workerState === WorkerState.Unknown\n  ) {\n    workerColor = \"red\";\n  }\n\n  let noUrlKeys = true;\n  let urlParams = \"?\";\n  if (\n    widgetsParams !== undefined &&\n    widgetsParams !== null &&\n    widgetsValues !== undefined &&\n    widgetsValues !== null\n  ) {\n    for (let [key, widgetParams] of Object.entries(widgetsParams)) {\n      if (widgetsValues[key] === undefined) {\n        continue;\n      }\n\n      if (\n        isCheckboxWidget(widgetParams) ||\n        isNumericWidget(widgetParams) ||\n        isRangeWidget(widgetParams) ||\n        isSelectWidget(widgetParams) ||\n        isSliderWidget(widgetParams) ||\n        isTextWidget(widgetParams)\n      ) {\n        if (widgetParams?.url_key !== null && widgetParams?.url_key !== \"\") {\n          noUrlKeys = false;\n        }\n      }\n\n      if (\n        isCheckboxWidget(widgetParams) ||\n        isNumericWidget(widgetParams) ||\n        isSliderWidget(widgetParams) ||\n        isTextWidget(widgetParams)\n      ) {\n        if (widgetParams?.url_key !== null && widgetParams?.url_key !== \"\") {\n          urlParams += `${widgetParams?.url_key}=${widgetsValues[key]}&`;\n        }\n      }\n\n      if (isRangeWidget(widgetParams)) {\n        if (widgetParams?.url_key !== null && widgetParams?.url_key !== \"\") {\n          const v = widgetsValues[key] as [number, number];\n\n          urlParams += `${widgetParams?.url_key}=${v[0]},${v[1]}&`;\n        }\n      }\n      if (isSelectWidget(widgetParams)) {\n        if (widgetParams?.url_key !== null && widgetParams?.url_key !== \"\") {\n          if (widgetParams?.multi) {\n            const v = widgetsValues[key] as string[];\n\n            urlParams += `${widgetParams?.url_key}=${v.join(\",\")}&`;\n          } else {\n            const v = widgetsValues[key] as string;\n            urlParams += `${widgetParams?.url_key}=${v}&`;\n          }\n        }\n      }\n    }\n    if (urlParams !== \"?\") {\n      urlParams = urlParams.slice(0, urlParams.length - 1);\n    }\n  }\n\n  return (\n    <div style={{ paddingBottom: \"25px\" }}>\n      {notebookId !== undefined && !staticNotebook && (\n        <>\n          <span title={`WebSocket: ${wsStatus}`}>\n            <svg\n              xmlns=\"http://www.w3.org/2000/svg\"\n              width=\"16\"\n              height=\"16\"\n              fill={wifiColor}\n              className=\"bi bi-wifi\"\n              viewBox=\"0 0 16 16\"\n            >\n              <path d=\"M15.384 6.115a.485.485 0 0 0-.047-.736A12.444 12.444 0 0 0 8 3C5.259 3 2.723 3.882.663 5.379a.485.485 0 0 0-.048.736.518.518 0 0 0 .668.05A11.448 11.448 0 0 1 8 4c2.507 0 4.827.802 6.716 2.164.205.148.49.13.668-.049z\" />\n              <path d=\"M13.229 8.271a.482.482 0 0 0-.063-.745A9.455 9.455 0 0 0 8 6c-1.905 0-3.68.56-5.166 1.526a.48.48 0 0 0-.063.745.525.525 0 0 0 .652.065A8.46 8.46 0 0 1 8 7a8.46 8.46 0 0 1 4.576 1.336c.206.132.48.108.653-.065zm-2.183 2.183c.226-.226.185-.605-.1-.75A6.473 6.473 0 0 0 8 9c-1.06 0-2.062.254-2.946.704-.285.145-.326.524-.1.75l.015.015c.16.16.407.19.611.09A5.478 5.478 0 0 1 8 10c.868 0 1.69.201 2.42.56.203.1.45.07.61-.091l.016-.015zM9.06 12.44c.196-.196.198-.52-.04-.66A1.99 1.99 0 0 0 8 11.5a1.99 1.99 0 0 0-1.02.28c-.238.14-.236.464-.04.66l.706.706a.5.5 0 0 0 .707 0l.707-.707z\" />\n            </svg>\n          </span>{\" \"}\n          <span title={`Worker: ${workerState}\\nSession Id: ${getSessionId()}`}>\n            <svg\n              xmlns=\"http://www.w3.org/2000/svg\"\n              width=\"16\"\n              height=\"16\"\n              fill={workerColor}\n              className=\"bi bi-cpu\"\n              viewBox=\"0 0 16 16\"\n            >\n              <path d=\"M5 0a.5.5 0 0 1 .5.5V2h1V.5a.5.5 0 0 1 1 0V2h1V.5a.5.5 0 0 1 1 0V2h1V.5a.5.5 0 0 1 1 0V2A2.5 2.5 0 0 1 14 4.5h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14a2.5 2.5 0 0 1-2.5 2.5v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14A2.5 2.5 0 0 1 2 11.5H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2A2.5 2.5 0 0 1 4.5 2V.5A.5.5 0 0 1 5 0zm-.5 3A1.5 1.5 0 0 0 3 4.5v7A1.5 1.5 0 0 0 4.5 13h7a1.5 1.5 0 0 0 1.5-1.5v-7A1.5 1.5 0 0 0 11.5 3h-7zM5 6.5A1.5 1.5 0 0 1 6.5 5h3A1.5 1.5 0 0 1 11 6.5v3A1.5 1.5 0 0 1 9.5 11h-3A1.5 1.5 0 0 1 5 9.5v-3zM6.5 6a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5h-3z\" />\n            </svg>\n          </span>\n        </>\n      )}\n      {workerState === WorkerState.Busy && (\n        <span title=\"Worker is busy\">\n          {\" \"}\n          <svg\n            xmlns=\"http://www.w3.org/2000/svg\"\n            width=\"16\"\n            height=\"16\"\n            fill=\"green\"\n            className=\"bi bi-activity\"\n            viewBox=\"0 0 16 16\"\n          >\n            <path\n              fillRule=\"evenodd\"\n              d=\"M6 2a.5.5 0 0 1 .47.33L10 12.036l1.53-4.208A.5.5 0 0 1 12 7.5h3.5a.5.5 0 0 1 0 1h-3.15l-1.88 5.17a.5.5 0 0 1-.94 0L6 3.964 4.47 8.171A.5.5 0 0 1 4 8.5H.5a.5.5 0 0 1 0-1h3.15l1.88-5.17A.5.5 0 0 1 6 2Z\"\n            />\n          </svg>\n        </span>\n      )}\n      <div style={{ float: \"right\" }}>\n        {allowDownload && (\n          <div\n            className=\"dropdown mx-2 btn-group\"\n            style={{\n              display: \"inline\",\n              // width: \"47%\",\n              // float: continuousUpdate ? \"left\" : \"right\",\n            }}\n          >\n            <button\n              className=\"btn btn-sm btn-primary dropdown-toggle\"\n              // style={{ margin: \"0px\", width: \"100%\" }}\n              type=\"button\"\n              data-bs-toggle=\"dropdown\"\n              disabled={waiting}\n            >\n              <svg\n                xmlns=\"http://www.w3.org/2000/svg\"\n                width=\"14\"\n                height=\"14\"\n                viewBox=\"0 0 24 24\"\n                strokeWidth=\"2\"\n                stroke=\"currentColor\"\n                fill=\"none\"\n                strokeLinecap=\"round\"\n                strokeLinejoin=\"round\"\n                style={{ paddingBottom: \"1px\" }}\n              >\n                <path stroke=\"none\" d=\"M0 0h24v24H0z\" fill=\"none\"></path>\n                <path d=\"M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-2\"></path>\n                <path d=\"M7 11l5 5l5 -5\"></path>\n                <path d=\"M12 4l0 12\"></path>\n              </svg>{\" \"}\n              Download\n            </button>\n\n            {/* dropdown-menu-end */}\n            <ul className=\"dropdown-menu my-2\">\n              <li>\n                <button\n                  type=\"button\"\n                  style={{ cursor: \"pointer\" }}\n                  className=\"dropdown-item\"\n                  onClick={() => {\n                    if (staticNotebook) {\n                      handleDownload(\n                        `${axios.defaults.baseURL}${notebookPath}`,\n                        `${notebookTitle}.html`\n                      );\n                    } else {\n                      runDownloadHTML();\n                    }\n                  }}\n                >\n                  <i className=\"fa fa-file-code-o\" aria-hidden=\"true\"></i>{\" \"}\n                  Download as HTML\n                </button>\n              </li>\n              <li>\n                <hr className=\"dropdown-divider\" />\n              </li>\n              <li>\n                <button\n                  type=\"button\"\n                  className=\"dropdown-item\"\n                  onClick={() => {\n                    if (staticNotebook) {\n                      dispatch(exportToPDF(notebookId, notebookPath));\n                    } else {\n                      dispatch(setExportingToPDF(true));\n                      runDownloadPDF();\n                    }\n                  }}\n                >\n                  <i className=\"fa fa-file-pdf-o\" aria-hidden=\"true\"></i>{\" \"}\n                  Download as PDF\n                </button>\n              </li>\n            </ul>\n          </div>\n        )}\n        <button\n          className=\"btn btn-sm btn-primary\"\n          onClick={() => setShowShareModal(!showShareModal)}\n          disabled={waiting}\n        >\n          <svg\n            xmlns=\"http://www.w3.org/2000/svg\"\n            width=\"14\"\n            height=\"14\"\n            viewBox=\"0 0 24 24\"\n            strokeWidth=\"2\"\n            stroke=\"currentColor\"\n            fill=\"none\"\n            strokeLinecap=\"round\"\n            strokeLinejoin=\"round\"\n          >\n            <path stroke=\"none\" d=\"M0 0h24v24H0z\" fill=\"none\"></path>\n            <path d=\"M6 12m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0\"></path>\n            <path d=\"M18 6m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0\"></path>\n            <path d=\"M18 18m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0\"></path>\n            <path d=\"M8.7 10.7l6.6 -3.4\"></path>\n            <path d=\"M8.7 13.3l6.6 3.4\"></path>\n          </svg>{\" \"}\n          Share\n        </button>\n      </div>\n\n      <div\n        className=\"\"\n        style={{\n          position: \"fixed\",\n          top: \"0\",\n          left: \"0\",\n          width: \"100%\",\n          height: \"100%\",\n          background: \"rgba(0, 0, 0, 0.6)\",\n          display: showShareModal ? \"block\" : \"none\",\n        }}\n      >\n        <section\n          className=\"\"\n          style={{\n            position: \"fixed\",\n            width: \"100%\",\n            height: \"auto\",\n            top: \"50%\",\n            left: \"50%\",\n            transform: \"translate(-50%,-50%)\",\n          }}\n        >\n          <div className=\"modal-dialog\">\n            <div className=\"modal-content\">\n              <div className=\"modal-header\">\n                <h3 className=\"modal-title\">\n                  <svg\n                    xmlns=\"http://www.w3.org/2000/svg\"\n                    width=\"24\"\n                    height=\"24\"\n                    viewBox=\"0 0 24 24\"\n                    strokeWidth=\"2\"\n                    stroke=\"currentColor\"\n                    fill=\"none\"\n                    strokeLinecap=\"round\"\n                    strokeLinejoin=\"round\"\n                  >\n                    <path stroke=\"none\" d=\"M0 0h24v24H0z\" fill=\"none\"></path>\n                    <path d=\"M6 12m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0\"></path>\n                    <path d=\"M18 6m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0\"></path>\n                    <path d=\"M18 18m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0\"></path>\n                    <path d=\"M8.7 10.7l6.6 -3.4\"></path>\n                    <path d=\"M8.7 13.3l6.6 3.4\"></path>\n                  </svg>{\" \"}\n                  Share\n                </h3>\n                <button\n                  type=\"button\"\n                  className=\"btn-close\"\n                  aria-label=\"Close\"\n                  onClick={() => setShowShareModal(false)}\n                ></button>\n              </div>\n              <div className=\"modal-body\">\n                <div className=\"py-2\">\n                  <label>App address</label>\n                  <input\n                    type=\"text\"\n                    className=\"form-control\"\n                    disabled={true}\n                    value={window.location.href}\n                  ></input>\n                </div>\n\n                {!noUrlKeys && (\n                  <div className=\"py-2\">\n                    <label>App address with current paramters</label>\n                    <textarea\n                      rows={5}\n                      className=\"form-control\"\n                      disabled={true}\n                      value={window.location.href + urlParams}\n                    />\n                  </div>\n                )}\n                {noUrlKeys && (\n                  <div className=\"py-2\">\n                    There are no <code>url_key</code> defined for any widget.\n                    You can easily share URL to your notebook with preset values\n                    by using <code>url_key</code> in the widget. Please check{\" \"}\n                    <a\n                      href=\"https://runmercury.com/docs/input-widgets/\"\n                      target=\"_blank\"\n                      rel=\"noreferrer\"\n                    >\n                      documentation\n                    </a>\n                    .\n                  </div>\n                )}\n                <div className=\"py-2\"></div>\n              </div>\n              <div className=\"modal-footer\">\n                <button\n                  type=\"button\"\n                  className=\"btn btn-secondary\"\n                  onClick={() => setShowShareModal(false)}\n                >\n                  Close\n                </button>\n              </div>\n            </div>\n          </div>\n        </section>\n      </div>\n    </div>\n  );\n}\n",
         "import React, { useEffect } from \"react\";\nimport { useDispatch } from \"react-redux\";\nimport { setWidgetValue } from \"../slices/notebooksSlice\";\n\ntype ButtonProps = {\n  widgetKey: string;\n  label: string | null;\n  style: string;\n  value: string | boolean | null;\n  disabled: boolean;\n  hidden: boolean;\n  runNb: () => void;\n};\n\nexport default function ButtonWidget({\n  widgetKey,\n  label,\n  style,\n  value,\n  disabled,\n  hidden,\n  runNb,\n}: ButtonProps) {\n  const dispatch = useDispatch();\n\n  let selectedClass = \"btn-primary\";\n  if (style === \"success\") {\n    selectedClass = \"btn-success\";\n  } else if (style === \"danger\") {\n    selectedClass = \"btn-danger\";\n  } else if (style === \"info\") {\n    selectedClass = \"btn-info\";\n  } else if (style === \"warning\") {\n    selectedClass = \"btn-warning\";\n  }\n\n  useEffect(() => {\n    if (value) {\n      runNb();\n    }\n    // eslint-disable-next-line react-hooks/exhaustive-deps\n  }, [value]);\n\n  return (\n    <div className=\"form-group mb-3\" style={{ display: hidden ? \"none\" : \"\" }}>\n      <button\n        type=\"button\"\n        className={`btn ${selectedClass}`}\n        style={{ marginRight: \"10px\", width: \"47%\" }}\n        onClick={() => {\n          dispatch(\n            setWidgetValue({\n              key: widgetKey,\n              value: true,\n            })\n          );\n        }}\n        disabled={disabled}\n      >\n        {label}\n      </button>\n    </div>\n  );\n}\n",
-        "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React from \"react\";\nimport { WorkerState } from \"../slices/wsSlice\";\n\ntype RunButtonProps = {\n  runNb: () => void;\n  waiting: boolean;\n  workerState: WorkerState;\n};\n\nexport default function RunButton({\n  runNb,\n  waiting,\n  workerState,\n}: RunButtonProps) {\n  return (\n    <button\n      type=\"button\"\n      className=\"btn btn-success\"\n      style={{ marginRight: \"10px\", width: \"47%\" }}\n      onClick={() => {\n        runNb();\n      }}\n      disabled={\n        waiting ||\n        // !allFilesUploaded() ||\n        workerState !== WorkerState.Running\n      }\n    >\n      {workerState === WorkerState.Running && (\n        <span>\n          <i className=\"fa fa-play\" aria-hidden=\"true\"></i> Run\n        </span>\n      )}\n      {workerState === WorkerState.Busy && (\n        <span>\n          <svg\n            xmlns=\"http://www.w3.org/2000/svg\"\n            width=\"16\"\n            height=\"16\"\n            fill=\"white\"\n            className=\"bi bi-activity\"\n            viewBox=\"0 0 16 16\"\n          >\n            <path\n              fillRule=\"evenodd\"\n              d=\"M6 2a.5.5 0 0 1 .47.33L10 12.036l1.53-4.208A.5.5 0 0 1 12 7.5h3.5a.5.5 0 0 1 0 1h-3.15l-1.88 5.17a.5.5 0 0 1-.94 0L6 3.964 4.47 8.171A.5.5 0 0 1 4 8.5H.5a.5.5 0 0 1 0-1h3.15l1.88-5.17A.5.5 0 0 1 6 2Z\"\n            />\n          </svg>{\" \"}\n          Busy\n        </span>\n      )}\n      {workerState !== WorkerState.Busy &&\n        workerState !== WorkerState.Running && <span>Waiting ...</span>}\n    </button>\n  );\n}\n",
-        "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React, { useContext } from \"react\";\nimport { useEffect } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\nimport axios from \"axios\";\nimport {\n  exportToPDF,\n  scrapeSlidesHash,\n  setExportingToPDF,\n} from \"../slices/tasksSlice\";\nimport CheckboxWidget from \"../widgets/Checkbox\";\nimport NumericWidget from \"../widgets/Numeric\";\nimport RangeWidget from \"../widgets/Range\";\nimport SelectWidget from \"../widgets/Select\";\nimport SliderWidget from \"../widgets/Slider\";\n\nimport {\n  isCheckboxWidget,\n  isFileWidget,\n  isNumericWidget,\n  isRangeWidget,\n  isSelectWidget,\n  isSliderWidget,\n  isTextWidget,\n  isMarkdownWidget,\n  IWidget,\n  isOutputFilesWidget,\n  isButtonWidget,\n} from \"../widgets/Types\";\n\nimport {\n  clearWidgetsUrlValues,\n  getUrlValuesUsed,\n  getWidgetsInitialized,\n  getWidgetsUrlValues,\n  getWidgetsValues,\n  setSlidesHash,\n  setUrlValuesUsed,\n  setWidgetsInitialized,\n  setWidgetValue,\n  WidgetValueType,\n} from \"../slices/notebooksSlice\";\nimport FileWidget from \"../widgets/File\";\nimport TextWidget from \"../widgets/Text\";\nimport { setShowSideBar, setView } from \"../slices/appSlice\";\nimport { handleDownload } from \"../utils\";\nimport MarkdownWidget from \"../widgets/Markdown\";\n\nimport { WebSocketContext } from \"../websocket/Provider\";\nimport WebSocketStateBar from \"../websocket/StatusBar\";\nimport {\n  downloadHTML,\n  downloadPDF,\n  getWorkerState,\n  runNotebook,\n  WorkerState,\n} from \"../slices/wsSlice\";\nimport ButtonWidget from \"../widgets/Button\";\nimport RunButton from \"./RunButton\";\nimport BlockUi from \"react-block-ui\";\n\ntype SideBarProps = {\n  notebookTitle: string;\n  notebookId: number;\n  notebookSchedule: string;\n  taskCreatedAt: Date;\n  loadingState: string;\n  waiting: boolean;\n  widgetsParams: Record<string, IWidget>;\n  watchMode: boolean;\n  notebookPath: string;\n  displayEmbed: boolean;\n  showFiles: boolean;\n  isPresentation: boolean;\n  notebookParseErrors: string;\n  continuousUpdate: boolean;\n  staticNotebook: boolean;\n  allowDownload: boolean;\n};\n\nexport default function SideBar({\n  notebookTitle,\n  notebookId,\n  notebookSchedule,\n  taskCreatedAt,\n  loadingState,\n  waiting,\n  widgetsParams,\n  watchMode,\n  notebookPath,\n  displayEmbed,\n  showFiles,\n  isPresentation,\n  notebookParseErrors,\n  continuousUpdate,\n  staticNotebook,\n  allowDownload,\n}: SideBarProps) {\n  const dispatch = useDispatch();\n  const widgetsValues: Record<string, WidgetValueType> = useSelector(\n    getWidgetsValues\n  ) as Record<string, WidgetValueType>;\n  const widgetsUrlValues = useSelector(getWidgetsUrlValues);\n  const workerState = useSelector(getWorkerState);\n  const widgetsInitialized = useSelector(getWidgetsInitialized);\n  const urlValuesUsed = useSelector(getUrlValuesUsed);\n\n  const ws = useContext(WebSocketContext);\n\n  const runNb = () => {\n    if (continuousUpdate) {\n      execNb();\n    }\n  };\n\n  const execNb = () => {\n    const slidesHash = scrapeSlidesHash();\n    dispatch(setSlidesHash(slidesHash));\n\n    if (widgetsUrlValues) {\n      let params = {} as Record<string, WidgetValueType>;\n      for (let [key, widgetParams] of Object.entries(widgetsParams)) {\n        if (key in widgetsUrlValues) {\n          params[key] = widgetsUrlValues[key];\n          dispatch(setWidgetValue({ key, value: params[key] }));\n        } else if (key in widgetsValues) {\n          params[key] = widgetsValues[key];\n        }\n      }\n      ws.sendMessage(JSON.stringify(runNotebook(JSON.stringify(params))));\n      dispatch(clearWidgetsUrlValues());\n    } else {\n      ws.sendMessage(\n        JSON.stringify(runNotebook(JSON.stringify(widgetsValues)))\n      );\n    }\n  };\n\n  useEffect(() => {\n    if (widgetsInitialized && urlValuesUsed) {\n      execNb();\n      dispatch(setUrlValuesUsed(false));\n      dispatch(setWidgetsInitialized(false));\n    }\n    // eslint-disable-next-line react-hooks/exhaustive-deps\n  }, [widgetsInitialized, urlValuesUsed]);\n\n  const runDownloadHTML = () => {\n    if (!staticNotebook) {\n      ws.sendMessage(JSON.stringify(downloadHTML()));\n    }\n  };\n\n  const runDownloadPDF = () => {\n    if (!staticNotebook) {\n      ws.sendMessage(JSON.stringify(downloadPDF()));\n    }\n  };\n\n  useEffect(() => {\n    if (widgetsParams) {\n      for (let [key, widgetParams] of Object.entries(widgetsParams)) {\n        if (key in widgetsValues) {\n          continue;\n        }\n\n        if (widgetParams.input === \"file\") {\n          dispatch(setWidgetValue({ key, value: [] as string[] }));\n        } else if (widgetParams.input === \"text\") {\n          dispatch(\n            setWidgetValue({\n              key,\n              value: widgetParams.value ? widgetParams.value : \"\",\n            })\n          );\n        } else if (isMarkdownWidget(widgetParams)) {\n          // do nothing\n          // dont put value into store\n        } else if (isOutputFilesWidget(widgetParams)) {\n          dispatch(setWidgetValue({ key, value: \"output-dir\" }));\n        } else {\n          dispatch(setWidgetValue({ key, value: widgetParams.value }));\n        }\n      }\n    }\n  }, [dispatch, widgetsParams, widgetsValues]);\n\n  let widgets = [];\n  let fileKeys = [] as string[]; // keys to file widgets, all need to be selected to enable RUN button\n\n  if (widgetsParams && !staticNotebook) {\n    // sort widgets keys based on cell index and code line number\n    let widgetKeys = [];\n    for (let key of Object.keys(widgetsParams)) {\n      const parts = key.split(\".\");\n      widgetKeys.push([key, parseFloat(`${parts[1]}.${parts[2]}`)]);\n    }\n    widgetKeys.sort(function (a, b) {\n      const a1 = a[1] as number;\n      const b1 = b[1] as number;\n      return a1 - b1;\n    });\n\n    for (let wKey of widgetKeys) {\n      const key = wKey[0] as string;\n      const widgetParams = widgetsParams[key];\n\n      if (isSelectWidget(widgetParams)) {\n        widgets.push(\n          <SelectWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as string}\n            choices={widgetParams?.choices}\n            multi={widgetParams?.multi}\n            key={key}\n            runNb={runNb}\n            url_key={widgetParams?.url_key}\n\n          />\n        );\n      } else if (isCheckboxWidget(widgetParams)) {\n        widgets.push(\n          <CheckboxWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as boolean}\n            key={key}\n            runNb={runNb}\n            url_key={widgetParams?.url_key}\n          />\n        );\n      } else if (isNumericWidget(widgetParams)) {\n        widgets.push(\n          <NumericWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as number}\n            min={widgetParams?.min}\n            max={widgetParams?.max}\n            step={widgetParams?.step}\n            key={key}\n            runNb={runNb}\n            continuousUpdate={continuousUpdate}\n            url_key={widgetParams?.url_key}\n          />\n        );\n      } else if (isSliderWidget(widgetParams)) {\n        widgets.push(\n          <SliderWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as number}\n            min={widgetParams?.min}\n            max={widgetParams?.max}\n            step={widgetParams?.step}\n            vertical={widgetParams?.vertical}\n            key={key}\n            runNb={runNb}\n            url_key={widgetParams?.url_key}\n          />\n        );\n      } else if (isRangeWidget(widgetParams)) {\n        widgets.push(\n          <RangeWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as [number, number]}\n            min={widgetParams?.min}\n            max={widgetParams?.max}\n            step={widgetParams?.step}\n            vertical={widgetParams?.vertical}\n            key={key}\n            runNb={runNb}\n            url_key={widgetParams.url_key}\n          />\n        );\n      } else if (isFileWidget(widgetParams)) {\n        widgets.push(\n          <FileWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            maxFileSize={widgetParams?.maxFileSize}\n            key={key}\n            value={widgetsValues[key] as string[]}\n            runNb={runNb}\n          />\n        );\n        fileKeys.push(key);\n      } else if (isTextWidget(widgetParams)) {\n        widgets.push(\n          <TextWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as string}\n            rows={widgetParams?.rows}\n            key={key}\n            runNb={runNb}\n            continuousUpdate={continuousUpdate}\n            url_key={widgetParams?.url_key}\n          />\n        );\n      } else if (isMarkdownWidget(widgetParams)) {\n        widgets.push(\n          <MarkdownWidget\n            value={widgetParams.value as string}\n            disabled={waiting}\n            key={key}\n          />\n        );\n      } else if (isButtonWidget(widgetParams)) {\n        widgets.push(\n          <ButtonWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as boolean}\n            style={widgetParams?.style}\n            key={key}\n            runNb={runNb}\n          />\n        );\n      } else if (isOutputFilesWidget(widgetParams)) {\n        // do nothing\n      } else {\n        console.log(\"Unknown widget type\", widgetParams);\n      }\n    }\n  }\n\n  let additionalStyle = {};\n  if (displayEmbed) {\n    additionalStyle = { padding: \"0px\" };\n  }\n\n  const addSpaceInsteadTitle =\n    notebookTitle === undefined ||\n    notebookTitle === null ||\n    notebookTitle === \"\";\n\n  return (\n    <nav\n      id=\"sidebarMenu\"\n      className=\"col-lg-3 d-md-block bg-light sidebar\"\n      style={{ ...additionalStyle, overflowY: \"auto\" }}\n    >\n      <BlockUi blocking={false} message=\"\">\n        <div className=\"position-sticky p-3\">\n          <h4>\n            {notebookTitle}\n            <button\n              className=\"btn btn-sm  btn-outline-primary\"\n              type=\"button\"\n              style={{\n                float: \"right\",\n                zIndex: \"101\",\n              }}\n              onClick={() => dispatch(setShowSideBar(false))}\n              data-toggle=\"tooltip\"\n              data-placement=\"right\"\n              title=\"Hide sidebar\"\n            >\n              <i className=\"fa fa-chevron-left\" aria-hidden=\"true\" />\n            </button>\n          </h4>\n\n          <div style={{ padding: \"0px\" }}>\n            <form>\n              {widgets}\n              {addSpaceInsteadTitle && <div style={{ padding: \"15px\" }}></div>}\n              <div className=\"form-group mb-3 pb-1 pt-2\">\n                {!continuousUpdate && (\n                  <RunButton\n                    runNb={execNb}\n                    waiting={waiting}\n                    workerState={workerState}\n                  />\n                )}\n                {allowDownload && (\n                  <div\n                    className=\"dropdown\"\n                    style={{\n                      width: \"47%\",\n                      float: continuousUpdate ? \"left\" : \"right\",\n                    }}\n                  >\n                    <button\n                      className=\"btn btn-primary dropdown-toggle\"\n                      style={{ margin: \"0px\", width: \"100%\" }}\n                      type=\"button\"\n                      data-bs-toggle=\"dropdown\"\n                      disabled={waiting}\n                    >\n                      Download\n                    </button>\n\n                    <ul className=\"dropdown-menu dropdown-menu-end\">\n                      <li>\n                        <a\n                          style={{ cursor: \"pointer\" }}\n                          className=\"dropdown-item\"\n                          onClick={() => {\n                            if (staticNotebook) {\n                              handleDownload(\n                                `${axios.defaults.baseURL}${notebookPath}`,\n                                `${notebookTitle}.html`\n                              );\n                            } else {\n                              runDownloadHTML();\n\n                              //handleDownload(\n                              //  `${axios.defaults.baseURL}${notebookPath}`,\n                              //</li>  `${notebookTitle}.html`\n                              //);\n                            }\n                          }}\n                        >\n                          <i\n                            className=\"fa fa-file-code-o\"\n                            aria-hidden=\"true\"\n                          ></i>{\" \"}\n                          Download as HTML\n                        </a>\n                      </li>\n                      <li>\n                        <hr className=\"dropdown-divider\" />\n                      </li>\n                      <li>\n                        <button\n                          type=\"button\"\n                          className=\"dropdown-item\"\n                          onClick={() => {\n                            if (staticNotebook) {\n                              dispatch(exportToPDF(notebookId, notebookPath));\n                            } else {\n                              dispatch(setExportingToPDF(true));\n                              runDownloadPDF();\n                            }\n                          }}\n                        >\n                          <i\n                            className=\"fa fa-file-pdf-o\"\n                            aria-hidden=\"true\"\n                          ></i>{\" \"}\n                          Download as PDF\n                        </button>\n                      </li>\n                    </ul>\n                  </div>\n                )}\n              </div>\n\n              {/* {notebookSchedule !== \"\" && (\n                <div className=\"alert alert-success mb-3\" role=\"alert\">\n                  <p>\n                    <i className=\"fa fa-clock-o\" aria-hidden=\"true\"></i>{\" \"}\n                    Scheduled notebook at '{notebookSchedule}'.\n                  </p>\n\n                  {taskCreatedAt && (\n                    <p>\n                      {\" \"}\n                      <i className=\"fa fa-calendar\" aria-hidden=\"true\"></i> Last\n                      execution at {taskCreatedAt}.\n                    </p>\n                  )}\n                  <div>\n                    <i className=\"fa fa-refresh\" aria-hidden=\"true\"></i> Website\n                    refresh every minute.\n                  </div>\n                </div>\n              )} */}\n\n              {continuousUpdate && (\n                <div>\n                  {/* add some space */}\n                  <br />\n                </div>\n              )}\n\n              {/* {waiting && workerState === WorkerState.Busy && (\n                <div className=\"alert alert-success mb-3 mt-3\" role=\"alert\">\n                  <i className=\"fa fa-cogs\" aria-hidden=\"true\"></i> Notebook is\n                  executed. Please wait.\n                </div>\n              )} */}\n\n              {workerState === WorkerState.MaxIdleTimeReached && (\n                <div className=\"alert alert-info mb-3 mt-3\" role=\"alert\">\n                  <i className=\"fa fa-info-circle\" aria-hidden=\"true\"></i> Your\n                  worker was idle for too long, that's why we have stopped it.\n                  Do you need a worker?\n                  <br />\n                  <button\n                    className=\"btn btn-sm btn-primary my-2\"\n                    onClick={() => window.location.reload()}\n                  >\n                    Restart worker\n                  </button>\n                </div>\n              )}\n              {workerState === WorkerState.MaxRunTimeReached && (\n                <div className=\"alert alert-info mb-3 mt-3\" role=\"alert\">\n                  <i className=\"fa fa-info-circle\" aria-hidden=\"true\"></i> Your\n                  worker was running for too long, that's why we have stopped\n                  it. Do you need a worker?\n                  <br />\n                  <button\n                    className=\"btn btn-sm btn-primary my-2\"\n                    onClick={() => window.location.reload()}\n                  >\n                    Restart worker\n                  </button>\n                </div>\n              )}\n              {waiting &&\n                (workerState === WorkerState.Unknown ||\n                  workerState === WorkerState.Queued) && (\n                  <div className=\"alert alert-warning mb-3 mt-3\" role=\"alert\">\n                    <i className=\"fa fa-cogs\" aria-hidden=\"true\"></i> Waiting\n                    for worker ...\n                  </div>\n                )}\n              {waiting && workerState === WorkerState.Starting && (\n                <div className=\"alert alert-success mb-3 mt-3\" role=\"alert\">\n                  <i className=\"fa fa-cogs\" aria-hidden=\"true\"></i> Initializing\n                  worker ...\n                </div>\n              )}\n              {watchMode && (\n                <div className=\"alert alert-secondary mb-3 mt-3\" role=\"alert\">\n                  <i className=\"fa fa-refresh\" aria-hidden=\"true\"></i> Notebook\n                  in watch mode. All changes to Notebook will be automatically\n                  visible in Mercury.\n                </div>\n              )}\n\n              {isPresentation && (\n                <div className=\"alert alert-primary mb-3\" role=\"alert\">\n                  <i className=\"fa fa-television\" aria-hidden=\"true\"></i> Click\n                  on presentation and press <b>F</b> for full screen. Press{\" \"}\n                  <b>Esc</b> to quit.\n                  <br />\n                  <br />\n                  <i className=\"fa fa-arrows\" aria-hidden=\"true\"></i> Click on\n                  presentation and press <b>Esc</b> to navigate slides.\n                </div>\n              )}\n\n              {/* {notebookParseErrors && (\n                <div className=\"alert alert-danger mb-3\" role=\"alert\">\n                  <i\n                    className=\"fa fa-exclamation-circle\"\n                    aria-hidden=\"true\"\n                  ></i>{\" \"}\n                  <b>Errors in the YAML</b>\n                  <br />\n                  {notebookParseErrors}\n                </div>\n              )} */}\n            </form>\n          </div>\n\n          {/* <hr style={{ marginTop: \"20px\", marginBottom: \"20px\" }} />\n          <div>\n            {!watchMode && <SelectExecutionHistory disabled={waiting} displayNb={displayNb} />}\n            {!staticNotebook && (\n              <div>\n                <button\n                  className=\"btn btn-sm btn-outline-primary\"\n                  onClick={() => {\n                    saveNb();\n                  }}\n                  style={{ border: \"none\" }}\n                  disabled={waiting}\n                  title=\"Click to save current run\"\n                >\n                  <i className=\"fa fa-floppy-o\" aria-hidden=\"true\"></i> Save run\n                </button>\n                <button\n                  className=\"btn btn-sm btn-outline-danger\"\n                  onClick={() => {\n                    dispatch(clearTasks(notebookId));\n                    dispatch(fetchNotebook(notebookId));\n                  }}\n                  style={{ border: \"none\" }}\n                  disabled={waiting}\n                  title=\"Click to clear all previous runs of the notebook\"\n                >\n                  <i className=\"fa fa-times-circle\" aria-hidden=\"true\"></i>{\" \"}\n                  Delete runs\n                </button>\n              </div>\n            )}\n          </div>\n           */}\n          {showFiles && (\n            <div>\n              <hr />\n              <button\n                className=\"btn btn-sm btn-outline-secondary\"\n                style={{\n                  border: \"none\",\n                  //fontWeight: 500,\n                }}\n                onClick={() => {\n                  dispatch(setView(\"app\"));\n                }}\n              >\n                <i className=\"fa fa-laptop\" aria-hidden=\"true\"></i> App\n              </button>\n\n              <button\n                className=\"btn btn-sm btn-outline-secondary\"\n                style={{\n                  border: \"none\",\n                  //fontWeight: 500,\n                }}\n                onClick={() => {\n                  dispatch(setView(\"files\"));\n                }}\n              >\n                <i className=\"fa fa-folder-open-o\" aria-hidden=\"true\"></i>{\" \"}\n                Output Files\n              </button>\n            </div>\n          )}\n          {notebookId !== undefined && !staticNotebook && (\n            <div>\n              <hr />\n              <div style={{ paddingLeft: \"10px\" }}>\n                <WebSocketStateBar />{\" \"}\n              </div>\n            </div>\n          )}\n        </div>\n      </BlockUi>\n    </nav>\n  );\n}\n",
+        "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React from \"react\";\nimport { WorkerState } from \"../slices/wsSlice\";\n\ntype RunButtonProps = {\n  runNb: () => void;\n  waiting: boolean;\n  workerState: WorkerState;\n};\n\nexport default function RunButton({\n  runNb,\n  waiting,\n  workerState,\n}: RunButtonProps) {\n  return (\n    <button\n      type=\"button\"\n      className=\"btn btn-success\"\n      style={{ marginRight: \"10px\", width: \"100%\" }}\n      onClick={() => {\n        runNb();\n      }}\n      disabled={\n        waiting ||\n        // !allFilesUploaded() ||\n        workerState !== WorkerState.Running\n      }\n    >\n      {workerState === WorkerState.Running && (\n        <span>\n          <i className=\"fa fa-play\" aria-hidden=\"true\"></i> Run\n        </span>\n      )}\n      {workerState === WorkerState.Busy && (\n        <span>\n          <svg\n            xmlns=\"http://www.w3.org/2000/svg\"\n            width=\"16\"\n            height=\"16\"\n            fill=\"white\"\n            className=\"bi bi-activity\"\n            viewBox=\"0 0 16 16\"\n          >\n            <path\n              fillRule=\"evenodd\"\n              d=\"M6 2a.5.5 0 0 1 .47.33L10 12.036l1.53-4.208A.5.5 0 0 1 12 7.5h3.5a.5.5 0 0 1 0 1h-3.15l-1.88 5.17a.5.5 0 0 1-.94 0L6 3.964 4.47 8.171A.5.5 0 0 1 4 8.5H.5a.5.5 0 0 1 0-1h3.15l1.88-5.17A.5.5 0 0 1 6 2Z\"\n            />\n          </svg>{\" \"}\n          Busy\n        </span>\n      )}\n      {workerState !== WorkerState.Busy &&\n        workerState !== WorkerState.Running && <span>Waiting ...</span>}\n    </button>\n  );\n}\n",
+        "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React, { useContext } from \"react\";\nimport { useEffect } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\nimport axios from \"axios\";\nimport {\n  exportToPDF,\n  scrapeSlidesHash,\n  setExportingToPDF,\n} from \"../slices/tasksSlice\";\nimport CheckboxWidget from \"../widgets/Checkbox\";\nimport NumericWidget from \"../widgets/Numeric\";\nimport RangeWidget from \"../widgets/Range\";\nimport SelectWidget from \"../widgets/Select\";\nimport SliderWidget from \"../widgets/Slider\";\n\nimport {\n  isCheckboxWidget,\n  isFileWidget,\n  isNumericWidget,\n  isRangeWidget,\n  isSelectWidget,\n  isSliderWidget,\n  isTextWidget,\n  isMarkdownWidget,\n  IWidget,\n  isOutputFilesWidget,\n  isButtonWidget,\n} from \"../widgets/Types\";\n\nimport {\n  clearWidgetsUrlValues,\n  getUrlValuesUsed,\n  getWidgetsInitialized,\n  getWidgetsUrlValues,\n  getWidgetsValues,\n  setSlidesHash,\n  setUrlValuesUsed,\n  setWidgetsInitialized,\n  setWidgetValue,\n  WidgetValueType,\n} from \"../slices/notebooksSlice\";\nimport FileWidget from \"../widgets/File\";\nimport TextWidget from \"../widgets/Text\";\nimport { setShowSideBar, setView } from \"../slices/appSlice\";\nimport { handleDownload } from \"../utils\";\nimport MarkdownWidget from \"../widgets/Markdown\";\n\nimport { WebSocketContext } from \"../websocket/Provider\";\nimport WebSocketStateBar from \"./StatusBar\";\nimport {\n  downloadHTML,\n  downloadPDF,\n  getWorkerState,\n  runNotebook,\n  WorkerState,\n} from \"../slices/wsSlice\";\nimport ButtonWidget from \"../widgets/Button\";\nimport RunButton from \"./RunButton\";\nimport BlockUi from \"react-block-ui\";\n\ntype SideBarProps = {\n  notebookTitle: string;\n  notebookId: number;\n  notebookSchedule: string;\n  taskCreatedAt: Date;\n  loadingState: string;\n  waiting: boolean;\n  widgetsParams: Record<string, IWidget>;\n  watchMode: boolean;\n  notebookPath: string;\n  displayEmbed: boolean;\n  showFiles: boolean;\n  isPresentation: boolean;\n  notebookParseErrors: string;\n  continuousUpdate: boolean;\n  staticNotebook: boolean;\n  allowDownload: boolean;\n};\n\nexport default function SideBar({\n  notebookTitle,\n  notebookId,\n  notebookSchedule,\n  taskCreatedAt,\n  loadingState,\n  waiting,\n  widgetsParams,\n  watchMode,\n  notebookPath,\n  displayEmbed,\n  showFiles,\n  isPresentation,\n  notebookParseErrors,\n  continuousUpdate,\n  staticNotebook,\n  allowDownload,\n}: SideBarProps) {\n  const dispatch = useDispatch();\n  const widgetsValues: Record<string, WidgetValueType> = useSelector(\n    getWidgetsValues\n  ) as Record<string, WidgetValueType>;\n  const widgetsUrlValues = useSelector(getWidgetsUrlValues);\n  const workerState = useSelector(getWorkerState);\n  const widgetsInitialized = useSelector(getWidgetsInitialized);\n  const urlValuesUsed = useSelector(getUrlValuesUsed);\n\n  const ws = useContext(WebSocketContext);\n\n  const runNb = () => {\n    if (continuousUpdate) {\n      execNb();\n    }\n  };\n\n  const execNb = () => {\n    const slidesHash = scrapeSlidesHash();\n    dispatch(setSlidesHash(slidesHash));\n\n    if (widgetsUrlValues) {\n      let params = {} as Record<string, WidgetValueType>;\n      for (let [key, widgetParams] of Object.entries(widgetsParams)) {\n        if (key in widgetsUrlValues) {\n          params[key] = widgetsUrlValues[key];\n          dispatch(setWidgetValue({ key, value: params[key] }));\n        } else if (key in widgetsValues) {\n          params[key] = widgetsValues[key];\n        }\n      }\n      ws.sendMessage(JSON.stringify(runNotebook(JSON.stringify(params))));\n      dispatch(clearWidgetsUrlValues());\n    } else {\n      ws.sendMessage(\n        JSON.stringify(runNotebook(JSON.stringify(widgetsValues)))\n      );\n    }\n  };\n\n  useEffect(() => {\n    if (widgetsInitialized && urlValuesUsed) {\n      execNb();\n      dispatch(setUrlValuesUsed(false));\n      dispatch(setWidgetsInitialized(false));\n    }\n    // eslint-disable-next-line react-hooks/exhaustive-deps\n  }, [widgetsInitialized, urlValuesUsed]);\n\n  const runDownloadHTML = () => {\n    if (!staticNotebook) {\n      ws.sendMessage(JSON.stringify(downloadHTML()));\n    }\n  };\n\n  const runDownloadPDF = () => {\n    if (!staticNotebook) {\n      ws.sendMessage(JSON.stringify(downloadPDF()));\n    }\n  };\n\n  useEffect(() => {\n    if (widgetsParams) {\n      for (let [key, widgetParams] of Object.entries(widgetsParams)) {\n        if (key in widgetsValues) {\n          continue;\n        }\n\n        if (widgetParams.input === \"file\") {\n          dispatch(setWidgetValue({ key, value: [] as string[] }));\n        } else if (widgetParams.input === \"text\") {\n          dispatch(\n            setWidgetValue({\n              key,\n              value: widgetParams.value ? widgetParams.value : \"\",\n            })\n          );\n        } else if (isMarkdownWidget(widgetParams)) {\n          // do nothing\n          // dont put value into store\n        } else if (isOutputFilesWidget(widgetParams)) {\n          dispatch(setWidgetValue({ key, value: \"output-dir\" }));\n        } else {\n          dispatch(setWidgetValue({ key, value: widgetParams.value }));\n        }\n      }\n    }\n  }, [dispatch, widgetsParams, widgetsValues]);\n\n  let widgets = [];\n  let fileKeys = [] as string[]; // keys to file widgets, all need to be selected to enable RUN button\n\n  if (widgetsParams && !staticNotebook) {\n    // sort widgets keys based on cell index and code line number\n    let widgetKeys = [];\n    for (let key of Object.keys(widgetsParams)) {\n      const parts = key.split(\".\");\n      widgetKeys.push([key, parseFloat(`${parts[1]}.${parts[2]}`)]);\n    }\n    widgetKeys.sort(function (a, b) {\n      const a1 = a[1] as number;\n      const b1 = b[1] as number;\n      return a1 - b1;\n    });\n\n    for (let wKey of widgetKeys) {\n      const key = wKey[0] as string;\n      const widgetParams = widgetsParams[key];\n\n      if (isSelectWidget(widgetParams)) {\n        widgets.push(\n          <SelectWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as string}\n            choices={widgetParams?.choices}\n            multi={widgetParams?.multi}\n            key={key}\n            runNb={runNb}\n            url_key={widgetParams?.url_key}\n          />\n        );\n      } else if (isCheckboxWidget(widgetParams)) {\n        widgets.push(\n          <CheckboxWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as boolean}\n            key={key}\n            runNb={runNb}\n            url_key={widgetParams?.url_key}\n          />\n        );\n      } else if (isNumericWidget(widgetParams)) {\n        widgets.push(\n          <NumericWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as number}\n            min={widgetParams?.min}\n            max={widgetParams?.max}\n            step={widgetParams?.step}\n            key={key}\n            runNb={runNb}\n            continuousUpdate={continuousUpdate}\n            url_key={widgetParams?.url_key}\n          />\n        );\n      } else if (isSliderWidget(widgetParams)) {\n        widgets.push(\n          <SliderWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as number}\n            min={widgetParams?.min}\n            max={widgetParams?.max}\n            step={widgetParams?.step}\n            vertical={widgetParams?.vertical}\n            key={key}\n            runNb={runNb}\n            url_key={widgetParams?.url_key}\n          />\n        );\n      } else if (isRangeWidget(widgetParams)) {\n        widgets.push(\n          <RangeWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as [number, number]}\n            min={widgetParams?.min}\n            max={widgetParams?.max}\n            step={widgetParams?.step}\n            vertical={widgetParams?.vertical}\n            key={key}\n            runNb={runNb}\n            url_key={widgetParams.url_key}\n          />\n        );\n      } else if (isFileWidget(widgetParams)) {\n        widgets.push(\n          <FileWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            maxFileSize={widgetParams?.maxFileSize}\n            key={key}\n            value={widgetsValues[key] as string[]}\n            runNb={runNb}\n          />\n        );\n        fileKeys.push(key);\n      } else if (isTextWidget(widgetParams)) {\n        widgets.push(\n          <TextWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as string}\n            rows={widgetParams?.rows}\n            key={key}\n            runNb={runNb}\n            continuousUpdate={continuousUpdate}\n            url_key={widgetParams?.url_key}\n          />\n        );\n      } else if (isMarkdownWidget(widgetParams)) {\n        widgets.push(\n          <MarkdownWidget\n            value={widgetParams.value as string}\n            disabled={waiting}\n            key={key}\n          />\n        );\n      } else if (isButtonWidget(widgetParams)) {\n        widgets.push(\n          <ButtonWidget\n            widgetKey={key}\n            disabled={waiting || widgetParams?.disabled}\n            hidden={widgetParams?.hidden}\n            label={widgetParams?.label}\n            value={widgetsValues[key] as boolean}\n            style={widgetParams?.style}\n            key={key}\n            runNb={runNb}\n          />\n        );\n      } else if (isOutputFilesWidget(widgetParams)) {\n        // do nothing\n      } else {\n        console.log(\"Unknown widget type\", widgetParams);\n      }\n    }\n  }\n\n  let additionalStyle = {};\n  if (displayEmbed) {\n    additionalStyle = { padding: \"0px\" };\n  }\n\n  const addSpaceInsteadTitle =\n    notebookTitle === undefined ||\n    notebookTitle === null ||\n    notebookTitle === \"\";\n\n  return (\n    <nav\n      id=\"sidebarMenu\"\n      className=\"col-lg-3 d-md-block bg-light sidebar\"\n      style={{ ...additionalStyle, overflowY: \"auto\" }}\n    >\n      <BlockUi blocking={false} message=\"\">\n        <div className=\"position-sticky p-3\">\n          <h4>\n            {notebookTitle}\n            <button\n              className=\"btn btn-sm  btn-outline-primary\"\n              type=\"button\"\n              style={{\n                float: \"right\",\n                zIndex: \"101\",\n              }}\n              onClick={() => dispatch(setShowSideBar(false))}\n              data-toggle=\"tooltip\"\n              data-placement=\"right\"\n              title=\"Hide sidebar\"\n            >\n              <i className=\"fa fa-chevron-left\" aria-hidden=\"true\" />\n            </button>\n          </h4>\n\n          <div style={{ padding: \"0px\" }}>\n            <form>\n              {widgets}\n\n              {addSpaceInsteadTitle && <div style={{ padding: \"15px\" }}></div>}\n\n              <div className=\"form-group mb-3 pb-1 pt-2\">\n                {!continuousUpdate && (\n                  <RunButton\n                    runNb={execNb}\n                    waiting={waiting}\n                    workerState={workerState}\n                  />\n                )}\n              </div>\n\n              {workerState === WorkerState.UsageLimitReached && (\n                <div className=\"alert alert-info mb-3 mt-3\" role=\"alert\">\n                  <i className=\"fa fa-info-circle\" aria-hidden=\"true\"></i> Usage\n                  limit was reached. Please upgrade the plan.\n                </div>\n              )}\n\n              {workerState === WorkerState.MaxIdleTimeReached && (\n                <div className=\"alert alert-info mb-3 mt-3\" role=\"alert\">\n                  <i className=\"fa fa-info-circle\" aria-hidden=\"true\"></i> Your\n                  worker was idle for too long, that's why we have stopped it.\n                  Do you need a worker?\n                  <br />\n                  <button\n                    className=\"btn btn-sm btn-primary my-2\"\n                    onClick={() => window.location.reload()}\n                  >\n                    Restart worker\n                  </button>\n                </div>\n              )}\n              {workerState === WorkerState.MaxRunTimeReached && (\n                <div className=\"alert alert-info mb-3 mt-3\" role=\"alert\">\n                  <i className=\"fa fa-info-circle\" aria-hidden=\"true\"></i> Your\n                  worker was running for too long, that's why we have stopped\n                  it. Do you need a worker?\n                  <br />\n                  <button\n                    className=\"btn btn-sm btn-primary my-2\"\n                    onClick={() => window.location.reload()}\n                  >\n                    Restart worker\n                  </button>\n                </div>\n              )}\n              {waiting &&\n                (workerState === WorkerState.Unknown ||\n                  workerState === WorkerState.Queued) && (\n                  <div className=\"alert alert-warning mb-3 mt-3\" role=\"alert\">\n                    <i className=\"fa fa-cogs\" aria-hidden=\"true\"></i> Waiting\n                    for worker ...\n                  </div>\n                )}\n              {waiting && workerState === WorkerState.Starting && (\n                <div className=\"alert alert-success mb-3 mt-3\" role=\"alert\">\n                  <i className=\"fa fa-cogs\" aria-hidden=\"true\"></i> Initializing\n                  worker ...\n                </div>\n              )}\n              {watchMode && (\n                <div className=\"alert alert-secondary mb-3 mt-3\" role=\"alert\">\n                  <i className=\"fa fa-refresh\" aria-hidden=\"true\"></i> Notebook\n                  in watch mode. All changes to Notebook will be automatically\n                  visible in Mercury.\n                </div>\n              )}\n\n              {isPresentation && (\n                <div className=\"alert alert-primary mb-3\" role=\"alert\">\n                  <i className=\"fa fa-television\" aria-hidden=\"true\"></i> Click\n                  on presentation and press <b>F</b> for full screen. Press{\" \"}\n                  <b>Esc</b> to quit.\n                  <br />\n                  <br />\n                  <i className=\"fa fa-arrows\" aria-hidden=\"true\"></i> Click on\n                  presentation and press <b>Esc</b> to navigate slides.\n                </div>\n              )}\n\n              {/* {notebookParseErrors && (\n                <div className=\"alert alert-danger mb-3\" role=\"alert\">\n                  <i\n                    className=\"fa fa-exclamation-circle\"\n                    aria-hidden=\"true\"\n                  ></i>{\" \"}\n                  <b>Errors in the YAML</b>\n                  <br />\n                  {notebookParseErrors}\n                </div>\n              )} */}\n            </form>\n          </div>\n\n          {showFiles && (\n            <div>\n              <hr />\n              <button\n                className=\"btn btn-sm btn-outline-secondary\"\n                style={{\n                  border: \"none\",\n                  //fontWeight: 500,\n                }}\n                onClick={() => {\n                  dispatch(setView(\"app\"));\n                }}\n              >\n                <i className=\"fa fa-laptop\" aria-hidden=\"true\"></i> App\n              </button>\n\n              <button\n                className=\"btn btn-sm btn-outline-secondary\"\n                style={{\n                  border: \"none\",\n                  //fontWeight: 500,\n                }}\n                onClick={() => {\n                  dispatch(setView(\"files\"));\n                }}\n              >\n                <i className=\"fa fa-folder-open-o\" aria-hidden=\"true\"></i>{\" \"}\n                Output Files\n              </button>\n            </div>\n          )}\n\n          <div>\n            <hr />\n            <div style={{ paddingLeft: \"10px\" }}>\n              <WebSocketStateBar\n                notebookId={notebookId}\n                notebookPath={notebookPath}\n                notebookTitle={notebookTitle}\n                staticNotebook={staticNotebook}\n                allowDownload={allowDownload}\n                waiting={waiting}\n                continuousUpdate={continuousUpdate}\n                runDownloadHTML={runDownloadHTML}\n                runDownloadPDF={runDownloadPDF}\n                widgetsValues={widgetsValues}\n                widgetsParams={widgetsParams}\n              />{\" \"}\n            </div>\n          </div>\n        </div>\n      </BlockUi>\n    </nav>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React, { useEffect } from \"react\";\nimport axios from \"axios\";\nimport useWindowDimensions from \"./WindowDimensions\";\n\nimport BlockUi from \"react-block-ui\";\nimport { useDispatch, useSelector } from \"react-redux\";\nimport { getNotebookSrc, setNotebookSrc } from \"../slices/wsSlice\";\n\nimport InnerHTML from \"dangerously-set-html-content\";\nimport { getSelectedNotebook } from \"../slices/notebooksSlice\";\n\ntype MainViewProps = {\n  appView: string;\n  loadingState: string;\n  notebookPath: string;\n  waiting: boolean;\n  errorMsg: string;\n  watchMode: boolean;\n  displayEmbed: boolean;\n  username: string;\n  slidesHash: string;\n  columnsWidth: number;\n  isPresentation: boolean;\n  fullScreen: boolean;\n};\n\nexport default function MainView({\n  appView,\n  loadingState,\n  notebookPath,\n  waiting,\n  errorMsg,\n  watchMode,\n  displayEmbed,\n  username,\n  slidesHash,\n  columnsWidth,\n  isPresentation,\n  fullScreen,\n}: MainViewProps) {\n  const { height } = useWindowDimensions();\n\n  const iframeHeight = displayEmbed ? height - 10 : height - 58;\n  const dispatch = useDispatch();\n  let nb = useSelector(getSelectedNotebook);\n  let notebookSrc = useSelector(getNotebookSrc);\n\n  let showCode = false;\n  if (nb !== undefined && nb.params !== undefined) {\n    if (\n      nb.params[\"show-code\"] !== undefined &&\n      nb.params[\"show-code\"] !== null\n    ) {\n      showCode = nb.params[\"show-code\"];\n    }\n  }\n\n  if (notebookSrc !== \"\" && !isPresentation) {\n    notebookSrc = \"<script>init_mathjax();</script>\" + notebookSrc;\n\n    if (!showCode) {\n      const hideCodeStyle = `<style type=\"text/css\">\n      .jp-mod-noOutputs {\n          padding: 0px; \n      }\n      .jp-mod-noInput {\n        padding-top: 0px;\n        padding-bottom: 0px;\n      }\n      </style>`;\n      notebookSrc = hideCodeStyle + notebookSrc;\n    }\n  }\n\n  if (notebookSrc !== \"\" && isPresentation && slidesHash !== \"\") {\n    if (notebookSrc.indexOf(\"Reveal.slide(\") === -1) {\n      const splitted = slidesHash.split(\"/\");\n      let injectCode = \"\";\n      if (splitted.length === 4) {\n        injectCode = `Reveal.slide(${splitted[1]}, ${splitted[2]}, ${splitted[3]});`;\n      } else if (splitted.length === 3) {\n        injectCode = `Reveal.slide(${splitted[1]}, ${splitted[2]});`;\n      } else if (splitted.length === 2) {\n        injectCode = `Reveal.slide(${splitted[1]});`;\n      }\n\n      if (injectCode !== \"\") {\n        notebookSrc = notebookSrc.replace(\n          \"setScrollingSlide);\",\n          `setScrollingSlide); try{ ${injectCode} } catch(error) {}`\n        );\n      }\n    }\n  }\n\n  useEffect(() => {\n    if (notebookPath !== undefined) {\n      axios\n        .get(`${notebookPath}${slidesHash}`)\n        .then((response) => {\n          let nbSrc = response.data;\n          if (!isPresentation) {\n            nbSrc = nbSrc.replace(/<head>[\\s\\S]*?<\\/head>/, \"\");\n            nbSrc = nbSrc.replace(\"<html>\", \"\");\n            nbSrc = nbSrc.replace(\"</html>\", \"\");\n            nbSrc = nbSrc.replace(\"<body\", \"<div\");\n            nbSrc = nbSrc.replace(\"</body>\", \"</div>\");\n            nbSrc = nbSrc.replace(\"<!DOCTYPE html>\", \"\");\n          }\n          dispatch(setNotebookSrc(nbSrc));\n        });\n    }\n  }, [dispatch, notebookPath, slidesHash, isPresentation]);\n\n  let mainStyle = {\n    paddingTop: \"0px\",\n    paddingRight: \"0px\",\n    paddingLeft: fullScreen ? \"12px\" : \"0px\",\n    display: appView === \"files\" ? \"none\" : \"block\",\n  };\n\n  let divStyle = {};\n  if (!fullScreen) {\n    divStyle = { maxWidth: \"1140px\", margin: \"auto\" };\n  }\n\n  return (\n    <main className={`ms-sm-auto col-${columnsWidth}`} style={mainStyle}>\n      <BlockUi tag=\"div\" blocking={waiting}>\n        <div style={divStyle}>\n          {loadingState === \"loading\" && !watchMode && (\n            <p>Loading notebook. Please wait ...</p>\n          )}\n          {loadingState === \"error\" && (\n            <p style={{ margin: \"20px\" }}>\n              Problem while loading notebook. Please try again later or contact\n              Mercury administrator.\n            </p>\n          )}\n\n          {loadingState === \"error\" && username === \"\" && (\n            <p style={{ margin: \"20px\" }}>\n              <h5>Please log in to see the notebook</h5>\n              <a href=\"/login\" className=\"btn btn-primary btn-sm \">\n                <i className=\"fa fa-sign-in\" aria-hidden=\"true\"></i> Log in\n              </a>\n            </p>\n          )}\n\n          {errorMsg && (\n            <div className=\"alert alert-danger mb-3\" role=\"alert\">\n              <b>Notebook is executed with errors.</b>\n              <p>{errorMsg}</p>\n            </div>\n          )}\n\n          {errorMsg === \"\" &&\n            loadingState !== \"loading\" &&\n            isPresentation &&\n            notebookSrc !== \"\" && (\n              <iframe\n                width=\"100%\"\n                height={iframeHeight}\n                key={notebookPath}\n                srcDoc={notebookSrc}\n                title=\"display\"\n                id=\"main-iframe\"\n                onError={() => {\n                  console.log(\"iframe error\");\n                }}\n              ></iframe>\n            )}\n\n          {notebookSrc !== \"\" && !isPresentation && (\n            <InnerHTML html={notebookSrc} />\n          )}\n        </div>\n      </BlockUi>\n    </main>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React from \"react\";\nimport { useDispatch } from \"react-redux\";\nimport axios from \"axios\";\nimport fileDownload from \"js-file-download\";\nimport BlockUi from \"react-block-ui\";\nimport { setView } from \"../slices/appSlice\";\n\ntype FilesViewProps = {\n  files: string[];\n  filesState: string;\n  waiting: boolean;\n};\n\nexport default function FilesView({\n  files,\n  filesState,\n  waiting,\n}: FilesViewProps) {\n  const dispatch = useDispatch();\n\n  const handleDownload = (url: string, filename: string) => {\n    axios\n      .get(url, {\n        responseType: \"blob\",\n      })\n      .then((res) => {\n        fileDownload(res.data, filename);\n      });\n  };\n\n  console.log(files)\n\n  let filesLinks = [];\n\n  for (let f of files) {\n    let fname = f.split(\"/\").pop()\n    fname = fname?.split(\"?\")[0];\n\n    if (f && fname) {\n      let downloadLink = `${axios.defaults.baseURL}${f}`\n      if(f.includes(\"s3.amazonaws.com\")) {\n        downloadLink = f;\n      }\n      filesLinks.push(\n        <div key={f}>\n          <i\n            className=\"fa fa-file-text-o\"\n            aria-hidden=\"true\"\n            style={{ paddingRight: \"5px\" }}\n          ></i>{\" \"}\n          <b>{fname}</b>\n          <button\n            style={{ float: \"right\" }}\n            type=\"button\"\n            className=\"btn btn-primary\"\n            onClick={() =>\n\n              handleDownload(downloadLink, fname!)\n\n            }\n          >\n            <i className=\"fa fa-download\" aria-hidden=\"true\"></i> Download\n          </button>\n          <hr />\n        </div>\n      );\n    }\n  }\n\n  return (\n    <main className=\"col-md-9 ms-sm-auto col-lg-9\" style={{ padding: \"20px\" }}>\n      <div className=\"col-8\">\n        <h3 style={{ paddingBottom: \"10px\" }}>\n          <i className=\"fa fa-folder-open-o\" aria-hidden=\"true\"></i> Output Files\n        </h3>\n        <BlockUi tag=\"div\" blocking={waiting}>\n          <div>\n            {filesState === \"loaded\" && filesLinks}\n            {filesState === \"unknown\" && (\n              <p>Please run the notebook to produce output files ...</p>\n            )}\n            {filesState === \"loading\" && <p>Loading files please wait ...</p>}\n            {filesState === \"error\" && (\n              <div className=\"alert alert-danger mb-3\" role=\"alert\">\n                There was an error during loading files. Please try to run the\n                app again or contact the administrator.\n              </div>\n            )}\n          </div>\n        </BlockUi>\n      </div>\n\n      <button\n        className=\"btn btn-secondary btn-sm\"\n        // style={{ background: \"transparent\", border: \"none\", fontSize: \"0.9em\" }}\n        onClick={() => {\n          dispatch(setView(\"app\"));\n        }}\n      >\n        <i className=\"fa fa-arrow-left\" aria-hidden=\"true\"></i> Back to App\n      </button>\n    </main>\n  );\n}\n",
         "import React from \"react\";\n\nexport default function MadeWithDiv() {\n  return (\n    <a href=\"https://runmercury.com\" target=\"_blank\" rel=\"noreferrer\">\n      <div className=\"poweredby\">\n        <div className=\"text-center\">\n          {\" \"}\n          <b style={{ fontSize: \"0.9em\" }}>created with</b>{\" \"}\n        </div>\n        <div>\n          <img\n            alt=\"Mercury\"\n            src={\n              process.env.PUBLIC_URL +\n              process.env.REACT_APP_LOCAL_URL +\n              \"/mercury_black_logo.svg\"\n            }\n            style={{ height: \"27px\" }}\n          />\n        </div>\n      </div>\n    </a>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React, { useEffect, useState } from \"react\";\nimport axios from \"axios\";\nimport { IWidget } from \"../widgets/Types\";\nimport { useSelector } from \"react-redux\";\nimport { getWidgetsValues } from \"../slices/notebooksSlice\";\n\ntype Props = {\n  slug: string;\n  widgetsParams: Record<string, IWidget>;  \n  notebookPath: string;\n  columnsWidth: number;\n  taskSessionId: string | undefined;\n};\n\nexport default function RestAPIView({\n  slug,\n  widgetsParams,\n  notebookPath,\n  columnsWidth,\n  taskSessionId,\n}: Props) {\n  const [response, setResponse] = useState(\n    JSON.stringify({ msg: \"Example output\" })\n  );\n  const widgetsValues = useSelector(getWidgetsValues);\n\n  let examplePostData = {} as Record<\n    string,\n    | string\n    | number\n    | null\n    | undefined\n    | boolean\n    | [number, number]\n    | string[]\n    | unknown\n  >;\n  for (let [key, widgetParams] of Object.entries(widgetsParams)) {\n    if (widgetParams.input) {\n      examplePostData[key] = widgetsValues[key];\n    }\n  }\n\n  async function fetchResponse() {\n    try {\n      const { data } = await axios.get(`get/${taskSessionId}`);\n      setResponse(JSON.stringify(data));\n    } catch (error) {}\n  }\n\n  useEffect(() => {\n    if (taskSessionId) {\n      fetchResponse();\n    }\n    // eslint-disable-next-line react-hooks/exhaustive-deps\n  }, [taskSessionId, notebookPath]);\n\n  let sessionId = \"id-with-some-random-string\";\n  if (taskSessionId) {\n    sessionId = taskSessionId;\n  }\n\n  let postRequest = `curl -X POST -H \"Content-Type: application/json\" -d '${JSON.stringify(\n    examplePostData\n  )}' ${axios.defaults.baseURL}/run/${slug}`;\n  return (\n    <div\n      className={`ms-sm-auto col-lg-${columnsWidth}`}\n      style={{\n        border: \"none\",\n        paddingTop: \"0px\",\n        paddingRight: \"0px\",\n        paddingLeft: \"0px\",\n        padding: \"10px\",\n      }}\n    >\n      <h4>Notebook as REST API</h4>\n      <p>\n        This notebook can be executed as REST API. Please see the examples below\n        on how to access the notebook.\n      </p>\n\n      <div className=\"alert alert-secondary\" role=\"alert\">\n        <h5>POST request to execute the notebook</h5>\n        <textarea\n          disabled\n          style={{ width: \"100%\" }}\n          rows={3}\n          value={postRequest}\n        ></textarea>\n        The above request should return a JSON with `id`. The `id` should be\n        used in the GET request to fetch the result.\n        <br />\n        Example response:\n        <pre>{`{\"id\": \"${sessionId}\"}`}</pre>\n      </div>\n      <div className=\"alert alert-secondary\" role=\"alert\">\n        <h5>GET request to get execution result in JSON</h5>\n        <textarea\n          disabled\n          style={{ width: \"100%\" }}\n          rows={1}\n          value={`curl ${axios.defaults.baseURL}/get/${sessionId}`}\n        ></textarea>\n      </div>\n\n      <div className=\"alert alert-primary\" role=\"alert\">\n        <h5>Response</h5>\n        <pre>{response}</pre>\n      </div>\n    </div>\n  );\n}\n",
         "import React, { useEffect } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\nimport { toast } from \"react-toastify\";\nimport { getExportingToPDF, getExportToPDFCounter, getExportToPDFJobId, getPDF, stopPDFExport } from \"../slices/tasksSlice\";\n\nexport default function WaitPDFExport() {\n  const dispatch = useDispatch();\n  const counter = useSelector(getExportToPDFCounter);\n  const jobId = useSelector(getExportToPDFJobId);\n  const exportingPDF = useSelector(getExportingToPDF);\n\n  useEffect(() => {\n    if(jobId === '') {\n      return;\n    } \n    if(!exportingPDF) {\n      return;\n    }\n    // raise error after 2 minutes of waiting ...\n    if (counter < 120) {\n      setTimeout(() => {\n        dispatch(getPDF(jobId));\n      }, 1000); // every 1 second\n    } else {\n      dispatch(stopPDFExport());\n      toast.error(\"Problem with PDF export. Please try again later or ask your admin for help.\", { autoClose: 6000 })\n    }\n  }, [dispatch, counter, jobId, exportingPDF]);\n\n  return <div></div>;\n}\n",
-        "import React, { useEffect } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\nimport \"./App.css\";\nimport NavBar from \"../components/NavBar\";\nimport SideBar from \"../components/SideBar\";\nimport MainView from \"../components/MainView\";\n\nimport {\n  fetchNotebookWithSlug,\n  getLoadingStateSelected,\n  getSelectedNotebook,\n  getSlidesHash,\n  // getWatchModeCounter,\n} from \"../slices/notebooksSlice\";\nimport {\n  //fetchCurrentTask,\n  //fetchExecutionHistory,\n  getCurrentTask,\n  getExportingToPDF,\n  getHistoricTask,\n  getPreviousTask,\n  //ITask,\n  //setPreviousTask,\n} from \"../slices/tasksSlice\";\nimport { isOutputFilesWidget, IWidget } from \"../widgets/Types\";\nimport {\n  fetchWorkerOutputFiles,\n  getOutputFiles,\n  getOutputFilesState,\n  getShowSideBar,\n  getView,\n  setShowSideBar,\n} from \"../slices/appSlice\";\nimport FilesView from \"../components/FilesView\";\nimport { getToken, getUsername } from \"../slices/authSlice\";\nimport MadeWithDiv from \"../components/MadeWithDiv\";\nimport RestAPIView from \"../components/RestAPIView\";\nimport BlockUi from \"react-block-ui\";\nimport WaitPDFExport from \"../components/WaitPDFExport\";\nimport { getWorkerId, getWorkerState, WorkerState } from \"../slices/wsSlice\";\nimport { getSiteId, isPublic } from \"../slices/sitesSlice\";\n\ntype AppProps = {\n  isSingleApp: boolean;\n  notebookSlug: string;\n  displayEmbed: boolean;\n};\n\nfunction App({ isSingleApp, notebookSlug, displayEmbed }: AppProps) {\n  const dispatch = useDispatch();\n  const notebook = useSelector(getSelectedNotebook);\n  const loadingState = useSelector(getLoadingStateSelected);\n  const task = useSelector(getCurrentTask);\n  const historicTask = useSelector(getHistoricTask);\n  const previousTask = useSelector(getPreviousTask);\n  const appView = useSelector(getView);\n  const outputFiles = useSelector(getOutputFiles);\n  const outputFilesState = useSelector(getOutputFilesState);\n  const username = useSelector(getUsername);\n  const token = useSelector(getToken);\n  const slidesHash = useSelector(getSlidesHash);\n  const showSideBar = useSelector(getShowSideBar);\n  const exportingToPDF = useSelector(getExportingToPDF);\n  const workerId = useSelector(getWorkerId);\n  const workerState = useSelector(getWorkerState);\n  const siteId = useSelector(getSiteId);\n  const isSitePublic = useSelector(isPublic);\n\n  const pleaseWait = () => {\n    if (notebook?.params?.static_notebook) {\n      return false;\n    }\n    return workerState !== WorkerState.Running;\n  };\n\n  const isWatchMode = () => {\n    return (\n      notebook.state === \"WATCH_READY\" ||\n      notebook.state === \"WATCH_WAIT\" ||\n      notebook.state === \"WATCH_ERROR\"\n    );\n  };\n\n  useEffect(() => {\n    if (siteId !== undefined) {\n      dispatch(fetchNotebookWithSlug(siteId, notebookSlug));\n    }\n  }, [dispatch, siteId, notebookSlug, token]);\n\n  useEffect(() => {\n    if (\n      appView === \"files\" &&\n      notebook?.params?.version === \"2\" &&\n      workerId !== undefined &&\n      notebook.id !== undefined\n    ) {\n      dispatch(fetchWorkerOutputFiles(workerId, notebook.id));\n    }\n  }, [dispatch, appView, notebook, workerId]);\n\n  let notebookPath = notebook.default_view_path;\n  if (task.state && task.state === \"DONE\" && task.result) {\n    notebookPath = task.result;\n  }\n  let errorMsg = \"\";\n  if (task.state && task.result && task.state === \"ERROR\") {\n    errorMsg = task.result;\n  }\n\n  // set historic task to display if available\n  if (\n    historicTask.state &&\n    historicTask.state === \"DONE\" &&\n    historicTask.result\n  ) {\n    notebookPath = historicTask.result;\n  }\n  if (\n    historicTask.state &&\n    historicTask.result &&\n    historicTask.state === \"ERROR\"\n  ) {\n    errorMsg = historicTask.result;\n  }\n\n  // if we have previous task to show, just show it\n  if (\n    notebookPath === notebook.default_view_path &&\n    previousTask.state &&\n    previousTask.state === \"DONE\" &&\n    previousTask.result\n  ) {\n    notebookPath = previousTask.result;\n  }\n\n  const areOutputFilesAvailable = (\n    widgetsParams: Record<string, IWidget>\n  ): boolean => {\n    if (widgetsParams) {\n      for (let [, widgetParams] of Object.entries(widgetsParams)) {\n        if (isOutputFilesWidget(widgetParams)) {\n          return true;\n        }\n      }\n    }\n    return false;\n  };\n\n  let showRestApi = false;\n  if (notebook.output && notebook.output.toLowerCase().startsWith(\"rest\")) {\n    showRestApi = true;\n  }\n\n  const isFullScreen = () => {\n    if (notebook !== undefined && notebook !== null) {\n      return notebook?.params?.full_screen !== undefined &&\n        notebook?.params?.full_screen !== null\n        ? notebook.params.full_screen\n        : true;\n    }\n    return true;\n  };\n\n  const doAllowDownload = () => {\n    if (notebook !== undefined && notebook !== null) {\n      return notebook?.params?.allow_download !== undefined &&\n        notebook?.params?.allow_download !== null\n        ? notebook.params.allow_download\n        : true;\n    }\n    return true;\n  };\n\n  return (\n    <div className=\"App\">\n      {!displayEmbed && (\n        <NavBar isSitePublic={isSitePublic} username={username} />\n      )}\n      <BlockUi\n        blocking={exportingToPDF}\n        message=\"Exporting to PDF. Please wait ...\"\n      >\n        {exportingToPDF && <WaitPDFExport />}\n        <div className=\"container-fluid\">\n          <div className=\"row\">\n            {/* {notebook.schedule !== undefined && notebook.schedule !== \"\" && (\n              <AutoRefresh notebookId={notebookId} />\n            )} */}\n\n            {showSideBar && (\n              <SideBar\n                notebookTitle={notebook.title}\n                notebookId={notebook.id}\n                notebookSchedule={notebook.schedule}\n                taskCreatedAt={task.created_at}\n                loadingState={loadingState}\n                waiting={pleaseWait()}\n                widgetsParams={notebook?.params?.params}\n                watchMode={isWatchMode()}\n                notebookPath={notebookPath}\n                displayEmbed={displayEmbed}\n                showFiles={areOutputFilesAvailable(notebook?.params?.params)}\n                isPresentation={\n                  notebook.output !== undefined && notebook.output === \"slides\"\n                }\n                notebookParseErrors={notebook.errors}\n                continuousUpdate={notebook?.params?.continuous_update}\n                staticNotebook={notebook?.params?.static_notebook}\n                allowDownload={doAllowDownload()}\n              />\n            )}\n\n            {!showSideBar && (\n              <div>\n                <button\n                  className=\"btn btn-sm  btn-outline-primary\"\n                  type=\"button\"\n                  style={{\n                    position: \"absolute\",\n                    top: displayEmbed ? \"5px\" : \"50px\",\n                    left: \"5px\",\n                    zIndex: \"100\",\n                  }}\n                  onClick={() => dispatch(setShowSideBar(true))}\n                  data-toggle=\"tooltip\"\n                  data-placement=\"right\"\n                  title=\"Show sidebar\"\n                >\n                  <i className=\"fa fa-chevron-right\" aria-hidden=\"true\" />\n                </button>\n              </div>\n            )}\n\n            {showRestApi && (\n              <RestAPIView\n                slug={notebook.slug}\n                widgetsParams={notebook?.params?.params}\n                notebookPath={notebookPath}\n                columnsWidth={showSideBar ? 9 : 12}\n                taskSessionId={task.session_id}\n              />\n            )}\n\n            <MainView\n              appView={appView}\n              loadingState={loadingState}\n              notebookPath={notebookPath}\n              errorMsg={errorMsg}\n              waiting={pleaseWait()}\n              watchMode={isWatchMode()}\n              displayEmbed={displayEmbed}\n              username={username}\n              slidesHash={slidesHash}\n              columnsWidth={showSideBar ? 9 : 12}\n              isPresentation={\n                notebook.output !== undefined && notebook.output === \"slides\"\n              }\n              fullScreen={isFullScreen()}\n            />\n\n            {appView === \"files\" && (\n              <FilesView\n                files={outputFiles}\n                filesState={outputFilesState}\n                waiting={pleaseWait()}\n              />\n            )}\n          </div>\n        </div>\n      </BlockUi>\n      {displayEmbed && <MadeWithDiv />}\n    </div>\n  );\n}\n\nconst AppView = App;\nexport default AppView;\n",
+        "import React, { useEffect } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\nimport \"./App.css\";\nimport NavBar from \"../components/NavBar\";\nimport SideBar from \"../components/SideBar\";\nimport MainView from \"../components/MainView\";\n\nimport {\n  fetchNotebookWithSlug,\n  getLoadingStateSelected,\n  getSelectedNotebook,\n  getSlidesHash,\n  // getWatchModeCounter,\n} from \"../slices/notebooksSlice\";\nimport {\n  //fetchCurrentTask,\n  //fetchExecutionHistory,\n  getCurrentTask,\n  getExportingToPDF,\n  getHistoricTask,\n  getPreviousTask,\n  //ITask,\n  //setPreviousTask,\n} from \"../slices/tasksSlice\";\nimport { isOutputFilesWidget, IWidget } from \"../widgets/Types\";\nimport {\n  fetchWorkerOutputFiles,\n  getOutputFiles,\n  getOutputFilesState,\n  getShowSideBar,\n  getView,\n  setShowSideBar,\n} from \"../slices/appSlice\";\nimport FilesView from \"../components/FilesView\";\nimport { getToken, getUsername } from \"../slices/authSlice\";\nimport MadeWithDiv from \"../components/MadeWithDiv\";\nimport RestAPIView from \"../components/RestAPIView\";\nimport BlockUi from \"react-block-ui\";\nimport WaitPDFExport from \"../components/WaitPDFExport\";\nimport { getWorkerId, getWorkerState, WorkerState } from \"../slices/wsSlice\";\nimport { getSiteId, isPublic } from \"../slices/sitesSlice\";\n\ntype AppProps = {\n  isSingleApp: boolean;\n  notebookSlug: string;\n  displayEmbed: boolean;\n};\n\nfunction App({ isSingleApp, notebookSlug, displayEmbed }: AppProps) {\n  const dispatch = useDispatch();\n  const notebook = useSelector(getSelectedNotebook);\n  const loadingState = useSelector(getLoadingStateSelected);\n  const task = useSelector(getCurrentTask);\n  const historicTask = useSelector(getHistoricTask);\n  const previousTask = useSelector(getPreviousTask);\n  const appView = useSelector(getView);\n  const outputFiles = useSelector(getOutputFiles);\n  const outputFilesState = useSelector(getOutputFilesState);\n  const username = useSelector(getUsername);\n  const token = useSelector(getToken);\n  const slidesHash = useSelector(getSlidesHash);\n  const showSideBar = useSelector(getShowSideBar);\n  const exportingToPDF = useSelector(getExportingToPDF);\n  const workerId = useSelector(getWorkerId);\n  const workerState = useSelector(getWorkerState);\n  const siteId = useSelector(getSiteId);\n  const isSitePublic = useSelector(isPublic);\n\n  const pleaseWait = () => {\n    if (notebook?.params?.static_notebook) {\n      return false;\n    }\n    if (\n      workerState === WorkerState.UsageLimitReached ||\n      workerState === WorkerState.MaxIdleTimeReached ||\n      workerState === WorkerState.MaxRunTimeReached\n    ) {\n      return false;\n    }\n    return workerState !== WorkerState.Running;\n  };\n\n  const isWatchMode = () => {\n    return (\n      notebook.state === \"WATCH_READY\" ||\n      notebook.state === \"WATCH_WAIT\" ||\n      notebook.state === \"WATCH_ERROR\"\n    );\n  };\n\n  useEffect(() => {\n    if (siteId !== undefined) {\n      dispatch(fetchNotebookWithSlug(siteId, notebookSlug));\n    }\n  }, [dispatch, siteId, notebookSlug, token]);\n\n  useEffect(() => {\n    if (\n      appView === \"files\" &&\n      notebook?.params?.version === \"2\" &&\n      workerId !== undefined &&\n      notebook.id !== undefined\n    ) {\n      dispatch(fetchWorkerOutputFiles(workerId, notebook.id));\n    }\n  }, [dispatch, appView, notebook, workerId]);\n\n  let notebookPath = notebook.default_view_path;\n  if (task.state && task.state === \"DONE\" && task.result) {\n    notebookPath = task.result;\n  }\n  let errorMsg = \"\";\n  if (task.state && task.result && task.state === \"ERROR\") {\n    errorMsg = task.result;\n  }\n\n  // set historic task to display if available\n  if (\n    historicTask.state &&\n    historicTask.state === \"DONE\" &&\n    historicTask.result\n  ) {\n    notebookPath = historicTask.result;\n  }\n  if (\n    historicTask.state &&\n    historicTask.result &&\n    historicTask.state === \"ERROR\"\n  ) {\n    errorMsg = historicTask.result;\n  }\n\n  // if we have previous task to show, just show it\n  if (\n    notebookPath === notebook.default_view_path &&\n    previousTask.state &&\n    previousTask.state === \"DONE\" &&\n    previousTask.result\n  ) {\n    notebookPath = previousTask.result;\n  }\n\n  const areOutputFilesAvailable = (\n    widgetsParams: Record<string, IWidget>\n  ): boolean => {\n    if (widgetsParams) {\n      for (let [, widgetParams] of Object.entries(widgetsParams)) {\n        if (isOutputFilesWidget(widgetParams)) {\n          return true;\n        }\n      }\n    }\n    return false;\n  };\n\n  let showRestApi = false;\n  if (notebook.output && notebook.output.toLowerCase().startsWith(\"rest\")) {\n    showRestApi = true;\n  }\n\n  const isFullScreen = () => {\n    if (notebook !== undefined && notebook !== null) {\n      return notebook?.params?.full_screen !== undefined &&\n        notebook?.params?.full_screen !== null\n        ? notebook.params.full_screen\n        : true;\n    }\n    return true;\n  };\n\n  const doAllowDownload = () => {\n    if (notebook !== undefined && notebook !== null) {\n      return notebook?.params?.allow_download !== undefined &&\n        notebook?.params?.allow_download !== null\n        ? notebook.params.allow_download\n        : true;\n    }\n    return true;\n  };\n\n  return (\n    <div className=\"App\">\n      {!displayEmbed && (\n        <NavBar isSitePublic={isSitePublic} username={username} />\n      )}\n      <BlockUi\n        blocking={exportingToPDF}\n        message=\"Exporting to PDF. Please wait ...\"\n      >\n        {exportingToPDF && <WaitPDFExport />}\n        <div className=\"container-fluid\">\n          <div className=\"row\">\n            {/* {notebook.schedule !== undefined && notebook.schedule !== \"\" && (\n              <AutoRefresh notebookId={notebookId} />\n            )} */}\n\n            {showSideBar && (\n              <SideBar\n                notebookTitle={notebook.title}\n                notebookId={notebook.id}\n                notebookSchedule={notebook.schedule}\n                taskCreatedAt={task.created_at}\n                loadingState={loadingState}\n                waiting={pleaseWait()}\n                widgetsParams={notebook?.params?.params}\n                watchMode={isWatchMode()}\n                notebookPath={notebookPath}\n                displayEmbed={displayEmbed}\n                showFiles={areOutputFilesAvailable(notebook?.params?.params)}\n                isPresentation={\n                  notebook.output !== undefined && notebook.output === \"slides\"\n                }\n                notebookParseErrors={notebook.errors}\n                continuousUpdate={notebook?.params?.continuous_update}\n                staticNotebook={notebook?.params?.static_notebook}\n                allowDownload={doAllowDownload()}\n              />\n            )}\n\n            {!showSideBar && (\n              <div>\n                <button\n                  className=\"btn btn-sm  btn-outline-primary\"\n                  type=\"button\"\n                  style={{\n                    position: \"absolute\",\n                    top: displayEmbed ? \"5px\" : \"50px\",\n                    left: \"5px\",\n                    zIndex: \"100\",\n                  }}\n                  onClick={() => dispatch(setShowSideBar(true))}\n                  data-toggle=\"tooltip\"\n                  data-placement=\"right\"\n                  title=\"Show sidebar\"\n                >\n                  <i className=\"fa fa-chevron-right\" aria-hidden=\"true\" />\n                </button>\n              </div>\n            )}\n\n            {showRestApi && (\n              <RestAPIView\n                slug={notebook.slug}\n                widgetsParams={notebook?.params?.params}\n                notebookPath={notebookPath}\n                columnsWidth={showSideBar ? 9 : 12}\n                taskSessionId={task.session_id}\n              />\n            )}\n\n            <MainView\n              appView={appView}\n              loadingState={loadingState}\n              notebookPath={notebookPath}\n              errorMsg={errorMsg}\n              waiting={pleaseWait()}\n              watchMode={isWatchMode()}\n              displayEmbed={displayEmbed}\n              username={username}\n              slidesHash={slidesHash}\n              columnsWidth={showSideBar ? 9 : 12}\n              isPresentation={\n                notebook.output !== undefined && notebook.output === \"slides\"\n              }\n              fullScreen={isFullScreen()}\n            />\n\n            {appView === \"files\" && (\n              <FilesView\n                files={outputFiles}\n                filesState={outputFilesState}\n                waiting={pleaseWait()}\n              />\n            )}\n          </div>\n        </div>\n      </BlockUi>\n      {displayEmbed && <MadeWithDiv />}\n    </div>\n  );\n}\n\nconst AppView = App;\nexport default AppView;\n",
         "import { useParams } from \"react-router-dom\";\nimport AppView from \"./AppView\";\n\nimport WebSocketProvider from \"../websocket/Provider\";\n\nexport default function MyApp() {\n  const { slug } = useParams<{ slug: string }>();\n  const { embed } = useParams<{ embed: string }>();\n  const displayEmbed = !!(embed && embed === \"embed\");\n\n  return (\n    <WebSocketProvider>\n      <AppView\n        isSingleApp={false}\n        notebookSlug={slug as string}\n        displayEmbed={displayEmbed}\n      />\n    </WebSocketProvider>\n  );\n}\n",
         "import React from \"react\";\n\nexport default function Footer() {\n  return (\n    <footer\n      className=\"footer\"\n      style={{\n        position: \"absolute\",\n        bottom: \"0\",\n        width: \"100%\",\n        height: \"40px\",\n        lineHeight: \"40px\",\n        backgroundColor: \"#f5f5f5\",\n        borderTop: \"1px solid #e5e5e5\",\n      }}\n    >\n      <div className=\"container\">\n        <span className=\"text-muted\" style={{ color: \"gray\" }}>\n          Mercury \u00a9{\" \"}\n          <a\n            style={{ textDecoration: \"none\", color: \"gray\" }}\n            href=\"https://mljar.com\"\n            target=\"_blank\"\n            rel=\"noreferrer\"\n          >\n            MLJAR\n          </a>\n        </span>\n        <span className=\"text-muted\" style={{ float: \"right\" }}>\n          \n          <a\n            style={{ textDecoration: \"none\", color: \"gray\" }}\n            href=\"https://github.com/mljar/mercury\"\n            target=\"_blank\"\n            rel=\"noreferrer\"\n          >\n            Mercury\n          </a>\n          {\" \"}\n          <i className=\"fa fa-github\" aria-hidden=\"true\"></i>\n        </span>\n      </div>\n    </footer>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React from \"react\";\nimport LoginButton from \"./LoginButton\";\nimport UserButton from \"./UserButton\";\n\ntype NavBarProps = {\n  isSitePublic: boolean;\n  username: string;\n};\n\nexport default function NavBar({ isSitePublic, username }: NavBarProps) {\n  return (\n    <header\n      className=\"navbar navbar-dark sticky-top bg-dark p-0\"\n    >\n      <div className=\"row\" style={{ width: \"100%\", paddingRight: \"0px\" }}>\n        <div className=\"col-4\"></div>\n        <div className=\"col-4 text-center\">\n          <a href=\"/\">\n            <img\n              alt=\"Mercury\"\n              src={\n                process.env.PUBLIC_URL +\n                process.env.REACT_APP_LOCAL_URL +\n                \"/mercury_logo.svg\"\n              }\n              style={{ height: \"40px\" }}\n            />\n          </a>\n        </div>\n        <div\n          className=\"col-4\"\n          style={{ marginRight: \"0px\", paddingRight: \"0px\" }}\n        >\n          {!isSitePublic && username === \"\" && <LoginButton />}\n          {username !== \"\" && <UserButton username={username} />}\n        </div>\n      </div>\n    </header>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React, { useEffect, useState } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\nimport {\n  changePassword,\n  fetchUserInfo,\n  getUserInfo,\n  getUsername,\n} from \"../slices/authSlice\";\nimport Footer from \"../components/Footer\";\nimport HomeNavBar from \"../components/HomeNavBar\";\nimport { isPublic } from \"../slices/sitesSlice\";\n\nexport default function AccountView() {\n  const dispatch = useDispatch();\n  const [oldPassword, setOldPassword] = useState(\"\");\n  const [newPassword1, setNewPassword1] = useState(\"\");\n  const [newPassword2, setNewPassword2] = useState(\"\");\n  const username = useSelector(getUsername);\n  const user = useSelector(getUserInfo);\n  const isSitePublic = useSelector(isPublic);\n\n  document.body.style.backgroundColor = \"white\";\n\n  useEffect(() => {\n    dispatch(fetchUserInfo());\n  }, [dispatch]);\n\n  return (\n    <div className=\"App\">\n      <HomeNavBar isSitePublic={isSitePublic} username={username} />\n\n      <div className=\"container\">\n        <div className=\"mx-auto\" style={{ width: \"700px\" }}>\n          <div className=\"row\" style={{ marginTop: \"40px\" }}>\n            <h2>\n              <i className=\"fa fa-user\" aria-hidden=\"true\"></i> Account\n            </h2>\n            <form>\n              <div className=\"mb-3\">\n                <label className=\"form-label\">Username</label>\n                <input\n                  className=\"form-control\"\n                  value={user.username}\n                  disabled\n                />\n              </div>\n              <div className=\"mb-3\">\n                <label className=\"form-label\">First name</label>\n                <input\n                  className=\"form-control\"\n                  value={user.first_name}\n                  disabled\n                />\n              </div>\n              <div className=\"mb-3\">\n                <label className=\"form-label\">Last name</label>\n                <input\n                  className=\"form-control\"\n                  value={user.last_name}\n                  disabled\n                />\n              </div>\n\n              <div className=\"mb-3\">\n                <label className=\"form-label\">Email address</label>\n                <input className=\"form-control\" value={user.email} disabled />\n              </div>\n            </form>\n          </div>\n          <hr />\n          <div className=\"row\">\n            <h2>\n              <i className=\"fa fa-key\" aria-hidden=\"true\"></i> Change password\n            </h2>\n            <div>\n              <div className=\"mb-3\">\n                <label className=\"form-label\">Old password</label>\n                <input\n                  type=\"password\"\n                  className=\"form-control\"\n                  value={oldPassword}\n                  onChange={(e) => setOldPassword(e.target.value)}\n                />\n              </div>\n              <div className=\"mb-3\">\n                <label className=\"form-label\">New password</label>\n                <input\n                  type=\"password\"\n                  className=\"form-control\"\n                  value={newPassword1}\n                  onChange={(e) => setNewPassword1(e.target.value)}\n                />\n              </div>\n              <div className=\"mb-3\">\n                <label className=\"form-label\">Repeat new password</label>\n                <input\n                  type=\"password\"\n                  className=\"form-control\"\n                  value={newPassword2}\n                  onChange={(e) => setNewPassword2(e.target.value)}\n                />\n              </div>\n              <div className=\"mb-3\" style={{ paddingBottom: \"50px\" }}>\n                <button\n                  className=\"btn btn-primary\"\n                  onClick={() =>\n                    dispatch(\n                      changePassword(oldPassword, newPassword1, newPassword2)\n                    )\n                  }\n                  disabled={\n                    oldPassword === \"\" ||\n                    newPassword1 === \"\" ||\n                    newPassword2 === \"\"\n                  }\n                >\n                  Change password\n                </button>\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <Footer />\n    </div>\n  );\n}\n",
         "/* eslint-disable import/no-cycle */\r\nimport {\r\n  createSlice,\r\n  PayloadAction,\r\n  AnyAction,\r\n  Dispatch,\r\n} from '@reduxjs/toolkit';\r\nimport axios from 'axios';\r\n\r\nimport { RootState } from '../store';\r\nimport { setToken, setUsername } from './authSlice';\r\n\r\n\r\nconst initialState = {\r\n  fetchingIsPro: true,\r\n  isPro: false,\r\n  welcome: \"\"\r\n};\r\n\r\nconst versionSlice = createSlice({\r\n  name: 'version',\r\n  initialState,\r\n  reducers: {\r\n    setVersion(state, action: PayloadAction<{ isPro: boolean }>) {\r\n      const { isPro } = action.payload;\r\n      state.isPro = isPro;\r\n      state.fetchingIsPro = false;\r\n    },\r\n    setWelcome(state, action: PayloadAction<string>) {\r\n      state.welcome = action.payload;\r\n    }\r\n  },\r\n});\r\n\r\nexport default versionSlice.reducer;\r\n\r\nexport const {\r\n  setVersion,\r\n  setWelcome,\r\n} = versionSlice.actions;\r\n\r\nexport const getIsPro = (state: RootState) => state.version.isPro;\r\nexport const getFetchingIsPro = (state: RootState) => state.version.fetchingIsPro;\r\nexport const getWelcome = (state: RootState) => state.version.welcome;\r\n\r\nexport const fetchVersion =\r\n  () =>\r\n    async (dispatch: Dispatch<AnyAction>) => {\r\n\r\n      try {\r\n        const url = '/api/v1/version/';\r\n        const { data } = await axios.get(url);\r\n        dispatch(setVersion(data));\r\n      } catch (error) {\r\n        console.log(`Problem during loading Mercury version. ${error}`);\r\n        if (axios.isAxiosError(error)) {\r\n          if (error.response?.status === 401) {\r\n            // clear auth data \r\n            dispatch(setToken(null));\r\n            dispatch(setUsername(null));\r\n            window.location.reload();\r\n          }\r\n        }\r\n      }\r\n    };\r\n\r\n\r\nexport const fetchWelcome =\r\n  (siteId: number) =>\r\n    async (dispatch: Dispatch<AnyAction>) => {\r\n\r\n      try {\r\n        const url = `/api/v1/${siteId}/welcome/`;\r\n        const { data } = await axios.get(url);\r\n        dispatch(setWelcome(data.msg));\r\n      } catch (error) {\r\n        console.log(`Problem during loading Mercury welcome message. ${error}`);\r\n      }\r\n\r\n    };\r\n\r\n",
-        "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React, { useEffect, useState } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\n\nimport HomeNavBar from \"../components/HomeNavBar\";\nimport Footer from \"../components/Footer\";\nimport {\n  // fetchNbIframes,\n  fetchNotebooks,\n  getLoadingState,\n  // getNbIframes,\n  getNotebooks,\n} from \"../slices/notebooksSlice\";\nimport { fetchWelcome, getWelcome } from \"../slices/versionSlice\";\n\nimport ReactMarkdown from \"react-markdown\";\nimport rehypeHighlight from \"rehype-highlight\";\nimport remarkGfm from \"remark-gfm\";\nimport emoji from \"remark-emoji\";\nimport rehypeRaw from \"rehype-raw\";\nimport { getToken, getUsername } from \"../slices/authSlice\";\nimport { getSiteId, getSiteWelcome, isPublic } from \"../slices/sitesSlice\";\n\nexport default function HomeView() {\n  const dispatch = useDispatch();\n  const notebooks = useSelector(getNotebooks);\n  const loadingState = useSelector(getLoadingState);\n  const welcome = useSelector(getWelcome);\n  const username = useSelector(getUsername);\n  const token = useSelector(getToken);\n  const [showButton, setShowButton] = useState(\"\");\n  const siteId = useSelector(getSiteId);\n  const isSitePublic = useSelector(isPublic);\n  const siteWelcome = useSelector(getSiteWelcome);\n  \n  useEffect(() => {\n    if (siteId !== undefined) {\n      dispatch(fetchNotebooks(siteId));\n      if(siteWelcome === undefined || siteWelcome === \"\") {\n        dispatch(fetchWelcome(siteId));\n      }\n    }\n    // fetchNotebooks depends on token\n    // if token is set then private notebooks are returned\n  }, [dispatch, siteId, token, siteWelcome]);\n\n  const firstLetters = (text: string | null, count: number): string => {\n    if (text !== null && text !== undefined) {\n      return text.slice(0, count) + (text.length > count ? \" ...\" : \"\");\n    }\n    return \"\";\n  };\n\n  const notebookItems = notebooks.map((notebook, index) => {\n    return (\n      <div\n        className=\"col-md-4\"\n        style={{ paddingBottom: \"20px\" }}\n        key={`notebook-${notebook.id}}`}\n      >\n        <div className=\"card\">\n          <div\n            style={{\n              height: \"200px\",\n              width: \"100%\",\n              padding: \"1px\",\n              overflow: \"hidden\",\n            }}\n          >\n            <iframe\n              className=\"thumbnailIframe\"\n              width=\"200%\"\n              height={800}\n              src={`${notebook.default_view_path}`}\n              title=\"display\"\n              scrolling=\"no\"\n            ></iframe>\n          </div>\n          <a\n            href={`/app/${notebook.slug}`}\n            style={{ textDecoration: \"none\", color: \"black\" }}\n            className=\"title-card\"\n            onMouseEnter={() => {\n              setShowButton(notebook.slug);\n            }}\n            onMouseLeave={() => {\n              setShowButton(\"\");\n            }}\n          >\n            <div\n              className=\"card-body\"\n              style={{\n                borderTop: \"1px solid rgba(0,0,0,0.1)\",\n                height: \"110px\",\n              }}\n            >\n              <h5 className=\"card-title\">{firstLetters(notebook.title, 40)}</h5>\n\n              <p className=\"card-text\">\n                {firstLetters(notebook.params.description, 100)}\n              </p>\n\n              {/* <a href={`/app/${notebook.id}`} className=\"btn btn-primary\">\n              Open <i className=\"fa fa-arrow-right\" aria-hidden=\"true\"></i>\n            </a> */}\n            </div>\n            {showButton === notebook.slug && (\n              <button\n                className=\"btn btn-outline-primary\"\n                type=\"button\"\n                style={{\n                  zIndex: \"101\",\n                  border: \"none\",\n                  margin: \"5px\",\n                  position: \"absolute\",\n                  right: \"0px\",\n                  bottom: \"0px\",\n                }}\n                data-toggle=\"tooltip\"\n                data-placement=\"right\"\n                title={`Open ${notebook.title}`}\n              >\n                <i className=\"fa fa-chevron-right\" aria-hidden=\"true\" />\n              </button>\n            )}\n          </a>\n        </div>\n      </div>\n    );\n  });\n\n  document.body.style.backgroundColor = \"white\";\n\n  let welcomeMd = siteWelcome;\n  if(welcomeMd === undefined || welcomeMd === \"\") {\n    welcomeMd = welcome;\n  }\n\n  return (\n    <div className=\"App\">\n      <HomeNavBar isSitePublic={isSitePublic} username={username} />\n      <div className=\"container\" style={{ paddingBottom: \"50px\" }}>\n        {welcomeMd === \"\" && (\n          <h1 style={{ padding: \"30px\", textAlign: \"center\" }}>Welcome!</h1>\n        )}\n        {welcomeMd !== \"\" && (\n          <div style={{ paddingTop: \"20px\", paddingBottom: \"10px\" }}>\n            <ReactMarkdown\n              rehypePlugins={[remarkGfm, rehypeHighlight, emoji, rehypeRaw]}\n            >\n              {welcomeMd}\n            </ReactMarkdown>\n          </div>\n        )}\n\n        <div className=\"row\">\n          {loadingState === \"loading\" && (\n            <p>Loading notebooks. Please wait ...</p>\n          )}\n\n          {loadingState === \"loaded\" && notebooks.length === 0 && (\n            <div>\n              <p>\n                There are no notebooks available. \n              </p>\n            </div>\n          )}\n          {loadingState === \"error\" && (\n            <p>\n              Problem while loading notebooks. Please try again later or contact\n              Mercury administrator.\n            </p>\n          )}\n          {notebookItems}\n        </div>\n      </div>\n      <Footer />\n    </div>\n  );\n}\n",
+        "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React, { useEffect, useState } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\n\nimport HomeNavBar from \"../components/HomeNavBar\";\nimport Footer from \"../components/Footer\";\nimport {\n  // fetchNbIframes,\n  fetchNotebooks,\n  getLoadingState,\n  // getNbIframes,\n  getNotebooks,\n} from \"../slices/notebooksSlice\";\nimport { fetchWelcome, getWelcome } from \"../slices/versionSlice\";\n\nimport ReactMarkdown from \"react-markdown\";\nimport rehypeHighlight from \"rehype-highlight\";\nimport remarkGfm from \"remark-gfm\";\nimport emoji from \"remark-emoji\";\nimport rehypeRaw from \"rehype-raw\";\nimport { getToken, getUsername } from \"../slices/authSlice\";\nimport { getSiteId, getSiteWelcome, isPublic } from \"../slices/sitesSlice\";\n\nexport default function HomeView() {\n  const dispatch = useDispatch();\n  const notebooks = useSelector(getNotebooks);\n  const loadingState = useSelector(getLoadingState);\n  const welcome = useSelector(getWelcome);\n  const username = useSelector(getUsername);\n  const token = useSelector(getToken);\n  const [showButton, setShowButton] = useState(\"\");\n  const siteId = useSelector(getSiteId);\n  const isSitePublic = useSelector(isPublic);\n  const siteWelcome = useSelector(getSiteWelcome);\n\n  useEffect(() => {\n    if (siteId !== undefined) {\n      dispatch(fetchNotebooks(siteId));\n      if (siteWelcome === undefined || siteWelcome === \"\") {\n        dispatch(fetchWelcome(siteId));\n      }\n    }\n    // fetchNotebooks depends on token\n    // if token is set then private notebooks are returned\n  }, [dispatch, siteId, token, siteWelcome]);\n\n  const firstLetters = (text: string | null, count: number): string => {\n    if (text !== null && text !== undefined) {\n      return text.slice(0, count) + (text.length > count ? \" ...\" : \"\");\n    }\n    return \"\";\n  };\n\n  const notebookItems = notebooks.map((notebook, index) => {\n    return (\n      <div\n        className=\"col-md-4\"\n        style={{ paddingBottom: \"20px\" }}\n        key={`notebook-${notebook.id}}`}\n      >\n        <div className=\"card\">\n          <div\n            style={{\n              height: \"200px\",\n              width: \"100%\",\n              padding: \"1px\",\n              overflow: \"hidden\",\n            }}\n          >\n            <iframe\n              className=\"thumbnailIframe\"\n              width=\"200%\"\n              height={800}\n              src={`${notebook.default_view_path}`}\n              title=\"display\"\n              scrolling=\"no\"\n            ></iframe>\n\n            {/* <img\n              alt=\"some alt\" \n              \n              width=\"100%\"\n              src={`${notebook.default_view_path.replace(\".html\", \".png\")}`}\n            ></img> */}\n          </div>\n          <a\n            href={`/app/${notebook.slug}`}\n            style={{ textDecoration: \"none\", color: \"black\" }}\n            className=\"title-card\"\n            onMouseEnter={() => {\n              setShowButton(notebook.slug);\n            }}\n            onMouseLeave={() => {\n              setShowButton(\"\");\n            }}\n          >\n            <div\n              className=\"card-body\"\n              style={{\n                borderTop: \"1px solid rgba(0,0,0,0.1)\",\n                height: \"110px\",\n              }}\n            >\n              <h5 className=\"card-title\">{firstLetters(notebook.title, 40)}</h5>\n\n              <p className=\"card-text\">\n                {firstLetters(notebook.params.description, 100)}\n              </p>\n\n              {/* <a href={`/app/${notebook.id}`} className=\"btn btn-primary\">\n              Open <i className=\"fa fa-arrow-right\" aria-hidden=\"true\"></i>\n            </a> */}\n            </div>\n            {showButton === notebook.slug && (\n              <button\n                className=\"btn btn-outline-primary\"\n                type=\"button\"\n                style={{\n                  zIndex: \"101\",\n                  border: \"none\",\n                  margin: \"5px\",\n                  position: \"absolute\",\n                  right: \"0px\",\n                  bottom: \"0px\",\n                }}\n                data-toggle=\"tooltip\"\n                data-placement=\"right\"\n                title={`Open ${notebook.title}`}\n              >\n                <i className=\"fa fa-chevron-right\" aria-hidden=\"true\" />\n              </button>\n            )}\n          </a>\n        </div>\n      </div>\n    );\n  });\n\n  document.body.style.backgroundColor = \"white\";\n\n  let welcomeMd = siteWelcome;\n  if (welcomeMd === undefined || welcomeMd === \"\") {\n    welcomeMd = welcome;\n  }\n\n  return (\n    <div className=\"App\">\n      <HomeNavBar isSitePublic={isSitePublic} username={username} />\n      <div className=\"container\" style={{ paddingBottom: \"50px\" }}>\n        {welcomeMd === \"\" && (\n          <h1 style={{ padding: \"30px\", textAlign: \"center\" }}>Welcome!</h1>\n        )}\n        {welcomeMd !== \"\" && (\n          <div style={{ paddingTop: \"20px\", paddingBottom: \"10px\" }}>\n            <ReactMarkdown\n              rehypePlugins={[remarkGfm, rehypeHighlight, emoji, rehypeRaw]}\n            >\n              {welcomeMd}\n            </ReactMarkdown>\n          </div>\n        )}\n\n        <div className=\"row\">\n          {loadingState === \"loading\" && (\n            <p>Loading notebooks. Please wait ...</p>\n          )}\n\n          {loadingState === \"loaded\" && notebooks.length === 0 && (\n            <div>\n              <p>There are no notebooks available.</p>\n            </div>\n          )}\n          {loadingState === \"error\" && (\n            <p>\n              Problem while loading notebooks. Please try again later or contact\n              Mercury administrator.\n            </p>\n          )}\n          {notebookItems}\n        </div>\n      </div>\n      <Footer />\n    </div>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React, { useState } from \"react\";\nimport { useDispatch, useSelector } from \"react-redux\";\nimport { fetchToken } from \"../slices/authSlice\";\nimport Footer from \"../components/Footer\";\nimport HomeNavBar from \"../components/HomeNavBar\";\n\nimport { useLocation, useNavigate } from \"react-router-dom\";\nimport { isPublic } from \"../slices/sitesSlice\";\n\ntype LocationState = {\n  from: {\n    pathname: string;\n  };\n};\n\nexport default function LoginView() {\n  const dispatch = useDispatch();\n  const navigate = useNavigate();\n  const [email, setEmail] = useState(\"\");\n  const [password, setPassword] = useState(\"\");\n  const isSitePublic = useSelector(isPublic);\n\n  document.body.style.backgroundColor = \"#f5f5f5\";\n\n  let redirectPath = \"/\";\n  let location = useLocation();\n  if (location && location.state) {\n    // redirect from ...\n    const { from } = location.state as LocationState;\n    redirectPath = from.pathname;\n  }\n\n  return (\n    <div className=\"App\">\n      <HomeNavBar isSitePublic={isSitePublic} username={\"\"} />\n\n      <div className=\"div-signin text-center\">\n        <form\n          className=\"form-signin\"\n          onSubmit={(e) => {\n            e.preventDefault();\n            e.stopPropagation();\n            dispatch(fetchToken(email, password, redirectPath, navigate));\n          }}\n        >\n          <h3 className=\"h3 mb-3 font-weight-normal\">Please sign in</h3>\n          <label className=\"sr-only\">Email</label>\n          <input\n            type=\"email\"\n            id=\"inputEmail\"\n            className=\"form-control\"\n            placeholder=\"Email\"\n            value={email}\n            onChange={(e) => {\n              setEmail(e.target.value);\n            }}\n            required\n          />\n          <label className=\"sr-only\">Password</label>\n          <input\n            type=\"password\"\n            id=\"inputPassword\"\n            className=\"form-control\"\n            placeholder=\"Password\"\n            value={password}\n            onChange={(e) => {\n              setPassword(e.target.value);\n            }}\n            required\n          />\n          <button\n            className=\"btn btn-lg btn-primary btn-block\"\n            type=\"submit\"\n            style={{ margin: \"5px\" }}\n            disabled={email === \"\" || password === \"\"}\n          >\n            <i className=\"fa fa-sign-in\" aria-hidden=\"true\"></i> Log in\n          </button>\n        </form>\n        <div className=\"mx-auto\" style={{ width: \"400px\", marginTop: \"40px\" }}>\n          <p className=\"text-muted\">\n            No account? <br /> Please contact administrator to create account\n            for you.\n          </p>\n        </div>\n      </div>\n\n      <Footer />\n    </div>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React from \"react\"; \nimport Footer from \"../components/Footer\";\nimport HomeNavBar from \"../components/HomeNavBar\";\n\nexport default function LostConnection() {\n  return (\n    <div className=\"App\">\n      <HomeNavBar isSitePublic={true} username={\"\"} />\n      <div\n        style={{\n          width: \"100%\",\n          maxWidth: \"500px\",\n          padding: \"15px\",\n          margin: \"0 auto\",\n        }}\n      >\n        <h3>Lost connection</h3>\n        <p>\n          App lost connection to the server. Please try again in a moment or contact administrator.\n        </p>\n      </div>\n      <Footer />\n    </div>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React from \"react\";\nimport { Link } from \"react-router-dom\";\nimport Footer from \"../components/Footer\";\nimport HomeNavBar from \"../components/HomeNavBar\";\n\nexport default function SiteAccessForbiddenView() {\n  return (\n    <div className=\"App\">\n      <HomeNavBar isSitePublic={true} username={\"\"} />\n      <div\n        style={{\n          width: \"100%\",\n          maxWidth: \"500px\",\n          padding: \"15px\",\n          margin: \"0 auto\",\n        }}\n      >\n        <h3>Access forbidden</h3>\n        <p>\n          Please <Link to=\"/login\">login</Link> to access site.\n        </p>\n      </div>\n      <Footer />\n    </div>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React from \"react\";\nimport Footer from \"../components/Footer\";\nimport HomeNavBar from \"../components/HomeNavBar\";\n\nexport default function SiteLoadingView() {\n  return (\n    <div className=\"App\">\n      <HomeNavBar isSitePublic={true} username={\"\"} />\n      <div\n        style={{\n          width: \"100%\",\n          maxWidth: \"500px\",\n          padding: \"15px\",\n          margin: \"0 auto\",\n        }}\n      >\n        <p style={{ color: \"gray\" }}>Please wait. Loading site ...</p>\n      </div>\n      <Footer />\n    </div>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React from \"react\";\nimport Footer from \"../components/Footer\";\nimport HomeNavBar from \"../components/HomeNavBar\";\n\nexport default function SiteNetworkErrorView() {\n  return (\n    <div className=\"App\">\n      <HomeNavBar isSitePublic={true} username={\"\"} />\n      <div\n        style={{\n          width: \"100%\",\n          maxWidth: \"500px\",\n          padding: \"15px\",\n          margin: \"0 auto\",\n        }}\n      >\n        <h3>Network Error</h3>\n        <p>\n          Please check if you have internet connection and server is running. In\n          case of problems, please contact administrator.\n        </p>\n      </div>\n      <Footer />\n    </div>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React from \"react\";\nimport Footer from \"../components/Footer\";\nimport HomeNavBar from \"../components/HomeNavBar\";\n\nexport default function SiteNotFoundView() {\n  return (\n    <div className=\"App\">\n      <HomeNavBar isSitePublic={true} username={\"\"} />\n      <div\n        style={{\n          width: \"100%\",\n          maxWidth: \"500px\",\n          padding: \"15px\",\n          margin: \"0 auto\",\n        }}\n      >\n        <h3>Site does not exist</h3>\n        <p>\n          We can't find site you are looking for. Please make sure that URL\n          address is correct.\n        </p>\n      </div>\n      <Footer />\n    </div>\n  );\n}\n",
         "/* eslint-disable jsx-a11y/anchor-is-valid */\nimport React from \"react\";\nimport Footer from \"../components/Footer\";\nimport HomeNavBar from \"../components/HomeNavBar\";\n\nexport default function SitePleaseRefreshView() {\n  return (\n    <div className=\"App\">\n      <HomeNavBar isSitePublic={true} username={\"\"} />\n      <div\n        style={{\n          width: \"100%\",\n          maxWidth: \"500px\",\n          padding: \"15px\",\n          margin: \"0 auto\",\n        }}\n      >\n        <h3>Please refresh</h3>\n        <p>\n          Please try to refresh the website ...\n        </p>\n      </div>\n      <Footer />\n    </div>\n  );\n}\n",
```

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/js/runtime-main.248907bc.js` & `mercury-2.2.0/mercury/frontend-dist/static/js/runtime-main.248907bc.js`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/js/runtime-main.248907bc.js.map` & `mercury-2.2.0/mercury/frontend-dist/static/js/runtime-main.248907bc.js.map`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/media/fontawesome-webfont.1e59d233.ttf` & `mercury-2.2.0/mercury/frontend-dist/static/media/fontawesome-webfont.1e59d233.ttf`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/media/fontawesome-webfont.20fd1704.woff2` & `mercury-2.2.0/mercury/frontend-dist/static/media/fontawesome-webfont.20fd1704.woff2`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/media/fontawesome-webfont.8b43027f.eot` & `mercury-2.2.0/mercury/frontend-dist/static/media/fontawesome-webfont.8b43027f.eot`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/media/fontawesome-webfont.c1e38fd9.svg` & `mercury-2.2.0/mercury/frontend-dist/static/media/fontawesome-webfont.c1e38fd9.svg`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/frontend-dist/static/media/fontawesome-webfont.f691f37e.woff` & `mercury-2.2.0/mercury/frontend-dist/static/media/fontawesome-webfont.f691f37e.woff`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/manage.py` & `mercury-2.2.0/mercury/manage.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/mercury.py` & `mercury-2.2.0/mercury/mercury.py`

 * *Files 2% similar despite different names*

```diff
@@ -36,14 +36,16 @@
 from widgets.outputdir import OutputDir
 from widgets.note import Note
 from widgets.button import Button
 from widgets.md import Markdown
 from widgets.md import Markdown as Md
 from widgets.json import JSON
 from widgets.stop import StopExecution, Stop
+from widgets.confetti import Confetti
+from widgets.chat import Chat
 
 
 def main():
     """Run administrative tasks."""
     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
     try:
         from django.core.management import execute_from_command_line
```

### Comparing `mercury-2.1.9/mercury/requirements.txt` & `mercury-2.2.0/mercury/requirements.txt`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/server/asgi.py` & `mercury-2.2.0/mercury/server/asgi.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/server/celery.py` & `mercury-2.2.0/mercury/server/celery.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/server/settings.py` & `mercury-2.2.0/mercury/server/settings.py`

 * *Files 2% similar despite different names*

```diff
@@ -287,15 +287,15 @@
             "handlers": ["console", "file"],
             "level": os.getenv("DJANGO_LOG_LEVEL", "ERROR"),
             "propagate": False,
         },
     },
 }
 
-NBWORKERS_PER_MACHINE = 20
+NBWORKERS_PER_MACHINE = int(os.environ.get("NBWORKERS_PER_MACHINE", 20))
 
 # delta time after which worker is considered as stale and deleted
 WORKER_STALE_TIME = 1  # in minutes
 
 AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
 AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
 AWS_REGION_NAME = os.environ.get("AWS_REGION_NAME")
```

### Comparing `mercury-2.1.9/mercury/server/urls.py` & `mercury-2.2.0/mercury/server/urls.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/server/views.py` & `mercury-2.2.0/mercury/server/views.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/widgets/app.py` & `mercury-2.2.0/mercury/widgets/app.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/widgets/button.py` & `mercury-2.2.0/mercury/widgets/button.py`

 * *Files 4% similar despite different names*

```diff
@@ -16,15 +16,17 @@
 
         if WidgetsManager.widget_exists(self.code_uid):
             self.button = WidgetsManager.get_widget(self.code_uid)
             self.button.description = label
             self.button.button_style = style
             self.button.disabled = disabled
         else:
-            self.button = ipywidgets.Button(description=label, button_style=style, disabled=disabled)
+            self.button = ipywidgets.Button(
+                description=label, button_style=style, disabled=disabled
+            )
             self.button.value = False
 
             def on_button_clicked(b):
                 self.button.value = True
 
             self.button.on_click(on_button_clicked)
 
@@ -56,19 +58,19 @@
                 "widget": "Button",
                 "label": self.button.description,
                 "style": self.button.button_style,
                 "value": False,
                 "model_id": self.button.model_id,
                 "code_uid": self.code_uid,
                 "disabled": self.button.disabled,
-                "hidden": self.hidden
+                "hidden": self.hidden,
             }
             data["application/mercury+json"] = json.dumps(view, indent=4)
             if "text/plain" in data:
                 del data["text/plain"]
 
             if self.hidden:
-                key = 'application/vnd.jupyter.widget-view+json'
+                key = "application/vnd.jupyter.widget-view+json"
                 if key in data:
                     del data[key]
 
             return data
```

### Comparing `mercury-2.1.9/mercury/widgets/checkbox.py` & `mercury-2.2.0/mercury/widgets/checkbox.py`

 * *Files 5% similar despite different names*

```diff
@@ -13,15 +13,18 @@
         self.hidden = hidden
         if WidgetsManager.widget_exists(self.code_uid):
             self.checkbox = WidgetsManager.get_widget(self.code_uid)
             self.checkbox.description = label
             self.checkbox.disabled = disabled
         else:
             self.checkbox = ipywidgets.Checkbox(
-                value=value, description=label, style={"description_width": "initial"}, disabled=disabled
+                value=value,
+                description=label,
+                style={"description_width": "initial"},
+                disabled=disabled,
             )
             WidgetsManager.add_widget(
                 self.checkbox.model_id, self.code_uid, self.checkbox
             )
         display(self)
 
     @property
@@ -49,19 +52,19 @@
                 "widget": "Checkbox",
                 "value": self.checkbox.value,
                 "label": self.checkbox.description,
                 "model_id": self.checkbox.model_id,
                 "code_uid": self.code_uid,
                 "url_key": self.url_key,
                 "disabled": self.checkbox.disabled,
-                "hidden": self.hidden
+                "hidden": self.hidden,
             }
             data["application/mercury+json"] = json.dumps(view, indent=4)
             if "text/plain" in data:
                 del data["text/plain"]
 
             if self.hidden:
-                key = 'application/vnd.jupyter.widget-view+json'
+                key = "application/vnd.jupyter.widget-view+json"
                 if key in data:
                     del data[key]
 
             return data
```

### Comparing `mercury-2.1.9/mercury/widgets/file.py` & `mercury-2.2.0/mercury/widgets/file.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,17 @@
 import ipywidgets
 from IPython.display import display
 
 from .manager import WidgetsManager
 
 
 class File:
-    def __init__(self, label="File upload", max_file_size="100MB", disabled=False, hidden=False):
+    def __init__(
+        self, label="File upload", max_file_size="100MB", disabled=False, hidden=False
+    ):
         self.max_file_size = max_file_size
         self.code_uid = WidgetsManager.get_code_uid("File")
         self.temp_dir = None
         atexit.register(self.cleanup)
         self.hidden = hidden
 
         if WidgetsManager.widget_exists(self.code_uid):
@@ -32,17 +34,15 @@
     @property
     def value(self):
         if len(self.file.value):
             return self.file.value[0].content
 
         if self.file.filepath is not None:
             # read that file
-            with open(
-                self.file.filepath, "rb"
-            ) as fin:
+            with open(self.file.filepath, "rb") as fin:
                 return fin.read()
 
         return None
 
     @property
     def filename(self):
         if len(self.file.value):
@@ -68,20 +68,19 @@
 
             with open(self.file.filepath, "wb") as fout:
                 fout.write(self.value)
 
             return self.file.filepath
 
         return None
-    
+
     def cleanup(self):
         if self.temp_dir is not None and os.path.exists(self.temp_dir):
             shutil.rmtree(self.temp_dir, ignore_errors=True)
 
-
     @value.setter
     def value(self, v):
         filename, filepath = v
         self.file.filepath = filepath
         self.file.filename = filename
 
     def __str__(self):
@@ -100,19 +99,19 @@
             view = {
                 "widget": "File",
                 "max_file_size": self.max_file_size,
                 "label": self.file.description,
                 "model_id": self.file.model_id,
                 "code_uid": self.code_uid,
                 "disabled": self.file.disabled,
-                "hidden": self.hidden
+                "hidden": self.hidden,
             }
             data["application/mercury+json"] = json.dumps(view, indent=4)
             if "text/plain" in data:
                 del data["text/plain"]
 
             if self.hidden:
-                key = 'application/vnd.jupyter.widget-view+json'
+                key = "application/vnd.jupyter.widget-view+json"
                 if key in data:
                     del data[key]
 
             return data
```

### Comparing `mercury-2.1.9/mercury/widgets/json.py` & `mercury-2.2.0/mercury/widgets/json.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/widgets/manager.py` & `mercury-2.2.0/mercury/widgets/manager.py`

 * *Files 0% similar despite different names*

```diff
@@ -199,8 +199,7 @@
                 "label": output.get("label", ""),
                 "style": output.get("style", "primary"),
                 "disabled": output.get("disabled", False),
                 "hidden": output.get("hidden", False),
             }
 
         return {}
-
```

### Comparing `mercury-2.1.9/mercury/widgets/multiselect.py` & `mercury-2.2.0/mercury/widgets/multiselect.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,14 +12,16 @@
     ):
         if value is None and len(choices) > 1:
             value = [choices[0]]
 
         self.code_uid = WidgetsManager.get_code_uid("MultiSelect")
         self.url_key = url_key
         self.hidden = hidden
+        choices = list(choices)
+        value = list(value)
         if WidgetsManager.widget_exists(self.code_uid):
             self.select = WidgetsManager.get_widget(self.code_uid)
             if list(self.select.options) != choices:
                 self.select.options = choices
                 self.select.value = value
             self.select.description = label
             self.select.disabled = disabled
@@ -66,19 +68,19 @@
                 "value": self.select.value,
                 "choices": self.select.options,
                 "label": self.select.description,
                 "model_id": self.select.model_id,
                 "code_uid": self.code_uid,
                 "url_key": self.url_key,
                 "disabled": self.select.disabled,
-                "hidden": self.hidden
+                "hidden": self.hidden,
             }
             data["application/mercury+json"] = json.dumps(view, indent=4)
             if "text/plain" in data:
                 del data["text/plain"]
 
             if self.hidden:
-                key = 'application/vnd.jupyter.widget-view+json'
+                key = "application/vnd.jupyter.widget-view+json"
                 if key in data:
                     del data[key]
 
             return data
```

### Comparing `mercury-2.1.9/mercury/widgets/note.py` & `mercury-2.2.0/mercury/widgets/note.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/widgets/numeric.py` & `mercury-2.2.0/mercury/widgets/numeric.py`

 * *Files 17% similar despite different names*

```diff
@@ -3,15 +3,25 @@
 import ipywidgets
 from IPython.display import display
 
 from .manager import WidgetException, WidgetsManager
 
 
 class Numeric:
-    def __init__(self, value=0, min=0, max=10, label="", step=1, url_key="", disabled=False, hidden=False):
+    def __init__(
+        self,
+        value=0,
+        min=0,
+        max=10,
+        label="",
+        step=1,
+        url_key="",
+        disabled=False,
+        hidden=False,
+    ):
         if value < min:
             raise WidgetException("value should be equal or larger than min")
         if value > max:
             raise WidgetException("value should be equal or smaller than max")
 
         self.code_uid = WidgetsManager.get_code_uid("Numeric")
         self.url_key = url_key
@@ -33,15 +43,15 @@
             self.numeric = ipywidgets.BoundedFloatText(
                 value=value,
                 min=min,
                 max=max,
                 description=label,
                 step=step,
                 style={"description_width": "initial"},
-                disabled=disabled
+                disabled=disabled,
             )
             WidgetsManager.add_widget(
                 self.numeric.model_id, self.code_uid, self.numeric
             )
         display(self)
 
     @property
@@ -72,19 +82,19 @@
                 "max": self.numeric.max,
                 "step": self.numeric.step,
                 "label": self.numeric.description,
                 "model_id": self.numeric.model_id,
                 "code_uid": self.code_uid,
                 "url_key": self.url_key,
                 "disabled": self.numeric.disabled,
-                "hidden": self.hidden
+                "hidden": self.hidden,
             }
             data["application/mercury+json"] = json.dumps(view, indent=4)
             if "text/plain" in data:
                 del data["text/plain"]
 
             if self.hidden:
-                key = 'application/vnd.jupyter.widget-view+json'
+                key = "application/vnd.jupyter.widget-view+json"
                 if key in data:
                     del data[key]
 
             return data
```

### Comparing `mercury-2.1.9/mercury/widgets/outputdir.py` & `mercury-2.2.0/mercury/widgets/outputdir.py`

 * *Files identical despite different names*

### Comparing `mercury-2.1.9/mercury/widgets/range.py` & `mercury-2.2.0/mercury/widgets/range.py`

 * *Files 12% similar despite different names*

```diff
@@ -3,15 +3,25 @@
 import ipywidgets
 from IPython.display import display
 
 from .manager import WidgetException, WidgetsManager
 
 
 class Range:
-    def __init__(self, value=[0, 1], min=0, max=10, label="", step=1, url_key="", disabled=False, hidden=False):
+    def __init__(
+        self,
+        value=[0, 1],
+        min=0,
+        max=10,
+        label="",
+        step=1,
+        url_key="",
+        disabled=False,
+        hidden=False,
+    ):
         for i in [0, 1]:
             if value[i] < min:
                 raise WidgetException(f"value[{i}] should be equal or larger than min")
             if value[i] > max:
                 raise WidgetException(f"value[{i}] should be equal or smaller than max")
 
         if len(value) != 2:
@@ -37,15 +47,15 @@
             self.range = ipywidgets.IntRangeSlider(
                 value=value,
                 min=min,
                 max=max,
                 description=label,
                 step=step,
                 style={"description_width": "initial"},
-                disabled=disabled
+                disabled=disabled,
             )
             WidgetsManager.add_widget(self.range.model_id, self.code_uid, self.range)
         display(self)
 
     @property
     def value(self):
         return list(self.range.value)
@@ -70,19 +80,19 @@
                 "max": self.range.max,
                 "step": self.range.step,
                 "label": self.range.description,
                 "model_id": self.range.model_id,
                 "code_uid": self.code_uid,
                 "url_key": self.url_key,
                 "disabled": self.range.disabled,
-                "hidden": self.hidden
+                "hidden": self.hidden,
             }
             data["application/mercury+json"] = json.dumps(view, indent=4)
             if "text/plain" in data:
                 del data["text/plain"]
 
             if self.hidden:
-                key = 'application/vnd.jupyter.widget-view+json'
+                key = "application/vnd.jupyter.widget-view+json"
                 if key in data:
                     del data[key]
 
             return data
```

### Comparing `mercury-2.1.9/mercury/widgets/select.py` & `mercury-2.2.0/mercury/widgets/select.py`

 * *Files 11% similar despite different names*

```diff
@@ -3,35 +3,38 @@
 import ipywidgets
 from IPython.display import display
 
 from .manager import WidgetsManager
 
 
 class Select:
-    def __init__(self, value=None, choices=[], label="", url_key="", disabled=False, hidden=False):
+    def __init__(
+        self, value=None, choices=[], label="", url_key="", disabled=False, hidden=False
+    ):
         if value is None and len(choices) > 1:
             value = choices[0]
 
         self.code_uid = WidgetsManager.get_code_uid("Select")
         self.url_key = url_key
         self.hidden = hidden
+        choices = list(choices)
         if WidgetsManager.widget_exists(self.code_uid):
             self.dropdown = WidgetsManager.get_widget(self.code_uid)
             if list(self.dropdown.options) != choices:
                 self.dropdown.options = choices
                 self.dropdown.value = value
             self.dropdown.description = label
             self.dropdown.disabled = disabled
         else:
             self.dropdown = ipywidgets.Dropdown(
                 value=value,
                 options=choices,
                 description=label,
                 style={"description_width": "initial"},
-                disabled=disabled
+                disabled=disabled,
             )
             WidgetsManager.add_widget(
                 self.dropdown.model_id, self.code_uid, self.dropdown
             )
         display(self)
 
     @property
@@ -56,19 +59,19 @@
                 "value": self.dropdown.value,
                 "choices": self.dropdown.options,
                 "label": self.dropdown.description,
                 "model_id": self.dropdown.model_id,
                 "code_uid": self.code_uid,
                 "url_key": self.url_key,
                 "disabled": self.dropdown.disabled,
-                "hidden": self.hidden
+                "hidden": self.hidden,
             }
             data["application/mercury+json"] = json.dumps(view, indent=4)
             if "text/plain" in data:
                 del data["text/plain"]
 
             if self.hidden:
-                key = 'application/vnd.jupyter.widget-view+json'
+                key = "application/vnd.jupyter.widget-view+json"
                 if key in data:
                     del data[key]
 
             return data
```

### Comparing `mercury-2.1.9/mercury/widgets/slider.py` & `mercury-2.2.0/mercury/widgets/slider.py`

 * *Files 10% similar despite different names*

```diff
@@ -3,15 +3,25 @@
 import ipywidgets
 from IPython.display import display
 
 from .manager import WidgetException, WidgetsManager
 
 
 class Slider:
-    def __init__(self, value=0, min=0, max=10, label="", step=1, url_key="", disabled=False, hidden=False):
+    def __init__(
+        self,
+        value=0,
+        min=0,
+        max=10,
+        label="",
+        step=1,
+        url_key="",
+        disabled=False,
+        hidden=False,
+    ):
         if value < min:
             raise WidgetException("value should be equal or larger than min")
         if value > max:
             raise WidgetException("value should be equal or smaller than max")
 
         self.code_uid = WidgetsManager.get_code_uid("Slider")
         self.url_key = url_key
@@ -33,15 +43,15 @@
             self.slider = ipywidgets.IntSlider(
                 value=value,
                 min=min,
                 max=max,
                 description=label,
                 step=step,
                 style={"description_width": "initial"},
-                disabled=disabled
+                disabled=disabled,
             )
             WidgetsManager.add_widget(self.slider.model_id, self.code_uid, self.slider)
         display(self)
 
     @property
     def value(self):
         return self.slider.value
@@ -70,19 +80,19 @@
                 "max": self.slider.max,
                 "step": self.slider.step,
                 "label": self.slider.description,
                 "model_id": self.slider.model_id,
                 "code_uid": self.code_uid,
                 "url_key": self.url_key,
                 "disabled": self.slider.disabled,
-                "hidden": self.hidden
+                "hidden": self.hidden,
             }
             data["application/mercury+json"] = json.dumps(view, indent=4)
             if "text/plain" in data:
                 del data["text/plain"]
 
             if self.hidden:
-                key = 'application/vnd.jupyter.widget-view+json'
+                key = "application/vnd.jupyter.widget-view+json"
                 if key in data:
                     del data[key]
 
             return data
```

### Comparing `mercury-2.1.9/mercury/widgets/text.py` & `mercury-2.2.0/mercury/widgets/text.py`

 * *Files 2% similar despite different names*

```diff
@@ -3,26 +3,30 @@
 import ipywidgets
 from IPython.display import display
 
 from .manager import WidgetException, WidgetsManager
 
 
 class Text:
-    def __init__(self, value="", label="", rows=1, url_key="", disabled=False, hidden=False):
+    def __init__(
+        self, value="", label="", rows=1, url_key="", disabled=False, hidden=False
+    ):
         self.rows = rows
 
         self.code_uid = WidgetsManager.get_code_uid("Text")
         self.url_key = url_key
         self.hidden = hidden
         if WidgetsManager.widget_exists(self.code_uid):
             self.text = WidgetsManager.get_widget(self.code_uid)
             self.text.description = label
             self.text.disabled = disabled
         else:
-            self.text = ipywidgets.Textarea(value=value, description=label, disabled=disabled)
+            self.text = ipywidgets.Textarea(
+                value=value, description=label, disabled=disabled
+            )
             WidgetsManager.add_widget(self.text.model_id, self.code_uid, self.text)
         display(self)
 
     @property
     def value(self):
         return self.text.value
 
@@ -48,19 +52,19 @@
                 "value": self.text.value,
                 "rows": self.rows,
                 "label": self.text.description,
                 "model_id": self.text.model_id,
                 "code_uid": self.code_uid,
                 "url_key": self.url_key,
                 "disabled": self.text.disabled,
-                "hidden": self.hidden
+                "hidden": self.hidden,
             }
             data["application/mercury+json"] = json.dumps(view, indent=4)
             if "text/plain" in data:
                 del data["text/plain"]
 
             if self.hidden:
-                key = 'application/vnd.jupyter.widget-view+json'
+                key = "application/vnd.jupyter.widget-view+json"
                 if key in data:
                     del data[key]
 
             return data
```

### Comparing `mercury-2.1.9/mercury.egg-info/PKG-INFO` & `mercury-2.2.0/mercury.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mercury
-Version: 2.1.9
+Version: 2.2.0
 Summary: Turn Jupyter Notebook to Web App and share with non-technical users
 Home-page: https://github.com/mljar/mercury
 Maintainer: MLJAR Sp. z o.o.
 Maintainer-email: contact@mljar.com
 License: UNKNOWN
 Description:
```

### Comparing `mercury-2.1.9/mercury.egg-info/SOURCES.txt` & `mercury-2.2.0/mercury.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -39,14 +39,16 @@
 mercury/apps/accounts/views/subscription.py
 mercury/apps/accounts/views/utils.py
 mercury/apps/nb/__init__.py
 mercury/apps/nb/exporter.py
 mercury/apps/nb/nbrun.py
 mercury/apps/nb/tests.py
 mercury/apps/nb/utils.py
+mercury/apps/nb/tests/__init__.py
+mercury/apps/nb/tests/test_nbrun.py
 mercury/apps/nbworker/__init__.py
 mercury/apps/nbworker/__main__.py
 mercury/apps/nbworker/nb.py
 mercury/apps/nbworker/rest.py
 mercury/apps/nbworker/tests.py
 mercury/apps/nbworker/utils.py
 mercury/apps/nbworker/ws.py
@@ -86,14 +88,15 @@
 mercury/apps/storage/views/notebookfiles.py
 mercury/apps/storage/views/workerfiles.py
 mercury/apps/tasks/__init__.py
 mercury/apps/tasks/admin.py
 mercury/apps/tasks/apps.py
 mercury/apps/tasks/clean_service.py
 mercury/apps/tasks/export_pdf.py
+mercury/apps/tasks/export_png.py
 mercury/apps/tasks/models.py
 mercury/apps/tasks/notify.py
 mercury/apps/tasks/serializers.py
 mercury/apps/tasks/tasks.py
 mercury/apps/tasks/tasks_export.py
 mercury/apps/tasks/tests.py
 mercury/apps/tasks/urls.py
@@ -134,16 +137,16 @@
 mercury/frontend-dist/static/css/2.c6cf5ff9.chunk.css
 mercury/frontend-dist/static/css/2.c6cf5ff9.chunk.css.map
 mercury/frontend-dist/static/css/main.26f96620.chunk.css
 mercury/frontend-dist/static/css/main.26f96620.chunk.css.map
 mercury/frontend-dist/static/js/2.20950ecb.chunk.js
 mercury/frontend-dist/static/js/2.20950ecb.chunk.js.LICENSE.txt
 mercury/frontend-dist/static/js/2.20950ecb.chunk.js.map
-mercury/frontend-dist/static/js/main.b729f6a0.chunk.js
-mercury/frontend-dist/static/js/main.b729f6a0.chunk.js.map
+mercury/frontend-dist/static/js/main.717ee96a.chunk.js
+mercury/frontend-dist/static/js/main.717ee96a.chunk.js.map
 mercury/frontend-dist/static/js/runtime-main.248907bc.js
 mercury/frontend-dist/static/js/runtime-main.248907bc.js.map
 mercury/frontend-dist/static/media/fontawesome-webfont.1e59d233.ttf
 mercury/frontend-dist/static/media/fontawesome-webfont.20fd1704.woff2
 mercury/frontend-dist/static/media/fontawesome-webfont.8b43027f.eot
 mercury/frontend-dist/static/media/fontawesome-webfont.c1e38fd9.svg
 mercury/frontend-dist/static/media/fontawesome-webfont.f691f37e.woff
@@ -153,15 +156,17 @@
 mercury/server/settings.py
 mercury/server/urls.py
 mercury/server/views.py
 mercury/server/wsgi.py
 mercury/widgets/__init__.py
 mercury/widgets/app.py
 mercury/widgets/button.py
+mercury/widgets/chat.py
 mercury/widgets/checkbox.py
+mercury/widgets/confetti.py
 mercury/widgets/file.py
 mercury/widgets/json.py
 mercury/widgets/manager.py
 mercury/widgets/md.py
 mercury/widgets/multiselect.py
 mercury/widgets/note.py
 mercury/widgets/numeric.py
```

### Comparing `mercury-2.1.9/setup.py` & `mercury-2.2.0/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -9,15 +9,15 @@
     for (path, directories, filenames) in os.walk(directory):
         for filename in filenames:
             paths.append(os.path.join(path, filename))
     return paths
 
 setup(
     name="mercury",
-    version="2.1.9",
+    version="2.2.0",
     maintainer="MLJAR Sp. z o.o.",
     maintainer_email="contact@mljar.com",
     description="Turn Jupyter Notebook to Web App and share with non-technical users",
     long_description=long_description,
     long_description_content_type="text/markdown",
     install_requires=open("mercury/requirements.txt").readlines(),
     url="https://github.com/mljar/mercury",
```

