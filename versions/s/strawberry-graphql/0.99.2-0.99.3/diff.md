# Comparing `tmp/strawberry-graphql-0.99.2.tar.gz` & `tmp/strawberry-graphql-0.99.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "strawberry-graphql-0.99.2.tar", max compression
+gzip compressed data, was "strawberry-graphql-0.99.3.tar", max compression
```

## Comparing `strawberry-graphql-0.99.2.tar` & `strawberry-graphql-0.99.3.tar`

### file list

```diff
@@ -1,149 +1,149 @@
--rw-r--r--   0        0        0     1072 2022-03-04 15:52:37.931865 strawberry-graphql-0.99.2/LICENSE
--rw-r--r--   0        0        0     3976 2022-03-04 15:52:37.931865 strawberry-graphql-0.99.2/README.md
--rw-r--r--   0        0        0     4666 2022-03-04 15:52:52.860055 strawberry-graphql-0.99.2/pyproject.toml
--rw-r--r--   0        0        0      855 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/__init__.py
--rw-r--r--   0        0        0       60 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/__main__.py
--rw-r--r--   0        0        0        0 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/aiohttp/__init__.py
--rw-r--r--   0        0        0      322 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/aiohttp/handlers/__init__.py
--rw-r--r--   0        0        0     1950 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/aiohttp/handlers/graphql_transport_ws_handler.py
--rw-r--r--   0        0        0     2126 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/aiohttp/handlers/graphql_ws_handler.py
--rw-r--r--   0        0        0     4284 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/aiohttp/handlers/http_handler.py
--rw-r--r--   0        0        0     3561 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/aiohttp/views.py
--rw-r--r--   0        0        0     9155 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/annotation.py
--rw-r--r--   0        0        0     6512 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/arguments.py
--rw-r--r--   0        0        0     3993 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/asgi/__init__.py
--rw-r--r--   0        0        0      313 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/asgi/handlers/__init__.py
--rw-r--r--   0        0        0     2018 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/asgi/handlers/graphql_transport_ws_handler.py
--rw-r--r--   0        0        0     2204 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/asgi/handlers/graphql_ws_handler.py
--rw-r--r--   0        0        0     4952 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/asgi/handlers/http_handler.py
--rw-r--r--   0        0        0       72 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/asgi/test/__init__.py
--rw-r--r--   0        0        0     1321 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/asgi/test/client.py
--rw-r--r--   0        0        0      257 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/asgi/utils.py
--rw-r--r--   0        0        0       49 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/auto.py
--rw-r--r--   0        0        0        0 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/chalice/__init__.py
--rw-r--r--   0        0        0      690 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/chalice/graphiql.py
--rw-r--r--   0        0        0     3838 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/chalice/views.py
--rw-r--r--   0        0        0      257 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/cli/__init__.py
--rw-r--r--   0        0        0        0 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/cli/commands/__init__.py
--rw-r--r--   0        0        0     1043 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/cli/commands/export_schema.py
--rw-r--r--   0        0        0     2131 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/cli/commands/server.py
--rw-r--r--   0        0        0       67 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/cli/constants.py
--rw-r--r--   0        0        0      816 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/cli/debug_server.py
--rw-r--r--   0        0        0     3130 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/custom_scalar.py
--rw-r--r--   0        0        0     3449 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/dataloader.py
--rw-r--r--   0        0        0     1965 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/directive.py
--rw-r--r--   0        0        0      769 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/django/__init__.py
--rw-r--r--   0        0        0      135 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/django/apps.py
--rw-r--r--   0        0        0      494 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/django/context.py
--rw-r--r--   0        0        0       72 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/django/test/__init__.py
--rw-r--r--   0        0        0      586 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/django/test/client.py
--rw-r--r--   0        0        0     7755 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/django/views.py
--rw-r--r--   0        0        0     2085 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/enum.py
--rw-r--r--   0        0        0     6774 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/exceptions.py
--rw-r--r--   0        0        0       94 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/experimental/__init__.py
--rw-r--r--   0        0        0      242 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/experimental/pydantic/__init__.py
--rw-r--r--   0        0        0     3954 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/experimental/pydantic/conversion.py
--rw-r--r--   0        0        0      841 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/experimental/pydantic/conversion_types.py
--rw-r--r--   0        0        0     3909 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/experimental/pydantic/error_type.py
--rw-r--r--   0        0        0     1344 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/experimental/pydantic/exceptions.py
--rw-r--r--   0        0        0     1964 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/experimental/pydantic/fields.py
--rw-r--r--   0        0        0    10019 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/experimental/pydantic/object_type.py
--rw-r--r--   0        0        0     4111 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/experimental/pydantic/utils.py
--rw-r--r--   0        0        0     1249 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/ext/LICENSE
--rw-r--r--   0        0        0    30970 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/ext/mypy_plugin.py
--rw-r--r--   0        0        0      427 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/extensions/__init__.py
--rw-r--r--   0        0        0     1243 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/extensions/add_validation_rules.py
--rw-r--r--   0        0        0     1526 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/extensions/base_extension.py
--rw-r--r--   0        0        0     2703 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/extensions/context.py
--rw-r--r--   0        0        0     2325 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/extensions/directives.py
--rw-r--r--   0        0        0      661 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/extensions/disable_validation.py
--rw-r--r--   0        0        0     1148 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/extensions/parser_cache.py
--rw-r--r--   0        0        0     7715 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/extensions/query_depth_limiter.py
--rw-r--r--   0        0        0     2537 2022-03-04 15:52:37.939865 strawberry-graphql-0.99.2/strawberry/extensions/runner.py
--rw-r--r--   0        0        0      165 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/extensions/tracing/__init__.py
--rw-r--r--   0        0        0     5412 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/extensions/tracing/apollo.py
--rw-r--r--   0        0        0     5191 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/extensions/tracing/opentelemetry.py
--rw-r--r--   0        0        0      530 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/extensions/tracing/utils.py
--rw-r--r--   0        0        0      845 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/extensions/utils.py
--rw-r--r--   0        0        0     1297 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/extensions/validation_cache.py
--rw-r--r--   0        0        0      110 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/fastapi/__init__.py
--rw-r--r--   0        0        0      242 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/fastapi/handlers/__init__.py
--rw-r--r--   0        0        0      364 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/fastapi/handlers/graphql_transport_ws_handler.py
--rw-r--r--   0        0        0      319 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/fastapi/handlers/graphql_ws_handler.py
--rw-r--r--   0        0        0    10659 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/fastapi/router.py
--rw-r--r--   0        0        0      137 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/federation/__init__.py
--rw-r--r--   0        0        0     3354 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/federation/field.py
--rw-r--r--   0        0        0     1205 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/federation/object_type.py
--rw-r--r--   0        0        0     4376 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/federation/schema.py
--rw-r--r--   0        0        0      641 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/federation/schema_directives.py
--rw-r--r--   0        0        0    13545 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/field.py
--rw-r--r--   0        0        0       51 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/file_uploads/__init__.py
--rw-r--r--   0        0        0      132 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/file_uploads/scalars.py
--rw-r--r--   0        0        0     1047 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/file_uploads/utils.py
--rw-r--r--   0        0        0        0 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/flask/__init__.py
--rw-r--r--   0        0        0      359 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/flask/graphiql.py
--rw-r--r--   0        0        0     2286 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/flask/views.py
--rw-r--r--   0        0        0     1201 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/http.py
--rw-r--r--   0        0        0     1051 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/lazy_type.py
--rw-r--r--   0        0        0      256 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/mutation.py
--rw-r--r--   0        0        0     8674 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/object_type.py
--rw-r--r--   0        0        0      434 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/permission.py
--rw-r--r--   0        0        0     5220 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/printer.py
--rw-r--r--   0        0        0      622 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/private.py
--rw-r--r--   0        0        0        0 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/py.typed
--rw-r--r--   0        0        0      209 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/resolvers.py
--rw-r--r--   0        0        0        0 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/sanic/__init__.py
--rw-r--r--   0        0        0      211 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/sanic/context.py
--rw-r--r--   0        0        0      366 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/sanic/graphiql.py
--rw-r--r--   0        0        0      782 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/sanic/utils.py
--rw-r--r--   0        0        0     3482 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/sanic/views.py
--rw-r--r--   0        0        0     1976 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/scalars.py
--rw-r--r--   0        0        0      117 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema/__init__.py
--rw-r--r--   0        0        0     2317 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema/base.py
--rw-r--r--   0        0        0     1995 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema/compat.py
--rw-r--r--   0        0        0      463 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema/config.py
--rw-r--r--   0        0        0     7599 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema/execute.py
--rw-r--r--   0        0        0     5564 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema/name_converter.py
--rw-r--r--   0        0        0     7451 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema/schema.py
--rw-r--r--   0        0        0    18054 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema/schema_converter.py
--rw-r--r--   0        0        0       85 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema/types/__init__.py
--rw-r--r--   0        0        0     1824 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema/types/base_scalars.py
--rw-r--r--   0        0        0      624 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema/types/concrete_type.py
--rw-r--r--   0        0        0     1921 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema/types/scalar.py
--rw-r--r--   0        0        0     1597 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/schema_directive.py
--rw-r--r--   0        0        0     3738 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/static/graphiql.html
--rw-r--r--   0        0        0       90 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/subscriptions/__init__.py
--rw-r--r--   0        0        0        0 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/subscriptions/protocols/__init__.py
--rw-r--r--   0        0        0        0 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/subscriptions/protocols/graphql_transport_ws/__init__.py
--rw-r--r--   0        0        0     8242 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/subscriptions/protocols/graphql_transport_ws/handlers.py
--rw-r--r--   0        0        0     2104 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/subscriptions/protocols/graphql_transport_ws/types.py
--rw-r--r--   0        0        0      305 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/subscriptions/protocols/graphql_ws/__init__.py
--rw-r--r--   0        0        0     6934 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/subscriptions/protocols/graphql_ws/handlers.py
--rw-r--r--   0        0        0      822 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/subscriptions/protocols/graphql_ws/types.py
--rw-r--r--   0        0        0      116 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/test/__init__.py
--rw-r--r--   0        0        0     5152 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/test/client.py
--rw-r--r--   0        0        0      128 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/tools/__init__.py
--rw-r--r--   0        0        0     1272 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/tools/create_type.py
--rw-r--r--   0        0        0      921 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/tools/merge_types.py
--rw-r--r--   0        0        0     4073 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/type.py
--rw-r--r--   0        0        0      140 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/types/__init__.py
--rw-r--r--   0        0        0     3181 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/types/execution.py
--rw-r--r--   0        0        0        0 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/types/fields/__init__.py
--rw-r--r--   0        0        0     6045 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/types/fields/resolver.py
--rw-r--r--   0        0        0     2368 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/types/info.py
--rw-r--r--   0        0        0     4686 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/types/nodes.py
--rw-r--r--   0        0        0     6053 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/types/type_resolver.py
--rw-r--r--   0        0        0     5830 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/types/types.py
--rw-r--r--   0        0        0     7581 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/union.py
--rw-r--r--   0        0        0      101 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/unset.py
--rw-r--r--   0        0        0        0 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/utils/__init__.py
--rw-r--r--   0        0        0      252 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/utils/await_maybe.py
--rw-r--r--   0        0        0     1042 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/utils/debug.py
--rw-r--r--   0        0        0     1085 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/utils/graphql_lexer.py
--rw-r--r--   0        0        0      592 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/utils/importer.py
--rw-r--r--   0        0        0      399 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/utils/inspect.py
--rw-r--r--   0        0        0     1025 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/utils/logging.py
--rw-r--r--   0        0        0      476 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/utils/str_converters.py
--rw-r--r--   0        0        0     3434 2022-03-04 15:52:37.943866 strawberry-graphql-0.99.2/strawberry/utils/typing.py
--rw-r--r--   0        0        0     6616 2022-03-04 15:52:54.541532 strawberry-graphql-0.99.2/setup.py
--rw-r--r--   0        0        0     6408 2022-03-04 15:52:54.542021 strawberry-graphql-0.99.2/PKG-INFO
+-rw-r--r--   0        0        0     1072 2021-08-09 16:29:08.230514 strawberry-graphql-0.99.3/LICENSE
+-rw-r--r--   0        0        0     3976 2021-11-12 18:54:44.760239 strawberry-graphql-0.99.3/README.md
+-rw-r--r--   0        0        0     4361 2022-03-05 02:16:59.355481 strawberry-graphql-0.99.3/pyproject.toml
+-rw-r--r--   0        0        0      855 2021-10-24 14:47:02.837739 strawberry-graphql-0.99.3/strawberry/__init__.py
+-rw-r--r--   0        0        0       60 2022-01-14 20:10:45.020988 strawberry-graphql-0.99.3/strawberry/__main__.py
+-rw-r--r--   0        0        0        0 2021-09-15 08:24:18.339285 strawberry-graphql-0.99.3/strawberry/aiohttp/__init__.py
+-rw-r--r--   0        0        0      322 2021-10-23 19:55:46.569066 strawberry-graphql-0.99.3/strawberry/aiohttp/handlers/__init__.py
+-rw-r--r--   0        0        0     1950 2021-10-23 19:55:46.570392 strawberry-graphql-0.99.3/strawberry/aiohttp/handlers/graphql_transport_ws_handler.py
+-rw-r--r--   0        0        0     2126 2021-10-23 19:55:46.571590 strawberry-graphql-0.99.3/strawberry/aiohttp/handlers/graphql_ws_handler.py
+-rw-r--r--   0        0        0     4284 2022-02-21 17:52:55.285049 strawberry-graphql-0.99.3/strawberry/aiohttp/handlers/http_handler.py
+-rw-r--r--   0        0        0     3561 2022-03-02 22:41:49.278081 strawberry-graphql-0.99.3/strawberry/aiohttp/views.py
+-rw-r--r--   0        0        0     9155 2022-02-28 20:55:22.016683 strawberry-graphql-0.99.3/strawberry/annotation.py
+-rw-r--r--   0        0        0     6512 2022-02-28 20:55:22.018241 strawberry-graphql-0.99.3/strawberry/arguments.py
+-rw-r--r--   0        0        0     3993 2021-10-23 19:55:46.575990 strawberry-graphql-0.99.3/strawberry/asgi/__init__.py
+-rw-r--r--   0        0        0      313 2021-10-23 19:55:46.577236 strawberry-graphql-0.99.3/strawberry/asgi/handlers/__init__.py
+-rw-r--r--   0        0        0     2018 2021-10-23 19:55:46.578433 strawberry-graphql-0.99.3/strawberry/asgi/handlers/graphql_transport_ws_handler.py
+-rw-r--r--   0        0        0     2204 2021-10-23 19:55:46.579533 strawberry-graphql-0.99.3/strawberry/asgi/handlers/graphql_ws_handler.py
+-rw-r--r--   0        0        0     4952 2022-01-27 14:19:27.974597 strawberry-graphql-0.99.3/strawberry/asgi/handlers/http_handler.py
+-rw-r--r--   0        0        0       72 2022-01-14 20:10:45.022369 strawberry-graphql-0.99.3/strawberry/asgi/test/__init__.py
+-rw-r--r--   0        0        0     1321 2022-01-14 20:10:45.022569 strawberry-graphql-0.99.3/strawberry/asgi/test/client.py
+-rw-r--r--   0        0        0      257 2021-08-09 16:29:08.247167 strawberry-graphql-0.99.3/strawberry/asgi/utils.py
+-rw-r--r--   0        0        0       49 2021-10-23 19:55:46.582129 strawberry-graphql-0.99.3/strawberry/auto.py
+-rw-r--r--   0        0        0        0 2022-01-14 20:10:45.022647 strawberry-graphql-0.99.3/strawberry/chalice/__init__.py
+-rw-r--r--   0        0        0      690 2022-01-14 20:10:45.022798 strawberry-graphql-0.99.3/strawberry/chalice/graphiql.py
+-rw-r--r--   0        0        0     3838 2022-01-14 20:10:45.022947 strawberry-graphql-0.99.3/strawberry/chalice/views.py
+-rw-r--r--   0        0        0      257 2022-03-05 02:16:57.261232 strawberry-graphql-0.99.3/strawberry/cli/__init__.py
+-rw-r--r--   0        0        0        0 2022-03-05 02:16:57.261308 strawberry-graphql-0.99.3/strawberry/cli/commands/__init__.py
+-rw-r--r--   0        0        0     1043 2022-03-05 02:16:57.263958 strawberry-graphql-0.99.3/strawberry/cli/commands/export_schema.py
+-rw-r--r--   0        0        0     2131 2022-03-05 02:16:57.264755 strawberry-graphql-0.99.3/strawberry/cli/commands/server.py
+-rw-r--r--   0        0        0       67 2021-09-15 08:24:18.344410 strawberry-graphql-0.99.3/strawberry/cli/constants.py
+-rw-r--r--   0        0        0      816 2021-09-15 08:24:18.346044 strawberry-graphql-0.99.3/strawberry/cli/debug_server.py
+-rw-r--r--   0        0        0     3130 2022-03-05 02:16:57.265056 strawberry-graphql-0.99.3/strawberry/custom_scalar.py
+-rw-r--r--   0        0        0     3449 2022-01-25 23:12:58.538726 strawberry-graphql-0.99.3/strawberry/dataloader.py
+-rw-r--r--   0        0        0     1965 2022-02-21 17:52:55.286514 strawberry-graphql-0.99.3/strawberry/directive.py
+-rw-r--r--   0        0        0      769 2021-11-10 13:54:58.757852 strawberry-graphql-0.99.3/strawberry/django/__init__.py
+-rw-r--r--   0        0        0      135 2021-08-09 16:29:08.248994 strawberry-graphql-0.99.3/strawberry/django/apps.py
+-rw-r--r--   0        0        0      494 2021-08-23 11:28:32.873145 strawberry-graphql-0.99.3/strawberry/django/context.py
+-rw-r--r--   0        0        0       72 2022-01-14 20:10:45.024894 strawberry-graphql-0.99.3/strawberry/django/test/__init__.py
+-rw-r--r--   0        0        0      586 2022-01-14 20:10:45.025437 strawberry-graphql-0.99.3/strawberry/django/test/client.py
+-rw-r--r--   0        0        0     7755 2022-02-28 20:55:22.039538 strawberry-graphql-0.99.3/strawberry/django/views.py
+-rw-r--r--   0        0        0     2085 2022-01-25 23:12:58.539428 strawberry-graphql-0.99.3/strawberry/enum.py
+-rw-r--r--   0        0        0     6774 2022-02-21 17:52:55.287251 strawberry-graphql-0.99.3/strawberry/exceptions.py
+-rw-r--r--   0        0        0       94 2021-11-10 15:11:28.661760 strawberry-graphql-0.99.3/strawberry/experimental/__init__.py
+-rw-r--r--   0        0        0      242 2021-10-23 19:55:46.586473 strawberry-graphql-0.99.3/strawberry/experimental/pydantic/__init__.py
+-rw-r--r--   0        0        0     3954 2022-02-21 17:52:55.288292 strawberry-graphql-0.99.3/strawberry/experimental/pydantic/conversion.py
+-rw-r--r--   0        0        0      841 2022-01-25 23:13:01.410897 strawberry-graphql-0.99.3/strawberry/experimental/pydantic/conversion_types.py
+-rw-r--r--   0        0        0     3909 2022-02-28 20:55:22.041652 strawberry-graphql-0.99.3/strawberry/experimental/pydantic/error_type.py
+-rw-r--r--   0        0        0     1344 2022-01-25 23:12:58.540441 strawberry-graphql-0.99.3/strawberry/experimental/pydantic/exceptions.py
+-rw-r--r--   0        0        0     1964 2022-03-02 22:41:49.279370 strawberry-graphql-0.99.3/strawberry/experimental/pydantic/fields.py
+-rw-r--r--   0        0        0    10019 2022-03-02 22:41:49.280070 strawberry-graphql-0.99.3/strawberry/experimental/pydantic/object_type.py
+-rw-r--r--   0        0        0     4111 2022-02-28 20:55:22.045376 strawberry-graphql-0.99.3/strawberry/experimental/pydantic/utils.py
+-rw-r--r--   0        0        0     1249 2021-08-09 16:29:08.251626 strawberry-graphql-0.99.3/strawberry/ext/LICENSE
+-rw-r--r--   0        0        0    30970 2022-02-28 20:55:22.047363 strawberry-graphql-0.99.3/strawberry/ext/mypy_plugin.py
+-rw-r--r--   0        0        0      427 2021-10-23 19:55:46.589860 strawberry-graphql-0.99.3/strawberry/extensions/__init__.py
+-rw-r--r--   0        0        0     1243 2021-10-23 19:55:46.590088 strawberry-graphql-0.99.3/strawberry/extensions/add_validation_rules.py
+-rw-r--r--   0        0        0     1526 2022-01-14 20:10:45.032346 strawberry-graphql-0.99.3/strawberry/extensions/base_extension.py
+-rw-r--r--   0        0        0     2703 2022-01-14 20:10:45.032662 strawberry-graphql-0.99.3/strawberry/extensions/context.py
+-rw-r--r--   0        0        0     2325 2022-02-28 20:55:22.048881 strawberry-graphql-0.99.3/strawberry/extensions/directives.py
+-rw-r--r--   0        0        0      661 2021-10-23 19:55:46.590692 strawberry-graphql-0.99.3/strawberry/extensions/disable_validation.py
+-rw-r--r--   0        0        0     1148 2021-10-23 19:55:46.590991 strawberry-graphql-0.99.3/strawberry/extensions/parser_cache.py
+-rw-r--r--   0        0        0     7715 2022-02-28 20:55:22.051794 strawberry-graphql-0.99.3/strawberry/extensions/query_depth_limiter.py
+-rw-r--r--   0        0        0     2537 2022-02-28 20:55:22.053423 strawberry-graphql-0.99.3/strawberry/extensions/runner.py
+-rw-r--r--   0        0        0      165 2021-08-09 16:29:08.252667 strawberry-graphql-0.99.3/strawberry/extensions/tracing/__init__.py
+-rw-r--r--   0        0        0     5412 2021-09-20 20:16:20.099179 strawberry-graphql-0.99.3/strawberry/extensions/tracing/apollo.py
+-rw-r--r--   0        0        0     5191 2022-02-28 20:55:22.055456 strawberry-graphql-0.99.3/strawberry/extensions/tracing/opentelemetry.py
+-rw-r--r--   0        0        0      530 2021-11-16 14:59:39.887177 strawberry-graphql-0.99.3/strawberry/extensions/tracing/utils.py
+-rw-r--r--   0        0        0      845 2021-09-20 20:16:20.100045 strawberry-graphql-0.99.3/strawberry/extensions/utils.py
+-rw-r--r--   0        0        0     1297 2021-10-23 19:55:46.593675 strawberry-graphql-0.99.3/strawberry/extensions/validation_cache.py
+-rw-r--r--   0        0        0      110 2022-02-21 17:52:55.293032 strawberry-graphql-0.99.3/strawberry/fastapi/__init__.py
+-rw-r--r--   0        0        0      242 2021-10-23 19:55:46.594468 strawberry-graphql-0.99.3/strawberry/fastapi/handlers/__init__.py
+-rw-r--r--   0        0        0      364 2021-10-23 19:55:46.594820 strawberry-graphql-0.99.3/strawberry/fastapi/handlers/graphql_transport_ws_handler.py
+-rw-r--r--   0        0        0      319 2021-10-23 19:55:46.595090 strawberry-graphql-0.99.3/strawberry/fastapi/handlers/graphql_ws_handler.py
+-rw-r--r--   0        0        0    10659 2022-02-21 17:52:55.293843 strawberry-graphql-0.99.3/strawberry/fastapi/router.py
+-rw-r--r--   0        0        0      137 2021-10-24 14:47:02.842583 strawberry-graphql-0.99.3/strawberry/federation/__init__.py
+-rw-r--r--   0        0        0     3354 2021-10-24 14:47:02.843227 strawberry-graphql-0.99.3/strawberry/federation/field.py
+-rw-r--r--   0        0        0     1205 2022-02-28 20:55:22.057076 strawberry-graphql-0.99.3/strawberry/federation/object_type.py
+-rw-r--r--   0        0        0     4376 2022-02-28 20:55:22.059558 strawberry-graphql-0.99.3/strawberry/federation/schema.py
+-rw-r--r--   0        0        0      641 2021-11-26 10:49:17.340012 strawberry-graphql-0.99.3/strawberry/federation/schema_directives.py
+-rw-r--r--   0        0        0    13545 2022-02-28 20:55:22.060584 strawberry-graphql-0.99.3/strawberry/field.py
+-rw-r--r--   0        0        0       51 2021-08-09 16:29:08.254048 strawberry-graphql-0.99.3/strawberry/file_uploads/__init__.py
+-rw-r--r--   0        0        0      132 2021-08-09 16:29:08.254227 strawberry-graphql-0.99.3/strawberry/file_uploads/scalars.py
+-rw-r--r--   0        0        0     1047 2021-09-15 08:24:18.356449 strawberry-graphql-0.99.3/strawberry/file_uploads/utils.py
+-rw-r--r--   0        0        0        0 2021-08-09 16:29:08.254597 strawberry-graphql-0.99.3/strawberry/flask/__init__.py
+-rw-r--r--   0        0        0      359 2021-08-09 16:29:08.254782 strawberry-graphql-0.99.3/strawberry/flask/graphiql.py
+-rw-r--r--   0        0        0     2286 2021-09-15 08:24:18.356831 strawberry-graphql-0.99.3/strawberry/flask/views.py
+-rw-r--r--   0        0        0     1201 2022-02-28 20:55:22.061589 strawberry-graphql-0.99.3/strawberry/http.py
+-rw-r--r--   0        0        0     1051 2022-02-28 20:55:22.062661 strawberry-graphql-0.99.3/strawberry/lazy_type.py
+-rw-r--r--   0        0        0      256 2021-08-09 16:29:08.255710 strawberry-graphql-0.99.3/strawberry/mutation.py
+-rw-r--r--   0        0        0     8674 2022-01-14 20:10:45.035749 strawberry-graphql-0.99.3/strawberry/object_type.py
+-rw-r--r--   0        0        0      434 2021-09-15 08:24:18.359640 strawberry-graphql-0.99.3/strawberry/permission.py
+-rw-r--r--   0        0        0     5220 2022-03-05 02:16:59.355936 strawberry-graphql-0.99.3/strawberry/printer.py
+-rw-r--r--   0        0        0      622 2022-01-14 20:10:45.038144 strawberry-graphql-0.99.3/strawberry/private.py
+-rw-r--r--   0        0        0        0 2021-08-09 16:29:08.256524 strawberry-graphql-0.99.3/strawberry/py.typed
+-rw-r--r--   0        0        0      209 2021-08-23 11:28:32.886869 strawberry-graphql-0.99.3/strawberry/resolvers.py
+-rw-r--r--   0        0        0        0 2021-08-23 11:28:32.887032 strawberry-graphql-0.99.3/strawberry/sanic/__init__.py
+-rw-r--r--   0        0        0      211 2021-08-23 11:28:32.887470 strawberry-graphql-0.99.3/strawberry/sanic/context.py
+-rw-r--r--   0        0        0      366 2021-08-23 11:28:32.887736 strawberry-graphql-0.99.3/strawberry/sanic/graphiql.py
+-rw-r--r--   0        0        0      782 2021-09-15 08:24:18.360069 strawberry-graphql-0.99.3/strawberry/sanic/utils.py
+-rw-r--r--   0        0        0     3482 2022-01-25 23:12:58.547354 strawberry-graphql-0.99.3/strawberry/sanic/views.py
+-rw-r--r--   0        0        0     1976 2022-03-02 22:41:49.280736 strawberry-graphql-0.99.3/strawberry/scalars.py
+-rw-r--r--   0        0        0      117 2021-10-23 19:55:46.606067 strawberry-graphql-0.99.3/strawberry/schema/__init__.py
+-rw-r--r--   0        0        0     2317 2021-10-24 19:31:38.565039 strawberry-graphql-0.99.3/strawberry/schema/base.py
+-rw-r--r--   0        0        0     1995 2022-01-14 20:10:45.039963 strawberry-graphql-0.99.3/strawberry/schema/compat.py
+-rw-r--r--   0        0        0      463 2022-02-28 20:55:22.065890 strawberry-graphql-0.99.3/strawberry/schema/config.py
+-rw-r--r--   0        0        0     7599 2022-01-14 20:10:45.041732 strawberry-graphql-0.99.3/strawberry/schema/execute.py
+-rw-r--r--   0        0        0     5564 2022-02-21 17:52:55.297261 strawberry-graphql-0.99.3/strawberry/schema/name_converter.py
+-rw-r--r--   0        0        0     7451 2022-03-05 02:16:57.266194 strawberry-graphql-0.99.3/strawberry/schema/schema.py
+-rw-r--r--   0        0        0    18054 2022-02-28 20:55:22.071397 strawberry-graphql-0.99.3/strawberry/schema/schema_converter.py
+-rw-r--r--   0        0        0       85 2021-08-09 16:29:08.259443 strawberry-graphql-0.99.3/strawberry/schema/types/__init__.py
+-rw-r--r--   0        0        0     1824 2022-02-28 20:55:22.072793 strawberry-graphql-0.99.3/strawberry/schema/types/base_scalars.py
+-rw-r--r--   0        0        0      624 2021-10-24 19:31:38.569090 strawberry-graphql-0.99.3/strawberry/schema/types/concrete_type.py
+-rw-r--r--   0        0        0     1921 2022-03-05 02:16:57.266448 strawberry-graphql-0.99.3/strawberry/schema/types/scalar.py
+-rw-r--r--   0        0        0     1597 2022-01-14 20:10:45.045570 strawberry-graphql-0.99.3/strawberry/schema_directive.py
+-rw-r--r--   0        0        0     3738 2021-09-21 15:50:03.722756 strawberry-graphql-0.99.3/strawberry/static/graphiql.html
+-rw-r--r--   0        0        0       90 2021-10-23 19:55:46.607919 strawberry-graphql-0.99.3/strawberry/subscriptions/__init__.py
+-rw-r--r--   0        0        0        0 2021-10-23 19:55:46.608124 strawberry-graphql-0.99.3/strawberry/subscriptions/protocols/__init__.py
+-rw-r--r--   0        0        0        0 2021-10-23 19:55:46.608339 strawberry-graphql-0.99.3/strawberry/subscriptions/protocols/graphql_transport_ws/__init__.py
+-rw-r--r--   0        0        0     8242 2022-02-28 20:55:22.076015 strawberry-graphql-0.99.3/strawberry/subscriptions/protocols/graphql_transport_ws/handlers.py
+-rw-r--r--   0        0        0     2104 2022-02-28 20:55:22.077760 strawberry-graphql-0.99.3/strawberry/subscriptions/protocols/graphql_transport_ws/types.py
+-rw-r--r--   0        0        0      305 2021-10-23 19:55:46.782880 strawberry-graphql-0.99.3/strawberry/subscriptions/protocols/graphql_ws/__init__.py
+-rw-r--r--   0        0        0     6934 2022-02-28 20:55:22.079887 strawberry-graphql-0.99.3/strawberry/subscriptions/protocols/graphql_ws/handlers.py
+-rw-r--r--   0        0        0      822 2022-02-28 20:55:22.081890 strawberry-graphql-0.99.3/strawberry/subscriptions/protocols/graphql_ws/types.py
+-rw-r--r--   0        0        0      116 2022-01-14 20:10:45.045730 strawberry-graphql-0.99.3/strawberry/test/__init__.py
+-rw-r--r--   0        0        0     5152 2022-01-14 20:10:45.045848 strawberry-graphql-0.99.3/strawberry/test/client.py
+-rw-r--r--   0        0        0      128 2021-10-23 19:55:46.614687 strawberry-graphql-0.99.3/strawberry/tools/__init__.py
+-rw-r--r--   0        0        0     1272 2021-09-15 08:24:18.364680 strawberry-graphql-0.99.3/strawberry/tools/create_type.py
+-rw-r--r--   0        0        0      921 2021-10-23 19:55:46.616044 strawberry-graphql-0.99.3/strawberry/tools/merge_types.py
+-rw-r--r--   0        0        0     4073 2022-02-28 20:55:22.083212 strawberry-graphql-0.99.3/strawberry/type.py
+-rw-r--r--   0        0        0      140 2021-08-23 11:28:32.899179 strawberry-graphql-0.99.3/strawberry/types/__init__.py
+-rw-r--r--   0        0        0     3181 2022-01-14 20:10:45.046243 strawberry-graphql-0.99.3/strawberry/types/execution.py
+-rw-r--r--   0        0        0        0 2021-08-09 16:29:08.262403 strawberry-graphql-0.99.3/strawberry/types/fields/__init__.py
+-rw-r--r--   0        0        0     6045 2022-01-25 23:12:58.549389 strawberry-graphql-0.99.3/strawberry/types/fields/resolver.py
+-rw-r--r--   0        0        0     2368 2022-02-28 20:55:22.085256 strawberry-graphql-0.99.3/strawberry/types/info.py
+-rw-r--r--   0        0        0     4686 2022-02-28 20:55:22.087742 strawberry-graphql-0.99.3/strawberry/types/nodes.py
+-rw-r--r--   0        0        0     6053 2022-01-14 20:10:45.047924 strawberry-graphql-0.99.3/strawberry/types/type_resolver.py
+-rw-r--r--   0        0        0     5830 2022-01-14 20:10:45.048690 strawberry-graphql-0.99.3/strawberry/types/types.py
+-rw-r--r--   0        0        0     7581 2022-02-28 20:55:22.089190 strawberry-graphql-0.99.3/strawberry/union.py
+-rw-r--r--   0        0        0      101 2022-01-14 20:10:45.049574 strawberry-graphql-0.99.3/strawberry/unset.py
+-rw-r--r--   0        0        0        0 2021-08-09 16:29:08.263932 strawberry-graphql-0.99.3/strawberry/utils/__init__.py
+-rw-r--r--   0        0        0      252 2022-01-14 20:10:45.049870 strawberry-graphql-0.99.3/strawberry/utils/await_maybe.py
+-rw-r--r--   0        0        0     1042 2021-09-15 08:24:18.369975 strawberry-graphql-0.99.3/strawberry/utils/debug.py
+-rw-r--r--   0        0        0     1085 2021-08-09 16:29:08.264395 strawberry-graphql-0.99.3/strawberry/utils/graphql_lexer.py
+-rw-r--r--   0        0        0      592 2021-09-15 08:24:18.370139 strawberry-graphql-0.99.3/strawberry/utils/importer.py
+-rw-r--r--   0        0        0      399 2021-08-09 16:29:08.264981 strawberry-graphql-0.99.3/strawberry/utils/inspect.py
+-rw-r--r--   0        0        0     1025 2021-10-23 19:55:46.620451 strawberry-graphql-0.99.3/strawberry/utils/logging.py
+-rw-r--r--   0        0        0      476 2021-08-09 16:29:08.265398 strawberry-graphql-0.99.3/strawberry/utils/str_converters.py
+-rw-r--r--   0        0        0     3434 2022-02-28 20:55:22.091924 strawberry-graphql-0.99.3/strawberry/utils/typing.py
+-rw-r--r--   0        0        0     6517 2022-03-05 02:28:00.561628 strawberry-graphql-0.99.3/setup.py
+-rw-r--r--   0        0        0     6293 2022-03-05 02:28:00.562019 strawberry-graphql-0.99.3/PKG-INFO
```

### Comparing `strawberry-graphql-0.99.2/LICENSE` & `strawberry-graphql-0.99.3/LICENSE`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/README.md` & `strawberry-graphql-0.99.3/README.md`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/pyproject.toml` & `strawberry-graphql-0.99.3/pyproject.toml`

 * *Files 5% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 [tool.poetry]
 name = "strawberry-graphql"
 packages = [ { include = "strawberry" } ]
-version = "0.99.2"
+version = "0.99.3"
 description = "A library for creating GraphQL APIs"
 authors = ["Patrick Arminio <patrick.arminio@gmail.com>"]
 license = "MIT"
 readme = "README.md"
 keywords = ["grapqhl", "api", "rest", "starlette", "async"]
 
 homepage = "https://strawberry.rocks/"
@@ -27,21 +27,18 @@
 
 [tool.poetry.dependencies]
 python = "^3.7"
 starlette = {version = ">=0.13.6,<0.17.0", optional = true}
 click = {version = ">=7.0,<9.0", optional = true}
 pygments = "^2.3"
 uvicorn = {version = ">=0.11.6,<0.18.0", optional = true}
-Django = [
-    {version = ">=2.2,<4", markers = "python_version < '3.8' and extra == 'django'", optional = true},
-    {version = ">=2.2,<5", markers = "python_version >= '3.8' and extra == 'django'", optional = true}
-]
+Django = {version = ">=2.2", optional = true}
 graphql-core = "~3.2.0"
 asgiref = {version = "^3.2", optional = true}
-flask = {version = "^1.1", optional = true}
+flask = {version = ">=1.1", optional = true}
 typing_extensions = ">=3.7.4,<5.0.0"
 opentelemetry-api = {version = "<2", optional = true}
 opentelemetry-sdk = {version = "<2", optional = true}
 chalice = {version = "^1.22", optional = true}
 python-dateutil = "^2.7.0"
 pydantic = {version = "<2", optional = true}
 python-multipart = "^0.0.5"
@@ -63,28 +60,25 @@
 flake8-bugbear = "^22.1.11"
 flake8-eradicate = "^1.2.0"
 pytest-mypy-plugins = "^1.9"
 pytest-mock = "^3.7"
 pytest-django = {version = "^4.5"}
 asgiref = "^3.2"
 pytest-flask = {version = "^1.2.0"}
-flask = {version = "^1.1"}
+flask = ">=1.1"
 chalice = {version = "^1.22"}
 requests = "^2.27.1"
 pre-commit = "^2.16.0"
 pytest-benchmark = "^3.4.1"
 freezegun = "^1.1.0"
 opentelemetry-api = "<2"
 opentelemetry-sdk = "<2"
 flake8-isort = "^4.1.1"
 flake8-black = "^0.2.5"
-Django = [
-    {version = ">=2.2,<4", python = "<3.8", optional = false},
-    {version = ">=2.2,<5", python = ">=3.8", optional = false}
-]
+Django = ">=2.2"
 pydantic = {version = "<2", optional = false}
 email-validator = {version = "^1.1.3", optional = false}
 starlette = ">=0.13.6,<0.17.0"
 uvicorn = ">=0.11.6,<0.18.0"
 sanic = ">=20.12.2,<22.0.0"
 aiohttp = "^3.7.4.post0"
 pytest-aiohttp = "^1.0.3"
```

### Comparing `strawberry-graphql-0.99.2/strawberry/__init__.py` & `strawberry-graphql-0.99.3/strawberry/__init__.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/aiohttp/handlers/graphql_transport_ws_handler.py` & `strawberry-graphql-0.99.3/strawberry/aiohttp/handlers/graphql_transport_ws_handler.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/aiohttp/handlers/graphql_ws_handler.py` & `strawberry-graphql-0.99.3/strawberry/aiohttp/handlers/graphql_ws_handler.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/aiohttp/handlers/http_handler.py` & `strawberry-graphql-0.99.3/strawberry/aiohttp/handlers/http_handler.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/aiohttp/views.py` & `strawberry-graphql-0.99.3/strawberry/aiohttp/views.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/annotation.py` & `strawberry-graphql-0.99.3/strawberry/annotation.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/arguments.py` & `strawberry-graphql-0.99.3/strawberry/arguments.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/asgi/__init__.py` & `strawberry-graphql-0.99.3/strawberry/asgi/__init__.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/asgi/handlers/graphql_transport_ws_handler.py` & `strawberry-graphql-0.99.3/strawberry/asgi/handlers/graphql_transport_ws_handler.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/asgi/handlers/graphql_ws_handler.py` & `strawberry-graphql-0.99.3/strawberry/asgi/handlers/graphql_ws_handler.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/asgi/handlers/http_handler.py` & `strawberry-graphql-0.99.3/strawberry/asgi/handlers/http_handler.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/asgi/test/client.py` & `strawberry-graphql-0.99.3/strawberry/asgi/test/client.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/chalice/graphiql.py` & `strawberry-graphql-0.99.3/strawberry/chalice/graphiql.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/chalice/views.py` & `strawberry-graphql-0.99.3/strawberry/chalice/views.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/cli/commands/export_schema.py` & `strawberry-graphql-0.99.3/strawberry/cli/commands/export_schema.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/cli/commands/server.py` & `strawberry-graphql-0.99.3/strawberry/cli/commands/server.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/cli/debug_server.py` & `strawberry-graphql-0.99.3/strawberry/cli/debug_server.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/custom_scalar.py` & `strawberry-graphql-0.99.3/strawberry/custom_scalar.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/dataloader.py` & `strawberry-graphql-0.99.3/strawberry/dataloader.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/directive.py` & `strawberry-graphql-0.99.3/strawberry/directive.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/django/__init__.py` & `strawberry-graphql-0.99.3/strawberry/django/__init__.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/django/test/client.py` & `strawberry-graphql-0.99.3/strawberry/django/test/client.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/django/views.py` & `strawberry-graphql-0.99.3/strawberry/django/views.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/enum.py` & `strawberry-graphql-0.99.3/strawberry/enum.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/exceptions.py` & `strawberry-graphql-0.99.3/strawberry/exceptions.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/experimental/pydantic/conversion.py` & `strawberry-graphql-0.99.3/strawberry/experimental/pydantic/conversion.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/experimental/pydantic/conversion_types.py` & `strawberry-graphql-0.99.3/strawberry/experimental/pydantic/conversion_types.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/experimental/pydantic/error_type.py` & `strawberry-graphql-0.99.3/strawberry/experimental/pydantic/error_type.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/experimental/pydantic/exceptions.py` & `strawberry-graphql-0.99.3/strawberry/experimental/pydantic/exceptions.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/experimental/pydantic/fields.py` & `strawberry-graphql-0.99.3/strawberry/experimental/pydantic/fields.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/experimental/pydantic/object_type.py` & `strawberry-graphql-0.99.3/strawberry/experimental/pydantic/object_type.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/experimental/pydantic/utils.py` & `strawberry-graphql-0.99.3/strawberry/experimental/pydantic/utils.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/ext/LICENSE` & `strawberry-graphql-0.99.3/strawberry/ext/LICENSE`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/ext/mypy_plugin.py` & `strawberry-graphql-0.99.3/strawberry/ext/mypy_plugin.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/add_validation_rules.py` & `strawberry-graphql-0.99.3/strawberry/extensions/add_validation_rules.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/base_extension.py` & `strawberry-graphql-0.99.3/strawberry/extensions/base_extension.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/context.py` & `strawberry-graphql-0.99.3/strawberry/extensions/context.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/directives.py` & `strawberry-graphql-0.99.3/strawberry/extensions/directives.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/disable_validation.py` & `strawberry-graphql-0.99.3/strawberry/extensions/disable_validation.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/parser_cache.py` & `strawberry-graphql-0.99.3/strawberry/extensions/parser_cache.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/query_depth_limiter.py` & `strawberry-graphql-0.99.3/strawberry/extensions/query_depth_limiter.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/runner.py` & `strawberry-graphql-0.99.3/strawberry/extensions/runner.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/tracing/apollo.py` & `strawberry-graphql-0.99.3/strawberry/extensions/tracing/apollo.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/tracing/opentelemetry.py` & `strawberry-graphql-0.99.3/strawberry/extensions/tracing/opentelemetry.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/tracing/utils.py` & `strawberry-graphql-0.99.3/strawberry/extensions/tracing/utils.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/utils.py` & `strawberry-graphql-0.99.3/strawberry/extensions/utils.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/extensions/validation_cache.py` & `strawberry-graphql-0.99.3/strawberry/extensions/validation_cache.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/fastapi/router.py` & `strawberry-graphql-0.99.3/strawberry/fastapi/router.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/federation/field.py` & `strawberry-graphql-0.99.3/strawberry/federation/field.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/federation/object_type.py` & `strawberry-graphql-0.99.3/strawberry/federation/object_type.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/federation/schema.py` & `strawberry-graphql-0.99.3/strawberry/federation/schema.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/federation/schema_directives.py` & `strawberry-graphql-0.99.3/strawberry/federation/schema_directives.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/field.py` & `strawberry-graphql-0.99.3/strawberry/field.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/file_uploads/utils.py` & `strawberry-graphql-0.99.3/strawberry/file_uploads/utils.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/flask/views.py` & `strawberry-graphql-0.99.3/strawberry/flask/views.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/http.py` & `strawberry-graphql-0.99.3/strawberry/http.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/lazy_type.py` & `strawberry-graphql-0.99.3/strawberry/lazy_type.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/object_type.py` & `strawberry-graphql-0.99.3/strawberry/object_type.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/printer.py` & `strawberry-graphql-0.99.3/strawberry/printer.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/private.py` & `strawberry-graphql-0.99.3/strawberry/private.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/sanic/utils.py` & `strawberry-graphql-0.99.3/strawberry/sanic/utils.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/sanic/views.py` & `strawberry-graphql-0.99.3/strawberry/sanic/views.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/scalars.py` & `strawberry-graphql-0.99.3/strawberry/scalars.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/schema/base.py` & `strawberry-graphql-0.99.3/strawberry/schema/base.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/schema/compat.py` & `strawberry-graphql-0.99.3/strawberry/schema/compat.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/schema/execute.py` & `strawberry-graphql-0.99.3/strawberry/schema/execute.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/schema/name_converter.py` & `strawberry-graphql-0.99.3/strawberry/schema/name_converter.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/schema/schema.py` & `strawberry-graphql-0.99.3/strawberry/schema/schema.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/schema/schema_converter.py` & `strawberry-graphql-0.99.3/strawberry/schema/schema_converter.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/schema/types/base_scalars.py` & `strawberry-graphql-0.99.3/strawberry/schema/types/base_scalars.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/schema/types/concrete_type.py` & `strawberry-graphql-0.99.3/strawberry/schema/types/concrete_type.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/schema/types/scalar.py` & `strawberry-graphql-0.99.3/strawberry/schema/types/scalar.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/schema_directive.py` & `strawberry-graphql-0.99.3/strawberry/schema_directive.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/static/graphiql.html` & `strawberry-graphql-0.99.3/strawberry/static/graphiql.html`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/subscriptions/protocols/graphql_transport_ws/handlers.py` & `strawberry-graphql-0.99.3/strawberry/subscriptions/protocols/graphql_transport_ws/handlers.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/subscriptions/protocols/graphql_transport_ws/types.py` & `strawberry-graphql-0.99.3/strawberry/subscriptions/protocols/graphql_transport_ws/types.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/subscriptions/protocols/graphql_ws/handlers.py` & `strawberry-graphql-0.99.3/strawberry/subscriptions/protocols/graphql_ws/handlers.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/subscriptions/protocols/graphql_ws/types.py` & `strawberry-graphql-0.99.3/strawberry/subscriptions/protocols/graphql_ws/types.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/test/client.py` & `strawberry-graphql-0.99.3/strawberry/test/client.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/tools/create_type.py` & `strawberry-graphql-0.99.3/strawberry/tools/create_type.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/tools/merge_types.py` & `strawberry-graphql-0.99.3/strawberry/tools/merge_types.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/type.py` & `strawberry-graphql-0.99.3/strawberry/type.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/types/execution.py` & `strawberry-graphql-0.99.3/strawberry/types/execution.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/types/fields/resolver.py` & `strawberry-graphql-0.99.3/strawberry/types/fields/resolver.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/types/info.py` & `strawberry-graphql-0.99.3/strawberry/types/info.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/types/nodes.py` & `strawberry-graphql-0.99.3/strawberry/types/nodes.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/types/type_resolver.py` & `strawberry-graphql-0.99.3/strawberry/types/type_resolver.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/types/types.py` & `strawberry-graphql-0.99.3/strawberry/types/types.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/union.py` & `strawberry-graphql-0.99.3/strawberry/union.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/utils/debug.py` & `strawberry-graphql-0.99.3/strawberry/utils/debug.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/utils/graphql_lexer.py` & `strawberry-graphql-0.99.3/strawberry/utils/graphql_lexer.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/utils/importer.py` & `strawberry-graphql-0.99.3/strawberry/utils/importer.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/utils/logging.py` & `strawberry-graphql-0.99.3/strawberry/utils/logging.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/strawberry/utils/typing.py` & `strawberry-graphql-0.99.3/strawberry/utils/typing.py`

 * *Files identical despite different names*

### Comparing `strawberry-graphql-0.99.2/setup.py` & `strawberry-graphql-0.99.3/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -49,29 +49,27 @@
  'typing_extensions>=3.7.4,<5.0.0']
 
 extras_require = \
 {'aiohttp': ['aiohttp>=3.7.4.post0,<4.0.0'],
  'asgi': ['starlette>=0.13.6,<0.17.0'],
  'chalice': ['chalice>=1.22,<2.0'],
  'debug-server': ['starlette>=0.13.6,<0.17.0', 'uvicorn>=0.11.6,<0.18.0'],
- 'django': ['asgiref>=3.2,<4.0'],
- 'django:python_version < "3.8"': ['Django>=2.2,<4'],
- 'django:python_version >= "3.8"': ['Django>=2.2,<5'],
+ 'django': ['Django>=2.2', 'asgiref>=3.2,<4.0'],
  'fastapi': ['fastapi>=0.65.2'],
- 'flask': ['flask>=1.1,<2.0'],
+ 'flask': ['flask>=1.1'],
  'opentelemetry': ['opentelemetry-api<2', 'opentelemetry-sdk<2'],
  'pydantic': ['pydantic<2'],
  'sanic': ['sanic>=20.12.2,<22.0.0']}
 
 entry_points = \
 {'console_scripts': ['strawberry = strawberry.cli:run']}
 
 setup_kwargs = {
     'name': 'strawberry-graphql',
-    'version': '0.99.2',
+    'version': '0.99.3',
     'description': 'A library for creating GraphQL APIs',
     'long_description': '<img src="https://github.com/strawberry-graphql/strawberry/raw/main/.github/logo.png" width="124" height="150">\n\n# Strawberry GraphQL\n\n> Python GraphQL library based on dataclasses\n\n[![CircleCI](https://img.shields.io/circleci/token/307b40d5e152e074d34f84d30d226376a15667d5/project/github/strawberry-graphql/strawberry/main.svg?style=for-the-badge)](https://circleci.com/gh/strawberry-graphql/strawberry/tree/main)\n[![Discord](https://img.shields.io/discord/689806334337482765?label=discord&logo=discord&logoColor=white&style=for-the-badge&color=blue)](https://discord.gg/ZkRTEJQ)\n[![PyPI](https://img.shields.io/pypi/v/strawberry-graphql?logo=pypi&logoColor=white&style=for-the-badge)](https://pypi.org/project/strawberry-graphql/)\n\n## Installation ( Quick Start )\n\nThe quick start method provides a server and CLI to get going quickly. Install\nwith:\n\n```shell\npip install \'strawberry-graphql[debug-server]\'\n```\n\n## Getting Started\n\nCreate a file called `app.py` with the following code:\n\n```python\nimport strawberry\n\n\n@strawberry.type\nclass User:\n    name: str\n    age: int\n\n\n@strawberry.type\nclass Query:\n    @strawberry.field\n    def user(self) -> User:\n        return User(name="Patrick", age=100)\n\n\nschema = strawberry.Schema(query=Query)\n```\n\nThis will create a GraphQL schema defining a `User` type and a single query\nfield `user` that will return a hardcoded user.\n\nTo run the debug server run the following command:\n\n```shell\nstrawberry server app\n```\n\nOpen the debug server by clicking on the following link:\n[http://0.0.0.0:8000/graphql](http://0.0.0.0:8000/graphql)\n\nThis will open GraphiQL where you can test the API.\n\n### Type-checking\n\nStrawberry comes with a [mypy] plugin that enables statically type-checking your\nGraphQL schema. To enable it, add the following lines to your `mypy.ini`\nconfiguration:\n\n```ini\n[mypy]\nplugins = strawberry.ext.mypy_plugin\n```\n\n[mypy]: http://www.mypy-lang.org/\n\n### Django Integration\n\nA Django view is provided for adding a GraphQL endpoint to your application.\n\n1. Add the app to your `INSTALLED_APPS`.\n\n```python\nINSTALLED_APPS = [\n    ...\n    \'strawberry.django\',\n]\n```\n\n2. Add the view to your `urls.py` file.\n\n```python\nfrom strawberry.django.views import GraphQLView\nfrom .schema import schema\n\nurlpatterns = [\n    ...,\n    path(\'graphql\', GraphQLView.as_view(schema=schema)),\n]\n```\n\n## WebSockets\n\nTo support graphql Subscriptions over WebSockets you need to provide a WebSocket\nenabled server. The debug server can be made to support WebSockets with these\ncommands:\n\n```shell\npip install \'strawberry-graphql[debug-server]\'\npip install \'uvicorn[standard]\'\n```\n\n## Examples\n\n* [Various examples on how to use Strawberry](https://github.com/strawberry-graphql/examples)\n* [Full stack example using Starlette, SQLAlchemy, Typescript codegen and Next.js](https://github.com/jokull/python-ts-graphql-demo)\n* [Quart + Strawberry tutorial](https://github.com/rockyburt/Ketchup)\n\n## Contributing\n\nWe use [poetry](https://github.com/sdispater/poetry) to manage dependencies, to\nget started follow these steps:\n\n```shell\ngit clone https://github.com/strawberry-graphql/strawberry\ncd strawberry\npoetry install\npoetry run pytest\n```\n\nThis will install all the dependencies (including dev ones) and run the tests.\n\n### Pre commit\n\nWe have a configuration for\n[pre-commit](https://github.com/pre-commit/pre-commit), to add the hook run the\nfollowing command:\n\n```shell\npre-commit install\n```\n\n## Links\n\n- Project homepage: https://strawberry.rocks\n- Repository: https://github.com/strawberry-graphql/strawberry\n- Issue tracker: https://github.com/strawberry-graphql/strawberry/issues\n  - In case of sensitive bugs like security vulnerabilities, please contact\n    patrick.arminio@gmail.com directly instead of using the issue tracker. We\n    value your effort to improve the security and privacy of this project!\n\n## Licensing\n\nThe code in this project is licensed under MIT license. See [LICENSE](./LICENSE)\nfor more information.\n',
     'author': 'Patrick Arminio',
     'author_email': 'patrick.arminio@gmail.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://strawberry.rocks/',
```

### Comparing `strawberry-graphql-0.99.2/PKG-INFO` & `strawberry-graphql-0.99.3/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: strawberry-graphql
-Version: 0.99.2
+Version: 0.99.3
 Summary: A library for creating GraphQL APIs
 Home-page: https://strawberry.rocks/
 License: MIT
 Keywords: grapqhl,api,rest,starlette,async
 Author: Patrick Arminio
 Author-email: patrick.arminio@gmail.com
 Requires-Python: >=3.7,<4.0
@@ -24,23 +24,22 @@
 Provides-Extra: debug-server
 Provides-Extra: django
 Provides-Extra: fastapi
 Provides-Extra: flask
 Provides-Extra: opentelemetry
 Provides-Extra: pydantic
 Provides-Extra: sanic
-Requires-Dist: Django (>=2.2,<4); python_version < "3.8" and extra == "django"
-Requires-Dist: Django (>=2.2,<5); python_version >= "3.8" and extra == "django"
+Requires-Dist: Django (>=2.2); extra == "django"
 Requires-Dist: aiohttp (>=3.7.4.post0,<4.0.0); extra == "aiohttp"
 Requires-Dist: asgiref (>=3.2,<4.0); extra == "django"
 Requires-Dist: backports.cached-property (>=1.0.1,<2.0.0)
 Requires-Dist: chalice (>=1.22,<2.0); extra == "chalice"
 Requires-Dist: click (>=7.0,<9.0)
 Requires-Dist: fastapi (>=0.65.2); extra == "fastapi"
-Requires-Dist: flask (>=1.1,<2.0); extra == "flask"
+Requires-Dist: flask (>=1.1); extra == "flask"
 Requires-Dist: graphql-core (>=3.2.0,<3.3.0)
 Requires-Dist: opentelemetry-api (<2); extra == "opentelemetry"
 Requires-Dist: opentelemetry-sdk (<2); extra == "opentelemetry"
 Requires-Dist: pydantic (<2); extra == "pydantic"
 Requires-Dist: pygments (>=2.3,<3.0)
 Requires-Dist: python-dateutil (>=2.7.0,<3.0.0)
 Requires-Dist: python-multipart (>=0.0.5,<0.0.6)
```

