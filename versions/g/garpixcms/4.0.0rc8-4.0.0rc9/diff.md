# Comparing `tmp/garpixcms-4.0.0rc8.tar.gz` & `tmp/garpixcms-4.0.0rc9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "garpixcms-4.0.0rc8.tar", last modified: Fri Mar 24 12:22:56 2023, max compression
+gzip compressed data, was "garpixcms-4.0.0rc9.tar", last modified: Fri Mar 24 12:30:41 2023, max compression
```

## Comparing `garpixcms-4.0.0rc8.tar` & `garpixcms-4.0.0rc9.tar`

### file list

```diff
@@ -1,109 +1,109 @@
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.610206 garpixcms-4.0.0rc8/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       30 2023-03-24 12:22:56.000000 garpixcms-4.0.0rc8/MANIFEST.in
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1769 2023-03-24 12:22:56.610075 garpixcms-4.0.0rc8/PKG-INFO
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.602867 garpixcms-4.0.0rc8/garpixcms/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)    12349 2023-03-24 12:22:17.000000 garpixcms-4.0.0rc8/garpixcms/CHANGELOG.md
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1084 2022-10-06 14:32:51.000000 garpixcms-4.0.0rc8/garpixcms/CONTRIBUTING.md
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       30 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/MANIFEST.in
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1207 2023-03-09 03:45:19.000000 garpixcms-4.0.0rc8/garpixcms/README.rst
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/__init__.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.603913 garpixcms-4.0.0rc8/garpixcms/__pycache__/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      161 2022-08-16 12:23:45.000000 garpixcms-4.0.0rc8/garpixcms/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      387 2022-10-07 14:06:21.000000 garpixcms-4.0.0rc8/garpixcms/__pycache__/apps.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     6796 2023-03-13 04:19:08.000000 garpixcms-4.0.0rc8/garpixcms/__pycache__/settings.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1743 2023-03-09 03:45:38.000000 garpixcms-4.0.0rc8/garpixcms/__pycache__/urls.cpython-38.pyc
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.604120 garpixcms-4.0.0rc8/garpixcms/admin/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       36 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/admin/__init__.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.604335 garpixcms-4.0.0rc8/garpixcms/admin/__pycache__/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      205 2022-08-16 12:23:55.000000 garpixcms-4.0.0rc8/garpixcms/admin/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      487 2022-08-16 12:23:55.000000 garpixcms-4.0.0rc8/garpixcms/admin/__pycache__/page.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      173 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/admin/page.py
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       93 2022-10-07 14:06:19.000000 garpixcms-4.0.0rc8/garpixcms/apps.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.604521 garpixcms-4.0.0rc8/garpixcms/contexts/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/contexts/__init__.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.604731 garpixcms-4.0.0rc8/garpixcms/contexts/__pycache__/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      170 2022-08-16 12:23:57.000000 garpixcms-4.0.0rc8/garpixcms/contexts/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      948 2023-02-10 12:24:11.000000 garpixcms-4.0.0rc8/garpixcms/contexts/__pycache__/global_context.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      691 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/contexts/global_context.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.604836 garpixcms-4.0.0rc8/garpixcms/management/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2023-03-09 03:45:19.000000 garpixcms-4.0.0rc8/garpixcms/management/__init__.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.604916 garpixcms-4.0.0rc8/garpixcms/management/__pycache__/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      172 2023-03-13 04:19:20.000000 garpixcms-4.0.0rc8/garpixcms/management/__pycache__/__init__.cpython-38.pyc
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.605101 garpixcms-4.0.0rc8/garpixcms/management/commands/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2023-03-09 03:45:19.000000 garpixcms-4.0.0rc8/garpixcms/management/commands/__init__.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.605309 garpixcms-4.0.0rc8/garpixcms/management/commands/__pycache__/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      181 2022-11-07 06:29:29.000000 garpixcms-4.0.0rc8/garpixcms/management/commands/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1217 2022-11-07 06:29:29.000000 garpixcms-4.0.0rc8/garpixcms/management/commands/__pycache__/update_user_module.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      872 2023-03-09 03:45:19.000000 garpixcms-4.0.0rc8/garpixcms/management/commands/update_user_module.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.605493 garpixcms-4.0.0rc8/garpixcms/middleware/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/middleware/__init__.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.605700 garpixcms-4.0.0rc8/garpixcms/middleware/__pycache__/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      172 2023-03-09 03:38:29.000000 garpixcms-4.0.0rc8/garpixcms/middleware/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2037 2023-03-09 03:38:29.000000 garpixcms-4.0.0rc8/garpixcms/middleware/__pycache__/locale.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2196 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/middleware/locale.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.605921 garpixcms-4.0.0rc8/garpixcms/models/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       31 2022-10-07 15:53:24.000000 garpixcms-4.0.0rc8/garpixcms/models/__init__.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.606135 garpixcms-4.0.0rc8/garpixcms/models/__pycache__/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      201 2022-10-07 15:53:42.000000 garpixcms-4.0.0rc8/garpixcms/models/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      818 2022-08-16 12:23:46.000000 garpixcms-4.0.0rc8/garpixcms/models/__pycache__/page.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      413 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/models/page.py
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     8440 2023-03-09 04:14:34.000000 garpixcms-4.0.0rc8/garpixcms/settings.py
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1709 2023-03-24 12:22:17.000000 garpixcms-4.0.0rc8/garpixcms/setup.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.601051 garpixcms-4.0.0rc8/garpixcms/static/
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.601225 garpixcms-4.0.0rc8/garpixcms/static/admin/
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.607562 garpixcms-4.0.0rc8/garpixcms/static/admin/css/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     8440 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/autocomplete.css
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)    22662 2023-03-09 10:18:42.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/base.css
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     6469 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/changelists.css
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      355 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/dashboard.css
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      423 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/fonts.css
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     8370 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/forms.css
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1185 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/login.css
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2505 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/nav_sidebar.css
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)    18344 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/responsive.css
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1741 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/responsive_rtl.css
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     3487 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/rtl.css
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      502 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/tabbed_translation_fields.css
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)    10010 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/css/widgets.css
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.608100 garpixcms-4.0.0rc8/garpixcms/static/admin/img/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      908 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/img/icon-addlink.svg
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      825 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/img/icon-changelink.svg
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      218 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/img/icon-custom-checked.svg
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      705 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/img/icon-deletelink.svg
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      930 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/img/search.svg
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.608203 garpixcms-4.0.0rc8/garpixcms/static/admin/js/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      291 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/static/admin/js/admin.js
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.601393 garpixcms-4.0.0rc8/garpixcms/templates/
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.608520 garpixcms-4.0.0rc8/garpixcms/templates/admin/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     4421 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/templates/admin/app_list.html
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     4395 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/templates/admin/base.html
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      809 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc8/garpixcms/templates/admin/base_site.html
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.608621 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      450 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/base.html
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.608939 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/include/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      730 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/include/footer.html
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      642 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/include/header.html
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      428 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/include/login.html
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.609155 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/menus/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      202 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/menus/footer_menu.html
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      369 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/menus/header_menu.html
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.609478 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/pages/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      139 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/pages/default.html
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      202 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/pages/home.html
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      346 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/pages/login.html
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.609703 garpixcms-4.0.0rc8/garpixcms/translation/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       49 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/translation/__init__.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.609925 garpixcms-4.0.0rc8/garpixcms/translation/__pycache__/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      224 2022-08-16 12:23:46.000000 garpixcms-4.0.0rc8/garpixcms/translation/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      502 2022-08-16 12:23:46.000000 garpixcms-4.0.0rc8/garpixcms/translation/__pycache__/page.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      189 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc8/garpixcms/translation/page.py
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1842 2023-03-09 03:45:19.000000 garpixcms-4.0.0rc8/garpixcms/urls.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:22:56.603488 garpixcms-4.0.0rc8/garpixcms.egg-info/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1769 2023-03-24 12:22:56.000000 garpixcms-4.0.0rc8/garpixcms.egg-info/PKG-INFO
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     3106 2023-03-24 12:22:56.000000 garpixcms-4.0.0rc8/garpixcms.egg-info/SOURCES.txt
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        1 2023-03-24 12:22:56.000000 garpixcms-4.0.0rc8/garpixcms.egg-info/dependency_links.txt
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        1 2023-03-24 12:22:56.000000 garpixcms-4.0.0rc8/garpixcms.egg-info/not-zip-safe
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      409 2023-03-24 12:22:56.000000 garpixcms-4.0.0rc8/garpixcms.egg-info/requires.txt
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       10 2023-03-24 12:22:56.000000 garpixcms-4.0.0rc8/garpixcms.egg-info/top_level.txt
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       38 2023-03-24 12:22:56.610242 garpixcms-4.0.0rc8/setup.cfg
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1709 2023-03-24 12:22:56.000000 garpixcms-4.0.0rc8/setup.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.339255 garpixcms-4.0.0rc9/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       30 2023-03-24 12:30:41.000000 garpixcms-4.0.0rc9/MANIFEST.in
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1769 2023-03-24 12:30:41.339075 garpixcms-4.0.0rc9/PKG-INFO
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.297014 garpixcms-4.0.0rc9/garpixcms/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)    12359 2023-03-24 12:30:31.000000 garpixcms-4.0.0rc9/garpixcms/CHANGELOG.md
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1084 2022-10-06 14:32:51.000000 garpixcms-4.0.0rc9/garpixcms/CONTRIBUTING.md
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       30 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/MANIFEST.in
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1207 2023-03-09 03:45:19.000000 garpixcms-4.0.0rc9/garpixcms/README.rst
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/__init__.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.303423 garpixcms-4.0.0rc9/garpixcms/__pycache__/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      161 2022-08-16 12:23:45.000000 garpixcms-4.0.0rc9/garpixcms/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      387 2022-10-07 14:06:21.000000 garpixcms-4.0.0rc9/garpixcms/__pycache__/apps.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     6796 2023-03-13 04:19:08.000000 garpixcms-4.0.0rc9/garpixcms/__pycache__/settings.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1743 2023-03-09 03:45:38.000000 garpixcms-4.0.0rc9/garpixcms/__pycache__/urls.cpython-38.pyc
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.303673 garpixcms-4.0.0rc9/garpixcms/admin/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       36 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/admin/__init__.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.303920 garpixcms-4.0.0rc9/garpixcms/admin/__pycache__/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      205 2022-08-16 12:23:55.000000 garpixcms-4.0.0rc9/garpixcms/admin/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      487 2022-08-16 12:23:55.000000 garpixcms-4.0.0rc9/garpixcms/admin/__pycache__/page.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      173 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/admin/page.py
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       93 2022-10-07 14:06:19.000000 garpixcms-4.0.0rc9/garpixcms/apps.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.306566 garpixcms-4.0.0rc9/garpixcms/contexts/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/contexts/__init__.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.307336 garpixcms-4.0.0rc9/garpixcms/contexts/__pycache__/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      170 2022-08-16 12:23:57.000000 garpixcms-4.0.0rc9/garpixcms/contexts/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      948 2023-02-10 12:24:11.000000 garpixcms-4.0.0rc9/garpixcms/contexts/__pycache__/global_context.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      691 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/contexts/global_context.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.307742 garpixcms-4.0.0rc9/garpixcms/management/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2023-03-09 03:45:19.000000 garpixcms-4.0.0rc9/garpixcms/management/__init__.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.307870 garpixcms-4.0.0rc9/garpixcms/management/__pycache__/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      172 2023-03-13 04:19:20.000000 garpixcms-4.0.0rc9/garpixcms/management/__pycache__/__init__.cpython-38.pyc
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.308176 garpixcms-4.0.0rc9/garpixcms/management/commands/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2023-03-09 03:45:19.000000 garpixcms-4.0.0rc9/garpixcms/management/commands/__init__.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.319476 garpixcms-4.0.0rc9/garpixcms/management/commands/__pycache__/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      181 2022-11-07 06:29:29.000000 garpixcms-4.0.0rc9/garpixcms/management/commands/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1217 2022-11-07 06:29:29.000000 garpixcms-4.0.0rc9/garpixcms/management/commands/__pycache__/update_user_module.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      872 2023-03-09 03:45:19.000000 garpixcms-4.0.0rc9/garpixcms/management/commands/update_user_module.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.321612 garpixcms-4.0.0rc9/garpixcms/middleware/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/middleware/__init__.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.322032 garpixcms-4.0.0rc9/garpixcms/middleware/__pycache__/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      172 2023-03-09 03:38:29.000000 garpixcms-4.0.0rc9/garpixcms/middleware/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2037 2023-03-09 03:38:29.000000 garpixcms-4.0.0rc9/garpixcms/middleware/__pycache__/locale.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2196 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/middleware/locale.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.322322 garpixcms-4.0.0rc9/garpixcms/models/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       31 2022-10-07 15:53:24.000000 garpixcms-4.0.0rc9/garpixcms/models/__init__.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.322760 garpixcms-4.0.0rc9/garpixcms/models/__pycache__/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      201 2022-10-07 15:53:42.000000 garpixcms-4.0.0rc9/garpixcms/models/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      818 2022-08-16 12:23:46.000000 garpixcms-4.0.0rc9/garpixcms/models/__pycache__/page.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      413 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/models/page.py
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     8440 2023-03-09 04:14:34.000000 garpixcms-4.0.0rc9/garpixcms/settings.py
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1709 2023-03-24 12:30:06.000000 garpixcms-4.0.0rc9/garpixcms/setup.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.289338 garpixcms-4.0.0rc9/garpixcms/static/
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.289539 garpixcms-4.0.0rc9/garpixcms/static/admin/
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.335081 garpixcms-4.0.0rc9/garpixcms/static/admin/css/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     8440 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/autocomplete.css
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)    22662 2023-03-09 10:18:42.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/base.css
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     6469 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/changelists.css
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      355 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/dashboard.css
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      423 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/fonts.css
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     8370 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/forms.css
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1185 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/login.css
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2505 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/nav_sidebar.css
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)    18344 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/responsive.css
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1741 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/responsive_rtl.css
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     3487 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/rtl.css
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      502 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/tabbed_translation_fields.css
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)    10010 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/css/widgets.css
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.336137 garpixcms-4.0.0rc9/garpixcms/static/admin/img/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      908 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/img/icon-addlink.svg
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      825 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/img/icon-changelink.svg
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      218 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/img/icon-custom-checked.svg
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      705 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/img/icon-deletelink.svg
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      930 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/img/search.svg
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.336270 garpixcms-4.0.0rc9/garpixcms/static/admin/js/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      291 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/static/admin/js/admin.js
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.289764 garpixcms-4.0.0rc9/garpixcms/templates/
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.336771 garpixcms-4.0.0rc9/garpixcms/templates/admin/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     4421 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/templates/admin/app_list.html
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     4395 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/templates/admin/base.html
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      809 2023-03-07 14:17:49.000000 garpixcms-4.0.0rc9/garpixcms/templates/admin/base_site.html
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.336910 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      450 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/base.html
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.337397 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/include/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      730 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/include/footer.html
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      642 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/include/header.html
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      428 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/include/login.html
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.337665 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/menus/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      202 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/menus/footer_menu.html
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      369 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/menus/header_menu.html
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.338305 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/pages/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      139 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/pages/default.html
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      202 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/pages/home.html
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      346 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/pages/login.html
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.338563 garpixcms-4.0.0rc9/garpixcms/translation/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       49 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/translation/__init__.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.338853 garpixcms-4.0.0rc9/garpixcms/translation/__pycache__/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      224 2022-08-16 12:23:46.000000 garpixcms-4.0.0rc9/garpixcms/translation/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      502 2022-08-16 12:23:46.000000 garpixcms-4.0.0rc9/garpixcms/translation/__pycache__/page.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      189 2022-06-29 08:47:07.000000 garpixcms-4.0.0rc9/garpixcms/translation/page.py
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1842 2023-03-09 03:45:19.000000 garpixcms-4.0.0rc9/garpixcms/urls.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-03-24 12:30:41.302852 garpixcms-4.0.0rc9/garpixcms.egg-info/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1769 2023-03-24 12:30:41.000000 garpixcms-4.0.0rc9/garpixcms.egg-info/PKG-INFO
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     3106 2023-03-24 12:30:41.000000 garpixcms-4.0.0rc9/garpixcms.egg-info/SOURCES.txt
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        1 2023-03-24 12:30:41.000000 garpixcms-4.0.0rc9/garpixcms.egg-info/dependency_links.txt
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        1 2023-03-24 12:30:41.000000 garpixcms-4.0.0rc9/garpixcms.egg-info/not-zip-safe
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      409 2023-03-24 12:30:41.000000 garpixcms-4.0.0rc9/garpixcms.egg-info/requires.txt
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       10 2023-03-24 12:30:41.000000 garpixcms-4.0.0rc9/garpixcms.egg-info/top_level.txt
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       38 2023-03-24 12:30:41.339300 garpixcms-4.0.0rc9/setup.cfg
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1709 2023-03-24 12:30:41.000000 garpixcms-4.0.0rc9/setup.py
```

### Comparing `garpixcms-4.0.0rc8/PKG-INFO` & `garpixcms-4.0.0rc9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: garpixcms
-Version: 4.0.0rc8
+Version: 4.0.0rc9
 Home-page: https://github.com/garpixcms/garpixcms
 Author: Garpix LTD
 Author-email: info@garpix.com
 License: MIT
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Web Environment
 Classifier: Intended Audience :: Developers
```

### Comparing `garpixcms-4.0.0rc8/garpixcms/CHANGELOG.md` & `garpixcms-4.0.0rc9/garpixcms/CHANGELOG.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
-### 4.0.0-rc8 (24.03.2023)
+### 4.0.0-rc8-4.0.0-rc9 (24.03.2023)
 
-- Upgrade `garpix_page` to version 2.45.0-rc2.
+- Upgrade `garpix_page` to version 2.45.0-rc3.
 
 ### 4.0.0-rc7 (24.03.2023)
 
 - Upgrade `garpix_page` to version 2.45.0-rc1.
 - Upgrade `garpix_menu` to version 1.15.0.
 - Upgrade `garpix_notify` to version 5.14.0.
```

### Comparing `garpixcms-4.0.0rc8/garpixcms/CONTRIBUTING.md` & `garpixcms-4.0.0rc9/garpixcms/CONTRIBUTING.md`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/README.rst` & `garpixcms-4.0.0rc9/garpixcms/README.rst`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/__pycache__/settings.cpython-38.pyc` & `garpixcms-4.0.0rc9/garpixcms/__pycache__/settings.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/__pycache__/urls.cpython-38.pyc` & `garpixcms-4.0.0rc9/garpixcms/__pycache__/urls.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/contexts/__pycache__/global_context.cpython-38.pyc` & `garpixcms-4.0.0rc9/garpixcms/contexts/__pycache__/global_context.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/contexts/global_context.py` & `garpixcms-4.0.0rc9/garpixcms/contexts/global_context.py`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/management/commands/__pycache__/update_user_module.cpython-38.pyc` & `garpixcms-4.0.0rc9/garpixcms/management/commands/__pycache__/update_user_module.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/management/commands/update_user_module.py` & `garpixcms-4.0.0rc9/garpixcms/management/commands/update_user_module.py`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/middleware/__pycache__/locale.cpython-38.pyc` & `garpixcms-4.0.0rc9/garpixcms/middleware/__pycache__/locale.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/middleware/locale.py` & `garpixcms-4.0.0rc9/garpixcms/middleware/locale.py`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/models/__pycache__/page.cpython-38.pyc` & `garpixcms-4.0.0rc9/garpixcms/models/__pycache__/page.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/settings.py` & `garpixcms-4.0.0rc9/garpixcms/settings.py`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/setup.py` & `garpixcms-4.0.0rc9/garpixcms/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 here = path.join(path.abspath(path.dirname(__file__)), 'garpixcms')
 
 with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
     long_description = f.read()
 
 setup(
     name='garpixcms',
-    version='4.0.0-rc8',
+    version='4.0.0-rc9',
     description='',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/garpixcms/garpixcms',
     author='Garpix LTD',
     author_email='info@garpix.com',
     license='MIT',
@@ -28,15 +28,15 @@
         'Programming Language :: Python :: 3.8',
     ],
     include_package_data=True,
     zip_safe=False,
     install_requires=[
         'Django >= 3.1, < 4',
         'garpix_utils == 1.8.0',
-        'garpix_page == 2.45.0-rc2',
+        'garpix_page == 2.45.0-rc3',
         'garpix_menu == 1.15.0',
         'eqator == 2.6.0',
         'garpix_auth == 2.3.0',
         'garpix_notify == 5.14.0',
         'garpix_user == 3.5.0-rc5',
         'garpix_package == 2.0.1',
         'psycopg2-binary >= 2.8.6',
```

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/css/autocomplete.css` & `garpixcms-4.0.0rc9/garpixcms/static/admin/css/autocomplete.css`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/css/base.css` & `garpixcms-4.0.0rc9/garpixcms/static/admin/css/base.css`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/css/changelists.css` & `garpixcms-4.0.0rc9/garpixcms/static/admin/css/changelists.css`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/css/forms.css` & `garpixcms-4.0.0rc9/garpixcms/static/admin/css/forms.css`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/css/login.css` & `garpixcms-4.0.0rc9/garpixcms/static/admin/css/login.css`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/css/nav_sidebar.css` & `garpixcms-4.0.0rc9/garpixcms/static/admin/css/nav_sidebar.css`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/css/responsive.css` & `garpixcms-4.0.0rc9/garpixcms/static/admin/css/responsive.css`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/css/responsive_rtl.css` & `garpixcms-4.0.0rc9/garpixcms/static/admin/css/responsive_rtl.css`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/css/rtl.css` & `garpixcms-4.0.0rc9/garpixcms/static/admin/css/rtl.css`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/css/widgets.css` & `garpixcms-4.0.0rc9/garpixcms/static/admin/css/widgets.css`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/img/icon-addlink.svg` & `garpixcms-4.0.0rc9/garpixcms/static/admin/img/icon-addlink.svg`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/img/icon-changelink.svg` & `garpixcms-4.0.0rc9/garpixcms/static/admin/img/icon-changelink.svg`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/img/icon-deletelink.svg` & `garpixcms-4.0.0rc9/garpixcms/static/admin/img/icon-deletelink.svg`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/static/admin/img/search.svg` & `garpixcms-4.0.0rc9/garpixcms/static/admin/img/search.svg`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/templates/admin/app_list.html` & `garpixcms-4.0.0rc9/garpixcms/templates/admin/app_list.html`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/templates/admin/base.html` & `garpixcms-4.0.0rc9/garpixcms/templates/admin/base.html`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/templates/admin/base_site.html` & `garpixcms-4.0.0rc9/garpixcms/templates/admin/base_site.html`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/include/footer.html` & `garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/include/footer.html`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/templates/garpixcms/include/header.html` & `garpixcms-4.0.0rc9/garpixcms/templates/garpixcms/include/header.html`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms/urls.py` & `garpixcms-4.0.0rc9/garpixcms/urls.py`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/garpixcms.egg-info/PKG-INFO` & `garpixcms-4.0.0rc9/garpixcms.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: garpixcms
-Version: 4.0.0rc8
+Version: 4.0.0rc9
 Home-page: https://github.com/garpixcms/garpixcms
 Author: Garpix LTD
 Author-email: info@garpix.com
 License: MIT
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Web Environment
 Classifier: Intended Audience :: Developers
```

### Comparing `garpixcms-4.0.0rc8/garpixcms.egg-info/SOURCES.txt` & `garpixcms-4.0.0rc9/garpixcms.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `garpixcms-4.0.0rc8/setup.py` & `garpixcms-4.0.0rc9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 here = path.join(path.abspath(path.dirname(__file__)), 'garpixcms')
 
 with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
     long_description = f.read()
 
 setup(
     name='garpixcms',
-    version='4.0.0-rc8',
+    version='4.0.0-rc9',
     description='',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/garpixcms/garpixcms',
     author='Garpix LTD',
     author_email='info@garpix.com',
     license='MIT',
@@ -28,15 +28,15 @@
         'Programming Language :: Python :: 3.8',
     ],
     include_package_data=True,
     zip_safe=False,
     install_requires=[
         'Django >= 3.1, < 4',
         'garpix_utils == 1.8.0',
-        'garpix_page == 2.45.0-rc2',
+        'garpix_page == 2.45.0-rc3',
         'garpix_menu == 1.15.0',
         'eqator == 2.6.0',
         'garpix_auth == 2.3.0',
         'garpix_notify == 5.14.0',
         'garpix_user == 3.5.0-rc5',
         'garpix_package == 2.0.1',
         'psycopg2-binary >= 2.8.6',
```

