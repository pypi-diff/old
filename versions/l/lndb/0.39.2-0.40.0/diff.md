# Comparing `tmp/lndb-0.39.2.tar.gz` & `tmp/lndb-0.40.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lndb-0.39.2.tar", last modified: Mon Apr  3 11:01:52 2023, max compression
+gzip compressed data, was "lndb-0.40.0.tar", last modified: Fri Apr  7 04:15:09 2023, max compression
```

## Comparing `lndb-0.39.2.tar` & `lndb-0.40.0.tar`

### file list

```diff
@@ -1,77 +1,77 @@
--rw-r--r--   0        0        0     3899 2023-03-31 06:18:24.411522 lndb-0.39.2/.github/workflows/build.yml
--rw-r--r--   0        0        0      133 2023-02-17 13:49:16.959104 lndb-0.39.2/.github/workflows/latest-changes.jinja2
--rw-r--r--   0        0        0      597 2023-02-17 13:49:16.959170 lndb-0.39.2/.github/workflows/latest-changes.yml
--rw-r--r--   0        0        0     1204 2023-02-17 13:49:16.959268 lndb-0.39.2/.gitignore
--rw-r--r--   0        0        0     1772 2023-02-17 13:49:16.959356 lndb-0.39.2/.pre-commit-config.yaml
--rw-r--r--   0        0        0    11324 2023-02-17 13:49:16.959462 lndb-0.39.2/LICENSE
--rw-r--r--   0        0        0      173 2023-03-31 06:18:24.412474 lndb-0.39.2/README.md
--rw-r--r--   0        0        0       52 2023-03-06 07:28:24.074432 lndb-0.39.2/docs/api.md
--rw-r--r--   0        0        0    44453 2023-04-03 11:01:27.991038 lndb-0.39.2/docs/changelog.md
--rw-r--r--   0        0        0     4832 2023-03-31 06:18:24.413743 lndb-0.39.2/docs/faq/check-synchronization.ipynb
--rw-r--r--   0        0        0     3334 2023-03-31 06:18:24.414194 lndb-0.39.2/docs/faq/clone.ipynb
--rw-r--r--   0        0        0     8397 2023-03-31 06:18:24.415119 lndb-0.39.2/docs/faq/edge-cases-login-init.ipynb
--rw-r--r--   0        0        0      166 2023-03-31 06:18:24.415959 lndb-0.39.2/docs/faq/index.md
--rw-r--r--   0        0        0     1464 2023-03-31 06:18:24.416798 lndb-0.39.2/docs/faq/manage-migrations.ipynb
--rw-r--r--   0        0        0     3248 2023-03-31 06:18:24.417221 lndb-0.39.2/docs/faq/switch-environment.ipynb
--rw-r--r--   0        0        0     2843 2023-03-31 06:18:24.417695 lndb-0.39.2/docs/faq/test-migrations-e2e.ipynb
--rw-r--r--   0        0        0     3806 2023-03-31 06:18:24.418155 lndb-0.39.2/docs/faq/test-migrations-unit.ipynb
--rw-r--r--   0        0        0     5163 2023-03-31 06:18:24.418653 lndb-0.39.2/docs/guide/01-setup-user.ipynb
--rw-r--r--   0        0        0    10400 2023-03-31 06:18:24.419025 lndb-0.39.2/docs/guide/02-init-instance.ipynb
--rw-r--r--   0        0        0     5573 2023-03-31 06:18:24.419573 lndb-0.39.2/docs/guide/03-load-instance.ipynb
--rw-r--r--   0        0        0     5290 2023-03-31 06:18:24.420036 lndb-0.39.2/docs/guide/04-set-storage.ipynb
--rw-r--r--   0        0        0     3724 2023-03-31 06:18:24.420381 lndb-0.39.2/docs/guide/05-schema-modules.ipynb
--rw-r--r--   0        0        0     1496 2023-03-31 06:18:24.420751 lndb-0.39.2/docs/guide/06-info.ipynb
--rw-r--r--   0        0        0     3282 2023-03-31 06:18:24.421507 lndb-0.39.2/docs/guide/07-delete.ipynb
--rw-r--r--   0        0        0      129 2023-02-17 19:35:05.599031 lndb-0.39.2/docs/guide/index.md
--rw-r--r--   0        0        0     3152 2023-03-31 06:18:24.421916 lndb-0.39.2/docs/guide/migrate.md
--rw-r--r--   0        0        0      126 2023-02-17 19:35:05.599275 lndb-0.39.2/docs/index.md
--rw-r--r--   0        0        0      118 2023-02-17 19:35:05.599424 lndb-0.39.2/lamin-project.yaml
--rw-r--r--   0        0        0     1926 2023-04-03 11:01:08.241399 lndb-0.39.2/lndb/__init__.py
--rw-r--r--   0        0        0     4242 2023-02-24 23:35:29.913848 lndb-0.39.2/lndb/__main__.py
--rw-r--r--   0        0        0      100 2023-02-17 13:49:16.961660 lndb-0.39.2/lndb/_assets/__init__.py
--rw-r--r--   0        0        0      216 2023-04-01 08:36:57.992002 lndb-0.39.2/lndb/_check_versions.py
--rw-r--r--   0        0        0      360 2023-02-17 19:35:05.600174 lndb-0.39.2/lndb/_close.py
--rw-r--r--   0        0        0     2062 2023-03-31 06:18:24.423693 lndb-0.39.2/lndb/_delete.py
--rw-r--r--   0        0        0      222 2023-02-17 19:35:05.600535 lndb-0.39.2/lndb/_info.py
--rw-r--r--   0        0        0     5731 2023-03-31 06:18:24.424157 lndb-0.39.2/lndb/_init_instance.py
--rw-r--r--   0        0        0     3752 2023-04-03 11:01:24.936585 lndb-0.39.2/lndb/_load_instance.py
--rw-r--r--   0        0        0     3525 2023-03-31 06:18:24.425302 lndb-0.39.2/lndb/_migrate/__init__.py
--rw-r--r--   0        0        0     6279 2023-03-31 06:18:24.425766 lndb-0.39.2/lndb/_migrate/_deploy.py
--rw-r--r--   0        0        0     5099 2023-03-31 06:18:24.426237 lndb-0.39.2/lndb/_migrate/_utils.py
--rw-r--r--   0        0        0      724 2023-02-17 19:35:05.601448 lndb-0.39.2/lndb/_migrate/alembic.ini
--rw-r--r--   0        0        0     3179 2023-02-17 19:35:05.601566 lndb-0.39.2/lndb/_migrate/env.py
--rw-r--r--   0        0        0      341 2023-02-17 19:35:05.601662 lndb-0.39.2/lndb/_migrate/script.py.mako
--rw-r--r--   0        0        0     1020 2023-02-17 13:49:16.963182 lndb-0.39.2/lndb/_schema.py
--rw-r--r--   0        0        0     1466 2023-02-24 18:23:12.622270 lndb-0.39.2/lndb/_set.py
--rw-r--r--   0        0        0     2087 2023-03-31 06:18:24.426717 lndb-0.39.2/lndb/_settings.py
--rw-r--r--   0        0        0       87 2023-02-17 19:35:05.602225 lndb-0.39.2/lndb/_settings_load.py
--rw-r--r--   0        0        0       72 2023-02-17 19:35:05.602342 lndb-0.39.2/lndb/_settings_store.py
--rw-r--r--   0        0        0     5291 2023-03-31 06:18:24.427489 lndb-0.39.2/lndb/_setup_user.py
--rw-r--r--   0        0        0      393 2023-02-20 08:48:26.781270 lndb-0.39.2/lndb/dev/__init__.py
--rw-r--r--   0        0        0     4030 2023-03-31 06:18:24.427954 lndb-0.39.2/lndb/dev/_clone.py
--rw-r--r--   0        0        0     6338 2023-03-31 06:18:24.428617 lndb-0.39.2/lndb/dev/_db.py
--rw-r--r--   0        0        0     2491 2023-02-17 19:35:05.603115 lndb-0.39.2/lndb/dev/_deprecated.py
--rw-r--r--   0        0        0      240 2023-02-17 19:35:05.603192 lndb-0.39.2/lndb/dev/_docs.py
--rw-r--r--   0        0        0     5562 2023-02-22 12:24:15.566492 lndb-0.39.2/lndb/dev/_exclusion.py
--rw-r--r--   0        0        0     8388 2023-02-20 08:48:26.781737 lndb-0.39.2/lndb/dev/_settings_instance.py
--rw-r--r--   0        0        0     2629 2023-03-31 06:18:24.428886 lndb-0.39.2/lndb/dev/_settings_load.py
--rw-r--r--   0        0        0     2061 2023-02-17 19:35:05.603816 lndb-0.39.2/lndb/dev/_settings_save.py
--rw-r--r--   0        0        0     1927 2023-03-31 06:18:24.429392 lndb-0.39.2/lndb/dev/_settings_store.py
--rw-r--r--   0        0        0      976 2023-02-17 19:35:05.604025 lndb-0.39.2/lndb/dev/_settings_user.py
--rw-r--r--   0        0        0     2446 2023-03-31 06:18:24.430632 lndb-0.39.2/lndb/dev/_setup_knowledge.py
--rw-r--r--   0        0        0     6996 2023-03-31 06:18:24.431076 lndb-0.39.2/lndb/dev/_setup_schema.py
--rw-r--r--   0        0        0     4004 2023-03-05 14:46:44.306277 lndb-0.39.2/lndb/dev/_storage.py
--rw-r--r--   0        0        0      140 2023-02-23 22:37:08.720821 lndb-0.39.2/lndb/dev/_testdb.py
--rw-r--r--   0        0        0     2001 2023-02-20 08:48:26.782279 lndb-0.39.2/lndb/dev/_upath_ext.py
--rw-r--r--   0        0        0      388 2023-03-31 06:18:24.431483 lndb-0.39.2/lndb/test/__init__.py
--rw-r--r--   0        0        0       50 2023-02-23 22:37:08.722119 lndb-0.39.2/lndb/test/_env.py
--rw-r--r--   0        0        0     3856 2023-03-31 06:18:24.431826 lndb-0.39.2/lndb/test/_migrations_e2e.py
--rw-r--r--   0        0        0     6229 2023-02-17 13:49:16.964351 lndb-0.39.2/lndb/test/_migrations_unit.py
--rw-r--r--   0        0        0      310 2023-02-23 22:37:08.722350 lndb-0.39.2/lndb/test/_nox.py
--rw-r--r--   0        0        0      188 2023-02-23 07:03:13.300099 lndb-0.39.2/lndb/test/nox.py
--rw-r--r--   0        0        0     1514 2023-03-31 06:18:24.432328 lndb-0.39.2/noxfile.py
--rw-r--r--   0        0        0     1414 2023-04-01 08:36:57.992406 lndb-0.39.2/pyproject.toml
--rw-r--r--   0        0        0      506 2023-02-17 13:49:16.964718 lndb-0.39.2/tests/test_bionty.py
--rw-r--r--   0        0        0      680 2023-03-31 06:18:24.433575 lndb-0.39.2/tests/test_init_instance.py
--rw-r--r--   0        0        0      385 2023-02-20 08:48:26.782884 lndb-0.39.2/tests/test_notebooks.py
--rw-r--r--   0        0        0     1395 1970-01-01 00:00:00.000000 lndb-0.39.2/PKG-INFO
+-rw-r--r--   0        0        0     3899 2023-04-05 12:41:02.524447 lndb-0.40.0/.github/workflows/build.yml
+-rw-r--r--   0        0        0      133 2023-01-15 12:18:16.566196 lndb-0.40.0/.github/workflows/latest-changes.jinja2
+-rw-r--r--   0        0        0      597 2023-01-15 12:18:16.566256 lndb-0.40.0/.github/workflows/latest-changes.yml
+-rw-r--r--   0        0        0     1204 2023-01-15 12:18:16.566326 lndb-0.40.0/.gitignore
+-rw-r--r--   0        0        0     1772 2023-01-16 03:13:03.815140 lndb-0.40.0/.pre-commit-config.yaml
+-rw-r--r--   0        0        0    11324 2023-01-15 12:18:16.566501 lndb-0.40.0/LICENSE
+-rw-r--r--   0        0        0      173 2023-03-27 04:37:15.707800 lndb-0.40.0/README.md
+-rw-r--r--   0        0        0       52 2023-03-06 11:50:26.265030 lndb-0.40.0/docs/api.md
+-rw-r--r--   0        0        0    45042 2023-04-07 04:14:47.673444 lndb-0.40.0/docs/changelog.md
+-rw-r--r--   0        0        0     4832 2023-03-22 14:41:54.962234 lndb-0.40.0/docs/faq/check-synchronization.ipynb
+-rw-r--r--   0        0        0     3334 2023-03-09 09:28:04.965028 lndb-0.40.0/docs/faq/clone.ipynb
+-rw-r--r--   0        0        0     8397 2023-03-22 05:59:33.863010 lndb-0.40.0/docs/faq/edge-cases-login-init.ipynb
+-rw-r--r--   0        0        0      166 2023-03-22 14:56:35.817208 lndb-0.40.0/docs/faq/index.md
+-rw-r--r--   0        0        0     1180 2023-04-05 05:10:26.112382 lndb-0.40.0/docs/faq/manage-migrations.ipynb
+-rw-r--r--   0        0        0     3248 2023-03-09 09:28:04.965998 lndb-0.40.0/docs/faq/switch-environment.ipynb
+-rw-r--r--   0        0        0     2798 2023-04-05 05:10:26.112662 lndb-0.40.0/docs/faq/test-migrations-e2e.ipynb
+-rw-r--r--   0        0        0     2073 2023-04-05 05:10:26.112933 lndb-0.40.0/docs/faq/test-migrations-unit.ipynb
+-rw-r--r--   0        0        0     5163 2023-03-22 05:59:33.863390 lndb-0.40.0/docs/guide/01-setup-user.ipynb
+-rw-r--r--   0        0        0    10400 2023-03-22 05:59:33.863723 lndb-0.40.0/docs/guide/02-init-instance.ipynb
+-rw-r--r--   0        0        0     5573 2023-03-22 14:56:35.818426 lndb-0.40.0/docs/guide/03-load-instance.ipynb
+-rw-r--r--   0        0        0     5290 2023-03-09 09:28:04.966850 lndb-0.40.0/docs/guide/04-set-storage.ipynb
+-rw-r--r--   0        0        0     3724 2023-03-22 05:59:33.864269 lndb-0.40.0/docs/guide/05-schema-modules.ipynb
+-rw-r--r--   0        0        0     1496 2023-03-22 05:59:33.864524 lndb-0.40.0/docs/guide/06-info.ipynb
+-rw-r--r--   0        0        0     3282 2023-03-22 05:59:33.864793 lndb-0.40.0/docs/guide/07-delete.ipynb
+-rw-r--r--   0        0        0      129 2023-02-16 15:52:14.590660 lndb-0.40.0/docs/guide/index.md
+-rw-r--r--   0        0        0     3152 2023-03-25 20:23:06.444401 lndb-0.40.0/docs/guide/migrate.md
+-rw-r--r--   0        0        0      126 2023-02-16 21:53:37.660107 lndb-0.40.0/docs/index.md
+-rw-r--r--   0        0        0      118 2023-02-17 10:58:37.191812 lndb-0.40.0/lamin-project.yaml
+-rw-r--r--   0        0        0     1932 2023-04-07 04:14:15.041388 lndb-0.40.0/lndb/__init__.py
+-rw-r--r--   0        0        0     4242 2023-02-27 18:35:12.951712 lndb-0.40.0/lndb/__main__.py
+-rw-r--r--   0        0        0      100 2023-02-12 04:51:38.272115 lndb-0.40.0/lndb/_assets/__init__.py
+-rw-r--r--   0        0        0      216 2023-04-03 04:25:19.341088 lndb-0.40.0/lndb/_check_versions.py
+-rw-r--r--   0        0        0      360 2023-02-16 21:53:37.660535 lndb-0.40.0/lndb/_close.py
+-rw-r--r--   0        0        0     2146 2023-04-05 13:47:39.618861 lndb-0.40.0/lndb/_delete.py
+-rw-r--r--   0        0        0      222 2023-02-16 21:53:37.660919 lndb-0.40.0/lndb/_info.py
+-rw-r--r--   0        0        0     5755 2023-04-05 12:41:02.525310 lndb-0.40.0/lndb/_init_instance.py
+-rw-r--r--   0        0        0     3752 2023-04-05 05:10:26.113362 lndb-0.40.0/lndb/_load_instance.py
+-rw-r--r--   0        0        0      135 2023-04-05 05:10:26.113647 lndb-0.40.0/lndb/_migrate/__init__.py
+-rw-r--r--   0        0        0      723 2023-04-05 05:10:26.113978 lndb-0.40.0/lndb/_migrate/alembic.ini
+-rw-r--r--   0        0        0     3469 2023-04-05 12:41:02.533096 lndb-0.40.0/lndb/_migrate/core.py
+-rw-r--r--   0        0        0     6303 2023-04-05 05:10:26.114561 lndb-0.40.0/lndb/_migrate/deploy.py
+-rw-r--r--   0        0        0     3179 2023-02-16 21:53:37.661733 lndb-0.40.0/lndb/_migrate/env.py
+-rw-r--r--   0        0        0      341 2023-02-16 21:53:37.661843 lndb-0.40.0/lndb/_migrate/script.py.mako
+-rw-r--r--   0        0        0     4840 2023-04-05 05:10:26.114776 lndb-0.40.0/lndb/_migrate/utils.py
+-rw-r--r--   0        0        0     1020 2023-02-12 04:51:38.274334 lndb-0.40.0/lndb/_schema.py
+-rw-r--r--   0        0        0     1490 2023-04-05 12:41:02.525753 lndb-0.40.0/lndb/_set.py
+-rw-r--r--   0        0        0     2165 2023-04-07 02:52:01.648931 lndb-0.40.0/lndb/_settings.py
+-rw-r--r--   0        0        0       87 2023-02-16 21:53:37.662311 lndb-0.40.0/lndb/_settings_load.py
+-rw-r--r--   0        0        0       72 2023-02-16 21:53:37.662460 lndb-0.40.0/lndb/_settings_store.py
+-rw-r--r--   0        0        0     5291 2023-03-12 15:04:39.932675 lndb-0.40.0/lndb/_setup_user.py
+-rw-r--r--   0        0        0      363 2023-04-05 12:41:02.526023 lndb-0.40.0/lndb/dev/__init__.py
+-rw-r--r--   0        0        0     4030 2023-03-27 17:35:42.591834 lndb-0.40.0/lndb/dev/_clone.py
+-rw-r--r--   0        0        0     6341 2023-04-05 12:41:02.526216 lndb-0.40.0/lndb/dev/_db.py
+-rw-r--r--   0        0        0     2491 2023-02-16 21:53:37.663214 lndb-0.40.0/lndb/dev/_deprecated.py
+-rw-r--r--   0        0        0      240 2023-02-16 21:53:37.663286 lndb-0.40.0/lndb/dev/_docs.py
+-rw-r--r--   0        0        0     5284 2023-04-05 12:41:02.526831 lndb-0.40.0/lndb/dev/_exclusion.py
+-rw-r--r--   0        0        0     8389 2023-04-05 12:41:02.527633 lndb-0.40.0/lndb/dev/_settings_instance.py
+-rw-r--r--   0        0        0     2629 2023-03-22 05:59:33.865686 lndb-0.40.0/lndb/dev/_settings_load.py
+-rw-r--r--   0        0        0     2061 2023-02-16 21:53:37.663723 lndb-0.40.0/lndb/dev/_settings_save.py
+-rw-r--r--   0        0        0     2454 2023-04-07 04:13:56.734044 lndb-0.40.0/lndb/dev/_settings_store.py
+-rw-r--r--   0        0        0      976 2023-02-16 21:53:37.663901 lndb-0.40.0/lndb/dev/_settings_user.py
+-rw-r--r--   0        0        0     2446 2023-03-21 06:52:10.981980 lndb-0.40.0/lndb/dev/_setup_knowledge.py
+-rw-r--r--   0        0        0     6996 2023-03-30 17:54:01.453792 lndb-0.40.0/lndb/dev/_setup_schema.py
+-rw-r--r--   0        0        0     4004 2023-04-05 12:41:02.528400 lndb-0.40.0/lndb/dev/_storage.py
+-rw-r--r--   0        0        0      140 2023-02-24 20:31:36.945684 lndb-0.40.0/lndb/dev/_testdb.py
+-rw-r--r--   0        0        0      356 2023-04-05 05:10:26.115134 lndb-0.40.0/lndb/test/__init__.py
+-rw-r--r--   0        0        0       50 2023-02-24 20:31:36.946187 lndb-0.40.0/lndb/test/_env.py
+-rw-r--r--   0        0        0     3856 2023-03-30 17:54:01.454075 lndb-0.40.0/lndb/test/_migrations_e2e.py
+-rw-r--r--   0        0        0     6646 2023-04-05 05:10:26.115464 lndb-0.40.0/lndb/test/_migrations_unit.py
+-rw-r--r--   0        0        0      310 2023-02-24 20:31:36.946490 lndb-0.40.0/lndb/test/_nox.py
+-rw-r--r--   0        0        0      188 2023-02-22 22:13:54.788863 lndb-0.40.0/lndb/test/nox.py
+-rw-r--r--   0        0        0     1514 2023-03-09 09:28:04.969263 lndb-0.40.0/noxfile.py
+-rw-r--r--   0        0        0     1219 2023-04-07 03:35:22.756124 lndb-0.40.0/pyproject.toml
+-rw-r--r--   0        0        0      506 2023-02-12 04:51:38.276939 lndb-0.40.0/tests/test_bionty.py
+-rw-r--r--   0        0        0      680 2023-03-09 09:28:04.969725 lndb-0.40.0/tests/test_init_instance.py
+-rw-r--r--   0        0        0      385 2023-02-21 15:53:42.076396 lndb-0.40.0/tests/test_notebooks.py
+-rw-r--r--   0        0        0     1162 1970-01-01 00:00:00.000000 lndb-0.40.0/PKG-INFO
```

### Comparing `lndb-0.39.2/.github/workflows/build.yml` & `lndb-0.40.0/.github/workflows/build.yml`

 * *Files 2% similar despite different names*

```diff
@@ -30,15 +30,15 @@
       - name: Setup Python
         uses: actions/setup-python@v3
         with:
           python-version: ${{ matrix.python-version }}
       - name: Cache pre-commit & nox
         uses: actions/cache@v3
         env:
-          cache-name: cache-3
+          cache-name: cache-4
         with:
           path: |
             .nox
             ~/.cache/pre-commit
           key: ${{ runner.os }}-build-${{ env.cache-name }}-${{ hashFiles('.pre-commit-config.yaml') }}-${{ hashFiles('pyproject.yaml') }}
       - name: Cache postgres
         id: cache-postgres
```

### Comparing `lndb-0.39.2/.github/workflows/latest-changes.yml` & `lndb-0.40.0/.github/workflows/latest-changes.yml`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/.gitignore` & `lndb-0.40.0/.gitignore`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/.pre-commit-config.yaml` & `lndb-0.40.0/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/LICENSE` & `lndb-0.40.0/LICENSE`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/docs/changelog.md` & `lndb-0.40.0/docs/changelog.md`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,19 @@
 # Changelog
 
 <!-- prettier-ignore -->
 Name | PR | Developer | Date | Version
 --- | --- | --- | --- | ---
+🚸 Rename settings directory to `.lamin` | [349](https://github.com/laminlabs/lndb/pull/349) | [falexwolf](https://github.com/falexwolf) | 2023-04-07 | 0.40.0
+🚸 Expose storage in settings | [348](https://github.com/laminlabs/lndb/pull/348) | [falexwolf](https://github.com/falexwolf) | 2023-04-07 |
+♻️ Move storage related code to lndb_storage | [338](https://github.com/laminlabs/lndb/pull/338) | [Koncopd](https://github.com/Koncopd) | 2023-04-05 |
+♻️ Refactor migrations | [346](https://github.com/laminlabs/lndb/pull/346) | [falexwolf](https://github.com/falexwolf) | 2023-04-04 |
 🧑‍💻 Enable to load instance from hub using access token | [343](https://github.com/laminlabs/lndb/pull/343) | [fredericenard](https://github.com/fredericenard) | 2023-04-03 | 0.39.2
 ⬆️ Upgrade lnhub-rest to 0.7.2 | [341](https://github.com/laminlabs/lndb/pull/341) | [falexwolf](https://github.com/falexwolf) | 2023-03-31 | 0.39.1
-:green_heart: Try to fix CI | [342](https://github.com/laminlabs/lndb/pull/342) | [falexwolf](https://github.com/falexwolf) | 2023-03-30 |
+💚 Try to fix CI | [342](https://github.com/laminlabs/lndb/pull/342) | [falexwolf](https://github.com/falexwolf) | 2023-03-30 |
 🚸 Check schema version upon init | [340](https://github.com/laminlabs/lndb/pull/340) | [falexwolf](https://github.com/falexwolf) | 2023-03-30 | 0.39.0
 🚸 Enforce order of schema modules for migration | [339](https://github.com/laminlabs/lndb/pull/339) | [falexwolf](https://github.com/falexwolf) | 2023-03-27 | 0.38.1
 💚 Improve e2e migrations guide | [337](https://github.com/laminlabs/lndb/pull/337) | [falexwolf](https://github.com/falexwolf) | 2023-03-26 | 0.38.0
 🚸 Update `_migration` in `__init__.py` of schema modules | [336](https://github.com/laminlabs/lndb/pull/336) | [falexwolf](https://github.com/falexwolf) | 2023-03-25 |
 🎨 Improve e2e migrations testing | [335](https://github.com/laminlabs/lndb/pull/335) | [falexwolf](https://github.com/falexwolf) | 2023-03-25 |
 🎨 Improve switching logic from and to sqlite | [334](https://github.com/laminlabs/lndb/pull/334) | [falexwolf](https://github.com/falexwolf) | 2023-03-22 | 0.37.9
 ✅ Add tests for migration unit tests | [333](https://github.com/laminlabs/lndb/pull/333) | [falexwolf](https://github.com/falexwolf) | 2023-03-22 | 0.37.8
```

### Comparing `lndb-0.39.2/docs/faq/check-synchronization.ipynb` & `lndb-0.40.0/docs/faq/check-synchronization.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/docs/faq/clone.ipynb` & `lndb-0.40.0/docs/faq/clone.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/docs/faq/edge-cases-login-init.ipynb` & `lndb-0.40.0/docs/faq/edge-cases-login-init.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/docs/faq/manage-migrations.ipynb` & `lndb-0.40.0/docs/guide/06-info.ipynb`

 * *Files 12% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8350694444444444%*

 * *Differences: {"'cells'": "{0: {'metadata': {replace: OrderedDict([('tags', [])])}, 'source': ['# Get info on an "*

 * *            "instance'], 'id': 'b43d09d5-26d3-440d-b334-9643ec5248e6'}, 1: {'source': ['import "*

 * *            "lamindb as ln'], 'id': '33c2bb76-d61f-4866-87e2-780e61600022'}, 2: {'source': "*

 * *            '[\'ln.setup.load("mydata")\'], \'id\': \'b8a6f1fe\'}, 3: {\'source\': {insert: [(0, '*

 * *            "'Running \\n'), (2, 'lamin info\\n'), (4, '\\n'), (5, 'on the command line runs the "*

 * *            "following: […]*

```diff
@@ -1,54 +1,60 @@
 {
     "cells": [
         {
             "cell_type": "markdown",
-            "metadata": {},
+            "id": "b43d09d5-26d3-440d-b334-9643ec5248e6",
+            "metadata": {
+                "tags": []
+            },
             "source": [
-                "# Manage migrations"
+                "# Get info on an instance"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
+            "id": "33c2bb76-d61f-4866-87e2-780e61600022",
             "metadata": {},
             "outputs": [],
             "source": [
-                "from lndb import migrate, init\n",
-                "import lnschema_core\n",
-                "from pathlib import Path"
+                "import lamindb as ln"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
+            "id": "b8a6f1fe",
             "metadata": {},
             "outputs": [],
             "source": [
-                "schema_root = Path(lnschema_core.__file__).parent.parent"
+                "ln.setup.load(\"mydata\")"
             ]
         },
         {
             "cell_type": "markdown",
+            "id": "25a13298",
             "metadata": {},
             "source": [
-                "Running the following on the CLI\n",
+                "Running \n",
                 "```\n",
-                "lamin migrate generate\n",
+                "lamin info\n",
                 "```\n",
-                "runs"
+                "\n",
+                "on the command line runs the following:"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
+            "id": "8436575d",
             "metadata": {},
             "outputs": [],
             "source": [
-                "migrate.generate(schema_root=schema_root, package_name=\"lnschema_core\")"
+                "ln.setup.info()"
             ]
         }
     ],
     "metadata": {
         "kernelspec": {
             "display_name": "Python 3 (ipykernel)",
             "language": "python",
@@ -69,9 +75,9 @@
         "vscode": {
             "interpreter": {
                 "hash": "40d3a090f54c6569ab1632332b64b2c03c39dcf918b08424e98f38b5ae0af88f"
             }
         }
     },
     "nbformat": 4,
-    "nbformat_minor": 4
+    "nbformat_minor": 5
 }
```

### Comparing `lndb-0.39.2/docs/faq/switch-environment.ipynb` & `lndb-0.40.0/docs/faq/switch-environment.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/docs/faq/test-migrations-e2e.ipynb` & `lndb-0.40.0/docs/faq/test-migrations-e2e.ipynb`

 * *Files 13% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9856944444444444%*

 * *Differences: {"'cells'": "{2: {'source': ['import lndb']}, 4: {'source': "*

 * *            '[\'lndb.test.migrate_clone(storage="s3://lamin-site-assets")\']}, 5: {\'source\': '*

 * *            '[\'lndb.delete("lamin-site-assets_test")\']}, 6: {\'source\': '*

 * *            '[\'lndb.test.migrate_clones("lnschema_core", n_instances=1, '*

 * *            'dialect_name="sqlite")\']}, 8: {\'source\': {insert: [(1, \'# '*

 * *            "lndb.test.migrate_clone(\\n')], delete: [1]}}, 9: {'source': "*

 * *            '[\'lndb.test.migrate_clones("lnsche […]*

```diff
@@ -21,15 +21,15 @@
         {
             "cell_type": "code",
             "execution_count": null,
             "id": "33c2bb76-d61f-4866-87e2-780e61600022",
             "metadata": {},
             "outputs": [],
             "source": [
-                "import lamindb as ln"
+                "import lndb"
             ]
         },
         {
             "cell_type": "markdown",
             "id": "119134fc-1362-4b6f-85e9-d65e5ab091cf",
             "metadata": {},
             "source": [
@@ -39,39 +39,39 @@
         {
             "cell_type": "code",
             "execution_count": null,
             "id": "2fe506c7-9788-4f04-8d12-a5a855a81db0",
             "metadata": {},
             "outputs": [],
             "source": [
-                "ln.setup.test.migrate_clone(storage=\"s3://lamin-site-assets\")"
+                "lndb.test.migrate_clone(storage=\"s3://lamin-site-assets\")"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
             "id": "8f16a4b4-e165-4df3-af1b-592796b9bca5",
             "metadata": {
                 "tags": [
                     "hide-cell"
                 ]
             },
             "outputs": [],
             "source": [
-                "ln.setup.delete(\"lamin-site-assets_test\")"
+                "lndb.delete(\"lamin-site-assets_test\")"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
             "id": "f1f43b5a-59ca-419a-8ed1-9672f2ff2025",
             "metadata": {},
             "outputs": [],
             "source": [
-                "ln.setup.test.migrate_clones(\"lnschema_core\", n_instances=1, dialect_name=\"sqlite\")"
+                "lndb.test.migrate_clones(\"lnschema_core\", n_instances=1, dialect_name=\"sqlite\")"
             ]
         },
         {
             "cell_type": "markdown",
             "id": "e53c8996-73a1-4c5f-b54f-4ea9ea117702",
             "metadata": {},
             "source": [
@@ -82,33 +82,33 @@
             "cell_type": "code",
             "execution_count": null,
             "id": "cd10731f-5667-4550-99db-90fb47e92c32",
             "metadata": {},
             "outputs": [],
             "source": [
                 "# replace with lamindata!\n",
-                "# ln.setup.test.migrate_clone(\n",
+                "# lndb.test.migrate_clone(\n",
                 "#     db=\"postgresql://batman:robin@35.222.187.204:5432/retro\", schema=\"bionty,retro\"\n",
                 "# )"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
             "id": "58c449e1-74e3-46b4-9361-343802fc1841",
             "metadata": {},
             "outputs": [],
             "source": [
-                "ln.setup.test.migrate_clones(\"lnschema_core\", n_instances=1, dialect_name=\"postgresql\")"
+                "lndb.test.migrate_clones(\"lnschema_core\", n_instances=1, dialect_name=\"postgresql\")"
             ]
         }
     ],
     "metadata": {
         "kernelspec": {
-            "display_name": "Python 3 (ipykernel)",
+            "display_name": "py39",
             "language": "python",
             "name": "python3"
         },
         "language_info": {
             "codemirror_mode": {
                 "name": "ipython",
                 "version": 3
@@ -118,14 +118,14 @@
             "name": "python",
             "nbconvert_exporter": "python",
             "pygments_lexer": "ipython3",
             "version": "3.9.15"
         },
         "vscode": {
             "interpreter": {
-                "hash": "40d3a090f54c6569ab1632332b64b2c03c39dcf918b08424e98f38b5ae0af88f"
+                "hash": "61b4062b24dfb1010f420dad5aa3bd73a4d2af47d0ec44eafec465a35a9d7239"
             }
         }
     },
     "nbformat": 4,
     "nbformat_minor": 5
 }
```

### Comparing `lndb-0.39.2/docs/faq/test-migrations-unit.ipynb` & `lndb-0.40.0/docs/guide/07-delete.ipynb`

 * *Files 15% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9107638888888889%*

 * *Differences: {"'cells'": "{0: {'id': 'b43d09d5-26d3-440d-b334-9643ec5248e6', 'metadata': {replace: "*

 * *            "OrderedDict([('tags', [])])}, 'source': ['# Delete an instance']}, 1: {'id': "*

 * *            "'33c2bb76-d61f-4866-87e2-780e61600022', 'source': ['from lndb import delete, load, "*

 * *            "login, init, settings\\n', 'from lndb.dev._settings_store import "*

 * *            "instance_settings_file\\n', 'from pathlib import Path\\n', 'from datetime import "*

 * *            'datetime\']}, 2: {\'id\': \'485f5ee1\', \'sou […]*

```diff
@@ -1,143 +1,148 @@
 {
     "cells": [
         {
             "cell_type": "markdown",
-            "id": "558d9dfc-e367-4406-b8df-c67647385e76",
-            "metadata": {},
+            "id": "b43d09d5-26d3-440d-b334-9643ec5248e6",
+            "metadata": {
+                "tags": []
+            },
             "source": [
-                "# Test migrations unit"
+                "# Delete an instance"
             ]
         },
         {
-            "cell_type": "markdown",
-            "id": "4330bc99-65c0-491d-a750-f59d86278b98",
+            "cell_type": "code",
+            "execution_count": null,
+            "id": "33c2bb76-d61f-4866-87e2-780e61600022",
             "metadata": {},
+            "outputs": [],
             "source": [
-                "Let us first mimic what happens inside a noxfile in a schema module. We set up a reference instance:"
+                "from lndb import delete, load, login, init, settings\n",
+                "from lndb.dev._settings_store import instance_settings_file\n",
+                "from pathlib import Path\n",
+                "from datetime import datetime"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
-            "id": "a11f61be-cdb7-4f2c-9ab1-7f7a8c0351ea",
+            "id": "485f5ee1",
             "metadata": {},
             "outputs": [],
             "source": [
-                "import lndb\n",
-                "from laminci.db import setup_local_test_postgres"
+                "login(\"testuser1\")"
             ]
         },
         {
-            "cell_type": "code",
-            "execution_count": null,
-            "id": "ce23227a-af86-4621-90b3-baff8107cd67",
+            "cell_type": "markdown",
+            "id": "cceb6b43",
             "metadata": {},
-            "outputs": [],
             "source": [
-                "pgurl = setup_local_test_postgres()"
+                "## With local default storage"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
-            "id": "cd90aa98-51a6-4e08-9945-be2b2c5944bf",
+            "id": "2609e58d",
             "metadata": {},
             "outputs": [],
             "source": [
-                "lndb.init(storage=\"./pgtest\", db=pgurl)"
+                "init(storage=\"mydata-delete\")\n",
+                "settings_file = instance_settings_file(\"mydata-delete\", \"testuser1\")"
             ]
         },
         {
             "cell_type": "markdown",
-            "id": "5082f68d-11c4-4568-8651-1b58f12825a7",
+            "id": "25a13298",
             "metadata": {},
             "source": [
-                "Let's now procede to importing lnschema_core (it depends on the current instance settings which were changed by lndb.init):"
+                "Running \n",
+                "```\n",
+                "!lamin delete mydata\n",
+                "```"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
-            "id": "5ce51d4d-b5a5-4a50-98f1-5ac993070f19",
+            "id": "8436575d",
             "metadata": {},
             "outputs": [],
             "source": [
-                "import os\n",
-                "import lnschema_core\n",
-                "from pathlib import Path\n",
-                "from lnschema_core import _schema_id as schema_id\n",
-                "from lndb._migrate import generate_module_files\n",
-                "from lndb.test import model_definitions_match_ddl"
+                "delete(\"mydata-delete\")"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
-            "id": "24ce5c11-2f13-40b7-baa8-a6c8e4c7800c",
+            "id": "d2e607c9",
             "metadata": {},
             "outputs": [],
             "source": [
-                "package_name = \"lnschema_core\"\n",
-                "migrations_path = Path(lnschema_core.__file__).parent / \"migrations\""
+                "assert settings_file.exists() == False"
             ]
         },
         {
-            "cell_type": "code",
-            "execution_count": null,
-            "id": "c4ef3b08-486d-43d3-9e02-201fc4f91957",
+            "cell_type": "markdown",
+            "id": "3286fbcc",
             "metadata": {},
-            "outputs": [],
             "source": [
-                "migrations_path"
+                "## With remote default storage"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
-            "id": "e6a8fb6d-82bb-4546-aa3b-87a9b456bd3d",
+            "id": "fa1efbce",
             "metadata": {},
             "outputs": [],
             "source": [
-                "Path(lnschema_core.__file__).parent.parent"
+                "instance_name = f\"lamin.ci.instance.{datetime.now().timestamp()}\""
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
-            "id": "79a3214f-ef24-4927-afe6-aaa8cde23157",
+            "id": "037f38a3",
             "metadata": {},
             "outputs": [],
             "source": [
-                "# currently still needed\n",
-                "os.chdir(Path(lnschema_core.__file__).parent.parent)"
+                "init(storage=\"s3://lndb-setup-delete-ci\", name=instance_name)"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
-            "id": "b49d863b-37e4-44f1-be3f-2e5fce1e9342",
+            "id": "b2593ef8",
             "metadata": {},
             "outputs": [],
             "source": [
-                "def test_model_definitions_match_ddl_postgres():\n",
-                "    generate_module_files(\n",
-                "        package_name=package_name, migrations_path=migrations_path, schema_id=schema_id\n",
-                "    )\n",
-                "    model_definitions_match_ddl(package_name, dialect_name=\"postgresql\")"
+                "delete(instance_name)"
+            ]
+        },
+        {
+            "cell_type": "markdown",
+            "id": "06a22900",
+            "metadata": {},
+            "source": [
+                "Clean up instances."
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
-            "id": "a0dca892-4a44-48ba-91f0-7f6b78bba4d2",
+            "id": "9117428e",
             "metadata": {},
             "outputs": [],
             "source": [
-                "test_model_definitions_match_ddl_postgres()"
+                "from lnhub_rest._clean_ci import delete_ci_instances\n",
+                "\n",
+                "delete_ci_instances()"
             ]
         }
     ],
     "metadata": {
         "kernelspec": {
             "display_name": "Python 3 (ipykernel)",
             "language": "python",
@@ -150,12 +155,17 @@
             },
             "file_extension": ".py",
             "mimetype": "text/x-python",
             "name": "python",
             "nbconvert_exporter": "python",
             "pygments_lexer": "ipython3",
             "version": "3.9.15"
+        },
+        "vscode": {
+            "interpreter": {
+                "hash": "40d3a090f54c6569ab1632332b64b2c03c39dcf918b08424e98f38b5ae0af88f"
+            }
         }
     },
     "nbformat": 4,
     "nbformat_minor": 5
 }
```

### Comparing `lndb-0.39.2/docs/guide/01-setup-user.ipynb` & `lndb-0.40.0/docs/guide/01-setup-user.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/docs/guide/02-init-instance.ipynb` & `lndb-0.40.0/docs/guide/02-init-instance.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/docs/guide/03-load-instance.ipynb` & `lndb-0.40.0/docs/guide/03-load-instance.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/docs/guide/04-set-storage.ipynb` & `lndb-0.40.0/docs/guide/04-set-storage.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/docs/guide/05-schema-modules.ipynb` & `lndb-0.40.0/docs/guide/05-schema-modules.ipynb`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/docs/guide/06-info.ipynb` & `lndb-0.40.0/docs/faq/manage-migrations.ipynb`

 * *Files 14% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8163194444444444%*

 * *Differences: {"'cells'": "{0: {'metadata': {replace: OrderedDict()}, 'source': ['# Manage migrations'], delete: "*

 * *            "['id']}, 1: {'source': ['import lndb'], delete: ['id']}, 2: {'source': {insert: [(0, "*

 * *            "'Running the following on the CLI\\n'), (2, 'lamin migrate generate\\n'), (4, "*

 * *            "'runs')], delete: [5, 4, 2, 0]}, delete: ['id']}, 3: {'source': "*

 * *            '[\'lndb.migrate.generate(package_name="lnschema_core")\'], delete: [\'id\']}, delete: '*

 * *            '[1]}',*

 * * "'nbformat_minor' […]*

```diff
@@ -1,60 +1,43 @@
 {
     "cells": [
         {
             "cell_type": "markdown",
-            "id": "b43d09d5-26d3-440d-b334-9643ec5248e6",
-            "metadata": {
-                "tags": []
-            },
-            "source": [
-                "# Get info on an instance"
-            ]
-        },
-        {
-            "cell_type": "code",
-            "execution_count": null,
-            "id": "33c2bb76-d61f-4866-87e2-780e61600022",
             "metadata": {},
-            "outputs": [],
             "source": [
-                "import lamindb as ln"
+                "# Manage migrations"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
-            "id": "b8a6f1fe",
             "metadata": {},
             "outputs": [],
             "source": [
-                "ln.setup.load(\"mydata\")"
+                "import lndb"
             ]
         },
         {
             "cell_type": "markdown",
-            "id": "25a13298",
             "metadata": {},
             "source": [
-                "Running \n",
+                "Running the following on the CLI\n",
                 "```\n",
-                "lamin info\n",
+                "lamin migrate generate\n",
                 "```\n",
-                "\n",
-                "on the command line runs the following:"
+                "runs"
             ]
         },
         {
             "cell_type": "code",
             "execution_count": null,
-            "id": "8436575d",
             "metadata": {},
             "outputs": [],
             "source": [
-                "ln.setup.info()"
+                "lndb.migrate.generate(package_name=\"lnschema_core\")"
             ]
         }
     ],
     "metadata": {
         "kernelspec": {
             "display_name": "Python 3 (ipykernel)",
             "language": "python",
@@ -75,9 +58,9 @@
         "vscode": {
             "interpreter": {
                 "hash": "40d3a090f54c6569ab1632332b64b2c03c39dcf918b08424e98f38b5ae0af88f"
             }
         }
     },
     "nbformat": 4,
-    "nbformat_minor": 5
+    "nbformat_minor": 4
 }
```

### Comparing `lndb-0.39.2/docs/guide/migrate.md` & `lndb-0.40.0/docs/guide/migrate.md`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/__init__.py` & `lndb-0.40.0/lndb/__init__.py`

 * *Files 6% similar despite different names*

```diff
@@ -46,21 +46,21 @@
 
 .. autosummary::
    :toctree:
 
    dev
 """
 
-__version__ = "0.39.2"  # denote a release candidate for 0.1.0 with 0.1rc1
+__version__ = "0.40.0"  # denote a release candidate for 0.1.0 with 0.1rc1
 
 import sys
 from os import name as _os_name
 
 from . import _check_versions  # noqa
-from . import dev
+from . import dev, test
 from ._close import close  # noqa
 from ._delete import delete  # noqa
 from ._info import info  # noqa
 from ._init_instance import init  # noqa
 from ._load_instance import load  # noqa
 from ._migrate import migrate
 from ._schema import schema  # noqa
```

### Comparing `lndb-0.39.2/lndb/__main__.py` & `lndb-0.40.0/lndb/__main__.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/_delete.py` & `lndb-0.40.0/lndb/_delete.py`

 * *Files 14% similar despite different names*

```diff
@@ -17,19 +17,22 @@
         raise RuntimeError(
             "Instance settings do not exist locally. Did you provide a wrong instance"
             " name? Could you try loading it?"
         )
     isettings = load_instance_settings(settings_file)
 
     delete_settings(settings_file)
-    if instance_identifier == settings.instance.identifier:
-        current_settings_file = current_instance_settings_file()
-        logger.info(f"    current instance settings {current_settings_file} deleted")
-        current_settings_file.unlink()
-        settings._instance_settings = None
+    if settings._instance_exists:
+        if instance_identifier == settings.instance.identifier:
+            current_settings_file = current_instance_settings_file()
+            logger.info(
+                f"    current instance settings {current_settings_file} deleted"
+            )
+            current_settings_file.unlink()
+            settings._instance_settings = None
     delete_cache(isettings.storage.cache_dir)
     logger.info(
         f"    consider deleting your stored data manually: {isettings.storage.root}"
     )
     if isettings.dialect == "sqlite":
         if isettings._sqlite_file.exists():
             isettings._sqlite_file.unlink()
```

### Comparing `lndb-0.39.2/lndb/_init_instance.py` & `lndb-0.40.0/lndb/_init_instance.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,24 +1,25 @@
 import sys
 from pathlib import Path
 from typing import Optional, Union
 
 from lamin_logger import logger
+from lndb_storage import UPath
 from lnhub_rest._add_storage import get_storage_region
 from lnhub_rest._init_instance import init_instance as init_instance_hub
 from lnhub_rest._init_instance import (
     validate_db_arg,
     validate_schema_arg,
     validate_storage_arg,
 )
 from pydantic import PostgresDsn
 
 from ._load_instance import load, load_from_isettings
 from ._settings import settings
-from .dev import InstanceSettings, UPath
+from .dev import InstanceSettings
 from .dev._db import insert_if_not_exists, upsert
 from .dev._docs import doc_args
 from .dev._setup_knowledge import write_bionty_versions
 from .dev._setup_schema import load_schema, setup_schema
 from .dev._storage import Storage
```

### Comparing `lndb-0.39.2/lndb/_load_instance.py` & `lndb-0.40.0/lndb/_load_instance.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/_migrate/__init__.py` & `lndb-0.40.0/lndb/_migrate/core.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,96 +1,96 @@
-from pathlib import Path
 from subprocess import run
 from typing import Optional
 
 from lamin_logger import logger
+from laminci import get_package_name
 
-from ._deploy import check_deploy_migration  # noqa
-from ._utils import (
+from lndb._migrate.deploy import check_deploy_migration  # noqa
+from lndb._migrate.utils import (
     generate_module_files,
-    get_package_info,
+    get_schema_package_info,
     modify_alembic_ini,
     modify_migration_id_in__init__,
     set_alembic_logging_level,
 )
 
-push_instruction = """Please push your changes to a new remote branch and open a PR.
-Inspect CI step Build output and add migration code to the script.
-It will look like the following, beware of the renaming:
+push_instruction = """\
+Please push your changes to a new remote branch, open a PR, and wait for CI.
+
+Inspect the bottom of the output of the CI step 'Build'
+and add the code to the migration script.
+
+It will look like the following:
     op.drop_column('biosample', 'description', schema='wetlab')
-    op.add_column('experiment', sa.Column('donor_id', sqlmodel.sql.sqltypes.AutoString(), schema="wetlab")"""  # noqa
+    op.add_column('experiment', sa.Column('donor_id', sqlmodel.sql.sqltypes.AutoString(), schema="wetlab")  # noqa
+
+Beware to account for renaming columns and tables manually, e.g.:
+    op.alter_column("mytable", column_name="oldname", new_column_name="newname", schema="myschema")  # noqa
+
+"""
 
 
 class migrate:
     """Manage migrations."""
 
     @staticmethod
     def generate(
         version: str = "vX.X.X",
-        schema_root: Optional[Path] = None,
         package_name: Optional[str] = None,
     ):
         """Generate migration for current schema module.
 
         Needs to be executed at the root level of the python package that contains
         the schema module.
 
         Args:
             version: Version string to label migration with.
-            schema_root: Optional. Root directory of schema module.
             package_name: Optional. Name of schema module package.
         """
-        package_name, migrations_path, schema_id = get_package_info(
-            schema_root=schema_root, package_name=package_name
-        )
-        generate_module_files(
-            package_name=package_name,  # type:ignore
-            migrations_path=migrations_path,
-            schema_id=schema_id,
-        )
-        testdb_path = migrations_path.parent.parent / "testdb/testdb.lndb"  # type: ignore # noqa
+        if package_name is None:
+            package_name = get_package_name()
+        package_dir, migrations_dir, schema_id = get_schema_package_info(package_name)
+        generate_module_files(package_name)
+        testdb_path = package_dir.parent / "testdb/testdb.lndb"  # type: ignore # noqa
         if testdb_path.exists():
             # runs dev mode to write migration scripts
             rm = False
-            set_alembic_logging_level(migrations_path, level="INFO")
-            logger.info("Generate migration with reference db: testdb/testdb.lndb")
+            set_alembic_logging_level(migrations_dir, level="INFO")
+            logger.info(f"Generating based on {testdb_path}")
         else:
             # runs CI-guided mode to generate empty migration scripts
             rm = True
             from lndb._settings import settings
 
             modify_alembic_ini(
-                filepath=migrations_path.parent / "alembic.ini",
+                filepath=package_dir / "alembic.ini",
                 isettings=settings.instance,
                 package_name=package_name,
                 move_sl=False,
             )
-            set_alembic_logging_level(migrations_path, level="WARN")
+            set_alembic_logging_level(migrations_dir, level="WARN")
             logger.info("Generate empty migration script.")
         command = (
-            f"alembic --config {package_name}/alembic.ini --name {schema_id} revision"
-            f" --autogenerate -m '{version}'"
+            f"alembic --config {str(package_dir)}/alembic.ini --name"
+            f" {schema_id} revision --autogenerate -m '{version}'"
         )
-        if schema_root is not None:
-            cwd = f"{schema_root}"
-        else:
-            cwd = None
-        process = run(command, shell=True, cwd=cwd)
+        process = run(command, shell=True)
 
         modify_migration_id_in__init__(package_name)
 
         if process.returncode == 0:
             logger.success(f"Successfully generated migration {version}.")
             if rm:
                 modify_alembic_ini(
-                    filepath=migrations_path.parent / "alembic.ini",
+                    filepath=migrations_dir.parent / "alembic.ini",
                     isettings=settings.instance,
                     package_name=package_name,
                     move_sl=False,
                     revert=True,
                 )
                 logger.info(push_instruction)
             return None
         else:
             print(process.stderr)
             logger.error("Generating migration failed.")
+            logger.info(f"Check content of {str(package_dir)}/alembic.ini")
             return "migrate-gen-failed"
```

### Comparing `lndb-0.39.2/lndb/_migrate/_deploy.py` & `lndb-0.40.0/lndb/_migrate/deploy.py`

 * *Files 3% similar despite different names*

```diff
@@ -7,19 +7,19 @@
 from typing import Any, Optional
 
 import sqlmodel as sqm
 from lamin_logger import logger
 from natsort import natsorted
 from packaging.version import parse as vparse
 
-from ..dev._db import insert
-from ..dev._settings_instance import InstanceSettings
-from ..dev._settings_user import UserSettings
-from ..dev._setup_schema import create_schema_if_not_exists, get_schema_module_name
-from ._utils import generate_module_files, modify_alembic_ini
+from lndb._migrate.utils import generate_module_files, modify_alembic_ini
+from lndb.dev._db import insert
+from lndb.dev._settings_instance import InstanceSettings
+from lndb.dev._settings_user import UserSettings
+from lndb.dev._setup_schema import create_schema_if_not_exists, get_schema_module_name
 
 
 def check_deploy_migration(
     *,
     usettings: UserSettings,
     isettings: InstanceSettings,
     attempt_deploy: Optional[bool] = None,
```

### Comparing `lndb-0.39.2/lndb/_migrate/_utils.py` & `lndb-0.40.0/lndb/_migrate/utils.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,48 +1,26 @@
 import importlib
+import shutil
 from pathlib import Path
-from typing import Optional
-
-from lndb.test import get_package_name
-from lndb.test._migrations_unit import get_migration_id_from_scripts
+from typing import Optional, Tuple
 
 from ..dev._settings_instance import InstanceSettings
 from ..dev._setup_schema import get_schema_module_name
 
 
-def get_package_info(
-    schema_root: Optional[Path] = None, package_name: Optional[str] = None
-):
-    if package_name is None:
-        package_name = get_package_name(schema_root)
+# this is a special function for schema packages
+def get_schema_package_info(package_name: str) -> Tuple[Path, Path, str]:
     package = importlib.import_module(package_name)
     if not hasattr(package, "_schema_id"):
         package_name = f"{package_name}.schema"
         package = importlib.import_module(package_name)
     schema_id = getattr(package, "_schema_id")
-    migrations_path = Path(package.__file__).parent / "migrations"  # type:ignore
-    return package_name, migrations_path, schema_id
-
-
-def generate_alembic_ini(
-    package_name: str,
-    migrations_path: Optional[Path] = None,
-    schema_id: Optional[str] = None,
-):
-    if migrations_path is None:
-        _, migrations_path, schema_id = get_package_info(package_name=package_name)
-    _migrations_path = Path(__file__).parent
-
-    if not (migrations_path.parent / "alembic.ini").exists():
-        content = (
-            _readfile(_migrations_path / "alembic.ini")
-            .replace("[{schema_id}]", f"[{schema_id}]")
-            .replace("{package_name}/migrations", f"{package_name}/migrations")
-        )
-        _writefile(migrations_path.parent / "alembic.ini", content)
+    package_dir = Path(package.__file__).parent  # type: ignore
+    migrations_dir = package_dir / "migrations"
+    return package_dir, migrations_dir, schema_id
 
 
 def modify_migration_id_in__init__(package_name) -> None:
     """Rewrite the migration_id in the __init__.py of the schema module."""
     package = importlib.import_module(package_name)
     filepath = str(package.__file__)
 
@@ -51,14 +29,16 @@
 
     # get line with migration id
     for line in content.split("\n"):
         if line.startswith("_migration = "):
             current_line = line
             break
 
+    from lndb.test._migrations_unit import get_migration_id_from_scripts
+
     migration_id = get_migration_id_from_scripts(package_name)
     content = content.replace(current_line, f'_migration = "{migration_id}"')
 
     with open(filepath, "w") as f:
         f.write(content)
 
 
@@ -96,50 +76,56 @@
 
     with open(filepath, "w") as f:
         f.write(content)
 
 
 def generate_module_files(
     package_name: str,
-    migrations_path: Optional[Path] = None,
+    # the following two are for backward compat only!
+    # they are not being used
+    migrations_path: Optional[Path] = None,  # noqa
     schema_id: Optional[str] = None,
 ):
-    if migrations_path is None:
-        _, migrations_path, schema_id = get_package_info(package_name=package_name)
-    _migrations_path = Path(__file__).parent
+    # this calls ensures that package_name is the only used argument here
+    package_dir, migrations_dir, schema_id = get_schema_package_info(package_name)
+    migrations_templates_dir = Path(__file__).parent
 
     # ensures migrations/versions folder exists
-    (migrations_path / "versions").mkdir(exist_ok=True, parents=True)
+    (migrations_dir / "versions").mkdir(exist_ok=True, parents=True)
 
-    if not (migrations_path / "env.py").exists():
+    if not (migrations_dir / "env.py").exists():
         content = (
-            _readfile(_migrations_path / "env.py")
+            _readfile(migrations_templates_dir / "env.py")
             .replace("_schema_id = None\n", "")
             .replace("# from {package_name} import *", f"from {package_name} import *")
             .replace(
                 "# from {package_name} import _schema_id",
                 f"from {package_name} import _schema_id",
             )
         )
-        _writefile(migrations_path / "env.py", content)
-
-    if not (migrations_path / "script.py.mako").exists():
-        import shutil
+        _writefile(migrations_dir / "env.py", content)
 
+    if not (migrations_dir / "script.py.mako").exists():
         shutil.copyfile(
-            _migrations_path / "script.py.mako", migrations_path / "script.py.mako"
+            migrations_templates_dir / "script.py.mako",
+            migrations_dir / "script.py.mako",
         )
 
-    generate_alembic_ini(
-        package_name=package_name, migrations_path=migrations_path, schema_id=schema_id
-    )
+    # this is at the package_dir level, not at the migrations_dir level
+    if not (package_dir / "alembic.ini").exists():
+        content = (
+            _readfile(migrations_templates_dir / "alembic.ini")
+            .replace("[{schema_id}]", f"[{schema_id}]")
+            .replace("{package_dir}/migrations", f"{str(migrations_dir)}")
+        )
+        _writefile(migrations_dir.parent / "alembic.ini", content)
 
 
-def set_alembic_logging_level(migrations_path: Path, level="INFO"):
-    alembic_ini_path = migrations_path.parent / "alembic.ini"
+def set_alembic_logging_level(migrations_dir: Path, level="INFO"):
+    alembic_ini_path = migrations_dir.parent / "alembic.ini"
     text = _readfile(alembic_ini_path)
     current_level = text.split("[logger_alembic]\n")[1].split("\n")[0]
     new_level = f"level = {level}"
     _writefile(
         alembic_ini_path,
         text.replace(
             f"[logger_alembic]\n{current_level}", f"[logger_alembic]\n{new_level}"
```

### Comparing `lndb-0.39.2/lndb/_migrate/alembic.ini` & `lndb-0.40.0/lndb/_migrate/alembic.ini`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 [{schema_id}]
-script_location = {package_name}/migrations
+script_location = {package_dir}/migrations
 file_template = %%(year)d-%%(month).2d-%%(day).2d-%%(rev)s-%%(slug)s
 prepend_sys_path = .
 version_path_separator = os
 sqlalchemy.url = sqlite:///testdb/testdb.lndb
 
 # Logging configuration
 [loggers]
```

### Comparing `lndb-0.39.2/lndb/_migrate/env.py` & `lndb-0.40.0/lndb/_migrate/env.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/_schema.py` & `lndb-0.40.0/lndb/_schema.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/_set.py` & `lndb-0.40.0/lndb/_set.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,16 +1,17 @@
 from pathlib import Path
 from typing import Union
 
 from lamin_logger import logger
+from lndb_storage import UPath
 from lnhub_rest._add_storage import add_storage as add_storage_hub
 
 from ._init_instance import register
 from ._settings import settings
-from .dev import UPath, deprecated
+from .dev import deprecated
 from .dev._settings_instance import InstanceSettings
 
 
 class set:
     """Set properties of current instance."""
 
     @staticmethod
```

### Comparing `lndb-0.39.2/lndb/_settings.py` & `lndb-0.40.0/lndb/_settings.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 import os
 from typing import Union
 
-from .dev._settings_instance import InstanceSettings
-from .dev._settings_load import load_instance_settings, load_or_create_user_settings
-from .dev._settings_user import UserSettings
+from lndb.dev import InstanceSettings, Storage, UserSettings
+from lndb.dev._settings_load import load_instance_settings, load_or_create_user_settings
 
 
 # https://stackoverflow.com/questions/128573/using-property-on-classmethods/64738850#64738850
 class classproperty(object):
     def __init__(self, fget):
         self.fget = fget
 
@@ -16,48 +15,54 @@
         return self.fget(owner_cls)
 
 
 class settings:
     """Settings access.
 
     - :class:`~lndb.dev.InstanceSettings`
+    - :class:`~lndb.dev.Storage`
     - :class:`~lndb.dev.UserSettings`
     """
 
     _user_settings: Union[UserSettings, None] = None
     _instance_settings: Union[InstanceSettings, None] = None
 
     _user_settings_env: Union[str, None] = None
     _instance_settings_env: Union[str, None] = None
 
     @classproperty
     def user(cls) -> UserSettings:
-        """User-related settings."""
+        """User."""
         if (
             cls._user_settings is None
             or cls._user_settings_env != get_env_name()  # noqa
         ):
             cls._user_settings = load_or_create_user_settings()
             cls._user_settings_env = get_env_name()
             if cls._user_settings and cls._user_settings.id is None:
                 raise RuntimeError("Need to login, first: lamin login <email>")
         return cls._user_settings  # type: ignore
 
     @classproperty
     def instance(cls) -> InstanceSettings:
-        """Instance-related settings."""
+        """Instance."""
         if (
             cls._instance_settings is None
             or cls._instance_settings_env != get_env_name()  # noqa
         ):
             cls._instance_settings = load_instance_settings()
             cls._instance_settings_env = get_env_name()
         return cls._instance_settings  # type: ignore
 
     @classproperty
+    def storage(cls) -> Storage:
+        """Storage."""
+        return cls.instance.storage
+
+    @classproperty
     def _instance_exists(cls):
         try:
             cls.instance
             return True
         except RuntimeError:
             return False
```

### Comparing `lndb-0.39.2/lndb/_setup_user.py` & `lndb-0.40.0/lndb/_setup_user.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/dev/_clone.py` & `lndb-0.40.0/lndb/dev/_clone.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/dev/_db.py` & `lndb-0.40.0/lndb/dev/_db.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,18 +2,17 @@
 # This is currently needed as we can only import the schema module
 # once isettings have been adjusted
 from pathlib import Path
 from typing import Any, List, Optional, Union
 
 import sqlmodel as sqm
 from lamin_logger import logger
+from lndb_storage import UPath
 from sqlalchemy.exc import ProgrammingError
 
-from lndb.dev import UPath
-
 from .._settings import settings
 
 
 class upsert:
     @classmethod
     def user(cls, email: str, user_id: str, handle: str, name: str = None):
         import lnschema_core as schema_core
```

### Comparing `lndb-0.39.2/lndb/dev/_deprecated.py` & `lndb-0.40.0/lndb/dev/_deprecated.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/dev/_exclusion.py` & `lndb-0.40.0/lndb/dev/_exclusion.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,16 +1,15 @@
 from datetime import datetime, timezone
 from pathlib import Path
 from typing import Optional, Union
 
 import fsspec
 from dateutil.parser import isoparse  # type: ignore
 from lamin_logger import logger
-
-from ._upath_ext import UPath
+from lndb_storage import UPath, _infer_filesystem
 
 EXPIRATION_TIME = 1800  # 30 min
 
 MAX_MSG_COUNTER = 1000  # print the msg after this number of iterations
 
 
 class empty_locker:
@@ -27,28 +26,18 @@
     def __init__(self, user_id: str, storage_root: Union[UPath, Path]):
         logger.debug(f"Init cloud sqlite locker: {user_id}, {storage_root}.")
 
         self._counter = 0
 
         self.user = user_id
 
-        root = storage_root
-        self.root = root
-
-        if isinstance(root, UPath):
-            self.fs = root.fs
-        else:
-            protocol = fsspec.utils.get_protocol(str(root))
-            if protocol == "s3":
-                fs_kwargs = {"cache_regions": True}
-            else:
-                fs_kwargs = {}
-            self.fs = fsspec.filesystem(protocol, **fs_kwargs)
+        self.root = storage_root
+        self.fs, _ = _infer_filesystem(storage_root)
 
-        exclusion_path = root / "exclusion"
+        exclusion_path = storage_root / "exclusion"
         self.mapper = fsspec.FSMap(str(exclusion_path), self.fs, create=True)
 
         priorities_path = str(exclusion_path / "priorities")
         if self.fs.exists(priorities_path):
             self.users = self.mapper["priorities"].decode().split("*")
 
             if self.user not in self.users:
```

### Comparing `lndb-0.39.2/lndb/dev/_settings_instance.py` & `lndb-0.40.0/lndb/dev/_settings_instance.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 import os
 import shutil
 from pathlib import Path
 from typing import Literal, Optional, Set, Tuple, Union
 
 import sqlalchemy as sa
 import sqlmodel as sqm
+from lndb_storage import UPath
 from pydantic import PostgresDsn
 from sqlalchemy.future import Engine
 
 from ._exclusion import empty_locker, get_locker
 from ._settings_save import save_instance_settings
 from ._settings_store import current_instance_settings_file, instance_settings_file
 from ._storage import Storage
-from ._upath_ext import UPath
 
 # leave commented out until we understand more how to deal with
 # migrations in redun
 # https://stackoverflow.com/questions/2614984/sqlite-sqlalchemy-how-to-enforce-foreign-keys
 # foreign key constraints for sqlite3
 # from sqlite3 import Connection as SQLite3Connection
 # from sqlalchemy import event
```

### Comparing `lndb-0.39.2/lndb/dev/_settings_load.py` & `lndb-0.40.0/lndb/dev/_settings_load.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/dev/_settings_save.py` & `lndb-0.40.0/lndb/dev/_settings_save.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/dev/_settings_user.py` & `lndb-0.40.0/lndb/dev/_settings_user.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/dev/_setup_knowledge.py` & `lndb-0.40.0/lndb/dev/_setup_knowledge.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/dev/_setup_schema.py` & `lndb-0.40.0/lndb/dev/_setup_schema.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/dev/_storage.py` & `lndb-0.40.0/lndb/dev/_storage.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 import os
 from pathlib import Path
 from typing import Literal, Optional, Union
 
 from appdirs import AppDirs
-
-from ._upath_ext import UPath
+from lndb_storage import UPath
 
 DIRS = AppDirs("lamindb", "laminlabs")
 
 
 class Storage:
     """Manage cloud or local storage."""
```

### Comparing `lndb-0.39.2/lndb/test/_migrations_e2e.py` & `lndb-0.40.0/lndb/test/_migrations_e2e.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/lndb/test/_migrations_unit.py` & `lndb-0.40.0/lndb/test/_migrations_unit.py`

 * *Files 11% similar despite different names*

```diff
@@ -3,87 +3,93 @@
 from pathlib import Path
 from subprocess import run
 
 import sqlalchemy as sa
 from alembic import command
 from alembic.autogenerate.api import AutogenContext
 from alembic.autogenerate.render import _render_cmd_body
+from lamin_logger import logger
 from pytest_alembic.config import Config
 from pytest_alembic.executor import CommandExecutor, ConnectionExecutor
 from pytest_alembic.plugin.error import AlembicTestFailure
 from pytest_alembic.runner import MigrationContext
 from sqlmodel import SQLModel
 
 from lndb._delete import delete
 from lndb._init_instance import init
+from lndb._migrate import generate_module_files, get_schema_package_info
 
 
-def get_migration_config(schema_package_loc, *, target_metadata=None, **kwargs):
+def get_migration_config(package_name: str, *, target_metadata=None, **kwargs):
+    schema_package_dir = str(get_schema_package_info(package_name)[0])
     if target_metadata is None:
         target_metadata = SQLModel.metadata
     target_metadata.naming_convention = {
         "ix": "ix_%(column_0_label)s",
         "uq": "uq_%(table_name)s_%(column_0_name)s",
         "ck": "ck_%(table_name)s_`%(constraint_name)s`",
         "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
         "pk": "pk_%(table_name)s",
     }
     raw_config = dict(
-        config_file_name=f"{schema_package_loc}/alembic.ini",
-        script_location=f"{schema_package_loc}/migrations",
+        config_file_name=f"{schema_package_dir}/alembic.ini",
+        script_location=f"{schema_package_dir}/migrations",
         target_metadata=target_metadata,
         **kwargs,
     )
     config = Config.from_raw_config(raw_config)
     return config
 
 
-def get_migration_context(schema_package, db, include_schemas=None):
+def get_migration_context(package_name: str, db: str, include_schemas=None):
     engine = sa.create_engine(db)
-    config = get_migration_config(schema_package, include_schemas=include_schemas)
+    config = get_migration_config(package_name, include_schemas=include_schemas)
     command_executor = CommandExecutor.from_config(config)
     command_executor.configure(connection=engine)
     migration_context = MigrationContext.from_config(
         config, command_executor, ConnectionExecutor(), engine
     )
     return migration_context
 
 
-def get_migration_id_from_scripts(schema_package):
-    config = get_migration_config(schema_package)
+def get_migration_id_from_scripts(package_name: str):
+    config = get_migration_config(package_name)
     output_buffer = io.StringIO()
+    schema_package_dir = str(get_schema_package_info(package_name)[0])
     # get the id of the latest migration script
-    if Path(f"./{schema_package}/migrations/versions").exists():
+    if Path(f"{schema_package_dir}/migrations/versions").exists():
         command.heads(config.make_alembic_config(stdout=output_buffer))
         output = output_buffer.getvalue()
         migration_id = output.split(" ")[0]
     else:  # there is no scripts directory
+        logger.warning(f"'{schema_package_dir}/migrations/versions' does not exist")
         migration_id = ""
     return migration_id
 
 
 def migration_id_is_consistent(package_name):
     # package_name is either a simple module (if schema is at the root)
     # or a relative path to the submodule that contains the schema,
     # e.g. ./lnhub_rest/schema
-    migration_id = get_migration_id_from_scripts(package_name)
+    migration_id_from_scripts = get_migration_id_from_scripts(package_name)
     if package_name.startswith("./"):
         _, root, relative = package_name.split("/")
         assert relative == "schema"
         package = importlib.import_module(f".{relative}", package=root.lstrip("./"))
     else:
         package = importlib.import_module(package_name)
     if package._migration is None:
-        manual_migration_id = ""
+        migration_id_from_import = ""
     else:
-        manual_migration_id = package._migration
-    return manual_migration_id == migration_id
+        migration_id_from_import = package._migration
+    return migration_id_from_import == migration_id_from_scripts
 
 
-def model_definitions_match_ddl(schema_package, db=None, dialect_name="sqlite"):
+def model_definitions_match_ddl(package_name, db=None, dialect_name="sqlite"):
+    generate_module_files(package_name)
     if db is None and dialect_name == "sqlite":
         db = "sqlite:///testdb/testdb.lndb"
         # need to call init to reload schema
         init(storage="testdb", _migrate=False)
     elif db is None and dialect_name == "postgresql":
         # requires postgres has been set up through _nox_tools
         db = "postgresql://postgres:pwd@0.0.0.0:5432/pgtest"
@@ -94,15 +100,15 @@
             "Only sqlite and postgres test databases are implemented."
         )
     # the below is for debugging purposes, something with indexes doesn't work 100%
     # e = sa.create_engine(db)
     # print(sa.inspect(e).get_indexes("core.dobject"))
     include_schemas = True if dialect_name == "postgresql" else False
     migration_context = get_migration_context(
-        schema_package, db, include_schemas=include_schemas
+        package_name, db, include_schemas=include_schemas
     )
     execute_model_definitions_match_ddl(migration_context)
     if dialect_name == "postgresql":
         run("docker stop pgtest && docker rm pgtest", shell=True)
         delete("pgtest")
     else:
         delete("testdb")
```

### Comparing `lndb-0.39.2/noxfile.py` & `lndb-0.40.0/noxfile.py`

 * *Files identical despite different names*

### Comparing `lndb-0.39.2/tests/test_init_instance.py` & `lndb-0.40.0/tests/test_init_instance.py`

 * *Files identical despite different names*

