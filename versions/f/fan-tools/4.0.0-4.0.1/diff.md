# Comparing `tmp/fan_tools-4.0.0.tar.gz` & `tmp/fan_tools-4.0.1.tar.gz`

## Comparing `fan_tools-4.0.0.tar` & `fan_tools-4.0.1.tar`

### file list

```diff
@@ -1,132 +1,132 @@
--rw-r--r--   0        0        0      557 2020-02-02 00:00:00.000000 fan_tools-4.0.0/.editorconfig
--rw-r--r--   0        0        0      113 2020-02-02 00:00:00.000000 fan_tools-4.0.0/pytest.ini
--rw-r--r--   0        0        0       21 2020-02-02 00:00:00.000000 fan_tools-4.0.0/setup.cfg
--rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tox.ini
--rw-r--r--   0        0        0      290 2020-02-02 00:00:00.000000 fan_tools-4.0.0/.github/workflows/master.yml
--rw-r--r--   0        0        0      293 2020-02-02 00:00:00.000000 fan_tools-4.0.0/.github/workflows/test.yml
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/__init__.py
--rw-r--r--   0        0        0     2027 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/conftest.py
--rwxr-xr-x   0        0        0      957 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/manage.py
--rw-r--r--   0        0        0     5777 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/test_django.py
--rw-r--r--   0        0        0     6688 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/test_drf_validation.py
--rw-r--r--   0        0        0      741 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/test_ltree.py
--rw-r--r--   0        0        0      161 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/test_mail.py
--rw-r--r--   0        0        0      252 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/test_uri.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/__init__.py
--rw-r--r--   0        0        0       63 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/admin.py
--rw-r--r--   0        0        0       93 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/apps.py
--rw-r--r--   0        0        0     1204 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/models.py
--rw-r--r--   0        0        0      311 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/urls.py
--rw-r--r--   0        0        0     1439 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/views.py
--rw-r--r--   0        0        0     2244 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/migrations/0001_initial.py
--rw-r--r--   0        0        0      265 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/migrations/0002_ltree_extension.py
--rw-r--r--   0        0        0     2283 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/migrations/0003_auto_20190603_1218.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/migrations/__init__.py
--rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/templates/test_email_body.html
--rw-r--r--   0        0        0       45 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/templates/test_email_body.txt
--rw-r--r--   0        0        0       45 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleapp/templates/test_email_subject.txt
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleproj/__init__.py
--rw-r--r--   0        0        0     3682 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleproj/settings.py
--rw-r--r--   0        0        0      823 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleproj/urls.py
--rw-r--r--   0        0        0      397 2020-02-02 00:00:00.000000 fan_tools-4.0.0/django_tests/sampleproj/wsgi.py
--rw-r--r--   0        0        0      258 2020-02-02 00:00:00.000000 fan_tools-4.0.0/docs/development.md
--rw-r--r--   0        0        0     4086 2020-02-02 00:00:00.000000 fan_tools-4.0.0/docs/vector.toml
--rw-r--r--   0        0        0     1144 2020-02-02 00:00:00.000000 fan_tools-4.0.0/examples/send_dd_metric.py
--rw-r--r--   0        0        0     1329 2020-02-02 00:00:00.000000 fan_tools-4.0.0/examples/send_dd_metric.toml
--rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/__init__.py
--rw-r--r--   0        0        0     2769 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/aio_utils.py
--rw-r--r--   0        0        0      509 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/const.py
--rw-r--r--   0        0        0     3646 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/container_utils.py
--rw-r--r--   0        0        0     1935 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/file_utils.py
--rw-r--r--   0        0        0     3806 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/image_utils.py
--rw-r--r--   0        0        0     1077 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/metrics.py
--rw-r--r--   0        0        0      494 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/monitoring.py
--rw-r--r--   0        0        0     1650 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/profiler.py
--rw-r--r--   0        0        0      816 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/sentry.py
--rw-r--r--   0        0        0     5984 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/unix.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/aws/__init__.py
--rw-r--r--   0        0        0     4262 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/aws/lambda_cleanup.py
--rw-r--r--   0        0        0     2763 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/backup/__init__.py
--rw-r--r--   0        0        0      813 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/backup/gcloud.py
--rw-r--r--   0        0        0     1309 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/backup/s3.py
--rw-r--r--   0        0        0     2841 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/backup/utils.py
--rw-r--r--   0        0        0     1066 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/__init__.py
--rw-r--r--   0        0        0      138 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/fields.py
--rw-r--r--   0        0        0     1923 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/log_requests.py
--rw-r--r--   0        0        0     1604 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/mail.py
--rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/models.py
--rw-r--r--   0        0        0      142 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/url.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/contrib/__init__.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/contrib/postgres/__init__.py
--rw-r--r--   0        0        0     2678 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/contrib/postgres/indexes.py
--rw-r--r--   0        0        0     1172 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/contrib/postgres/models.py
--rw-r--r--   0        0        0      157 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/contrib/postgres/operations.py
--rw-r--r--   0        0        0       41 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/contrib/postgres/fields/__init__.py
--rw-r--r--   0        0        0     2177 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/contrib/postgres/fields/ltree.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/core/__init__.py
--rw-r--r--   0        0        0      890 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/core/management.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/db/__init__.py
--rw-r--r--   0        0        0      526 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/db/pgfields.py
--rw-r--r--   0        0        0      311 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/django/db/utils.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/doc_utils/__init__.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/doc_utils/fan_sphinx/__init__.py
--rwxr-xr-x   0        0        0     3218 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/doc_utils/fan_sphinx/dyn.py
--rw-r--r--   0        0        0     5627 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/doc_utils/fan_sphinx/dyn_json.py
--rw-r--r--   0        0        0     5585 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/doc_utils/fan_sphinx/dyn_serializer.py
--rw-r--r--   0        0        0     1708 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/doc_utils/fan_sphinx/http_log.py
--rw-r--r--   0        0        0        1 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/doc_utils/fan_sphinx/init.py
--rw-r--r--   0        0        0      634 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/doc_utils/fan_sphinx/parse_mixin.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/drf/__init__.py
--rw-r--r--   0        0        0      344 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/drf/asserts.py
--rw-r--r--   0        0        0     2787 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/drf/filters.py
--rw-r--r--   0        0        0     1100 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/drf/handlers.py
--rw-r--r--   0        0        0      787 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/drf/pagination.py
--rw-r--r--   0        0        0      764 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/drf/renderers.py
--rw-r--r--   0        0        0     1158 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/drf/serializers.py
--rw-r--r--   0        0        0     3770 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/drf/validation.py
--rw-r--r--   0        0        0     4107 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/fan_logging/__init__.py
--rw-r--r--   0        0        0    11054 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/fan_logging/handlers.py
--rw-r--r--   0        0        0     2389 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/mon_server/__init__.py
--rw-r--r--   0        0        0     1427 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/mon_server/certs.py
--rw-r--r--   0        0        0     1285 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/mon_server/gitlab_runners.py
--rw-r--r--   0        0        0        1 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/mon_server/tests/__init__.py
--rw-r--r--   0        0        0     1843 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/otel/__init__.py
--rw-r--r--   0        0        0     1032 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/otel/django.py
--rw-r--r--   0        0        0     1047 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/otel/jaeger_tracing.py
--rw-r--r--   0        0        0     1578 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/otel/log.py
--rw-r--r--   0        0        0     5014 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/python/__init__.py
--rw-r--r--   0        0        0     3409 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/python/decorators.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/scripts/__init__.py
--rwxr-xr-x   0        0        0     2169 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/scripts/fan_ci_script.py
--rw-r--r--   0        0        0     1176 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/scripts/fan_env_yaml.py
--rw-r--r--   0        0        0      633 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/scripts/fan_tools_wait.py
--rw-r--r--   0        0        0     1464 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/scripts/run_filebeat.py
--rw-r--r--   0        0        0      290 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/testing/__init__.py
--rw-r--r--   0        0        0     1175 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/testing/meta.py
--rw-r--r--   0        0        0     1452 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/testing/drf/__init__.py
--rw-r--r--   0        0        0     7432 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/testing/drf/base.py
--rw-r--r--   0        0        0     1669 2020-02-02 00:00:00.000000 fan_tools-4.0.0/fan_tools/testing/drf/proxy.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/__init__.py
--rw-r--r--   0        0        0       91 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/conftest.py
--rw-r--r--   0        0        0     3603 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/image.png
--rw-r--r--   0        0        0     1174 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_async.py
--rw-r--r--   0        0        0     1248 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_backups.py
--rw-r--r--   0        0        0     5271 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_common.py
--rw-r--r--   0        0        0      561 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_decorators.py
--rw-r--r--   0        0        0     3353 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_file_utils.py
--rw-r--r--   0        0        0      366 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_image_utils.py
--rw-r--r--   0        0        0      319 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_logging.py
--rw-r--r--   0        0        0      248 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_meta.py
--rw-r--r--   0        0        0     1644 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_metric_storage.py
--rw-r--r--   0        0        0     1431 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_metric_views.py
--rw-r--r--   0        0        0      907 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_metrics.py
--rw-r--r--   0        0        0     2143 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_mon_server.py
--rw-r--r--   0        0        0      723 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_rel_path.py
--rw-r--r--   0        0        0     2047 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_root_directory.py
--rw-r--r--   0        0        0      923 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_testing_helpers.py
--rw-r--r--   0        0        0      302 2020-02-02 00:00:00.000000 fan_tools-4.0.0/tests/test_unix.py
--rw-r--r--   0        0        0     1104 2020-02-02 00:00:00.000000 fan_tools-4.0.0/.gitignore
--rw-r--r--   0        0        0     1057 2020-02-02 00:00:00.000000 fan_tools-4.0.0/LICENSE
--rw-r--r--   0        0        0    16449 2020-02-02 00:00:00.000000 fan_tools-4.0.0/README.md
--rw-r--r--   0        0        0     3004 2020-02-02 00:00:00.000000 fan_tools-4.0.0/pyproject.toml
--rw-r--r--   0        0        0    18896 2020-02-02 00:00:00.000000 fan_tools-4.0.0/PKG-INFO
+-rw-r--r--   0        0        0      557 2020-02-02 00:00:00.000000 fan_tools-4.0.1/.editorconfig
+-rw-r--r--   0        0        0      113 2020-02-02 00:00:00.000000 fan_tools-4.0.1/pytest.ini
+-rw-r--r--   0        0        0       21 2020-02-02 00:00:00.000000 fan_tools-4.0.1/setup.cfg
+-rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tox.ini
+-rw-r--r--   0        0        0      290 2020-02-02 00:00:00.000000 fan_tools-4.0.1/.github/workflows/master.yml
+-rw-r--r--   0        0        0      293 2020-02-02 00:00:00.000000 fan_tools-4.0.1/.github/workflows/test.yml
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/__init__.py
+-rw-r--r--   0        0        0     2027 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/conftest.py
+-rwxr-xr-x   0        0        0      957 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/manage.py
+-rw-r--r--   0        0        0     5777 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/test_django.py
+-rw-r--r--   0        0        0     6688 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/test_drf_validation.py
+-rw-r--r--   0        0        0      741 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/test_ltree.py
+-rw-r--r--   0        0        0      161 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/test_mail.py
+-rw-r--r--   0        0        0      252 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/test_uri.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/__init__.py
+-rw-r--r--   0        0        0       63 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/admin.py
+-rw-r--r--   0        0        0       93 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/apps.py
+-rw-r--r--   0        0        0     1204 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/models.py
+-rw-r--r--   0        0        0      311 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/urls.py
+-rw-r--r--   0        0        0     1439 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/views.py
+-rw-r--r--   0        0        0     2244 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/migrations/0001_initial.py
+-rw-r--r--   0        0        0      265 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/migrations/0002_ltree_extension.py
+-rw-r--r--   0        0        0     2283 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/migrations/0003_auto_20190603_1218.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/migrations/__init__.py
+-rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/templates/test_email_body.html
+-rw-r--r--   0        0        0       45 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/templates/test_email_body.txt
+-rw-r--r--   0        0        0       45 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleapp/templates/test_email_subject.txt
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleproj/__init__.py
+-rw-r--r--   0        0        0     3682 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleproj/settings.py
+-rw-r--r--   0        0        0      823 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleproj/urls.py
+-rw-r--r--   0        0        0      397 2020-02-02 00:00:00.000000 fan_tools-4.0.1/django_tests/sampleproj/wsgi.py
+-rw-r--r--   0        0        0      258 2020-02-02 00:00:00.000000 fan_tools-4.0.1/docs/development.md
+-rw-r--r--   0        0        0     4086 2020-02-02 00:00:00.000000 fan_tools-4.0.1/docs/vector.toml
+-rw-r--r--   0        0        0     1144 2020-02-02 00:00:00.000000 fan_tools-4.0.1/examples/send_dd_metric.py
+-rw-r--r--   0        0        0     1329 2020-02-02 00:00:00.000000 fan_tools-4.0.1/examples/send_dd_metric.toml
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/__init__.py
+-rw-r--r--   0        0        0     2769 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/aio_utils.py
+-rw-r--r--   0        0        0      509 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/const.py
+-rw-r--r--   0        0        0     3646 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/container_utils.py
+-rw-r--r--   0        0        0     1935 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/file_utils.py
+-rw-r--r--   0        0        0     3806 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/image_utils.py
+-rw-r--r--   0        0        0     1077 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/metrics.py
+-rw-r--r--   0        0        0      494 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/monitoring.py
+-rw-r--r--   0        0        0     1650 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/profiler.py
+-rw-r--r--   0        0        0      816 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/sentry.py
+-rw-r--r--   0        0        0     5984 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/unix.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/aws/__init__.py
+-rw-r--r--   0        0        0     4262 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/aws/lambda_cleanup.py
+-rw-r--r--   0        0        0     2763 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/backup/__init__.py
+-rw-r--r--   0        0        0      813 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/backup/gcloud.py
+-rw-r--r--   0        0        0     1309 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/backup/s3.py
+-rw-r--r--   0        0        0     2841 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/backup/utils.py
+-rw-r--r--   0        0        0     1066 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/__init__.py
+-rw-r--r--   0        0        0      138 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/fields.py
+-rw-r--r--   0        0        0     1923 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/log_requests.py
+-rw-r--r--   0        0        0     1604 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/mail.py
+-rw-r--r--   0        0        0      750 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/models.py
+-rw-r--r--   0        0        0      142 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/url.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/contrib/__init__.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/contrib/postgres/__init__.py
+-rw-r--r--   0        0        0     2678 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/contrib/postgres/indexes.py
+-rw-r--r--   0        0        0     1172 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/contrib/postgres/models.py
+-rw-r--r--   0        0        0      157 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/contrib/postgres/operations.py
+-rw-r--r--   0        0        0       41 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/contrib/postgres/fields/__init__.py
+-rw-r--r--   0        0        0     2177 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/contrib/postgres/fields/ltree.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/core/__init__.py
+-rw-r--r--   0        0        0      890 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/core/management.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/db/__init__.py
+-rw-r--r--   0        0        0      526 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/db/pgfields.py
+-rw-r--r--   0        0        0      311 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/django/db/utils.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/doc_utils/__init__.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/doc_utils/fan_sphinx/__init__.py
+-rwxr-xr-x   0        0        0     3218 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/doc_utils/fan_sphinx/dyn.py
+-rw-r--r--   0        0        0     5627 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/doc_utils/fan_sphinx/dyn_json.py
+-rw-r--r--   0        0        0     5585 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/doc_utils/fan_sphinx/dyn_serializer.py
+-rw-r--r--   0        0        0     1708 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/doc_utils/fan_sphinx/http_log.py
+-rw-r--r--   0        0        0        1 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/doc_utils/fan_sphinx/init.py
+-rw-r--r--   0        0        0      634 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/doc_utils/fan_sphinx/parse_mixin.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/drf/__init__.py
+-rw-r--r--   0        0        0      344 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/drf/asserts.py
+-rw-r--r--   0        0        0     2787 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/drf/filters.py
+-rw-r--r--   0        0        0     1100 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/drf/handlers.py
+-rw-r--r--   0        0        0      787 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/drf/pagination.py
+-rw-r--r--   0        0        0      764 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/drf/renderers.py
+-rw-r--r--   0        0        0     1158 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/drf/serializers.py
+-rw-r--r--   0        0        0     3770 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/drf/validation.py
+-rw-r--r--   0        0        0     4107 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/fan_logging/__init__.py
+-rw-r--r--   0        0        0    11054 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/fan_logging/handlers.py
+-rw-r--r--   0        0        0     2389 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/mon_server/__init__.py
+-rw-r--r--   0        0        0     1427 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/mon_server/certs.py
+-rw-r--r--   0        0        0     1285 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/mon_server/gitlab_runners.py
+-rw-r--r--   0        0        0        1 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/mon_server/tests/__init__.py
+-rw-r--r--   0        0        0     1843 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/otel/__init__.py
+-rw-r--r--   0        0        0     1032 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/otel/django.py
+-rw-r--r--   0        0        0     1047 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/otel/jaeger_tracing.py
+-rw-r--r--   0        0        0     1578 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/otel/log.py
+-rw-r--r--   0        0        0     5014 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/python/__init__.py
+-rw-r--r--   0        0        0     3445 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/python/decorators.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/scripts/__init__.py
+-rwxr-xr-x   0        0        0     2169 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/scripts/fan_ci_script.py
+-rw-r--r--   0        0        0     1176 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/scripts/fan_env_yaml.py
+-rw-r--r--   0        0        0      633 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/scripts/fan_tools_wait.py
+-rw-r--r--   0        0        0     1464 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/scripts/run_filebeat.py
+-rw-r--r--   0        0        0      290 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/testing/__init__.py
+-rw-r--r--   0        0        0     1175 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/testing/meta.py
+-rw-r--r--   0        0        0     1452 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/testing/drf/__init__.py
+-rw-r--r--   0        0        0     7432 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/testing/drf/base.py
+-rw-r--r--   0        0        0     1669 2020-02-02 00:00:00.000000 fan_tools-4.0.1/fan_tools/testing/drf/proxy.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/__init__.py
+-rw-r--r--   0        0        0       91 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/conftest.py
+-rw-r--r--   0        0        0     3603 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/image.png
+-rw-r--r--   0        0        0     1174 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_async.py
+-rw-r--r--   0        0        0     1248 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_backups.py
+-rw-r--r--   0        0        0     5271 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_common.py
+-rw-r--r--   0        0        0      883 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_decorators.py
+-rw-r--r--   0        0        0     3353 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_file_utils.py
+-rw-r--r--   0        0        0      366 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_image_utils.py
+-rw-r--r--   0        0        0      319 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_logging.py
+-rw-r--r--   0        0        0      248 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_meta.py
+-rw-r--r--   0        0        0     1644 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_metric_storage.py
+-rw-r--r--   0        0        0     1431 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_metric_views.py
+-rw-r--r--   0        0        0      907 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_metrics.py
+-rw-r--r--   0        0        0     2143 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_mon_server.py
+-rw-r--r--   0        0        0      723 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_rel_path.py
+-rw-r--r--   0        0        0     2047 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_root_directory.py
+-rw-r--r--   0        0        0      923 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_testing_helpers.py
+-rw-r--r--   0        0        0      302 2020-02-02 00:00:00.000000 fan_tools-4.0.1/tests/test_unix.py
+-rw-r--r--   0        0        0     1104 2020-02-02 00:00:00.000000 fan_tools-4.0.1/.gitignore
+-rw-r--r--   0        0        0     1057 2020-02-02 00:00:00.000000 fan_tools-4.0.1/LICENSE
+-rw-r--r--   0        0        0    16449 2020-02-02 00:00:00.000000 fan_tools-4.0.1/README.md
+-rw-r--r--   0        0        0     3004 2020-02-02 00:00:00.000000 fan_tools-4.0.1/pyproject.toml
+-rw-r--r--   0        0        0    18896 2020-02-02 00:00:00.000000 fan_tools-4.0.1/PKG-INFO
```

### Comparing `fan_tools-4.0.0/.editorconfig` & `fan_tools-4.0.1/.editorconfig`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tox.ini` & `fan_tools-4.0.1/tox.ini`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/django_tests/conftest.py` & `fan_tools-4.0.1/django_tests/conftest.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/django_tests/manage.py` & `fan_tools-4.0.1/django_tests/manage.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/django_tests/test_django.py` & `fan_tools-4.0.1/django_tests/test_django.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/django_tests/test_drf_validation.py` & `fan_tools-4.0.1/django_tests/test_drf_validation.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/django_tests/test_ltree.py` & `fan_tools-4.0.1/django_tests/test_ltree.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/django_tests/sampleapp/models.py` & `fan_tools-4.0.1/django_tests/sampleapp/models.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/django_tests/sampleapp/views.py` & `fan_tools-4.0.1/django_tests/sampleapp/views.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/django_tests/sampleapp/migrations/0001_initial.py` & `fan_tools-4.0.1/django_tests/sampleapp/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/django_tests/sampleapp/migrations/0003_auto_20190603_1218.py` & `fan_tools-4.0.1/django_tests/sampleapp/migrations/0003_auto_20190603_1218.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/django_tests/sampleproj/settings.py` & `fan_tools-4.0.1/django_tests/sampleproj/settings.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/django_tests/sampleproj/urls.py` & `fan_tools-4.0.1/django_tests/sampleproj/urls.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/docs/vector.toml` & `fan_tools-4.0.1/docs/vector.toml`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/examples/send_dd_metric.py` & `fan_tools-4.0.1/examples/send_dd_metric.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/examples/send_dd_metric.toml` & `fan_tools-4.0.1/examples/send_dd_metric.toml`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/aio_utils.py` & `fan_tools-4.0.1/fan_tools/aio_utils.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/container_utils.py` & `fan_tools-4.0.1/fan_tools/container_utils.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/file_utils.py` & `fan_tools-4.0.1/fan_tools/file_utils.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/image_utils.py` & `fan_tools-4.0.1/fan_tools/image_utils.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/metrics.py` & `fan_tools-4.0.1/fan_tools/metrics.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/profiler.py` & `fan_tools-4.0.1/fan_tools/profiler.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/sentry.py` & `fan_tools-4.0.1/fan_tools/sentry.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/unix.py` & `fan_tools-4.0.1/fan_tools/unix.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/aws/lambda_cleanup.py` & `fan_tools-4.0.1/fan_tools/aws/lambda_cleanup.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/backup/__init__.py` & `fan_tools-4.0.1/fan_tools/backup/__init__.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/backup/gcloud.py` & `fan_tools-4.0.1/fan_tools/backup/gcloud.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/backup/s3.py` & `fan_tools-4.0.1/fan_tools/backup/s3.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/backup/utils.py` & `fan_tools-4.0.1/fan_tools/backup/utils.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/django/__init__.py` & `fan_tools-4.0.1/fan_tools/django/__init__.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/django/log_requests.py` & `fan_tools-4.0.1/fan_tools/django/log_requests.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/django/mail.py` & `fan_tools-4.0.1/fan_tools/django/mail.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/django/models.py` & `fan_tools-4.0.1/fan_tools/django/models.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/django/contrib/postgres/indexes.py` & `fan_tools-4.0.1/fan_tools/django/contrib/postgres/indexes.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/django/contrib/postgres/models.py` & `fan_tools-4.0.1/fan_tools/django/contrib/postgres/models.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/django/contrib/postgres/fields/ltree.py` & `fan_tools-4.0.1/fan_tools/django/contrib/postgres/fields/ltree.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/django/core/management.py` & `fan_tools-4.0.1/fan_tools/django/core/management.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/django/db/pgfields.py` & `fan_tools-4.0.1/fan_tools/django/db/pgfields.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/doc_utils/fan_sphinx/dyn.py` & `fan_tools-4.0.1/fan_tools/doc_utils/fan_sphinx/dyn.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/doc_utils/fan_sphinx/dyn_json.py` & `fan_tools-4.0.1/fan_tools/doc_utils/fan_sphinx/dyn_json.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/doc_utils/fan_sphinx/dyn_serializer.py` & `fan_tools-4.0.1/fan_tools/doc_utils/fan_sphinx/dyn_serializer.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/doc_utils/fan_sphinx/http_log.py` & `fan_tools-4.0.1/fan_tools/doc_utils/fan_sphinx/http_log.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/doc_utils/fan_sphinx/parse_mixin.py` & `fan_tools-4.0.1/fan_tools/doc_utils/fan_sphinx/parse_mixin.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/drf/filters.py` & `fan_tools-4.0.1/fan_tools/drf/filters.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/drf/handlers.py` & `fan_tools-4.0.1/fan_tools/drf/handlers.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/drf/pagination.py` & `fan_tools-4.0.1/fan_tools/drf/pagination.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/drf/renderers.py` & `fan_tools-4.0.1/fan_tools/drf/renderers.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/drf/serializers.py` & `fan_tools-4.0.1/fan_tools/drf/serializers.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/drf/validation.py` & `fan_tools-4.0.1/fan_tools/drf/validation.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/fan_logging/__init__.py` & `fan_tools-4.0.1/fan_tools/fan_logging/__init__.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/fan_logging/handlers.py` & `fan_tools-4.0.1/fan_tools/fan_logging/handlers.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/mon_server/__init__.py` & `fan_tools-4.0.1/fan_tools/mon_server/__init__.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/mon_server/certs.py` & `fan_tools-4.0.1/fan_tools/mon_server/certs.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/mon_server/gitlab_runners.py` & `fan_tools-4.0.1/fan_tools/mon_server/gitlab_runners.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/otel/__init__.py` & `fan_tools-4.0.1/fan_tools/otel/__init__.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/otel/django.py` & `fan_tools-4.0.1/fan_tools/otel/django.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/otel/jaeger_tracing.py` & `fan_tools-4.0.1/fan_tools/otel/jaeger_tracing.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/otel/log.py` & `fan_tools-4.0.1/fan_tools/otel/log.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/python/__init__.py` & `fan_tools-4.0.1/fan_tools/python/__init__.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/python/decorators.py` & `fan_tools-4.0.1/fan_tools/python/decorators.py`

 * *Files 1% similar despite different names*

```diff
@@ -106,8 +106,9 @@
 
         wrapper.reset_cache = self.reset_cache  # type: ignore
 
         return wrapper
 
     def reset_cache(self):
         self.cache = self._default
-        self.fname.unlink()
+        if self.fname.exists():
+            self.fname.unlink()
```

### Comparing `fan_tools-4.0.0/fan_tools/scripts/fan_ci_script.py` & `fan_tools-4.0.1/fan_tools/scripts/fan_ci_script.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/scripts/fan_env_yaml.py` & `fan_tools-4.0.1/fan_tools/scripts/fan_env_yaml.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/scripts/fan_tools_wait.py` & `fan_tools-4.0.1/fan_tools/scripts/fan_tools_wait.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/scripts/run_filebeat.py` & `fan_tools-4.0.1/fan_tools/scripts/run_filebeat.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/testing/meta.py` & `fan_tools-4.0.1/fan_tools/testing/meta.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/testing/drf/__init__.py` & `fan_tools-4.0.1/fan_tools/testing/drf/__init__.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/testing/drf/base.py` & `fan_tools-4.0.1/fan_tools/testing/drf/base.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/fan_tools/testing/drf/proxy.py` & `fan_tools-4.0.1/fan_tools/testing/drf/proxy.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tests/image.png` & `fan_tools-4.0.1/tests/image.png`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tests/test_async.py` & `fan_tools-4.0.1/tests/test_async.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tests/test_backups.py` & `fan_tools-4.0.1/tests/test_backups.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tests/test_common.py` & `fan_tools-4.0.1/tests/test_common.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tests/test_decorators.py` & `fan_tools-4.0.1/tests/test_decorators.py`

 * *Files 12% similar despite different names*

```diff
@@ -17,7 +17,20 @@
         assert not fname.exists()
         await func()
         assert fname.exists()
         assert fname.read_text() == '{"a": "b"}'
 
         func.reset_cache()
         assert not fname.exists()
+
+    def test_02_unlink(self, tmp_path):
+        fname = tmp_path / 'cache.json'
+        model = MagicMock()
+
+        model.json.return_value = '{"a": "b"}'
+
+        @cache_async[type(dict)](fname, model, {})
+        async def func():
+            return model
+
+        assert not fname.exists()
+        func.reset_cache()
```

### Comparing `fan_tools-4.0.0/tests/test_file_utils.py` & `fan_tools-4.0.1/tests/test_file_utils.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tests/test_metric_storage.py` & `fan_tools-4.0.1/tests/test_metric_storage.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tests/test_metric_views.py` & `fan_tools-4.0.1/tests/test_metric_views.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tests/test_metrics.py` & `fan_tools-4.0.1/tests/test_metrics.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tests/test_mon_server.py` & `fan_tools-4.0.1/tests/test_mon_server.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tests/test_rel_path.py` & `fan_tools-4.0.1/tests/test_rel_path.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tests/test_root_directory.py` & `fan_tools-4.0.1/tests/test_root_directory.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/tests/test_testing_helpers.py` & `fan_tools-4.0.1/tests/test_testing_helpers.py`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/.gitignore` & `fan_tools-4.0.1/.gitignore`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/LICENSE` & `fan_tools-4.0.1/LICENSE`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/README.md` & `fan_tools-4.0.1/README.md`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/pyproject.toml` & `fan_tools-4.0.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `fan_tools-4.0.0/PKG-INFO` & `fan_tools-4.0.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fan-tools
-Version: 4.0.0
+Version: 4.0.1
 Summary: Various python stuff: testing, aio helpers, etc
 Project-URL: github, http://github.com/micro-fan/fan_tools
 Author-email: cybergrind <cybergind+pypi@gmail.com>
 License-File: LICENSE
 Keywords: asyncio,testing
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

