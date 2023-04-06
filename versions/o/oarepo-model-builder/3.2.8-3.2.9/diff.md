# Comparing `tmp/oarepo-model-builder-3.2.8.tar.gz` & `tmp/oarepo-model-builder-3.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "oarepo-model-builder-3.2.8.tar", last modified: Tue Feb 21 14:04:16 2023, max compression
+gzip compressed data, was "oarepo-model-builder-3.2.9.tar", last modified: Tue Feb 21 14:30:37 2023, max compression
```

## Comparing `oarepo-model-builder-3.2.8.tar` & `oarepo-model-builder-3.2.9.tar`

### file list

```diff
@@ -1,198 +1,198 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.758866 oarepo-model-builder-3.2.8/
--rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      785 2023-02-21 14:04:16.758866 oarepo-model-builder-3.2.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      508 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.726866 oarepo-model-builder-3.2.8/oarepo_model_builder/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8646 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.730866 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/
--rw-r--r--   0 runner    (1001) docker     (123)     5961 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      978 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/extend.py
--rw-r--r--   0 runner    (1001) docker     (123)     1512 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/json_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1857 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/jsonschema.py
--rw-r--r--   0 runner    (1001) docker     (123)     2342 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/mapping.py
--rw-r--r--   0 runner    (1001) docker     (123)     2951 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/model_saver.py
--rw-r--r--   0 runner    (1001) docker     (123)      541 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/pyproject_toml.py
--rw-r--r--   0 runner    (1001) docker     (123)      646 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/python.py
--rw-r--r--   0 runner    (1001) docker     (123)      630 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/python_structure.py
--rw-r--r--   0 runner    (1001) docker     (123)     2562 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/setup_cfg.py
--rw-r--r--   0 runner    (1001) docker     (123)      398 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/setup_py.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.730866 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/templates/
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/templates/setup.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)     1060 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builders/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.730866 oarepo-model-builder-3.2.8/oarepo_model_builder/builtin_models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builtin_models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1012 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/builtin_models/invenio.json
--rw-r--r--   0 runner    (1001) docker     (123)     6774 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     4575 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/conflict_resolvers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.730866 oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/
--rw-r--r--   0 runner    (1001) docker     (123)     1355 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8579 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/containers.py
--rw-r--r--   0 runner    (1001) docker     (123)     2597 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/datatypes.py
--rw-r--r--   0 runner    (1001) docker     (123)     3418 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/dates.py
--rw-r--r--   0 runner    (1001) docker     (123)     2829 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/primitive_types.py
--rw-r--r--   0 runner    (1001) docker     (123)     2957 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/strings.py
--rw-r--r--   0 runner    (1001) docker     (123)     5401 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/entrypoints.py
--rw-r--r--   0 runner    (1001) docker     (123)      126 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2275 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/fs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.734866 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/
--rw-r--r--   0 runner    (1001) docker     (123)     1189 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1244 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_base.py
--rw-r--r--   0 runner    (1001) docker     (123)      194 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_cli.py
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_cli_setup_cfg.py
--rw-r--r--   0 runner    (1001) docker     (123)      209 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_config.py
--rw-r--r--   0 runner    (1001) docker     (123)      191 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_ext.py
--rw-r--r--   0 runner    (1001) docker     (123)      838 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_ext_setup_cfg.py
--rw-r--r--   0 runner    (1001) docker     (123)      218 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_proxies.py
--rw-r--r--   0 runner    (1001) docker     (123)      234 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record.py
--rw-r--r--   0 runner    (1001) docker     (123)      230 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_dumper.py
--rw-r--r--   0 runner    (1001) docker     (123)      507 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_jsonschemas_setup_cfg.py
--rw-r--r--   0 runner    (1001) docker     (123)      238 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     2163 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_metadata_alembic_setup_cfg.py
--rw-r--r--   0 runner    (1001) docker     (123)      628 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_metadata_models_setup_cfg.py
--rw-r--r--   0 runner    (1001) docker     (123)      250 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_permissions.py
--rw-r--r--   0 runner    (1001) docker     (123)      238 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_resource.py
--rw-r--r--   0 runner    (1001) docker     (123)      265 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_resource_config.py
--rw-r--r--   0 runner    (1001) docker     (123)      706 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_resource_setup_cfg.py
--rw-r--r--   0 runner    (1001) docker     (123)    12930 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     8526 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_search.py
--rw-r--r--   0 runner    (1001) docker     (123)      485 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_search_setup_cfg.py
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_service.py
--rw-r--r--   0 runner    (1001) docker     (123)      947 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_service_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     6647 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_script_sample_data.py
--rw-r--r--   0 runner    (1001) docker     (123)      538 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_version.py
--rw-r--r--   0 runner    (1001) docker     (123)      213 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.738866 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/
--rw-r--r--   0 runner    (1001) docker     (123)      428 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/imports.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)     2551 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_cli.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      960 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_config.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)     2547 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_ext.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      451 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_proxies.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)     1588 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      440 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_dumper.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      382 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_facets.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      635 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_metadata.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      773 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_permissions.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      505 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_resource.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      975 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_resource_config.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      671 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_schema.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)     1140 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_search_options.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      492 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_service.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)     2579 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_service_config.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)       93 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_version.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)     1692 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_views.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      915 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/script_import_sample_data.py.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      106 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/script_import_sample_data.sh.jinja2
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.738866 oarepo-model-builder-3.2.8/oarepo_model_builder/loaders/
--rw-r--r--   0 runner    (1001) docker     (123)      584 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/loaders/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4428 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/merger.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.742866 oarepo-model-builder-3.2.8/oarepo_model_builder/model_preprocessors/
--rw-r--r--   0 runner    (1001) docker     (123)      953 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/model_preprocessors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3110 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/model_preprocessors/default_values.py
--rw-r--r--   0 runner    (1001) docker     (123)      761 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/model_preprocessors/extend.py
--rw-r--r--   0 runner    (1001) docker     (123)    10725 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/model_preprocessors/invenio.py
--rw-r--r--   0 runner    (1001) docker     (123)     1293 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/model_preprocessors/invenio_base_classes.py
--rw-r--r--   0 runner    (1001) docker     (123)      355 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/model_preprocessors/opensearch.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.742866 oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/
--rw-r--r--   0 runner    (1001) docker     (123)      452 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2922 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/cfg.py
--rw-r--r--   0 runner    (1001) docker     (123)     1039 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/diff.py
--rw-r--r--   0 runner    (1001) docker     (123)     1537 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/json.py
--rw-r--r--   0 runner    (1001) docker     (123)     2352 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/json_stack.py
--rw-r--r--   0 runner    (1001) docker     (123)      769 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/jsonschema.py
--rw-r--r--   0 runner    (1001) docker     (123)      171 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/mapping.py
--rw-r--r--   0 runner    (1001) docker     (123)     3714 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/python.py
--rw-r--r--   0 runner    (1001) docker     (123)      607 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/text.py
--rw-r--r--   0 runner    (1001) docker     (123)     3154 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/toml.py
--rw-r--r--   0 runner    (1001) docker     (123)     1911 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/yaml.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.742866 oarepo-model-builder-3.2.8/oarepo_model_builder/profiles/
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/profiles/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/profiles/extend.py
--rw-r--r--   0 runner    (1001) docker     (123)     2936 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/profiles/model.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.746866 oarepo-model-builder-3.2.8/oarepo_model_builder/property_preprocessors/
--rw-r--r--   0 runner    (1001) docker     (123)     3519 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/property_preprocessors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3448 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/property_preprocessors/datatype_preprocessor.py
--rw-r--r--   0 runner    (1001) docker     (123)     2120 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/property_preprocessors/enum.py
--rw-r--r--   0 runner    (1001) docker     (123)     1687 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/property_preprocessors/extend.py
--rw-r--r--   0 runner    (1001) docker     (123)    10222 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/schema.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.746866 oarepo-model-builder-3.2.8/oarepo_model_builder/stack/
--rw-r--r--   0 runner    (1001) docker     (123)      154 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/stack/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3887 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/stack/schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     2940 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/stack/stack.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.746866 oarepo-model-builder-3.2.8/oarepo_model_builder/templates/
--rw-r--r--   0 runner    (1001) docker     (123)     1259 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/templates/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.746866 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      300 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/camelcase.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.750866 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1894 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/call.py
--rw-r--r--   0 runner    (1001) docker     (123)     3413 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/collections.py
--rw-r--r--   0 runner    (1001) docker     (123)     5833 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/common.py
--rw-r--r--   0 runner    (1001) docker     (123)     3988 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/indented_nodes.py
--rw-r--r--   0 runner    (1001) docker     (123)     2009 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/mergers.py
--rw-r--r--   0 runner    (1001) docker     (123)     2220 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/simple_nodes.py
--rw-r--r--   0 runner    (1001) docker     (123)     1763 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/deepmerge.py
--rw-r--r--   0 runner    (1001) docker     (123)      460 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/facet_helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)      761 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/hyphen_munch.py
--rw-r--r--   0 runner    (1001) docker     (123)      634 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/jinja.py
--rw-r--r--   0 runner    (1001) docker     (123)     4820 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/json_pathlib.py
--rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/python_name.py
--rw-r--r--   0 runner    (1001) docker     (123)     1321 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/utils/verbose.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.754866 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/
--rw-r--r--   0 runner    (1001) docker     (123)     1334 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1052 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/model.py
--rw-r--r--   0 runner    (1001) docker     (123)    10886 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/model_defaults.py
--rw-r--r--   0 runner    (1001) docker     (123)      926 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/model_plugins.py
--rw-r--r--   0 runner    (1001) docker     (123)     3423 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/model_validation.py
--rw-r--r--   0 runner    (1001) docker     (123)     3919 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/properties.py
--rw-r--r--   0 runner    (1001) docker     (123)     2069 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/property.py
--rw-r--r--   0 runner    (1001) docker     (123)      268 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/property_facets.py
--rw-r--r--   0 runner    (1001) docker     (123)      210 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/property_jsonschema.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/property_mapping.py
--rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/property_marshmallow.py
--rw-r--r--   0 runner    (1001) docker     (123)      528 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/property_sample_data.py
--rw-r--r--   0 runner    (1001) docker     (123)      323 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/property_sortable.py
--rw-r--r--   0 runner    (1001) docker     (123)     5191 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/registration.py
--rw-r--r--   0 runner    (1001) docker     (123)      512 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/root.py
--rw-r--r--   0 runner    (1001) docker     (123)      868 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/settings.py
--rw-r--r--   0 runner    (1001) docker     (123)     4276 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/oarepo_model_builder/validation/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.726866 oarepo-model-builder-3.2.8/oarepo_model_builder.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      785 2023-02-21 14:04:16.000000 oarepo-model-builder-3.2.8/oarepo_model_builder.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     7952 2023-02-21 14:04:16.000000 oarepo-model-builder-3.2.8/oarepo_model_builder.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-21 14:04:16.000000 oarepo-model-builder-3.2.8/oarepo_model_builder.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)     7152 2023-02-21 14:04:16.000000 oarepo-model-builder-3.2.8/oarepo_model_builder.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      398 2023-02-21 14:04:16.000000 oarepo-model-builder-3.2.8/oarepo_model_builder.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       21 2023-02-21 14:04:16.000000 oarepo-model-builder-3.2.8/oarepo_model_builder.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      102 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     8293 2023-02-21 14:04:16.762866 oarepo-model-builder-3.2.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:04:16.758866 oarepo-model-builder-3.2.8/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      948 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)     5328 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_builder_from_entrypoints.py
--rw-r--r--   0 runner    (1001) docker     (123)     1268 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_dependencies.py
--rw-r--r--   0 runner    (1001) docker     (123)      892 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_empty_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)    15218 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_facets.py
--rw-r--r--   0 runner    (1001) docker     (123)     3639 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_fulltext_keyword.py
--rw-r--r--   0 runner    (1001) docker     (123)      675 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_is_schema_element.py
--rw-r--r--   0 runner    (1001) docker     (123)     1492 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_json_pathlib.py
--rw-r--r--   0 runner    (1001) docker     (123)      412 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_json_stack.py
--rw-r--r--   0 runner    (1001) docker     (123)     4621 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_jsonchema_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)      687 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_jsonschema_output.py
--rw-r--r--   0 runner    (1001) docker     (123)     2156 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_loading.py
--rw-r--r--   0 runner    (1001) docker     (123)     3766 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_mapping_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)    12182 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_marshmallow_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)      704 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_merge.py
--rw-r--r--   0 runner    (1001) docker     (123)    17511 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_model_saver.py
--rw-r--r--   0 runner    (1001) docker     (123)      909 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_overwrite.py
--rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_plugin_configuration.py
--rw-r--r--   0 runner    (1001) docker     (123)    10744 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_python_mergers.py
--rw-r--r--   0 runner    (1001) docker     (123)     2577 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_raw.py
--rw-r--r--   0 runner    (1001) docker     (123)     4136 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_sample_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)     2716 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_schema_props.py
--rw-r--r--   0 runner    (1001) docker     (123)     3344 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_search_options.py
--rw-r--r--   0 runner    (1001) docker     (123)     5197 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_shortcuts.py
--rw-r--r--   0 runner    (1001) docker     (123)      515 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_stack.py
--rw-r--r--   0 runner    (1001) docker     (123)      468 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_template_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)     2540 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_type_shortcuts.py
--rw-r--r--   0 runner    (1001) docker     (123)     1886 2023-02-21 14:03:17.000000 oarepo-model-builder-3.2.8/tests/test_validation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.742198 oarepo-model-builder-3.2.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      785 2023-02-21 14:30:37.742198 oarepo-model-builder-3.2.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      508 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.706197 oarepo-model-builder-3.2.9/oarepo_model_builder/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8642 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.710198 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/
+-rw-r--r--   0 runner    (1001) docker     (123)     5961 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      978 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/extend.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1512 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/json_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1857 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/jsonschema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2342 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/mapping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2951 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/model_saver.py
+-rw-r--r--   0 runner    (1001) docker     (123)      541 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/pyproject_toml.py
+-rw-r--r--   0 runner    (1001) docker     (123)      646 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/python.py
+-rw-r--r--   0 runner    (1001) docker     (123)      630 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/python_structure.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2562 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/setup_cfg.py
+-rw-r--r--   0 runner    (1001) docker     (123)      398 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/setup_py.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.710198 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/templates/
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/templates/setup.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)     1060 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builders/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.714197 oarepo-model-builder-3.2.9/oarepo_model_builder/builtin_models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builtin_models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1012 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/builtin_models/invenio.json
+-rw-r--r--   0 runner    (1001) docker     (123)     6655 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4575 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/conflict_resolvers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.714197 oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/
+-rw-r--r--   0 runner    (1001) docker     (123)     1320 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8715 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/containers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2595 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/datatypes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3415 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/dates.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2826 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/primitive_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2949 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/strings.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5401 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/entrypoints.py
+-rw-r--r--   0 runner    (1001) docker     (123)      126 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2275 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/fs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.718197 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/
+-rw-r--r--   0 runner    (1001) docker     (123)     1189 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1244 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      194 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_cli_setup_cfg.py
+-rw-r--r--   0 runner    (1001) docker     (123)      209 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      191 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_ext.py
+-rw-r--r--   0 runner    (1001) docker     (123)      838 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_ext_setup_cfg.py
+-rw-r--r--   0 runner    (1001) docker     (123)      218 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_proxies.py
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record.py
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_dumper.py
+-rw-r--r--   0 runner    (1001) docker     (123)      507 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_jsonschemas_setup_cfg.py
+-rw-r--r--   0 runner    (1001) docker     (123)      238 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2163 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_metadata_alembic_setup_cfg.py
+-rw-r--r--   0 runner    (1001) docker     (123)      628 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_metadata_models_setup_cfg.py
+-rw-r--r--   0 runner    (1001) docker     (123)      250 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_permissions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      238 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_resource.py
+-rw-r--r--   0 runner    (1001) docker     (123)      265 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_resource_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      706 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_resource_setup_cfg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12853 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9405 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_search.py
+-rw-r--r--   0 runner    (1001) docker     (123)      485 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_search_setup_cfg.py
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_service.py
+-rw-r--r--   0 runner    (1001) docker     (123)      947 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_service_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6647 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_script_sample_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)      538 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)      213 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.722197 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/
+-rw-r--r--   0 runner    (1001) docker     (123)      428 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/imports.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)     2551 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_cli.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      960 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_config.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)     2547 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_ext.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      451 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_proxies.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)     1588 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      440 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_dumper.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      382 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_facets.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      635 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_metadata.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      773 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_permissions.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      505 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_resource.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      975 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_resource_config.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      671 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_schema.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)     1140 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_search_options.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      492 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_service.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)     2579 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_service_config.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)       93 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_version.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)     1692 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_views.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      915 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/script_import_sample_data.py.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      106 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/script_import_sample_data.sh.jinja2
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.722197 oarepo-model-builder-3.2.9/oarepo_model_builder/loaders/
+-rw-r--r--   0 runner    (1001) docker     (123)      584 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/loaders/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4428 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/merger.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.726198 oarepo-model-builder-3.2.9/oarepo_model_builder/model_preprocessors/
+-rw-r--r--   0 runner    (1001) docker     (123)      953 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/model_preprocessors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3110 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/model_preprocessors/default_values.py
+-rw-r--r--   0 runner    (1001) docker     (123)      761 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/model_preprocessors/extend.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10725 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/model_preprocessors/invenio.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1293 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/model_preprocessors/invenio_base_classes.py
+-rw-r--r--   0 runner    (1001) docker     (123)      355 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/model_preprocessors/opensearch.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.726198 oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/
+-rw-r--r--   0 runner    (1001) docker     (123)      452 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2922 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/cfg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1039 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/diff.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1537 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/json.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2352 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/json_stack.py
+-rw-r--r--   0 runner    (1001) docker     (123)      769 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/jsonschema.py
+-rw-r--r--   0 runner    (1001) docker     (123)      171 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/mapping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3641 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/python.py
+-rw-r--r--   0 runner    (1001) docker     (123)      607 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/text.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3154 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/toml.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1911 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/yaml.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.730198 oarepo-model-builder-3.2.9/oarepo_model_builder/profiles/
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/profiles/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/profiles/extend.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2888 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/profiles/model.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.730198 oarepo-model-builder-3.2.9/oarepo_model_builder/property_preprocessors/
+-rw-r--r--   0 runner    (1001) docker     (123)     3519 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/property_preprocessors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3392 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/property_preprocessors/datatype_preprocessor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2067 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/property_preprocessors/enum.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1634 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/property_preprocessors/extend.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10222 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/schema.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.730198 oarepo-model-builder-3.2.9/oarepo_model_builder/stack/
+-rw-r--r--   0 runner    (1001) docker     (123)      154 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/stack/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3887 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/stack/schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2940 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/stack/stack.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.730198 oarepo-model-builder-3.2.9/oarepo_model_builder/templates/
+-rw-r--r--   0 runner    (1001) docker     (123)     1259 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/templates/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.730198 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      300 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/camelcase.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.734197 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1894 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/call.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3413 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/collections.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5833 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3988 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/indented_nodes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1971 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/mergers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2197 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/simple_nodes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1763 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/deepmerge.py
+-rw-r--r--   0 runner    (1001) docker     (123)      498 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/facet_helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)      761 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/hyphen_munch.py
+-rw-r--r--   0 runner    (1001) docker     (123)      634 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/jinja.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4820 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/json_pathlib.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1131 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/python_name.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1321 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/utils/verbose.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.738197 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/
+-rw-r--r--   0 runner    (1001) docker     (123)     1334 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1052 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/model.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10886 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/model_defaults.py
+-rw-r--r--   0 runner    (1001) docker     (123)      926 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/model_plugins.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3423 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/model_validation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3919 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/properties.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2069 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/property.py
+-rw-r--r--   0 runner    (1001) docker     (123)      268 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/property_facets.py
+-rw-r--r--   0 runner    (1001) docker     (123)      210 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/property_jsonschema.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/property_mapping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/property_marshmallow.py
+-rw-r--r--   0 runner    (1001) docker     (123)      528 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/property_sample_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)      323 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/property_sortable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5111 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/registration.py
+-rw-r--r--   0 runner    (1001) docker     (123)      512 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/root.py
+-rw-r--r--   0 runner    (1001) docker     (123)      868 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/settings.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4276 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/oarepo_model_builder/validation/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.710198 oarepo-model-builder-3.2.9/oarepo_model_builder.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      785 2023-02-21 14:30:37.000000 oarepo-model-builder-3.2.9/oarepo_model_builder.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     7952 2023-02-21 14:30:37.000000 oarepo-model-builder-3.2.9/oarepo_model_builder.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-21 14:30:37.000000 oarepo-model-builder-3.2.9/oarepo_model_builder.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     7152 2023-02-21 14:30:37.000000 oarepo-model-builder-3.2.9/oarepo_model_builder.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      398 2023-02-21 14:30:37.000000 oarepo-model-builder-3.2.9/oarepo_model_builder.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       21 2023-02-21 14:30:37.000000 oarepo-model-builder-3.2.9/oarepo_model_builder.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      102 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     8293 2023-02-21 14:30:37.742198 oarepo-model-builder-3.2.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-21 14:30:37.742198 oarepo-model-builder-3.2.9/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      948 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5280 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_builder_from_entrypoints.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1220 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_dependencies.py
+-rw-r--r--   0 runner    (1001) docker     (123)      844 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_empty_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14864 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_facets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3648 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_fulltext_keyword.py
+-rw-r--r--   0 runner    (1001) docker     (123)      675 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_is_schema_element.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1492 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_json_pathlib.py
+-rw-r--r--   0 runner    (1001) docker     (123)      412 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_json_stack.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4593 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_jsonchema_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)      687 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_jsonschema_output.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2156 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_loading.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3738 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_mapping_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12188 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_marshmallow_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)      704 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_merge.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17496 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_model_saver.py
+-rw-r--r--   0 runner    (1001) docker     (123)      861 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_overwrite.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_plugin_configuration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10744 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_python_mergers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2529 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_raw.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4139 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_sample_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2668 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_schema_props.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3342 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_search_options.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5149 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_shortcuts.py
+-rw-r--r--   0 runner    (1001) docker     (123)      515 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_stack.py
+-rw-r--r--   0 runner    (1001) docker     (123)      468 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_template_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2543 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_type_shortcuts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1886 2023-02-21 14:29:40.000000 oarepo-model-builder-3.2.9/tests/test_validation.py
```

### Comparing `oarepo-model-builder-3.2.8/LICENSE` & `oarepo-model-builder-3.2.9/LICENSE`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/PKG-INFO` & `oarepo-model-builder-3.2.9/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: oarepo-model-builder
-Version: 3.2.8
+Version: 3.2.9
 Summary: A utility library that generates OARepo required data model files from a JSON specification file
 Description-Content-Type: text/markdown
 Provides-Extra: devs
 Provides-Extra: tests
 License-File: LICENSE
 
 # OARepo model builder
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builder.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builder.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,16 +2,20 @@
 import importlib
 import json
 from pathlib import Path
 from typing import Dict, List, Type, Union
 
 import yaml
 
-from .builders import (ModelBuilderStack, OutputBuilder,
-                       OutputBuilderComponent, ReplaceElement)
+from .builders import (
+    ModelBuilderStack,
+    OutputBuilder,
+    OutputBuilderComponent,
+    ReplaceElement,
+)
 from .fs import AbstractFileSystem, FileSystem
 from .model_preprocessors import ModelPreprocessor
 from .outputs import OutputBase
 from .property_preprocessors import PropertyPreprocessor
 from .schema import ModelSchema
 from .utils.cst import ConflictResolver
 from .validation import validate_model
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builders/__init__.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builders/__init__.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builders/extend.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builders/extend.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builders/json_base.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builders/json_base.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builders/jsonschema.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builders/jsonschema.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builders/mapping.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builders/mapping.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builders/model_saver.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builders/model_saver.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builders/pyproject_toml.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builders/pyproject_toml.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builders/python.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builders/python.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builders/python_structure.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builders/python_structure.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builders/setup_cfg.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builders/setup_cfg.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builders/utils.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builders/utils.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/builtin_models/invenio.json` & `oarepo-model-builder-3.2.9/oarepo_model_builder/builtin_models/invenio.json`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/cli.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/cli.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,19 +5,23 @@
 import sys
 import traceback
 from pathlib import Path
 
 import click
 import yaml
 
-from oarepo_model_builder.conflict_resolvers import (AutomaticResolver,
-                                                     InteractiveResolver)
-from oarepo_model_builder.entrypoints import (create_builder_from_entrypoints,
-                                              load_entry_points_dict,
-                                              load_model)
+from oarepo_model_builder.conflict_resolvers import (
+    AutomaticResolver,
+    InteractiveResolver,
+)
+from oarepo_model_builder.entrypoints import (
+    create_builder_from_entrypoints,
+    load_entry_points_dict,
+    load_model,
+)
 from oarepo_model_builder.utils.verbose import log
 
 
 @click.command()
 @click.option(
     "--output-directory",
     help="Output directory where the generated files will be placed. "
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/conflict_resolvers.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/conflict_resolvers.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/__init__.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/__init__.py`

 * *Files 8% similar despite different names*

```diff
@@ -17,22 +17,30 @@
   minLength, maxLength, pattern
 
 flatten:
   object represented as flatten type in elasticsearch
 """
 
 
-from .containers import (ArrayDataType, FlattenDataType, NestedDataType,
-                         ObjectDataType)
+from .containers import ArrayDataType, FlattenDataType, NestedDataType, ObjectDataType
 from .datatypes import DataType, Import, datatypes  # noqa
-from .dates import (DateDataType, DateTimeDataType, EDTFDataType,
-                    EDTFIntervalType, TimeDataType)
+from .dates import (
+    DateDataType,
+    DateTimeDataType,
+    EDTFDataType,
+    EDTFIntervalType,
+    TimeDataType,
+)
 from .primitive_types import NumberDataType  # noqa
-from .primitive_types import (BooleanDataType, DoubleDataType, FloatDataType,
-                              IntegerDataType)
+from .primitive_types import (
+    BooleanDataType,
+    DoubleDataType,
+    FloatDataType,
+    IntegerDataType,
+)
 from .strings import StringDataType  # noqa
 from .strings import FulltextDataType, FulltextKeywordDataType, KeywordDataType
 
 DEFAULT_DATATYPES = [
     IntegerDataType,
     FloatDataType,
     DoubleDataType,
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/containers.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/containers.py`

 * *Files 9% similar despite different names*

```diff
@@ -3,19 +3,18 @@
 from hashlib import sha256
 
 from marshmallow import fields
 
 from oarepo_model_builder.utils.camelcase import camel_case
 from oarepo_model_builder.utils.jinja import split_package_name
 from oarepo_model_builder.utils.python_name import convert_name_to_python_class
-from oarepo_model_builder.validation import (InvalidModelException,
-                                             model_validator)
+from oarepo_model_builder.validation import InvalidModelException, model_validator
 
-from .datatypes import DataType
 from ..utils.facet_helpers import searchable
+from .datatypes import DataType
 
 log = logging.getLogger("datatypes")
 
 
 class ObjectDataType(DataType):
     schema_type = "object"
     mapping_type = "object"
@@ -126,103 +125,114 @@
                 if package_path:
                     package_path = package_path[:-1]
                 class_name = class_name[1:]
             if package_path:
                 class_name = f"{'.'.join(package_path)}.{class_name}"
         return class_name
 
-    def facet(self, key, definition={}, props_num = None, create = True):
-        key = definition.get('key', key)
-        field = definition.get('field', "TermFacet")
+    def facet(self, key, definition={}, props_num=None, create=True):
+        key = definition.get("key", key)
+        field = definition.get("field", "TermFacet")
         if "searchable" in definition:
             for d in self.stack.top.data.properties:
-                self.stack.top.data.properties[d]['facets'] = {"searchable" : definition["searchable"]}
+                self.stack.top.data.properties[d]["facets"] = {
+                    "searchable": definition["searchable"]
+                }
         if not searchable(definition, create):
             return False
         if props_num == 0:
             return False
 
-        return {"path": key, "class": field, 'props_num' : props_num}
+        return {"path": key, "class": field, "props_num": props_num}
+
 
 class NestedDataType(ObjectDataType):
     schema_type = "object"
     mapping_type = "nested"
     marshmallow_field = "ma_fields.Nested"
     model_type = "nested"
 
-    def facet(self, key, definition={}, props_num = None, create = True):
+    def facet(self, key, definition={}, props_num=None, create=True):
         if "searchable" in definition:
             for d in self.stack.top.data.properties:
-                self.stack.top.data.properties[d]['facets'] = {"searchable" : definition["searchable"]}
+                self.stack.top.data.properties[d]["facets"] = {
+                    "searchable": definition["searchable"]
+                }
         if not searchable(definition, create):
             return False
         upper = self.stack[-2]
         if key in definition:
-            key = definition['key']
+            key = definition["key"]
         elif upper.json_schema_type == "array":
             key = upper.key
-        return {"path": key, "class": "NestedLabeledFacet", 'props_num' : props_num}
-
+        return {"path": key, "class": "NestedLabeledFacet", "props_num": props_num}
 
 
 class FlattenDataType(DataType):
     schema_type = "object"
     mapping_type = "flatten"
     marshmallow_field = "ma_fields.Raw"
     model_type = "flatten"
 
-    def facet(self, key, definition= {}, props_num = None, create = True):
+    def facet(self, key, definition={}, props_num=None, create=True):
         if not searchable(definition, create):
             return False
         facet_def = {}
-        if 'field' in definition:
-            key = definition.get('key', key)
-            facet_def = {'path': key, 'class': definition['field']}
-            facet_def['defined_class'] = True
+        if "field" in definition:
+            key = definition.get("key", key)
+            facet_def = {"path": key, "class": definition["field"]}
+            facet_def["defined_class"] = True
             return facet_def
         else:
             return False
 
+
 class ArrayDataType(DataType):
     schema_type = "array"
     mapping_type = None
     marshmallow_field = "ma_fields.List"
     model_type = "array"
 
     class ModelSchema(DataType.ModelSchema):
         items = fields.Nested(
             lambda: model_validator.validator_class("array-items", strict=False)()
         )
         uniqueItems = fields.Boolean(required=False)
         minItems = fields.Integer(required=False)
         maxItems = fields.Integer(required=False)
 
-    def facet(self, key, definition={}, props_num = None, create = True):
+    def facet(self, key, definition={}, props_num=None, create=True):
         if "searchable" in definition:
-            if 'properties' in self.stack.top.data['items']:
-                self.stack.top.data['items']['facets'] = {"searchable" : definition["searchable"]}
-                for d in self.stack.top.data['items'].properties:
-                    self.stack.top.data['items'].properties[d]['facets'] = {"searchable" : definition["searchable"]}
+            if "properties" in self.stack.top.data["items"]:
+                self.stack.top.data["items"]["facets"] = {
+                    "searchable": definition["searchable"]
+                }
+                for d in self.stack.top.data["items"].properties:
+                    self.stack.top.data["items"].properties[d]["facets"] = {
+                        "searchable": definition["searchable"]
+                    }
             else:
-                for d in self.stack.top.data['items']:
-                    self.stack.top.data['items'][d]['facets'] = {"searchable" : definition["searchable"]}
+                for d in self.stack.top.data["items"]:
+                    self.stack.top.data["items"][d]["facets"] = {
+                        "searchable": definition["searchable"]
+                    }
         if not searchable(definition, create):
             return False
-        key = definition.get('key', key)
-        if key not in definition and 'keyword' in definition:
+        key = definition.get("key", key)
+        if key not in definition and "keyword" in definition:
             key = key + "_keyword"
 
-        field = definition.get('field', "TermsFacet(field = ")
+        field = definition.get("field", "TermsFacet(field = ")
         facet_def = {}
-        if 'nested' in definition:
+        if "nested" in definition:
             field = "NestedLabeledFacet"
-        elif 'field' in definition:
-            facet_def['defined_class'] = True
-        facet_def["path"] =  key
+        elif "field" in definition:
+            facet_def["defined_class"] = True
+        facet_def["path"] = key
         facet_def["class"] = field
 
         if props_num == 0:
             return False
         if int(props_num or 0) > 1:
-            facet_def['props_num'] = props_num
+            facet_def["props_num"] = props_num
 
-        return facet_def
+        return facet_def
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/datatypes.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/datatypes.py`

 * *Files 1% similar despite different names*

```diff
@@ -53,15 +53,15 @@
 
     def marshmallow_validators(self) -> List[str]:
         return []
 
     def imports(self, *extra) -> List[Import]:
         return extra
 
-    def facet(self, key, definition={}, props_num=None, create = True):
+    def facet(self, key, definition={}, props_num=None, create=True):
         return False
 
     def dumper_class(self, data):  # NOSONAR
         return None
 
 
 class DataTypes:
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/dates.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/dates.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from typing import List
 
-from .datatypes import DataType, Import
 from ..utils.facet_helpers import searchable
+from .datatypes import DataType, Import
 
 
 class BaseDateDataType(DataType):
     marshmallow_field = "ma_fields.String"
 
 
 class DateDataType(BaseDateDataType):
@@ -25,22 +25,22 @@
         ]
 
     def imports(self, *extra) -> List[Import]:
         return super().imports(
             Import(import_path="oarepo_runtime.validation.validate_date", alias=None)
         )
 
-    def facet(self, key, definition={}, props_num=None, create = True):
+    def facet(self, key, definition={}, props_num=None, create=True):
         if not searchable(definition, create):
             return False
-        key = definition.get('key', key)
-        field = definition.get('field', "TermsFacet(field = ")
+        key = definition.get("key", key)
+        field = definition.get("field", "TermsFacet(field = ")
         facet_def = {"path": key, "class": field}
-        if 'field' in definition:
-            facet_def['defined_class'] = True
+        if "field" in definition:
+            facet_def["defined_class"] = True
         return facet_def
 
 
 class TimeDataType(BaseDateDataType):
     schema_type = "string"
     mapping_type = "date"
     model_type = "time"
@@ -107,8 +107,7 @@
     def marshmallow_validators(self):
         return super().marshmallow_validators() + [
             "mu_fields.EDTFValidator(types=EDTFInterval)"
         ]
 
     def imports(self, *args):
         return super().imports(Import(name="edtf.Interval", alias="EDTFInterval"))
-
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/primitive_types.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/primitive_types.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from typing import List
 
 from marshmallow import fields
 
-from .datatypes import DataType, Import
 from ..utils.facet_helpers import searchable
+from .datatypes import DataType, Import
 
 
 class NumberDataType(DataType):
     def marshmallow_validators(self):
         validators = []
         ranges = {}
         for param, schema in (
@@ -21,22 +21,22 @@
 
         if ranges:
             params = ", ".join(f"{k}={v}" for k, v in ranges.items())
             validators.append(f"ma_validate.Range({params})")
 
         return validators
 
-    def facet(self, key, definition={}, props_num=None, create = True):
+    def facet(self, key, definition={}, props_num=None, create=True):
         if not searchable(definition, create):
             return False
-        key = definition.get('key', key)
-        field = definition.get('field', "TermsFacet(field = ")
+        key = definition.get("key", key)
+        field = definition.get("field", "TermsFacet(field = ")
         facet_def = {"path": key, "class": field}
-        if 'field' in definition:
-            facet_def['defined_class'] = True
+        if "field" in definition:
+            facet_def["defined_class"] = True
         return facet_def
 
 
 class IntegerDataType(NumberDataType):
     marshmallow_field = "ma_fields.Integer"
     schema_type = "integer"
     model_type = "integer"
@@ -72,16 +72,16 @@
         exclusiveMaximum = fields.Float(required=False)
 
 
 class BooleanDataType(DataType):
     marshmallow_field = "ma_fields.Boolean"
     model_type = "boolean"
 
-    def facet(self, key, definition={}, props_num=None, create = True):
+    def facet(self, key, definition={}, props_num=None, create=True):
         if not searchable(definition, create):
             return False
-        key = definition.get('key', key)
-        field = definition.get('field', "TermsFacet(field = ")
+        key = definition.get("key", key)
+        field = definition.get("field", "TermsFacet(field = ")
         facet_def = {"path": key, "class": field}
-        if 'field' in definition:
-            facet_def['defined_class'] = True
-        return facet_def
+        if "field" in definition:
+            facet_def["defined_class"] = True
+        return facet_def
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/datatypes/strings.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/datatypes/strings.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import re
 
 from marshmallow import fields
 from marshmallow.exceptions import ValidationError
 
-from .datatypes import DataType
 from ..utils.facet_helpers import searchable
+from .datatypes import DataType
 
 
 def validate_regex(value):
     if not value:
         return
     try:
         re.compile(value)
@@ -46,52 +46,50 @@
             pattern = self.definition["pattern"]
             pattern = pattern.replace("\\", "\\\\")
             pattern = pattern.replace('"', '\\"')
             validators.append(f'ma_validate.Regexp("{pattern}")')
 
         return validators
 
-    def facet(self, key, definition={}, props_num=None, create = True):
+    def facet(self, key, definition={}, props_num=None, create=True):
         if not searchable(definition, create):
             return False
-        key = definition.get('key', key)
-        field = definition.get('field', "TermsFacet(field = ")
+        key = definition.get("key", key)
+        field = definition.get("field", "TermsFacet(field = ")
         facet_def = {"path": key, "class": field}
-        if 'field' in definition:
-            facet_def['defined_class'] = True
+        if "field" in definition:
+            facet_def["defined_class"] = True
         return facet_def
 
+
 class FulltextDataType(StringDataType):
     mapping_type = "text"
     model_type = "fulltext"
 
-    def facet(self, key, definition=None, props_num=None, create = True):
+    def facet(self, key, definition=None, props_num=None, create=True):
         return False
 
 
 class KeywordDataType(StringDataType):
     mapping_type = "keyword"
     model_type = "keyword"
 
 
-
-
 class FulltextKeywordDataType(StringDataType):
     mapping_type = "text"
     model_type = "fulltext+keyword"
 
     def mapping(self):
         ret = super().mapping()
         mapping_el = ret.setdefault("mapping", {})
         mapping_el.setdefault("fields", {}).setdefault("keyword", {"type": "keyword"})
         return ret
 
-
-    def facet(self, key, definition={}, props_num=None, create = True):
+    def facet(self, key, definition={}, props_num=None, create=True):
         if not searchable(definition, create):
             return False
-        key = definition.get('key', key + "_keyword")
-        field = definition.get('field', "TermsFacet(field = ")
+        key = definition.get("key", key + "_keyword")
+        field = definition.get("field", "TermsFacet(field = ")
         facet_def = {"path": key, "class": field}
-        if 'field' in definition:
-            facet_def['defined_class'] = True
+        if "field" in definition:
+            facet_def["defined_class"] = True
         return facet_def
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/entrypoints.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/entrypoints.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/fs.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/fs.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/__init__.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/__init__.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_base.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_base.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_cli_setup_cfg.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_cli_setup_cfg.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_ext_setup_cfg.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_ext_setup_cfg.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_metadata_alembic_setup_cfg.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_metadata_alembic_setup_cfg.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_metadata_models_setup_cfg.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_metadata_models_setup_cfg.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_resource_setup_cfg.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_resource_setup_cfg.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_schema.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -7,17 +7,19 @@
 
 from oarepo_model_builder.builders import process
 from oarepo_model_builder.builders.python import PythonBuilder
 from oarepo_model_builder.datatypes import Import, datatypes
 from oarepo_model_builder.schema import ModelSchema
 from oarepo_model_builder.stack.stack import ModelBuilderStack
 from oarepo_model_builder.utils.camelcase import camel_case
-from oarepo_model_builder.utils.jinja import (split_base_name,
-                                              split_package_base_name,
-                                              split_package_name)
+from oarepo_model_builder.utils.jinja import (
+    split_base_name,
+    split_package_base_name,
+    split_package_name,
+)
 from oarepo_model_builder.utils.python_name import convert_name_to_python
 from oarepo_model_builder.validation import InvalidModelException
 
 from .invenio_base import InvenioBaseClassPythonBuilder
 
 log = logging.getLogger("invenio_record_schema")
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_search.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_search.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 import keyword
 import re
 
 from oarepo_model_builder.builders import process
 from oarepo_model_builder.utils.jinja import package_name
-from ..datatypes import datatypes
+from oarepo_model_builder.utils.python_name import convert_name_to_python
 
+from ..datatypes import datatypes
 from ..outputs.json_stack import JSONStack
 from ..utils.deepmerge import deepmerge
 from .invenio_base import InvenioBaseClassPythonBuilder
-from oarepo_model_builder.utils.python_name import convert_name_to_python
 
 OAREPO_FACETS_PROPERTY = "facets"
 OAREPO_SORTABLE_PROPERTY = "sortable"
 
 
 class InvenioRecordSearchOptionsBuilder(InvenioBaseClassPythonBuilder):
     TYPE = "invenio_record_search"
@@ -62,73 +62,110 @@
         schema_element_type = self.stack.top.schema_element_type
         data = self.stack.top.data
         recurse = True
 
         if recurse:
             try:
                 self.definition = data.get(OAREPO_FACETS_PROPERTY, {})
-                fd = datatypes.get_datatype(data, data.type, self.current_model, self.schema, self.stack)
+                fd = datatypes.get_datatype(
+                    data, data.type, self.current_model, self.schema, self.stack
+                )
                 ft = False
-                if fd.schema_type == 'object':
-                    properties = data.get('properties', {})
-                    ft = fd.facet(key = self.stack.top.key, props_num= self.properties_types(properties),definition = self.definition,  create=self.facet_switch)
-                elif fd.schema_type == 'array':
-                    ft = fd.facet(key = self.stack.top.key, props_num= self.properties_types(data['items'], True), definition=self.definition, create=self.facet_switch)
+                if fd.schema_type == "object":
+                    properties = data.get("properties", {})
+                    ft = fd.facet(
+                        key=self.stack.top.key,
+                        props_num=self.properties_types(properties),
+                        definition=self.definition,
+                        create=self.facet_switch,
+                    )
+                elif fd.schema_type == "array":
+                    ft = fd.facet(
+                        key=self.stack.top.key,
+                        props_num=self.properties_types(data["items"], True),
+                        definition=self.definition,
+                        create=self.facet_switch,
+                    )
                 if ft:
                     self.facet_stack.append(ft)
-            except: pass
+            except:
+                pass
 
             self.build_children()
 
         if not self.search_options_stack:
             return
 
         if schema_element_type == "property":
             sort_definition = data.get(OAREPO_SORTABLE_PROPERTY, None)
 
             if sort_definition != None:
                 self.sort_options_data.append(
                     self.process_sort_options(self.stack.path, sort_definition)
                 )
 
-        if schema_element_type == "property" and \
-                (('type' in data) and (datatypes.get_datatype(data, data.type, self.current_model, self.schema, self.stack).schema_type != 'object')):
-
-            d_type = datatypes.get_datatype(data, data.type, self.current_model, self.schema, self.stack)
-            ft = d_type.facet(key=self.stack.top.key, definition=self.definition, create=self.facet_switch)
-            if ft and data.type != "array": self.facet_stack.append(ft)
+        if schema_element_type == "property" and (
+            ("type" in data)
+            and (
+                datatypes.get_datatype(
+                    data, data.type, self.current_model, self.schema, self.stack
+                ).schema_type
+                != "object"
+            )
+        ):
+
+            d_type = datatypes.get_datatype(
+                data, data.type, self.current_model, self.schema, self.stack
+            )
+            ft = d_type.facet(
+                key=self.stack.top.key,
+                definition=self.definition,
+                create=self.facet_switch,
+            )
+            if ft and data.type != "array":
+                self.facet_stack.append(ft)
             if len(self.facet_stack) > 0:
                 facet_def = ""
                 facet_name = ""
                 facet_path = ""
                 nested_count = 0
                 for facet in self.facet_stack:
-                    facet_name = facet_name + convert_name_to_python(facet["path"]) + "_"
+                    facet_name = (
+                        facet_name + convert_name_to_python(facet["path"]) + "_"
+                    )
                     facet_path = facet_path + facet["path"] + "."
-                    if 'defined_class' in facet:
+                    if "defined_class" in facet:
                         facet_def = facet_def + facet["class"]
-                    elif facet['class'].startswith("Nested"):
+                    elif facet["class"].startswith("Nested"):
                         nested_count += 1
-                        facet_def = facet_def + f"NestedLabeledFacet(path =\" {facet_path[:-1]}\", nested_facet="
-                    elif 'props_num' in facet:
+                        facet_def = (
+                            facet_def
+                            + f'NestedLabeledFacet(path =" {facet_path[:-1]}", nested_facet='
+                        )
+                    elif "props_num" in facet:
                         pass
                     else:
-                        facet_path = (facet_path[::-1]).replace('_keyword.'[::-1], '.keyword.'[::-1], 1)[::-1] \
-                            if facet_path.endswith('_keyword.') else facet_path
-                        facet_def = facet_def + facet["class"] + f"\"{facet_path[:-1]}\""
+                        facet_path = (
+                            (facet_path[::-1]).replace(
+                                "_keyword."[::-1], ".keyword."[::-1], 1
+                            )[::-1]
+                            if facet_path.endswith("_keyword.")
+                            else facet_path
+                        )
+                        facet_def = facet_def + facet["class"] + f'"{facet_path[:-1]}"'
                         for i in range(0, nested_count):
-                            facet_def = facet_def + ')'
-                        facet_def = facet_def + ')'
+                            facet_def = facet_def + ")"
+                        facet_def = facet_def + ")"
                 self.clean_stack()
 
                 facet_name = facet_name[:-1]
-                self.search_options_data.append({facet_name: facet_def})
-                search_ops_name = "facets." + facet_name
-                self.facets_definition.append({facet_name: search_ops_name})
-
+                if facet_def:
+                    self.search_options_data.append({facet_name: facet_def})
+                    search_ops_name = "facets." + facet_name
+                    self.facets_definition.append({facet_name: search_ops_name})
 
     def process_search_options(self, data, field_class):
         text = ""
         for x in data:
             if text == "":
                 text = text + x[0] + ' = "' + x[1] + '"'
             else:
@@ -136,48 +173,51 @@
         return field_class + "(" + text + ")"
 
     def clean_stack(self):
         self.facet_stack.reverse()
         del_indices = []
         del self.facet_stack[:1]
         for facet in self.facet_stack:
-            if 'props_num' in facet and facet['props_num'] == 1:
+            if "props_num" in facet and facet["props_num"] == 1:
                 del_indices.append(self.facet_stack.index(facet))
-            elif 'props_num' in facet:
-                facet['props_num'] = facet['props_num'] -1
+            elif "props_num" in facet:
+                facet["props_num"] = facet["props_num"] - 1
                 break
         for i in del_indices[::-1]:
             del self.facet_stack[i]
         self.facet_stack.reverse()
 
-
-    def properties_types(self, data, array = False):
+    def properties_types(self, data, array=False):
         count = 0
         ft = False
         if array:
-            if 'type' in data and data['type'] == 'object':
-                self.definition['obj'] = True
-                data = data['properties']
-            elif 'type' in data and data['type'] == 'nested':
-                self.definition['nested'] = True
-            elif 'type' in data and data['type'] == "fulltext+keyword":
-                self.definition['keyword'] = True
+            if "type" in data and data["type"] == "object":
+                self.definition["obj"] = True
+                data = data["properties"]
+            elif "type" in data and data["type"] == "nested":
+                self.definition["nested"] = True
+            elif "type" in data and data["type"] == "fulltext+keyword":
+                self.definition["keyword"] = True
                 return 1
-            elif 'type' in data:
-                fd = datatypes.get_datatype(data, data.type, self.current_model, self.schema, self.stack)
+            elif "type" in data:
+                fd = datatypes.get_datatype(
+                    data, data.type, self.current_model, self.schema, self.stack
+                )
                 ft = fd.facet(key="")
                 if ft:
                     return 1
             else:
                 return 0
         for d in data:
-            if 'properties' in data[d]:
+            if "properties" in data[d]:
                 count = count + 1
-            elif 'type' in data[d]:
-                fd = datatypes.get_datatype(data[d], data[d].type, self.current_model, self.schema, self.stack)
+            elif "type" in data[d]:
+                fd = datatypes.get_datatype(
+                    data[d], data[d].type, self.current_model, self.schema, self.stack
+                )
                 ft = fd.facet(key=d)
                 if ft:
                     count = count + 1
         return count
 
     def process_name(self, path, type):
         path_array = (path.split("/"))[2:]
@@ -206,8 +246,7 @@
         if key == "":
             key = self.process_name(path, "name")
         order = definition.get("order", "asc")
         if order == "desc":
             field = "-" + field
 
         return {key: dict(fields=[field])}
-
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_record_service_config.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_record_service_config.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_script_sample_data.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_script_sample_data.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/invenio_version.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/invenio_version.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_cli.py.jinja2` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_cli.py.jinja2`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_config.py.jinja2` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_config.py.jinja2`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_ext.py.jinja2` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_ext.py.jinja2`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record.py.jinja2` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record.py.jinja2`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_metadata.py.jinja2` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_metadata.py.jinja2`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_permissions.py.jinja2` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_permissions.py.jinja2`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_resource_config.py.jinja2` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_resource_config.py.jinja2`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_schema.py.jinja2` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_schema.py.jinja2`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_search_options.py.jinja2` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_search_options.py.jinja2`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_record_service_config.py.jinja2` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_record_service_config.py.jinja2`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/invenio_views.py.jinja2` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/invenio_views.py.jinja2`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/invenio/templates/script_import_sample_data.py.jinja2` & `oarepo-model-builder-3.2.9/oarepo_model_builder/invenio/templates/script_import_sample_data.py.jinja2`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/loaders/__init__.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/loaders/__init__.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/merger.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/merger.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
-from functools import partial
 import json
 import shutil
 import sys
+from functools import partial
 from pathlib import Path
 
 import click
 import json5
 import libcst as cst
 import yaml
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/model_preprocessors/__init__.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/model_preprocessors/__init__.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/model_preprocessors/default_values.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/model_preprocessors/default_values.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/model_preprocessors/extend.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/model_preprocessors/extend.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/model_preprocessors/invenio.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/model_preprocessors/invenio.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/model_preprocessors/invenio_base_classes.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/model_preprocessors/invenio_base_classes.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/cfg.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/cfg.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/diff.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/diff.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/json.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/json.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/json_stack.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/json_stack.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/jsonschema.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/jsonschema.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/python.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/python.py`

 * *Files 5% similar despite different names*

```diff
@@ -2,17 +2,20 @@
 
 import libcst as cst
 from jinja2 import Environment, FunctionLoader, pass_context
 
 from oarepo_model_builder.outputs import OutputBase
 from oarepo_model_builder.templates import templates
 from oarepo_model_builder.utils.cst import PythonContext, merge
-from oarepo_model_builder.utils.jinja import (base_name, in_different_package,
-                                              package_name,
-                                              with_defined_prefix)
+from oarepo_model_builder.utils.jinja import (
+    base_name,
+    in_different_package,
+    package_name,
+    with_defined_prefix,
+)
 from oarepo_model_builder.utils.verbose import log
 
 
 class PythonOutput(OutputBase):
     TYPE = "python"
     cst = None
     original_data = None
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/text.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/text.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/toml.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/toml.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/outputs/yaml.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/outputs/yaml.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/profiles/model.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/profiles/model.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 from pathlib import Path
 from typing import Union
 
 import json5
 
 from oarepo_model_builder.builder import ModelBuilder
-from oarepo_model_builder.entrypoints import (create_builder_from_entrypoints,
-                                              load_model)
+from oarepo_model_builder.entrypoints import create_builder_from_entrypoints, load_model
 from oarepo_model_builder.fs import InMemoryFileSystem
 from oarepo_model_builder.profiles import Profile
 from oarepo_model_builder.profiles.extend import ExtendProfile
 from oarepo_model_builder.schema import ModelSchema
 from oarepo_model_builder.utils.deepmerge import deepmerge
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/property_preprocessors/__init__.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/property_preprocessors/__init__.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/property_preprocessors/datatype_preprocessor.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/property_preprocessors/datatype_preprocessor.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 from oarepo_model_builder.builders.jsonschema import JSONSchemaBuilder
 from oarepo_model_builder.builders.mapping import MappingBuilder
 from oarepo_model_builder.datatypes import datatypes
-from oarepo_model_builder.invenio.invenio_record_schema import \
-    InvenioRecordSchemaBuilder
-from oarepo_model_builder.property_preprocessors import (PropertyPreprocessor,
-                                                         process)
+from oarepo_model_builder.invenio.invenio_record_schema import (
+    InvenioRecordSchemaBuilder,
+)
+from oarepo_model_builder.property_preprocessors import PropertyPreprocessor, process
 from oarepo_model_builder.stack import ModelBuilderStack
 from oarepo_model_builder.utils.deepmerge import deepmerge
 
 
 class DataTypePreprocessor(PropertyPreprocessor):
     TYPE = "datatype"
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/property_preprocessors/enum.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/property_preprocessors/enum.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 from oarepo_model_builder.builders.jsonschema import JSONSchemaBuilder
 from oarepo_model_builder.builders.mapping import MappingBuilder
-from oarepo_model_builder.invenio.invenio_record_schema import \
-    InvenioRecordSchemaBuilder
-from oarepo_model_builder.invenio.invenio_script_sample_data import \
-    InvenioScriptSampleDataBuilder
-from oarepo_model_builder.property_preprocessors import (PropertyPreprocessor,
-                                                         process)
+from oarepo_model_builder.invenio.invenio_record_schema import (
+    InvenioRecordSchemaBuilder,
+)
+from oarepo_model_builder.invenio.invenio_script_sample_data import (
+    InvenioScriptSampleDataBuilder,
+)
+from oarepo_model_builder.property_preprocessors import PropertyPreprocessor, process
 from oarepo_model_builder.stack import ModelBuilderStack
 from oarepo_model_builder.utils.deepmerge import deepmerge
 
 
 class EnumPreprocessor(PropertyPreprocessor):
     TYPE = "enum"
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/property_preprocessors/extend.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/property_preprocessors/extend.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,16 +1,17 @@
 from oarepo_model_builder.builders.extend import ExtendBuilder
 from oarepo_model_builder.builders.jsonschema import JSONSchemaBuilder
 from oarepo_model_builder.builders.mapping import MappingBuilder
-from oarepo_model_builder.invenio.invenio_record_schema import \
-    InvenioRecordSchemaBuilder
-from oarepo_model_builder.invenio.invenio_script_sample_data import \
-    InvenioScriptSampleDataBuilder
-from oarepo_model_builder.property_preprocessors import (PropertyPreprocessor,
-                                                         process)
+from oarepo_model_builder.invenio.invenio_record_schema import (
+    InvenioRecordSchemaBuilder,
+)
+from oarepo_model_builder.invenio.invenio_script_sample_data import (
+    InvenioScriptSampleDataBuilder,
+)
+from oarepo_model_builder.property_preprocessors import PropertyPreprocessor, process
 from oarepo_model_builder.stack import ModelBuilderStack
 from oarepo_model_builder.utils.deepmerge import deepmerge
 
 
 class DisableMarshmallowPreprocessor(PropertyPreprocessor):
     TYPE = "disable-marshmallow"
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/schema.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/schema.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/stack/schema.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/stack/schema.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/stack/stack.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/stack/stack.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/templates/__init__.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/templates/__init__.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/call.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/call.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/collections.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/collections.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/common.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/common.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/indented_nodes.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/indented_nodes.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/mergers.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/mergers.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,12 +1,29 @@
 import lazy_object_proxy
-from libcst import (Arg, Assign, Call, ClassDef, Dict, Element, Expr,
-                    FunctionDef, Import, ImportFrom, Integer, List, Module,
-                    Name, Pass, SimpleStatementLine, SimpleString,
-                    StarredElement, Tuple)
+from libcst import (
+    Arg,
+    Assign,
+    Call,
+    ClassDef,
+    Dict,
+    Element,
+    Expr,
+    FunctionDef,
+    Import,
+    ImportFrom,
+    Integer,
+    List,
+    Module,
+    Name,
+    Pass,
+    SimpleStatementLine,
+    SimpleString,
+    StarredElement,
+    Tuple,
+)
 
 
 @lazy_object_proxy.Proxy
 def module_mergers():
     from .indented_nodes import ModuleMerger
 
     return {Module: ModuleMerger()}
@@ -22,16 +39,21 @@
         ClassDef: ClassMerger(),
         FunctionDef: FunctionMerger(),
     }
 
 
 @lazy_object_proxy.Proxy
 def simple_line_mergers():
-    from .simple_nodes import (AssignMerger, ExprMerger, ImportFromMerger,
-                               ImportMerger, PassMerger)
+    from .simple_nodes import (
+        AssignMerger,
+        ExprMerger,
+        ImportFromMerger,
+        ImportMerger,
+        PassMerger,
+    )
 
     return {
         Assign: AssignMerger(),
         Import: ImportMerger(),
         ImportFrom: ImportFromMerger(),
         Expr: ExprMerger(),
         Pass: PassMerger(),
@@ -43,21 +65,28 @@
     from .call import ArgMerger
 
     return {Arg: ArgMerger()}
 
 
 @lazy_object_proxy.Proxy
 def expression_mergers():
-    from oarepo_model_builder.utils.cst.collections import (DictMerger,
-                                                            ElementMerger,
-                                                            ListMerger)
+    from oarepo_model_builder.utils.cst.collections import (
+        DictMerger,
+        ElementMerger,
+        ListMerger,
+    )
 
     from .call import CallMerger
-    from .simple_nodes import (ExprMerger, IntegerMerger, NameMerger,
-                               SimpleStringMerger, StarredElementMerger)
+    from .simple_nodes import (
+        ExprMerger,
+        IntegerMerger,
+        NameMerger,
+        SimpleStringMerger,
+        StarredElementMerger,
+    )
 
     return {
         Call: CallMerger(),
         List: ListMerger(),
         Tuple: ListMerger(),
         Integer: IntegerMerger(),
         Element: ElementMerger(),
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/utils/cst/simple_nodes.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/utils/cst/simple_nodes.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 import logging
 
 from libcst import Assign, Integer, Name
 
-from .common import (IdentityBaseMerger, IdentityMerger, MergerBase,
-                     PythonContext)
+from .common import IdentityBaseMerger, IdentityMerger, MergerBase, PythonContext
 from .mergers import expression_mergers, simple_line_mergers
 
 log = logging.getLogger("oarepo_model_builder.cst")
 
 
 class AssignMerger(MergerBase):
     def merge_internal(self, context: PythonContext, existing_node, new_node):
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/utils/deepmerge.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/utils/deepmerge.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/utils/hyphen_munch.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/utils/hyphen_munch.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/utils/jinja.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/utils/jinja.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/utils/json_pathlib.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/utils/json_pathlib.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/utils/python_name.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/utils/python_name.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -30,8 +30,8 @@
     class_name = "".join([capitalize(word) for word in name.split("-")])
     class_name = "".join([capitalize(word) for word in class_name.split("_")])
 
     # Replace any spaces or special characters in the string with an underscore
     class_name = re.sub(r"[^\w\s]", "", class_name)
     class_name = re.sub(r"\s+", "_", class_name)
 
-    return class_name
+    return class_name
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/utils/verbose.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/utils/verbose.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/__init__.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/__init__.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/model.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/model.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/model_defaults.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/model_defaults.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/model_plugins.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/model_plugins.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/model_validation.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/model_validation.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/properties.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/properties.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/property.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/property.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/property_marshmallow.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/property_marshmallow.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/property_sample_data.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/property_sample_data.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/registration.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/registration.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,22 +2,23 @@
 from .model_defaults import ModelDefaults
 from .model_plugins import PluginConfigSchema, PluginsSchema
 from .properties import ArrayItemsSchema, ObjectFieldSchema, PropertiesSchema
 from .property import ObjectProperty, Property
 from .property_facets import PropertyFacets
 from .property_jsonschema import PropertyJSONSchema
 from .property_mapping import PropertyMapping
-from .property_marshmallow import (ModelMarshmallowSchema,
-                                   ObjectPropertyMarshmallowSchema,
-                                   PropertyMarshmallowSchema)
+from .property_marshmallow import (
+    ModelMarshmallowSchema,
+    ObjectPropertyMarshmallowSchema,
+    PropertyMarshmallowSchema,
+)
 from .property_sample_data import ModelSampleConfiguration, PropertySampleData
 from .property_sortable import PropertySortable
 from .root import RootSchema
-from .settings import (SettingsOpenSearchSchema, SettingsPythonSchema,
-                       SettingsSchema)
+from .settings import SettingsOpenSearchSchema, SettingsPythonSchema, SettingsSchema
 
 #
 # Validators is a dictionary of "points" in model schema mapped to a single ma.Schema class
 # or a list of ma.Schema classes. During validation, a new marshmallow class is constructed
 # with all those classes as the bases for the class.
 #
 # To create your own extension point, see for example root.py: RootSchema
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/root.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/root.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/settings.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/settings.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder/validation/utils.py` & `oarepo-model-builder-3.2.9/oarepo_model_builder/validation/utils.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder.egg-info/PKG-INFO` & `oarepo-model-builder-3.2.9/oarepo_model_builder.egg-info/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: oarepo-model-builder
-Version: 3.2.8
+Version: 3.2.9
 Summary: A utility library that generates OARepo required data model files from a JSON specification file
 Description-Content-Type: text/markdown
 Provides-Extra: devs
 Provides-Extra: tests
 License-File: LICENSE
 
 # OARepo model builder
```

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder.egg-info/SOURCES.txt` & `oarepo-model-builder-3.2.9/oarepo_model_builder.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/oarepo_model_builder.egg-info/entry_points.txt` & `oarepo-model-builder-3.2.9/oarepo_model_builder.egg-info/entry_points.txt`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/setup.cfg` & `oarepo-model-builder-3.2.9/setup.cfg`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = oarepo-model-builder
-version = 3.2.8
+version = 3.2.9
 description = A utility library that generates OARepo required data model files from a JSON specification file
 authors = Miroslav Bauer <bauer@cesnet.cz>, Miroslav Simek <simeki@vscht.cz>
 readme = README.md
 long_description = file:README.md
 long_description_content_type = text/markdown
 
 [options]
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_builder.py` & `oarepo-model-builder-3.2.9/tests/test_builder.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/tests/test_builder_from_entrypoints.py` & `oarepo-model-builder-3.2.9/tests/test_builder_from_entrypoints.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 import json
 import os
 import re
 import sys
 from pathlib import Path
 
-from oarepo_model_builder.entrypoints import (create_builder_from_entrypoints,
-                                              load_model)
+from oarepo_model_builder.entrypoints import create_builder_from_entrypoints, load_model
 from oarepo_model_builder.fs import InMemoryFileSystem
 from tests.utils import assert_python_equals
 
 OAREPO_USE = "use"
 
 
 def test_include_invenio():
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_dependencies.py` & `oarepo-model-builder-3.2.9/tests/test_dependencies.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,10 @@
 import os
 
-from oarepo_model_builder.entrypoints import (create_builder_from_entrypoints,
-                                              load_model)
+from oarepo_model_builder.entrypoints import create_builder_from_entrypoints, load_model
 from oarepo_model_builder.fs import InMemoryFileSystem
 
 
 def test_no_dependencies():
     data = build()
     print(data)
     assert data.startswith("[metadata]")
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_empty_metadata.py` & `oarepo-model-builder-3.2.9/tests/test_empty_metadata.py`

 * *Files 19% similar despite different names*

```diff
@@ -2,16 +2,15 @@
 import os
 import re
 import shutil
 import sys
 from pathlib import Path
 from tempfile import mkdtemp, tempdir
 
-from oarepo_model_builder.entrypoints import (create_builder_from_entrypoints,
-                                              load_model)
+from oarepo_model_builder.entrypoints import create_builder_from_entrypoints, load_model
 from oarepo_model_builder.fs import FileSystem, InMemoryFileSystem
 from tests.utils import assert_python_equals
 
 OAREPO_USE = "use"
 
 
 def test_empty_metadata():
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_facets.py` & `oarepo-model-builder-3.2.9/tests/test_facets.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,31 +1,30 @@
-
 import os
 import re
 
-
 from oarepo_model_builder.entrypoints import create_builder_from_entrypoints, load_model
 from oarepo_model_builder.fs import InMemoryFileSystem
 
 DUMMY_YAML = "test.yaml"
 
+
 def test_include_invenio():
     schema = load_model(
         DUMMY_YAML,
         "test",
         model_content={
             "model": {
                 "use": "invenio",
                 "properties": {
-                    "a":  "fulltext+keyword",
+                    "a": "fulltext+keyword",
                     "b": {
                         "type": "keyword",
                         "facets": {"field": 'TermsFacet(field="cosi")'},
                     },
-                    "c": "fulltext"
+                    "c": "fulltext",
                 },
             },
         },
         isort=False,
         black=False,
     )
 
@@ -68,14 +67,15 @@
 
 
 
 _schema = TermsFacet(field = "$schema")
     """,
     )
 
+
 def test_nested():
     schema = load_model(
         DUMMY_YAML,
         "test",
         model_content={
             "model": {
                 "use": "invenio",
@@ -84,19 +84,18 @@
                         "type": "nested",
                         "properties": {
                             "c": {
                                 "type": "keyword",
                             },
                             "d": {"type": "fulltext+keyword"},
                             "f": {
-                                "type" : "nested",
+                                "type": "nested",
                                 "properties": {"g": {"type": "keyword"}},
-
                             },
-                        }
+                        },
                     }
                 },
             },
         },
         isort=False,
         black=False,
     )
@@ -145,15 +144,18 @@
 
 updated = TermsFacet(field = "updated")
 
 
 
 _schema = TermsFacet(field = "$schema")
     
-""",)
+""",
+    )
+
+
 def test_object():
     schema = load_model(
         DUMMY_YAML,
         "test",
         model_content={
             "model": {
                 "use": "invenio",
@@ -162,20 +164,19 @@
                         "type": "object",
                         "properties": {
                             "c": {
                                 "type": "keyword",
                             },
                             "d": {"type": "fulltext+keyword"},
                             "f": {
-                                "type" : "object",
+                                "type": "object",
                                 "properties": {"g": {"type": "keyword"}},
-
                             },
-                            "e": "fulltext"
-                        }
+                            "e": "fulltext",
+                        },
                     }
                 },
             },
         },
         isort=False,
         black=False,
     )
@@ -226,51 +227,49 @@
 
 
 
 _schema = TermsFacet(field = "$schema")
 """,
     )
 
+
 def test_nest_obj():
     schema = load_model(
         DUMMY_YAML,
         "test",
         model_content={
             "model": {
                 "use": "invenio",
                 "properties": {
                     "b_nes": {
                         "type": "nested",
                         "properties": {
                             "c": {
                                 "type": "keyword",
-
                             },
                             "d": {"type": "fulltext+keyword"},
                             "f": {
-                                "type" : "object",
+                                "type": "object",
                                 "properties": {"g": {"type": "keyword"}},
-
                             },
-                        }
+                        },
                     },
                     "b_obj": {
                         "type": "object",
                         "properties": {
                             "c": {
                                 "type": "keyword",
                             },
                             "d": {"type": "fulltext+keyword"},
                             "f": {
                                 "type": "nested",
                                 "properties": {"g": {"type": "keyword"}},
-
                             },
-                        }
-                    }
+                        },
+                    },
                 },
             },
         },
         isort=False,
         black=False,
     )
 
@@ -331,26 +330,26 @@
 
 
 
 _schema = TermsFacet(field = "$schema")
 """,
     )
 
+
 def test_array():
     schema = load_model(
         DUMMY_YAML,
         "test",
         model_content={
             "model": {
                 "use": "invenio",
                 "properties": {
-
                     "a[]": "keyword",
                     "b[]": "fulltext",
-                    "c[]": "fulltext+keyword"
+                    "c[]": "fulltext+keyword",
                 },
             },
         },
         isort=False,
         black=False,
     )
 
@@ -394,14 +393,15 @@
 
 
 
 _schema = TermsFacet(field = "$schema")
 """,
     )
 
+
 def test_array_nested():
     schema = load_model(
         DUMMY_YAML,
         "test",
         model_content={
             "model": {
                 "use": "invenio",
@@ -413,25 +413,20 @@
                                 "type": "array",
                                 "items": {
                                     "type": "nested",
                                     "properties": {
                                         "d": {"type": "keyword"},
                                         "e": {
                                             "type": "object",
-                                            "properties": {
-                                                "f": "keyword"
-                                            }
-                                        }
-
-                                    }
-                                }
-
+                                            "properties": {"f": "keyword"},
+                                        },
+                                    },
+                                },
                             }
-                        }
-
+                        },
                     },
                 },
             },
         },
         isort=False,
         black=False,
     )
@@ -472,52 +467,45 @@
 
 
 
 _schema = TermsFacet(field = "$schema")
 """,
     )
 
+
 def test_top_facets():
     schema = load_model(
         DUMMY_YAML,
         "test",
         model_content={
             "model": {
                 "use": "invenio",
                 "searchable": False,
                 "properties": {
-                    "a":  {"type": "fulltext+keyword",
-                           "facets": {"searchable": True}},
+                    "a": {"type": "fulltext+keyword", "facets": {"searchable": True}},
                     "b": {
                         "type": "keyword",
                         "facets": {"field": 'TermsFacet(field="cosi")'},
                     },
                     "c": "keyword",
                     "arr": {
                         "type": "array",
                         "facets": {"searchable": True},
                         "items": {
                             "type": "nested",
                             "properties": {
                                 "d": {"type": "keyword"},
-                                "e": {
-                                    "type": "object",
-                                    "properties": {
-                                        "f": "keyword"
-                                    }
-                                }
-
-                            }
-                        }
-
+                                "e": {"type": "object", "properties": {"f": "keyword"}},
+                            },
+                        },
                     },
                     "lst2": {
                         "type": "array",
                         "items": {"type": "keyword"},
-                        "facets": {"field": 'TermsFacet(field="cosi")'}
+                        "facets": {"field": 'TermsFacet(field="cosi")'},
                     },
                     "lst[]": "keyword",
                 },
             },
         },
         isort=False,
         black=False,
@@ -579,27 +567,25 @@
     schema = load_model(
         DUMMY_YAML,
         "test",
         model_content={
             "model": {
                 "use": "invenio",
                 "properties": {
-                    "a":  {"type": "fulltext+keyword",
-                           "facets": {"searchable": False}},
+                    "a": {"type": "fulltext+keyword", "facets": {"searchable": False}},
                     "b": {
                         "type": "keyword",
                         "facets": {"field": 'TermsFacet(field="cosi")'},
                     },
                     "c": "fulltext",
                     "f": {
-                                "type" : "object",
-                                "facets": {"searchable": False},
-                                "properties": {"g": {"type": "keyword"}},
-
-                            },
+                        "type": "object",
+                        "facets": {"searchable": False},
+                        "properties": {"g": {"type": "keyword"}},
+                    },
                 },
             },
         },
         isort=False,
         black=False,
     )
 
@@ -638,8 +624,8 @@
 updated = TermsFacet(field = "updated")
 
 
 
 _schema = TermsFacet(field = "$schema")
 
     """,
-    )
+    )
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_fulltext_keyword.py` & `oarepo-model-builder-3.2.9/tests/test_fulltext_keyword.py`

 * *Files 5% similar despite different names*

```diff
@@ -3,23 +3,26 @@
 import json5
 import pytest
 
 from oarepo_model_builder.builder import ModelBuilder
 from oarepo_model_builder.builders.jsonschema import JSONSchemaBuilder
 from oarepo_model_builder.builders.mapping import MappingBuilder
 from oarepo_model_builder.fs import InMemoryFileSystem
-from oarepo_model_builder.model_preprocessors.default_values import \
-    DefaultValuesModelPreprocessor
-from oarepo_model_builder.model_preprocessors.opensearch import \
-    OpensearchModelPreprocessor
+from oarepo_model_builder.model_preprocessors.default_values import (
+    DefaultValuesModelPreprocessor,
+)
+from oarepo_model_builder.model_preprocessors.opensearch import (
+    OpensearchModelPreprocessor,
+)
 from oarepo_model_builder.outputs.jsonschema import JSONSchemaOutput
 from oarepo_model_builder.outputs.mapping import MappingOutput
 from oarepo_model_builder.outputs.python import PythonOutput
-from oarepo_model_builder.property_preprocessors.datatype_preprocessor import \
-    DataTypePreprocessor
+from oarepo_model_builder.property_preprocessors.datatype_preprocessor import (
+    DataTypePreprocessor,
+)
 from oarepo_model_builder.schema import ModelSchema
 
 
 def get_model_schema(field_type):
     return ModelSchema(
         "",
         {
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_is_schema_element.py` & `oarepo-model-builder-3.2.9/tests/test_is_schema_element.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/tests/test_json_pathlib.py` & `oarepo-model-builder-3.2.9/tests/test_json_pathlib.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/tests/test_jsonchema_builder.py` & `oarepo-model-builder-3.2.9/tests/test_jsonchema_builder.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 import os
 
 from oarepo_model_builder.builder import ModelBuilder
 from oarepo_model_builder.builders import OutputBuilderComponent
 from oarepo_model_builder.builders.jsonschema import JSONSchemaBuilder
 from oarepo_model_builder.datatypes import datatypes
 from oarepo_model_builder.fs import InMemoryFileSystem
-from oarepo_model_builder.model_preprocessors.default_values import \
-    DefaultValuesModelPreprocessor
+from oarepo_model_builder.model_preprocessors.default_values import (
+    DefaultValuesModelPreprocessor,
+)
 from oarepo_model_builder.outputs.jsonschema import JSONSchemaOutput
 from oarepo_model_builder.outputs.python import PythonOutput
 from oarepo_model_builder.schema import ModelSchema
 from oarepo_model_builder.validation.model_validation import model_validator
-from tests.multilang import (MultilangPreprocessor, MultilingualDataType,
-                             UIValidator)
+from tests.multilang import MultilangPreprocessor, MultilingualDataType, UIValidator
 
 try:
     import json5
 except ImportError:
     import json as json5
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_jsonschema_output.py` & `oarepo-model-builder-3.2.9/tests/test_jsonschema_output.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/tests/test_loading.py` & `oarepo-model-builder-3.2.9/tests/test_loading.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/tests/test_mapping_builder.py` & `oarepo-model-builder-3.2.9/tests/test_mapping_builder.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 import os
 
 from oarepo_model_builder.builder import ModelBuilder
 from oarepo_model_builder.builders.mapping import MappingBuilder
 from oarepo_model_builder.datatypes import datatypes
 from oarepo_model_builder.fs import InMemoryFileSystem
-from oarepo_model_builder.model_preprocessors.default_values import \
-    DefaultValuesModelPreprocessor
+from oarepo_model_builder.model_preprocessors.default_values import (
+    DefaultValuesModelPreprocessor,
+)
 from oarepo_model_builder.outputs.mapping import MappingOutput
 from oarepo_model_builder.outputs.python import PythonOutput
 from oarepo_model_builder.schema import ModelSchema
 from oarepo_model_builder.validation.model_validation import model_validator
-from tests.multilang import (MultilangPreprocessor, MultilingualDataType,
-                             UIValidator)
+from tests.multilang import MultilangPreprocessor, MultilingualDataType, UIValidator
 
 try:
     import json5
 except ImportError:
     import json as json5
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_marshmallow_builder.py` & `oarepo-model-builder-3.2.9/tests/test_marshmallow_builder.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,25 +1,28 @@
 import os
 import re
 
 import pytest
 
 from oarepo_model_builder.builder import ModelBuilder
 from oarepo_model_builder.fs import InMemoryFileSystem
-from oarepo_model_builder.invenio.invenio_record_schema import \
-    InvenioRecordSchemaBuilder
-from oarepo_model_builder.model_preprocessors.default_values import \
-    DefaultValuesModelPreprocessor
-from oarepo_model_builder.model_preprocessors.invenio import \
-    InvenioModelPreprocessor
-from oarepo_model_builder.model_preprocessors.opensearch import \
-    OpensearchModelPreprocessor
+from oarepo_model_builder.invenio.invenio_record_schema import (
+    InvenioRecordSchemaBuilder,
+)
+from oarepo_model_builder.model_preprocessors.default_values import (
+    DefaultValuesModelPreprocessor,
+)
+from oarepo_model_builder.model_preprocessors.invenio import InvenioModelPreprocessor
+from oarepo_model_builder.model_preprocessors.opensearch import (
+    OpensearchModelPreprocessor,
+)
 from oarepo_model_builder.outputs.python import PythonOutput
-from oarepo_model_builder.property_preprocessors.datatype_preprocessor import \
-    DataTypePreprocessor
+from oarepo_model_builder.property_preprocessors.datatype_preprocessor import (
+    DataTypePreprocessor,
+)
 from oarepo_model_builder.schema import ModelSchema
 
 OAREPO_MARSHMALLOW = "marshmallow"
 B_SCHEMA = 'classB(ma.Schema):"""Bschema."""b=ma_fields.String()'
 
 
 def get_test_schema(**props):
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_merge.py` & `oarepo-model-builder-3.2.9/tests/test_merge.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/tests/test_model_saver.py` & `oarepo-model-builder-3.2.9/tests/test_model_saver.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,30 +1,34 @@
 import json
 import os
 
 from oarepo_model_builder.builder import ModelBuilder
 from oarepo_model_builder.builders.model_saver import (
-    ModelRegistrationBuilder, ModelSaverBuilder)
+    ModelRegistrationBuilder,
+    ModelSaverBuilder,
+)
 from oarepo_model_builder.datatypes import datatypes
 from oarepo_model_builder.entrypoints import (
-    load_entry_points_dict, load_included_models_from_entry_points)
+    load_entry_points_dict,
+    load_included_models_from_entry_points,
+)
 from oarepo_model_builder.fs import InMemoryFileSystem
-from oarepo_model_builder.model_preprocessors.default_values import \
-    DefaultValuesModelPreprocessor
-from oarepo_model_builder.model_preprocessors.invenio import \
-    InvenioModelPreprocessor
+from oarepo_model_builder.model_preprocessors.default_values import (
+    DefaultValuesModelPreprocessor,
+)
+from oarepo_model_builder.model_preprocessors.invenio import InvenioModelPreprocessor
 from oarepo_model_builder.outputs.cfg import CFGOutput
 from oarepo_model_builder.outputs.json import JSONOutput
 from oarepo_model_builder.outputs.python import PythonOutput
-from oarepo_model_builder.property_preprocessors.datatype_preprocessor import \
-    DataTypePreprocessor
+from oarepo_model_builder.property_preprocessors.datatype_preprocessor import (
+    DataTypePreprocessor,
+)
 from oarepo_model_builder.schema import ModelSchema
 from oarepo_model_builder.validation.model_validation import model_validator
-from tests.multilang import (MultilangPreprocessor, MultilingualDataType,
-                             UIValidator)
+from tests.multilang import MultilangPreprocessor, MultilingualDataType, UIValidator
 
 try:
     import json5
 except ImportError:
     import json as json5
 
 
@@ -276,55 +280,55 @@
                         "read": False,
                         "field-class": "ma_fields.String",
                         "validators": [],
                         "imports": [],
                     },
                     "type": "keyword",
                     "sample": {"skip": True},
-                    "facets": {"searchable": True}
+                    "facets": {"searchable": True},
                 },
                 "created": {
                     "marshmallow": {
                         "write": False,
                         "read": True,
                         "field-class": "ma_fields.String",
                         "validators": ["validate_date('%Y-%m-%d')"],
                         "imports": [
                             {"import": "oarepo_runtime.validation.validate_date"}
                         ],
                     },
                     "type": "date",
                     "sample": {"skip": True},
-                    "facets": {"searchable": True}
+                    "facets": {"searchable": True},
                 },
                 "updated": {
                     "marshmallow": {
                         "write": False,
                         "read": True,
                         "field-class": "ma_fields.String",
                         "validators": ["validate_date('%Y-%m-%d')"],
                         "imports": [
                             {"import": "oarepo_runtime.validation.validate_date"}
                         ],
                     },
                     "type": "date",
                     "sample": {"skip": True},
-                    "facets": {"searchable": True}
+                    "facets": {"searchable": True},
                 },
                 "$schema": {
                     "marshmallow": {
                         "write": False,
                         "read": False,
                         "field-class": "ma_fields.String",
                         "validators": [],
                         "imports": [],
                     },
                     "type": "keyword",
                     "sample": {"skip": True},
-                    "facets": {"searchable": True}
+                    "facets": {"searchable": True},
                 },
             },
             "config-resource-register-blueprint-key": "TEST_REGISTER_BLUEPRINT",
             "record-facets-class": "test.services.records.facets.Test",
             "record-permissions-class": "test.services.records.permissions.TestPermissionPolicy",
             "create-blueprint-from-app": "test.views.create_blueprint_from_app_test",
             "script-import-sample-data": "data/sample_data.yaml",
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_overwrite.py` & `oarepo-model-builder-3.2.9/tests/test_overwrite.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,16 +2,15 @@
 import os
 import re
 import shutil
 import sys
 from pathlib import Path
 from tempfile import mkdtemp, tempdir
 
-from oarepo_model_builder.entrypoints import (create_builder_from_entrypoints,
-                                              load_model)
+from oarepo_model_builder.entrypoints import create_builder_from_entrypoints, load_model
 from oarepo_model_builder.fs import FileSystem, InMemoryFileSystem
 from tests.utils import assert_python_equals
 
 OAREPO_USE = "use"
 
 
 def test_overwrite():
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_plugin_configuration.py` & `oarepo-model-builder-3.2.9/tests/test_plugin_configuration.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/tests/test_python_mergers.py` & `oarepo-model-builder-3.2.9/tests/test_python_mergers.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/tests/test_raw.py` & `oarepo-model-builder-3.2.9/tests/test_raw.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 import json
 import os
 import re
 from pathlib import Path
 
-from oarepo_model_builder.entrypoints import (create_builder_from_entrypoints,
-                                              load_model)
+from oarepo_model_builder.entrypoints import create_builder_from_entrypoints, load_model
 from oarepo_model_builder.fs import InMemoryFileSystem
 from tests.utils import assert_python_equals
 
 
 def test_raw_type():
     schema = load_model(
         "test.yaml",
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_sample_builder.py` & `oarepo-model-builder-3.2.9/tests/test_sample_builder.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 from pathlib import Path
 
 import faker.config
 
 from oarepo_model_builder.entrypoints import create_builder_from_entrypoints
 from oarepo_model_builder.fs import InMemoryFileSystem
-from oarepo_model_builder.invenio.invenio_script_sample_data import \
-    InvenioScriptSampleDataBuilder
+from oarepo_model_builder.invenio.invenio_script_sample_data import (
+    InvenioScriptSampleDataBuilder,
+)
 from oarepo_model_builder.schema import ModelSchema
 
 
 def test_sample_builder_string():
     assert (
         build_sample_data(
             {
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_schema_props.py` & `oarepo-model-builder-3.2.9/tests/test_schema_props.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 import json
 import os
 import re
 from pathlib import Path
 
-from oarepo_model_builder.entrypoints import (create_builder_from_entrypoints,
-                                              load_model)
+from oarepo_model_builder.entrypoints import create_builder_from_entrypoints, load_model
 from oarepo_model_builder.fs import InMemoryFileSystem
 from tests.utils import assert_python_equals
 
 
 def test_enum():
     schema = load_model(
         "test.yaml",
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_search_options.py` & `oarepo-model-builder-3.2.9/tests/test_search_options.py`

 * *Files 0% similar despite different names*

```diff
@@ -7,15 +7,14 @@
 
 from oarepo_model_builder.entrypoints import create_builder_from_entrypoints, load_model
 from oarepo_model_builder.fs import InMemoryFileSystem
 
 DUMMY_YAML = "test.yaml"
 
 
-
 def test_sort():
     schema = load_model(
         DUMMY_YAML,
         "test",
         model_content={
             "model": {
                 "use": "invenio",
@@ -70,15 +69,14 @@
     'a_test': {'fields': ['a']},
     'b_test': {'fields': ['-b']},
     }
     """,
     )
 
 
-
 def test_search_class():
     schema = load_model(
         DUMMY_YAML,
         "test",
         model_content={
             "model": {
                 "use": "invenio",
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_shortcuts.py` & `oarepo-model-builder-3.2.9/tests/test_shortcuts.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,15 @@
 import json
 import os
 import re
 from pathlib import Path
 
 import yaml
 
-from oarepo_model_builder.entrypoints import (create_builder_from_entrypoints,
-                                              load_model)
+from oarepo_model_builder.entrypoints import create_builder_from_entrypoints, load_model
 from oarepo_model_builder.fs import InMemoryFileSystem
 from tests.utils import assert_python_equals
 
 
 def test_array_shortcuts():
     schema = load_model(
         "test.yaml",  # NOSONAR
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_stack.py` & `oarepo-model-builder-3.2.9/tests/test_stack.py`

 * *Files identical despite different names*

### Comparing `oarepo-model-builder-3.2.8/tests/test_type_shortcuts.py` & `oarepo-model-builder-3.2.9/tests/test_type_shortcuts.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,16 +1,17 @@
 import os
 
 import json5
 
 from oarepo_model_builder.builder import ModelBuilder
 from oarepo_model_builder.builders.jsonschema import JSONSchemaBuilder
 from oarepo_model_builder.fs import InMemoryFileSystem
-from oarepo_model_builder.model_preprocessors.default_values import \
-    DefaultValuesModelPreprocessor
+from oarepo_model_builder.model_preprocessors.default_values import (
+    DefaultValuesModelPreprocessor,
+)
 from oarepo_model_builder.outputs.jsonschema import JSONSchemaOutput
 from oarepo_model_builder.outputs.python import PythonOutput
 from oarepo_model_builder.schema import ModelSchema
 
 
 def test_object():
     data = build_jsonschema(
```

### Comparing `oarepo-model-builder-3.2.8/tests/test_validation.py` & `oarepo-model-builder-3.2.9/tests/test_validation.py`

 * *Files identical despite different names*

