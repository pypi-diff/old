# Comparing `tmp/pydantic_core-0.8.2.tar.gz` & `tmp/pydantic_core-0.9.0.tar.gz`

## Comparing `pydantic_core-0.8.2.tar` & `pydantic_core-0.9.0.tar`

### file list

```diff
@@ -1,188 +1,188 @@
--rw-r--r--   0        0        0     1952 1970-01-01 00:00:00.000000 pydantic_core-0.8.2/Cargo.toml
--rw-r--r--   0     1001      123      505 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/.cargo/config.toml
--rw-r--r--   0     1001      123     1080 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/LICENSE
--rw-r--r--   0     1001      123     3477 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/Makefile
--rw-r--r--   0     1001      123     5640 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/README.md
--rw-r--r--   0     1001      123     1220 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/build.rs
--rw-r--r--   0     1001      123     8951 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/generate_self_schema.py
--rw-r--r--   0     1001      123      715 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/pydantic_core/__init__.py
--rw-r--r--   0     1001      123     5184 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/pydantic_core/_pydantic_core.pyi
--rw-r--r--   0     1001      123    81000 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/pydantic_core/core_schema.py
--rw-r--r--   0     1001      123        1 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/pydantic_core/py.typed
--rw-r--r--   0     1001      123     2745 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/pyproject.toml
--rw-r--r--   0     1001      123        8 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/rust-toolchain
--rw-r--r--   0     1001      123     5831 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/build_context.rs
--rw-r--r--   0     1001      123     5657 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/build_tools.rs
--rw-r--r--   0     1001      123     5435 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/errors/line_error.rs
--rw-r--r--   0     1001      123     3767 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/errors/location.rs
--rw-r--r--   0     1001      123     1054 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/errors/mod.rs
--rw-r--r--   0     1001      123    27211 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/errors/types.rs
--rw-r--r--   0     1001      123     6626 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/errors/validation_exception.rs
--rw-r--r--   0     1001      123     4603 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/errors/value_exception.rs
--rw-r--r--   0     1001      123    14254 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/input/datetime.rs
--rw-r--r--   0     1001      123     7583 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/input/input_abstract.rs
--rw-r--r--   0     1001      123    18053 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/input/input_json.rs
--rw-r--r--   0     1001      123    26555 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/input/input_python.rs
--rw-r--r--   0     1001      123      926 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/input/mod.rs
--rw-r--r--   0     1001      123     6138 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/input/parse_json.rs
--rw-r--r--   0     1001      123    20065 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/input/return_enums.rs
--rw-r--r--   0     1001      123     1913 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/input/shared.rs
--rw-r--r--   0     1001      123     2033 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/lib.rs
--rw-r--r--   0     1001      123    14125 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/lookup_key.rs
--rw-r--r--   0     1001      123      661 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/questions.rs
--rw-r--r--   0     1001      123     1660 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/recursion_guard.rs
--rw-r--r--   0     1001      123     5386 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/config.rs
--rw-r--r--   0     1001      123     2385 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/errors.rs
--rw-r--r--   0     1001      123     9414 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/extra.rs
--rw-r--r--   0     1001      123    11729 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/filter.rs
--rw-r--r--   0     1001      123    20353 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/infer.rs
--rw-r--r--   0     1001      123     4833 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/mod.rs
--rw-r--r--   0     1001      123    10817 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/ob_type.rs
--rw-r--r--   0     1001      123    13296 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/shared.rs
--rw-r--r--   0     1001      123     1411 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/any.rs
--rw-r--r--   0     1001      123     2499 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/bytes.rs
--rw-r--r--   0     1001      123     3942 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/datetime_etc.rs
--rw-r--r--   0     1001      123     5256 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/dict.rs
--rw-r--r--   0     1001      123     6493 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/format.rs
--rw-r--r--   0     1001      123    14140 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/function.rs
--rw-r--r--   0     1001      123     7328 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/generator.rs
--rw-r--r--   0     1001      123     2963 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/json.rs
--rw-r--r--   0     1001      123     4016 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/list.rs
--rw-r--r--   0     1001      123     5456 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/literal.rs
--rw-r--r--   0     1001      123      973 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/mod.rs
--rw-r--r--   0     1001      123     3424 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/model.rs
--rw-r--r--   0     1001      123     2388 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/nullable.rs
--rw-r--r--   0     1001      123     4422 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/other.rs
--rw-r--r--   0     1001      123     2254 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/recursive.rs
--rw-r--r--   0     1001      123     4491 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/set_frozenset.rs
--rw-r--r--   0     1001      123     5900 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/simple.rs
--rw-r--r--   0     1001      123     2568 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/string.rs
--rw-r--r--   0     1001      123     2456 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/timedelta.rs
--rw-r--r--   0     1001      123    12846 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/tuple.rs
--rw-r--r--   0     1001      123    10492 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/typed_dict.rs
--rw-r--r--   0     1001      123     6839 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/union.rs
--rw-r--r--   0     1001      123     3106 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/url.rs
--rw-r--r--   0     1001      123     2226 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/serializers/type_serializers/with_default.rs
--rw-r--r--   0     1001      123     9113 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/url.rs
--rw-r--r--   0     1001      123     1122 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/any.rs
--rw-r--r--   0     1001      123    14031 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/arguments.rs
--rw-r--r--   0     1001      123     1309 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/bool.rs
--rw-r--r--   0     1001      123     3070 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/bytes.rs
--rw-r--r--   0     1001      123     3076 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/call.rs
--rw-r--r--   0     1001      123     1158 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/callable.rs
--rw-r--r--   0     1001      123     3302 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/chain.rs
--rw-r--r--   0     1001      123     3558 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/custom_error.rs
--rw-r--r--   0     1001      123     6652 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/date.rs
--rw-r--r--   0     1001      123     7881 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/datetime.rs
--rw-r--r--   0     1001      123     6002 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/dict.rs
--rw-r--r--   0     1001      123     4723 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/float.rs
--rw-r--r--   0     1001      123     2250 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/frozenset.rs
--rw-r--r--   0     1001      123    10030 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/function.rs
--rw-r--r--   0     1001      123     7053 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/generator.rs
--rw-r--r--   0     1001      123     3960 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/int.rs
--rw-r--r--   0     1001      123     3174 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/is_instance.rs
--rw-r--r--   0     1001      123     1861 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/is_subclass.rs
--rw-r--r--   0     1001      123     2402 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/json.rs
--rw-r--r--   0     1001      123     2336 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/lax_or_strict.rs
--rw-r--r--   0     1001      123     4773 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/list.rs
--rw-r--r--   0     1001      123     9837 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/literal.rs
--rw-r--r--   0     1001      123    17794 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/mod.rs
--rw-r--r--   0     1001      123     8226 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/model.rs
--rw-r--r--   0     1001      123     1131 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/none.rs
--rw-r--r--   0     1001      123     1793 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/nullable.rs
--rw-r--r--   0     1001      123     3786 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/recursive.rs
--rw-r--r--   0     1001      123     3394 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/set.rs
--rw-r--r--   0     1001      123     5468 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/string.rs
--rw-r--r--   0     1001      123     3343 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/time.rs
--rw-r--r--   0     1001      123     3506 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/timedelta.rs
--rw-r--r--   0     1001      123     9363 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/tuple.rs
--rw-r--r--   0     1001      123    16103 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/typed_dict.rs
--rw-r--r--   0     1001      123    17050 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/union.rs
--rw-r--r--   0     1001      123    16923 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/url.rs
--rw-r--r--   0     1001      123     4424 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/src/validators/with_default.rs
--rw-r--r--   0     1001      123        0 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/__init__.py
--rw-r--r--   0     1001      123    23377 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/benchmarks/README.md
--rw-r--r--   0     1001      123        0 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/benchmarks/__init__.py
--rw-r--r--   0     1001      123    15868 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/benchmarks/complete_schema.py
--rw-r--r--   0     1001      123     6610 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/benchmarks/test_complete_benchmark.py
--rw-r--r--   0     1001      123    34451 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/benchmarks/test_micro_benchmarks.py
--rw-r--r--   0     1001      123    13845 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/benchmarks/test_serialization_micro.py
--rwxr-xr-x   0     1001      123      196 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/check-debug.sh
--rw-r--r--   0     1001      123     3367 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/conftest.py
--rw-r--r--   0     1001      123     3247 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/emscripten_runner.js
--rw-r--r--   0     1001      123       68 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/requirements-linting.txt
--rw-r--r--   0     1001      123      206 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/requirements.txt
--rw-r--r--   0     1001      123        0 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/__init__.py
--rw-r--r--   0     1001      123    15270 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_any.py
--rw-r--r--   0     1001      123     4462 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_bytes.py
--rw-r--r--   0     1001      123     4798 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_datetime.py
--rw-r--r--   0     1001      123     7509 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_dict.py
--rw-r--r--   0     1001      123     4659 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_format.py
--rw-r--r--   0     1001      123    11241 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_functions.py
--rw-r--r--   0     1001      123     5198 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_generator.py
--rw-r--r--   0     1001      123     1853 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_json.py
--rw-r--r--   0     1001      123    15520 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_list_tuple.py
--rw-r--r--   0     1001      123     2164 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_literal.py
--rw-r--r--   0     1001      123      517 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_misc.py
--rw-r--r--   0     1001      123    16117 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_model.py
--rw-r--r--   0     1001      123      944 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_none.py
--rw-r--r--   0     1001      123      566 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_nullable.py
--rw-r--r--   0     1001      123     2121 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_other.py
--rw-r--r--   0     1001      123     2475 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_recursive.py
--rw-r--r--   0     1001      123     2052 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_set_frozenset.py
--rw-r--r--   0     1001      123     2292 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_simple.py
--rw-r--r--   0     1001      123     2623 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_string.py
--rw-r--r--   0     1001      123     1665 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_timedelta.py
--rw-r--r--   0     1001      123     7775 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_typed_dict.py
--rw-r--r--   0     1001      123     9668 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_union.py
--rw-r--r--   0     1001      123     3740 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/serializers/test_url.py
--rw-r--r--   0     1001      123     3005 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/test_build.py
--rw-r--r--   0     1001      123     8447 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/test_config.py
--rw-r--r--   0     1001      123     2444 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/test_docstrings.py
--rw-r--r--   0     1001      123    15313 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/test_errors.py
--rw-r--r--   0     1001      123     5391 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/test_hypothesis.py
--rw-r--r--   0     1001      123     2879 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/test_isinstance.py
--rw-r--r--   0     1001      123     5658 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/test_json.py
--rw-r--r--   0     1001      123     5839 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/test_misc.py
--rw-r--r--   0     1001      123    10433 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/test_schema_functions.py
--rw-r--r--   0     1001      123     1795 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/test_strict.py
--rw-r--r--   0     1001      123     7862 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/test_typing.py
--rw-r--r--   0     1001      123     4310 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/test_validation_context.py
--rw-r--r--   0     1001      123        0 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/__init__.py
--rw-r--r--   0     1001      123    35440 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_arguments.py
--rw-r--r--   0     1001      123     3456 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_bool.py
--rw-r--r--   0     1001      123     4345 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_bytes.py
--rw-r--r--   0     1001      123     5866 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_call.py
--rw-r--r--   0     1001      123     1523 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_callable.py
--rw-r--r--   0     1001      123     4702 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_chain.py
--rw-r--r--   0     1001      123     2929 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_custom_error.py
--rw-r--r--   0     1001      123    11563 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_date.py
--rw-r--r--   0     1001      123    17084 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_datetime.py
--rw-r--r--   0     1001      123     8238 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_dict.py
--rw-r--r--   0     1001      123    11498 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_float.py
--rw-r--r--   0     1001      123    11835 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_frozenset.py
--rw-r--r--   0     1001      123    12458 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_function.py
--rw-r--r--   0     1001      123     3803 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_generator.py
--rw-r--r--   0     1001      123     8201 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_int.py
--rw-r--r--   0     1001      123     7318 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_is_instance.py
--rw-r--r--   0     1001      123     1997 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_is_subclass.py
--rw-r--r--   0     1001      123     6639 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_json.py
--rw-r--r--   0     1001      123     1606 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_lax_or_strict.py
--rw-r--r--   0     1001      123    13988 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_list.py
--rw-r--r--   0     1001      123     7189 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_literal.py
--rw-r--r--   0     1001      123    18899 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_model.py
--rw-r--r--   0     1001      123      430 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_none.py
--rw-r--r--   0     1001      123     1039 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_nullable.py
--rw-r--r--   0     1001      123    25475 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_recursive.py
--rw-r--r--   0     1001      123    11090 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_set.py
--rw-r--r--   0     1001      123     8719 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_string.py
--rw-r--r--   0     1001      123    15176 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_tagged_union.py
--rw-r--r--   0     1001      123     8739 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_time.py
--rw-r--r--   0     1001      123    12266 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_timedelta.py
--rw-r--r--   0     1001      123    18806 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_tuple.py
--rw-r--r--   0     1001      123    48967 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_typed_dict.py
--rw-r--r--   0     1001      123    10967 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_union.py
--rw-r--r--   0     1001      123    49419 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_url.py
--rw-r--r--   0     1001      123    10340 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/tests/validators/test_with_default.py
--rw-r--r--   0     1001      123    14622 2023-02-02 15:29:47.000000 pydantic_core-0.8.2/Cargo.lock
--rw-r--r--   0        0        0     7106 1970-01-01 00:00:00.000000 pydantic_core-0.8.2/PKG-INFO
+-rw-r--r--   0        0        0     1618 1970-01-01 00:00:00.000000 pydantic_core-0.9.0/Cargo.toml
+-rw-r--r--   0     1001      123      505 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/.cargo/config.toml
+-rw-r--r--   0     1001      123     1080 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/LICENSE
+-rw-r--r--   0     1001      123     3477 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/Makefile
+-rw-r--r--   0     1001      123     5640 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/README.md
+-rw-r--r--   0     1001      123     1220 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/build.rs
+-rw-r--r--   0     1001      123     8951 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/generate_self_schema.py
+-rw-r--r--   0     1001      123      753 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/pydantic_core/__init__.py
+-rw-r--r--   0     1001      123     5184 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/pydantic_core/_pydantic_core.pyi
+-rw-r--r--   0     1001      123    82414 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/pydantic_core/core_schema.py
+-rw-r--r--   0     1001      123        1 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/pydantic_core/py.typed
+-rw-r--r--   0     1001      123     2655 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/pyproject.toml
+-rw-r--r--   0     1001      123        8 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/rust-toolchain
+-rw-r--r--   0     1001      123     5831 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/build_context.rs
+-rw-r--r--   0     1001      123     5657 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/build_tools.rs
+-rw-r--r--   0     1001      123     5435 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/errors/line_error.rs
+-rw-r--r--   0     1001      123     3767 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/errors/location.rs
+-rw-r--r--   0     1001      123     1054 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/errors/mod.rs
+-rw-r--r--   0     1001      123    27211 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/errors/types.rs
+-rw-r--r--   0     1001      123     6626 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/errors/validation_exception.rs
+-rw-r--r--   0     1001      123     4603 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/errors/value_exception.rs
+-rw-r--r--   0     1001      123    14254 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/input/datetime.rs
+-rw-r--r--   0     1001      123     7583 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/input/input_abstract.rs
+-rw-r--r--   0     1001      123    18053 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/input/input_json.rs
+-rw-r--r--   0     1001      123    26555 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/input/input_python.rs
+-rw-r--r--   0     1001      123      926 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/input/mod.rs
+-rw-r--r--   0     1001      123     6138 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/input/parse_json.rs
+-rw-r--r--   0     1001      123    20065 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/input/return_enums.rs
+-rw-r--r--   0     1001      123     1913 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/input/shared.rs
+-rw-r--r--   0     1001      123     2033 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/lib.rs
+-rw-r--r--   0     1001      123    14125 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/lookup_key.rs
+-rw-r--r--   0     1001      123      661 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/questions.rs
+-rw-r--r--   0     1001      123     1660 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/recursion_guard.rs
+-rw-r--r--   0     1001      123     5386 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/config.rs
+-rw-r--r--   0     1001      123     2385 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/errors.rs
+-rw-r--r--   0     1001      123     9414 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/extra.rs
+-rw-r--r--   0     1001      123    11729 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/filter.rs
+-rw-r--r--   0     1001      123    20353 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/infer.rs
+-rw-r--r--   0     1001      123     4833 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/mod.rs
+-rw-r--r--   0     1001      123    10817 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/ob_type.rs
+-rw-r--r--   0     1001      123    13296 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/shared.rs
+-rw-r--r--   0     1001      123     1411 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/any.rs
+-rw-r--r--   0     1001      123     2499 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/bytes.rs
+-rw-r--r--   0     1001      123     3942 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/datetime_etc.rs
+-rw-r--r--   0     1001      123     5256 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/dict.rs
+-rw-r--r--   0     1001      123     6493 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/format.rs
+-rw-r--r--   0     1001      123    14140 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/function.rs
+-rw-r--r--   0     1001      123     7328 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/generator.rs
+-rw-r--r--   0     1001      123     2963 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/json.rs
+-rw-r--r--   0     1001      123     4016 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/list.rs
+-rw-r--r--   0     1001      123     5456 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/literal.rs
+-rw-r--r--   0     1001      123      973 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/mod.rs
+-rw-r--r--   0     1001      123     3424 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/model.rs
+-rw-r--r--   0     1001      123     2388 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/nullable.rs
+-rw-r--r--   0     1001      123     4422 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/other.rs
+-rw-r--r--   0     1001      123     2254 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/recursive.rs
+-rw-r--r--   0     1001      123     4491 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/set_frozenset.rs
+-rw-r--r--   0     1001      123     5900 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/simple.rs
+-rw-r--r--   0     1001      123     2568 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/string.rs
+-rw-r--r--   0     1001      123     2456 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/timedelta.rs
+-rw-r--r--   0     1001      123    12846 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/tuple.rs
+-rw-r--r--   0     1001      123    10492 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/typed_dict.rs
+-rw-r--r--   0     1001      123     6839 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/union.rs
+-rw-r--r--   0     1001      123     3106 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/url.rs
+-rw-r--r--   0     1001      123     2226 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/serializers/type_serializers/with_default.rs
+-rw-r--r--   0     1001      123     9113 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/url.rs
+-rw-r--r--   0     1001      123     1122 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/any.rs
+-rw-r--r--   0     1001      123    14031 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/arguments.rs
+-rw-r--r--   0     1001      123     1309 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/bool.rs
+-rw-r--r--   0     1001      123     3070 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/bytes.rs
+-rw-r--r--   0     1001      123     3076 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/call.rs
+-rw-r--r--   0     1001      123     1158 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/callable.rs
+-rw-r--r--   0     1001      123     3302 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/chain.rs
+-rw-r--r--   0     1001      123     3558 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/custom_error.rs
+-rw-r--r--   0     1001      123     6652 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/date.rs
+-rw-r--r--   0     1001      123     7881 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/datetime.rs
+-rw-r--r--   0     1001      123     6002 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/dict.rs
+-rw-r--r--   0     1001      123     4723 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/float.rs
+-rw-r--r--   0     1001      123     2250 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/frozenset.rs
+-rw-r--r--   0     1001      123    10030 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/function.rs
+-rw-r--r--   0     1001      123     7053 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/generator.rs
+-rw-r--r--   0     1001      123     3960 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/int.rs
+-rw-r--r--   0     1001      123     3174 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/is_instance.rs
+-rw-r--r--   0     1001      123     1861 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/is_subclass.rs
+-rw-r--r--   0     1001      123     2402 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/json.rs
+-rw-r--r--   0     1001      123     2336 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/lax_or_strict.rs
+-rw-r--r--   0     1001      123     4773 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/list.rs
+-rw-r--r--   0     1001      123     9837 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/literal.rs
+-rw-r--r--   0     1001      123    17794 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/mod.rs
+-rw-r--r--   0     1001      123     8226 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/model.rs
+-rw-r--r--   0     1001      123     1131 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/none.rs
+-rw-r--r--   0     1001      123     1793 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/nullable.rs
+-rw-r--r--   0     1001      123     3786 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/recursive.rs
+-rw-r--r--   0     1001      123     3394 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/set.rs
+-rw-r--r--   0     1001      123     5468 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/string.rs
+-rw-r--r--   0     1001      123     3343 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/time.rs
+-rw-r--r--   0     1001      123     3506 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/timedelta.rs
+-rw-r--r--   0     1001      123     9363 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/tuple.rs
+-rw-r--r--   0     1001      123    16103 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/typed_dict.rs
+-rw-r--r--   0     1001      123    17050 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/union.rs
+-rw-r--r--   0     1001      123    16923 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/url.rs
+-rw-r--r--   0     1001      123     4424 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/src/validators/with_default.rs
+-rw-r--r--   0     1001      123        0 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/__init__.py
+-rw-r--r--   0     1001      123    23377 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/benchmarks/README.md
+-rw-r--r--   0     1001      123        0 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/benchmarks/__init__.py
+-rw-r--r--   0     1001      123    15868 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/benchmarks/complete_schema.py
+-rw-r--r--   0     1001      123     6610 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/benchmarks/test_complete_benchmark.py
+-rw-r--r--   0     1001      123    34451 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/benchmarks/test_micro_benchmarks.py
+-rw-r--r--   0     1001      123    13845 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/benchmarks/test_serialization_micro.py
+-rwxr-xr-x   0     1001      123      196 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/check-debug.sh
+-rw-r--r--   0     1001      123     3367 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/conftest.py
+-rw-r--r--   0     1001      123     3247 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/emscripten_runner.js
+-rw-r--r--   0     1001      123       68 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/requirements-linting.txt
+-rw-r--r--   0     1001      123      206 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/requirements.txt
+-rw-r--r--   0     1001      123        0 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/__init__.py
+-rw-r--r--   0     1001      123    15164 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_any.py
+-rw-r--r--   0     1001      123     4342 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_bytes.py
+-rw-r--r--   0     1001      123     4798 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_datetime.py
+-rw-r--r--   0     1001      123     7509 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_dict.py
+-rw-r--r--   0     1001      123     4659 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_format.py
+-rw-r--r--   0     1001      123    11241 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_functions.py
+-rw-r--r--   0     1001      123     5198 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_generator.py
+-rw-r--r--   0     1001      123     1853 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_json.py
+-rw-r--r--   0     1001      123    15520 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_list_tuple.py
+-rw-r--r--   0     1001      123     2164 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_literal.py
+-rw-r--r--   0     1001      123      517 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_misc.py
+-rw-r--r--   0     1001      123    16117 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_model.py
+-rw-r--r--   0     1001      123      944 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_none.py
+-rw-r--r--   0     1001      123      566 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_nullable.py
+-rw-r--r--   0     1001      123     2121 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_other.py
+-rw-r--r--   0     1001      123     2475 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_recursive.py
+-rw-r--r--   0     1001      123     2052 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_set_frozenset.py
+-rw-r--r--   0     1001      123     2172 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_simple.py
+-rw-r--r--   0     1001      123     2503 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_string.py
+-rw-r--r--   0     1001      123     1665 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_timedelta.py
+-rw-r--r--   0     1001      123     7775 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_typed_dict.py
+-rw-r--r--   0     1001      123     9668 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_union.py
+-rw-r--r--   0     1001      123     3740 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/serializers/test_url.py
+-rw-r--r--   0     1001      123     3005 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/test_build.py
+-rw-r--r--   0     1001      123     8447 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/test_config.py
+-rw-r--r--   0     1001      123     2444 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/test_docstrings.py
+-rw-r--r--   0     1001      123    15319 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/test_errors.py
+-rw-r--r--   0     1001      123     5391 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/test_hypothesis.py
+-rw-r--r--   0     1001      123     2879 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/test_isinstance.py
+-rw-r--r--   0     1001      123     5658 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/test_json.py
+-rw-r--r--   0     1001      123     6638 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/test_misc.py
+-rw-r--r--   0     1001      123    10445 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/test_schema_functions.py
+-rw-r--r--   0     1001      123     1795 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/test_strict.py
+-rw-r--r--   0     1001      123     7862 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/test_typing.py
+-rw-r--r--   0     1001      123     4310 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/test_validation_context.py
+-rw-r--r--   0     1001      123        0 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/__init__.py
+-rw-r--r--   0     1001      123    35440 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_arguments.py
+-rw-r--r--   0     1001      123     3456 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_bool.py
+-rw-r--r--   0     1001      123     4345 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_bytes.py
+-rw-r--r--   0     1001      123     5866 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_call.py
+-rw-r--r--   0     1001      123     1523 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_callable.py
+-rw-r--r--   0     1001      123     4702 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_chain.py
+-rw-r--r--   0     1001      123     2929 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_custom_error.py
+-rw-r--r--   0     1001      123    11563 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_date.py
+-rw-r--r--   0     1001      123    17084 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_datetime.py
+-rw-r--r--   0     1001      123     8238 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_dict.py
+-rw-r--r--   0     1001      123    11498 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_float.py
+-rw-r--r--   0     1001      123    11835 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_frozenset.py
+-rw-r--r--   0     1001      123    12458 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_function.py
+-rw-r--r--   0     1001      123     3803 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_generator.py
+-rw-r--r--   0     1001      123     8201 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_int.py
+-rw-r--r--   0     1001      123     7318 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_is_instance.py
+-rw-r--r--   0     1001      123     1997 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_is_subclass.py
+-rw-r--r--   0     1001      123     6639 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_json.py
+-rw-r--r--   0     1001      123     1606 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_lax_or_strict.py
+-rw-r--r--   0     1001      123    13856 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_list.py
+-rw-r--r--   0     1001      123     7189 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_literal.py
+-rw-r--r--   0     1001      123    18899 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_model.py
+-rw-r--r--   0     1001      123      430 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_none.py
+-rw-r--r--   0     1001      123     1039 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_nullable.py
+-rw-r--r--   0     1001      123    25475 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_recursive.py
+-rw-r--r--   0     1001      123    11090 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_set.py
+-rw-r--r--   0     1001      123     8719 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_string.py
+-rw-r--r--   0     1001      123    15176 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_tagged_union.py
+-rw-r--r--   0     1001      123     8739 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_time.py
+-rw-r--r--   0     1001      123    12266 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_timedelta.py
+-rw-r--r--   0     1001      123    18806 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_tuple.py
+-rw-r--r--   0     1001      123    48967 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_typed_dict.py
+-rw-r--r--   0     1001      123    10967 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_union.py
+-rw-r--r--   0     1001      123    49419 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_url.py
+-rw-r--r--   0     1001      123    10340 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/tests/validators/test_with_default.py
+-rw-r--r--   0     1001      123    14927 2023-02-10 17:51:11.000000 pydantic_core-0.9.0/Cargo.lock
+-rw-r--r--   0        0        0     7011 1970-01-01 00:00:00.000000 pydantic_core-0.9.0/PKG-INFO
```

### Comparing `pydantic_core-0.8.2/Cargo.toml` & `pydantic_core-0.9.0/Cargo.toml`

 * *Files 23% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [package]
 name = "pydantic-core"
-version = "0.8.2"
+version = "0.9.0"
 edition = "2021"
 license = "MIT"
 homepage = "https://github.com/pydantic/pydantic-core"
 repository = "https://github.com/pydantic/pydantic-core.git"
 readme = "README.md"
 include = [
     "/pyproject.toml",
@@ -22,17 +22,15 @@
     "!__pycache__",
     "!tests/.hypothesis",
     "!tests/.pytest_cache",
     "!*.so",
 ]
 
 [dependencies]
-# required since `Py_Ellipsis` fails on windows, see https://github.com/PyO3/pyo3/pull/2911
-pyo3 = { git = "https://github.com/PyO3/pyo3", rev = "ec2485bb7dadbed602f286efba9e0900bbcbd50d" }
-#pyo3 = "0.18.0"
+pyo3 = "0.18.1"
 regex = "1.6.0"
 strum = { version = "0.24.1", features = ["derive"] }
 strum_macros = "0.24.3"
 serde_json = {version = "1.0.87", features = ["preserve_order"]}
 enum_dispatch = "0.3.8"
 serde = "1.0.147"
 indexmap = "1.9.1"
@@ -63,10 +61,8 @@
 codegen-units = 1
 panic = "abort"
 strip = true
 
 [build-dependencies]
 version_check = "0.9.4"
 # used where logic has to be version/distribution specific, e.g. pypy
-# FIXME change when `pyo3` above is updated
-pyo3-build-config = { git = "https://github.com/PyO3/pyo3", rev = "ec2485bb7dadbed602f286efba9e0900bbcbd50d" }
-#pyo3 = "0.18.0"
+pyo3-build-config = "0.18.1"
```

### Comparing `pydantic_core-0.8.2/LICENSE` & `pydantic_core-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/Makefile` & `pydantic_core-0.9.0/Makefile`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/README.md` & `pydantic_core-0.9.0/README.md`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/build.rs` & `pydantic_core-0.9.0/build.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/generate_self_schema.py` & `pydantic_core-0.9.0/generate_self_schema.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/pydantic_core/__init__.py` & `pydantic_core-0.9.0/pydantic_core/__init__.py`

 * *Files 7% similar despite different names*

```diff
@@ -9,20 +9,21 @@
     SchemaSerializer,
     SchemaValidator,
     Url,
     ValidationError,
     __version__,
     to_json,
 )
-from .core_schema import CoreConfig, CoreSchema
+from .core_schema import CoreConfig, CoreSchema, CoreSchemaType
 
 __all__ = (
     '__version__',
     'CoreConfig',
     'CoreSchema',
+    'CoreSchemaType',
     'SchemaValidator',
     'SchemaSerializer',
     'Url',
     'MultiHostUrl',
     'SchemaError',
     'ValidationError',
     'PydanticCustomError',
```

### Comparing `pydantic_core-0.8.2/pydantic_core/_pydantic_core.pyi` & `pydantic_core-0.9.0/pydantic_core/_pydantic_core.pyi`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/pydantic_core/core_schema.py` & `pydantic_core-0.9.0/pydantic_core/core_schema.py`

 * *Files 12% similar despite different names*

```diff
@@ -280,116 +280,116 @@
     SimpleSerSchema, FunctionPlainSerSchema, FunctionWrapSerSchema, FormatSerSchema, ToStringSerSchema, ModelSerSchema
 ]
 
 
 class AnySchema(TypedDict, total=False):
     type: Required[Literal['any']]
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
-def any_schema(*, ref: str | None = None, extra: Any = None, serialization: SerSchema | None = None) -> AnySchema:
+def any_schema(*, ref: str | None = None, metadata: Any = None, serialization: SerSchema | None = None) -> AnySchema:
     """
     Returns a schema that matches any value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
     schema = core_schema.any_schema()
     v = SchemaValidator(schema)
     assert v.validate_python(1) == 1
     ```
 
     Args:
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
-    return dict_not_none(type='any', ref=ref, extra=extra, serialization=serialization)
+    return dict_not_none(type='any', ref=ref, metadata=metadata, serialization=serialization)
 
 
 class NoneSchema(TypedDict, total=False):
     type: Required[Literal['none']]
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
-def none_schema(*, ref: str | None = None, extra: Any = None, serialization: SerSchema | None = None) -> NoneSchema:
+def none_schema(*, ref: str | None = None, metadata: Any = None, serialization: SerSchema | None = None) -> NoneSchema:
     """
     Returns a schema that matches a None value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
     schema = core_schema.none_schema()
     v = SchemaValidator(schema)
     assert v.validate_python(None) is None
     ```
 
     Args:
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
-    return dict_not_none(type='none', ref=ref, extra=extra, serialization=serialization)
+    return dict_not_none(type='none', ref=ref, metadata=metadata, serialization=serialization)
 
 
 class BoolSchema(TypedDict, total=False):
     type: Required[Literal['bool']]
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def bool_schema(
-    strict: bool | None = None, ref: str | None = None, extra: Any = None, serialization: SerSchema | None = None
+    strict: bool | None = None, ref: str | None = None, metadata: Any = None, serialization: SerSchema | None = None
 ) -> BoolSchema:
     """
     Returns a schema that matches a bool value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
     schema = core_schema.bool_schema()
     v = SchemaValidator(schema)
     assert v.validate_python('True') is True
     ```
 
     Args:
         strict: Whether the value should be a bool or a value that can be converted to a bool
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
-    return dict_not_none(type='bool', strict=strict, ref=ref, extra=extra, serialization=serialization)
+    return dict_not_none(type='bool', strict=strict, ref=ref, metadata=metadata, serialization=serialization)
 
 
 class IntSchema(TypedDict, total=False):
     type: Required[Literal['int']]
     multiple_of: int
     le: int
     ge: int
     lt: int
     gt: int
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def int_schema(
     *,
     multiple_of: int | None = None,
     le: int | None = None,
     ge: int | None = None,
     lt: int | None = None,
     gt: int | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> IntSchema:
     """
     Returns a schema that matches a int value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -402,56 +402,56 @@
         multiple_of: The value must be a multiple of this number
         le: The value must be less than or equal to this number
         ge: The value must be greater than or equal to this number
         lt: The value must be strictly less than this number
         gt: The value must be strictly greater than this number
         strict: Whether the value should be a int or a value that can be converted to a int
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='int',
         multiple_of=multiple_of,
         le=le,
         ge=ge,
         lt=lt,
         gt=gt,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class FloatSchema(TypedDict, total=False):
     type: Required[Literal['float']]
     allow_inf_nan: bool  # whether 'NaN', '+inf', '-inf' should be forbidden. default: True
     multiple_of: float
     le: float
     ge: float
     lt: float
     gt: float
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def float_schema(
     *,
     allow_inf_nan: bool | None = None,
     multiple_of: float | None = None,
     le: float | None = None,
     ge: float | None = None,
     lt: float | None = None,
     gt: float | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> FloatSchema:
     """
     Returns a schema that matches a float value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -465,57 +465,57 @@
         multiple_of: The value must be a multiple of this number
         le: The value must be less than or equal to this number
         ge: The value must be greater than or equal to this number
         lt: The value must be strictly less than this number
         gt: The value must be strictly greater than this number
         strict: Whether the value should be a float or a value that can be converted to a float
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='float',
         allow_inf_nan=allow_inf_nan,
         multiple_of=multiple_of,
         le=le,
         ge=ge,
         lt=lt,
         gt=gt,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class StringSchema(TypedDict, total=False):
     type: Required[Literal['str']]
     pattern: str
     max_length: int
     min_length: int
     strip_whitespace: bool
     to_lower: bool
     to_upper: bool
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def str_schema(
     *,
     pattern: str | None = None,
     max_length: int | None = None,
     min_length: int | None = None,
     strip_whitespace: bool | None = None,
     to_lower: bool | None = None,
     to_upper: bool | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> StringSchema:
     """
     Returns a schema that matches a string value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -529,49 +529,49 @@
         max_length: The value must be at most this length
         min_length: The value must be at least this length
         strip_whitespace: Whether to strip whitespace from the value
         to_lower: Whether to convert the value to lowercase
         to_upper: Whether to convert the value to uppercase
         strict: Whether the value should be a string or a value that can be converted to a string
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='str',
         pattern=pattern,
         max_length=max_length,
         min_length=min_length,
         strip_whitespace=strip_whitespace,
         to_lower=to_lower,
         to_upper=to_upper,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class BytesSchema(TypedDict, total=False):
     type: Required[Literal['bytes']]
     max_length: int
     min_length: int
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def bytes_schema(
     *,
     max_length: int | None = None,
     min_length: int | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> BytesSchema:
     """
     Returns a schema that matches a bytes value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -581,24 +581,24 @@
     ```
 
     Args:
         max_length: The value must be at most this length
         min_length: The value must be at least this length
         strict: Whether the value should be a bytes or a value that can be converted to a bytes
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='bytes',
         max_length=max_length,
         min_length=min_length,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class DateSchema(TypedDict, total=False):
     type: Required[Literal['date']]
     strict: bool
@@ -607,29 +607,29 @@
     lt: date
     gt: date
     now_op: Literal['past', 'future']
     # defaults to current local utc offset from `time.localtime().tm_gmtoff`
     # value is restricted to -86_400 < offset < 86_400 by bounds in generate_self_schema.py
     now_utc_offset: int
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def date_schema(
     *,
     strict: bool | None = None,
     le: date | None = None,
     ge: date | None = None,
     lt: date | None = None,
     gt: date | None = None,
     now_op: Literal['past', 'future'] | None = None,
     now_utc_offset: int | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> DateSchema:
     """
     Returns a schema that matches a date value, e.g.:
 
     ```py
     from datetime import date
@@ -644,53 +644,53 @@
         le: The value must be less than or equal to this date
         ge: The value must be greater than or equal to this date
         lt: The value must be strictly less than this date
         gt: The value must be strictly greater than this date
         now_op: The value must be in the past or future relative to the current date
         now_utc_offset: The value must be in the past or future relative to the current date with this utc offset
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='date',
         strict=strict,
         le=le,
         ge=ge,
         lt=lt,
         gt=gt,
         now_op=now_op,
         now_utc_offset=now_utc_offset,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class TimeSchema(TypedDict, total=False):
     type: Required[Literal['time']]
     strict: bool
     le: time
     ge: time
     lt: time
     gt: time
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def time_schema(
     *,
     strict: bool | None = None,
     le: time | None = None,
     ge: time | None = None,
     lt: time | None = None,
     gt: time | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> TimeSchema:
     """
     Returns a schema that matches a time value, e.g.:
 
     ```py
     from datetime import time
@@ -703,19 +703,19 @@
     Args:
         strict: Whether the value should be a time or a value that can be converted to a time
         le: The value must be less than or equal to this time
         ge: The value must be greater than or equal to this time
         lt: The value must be strictly less than this time
         gt: The value must be strictly greater than this time
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
-        type='time', strict=strict, le=le, ge=ge, lt=lt, gt=gt, ref=ref, extra=extra, serialization=serialization
+        type='time', strict=strict, le=le, ge=ge, lt=lt, gt=gt, ref=ref, metadata=metadata, serialization=serialization
     )
 
 
 class DatetimeSchema(TypedDict, total=False):
     type: Required[Literal['datetime']]
     strict: bool
     le: datetime
@@ -724,30 +724,30 @@
     gt: datetime
     now_op: Literal['past', 'future']
     tz_constraint: Literal['aware', 'naive']
     # defaults to current local utc offset from `time.localtime().tm_gmtoff`
     # value is restricted to -86_400 < offset < 86_400 by bounds in generate_self_schema.py
     now_utc_offset: int
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def datetime_schema(
     *,
     strict: bool | None = None,
     le: datetime | None = None,
     ge: datetime | None = None,
     lt: datetime | None = None,
     gt: datetime | None = None,
     now_op: Literal['past', 'future'] | None = None,
     tz_constraint: Literal['aware', 'naive'] | None = None,
     now_utc_offset: int | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> DatetimeSchema:
     """
     Returns a schema that matches a datetime value, e.g.:
 
     ```py
     from datetime import datetime
@@ -764,54 +764,54 @@
         ge: The value must be greater than or equal to this datetime
         lt: The value must be strictly less than this datetime
         gt: The value must be strictly greater than this datetime
         now_op: The value must be in the past or future relative to the current datetime
         tz_constraint: The value must be timezone aware or naive
         now_utc_offset: The value must be in the past or future relative to the current datetime with this utc offset
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='datetime',
         strict=strict,
         le=le,
         ge=ge,
         lt=lt,
         gt=gt,
         now_op=now_op,
         tz_constraint=tz_constraint,
         now_utc_offset=now_utc_offset,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class TimedeltaSchema(TypedDict, total=False):
     type: Required[Literal['timedelta']]
     strict: bool
     le: timedelta
     ge: timedelta
     lt: timedelta
     gt: timedelta
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def timedelta_schema(
     *,
     strict: bool | None = None,
     le: timedelta | None = None,
     ge: timedelta | None = None,
     lt: timedelta | None = None,
     gt: timedelta | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> TimedeltaSchema:
     """
     Returns a schema that matches a timedelta value, e.g.:
 
     ```py
     from datetime import timedelta
@@ -824,75 +824,83 @@
     Args:
         strict: Whether the value should be a timedelta or a value that can be converted to a timedelta
         le: The value must be less than or equal to this timedelta
         ge: The value must be greater than or equal to this timedelta
         lt: The value must be strictly less than this timedelta
         gt: The value must be strictly greater than this timedelta
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
-        type='timedelta', strict=strict, le=le, ge=ge, lt=lt, gt=gt, ref=ref, extra=extra, serialization=serialization
+        type='timedelta',
+        strict=strict,
+        le=le,
+        ge=ge,
+        lt=lt,
+        gt=gt,
+        ref=ref,
+        metadata=metadata,
+        serialization=serialization,
     )
 
 
 class LiteralSchema(TypedDict, total=False):
     type: Required[Literal['literal']]
     expected: Required[List[Any]]
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def literal_schema(
-    *expected: Any, ref: str | None = None, extra: Any = None, serialization: SerSchema | None = None
+    *expected: Any, ref: str | None = None, metadata: Any = None, serialization: SerSchema | None = None
 ) -> LiteralSchema:
     """
     Returns a schema that matches a literal value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
     schema = core_schema.literal_schema('hello', "world")
     v = SchemaValidator(schema)
     assert v.validate_python('hello') == 'hello'
     ```
 
     Args:
         expected: The value must be one of these values
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
-    return dict_not_none(type='literal', expected=expected, ref=ref, extra=extra, serialization=serialization)
+    return dict_not_none(type='literal', expected=expected, ref=ref, metadata=metadata, serialization=serialization)
 
 
 # must match input/parse_json.rs::JsonType::try_from
 JsonType = Literal['null', 'bool', 'int', 'float', 'str', 'list', 'dict']
 
 
 class IsInstanceSchema(TypedDict, total=False):
     type: Required[Literal['is-instance']]
     cls: Required[Any]
     cls_repr: str
     json_types: Set[JsonType]
     json_function: Callable[[Any], Any]
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def is_instance_schema(
     cls: Any,
     *,
     json_types: Set[JsonType] | None = None,
     json_function: Callable[[Any], Any] | None = None,
     cls_repr: str | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> IsInstanceSchema:
     """
     Returns a schema that checks if a value is an instance of a class, equivalent to python's `isinstnace` method, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -908,44 +916,44 @@
     Args:
         cls: The value must be an instance of this class
         json_types: When parsing JSON directly, the value must be one of these json types
         json_function: When parsing JSON directly, If provided, the JSON value is passed to this
             function and the return value used as the output value
         cls_repr: If provided this string is used in the validator name instead of `repr(cls)`
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='is-instance',
         cls=cls,
         json_types=json_types,
         json_function=json_function,
         cls_repr=cls_repr,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class IsSubclassSchema(TypedDict, total=False):
     type: Required[Literal['is-subclass']]
     cls: Required[Type[Any]]
     cls_repr: str
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def is_subclass_schema(
     cls: Type[Any],
     *,
     cls_repr: str | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> IsInstanceSchema:
     """
     Returns a schema that checks if a value is a subtype of a class, equivalent to python's `issubclass` method, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -961,48 +969,48 @@
     v.validate_python(B)
     ```
 
     Args:
         cls: The value must be a subclass of this class
         cls_repr: If provided this string is used in the validator name instead of `repr(cls)`
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
-        type='is-subclass', cls=cls, cls_repr=cls_repr, ref=ref, extra=extra, serialization=serialization
+        type='is-subclass', cls=cls, cls_repr=cls_repr, ref=ref, metadata=metadata, serialization=serialization
     )
 
 
 class CallableSchema(TypedDict, total=False):
     type: Required[Literal['callable']]
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def callable_schema(
-    *, ref: str | None = None, extra: Any = None, serialization: SerSchema | None = None
+    *, ref: str | None = None, metadata: Any = None, serialization: SerSchema | None = None
 ) -> CallableSchema:
     """
     Returns a schema that checks if a value is callable, equivalent to python's `callable` method, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
     schema = core_schema.callable_schema()
     v = SchemaValidator(schema)
     v.validate_python(min)
     ```
 
     Args:
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
-    return dict_not_none(type='callable', ref=ref, extra=extra, serialization=serialization)
+    return dict_not_none(type='callable', ref=ref, metadata=metadata, serialization=serialization)
 
 
 class IncExSeqSerSchema(TypedDict, total=False):
     type: Required[Literal['include-exclude-sequence']]
     include: Set[int]
     exclude: Set[int]
 
@@ -1018,27 +1026,27 @@
     type: Required[Literal['list']]
     items_schema: CoreSchema
     min_length: int
     max_length: int
     strict: bool
     allow_any_iter: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: IncExSeqOrElseSerSchema
 
 
 def list_schema(
     items_schema: CoreSchema | None = None,
     *,
     min_length: int | None = None,
     max_length: int | None = None,
     strict: bool | None = None,
     allow_any_iter: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: IncExSeqOrElseSerSchema | None = None,
 ) -> ListSchema:
     """
     Returns a schema that matches a list value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -1050,47 +1058,47 @@
     Args:
         items_schema: The value must be a list of items that match this schema
         min_length: The value must be a list with at least this many items
         max_length: The value must be a list with at most this many items
         strict: The value must be a list with exactly this many items
         allow_any_iter: Whether the value can be any iterable
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='list',
         items_schema=items_schema,
         min_length=min_length,
         max_length=max_length,
         strict=strict,
         allow_any_iter=allow_any_iter,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class TuplePositionalSchema(TypedDict, total=False):
     type: Required[Literal['tuple']]
     mode: Required[Literal['positional']]
     items_schema: Required[List[CoreSchema]]
     extra_schema: CoreSchema
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: IncExSeqOrElseSerSchema
 
 
 def tuple_positional_schema(
     *items_schema: CoreSchema,
     extra_schema: CoreSchema | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: IncExSeqOrElseSerSchema | None = None,
 ) -> TuplePositionalSchema:
     """
     Returns a schema that matches a tuple of schemas, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -1100,49 +1108,49 @@
     ```
 
     Args:
         items_schema: The value must be a tuple with items that match these schemas
         extra_schema: The value must be a tuple with items that match this schema
         strict: The value must be a tuple with exactly this many items
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='tuple',
         mode='positional',
         items_schema=items_schema,
         extra_schema=extra_schema,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class TupleVariableSchema(TypedDict, total=False):
     type: Required[Literal['tuple']]
     mode: Literal['variable']
     items_schema: CoreSchema
     min_length: int
     max_length: int
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: IncExSeqOrElseSerSchema
 
 
 def tuple_variable_schema(
     items_schema: CoreSchema | None = None,
     *,
     min_length: int | None = None,
     max_length: int | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: IncExSeqOrElseSerSchema | None = None,
 ) -> TupleVariableSchema:
     """
     Returns a schema that matches a tuple of a given schema, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -1153,51 +1161,51 @@
 
     Args:
         items_schema: The value must be a tuple with items that match this schema
         min_length: The value must be a tuple with at least this many items
         max_length: The value must be a tuple with at most this many items
         strict: The value must be a tuple with exactly this many items
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='tuple',
         mode='variable',
         items_schema=items_schema,
         min_length=min_length,
         max_length=max_length,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class SetSchema(TypedDict, total=False):
     type: Required[Literal['set']]
     items_schema: CoreSchema
     min_length: int
     max_length: int
     generator_max_length: int
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def set_schema(
     items_schema: CoreSchema | None = None,
     *,
     min_length: int | None = None,
     max_length: int | None = None,
     generator_max_length: int | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> SetSchema:
     """
     Returns a schema that matches a set of a given schema, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -1209,51 +1217,51 @@
     Args:
         items_schema: The value must be a set with items that match this schema
         min_length: The value must be a set with at least this many items
         max_length: The value must be a set with at most this many items
         generator_max_length: The value must be a set with at most this many items
         strict: The value must be a set with exactly this many items
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='set',
         items_schema=items_schema,
         min_length=min_length,
         max_length=max_length,
         generator_max_length=generator_max_length,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class FrozenSetSchema(TypedDict, total=False):
     type: Required[Literal['frozenset']]
     items_schema: CoreSchema
     min_length: int
     max_length: int
     generator_max_length: int
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def frozenset_schema(
     items_schema: CoreSchema | None = None,
     *,
     min_length: int | None = None,
     max_length: int | None = None,
     generator_max_length: int | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> FrozenSetSchema:
     """
     Returns a schema that matches a frozenset of a given schema, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -1265,45 +1273,45 @@
     Args:
         items_schema: The value must be a frozenset with items that match this schema
         min_length: The value must be a frozenset with at least this many items
         max_length: The value must be a frozenset with at most this many items
         generator_max_length: The value must generate a frozenset with at most this many items
         strict: The value must be a frozenset with exactly this many items
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='frozenset',
         items_schema=items_schema,
         min_length=min_length,
         max_length=max_length,
         generator_max_length=generator_max_length,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class GeneratorSchema(TypedDict, total=False):
     type: Required[Literal['generator']]
     items_schema: CoreSchema
     max_length: int
     ref: str
-    extra: Any
+    metadata: Any
     serialization: IncExSeqOrElseSerSchema
 
 
 def generator_schema(
     items_schema: CoreSchema | None = None,
     *,
     max_length: int | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: IncExSeqOrElseSerSchema | None = None,
 ) -> GeneratorSchema:
     """
     Returns a schema that matches a generator value, e.g.:
 
     ```py
     from typing import Iterator
@@ -1317,23 +1325,23 @@
     v.validate_python(gen())
     ```
 
     Args:
         items_schema: The value must be a generator with items that match this schema
         max_length: The value must be a generator that yields at most this many items
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='generator',
         items_schema=items_schema,
         max_length=max_length,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 IncExDict = Set[Union[int, str]]
 
 
@@ -1354,27 +1362,27 @@
     type: Required[Literal['dict']]
     keys_schema: CoreSchema  # default: AnySchema
     values_schema: CoreSchema  # default: AnySchema
     min_length: int
     max_length: int
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: IncExDictOrElseSerSchema
 
 
 def dict_schema(
     keys_schema: CoreSchema | None = None,
     values_schema: CoreSchema | None = None,
     *,
     min_length: int | None = None,
     max_length: int | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> DictSchema:
     """
     Returns a schema that matches a dict value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -1388,26 +1396,26 @@
     Args:
         keys_schema: The value must be a dict with keys that match this schema
         values_schema: The value must be a dict with values that match this schema
         min_length: The value must be a dict with at least this many items
         max_length: The value must be a dict with at most this many items
         strict: Whether the keys and values should be validated with strict mode
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='dict',
         keys_schema=keys_schema,
         values_schema=values_schema,
         min_length=min_length,
         max_length=max_length,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class ValidatorFunction(Protocol):
     def __call__(
         self, __input_value: Any, *, data: Any, config: CoreConfig | None, context: Any, **future_kwargs: Any
@@ -1417,24 +1425,24 @@
 
 class FunctionSchema(TypedDict, total=False):
     type: Required[Literal['function']]
     mode: Required[Literal['before', 'after']]
     function: Required[ValidatorFunction]
     schema: Required[CoreSchema]
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def function_before_schema(
     function: ValidatorFunction,
     schema: CoreSchema,
     *,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> FunctionSchema:
     """
     Returns a schema that calls a validator function before validating the provided schema, e.g.:
 
     ```py
     from typing import Any
@@ -1450,34 +1458,34 @@
     assert v.validate_python(b"hello ") == "b'hello 'world"
     ```
 
     Args:
         function: The validator function to call
         schema: The schema to validate the output of the validator function
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='function',
         mode='before',
         function=function,
         schema=schema,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 def function_after_schema(
     schema: CoreSchema,
     function: ValidatorFunction,
     *,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> FunctionSchema:
     """
     Returns a schema that calls a validator function after validating the provided schema, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -1491,24 +1499,24 @@
     assert v.validate_python('hello ') == 'hello world'
     ```
 
     Args:
         schema: The schema to validate before the validator function
         function: The validator function to call after the schema is validated
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='function',
         mode='after',
         function=function,
         schema=schema,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class CallableValidator(Protocol):
     def __call__(self, input_value: Any, outer_location: str | int | None = None) -> Any:  # pragma: no cover
         ...
@@ -1530,24 +1538,24 @@
 
 class FunctionWrapSchema(TypedDict, total=False):
     type: Required[Literal['function']]
     mode: Required[Literal['wrap']]
     function: Required[WrapValidatorFunction]
     schema: Required[CoreSchema]
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def function_wrap_schema(
     function: WrapValidatorFunction,
     schema: CoreSchema,
     *,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> FunctionWrapSchema:
     """
     Returns a schema which calls a function with a `validator` callable argument which can
     optionally be used to call inner validation with the function logic, this is much like the
     "onion" implementation of middleware in many popular web frameworks, e.g.:
 
@@ -1562,39 +1570,39 @@
     assert v.validate_python('hello ') == 'hello world'
     ```
 
     Args:
         function: The validator function to call
         schema: The schema to validate the output of the validator function
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='function',
         mode='wrap',
         function=function,
         schema=schema,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class FunctionPlainSchema(TypedDict, total=False):
     type: Required[Literal['function']]
     mode: Required[Literal['plain']]
     function: Required[ValidatorFunction]
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def function_plain_schema(
-    function: ValidatorFunction, *, ref: str | None = None, extra: Any = None, serialization: SerSchema | None = None
+    function: ValidatorFunction, *, ref: str | None = None, metadata: Any = None, serialization: SerSchema | None = None
 ) -> FunctionPlainSchema:
     """
     Returns a schema that uses the provided function for validation, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
 
@@ -1606,46 +1614,46 @@
     v = SchemaValidator(schema)
     assert v.validate_python("hello ") == 'hello world'
     ```
 
     Args:
         function: The validator function to call
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
-        type='function', mode='plain', function=function, ref=ref, extra=extra, serialization=serialization
+        type='function', mode='plain', function=function, ref=ref, metadata=metadata, serialization=serialization
     )
 
 
 class WithDefaultSchema(TypedDict, total=False):
     type: Required[Literal['default']]
     schema: Required[CoreSchema]
     default: Any
     default_factory: Callable[[], Any]
     on_error: Literal['raise', 'omit', 'default']  # default: 'raise'
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 Omitted = object()
 
 
 def with_default_schema(
     schema: CoreSchema,
     *,
     default: Any = Omitted,
     default_factory: Callable[[], Any] | None = None,
     on_error: Literal['raise', 'omit', 'default'] | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> WithDefaultSchema:
     """
     Returns a schema that adds a default value to the given schema, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -1660,47 +1668,47 @@
     Args:
         schema: The schema to add a default value to
         default: The default value to use
         default_factory: A function that returns the default value to use
         on_error: What to do if the schema validation fails. One of 'raise', 'omit', 'default'
         strict: Whether the underlying schema should be validated with strict mode
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     s = dict_not_none(
         type='default',
         schema=schema,
         default_factory=default_factory,
         on_error=on_error,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
     if default is not Omitted:
         s['default'] = default
     return s
 
 
 class NullableSchema(TypedDict, total=False):
     type: Required[Literal['nullable']]
     schema: Required[CoreSchema]
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def nullable_schema(
     schema: CoreSchema,
     *,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> NullableSchema:
     """
     Returns a schema that matches a nullable value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -1709,45 +1717,45 @@
     assert v.validate_python(None) is None
     ```
 
     Args:
         schema: The schema to wrap
         strict: Whether the underlying schema should be validated with strict mode
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
-        type='nullable', schema=schema, strict=strict, ref=ref, extra=extra, serialization=serialization
+        type='nullable', schema=schema, strict=strict, ref=ref, metadata=metadata, serialization=serialization
     )
 
 
 class UnionSchema(TypedDict, total=False):
     type: Required[Literal['union']]
     choices: Required[List[CoreSchema]]
     # default true, whether to automatically collapse unions with one element to the inner validator
     auto_collapse: bool
     custom_error_type: str
     custom_error_message: str
     custom_error_context: Dict[str, Union[str, int, float]]
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def union_schema(
     *choices: CoreSchema,
     auto_collapse: bool | None = None,
     custom_error_type: str | None = None,
     custom_error_message: str | None = None,
     custom_error_context: dict[str, str | int] | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> UnionSchema:
     """
     Returns a schema that matches a union value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -1761,27 +1769,27 @@
         *choices: The schemas to match
         auto_collapse: whether to automatically collapse unions with one element to the inner validator, default true
         custom_error_type: The custom error type to use if the validation fails
         custom_error_message: The custom error message to use if the validation fails
         custom_error_context: The custom error context to use if the validation fails
         strict: Whether the underlying schemas should be validated with strict mode
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='union',
         choices=choices,
         auto_collapse=auto_collapse,
         custom_error_type=custom_error_type,
         custom_error_message=custom_error_message,
         custom_error_context=custom_error_context,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class TaggedUnionSchema(TypedDict, total=False):
     type: Required[Literal['tagged-union']]
     choices: Required[Dict[str, Union[str, CoreSchema]]]
@@ -1789,28 +1797,28 @@
         Union[str, List[Union[str, int]], List[List[Union[str, int]]], Callable[[Any], Optional[str]]]
     ]
     custom_error_type: str
     custom_error_message: str
     custom_error_context: Dict[str, Union[str, int, float]]
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def tagged_union_schema(
     choices: Dict[str, str | CoreSchema],
     discriminator: str | list[str | int] | list[list[str | int]] | Callable[[Any], str | None],
     *,
     custom_error_type: str | None = None,
     custom_error_message: str | None = None,
     custom_error_context: dict[str, int | str | float] | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> TaggedUnionSchema:
     """
     Returns a schema that matches a tagged union value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -1842,41 +1850,41 @@
         choices: The schemas to match
         discriminator: The discriminator to use to determine the schema to use
         custom_error_type: The custom error type to use if the validation fails
         custom_error_message: The custom error message to use if the validation fails
         custom_error_context: The custom error context to use if the validation fails
         strict: Whether the underlying schemas should be validated with strict mode
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='tagged-union',
         choices=choices,
         discriminator=discriminator,
         custom_error_type=custom_error_type,
         custom_error_message=custom_error_message,
         custom_error_context=custom_error_context,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class ChainSchema(TypedDict, total=False):
     type: Required[Literal['chain']]
     steps: Required[List[CoreSchema]]
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def chain_schema(
-    *steps: CoreSchema, ref: str | None = None, extra: Any = None, serialization: SerSchema | None = None
+    *steps: CoreSchema, ref: str | None = None, metadata: Any = None, serialization: SerSchema | None = None
 ) -> ChainSchema:
     """
     Returns a schema that chains the provided validation schemas, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
 
@@ -1889,37 +1897,37 @@
     v = SchemaValidator(schema)
     assert v.validate_python("hello") == 'hello world world world'
     ```
 
     Args:
         steps: The schemas to chain
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
-    return dict_not_none(type='chain', steps=steps, ref=ref, extra=extra, serialization=serialization)
+    return dict_not_none(type='chain', steps=steps, ref=ref, metadata=metadata, serialization=serialization)
 
 
 class LaxOrStrictSchema(TypedDict, total=False):
     type: Required[Literal['lax-or-strict']]
     lax_schema: Required[CoreSchema]
     strict_schema: Required[CoreSchema]
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def lax_or_strict_schema(
     lax_schema: CoreSchema,
     strict_schema: CoreSchema,
     *,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> LaxOrStrictSchema:
     """
     Returns a schema that uses the lax or strict schema, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -1941,45 +1949,47 @@
     ```
 
     Args:
         lax_schema: The lax schema to use
         strict_schema: The strict schema to use
         strict: Whether the strict schema should be used
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='lax-or-strict',
         lax_schema=lax_schema,
         strict_schema=strict_schema,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class TypedDictField(TypedDict, total=False):
     schema: Required[CoreSchema]
     required: bool
     validation_alias: Union[str, List[Union[str, int]], List[List[Union[str, int]]]]
     serialization_alias: str
     serialization_exclude: bool  # default: False
     frozen: bool
+    metadata: Any
 
 
 def typed_dict_field(
     schema: CoreSchema,
     *,
     required: bool | None = None,
     validation_alias: str | list[str | int] | list[list[str | int]] | None = None,
     serialization_alias: str | None = None,
     serialization_exclude: bool | None = None,
     frozen: bool | None = None,
+    metadata: Any = None,
 ) -> TypedDictField:
     """
     Returns a schema that matches a typed dict field, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
     field = core_schema.typed_dict_field(schema=core_schema.int_schema(), required=True)
@@ -1994,14 +2004,15 @@
     return dict_not_none(
         schema=schema,
         required=required,
         validation_alias=validation_alias,
         serialization_alias=serialization_alias,
         serialization_exclude=serialization_exclude,
         frozen=frozen,
+        metadata=metadata,
     )
 
 
 class TypedDictSchema(TypedDict, total=False):
     type: Required[Literal['typed-dict']]
     fields: Required[Dict[str, TypedDictField]]
     strict: bool
@@ -2009,30 +2020,30 @@
     return_fields_set: bool
     # all these values can be set via config, equivalent fields have `typed_dict_` prefix
     extra_behavior: Literal['allow', 'forbid', 'ignore']
     total: bool  # default: True
     populate_by_name: bool  # replaces `allow_population_by_field_name` in pydantic v1
     from_attributes: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def typed_dict_schema(
     fields: Dict[str, TypedDictField],
     *,
     strict: bool | None = None,
     extra_validator: CoreSchema | None = None,
     return_fields_set: bool | None = None,
     extra_behavior: Literal['allow', 'forbid', 'ignore'] | None = None,
     total: bool | None = None,
     populate_by_name: bool | None = None,
     from_attributes: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> TypedDictSchema:
     """
     Returns a schema that matches a typed dict, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -2045,15 +2056,15 @@
 
     Args:
         fields: The fields to use for the typed dict
         strict: Whether the typed dict is strict
         extra_validator: The extra validator to use for the typed dict
         return_fields_set: Whether the typed dict should return a fields set
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         extra_behavior: The extra behavior to use for the typed dict
         total: Whether the typed dict is total
         populate_by_name: Whether the typed dict should populate by name
         from_attributes: Whether the typed dict should be populated from attributes
     """
     return dict_not_none(
         type='typed-dict',
@@ -2062,40 +2073,40 @@
         extra_validator=extra_validator,
         return_fields_set=return_fields_set,
         extra_behavior=extra_behavior,
         total=total,
         populate_by_name=populate_by_name,
         from_attributes=from_attributes,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class ModelSchema(TypedDict, total=False):
     type: Required[Literal['model']]
     cls: Required[Type[Any]]
     schema: Required[CoreSchema]
     call_after_init: str
     strict: bool
     config: CoreConfig
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def model_schema(
     cls: Type[Any],
     schema: CoreSchema,
     *,
     call_after_init: str | None = None,
     strict: bool | None = None,
     config: CoreConfig | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> ModelSchema:
     """
     A model schema generally contains a typed-dict schema.
     It will run the typed dict validator, then create a new class
     and set the dict and fields set returned from the typed dict validator
     to `__dict__` and `__fields_set__` respectively.
@@ -2123,26 +2134,26 @@
     Args:
         cls: The class to use for the model
         schema: The schema to use for the model
         call_after_init: The call after init to use for the model
         strict: Whether the model is strict
         config: The config to use for the model
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='model',
         cls=cls,
         schema=schema,
         call_after_init=call_after_init,
         strict=strict,
         config=config,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class ArgumentsParameter(TypedDict, total=False):
     name: Required[str]
     schema: Required[CoreSchema]
@@ -2177,25 +2188,25 @@
 class ArgumentsSchema(TypedDict, total=False):
     type: Required[Literal['arguments']]
     arguments_schema: Required[List[ArgumentsParameter]]
     populate_by_name: bool
     var_args_schema: CoreSchema
     var_kwargs_schema: CoreSchema
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def arguments_schema(
     *arguments: ArgumentsParameter,
     populate_by_name: bool | None = None,
     var_args_schema: CoreSchema | None = None,
     var_kwargs_schema: CoreSchema | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> ArgumentsSchema:
     """
     Returns a schema that matches an arguments schema, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -2208,46 +2219,46 @@
 
     Args:
         arguments: The arguments to use for the arguments schema
         populate_by_name: Whether to populate by name
         var_args_schema: The variable args schema to use for the arguments schema
         var_kwargs_schema: The variable kwargs schema to use for the arguments schema
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='arguments',
         arguments_schema=arguments,
         populate_by_name=populate_by_name,
         var_args_schema=var_args_schema,
         var_kwargs_schema=var_kwargs_schema,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class CallSchema(TypedDict, total=False):
     type: Required[Literal['call']]
     arguments_schema: Required[CoreSchema]
     function: Required[Callable[..., Any]]
     return_schema: CoreSchema
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def call_schema(
     arguments: CoreSchema,
     function: Callable[..., Any],
     *,
     return_schema: CoreSchema | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> CallSchema:
     """
     Returns a schema that matches an arguments schema, then calls a function, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -2265,76 +2276,76 @@
     ```
 
     Args:
         arguments: The arguments to use for the arguments schema
         function: The function to use for the call schema
         return_schema: The return schema to use for the call schema
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='call',
         arguments_schema=arguments,
         function=function,
         return_schema=return_schema,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class RecursiveReferenceSchema(TypedDict, total=False):
     type: Required[Literal['recursive-ref']]
     schema_ref: Required[str]
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def recursive_reference_schema(
-    schema_ref: str, extra: Any = None, serialization: SerSchema | None = None
+    schema_ref: str, metadata: Any = None, serialization: SerSchema | None = None
 ) -> RecursiveReferenceSchema:
     """
     Returns a schema that matches a recursive reference value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
     schema_recursive = core_schema.recursive_reference_schema('list-schema')
     schema = core_schema.list_schema(items_schema=schema_recursive, ref='list-schema')
     v = SchemaValidator(schema)
     assert v.validate_python([[]]) == [[]]
     ```
 
     Args:
         schema_ref: The schema ref to use for the recursive reference schema
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
-    return dict_not_none(type='recursive-ref', schema_ref=schema_ref, extra=extra, serialization=serialization)
+    return dict_not_none(type='recursive-ref', schema_ref=schema_ref, metadata=metadata, serialization=serialization)
 
 
 class CustomErrorSchema(TypedDict, total=False):
     type: Required[Literal['custom-error']]
     schema: Required[CoreSchema]
     custom_error_type: Required[str]
     custom_error_message: str
     custom_error_context: Dict[str, Union[str, int, float]]
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def custom_error_schema(
     schema: CoreSchema,
     custom_error_type: str,
     *,
     custom_error_message: str | None = None,
     custom_error_context: dict[str, str | int | float] | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> CustomErrorSchema:
     """
     Returns a schema that matches a custom error value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -2347,42 +2358,42 @@
 
     Args:
         schema: The schema to use for the custom error schema
         custom_error_type: The custom error type to use for the custom error schema
         custom_error_message: The custom error message to use for the custom error schema
         custom_error_context: The custom error context to use for the custom error schema
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='custom-error',
         schema=schema,
         custom_error_type=custom_error_type,
         custom_error_message=custom_error_message,
         custom_error_context=custom_error_context,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class JsonSchema(TypedDict, total=False):
     type: Required[Literal['json']]
     schema: CoreSchema
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def json_schema(
     schema: CoreSchema | None = None,
     *,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> JsonSchema:
     """
     Returns a schema that matches a JSON value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -2404,45 +2415,45 @@
     m = v.validate_python('{"field_a": "hello", "field_b": true}')
     assert isinstance(m, MyModel)
     ```
 
     Args:
         schema: The schema to use for the JSON schema
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
-    return dict_not_none(type='json', schema=schema, ref=ref, extra=extra, serialization=serialization)
+    return dict_not_none(type='json', schema=schema, ref=ref, metadata=metadata, serialization=serialization)
 
 
 class UrlSchema(TypedDict, total=False):
     type: Required[Literal['url']]
     max_length: int
     allowed_schemes: List[str]
     host_required: bool  # default False
     default_host: str
     default_port: int
     default_path: str
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def url_schema(
     *,
     max_length: int | None = None,
     allowed_schemes: list[str] | None = None,
     host_required: bool | None = None,
     default_host: str | None = None,
     default_port: int | None = None,
     default_path: str | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> UrlSchema:
     """
     Returns a schema that matches a URL value, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -2457,57 +2468,57 @@
         allowed_schemes: The allowed URL schemes
         host_required: Whether the URL must have a host
         default_host: The default host to use if the URL does not have a host
         default_port: The default port to use if the URL does not have a port
         default_path: The default path to use if the URL does not have a path
         strict: Whether to use strict URL parsing
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='url',
         max_length=max_length,
         allowed_schemes=allowed_schemes,
         host_required=host_required,
         default_host=default_host,
         default_port=default_port,
         default_path=default_path,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 class MultiHostUrlSchema(TypedDict, total=False):
     type: Required[Literal['multi-host-url']]
     max_length: int
     allowed_schemes: List[str]
     host_required: bool  # default False
     default_host: str
     default_port: int
     default_path: str
     strict: bool
     ref: str
-    extra: Any
+    metadata: Any
     serialization: SerSchema
 
 
 def multi_host_url_schema(
     *,
     max_length: int | None = None,
     allowed_schemes: list[str] | None = None,
     host_required: bool | None = None,
     default_host: str | None = None,
     default_port: int | None = None,
     default_path: str | None = None,
     strict: bool | None = None,
     ref: str | None = None,
-    extra: Any = None,
+    metadata: Any = None,
     serialization: SerSchema | None = None,
 ) -> MultiHostUrlSchema:
     """
     Returns a schema that matches a URL value with possibly multiple hosts, e.g.:
 
     ```py
     from pydantic_core import SchemaValidator, core_schema
@@ -2522,28 +2533,28 @@
         allowed_schemes: The allowed URL schemes
         host_required: Whether the URL must have a host
         default_host: The default host to use if the URL does not have a host
         default_port: The default port to use if the URL does not have a port
         default_path: The default path to use if the URL does not have a path
         strict: Whether to use strict URL parsing
         ref: See [TODO] for details
-        extra: See [TODO] for details
+        metadata: See [TODO] for details
         serialization: Custom serialization schema
     """
     return dict_not_none(
         type='multi-host-url',
         max_length=max_length,
         allowed_schemes=allowed_schemes,
         host_required=host_required,
         default_host=default_host,
         default_port=default_port,
         default_path=default_path,
         strict=strict,
         ref=ref,
-        extra=extra,
+        metadata=metadata,
         serialization=serialization,
     )
 
 
 CoreSchema = Union[
     AnySchema,
     NoneSchema,
@@ -2583,14 +2594,56 @@
     RecursiveReferenceSchema,
     CustomErrorSchema,
     JsonSchema,
     UrlSchema,
     MultiHostUrlSchema,
 ]
 
+# to update this, call `pytest -k test_core_schema_type_literal` and copy the output
+CoreSchemaType = Literal[
+    'any',
+    'none',
+    'bool',
+    'int',
+    'float',
+    'str',
+    'bytes',
+    'date',
+    'time',
+    'datetime',
+    'timedelta',
+    'literal',
+    'is-instance',
+    'is-subclass',
+    'callable',
+    'list',
+    'tuple',
+    'set',
+    'frozenset',
+    'generator',
+    'dict',
+    'function',
+    'default',
+    'nullable',
+    'union',
+    'tagged-union',
+    'chain',
+    'lax-or-strict',
+    'typed-dict',
+    'model',
+    'arguments',
+    'call',
+    'recursive-ref',
+    'custom-error',
+    'json',
+    'url',
+    'multi-host-url',
+]
+
+
 # used in _pydantic_core.pyi::PydanticKnownError
 # to update this, call `pytest -k test_all_errors` and copy the output
 ErrorType = Literal[
     'json_invalid',
     'json_type',
     'recursion_loop',
     'dict_attributes_type',
```

### Comparing `pydantic_core-0.8.2/pyproject.toml` & `pydantic_core-0.9.0/pyproject.toml`

 * *Files 11% similar despite different names*

```diff
@@ -6,32 +6,31 @@
 name = 'pydantic_core'
 requires-python = '>=3.7'
 authors = [
     {name = 'Samuel Colvin', email = 's@muelcolvin.com'}
 ]
 classifiers = [
     'Development Status :: 3 - Alpha',
-    'Environment :: Console',
     'Programming Language :: Python',
     'Programming Language :: Python :: 3',
     'Programming Language :: Python :: 3 :: Only',
     'Programming Language :: Python :: 3.7',
     'Programming Language :: Python :: 3.8',
     'Programming Language :: Python :: 3.9',
     'Programming Language :: Python :: 3.10',
     'Programming Language :: Python :: 3.11',
+    'Programming Language :: Rust',
+    'Framework :: Pydantic',
     'Intended Audience :: Developers',
     'Intended Audience :: Information Technology',
-    'Intended Audience :: System Administrators',
     'License :: OSI Approved :: MIT License',
     'Operating System :: POSIX :: Linux',
     'Operating System :: Microsoft :: Windows',
     'Operating System :: MacOS',
-    'Environment :: MacOS X',
-    'Topic :: Software Development :: Libraries :: Python Modules',
+    'Typing :: Typed',
 ]
 dependencies = [
     'typing_extensions; python_version < "3.11.0"'
 ]
 dynamic = [
     'description',
     'license',
```

### Comparing `pydantic_core-0.8.2/src/build_context.rs` & `pydantic_core-0.9.0/src/build_context.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/build_tools.rs` & `pydantic_core-0.9.0/src/build_tools.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/errors/line_error.rs` & `pydantic_core-0.9.0/src/errors/line_error.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/errors/location.rs` & `pydantic_core-0.9.0/src/errors/location.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/errors/mod.rs` & `pydantic_core-0.9.0/src/errors/mod.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/errors/types.rs` & `pydantic_core-0.9.0/src/errors/types.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/errors/validation_exception.rs` & `pydantic_core-0.9.0/src/errors/validation_exception.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/errors/value_exception.rs` & `pydantic_core-0.9.0/src/errors/value_exception.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/input/datetime.rs` & `pydantic_core-0.9.0/src/input/datetime.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/input/input_abstract.rs` & `pydantic_core-0.9.0/src/input/input_abstract.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/input/input_json.rs` & `pydantic_core-0.9.0/src/input/input_json.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/input/input_python.rs` & `pydantic_core-0.9.0/src/input/input_python.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/input/mod.rs` & `pydantic_core-0.9.0/src/input/mod.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/input/parse_json.rs` & `pydantic_core-0.9.0/src/input/parse_json.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/input/return_enums.rs` & `pydantic_core-0.9.0/src/input/return_enums.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/input/shared.rs` & `pydantic_core-0.9.0/src/input/shared.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/lib.rs` & `pydantic_core-0.9.0/src/lib.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/lookup_key.rs` & `pydantic_core-0.9.0/src/lookup_key.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/questions.rs` & `pydantic_core-0.9.0/src/questions.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/recursion_guard.rs` & `pydantic_core-0.9.0/src/recursion_guard.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/config.rs` & `pydantic_core-0.9.0/src/serializers/config.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/errors.rs` & `pydantic_core-0.9.0/src/serializers/errors.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/extra.rs` & `pydantic_core-0.9.0/src/serializers/extra.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/filter.rs` & `pydantic_core-0.9.0/src/serializers/filter.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/infer.rs` & `pydantic_core-0.9.0/src/serializers/infer.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/mod.rs` & `pydantic_core-0.9.0/src/serializers/mod.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/ob_type.rs` & `pydantic_core-0.9.0/src/serializers/ob_type.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/shared.rs` & `pydantic_core-0.9.0/src/serializers/shared.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/any.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/any.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/bytes.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/bytes.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/datetime_etc.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/datetime_etc.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/dict.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/dict.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/format.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/format.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/function.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/function.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/generator.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/generator.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/json.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/json.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/list.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/list.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/literal.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/literal.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/mod.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/mod.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/model.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/model.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/nullable.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/nullable.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/other.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/other.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/recursive.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/recursive.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/set_frozenset.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/set_frozenset.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/simple.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/simple.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/string.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/string.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/timedelta.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/timedelta.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/tuple.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/tuple.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/typed_dict.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/typed_dict.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/union.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/union.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/url.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/url.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/serializers/type_serializers/with_default.rs` & `pydantic_core-0.9.0/src/serializers/type_serializers/with_default.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/url.rs` & `pydantic_core-0.9.0/src/url.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/any.rs` & `pydantic_core-0.9.0/src/validators/any.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/arguments.rs` & `pydantic_core-0.9.0/src/validators/arguments.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/bool.rs` & `pydantic_core-0.9.0/src/validators/bool.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/bytes.rs` & `pydantic_core-0.9.0/src/validators/bytes.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/call.rs` & `pydantic_core-0.9.0/src/validators/call.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/callable.rs` & `pydantic_core-0.9.0/src/validators/callable.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/chain.rs` & `pydantic_core-0.9.0/src/validators/chain.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/custom_error.rs` & `pydantic_core-0.9.0/src/validators/custom_error.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/date.rs` & `pydantic_core-0.9.0/src/validators/date.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/datetime.rs` & `pydantic_core-0.9.0/src/validators/datetime.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/dict.rs` & `pydantic_core-0.9.0/src/validators/dict.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/float.rs` & `pydantic_core-0.9.0/src/validators/float.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/frozenset.rs` & `pydantic_core-0.9.0/src/validators/frozenset.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/function.rs` & `pydantic_core-0.9.0/src/validators/function.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/generator.rs` & `pydantic_core-0.9.0/src/validators/generator.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/int.rs` & `pydantic_core-0.9.0/src/validators/int.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/is_instance.rs` & `pydantic_core-0.9.0/src/validators/is_instance.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/is_subclass.rs` & `pydantic_core-0.9.0/src/validators/is_subclass.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/json.rs` & `pydantic_core-0.9.0/src/validators/json.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/lax_or_strict.rs` & `pydantic_core-0.9.0/src/validators/lax_or_strict.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/list.rs` & `pydantic_core-0.9.0/src/validators/list.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/literal.rs` & `pydantic_core-0.9.0/src/validators/literal.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/mod.rs` & `pydantic_core-0.9.0/src/validators/mod.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/model.rs` & `pydantic_core-0.9.0/src/validators/model.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/none.rs` & `pydantic_core-0.9.0/src/validators/none.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/nullable.rs` & `pydantic_core-0.9.0/src/validators/nullable.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/recursive.rs` & `pydantic_core-0.9.0/src/validators/recursive.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/set.rs` & `pydantic_core-0.9.0/src/validators/set.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/string.rs` & `pydantic_core-0.9.0/src/validators/string.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/time.rs` & `pydantic_core-0.9.0/src/validators/time.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/timedelta.rs` & `pydantic_core-0.9.0/src/validators/timedelta.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/tuple.rs` & `pydantic_core-0.9.0/src/validators/tuple.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/typed_dict.rs` & `pydantic_core-0.9.0/src/validators/typed_dict.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/union.rs` & `pydantic_core-0.9.0/src/validators/union.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/url.rs` & `pydantic_core-0.9.0/src/validators/url.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/src/validators/with_default.rs` & `pydantic_core-0.9.0/src/validators/with_default.rs`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/benchmarks/README.md` & `pydantic_core-0.9.0/tests/benchmarks/README.md`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/benchmarks/complete_schema.py` & `pydantic_core-0.9.0/tests/benchmarks/complete_schema.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/benchmarks/test_complete_benchmark.py` & `pydantic_core-0.9.0/tests/benchmarks/test_complete_benchmark.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/benchmarks/test_micro_benchmarks.py` & `pydantic_core-0.9.0/tests/benchmarks/test_micro_benchmarks.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/benchmarks/test_serialization_micro.py` & `pydantic_core-0.9.0/tests/benchmarks/test_serialization_micro.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/conftest.py` & `pydantic_core-0.9.0/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/emscripten_runner.js` & `pydantic_core-0.9.0/tests/emscripten_runner.js`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_any.py` & `pydantic_core-0.9.0/tests/serializers/test_any.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,8 @@
 import json
-import sys
 from dataclasses import dataclass
 from datetime import date, datetime, time, timedelta, timezone
 from decimal import Decimal
 from enum import Enum
 
 import pytest
 from dirty_equals import IsList
@@ -249,15 +248,14 @@
     assert any_serializer.to_json(m, exclude={'bar': {}}, exclude_unset=True) == b'{"bar":2,"spam":3}'
 
     m2 = FieldsSetModel(foo=1, bar=2, spam=3, __fields_set__={'bar', 'spam', 'missing'})
     assert any_serializer.to_python(m2) == {'foo': 1, 'bar': 2, 'spam': 3}
     assert any_serializer.to_python(m2, exclude_unset=True) == {'bar': 2, 'spam': 3}
 
 
-@pytest.mark.xfail(sys.platform == 'win32', reason='https://github.com/PyO3/pyo3/issues/2913')
 def test_unknown_type(any_serializer):
     class Foobar:
         def __repr__(self):
             return '<Foobar repr>'
 
     f = Foobar()
     assert any_serializer.to_python(f) == f
```

### Comparing `pydantic_core-0.8.2/tests/serializers/test_bytes.py` & `pydantic_core-0.9.0/tests/serializers/test_bytes.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,9 @@
 import base64
 import json
-import sys
 from enum import Enum
 
 import pytest
 
 from pydantic_core import PydanticSerializationError, SchemaSerializer, core_schema
 
 
@@ -70,15 +69,14 @@
 
 
 class BytesEnum(bytes, Enum):
     foo = b'foo-value'
     bar = b'bar-value'
 
 
-@pytest.mark.xfail(sys.platform == 'win32', reason='https://github.com/PyO3/pyo3/issues/2913', strict=False)
 @pytest.mark.parametrize('schema_type', ['bytes', 'any'])
 @pytest.mark.parametrize(
     'input_value,expected_json',
     [(BytesSubclass(b'foo'), 'foo'), (BytesMixin(b'foo'), 'foo'), (BytesEnum.foo, 'foo-value')],
 )
 def test_subclass_bytes(schema_type, input_value, expected_json):
     s = SchemaSerializer({'type': schema_type})
```

### Comparing `pydantic_core-0.8.2/tests/serializers/test_datetime.py` & `pydantic_core-0.9.0/tests/serializers/test_datetime.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_dict.py` & `pydantic_core-0.9.0/tests/serializers/test_dict.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_format.py` & `pydantic_core-0.9.0/tests/serializers/test_format.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_functions.py` & `pydantic_core-0.9.0/tests/serializers/test_functions.py`

 * *Files 1% similar despite different names*

```diff
@@ -160,27 +160,27 @@
         return f'{value} info={info}'
 
     s = SchemaSerializer(
         core_schema.any_schema(serialization=core_schema.function_plain_ser_schema(append_args, json_return_type='str'))
     )
     assert s.to_python(123) == (
         "123 info=SerializationInfo(include=None, exclude=None, mode='python', by_alias=True, exclude_unset=False, "
-        "exclude_defaults=False, exclude_none=False, round_trip=False)"
+        'exclude_defaults=False, exclude_none=False, round_trip=False)'
     )
     assert s.to_python(123, mode='other') == (
         "123 info=SerializationInfo(include=None, exclude=None, mode='other', by_alias=True, exclude_unset=False, "
-        "exclude_defaults=False, exclude_none=False, round_trip=False)"
+        'exclude_defaults=False, exclude_none=False, round_trip=False)'
     )
     assert s.to_python(123, include={'x'}) == (
         "123 info=SerializationInfo(include={'x'}, exclude=None, mode='python', by_alias=True, exclude_unset=False, "
-        "exclude_defaults=False, exclude_none=False, round_trip=False)"
+        'exclude_defaults=False, exclude_none=False, round_trip=False)'
     )
     assert s.to_python(123, mode='json', exclude={1: {2}}) == (
         "123 info=SerializationInfo(include=None, exclude={1: {2}}, mode='json', by_alias=True, exclude_unset=False, "
-        "exclude_defaults=False, exclude_none=False, round_trip=False)"
+        'exclude_defaults=False, exclude_none=False, round_trip=False)'
     )
     assert s.to_json(123) == (
         b'"123 info=SerializationInfo(include=None, exclude=None, mode=\'json\', by_alias=True, exclude_unset=False, '
         b'exclude_defaults=False, exclude_none=False, round_trip=False)"'
     )
```

### Comparing `pydantic_core-0.8.2/tests/serializers/test_generator.py` & `pydantic_core-0.9.0/tests/serializers/test_generator.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_json.py` & `pydantic_core-0.9.0/tests/serializers/test_json.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_list_tuple.py` & `pydantic_core-0.9.0/tests/serializers/test_list_tuple.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_literal.py` & `pydantic_core-0.9.0/tests/serializers/test_literal.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_misc.py` & `pydantic_core-0.9.0/tests/serializers/test_misc.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_model.py` & `pydantic_core-0.9.0/tests/serializers/test_model.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_none.py` & `pydantic_core-0.9.0/tests/serializers/test_none.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_nullable.py` & `pydantic_core-0.9.0/tests/serializers/test_nullable.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_other.py` & `pydantic_core-0.9.0/tests/serializers/test_other.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_recursive.py` & `pydantic_core-0.9.0/tests/serializers/test_recursive.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_set_frozenset.py` & `pydantic_core-0.9.0/tests/serializers/test_set_frozenset.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_simple.py` & `pydantic_core-0.9.0/tests/serializers/test_simple.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,9 +1,8 @@
 import json
-import sys
 from enum import IntEnum
 
 import pytest
 
 from pydantic_core import SchemaSerializer
 
 
@@ -16,15 +15,14 @@
     two = 2
 
 
 class FloatSubClass(float):
     pass
 
 
-@pytest.mark.xfail(sys.platform == 'win32', reason='https://github.com/PyO3/pyo3/issues/2913', strict=False)
 @pytest.mark.parametrize('custom_type_schema', [None, 'any'])
 @pytest.mark.parametrize(
     'schema_type,value,expected_python,expected_json',
     [
         ('int', 1, 1, b'1'),
         ('bool', True, True, b'true'),
         ('bool', False, False, b'false'),
```

### Comparing `pydantic_core-0.8.2/tests/serializers/test_string.py` & `pydantic_core-0.9.0/tests/serializers/test_string.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,9 +1,8 @@
 import json
-import sys
 from enum import Enum
 
 import pytest
 
 from pydantic_core import SchemaSerializer, core_schema
 
 
@@ -57,15 +56,14 @@
 
 
 class StrEnum(str, Enum):
     foo = 'foo-value'
     bar = 'bar-value'
 
 
-@pytest.mark.xfail(sys.platform == 'win32', reason='https://github.com/PyO3/pyo3/issues/2913', strict=False)
 @pytest.mark.parametrize('schema_type', ['str', 'any'])
 @pytest.mark.parametrize(
     'input_value,expected', [(StrSubclass('foo'), 'foo'), (StrMixin('foo'), 'foo'), (StrEnum.foo, 'foo-value')]
 )
 def test_subclass_str(schema_type, input_value, expected):
     s = SchemaSerializer({'type': schema_type})
     v = s.to_python(input_value)
```

### Comparing `pydantic_core-0.8.2/tests/serializers/test_timedelta.py` & `pydantic_core-0.9.0/tests/serializers/test_timedelta.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_typed_dict.py` & `pydantic_core-0.9.0/tests/serializers/test_typed_dict.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_union.py` & `pydantic_core-0.9.0/tests/serializers/test_union.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/serializers/test_url.py` & `pydantic_core-0.9.0/tests/serializers/test_url.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/test_build.py` & `pydantic_core-0.9.0/tests/test_build.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/test_config.py` & `pydantic_core-0.9.0/tests/test_config.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/test_docstrings.py` & `pydantic_core-0.9.0/tests/test_docstrings.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/test_errors.py` & `pydantic_core-0.9.0/tests/test_errors.py`

 * *Files 1% similar despite different names*

```diff
@@ -86,15 +86,15 @@
             self.foo = 42
             self.bar = 'before'
 
         def validate(self, input_value, **kwargs):
             return f'{input_value} {self.foo} {self.bar}'
 
     c = CustomValidator()
-    v = SchemaValidator({'type': 'function', 'mode': 'plain', 'extra': {'instance': c}, 'function': c.validate})
+    v = SchemaValidator({'type': 'function', 'mode': 'plain', 'metadata': {'instance': c}, 'function': c.validate})
     c.foo += 1
 
     assert v.validate_python('input value') == 'input value 43 before'
     c.bar = 'changed'
     assert v.validate_python('input value') == 'input value 43 changed'
 
 
@@ -108,15 +108,15 @@
             return f'{input_value} {self.foo}'
 
     c = CustomValidator()
     v = SchemaValidator(
         {
             'type': 'function',
             'mode': 'after',
-            'extra': {'instance': c},
+            'metadata': {'instance': c},
             'function': c.validate,
             'schema': {'type': 'str'},
         }
     )
     c.foo += 1
 
     assert v.validate_python('input value') == 'input value 43'
```

### Comparing `pydantic_core-0.8.2/tests/test_hypothesis.py` & `pydantic_core-0.9.0/tests/test_hypothesis.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/test_isinstance.py` & `pydantic_core-0.9.0/tests/test_isinstance.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/test_json.py` & `pydantic_core-0.9.0/tests/test_json.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/test_misc.py` & `pydantic_core-0.9.0/tests/test_misc.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 import re
 import sys
 from pathlib import Path
 
 import pytest
+from typing_extensions import get_args
 
-from pydantic_core import core_schema
+from pydantic_core import CoreSchema, CoreSchemaType, core_schema
 from pydantic_core._pydantic_core import (
     SchemaError,
     SchemaValidator,
     ValidationError,
     __version__,
     build_profile,
     list_all_errors,
@@ -174,7 +175,22 @@
         },
     ]
     error_types = [e['type'] for e in errors]
     if error_types != list(core_schema.ErrorType.__args__):
         literal = ''.join(f'\n    {e!r},' for e in error_types)
         print(f'python code (end of pydantic_core/core_schema.py):\n\nErrorType = Literal[{literal}\n]')
         pytest.fail('core_schema.ErrorType needs to be updated')
+
+
+def test_core_schema_type_literal():
+    def get_type_value(schema):
+        type_ = schema.__annotations__['type']
+        m = re.search(r"Literal\['(.+?)']", type_.__forward_arg__)
+        assert m, f'Unknown schema type: {type_}'
+        return m.group(1)
+
+    schema_types = tuple(get_type_value(x) for x in CoreSchema.__args__)
+    schema_types = tuple(dict.fromkeys(schema_types))  # remove duplicates while preserving order
+    if get_args(CoreSchemaType) != schema_types:
+        literal = ''.join(f'\n    {e!r},' for e in schema_types)
+        print(f'python code (near end of pydantic_core/core_schema.py):\n\nCoreSchemaType = Literal[{literal}\n]')
+        pytest.fail('core_schema.CoreSchemaType needs to be updated')
```

### Comparing `pydantic_core-0.8.2/tests/test_schema_functions.py` & `pydantic_core-0.9.0/tests/test_schema_functions.py`

 * *Files 1% similar despite different names*

```diff
@@ -29,20 +29,20 @@
 
 def args(*args, **kwargs):
     return args, kwargs
 
 
 all_schema_functions = [
     (core_schema.any_schema, args(), {'type': 'any'}),
-    (core_schema.any_schema, args(extra=['foot', 'spa']), {'type': 'any', 'extra': ['foot', 'spa']}),
+    (core_schema.any_schema, args(metadata=['foot', 'spa']), {'type': 'any', 'metadata': ['foot', 'spa']}),
     (core_schema.none_schema, args(), {'type': 'none'}),
     (core_schema.bool_schema, args(), {'type': 'bool'}),
     (core_schema.bool_schema, args(strict=True), {'type': 'bool', 'strict': True}),
     (core_schema.int_schema, args(), {'type': 'int'}),
-    (core_schema.int_schema, args(extra={'fred'}), {'type': 'int', 'extra': {'fred'}}),
+    (core_schema.int_schema, args(metadata={'fred'}), {'type': 'int', 'metadata': {'fred'}}),
     (core_schema.int_schema, args(multiple_of=5, gt=10, lt=20), {'type': 'int', 'multiple_of': 5, 'gt': 10, 'lt': 20}),
     (core_schema.float_schema, args(), {'type': 'float'}),
     (core_schema.float_schema, args(multiple_of=5, gt=1.2), {'type': 'float', 'multiple_of': 5, 'gt': 1.2}),
     (core_schema.str_schema, args(), {'type': 'str'}),
     (core_schema.str_schema, args(min_length=5, max_length=10), {'type': 'str', 'min_length': 5, 'max_length': 10}),
     (core_schema.bytes_schema, args(), {'type': 'bytes'}),
     (core_schema.bytes_schema, args(min_length=5, ref='xx'), {'type': 'bytes', 'min_length': 5, 'ref': 'xx'}),
```

### Comparing `pydantic_core-0.8.2/tests/test_strict.py` & `pydantic_core-0.9.0/tests/test_strict.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/test_typing.py` & `pydantic_core-0.9.0/tests/test_typing.py`

 * *Files 1% similar despite different names*

```diff
@@ -185,26 +185,26 @@
         return str(__info)
 
     s = SchemaSerializer(
         core_schema.any_schema(serialization=core_schema.function_plain_ser_schema(f, json_return_type='str'))
     )
     assert s.to_python(123) == (
         "SerializationInfo(include=None, exclude=None, mode='python', by_alias=True, exclude_unset=False, "
-        "exclude_defaults=False, exclude_none=False, round_trip=False)"
+        'exclude_defaults=False, exclude_none=False, round_trip=False)'
     )
 
 
 def test_ser_function_wrap():
     def f(__input: Any, __serialize: core_schema.SerializeWrapHandler, __info: core_schema.SerializationInfo) -> str:
         return f'{__serialize} {__info}'
 
     s = SchemaSerializer(
         core_schema.any_schema(
             serialization=core_schema.function_wrap_ser_schema(f, core_schema.str_schema(), when_used='json')
         )
     )
     # insert_assert(s.to_python(123, mode='json'))
     assert s.to_python(123, mode='json') == (
-        "SerializationCallable(serializer=str) "
+        'SerializationCallable(serializer=str) '
         "SerializationInfo(include=None, exclude=None, mode='json', by_alias=True, exclude_unset=False, "
-        "exclude_defaults=False, exclude_none=False, round_trip=False)"
+        'exclude_defaults=False, exclude_none=False, round_trip=False)'
     )
```

### Comparing `pydantic_core-0.8.2/tests/test_validation_context.py` & `pydantic_core-0.9.0/tests/test_validation_context.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_arguments.py` & `pydantic_core-0.9.0/tests/validators/test_arguments.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_bool.py` & `pydantic_core-0.9.0/tests/validators/test_bool.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_bytes.py` & `pydantic_core-0.9.0/tests/validators/test_bytes.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_call.py` & `pydantic_core-0.9.0/tests/validators/test_call.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_callable.py` & `pydantic_core-0.9.0/tests/validators/test_callable.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_chain.py` & `pydantic_core-0.9.0/tests/validators/test_chain.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_custom_error.py` & `pydantic_core-0.9.0/tests/validators/test_custom_error.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_date.py` & `pydantic_core-0.9.0/tests/validators/test_date.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_datetime.py` & `pydantic_core-0.9.0/tests/validators/test_datetime.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_dict.py` & `pydantic_core-0.9.0/tests/validators/test_dict.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_float.py` & `pydantic_core-0.9.0/tests/validators/test_float.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_frozenset.py` & `pydantic_core-0.9.0/tests/validators/test_frozenset.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_function.py` & `pydantic_core-0.9.0/tests/validators/test_function.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_generator.py` & `pydantic_core-0.9.0/tests/validators/test_generator.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_int.py` & `pydantic_core-0.9.0/tests/validators/test_int.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_is_instance.py` & `pydantic_core-0.9.0/tests/validators/test_is_instance.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_is_subclass.py` & `pydantic_core-0.9.0/tests/validators/test_is_subclass.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_json.py` & `pydantic_core-0.9.0/tests/validators/test_json.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_lax_or_strict.py` & `pydantic_core-0.9.0/tests/validators/test_lax_or_strict.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_list.py` & `pydantic_core-0.9.0/tests/validators/test_list.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,9 @@
 import platform
 import re
-import sys
 from collections import deque
 from collections.abc import Sequence
 from typing import Any, Dict
 
 import pytest
 from dirty_equals import HasRepr, IsInstance, IsStr
 
@@ -314,15 +313,14 @@
         def count(self, value):
             return self._data.count(value)
 
     assert isinstance(MySequence(), Sequence)
     return MySequence
 
 
-@pytest.mark.xfail(sys.platform == 'win32', reason='TODO: why doesnt `validate_python` raise an error on windows here?')
 def test_sequence(MySequence):
     v = SchemaValidator({'type': 'list', 'items_schema': {'type': 'int'}})
     with pytest.raises(ValidationError) as exc_info:
         v.validate_python(MySequence())
     # insert_assert(exc_info.value.errors())
     assert exc_info.value.errors() == [
         {'type': 'list_type', 'loc': (), 'msg': 'Input should be a valid list/array', 'input': IsInstance(MySequence)}
```

### Comparing `pydantic_core-0.8.2/tests/validators/test_literal.py` & `pydantic_core-0.9.0/tests/validators/test_literal.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_model.py` & `pydantic_core-0.9.0/tests/validators/test_model.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_nullable.py` & `pydantic_core-0.9.0/tests/validators/test_nullable.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_recursive.py` & `pydantic_core-0.9.0/tests/validators/test_recursive.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_set.py` & `pydantic_core-0.9.0/tests/validators/test_set.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_string.py` & `pydantic_core-0.9.0/tests/validators/test_string.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_tagged_union.py` & `pydantic_core-0.9.0/tests/validators/test_tagged_union.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_time.py` & `pydantic_core-0.9.0/tests/validators/test_time.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_timedelta.py` & `pydantic_core-0.9.0/tests/validators/test_timedelta.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_tuple.py` & `pydantic_core-0.9.0/tests/validators/test_tuple.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_typed_dict.py` & `pydantic_core-0.9.0/tests/validators/test_typed_dict.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_union.py` & `pydantic_core-0.9.0/tests/validators/test_union.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_url.py` & `pydantic_core-0.9.0/tests/validators/test_url.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/tests/validators/test_with_default.py` & `pydantic_core-0.9.0/tests/validators/test_with_default.py`

 * *Files identical despite different names*

### Comparing `pydantic_core-0.8.2/Cargo.lock` & `pydantic_core-0.9.0/Cargo.lock`

 * *Files 7% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 # This file is automatically @generated by Cargo.
 # It is not intended for manual editing.
 version = 3
 
 [[package]]
 name = "ahash"
-version = "0.8.2"
+version = "0.8.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "bf6ccdb167abbf410dcb915cabd428929d7f6a04980b54a11f26a39f1c7f7107"
+checksum = "2c99f64d1e06488f620f932677e24bc6e2897582980441ae90a671415bd7ec2f"
 dependencies = [
  "cfg-if",
  "getrandom",
  "once_cell",
  "version_check",
 ]
 
@@ -39,17 +39,17 @@
 name = "bitflags"
 version = "1.3.2"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "bef38d45163c2f1dde094a7dfd33ccf595c92905c8f8f4fdc18d06fb1037718a"
 
 [[package]]
 name = "cc"
-version = "1.0.78"
+version = "1.0.79"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "a20104e2335ce8a659d6dd92a51a767a0c062599c73b343fd152cb401e828c3d"
+checksum = "50d30906286121d95be3d479533b458f87493b30a4b5f79a607db8f5d11aa91f"
 
 [[package]]
 name = "cfg-if"
 version = "1.0.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "baf1de4339761588bc0619e3cbc0120ee582ebb74b53b4efbf79117bd2da40fd"
 
@@ -89,17 +89,17 @@
 name = "hashbrown"
 version = "0.12.3"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "8a9ee70c43aaf417c914396645a0fa852624801b24ebb7ae78fe8272889ac888"
 
 [[package]]
 name = "heck"
-version = "0.4.0"
+version = "0.4.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "2540771e65fc8cb83cd6e8a237f70c319bd5c29f78ed1084ba5d50eeac86f7f9"
+checksum = "95505c38b4572b2d910cecb0281560f54b440a19336cbbcb27bf6ce6adc6f5a8"
 
 [[package]]
 name = "idna"
 version = "0.3.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "e14ddfc70884202db2244c223200c204c2bda1bc6e0998d11b5e024d657209e6"
 dependencies = [
@@ -115,17 +115,17 @@
 dependencies = [
  "autocfg",
  "hashbrown",
 ]
 
 [[package]]
 name = "indoc"
-version = "1.0.8"
+version = "1.0.9"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "da2d6f23ffea9d7e76c53eee25dfb67bcd8fde7f1198b0855350698c9f07c780"
+checksum = "bfa799dd5ed20a7e349f3b4639aa80d74549c81716d9ec4f994c9b5815598306"
 
 [[package]]
 name = "itoa"
 version = "1.0.5"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "fad582f4b9e86b6caa621cabeb0963332d92eea04729ab12892c2533951e6440"
 
@@ -193,17 +193,17 @@
 dependencies = [
  "lock_api",
  "parking_lot_core",
 ]
 
 [[package]]
 name = "parking_lot_core"
-version = "0.9.6"
+version = "0.9.7"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "ba1ef8814b5c993410bb3adfad7a5ed269563e4a2f90c41f5d85be7fb47133bf"
+checksum = "9069cbb9f99e3a5083476ccb29ceb1de18b9118cafa53e90c9551235de2b9521"
 dependencies = [
  "cfg-if",
  "libc",
  "redox_syscall",
  "smallvec",
  "windows-sys",
 ]
@@ -212,24 +212,24 @@
 name = "percent-encoding"
 version = "2.2.0"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "478c572c3d73181ff3c2539045f6eb99e5491218eae919370993b890cdbdd98e"
 
 [[package]]
 name = "proc-macro2"
-version = "1.0.50"
+version = "1.0.51"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "6ef7d57beacfaf2d8aee5937dab7b7f28de3cb8b1828479bb5de2a7106f2bae2"
+checksum = "5d727cae5b39d21da60fa540906919ad737832fe0b1c165da3a34d6548c849d6"
 dependencies = [
  "unicode-ident",
 ]
 
 [[package]]
 name = "pydantic-core"
-version = "0.8.2"
+version = "0.9.0"
 dependencies = [
  "ahash",
  "base64",
  "enum_dispatch",
  "idna",
  "indexmap",
  "mimalloc",
@@ -244,15 +244,16 @@
  "url",
  "version_check",
 ]
 
 [[package]]
 name = "pyo3"
 version = "0.18.1"
-source = "git+https://github.com/PyO3/pyo3?rev=ec2485bb7dadbed602f286efba9e0900bbcbd50d#ec2485bb7dadbed602f286efba9e0900bbcbd50d"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "06a3d8e8a46ab2738109347433cb7b96dffda2e4a218b03ef27090238886b147"
 dependencies = [
  "cfg-if",
  "indoc",
  "libc",
  "memoffset",
  "parking_lot",
  "pyo3-build-config",
@@ -260,44 +261,48 @@
  "pyo3-macros",
  "unindent",
 ]
 
 [[package]]
 name = "pyo3-build-config"
 version = "0.18.1"
-source = "git+https://github.com/PyO3/pyo3?rev=ec2485bb7dadbed602f286efba9e0900bbcbd50d#ec2485bb7dadbed602f286efba9e0900bbcbd50d"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "75439f995d07ddfad42b192dfcf3bc66a7ecfd8b4a1f5f6f046aa5c2c5d7677d"
 dependencies = [
  "once_cell",
  "target-lexicon",
 ]
 
 [[package]]
 name = "pyo3-ffi"
 version = "0.18.1"
-source = "git+https://github.com/PyO3/pyo3?rev=ec2485bb7dadbed602f286efba9e0900bbcbd50d#ec2485bb7dadbed602f286efba9e0900bbcbd50d"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "839526a5c07a17ff44823679b68add4a58004de00512a95b6c1c98a6dcac0ee5"
 dependencies = [
  "libc",
  "pyo3-build-config",
 ]
 
 [[package]]
 name = "pyo3-macros"
 version = "0.18.1"
-source = "git+https://github.com/PyO3/pyo3?rev=ec2485bb7dadbed602f286efba9e0900bbcbd50d#ec2485bb7dadbed602f286efba9e0900bbcbd50d"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "bd44cf207476c6a9760c4653559be4f206efafb924d3e4cbf2721475fc0d6cc5"
 dependencies = [
  "proc-macro2",
  "pyo3-macros-backend",
  "quote",
  "syn",
 ]
 
 [[package]]
 name = "pyo3-macros-backend"
 version = "0.18.1"
-source = "git+https://github.com/PyO3/pyo3?rev=ec2485bb7dadbed602f286efba9e0900bbcbd50d#ec2485bb7dadbed602f286efba9e0900bbcbd50d"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "dc1f43d8e30460f36350d18631ccf85ded64c059829208fe680904c65bcd0a4c"
 dependencies = [
  "proc-macro2",
  "quote",
  "syn",
 ]
 
 [[package]]
@@ -357,17 +362,17 @@
 name = "serde"
 version = "1.0.152"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "bb7d1f0d3021d347a83e556fc4683dea2ea09d87bccdf88ff5c12545d89d5efb"
 
 [[package]]
 name = "serde_json"
-version = "1.0.91"
+version = "1.0.92"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "877c235533714907a8c2464236f5c4b2a17262ef1bd71f38f35ea592c8da6883"
+checksum = "7434af0dc1cbd59268aa98b4c22c131c0584d2232f6fb166efb993e2832e896a"
 dependencies = [
  "indexmap",
  "itoa",
  "ryu",
  "serde",
 ]
 
@@ -433,23 +438,23 @@
 checksum = "87cc5ceb3875bb20c2890005a4e226a4651264a5c75edb2421b52861a0a0cb50"
 dependencies = [
  "tinyvec_macros",
 ]
 
 [[package]]
 name = "tinyvec_macros"
-version = "0.1.0"
+version = "0.1.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "cda74da7e1a664f795bb1f8a87ec406fb89a02522cf6e50620d016add6dbbf5c"
+checksum = "1f3ccbac311fea05f86f61904b462b55fb3df8837a366dfc601a0161d0532f20"
 
 [[package]]
 name = "unicode-bidi"
-version = "0.3.8"
+version = "0.3.10"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "099b7128301d285f79ddd55b9a83d5e6b9e97c92e0ea0daebee7263e932de992"
+checksum = "d54675592c1dbefd78cbd98db9bacd89886e1ca50692a0692baefffdeb92dd58"
 
 [[package]]
 name = "unicode-ident"
 version = "1.0.6"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "84a22b9f218b40614adcb3f4ff08b703773ad44fa9423e4e0d346d5db86e4ebc"
 
@@ -489,17 +494,26 @@
 name = "wasi"
 version = "0.11.0+wasi-snapshot-preview1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
 checksum = "9c8d87e72b64a3b4db28d11ce29237c246188f4f51057d65a7eab63b7987e423"
 
 [[package]]
 name = "windows-sys"
-version = "0.42.0"
+version = "0.45.0"
+source = "registry+https://github.com/rust-lang/crates.io-index"
+checksum = "75283be5efb2831d37ea142365f009c02ec203cd29a3ebecbc093d52315b66d0"
+dependencies = [
+ "windows-targets",
+]
+
+[[package]]
+name = "windows-targets"
+version = "0.42.1"
 source = "registry+https://github.com/rust-lang/crates.io-index"
-checksum = "5a3e1820f08b8513f676f7ab6c1f99ff312fb97b553d30ff4dd86f9f15728aa7"
+checksum = "8e2522491fbfcd58cc84d47aeb2958948c4b8982e9a2d8a2a35bbaed431390e7"
 dependencies = [
  "windows_aarch64_gnullvm",
  "windows_aarch64_msvc",
  "windows_i686_gnu",
  "windows_i686_msvc",
  "windows_x86_64_gnu",
  "windows_x86_64_gnullvm",
```

### Comparing `pydantic_core-0.8.2/PKG-INFO` & `pydantic_core-0.9.0/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,39 +1,38 @@
 Metadata-Version: 2.1
 Name: pydantic_core
-Version: 0.8.2
+Version: 0.9.0
 Classifier: Development Status :: 3 - Alpha
-Classifier: Environment :: Console
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Rust
+Classifier: Framework :: Pydantic
 Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: Information Technology
-Classifier: Intended Audience :: System Administrators
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: POSIX :: Linux
 Classifier: Operating System :: Microsoft :: Windows
 Classifier: Operating System :: MacOS
-Classifier: Environment :: MacOS X
-Classifier: Topic :: Software Development :: Libraries :: Python Modules
+Classifier: Typing :: Typed
 Requires-Dist: typing_extensions; python_version < "3.11.0"
 License-File: LICENSE
 Home-Page: https://github.com/pydantic/pydantic-core
 Author-email: Samuel Colvin <s@muelcolvin.com>
 License: MIT
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown; charset=UTF-8; variant=GFM
+Project-URL: Homepage, https://github.com/pydantic/pydantic-core
 Project-URL: Funding, https://github.com/sponsors/samuelcolvin
 Project-URL: Source, https://github.com/pydantic/pydantic-core
-Project-URL: Homepage, https://github.com/pydantic/pydantic-core
 
 # pydantic-core
 
 [![CI](https://github.com/pydantic/pydantic-core/workflows/ci/badge.svg?event=push)](https://github.com/pydantic/pydantic-core/actions?query=event%3Apush+branch%3Amain+workflow%3Aci)
 [![Coverage](https://codecov.io/gh/pydantic/pydantic-core/branch/main/graph/badge.svg)](https://codecov.io/gh/pydantic/pydantic-core)
 [![pypi](https://img.shields.io/pypi/v/pydantic-core.svg)](https://pypi.python.org/pypi/pydantic-core)
 [![versions](https://img.shields.io/pypi/pyversions/pydantic-core.svg)](https://github.com/pydantic/pydantic-core)
```

