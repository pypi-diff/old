# Comparing `tmp/jnt-django-admin-tools-0.9.8.tar.gz` & `tmp/jnt-django-admin-tools-0.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "jnt-django-admin-tools-0.9.8.tar", last modified: Fri Jul  3 08:06:43 2020, max compression
+gzip compressed data, was "jnt-django-admin-tools-0.9.9.tar", last modified: Mon Aug 17 12:17:54 2020, max compression
```

## Comparing `jnt-django-admin-tools-0.9.8.tar` & `jnt-django-admin-tools-0.9.9.tar`

### file list

```diff
@@ -1,190 +1,190 @@
--rw-r--r--   0        0        0     1325 2020-07-03 08:05:46.096700 jnt-django-admin-tools-0.9.8/pyproject.toml
--rw-r--r--   0        0        0       61 2020-06-09 13:10:23.844943 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/__init__.py
--rw-r--r--   0        0        0      742 2020-06-09 13:10:23.845181 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/admin.py
--rw-r--r--   0        0        0      227 2020-06-09 13:10:23.845409 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/apps.py
--rw-r--r--   0        0        0     3772 2020-06-22 13:32:33.687132 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/autocomplete_filter.py
--rw-r--r--   0        0        0      629 2020-06-09 13:10:23.845899 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/checks.py
--rw-r--r--   0        0        0      100 2020-06-09 13:10:23.846175 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/__init__.py
--rw-r--r--   0        0        0      109 2020-06-09 13:10:23.846408 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/apps.py
--rw-r--r--   0        0        0     9007 2020-06-22 14:36:33.043531 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/dashboards.py
--rw-r--r--   0        0        0      908 2020-06-09 13:10:23.847174 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/forms.py
--rw-r--r--   0        0        0        0 2020-06-09 13:10:23.847336 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/management/__init__.py
--rw-r--r--   0        0        0        0 2020-06-09 13:10:23.847553 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/management/commands/__init__.py
--rw-r--r--   0        0        0      293 2020-06-09 13:10:23.847852 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/management/commands/clear_dashboard_preferences.py
--rw-r--r--   0        0        0      960 2020-06-09 13:10:23.848104 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/management/commands/customdashboard.py
--rw-r--r--   0        0        0     1079 2020-06-09 13:10:23.848449 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/migrations/0001_initial.py
--rw-r--r--   0        0        0       25 2020-06-09 13:10:23.848780 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/migrations/__init__.py
--rw-r--r--   0        0        0     2985 2020-06-09 13:10:23.849300 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/models.py
--rw-r--r--   0        0        0    26124 2020-06-09 13:10:23.849906 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/modules.py
--rw-r--r--   0        0        0     1909 2020-06-09 13:10:23.850386 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/registry.py
--rw-r--r--   0        0        0      457 2020-06-09 13:10:23.850981 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/dashboard-ie.css
--rw-r--r--   0        0        0     5031 2020-06-09 13:10:23.851243 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/dashboard.css
--rw-r--r--   0        0        0     1738 2020-06-09 13:10:23.851756 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/animated-overlay.gif
--rw-r--r--   0        0        0      212 2020-06-09 13:10:23.852208 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_flat_0_aaaaaa_40x100.png
--rw-r--r--   0        0        0      208 2020-06-09 13:10:23.852569 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_flat_75_ffffff_40x100.png
--rw-r--r--   0        0        0      335 2020-06-09 13:10:23.852890 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_glass_55_fbf9ee_1x400.png
--rw-r--r--   0        0        0      207 2020-06-09 13:10:23.853224 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_glass_65_ffffff_1x400.png
--rw-r--r--   0        0        0      262 2020-06-09 13:10:23.853522 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_glass_75_dadada_1x400.png
--rw-r--r--   0        0        0      262 2020-06-09 13:10:23.853814 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_glass_75_e6e6e6_1x400.png
--rw-r--r--   0        0        0      332 2020-06-09 13:10:23.854250 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_glass_95_fef1ec_1x400.png
--rw-r--r--   0        0        0      280 2020-06-09 13:10:23.854635 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_highlight-soft_75_cccccc_1x100.png
--rw-r--r--   0        0        0     6922 2020-06-09 13:10:23.855014 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_222222_256x240.png
--rw-r--r--   0        0        0     4549 2020-06-09 13:10:23.855301 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_2e83ff_256x240.png
--rw-r--r--   0        0        0     6992 2020-06-09 13:10:23.855559 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_454545_256x240.png
--rw-r--r--   0        0        0     6999 2020-06-09 13:10:23.855854 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_888888_256x240.png
--rw-r--r--   0        0        0     4549 2020-06-09 13:10:23.856216 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_cd0a0a_256x240.png
--rw-r--r--   0        0        0    31890 2020-06-09 13:10:23.856715 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/jquery-ui.css
--rw-r--r--   0        0        0      495 2020-06-09 13:10:23.857239 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/dashboard.js
--rw-r--r--   0        0        0   228147 2020-06-09 13:10:23.859367 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/jquery/jquery-ui.min.js
--rw-r--r--   0        0        0     1043 2020-06-09 13:10:23.859845 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/jquery/jquery.cookie.min.js
--rw-r--r--   0        0        0    13093 2020-06-09 13:10:23.860274 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/jquery/jquery.dashboard.js
--rw-r--r--   0        0        0      323 2020-06-09 13:10:23.860869 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/admin/app_index.html
--rw-r--r--   0        0        0      446 2020-06-09 13:10:23.861230 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/admin/index.html
--rw-r--r--   0        0        0      615 2020-06-22 14:36:33.043928 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/css.html
--rw-r--r--   0        0        0     2695 2020-06-23 05:50:35.375410 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dashboard.html
--rw-r--r--   0        0        0     3810 2020-06-09 13:10:23.862495 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dashboard.txt
--rw-r--r--   0        0        0     1131 2020-06-09 13:10:23.862827 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dashboard_app_index.txt
--rw-r--r--   0        0        0       23 2020-06-09 13:10:23.863116 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dummy.html
--rw-r--r--   0        0        0      850 2020-06-09 13:10:23.863405 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/module.html
--rw-r--r--   0        0        0     1046 2020-06-22 14:36:33.044571 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/app_list.html
--rw-r--r--   0        0        0      524 2020-06-22 14:36:33.044872 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/feed.html
--rw-r--r--   0        0        0      998 2020-06-22 14:36:33.045277 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/group.html
--rw-r--r--   0        0        0      347 2020-06-22 14:36:33.045598 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/link_list.html
--rw-r--r--   0        0        0      911 2020-06-22 14:36:33.045915 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/model_list.html
--rw-r--r--   0        0        0      856 2020-06-22 14:36:33.046260 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/recent_actions.html
--rw-r--r--   0        0        0      183 2020-06-09 13:10:23.866172 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/preferences_form.html
--rw-r--r--   0        0        0        0 2020-06-09 13:10:23.866407 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templatetags/__init__.py
--rw-r--r--   0        0        0     4126 2020-07-03 08:05:35.871804 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templatetags/admin_tools_dashboard_tags.py
--rw-r--r--   0        0        0     1322 2020-06-09 13:10:23.867279 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/tests.py
--rw-r--r--   0        0        0      249 2020-06-09 13:10:23.867633 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/urls.py
--rw-r--r--   0        0        0     3138 2020-06-09 13:10:23.868289 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/utils.py
--rw-r--r--   0        0        0     1439 2020-06-09 13:10:23.868831 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/views.py
--rw-r--r--   0        0        0       51 2020-06-09 13:10:23.869300 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/db/fields/__init__.py
--rw-r--r--   0        0        0      933 2020-06-09 13:10:23.869697 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/db/fields/generic_foreign_key.py
--rw-r--r--   0        0        0     5061 2020-06-09 13:14:47.340408 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/decorators.py
--rw-r--r--   0        0        0      551 2020-06-09 13:10:23.870506 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/deprecate_utils.py
--rw-r--r--   0        0        0       55 2020-06-09 13:10:23.870954 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/fields/__init__.py
--rw-r--r--   0        0        0      997 2020-06-09 13:10:23.871296 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/fields/permissions.py
--rw-r--r--   0        0        0      378 2020-06-09 13:10:23.871851 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ar/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     2902 2020-06-09 13:10:23.872162 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ar/LC_MESSAGES/django.po
--rw-r--r--   0        0        0      378 2020-06-09 13:10:23.872803 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/bg/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     2902 2020-06-09 13:10:23.873165 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/bg/LC_MESSAGES/django.po
--rw-r--r--   0        0        0      378 2020-06-09 13:10:23.873741 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/bn/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     2926 2020-06-23 05:50:35.376339 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/bn/LC_MESSAGES/django.po
--rw-r--r--   0        0        0      378 2020-06-09 13:10:23.874653 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ca/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     2926 2020-06-23 05:50:35.376699 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ca/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1731 2020-06-09 13:10:23.875705 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/cs/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3294 2020-06-23 05:50:35.377120 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/cs/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1729 2020-06-09 13:10:23.876772 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/da/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3368 2020-06-23 05:50:35.377684 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/da/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1623 2020-06-09 13:10:23.877749 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/de/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3243 2020-06-09 13:10:23.878119 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/de/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1933 2020-06-09 13:10:23.878698 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/el/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3553 2020-06-09 13:10:23.879063 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/el/LC_MESSAGES/django.po
--rw-r--r--   0        0        0      422 2020-06-09 13:10:23.879536 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/en/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     2902 2020-06-09 13:10:23.879771 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/en/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1802 2020-06-09 13:10:23.880130 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/es/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3406 2020-06-09 13:10:23.880422 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/es/LC_MESSAGES/django.po
--rw-r--r--   0        0        0      378 2020-06-09 13:10:23.880951 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/es_AR/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     2902 2020-06-09 13:10:23.881335 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/es_AR/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1847 2020-06-09 13:10:23.881790 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/fi/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3398 2020-06-09 13:10:23.882129 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/fi/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1782 2020-06-09 13:10:23.882737 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/fr/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3421 2020-06-09 13:10:23.883111 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/fr/LC_MESSAGES/django.po
--rw-r--r--   0        0        0      378 2020-06-09 13:10:23.883717 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/he/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     2906 2020-06-23 05:50:35.378153 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/he/LC_MESSAGES/django.po
--rw-r--r--   0        0        0      378 2020-06-09 13:10:23.884862 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/hu/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     2902 2020-06-09 13:10:23.885296 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/hu/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1587 2020-06-09 13:10:23.885942 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/it/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3257 2020-06-09 13:10:23.886311 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/it/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1911 2020-06-09 13:10:23.886927 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ja/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3530 2020-06-09 13:10:23.887257 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ja/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1728 2020-06-09 13:10:23.887754 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/nl/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3331 2020-06-09 13:10:23.888030 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/nl/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1711 2020-06-09 13:10:23.888413 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/pl/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3300 2020-06-23 05:50:35.378579 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/pl/LC_MESSAGES/django.po
--rw-r--r--   0        0        0      378 2020-06-09 13:10:23.889216 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/pt/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     2926 2020-06-23 05:50:35.378946 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/pt/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1734 2020-06-09 13:10:23.890059 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/pt_BR/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3371 2020-06-09 13:10:23.890305 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/pt_BR/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     2124 2020-06-09 13:10:23.890673 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ru/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3694 2020-06-23 05:50:35.379453 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ru/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1670 2020-06-09 13:10:23.891317 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/sk/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3285 2020-06-09 13:10:23.891575 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/sk/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1794 2020-06-09 13:10:23.892044 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/sv/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3276 2020-06-09 13:10:23.892364 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/sv/LC_MESSAGES/django.po
--rw-r--r--   0        0        0      378 2020-06-09 13:10:23.892829 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/tr/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     2902 2020-06-09 13:10:23.893076 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/tr/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     2032 2020-06-09 13:10:23.893505 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/uk/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3794 2020-06-09 13:10:23.893895 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/uk/LC_MESSAGES/django.po
--rw-r--r--   0        0        0     1647 2020-06-09 13:10:23.894629 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/zh_CN/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     3240 2020-06-09 13:10:23.895021 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/zh_CN/LC_MESSAGES/django.po
--rw-r--r--   0        0        0      686 2020-06-09 13:10:23.895607 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/zh_TW/LC_MESSAGES/django.mo
--rw-r--r--   0        0        0     2967 2020-06-09 13:10:23.895990 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/zh_TW/LC_MESSAGES/django.po
--rw-r--r--   0        0        0       41 2020-06-09 13:10:23.896492 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/__init__.py
--rw-r--r--   0        0        0      115 2020-06-09 13:10:23.896855 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/apps.py
--rw-r--r--   0        0        0      821 2020-06-09 13:10:23.897348 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/forms.py
--rw-r--r--   0        0        0    12511 2020-06-09 13:10:23.897899 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/items.py
--rw-r--r--   0        0        0        0 2020-06-09 13:10:23.898173 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/management/__init__.py
--rw-r--r--   0        0        0        0 2020-06-09 13:10:23.898456 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/management/commands/__init__.py
--rw-r--r--   0        0        0      936 2020-06-09 13:10:23.898778 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/management/commands/custommenu.py
--rw-r--r--   0        0        0     3634 2020-06-09 13:10:23.899082 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/menus.py
--rw-r--r--   0        0        0      910 2020-06-09 13:10:23.899380 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/migrations/0001_initial.py
--rw-r--r--   0        0        0       25 2020-06-09 13:10:23.899585 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/migrations/__init__.py
--rw-r--r--   0        0        0     1682 2020-06-09 13:10:23.899833 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/models.py
--rw-r--r--   0        0        0      299 2020-06-22 14:36:33.046988 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/static/jnt_admin_tools/css/menu-ie.css
--rw-r--r--   0        0        0     3413 2020-06-22 14:36:33.047387 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/static/jnt_admin_tools/css/menu.css
--rw-r--r--   0        0        0     2154 2020-06-22 14:36:33.047995 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/static/jnt_admin_tools/js/menu.js
--rw-r--r--   0        0        0      406 2020-06-09 13:10:23.901456 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/admin/base_site.html
--rw-r--r--   0        0        0      472 2020-06-22 14:36:33.048667 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/add_bookmark_form.html
--rw-r--r--   0        0        0      473 2020-06-22 14:36:33.048934 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/css.html
--rw-r--r--   0        0        0      269 2020-06-22 14:36:33.049465 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/delete_confirm.html
--rw-r--r--   0        0        0       23 2020-06-22 14:36:33.049843 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/dummy.html
--rw-r--r--   0        0        0      183 2020-06-22 14:36:33.050212 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/form.html
--rw-r--r--   0        0        0      845 2020-06-22 14:36:33.050583 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/item.html
--rw-r--r--   0        0        0     1909 2020-06-23 05:50:35.379878 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/menu.html
--rw-r--r--   0        0        0     1240 2020-06-22 14:36:33.051365 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/menu.txt
--rw-r--r--   0        0        0      350 2020-06-22 14:36:33.051757 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/remove_bookmark_form.html
--rw-r--r--   0        0        0        0 2020-06-09 13:10:23.904150 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templatetags/__init__.py
--rw-r--r--   0        0        0     2886 2020-06-09 13:10:23.904481 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templatetags/admin_tools_menu_tags.py
--rw-r--r--   0        0        0     2205 2020-06-09 13:10:23.904773 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/tests.py
--rw-r--r--   0        0        0      479 2020-06-09 13:10:23.905029 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/urls.py
--rw-r--r--   0        0        0     1378 2020-06-09 13:10:23.905301 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/utils.py
--rw-r--r--   0        0        0     3263 2020-06-09 13:10:23.905760 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/views.py
--rw-r--r--   0        0        0     8725 2020-06-09 13:10:23.906237 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/mixins.py
--rw-r--r--   0        0        0        0 2020-06-09 13:10:23.906525 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/services/__init__.py
--rw-r--r--   0        0        0      267 2020-06-09 13:10:23.907005 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/services/objects.py
--rw-r--r--   0        0        0      672 2020-06-09 13:10:23.907412 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/services/urls.py
--rw-r--r--   0        0        0        0 2020-06-22 14:36:33.052036 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/css/__init__.py
--rw-r--r--   0        0        0       66 2020-06-22 14:36:33.052536 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/css/autocomplete_filter/autocomplete_fix.css
--rw-r--r--   0        0        0        0 2020-06-22 14:36:33.052667 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/css/widgets/__init__.py
--rw-r--r--   0        0        0      152 2020-06-22 14:36:33.053289 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/css/widgets/permissions.css
--rw-r--r--   0        0        0     7013 2020-06-22 14:36:33.053974 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/images/admin-tools.png
--rw-r--r--   0        0        0     2316 2020-06-22 14:36:33.054589 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/js/autocomplete_filter/autocomplete_filter_qs.js
--rw-r--r--   0        0        0     3390 2020-06-22 14:36:33.055008 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/js/json.min.js
--rw-r--r--   0        0        0     1203 2020-06-22 14:36:33.055418 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/js/utils.js
--rw-r--r--   0        0        0        0 2020-06-22 14:36:33.055589 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/js/widgets/__init__.py
--rw-r--r--   0        0        0     6961 2020-06-22 14:36:33.055861 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/js/widgets/generic-foreign-key-field.js
--rw-r--r--   0        0        0     2172 2020-06-09 13:10:23.912327 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/template_loaders.py
--rw-r--r--   0        0        0        0 2020-06-09 13:10:23.912560 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/templates/__init__.py
--rw-r--r--   0        0        0        0 2020-06-22 14:36:33.056070 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/templates/jnt_admin_tools/__init__.py
--rw-r--r--   0        0        0      259 2020-06-22 14:36:33.056344 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/templates/jnt_admin_tools/autocomplete_filter/autocomplete_filter.html
--rw-r--r--   0        0        0     2805 2020-06-22 14:36:33.056747 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/templates/jnt_admin_tools/widgets/permissions.html
--rw-r--r--   0        0        0        0 2020-06-09 13:10:23.914692 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/templatetags/__init__.py
--rw-r--r--   0        0        0      258 2020-06-09 13:10:23.915201 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/templatetags/permissions_widget_tags.py
--rw-r--r--   0        0        0     2909 2020-06-09 13:10:23.915618 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/tests.py
--rw-r--r--   0        0        0        0 2020-06-09 13:10:23.916388 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/theming/__init__.py
--rw-r--r--   0        0        0      122 2020-06-09 13:10:23.916885 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/theming/apps.py
--rw-r--r--   0        0        0      860 2020-06-09 13:10:23.917899 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/theming/static/jnt_admin_tools/css/theming.css
--rw-r--r--   0        0        0     2947 2020-06-09 13:10:23.918365 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/theming/static/jnt_admin_tools/images/django.png
--rw-r--r--   0        0        0      237 2020-06-09 13:10:23.919178 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/theming/templates/admin/base.html
--rw-r--r--   0        0        0        0 2020-06-09 13:10:23.919955 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/theming/templatetags/__init__.py
--rw-r--r--   0        0        0      747 2020-06-09 13:10:23.920576 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/theming/templatetags/theming_tags.py
--rw-r--r--   0        0        0      436 2020-06-09 13:10:23.921084 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/urls.py
--rw-r--r--   0        0        0     5650 2020-06-09 13:10:23.921818 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/utils.py
--rw-r--r--   0        0        0     1726 2020-06-09 13:10:23.922458 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/views.py
--rw-r--r--   0        0        0       56 2020-06-09 13:10:23.923438 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/widgets/__init__.py
--rw-r--r--   0        0        0     1302 2020-06-09 13:10:23.924158 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/widgets/autocomplete.py
--rw-r--r--   0        0        0     3404 2020-06-09 13:10:23.924806 jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/widgets/permissions.py
--rw-r--r--   0        0        0     4228 2020-07-03 08:06:44.001077 jnt-django-admin-tools-0.9.8/setup.py
--rw-r--r--   0        0        0      808 2020-07-03 08:06:44.001526 jnt-django-admin-tools-0.9.8/PKG-INFO
+-rw-r--r--   0        0        0     1325 2020-08-17 12:17:44.499011 jnt-django-admin-tools-0.9.9/pyproject.toml
+-rw-r--r--   0        0        0       61 2020-06-09 13:10:23.844943 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/__init__.py
+-rw-r--r--   0        0        0      742 2020-06-09 13:10:23.845181 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/admin.py
+-rw-r--r--   0        0        0      227 2020-06-09 13:10:23.845409 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/apps.py
+-rw-r--r--   0        0        0     3772 2020-06-22 13:32:33.687132 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/autocomplete_filter.py
+-rw-r--r--   0        0        0      629 2020-06-09 13:10:23.845899 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/checks.py
+-rw-r--r--   0        0        0      100 2020-06-09 13:10:23.846175 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/__init__.py
+-rw-r--r--   0        0        0      109 2020-06-09 13:10:23.846408 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/apps.py
+-rw-r--r--   0        0        0     9007 2020-06-22 14:36:33.043531 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/dashboards.py
+-rw-r--r--   0        0        0      908 2020-06-09 13:10:23.847174 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/forms.py
+-rw-r--r--   0        0        0        0 2020-06-09 13:10:23.847336 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/management/__init__.py
+-rw-r--r--   0        0        0        0 2020-06-09 13:10:23.847553 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/management/commands/__init__.py
+-rw-r--r--   0        0        0      293 2020-06-09 13:10:23.847852 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/management/commands/clear_dashboard_preferences.py
+-rw-r--r--   0        0        0      960 2020-06-09 13:10:23.848104 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/management/commands/customdashboard.py
+-rw-r--r--   0        0        0     1079 2020-06-09 13:10:23.848449 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/migrations/0001_initial.py
+-rw-r--r--   0        0        0       25 2020-06-09 13:10:23.848780 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/migrations/__init__.py
+-rw-r--r--   0        0        0     2985 2020-06-09 13:10:23.849300 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/models.py
+-rw-r--r--   0        0        0    26124 2020-06-09 13:10:23.849906 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/modules.py
+-rw-r--r--   0        0        0     1909 2020-06-09 13:10:23.850386 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/registry.py
+-rw-r--r--   0        0        0      457 2020-06-09 13:10:23.850981 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/dashboard-ie.css
+-rw-r--r--   0        0        0     5031 2020-06-09 13:10:23.851243 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/dashboard.css
+-rw-r--r--   0        0        0     1738 2020-06-09 13:10:23.851756 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/animated-overlay.gif
+-rw-r--r--   0        0        0      212 2020-06-09 13:10:23.852208 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_flat_0_aaaaaa_40x100.png
+-rw-r--r--   0        0        0      208 2020-06-09 13:10:23.852569 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_flat_75_ffffff_40x100.png
+-rw-r--r--   0        0        0      335 2020-06-09 13:10:23.852890 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_glass_55_fbf9ee_1x400.png
+-rw-r--r--   0        0        0      207 2020-06-09 13:10:23.853224 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_glass_65_ffffff_1x400.png
+-rw-r--r--   0        0        0      262 2020-06-09 13:10:23.853522 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_glass_75_dadada_1x400.png
+-rw-r--r--   0        0        0      262 2020-06-09 13:10:23.853814 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_glass_75_e6e6e6_1x400.png
+-rw-r--r--   0        0        0      332 2020-06-09 13:10:23.854250 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_glass_95_fef1ec_1x400.png
+-rw-r--r--   0        0        0      280 2020-06-09 13:10:23.854635 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-bg_highlight-soft_75_cccccc_1x100.png
+-rw-r--r--   0        0        0     6922 2020-06-09 13:10:23.855014 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_222222_256x240.png
+-rw-r--r--   0        0        0     4549 2020-06-09 13:10:23.855301 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_2e83ff_256x240.png
+-rw-r--r--   0        0        0     6992 2020-06-09 13:10:23.855559 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_454545_256x240.png
+-rw-r--r--   0        0        0     6999 2020-06-09 13:10:23.855854 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_888888_256x240.png
+-rw-r--r--   0        0        0     4549 2020-06-09 13:10:23.856216 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_cd0a0a_256x240.png
+-rw-r--r--   0        0        0    31890 2020-06-09 13:10:23.856715 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/jquery-ui.css
+-rw-r--r--   0        0        0      495 2020-06-09 13:10:23.857239 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/dashboard.js
+-rw-r--r--   0        0        0   228147 2020-06-09 13:10:23.859367 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/jquery/jquery-ui.min.js
+-rw-r--r--   0        0        0     1043 2020-06-09 13:10:23.859845 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/jquery/jquery.cookie.min.js
+-rw-r--r--   0        0        0    13093 2020-06-09 13:10:23.860274 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/jquery/jquery.dashboard.js
+-rw-r--r--   0        0        0      323 2020-06-09 13:10:23.860869 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/admin/app_index.html
+-rw-r--r--   0        0        0      446 2020-06-09 13:10:23.861230 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/admin/index.html
+-rw-r--r--   0        0        0      615 2020-06-22 14:36:33.043928 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/css.html
+-rw-r--r--   0        0        0     2695 2020-06-23 05:50:35.375410 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dashboard.html
+-rw-r--r--   0        0        0     3810 2020-06-09 13:10:23.862495 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dashboard.txt
+-rw-r--r--   0        0        0     1131 2020-06-09 13:10:23.862827 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dashboard_app_index.txt
+-rw-r--r--   0        0        0       23 2020-06-09 13:10:23.863116 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dummy.html
+-rw-r--r--   0        0        0      850 2020-06-09 13:10:23.863405 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/module.html
+-rw-r--r--   0        0        0     1046 2020-06-22 14:36:33.044571 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/app_list.html
+-rw-r--r--   0        0        0      524 2020-06-22 14:36:33.044872 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/feed.html
+-rw-r--r--   0        0        0      998 2020-06-22 14:36:33.045277 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/group.html
+-rw-r--r--   0        0        0      347 2020-06-22 14:36:33.045598 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/link_list.html
+-rw-r--r--   0        0        0      911 2020-06-22 14:36:33.045915 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/model_list.html
+-rw-r--r--   0        0        0      856 2020-06-22 14:36:33.046260 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/recent_actions.html
+-rw-r--r--   0        0        0      183 2020-06-09 13:10:23.866172 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/preferences_form.html
+-rw-r--r--   0        0        0        0 2020-06-09 13:10:23.866407 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templatetags/__init__.py
+-rw-r--r--   0        0        0     4126 2020-07-03 08:05:35.871804 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templatetags/admin_tools_dashboard_tags.py
+-rw-r--r--   0        0        0     1322 2020-06-09 13:10:23.867279 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/tests.py
+-rw-r--r--   0        0        0      249 2020-06-09 13:10:23.867633 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/urls.py
+-rw-r--r--   0        0        0     3138 2020-06-09 13:10:23.868289 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/utils.py
+-rw-r--r--   0        0        0     1439 2020-06-09 13:10:23.868831 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/views.py
+-rw-r--r--   0        0        0       51 2020-06-09 13:10:23.869300 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/db/fields/__init__.py
+-rw-r--r--   0        0        0      933 2020-06-09 13:10:23.869697 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/db/fields/generic_foreign_key.py
+-rw-r--r--   0        0        0     5061 2020-08-17 12:17:26.028445 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/decorators.py
+-rw-r--r--   0        0        0      551 2020-06-09 13:10:23.870506 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/deprecate_utils.py
+-rw-r--r--   0        0        0       55 2020-06-09 13:10:23.870954 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/fields/__init__.py
+-rw-r--r--   0        0        0      997 2020-06-09 13:10:23.871296 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/fields/permissions.py
+-rw-r--r--   0        0        0      378 2020-06-09 13:10:23.871851 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ar/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     2902 2020-06-09 13:10:23.872162 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ar/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0      378 2020-06-09 13:10:23.872803 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/bg/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     2902 2020-06-09 13:10:23.873165 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/bg/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0      378 2020-06-09 13:10:23.873741 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/bn/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     2926 2020-06-23 05:50:35.376339 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/bn/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0      378 2020-06-09 13:10:23.874653 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ca/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     2926 2020-06-23 05:50:35.376699 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ca/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1731 2020-06-09 13:10:23.875705 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/cs/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3294 2020-06-23 05:50:35.377120 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/cs/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1729 2020-06-09 13:10:23.876772 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/da/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3368 2020-06-23 05:50:35.377684 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/da/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1623 2020-06-09 13:10:23.877749 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/de/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3243 2020-06-09 13:10:23.878119 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/de/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1933 2020-06-09 13:10:23.878698 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/el/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3553 2020-06-09 13:10:23.879063 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/el/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0      422 2020-06-09 13:10:23.879536 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/en/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     2902 2020-06-09 13:10:23.879771 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/en/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1802 2020-06-09 13:10:23.880130 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/es/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3406 2020-06-09 13:10:23.880422 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/es/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0      378 2020-06-09 13:10:23.880951 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/es_AR/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     2902 2020-06-09 13:10:23.881335 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/es_AR/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1847 2020-06-09 13:10:23.881790 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/fi/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3398 2020-06-09 13:10:23.882129 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/fi/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1782 2020-06-09 13:10:23.882737 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/fr/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3421 2020-06-09 13:10:23.883111 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/fr/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0      378 2020-06-09 13:10:23.883717 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/he/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     2906 2020-06-23 05:50:35.378153 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/he/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0      378 2020-06-09 13:10:23.884862 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/hu/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     2902 2020-06-09 13:10:23.885296 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/hu/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1587 2020-06-09 13:10:23.885942 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/it/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3257 2020-06-09 13:10:23.886311 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/it/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1911 2020-06-09 13:10:23.886927 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ja/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3530 2020-06-09 13:10:23.887257 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ja/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1728 2020-06-09 13:10:23.887754 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/nl/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3331 2020-06-09 13:10:23.888030 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/nl/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1711 2020-06-09 13:10:23.888413 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/pl/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3300 2020-06-23 05:50:35.378579 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/pl/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0      378 2020-06-09 13:10:23.889216 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/pt/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     2926 2020-06-23 05:50:35.378946 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/pt/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1734 2020-06-09 13:10:23.890059 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/pt_BR/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3371 2020-06-09 13:10:23.890305 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/pt_BR/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     2124 2020-06-09 13:10:23.890673 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ru/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3694 2020-06-23 05:50:35.379453 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ru/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1670 2020-06-09 13:10:23.891317 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/sk/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3285 2020-06-09 13:10:23.891575 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/sk/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1794 2020-06-09 13:10:23.892044 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/sv/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3276 2020-06-09 13:10:23.892364 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/sv/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0      378 2020-06-09 13:10:23.892829 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/tr/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     2902 2020-06-09 13:10:23.893076 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/tr/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     2032 2020-06-09 13:10:23.893505 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/uk/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3794 2020-06-09 13:10:23.893895 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/uk/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0     1647 2020-06-09 13:10:23.894629 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/zh_CN/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     3240 2020-06-09 13:10:23.895021 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/zh_CN/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0      686 2020-06-09 13:10:23.895607 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/zh_TW/LC_MESSAGES/django.mo
+-rw-r--r--   0        0        0     2967 2020-06-09 13:10:23.895990 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/zh_TW/LC_MESSAGES/django.po
+-rw-r--r--   0        0        0       41 2020-06-09 13:10:23.896492 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/__init__.py
+-rw-r--r--   0        0        0      115 2020-06-09 13:10:23.896855 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/apps.py
+-rw-r--r--   0        0        0      821 2020-06-09 13:10:23.897348 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/forms.py
+-rw-r--r--   0        0        0    12511 2020-06-09 13:10:23.897899 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/items.py
+-rw-r--r--   0        0        0        0 2020-06-09 13:10:23.898173 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/management/__init__.py
+-rw-r--r--   0        0        0        0 2020-06-09 13:10:23.898456 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/management/commands/__init__.py
+-rw-r--r--   0        0        0      936 2020-06-09 13:10:23.898778 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/management/commands/custommenu.py
+-rw-r--r--   0        0        0     3634 2020-06-09 13:10:23.899082 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/menus.py
+-rw-r--r--   0        0        0      910 2020-06-09 13:10:23.899380 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/migrations/0001_initial.py
+-rw-r--r--   0        0        0       25 2020-06-09 13:10:23.899585 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/migrations/__init__.py
+-rw-r--r--   0        0        0     1682 2020-06-09 13:10:23.899833 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/models.py
+-rw-r--r--   0        0        0      299 2020-06-22 14:36:33.046988 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/static/jnt_admin_tools/css/menu-ie.css
+-rw-r--r--   0        0        0     3413 2020-06-22 14:36:33.047387 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/static/jnt_admin_tools/css/menu.css
+-rw-r--r--   0        0        0     2154 2020-06-22 14:36:33.047995 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/static/jnt_admin_tools/js/menu.js
+-rw-r--r--   0        0        0      406 2020-06-09 13:10:23.901456 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/admin/base_site.html
+-rw-r--r--   0        0        0      472 2020-06-22 14:36:33.048667 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/add_bookmark_form.html
+-rw-r--r--   0        0        0      473 2020-06-22 14:36:33.048934 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/css.html
+-rw-r--r--   0        0        0      269 2020-06-22 14:36:33.049465 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/delete_confirm.html
+-rw-r--r--   0        0        0       23 2020-06-22 14:36:33.049843 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/dummy.html
+-rw-r--r--   0        0        0      183 2020-06-22 14:36:33.050212 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/form.html
+-rw-r--r--   0        0        0      845 2020-06-22 14:36:33.050583 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/item.html
+-rw-r--r--   0        0        0     1909 2020-06-23 05:50:35.379878 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/menu.html
+-rw-r--r--   0        0        0     1240 2020-06-22 14:36:33.051365 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/menu.txt
+-rw-r--r--   0        0        0      350 2020-06-22 14:36:33.051757 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/remove_bookmark_form.html
+-rw-r--r--   0        0        0        0 2020-06-09 13:10:23.904150 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templatetags/__init__.py
+-rw-r--r--   0        0        0     2886 2020-06-09 13:10:23.904481 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templatetags/admin_tools_menu_tags.py
+-rw-r--r--   0        0        0     2205 2020-06-09 13:10:23.904773 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/tests.py
+-rw-r--r--   0        0        0      479 2020-06-09 13:10:23.905029 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/urls.py
+-rw-r--r--   0        0        0     1378 2020-06-09 13:10:23.905301 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/utils.py
+-rw-r--r--   0        0        0     3263 2020-06-09 13:10:23.905760 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/views.py
+-rw-r--r--   0        0        0     8725 2020-06-09 13:10:23.906237 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/mixins.py
+-rw-r--r--   0        0        0        0 2020-06-09 13:10:23.906525 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/services/__init__.py
+-rw-r--r--   0        0        0      267 2020-06-09 13:10:23.907005 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/services/objects.py
+-rw-r--r--   0        0        0      672 2020-06-09 13:10:23.907412 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/services/urls.py
+-rw-r--r--   0        0        0        0 2020-06-22 14:36:33.052036 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/css/__init__.py
+-rw-r--r--   0        0        0       66 2020-06-22 14:36:33.052536 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/css/autocomplete_filter/autocomplete_fix.css
+-rw-r--r--   0        0        0        0 2020-06-22 14:36:33.052667 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/css/widgets/__init__.py
+-rw-r--r--   0        0        0      152 2020-06-22 14:36:33.053289 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/css/widgets/permissions.css
+-rw-r--r--   0        0        0     7013 2020-06-22 14:36:33.053974 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/images/admin-tools.png
+-rw-r--r--   0        0        0     2316 2020-06-22 14:36:33.054589 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/js/autocomplete_filter/autocomplete_filter_qs.js
+-rw-r--r--   0        0        0     3390 2020-06-22 14:36:33.055008 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/js/json.min.js
+-rw-r--r--   0        0        0     1203 2020-06-22 14:36:33.055418 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/js/utils.js
+-rw-r--r--   0        0        0        0 2020-06-22 14:36:33.055589 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/js/widgets/__init__.py
+-rw-r--r--   0        0        0     6961 2020-06-22 14:36:33.055861 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/js/widgets/generic-foreign-key-field.js
+-rw-r--r--   0        0        0     2172 2020-06-09 13:10:23.912327 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/template_loaders.py
+-rw-r--r--   0        0        0        0 2020-06-09 13:10:23.912560 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/templates/__init__.py
+-rw-r--r--   0        0        0        0 2020-06-22 14:36:33.056070 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/templates/jnt_admin_tools/__init__.py
+-rw-r--r--   0        0        0      259 2020-06-22 14:36:33.056344 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/templates/jnt_admin_tools/autocomplete_filter/autocomplete_filter.html
+-rw-r--r--   0        0        0     2805 2020-06-22 14:36:33.056747 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/templates/jnt_admin_tools/widgets/permissions.html
+-rw-r--r--   0        0        0        0 2020-06-09 13:10:23.914692 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/templatetags/__init__.py
+-rw-r--r--   0        0        0      258 2020-06-09 13:10:23.915201 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/templatetags/permissions_widget_tags.py
+-rw-r--r--   0        0        0     2909 2020-06-09 13:10:23.915618 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/tests.py
+-rw-r--r--   0        0        0        0 2020-06-09 13:10:23.916388 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/theming/__init__.py
+-rw-r--r--   0        0        0      122 2020-06-09 13:10:23.916885 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/theming/apps.py
+-rw-r--r--   0        0        0      860 2020-06-09 13:10:23.917899 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/theming/static/jnt_admin_tools/css/theming.css
+-rw-r--r--   0        0        0     2947 2020-06-09 13:10:23.918365 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/theming/static/jnt_admin_tools/images/django.png
+-rw-r--r--   0        0        0      237 2020-06-09 13:10:23.919178 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/theming/templates/admin/base.html
+-rw-r--r--   0        0        0        0 2020-06-09 13:10:23.919955 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/theming/templatetags/__init__.py
+-rw-r--r--   0        0        0      747 2020-06-09 13:10:23.920576 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/theming/templatetags/theming_tags.py
+-rw-r--r--   0        0        0      436 2020-06-09 13:10:23.921084 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/urls.py
+-rw-r--r--   0        0        0     5650 2020-06-09 13:10:23.921818 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/utils.py
+-rw-r--r--   0        0        0     1726 2020-06-09 13:10:23.922458 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/views.py
+-rw-r--r--   0        0        0       56 2020-06-09 13:10:23.923438 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/widgets/__init__.py
+-rw-r--r--   0        0        0     1302 2020-06-09 13:10:23.924158 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/widgets/autocomplete.py
+-rw-r--r--   0        0        0     3404 2020-06-09 13:10:23.924806 jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/widgets/permissions.py
+-rw-r--r--   0        0        0     4228 2020-08-17 12:17:55.478917 jnt-django-admin-tools-0.9.9/setup.py
+-rw-r--r--   0        0        0      808 2020-08-17 12:17:55.479450 jnt-django-admin-tools-0.9.9/PKG-INFO
```

### Comparing `jnt-django-admin-tools-0.9.8/pyproject.toml` & `jnt-django-admin-tools-0.9.9/pyproject.toml`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "jnt-django-admin-tools"
-version = "0.9.8"
+version = "0.9.9"
 description="A collection of tools for the django administration interface"
 authors = ["Junte <tech@junte.ru>"]
 classifiers=[
         'Environment :: Web Environment',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
```

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/admin.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/admin.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/autocomplete_filter.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/autocomplete_filter.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/checks.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/checks.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/dashboards.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/dashboards.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/forms.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/forms.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/management/commands/customdashboard.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/management/commands/customdashboard.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/migrations/0001_initial.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/models.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/models.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/modules.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/modules.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/registry.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/registry.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/dashboard.css` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/dashboard.css`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/animated-overlay.gif` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/animated-overlay.gif`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_222222_256x240.png` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_222222_256x240.png`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_2e83ff_256x240.png` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_2e83ff_256x240.png`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_454545_256x240.png` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_454545_256x240.png`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_888888_256x240.png` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_888888_256x240.png`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_cd0a0a_256x240.png` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/images/ui-icons_cd0a0a_256x240.png`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/jquery-ui.css` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/css/jquery/jquery-ui.css`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/jquery/jquery-ui.min.js` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/jquery/jquery-ui.min.js`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/jquery/jquery.cookie.min.js` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/jquery/jquery.cookie.min.js`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/jquery/jquery.dashboard.js` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/static/jnt_admin_tools/js/jquery/jquery.dashboard.js`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/css.html` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/css.html`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dashboard.html` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dashboard.html`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dashboard.txt` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dashboard.txt`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dashboard_app_index.txt` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/dashboard_app_index.txt`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/module.html` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/module.html`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/app_list.html` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/app_list.html`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/feed.html` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/feed.html`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/group.html` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/group.html`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/model_list.html` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/model_list.html`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/recent_actions.html` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templates/jnt_admin_tools/dashboard/modules/recent_actions.html`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/templatetags/admin_tools_dashboard_tags.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/templatetags/admin_tools_dashboard_tags.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/tests.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/tests.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/utils.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/utils.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/dashboard/views.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/dashboard/views.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/db/fields/generic_foreign_key.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/db/fields/generic_foreign_key.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/decorators.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/decorators.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 from functools import reduce, wraps
 
+from django.forms.utils import pretty_name
 from jnt_admin_tools.services.urls import (
     admin_change_url,
     admin_changelist_url,
 )
-from django.forms.forms import pretty_name
 from django.utils.html import format_html
 
 
 def getattr_nested(obj, attr):
     return reduce(getattr, [obj] + attr.split("__"))
```

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/deprecate_utils.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/deprecate_utils.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/fields/permissions.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/fields/permissions.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ar/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ar/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/bg/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/bg/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/bn/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/bn/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ca/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ca/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/cs/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/cs/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/cs/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/cs/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/da/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/da/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/da/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/da/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/de/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/de/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/de/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/de/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/el/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/el/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/el/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/el/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/en/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/en/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/es/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/es/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/es/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/es/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/es_AR/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/es_AR/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/fi/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/fi/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/fi/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/fi/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/fr/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/fr/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/fr/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/fr/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/he/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/he/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/hu/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/hu/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/it/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/it/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/it/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/it/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ja/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ja/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ja/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ja/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/nl/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/nl/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/nl/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/nl/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/pl/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/pl/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/pl/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/pl/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/pt/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/pt/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/pt_BR/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/pt_BR/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/pt_BR/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/pt_BR/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ru/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ru/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/ru/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/ru/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/sk/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/sk/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/sk/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/sk/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/sv/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/sv/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/sv/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/sv/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/tr/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/tr/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/uk/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/uk/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/uk/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/uk/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/zh_CN/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/zh_CN/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/zh_CN/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/zh_CN/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/zh_TW/LC_MESSAGES/django.mo` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/zh_TW/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/locale/zh_TW/LC_MESSAGES/django.po` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/locale/zh_TW/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/forms.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/forms.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/items.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/items.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/management/commands/custommenu.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/management/commands/custommenu.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/menus.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/menus.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/migrations/0001_initial.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/models.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/models.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/static/jnt_admin_tools/css/menu.css` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/static/jnt_admin_tools/css/menu.css`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/static/jnt_admin_tools/js/menu.js` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/static/jnt_admin_tools/js/menu.js`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/item.html` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/item.html`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/menu.html` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/menu.html`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/menu.txt` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templates/jnt_admin_tools/menu/menu.txt`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/templatetags/admin_tools_menu_tags.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/templatetags/admin_tools_menu_tags.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/tests.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/tests.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/utils.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/utils.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/menu/views.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/menu/views.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/mixins.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/mixins.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/services/urls.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/services/urls.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/images/admin-tools.png` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/images/admin-tools.png`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/js/autocomplete_filter/autocomplete_filter_qs.js` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/js/autocomplete_filter/autocomplete_filter_qs.js`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/js/json.min.js` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/js/json.min.js`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/js/utils.js` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/js/utils.js`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/static/jnt_admin_tools/js/widgets/generic-foreign-key-field.js` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/static/jnt_admin_tools/js/widgets/generic-foreign-key-field.js`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/template_loaders.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/template_loaders.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/templates/jnt_admin_tools/widgets/permissions.html` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/templates/jnt_admin_tools/widgets/permissions.html`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/tests.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/tests.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/theming/static/jnt_admin_tools/css/theming.css` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/theming/static/jnt_admin_tools/css/theming.css`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/theming/static/jnt_admin_tools/images/django.png` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/theming/static/jnt_admin_tools/images/django.png`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/theming/templatetags/theming_tags.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/theming/templatetags/theming_tags.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/utils.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/utils.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/views.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/views.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/widgets/autocomplete.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/widgets/autocomplete.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/src/jnt_admin_tools/widgets/permissions.py` & `jnt-django-admin-tools-0.9.9/src/jnt_admin_tools/widgets/permissions.py`

 * *Files identical despite different names*

### Comparing `jnt-django-admin-tools-0.9.8/setup.py` & `jnt-django-admin-tools-0.9.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -82,15 +82,15 @@
                              'templates/admin/*']}
 
 install_requires = \
 ['django>=2']
 
 setup_kwargs = {
     'name': 'jnt-django-admin-tools',
-    'version': '0.9.8',
+    'version': '0.9.9',
     'description': 'A collection of tools for the django administration interface',
     'long_description': None,
     'author': 'Junte',
     'author_email': 'tech@junte.ru',
     'maintainer': None,
     'maintainer_email': None,
     'url': None,
```

### Comparing `jnt-django-admin-tools-0.9.8/PKG-INFO` & `jnt-django-admin-tools-0.9.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jnt-django-admin-tools
-Version: 0.9.8
+Version: 0.9.9
 Summary: A collection of tools for the django administration interface
 Author: Junte
 Author-email: tech@junte.ru
 Requires-Python: >=3.6,<4.0
 Classifier: Environment :: Web Environment
 Classifier: Framework :: Django :: 2.0
 Classifier: Framework :: Django :: 3.0
```

