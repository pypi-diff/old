# Comparing `tmp/lndb-0.40.1.tar.gz` & `tmp/lndb-0.40.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lndb-0.40.1.tar", last modified: Fri Apr  7 04:41:48 2023, max compression
+gzip compressed data, was "lndb-0.40.2.tar", last modified: Fri Apr  7 09:42:29 2023, max compression
```

## Comparing `lndb-0.40.1.tar` & `lndb-0.40.2.tar`

### file list

```diff
@@ -1,77 +1,77 @@
--rw-r--r--   0        0        0     3899 2023-04-05 12:41:02.524447 lndb-0.40.1/.github/workflows/build.yml
--rw-r--r--   0        0        0      133 2023-01-15 12:18:16.566196 lndb-0.40.1/.github/workflows/latest-changes.jinja2
--rw-r--r--   0        0        0      597 2023-01-15 12:18:16.566256 lndb-0.40.1/.github/workflows/latest-changes.yml
--rw-r--r--   0        0        0     1204 2023-01-15 12:18:16.566326 lndb-0.40.1/.gitignore
--rw-r--r--   0        0        0     1772 2023-01-16 03:13:03.815140 lndb-0.40.1/.pre-commit-config.yaml
--rw-r--r--   0        0        0    11324 2023-01-15 12:18:16.566501 lndb-0.40.1/LICENSE
--rw-r--r--   0        0        0      173 2023-03-27 04:37:15.707800 lndb-0.40.1/README.md
--rw-r--r--   0        0        0       52 2023-03-06 11:50:26.265030 lndb-0.40.1/docs/api.md
--rw-r--r--   0        0        0    45186 2023-04-07 04:41:11.024667 lndb-0.40.1/docs/changelog.md
--rw-r--r--   0        0        0     4832 2023-03-22 14:41:54.962234 lndb-0.40.1/docs/faq/check-synchronization.ipynb
--rw-r--r--   0        0        0     3334 2023-03-09 09:28:04.965028 lndb-0.40.1/docs/faq/clone.ipynb
--rw-r--r--   0        0        0     8397 2023-03-22 05:59:33.863010 lndb-0.40.1/docs/faq/edge-cases-login-init.ipynb
--rw-r--r--   0        0        0      166 2023-03-22 14:56:35.817208 lndb-0.40.1/docs/faq/index.md
--rw-r--r--   0        0        0     1180 2023-04-05 05:10:26.112382 lndb-0.40.1/docs/faq/manage-migrations.ipynb
--rw-r--r--   0        0        0     3248 2023-03-09 09:28:04.965998 lndb-0.40.1/docs/faq/switch-environment.ipynb
--rw-r--r--   0        0        0     2798 2023-04-05 05:10:26.112662 lndb-0.40.1/docs/faq/test-migrations-e2e.ipynb
--rw-r--r--   0        0        0     2073 2023-04-05 05:10:26.112933 lndb-0.40.1/docs/faq/test-migrations-unit.ipynb
--rw-r--r--   0        0        0     5163 2023-03-22 05:59:33.863390 lndb-0.40.1/docs/guide/01-setup-user.ipynb
--rw-r--r--   0        0        0    10400 2023-03-22 05:59:33.863723 lndb-0.40.1/docs/guide/02-init-instance.ipynb
--rw-r--r--   0        0        0     5573 2023-03-22 14:56:35.818426 lndb-0.40.1/docs/guide/03-load-instance.ipynb
--rw-r--r--   0        0        0     5290 2023-03-09 09:28:04.966850 lndb-0.40.1/docs/guide/04-set-storage.ipynb
--rw-r--r--   0        0        0     3724 2023-03-22 05:59:33.864269 lndb-0.40.1/docs/guide/05-schema-modules.ipynb
--rw-r--r--   0        0        0     1496 2023-03-22 05:59:33.864524 lndb-0.40.1/docs/guide/06-info.ipynb
--rw-r--r--   0        0        0     3282 2023-03-22 05:59:33.864793 lndb-0.40.1/docs/guide/07-delete.ipynb
--rw-r--r--   0        0        0      129 2023-02-16 15:52:14.590660 lndb-0.40.1/docs/guide/index.md
--rw-r--r--   0        0        0     3152 2023-03-25 20:23:06.444401 lndb-0.40.1/docs/guide/migrate.md
--rw-r--r--   0        0        0      126 2023-02-16 21:53:37.660107 lndb-0.40.1/docs/index.md
--rw-r--r--   0        0        0      118 2023-02-17 10:58:37.191812 lndb-0.40.1/lamin-project.yaml
--rw-r--r--   0        0        0     1932 2023-04-07 04:41:06.516334 lndb-0.40.1/lndb/__init__.py
--rw-r--r--   0        0        0     4242 2023-02-27 18:35:12.951712 lndb-0.40.1/lndb/__main__.py
--rw-r--r--   0        0        0      100 2023-02-12 04:51:38.272115 lndb-0.40.1/lndb/_assets/__init__.py
--rw-r--r--   0        0        0      216 2023-04-03 04:25:19.341088 lndb-0.40.1/lndb/_check_versions.py
--rw-r--r--   0        0        0      360 2023-02-16 21:53:37.660535 lndb-0.40.1/lndb/_close.py
--rw-r--r--   0        0        0     2146 2023-04-05 13:47:39.618861 lndb-0.40.1/lndb/_delete.py
--rw-r--r--   0        0        0      222 2023-02-16 21:53:37.660919 lndb-0.40.1/lndb/_info.py
--rw-r--r--   0        0        0     5755 2023-04-05 12:41:02.525310 lndb-0.40.1/lndb/_init_instance.py
--rw-r--r--   0        0        0     3752 2023-04-05 05:10:26.113362 lndb-0.40.1/lndb/_load_instance.py
--rw-r--r--   0        0        0      135 2023-04-05 05:10:26.113647 lndb-0.40.1/lndb/_migrate/__init__.py
--rw-r--r--   0        0        0      723 2023-04-05 05:10:26.113978 lndb-0.40.1/lndb/_migrate/alembic.ini
--rw-r--r--   0        0        0     3469 2023-04-05 12:41:02.533096 lndb-0.40.1/lndb/_migrate/core.py
--rw-r--r--   0        0        0     6303 2023-04-05 05:10:26.114561 lndb-0.40.1/lndb/_migrate/deploy.py
--rw-r--r--   0        0        0     3179 2023-02-16 21:53:37.661733 lndb-0.40.1/lndb/_migrate/env.py
--rw-r--r--   0        0        0      341 2023-02-16 21:53:37.661843 lndb-0.40.1/lndb/_migrate/script.py.mako
--rw-r--r--   0        0        0     4840 2023-04-05 05:10:26.114776 lndb-0.40.1/lndb/_migrate/utils.py
--rw-r--r--   0        0        0     1020 2023-02-12 04:51:38.274334 lndb-0.40.1/lndb/_schema.py
--rw-r--r--   0        0        0     1490 2023-04-05 12:41:02.525753 lndb-0.40.1/lndb/_set.py
--rw-r--r--   0        0        0     2165 2023-04-07 02:52:01.648931 lndb-0.40.1/lndb/_settings.py
--rw-r--r--   0        0        0       87 2023-02-16 21:53:37.662311 lndb-0.40.1/lndb/_settings_load.py
--rw-r--r--   0        0        0       72 2023-02-16 21:53:37.662460 lndb-0.40.1/lndb/_settings_store.py
--rw-r--r--   0        0        0     5291 2023-03-12 15:04:39.932675 lndb-0.40.1/lndb/_setup_user.py
--rw-r--r--   0        0        0      363 2023-04-05 12:41:02.526023 lndb-0.40.1/lndb/dev/__init__.py
--rw-r--r--   0        0        0     4030 2023-03-27 17:35:42.591834 lndb-0.40.1/lndb/dev/_clone.py
--rw-r--r--   0        0        0     6341 2023-04-05 12:41:02.526216 lndb-0.40.1/lndb/dev/_db.py
--rw-r--r--   0        0        0     2491 2023-02-16 21:53:37.663214 lndb-0.40.1/lndb/dev/_deprecated.py
--rw-r--r--   0        0        0      240 2023-02-16 21:53:37.663286 lndb-0.40.1/lndb/dev/_docs.py
--rw-r--r--   0        0        0     5284 2023-04-05 12:41:02.526831 lndb-0.40.1/lndb/dev/_exclusion.py
--rw-r--r--   0        0        0     8389 2023-04-05 12:41:02.527633 lndb-0.40.1/lndb/dev/_settings_instance.py
--rw-r--r--   0        0        0     2629 2023-03-22 05:59:33.865686 lndb-0.40.1/lndb/dev/_settings_load.py
--rw-r--r--   0        0        0     2061 2023-02-16 21:53:37.663723 lndb-0.40.1/lndb/dev/_settings_save.py
--rw-r--r--   0        0        0     2454 2023-04-07 04:13:56.734044 lndb-0.40.1/lndb/dev/_settings_store.py
--rw-r--r--   0        0        0      976 2023-02-16 21:53:37.663901 lndb-0.40.1/lndb/dev/_settings_user.py
--rw-r--r--   0        0        0     2446 2023-03-21 06:52:10.981980 lndb-0.40.1/lndb/dev/_setup_knowledge.py
--rw-r--r--   0        0        0     6996 2023-03-30 17:54:01.453792 lndb-0.40.1/lndb/dev/_setup_schema.py
--rw-r--r--   0        0        0     4004 2023-04-05 12:41:02.528400 lndb-0.40.1/lndb/dev/_storage.py
--rw-r--r--   0        0        0      140 2023-02-24 20:31:36.945684 lndb-0.40.1/lndb/dev/_testdb.py
--rw-r--r--   0        0        0      356 2023-04-05 05:10:26.115134 lndb-0.40.1/lndb/test/__init__.py
--rw-r--r--   0        0        0       50 2023-02-24 20:31:36.946187 lndb-0.40.1/lndb/test/_env.py
--rw-r--r--   0        0        0     3856 2023-03-30 17:54:01.454075 lndb-0.40.1/lndb/test/_migrations_e2e.py
--rw-r--r--   0        0        0     6646 2023-04-05 05:10:26.115464 lndb-0.40.1/lndb/test/_migrations_unit.py
--rw-r--r--   0        0        0      310 2023-02-24 20:31:36.946490 lndb-0.40.1/lndb/test/_nox.py
--rw-r--r--   0        0        0      188 2023-02-22 22:13:54.788863 lndb-0.40.1/lndb/test/nox.py
--rw-r--r--   0        0        0     1514 2023-03-09 09:28:04.969263 lndb-0.40.1/noxfile.py
--rw-r--r--   0        0        0     1305 2023-04-07 04:41:04.152199 lndb-0.40.1/pyproject.toml
--rw-r--r--   0        0        0      506 2023-02-12 04:51:38.276939 lndb-0.40.1/tests/test_bionty.py
--rw-r--r--   0        0        0      680 2023-03-09 09:28:04.969725 lndb-0.40.1/tests/test_init_instance.py
--rw-r--r--   0        0        0      385 2023-02-21 15:53:42.076396 lndb-0.40.1/tests/test_notebooks.py
--rw-r--r--   0        0        0     1190 1970-01-01 00:00:00.000000 lndb-0.40.1/PKG-INFO
+-rw-r--r--   0        0        0     3899 2023-04-05 12:41:02.524447 lndb-0.40.2/.github/workflows/build.yml
+-rw-r--r--   0        0        0      133 2023-01-15 12:18:16.566196 lndb-0.40.2/.github/workflows/latest-changes.jinja2
+-rw-r--r--   0        0        0      597 2023-01-15 12:18:16.566256 lndb-0.40.2/.github/workflows/latest-changes.yml
+-rw-r--r--   0        0        0     1204 2023-01-15 12:18:16.566326 lndb-0.40.2/.gitignore
+-rw-r--r--   0        0        0     1772 2023-01-16 03:13:03.815140 lndb-0.40.2/.pre-commit-config.yaml
+-rw-r--r--   0        0        0    11324 2023-01-15 12:18:16.566501 lndb-0.40.2/LICENSE
+-rw-r--r--   0        0        0      173 2023-03-27 04:37:15.707800 lndb-0.40.2/README.md
+-rw-r--r--   0        0        0       52 2023-03-06 11:50:26.265030 lndb-0.40.2/docs/api.md
+-rw-r--r--   0        0        0    45342 2023-04-07 09:41:52.757903 lndb-0.40.2/docs/changelog.md
+-rw-r--r--   0        0        0     4832 2023-03-22 14:41:54.962234 lndb-0.40.2/docs/faq/check-synchronization.ipynb
+-rw-r--r--   0        0        0     3334 2023-03-09 09:28:04.965028 lndb-0.40.2/docs/faq/clone.ipynb
+-rw-r--r--   0        0        0     8397 2023-03-22 05:59:33.863010 lndb-0.40.2/docs/faq/edge-cases-login-init.ipynb
+-rw-r--r--   0        0        0      166 2023-03-22 14:56:35.817208 lndb-0.40.2/docs/faq/index.md
+-rw-r--r--   0        0        0     1180 2023-04-05 05:10:26.112382 lndb-0.40.2/docs/faq/manage-migrations.ipynb
+-rw-r--r--   0        0        0     3248 2023-03-09 09:28:04.965998 lndb-0.40.2/docs/faq/switch-environment.ipynb
+-rw-r--r--   0        0        0     2798 2023-04-05 05:10:26.112662 lndb-0.40.2/docs/faq/test-migrations-e2e.ipynb
+-rw-r--r--   0        0        0     2073 2023-04-05 05:10:26.112933 lndb-0.40.2/docs/faq/test-migrations-unit.ipynb
+-rw-r--r--   0        0        0     5163 2023-03-22 05:59:33.863390 lndb-0.40.2/docs/guide/01-setup-user.ipynb
+-rw-r--r--   0        0        0    10679 2023-04-07 09:41:26.324653 lndb-0.40.2/docs/guide/02-init-instance.ipynb
+-rw-r--r--   0        0        0     5573 2023-03-22 14:56:35.818426 lndb-0.40.2/docs/guide/03-load-instance.ipynb
+-rw-r--r--   0        0        0     5290 2023-03-09 09:28:04.966850 lndb-0.40.2/docs/guide/04-set-storage.ipynb
+-rw-r--r--   0        0        0     3724 2023-03-22 05:59:33.864269 lndb-0.40.2/docs/guide/05-schema-modules.ipynb
+-rw-r--r--   0        0        0     1496 2023-03-22 05:59:33.864524 lndb-0.40.2/docs/guide/06-info.ipynb
+-rw-r--r--   0        0        0     3282 2023-03-22 05:59:33.864793 lndb-0.40.2/docs/guide/07-delete.ipynb
+-rw-r--r--   0        0        0      129 2023-02-16 15:52:14.590660 lndb-0.40.2/docs/guide/index.md
+-rw-r--r--   0        0        0     3152 2023-03-25 20:23:06.444401 lndb-0.40.2/docs/guide/migrate.md
+-rw-r--r--   0        0        0      126 2023-02-16 21:53:37.660107 lndb-0.40.2/docs/index.md
+-rw-r--r--   0        0        0      118 2023-02-17 10:58:37.191812 lndb-0.40.2/lamin-project.yaml
+-rw-r--r--   0        0        0     1932 2023-04-07 09:41:45.725396 lndb-0.40.2/lndb/__init__.py
+-rw-r--r--   0        0        0     4242 2023-02-27 18:35:12.951712 lndb-0.40.2/lndb/__main__.py
+-rw-r--r--   0        0        0      100 2023-02-12 04:51:38.272115 lndb-0.40.2/lndb/_assets/__init__.py
+-rw-r--r--   0        0        0      216 2023-04-03 04:25:19.341088 lndb-0.40.2/lndb/_check_versions.py
+-rw-r--r--   0        0        0      360 2023-02-16 21:53:37.660535 lndb-0.40.2/lndb/_close.py
+-rw-r--r--   0        0        0     2146 2023-04-05 13:47:39.618861 lndb-0.40.2/lndb/_delete.py
+-rw-r--r--   0        0        0      222 2023-02-16 21:53:37.660919 lndb-0.40.2/lndb/_info.py
+-rw-r--r--   0        0        0     5724 2023-04-07 09:41:26.324840 lndb-0.40.2/lndb/_init_instance.py
+-rw-r--r--   0        0        0     3752 2023-04-05 05:10:26.113362 lndb-0.40.2/lndb/_load_instance.py
+-rw-r--r--   0        0        0      135 2023-04-05 05:10:26.113647 lndb-0.40.2/lndb/_migrate/__init__.py
+-rw-r--r--   0        0        0      723 2023-04-05 05:10:26.113978 lndb-0.40.2/lndb/_migrate/alembic.ini
+-rw-r--r--   0        0        0     3469 2023-04-05 12:41:02.533096 lndb-0.40.2/lndb/_migrate/core.py
+-rw-r--r--   0        0        0     6303 2023-04-05 05:10:26.114561 lndb-0.40.2/lndb/_migrate/deploy.py
+-rw-r--r--   0        0        0     3179 2023-02-16 21:53:37.661733 lndb-0.40.2/lndb/_migrate/env.py
+-rw-r--r--   0        0        0      341 2023-02-16 21:53:37.661843 lndb-0.40.2/lndb/_migrate/script.py.mako
+-rw-r--r--   0        0        0     4840 2023-04-05 05:10:26.114776 lndb-0.40.2/lndb/_migrate/utils.py
+-rw-r--r--   0        0        0     1020 2023-02-12 04:51:38.274334 lndb-0.40.2/lndb/_schema.py
+-rw-r--r--   0        0        0     1490 2023-04-05 12:41:02.525753 lndb-0.40.2/lndb/_set.py
+-rw-r--r--   0        0        0     2181 2023-04-07 09:41:26.325000 lndb-0.40.2/lndb/_settings.py
+-rw-r--r--   0        0        0       87 2023-02-16 21:53:37.662311 lndb-0.40.2/lndb/_settings_load.py
+-rw-r--r--   0        0        0       72 2023-02-16 21:53:37.662460 lndb-0.40.2/lndb/_settings_store.py
+-rw-r--r--   0        0        0     5291 2023-03-12 15:04:39.932675 lndb-0.40.2/lndb/_setup_user.py
+-rw-r--r--   0        0        0      437 2023-04-07 09:41:26.325162 lndb-0.40.2/lndb/dev/__init__.py
+-rw-r--r--   0        0        0     4030 2023-03-27 17:35:42.591834 lndb-0.40.2/lndb/dev/_clone.py
+-rw-r--r--   0        0        0     6226 2023-04-07 09:41:26.325330 lndb-0.40.2/lndb/dev/_db.py
+-rw-r--r--   0        0        0     2491 2023-02-16 21:53:37.663214 lndb-0.40.2/lndb/dev/_deprecated.py
+-rw-r--r--   0        0        0      240 2023-02-16 21:53:37.663286 lndb-0.40.2/lndb/dev/_docs.py
+-rw-r--r--   0        0        0     5284 2023-04-05 12:41:02.526831 lndb-0.40.2/lndb/dev/_exclusion.py
+-rw-r--r--   0        0        0     8435 2023-04-07 09:41:26.325515 lndb-0.40.2/lndb/dev/_settings_instance.py
+-rw-r--r--   0        0        0     2629 2023-03-22 05:59:33.865686 lndb-0.40.2/lndb/dev/_settings_load.py
+-rw-r--r--   0        0        0     2061 2023-02-16 21:53:37.663723 lndb-0.40.2/lndb/dev/_settings_save.py
+-rw-r--r--   0        0        0     2314 2023-04-07 05:02:28.778847 lndb-0.40.2/lndb/dev/_settings_store.py
+-rw-r--r--   0        0        0      976 2023-02-16 21:53:37.663901 lndb-0.40.2/lndb/dev/_settings_user.py
+-rw-r--r--   0        0        0     2446 2023-03-21 06:52:10.981980 lndb-0.40.2/lndb/dev/_setup_knowledge.py
+-rw-r--r--   0        0        0     6996 2023-03-30 17:54:01.453792 lndb-0.40.2/lndb/dev/_setup_schema.py
+-rw-r--r--   0        0        0     4922 2023-04-07 09:41:26.325689 lndb-0.40.2/lndb/dev/_storage.py
+-rw-r--r--   0        0        0      140 2023-02-24 20:31:36.945684 lndb-0.40.2/lndb/dev/_testdb.py
+-rw-r--r--   0        0        0      356 2023-04-05 05:10:26.115134 lndb-0.40.2/lndb/test/__init__.py
+-rw-r--r--   0        0        0       50 2023-02-24 20:31:36.946187 lndb-0.40.2/lndb/test/_env.py
+-rw-r--r--   0        0        0     3856 2023-03-30 17:54:01.454075 lndb-0.40.2/lndb/test/_migrations_e2e.py
+-rw-r--r--   0        0        0     6646 2023-04-05 05:10:26.115464 lndb-0.40.2/lndb/test/_migrations_unit.py
+-rw-r--r--   0        0        0      310 2023-02-24 20:31:36.946490 lndb-0.40.2/lndb/test/_nox.py
+-rw-r--r--   0        0        0      188 2023-02-22 22:13:54.788863 lndb-0.40.2/lndb/test/nox.py
+-rw-r--r--   0        0        0     1514 2023-03-09 09:28:04.969263 lndb-0.40.2/noxfile.py
+-rw-r--r--   0        0        0     1305 2023-04-07 04:41:04.152199 lndb-0.40.2/pyproject.toml
+-rw-r--r--   0        0        0      506 2023-02-12 04:51:38.276939 lndb-0.40.2/tests/test_bionty.py
+-rw-r--r--   0        0        0      680 2023-03-09 09:28:04.969725 lndb-0.40.2/tests/test_init_instance.py
+-rw-r--r--   0        0        0      385 2023-02-21 15:53:42.076396 lndb-0.40.2/tests/test_notebooks.py
+-rw-r--r--   0        0        0     1190 1970-01-01 00:00:00.000000 lndb-0.40.2/PKG-INFO
```

### Comparing `lndb-0.40.1/.github/workflows/build.yml` & `lndb-0.40.2/.github/workflows/build.yml`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/.github/workflows/latest-changes.yml` & `lndb-0.40.2/.github/workflows/latest-changes.yml`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/.gitignore` & `lndb-0.40.2/.gitignore`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/.pre-commit-config.yaml` & `lndb-0.40.2/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/LICENSE` & `lndb-0.40.2/LICENSE`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/changelog.md` & `lndb-0.40.2/docs/changelog.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 # Changelog
 
 <!-- prettier-ignore -->
 Name | PR | Developer | Date | Version
 --- | --- | --- | --- | ---
+🚸 Expose `id` in `StorageSettings` | [351](https://github.com/laminlabs/lndb/pull/351) | [falexwolf](https://github.com/falexwolf) | 2023-04-07 | 0.40.2
 ➕ Add cloudpathlib back | [350](https://github.com/laminlabs/lndb/pull/350) | [falexwolf](https://github.com/falexwolf) | 2023-04-07 | 0.40.1
 🚸 Rename settings directory to `.lamin` | [349](https://github.com/laminlabs/lndb/pull/349) | [falexwolf](https://github.com/falexwolf) | 2023-04-07 | 0.40.0
 🚸 Expose storage in settings | [348](https://github.com/laminlabs/lndb/pull/348) | [falexwolf](https://github.com/falexwolf) | 2023-04-07 |
 ♻️ Move storage related code to lndb_storage | [338](https://github.com/laminlabs/lndb/pull/338) | [Koncopd](https://github.com/Koncopd) | 2023-04-05 |
 ♻️ Refactor migrations | [346](https://github.com/laminlabs/lndb/pull/346) | [falexwolf](https://github.com/falexwolf) | 2023-04-04 |
 🧑‍💻 Enable to load instance from hub using access token | [343](https://github.com/laminlabs/lndb/pull/343) | [fredericenard](https://github.com/fredericenard) | 2023-04-03 | 0.39.2
 ⬆️ Upgrade lnhub-rest to 0.7.2 | [341](https://github.com/laminlabs/lndb/pull/341) | [falexwolf](https://github.com/falexwolf) | 2023-03-31 | 0.39.1
```

### Comparing `lndb-0.40.1/docs/faq/check-synchronization.ipynb` & `lndb-0.40.2/docs/faq/check-synchronization.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/faq/clone.ipynb` & `lndb-0.40.2/docs/faq/clone.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/faq/edge-cases-login-init.ipynb` & `lndb-0.40.2/docs/faq/edge-cases-login-init.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/faq/manage-migrations.ipynb` & `lndb-0.40.2/docs/faq/manage-migrations.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/faq/switch-environment.ipynb` & `lndb-0.40.2/docs/faq/switch-environment.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/faq/test-migrations-e2e.ipynb` & `lndb-0.40.2/docs/faq/test-migrations-e2e.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/faq/test-migrations-unit.ipynb` & `lndb-0.40.2/docs/faq/test-migrations-unit.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/guide/01-setup-user.ipynb` & `lndb-0.40.2/docs/guide/01-setup-user.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/guide/02-init-instance.ipynb` & `lndb-0.40.2/docs/guide/02-init-instance.ipynb`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9946808510638299%*

 * *Differences: {"'cells'": "{insert: [(45, OrderedDict([('cell_type', 'markdown'), ('metadata', OrderedDict()), "*

 * *            "('source', ['For now, only assert the type.'])])), (46, OrderedDict([('cell_type', "*

 * *            "'code'), ('execution_count', None), ('metadata', OrderedDict()), ('outputs', []), "*

 * *            "('source', ['assert type(ln.setup.settings.storage.id)'])]))]}"}*

```diff
@@ -450,14 +450,30 @@
             "cell_type": "code",
             "execution_count": null,
             "metadata": {},
             "outputs": [],
             "source": [
                 "assert ln.setup.init(storage=\"mydata\") == \"migrate-unnecessary\""
             ]
+        },
+        {
+            "cell_type": "markdown",
+            "metadata": {},
+            "source": [
+                "For now, only assert the type."
+            ]
+        },
+        {
+            "cell_type": "code",
+            "execution_count": null,
+            "metadata": {},
+            "outputs": [],
+            "source": [
+                "assert type(ln.setup.settings.storage.id)"
+            ]
         }
     ],
     "metadata": {
         "kernelspec": {
             "display_name": "Python 3 (ipykernel)",
             "language": "python",
             "name": "python3"
```

### Comparing `lndb-0.40.1/docs/guide/03-load-instance.ipynb` & `lndb-0.40.2/docs/guide/03-load-instance.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/guide/04-set-storage.ipynb` & `lndb-0.40.2/docs/guide/04-set-storage.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/guide/05-schema-modules.ipynb` & `lndb-0.40.2/docs/guide/05-schema-modules.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/guide/06-info.ipynb` & `lndb-0.40.2/docs/guide/06-info.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/guide/07-delete.ipynb` & `lndb-0.40.2/docs/guide/07-delete.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/docs/guide/migrate.md` & `lndb-0.40.2/docs/guide/migrate.md`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/__init__.py` & `lndb-0.40.2/lndb/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -46,15 +46,15 @@
 
 .. autosummary::
    :toctree:
 
    dev
 """
 
-__version__ = "0.40.1"  # denote a release candidate for 0.1.0 with 0.1rc1
+__version__ = "0.40.2"  # denote a release candidate for 0.1.0 with 0.1rc1
 
 import sys
 from os import name as _os_name
 
 from . import _check_versions  # noqa
 from . import dev, test
 from ._close import close  # noqa
```

### Comparing `lndb-0.40.1/lndb/__main__.py` & `lndb-0.40.2/lndb/__main__.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/_delete.py` & `lndb-0.40.2/lndb/_delete.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/_init_instance.py` & `lndb-0.40.2/lndb/_init_instance.py`

 * *Files 2% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 from .dev._setup_schema import load_schema, setup_schema
 from .dev._storage import Storage
 
 
 def register(isettings: InstanceSettings, usettings):
     """Register user & storage in DB."""
     upsert.user(usettings.email, usettings.id, usettings.handle, usettings.name)
-    insert_if_not_exists.storage(isettings.storage.root, isettings.storage.region)
+    insert_if_not_exists.storage(isettings.storage)
 
 
 def import_schema_lamin_root_api():
     # only touch lamindb if we're operating from lamindb
     if "lamindb" in sys.modules:
         import lamindb
```

### Comparing `lndb-0.40.1/lndb/_load_instance.py` & `lndb-0.40.2/lndb/_load_instance.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/_migrate/alembic.ini` & `lndb-0.40.2/lndb/_migrate/alembic.ini`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/_migrate/core.py` & `lndb-0.40.2/lndb/_migrate/core.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/_migrate/deploy.py` & `lndb-0.40.2/lndb/_migrate/deploy.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/_migrate/env.py` & `lndb-0.40.2/lndb/_migrate/env.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/_migrate/utils.py` & `lndb-0.40.2/lndb/_migrate/utils.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/_schema.py` & `lndb-0.40.2/lndb/_schema.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/_set.py` & `lndb-0.40.2/lndb/_set.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/_settings.py` & `lndb-0.40.2/lndb/_settings.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import os
 from typing import Union
 
-from lndb.dev import InstanceSettings, Storage, UserSettings
+from lndb.dev import InstanceSettings, StorageSettings, UserSettings
 from lndb.dev._settings_load import load_instance_settings, load_or_create_user_settings
 
 
 # https://stackoverflow.com/questions/128573/using-property-on-classmethods/64738850#64738850
 class classproperty(object):
     def __init__(self, fget):
         self.fget = fget
@@ -50,15 +50,15 @@
             or cls._instance_settings_env != get_env_name()  # noqa
         ):
             cls._instance_settings = load_instance_settings()
             cls._instance_settings_env = get_env_name()
         return cls._instance_settings  # type: ignore
 
     @classproperty
-    def storage(cls) -> Storage:
+    def storage(cls) -> StorageSettings:
         """Storage."""
         return cls.instance.storage
 
     @classproperty
     def _instance_exists(cls):
         try:
             cls.instance
```

### Comparing `lndb-0.40.1/lndb/_setup_user.py` & `lndb-0.40.2/lndb/_setup_user.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/dev/_clone.py` & `lndb-0.40.2/lndb/dev/_clone.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/dev/_db.py` & `lndb-0.40.2/lndb/dev/_db.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,19 +1,18 @@
 # We see a lot of import statements for lnschema_core below
 # This is currently needed as we can only import the schema module
 # once isettings have been adjusted
-from pathlib import Path
-from typing import Any, List, Optional, Union
+from typing import Any, List
 
 import sqlmodel as sqm
 from lamin_logger import logger
-from lndb_storage import UPath
 from sqlalchemy.exc import ProgrammingError
 
 from .._settings import settings
+from ._storage import StorageSettings
 
 
 class upsert:
     @classmethod
     def user(cls, email: str, user_id: str, handle: str, name: str = None):
         import lnschema_core as schema_core
 
@@ -65,28 +64,24 @@
 class insert_if_not_exists:
     """Insert data if it does not yet exist.
 
     A wrapper around the `insert` class below.
     """
 
     @classmethod
-    def storage(cls, root: Union[Path, UPath], region: Optional[str]):
-        from lnschema_core import Storage
+    def storage(cls, storage_settings: StorageSettings):
+        from lnschema_core import Storage as StorageORM
 
-        if isinstance(root, UPath):
-            root_str = root.as_posix().rstrip("/")
-        else:
-            root_str = root.resolve().as_posix()
+        root_str = storage_settings.root_as_str
         with sqm.Session(settings.instance.engine) as session:
             storage = session.exec(
-                sqm.select(Storage).where(Storage.root == root_str)
+                sqm.select(StorageORM).where(StorageORM.root == root_str)
             ).first()
         if storage is None:
-            storage = insert.storage(root_str, region)
-
+            storage = insert.storage(root_str, storage_settings.region)
         return storage
 
 
 class insert:
     """Insert data."""
 
     # this here actually first checks for existence
```

### Comparing `lndb-0.40.1/lndb/dev/_deprecated.py` & `lndb-0.40.2/lndb/dev/_deprecated.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/dev/_exclusion.py` & `lndb-0.40.2/lndb/dev/_exclusion.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/dev/_settings_instance.py` & `lndb-0.40.2/lndb/dev/_settings_instance.py`

 * *Files 0% similar despite different names*

```diff
@@ -39,15 +39,17 @@
         storage_root: Union[str, Path, UPath],  # storage location on cloud
         storage_region: Optional[str] = None,
         db: Optional[PostgresDsn] = None,  # DB URI
         schema: Optional[str] = None,  # comma-separated string of schema names
     ):
         self._owner: str = owner
         self._name: str = name
-        self._storage: Storage = Storage(storage_root, region=storage_region)
+        self._storage: Storage = Storage(
+            storage_root, instance_settings=self, region=storage_region
+        )
         self._db: Optional[str] = db
         self._schema_str: Optional[str] = schema
         self._engine: Engine = sqm.create_engine(self.db)
 
     def __repr__(self):
         """Rich string representation."""
         representation = f"Current instance: {self.identifier}"
```

### Comparing `lndb-0.40.1/lndb/dev/_settings_load.py` & `lndb-0.40.2/lndb/dev/_settings_load.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/dev/_settings_save.py` & `lndb-0.40.2/lndb/dev/_settings_save.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/dev/_settings_store.py` & `lndb-0.40.2/lndb/dev/_settings_store.py`

 * *Files 4% similar despite different names*

```diff
@@ -3,18 +3,15 @@
 from pathlib import Path
 
 from lamin_logger import logger
 from pydantic import BaseSettings
 
 
 def get_settings_dir():
-    if "LAMIN_BASE_SETTINGS_DIR" in os.environ:
-        settings_dir = Path(os.environ["LAMIN_BASE_SETTINGS_DIR"]) / ".lamin"
-    else:
-        settings_dir = Path.home() / ".lamin"
+    settings_dir = Path.home() / ".lamin"
     settings_dir.mkdir(parents=True, exist_ok=True)
     # deal with legacy settings directory
     legacy_dir = settings_dir.with_name(".lndb")
     if legacy_dir.exists():
         if not settings_dir.exists():
             legacy_dir.rename(settings_dir)
             logger.info(f"Renamed legacy settings dir {legacy_dir} to {settings_dir}")
```

### Comparing `lndb-0.40.1/lndb/dev/_settings_user.py` & `lndb-0.40.2/lndb/dev/_settings_user.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/dev/_setup_knowledge.py` & `lndb-0.40.2/lndb/dev/_setup_knowledge.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/dev/_setup_schema.py` & `lndb-0.40.2/lndb/dev/_setup_schema.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/dev/_storage.py` & `lndb-0.40.2/lndb/dev/_storage.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,58 +1,82 @@
 import os
 from pathlib import Path
 from typing import Literal, Optional, Union
 
+import sqlmodel as sqm
 from appdirs import AppDirs
 from lndb_storage import UPath
 
 DIRS = AppDirs("lamindb", "laminlabs")
 
 
-class Storage:
-    """Manage cloud or local storage."""
+class StorageSettings:
+    """Manage cloud or local storage settings."""
 
-    def __init__(self, root: Union[str, Path, UPath], region: Optional[str] = None):
+    # we can't type instance_settings if we keep it in this separate file
+    def __init__(
+        self,
+        root: Union[str, Path, UPath],
+        instance_settings,
+        region: Optional[str] = None,
+    ):
         if isinstance(root, UPath):
             root_path = root
         elif isinstance(root, Path):
             root.mkdir(parents=True, exist_ok=True)  # resolve fails for nonexisting dir
             root_path = root.resolve()
         elif isinstance(root, str):
             root_path = Storage._str_to_path(root)
         else:
             raise ValueError("root should be of type Union[str, Path, UPath].")
         self._root = root_path
         self._region = region
+        self._id: Optional[str] = None
+        self._instance_settings = instance_settings
 
     @staticmethod
     def _str_to_path(storage: str) -> Union[Path, UPath]:
         if storage.startswith("s3://"):
             # for new buckets there could be problems if the region is not specified
             storage_root = UPath(storage, cache_regions=True)
         elif storage.startswith("gs://"):
             storage_root = UPath(storage)
         else:  # local path
             os.makedirs(storage, exist_ok=True)  # resolve fails for nonexisting dir
             storage_root = Path(storage).resolve()
         return storage_root
 
     @property
+    def id(self) -> str:
+        """Storage id."""
+        if self._id is None:
+            from lnschema_core import Storage
+
+            with sqm.Session(self._instance_settings.engine) as session:
+                # needs to have been registered before!
+                storage = session.exec(
+                    sqm.select(Storage).where(Storage.root == self.root_as_str)
+                ).one_or_none()
+            if storage is None:
+                raise RuntimeError(
+                    f"{self.root_as_str} wasn't registered in the db! "
+                    "Check ln.select(ln.Storage).all()"
+                )
+            self._id = storage.id
+        return self._id
+
+    @property
     def root(self) -> Union[Path, UPath]:
         """Root storage location."""
         return self._root
 
     @property
     def root_as_str(self) -> str:
         """Formatted root string."""
-        root_str = self.root.as_posix()
-        if root_str[-1] == "/":
-            return root_str[:-1]
-        else:
-            return root_str
+        return self.root.as_posix().rstrip("/")
 
     @property
     def cache_dir(
         self,
     ) -> Union[Path, None]:
         """Cache root, a local directory to cache cloud files."""
         if self.is_cloud:
@@ -107,7 +131,11 @@
         if self.is_cloud:
             return self.cache_dir.joinpath(filepath._url.netloc, *filepath.parts[1:])  # type: ignore # noqa
         return filepath
 
     def local_filepath(self, filekey: Union[Path, UPath, str]) -> Path:
         """Local (cache) filepath from filekey: `local(filepath(...))`."""
         return self.cloud_to_local(self.key_to_filepath(filekey))
+
+
+# below is for backward compat
+Storage = StorageSettings
```

### Comparing `lndb-0.40.1/lndb/test/_migrations_e2e.py` & `lndb-0.40.2/lndb/test/_migrations_e2e.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/lndb/test/_migrations_unit.py` & `lndb-0.40.2/lndb/test/_migrations_unit.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/noxfile.py` & `lndb-0.40.2/noxfile.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/pyproject.toml` & `lndb-0.40.2/pyproject.toml`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/tests/test_init_instance.py` & `lndb-0.40.2/tests/test_init_instance.py`

 * *Files identical despite different names*

### Comparing `lndb-0.40.1/PKG-INFO` & `lndb-0.40.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lndb
-Version: 0.40.1
+Version: 0.40.2
 Summary: LaminDB setup.
 Author-email: Lamin Labs <laminlabs@gmail.com>
 Description-Content-Type: text/markdown
 Requires-Dist: lnhub_rest==0.7.2
 Requires-Dist: lndb_storage==0.2rc2
 Requires-Dist: laminci>=0.3.0
 Requires-Dist: lnschema_core>=0.28.0
```

