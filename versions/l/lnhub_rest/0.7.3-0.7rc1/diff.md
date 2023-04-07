# Comparing `tmp/lnhub_rest-0.7.3.tar.gz` & `tmp/lnhub_rest-0.7rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lnhub_rest-0.7.3.tar", last modified: Fri Apr  7 11:11:41 2023, max compression
+gzip compressed data, was "lnhub_rest-0.7rc1.tar", last modified: Wed Mar 29 10:58:59 2023, max compression
```

## Comparing `lnhub_rest-0.7.3.tar` & `lnhub_rest-0.7rc1.tar`

### file list

```diff
@@ -1,126 +1,126 @@
--rw-r--r--   0        0        0     1259 2023-01-21 09:45:45.805481 lnhub_rest-0.7.3/.dockerignore
--rw-r--r--   0        0        0     2724 2023-03-30 12:47:50.834403 lnhub_rest-0.7.3/.github/workflows/build.yml
--rw-r--r--   0        0        0     4871 2023-03-30 13:19:18.603924 lnhub_rest-0.7.3/.github/workflows/google-cloudrun-docker.yml
--rw-r--r--   0        0        0      133 2023-01-21 09:45:45.805824 lnhub_rest-0.7.3/.github/workflows/latest-changes.jinja2
--rw-r--r--   0        0        0      613 2023-03-30 12:47:50.835447 lnhub_rest-0.7.3/.github/workflows/latest-changes.yml
--rw-r--r--   0        0        0     1212 2023-03-30 12:47:50.836395 lnhub_rest-0.7.3/.gitignore
--rw-r--r--   0        0        0     1772 2023-02-18 02:41:50.422341 lnhub_rest-0.7.3/.pre-commit-config.yaml
--rw-r--r--   0        0        0      134 2023-03-30 12:47:50.836955 lnhub_rest-0.7.3/Dockerfile
--rw-r--r--   0        0        0     1149 2023-03-30 13:19:18.604852 lnhub_rest-0.7.3/README.md
--rw-r--r--   0        0        0    12677 2023-01-30 16:03:09.912627 lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-2efe1dee9baf.svg
--rw-r--r--   0        0        0    16617 2023-03-30 12:47:50.838098 lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-a88f5298b8f7.svg
--rw-r--r--   0        0        0    13696 2023-01-23 16:47:40.572752 lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-c13c9dd0f3ae.svg
--rw-r--r--   0        0        0    12677 2023-01-30 16:03:01.303256 lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-e7151581f790.svg
--rw-r--r--   0        0        0    15062 2023-02-11 08:19:54.737363 lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-e7eef9775586.svg
--rw-r--r--   0        0        0    14594 2023-02-06 03:22:51.375074 lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-f2cb77148a6e.svg
--rw-r--r--   0        0        0    12677 2023-01-21 09:45:45.806372 lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-f7ba9352c706.svg
--rw-r--r--   0        0        0    14594 2023-02-06 04:17:13.996852 lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-fe962c9a0ae7.svg
--rw-r--r--   0        0        0     5302 2023-03-30 12:47:50.838904 lnhub_rest-0.7.3/docs/account/01-signup-signin.ipynb
--rw-r--r--   0        0        0     4484 2023-03-30 12:47:50.839598 lnhub_rest-0.7.3/docs/account/02-create-account.ipynb
--rw-r--r--   0        0        0     5600 2023-03-30 12:47:50.839973 lnhub_rest-0.7.3/docs/account/03-update-account.ipynb
--rw-r--r--   0        0        0     6188 2023-03-30 12:47:50.840482 lnhub_rest-0.7.3/docs/account/04-fetch-account.ipynb
--rw-r--r--   0        0        0     9826 2023-03-30 12:47:50.841115 lnhub_rest-0.7.3/docs/account/05-rls.ipynb
--rw-r--r--   0        0        0    20057 2023-04-07 11:11:22.675202 lnhub_rest-0.7.3/docs/changelog.md
--rw-r--r--   0        0        0     1299 2023-03-30 12:47:50.842208 lnhub_rest-0.7.3/docs/checks/01-check-break-lndb.ipynb
--rw-r--r--   0        0        0       69 2023-01-21 09:45:45.806494 lnhub_rest-0.7.3/docs/content.md
--rw-r--r--   0        0        0    11226 2023-03-30 12:47:50.842564 lnhub_rest-0.7.3/docs/instance/01-init-instance.ipynb
--rw-r--r--   0        0        0     5286 2023-03-30 12:47:50.843030 lnhub_rest-0.7.3/docs/instance/02-load-instance.ipynb
--rw-r--r--   0        0        0     6187 2023-03-30 12:47:50.843650 lnhub_rest-0.7.3/docs/instance/03-update-instance.ipynb
--rw-r--r--   0        0        0     7063 2023-04-04 09:48:29.001245 lnhub_rest-0.7.3/docs/instance/04-delete-instance.ipynb
--rw-r--r--   0        0        0     7023 2023-03-30 12:47:50.844657 lnhub_rest-0.7.3/docs/instance/05-fetch-instance.ipynb
--rw-r--r--   0        0        0    19524 2023-03-30 13:41:16.586041 lnhub_rest-0.7.3/docs/instance/06-rls.ipynb
--rw-r--r--   0        0        0     6881 2023-04-04 09:48:29.001772 lnhub_rest-0.7.3/docs/migration/01-migration.ipynb
--rw-r--r--   0        0        0      520 2023-02-18 02:41:50.423424 lnhub_rest-0.7.3/docs/migrations.md
--rw-r--r--   0        0        0      162 2023-02-18 02:41:50.423560 lnhub_rest-0.7.3/docs/notes/index.md
--rw-r--r--   0        0        0    26418 2023-03-31 06:14:32.444574 lnhub_rest-0.7.3/docs/notes/multiple-sign-ups-same-email.ipynb
--rw-r--r--   0        0        0     3866 2023-03-30 12:47:50.846599 lnhub_rest-0.7.3/docs/storage/01-add-storage.ipynb
--rw-r--r--   0        0        0     9665 2023-03-30 12:47:50.846975 lnhub_rest-0.7.3/docs/storage/02-rls.ipynb
--rw-r--r--   0        0        0      137 2023-01-21 09:45:45.806726 lnhub_rest-0.7.3/lamin-project.yaml
--rw-r--r--   0        0        0      225 2023-04-07 11:11:22.675271 lnhub_rest-0.7.3/lnhub_rest/__init__.py
--rw-r--r--   0        0        0     8143 2023-03-30 12:47:50.847973 lnhub_rest-0.7.3/lnhub_rest/__main__.py
--rw-r--r--   0        0        0       59 2023-03-30 12:47:50.848496 lnhub_rest-0.7.3/lnhub_rest/_add_storage.py
--rw-r--r--   0        0        0       64 2023-01-21 09:45:45.807011 lnhub_rest-0.7.3/lnhub_rest/_assets/__init__.py
--rw-r--r--   0        0        0     1026 2023-01-21 09:45:45.807071 lnhub_rest-0.7.3/lnhub_rest/_assets/_instances.py
--rw-r--r--   0        0        0     1094 2023-02-07 18:29:12.120185 lnhub_rest-0.7.3/lnhub_rest/_assets/_schemas.py
--rw-r--r--   0        0        0     1628 2023-03-30 12:47:50.849372 lnhub_rest-0.7.3/lnhub_rest/_check_breaks_lndb.py
--rw-r--r--   0        0        0     5375 2023-03-30 12:47:50.849882 lnhub_rest-0.7.3/lnhub_rest/_clean_ci.py
--rw-r--r--   0        0        0       64 2023-03-30 12:47:50.850319 lnhub_rest-0.7.3/lnhub_rest/_delete_instance.py
--rw-r--r--   0        0        0       45 2023-03-30 12:47:50.850817 lnhub_rest-0.7.3/lnhub_rest/_engine.py
--rw-r--r--   0        0        0       62 2023-03-30 12:47:50.851089 lnhub_rest-0.7.3/lnhub_rest/_init_instance.py
--rw-r--r--   0        0        0       62 2023-03-30 12:47:50.851363 lnhub_rest-0.7.3/lnhub_rest/_load_instance.py
--rw-r--r--   0        0        0       90 2023-01-21 09:45:45.807616 lnhub_rest-0.7.3/lnhub_rest/_models.py
--rw-r--r--   0        0        0       47 2023-03-30 12:47:50.851778 lnhub_rest-0.7.3/lnhub_rest/_sbclient.py
--rw-r--r--   0        0        0       61 2023-03-30 12:47:50.852085 lnhub_rest-0.7.3/lnhub_rest/_signup_signin.py
--rw-r--r--   0        0        0       42 2023-03-30 12:47:50.852238 lnhub_rest-0.7.3/lnhub_rest/core/__init__.py
--rw-r--r--   0        0        0      251 2023-03-30 12:47:50.853103 lnhub_rest-0.7.3/lnhub_rest/core/account/__init__.py
--rw-r--r--   0        0        0     1207 2023-03-30 12:47:50.853709 lnhub_rest-0.7.3/lnhub_rest/core/account/_create_account.py
--rw-r--r--   0        0        0     1062 2023-03-30 12:47:50.854091 lnhub_rest-0.7.3/lnhub_rest/core/account/_crud.py
--rw-r--r--   0        0        0      735 2023-03-30 12:47:50.854350 lnhub_rest-0.7.3/lnhub_rest/core/account/_delete_account.py
--rw-r--r--   0        0        0     3314 2023-03-30 12:47:50.854633 lnhub_rest-0.7.3/lnhub_rest/core/account/_signup_signin.py
--rw-r--r--   0        0        0     1419 2023-03-30 12:47:50.854997 lnhub_rest-0.7.3/lnhub_rest/core/account/_update_account.py
--rw-r--r--   0        0        0       38 2023-03-30 13:41:16.586807 lnhub_rest-0.7.3/lnhub_rest/core/collaborator/__init__.py
--rw-r--r--   0        0        0     2710 2023-04-04 09:48:29.002913 lnhub_rest-0.7.3/lnhub_rest/core/collaborator/_crud.py
--rw-r--r--   0        0        0      243 2023-03-30 12:47:50.856613 lnhub_rest-0.7.3/lnhub_rest/core/instance/__init__.py
--rw-r--r--   0        0        0     1651 2023-03-30 12:47:50.856859 lnhub_rest-0.7.3/lnhub_rest/core/instance/_crud.py
--rw-r--r--   0        0        0     1440 2023-04-04 09:48:29.003505 lnhub_rest-0.7.3/lnhub_rest/core/instance/_delete_instance.py
--rw-r--r--   0        0        0     6477 2023-03-30 12:47:50.857546 lnhub_rest-0.7.3/lnhub_rest/core/instance/_init_instance.py
--rw-r--r--   0        0        0     1528 2023-03-30 12:47:50.857781 lnhub_rest-0.7.3/lnhub_rest/core/instance/_load_instance.py
--rw-r--r--   0        0        0     1063 2023-03-30 13:19:18.609359 lnhub_rest-0.7.3/lnhub_rest/core/instance/_update_instance.py
--rw-r--r--   0        0        0       80 2023-03-30 12:47:50.858308 lnhub_rest-0.7.3/lnhub_rest/core/storage/__init__.py
--rw-r--r--   0        0        0     2775 2023-03-30 12:47:50.858813 lnhub_rest-0.7.3/lnhub_rest/core/storage/_add_storage.py
--rw-r--r--   0        0        0     1167 2023-03-30 12:47:50.859242 lnhub_rest-0.7.3/lnhub_rest/core/storage/_crud.py
--rw-r--r--   0        0        0      742 2023-03-30 12:47:50.859827 lnhub_rest-0.7.3/lnhub_rest/main.py
--rw-r--r--   0        0        0       11 2023-03-30 12:47:50.860315 lnhub_rest-0.7.3/lnhub_rest/orm/__init__.py
--rw-r--r--   0        0        0      224 2023-03-30 12:47:50.860773 lnhub_rest-0.7.3/lnhub_rest/orm/_engine.py
--rw-r--r--   0        0        0     2491 2023-03-31 06:29:00.104332 lnhub_rest-0.7.3/lnhub_rest/orm/_sbclient.py
--rw-r--r--   0        0        0      157 2023-03-30 12:47:50.861629 lnhub_rest-0.7.3/lnhub_rest/routers/__init__.py
--rw-r--r--   0        0        0     3034 2023-04-07 11:11:03.950428 lnhub_rest-0.7.3/lnhub_rest/routers/account.py
--rw-r--r--   0        0        0      538 2023-03-30 12:47:50.862589 lnhub_rest-0.7.3/lnhub_rest/routers/ci.py
--rw-r--r--   0        0        0      408 2023-03-30 12:47:50.862937 lnhub_rest-0.7.3/lnhub_rest/routers/dev.py
--rw-r--r--   0        0        0     4397 2023-03-30 13:19:18.609525 lnhub_rest-0.7.3/lnhub_rest/routers/instance.py
--rw-r--r--   0        0        0     1079 2023-03-30 12:47:50.863921 lnhub_rest-0.7.3/lnhub_rest/routers/utils.py
--rw-r--r--   0        0        0      245 2023-04-04 09:48:29.004209 lnhub_rest-0.7.3/lnhub_rest/schema/__init__.py
--rw-r--r--   0        0        0     3925 2023-04-04 09:48:29.004817 lnhub_rest-0.7.3/lnhub_rest/schema/_core.py
--rw-r--r--   0        0        0      270 2023-02-18 02:41:50.426182 lnhub_rest-0.7.3/lnhub_rest/schema/_timestamps.py
--rw-r--r--   0        0        0      252 2023-02-18 02:41:50.426385 lnhub_rest-0.7.3/lnhub_rest/schema/_users.py
--rw-r--r--   0        0        0     1079 2023-02-18 02:41:50.426502 lnhub_rest-0.7.3/lnhub_rest/schema/_versions.py
--rw-r--r--   0        0        0      674 2023-01-21 09:45:45.808225 lnhub_rest-0.7.3/lnhub_rest/schema/alembic.ini
--rw-r--r--   0        0        0       48 2023-03-10 14:48:26.653017 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/__init__.py
--rw-r--r--   0        0        0     2977 2023-03-30 12:47:50.865542 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/env.py
--rw-r--r--   0        0        0     1193 2023-03-30 12:47:50.866216 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/function/_2023_02_21_a88f5298b8f7_v0_4_2.py
--rw-r--r--   0        0        0       39 2023-03-30 12:47:50.866749 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/function/__init__.py
--rw-r--r--   0        0        0     3940 2023-03-30 12:47:50.867035 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/rls/_2023_02_21_a88f5298b8f7_v0_4_2.py
--rw-r--r--   0        0        0      639 2023-03-30 12:47:50.867452 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/rls/_2023_03_09_0c4d4fe5f2c6_v0_6_1.py
--rw-r--r--   0        0        0      222 2023-04-04 09:48:29.005122 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/rls/_2023_03_24_333fd693eac8_v0_6_1b.py
--rw-r--r--   0        0        0       33 2023-03-30 12:47:50.867945 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/rls/__init__.py
--rw-r--r--   0        0        0      542 2023-01-21 09:45:45.808428 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/script.py.mako
--rw-r--r--   0        0        0      757 2023-03-30 12:47:50.868322 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/settings.py
--rw-r--r--   0        0        0      170 2023-04-04 09:48:29.005328 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/utils.py
--rw-r--r--   0        0        0     1816 2023-01-21 09:45:45.808625 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-01-13-53709f2a2043-v0_0_1a.py
--rw-r--r--   0        0        0      935 2023-01-21 09:45:45.808695 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-01-13-c555c87a640c-v0_0_1.py
--rw-r--r--   0        0        0     5052 2023-01-21 09:45:45.808760 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-01-14-f7ba9352c706-v0_0_2.py
--rw-r--r--   0        0        0     1401 2023-01-23 16:47:40.574183 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-01-23-c13c9dd0f3ae-v0_1_4a.py
--rw-r--r--   0        0        0      536 2023-01-24 17:03:32.132346 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-01-24-e7151581f790-v0_1_4b.py
--rw-r--r--   0        0        0      512 2023-01-30 16:03:09.913495 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-01-30-2efe1dee9baf-v0_1_4c.py
--rw-r--r--   0        0        0      667 2023-02-06 03:51:44.507281 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-06-95073282294e-v0_1_4e.py
--rw-r--r--   0        0        0      869 2023-02-08 11:03:56.952408 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-06-9c02109e4faa-v0_2_0.py
--rw-r--r--   0        0        0     2190 2023-02-06 03:05:52.825943 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-06-f2cb77148a6e-v0_1_4d.py
--rw-r--r--   0        0        0      458 2023-02-08 11:03:56.952546 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-08-e7eef9775586-0_2_1.py
--rw-r--r--   0        0        0     1220 2023-02-18 02:41:50.426631 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-15-641d1508baab-v0_4_0.py
--rw-r--r--   0        0        0      624 2023-02-18 02:41:50.426731 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-16-1fdc05837919-v0_4_1.py
--rw-r--r--   0        0        0      918 2023-03-30 12:47:50.868888 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-21-a88f5298b8f7-v0_4_2.py
--rw-r--r--   0        0        0      575 2023-03-30 12:47:50.869315 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-03-09-0c4d4fe5f2c6-v0_6_1.py
--rw-r--r--   0        0        0      558 2023-04-04 09:48:29.005551 lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-03-24-333fd693eac8-v0_6_1b.py
--rw-r--r--   0        0        0       60 2023-02-18 02:41:50.426815 lnhub_rest-0.7.3/lnhub_rest/schema/versions.py
--rw-r--r--   0        0        0      171 2023-03-30 12:47:50.870315 lnhub_rest-0.7.3/lnhub_rest/utils/__init__.py
--rw-r--r--   0        0        0      212 2023-03-30 12:47:50.870738 lnhub_rest-0.7.3/lnhub_rest/utils/_access_token.py
--rw-r--r--   0        0        0      259 2023-03-30 12:47:50.871114 lnhub_rest-0.7.3/lnhub_rest/utils/_id.py
--rw-r--r--   0        0        0      109 2023-03-30 12:47:50.871506 lnhub_rest-0.7.3/lnhub_rest/utils/_query.py
--rw-r--r--   0        0        0     3803 2023-03-30 12:47:50.871751 lnhub_rest-0.7.3/lnhub_rest/utils/_test.py
--rw-r--r--   0        0        0     1111 2023-04-04 09:48:29.005988 lnhub_rest-0.7.3/noxfile.py
--rw-r--r--   0        0        0     1302 2023-03-30 12:47:50.872289 lnhub_rest-0.7.3/pyproject.toml
--rwxr-xr-x   0        0        0       29 2023-03-30 12:47:50.872391 lnhub_rest-0.7.3/scripts/run.sh
--rw-r--r--   0        0        0       27 2023-02-21 14:39:20.630598 lnhub_rest-0.7.3/supabase/.gitignore
--rw-r--r--   0        0        0     2548 2023-02-21 14:39:20.630843 lnhub_rest-0.7.3/supabase/config.toml
--rw-r--r--   0        0        0      760 2023-03-30 12:47:50.872822 lnhub_rest-0.7.3/tests/test_notebooks.py
--rw-r--r--   0        0        0     2169 1970-01-01 00:00:00.000000 lnhub_rest-0.7.3/PKG-INFO
+-rw-r--r--   0        0        0     1259 2023-02-13 09:20:16.808732 lnhub_rest-0.7rc1/.dockerignore
+-rw-r--r--   0        0        0     2724 2023-03-08 16:14:44.728272 lnhub_rest-0.7rc1/.github/workflows/build.yml
+-rw-r--r--   0        0        0     4871 2023-03-29 09:08:29.674856 lnhub_rest-0.7rc1/.github/workflows/google-cloudrun-docker.yml
+-rw-r--r--   0        0        0      133 2022-12-05 16:31:02.016205 lnhub_rest-0.7rc1/.github/workflows/latest-changes.jinja2
+-rw-r--r--   0        0        0      613 2023-03-08 16:14:44.728725 lnhub_rest-0.7rc1/.github/workflows/latest-changes.yml
+-rw-r--r--   0        0        0     1212 2023-03-08 16:14:44.728869 lnhub_rest-0.7rc1/.gitignore
+-rw-r--r--   0        0        0     1772 2023-03-02 11:17:31.745149 lnhub_rest-0.7rc1/.pre-commit-config.yaml
+-rw-r--r--   0        0        0      134 2023-03-08 16:14:44.728986 lnhub_rest-0.7rc1/Dockerfile
+-rw-r--r--   0        0        0     1149 2023-03-29 09:08:29.675283 lnhub_rest-0.7rc1/README.md
+-rw-r--r--   0        0        0    12677 2023-02-13 09:20:16.809717 lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-2efe1dee9baf.svg
+-rw-r--r--   0        0        0    16617 2023-03-08 16:14:44.729168 lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-a88f5298b8f7.svg
+-rw-r--r--   0        0        0    13696 2023-02-13 09:20:16.809873 lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-c13c9dd0f3ae.svg
+-rw-r--r--   0        0        0    12677 2023-02-13 09:20:16.809956 lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-e7151581f790.svg
+-rw-r--r--   0        0        0    15062 2023-02-13 09:20:16.810073 lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-e7eef9775586.svg
+-rw-r--r--   0        0        0    14594 2023-02-13 09:20:16.810196 lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-f2cb77148a6e.svg
+-rw-r--r--   0        0        0    12677 2023-02-13 09:20:16.810300 lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-f7ba9352c706.svg
+-rw-r--r--   0        0        0    14594 2023-02-13 09:20:16.810415 lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-fe962c9a0ae7.svg
+-rw-r--r--   0        0        0     5302 2023-03-14 16:02:39.647880 lnhub_rest-0.7rc1/docs/account/01-signup-signin.ipynb
+-rw-r--r--   0        0        0     4484 2023-03-14 16:02:39.645047 lnhub_rest-0.7rc1/docs/account/02-create-account.ipynb
+-rw-r--r--   0        0        0     5600 2023-03-14 16:02:39.643723 lnhub_rest-0.7rc1/docs/account/03-update-account.ipynb
+-rw-r--r--   0        0        0     6188 2023-03-14 16:02:39.646649 lnhub_rest-0.7rc1/docs/account/04-fetch-account.ipynb
+-rw-r--r--   0        0        0     9826 2023-03-14 16:02:39.646731 lnhub_rest-0.7rc1/docs/account/05-rls.ipynb
+-rw-r--r--   0        0        0    19381 2023-03-29 10:55:16.837446 lnhub_rest-0.7rc1/docs/changelog.md
+-rw-r--r--   0        0        0     1299 2023-03-15 11:16:45.486458 lnhub_rest-0.7rc1/docs/checks/01-check-break-lndb.ipynb
+-rw-r--r--   0        0        0       69 2023-02-13 09:20:16.810963 lnhub_rest-0.7rc1/docs/content.md
+-rw-r--r--   0        0        0    11226 2023-03-14 16:02:39.646645 lnhub_rest-0.7rc1/docs/instance/01-init-instance.ipynb
+-rw-r--r--   0        0        0     5286 2023-03-15 11:18:07.148653 lnhub_rest-0.7rc1/docs/instance/02-load-instance.ipynb
+-rw-r--r--   0        0        0     6187 2023-03-14 16:02:39.643793 lnhub_rest-0.7rc1/docs/instance/03-update-instance.ipynb
+-rw-r--r--   0        0        0     7063 2023-03-29 10:50:51.815991 lnhub_rest-0.7rc1/docs/instance/04-delete-instance.ipynb
+-rw-r--r--   0        0        0     7023 2023-03-29 10:50:51.816594 lnhub_rest-0.7rc1/docs/instance/05-fetch-instance.ipynb
+-rw-r--r--   0        0        0    19524 2023-03-29 10:50:58.291610 lnhub_rest-0.7rc1/docs/instance/06-rls.ipynb
+-rw-r--r--   0        0        0     6881 2023-03-29 10:50:58.291810 lnhub_rest-0.7rc1/docs/migration/01-migration.ipynb
+-rw-r--r--   0        0        0      520 2023-03-02 11:17:31.746920 lnhub_rest-0.7rc1/docs/migrations.md
+-rw-r--r--   0        0        0      162 2023-03-02 11:17:31.748210 lnhub_rest-0.7rc1/docs/notes/index.md
+-rw-r--r--   0        0        0    26218 2023-03-08 16:14:44.732401 lnhub_rest-0.7rc1/docs/notes/multiple-sign-ups-same-email.ipynb
+-rw-r--r--   0        0        0     3866 2023-03-14 16:02:39.643530 lnhub_rest-0.7rc1/docs/storage/01-add-storage.ipynb
+-rw-r--r--   0        0        0     9665 2023-03-14 16:02:39.644130 lnhub_rest-0.7rc1/docs/storage/02-rls.ipynb
+-rw-r--r--   0        0        0      137 2022-12-05 16:31:02.018378 lnhub_rest-0.7rc1/lamin-project.yaml
+-rw-r--r--   0        0        0      226 2023-03-29 10:55:19.550099 lnhub_rest-0.7rc1/lnhub_rest/__init__.py
+-rw-r--r--   0        0        0     8143 2023-03-29 10:50:51.817381 lnhub_rest-0.7rc1/lnhub_rest/__main__.py
+-rw-r--r--   0        0        0       59 2023-03-08 16:14:44.733412 lnhub_rest-0.7rc1/lnhub_rest/_add_storage.py
+-rw-r--r--   0        0        0       64 2023-02-13 09:20:16.812158 lnhub_rest-0.7rc1/lnhub_rest/_assets/__init__.py
+-rw-r--r--   0        0        0     1026 2023-02-13 09:20:16.812240 lnhub_rest-0.7rc1/lnhub_rest/_assets/_instances.py
+-rw-r--r--   0        0        0     1094 2023-02-13 09:20:16.812323 lnhub_rest-0.7rc1/lnhub_rest/_assets/_schemas.py
+-rw-r--r--   0        0        0     1628 2023-03-13 07:50:24.229781 lnhub_rest-0.7rc1/lnhub_rest/_check_breaks_lndb.py
+-rw-r--r--   0        0        0     5375 2023-03-08 16:14:44.733769 lnhub_rest-0.7rc1/lnhub_rest/_clean_ci.py
+-rw-r--r--   0        0        0       64 2023-03-08 16:14:44.733916 lnhub_rest-0.7rc1/lnhub_rest/_delete_instance.py
+-rw-r--r--   0        0        0       45 2023-03-08 16:14:44.734007 lnhub_rest-0.7rc1/lnhub_rest/_engine.py
+-rw-r--r--   0        0        0       62 2023-03-08 16:14:44.734105 lnhub_rest-0.7rc1/lnhub_rest/_init_instance.py
+-rw-r--r--   0        0        0       62 2023-03-08 16:14:44.734189 lnhub_rest-0.7rc1/lnhub_rest/_load_instance.py
+-rw-r--r--   0        0        0       90 2023-02-13 09:20:16.813123 lnhub_rest-0.7rc1/lnhub_rest/_models.py
+-rw-r--r--   0        0        0       47 2023-03-08 16:14:44.734275 lnhub_rest-0.7rc1/lnhub_rest/_sbclient.py
+-rw-r--r--   0        0        0       61 2023-03-08 16:14:44.734361 lnhub_rest-0.7rc1/lnhub_rest/_signup_signin.py
+-rw-r--r--   0        0        0       42 2023-03-08 16:14:44.734489 lnhub_rest-0.7rc1/lnhub_rest/core/__init__.py
+-rw-r--r--   0        0        0      251 2023-03-08 16:14:44.734790 lnhub_rest-0.7rc1/lnhub_rest/core/account/__init__.py
+-rw-r--r--   0        0        0     1207 2023-03-08 16:14:44.734878 lnhub_rest-0.7rc1/lnhub_rest/core/account/_create_account.py
+-rw-r--r--   0        0        0     1062 2023-03-08 16:14:44.734978 lnhub_rest-0.7rc1/lnhub_rest/core/account/_crud.py
+-rw-r--r--   0        0        0      735 2023-03-08 16:14:44.735141 lnhub_rest-0.7rc1/lnhub_rest/core/account/_delete_account.py
+-rw-r--r--   0        0        0     3314 2023-03-24 15:16:03.675096 lnhub_rest-0.7rc1/lnhub_rest/core/account/_signup_signin.py
+-rw-r--r--   0        0        0     1419 2023-03-08 16:14:44.735288 lnhub_rest-0.7rc1/lnhub_rest/core/account/_update_account.py
+-rw-r--r--   0        0        0       38 2023-03-29 10:50:58.291948 lnhub_rest-0.7rc1/lnhub_rest/core/collaborator/__init__.py
+-rw-r--r--   0        0        0     2710 2023-03-29 10:50:58.292258 lnhub_rest-0.7rc1/lnhub_rest/core/collaborator/_crud.py
+-rw-r--r--   0        0        0      243 2023-03-08 16:14:44.735569 lnhub_rest-0.7rc1/lnhub_rest/core/instance/__init__.py
+-rw-r--r--   0        0        0     1651 2023-03-13 13:43:06.983275 lnhub_rest-0.7rc1/lnhub_rest/core/instance/_crud.py
+-rw-r--r--   0        0        0     1440 2023-03-29 10:50:58.292588 lnhub_rest-0.7rc1/lnhub_rest/core/instance/_delete_instance.py
+-rw-r--r--   0        0        0     6477 2023-03-08 16:14:44.735785 lnhub_rest-0.7rc1/lnhub_rest/core/instance/_init_instance.py
+-rw-r--r--   0        0        0     1528 2023-03-15 11:18:07.150180 lnhub_rest-0.7rc1/lnhub_rest/core/instance/_load_instance.py
+-rw-r--r--   0        0        0     1063 2023-03-29 09:08:29.676385 lnhub_rest-0.7rc1/lnhub_rest/core/instance/_update_instance.py
+-rw-r--r--   0        0        0       80 2023-03-08 16:14:44.735963 lnhub_rest-0.7rc1/lnhub_rest/core/storage/__init__.py
+-rw-r--r--   0        0        0     2775 2023-03-08 16:14:44.736240 lnhub_rest-0.7rc1/lnhub_rest/core/storage/_add_storage.py
+-rw-r--r--   0        0        0     1167 2023-03-08 16:14:44.736339 lnhub_rest-0.7rc1/lnhub_rest/core/storage/_crud.py
+-rw-r--r--   0        0        0      742 2023-03-08 16:14:44.736544 lnhub_rest-0.7rc1/lnhub_rest/main.py
+-rw-r--r--   0        0        0       11 2023-03-08 16:14:44.736622 lnhub_rest-0.7rc1/lnhub_rest/orm/__init__.py
+-rw-r--r--   0        0        0      224 2023-03-08 16:14:44.736695 lnhub_rest-0.7rc1/lnhub_rest/orm/_engine.py
+-rw-r--r--   0        0        0     2380 2023-03-29 09:46:37.463552 lnhub_rest-0.7rc1/lnhub_rest/orm/_sbclient.py
+-rw-r--r--   0        0        0      157 2023-03-08 16:14:44.736894 lnhub_rest-0.7rc1/lnhub_rest/routers/__init__.py
+-rw-r--r--   0        0        0     2724 2023-03-13 07:50:24.229941 lnhub_rest-0.7rc1/lnhub_rest/routers/account.py
+-rw-r--r--   0        0        0      538 2023-03-08 16:14:44.737254 lnhub_rest-0.7rc1/lnhub_rest/routers/ci.py
+-rw-r--r--   0        0        0      408 2023-03-08 16:14:44.737389 lnhub_rest-0.7rc1/lnhub_rest/routers/dev.py
+-rw-r--r--   0        0        0     4397 2023-03-29 09:08:29.676776 lnhub_rest-0.7rc1/lnhub_rest/routers/instance.py
+-rw-r--r--   0        0        0     1079 2023-03-08 16:14:44.737615 lnhub_rest-0.7rc1/lnhub_rest/routers/utils.py
+-rw-r--r--   0        0        0      245 2023-03-29 10:50:58.292912 lnhub_rest-0.7rc1/lnhub_rest/schema/__init__.py
+-rw-r--r--   0        0        0     3925 2023-03-20 08:26:20.388108 lnhub_rest-0.7rc1/lnhub_rest/schema/_core.py
+-rw-r--r--   0        0        0      270 2023-03-02 11:17:31.752043 lnhub_rest-0.7rc1/lnhub_rest/schema/_timestamps.py
+-rw-r--r--   0        0        0      252 2023-03-02 11:17:31.752112 lnhub_rest-0.7rc1/lnhub_rest/schema/_users.py
+-rw-r--r--   0        0        0     1079 2023-03-02 11:17:31.752187 lnhub_rest-0.7rc1/lnhub_rest/schema/_versions.py
+-rw-r--r--   0        0        0      674 2023-02-13 09:20:16.814087 lnhub_rest-0.7rc1/lnhub_rest/schema/alembic.ini
+-rw-r--r--   0        0        0       48 2023-02-13 09:20:16.814178 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/__init__.py
+-rw-r--r--   0        0        0     2977 2023-03-08 16:14:44.737843 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/env.py
+-rw-r--r--   0        0        0     1193 2023-03-13 07:50:24.230447 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/function/_2023_02_21_a88f5298b8f7_v0_4_2.py
+-rw-r--r--   0        0        0       39 2023-03-13 07:50:24.230571 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/function/__init__.py
+-rw-r--r--   0        0        0     3940 2023-03-13 07:50:24.230771 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/rls/_2023_02_21_a88f5298b8f7_v0_4_2.py
+-rw-r--r--   0        0        0      639 2023-03-24 15:20:21.151607 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/rls/_2023_03_09_0c4d4fe5f2c6_v0_6_1.py
+-rw-r--r--   0        0        0      222 2023-03-29 10:50:58.293165 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/rls/_2023_03_24_333fd693eac8_v0_6_1b.py
+-rw-r--r--   0        0        0       33 2023-03-13 07:50:24.230894 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/rls/__init__.py
+-rw-r--r--   0        0        0      542 2023-02-13 09:20:16.814349 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/script.py.mako
+-rw-r--r--   0        0        0      757 2023-03-08 16:14:44.737944 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/settings.py
+-rw-r--r--   0        0        0      170 2023-02-13 09:20:16.814484 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/utils.py
+-rw-r--r--   0        0        0     1816 2023-02-13 09:20:16.814592 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-01-13-53709f2a2043-v0_0_1a.py
+-rw-r--r--   0        0        0      935 2023-02-13 09:20:16.814670 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-01-13-c555c87a640c-v0_0_1.py
+-rw-r--r--   0        0        0     5052 2023-02-13 09:20:16.814754 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-01-14-f7ba9352c706-v0_0_2.py
+-rw-r--r--   0        0        0     1401 2023-02-13 09:20:16.814833 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-01-23-c13c9dd0f3ae-v0_1_4a.py
+-rw-r--r--   0        0        0      536 2023-02-13 09:20:16.814901 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-01-24-e7151581f790-v0_1_4b.py
+-rw-r--r--   0        0        0      512 2023-02-13 09:20:16.814968 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-01-30-2efe1dee9baf-v0_1_4c.py
+-rw-r--r--   0        0        0      667 2023-02-13 09:20:16.815042 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-06-95073282294e-v0_1_4e.py
+-rw-r--r--   0        0        0      869 2023-02-13 09:20:16.815111 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-06-9c02109e4faa-v0_2_0.py
+-rw-r--r--   0        0        0     2190 2023-02-13 09:20:16.815184 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-06-f2cb77148a6e-v0_1_4d.py
+-rw-r--r--   0        0        0      458 2023-02-13 09:20:16.815255 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-08-e7eef9775586-0_2_1.py
+-rw-r--r--   0        0        0     1220 2023-03-02 11:17:31.752307 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-15-641d1508baab-v0_4_0.py
+-rw-r--r--   0        0        0      624 2023-03-02 11:17:31.752395 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-16-1fdc05837919-v0_4_1.py
+-rw-r--r--   0        0        0      918 2023-03-13 07:50:24.231076 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-21-a88f5298b8f7-v0_4_2.py
+-rw-r--r--   0        0        0      575 2023-03-24 15:20:21.152374 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-03-09-0c4d4fe5f2c6-v0_6_1.py
+-rw-r--r--   0        0        0      558 2023-03-29 10:50:58.293373 lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-03-24-333fd693eac8-v0_6_1b.py
+-rw-r--r--   0        0        0       60 2023-03-02 11:17:31.752459 lnhub_rest-0.7rc1/lnhub_rest/schema/versions.py
+-rw-r--r--   0        0        0      171 2023-03-08 16:14:44.738113 lnhub_rest-0.7rc1/lnhub_rest/utils/__init__.py
+-rw-r--r--   0        0        0      212 2023-03-08 16:14:44.738175 lnhub_rest-0.7rc1/lnhub_rest/utils/_access_token.py
+-rw-r--r--   0        0        0      259 2023-03-08 16:14:44.738231 lnhub_rest-0.7rc1/lnhub_rest/utils/_id.py
+-rw-r--r--   0        0        0      109 2023-03-08 16:14:44.738291 lnhub_rest-0.7rc1/lnhub_rest/utils/_query.py
+-rw-r--r--   0        0        0     3803 2023-03-24 15:16:03.676926 lnhub_rest-0.7rc1/lnhub_rest/utils/_test.py
+-rw-r--r--   0        0        0     1111 2023-03-29 09:08:29.677007 lnhub_rest-0.7rc1/noxfile.py
+-rw-r--r--   0        0        0     1302 2023-03-24 15:16:03.677102 lnhub_rest-0.7rc1/pyproject.toml
+-rwxr-xr-x   0        0        0       29 2023-03-08 16:14:44.738954 lnhub_rest-0.7rc1/scripts/run.sh
+-rw-r--r--   0        0        0       27 2023-03-02 11:17:31.752828 lnhub_rest-0.7rc1/supabase/.gitignore
+-rw-r--r--   0        0        0     2548 2023-03-02 11:17:31.752925 lnhub_rest-0.7rc1/supabase/config.toml
+-rw-r--r--   0        0        0      760 2023-03-13 07:50:24.231725 lnhub_rest-0.7rc1/tests/test_notebooks.py
+-rw-r--r--   0        0        0     2170 1970-01-01 00:00:00.000000 lnhub_rest-0.7rc1/PKG-INFO
```

### Comparing `lnhub_rest-0.7.3/.dockerignore` & `lnhub_rest-0.7rc1/.dockerignore`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/.github/workflows/build.yml` & `lnhub_rest-0.7rc1/.github/workflows/build.yml`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/.github/workflows/google-cloudrun-docker.yml` & `lnhub_rest-0.7rc1/.github/workflows/google-cloudrun-docker.yml`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/.github/workflows/latest-changes.yml` & `lnhub_rest-0.7rc1/.github/workflows/latest-changes.yml`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/.gitignore` & `lnhub_rest-0.7rc1/.gitignore`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/.pre-commit-config.yaml` & `lnhub_rest-0.7rc1/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/README.md` & `lnhub_rest-0.7rc1/README.md`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-2efe1dee9baf.svg` & `lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-2efe1dee9baf.svg`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-a88f5298b8f7.svg` & `lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-a88f5298b8f7.svg`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-c13c9dd0f3ae.svg` & `lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-c13c9dd0f3ae.svg`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-e7151581f790.svg` & `lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-e7151581f790.svg`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-e7eef9775586.svg` & `lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-e7eef9775586.svg`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-f2cb77148a6e.svg` & `lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-f2cb77148a6e.svg`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-f7ba9352c706.svg` & `lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-f7ba9352c706.svg`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/_schemas/lnhub-schema-fe962c9a0ae7.svg` & `lnhub_rest-0.7rc1/docs/_schemas/lnhub-schema-fe962c9a0ae7.svg`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/account/01-signup-signin.ipynb` & `lnhub_rest-0.7rc1/docs/account/01-signup-signin.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/account/02-create-account.ipynb` & `lnhub_rest-0.7rc1/docs/account/02-create-account.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/account/03-update-account.ipynb` & `lnhub_rest-0.7rc1/docs/account/03-update-account.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/account/04-fetch-account.ipynb` & `lnhub_rest-0.7rc1/docs/account/04-fetch-account.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/account/05-rls.ipynb` & `lnhub_rest-0.7rc1/docs/account/05-rls.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/changelog.md` & `lnhub_rest-0.7rc1/docs/changelog.md`

 * *Files 1% similar despite different names*

```diff
@@ -1,16 +1,12 @@
 # Changelog
 
 <!-- prettier-ignore -->
 Name | PR | Developer | Date | Version
 --- | --- | --- | --- | ---
-✨ Create an endpoint to fetch avatar given a list of lnid | [166](https://github.com/laminlabs/lnhub-rest/pull/166) | [fredericenard](https://github.com/fredericenard) | 2023-04-07 | 0.7.3
-🐛 Fix sign in | [160](https://github.com/laminlabs/lnhub-rest/pull/160) | [fredericenard](https://github.com/fredericenard) | 2023-03-31 | 0.7.2
-🐛 Enforce compatibility with new sign in API | [159](https://github.com/laminlabs/lnhub-rest/pull/159) | [fredericenard](https://github.com/fredericenard) | 2023-03-31 | 0.7.1
-🔖 Staging version 0.7.0 | [150](https://github.com/laminlabs/lnhub-rest/pull/150) | [fredericenard](https://github.com/fredericenard) | 2023-03-29 | 0.7.0
 ⚡ Improve instance deletion through RLS | [154](https://github.com/laminlabs/lnhub-rest/pull/154) | [bpenteado](https://github.com/bpenteado) | 2023-03-29 | 0.7rc1
 ✨ Enable instance ownership transfer | [156](https://github.com/laminlabs/lnhub-rest/pull/156) | [bpenteado](https://github.com/bpenteado) | 2023-03-28 |
 Deploy lnhub-rest on Cloud Run using Github actions | [155](https://github.com/laminlabs/lnhub-rest/pull/155) | [lawrlee](https://github.com/lawrlee) | 2023-03-27 |
 🐛 Ensure integrity of RLS for local tests | [152](https://github.com/laminlabs/lnhub-rest/pull/152) | [fredericenard](https://github.com/fredericenard) | 2023-03-24 |
 🐛 Add test to ensure an owner can delete collaborators | [153](https://github.com/laminlabs/lnhub-rest/pull/153) | [fredericenard](https://github.com/fredericenard) | 2023-03-24 |
 ⬆️ Upgrade supabase | [149](https://github.com/laminlabs/lnhub-rest/pull/149) | [fredericenard](https://github.com/fredericenard) | 2023-03-23 |
 🔖 Staging version 0.7.0 | [148](https://github.com/laminlabs/lnhub-rest/pull/148) | [bpenteado](https://github.com/bpenteado) | 2023-03-21 |
```

### Comparing `lnhub_rest-0.7.3/docs/checks/01-check-break-lndb.ipynb` & `lnhub_rest-0.7rc1/docs/checks/01-check-break-lndb.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/instance/01-init-instance.ipynb` & `lnhub_rest-0.7rc1/docs/instance/01-init-instance.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/instance/02-load-instance.ipynb` & `lnhub_rest-0.7rc1/docs/instance/02-load-instance.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/instance/03-update-instance.ipynb` & `lnhub_rest-0.7rc1/docs/instance/03-update-instance.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/instance/04-delete-instance.ipynb` & `lnhub_rest-0.7rc1/docs/instance/04-delete-instance.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/instance/05-fetch-instance.ipynb` & `lnhub_rest-0.7rc1/docs/instance/05-fetch-instance.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/instance/06-rls.ipynb` & `lnhub_rest-0.7rc1/docs/instance/06-rls.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/migration/01-migration.ipynb` & `lnhub_rest-0.7rc1/docs/migration/01-migration.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/migrations.md` & `lnhub_rest-0.7rc1/docs/migrations.md`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/notes/multiple-sign-ups-same-email.ipynb` & `lnhub_rest-0.7rc1/docs/notes/multiple-sign-ups-same-email.ipynb`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9994918699186992%*

 * *Differences: {"'cells'": "{37: {'source': ['hub.auth.sign_in(email=settings.email, password=password1)']}, 39: "*

 * *            "{'source': ['hub.auth.sign_in(email=settings.email, password=password2)']}}"}*

```diff
@@ -553,20 +553,15 @@
                     },
                     "execution_count": 31,
                     "metadata": {},
                     "output_type": "execute_result"
                 }
             ],
             "source": [
-                "hub.auth.sign_in_with_password(\n",
-                "    {\n",
-                "        \"email\": settings.email,\n",
-                "        \"password\": password1,\n",
-                "    }\n",
-                ")"
+                "hub.auth.sign_in(email=settings.email, password=password1)"
             ]
         },
         {
             "cell_type": "markdown",
             "id": "e41c4704-0a74-4be6-8a93-c24e41bfb4b2",
             "metadata": {},
             "source": [
@@ -598,20 +593,15 @@
                         "File \u001b[0;32m/opt/anaconda3/envs/base1/lib/python3.9/site-packages/gotrue/types.py:26\u001b[0m, in \u001b[0;36mBaseModelFromResponse.parse_response\u001b[0;34m(cls, response)\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[38;5;129m@classmethod\u001b[39m\n\u001b[1;32m     25\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mparse_response\u001b[39m(\u001b[38;5;28mcls\u001b[39m: Type[T], response: Response) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m T:\n\u001b[0;32m---> 26\u001b[0m     \u001b[43mcheck_response\u001b[49m\u001b[43m(\u001b[49m\u001b[43mresponse\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     27\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mcls\u001b[39m\u001b[38;5;241m.\u001b[39mparse_obj(response\u001b[38;5;241m.\u001b[39mjson())\n",
                         "File \u001b[0;32m/opt/anaconda3/envs/base1/lib/python3.9/site-packages/gotrue/helpers.py:18\u001b[0m, in \u001b[0;36mcheck_response\u001b[0;34m(response)\u001b[0m\n\u001b[1;32m     16\u001b[0m     response\u001b[38;5;241m.\u001b[39mraise_for_status()\n\u001b[1;32m     17\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m HTTPError:\n\u001b[0;32m---> 18\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m APIError\u001b[38;5;241m.\u001b[39mfrom_dict(response\u001b[38;5;241m.\u001b[39mjson())\n",
                         "\u001b[0;31mAPIError\u001b[0m: "
                     ]
                 }
             ],
             "source": [
-                "hub.auth.sign_in_with_password(\n",
-                "    {\n",
-                "        \"email\": settings.email,\n",
-                "        \"password\": password2,\n",
-                "    }\n",
-                ")"
+                "hub.auth.sign_in(email=settings.email, password=password2)"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
             "id": "21b389b7-b362-41d0-8944-60df78e465ee",
             "metadata": {},
```

### Comparing `lnhub_rest-0.7.3/docs/storage/01-add-storage.ipynb` & `lnhub_rest-0.7rc1/docs/storage/01-add-storage.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/docs/storage/02-rls.ipynb` & `lnhub_rest-0.7rc1/docs/storage/02-rls.ipynb`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/__main__.py` & `lnhub_rest-0.7rc1/lnhub_rest/__main__.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/_assets/_instances.py` & `lnhub_rest-0.7rc1/lnhub_rest/_assets/_instances.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/_assets/_schemas.py` & `lnhub_rest-0.7rc1/lnhub_rest/_assets/_schemas.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/_check_breaks_lndb.py` & `lnhub_rest-0.7rc1/lnhub_rest/_check_breaks_lndb.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/_clean_ci.py` & `lnhub_rest-0.7rc1/lnhub_rest/_clean_ci.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/account/_create_account.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/account/_create_account.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/account/_crud.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/account/_crud.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/account/_delete_account.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/account/_delete_account.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/account/_signup_signin.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/account/_signup_signin.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/account/_update_account.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/account/_update_account.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/collaborator/_crud.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/collaborator/_crud.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/instance/_crud.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/instance/_crud.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/instance/_delete_instance.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/instance/_delete_instance.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/instance/_init_instance.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/instance/_init_instance.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/instance/_load_instance.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/instance/_load_instance.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/instance/_update_instance.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/instance/_update_instance.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/storage/_add_storage.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/storage/_add_storage.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/core/storage/_crud.py` & `lnhub_rest-0.7rc1/lnhub_rest/core/storage/_crud.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/main.py` & `lnhub_rest-0.7rc1/lnhub_rest/main.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/orm/_sbclient.py` & `lnhub_rest-0.7rc1/lnhub_rest/orm/_sbclient.py`

 * *Files 11% similar despite different names*

```diff
@@ -70,16 +70,11 @@
         os.environ["SUPABASE_PROD_SERVICE_ROLE_KEY"],
     )
 
 
 def get_access_token(email: Optional[str] = None, password: Optional[str] = None):
     hub = connect_hub()
     try:
-        auth_response = hub.auth.sign_in_with_password(
-            {
-                "email": email,
-                "password": password,
-            }
-        )
-        return auth_response.session.access_token
+        session = hub.auth.sign_in(email=email, password=password)
+        return session.access_token
     finally:
         hub.auth.sign_out()
```

### Comparing `lnhub_rest-0.7.3/lnhub_rest/routers/account.py` & `lnhub_rest-0.7rc1/lnhub_rest/routers/account.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
-from typing import Annotated, Union
+from typing import Union
 
-from fastapi import APIRouter, Header, Query
+from fastapi import APIRouter, Header
 
 from ..core.account._create_account import create_account as create_account_base
 from ..core.account._update_account import update_account as update_account_base
 from .utils import extract_access_token, get_supabase_client, supabase_client
 
 router = APIRouter(prefix="/account")
 
@@ -88,19 +88,7 @@
         twitter_handle=twitter_handle,
         website=website,
         _access_token=access_token,
     )
     if message is None:
         return "success"
     return message
-
-
-@router.get("/bulk/avatars")
-def get_account_avatars(lnids: Annotated[list[str], Query()]):
-    data = (
-        supabase_client.table("account")
-        .select("lnid, avatar_url")
-        .in_("lnid", lnids)
-        .execute()
-        .data
-    )
-    return data if len(data) > 0 else []
```

### Comparing `lnhub_rest-0.7.3/lnhub_rest/routers/ci.py` & `lnhub_rest-0.7rc1/lnhub_rest/routers/ci.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/routers/instance.py` & `lnhub_rest-0.7rc1/lnhub_rest/routers/instance.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/routers/utils.py` & `lnhub_rest-0.7rc1/lnhub_rest/routers/utils.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/_core.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/_core.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/_versions.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/_versions.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/alembic.ini` & `lnhub_rest-0.7rc1/lnhub_rest/schema/alembic.ini`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/env.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/env.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/function/_2023_02_21_a88f5298b8f7_v0_4_2.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/function/_2023_02_21_a88f5298b8f7_v0_4_2.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/rls/_2023_02_21_a88f5298b8f7_v0_4_2.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/rls/_2023_02_21_a88f5298b8f7_v0_4_2.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/rls/_2023_03_09_0c4d4fe5f2c6_v0_6_1.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/rls/_2023_03_09_0c4d4fe5f2c6_v0_6_1.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/script.py.mako` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/script.py.mako`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/settings.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/settings.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-01-13-53709f2a2043-v0_0_1a.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-01-13-53709f2a2043-v0_0_1a.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-01-13-c555c87a640c-v0_0_1.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-01-13-c555c87a640c-v0_0_1.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-01-14-f7ba9352c706-v0_0_2.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-01-14-f7ba9352c706-v0_0_2.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-01-23-c13c9dd0f3ae-v0_1_4a.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-01-23-c13c9dd0f3ae-v0_1_4a.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-01-24-e7151581f790-v0_1_4b.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-01-24-e7151581f790-v0_1_4b.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-01-30-2efe1dee9baf-v0_1_4c.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-01-30-2efe1dee9baf-v0_1_4c.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-06-95073282294e-v0_1_4e.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-06-95073282294e-v0_1_4e.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-06-9c02109e4faa-v0_2_0.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-06-9c02109e4faa-v0_2_0.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-06-f2cb77148a6e-v0_1_4d.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-06-f2cb77148a6e-v0_1_4d.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-15-641d1508baab-v0_4_0.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-15-641d1508baab-v0_4_0.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-16-1fdc05837919-v0_4_1.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-16-1fdc05837919-v0_4_1.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-02-21-a88f5298b8f7-v0_4_2.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-02-21-a88f5298b8f7-v0_4_2.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-03-09-0c4d4fe5f2c6-v0_6_1.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-03-09-0c4d4fe5f2c6-v0_6_1.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/schema/migrations/versions/2023-03-24-333fd693eac8-v0_6_1b.py` & `lnhub_rest-0.7rc1/lnhub_rest/schema/migrations/versions/2023-03-24-333fd693eac8-v0_6_1b.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/lnhub_rest/utils/_test.py` & `lnhub_rest-0.7rc1/lnhub_rest/utils/_test.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/noxfile.py` & `lnhub_rest-0.7rc1/noxfile.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/pyproject.toml` & `lnhub_rest-0.7rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/supabase/config.toml` & `lnhub_rest-0.7rc1/supabase/config.toml`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/tests/test_notebooks.py` & `lnhub_rest-0.7rc1/tests/test_notebooks.py`

 * *Files identical despite different names*

### Comparing `lnhub_rest-0.7.3/PKG-INFO` & `lnhub_rest-0.7rc1/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lnhub_rest
-Version: 0.7.3
+Version: 0.7rc1
 Summary: Rest API for the hub.
 Author-email: Lamin Labs <laminlabs@gmail.com>
 Description-Content-Type: text/markdown
 Requires-Dist: lamin_logger>=0.2.3
 Requires-Dist: supabase==1.0.2
 Requires-Dist: fastapi
 Requires-Dist: uvicorn
```

