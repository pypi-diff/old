# Comparing `tmp/metaphor-connectors-0.9.3.tar.gz` & `tmp/metaphor-connectors-0.9.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "metaphor-connectors-0.9.3.tar", max compression
+gzip compressed data, was "metaphor-connectors-0.9.4.tar", max compression
```

## Comparing `metaphor-connectors-0.9.3.tar` & `metaphor-connectors-0.9.4.tar`

### file list

```diff
@@ -1,105 +1,105 @@
--rw-r--r--   0        0        0    11357 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/LICENSE
--rw-r--r--   0        0        0     2242 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/__init__.py
--rw-r--r--   0        0        0      174 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/__main__.py
--rw-r--r--   0        0        0      801 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/config.py
--rw-r--r--   0        0        0     6178 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/extractor.py
--rw-r--r--   0        0        0     1316 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/profile/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/profile/__init__.py
--rw-r--r--   0        0        0      296 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/profile/__main__.py
--rw-r--r--   0        0        0      337 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/profile/config.py
--rw-r--r--   0        0        0     7953 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/profile/extractor.py
--rw-r--r--   0        0        0     2137 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/usage/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/usage/__init__.py
--rw-r--r--   0        0        0      190 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/usage/__main__.py
--rw-r--r--   0        0        0      475 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/usage/config.py
--rw-r--r--   0        0        0     5804 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/bigquery/usage/extractor.py
--rw-r--r--   0        0        0     1087 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/__init__.py
--rw-r--r--   0        0        0     1936 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/api_sink.py
--rw-r--r--   0        0        0      879 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/cli.py
--rw-r--r--   0        0        0     1292 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/docs/filter.md
--rw-r--r--   0        0        0      555 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/docs/sampling.md
--rw-r--r--   0        0        0     1552 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/entity_id.py
--rw-r--r--   0        0        0     3028 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/event_util.py
--rw-r--r--   0        0        0     3220 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/extractor.py
--rw-r--r--   0        0        0     2729 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/file_sink.py
--rw-r--r--   0        0        0     2773 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/filter.py
--rw-r--r--   0        0        0      402 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/logger.py
--rw-r--r--   0        0        0     1013 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/s3.py
--rw-r--r--   0        0        0      362 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/sampling.py
--rw-r--r--   0        0        0     1126 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/sink.py
--rw-r--r--   0        0        0     5843 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/common/usage_util.py
--rw-r--r--   0        0        0     1816 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/dbt/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/dbt/__init__.py
--rw-r--r--   0        0        0      159 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/dbt/__main__.py
--rw-r--r--   0        0        0      582 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/dbt/config.py
--rw-r--r--   0        0        0    17383 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/dbt/extractor.py
--rwxr-xr-x   0        0        0      777 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/dbt/gen_models.sh
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/dbt/generated/__init__.py
--rw-r--r--   0        0        0     1842 2022-01-21 16:25:16.347592 metaphor-connectors-0.9.3/metaphor/dbt/generated/dbt_catalog_v1.py
--rw-r--r--   0        0        0    38493 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/dbt/generated/dbt_manifest_v1.py
--rw-r--r--   0        0        0    39482 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/dbt/generated/dbt_manifest_v2.py
--rw-r--r--   0        0        0    40223 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/dbt/generated/dbt_manifest_v3.py
--rw-r--r--   0        0        0    45588 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/dbt/generated/dbt_manifest_v4.py
--rw-r--r--   0        0        0       28 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/google_directory/.gitignore
--rw-r--r--   0        0        0     2838 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/google_directory/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/google_directory/__init__.py
--rw-r--r--   0        0        0      187 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/google_directory/__main__.py
--rw-r--r--   0        0        0     1827 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/google_directory/authenticate.py
--rw-r--r--   0        0        0     3817 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/google_directory/extractor.py
--rw-r--r--   0        0        0     3770 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/looker/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/looker/__init__.py
--rw-r--r--   0        0        0      168 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/looker/__main__.py
--rw-r--r--   0        0        0     1105 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/looker/config.py
--rw-r--r--   0        0        0     6983 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/looker/extractor.py
--rw-r--r--   0        0        0    11906 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/looker/lookml_parser.py
--rw-r--r--   0        0        0     1668 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/metabase/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/metabase/__init__.py
--rw-r--r--   0        0        0      174 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/metabase/__main__.py
--rw-r--r--   0        0        0      232 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/metabase/config.py
--rw-r--r--   0        0        0     9154 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/metabase/extractor.py
--rw-r--r--   0        0        0     1618 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/postgresql/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/postgresql/__init__.py
--rw-r--r--   0        0        0      180 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/postgresql/__main__.py
--rw-r--r--   0        0        0      493 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/postgresql/config.py
--rw-r--r--   0        0        0    11254 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/postgresql/extractor.py
--rw-r--r--   0        0        0     1639 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/redshift/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/redshift/__init__.py
--rw-r--r--   0        0        0      174 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/redshift/__main__.py
--rw-r--r--   0        0        0      218 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/redshift/config.py
--rw-r--r--   0        0        0     2365 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/redshift/extractor.py
--rw-r--r--   0        0        0     1158 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/redshift/usage/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/redshift/usage/__init__.py
--rw-r--r--   0        0        0      190 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/redshift/usage/__main__.py
--rw-r--r--   0        0        0      447 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/redshift/usage/config.py
--rw-r--r--   0        0        0     4350 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/redshift/usage/extractor.py
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/slack_directory/__init__.py
--rw-r--r--   0        0        0      166 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/slack_directory/__main__.py
--rw-r--r--   0        0        0     2940 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/slack_directory/extractor.py
--rw-r--r--   0        0        0     3694 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/__init__.py
--rw-r--r--   0        0        0      177 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/__main__.py
--rw-r--r--   0        0        0     2687 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/auth.py
--rw-r--r--   0        0        0      600 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/config.py
--rw-r--r--   0        0        0    10931 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/extractor.py
--rw-r--r--   0        0        0     2283 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/profile/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/profile/__init__.py
--rw-r--r--   0        0        0      195 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/profile/__main__.py
--rw-r--r--   0        0        0      445 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/profile/config.py
--rw-r--r--   0        0        0     8983 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/profile/extractor.py
--rw-r--r--   0        0        0     1767 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/usage/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/usage/__init__.py
--rw-r--r--   0        0        0      193 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/usage/__main__.py
--rw-r--r--   0        0        0      595 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/usage/config.py
--rw-r--r--   0        0        0     5887 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/usage/extractor.py
--rw-r--r--   0        0        0     2685 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/snowflake/utils.py
--rw-r--r--   0        0        0     2736 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/tableau/README.md
--rw-r--r--   0        0        0        0 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/tableau/__init__.py
--rw-r--r--   0        0        0      171 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/tableau/__main__.py
--rw-r--r--   0        0        0      728 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/tableau/config.py
--rw-r--r--   0        0        0     8133 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/tableau/extractor.py
--rw-r--r--   0        0        0      736 2022-01-21 16:25:16.351593 metaphor-connectors-0.9.3/metaphor/tableau/query.py
--rw-r--r--   0        0        0     2737 2022-01-21 16:25:16.355593 metaphor-connectors-0.9.3/pyproject.toml
--rw-r--r--   0        0        0     2536 2022-01-21 16:25:26.667107 metaphor-connectors-0.9.3/setup.py
--rw-r--r--   0        0        0     2202 2022-01-21 16:25:26.667568 metaphor-connectors-0.9.3/PKG-INFO
+-rw-r--r--   0        0        0    11357 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/LICENSE
+-rw-r--r--   0        0        0     2242 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/__init__.py
+-rw-r--r--   0        0        0      174 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/__main__.py
+-rw-r--r--   0        0        0      801 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/config.py
+-rw-r--r--   0        0        0     6178 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/extractor.py
+-rw-r--r--   0        0        0     1316 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/profile/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/profile/__init__.py
+-rw-r--r--   0        0        0      296 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/profile/__main__.py
+-rw-r--r--   0        0        0      337 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/profile/config.py
+-rw-r--r--   0        0        0     7953 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/profile/extractor.py
+-rw-r--r--   0        0        0     2137 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/usage/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/usage/__init__.py
+-rw-r--r--   0        0        0      190 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/usage/__main__.py
+-rw-r--r--   0        0        0      475 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/usage/config.py
+-rw-r--r--   0        0        0     5804 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/bigquery/usage/extractor.py
+-rw-r--r--   0        0        0     1087 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/common/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/common/__init__.py
+-rw-r--r--   0        0        0     1936 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/common/api_sink.py
+-rw-r--r--   0        0        0      879 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/common/cli.py
+-rw-r--r--   0        0        0     1292 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/common/docs/filter.md
+-rw-r--r--   0        0        0      555 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/common/docs/sampling.md
+-rw-r--r--   0        0        0     1552 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/common/entity_id.py
+-rw-r--r--   0        0        0     3028 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/common/event_util.py
+-rw-r--r--   0        0        0     3220 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/common/extractor.py
+-rw-r--r--   0        0        0     2729 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/common/file_sink.py
+-rw-r--r--   0        0        0     2773 2022-01-25 06:32:50.759330 metaphor-connectors-0.9.4/metaphor/common/filter.py
+-rw-r--r--   0        0        0      402 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/common/logger.py
+-rw-r--r--   0        0        0     1013 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/common/s3.py
+-rw-r--r--   0        0        0      362 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/common/sampling.py
+-rw-r--r--   0        0        0     1126 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/common/sink.py
+-rw-r--r--   0        0        0     5843 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/common/usage_util.py
+-rw-r--r--   0        0        0     1816 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/dbt/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/dbt/__init__.py
+-rw-r--r--   0        0        0      159 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/dbt/__main__.py
+-rw-r--r--   0        0        0      582 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/dbt/config.py
+-rw-r--r--   0        0        0    17383 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/dbt/extractor.py
+-rwxr-xr-x   0        0        0      777 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/dbt/gen_models.sh
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/dbt/generated/__init__.py
+-rw-r--r--   0        0        0     1842 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/dbt/generated/dbt_catalog_v1.py
+-rw-r--r--   0        0        0    38493 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/dbt/generated/dbt_manifest_v1.py
+-rw-r--r--   0        0        0    39482 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/dbt/generated/dbt_manifest_v2.py
+-rw-r--r--   0        0        0    40223 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/dbt/generated/dbt_manifest_v3.py
+-rw-r--r--   0        0        0    45588 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/dbt/generated/dbt_manifest_v4.py
+-rw-r--r--   0        0        0       28 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/google_directory/.gitignore
+-rw-r--r--   0        0        0     2838 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/google_directory/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/google_directory/__init__.py
+-rw-r--r--   0        0        0      187 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/google_directory/__main__.py
+-rw-r--r--   0        0        0     1827 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/google_directory/authenticate.py
+-rw-r--r--   0        0        0     3817 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/google_directory/extractor.py
+-rw-r--r--   0        0        0     3770 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/looker/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/looker/__init__.py
+-rw-r--r--   0        0        0      168 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/looker/__main__.py
+-rw-r--r--   0        0        0     1105 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/looker/config.py
+-rw-r--r--   0        0        0     6983 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/looker/extractor.py
+-rw-r--r--   0        0        0    11906 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/looker/lookml_parser.py
+-rw-r--r--   0        0        0     1668 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/metabase/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/metabase/__init__.py
+-rw-r--r--   0        0        0      174 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/metabase/__main__.py
+-rw-r--r--   0        0        0      232 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/metabase/config.py
+-rw-r--r--   0        0        0     9154 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/metabase/extractor.py
+-rw-r--r--   0        0        0     1784 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/postgresql/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/postgresql/__init__.py
+-rw-r--r--   0        0        0      180 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/postgresql/__main__.py
+-rw-r--r--   0        0        0      493 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/postgresql/config.py
+-rw-r--r--   0        0        0    13646 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/postgresql/extractor.py
+-rw-r--r--   0        0        0     1688 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/redshift/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/redshift/__init__.py
+-rw-r--r--   0        0        0      174 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/redshift/__main__.py
+-rw-r--r--   0        0        0      218 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/redshift/config.py
+-rw-r--r--   0        0        0     2380 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/redshift/extractor.py
+-rw-r--r--   0        0        0     1158 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/redshift/usage/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/redshift/usage/__init__.py
+-rw-r--r--   0        0        0      190 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/redshift/usage/__main__.py
+-rw-r--r--   0        0        0      447 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/redshift/usage/config.py
+-rw-r--r--   0        0        0     4350 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/redshift/usage/extractor.py
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/slack_directory/__init__.py
+-rw-r--r--   0        0        0      166 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/slack_directory/__main__.py
+-rw-r--r--   0        0        0     2940 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/slack_directory/extractor.py
+-rw-r--r--   0        0        0     3694 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/__init__.py
+-rw-r--r--   0        0        0      177 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/__main__.py
+-rw-r--r--   0        0        0     2687 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/auth.py
+-rw-r--r--   0        0        0      600 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/config.py
+-rw-r--r--   0        0        0    10931 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/extractor.py
+-rw-r--r--   0        0        0     2283 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/profile/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/profile/__init__.py
+-rw-r--r--   0        0        0      195 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/profile/__main__.py
+-rw-r--r--   0        0        0      445 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/profile/config.py
+-rw-r--r--   0        0        0     8983 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/profile/extractor.py
+-rw-r--r--   0        0        0     1767 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/usage/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/usage/__init__.py
+-rw-r--r--   0        0        0      193 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/usage/__main__.py
+-rw-r--r--   0        0        0      595 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/usage/config.py
+-rw-r--r--   0        0        0     5887 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/usage/extractor.py
+-rw-r--r--   0        0        0     2685 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/snowflake/utils.py
+-rw-r--r--   0        0        0     2736 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/tableau/README.md
+-rw-r--r--   0        0        0        0 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/tableau/__init__.py
+-rw-r--r--   0        0        0      171 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/tableau/__main__.py
+-rw-r--r--   0        0        0      728 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/tableau/config.py
+-rw-r--r--   0        0        0     8133 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/tableau/extractor.py
+-rw-r--r--   0        0        0      736 2022-01-25 06:32:50.763330 metaphor-connectors-0.9.4/metaphor/tableau/query.py
+-rw-r--r--   0        0        0     2737 2022-01-25 06:32:50.767330 metaphor-connectors-0.9.4/pyproject.toml
+-rw-r--r--   0        0        0     2536 2022-01-25 06:32:59.376727 metaphor-connectors-0.9.4/setup.py
+-rw-r--r--   0        0        0     2202 2022-01-25 06:32:59.377115 metaphor-connectors-0.9.4/PKG-INFO
```

### Comparing `metaphor-connectors-0.9.3/LICENSE` & `metaphor-connectors-0.9.4/LICENSE`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/bigquery/README.md` & `metaphor-connectors-0.9.4/metaphor/bigquery/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/bigquery/config.py` & `metaphor-connectors-0.9.4/metaphor/bigquery/config.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/bigquery/extractor.py` & `metaphor-connectors-0.9.4/metaphor/bigquery/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/bigquery/profile/README.md` & `metaphor-connectors-0.9.4/metaphor/bigquery/profile/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/bigquery/profile/extractor.py` & `metaphor-connectors-0.9.4/metaphor/bigquery/profile/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/bigquery/usage/README.md` & `metaphor-connectors-0.9.4/metaphor/bigquery/usage/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/bigquery/usage/extractor.py` & `metaphor-connectors-0.9.4/metaphor/bigquery/usage/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/README.md` & `metaphor-connectors-0.9.4/metaphor/common/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/api_sink.py` & `metaphor-connectors-0.9.4/metaphor/common/api_sink.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/cli.py` & `metaphor-connectors-0.9.4/metaphor/common/cli.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/docs/filter.md` & `metaphor-connectors-0.9.4/metaphor/common/docs/filter.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/docs/sampling.md` & `metaphor-connectors-0.9.4/metaphor/common/docs/sampling.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/entity_id.py` & `metaphor-connectors-0.9.4/metaphor/common/entity_id.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/event_util.py` & `metaphor-connectors-0.9.4/metaphor/common/event_util.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/extractor.py` & `metaphor-connectors-0.9.4/metaphor/common/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/file_sink.py` & `metaphor-connectors-0.9.4/metaphor/common/file_sink.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/filter.py` & `metaphor-connectors-0.9.4/metaphor/common/filter.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/s3.py` & `metaphor-connectors-0.9.4/metaphor/common/s3.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/sink.py` & `metaphor-connectors-0.9.4/metaphor/common/sink.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/common/usage_util.py` & `metaphor-connectors-0.9.4/metaphor/common/usage_util.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/dbt/README.md` & `metaphor-connectors-0.9.4/metaphor/dbt/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/dbt/config.py` & `metaphor-connectors-0.9.4/metaphor/dbt/config.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/dbt/extractor.py` & `metaphor-connectors-0.9.4/metaphor/dbt/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/dbt/gen_models.sh` & `metaphor-connectors-0.9.4/metaphor/dbt/gen_models.sh`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/dbt/generated/dbt_catalog_v1.py` & `metaphor-connectors-0.9.4/metaphor/dbt/generated/dbt_catalog_v1.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/dbt/generated/dbt_manifest_v1.py` & `metaphor-connectors-0.9.4/metaphor/dbt/generated/dbt_manifest_v1.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/dbt/generated/dbt_manifest_v2.py` & `metaphor-connectors-0.9.4/metaphor/dbt/generated/dbt_manifest_v2.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/dbt/generated/dbt_manifest_v3.py` & `metaphor-connectors-0.9.4/metaphor/dbt/generated/dbt_manifest_v3.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/dbt/generated/dbt_manifest_v4.py` & `metaphor-connectors-0.9.4/metaphor/dbt/generated/dbt_manifest_v4.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/google_directory/README.md` & `metaphor-connectors-0.9.4/metaphor/google_directory/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/google_directory/authenticate.py` & `metaphor-connectors-0.9.4/metaphor/google_directory/authenticate.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/google_directory/extractor.py` & `metaphor-connectors-0.9.4/metaphor/google_directory/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/looker/README.md` & `metaphor-connectors-0.9.4/metaphor/looker/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/looker/config.py` & `metaphor-connectors-0.9.4/metaphor/looker/config.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/looker/extractor.py` & `metaphor-connectors-0.9.4/metaphor/looker/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/looker/lookml_parser.py` & `metaphor-connectors-0.9.4/metaphor/looker/lookml_parser.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/metabase/README.md` & `metaphor-connectors-0.9.4/metaphor/metabase/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/metabase/extractor.py` & `metaphor-connectors-0.9.4/metaphor/metabase/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/postgresql/README.md` & `metaphor-connectors-0.9.4/metaphor/redshift/README.md`

 * *Files 12% similar despite different names*

```diff
@@ -1,16 +1,20 @@
-# PostgreSQL Connector
+# Redshift Connector
 
-This connector extracts technical metadata from a PostgreSQL database using [asyncpg](https://github.com/MagicStack/asyncpg) library.
+This connector extracts technical metadata from a Redshift database using [asyncpg](https://github.com/MagicStack/asyncpg) library.
 
 ## Setup
 
-Currently you must run the connector using a user with `SELECT` [privilege](https://www.postgresql.org/docs/current/ddl-priv.html) to all tables & views.
+The connector extracts the metadata from [system catalogs](https://docs.aws.amazon.com/redshift/latest/dg/c_intro_catalog_views.html), with restricted access to system tables and additional `SELECT` [privilege](https://www.postgresql.org/docs/current/ddl-priv.html) to `pg_catalog.svv_table_info`.  
 
-> We're working on extracting the metadata from [system catalogs](https://www.postgresql.org/docs/current/catalogs.html), which greatly reduces the privileges required for the user.
+Use the following command to grant the permission:
+
+```sql
+GRANT SELECT ON pg_catalog.svv_table_info TO <User>;
+```
 
 ## Config File
 
 Create a YAML config file based on the following template.
 
 ### Required Configurations
 
@@ -26,26 +30,26 @@
     path: <path_to_output_file>
 ```
 
 See [Common Configurations](../common/README.md) for more information on `output`.
 
 ### Optional Configurations
 
-By default, the connector will connect using the default PostgreSQL port 5432. You can change it using the following config:
+By default, the connector will connect using the default Redshift port 5439. You can change it using the following config:
 
 ```yaml
 port: <port_number>
 ```
 
 See [Filter Configurations](../common/docs/filter.md) for more information on the optional `filter` config.
 
 ## Testing
 
-Follow the [Installation](../../README.md) instructions to install `metaphor-connectors` in your environment (or virtualenv). Make sure to include either `all` or `postgresql` extra.
+Follow the [Installation](../../README.md) instructions to install `metaphor-connectors` in your environment (or virtualenv). Make sure to include either `all` or `redshift` extra.
 
 To test the connector locally, change the config file to output to a local path and run the following command
 
 ```shell
-python -m metaphor.postgresql <config_file>
+python -m metaphor.redshift <config_file>
 ```
 
 Manually verify the output after the run finishes.
```

### Comparing `metaphor-connectors-0.9.3/metaphor/postgresql/extractor.py` & `metaphor-connectors-0.9.4/metaphor/postgresql/extractor.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from typing import Dict, List
+from typing import Dict, List, Optional, Tuple
 
 from asyncpg import Connection
 
 from metaphor.common.event_util import EventUtil
 from metaphor.common.logger import get_logger
 from metaphor.postgresql.config import PostgreSQLRunConfig
 
@@ -62,15 +62,15 @@
             if filter.includes is None
             else list(filter.includes.keys())
         )
 
         for db in databases:
             conn = await self._connect_database(config, db)
             try:
-                await self._fetch_tables(conn, filter)
+                await self._fetch_tables(conn, db, filter)
                 await self._fetch_columns(conn, db, filter)
                 await self._fetch_constraints(conn, db)
             finally:
                 await conn.close()
 
         return [EventUtil.build_dataset_event(d) for d in self._datasets.values()]
 
@@ -102,72 +102,89 @@
             return databases
         finally:
             await conn.close()
 
     # Exclude schemas in WHERE clause, e.g. table_schema not in ($1, $2, ...)
     _excluded_schemas_clause = f" table_schema NOT IN ({','.join([f'${i + 1}' for i in range(len(_ignored_schemas))])})"
 
-    async def _fetch_tables(self, conn: Connection, filter: DatasetFilter) -> None:
-
+    async def _fetch_tables(
+        self, conn: Connection, database: str, filter: DatasetFilter
+    ) -> None:
         results = await conn.fetch(
-            f"""
-            SELECT table_catalog, table_schema, table_name, table_type, pgd.description,
-                pgc.reltuples::bigint AS row_count,
-                pg_total_relation_size('"' || table_schema || '"."' || table_name || '"') as table_size
-            FROM information_schema.tables t
-            JOIN pg_class pgc
-              ON pgc.relname = t.table_name
-                AND pgc.relnamespace = (
-                  SELECT oid FROM pg_catalog.pg_namespace WHERE nspname = t.table_schema
-                )
+            """
+            SELECT schemaname, tablename AS name, pgd.description, pgc.reltuples::bigint AS row_count,
+                pg_total_relation_size('"' || schemaname || '"."' || tablename || '"') AS table_size,
+                'TABLE' as table_type
+            FROM pg_catalog.pg_tables t
+            LEFT JOIN pg_class pgc
+              ON pgc.relname = t.tablename
+            LEFT JOIN pg_catalog.pg_description pgd
+              ON pgd.objoid = pgc.oid AND pgd.objsubid = 0
+            WHERE schemaname !~ '^pg_' AND schemaname != 'information_schema'
+            UNION
+            SELECT schemaname, viewname AS name, pgd.description, pgc.reltuples::bigint AS row_count,
+                pg_total_relation_size('"' || schemaname || '"."' || viewname || '"') AS table_size,
+                'VIEW' as table_type
+            FROM pg_catalog.pg_views v
+            LEFT JOIN pg_class pgc
+              ON pgc.relname = v.viewname
             LEFT JOIN pg_catalog.pg_description pgd
               ON pgd.objoid = pgc.oid AND pgd.objsubid = 0
-            WHERE {self._excluded_schemas_clause}
-            ORDER BY table_schema, table_name;
-            """,
-            *_ignored_schemas,
+            WHERE schemaname != 'information_schema' and schemaname !~ '^pg_'
+            ORDER BY schemaname, name;
+            """
         )
 
         for table in results:
-            catalog = table["table_catalog"]
-            schema = table["table_schema"]
-            name = table["table_name"]
-            table_type = table["table_type"]
+            schema = table["schemaname"]
+            name = table["name"]
             description = table["description"]
             row_count = table["row_count"]
             table_size = table["table_size"]
-            full_name = self._dataset_name(catalog, schema, name)
-            if not include_table(catalog, schema, name, filter):
+            table_type = table["table_type"]
+            full_name = self._dataset_name(database, schema, name)
+            if not include_table(database, schema, name, filter):
                 logger.info(f"Ignore {full_name} due to filter config")
                 continue
             self._init_dataset(
                 full_name, table_type, description, row_count, table_size
             )
 
     async def _fetch_columns(
         self, conn: Connection, catalog: str, filter: DatasetFilter
     ) -> None:
         columns = await conn.fetch(
-            f"""
-            SELECT table_schema, table_name, ordinal_position, column_name, data_type,
-                   character_maximum_length, numeric_precision, is_nullable, pgd.description
-            FROM information_schema.columns AS cols
-            JOIN (
-                    SELECT pgc.oid, relname, nspname
-                    FROM pg_class pgc
-                    JOIN pg_catalog.pg_namespace pgn
-                        ON relnamespace = pgn.oid
-                ) pg
-                ON table_schema = nspname AND table_name = relname
-            LEFT JOIN pg_catalog.pg_description pgd
-              ON pgd.objoid = pg.oid AND pgd.objsubid = cols.ordinal_position
-            WHERE {self._excluded_schemas_clause}
-            ORDER BY table_schema, table_name, ordinal_position;
-            """,
-            *_ignored_schemas,
+            """
+            SELECT nc.nspname AS table_schema, c.relname AS table_name,
+                a.attnum AS ordinal_position, a.attname AS column_name,
+                a.attnotnull AS not_null, format_type(a.atttypid, a.atttypmod) AS format,
+                CASE WHEN t.typtype = 'd' THEN
+                  CASE WHEN bt.typelem <> 0 AND bt.typlen = -1 THEN 'ARRAY'
+                        WHEN nbt.nspname = 'pg_catalog' THEN format_type(t.typbasetype, null)
+                        ELSE 'USER-DEFINED' END
+                ELSE
+                  CASE WHEN t.typelem <> 0 AND t.typlen = -1 THEN 'ARRAY'
+                        WHEN nt.nspname = 'pg_catalog' THEN format_type(a.atttypid, null)
+                        ELSE 'USER-DEFINED' END
+                END AS data_type,
+                pgd.description
+            FROM (pg_attribute a LEFT JOIN pg_attrdef ad ON attrelid = adrelid AND attnum = adnum)
+                 JOIN (pg_class c JOIN pg_namespace nc ON (c.relnamespace = nc.oid)) ON a.attrelid = c.oid
+                 JOIN (pg_type t JOIN pg_namespace nt ON (t.typnamespace = nt.oid)) ON a.atttypid = t.oid
+                 LEFT JOIN (pg_type bt JOIN pg_namespace nbt ON (bt.typnamespace = nbt.oid))
+                   ON (t.typtype = 'd' AND t.typbasetype = bt.oid)
+                 LEFT JOIN pg_catalog.pg_description pgd
+                   ON pgd.objoid = c.oid AND pgd.objsubid = a.attnum
+            WHERE
+              c.relkind in ('r', 'v', 'f', 'p')
+              AND nc.nspname != 'information_schema' and nc.nspname !~ '^pg_'
+              AND a.attnum > 0
+              AND NOT a.attisdropped
+            ORDER BY nc.nspname, c.relname, a.attnum
+            """
         )
 
         for column in columns:
             schema, name = column["table_schema"], column["table_name"]
             full_name = self._dataset_name(catalog, schema, name)
             if not include_table(catalog, schema, name, filter):
                 logger.info(f"Ignore {full_name} due to filter config")
@@ -176,32 +193,41 @@
             assert dataset.schema is not None and dataset.schema.fields is not None
 
             dataset.schema.fields.append(PostgreSQLExtractor._build_field(column))
 
     async def _fetch_constraints(self, conn: Connection, catalog: str) -> None:
         constraints = await conn.fetch(
             """
-            SELECT constraints.table_schema, constraints.table_name,
-              constraints.constraint_name, constraints.constraint_type,
-              string_agg(key_col.column_name, ',') AS key_columns,
-              constraint_col.table_catalog AS constraint_db,
-              constraint_col.table_schema AS constraint_schema,
-              constraint_col.table_name AS constraint_table,
-              string_agg(constraint_col.column_name, ',') AS constraint_columns
-            FROM information_schema.table_constraints AS constraints
-            LEFT OUTER JOIN information_schema.key_column_usage AS key_col
-              ON constraints.table_schema = key_col.table_schema
-              AND constraints.constraint_name = key_col.constraint_name
-            LEFT OUTER JOIN  information_schema.constraint_column_usage AS constraint_col
-              ON constraints.table_schema = constraint_col.table_schema
-              AND constraints.constraint_name = constraint_col.constraint_name
-            WHERE constraints.constraint_type IN ('PRIMARY KEY', 'UNIQUE', 'FOREIGN KEY')
-            GROUP BY constraints.table_schema, constraints.table_name, constraints.constraint_name,
-              constraints.constraint_type, constraint_col.table_catalog, constraint_col.table_schema,
-              constraint_col.table_name;
+            SELECT nr.nspname AS table_schema, r.relname AS table_name,
+                   c.conname AS constraint_name,
+                   CASE c.contype WHEN 'f' THEN 'FOREIGN KEY'
+                                    WHEN 'p' THEN 'PRIMARY KEY'
+                                    WHEN 'u' THEN 'UNIQUE' END
+                   AS constraint_type,
+                   string_agg(a.attname, ',') AS key_columns,
+                   string_agg(af.attname, ',') AS constraint_columns,
+                   current_database() AS constraint_db,
+                   nf.nspname AS constraint_schema, rf.relname AS constraint_table
+            FROM (
+                SELECT cc.conname, unnest(cc.conkey) AS conkey_id, unnest(cc.confkey) AS confkey_id,
+                       cc.connamespace, cc.conrelid, cc.confrelid, cc.contype
+                FROM pg_constraint cc
+            ) AS c
+            JOIN pg_namespace nc ON c.connamespace = nc.oid
+            JOIN pg_class r ON r.oid = c.conrelid
+            JOIN pg_namespace nr ON nr.oid = r.relnamespace
+            LEFT OUTER JOIN pg_attribute a ON a.attrelid = c.conrelid AND c.conkey_id = a.attnum
+            LEFT OUTER JOIN pg_attribute af ON af.attrelid = c.confrelid AND c.confkey_id = af.attnum
+            LEFT JOIN pg_class rf ON rf.oid = af.attrelid
+            LEFT JOIN pg_namespace nf ON nf.oid = rf.relnamespace
+            WHERE c.contype IN ('f', 'p', 'u')
+                  AND r.relkind IN ('r', 'p')
+                  AND (NOT pg_is_other_temp_schema(nr.oid))
+            GROUP BY table_schema, table_name, constraint_name, constraint_type,
+                     constraint_db, constraint_schema, constraint_table;
             """
         )
 
         if not constraints:
             return
 
         for constraint in constraints:
@@ -247,25 +273,48 @@
         # There is no reliable way to directly get data last modified time, can explore alternatives in future
         # https://dba.stackexchange.com/questions/58214/getting-last-modification-date-of-a-postgresql-database-table/168752
 
         self._datasets[full_name] = dataset
 
     @staticmethod
     def _build_field(column) -> SchemaField:
+        def parse_format_type(
+            native_type: str,
+            type_str: str,
+        ) -> Tuple[Optional[float], Optional[float]]:
+            precision, max_length = None, None
+
+            if native_type == "integer":
+                precision = 32.0
+            elif native_type == "smallint":
+                precision = 16.0
+            elif native_type == "bigint":
+                precision = 64.0
+            elif native_type == "real":
+                precision = 24
+            elif native_type == "double precision":
+                precision = 53
+            elif native_type == "numeric" and type_str != "numeric":
+                precision = float(type_str.split("(")[1].split(",")[0])
+
+            if native_type == "character varying" or native_type == "character":
+                max_length = float(type_str.split("(")[1].strip(")"))
+
+            return precision, max_length
+
+        native_type = column["data_type"]
+        precision, max_length = parse_format_type(native_type, column["format"])
+
         return SchemaField(
             field_path=column["column_name"],
-            native_type=column["data_type"],
-            nullable=column["is_nullable"] == "YES",
+            native_type=native_type,
+            nullable=(not column["not_null"]),
             description=column["description"],
-            max_length=float(column["character_maximum_length"])
-            if column["character_maximum_length"] is not None
-            else None,
-            precision=float(column["numeric_precision"])
-            if column["numeric_precision"] is not None
-            else None,
+            max_length=max_length,
+            precision=precision,
         )
 
     @staticmethod
     def _build_constraint(constraint: Dict, schema: SQLSchema) -> None:
         if constraint["constraint_type"] == "PRIMARY KEY":
             schema.primary_key = constraint["key_columns"].split(",")
         elif constraint["constraint_type"] == "FOREIGN KEY":
```

### Comparing `metaphor-connectors-0.9.3/metaphor/redshift/README.md` & `metaphor-connectors-0.9.4/metaphor/postgresql/README.md`

 * *Files 20% similar despite different names*

```diff
@@ -1,16 +1,26 @@
-# Redshift Connector
+# PostgreSQL Connector
 
-This connector extracts technical metadata from a Redshift database using [asyncpg](https://github.com/MagicStack/asyncpg) library.
+This connector extracts technical metadata from a PostgreSQL database using [asyncpg](https://github.com/MagicStack/asyncpg) library.
 
 ## Setup
 
-Currently you must run the connector using a user with `SELECT` [privilege](https://docs.aws.amazon.com/redshift/latest/dg/r_Privileges.html) to all tables & views.
+You must run the connector using a user with `SELECT` [privilege](https://www.postgresql.org/docs/current/ddl-priv.html) to the following tables:
 
-> We're working on extracting the metadata from [system catalogs](https://docs.aws.amazon.com/redshift/latest/dg/c_intro_catalog_views.html), which greatly reduces the privileges required for the user.
+- `pg_catalog.pg_constraint`
+- `pg_catalog.pg_class`
+- `pg_catalog.pg_namespace`
+- `pg_catalog.pg_attribute`
+- `pg_catalog.pg_description`
+
+Or, use the following command to grant the privileges:
+
+```sql
+GRANT SELECT ON pg_catalog.pg_constraint, pg_catalog.pg_class, pg_catalog.pg_namespace, pg_catalog.pg_attribute, pg_catalog.pg_description TO [User]
+```
 
 ## Config File
 
 Create a YAML config file based on the following template.
 
 ### Required Configurations
 
@@ -26,26 +36,26 @@
     path: <path_to_output_file>
 ```
 
 See [Common Configurations](../common/README.md) for more information on `output`.
 
 ### Optional Configurations
 
-By default, the connector will connect using the default Redshift port 5439. You can change it using the following config:
+By default, the connector will connect using the default PostgreSQL port 5432. You can change it using the following config:
 
 ```yaml
 port: <port_number>
 ```
 
 See [Filter Configurations](../common/docs/filter.md) for more information on the optional `filter` config.
 
 ## Testing
 
-Follow the [Installation](../../README.md) instructions to install `metaphor-connectors` in your environment (or virtualenv). Make sure to include either `all` or `redshift` extra.
+Follow the [Installation](../../README.md) instructions to install `metaphor-connectors` in your environment (or virtualenv). Make sure to include either `all` or `postgresql` extra.
 
 To test the connector locally, change the config file to output to a local path and run the following command
 
 ```shell
-python -m metaphor.redshift <config_file>
+python -m metaphor.postgresql <config_file>
 ```
 
 Manually verify the output after the run finishes.
```

### Comparing `metaphor-connectors-0.9.3/metaphor/redshift/extractor.py` & `metaphor-connectors-0.9.4/metaphor/redshift/extractor.py`

 * *Files 0% similar despite different names*

```diff
@@ -32,27 +32,27 @@
             if filter.includes is None
             else list(filter.includes.keys())
         )
 
         for db in databases:
             conn = await self._connect_database(config, db)
             try:
-                await self._fetch_tables(conn, filter)
+                await self._fetch_tables(conn, db, filter)
                 await self._fetch_columns(conn, db, filter)
                 await self._fetch_redshift_table_stats(conn, db)
             finally:
                 await conn.close()
 
         return [EventUtil.build_dataset_event(d) for d in self._datasets.values()]
 
     async def _fetch_redshift_table_stats(self, conn, catalog: str) -> None:
         results = await conn.fetch(
             """
             SELECT "schema", "table", size, tbl_rows
-            FROM svv_table_info;
+            FROM pg_catalog.svv_table_info;
             """,
         )
 
         for result in results:
             full_name = self._dataset_name(catalog, result["schema"], result["table"])
             if full_name not in self._datasets:
                 logger.warning(f"table {full_name} not found")
```

### Comparing `metaphor-connectors-0.9.3/metaphor/redshift/usage/README.md` & `metaphor-connectors-0.9.4/metaphor/redshift/usage/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/redshift/usage/extractor.py` & `metaphor-connectors-0.9.4/metaphor/redshift/usage/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/slack_directory/extractor.py` & `metaphor-connectors-0.9.4/metaphor/slack_directory/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/snowflake/README.md` & `metaphor-connectors-0.9.4/metaphor/snowflake/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/snowflake/auth.py` & `metaphor-connectors-0.9.4/metaphor/snowflake/auth.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/snowflake/config.py` & `metaphor-connectors-0.9.4/metaphor/snowflake/config.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/snowflake/extractor.py` & `metaphor-connectors-0.9.4/metaphor/snowflake/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/snowflake/profile/README.md` & `metaphor-connectors-0.9.4/metaphor/snowflake/profile/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/snowflake/profile/extractor.py` & `metaphor-connectors-0.9.4/metaphor/snowflake/profile/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/snowflake/usage/README.md` & `metaphor-connectors-0.9.4/metaphor/snowflake/usage/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/snowflake/usage/config.py` & `metaphor-connectors-0.9.4/metaphor/snowflake/usage/config.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/snowflake/usage/extractor.py` & `metaphor-connectors-0.9.4/metaphor/snowflake/usage/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/snowflake/utils.py` & `metaphor-connectors-0.9.4/metaphor/snowflake/utils.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/tableau/README.md` & `metaphor-connectors-0.9.4/metaphor/tableau/README.md`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/tableau/config.py` & `metaphor-connectors-0.9.4/metaphor/tableau/config.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/tableau/extractor.py` & `metaphor-connectors-0.9.4/metaphor/tableau/extractor.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/metaphor/tableau/query.py` & `metaphor-connectors-0.9.4/metaphor/tableau/query.py`

 * *Files identical despite different names*

### Comparing `metaphor-connectors-0.9.3/pyproject.toml` & `metaphor-connectors-0.9.4/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "metaphor-connectors"
-version = "0.9.3"
+version = "0.9.4"
 description = ""
 authors = ["Metaphor <dev@metaphor.io>"]
 packages = [
     { include = "metaphor" },
 ]
 
 [tool.poetry.dependencies]
```

### Comparing `metaphor-connectors-0.9.3/setup.py` & `metaphor-connectors-0.9.4/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -61,15 +61,15 @@
  'slack_directory': ['slack-sdk>=3.5.1,<4.0.0'],
  'snowflake': ['snowflake-connector-python>=2.7.0,<2.8.0',
                'sql-metadata==2.2.2'],
  'tableau': ['tableauserverclient>=0.17.0,<0.18.0']}
 
 setup_kwargs = {
     'name': 'metaphor-connectors',
-    'version': '0.9.3',
+    'version': '0.9.4',
     'description': '',
     'long_description': None,
     'author': 'Metaphor',
     'author_email': 'dev@metaphor.io',
     'maintainer': None,
     'maintainer_email': None,
     'url': None,
```

### Comparing `metaphor-connectors-0.9.3/PKG-INFO` & `metaphor-connectors-0.9.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: metaphor-connectors
-Version: 0.9.3
+Version: 0.9.4
 Summary: 
 Author: Metaphor
 Author-email: dev@metaphor.io
 Requires-Python: >=3.7,<3.11
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.7
```

