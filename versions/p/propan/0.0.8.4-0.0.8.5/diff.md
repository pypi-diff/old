# Comparing `tmp/propan-0.0.8.4.tar.gz` & `tmp/propan-0.0.8.5.tar.gz`

## Comparing `propan-0.0.8.4.tar` & `propan-0.0.8.5.tar`

### file list

```diff
@@ -1,67 +1,125 @@
--rw-r--r--   0        0        0     1833 2020-02-02 00:00:00.000000 propan-0.0.8.4/CONTRIBUTING.md
--rw-r--r--   0        0        0      375 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/1_basic_usage.py
--rw-r--r--   0        0        0      472 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/2_specific_exchange.py
--rw-r--r--   0        0        0      677 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/3_lifespan_events.py
--rw-r--r--   0        0        0      681 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/4_cli_attributes_promotion.py
--rw-r--r--   0        0        0      506 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/5_publishing.py
--rw-r--r--   0        0        0     1003 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/6_arguments_casting.py
--rw-r--r--   0        0        0      674 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/7_handler_errors_processing.py
--rw-r--r--   0        0        0     1003 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/dependencies/1_dependency_injection.py
--rw-r--r--   0        0        0      573 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/dependencies/2_dependency_declaration.py
--rw-r--r--   0        0        0      372 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/dependencies/3_dependency_aliases.py
--rw-r--r--   0        0        0      568 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/dependencies/4_dependency_deep_aliases.py
--rw-r--r--   0        0        0      569 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/dependencies/5_dependency_nesting.py
--rw-r--r--   0        0        0      779 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/dependencies/6_dependecy_calling.py
--rw-r--r--   0        0        0      660 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/http_frameworks_integrations/aiohttp.py
--rw-r--r--   0        0        0      586 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/http_frameworks_integrations/blacksheep.py
--rw-r--r--   0        0        0      953 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/http_frameworks_integrations/falcon.py
--rw-r--r--   0        0        0      535 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/http_frameworks_integrations/fastapi.py
--rw-r--r--   0        0        0      528 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/http_frameworks_integrations/quart.py
--rw-r--r--   0        0        0      608 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/http_frameworks_integrations/sanic.py
--rw-r--r--   0        0        0      732 2020-02-02 00:00:00.000000 propan-0.0.8.4/examples/http_frameworks_integrations/tornado.py
--rw-r--r--   0        0        0      103 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/__about__.py
--rw-r--r--   0        0        0      570 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/__init__.py
--rw-r--r--   0        0        0       65 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/__main__.py
--rw-r--r--   0        0        0     2556 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/app.py
--rw-r--r--   0        0        0      260 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/__init__.py
--rw-r--r--   0        0        0     2690 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/push_back_watcher.py
--rw-r--r--   0        0        0      157 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/model/__init__.py
--rw-r--r--   0        0        0     4672 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/model/broker_usecase.py
--rw-r--r--   0        0        0      480 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/model/schemas.py
--rw-r--r--   0        0        0       89 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/nats/__init__.py
--rw-r--r--   0        0        0     4775 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/nats/nats_broker.py
--rw-r--r--   0        0        0     4704 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/nats/nats_broker.pyi
--rw-r--r--   0        0        0     1569 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/nats/nats_js_broker.py
--rw-r--r--   0        0        0      484 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/nats/schemas.py
--rw-r--r--   0        0        0      241 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/rabbit/__init__.py
--rw-r--r--   0        0        0     8035 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/rabbit/rabbit_broker.py
--rw-r--r--   0        0        0     4820 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/rabbit/rabbit_broker.pyi
--rw-r--r--   0        0        0      995 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/brokers/rabbit/schemas.py
--rw-r--r--   0        0        0       58 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/cli/__init__.py
--rw-r--r--   0        0        0     3820 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/cli/main.py
--rw-r--r--   0        0        0     4855 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/cli/startproject.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/cli/supervisors/__init__.py
--rw-r--r--   0        0        0     1715 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/cli/supervisors/basereload.py
--rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/cli/supervisors/multiprocess.py
--rw-r--r--   0        0        0     4633 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/cli/supervisors/utils.py
--rw-r--r--   0        0        0     4306 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/cli/supervisors/watchgodreloader.py
--rw-r--r--   0        0        0      103 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/log/__init__.py
--rw-r--r--   0        0        0     2331 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/log/formatter.py
--rw-r--r--   0        0        0     1435 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/log/logging.py
--rw-r--r--   0        0        0      236 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/utils/__init__.py
--rw-r--r--   0        0        0      193 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/utils/classes.py
--rw-r--r--   0        0        0      513 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/utils/functions.py
--rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/utils/context/__init__.py
--rw-r--r--   0        0        0     2563 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/utils/context/decorate.py
--rw-r--r--   0        0        0      746 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/utils/context/main.py
--rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/utils/context/types.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/utils/types/__init__.py
--rw-r--r--   0        0        0     1632 2020-02-02 00:00:00.000000 propan-0.0.8.4/propan/utils/types/decorate.py
--rwxr-xr-x   0        0        0       37 2020-02-02 00:00:00.000000 propan-0.0.8.4/scripts/publish.sh
--rwxr-xr-x   0        0        0       87 2020-02-02 00:00:00.000000 propan-0.0.8.4/scripts/test-cov.sh
--rwxr-xr-x   0        0        0       33 2020-02-02 00:00:00.000000 propan-0.0.8.4/scripts/test.sh
--rw-r--r--   0        0        0      149 2020-02-02 00:00:00.000000 propan-0.0.8.4/.gitignore
--rw-r--r--   0        0        0     1082 2020-02-02 00:00:00.000000 propan-0.0.8.4/LICENSE
--rw-r--r--   0        0        0     6118 2020-02-02 00:00:00.000000 propan-0.0.8.4/README.md
--rw-r--r--   0        0        0     3198 2020-02-02 00:00:00.000000 propan-0.0.8.4/pyproject.toml
--rw-r--r--   0        0        0     8715 2020-02-02 00:00:00.000000 propan-0.0.8.4/PKG-INFO
+-rw-r--r--   0        0        0     1837 2020-02-02 00:00:00.000000 propan-0.0.8.5/CONTRIBUTING.md
+-rw-r--r--   0        0        0        1 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/.gitignore
+-rw-r--r--   0        0        0       43 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/CACHEDIR.TAG
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/1745c0ed96a6e8de
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/1c80fd155c02e10e
+-rw-r--r--   0        0        0      182 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/206ce96841a5d5b6
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/249a3ca9f30079c7
+-rw-r--r--   0        0        0      187 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/255fba90a78d204a
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/263c30c57a00456e
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/2fb105970a2ceb87
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/329eac57592693f2
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/32bec607656c0ee1
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/34b61303da2ec326
+-rw-r--r--   0        0        0      710 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/3d1b00fcedd04f64
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/3ede93ba5a3a0b3c
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/41dc7869dd6cec05
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/46d05f8e8e449a34
+-rw-r--r--   0        0        0      163 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/492ac35fe99e6520
+-rw-r--r--   0        0        0      370 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/4c283fbd9fa5bee2
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/50891aa183db466
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/53d8715be78ee9cc
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/5461f7bb7479b5c2
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/555d134976544154
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/5c068fa3955de17
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/60579efce6d45359
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/617a1eb2023a741a
+-rw-r--r--   0        0        0      173 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/657ef5dbbfee08d2
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/6b377f7f025e0c65
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/6b7c6eb91fcdc896
+-rw-r--r--   0        0        0      705 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/6e5d815d3706389a
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/7067f7ae0276ee9f
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/70c50531d865d030
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/785d5ad21cf24fb6
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/7e1a4b6a3fc6e11e
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/7f3fcafb0cbbb25b
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/820601d7c1667793
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/8290a72879a6e0cd
+-rw-r--r--   0        0        0      878 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/a2e400b6fcc87569
+-rw-r--r--   0        0        0      202 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/a78c3cc474c733f9
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/b48551ec8b0a3b1a
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/c1b1d26724a9a2ff
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/c4adca91a2e68c73
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/d546c2b89392b77
+-rw-r--r--   0        0        0      190 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/d713e40c856d7a4e
+-rw-r--r--   0        0        0      182 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/d9022e4690f44cd0
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/da1a88894ee16d7d
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/db79cceb3cb1c8aa
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/ddc2e43ef33619b7
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/df17f2b89693c7fd
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/df79d279f7915184
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/e23b06d2941484f4
+-rw-r--r--   0        0        0      176 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/e2531cda33cdf215
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/e5ba0b81d91aab83
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/e63a1d6b371ccdbc
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/eacde52132e82651
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/ec5558cbe3baacb3
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/ed7abe59bc5d140f
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/f6effe6c2bcbfede
+-rw-r--r--   0        0        0       16 2020-02-02 00:00:00.000000 propan-0.0.8.5/.ruff_cache/content/f6f761cdb860bf36
+-rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/1_basic_usage.py
+-rw-r--r--   0        0        0      479 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/2_specific_exchange.py
+-rw-r--r--   0        0        0      684 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/3_lifespan_events.py
+-rw-r--r--   0        0        0      681 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/4_cli_attributes_promotion.py
+-rw-r--r--   0        0        0      513 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/5_publishing.py
+-rw-r--r--   0        0        0     1010 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/6_arguments_casting.py
+-rw-r--r--   0        0        0      681 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/7_handler_errors_processing.py
+-rw-r--r--   0        0        0     1010 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/dependencies/1_dependency_injection.py
+-rw-r--r--   0        0        0      580 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/dependencies/2_dependency_declaration.py
+-rw-r--r--   0        0        0      379 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/dependencies/3_dependency_aliases.py
+-rw-r--r--   0        0        0      568 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/dependencies/4_dependency_deep_aliases.py
+-rw-r--r--   0        0        0      576 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/dependencies/5_dependency_nesting.py
+-rw-r--r--   0        0        0      786 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/dependencies/6_dependecy_calling.py
+-rw-r--r--   0        0        0      667 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/http_frameworks_integrations/aiohttp.py
+-rw-r--r--   0        0        0      593 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/http_frameworks_integrations/blacksheep.py
+-rw-r--r--   0        0        0      960 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/http_frameworks_integrations/falcon.py
+-rw-r--r--   0        0        0      542 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/http_frameworks_integrations/fastapi.py
+-rw-r--r--   0        0        0      535 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/http_frameworks_integrations/quart.py
+-rw-r--r--   0        0        0      615 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/http_frameworks_integrations/sanic.py
+-rw-r--r--   0        0        0      738 2020-02-02 00:00:00.000000 propan-0.0.8.5/examples/http_frameworks_integrations/tornado.py
+-rw-r--r--   0        0        0      103 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/__about__.py
+-rw-r--r--   0        0        0      387 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/__init__.py
+-rw-r--r--   0        0        0       65 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/__main__.py
+-rw-r--r--   0        0        0     2556 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/app.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/__init__.py
+-rw-r--r--   0        0        0     2690 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/push_back_watcher.py
+-rw-r--r--   0        0        0      157 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/model/__init__.py
+-rw-r--r--   0        0        0     4672 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/model/broker_usecase.py
+-rw-r--r--   0        0        0      480 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/model/schemas.py
+-rw-r--r--   0        0        0       89 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/nats/__init__.py
+-rw-r--r--   0        0        0     4775 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/nats/nats_broker.py
+-rw-r--r--   0        0        0     4704 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/nats/nats_broker.pyi
+-rw-r--r--   0        0        0     1569 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/nats/nats_js_broker.py
+-rw-r--r--   0        0        0      484 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/nats/schemas.py
+-rw-r--r--   0        0        0      241 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/rabbit/__init__.py
+-rw-r--r--   0        0        0     8021 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/rabbit/rabbit_broker.py
+-rw-r--r--   0        0        0     4820 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/rabbit/rabbit_broker.pyi
+-rw-r--r--   0        0        0      995 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/brokers/rabbit/schemas.py
+-rw-r--r--   0        0        0       58 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/cli/__init__.py
+-rw-r--r--   0        0        0     3820 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/cli/main.py
+-rw-r--r--   0        0        0     4876 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/cli/startproject.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/cli/supervisors/__init__.py
+-rw-r--r--   0        0        0     1715 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/cli/supervisors/basereload.py
+-rw-r--r--   0        0        0     1576 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/cli/supervisors/multiprocess.py
+-rw-r--r--   0        0        0     4633 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/cli/supervisors/utils.py
+-rw-r--r--   0        0        0     4306 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/cli/supervisors/watchgodreloader.py
+-rw-r--r--   0        0        0      103 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/log/__init__.py
+-rw-r--r--   0        0        0     2331 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/log/formatter.py
+-rw-r--r--   0        0        0     1435 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/log/logging.py
+-rw-r--r--   0        0        0      236 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/utils/__init__.py
+-rw-r--r--   0        0        0      193 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/utils/classes.py
+-rw-r--r--   0        0        0      513 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/utils/functions.py
+-rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/utils/context/__init__.py
+-rw-r--r--   0        0        0     2563 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/utils/context/decorate.py
+-rw-r--r--   0        0        0      746 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/utils/context/main.py
+-rw-r--r--   0        0        0      195 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/utils/context/types.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/utils/types/__init__.py
+-rw-r--r--   0        0        0     1632 2020-02-02 00:00:00.000000 propan-0.0.8.5/propan/utils/types/decorate.py
+-rwxr-xr-x   0        0        0       37 2020-02-02 00:00:00.000000 propan-0.0.8.5/scripts/publish.sh
+-rwxr-xr-x   0        0        0       87 2020-02-02 00:00:00.000000 propan-0.0.8.5/scripts/test-cov.sh
+-rwxr-xr-x   0        0        0       33 2020-02-02 00:00:00.000000 propan-0.0.8.5/scripts/test.sh
+-rw-r--r--   0        0        0      154 2020-02-02 00:00:00.000000 propan-0.0.8.5/.gitignore
+-rw-r--r--   0        0        0     1082 2020-02-02 00:00:00.000000 propan-0.0.8.5/LICENSE
+-rw-r--r--   0        0        0     6236 2020-02-02 00:00:00.000000 propan-0.0.8.5/README.md
+-rw-r--r--   0        0        0     3198 2020-02-02 00:00:00.000000 propan-0.0.8.5/pyproject.toml
+-rw-r--r--   0        0        0     8833 2020-02-02 00:00:00.000000 propan-0.0.8.5/PKG-INFO
```

### Comparing `propan-0.0.8.4/CONTRIBUTING.md` & `propan-0.0.8.5/CONTRIBUTING.md`

 * *Files 9% similar despite different names*

```diff
@@ -48,15 +48,15 @@
 $ python -m propan ...
 ```
 
 ### Tests
 
 To run tests with your current Propan application and Python environment use:
 ```bash
-$ coverage run -m pytest
+$ bash ./scripts/test-cov.sh
 ```
 
 To run all tests based on RabbitMQ, NATS or another dependencies you should run first following *docker-compose.yml*
 
 ```yaml
 version: "3"
```

### Comparing `propan-0.0.8.4/examples/3_lifespan_events.py` & `propan-0.0.8.5/examples/3_lifespan_events.py`

 * *Files 3% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 application lifecycle hooks
 
 All `on_startup` hooks runs after broker has been started
 All `on_shutdown` hooks runs after broker has been stopped
 '''
 
 from propan.app import PropanApp
-from propan.brokers import RabbitBroker
+from propan.brokers.rabbit import RabbitBroker
 
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 app = PropanApp(broker)
```

### Comparing `propan-0.0.8.4/examples/4_cli_attributes_promotion.py` & `propan-0.0.8.5/examples/4_cli_attributes_promotion.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/examples/6_arguments_casting.py` & `propan-0.0.8.5/examples/6_arguments_casting.py`

 * *Files 20% similar despite different names*

```diff
@@ -2,16 +2,16 @@
 Propan has @apply_types decorator to cast incoming function
 arguments to type according their type annotation.
 
 If you doesn't create broker as `RabbitBroker(apply_types=False)`,
 all broker handlers are wrapped by @apply_types by default.
 '''
 from propan.app import PropanApp
-from propan.brokers import RabbitBroker
 from propan.utils import apply_types
+from propan.brokers.rabbit import RabbitBroker
 
 from pydantic import BaseModel
 
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 app = PropanApp(broker)
```

### Comparing `propan-0.0.8.4/examples/7_handler_errors_processing.py` & `propan-0.0.8.5/examples/7_handler_errors_processing.py`

 * *Files 13% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 If you want to redelivere messages just use
 @handler(retry=...) parameter.
 
 For more complex usecases just use the `tenacity` library.
 '''
 
 from propan.app import PropanApp
-from propan.brokers import RabbitBroker
+from propan.brokers.rabbit import RabbitBroker
 
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 app = PropanApp(broker)
```

### Comparing `propan-0.0.8.4/examples/dependencies/1_dependency_injection.py` & `propan-0.0.8.5/examples/dependencies/1_dependency_injection.py`

 * *Files 7% similar despite different names*

```diff
@@ -7,16 +7,16 @@
 If you call not existed field it returns None value.
 '''
 from logging import Logger
 
 import aio_pika
 
 from propan.app import PropanApp
-from propan.brokers import RabbitBroker
 from propan.utils import Context
+from propan.brokers.rabbit import RabbitBroker
 
 
 rabbit_broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 app = PropanApp(rabbit_broker)
```

### Comparing `propan-0.0.8.4/examples/dependencies/2_dependency_declaration.py` & `propan-0.0.8.5/examples/dependencies/2_dependency_declaration.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 '''
 All Context dependencies also available from on_startup hook
 (Some of them are None at application starting).
 
 You can use it to setup your custom context fields.
 '''
 from propan.app import PropanApp
-from propan.brokers import RabbitBroker
 from propan.utils import Context
+from propan.brokers.rabbit import RabbitBroker
 
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 app = PropanApp(broker)
```

### Comparing `propan-0.0.8.4/examples/dependencies/4_dependency_deep_aliases.py` & `propan-0.0.8.5/examples/dependencies/4_dependency_deep_aliases.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/examples/dependencies/5_dependency_nesting.py` & `propan-0.0.8.5/examples/dependencies/5_dependency_nesting.py`

 * *Files 26% similar despite different names*

```diff
@@ -2,16 +2,16 @@
 @use_context decorator allows pass context dependencies
 to all functions with the same context through the functions
 calling stack.
 '''
 import aio_pika
 
 from propan.app import PropanApp
-from propan.brokers import RabbitBroker
 from propan.utils import use_context
+from propan.brokers.rabbit import RabbitBroker
 
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 app = PropanApp(broker)
```

### Comparing `propan-0.0.8.4/examples/http_frameworks_integrations/aiohttp.py` & `propan-0.0.8.5/examples/http_frameworks_integrations/aiohttp.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 '''
 You can use Propan MQBrokers without PropanApp
 Just start and stop them whenever you want
 '''
 from aiohttp import web
-from propan.brokers import RabbitBroker
+from propan.brokers.rabbit import RabbitBroker
 
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 
 @broker.handle("test")
 async def base_handler(body):
```

### Comparing `propan-0.0.8.4/examples/http_frameworks_integrations/blacksheep.py` & `propan-0.0.8.5/examples/http_frameworks_integrations/blacksheep.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 '''
 You can use Propan MQBrokers without PropanApp
 Just start and stop them whenever you want
 '''
 from blacksheep import Application
-from propan.brokers import RabbitBroker
+from propan.brokers.rabbit import RabbitBroker
 
 
 app = Application()
 
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
```

### Comparing `propan-0.0.8.4/examples/http_frameworks_integrations/falcon.py` & `propan-0.0.8.5/examples/http_frameworks_integrations/falcon.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 '''
 You can use Propan MQBrokers without PropanApp
 Just start and stop them whenever you want
 '''
 import falcon
 import falcon.asgi
-from propan.brokers import RabbitBroker
+from propan.brokers.rabbit import RabbitBroker
 
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 
 @broker.handle("test")
 async def base_handler(body):
```

### Comparing `propan-0.0.8.4/examples/http_frameworks_integrations/fastapi.py` & `propan-0.0.8.5/examples/http_frameworks_integrations/tornado.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,31 +1,41 @@
 '''
 You can use Propan MQBrokers without PropanApp
 Just start and stop them whenever you want
 '''
-from fastapi import FastAPI
-from propan.brokers import RabbitBroker
+import asyncio
 
+import tornado.web
+from propan.brokers.rabbit import RabbitBroker
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
-app = FastAPI()
-
 
 @broker.handle("test")
 async def base_handler(body):
     print(body)
 
 
-@app.on_event("startup")
-async def start_broker():
-    await broker.start()
+class MainHandler(tornado.web.RequestHandler):
+    def get(self):
+        self.write("Hello, world")
+
 
+def make_app():
+    return tornado.web.Application([
+        (r"/", MainHandler),
+    ])
 
-@app.on_event("shutdown")
-async def stop_broker():
-    await broker.close()
+
+async def main():
+    app = make_app()
+    app.listen(8888)
+    
+    await broker.start()
+    try:
+        await asyncio.Event().wait()
+    finally:
+        await broker.close()
 
 
-@app.get("/")
-def read_root():
-    return {"Hello": "World"}
+if __name__ == "__main__":
+    asyncio.run(main())
```

### Comparing `propan-0.0.8.4/examples/http_frameworks_integrations/quart.py` & `propan-0.0.8.5/examples/http_frameworks_integrations/sanic.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,31 +1,31 @@
 '''
 You can use Propan MQBrokers without PropanApp
 Just start and stop them whenever you want
 '''
-from quart import Quart
-from propan.brokers import RabbitBroker
+from sanic import Sanic
+from sanic.response import text
+from propan.brokers.rabbit import RabbitBroker
 
-broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
-app = Quart(__name__)
+app = Sanic("MyHelloWorldApp")
+broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 
 @broker.handle("test")
 async def base_handler(body):
     print(body)
 
 
-@app.before_serving
-async def start_broker():
-    await broker.start()
+@app.get("/")
+async def hello_world(request):
+    return text("Hello, world.")
 
 
-@app.after_serving
-async def stop_broker():
-    await broker.close()
-
+@app.after_server_start
+async def start_broker(app, loop):
+    await broker.start()
 
-@app.route("/")
-async def json():
-    return {"hello": "world"}
 
+@app.after_server_stop
+async def stop_broker(app, loop):
+    await broker.close()
```

### Comparing `propan-0.0.8.4/examples/http_frameworks_integrations/sanic.py` & `propan-0.0.8.5/examples/http_frameworks_integrations/quart.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,31 +1,31 @@
 '''
 You can use Propan MQBrokers without PropanApp
 Just start and stop them whenever you want
 '''
-from sanic import Sanic
-from sanic.response import text
-from propan.brokers import RabbitBroker
+from quart import Quart
+from propan.brokers.rabbit import RabbitBroker
 
-
-app = Sanic("MyHelloWorldApp")
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
+app = Quart(__name__)
+
 
 @broker.handle("test")
 async def base_handler(body):
     print(body)
 
 
-@app.get("/")
-async def hello_world(request):
-    return text("Hello, world.")
+@app.before_serving
+async def start_broker():
+    await broker.start()
 
 
-@app.after_server_start
-async def start_broker(app, loop):
-    await broker.start()
+@app.after_serving
+async def stop_broker():
+    await broker.close()
+
 
+@app.route("/")
+async def json():
+    return {"hello": "world"}
 
-@app.after_server_stop
-async def stop_broker(app, loop):
-    await broker.close()
```

### Comparing `propan-0.0.8.4/propan/app.py` & `propan-0.0.8.5/propan/app.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/brokers/push_back_watcher.py` & `propan-0.0.8.5/propan/brokers/push_back_watcher.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/brokers/model/broker_usecase.py` & `propan-0.0.8.5/propan/brokers/model/broker_usecase.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/brokers/nats/nats_broker.py` & `propan-0.0.8.5/propan/brokers/nats/nats_broker.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/brokers/nats/nats_broker.pyi` & `propan-0.0.8.5/propan/brokers/nats/nats_broker.pyi`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/brokers/nats/nats_js_broker.py` & `propan-0.0.8.5/propan/brokers/nats/nats_js_broker.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/brokers/rabbit/rabbit_broker.py` & `propan-0.0.8.5/propan/brokers/rabbit/rabbit_broker.py`

 * *Files 1% similar despite different names*

```diff
@@ -133,15 +133,15 @@
     async def close(self):
         if self._connection:
             await self._connection.close()
 
     async def _init_handler(self, handler: Handler):
         queue = await self._init_queue(handler.queue)
         if handler.exchange is not None:
-            exchange = await self._init_exchange_init_exchange(handler.exchange)
+            exchange = await self._init_exchange(handler.exchange)
             await queue.bind(exchange)
         return queue
 
     async def _init_queue(self, queue: RabbitQueue) -> aio_pika.abc.AbstractRobustQueue:
         if queue.declare is True:
             return await self._channel.declare_queue(**queue.dict())
         else:
```

### Comparing `propan-0.0.8.4/propan/brokers/rabbit/rabbit_broker.pyi` & `propan-0.0.8.5/propan/brokers/rabbit/rabbit_broker.pyi`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/brokers/rabbit/schemas.py` & `propan-0.0.8.5/propan/brokers/rabbit/schemas.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/cli/main.py` & `propan-0.0.8.5/propan/cli/main.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/cli/startproject.py` & `propan-0.0.8.5/propan/cli/startproject.py`

 * *Files 3% similar despite different names*

```diff
@@ -56,16 +56,16 @@
 
     _write_file(
         app_dir / 'serve.py',
         'import logging',
         'from typing import Optional',
         '',
         'from propan.app import PropanApp',
-        'from propan.brokers import RabbitBroker',
         'from propan.utils import Context',
+        'from propan.brokers.rabbit import RabbitBroker',
         '',
         'from core import broker',
         'from config import Settings, BASE_DIR',
         '',
         'from apps import *  # import to register handlers  # NOQA',
         '',
         '',
@@ -140,15 +140,15 @@
     _write_file(
         core_dir / '__init__.py',
         'from .dependencies import broker',
     )
 
     _write_file(
         core_dir / 'dependencies.py',
-        'from propan.brokers import RabbitBroker',
+        'from propan.brokers.rabbit import RabbitBroker',
         '',
         'broker = RabbitBroker()',
     )
 
     return core_dir
 
 
@@ -160,15 +160,15 @@
         'from .handlers import base_handler',
     )
     
     _write_file(
         apps_dir / 'handlers.py',
         'from core import broker',
         '',
-        'from propan.brokers import RabbitQueue, RabbitExchange',
+        'from propan.brokers.rabbit import RabbitQueue, RabbitExchange',
         '',
         '',
         '@broker.handle(queue=RabbitQueue("test"),',
         '               exchange=RabbitExchange("test"))',
         'async def base_handler(body: dict, logger):',
         '    logger.info(body)',
     )
```

### Comparing `propan-0.0.8.4/propan/cli/supervisors/basereload.py` & `propan-0.0.8.5/propan/cli/supervisors/basereload.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/cli/supervisors/multiprocess.py` & `propan-0.0.8.5/propan/cli/supervisors/multiprocess.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/cli/supervisors/utils.py` & `propan-0.0.8.5/propan/cli/supervisors/utils.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/cli/supervisors/watchgodreloader.py` & `propan-0.0.8.5/propan/cli/supervisors/watchgodreloader.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/log/formatter.py` & `propan-0.0.8.5/propan/log/formatter.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/log/logging.py` & `propan-0.0.8.5/propan/log/logging.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/utils/functions.py` & `propan-0.0.8.5/propan/utils/functions.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/utils/context/decorate.py` & `propan-0.0.8.5/propan/utils/context/decorate.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/utils/context/main.py` & `propan-0.0.8.5/propan/utils/context/main.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/propan/utils/types/decorate.py` & `propan-0.0.8.5/propan/utils/types/decorate.py`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/LICENSE` & `propan-0.0.8.5/LICENSE`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/README.md` & `propan-0.0.8.5/README.md`

 * *Files 10% similar despite different names*

```diff
@@ -48,16 +48,16 @@
 
 ### Basic usage
 
 Create an application with the following code at `serve.py`:
 
 ```python
 from propan.app import PropanApp
-from propan.brokers import RabbitBroker
-# from propan.brokers import NatsBroker
+from propan.brokers.rabbit import RabbitBroker
+# from propan.brokers.nats import NatsBroker
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 # broker = NatsBroker("nats://localhost:4222")
 
 app = PropanApp(broker)
 
 @broker.handle("test")
@@ -75,16 +75,17 @@
 ---
 
 ## Type casting
 
 Propan uses `pydantic` to cast incoming function arguments to type according their type annotation.
 
 ```python
-from propan import PropanApp, RabbitBroker, Context
 from pydantic import BaseModel
+from propan import PropanApp, Context
+from propan.brokers.rabbit import RabbitBroker
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 app = PropanApp(broker)
 
 class SimpleMessage(BaseModel):
     key: int
 
@@ -108,15 +109,16 @@
 But you can specify your own dependencies, call dependencies functions (like `Fastapi Depends`)
 and [more](https://github.com/Lancetnik/Propan/tree/main/examples/dependencies).
 
 ```python
 from logging import Logger
 
 import aio_pika
-from propan import PropanApp, RabbitBroker, Context
+from propan import PropanApp, Context
+from propan.brokers.rabbit import RabbitBroker
 
 rabbit_broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 app = PropanApp(rabbit_broker)
 
 @rabbit_broker.handle("test")
 async def base_handler(body: dict,
@@ -144,15 +146,16 @@
 
 For example: pass your current *.env* project setting to context
 ```bash
 $ propan run serve:app --env=.env.dev
 ```
 
 ```python
-from propan import PropanApp, RabbitBroker, Context
+from propan import PropanApp, Context
+from propan.brokers.rabbit import RabbitBroker
 from pydantic import BaseSettings
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 app = PropanApp(broker)
 
 class Settings(BaseSettings):
@@ -191,15 +194,15 @@
 ## HTTP Frameworks integrations
 
 You can use Propan MQBrokers without PropanApp.
 Just *start* and *stop* them according your application lifespan.
 
 ```python
 from fastapi import FastAPI
-from propan.brokers import RabbitBroker
+from propan.brokers.rabbit import RabbitBroker
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 app = FastAPI()
 
 @broker.handle("test")
 async def base_handler(body):
```

### Comparing `propan-0.0.8.4/pyproject.toml` & `propan-0.0.8.5/pyproject.toml`

 * *Files identical despite different names*

### Comparing `propan-0.0.8.4/PKG-INFO` & `propan-0.0.8.5/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: propan
-Version: 0.0.8.4
+Version: 0.0.8.5
 Summary: Propan framework: the simplest way to work with a messaging queues
 Project-URL: Homepage, https://github.com/Lancetnik/Propan
 Project-URL: Documentation, https://github.com/Lancetnik/Propan
 Project-URL: Tracker, https://github.com/Lancetnik/Propan/issues
 Project-URL: Source, https://github.com/Lancetnik/Propan
 Author-email: Pastukhov Nikita <diementros@yandex.ru>
 License-Expression: MIT
@@ -106,16 +106,16 @@
 
 ### Basic usage
 
 Create an application with the following code at `serve.py`:
 
 ```python
 from propan.app import PropanApp
-from propan.brokers import RabbitBroker
-# from propan.brokers import NatsBroker
+from propan.brokers.rabbit import RabbitBroker
+# from propan.brokers.nats import NatsBroker
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 # broker = NatsBroker("nats://localhost:4222")
 
 app = PropanApp(broker)
 
 @broker.handle("test")
@@ -133,16 +133,17 @@
 ---
 
 ## Type casting
 
 Propan uses `pydantic` to cast incoming function arguments to type according their type annotation.
 
 ```python
-from propan import PropanApp, RabbitBroker, Context
 from pydantic import BaseModel
+from propan import PropanApp, Context
+from propan.brokers.rabbit import RabbitBroker
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 app = PropanApp(broker)
 
 class SimpleMessage(BaseModel):
     key: int
 
@@ -166,15 +167,16 @@
 But you can specify your own dependencies, call dependencies functions (like `Fastapi Depends`)
 and [more](https://github.com/Lancetnik/Propan/tree/main/examples/dependencies).
 
 ```python
 from logging import Logger
 
 import aio_pika
-from propan import PropanApp, RabbitBroker, Context
+from propan import PropanApp, Context
+from propan.brokers.rabbit import RabbitBroker
 
 rabbit_broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 app = PropanApp(rabbit_broker)
 
 @rabbit_broker.handle("test")
 async def base_handler(body: dict,
@@ -202,15 +204,16 @@
 
 For example: pass your current *.env* project setting to context
 ```bash
 $ propan run serve:app --env=.env.dev
 ```
 
 ```python
-from propan import PropanApp, RabbitBroker, Context
+from propan import PropanApp, Context
+from propan.brokers.rabbit import RabbitBroker
 from pydantic import BaseSettings
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 app = PropanApp(broker)
 
 class Settings(BaseSettings):
@@ -249,15 +252,15 @@
 ## HTTP Frameworks integrations
 
 You can use Propan MQBrokers without PropanApp.
 Just *start* and *stop* them according your application lifespan.
 
 ```python
 from fastapi import FastAPI
-from propan.brokers import RabbitBroker
+from propan.brokers.rabbit import RabbitBroker
 
 broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
 
 app = FastAPI()
 
 @broker.handle("test")
 async def base_handler(body):
```

