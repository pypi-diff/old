# Comparing `tmp/django_rq_scheduler-2023.4.0.tar.gz` & `tmp/django_rq_scheduler-2023.5.0b1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django_rq_scheduler-2023.4.0.tar", max compression
+gzip compressed data, was "django_rq_scheduler-2023.5.0b1.tar", max compression
```

## Comparing `django_rq_scheduler-2023.4.0.tar` & `django_rq_scheduler-2023.5.0b1.tar`

### file list

```diff
@@ -1,37 +1,66 @@
--rw-r--r--   0        0        0     1096 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/LICENSE
--rw-r--r--   0        0        0     1711 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/README.md
--rw-r--r--   0        0        0     1712 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/pyproject.toml
--rw-r--r--   0        0        0      142 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/__init__.py
--rw-r--r--   0        0        0     5264 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/admin.py
--rw-r--r--   0        0        0      563 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/apps.py
--rw-r--r--   0        0        0     1580 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/management/commands/export.py
--rw-r--r--   0        0        0     3420 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/management/commands/import.py
--rw-r--r--   0        0        0     7162 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/migrations/0001_initial_squashed_0005_added_result_ttl.py
--rw-r--r--   0        0        0      898 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/migrations/0002_alter_cronjob_id_alter_repeatablejob_id_and_more.py
--rw-r--r--   0        0        0     4196 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/migrations/0003_auto_20220329_2107.py
--rw-r--r--   0        0        0      791 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/migrations/0004_cronjob_at_front_repeatablejob_at_front_and_more.py
--rw-r--r--   0        0        0      896 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/migrations/0005_alter_cronjob_at_front_alter_repeatablejob_at_front_and_more.py
--rw-r--r--   0        0        0     1051 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/migrations/0006_auto_20230118_1640.py
--rw-r--r--   0        0        0     1302 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/migrations/0007_add_result_ttl.py
--rw-r--r--   0        0        0     1982 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/migrations/0008_rename_str_val_jobarg_val_and_more.py
--rw-r--r--   0        0        0     1279 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/migrations/0009_alter_jobarg_arg_type_alter_jobarg_val_and_more.py
--rw-r--r--   0        0        0        0 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/migrations/__init__.py
--rw-r--r--   0        0        0      148 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/models/__init__.py
--rw-r--r--   0        0        0     2725 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/models/args.py
--rw-r--r--   0        0        0    13459 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/models/scheduled_job.py
--rw-r--r--   0        0        0        0 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/py.typed
--rw-r--r--   0        0        0     1687 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/scheduler.py
--rw-r--r--   0        0        0     1588 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/static/scheduler/js/base.js
--rw-r--r--   0        0        0      278 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/templates/admin/scheduler/change_list.html
--rw-r--r--   0        0        0        0 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/templatetags/__init__.py
--rw-r--r--   0        0        0      296 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/templatetags/scheduler_tags.py
--rw-r--r--   0        0        0        0 2023-04-01 21:25:07.001531 django_rq_scheduler-2023.4.0/scheduler/tests/__init__.py
--rw-r--r--   0        0        0      381 2023-04-01 21:25:07.005531 django_rq_scheduler-2023.4.0/scheduler/tests/jobs.py
--rw-r--r--   0        0        0     1424 2023-04-01 21:25:07.005531 django_rq_scheduler-2023.4.0/scheduler/tests/test_admin.py
--rw-r--r--   0        0        0     4901 2023-04-01 21:25:07.005531 django_rq_scheduler-2023.4.0/scheduler/tests/test_job_arg_models.py
--rw-r--r--   0        0        0    23099 2023-04-01 21:25:07.005531 django_rq_scheduler-2023.4.0/scheduler/tests/test_models.py
--rw-r--r--   0        0        0     2379 2023-04-01 21:25:07.005531 django_rq_scheduler-2023.4.0/scheduler/tests/test_scheduler.py
--rw-r--r--   0        0        0     1967 2023-04-01 21:25:07.005531 django_rq_scheduler-2023.4.0/scheduler/tests/testtools.py
--rw-r--r--   0        0        0     2557 2023-04-01 21:25:07.005531 django_rq_scheduler-2023.4.0/scheduler/tools.py
--rw-r--r--   0        0        0       77 2023-04-01 21:25:07.005531 django_rq_scheduler-2023.4.0/scheduler/views.py
--rw-r--r--   0        0        0     3405 1970-01-01 00:00:00.000000 django_rq_scheduler-2023.4.0/PKG-INFO
+-rw-r--r--   0        0        0     1096 2023-04-06 22:49:33.158637 django_rq_scheduler-2023.5.0b1/LICENSE
+-rw-r--r--   0        0        0     1711 2023-04-06 22:49:33.158637 django_rq_scheduler-2023.5.0b1/README.md
+-rw-r--r--   0        0        0     1741 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/pyproject.toml
+-rw-r--r--   0        0        0      134 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/__init__.py
+-rw-r--r--   0        0        0      147 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/admin/__init__.py
+-rw-r--r--   0        0        0     4914 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/admin/job.py
+-rw-r--r--   0        0        0     1646 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/admin/redis_models.py
+-rw-r--r--   0        0        0      481 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/apps.py
+-rw-r--r--   0        0        0     1308 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/decorators.py
+-rw-r--r--   0        0        0        0 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/management/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/management/commands/__init__.py
+-rw-r--r--   0        0        0     1908 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/management/commands/export.py
+-rw-r--r--   0        0        0     3417 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/management/commands/import.py
+-rw-r--r--   0        0        0     3463 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/management/commands/rqstats.py
+-rw-r--r--   0        0        0     2902 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/management/commands/rqworker.py
+-rw-r--r--   0        0        0     1357 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/management/commands/run_job.py
+-rw-r--r--   0        0        0     7162 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/migrations/0001_initial_squashed_0005_added_result_ttl.py
+-rw-r--r--   0        0        0      898 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/migrations/0002_alter_cronjob_id_alter_repeatablejob_id_and_more.py
+-rw-r--r--   0        0        0     4196 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/migrations/0003_auto_20220329_2107.py
+-rw-r--r--   0        0        0      791 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/migrations/0004_cronjob_at_front_repeatablejob_at_front_and_more.py
+-rw-r--r--   0        0        0      896 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/migrations/0005_alter_cronjob_at_front_alter_repeatablejob_at_front_and_more.py
+-rw-r--r--   0        0        0     1051 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/migrations/0006_auto_20230118_1640.py
+-rw-r--r--   0        0        0     1302 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/migrations/0007_add_result_ttl.py
+-rw-r--r--   0        0        0     1982 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/migrations/0008_rename_str_val_jobarg_val_and_more.py
+-rw-r--r--   0        0        0     1279 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/migrations/0009_alter_jobarg_arg_type_alter_jobarg_val_and_more.py
+-rw-r--r--   0        0        0      662 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/migrations/0010_queue.py
+-rw-r--r--   0        0        0     6512 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/migrations/0011_worker_alter_queue_options_alter_cronjob_at_front_and_more.py
+-rw-r--r--   0        0        0        0 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/migrations/__init__.py
+-rw-r--r--   0        0        0      187 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/models/__init__.py
+-rw-r--r--   0        0        0     3102 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/models/args.py
+-rw-r--r--   0        0        0      364 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/models/queue.py
+-rw-r--r--   0        0        0    15115 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/models/scheduled_job.py
+-rw-r--r--   0        0        0      366 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/models/worker.py
+-rw-r--r--   0        0        0        0 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/py.typed
+-rw-r--r--   0        0        0     5437 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/queues.py
+-rw-r--r--   0        0        0     2643 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/rq_classes.py
+-rw-r--r--   0        0        0      551 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/settings.py
+-rw-r--r--   0        0        0     1555 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templates/admin/scheduler/change_form.html
+-rw-r--r--   0        0        0      127 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templates/admin/scheduler/change_list.html
+-rw-r--r--   0        0        0     1559 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templates/admin/scheduler/confirm_action.html
+-rw-r--r--   0        0        0     1282 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templates/admin/scheduler/delete_job.html
+-rw-r--r--   0        0        0     7124 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templates/admin/scheduler/job_detail.html
+-rw-r--r--   0        0        0     6268 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templates/admin/scheduler/jobs.html
+-rw-r--r--   0        0        0     1055 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templates/admin/scheduler/queue_workers.html
+-rw-r--r--   0        0        0      568 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templates/admin/scheduler/scheduler_base.html
+-rw-r--r--   0        0        0     3847 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templates/admin/scheduler/stats.html
+-rw-r--r--   0        0        0     3062 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templates/admin/scheduler/worker_details.html
+-rw-r--r--   0        0        0     1835 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templates/admin/scheduler/workers-list.partial.html
+-rw-r--r--   0        0        0      935 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templates/admin/scheduler/workers.html
+-rw-r--r--   0        0        0        0 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templatetags/__init__.py
+-rw-r--r--   0        0        0      541 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/templatetags/scheduler_tags.py
+-rw-r--r--   0        0        0        0 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/tests/__init__.py
+-rw-r--r--   0        0        0      535 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/tests/jobs.py
+-rw-r--r--   0        0        0      668 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/tests/test_internals.py
+-rw-r--r--   0        0        0     5483 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/tests/test_job_arg_models.py
+-rw-r--r--   0        0        0     2777 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/tests/test_mgmt_cmds.py
+-rw-r--r--   0        0        0    26904 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/tests/test_models.py
+-rw-r--r--   0        0        0      807 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/tests/test_redis_models.py
+-rw-r--r--   0        0        0     2184 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/tests/test_settings.py
+-rw-r--r--   0        0        0    13384 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/tests/test_views.py
+-rw-r--r--   0        0        0      517 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/tests/test_worker.py
+-rw-r--r--   0        0        0     3323 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/tests/testtools.py
+-rw-r--r--   0        0        0     3273 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/tools.py
+-rw-r--r--   0        0        0     1735 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/urls.py
+-rw-r--r--   0        0        0    15140 2023-04-06 22:49:33.166637 django_rq_scheduler-2023.5.0b1/scheduler/views.py
+-rw-r--r--   0        0        0     3459 1970-01-01 00:00:00.000000 django_rq_scheduler-2023.5.0b1/PKG-INFO
```

### Comparing `django_rq_scheduler-2023.4.0/LICENSE` & `django_rq_scheduler-2023.5.0b1/LICENSE`

 * *Files identical despite different names*

### Comparing `django_rq_scheduler-2023.4.0/README.md` & `django_rq_scheduler-2023.5.0b1/README.md`

 * *Files identical despite different names*

### Comparing `django_rq_scheduler-2023.4.0/pyproject.toml` & `django_rq_scheduler-2023.5.0b1/pyproject.toml`

 * *Files 5% similar despite different names*

```diff
@@ -3,16 +3,16 @@
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry]
 name = "django-rq-scheduler"
 packages = [
     { include = "scheduler" },
 ]
-version = "2023.4.0"
-description = "A database backed job scheduler for Django RQ with Django"
+version = "2023.5.0b1"
+description = "An async job scheduler for django using redis"
 readme = "README.md"
 keywords = ["redis", "django", "background-jobs", "job-queue", "task-queue", "redis-queue", "scheduled-jobs"]
 authors = [
     "Daniel Moran <daniel.maruani@gmail.com>",
 ]
 maintainers = [
     "Daniel Moran <daniel.maruani@gmail.com>",
@@ -28,29 +28,31 @@
     'Programming Language :: Python :: 3.9',
     'Programming Language :: Python :: 3.10',
     'Programming Language :: Python :: 3.11',
     'Framework :: Django',
     'Framework :: Django :: 4',
     'Framework :: Django :: 4.0',
     'Framework :: Django :: 4.1',
+    'Framework :: Django :: 4.2',
     'Framework :: Django :: 3.2',
 ]
 homepage = "https://github.com/dsoftwareinc/django-rq-scheduler"
 documentation = "https://django-rq-scheduler.readthedocs.io/en/latest/"
 
 [tool.poetry.urls]
 "Bug Tracker" = "https://github.com/dsoftwareinc/django-rq-scheduler/issues"
 "Funding" = "https://github.com/sponsors/cunla"
 
 [tool.poetry.dependencies]
 python = "^3.9"
-django = ">=3.2, <5"
+django = ">=3.2"
 django-model-utils = "^4.3"
-django-rq = "^2.7"
 croniter = "^1.3"
+click = "^8.1"
+rq = "^1.13"
 
 [tool.poetry.dev-dependencies]
 poetry = "^1.4"
 coverage = "^7"
 fakeredis = "^2.10"
 Flake8-pyproject = "^1.2"
```

### Comparing `django_rq_scheduler-2023.4.0/scheduler/admin.py` & `django_rq_scheduler-2023.5.0b1/scheduler/admin/job.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,115 +1,108 @@
-from django.conf import settings
 from django.contrib import admin, messages
 from django.contrib.contenttypes.admin import GenericStackedInline
-from django.db.models import QuerySet
 from django.utils.translation import gettext_lazy as _
 
 from scheduler import tools
-from scheduler.models import CronJob, JobArg, JobKwarg, RepeatableJob, ScheduledJob, BaseJob
-
-QUEUES = [(key, key) for key in settings.RQ_QUEUES.keys()]
+from scheduler.models import CronJob, JobArg, JobKwarg, RepeatableJob, ScheduledJob
+from scheduler.tools import get_job_executions
 
 
 class HiddenMixin(object):
     class Media:
-        js = ['admin/js/jquery.init.js', 'scheduler/js/base.js']
+        js = ['admin/js/jquery.init.js', ]
 
 
 class JobArgInline(HiddenMixin, GenericStackedInline):
     model = JobArg
     extra = 0
     fieldsets = (
         (None, {
-            'fields': ('arg_type', 'val',),
+            'fields': (('arg_type', 'val',),),
         }),
     )
 
 
 class JobKwargInline(HiddenMixin, GenericStackedInline):
     model = JobKwarg
     extra = 0
     fieldsets = (
         (None, {
-            'fields': ('key', 'arg_type', 'val',),
+            'fields': (('key',), ('arg_type', 'val',),),
         }),
     )
 
 
 class JobAdmin(admin.ModelAdmin):
-    actions = ['delete_model', 'disable_selected', 'enable_selected', 'run_job_now']
-    inlines = [JobArgInline, JobKwargInline]
+    """BaseJob admin class"""
+    change_form_template = 'admin/scheduler/change_form.html'
+    actions = ['disable_selected', 'enable_selected', 'enqueue_job_now', ]
+    inlines = [JobArgInline, JobKwargInline, ]
     list_filter = ('enabled',)
-    list_display = ('enabled', 'name', 'job_id', 'function_string', 'is_scheduled',)
+    list_display = ('enabled', 'name', 'job_id', 'function_string', 'is_scheduled', 'queue',)
     list_display_links = ('name',)
     readonly_fields = ('job_id',)
     fieldsets = (
         (None, {
             'fields': ('name', 'callable', 'enabled', 'at_front',),
         }),
         (_('RQ Settings'), {
             'fields': ('queue', 'job_id',),
         }),
     )
 
-    def get_actions(self, request):
-        actions = super(JobAdmin, self).get_actions(request)
-        actions.pop('delete_selected', None)
-        return actions
-
-    def get_form(self, request, obj=None, **kwargs):
-        queue_field = self.model._meta.get_field('queue')
-        queue_field.choices = QUEUES
-        return super(JobAdmin, self).get_form(request, obj, **kwargs)
-
-    @admin.action(description=_("Delete selected %(verbose_name_plural)s"), permissions=('delete',))
-    def delete_model(self, request, queryset):
-        rows_deleted = 0
-        if isinstance(queryset, BaseJob):
-            queryset.delete()
-            rows_deleted += 1
-        elif isinstance(queryset, QuerySet):
-            rows_deleted, _ = queryset.delete()
-        message_bit = "1 job was" if rows_deleted == 1 else f"{rows_deleted} jobs were"
-        level = messages.WARNING if not rows_deleted else messages.INFO
-        self.message_user(request, f"{message_bit} successfully deleted.", level=level)
+    def change_view(self, request, object_id, form_url='', extra_context=None):
+        extra = extra_context or {}
+        obj = self.get_object(request, object_id)
+        extra['executions'] = get_job_executions(obj.queue, obj)
+
+        return super(JobAdmin, self).change_view(
+            request, object_id, form_url, extra_context=extra)
+
+    def delete_queryset(self, request, queryset):
+        for job in queryset:
+            job.unschedule()
+        super(JobAdmin, self).delete_queryset(request, queryset)
+
+    def delete_model(self, request, obj):
+        obj.unschedule()
+        super(JobAdmin, self).delete_model(request, obj)
 
     @admin.action(description=_("Disable selected %(verbose_name_plural)s"), permissions=('change',))
     def disable_selected(self, request, queryset):
         rows_updated = 0
         for obj in queryset.filter(enabled=True).iterator():
             obj.enabled = False
-            obj.save()
+            obj.unschedule()
             rows_updated += 1
 
         message_bit = "1 job was" if rows_updated == 1 else f"{rows_updated} jobs were"
 
         level = messages.WARNING if not rows_updated else messages.INFO
-        self.message_user(request, f"{message_bit} successfully disabled.", level=level)
+        self.message_user(request, f"{message_bit} successfully disabled and unscheduled.", level=level)
 
     @admin.action(description=_("Enable selected %(verbose_name_plural)s"), permissions=('change',))
     def enable_selected(self, request, queryset):
         rows_updated = 0
         for obj in queryset.filter(enabled=False).iterator():
             obj.enabled = True
             obj.save()
             rows_updated += 1
 
         message_bit = "1 job was" if rows_updated == 1 else f"{rows_updated} jobs were"
         level = messages.WARNING if not rows_updated else messages.INFO
-        self.message_user(request, f"{message_bit} successfully enabled.", level=level)
+        self.message_user(request, f"{message_bit} successfully enabled and scheduled.", level=level)
 
-    @admin.action(description="Run now", permissions=('change',))
-    def run_job_now(self, request, queryset):
+    @admin.action(description="Enqueue now", permissions=('change',))
+    def enqueue_job_now(self, request, queryset):
         job_names = []
         for job in queryset:
-            job.schedule_now()
-            job.save()
+            job.enqueue_to_run()
             job_names.append(job.name)
-        self.message_user(request, "The following jobs have been enqueued: %s" % (', '.join(job_names),))
+        self.message_user(request, f"The following jobs have been enqueued: {', '.join(job_names)}", )
 
 
 @admin.register(ScheduledJob)
 class ScheduledJobAdmin(JobAdmin):
     list_display = JobAdmin.list_display + ('scheduled_time',)
 
     fieldsets = JobAdmin.fieldsets + (
```

### Comparing `django_rq_scheduler-2023.4.0/scheduler/management/commands/export.py` & `django_rq_scheduler-2023.5.0b1/scheduler/management/commands/export.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,7 +1,9 @@
+import sys
+
 import click
 from django.apps import apps
 from django.core.management.base import BaseCommand
 
 from scheduler.tools import MODEL_NAMES
 
 
@@ -23,33 +25,40 @@
 
         parser.add_argument(
             '-e', '--enabled',
             action='store_true',
             dest='enabled',
             help='Export only enabled jobs',
         )
+        parser.add_argument(
+            '-f', '--filename',
+            action='store',
+            dest='filename',
+            help='File name to load (otherwise writes to standard output)',
+        )
 
     def handle(self, *args, **options):
+        file = open(options.get('filename'), 'w') if options.get("filename") else sys.stdout
         res = list()
         for model_name in MODEL_NAMES:
             model = apps.get_model(app_label='scheduler', model_name=model_name)
             jobs = model.objects.all()
             if options.get('enabled'):
                 jobs = jobs.filtered(enabled=True)
             for job in jobs:
                 res.append(job.to_dict())
 
         if options.get("format") == 'json':
             import json
-            click.echo(json.dumps(res, indent=2))
+            click.echo(json.dumps(res, indent=2), file=file)
             return
 
         if options.get("format") == 'yaml':
             try:
                 import yaml
             except ImportError:
                 click.echo("Aborting. LibYAML is not installed.")
                 return
             # Disable YAML alias
-            yaml.Dumper.ignore_aliases = lambda *args: True
-            click.echo(yaml.dump(res, default_flow_style=False))
+            yaml.Dumper.ignore_aliases = lambda *x: True
+            click.echo(yaml.dump(res, default_flow_style=False), file=file)
             return
```

### Comparing `django_rq_scheduler-2023.4.0/scheduler/management/commands/import.py` & `django_rq_scheduler-2023.5.0b1/scheduler/management/commands/import.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 import sys
 from datetime import datetime
 
 import click
 from django.apps import apps
 from django.contrib.contenttypes.models import ContentType
 from django.core.management.base import BaseCommand
-from scheduler.models import JobArg, JobKwarg
 
+from scheduler.models import JobArg, JobKwarg
 from scheduler.tools import MODEL_NAMES
 
 
 def create_job_from_dict(job_dict, update):
     model = apps.get_model(app_label='scheduler', model_name=job_dict['model'])
     existing_job = model.objects.filter(name=job_dict['name']).first()
     if existing_job:
@@ -54,15 +54,15 @@
             dest='format',
             help='format of input',
         )
         parser.add_argument(
             '--filename',
             action='store',
             dest='filename',
-            help='File name to load (otherwise loads from standard input',
+            help='File name to load (otherwise loads from standard input)',
         )
 
         parser.add_argument(
             '-r', '--reset',
             action='store_true',
             dest='reset',
             help='Remove all currently scheduled jobs before importing',
@@ -78,24 +78,24 @@
         file = open(options.get('filename')) if options.get("filename") else sys.stdin
         jobs = list()
         if options.get("format") == 'json':
             import json
             try:
                 jobs = json.load(file)
             except json.decoder.JSONDecodeError:
-                click.echo(f'Error decoding json', err=True)
+                click.echo('Error decoding json', err=True)
 
         if options.get("format") == 'yaml':
             try:
                 import yaml
             except ImportError:
                 click.echo("Aborting. LibYAML is not installed.")
                 return
             # Disable YAML alias
-            yaml.Dumper.ignore_aliases = lambda *args: True
+            yaml.Dumper.ignore_aliases = lambda *x: True
             jobs = yaml.load(file, yaml.SafeLoader)
 
         if options.get('reset'):
             for model_name in MODEL_NAMES:
                 model = apps.get_model(app_label='scheduler', model_name=model_name)
                 model.objects.delete()
```

### Comparing `django_rq_scheduler-2023.4.0/scheduler/migrations/0001_initial_squashed_0005_added_result_ttl.py` & `django_rq_scheduler-2023.5.0b1/scheduler/migrations/0001_initial_squashed_0005_added_result_ttl.py`

 * *Files identical despite different names*

### Comparing `django_rq_scheduler-2023.4.0/scheduler/migrations/0002_alter_cronjob_id_alter_repeatablejob_id_and_more.py` & `django_rq_scheduler-2023.5.0b1/scheduler/migrations/0002_alter_cronjob_id_alter_repeatablejob_id_and_more.py`

 * *Files identical despite different names*

### Comparing `django_rq_scheduler-2023.4.0/scheduler/migrations/0003_auto_20220329_2107.py` & `django_rq_scheduler-2023.5.0b1/scheduler/migrations/0003_auto_20220329_2107.py`

 * *Files identical despite different names*

### Comparing `django_rq_scheduler-2023.4.0/scheduler/migrations/0004_cronjob_at_front_repeatablejob_at_front_and_more.py` & `django_rq_scheduler-2023.5.0b1/scheduler/migrations/0004_cronjob_at_front_repeatablejob_at_front_and_more.py`

 * *Files identical despite different names*

### Comparing `django_rq_scheduler-2023.4.0/scheduler/migrations/0005_alter_cronjob_at_front_alter_repeatablejob_at_front_and_more.py` & `django_rq_scheduler-2023.5.0b1/scheduler/migrations/0005_alter_cronjob_at_front_alter_repeatablejob_at_front_and_more.py`

 * *Files identical despite different names*

### Comparing `django_rq_scheduler-2023.4.0/scheduler/migrations/0006_auto_20230118_1640.py` & `django_rq_scheduler-2023.5.0b1/scheduler/migrations/0006_auto_20230118_1640.py`

 * *Files identical despite different names*

### Comparing `django_rq_scheduler-2023.4.0/scheduler/migrations/0007_add_result_ttl.py` & `django_rq_scheduler-2023.5.0b1/scheduler/migrations/0007_add_result_ttl.py`

 * *Files identical despite different names*

### Comparing `django_rq_scheduler-2023.4.0/scheduler/migrations/0008_rename_str_val_jobarg_val_and_more.py` & `django_rq_scheduler-2023.5.0b1/scheduler/migrations/0008_rename_str_val_jobarg_val_and_more.py`

 * *Files identical despite different names*

### Comparing `django_rq_scheduler-2023.4.0/scheduler/migrations/0009_alter_jobarg_arg_type_alter_jobarg_val_and_more.py` & `django_rq_scheduler-2023.5.0b1/scheduler/migrations/0009_alter_jobarg_arg_type_alter_jobarg_val_and_more.py`

 * *Files identical despite different names*

### Comparing `django_rq_scheduler-2023.4.0/scheduler/models/args.py` & `django_rq_scheduler-2023.5.0b1/scheduler/models/args.py`

 * *Files 12% similar despite different names*

```diff
@@ -38,15 +38,23 @@
     def clean(self):
         if self.arg_type not in ARG_TYPE_TYPES_DICT:
             raise ValidationError({
                 'arg_type': ValidationError(
                     _(f'Could not parse {self.arg_type}, options are: {ARG_TYPE_TYPES_DICT.keys()}'), code='invalid')
             })
         try:
-            self.value()
+            if self.arg_type == 'callable':
+                tools.callable_func(self.val)
+            elif self.arg_type == 'datetime':
+                datetime.fromisoformat(self.val)
+            elif self.arg_type == 'bool':
+                if self.val.lower() not in {'true', 'false'}:
+                    raise ValidationError
+            elif self.arg_type == 'int':
+                int(self.val)
         except Exception:
             raise ValidationError({
                 'arg_type': ValidationError(
                     _(f'Could not parse {self.val} as {self.arg_type}'), code='invalid')
             })
 
     def save(self, **kwargs):
```

### Comparing `django_rq_scheduler-2023.4.0/scheduler/models/scheduled_job.py` & `django_rq_scheduler-2023.5.0b1/scheduler/models/scheduled_job.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,220 +1,218 @@
 import math
+import uuid
 from datetime import timedelta
 from typing import Dict
 
 import croniter
 from django.apps import apps
 from django.conf import settings
 from django.contrib import admin
 from django.contrib.contenttypes.fields import GenericRelation
 from django.core.exceptions import ValidationError
 from django.db import models
 from django.templatetags.tz import utc
 from django.utils import timezone
+from django.utils.safestring import mark_safe
 from django.utils.translation import gettext_lazy as _
-from django_rq.queues import get_queue
 from model_utils import Choices
 from model_utils.models import TimeStampedModel
-from django.utils.timezone import now
 
-from scheduler import tools, logger
+from scheduler import tools
 from scheduler.models.args import JobArg, JobKwarg
+from scheduler.queues import get_queue, logger
+from scheduler.rq_classes import DjangoQueue
 
 RQ_SCHEDULER_INTERVAL = getattr(settings, "DJANGO_RQ_SCHEDULER_INTERVAL", 60)
 
 
 def callback_save_job(job, connection, result, *args, **kwargs):
     model_name = job.meta.get('job_type', None)
     if model_name is None:
         return
     model = apps.get_model(app_label='scheduler', model_name=model_name)
     scheduled_job = model.objects.filter(job_id=job.id).first()
-    if scheduled_job:
+    if scheduled_job is not None:
         scheduled_job.unschedule()
         scheduled_job.schedule()
-        scheduled_job.save()
 
 
 class BaseJob(TimeStampedModel):
+    QUEUES = [(key, key) for key in settings.RQ_QUEUES.keys()]
     JOB_TYPE = 'BaseJob'
     name = models.CharField(_('name'), max_length=128, unique=True)
     callable = models.CharField(_('callable'), max_length=2048)
     callable_args = GenericRelation(JobArg, related_query_name='args')
     callable_kwargs = GenericRelation(JobKwarg, related_query_name='kwargs')
-    enabled = models.BooleanField(_('enabled'), default=True)
+    enabled = models.BooleanField(
+        _('enabled'), default=True,
+        help_text=_('Should job be scheduled? This field is useful to keep '
+                    'past jobs that should no longer be scheduled'),
+    )
     queue = models.CharField(
-        _('queue'),
-        max_length=16,
-        help_text='Queue name', )
+        _('queue'), max_length=16, choices=QUEUES,
+        help_text=_('Queue name'), )
     job_id = models.CharField(
-        _('job id'), max_length=128, editable=False, blank=True, null=True)
-    repeat = models.PositiveIntegerField(_('repeat'), blank=True, null=True)
-    at_front = models.BooleanField(_('At front'), default=False, blank=True, null=True)
+        _('job id'), max_length=128, editable=False, blank=True, null=True,
+        help_text=_('Current job_id on queue'))
+    repeat = models.PositiveIntegerField(
+        _('repeat'), blank=True, null=True,
+        help_text=_('Number of times to run the job. Leaving this blank means it will run forever.'), )
+    at_front = models.BooleanField(
+        _('At front'), default=False, blank=True, null=True,
+        help_text=_('When queuing the job, add it in the front of the queue'), )
     timeout = models.IntegerField(
         _('timeout'), blank=True, null=True,
-        help_text=_(
-            'Timeout specifies the maximum runtime, in seconds, for the job '
-            'before it\'ll be considered \'lost\'. Blank uses the default '
-            'timeout.'
-        )
-    )
+        help_text=_("Timeout specifies the maximum runtime, in seconds, for the job "
+                    "before it'll be considered 'lost'. Blank uses the default "
+                    "timeout."), )
     result_ttl = models.IntegerField(
         _('result ttl'), blank=True, null=True,
-        help_text=_('The TTL value (in seconds) of the job result. -1: '
-                    'Result never expires, you should delete jobs manually. '
-                    '0: Result gets deleted immediately. >0: Result expires '
-                    'after n seconds.')
-    )
-
-    def __str__(self):
-        func = self.callable + "({})"  # zero-width space allows textwrap
-        args = self.parse_args()
-        args_list = [repr(arg) for arg in args]
-        kwargs = self.parse_kwargs()
-        kwargs_list = [k + '=' + repr(v) for (k, v) in kwargs.items()]
-        callable=func.format(', '.join(args_list + kwargs_list))
-        return f'{self.JOB_TYPE}[{self.name}={callable}]'
+        help_text=mark_safe(
+            """The TTL value (in seconds) of the job result.<br/>
+               -1: Result never expires, you should delete jobs manually. <br/>
+                0: Result gets deleted immediately. <br/>
+                >0: Result expires after n seconds."""), )
 
     def callable_func(self):
+        """Translate callable string to callable"""
         return tools.callable_func(self.callable)
 
-    def clean(self):
-        self.clean_callable()
-        self.clean_queue()
-
-    def clean_callable(self):
-        try:
-            tools.callable_func(self.callable)
-        except Exception:
-            raise ValidationError({
-                'callable': ValidationError(
-                    _('Invalid callable, must be importable'), code='invalid')
-            })
-
-    def clean_queue(self):
-        queue_keys = settings.RQ_QUEUES.keys()
-        if self.queue not in queue_keys:
-            raise ValidationError({
-                'queue': ValidationError(
-                    _('Invalid queue, must be one of: {}'.format(
-                        ', '.join(queue_keys))), code='invalid')
-            })
-
     @admin.display(boolean=True, description=_('is scheduled?'))
     def is_scheduled(self) -> bool:
+        """Check whether job is queued/scheduled to be executed"""
         if not self.job_id:
             return False
         scheduled_jobs = self._get_rqueue().scheduled_job_registry.get_job_ids()
-        return self.job_id in scheduled_jobs
-
-    def save(self, **kwargs):
-        schedule_job = kwargs.pop('schedule_job', True)
-        super(BaseJob, self).save(**kwargs)
-        if schedule_job:
-            self.schedule()
+        enqueued_jobs = self._get_rqueue().get_job_ids()
+        res = (self.job_id in scheduled_jobs) or (self.job_id in enqueued_jobs)
+        if not res:
+            self.job_id = None
             super(BaseJob, self).save()
-
-    def delete(self, **kwargs):
-        self.unschedule()
-        super(BaseJob, self).delete(**kwargs)
+        return res
 
     @admin.display(description='Callable')
     def function_string(self) -> str:
-        func = self.callable + "(\u200b{})"  # zero-width space allows textwrap
         args = self.parse_args()
         args_list = [repr(arg) for arg in args]
         kwargs = self.parse_kwargs()
         kwargs_list = [k + '=' + repr(v) for (k, v) in kwargs.items()]
-        return func.format(', '.join(args_list + kwargs_list))
+        return self.callable + f"({', '.join(args_list + kwargs_list)})"
 
     def parse_args(self):
+        """Parse args for running job"""
         args = self.callable_args.all()
         return [arg.value() for arg in args]
 
     def parse_kwargs(self):
+        """Parse kwargs for running job"""
         kwargs = self.callable_kwargs.all()
         return dict([kwarg.value() for kwarg in kwargs])
 
-    def enqueue_args(self) -> dict:
+    def _next_job_id(self):
+        addition = uuid.uuid4().hex[-10:]
+        return f'{self.queue}:{self.name}:{addition}'
+
+    def _enqueue_args(self) -> Dict:
+        """args for DjangoQueue.enqueue.
+        Set all arguments for DjangoQueue.enqueue/enqueue_at.
+        Particularly:
+        - set job timeout and ttl
+        - ensure a callback to reschedule job next iteration.
+        - set job-id to proper format
+        - set job meta
+        """
         res = dict(
             meta=dict(
                 repeat=self.repeat,
                 job_type=self.JOB_TYPE,
+                scheduled_job_id=self.id,
             ),
             on_success=callback_save_job,
             on_failure=callback_save_job,
+            job_id=self._next_job_id(),
         )
         if self.at_front:
             res['at_front'] = self.at_front
         if self.timeout:
             res['job_timeout'] = self.timeout
         if self.result_ttl is not None:
             res['result_ttl'] = self.result_ttl
         return res
 
-    def _get_rqueue(self):
+    def _get_rqueue(self) -> DjangoQueue:
+        """Returns django-queue for job
+        """
         return get_queue(self.queue)
 
     def ready_for_schedule(self) -> bool:
+        """Is job ready to be scheduled?
+
+        If job is already scheduled or disabled, then it is not
+        ready to be scheduled.
+
+        :returns: True if job is ready to be scheduled.
+        """
         if self.is_scheduled():
             logger.debug(f'Job {self.name} already scheduled')
             return False
         if not self.enabled:
             logger.debug(f'Job {str(self)} disabled, enable job before scheduling')
             return False
         return True
 
     def schedule(self) -> bool:
+        """Schedule job to run.
+        :returns: True if job was scheduled, False otherwise.
+        """
         if not self.ready_for_schedule():
             return False
         schedule_time = self._schedule_time()
-        kwargs = self.enqueue_args()
+        kwargs = self._enqueue_args()
         job = self._get_rqueue().enqueue_at(
             schedule_time,
             tools.run_job,
             args=(self.JOB_TYPE, self.id),
-            **kwargs,
-        )
-        self.job_id = job.id
-        return True
-
-    def schedule_now(self) -> bool:
-        kwargs = self.enqueue_args()
-        job = self._get_rqueue().enqueue_at(
-            utc(now()),
-            tools.run_job,
-            args=(self.JOB_TYPE, self.id),
-            **kwargs,
-        )
+            **kwargs, )
         self.job_id = job.id
+        super(BaseJob, self).save()
         return True
 
     def enqueue_to_run(self) -> bool:
-        kwargs = self.enqueue_args()
+        """Enqueue job to run now.
+        """
+        kwargs = self._enqueue_args()
         job = self._get_rqueue().enqueue(
             tools.run_job,
             args=(self.JOB_TYPE, self.id),
             **kwargs,
         )
         self.job_id = job.id
+        super(BaseJob, self).save()
         return True
 
     def unschedule(self) -> bool:
+        """Remove job from django-queue.
+
+        If job is queued to be executed or scheduled to be executed, it will remove it.
+        """
         queue = self._get_rqueue()
         if self.is_scheduled():
             queue.remove(self.job_id)
             queue.scheduled_job_registry.remove(self.job_id)
         self.job_id = None
+        super(BaseJob, self).save()
         return True
 
     def _schedule_time(self):
         raise NotImplementedError
 
     def to_dict(self) -> Dict:
+        """Export model to dictionary, so it can be saved as external file backup
+        """
         return dict(
             model=self.JOB_TYPE,
             name=self.name,
             callable=self.callable,
             callable_args=[
                 dict(arg_type=arg.arg_type, val=arg.val, )
                 for arg in self.callable_args.all()],
@@ -225,14 +223,52 @@
             queue=self.queue,
             repeat=self.repeat,
             at_front=self.at_front,
             timeout=self.timeout,
             result_ttl=self.result_ttl,
         )
 
+    def __str__(self):
+        func = self.function_string()
+        return f'{self.JOB_TYPE}[{self.name}={func}]'
+
+    def save(self, **kwargs):
+        schedule_job = kwargs.pop('schedule_job', True)
+        super(BaseJob, self).save(**kwargs)
+        if schedule_job:
+            self.schedule()
+            super(BaseJob, self).save()
+
+    def delete(self, **kwargs):
+        self.unschedule()
+        super(BaseJob, self).delete(**kwargs)
+
+    # Job form validation methods
+    def clean(self):
+        self.clean_callable()
+        self.clean_queue()
+
+    def clean_callable(self):
+        try:
+            tools.callable_func(self.callable)
+        except Exception:
+            raise ValidationError({
+                'callable': ValidationError(
+                    _('Invalid callable, must be importable'), code='invalid')
+            })
+
+    def clean_queue(self):
+        queue_keys = settings.RQ_QUEUES.keys()
+        if self.queue not in queue_keys:
+            raise ValidationError({
+                'queue': ValidationError(
+                    _('Invalid queue, must be one of: {}'.format(
+                        ', '.join(queue_keys))), code='invalid')
+            })
+
     class Meta:
         abstract = True
 
 
 class ScheduledTimeMixin(models.Model):
     scheduled_time = models.DateTimeField(_('scheduled time'))
 
@@ -244,19 +280,17 @@
 
 
 class ScheduledJob(ScheduledTimeMixin, BaseJob):
     repeat = None
     JOB_TYPE = 'ScheduledJob'
 
     def ready_for_schedule(self) -> bool:
-        if super(ScheduledJob, self).ready_for_schedule() is False:
-            return False
-        if self.scheduled_time is not None and self.scheduled_time < timezone.now():
-            return False
-        return True
+        return (super(ScheduledJob, self).ready_for_schedule()
+                and (self.scheduled_time is None
+                     or self.scheduled_time >= timezone.now()))
 
     def to_dict(self) -> Dict:
         res = super(ScheduledJob, self).to_dict()
         res['scheduled_time'] = self.scheduled_time.isoformat()
         del res['repeat']
         return res
 
@@ -331,16 +365,16 @@
         """
         Counts the number of repeats lapsed between scheduled time and now
         and decrements that amount from the repeats remaining and updates the scheduled time to the next repeat.
 
         self.repeat is None ==> Run forever.
         """
 
-    def enqueue_args(self):
-        res = super(RepeatableJob, self).enqueue_args()
+    def _enqueue_args(self):
+        res = super(RepeatableJob, self)._enqueue_args()
         res['meta']['interval'] = self.interval_seconds()
         return res
 
     def ready_for_schedule(self):
         if super(RepeatableJob, self).ready_for_schedule() is False:
             return False
         if self.scheduled_time < timezone.now():
@@ -360,15 +394,17 @@
 
 
 class CronJob(BaseJob):
     JOB_TYPE = 'CronJob'
 
     cron_string = models.CharField(
         _('cron string'), max_length=64,
-        help_text=_('Define the schedule in a crontab like syntax. Times are in UTC.')
+        help_text=mark_safe(
+            '''Define the schedule in a crontab like syntax.
+            Times are in UTC. Use <a href="https://crontab.guru/">crontab.guru</a> to create a cron string.''')
     )
 
     def to_dict(self) -> Dict:
         res = super(CronJob, self).to_dict()
         res['cron_string'] = self.cron_string
         return res
```

### Comparing `django_rq_scheduler-2023.4.0/scheduler/tests/test_job_arg_models.py` & `django_rq_scheduler-2023.5.0b1/scheduler/tests/test_job_arg_models.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 from django.core.exceptions import ValidationError
 from django.test import TestCase
 from django.utils import timezone
 
 from scheduler.models import JobArg, JobKwarg
+from .jobs import arg_callable
 from .testtools import jobarg_factory
 
 
 class TestAllJobArg(TestCase):
     JobArgClass = JobArg
 
     def test_bad_arg_type(self):
@@ -15,14 +16,19 @@
             arg.clean()
 
     def test_clean_one_value_invalid_str_int(self):
         arg = jobarg_factory(self.JobArgClass, arg_type='int', val='not blank', )
         with self.assertRaises(ValidationError):
             arg.clean()
 
+    def test_callable_arg_type__not_clean(self):
+        arg = jobarg_factory(self.JobArgClass, arg_type='callable', val='bad_callable', )
+        with self.assertRaises(ValidationError):
+            arg.clean()
+
     def test_clean_invalid(self):
         arg = jobarg_factory(self.JobArgClass, arg_type='int', val='str')
         with self.assertRaises(ValidationError):
             arg.clean()
 
     def test_clean(self):
         arg = jobarg_factory(self.JobArgClass, val='something')
@@ -71,14 +77,23 @@
         arg = jobarg_factory(self.JobArgClass, arg_type='datetime', val=str(_time))
         self.assertEqual(repr(_time), repr(arg.value()))
 
     def test__repr__bool_val(self):
         arg = jobarg_factory(self.JobArgClass, arg_type='bool', val='False')
         self.assertEqual('False', repr(arg.value()))
 
+    def test_callable_arg_type__clean(self):
+        method = arg_callable
+        arg = jobarg_factory(
+            self.JobArgClass, arg_type='callable',
+            val=f'{method.__module__}.{method.__name__}', )
+        self.assertIsNone(arg.clean())
+        self.assertEqual(1, arg.value())
+        self.assertEqual(2, arg.value())
+
 
 class TestJobKwarg(TestAllJobArg):
     JobArgClass = JobKwarg
 
     def test_str(self):
         arg = jobarg_factory(self.JobArgClass)
         self.assertEqual(
```

### Comparing `django_rq_scheduler-2023.4.0/scheduler/tests/test_models.py` & `django_rq_scheduler-2023.5.0b1/scheduler/tests/test_models.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,564 +1,637 @@
 import zoneinfo
 from datetime import datetime, timedelta
 
 from django.conf import settings
-from django.contrib.auth.models import User
+from django.contrib.messages import get_messages
 from django.core.exceptions import ValidationError
-from django.test import Client, TestCase
 from django.urls import reverse
 from django.utils import timezone
 
 from scheduler.models import BaseJob, CronJob, JobArg, JobKwarg, RepeatableJob, ScheduledJob
-from scheduler.tools import run_job
+from scheduler.tools import run_job, create_worker
 from . import jobs
-from .testtools import job_factory, jobarg_factory, _get_job_from_queue
+from .testtools import job_factory, jobarg_factory, _get_job_from_queue, SchedulerBaseCase, _get_executions
+from ..queues import get_queue
 
 
-class BaseTestCases:
-    class TestBaseJob(TestCase):
-        JobClass = BaseJob
+def assert_response_has_msg(response, message):
+    messages = [m.message for m in get_messages(response.wsgi_request)]
+    assert message in messages, f'expected "{message}" in {messages}'
+
+
+def has_execution_with_status(django_job, status):
+    job_list = _get_executions(django_job)
+    job_list = [(j.id, j.get_status()) for j in job_list]
+    for job in job_list:
+        if job[1] == status:
+            return True
+    print(f'{job_list} does not contain a job with status {status}')
+    return False
+
 
-        @classmethod
-        def setUpTestData(cls) -> None:
-            try:
-                User.objects.create_superuser('admin', 'admin@a.com', 'admin')
-            except Exception:
-                pass
-            cls.client = Client()
+class BaseTestCases:
+    class TestBaseJob(SchedulerBaseCase):
+        JobModelClass = BaseJob
 
         def test_callable_func(self):
-            job = job_factory(self.JobClass)
+            job = job_factory(self.JobModelClass)
             job.callable = 'scheduler.tests.jobs.test_job'
             func = job.callable_func()
             self.assertEqual(jobs.test_job, func)
 
         def test_callable_func_not_callable(self):
-            job = job_factory(self.JobClass)
+            job = job_factory(self.JobModelClass)
             job.callable = 'scheduler.tests.jobs.test_non_callable'
             with self.assertRaises(TypeError):
                 job.callable_func()
 
         def test_clean_callable(self):
-            job = job_factory(self.JobClass)
+            job = job_factory(self.JobModelClass)
             job.callable = 'scheduler.tests.jobs.test_job'
             self.assertIsNone(job.clean_callable())
 
         def test_clean_callable_invalid(self):
-            job = job_factory(self.JobClass)
+            job = job_factory(self.JobModelClass)
             job.callable = 'scheduler.tests.jobs.test_non_callable'
             with self.assertRaises(ValidationError):
                 job.clean_callable()
 
         def test_clean_queue(self):
             for queue in settings.RQ_QUEUES.keys():
-                job = job_factory(self.JobClass)
+                job = job_factory(self.JobModelClass)
                 job.queue = queue
                 self.assertIsNone(job.clean_queue())
 
         def test_clean_queue_invalid(self):
-            job = job_factory(self.JobClass)
+            job = job_factory(self.JobModelClass)
             job.queue = 'xxxxxx'
             job.callable = 'scheduler.tests.jobs.test_job'
             with self.assertRaises(ValidationError):
                 job.clean()
 
         # next 2 check the above are included in job.clean() function
         def test_clean_base(self):
-            job = job_factory(self.JobClass)
+            job = job_factory(self.JobModelClass)
             job.queue = list(settings.RQ_QUEUES)[0]
             job.callable = 'scheduler.tests.jobs.test_job'
             self.assertIsNone(job.clean())
 
         def test_clean_invalid_callable(self):
-            job = job_factory(self.JobClass)
+            job = job_factory(self.JobModelClass)
             job.queue = list(settings.RQ_QUEUES)[0]
             job.callable = 'scheduler.tests.jobs.test_non_callable'
             with self.assertRaises(ValidationError):
                 job.clean()
 
         def test_clean_invalid_queue(self):
-            job = job_factory(self.JobClass)
+            job = job_factory(self.JobModelClass)
             job.queue = 'xxxxxx'
             job.callable = 'scheduler.tests.jobs.test_job'
             with self.assertRaises(ValidationError):
                 job.clean()
 
         def test_is_schedulable_already_scheduled(self):
-            job = job_factory(self.JobClass, )
+            job = job_factory(self.JobModelClass, )
             job.schedule()
             self.assertTrue(job.is_scheduled())
 
         def test_is_schedulable_disabled(self):
-            job = job_factory(self.JobClass)
+            job = job_factory(self.JobModelClass)
             job.enabled = False
             self.assertFalse(job.enabled)
 
         def test_schedule(self):
-            job = job_factory(self.JobClass, )
+            job = job_factory(self.JobModelClass, )
             self.assertTrue(job.is_scheduled())
             self.assertIsNotNone(job.job_id)
 
         def test_unschedulable(self):
-            job = job_factory(self.JobClass, enabled=False)
+            job = job_factory(self.JobModelClass, enabled=False)
             self.assertFalse(job.is_scheduled())
             self.assertIsNone(job.job_id)
 
         def test_unschedule(self):
-            job = job_factory(self.JobClass, )
+            job = job_factory(self.JobModelClass, )
             self.assertTrue(job.unschedule())
             self.assertIsNone(job.job_id)
 
         def test_unschedule_not_scheduled(self):
-            job = job_factory(self.JobClass, enabled=False)
+            job = job_factory(self.JobModelClass, enabled=False)
             self.assertTrue(job.unschedule())
             self.assertIsNone(job.job_id)
 
         def test_save_enabled(self):
-            job = job_factory(self.JobClass, )
-            job.save()
+            job = job_factory(self.JobModelClass, )
             self.assertIsNotNone(job.job_id)
 
         def test_save_disabled(self):
-            job = job_factory(self.JobClass, enabled=False)
+            job = job_factory(self.JobModelClass, enabled=False)
             job.save()
             self.assertIsNone(job.job_id)
 
         def test_save_and_schedule(self):
-            job = job_factory(self.JobClass, )
+            job = job_factory(self.JobModelClass, )
             self.assertIsNotNone(job.job_id)
             self.assertTrue(job.is_scheduled())
 
         def test_schedule2(self):
-            job = job_factory(self.JobClass)
+            job = job_factory(self.JobModelClass)
             job.queue = list(settings.RQ_QUEUES)[0]
             job.enabled = False
             job.scheduled_time = timezone.now() + timedelta(minutes=1)
             self.assertFalse(job.schedule())
 
         def test_delete_and_unschedule(self):
-            job = job_factory(self.JobClass, )
+            job = job_factory(self.JobModelClass, )
             self.assertIsNotNone(job.job_id)
             self.assertTrue(job.is_scheduled())
             job.delete()
             self.assertFalse(job.is_scheduled())
 
         def test_job_create(self):
-            prev_count = self.JobClass.objects.count()
-            job_factory(self.JobClass)
-            self.assertEqual(self.JobClass.objects.count(), prev_count + 1)
+            prev_count = self.JobModelClass.objects.count()
+            job_factory(self.JobModelClass)
+            self.assertEqual(self.JobModelClass.objects.count(), prev_count + 1)
 
         def test_str(self):
             name = "test"
-            job = job_factory(self.JobClass, name=name)
-            self.assertEqual(f'{self.JobClass.__name__}[{name}={job.callable}()]', str(job))
+            job = job_factory(self.JobModelClass, name=name)
+            self.assertEqual(f'{self.JobModelClass.__name__}[{name}={job.callable}()]', str(job))
 
         def test_callable_passthrough(self):
-            job = job_factory(self.JobClass)
+            job = job_factory(self.JobModelClass)
             entry = _get_job_from_queue(job)
             self.assertEqual(entry.func, run_job)
             job_model, job_id = entry.args
-            self.assertEqual(job_model, self.JobClass.__name__)
+            self.assertEqual(job_model, self.JobModelClass.__name__)
             self.assertEqual(job_id, job.id)
 
         def test_timeout_passthrough(self):
-            job = job_factory(self.JobClass, timeout=500)
+            job = job_factory(self.JobModelClass, timeout=500)
             entry = _get_job_from_queue(job)
             self.assertEqual(entry.timeout, 500)
 
         def test_at_front_passthrough(self):
-            job = job_factory(self.JobClass, at_front=True)
+            job = job_factory(self.JobModelClass, at_front=True)
             queue = job._get_rqueue()
             jobs_to_schedule = queue.scheduled_job_registry.get_job_ids()
             self.assertIn(job.job_id, jobs_to_schedule)
 
         def test_callable_result(self):
-            job = job_factory(self.JobClass, )
+            job = job_factory(self.JobModelClass, )
             entry = _get_job_from_queue(job)
             self.assertEqual(entry.perform(), 2)
 
         def test_callable_empty_args_and_kwargs(self):
-            job = job_factory(self.JobClass, callable='scheduler.tests.jobs.test_args_kwargs')
+            job = job_factory(self.JobModelClass, callable='scheduler.tests.jobs.test_args_kwargs')
             entry = _get_job_from_queue(job)
             self.assertEqual(entry.perform(), 'test_args_kwargs()')
 
         def test_delete_args(self):
-            job = job_factory(self.JobClass, )
+            job = job_factory(self.JobModelClass, )
             arg = jobarg_factory(JobArg, val='one', content_object=job)
             self.assertEqual(1, job.callable_args.count())
             arg.delete()
             self.assertEqual(0, job.callable_args.count())
 
         def test_delete_kwargs(self):
-            job = job_factory(self.JobClass, )
+            job = job_factory(self.JobModelClass, )
             kwarg = jobarg_factory(JobKwarg, key='key1', arg_type='str', val='one', content_object=job)
             self.assertEqual(1, job.callable_kwargs.count())
             kwarg.delete()
             self.assertEqual(0, job.callable_kwargs.count())
 
         def test_parse_args(self):
-            job = job_factory(self.JobClass, )
+            job = job_factory(self.JobModelClass, )
             date = timezone.now()
             jobarg_factory(JobArg, val='one', content_object=job)
             jobarg_factory(JobArg, arg_type='int', val=2, content_object=job)
             jobarg_factory(JobArg, arg_type='bool', val=True, content_object=job)
             jobarg_factory(JobArg, arg_type='bool', val=False, content_object=job)
             jobarg_factory(JobArg, arg_type='datetime', val=date, content_object=job)
             self.assertEqual(job.parse_args(), ['one', 2, True, False, date])
 
         def test_parse_kwargs(self):
-            job = job_factory(self.JobClass, )
+            job = job_factory(self.JobModelClass, )
             date = timezone.now()
             jobarg_factory(JobKwarg, key='key1', arg_type='str', val='one', content_object=job)
             jobarg_factory(JobKwarg, key='key2', arg_type='int', val=2, content_object=job)
             jobarg_factory(JobKwarg, key='key3', arg_type='bool', val=True, content_object=job)
             jobarg_factory(JobKwarg, key='key4', arg_type='datetime', val=date, content_object=job)
             kwargs = job.parse_kwargs()
             self.assertEqual(kwargs, dict(key1='one', key2=2, key3=True, key4=date))
 
         def test_callable_args_and_kwargs(self):
-            job = job_factory(self.JobClass, callable='scheduler.tests.jobs.test_args_kwargs')
+            job = job_factory(self.JobModelClass, callable='scheduler.tests.jobs.test_args_kwargs')
             date = timezone.now()
             jobarg_factory(JobArg, arg_type='str', val='one', content_object=job)
             jobarg_factory(JobKwarg, key='key1', arg_type='int', val=2, content_object=job)
             jobarg_factory(JobKwarg, key='key2', arg_type='datetime', val=date, content_object=job)
             jobarg_factory(JobKwarg, key='key3', arg_type='bool', val=False, content_object=job)
             job.save()
             entry = _get_job_from_queue(job)
             self.assertEqual(entry.perform(),
                              "test_args_kwargs('one', key1=2, key2={}, key3=False)".format(date))
 
         def test_function_string(self):
-            job = job_factory(self.JobClass, )
+            job = job_factory(self.JobModelClass, )
             date = timezone.now()
             jobarg_factory(JobArg, arg_type='str', val='one', content_object=job)
             jobarg_factory(JobArg, arg_type='int', val='1', content_object=job)
             jobarg_factory(JobArg, arg_type='datetime', val=date, content_object=job)
             jobarg_factory(JobArg, arg_type='bool', val=True, content_object=job)
             jobarg_factory(JobKwarg, key='key1', arg_type='str', val='one', content_object=job)
             jobarg_factory(JobKwarg, key='key2', arg_type='int', val=2, content_object=job)
             jobarg_factory(JobKwarg, key='key3', arg_type='datetime', val=date, content_object=job)
             jobarg_factory(JobKwarg, key='key4', arg_type='bool', val=False, content_object=job)
             self.assertEqual(job.function_string(),
-                             ("scheduler.tests.jobs.test_job(\u200b'one', 1, {date}, True, " +
-                              "key1='one', key2=2, key3={date}, key4=False)").format(date=repr(date)))
+                             f"scheduler.tests.jobs.test_job('one', 1, {repr(date)}, True, "
+                             f"key1='one', key2=2, key3={repr(date)}, key4=False)")
 
         def test_admin_list_view(self):
             # arrange
             self.client.login(username='admin', password='admin')
-            job = job_factory(self.JobClass, )
+            job = job_factory(self.JobModelClass, )
             model = job._meta.model.__name__.lower()
             url = reverse(f'admin:scheduler_{model}_changelist')
             # act
             res = self.client.get(url)
             # assert
             self.assertEqual(200, res.status_code)
 
         def test_admin_list_view_delete_model(self):
             # arrange
             self.client.login(username='admin', password='admin')
-            job = job_factory(self.JobClass, )
-            job.save()
+            job = job_factory(self.JobModelClass, )
             model = job._meta.model.__name__.lower()
             url = reverse(f'admin:scheduler_{model}_changelist')
             # act
             res = self.client.post(url, data={
                 'action': 'delete_model',
                 '_selected_action': [job.pk, ],
             })
             # assert
             self.assertEqual(302, res.status_code)
 
-        def test_admin_single_view(self):
+        def test_admin_run_job_now_enqueues_job_at(self):
             # arrange
             self.client.login(username='admin', password='admin')
-            job = job_factory(self.JobClass, )
-            job.save()
+            job = job_factory(self.JobModelClass, )
             model = job._meta.model.__name__.lower()
-            url = reverse(f'admin:scheduler_{model}_change', args=[job.pk, ])
+            url = reverse(f'admin:scheduler_{model}_changelist')
             # act
-            res = self.client.get(url)
+            res = self.client.post(url, data={
+                'action': 'enqueue_job_now',
+                '_selected_action': [job.pk, ],
+            })
             # assert
-            self.assertEqual(200, res.status_code)
+            self.assertEqual(302, res.status_code)
+            job.refresh_from_db()
+            queue = get_queue(job.queue)
+            self.assertIn(job.job_id, queue.get_job_ids())
 
-        def test_admin_single_delete(self):
+        def test_admin_single_view(self):
             # arrange
             self.client.login(username='admin', password='admin')
-            job = job_factory(self.JobClass, )
-            job.save()
+            job = job_factory(self.JobModelClass, )
             model = job._meta.model.__name__.lower()
-            url = reverse(f'admin:scheduler_{model}_delete', args=[job.pk, ])
+            url = reverse(f'admin:scheduler_{model}_change', args=[job.pk, ])
             # act
-            res = self.client.post(url)
+            res = self.client.get(url)
             # assert
             self.assertEqual(200, res.status_code)
 
-        def test_admin_run_job_now(self):
+        def test_admin_enqueue_job_now(self):
             # arrange
             self.client.login(username='admin', password='admin')
-            job = job_factory(self.JobClass, )
-            job.save()
+            job = job_factory(self.JobModelClass, )
+            self.assertIsNotNone(job.job_id)
+            self.assertTrue(job.is_scheduled())
             data = {
-                'action': 'run_job_now',
+                'action': 'enqueue_job_now',
                 '_selected_action': [job.id, ],
             }
             model = job._meta.model.__name__.lower()
             url = reverse(f'admin:scheduler_{model}_changelist')
             # act
             res = self.client.post(url, data=data, follow=True)
-            # assert
-            entry = _get_job_from_queue(job)
-            job_model, job_id = entry.args
-            self.assertEqual(job_model, self.JobClass.__name__)
-            self.assertEqual(job_id, job.id)
+            # assert part 1
             self.assertEqual(200, res.status_code)
+            entry = _get_job_from_queue(job)
+            job_model, scheduled_job_id = entry.args
+            self.assertEqual(job_model, job.JOB_TYPE)
+            self.assertEqual(scheduled_job_id, job.id)
+            self.assertEqual('scheduled', entry.get_status())
+            self.assertTrue(has_execution_with_status(job, 'queued'))
+
+            # act 2
+            worker = create_worker('default')
+            worker.work(burst=True)
+
+            # assert 2
+            entry = _get_job_from_queue(job)
+            self.assertEqual(job_model, job.JOB_TYPE)
+            self.assertEqual(scheduled_job_id, job.id)
+            self.assertTrue(has_execution_with_status(job, 'finished'))
 
         def test_admin_enable_job(self):
             # arrange
             self.client.login(username='admin', password='admin')
-            job = job_factory(self.JobClass, enabled=False)
-            job.save()
+            job = job_factory(self.JobModelClass, enabled=False)
+            self.assertIsNone(job.job_id)
+            self.assertFalse(job.is_scheduled())
             data = {
                 'action': 'enable_selected',
                 '_selected_action': [job.id, ],
             }
             model = job._meta.model.__name__.lower()
             url = reverse(f'admin:scheduler_{model}_changelist')
             # act
             res = self.client.post(url, data=data, follow=True)
             # assert
             self.assertEqual(200, res.status_code)
-            job = self.JobClass.objects.filter(id=job.id).first()
+            job.refresh_from_db()
             self.assertTrue(job.enabled)
+            self.assertTrue(job.is_scheduled())
+            assert_response_has_msg(res, '1 job was successfully enabled and scheduled.')
 
         def test_admin_disable_job(self):
             # arrange
             self.client.login(username='admin', password='admin')
-            job = job_factory(self.JobClass, enabled=True)
+            job = job_factory(self.JobModelClass, enabled=True)
             job.save()
             data = {
                 'action': 'disable_selected',
                 '_selected_action': [job.id, ],
             }
             model = job._meta.model.__name__.lower()
             url = reverse(f'admin:scheduler_{model}_changelist')
+            self.assertTrue(job.is_scheduled())
             # act
             res = self.client.post(url, data=data, follow=True)
             # assert
             self.assertEqual(200, res.status_code)
-            job = self.JobClass.objects.filter(id=job.id).first()
+            job.refresh_from_db()
+            self.assertFalse(job.is_scheduled())
             self.assertFalse(job.enabled)
+            assert_response_has_msg(res, '1 job was successfully disabled and unscheduled.')
+
+        def test_admin_single_delete(self):
+            # arrange
+            self.client.login(username='admin', password='admin')
+            prev_count = self.JobModelClass.objects.count()
+            job = job_factory(self.JobModelClass, )
+            self.assertIsNotNone(job.job_id)
+            self.assertTrue(job.is_scheduled())
+            prev = len(_get_executions(job))
+            model = job._meta.model.__name__.lower()
+            url = reverse(f'admin:scheduler_{model}_delete', args=[job.pk, ])
+            data = {
+                'post': 'yes',
+            }
+            # act
+            res = self.client.post(url, data=data, follow=True)
+            # assert
+            self.assertEqual(200, res.status_code)
+            self.assertEqual(prev_count, self.JobModelClass.objects.count())
+            self.assertEquals(prev - 1, len(_get_executions(job)))
+
+        def test_admin_delete_selected(self):
+            # arrange
+            self.client.login(username='admin', password='admin')
+            job = job_factory(self.JobModelClass, enabled=True)
+            job.save()
+            queue = get_queue(job.queue)
+            scheduled_jobs = queue.scheduled_job_registry.get_job_ids()
+            job_id = job.job_id
+            self.assertIn(job_id, scheduled_jobs)
+            data = {
+                'action': 'delete_selected',
+                '_selected_action': [job.id, ],
+                'post': 'yes',
+            }
+            model = job._meta.model.__name__.lower()
+            url = reverse(f'admin:scheduler_{model}_changelist')
+            # act
+            res = self.client.post(url, data=data, follow=True)
+            # assert
+            self.assertEqual(200, res.status_code)
+            assert_response_has_msg(res, f'Successfully deleted 1 {self.JobModelClass._meta.verbose_name}.')
+            self.assertIsNone(self.JobModelClass.objects.filter(id=job.id).first())
+            scheduled_jobs = queue.scheduled_job_registry.get_job_ids()
+            self.assertNotIn(job_id, scheduled_jobs)
 
     class TestSchedulableJob(TestBaseJob):
         # Currently ScheduledJob and RepeatableJob
-        JobClass = ScheduledJob
+        JobModelClass = ScheduledJob
 
         def test_schedule_time_utc(self):
-            job = job_factory(self.JobClass)
+            job = job_factory(self.JobModelClass)
             est = zoneinfo.ZoneInfo('US/Eastern')
             scheduled_time = datetime(2016, 12, 25, 8, 0, 0, tzinfo=est)
             job.scheduled_time = scheduled_time
             utc = zoneinfo.ZoneInfo('UTC')
             expected = scheduled_time.astimezone(utc).isoformat()
             self.assertEqual(expected, job._schedule_time().isoformat())
 
         def test_result_ttl_passthrough(self):
-            job = job_factory(self.JobClass, result_ttl=500)
+            job = job_factory(self.JobModelClass, result_ttl=500)
             entry = _get_job_from_queue(job)
             self.assertEqual(entry.result_ttl, 500)
 
 
 class TestScheduledJob(BaseTestCases.TestSchedulableJob):
-    JobClass = ScheduledJob
+    JobModelClass = ScheduledJob
 
     def test_clean(self):
-        job = job_factory(self.JobClass)
+        job = job_factory(self.JobModelClass)
         job.queue = list(settings.RQ_QUEUES)[0]
         job.callable = 'scheduler.tests.jobs.test_job'
         self.assertIsNone(job.clean())
 
     def test_unschedulable_old_job(self):
-        job = job_factory(self.JobClass, scheduled_time=timezone.now() - timedelta(hours=1))
+        job = job_factory(self.JobModelClass, scheduled_time=timezone.now() - timedelta(hours=1))
         self.assertFalse(job.is_scheduled())
 
 
 class TestRepeatableJob(BaseTestCases.TestSchedulableJob):
-    JobClass = RepeatableJob
+    JobModelClass = RepeatableJob
 
     def test_unschedulable_old_job(self):
-        job = job_factory(self.JobClass, scheduled_time=timezone.now() - timedelta(hours=1), repeat=0)
+        job = job_factory(self.JobModelClass, scheduled_time=timezone.now() - timedelta(hours=1), repeat=0)
         self.assertFalse(job.is_scheduled())
 
     def test_schedulable_old_job_repeat_none(self):
         # If repeat is None, the job should be scheduled
-        job = job_factory(self.JobClass, scheduled_time=timezone.now() - timedelta(hours=1), repeat=None)
+        job = job_factory(self.JobModelClass, scheduled_time=timezone.now() - timedelta(hours=1), repeat=None)
         self.assertTrue(job.is_scheduled())
 
     def test_clean(self):
-        job = job_factory(self.JobClass)
+        job = job_factory(self.JobModelClass)
         job.queue = list(settings.RQ_QUEUES)[0]
         job.callable = 'scheduler.tests.jobs.test_job'
         job.interval = 1
         job.result_ttl = -1
         self.assertIsNone(job.clean())
 
     def test_clean_seconds(self):
-        job = job_factory(self.JobClass)
+        job = job_factory(self.JobModelClass)
         job.queue = list(settings.RQ_QUEUES)[0]
         job.callable = 'scheduler.tests.jobs.test_job'
         job.interval = 60
         job.result_ttl = -1
         job.interval_unit = 'seconds'
         self.assertIsNone(job.clean())
 
     def test_clean_too_frequent(self):
-        job = job_factory(self.JobClass)
+        job = job_factory(self.JobModelClass)
         job.queue = list(settings.RQ_QUEUES)[0]
         job.callable = 'scheduler.tests.jobs.test_job'
         job.interval = 10
         job.result_ttl = -1
         job.interval_unit = 'seconds'
         with self.assertRaises(ValidationError):
             job.clean_interval_unit()
 
     def test_clean_not_multiple(self):
-        job = job_factory(self.JobClass)
+        job = job_factory(self.JobModelClass)
         job.queue = list(settings.RQ_QUEUES)[0]
         job.callable = 'scheduler.tests.jobs.test_job'
         job.interval = 121
         job.interval_unit = 'seconds'
         with self.assertRaises(ValidationError):
             job.clean_interval_unit()
 
     def test_clean_short_result_ttl(self):
-        job = job_factory(self.JobClass)
+        job = job_factory(self.JobModelClass)
         job.queue = list(settings.RQ_QUEUES)[0]
         job.callable = 'scheduler.tests.jobs.test_job'
         job.interval = 1
         job.repeat = 1
         job.result_ttl = 3599
         job.interval_unit = 'hours'
         job.repeat = 42
         with self.assertRaises(ValidationError):
             job.clean_result_ttl()
 
     def test_clean_indefinite_result_ttl(self):
-        job = job_factory(self.JobClass)
+        job = job_factory(self.JobModelClass)
         job.queue = list(settings.RQ_QUEUES)[0]
         job.callable = 'scheduler.tests.jobs.test_job'
         job.interval = 1
         job.result_ttl = -1
         job.interval_unit = 'hours'
         job.clean_result_ttl()
 
     def test_clean_undefined_result_ttl(self):
-        job = job_factory(self.JobClass)
+        job = job_factory(self.JobModelClass)
         job.queue = list(settings.RQ_QUEUES)[0]
         job.callable = 'scheduler.tests.jobs.test_job'
         job.interval = 1
         job.interval_unit = 'hours'
         job.clean_result_ttl()
 
     def test_interval_seconds_weeks(self):
-        job = job_factory(self.JobClass, interval=2, interval_unit='weeks')
+        job = job_factory(self.JobModelClass, interval=2, interval_unit='weeks')
         self.assertEqual(1209600.0, job.interval_seconds())
 
     def test_interval_seconds_days(self):
-        job = job_factory(self.JobClass, interval=2, interval_unit='days')
+        job = job_factory(self.JobModelClass, interval=2, interval_unit='days')
         self.assertEqual(172800.0, job.interval_seconds())
 
     def test_interval_seconds_hours(self):
-        job = job_factory(self.JobClass, interval=2, interval_unit='hours')
+        job = job_factory(self.JobModelClass, interval=2, interval_unit='hours')
         self.assertEqual(7200.0, job.interval_seconds())
 
     def test_interval_seconds_minutes(self):
-        job = job_factory(self.JobClass, interval=15, interval_unit='minutes')
+        job = job_factory(self.JobModelClass, interval=15, interval_unit='minutes')
         self.assertEqual(900.0, job.interval_seconds())
 
     def test_interval_seconds_seconds(self):
         job = RepeatableJob(interval=15, interval_unit='seconds')
         self.assertEqual(15.0, job.interval_seconds())
 
     def test_interval_display(self):
-        job = job_factory(self.JobClass, interval=15, interval_unit='minutes')
+        job = job_factory(self.JobModelClass, interval=15, interval_unit='minutes')
         self.assertEqual(job.interval_display(), '15 minutes')
 
     def test_result_interval(self):
-        job = job_factory(self.JobClass, )
+        job = job_factory(self.JobModelClass, )
         entry = _get_job_from_queue(job)
         self.assertEqual(entry.meta['interval'], 3600)
 
     def test_repeat(self):
-        job = job_factory(self.JobClass, repeat=10)
+        job = job_factory(self.JobModelClass, repeat=10)
         entry = _get_job_from_queue(job)
         self.assertEqual(entry.meta['repeat'], 10)
 
     def test_repeat_old_job_exhausted(self):
         base_time = timezone.now()
-        job = job_factory(self.JobClass, scheduled_time=base_time - timedelta(hours=10), repeat=10)
+        job = job_factory(self.JobModelClass, scheduled_time=base_time - timedelta(hours=10), repeat=10)
         self.assertEqual(job.is_scheduled(), False)
 
     def test_repeat_old_job_last_iter(self):
         base_time = timezone.now()
-        job = job_factory(self.JobClass, scheduled_time=base_time - timedelta(hours=9, minutes=30), repeat=10)
+        job = job_factory(self.JobModelClass, scheduled_time=base_time - timedelta(hours=9, minutes=30), repeat=10)
         self.assertEqual(job.repeat, 0)
         self.assertEqual(job.is_scheduled(), True)
 
     def test_repeat_old_job_remaining(self):
         base_time = timezone.now()
-        job = job_factory(self.JobClass, scheduled_time=base_time - timedelta(minutes=30), repeat=5)
+        job = job_factory(self.JobModelClass, scheduled_time=base_time - timedelta(minutes=30), repeat=5)
         self.assertEqual(job.repeat, 4)
         self.assertEqual(job.scheduled_time, base_time + timedelta(minutes=30))
         self.assertEqual(job.is_scheduled(), True)
 
     def test_repeat_none_interval_2_min(self):
         base_time = timezone.now()
-        job = job_factory(self.JobClass, scheduled_time=base_time - timedelta(minutes=29), repeat=None)
+        job = job_factory(self.JobModelClass, scheduled_time=base_time - timedelta(minutes=29), repeat=None)
         job.interval = 120
         job.interval_unit = 'seconds'
         job.schedule()
         self.assertTrue(job.scheduled_time > base_time)
         self.assertTrue(job.is_scheduled())
 
     def test_check_rescheduled_after_execution(self):
-        job = job_factory(self.JobClass, scheduled_time=timezone.now() + timedelta(seconds=1))
+        job = job_factory(self.JobModelClass, scheduled_time=timezone.now() + timedelta(seconds=1))
         queue = job._get_rqueue()
         first_run_id = job.job_id
         entry = queue.fetch_job(first_run_id)
         queue.run_sync(entry)
         job.refresh_from_db()
         self.assertTrue(job.is_scheduled())
         self.assertNotEquals(job.job_id, first_run_id)
 
 
 class TestCronJob(BaseTestCases.TestBaseJob):
-    JobClass = CronJob
+    JobModelClass = CronJob
 
     def test_clean(self):
-        job = job_factory(self.JobClass)
+        job = job_factory(self.JobModelClass)
         job.cron_string = '* * * * *'
         job.queue = list(settings.RQ_QUEUES)[0]
         job.callable = 'scheduler.tests.jobs.test_job'
         self.assertIsNone(job.clean())
 
     def test_clean_cron_string_invalid(self):
-        job = job_factory(self.JobClass)
+        job = job_factory(self.JobModelClass)
         job.cron_string = 'not-a-cron-string'
         job.queue = list(settings.RQ_QUEUES)[0]
         job.callable = 'scheduler.tests.jobs.test_job'
         with self.assertRaises(ValidationError):
             job.clean_cron_string()
 
     def test_repeat(self):
-        job = job_factory(self.JobClass, repeat=10)
+        job = job_factory(self.JobModelClass, repeat=10)
         entry = _get_job_from_queue(job)
         self.assertEqual(entry.meta['repeat'], 10)
 
     def test_check_rescheduled_after_execution(self):
-        job = job_factory(self.JobClass, )
+        job = job_factory(self.JobModelClass, )
         queue = job._get_rqueue()
         first_run_id = job.job_id
         entry = queue.fetch_job(first_run_id)
         queue.run_sync(entry)
         job.refresh_from_db()
         self.assertTrue(job.is_scheduled())
         self.assertNotEquals(job.job_id, first_run_id)
```

### Comparing `django_rq_scheduler-2023.4.0/scheduler/tools.py` & `django_rq_scheduler-2023.5.0b1/scheduler/tools.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 import importlib
+import os
 
 import croniter
+import redis
 from django.apps import apps
-from django.conf import settings
 from django.utils import timezone
-from django_rq import job
 
-from scheduler import logger
-from scheduler.scheduler import DjangoRQScheduler
+from scheduler.decorators import job
+from scheduler.queues import get_queues, logger, get_queue
+from scheduler.rq_classes import DjangoWorker
 
 MODEL_NAMES = ['ScheduledJob', 'RepeatableJob', 'CronJob']
 
 
 def callable_func(callable_str: str):
     path = callable_str.split('.')
     module = importlib.import_module('.'.join(path[:-1]))
@@ -37,38 +38,62 @@
         enabled_jobs = model.objects.filter(enabled=True)
         unscheduled_jobs = filter(lambda j: not j.is_scheduled(), enabled_jobs)
         for item in unscheduled_jobs:
             logger.debug(f"Rescheduling {str(item)}")
             item.save()
 
 
-def start_scheduler_thread():
-    start_scheduler_as_thread = getattr(settings, 'SCHEDULER_THREAD', True)
-    if not start_scheduler_as_thread:
-        logger.info("Scheduler thread is turned off in the project settings")
-        logger.info("Make sure a scheduler is running")
-        return
-    if start_scheduler_as_thread:
-        interval = getattr(settings, 'SCHEDULER_INTERVAL', 60)
-        interval = max(1, interval)
-        if interval < 10:
-            logger.warn(
-                f"SCHEDULER_INTERVAL is set to {interval} - "
-                f"it is not recommended to have the interval less than 10 seconds")
-        scheduler = DjangoRQScheduler(interval=interval)
-        scheduler.start()
+def get_scheduled_job(task_model: str, task_id: int):
+    if task_model not in MODEL_NAMES:
+        raise ValueError(f'Job Model {task_model} does not exist, choices are {MODEL_NAMES}')
+    model = apps.get_model(app_label='scheduler', model_name=task_model)
+    task = model.objects.filter(id=task_id).first()
+    if task is None:
+        raise ValueError(f'Job {task_model}:{task_id} does not exit')
+    return task
 
 
-def run_job(job_model: str, job_id: int):
-    """Run a job
+def run_job(task_model: str, task_id: int):
+    """Run a scheduled job
     """
-    if job_model not in MODEL_NAMES:
-        raise ValueError(f'Job Model {job_model} does not exist, choices are {MODEL_NAMES}')
-    model = apps.get_model(app_label='scheduler', model_name=job_model)
-    job = model.objects.filter(id=job_id).first()
-    if job is None:
-        raise ValueError(f'Job {job_model}:{job_id} does not exit')
-    logger.debug(f'Running job {str(job)}')
-    args = job.parse_args()
-    kwargs = job.parse_kwargs()
-    res = job.callable_func()(*args, **kwargs)
+    scheduled_job = get_scheduled_job(task_model, task_id)
+    logger.debug(f'Running task {str(scheduled_job)}')
+    args = scheduled_job.parse_args()
+    kwargs = scheduled_job.parse_kwargs()
+    res = scheduled_job.callable_func()(*args, **kwargs)
+    return res
+
+
+def create_worker(*queue_names, **kwargs):
+    """
+    Returns a Django worker for all queues or specified ones.
+    """
+    queues = get_queues(*queue_names)
+    existing_workers = DjangoWorker.all(connection=queues[0].connection)
+    existing_worker_names = set(map(lambda w: w.name, existing_workers))
+    hostname = os.uname()[1]
+    c = 1
+    worker_name = f'{hostname}-worker:{c}'
+    while worker_name in existing_worker_names:
+        c += 1
+        worker_name = f'{hostname}-worker:{c}'
+    kwargs['name'] = worker_name
+    worker = DjangoWorker(queues, connection=queues[0].connection, **kwargs)
+    return worker
+
+
+def get_job_executions(queue_name, scheduled_job):
+    queue = get_queue(queue_name)
+    res = list()
+    try:
+        job_list = queue.get_jobs()
+    except redis.ConnectionError:
+        return res
+    res.extend(list(filter(lambda j: j.is_execution_of(scheduled_job), job_list)))
+    scheduled_job_id_list = queue.scheduled_job_registry.get_job_ids()
+
+    res.extend(list(
+        map(lambda j: j.to_json(),
+            filter(lambda j: j.is_execution_of(scheduled_job),
+                   map(queue.fetch_job, scheduled_job_id_list)
+                   ))))
     return res
```

### Comparing `django_rq_scheduler-2023.4.0/PKG-INFO` & `django_rq_scheduler-2023.5.0b1/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: django-rq-scheduler
-Version: 2023.4.0
-Summary: A database backed job scheduler for Django RQ with Django
+Version: 2023.5.0b1
+Summary: An async job scheduler for django using redis
 Home-page: https://github.com/dsoftwareinc/django-rq-scheduler
 License: MIT
 Keywords: redis,django,background-jobs,job-queue,task-queue,redis-queue,scheduled-jobs
 Author: Daniel Moran
 Author-email: daniel.maruani@gmail.com
 Maintainer: Daniel Moran
 Maintainer-email: daniel.maruani@gmail.com
@@ -13,29 +13,31 @@
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Environment :: Web Environment
 Classifier: Framework :: Django
 Classifier: Framework :: Django :: 3.2
 Classifier: Framework :: Django :: 4
 Classifier: Framework :: Django :: 4.0
 Classifier: Framework :: Django :: 4.1
+Classifier: Framework :: Django :: 4.2
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: 3.9
+Requires-Dist: click (>=8.1,<9.0)
 Requires-Dist: croniter (>=1.3,<2.0)
-Requires-Dist: django (>=3.2,<5)
+Requires-Dist: django (>=3.2)
 Requires-Dist: django-model-utils (>=4.3,<5.0)
-Requires-Dist: django-rq (>=2.7,<3.0)
+Requires-Dist: rq (>=1.13,<2.0)
 Project-URL: Bug Tracker, https://github.com/dsoftwareinc/django-rq-scheduler/issues
 Project-URL: Documentation, https://django-rq-scheduler.readthedocs.io/en/latest/
 Project-URL: Funding, https://github.com/sponsors/cunla
 Description-Content-Type: text/markdown
 
 Django RQ Scheduler
 ===================
```

