# Comparing `tmp/shexer-2.0.9.tar.gz` & `tmp/shexer-2.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "shexer-2.0.9.tar", last modified: Tue Apr  4 10:53:49 2023, max compression
+gzip compressed data, was "shexer-2.1.0.tar", last modified: Thu Apr  6 19:33:08 2023, max compression
```

## Comparing `shexer-2.0.9.tar` & `shexer-2.1.0.tar`

### file list

```diff
@@ -1,230 +1,237 @@
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.966241 shexer-2.0.9/
--rw-rw-rw-   0        0        0    11558 2019-11-23 19:24:24.000000 shexer-2.0.9/LICENSE
--rw-rw-rw-   0        0        0    25073 2023-04-04 10:53:49.967245 shexer-2.0.9/PKG-INFO
--rw-rw-rw-   0        0        0    24157 2023-04-04 10:53:17.000000 shexer-2.0.9/README.md
--rw-rw-rw-   0        0        0       86 2023-04-04 10:53:49.970245 shexer-2.0.9/setup.cfg
--rw-rw-rw-   0        0        0     1392 2023-04-04 10:53:17.000000 shexer-2.0.9/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:48.810242 shexer-2.0.9/shexer/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/__init__.py
--rw-rw-rw-   0        0        0      644 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/consts.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:48.849243 shexer-2.0.9/shexer/core/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/core/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:48.876253 shexer-2.0.9/shexer/core/instances/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/core/instances/__init__.py
--rw-rw-rw-   0        0        0      713 2021-10-25 09:34:37.000000 shexer-2.0.9/shexer/core/instances/abstract_instance_tracker.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:48.905245 shexer-2.0.9/shexer/core/instances/annotators/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/core/instances/annotators/__init__.py
--rw-rw-rw-   0        0        0      383 2021-01-14 17:50:11.000000 shexer-2.0.9/shexer/core/instances/annotators/annotator_func.py
--rw-rw-rw-   0        0        0     1817 2021-01-14 17:50:11.000000 shexer-2.0.9/shexer/core/instances/annotators/annotator_tracking_instances.py
--rw-rw-rw-   0        0        0     3198 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/instances/annotators/base_annotator.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:48.952244 shexer-2.0.9/shexer/core/instances/annotators/strategy_mode/
--rw-rw-rw-   0        0        0        0 2021-01-14 17:50:11.000000 shexer-2.0.9/shexer/core/instances/annotators/strategy_mode/__init__.py
--rw-rw-rw-   0        0        0      688 2021-10-25 09:34:37.000000 shexer-2.0.9/shexer/core/instances/annotators/strategy_mode/all_classes_mode.py
--rw-rw-rw-   0        0        0      592 2021-01-14 17:50:11.000000 shexer-2.0.9/shexer/core/instances/annotators/strategy_mode/base_strategy_mode.py
--rw-rw-rw-   0        0        0      807 2021-01-14 17:50:11.000000 shexer-2.0.9/shexer/core/instances/annotators/strategy_mode/compound_strategy_mode.py
--rw-rw-rw-   0        0        0     1793 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/instances/annotators/strategy_mode/shape_qualifiers_mode.py
--rw-rw-rw-   0        0        0      830 2021-10-25 09:34:37.000000 shexer-2.0.9/shexer/core/instances/annotators/strategy_mode/target_classes_mode.py
--rw-rw-rw-   0        0        0     4260 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/instances/instance_tracker.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:48.961310 shexer-2.0.9/shexer/core/instances/mappings/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/core/instances/mappings/__init__.py
--rw-rw-rw-   0        0        0     1081 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/instances/mappings/shape_map_instance_tracker.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:48.973243 shexer-2.0.9/shexer/core/instances/mix/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/core/instances/mix/__init__.py
--rw-rw-rw-   0        0        0     2652 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/instances/mix/mixed_instance_tracker.py
--rw-rw-rw-   0        0        0       22 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/core/instances/pconsts.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:48.991244 shexer-2.0.9/shexer/core/profiling/
--rw-rw-rw-   0        0        0        0 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/profiling/__init__.py
--rw-rw-rw-   0        0        0     7002 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/profiling/class_profiler.py
--rw-rw-rw-   0        0        0      182 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/profiling/consts.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.023243 shexer-2.0.9/shexer/core/profiling/strategy/
--rw-rw-rw-   0        0        0        0 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/profiling/strategy/__init__.py
--rw-rw-rw-   0        0        0     6960 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/profiling/strategy/abstract_strategy.py
--rw-rw-rw-   0        0        0     1299 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/profiling/strategy/direct_features_strategy.py
--rw-rw-rw-   0        0        0     7345 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/profiling/strategy/include_reverse_features_strategy.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.035295 shexer-2.0.9/shexer/core/shexing/
--rw-rw-rw-   0        0        0        0 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/shexing/__init__.py
--rw-rw-rw-   0        0        0     5926 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/core/shexing/class_shexer.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.062243 shexer-2.0.9/shexer/core/shexing/strategy/
--rw-rw-rw-   0        0        0        0 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/core/shexing/strategy/__init__.py
--rw-rw-rw-   0        0        0    16359 2023-04-03 18:35:42.000000 shexer-2.0.9/shexer/core/shexing/strategy/asbtract_shexing_strategy.py
--rw-rw-rw-   0        0        0     5668 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/core/shexing/strategy/direct_and_inverse_shexing_strategy.py
--rw-rw-rw-   0        0        0     2787 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/core/shexing/strategy/direct_shexing_strategy.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.080254 shexer-2.0.9/shexer/io/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/__init__.py
--rw-rw-rw-   0        0        0      103 2021-04-26 09:52:52.000000 shexer-2.0.9/shexer/io/file.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.082257 shexer-2.0.9/shexer/io/graph/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/graph/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.192283 shexer-2.0.9/shexer/io/graph/yielder/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/graph/yielder/__init__.py
--rw-rw-rw-   0        0        0     1431 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/io/graph/yielder/base_triples_yielder.py
--rw-rw-rw-   0        0        0    16303 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/io/graph/yielder/big_ttl_triples_yielder.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.205284 shexer-2.0.9/shexer/io/graph/yielder/filter/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/graph/yielder/filter/__init__.py
--rw-rw-rw-   0        0        0      862 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/graph/yielder/filter/filter_namespaces_triple_yielder.py
--rw-rw-rw-   0        0        0     1131 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/io/graph/yielder/multi_big_ttl_files_triple_yielder.py
--rw-rw-rw-   0        0        0     1132 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/io/graph/yielder/multi_nt_triples_yielder.py
--rw-rw-rw-   0        0        0     1757 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/io/graph/yielder/multi_rdflib_triple_yielder.py
--rw-rw-rw-   0        0        0     1166 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/io/graph/yielder/multi_tsv_nt_triples_yielder.py
--rw-rw-rw-   0        0        0     2674 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/io/graph/yielder/multifile_base_triples_yielder.py
--rw-rw-rw-   0        0        0     5686 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/io/graph/yielder/nt_triples_yielder.py
--rw-rw-rw-   0        0        0     6817 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/io/graph/yielder/rdflib_triple_yielder.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.209245 shexer-2.0.9/shexer/io/graph/yielder/remote/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/graph/yielder/remote/__init__.py
--rw-rw-rw-   0        0        0     3826 2023-04-03 18:35:42.000000 shexer-2.0.9/shexer/io/graph/yielder/remote/sgraph_from_selectors_triple_yielder.py
--rw-rw-rw-   0        0        0     4724 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/io/graph/yielder/tsv_nt_triples_yielder.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.219253 shexer-2.0.9/shexer/io/json/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/json/__init__.py
--rw-rw-rw-   0        0        0      207 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/json/json_loader.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.254258 shexer-2.0.9/shexer/io/line_reader/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/line_reader/__init__.py
--rw-rw-rw-   0        0        0      285 2021-01-14 17:50:12.000000 shexer-2.0.9/shexer/io/line_reader/file_line_reader.py
--rw-rw-rw-   0        0        0      332 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/io/line_reader/gz_line_reader.py
--rw-rw-rw-   0        0        0      260 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/line_reader/raw_string_line_reader.py
--rw-rw-rw-   0        0        0      353 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/io/line_reader/zip_file_line_reader.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.256243 shexer-2.0.9/shexer/io/profile/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/profile/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.265244 shexer-2.0.9/shexer/io/profile/formater/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/profile/formater/__init__.py
--rw-rw-rw-   0        0        0      409 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/profile/formater/abstract_profile_serializer.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.268253 shexer-2.0.9/shexer/io/shacl/
--rw-rw-rw-   0        0        0        0 2021-04-26 09:52:52.000000 shexer-2.0.9/shexer/io/shacl/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.282248 shexer-2.0.9/shexer/io/shacl/formater/
--rw-rw-rw-   0        0        0        0 2021-04-26 09:52:52.000000 shexer-2.0.9/shexer/io/shacl/formater/__init__.py
--rw-rw-rw-   0        0        0    15220 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/io/shacl/formater/shacl_serializer.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.311260 shexer-2.0.9/shexer/io/shape_map/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/shape_map/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.322299 shexer-2.0.9/shexer/io/shape_map/label/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/shape_map/label/__init__.py
--rw-rw-rw-   0        0        0     1410 2021-01-14 17:50:12.000000 shexer-2.0.9/shexer/io/shape_map/label/shape_map_label_parser.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.337242 shexer-2.0.9/shexer/io/shape_map/node_selector/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/shape_map/node_selector/__init__.py
--rw-rw-rw-   0        0        0     6755 2021-04-26 09:52:52.000000 shexer-2.0.9/shexer/io/shape_map/node_selector/node_selector_parser.py
--rw-rw-rw-   0        0        0     4966 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/shape_map/shape_map_parser.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.339255 shexer-2.0.9/shexer/io/shex/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/shex/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.374242 shexer-2.0.9/shexer/io/shex/formater/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/shex/formater/__init__.py
--rw-rw-rw-   0        0        0      244 2021-01-14 17:50:12.000000 shexer-2.0.9/shexer/io/shex/formater/consts.py
--rw-rw-rw-   0        0        0     6676 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/io/shex/formater/shex_serializer.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.414241 shexer-2.0.9/shexer/io/shex/formater/statement_serializers/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/shex/formater/statement_serializers/__init__.py
--rw-rw-rw-   0        0        0     6014 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/io/shex/formater/statement_serializers/base_statement_serializer.py
--rw-rw-rw-   0        0        0     2287 2023-02-03 19:09:46.000000 shexer-2.0.9/shexer/io/shex/formater/statement_serializers/fixed_prop_choice_statement_serializer.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.455246 shexer-2.0.9/shexer/io/shex/formater/statement_serializers/frequency_strategy/
--rw-rw-rw-   0        0        0        0 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/io/shex/formater/statement_serializers/frequency_strategy/__init__.py
--rw-rw-rw-   0        0        0      383 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/io/shex/formater/statement_serializers/frequency_strategy/abs_freq_serializer.py
--rw-rw-rw-   0        0        0      171 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/io/shex/formater/statement_serializers/frequency_strategy/base_frequency_strategy.py
--rw-rw-rw-   0        0        0      887 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/io/shex/formater/statement_serializers/frequency_strategy/mixed_frequency_strategy.py
--rw-rw-rw-   0        0        0     1278 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/io/shex/formater/statement_serializers/frequency_strategy/ratio_freq_serializer.py
--rw-rw-rw-   0        0        0     1500 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/io/shex/formater/statement_serializers/inverse_statement_serializer.py
--rw-rw-rw-   0        0        0     3211 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/io/shex/formater/statement_serializers/st_serializers_factory.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.465284 shexer-2.0.9/shexer/io/sparql/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/io/sparql/__init__.py
--rw-rw-rw-   0        0        0     4538 2022-07-15 19:02:46.000000 shexer-2.0.9/shexer/io/sparql/query.py
--rw-rw-rw-   0        0        0      469 2021-04-26 09:52:52.000000 shexer-2.0.9/shexer/io/wikidata.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.586243 shexer-2.0.9/shexer/model/
--rw-rw-rw-   0        0        0      552 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/model/IRI.py
--rw-rw-rw-   0        0        0      280 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/model/Literal.py
--rw-rw-rw-   0        0        0      810 2021-01-14 17:50:12.000000 shexer-2.0.9/shexer/model/Macro.py
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/model/__init__.py
--rw-rw-rw-   0        0        0      502 2021-10-04 17:33:25.000000 shexer-2.0.9/shexer/model/bnode.py
--rw-rw-rw-   0        0        0      100 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/model/const_elem_types.py
--rw-rw-rw-   0        0        0     1119 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/model/fixed_prop_choice_statement.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.607242 shexer-2.0.9/shexer/model/graph/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/model/graph/__init__.py
--rw-rw-rw-   0        0        0     6186 2022-07-15 19:02:46.000000 shexer-2.0.9/shexer/model/graph/abstract_sgraph.py
--rw-rw-rw-   0        0        0     7633 2023-04-04 10:53:17.000000 shexer-2.0.9/shexer/model/graph/endpoint_sgraph.py
--rw-rw-rw-   0        0        0     6224 2023-04-03 18:35:42.000000 shexer-2.0.9/shexer/model/graph/rdflib_sgraph.py
--rw-rw-rw-   0        0        0     4173 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/model/hierarchy_tree.py
--rw-rw-rw-   0        0        0     2527 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/model/node_selector.py
--rw-rw-rw-   0        0        0      427 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/model/property.py
--rw-rw-rw-   0        0        0     3126 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/model/shape.py
--rw-rw-rw-   0        0        0      858 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/model/shape_map.py
--rw-rw-rw-   0        0        0     2716 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/model/statement.py
--rw-rw-rw-   0        0        0    22302 2023-04-04 10:53:17.000000 shexer-2.0.9/shexer/shaper.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.700243 shexer-2.0.9/shexer/utils/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/utils/__init__.py
--rw-rw-rw-   0        0        0      621 2022-08-11 11:37:45.000000 shexer-2.0.9/shexer/utils/compression.py
--rw-rw-rw-   0        0        0       94 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/utils/dict.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.818255 shexer-2.0.9/shexer/utils/factories/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/utils/factories/__init__.py
--rw-rw-rw-   0        0        0     4185 2023-04-04 10:53:17.000000 shexer-2.0.9/shexer/utils/factories/class_profiler_factory.py
--rw-rw-rw-   0        0        0     2042 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/utils/factories/class_shexer_factory.py
--rw-rw-rw-   0        0        0      728 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/utils/factories/h_tree.py
--rw-rw-rw-   0        0        0    12215 2023-04-04 10:53:17.000000 shexer-2.0.9/shexer/utils/factories/instance_tracker_factory.py
--rw-rw-rw-   0        0        0      437 2021-10-03 10:32:18.000000 shexer-2.0.9/shexer/utils/factories/iri_factory.py
--rw-rw-rw-   0        0        0      286 2021-01-14 17:50:12.000000 shexer-2.0.9/shexer/utils/factories/remote_graph_factory.py
--rw-rw-rw-   0        0        0     1985 2021-04-26 09:52:52.000000 shexer-2.0.9/shexer/utils/factories/shape_map_factory.py
--rw-rw-rw-   0        0        0      616 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/utils/factories/shape_map_parser_factory.py
--rw-rw-rw-   0        0        0     1608 2023-02-02 16:28:05.000000 shexer-2.0.9/shexer/utils/factories/shape_serializer_factory.py
--rw-rw-rw-   0        0        0    18627 2023-04-04 10:53:17.000000 shexer-2.0.9/shexer/utils/factories/triple_yielders_factory.py
--rw-rw-rw-   0        0        0      123 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/utils/file.py
--rw-rw-rw-   0        0        0      397 2021-10-04 17:33:25.000000 shexer-2.0.9/shexer/utils/log.py
--rw-rw-rw-   0        0        0      803 2021-01-14 17:50:12.000000 shexer-2.0.9/shexer/utils/namespaces.py
--rw-rw-rw-   0        0        0      967 2019-11-23 19:24:28.000000 shexer-2.0.9/shexer/utils/obj_references.py
--rw-rw-rw-   0        0        0     2008 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/utils/shapes.py
--rw-rw-rw-   0        0        0     1397 2022-03-28 20:28:03.000000 shexer-2.0.9/shexer/utils/target_elements.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.830285 shexer-2.0.9/shexer/utils/translators/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:29.000000 shexer-2.0.9/shexer/utils/translators/__init__.py
--rw-rw-rw-   0        0        0     2881 2021-04-26 09:52:52.000000 shexer-2.0.9/shexer/utils/translators/list_of_classes_to_shape_map.py
--rw-rw-rw-   0        0        0     3026 2023-04-03 15:39:42.000000 shexer-2.0.9/shexer/utils/triple_yielders.py
--rw-rw-rw-   0        0        0     5058 2023-04-03 18:35:42.000000 shexer-2.0.9/shexer/utils/uri.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:48.847243 shexer-2.0.9/shexer.egg-info/
--rw-rw-rw-   0        0        0    25073 2023-04-04 10:53:47.000000 shexer-2.0.9/shexer.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     7336 2023-04-04 10:53:47.000000 shexer-2.0.9/shexer.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-04 10:53:47.000000 shexer-2.0.9/shexer.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       61 2023-04-04 10:53:47.000000 shexer-2.0.9/shexer.egg-info/requires.txt
--rw-rw-rw-   0        0        0       15 2023-04-04 10:53:47.000000 shexer-2.0.9/shexer.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.931245 shexer-2.0.9/test/
--rw-rw-rw-   0        0        0        0 2021-01-14 17:50:12.000000 shexer-2.0.9/test/__init__.py
--rw-rw-rw-   0        0        0     1903 2021-11-20 10:36:36.000000 shexer-2.0.9/test/const.py
--rw-rw-rw-   0        0        0     8963 2023-04-03 18:35:42.000000 shexer-2.0.9/test/t_utils.py
--rw-rw-rw-   0        0        0     1488 2022-08-10 11:13:26.000000 shexer-2.0.9/test/test_all_classes_mode.py
--rw-rw-rw-   0        0        0     1525 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_allow_opt_cardinality.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.936244 shexer-2.0.9/test/test_bugs/
--rw-rw-rw-   0        0        0        0 2022-03-28 20:28:03.000000 shexer-2.0.9/test/test_bugs/__init__.py
--rw-rw-rw-   0        0        0      796 2022-03-28 20:28:03.000000 shexer-2.0.9/test/test_bugs/test_no_sharp_in_auto_shape_names.py
--rw-rw-rw-   0        0        0     9920 2022-08-11 11:37:45.000000 shexer-2.0.9/test/test_compression_mode.py
--rw-rw-rw-   0        0        0     2171 2023-02-02 16:28:05.000000 shexer-2.0.9/test/test_decimals.py
--rw-rw-rw-   0        0        0     5564 2023-04-03 18:13:21.000000 shexer-2.0.9/test/test_depth_for_building_subgraph.py
--rw-rw-rw-   0        0        0     1388 2023-02-02 16:28:05.000000 shexer-2.0.9/test/test_disable_comments.py
--rw-rw-rw-   0        0        0     2922 2023-04-04 10:53:17.000000 shexer-2.0.9/test/test_disable_endpoint_cache.py
--rw-rw-rw-   0        0        0     1491 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_disable_exact_cardinality.py
--rw-rw-rw-   0        0        0     2552 2023-04-03 18:35:42.000000 shexer-2.0.9/test/test_disable_or_statements.py
--rw-rw-rw-   0        0        0     3786 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_discard_and_compliant.py
--rw-rw-rw-   0        0        0     2090 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_file_target_classes.py
--rw-rw-rw-   0        0        0     1677 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_graph_file_input.py
--rw-rw-rw-   0        0        0     3456 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_graph_list_of_file_inputs.py
--rw-rw-rw-   0        0        0     1951 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_infer_numeric_types_for_untyped_literals.py
--rw-rw-rw-   0        0        0     7818 2023-02-02 16:28:05.000000 shexer-2.0.9/test/test_input_format.py
--rw-rw-rw-   0        0        0     3367 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_instances_file_input.py
--rw-rw-rw-   0        0        0     3852 2023-02-02 16:28:05.000000 shexer-2.0.9/test/test_instances_report.py
--rw-rw-rw-   0        0        0     3548 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_instantiation_property.py
--rw-rw-rw-   0        0        0     1964 2022-03-28 20:28:03.000000 shexer-2.0.9/test/test_inverse_paths.py
--rw-rw-rw-   0        0        0     3594 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_keep_less_specific.py
--rw-rw-rw-   0        0        0     4051 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_list_of_url_input.py
--rw-rw-rw-   0        0        0     4106 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_namespaces_dict.py
--rw-rw-rw-   0        0        0     2082 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_namespaces_to_ignore.py
--rw-rw-rw-   0        0        0     5000 2021-01-14 17:50:12.000000 shexer-2.0.9/test/test_raw_graph.py
--rw-rw-rw-   0        0        0     4300 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_raw_shape_map.py
--rw-rw-rw-   0        0        0     1711 2022-07-15 19:02:46.000000 shexer-2.0.9/test/test_rdflib_graph.py
--rw-rw-rw-   0        0        0     2930 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_remove_empty_sahpes.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.944243 shexer-2.0.9/test/test_shacl/
--rw-rw-rw-   0        0        0        0 2021-04-26 09:52:52.000000 shexer-2.0.9/test/test_shacl/__init__.py
--rw-rw-rw-   0        0        0     2225 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_shacl/test_annotation.py
--rw-rw-rw-   0        0        0     2242 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_shacl/test_class_selection.py
--rw-rw-rw-   0        0        0      910 2022-03-28 20:28:03.000000 shexer-2.0.9/test/test_shacl/test_literal_types.py
--rw-rw-rw-   0        0        0     4313 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_shape_map_file.py
--rw-rw-rw-   0        0        0     6086 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_shape_map_format.py
--rw-rw-rw-   0        0        0     2307 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_shape_qualifiers_mode.py
--rw-rw-rw-   0        0        0     2889 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_shapes_namespaces.py
--rw-rw-rw-   0        0        0     2452 2022-03-28 20:28:03.000000 shexer-2.0.9/test/test_sort.py
--rw-rw-rw-   0        0        0     2058 2021-10-24 17:07:37.000000 shexer-2.0.9/test/test_target_classes.py
--rw-rw-rw-   0        0        0     3120 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_threshold.py
--rw-rw-rw-   0        0        0     2578 2023-04-03 18:13:27.000000 shexer-2.0.9/test/test_url_endpoint.py
--rw-rw-rw-   0        0        0     1867 2022-07-15 19:02:46.000000 shexer-2.0.9/test/test_url_graph.py
--rw-rw-rw-   0        0        0     1900 2021-10-03 10:32:18.000000 shexer-2.0.9/test/test_wikidata_annotation.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:53:49.964242 shexer-2.0.9/ws/
--rw-rw-rw-   0        0        0        0 2019-11-23 19:24:29.000000 shexer-2.0.9/ws/__init__.py
--rw-rw-rw-   0        0        0    19884 2022-03-28 20:28:03.000000 shexer-2.0.9/ws/shexer_rest.py
--rw-rw-rw-   0        0        0       28 2019-11-23 19:24:29.000000 shexer-2.0.9/ws/wsgi.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:08.576414 shexer-2.1.0/
+-rw-rw-rw-   0        0        0    11558 2019-11-23 19:24:24.000000 shexer-2.1.0/LICENSE
+-rw-rw-rw-   0        0        0    25474 2023-04-06 19:33:08.576414 shexer-2.1.0/PKG-INFO
+-rw-rw-rw-   0        0        0    24558 2023-04-04 16:55:09.000000 shexer-2.1.0/README.md
+-rw-rw-rw-   0        0        0       86 2023-04-06 19:33:08.579415 shexer-2.1.0/setup.cfg
+-rw-rw-rw-   0        0        0     1392 2023-04-06 19:32:13.000000 shexer-2.1.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.418408 shexer-2.1.0/shexer/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/__init__.py
+-rw-rw-rw-   0        0        0      644 2023-02-02 16:28:05.000000 shexer-2.1.0/shexer/consts.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.456410 shexer-2.1.0/shexer/core/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/core/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.491410 shexer-2.1.0/shexer/core/instances/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/core/instances/__init__.py
+-rw-rw-rw-   0        0        0      713 2021-10-25 09:34:37.000000 shexer-2.1.0/shexer/core/instances/abstract_instance_tracker.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.519411 shexer-2.1.0/shexer/core/instances/annotators/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/core/instances/annotators/__init__.py
+-rw-rw-rw-   0        0        0      383 2021-01-14 17:50:11.000000 shexer-2.1.0/shexer/core/instances/annotators/annotator_func.py
+-rw-rw-rw-   0        0        0     1817 2021-01-14 17:50:11.000000 shexer-2.1.0/shexer/core/instances/annotators/annotator_tracking_instances.py
+-rw-rw-rw-   0        0        0     3198 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/core/instances/annotators/base_annotator.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.565409 shexer-2.1.0/shexer/core/instances/annotators/strategy_mode/
+-rw-rw-rw-   0        0        0        0 2021-01-14 17:50:11.000000 shexer-2.1.0/shexer/core/instances/annotators/strategy_mode/__init__.py
+-rw-rw-rw-   0        0        0      688 2021-10-25 09:34:37.000000 shexer-2.1.0/shexer/core/instances/annotators/strategy_mode/all_classes_mode.py
+-rw-rw-rw-   0        0        0      592 2021-01-14 17:50:11.000000 shexer-2.1.0/shexer/core/instances/annotators/strategy_mode/base_strategy_mode.py
+-rw-rw-rw-   0        0        0      807 2021-01-14 17:50:11.000000 shexer-2.1.0/shexer/core/instances/annotators/strategy_mode/compound_strategy_mode.py
+-rw-rw-rw-   0        0        0     1793 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/core/instances/annotators/strategy_mode/shape_qualifiers_mode.py
+-rw-rw-rw-   0        0        0      830 2021-10-25 09:34:37.000000 shexer-2.1.0/shexer/core/instances/annotators/strategy_mode/target_classes_mode.py
+-rw-rw-rw-   0        0        0     4260 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/core/instances/instance_tracker.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.574412 shexer-2.1.0/shexer/core/instances/mappings/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/core/instances/mappings/__init__.py
+-rw-rw-rw-   0        0        0     1081 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/core/instances/mappings/shape_map_instance_tracker.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.583408 shexer-2.1.0/shexer/core/instances/mix/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/core/instances/mix/__init__.py
+-rw-rw-rw-   0        0        0     2652 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/core/instances/mix/mixed_instance_tracker.py
+-rw-rw-rw-   0        0        0       22 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/core/instances/pconsts.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.601410 shexer-2.1.0/shexer/core/profiling/
+-rw-rw-rw-   0        0        0        0 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/core/profiling/__init__.py
+-rw-rw-rw-   0        0        0     8614 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/core/profiling/class_profiler.py
+-rw-rw-rw-   0        0        0      182 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/core/profiling/consts.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.623409 shexer-2.1.0/shexer/core/profiling/strategy/
+-rw-rw-rw-   0        0        0        0 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/core/profiling/strategy/__init__.py
+-rw-rw-rw-   0        0        0     6976 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/core/profiling/strategy/abstract_feature_direction_strategy.py
+-rw-rw-rw-   0        0        0     1349 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/core/profiling/strategy/direct_features_strategy.py
+-rw-rw-rw-   0        0        0     7395 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/core/profiling/strategy/include_reverse_features_strategy.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.634410 shexer-2.1.0/shexer/core/shexing/
+-rw-rw-rw-   0        0        0        0 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/core/shexing/__init__.py
+-rw-rw-rw-   0        0        0     6110 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/core/shexing/class_shexer.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.664411 shexer-2.1.0/shexer/core/shexing/strategy/
+-rw-rw-rw-   0        0        0        0 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/core/shexing/strategy/__init__.py
+-rw-rw-rw-   0        0        0    16882 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/core/shexing/strategy/abstract_shexing_strategy.py
+-rw-rw-rw-   0        0        0     5685 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/core/shexing/strategy/direct_and_inverse_shexing_strategy.py
+-rw-rw-rw-   0        0        0     2804 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/core/shexing/strategy/direct_shexing_strategy.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.693411 shexer-2.1.0/shexer/core/shexing/strategy/minimal_iri_strategy/
+-rw-rw-rw-   0        0        0        0 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/core/shexing/strategy/minimal_iri_strategy/__init__.py
+-rw-rw-rw-   0        0        0      118 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/core/shexing/strategy/minimal_iri_strategy/abstract_min_iri_strategy.py
+-rw-rw-rw-   0        0        0     1088 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/core/shexing/strategy/minimal_iri_strategy/annotate_min_iri_strategy.py
+-rw-rw-rw-   0        0        0      412 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/core/shexing/strategy/minimal_iri_strategy/ignore_min_iri_strategy.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.711451 shexer-2.1.0/shexer/io/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/__init__.py
+-rw-rw-rw-   0        0        0      103 2021-04-26 09:52:52.000000 shexer-2.1.0/shexer/io/file.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.714411 shexer-2.1.0/shexer/io/graph/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/graph/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.809411 shexer-2.1.0/shexer/io/graph/yielder/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/graph/yielder/__init__.py
+-rw-rw-rw-   0        0        0     1431 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/io/graph/yielder/base_triples_yielder.py
+-rw-rw-rw-   0        0        0    16303 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/io/graph/yielder/big_ttl_triples_yielder.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.819409 shexer-2.1.0/shexer/io/graph/yielder/filter/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/graph/yielder/filter/__init__.py
+-rw-rw-rw-   0        0        0      862 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/graph/yielder/filter/filter_namespaces_triple_yielder.py
+-rw-rw-rw-   0        0        0     1131 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/io/graph/yielder/multi_big_ttl_files_triple_yielder.py
+-rw-rw-rw-   0        0        0     1132 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/io/graph/yielder/multi_nt_triples_yielder.py
+-rw-rw-rw-   0        0        0     1757 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/io/graph/yielder/multi_rdflib_triple_yielder.py
+-rw-rw-rw-   0        0        0     1166 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/io/graph/yielder/multi_tsv_nt_triples_yielder.py
+-rw-rw-rw-   0        0        0     2674 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/io/graph/yielder/multifile_base_triples_yielder.py
+-rw-rw-rw-   0        0        0     5686 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/io/graph/yielder/nt_triples_yielder.py
+-rw-rw-rw-   0        0        0     6817 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/io/graph/yielder/rdflib_triple_yielder.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.829451 shexer-2.1.0/shexer/io/graph/yielder/remote/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/graph/yielder/remote/__init__.py
+-rw-rw-rw-   0        0        0     3826 2023-04-03 18:35:42.000000 shexer-2.1.0/shexer/io/graph/yielder/remote/sgraph_from_selectors_triple_yielder.py
+-rw-rw-rw-   0        0        0     4724 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/io/graph/yielder/tsv_nt_triples_yielder.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.839409 shexer-2.1.0/shexer/io/json/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/json/__init__.py
+-rw-rw-rw-   0        0        0      207 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/json/json_loader.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.875417 shexer-2.1.0/shexer/io/line_reader/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/line_reader/__init__.py
+-rw-rw-rw-   0        0        0      285 2021-01-14 17:50:12.000000 shexer-2.1.0/shexer/io/line_reader/file_line_reader.py
+-rw-rw-rw-   0        0        0      332 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/io/line_reader/gz_line_reader.py
+-rw-rw-rw-   0        0        0      260 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/line_reader/raw_string_line_reader.py
+-rw-rw-rw-   0        0        0      353 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/io/line_reader/zip_file_line_reader.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.878409 shexer-2.1.0/shexer/io/profile/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/profile/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.886409 shexer-2.1.0/shexer/io/profile/formater/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/profile/formater/__init__.py
+-rw-rw-rw-   0        0        0      409 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/profile/formater/abstract_profile_serializer.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.888411 shexer-2.1.0/shexer/io/shacl/
+-rw-rw-rw-   0        0        0        0 2021-04-26 09:52:52.000000 shexer-2.1.0/shexer/io/shacl/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.902446 shexer-2.1.0/shexer/io/shacl/formater/
+-rw-rw-rw-   0        0        0        0 2021-04-26 09:52:52.000000 shexer-2.1.0/shexer/io/shacl/formater/__init__.py
+-rw-rw-rw-   0        0        0    15833 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/io/shacl/formater/shacl_serializer.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.915456 shexer-2.1.0/shexer/io/shape_map/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/shape_map/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.924411 shexer-2.1.0/shexer/io/shape_map/label/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/shape_map/label/__init__.py
+-rw-rw-rw-   0        0        0     1410 2021-01-14 17:50:12.000000 shexer-2.1.0/shexer/io/shape_map/label/shape_map_label_parser.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.936450 shexer-2.1.0/shexer/io/shape_map/node_selector/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/shape_map/node_selector/__init__.py
+-rw-rw-rw-   0        0        0     6755 2021-04-26 09:52:52.000000 shexer-2.1.0/shexer/io/shape_map/node_selector/node_selector_parser.py
+-rw-rw-rw-   0        0        0     4966 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/shape_map/shape_map_parser.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.938412 shexer-2.1.0/shexer/io/shex/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/shex/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.956409 shexer-2.1.0/shexer/io/shex/formater/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/shex/formater/__init__.py
+-rw-rw-rw-   0        0        0      244 2021-01-14 17:50:12.000000 shexer-2.1.0/shexer/io/shex/formater/consts.py
+-rw-rw-rw-   0        0        0     7004 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/io/shex/formater/shex_serializer.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.996409 shexer-2.1.0/shexer/io/shex/formater/statement_serializers/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/shex/formater/statement_serializers/__init__.py
+-rw-rw-rw-   0        0        0     6014 2023-02-02 16:28:05.000000 shexer-2.1.0/shexer/io/shex/formater/statement_serializers/base_statement_serializer.py
+-rw-rw-rw-   0        0        0     2287 2023-02-03 19:09:46.000000 shexer-2.1.0/shexer/io/shex/formater/statement_serializers/fixed_prop_choice_statement_serializer.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:08.036408 shexer-2.1.0/shexer/io/shex/formater/statement_serializers/frequency_strategy/
+-rw-rw-rw-   0        0        0        0 2023-02-02 16:28:05.000000 shexer-2.1.0/shexer/io/shex/formater/statement_serializers/frequency_strategy/__init__.py
+-rw-rw-rw-   0        0        0      383 2023-02-02 16:28:05.000000 shexer-2.1.0/shexer/io/shex/formater/statement_serializers/frequency_strategy/abs_freq_serializer.py
+-rw-rw-rw-   0        0        0      171 2023-02-02 16:28:05.000000 shexer-2.1.0/shexer/io/shex/formater/statement_serializers/frequency_strategy/base_frequency_strategy.py
+-rw-rw-rw-   0        0        0      887 2023-02-02 16:28:05.000000 shexer-2.1.0/shexer/io/shex/formater/statement_serializers/frequency_strategy/mixed_frequency_strategy.py
+-rw-rw-rw-   0        0        0     1278 2023-02-02 16:28:05.000000 shexer-2.1.0/shexer/io/shex/formater/statement_serializers/frequency_strategy/ratio_freq_serializer.py
+-rw-rw-rw-   0        0        0     1500 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/io/shex/formater/statement_serializers/inverse_statement_serializer.py
+-rw-rw-rw-   0        0        0     3211 2023-02-02 16:28:05.000000 shexer-2.1.0/shexer/io/shex/formater/statement_serializers/st_serializers_factory.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:08.050411 shexer-2.1.0/shexer/io/sparql/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/io/sparql/__init__.py
+-rw-rw-rw-   0        0        0     4538 2022-07-15 19:02:46.000000 shexer-2.1.0/shexer/io/sparql/query.py
+-rw-rw-rw-   0        0        0      469 2021-04-26 09:52:52.000000 shexer-2.1.0/shexer/io/wikidata.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:08.168413 shexer-2.1.0/shexer/model/
+-rw-rw-rw-   0        0        0      552 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/model/IRI.py
+-rw-rw-rw-   0        0        0      280 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/model/Literal.py
+-rw-rw-rw-   0        0        0      810 2021-01-14 17:50:12.000000 shexer-2.1.0/shexer/model/Macro.py
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/model/__init__.py
+-rw-rw-rw-   0        0        0      502 2021-10-04 17:33:25.000000 shexer-2.1.0/shexer/model/bnode.py
+-rw-rw-rw-   0        0        0      100 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/model/const_elem_types.py
+-rw-rw-rw-   0        0        0     1119 2023-02-02 16:28:05.000000 shexer-2.1.0/shexer/model/fixed_prop_choice_statement.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:08.195413 shexer-2.1.0/shexer/model/graph/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/model/graph/__init__.py
+-rw-rw-rw-   0        0        0     6186 2022-07-15 19:02:46.000000 shexer-2.1.0/shexer/model/graph/abstract_sgraph.py
+-rw-rw-rw-   0        0        0     7633 2023-04-04 10:53:17.000000 shexer-2.1.0/shexer/model/graph/endpoint_sgraph.py
+-rw-rw-rw-   0        0        0     6201 2023-04-04 17:24:52.000000 shexer-2.1.0/shexer/model/graph/rdflib_sgraph.py
+-rw-rw-rw-   0        0        0     4173 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/model/hierarchy_tree.py
+-rw-rw-rw-   0        0        0     2527 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/model/node_selector.py
+-rw-rw-rw-   0        0        0      427 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/model/property.py
+-rw-rw-rw-   0        0        0     3361 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/model/shape.py
+-rw-rw-rw-   0        0        0      858 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/model/shape_map.py
+-rw-rw-rw-   0        0        0     2716 2023-02-02 16:28:05.000000 shexer-2.1.0/shexer/model/statement.py
+-rw-rw-rw-   0        0        0    23678 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/shaper.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:08.306414 shexer-2.1.0/shexer/utils/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/utils/__init__.py
+-rw-rw-rw-   0        0        0      621 2022-08-11 11:37:45.000000 shexer-2.1.0/shexer/utils/compression.py
+-rw-rw-rw-   0        0        0       94 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/utils/dict.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:08.386414 shexer-2.1.0/shexer/utils/factories/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/utils/factories/__init__.py
+-rw-rw-rw-   0        0        0     4300 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/utils/factories/class_profiler_factory.py
+-rw-rw-rw-   0        0        0     2226 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/utils/factories/class_shexer_factory.py
+-rw-rw-rw-   0        0        0      728 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/utils/factories/h_tree.py
+-rw-rw-rw-   0        0        0    12215 2023-04-04 10:53:17.000000 shexer-2.1.0/shexer/utils/factories/instance_tracker_factory.py
+-rw-rw-rw-   0        0        0      437 2021-10-03 10:32:18.000000 shexer-2.1.0/shexer/utils/factories/iri_factory.py
+-rw-rw-rw-   0        0        0      286 2021-01-14 17:50:12.000000 shexer-2.1.0/shexer/utils/factories/remote_graph_factory.py
+-rw-rw-rw-   0        0        0     1985 2021-04-26 09:52:52.000000 shexer-2.1.0/shexer/utils/factories/shape_map_factory.py
+-rw-rw-rw-   0        0        0      616 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/utils/factories/shape_map_parser_factory.py
+-rw-rw-rw-   0        0        0     1723 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/utils/factories/shape_serializer_factory.py
+-rw-rw-rw-   0        0        0    18627 2023-04-04 10:53:17.000000 shexer-2.1.0/shexer/utils/factories/triple_yielders_factory.py
+-rw-rw-rw-   0        0        0      123 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/utils/file.py
+-rw-rw-rw-   0        0        0      397 2021-10-04 17:33:25.000000 shexer-2.1.0/shexer/utils/log.py
+-rw-rw-rw-   0        0        0      803 2021-01-14 17:50:12.000000 shexer-2.1.0/shexer/utils/namespaces.py
+-rw-rw-rw-   0        0        0      967 2019-11-23 19:24:28.000000 shexer-2.1.0/shexer/utils/obj_references.py
+-rw-rw-rw-   0        0        0     2008 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/utils/shapes.py
+-rw-rw-rw-   0        0        0     1397 2022-03-28 20:28:03.000000 shexer-2.1.0/shexer/utils/target_elements.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:08.420410 shexer-2.1.0/shexer/utils/translators/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:29.000000 shexer-2.1.0/shexer/utils/translators/__init__.py
+-rw-rw-rw-   0        0        0     2881 2021-04-26 09:52:52.000000 shexer-2.1.0/shexer/utils/translators/list_of_classes_to_shape_map.py
+-rw-rw-rw-   0        0        0     3026 2023-04-03 15:39:42.000000 shexer-2.1.0/shexer/utils/triple_yielders.py
+-rw-rw-rw-   0        0        0     5511 2023-04-06 19:32:13.000000 shexer-2.1.0/shexer/utils/uri.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:07.454408 shexer-2.1.0/shexer.egg-info/
+-rw-rw-rw-   0        0        0    25474 2023-04-06 19:33:07.000000 shexer-2.1.0/shexer.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     7726 2023-04-06 19:33:07.000000 shexer-2.1.0/shexer.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 19:33:07.000000 shexer-2.1.0/shexer.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       61 2023-04-06 19:33:07.000000 shexer-2.1.0/shexer.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       15 2023-04-06 19:33:07.000000 shexer-2.1.0/shexer.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:08.521409 shexer-2.1.0/test/
+-rw-rw-rw-   0        0        0        0 2021-01-14 17:50:12.000000 shexer-2.1.0/test/__init__.py
+-rw-rw-rw-   0        0        0     1903 2021-11-20 10:36:36.000000 shexer-2.1.0/test/const.py
+-rw-rw-rw-   0        0        0     8963 2023-04-03 18:35:42.000000 shexer-2.1.0/test/t_utils.py
+-rw-rw-rw-   0        0        0     1488 2022-08-10 11:13:26.000000 shexer-2.1.0/test/test_all_classes_mode.py
+-rw-rw-rw-   0        0        0     1525 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_allow_opt_cardinality.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:08.525411 shexer-2.1.0/test/test_bugs/
+-rw-rw-rw-   0        0        0        0 2022-03-28 20:28:03.000000 shexer-2.1.0/test/test_bugs/__init__.py
+-rw-rw-rw-   0        0        0      796 2022-03-28 20:28:03.000000 shexer-2.1.0/test/test_bugs/test_no_sharp_in_auto_shape_names.py
+-rw-rw-rw-   0        0        0     9920 2022-08-11 11:37:45.000000 shexer-2.1.0/test/test_compression_mode.py
+-rw-rw-rw-   0        0        0     2171 2023-02-02 16:28:05.000000 shexer-2.1.0/test/test_decimals.py
+-rw-rw-rw-   0        0        0     5564 2023-04-03 18:13:21.000000 shexer-2.1.0/test/test_depth_for_building_subgraph.py
+-rw-rw-rw-   0        0        0     3526 2023-04-06 19:32:13.000000 shexer-2.1.0/test/test_detect_minimal_iri.py
+-rw-rw-rw-   0        0        0     1388 2023-02-02 16:28:05.000000 shexer-2.1.0/test/test_disable_comments.py
+-rw-rw-rw-   0        0        0     2922 2023-04-04 10:53:17.000000 shexer-2.1.0/test/test_disable_endpoint_cache.py
+-rw-rw-rw-   0        0        0     1491 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_disable_exact_cardinality.py
+-rw-rw-rw-   0        0        0     2552 2023-04-03 18:35:42.000000 shexer-2.1.0/test/test_disable_or_statements.py
+-rw-rw-rw-   0        0        0     3786 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_discard_and_compliant.py
+-rw-rw-rw-   0        0        0     2090 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_file_target_classes.py
+-rw-rw-rw-   0        0        0     1677 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_graph_file_input.py
+-rw-rw-rw-   0        0        0     3456 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_graph_list_of_file_inputs.py
+-rw-rw-rw-   0        0        0     1951 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_infer_numeric_types_for_untyped_literals.py
+-rw-rw-rw-   0        0        0     7818 2023-02-02 16:28:05.000000 shexer-2.1.0/test/test_input_format.py
+-rw-rw-rw-   0        0        0     3367 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_instances_file_input.py
+-rw-rw-rw-   0        0        0     3852 2023-02-02 16:28:05.000000 shexer-2.1.0/test/test_instances_report.py
+-rw-rw-rw-   0        0        0     3548 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_instantiation_property.py
+-rw-rw-rw-   0        0        0     1964 2022-03-28 20:28:03.000000 shexer-2.1.0/test/test_inverse_paths.py
+-rw-rw-rw-   0        0        0     3594 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_keep_less_specific.py
+-rw-rw-rw-   0        0        0     4051 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_list_of_url_input.py
+-rw-rw-rw-   0        0        0     4106 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_namespaces_dict.py
+-rw-rw-rw-   0        0        0     2082 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_namespaces_to_ignore.py
+-rw-rw-rw-   0        0        0     5000 2021-01-14 17:50:12.000000 shexer-2.1.0/test/test_raw_graph.py
+-rw-rw-rw-   0        0        0     4300 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_raw_shape_map.py
+-rw-rw-rw-   0        0        0     1711 2022-07-15 19:02:46.000000 shexer-2.1.0/test/test_rdflib_graph.py
+-rw-rw-rw-   0        0        0     2930 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_remove_empty_sahpes.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:08.548446 shexer-2.1.0/test/test_shacl/
+-rw-rw-rw-   0        0        0        0 2021-04-26 09:52:52.000000 shexer-2.1.0/test/test_shacl/__init__.py
+-rw-rw-rw-   0        0        0     2225 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_shacl/test_annotation.py
+-rw-rw-rw-   0        0        0     2242 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_shacl/test_class_selection.py
+-rw-rw-rw-   0        0        0     3291 2023-04-06 19:32:13.000000 shexer-2.1.0/test/test_shacl/test_detect_minimal_iri.py
+-rw-rw-rw-   0        0        0      910 2022-03-28 20:28:03.000000 shexer-2.1.0/test/test_shacl/test_literal_types.py
+-rw-rw-rw-   0        0        0     4313 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_shape_map_file.py
+-rw-rw-rw-   0        0        0     6086 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_shape_map_format.py
+-rw-rw-rw-   0        0        0     2307 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_shape_qualifiers_mode.py
+-rw-rw-rw-   0        0        0     2889 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_shapes_namespaces.py
+-rw-rw-rw-   0        0        0     2452 2022-03-28 20:28:03.000000 shexer-2.1.0/test/test_sort.py
+-rw-rw-rw-   0        0        0     2058 2021-10-24 17:07:37.000000 shexer-2.1.0/test/test_target_classes.py
+-rw-rw-rw-   0        0        0     3120 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_threshold.py
+-rw-rw-rw-   0        0        0     2578 2023-04-03 18:13:27.000000 shexer-2.1.0/test/test_url_endpoint.py
+-rw-rw-rw-   0        0        0     1867 2022-07-15 19:02:46.000000 shexer-2.1.0/test/test_url_graph.py
+-rw-rw-rw-   0        0        0     1900 2021-10-03 10:32:18.000000 shexer-2.1.0/test/test_wikidata_annotation.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:08.573450 shexer-2.1.0/ws/
+-rw-rw-rw-   0        0        0        0 2019-11-23 19:24:29.000000 shexer-2.1.0/ws/__init__.py
+-rw-rw-rw-   0        0        0    19884 2022-03-28 20:28:03.000000 shexer-2.1.0/ws/shexer_rest.py
+-rw-rw-rw-   0        0        0       28 2019-11-23 19:24:29.000000 shexer-2.1.0/ws/wsgi.py
```

### Comparing `shexer-2.0.9/LICENSE` & `shexer-2.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/PKG-INFO` & `shexer-2.1.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: shexer
-Version: 2.0.9
+Version: 2.1.0
 Summary: Automatic schema extraction for RDF graphs
 Home-page: https://github.com/DaniFdezAlvarez/shexer
 Author: Daniel Fernandez-Alvarez
 Author-email: danifdezalvarez@gmail.com
 License: UNKNOWN
-Download-URL: https://github.com/DaniFdezAlvarez/shexer/archive/2.0.9.tar.gz
+Download-URL: https://github.com/DaniFdezAlvarez/shexer/archive/2.1.0.tar.gz
 Keywords: testing,shexer,shexerp3,rdf,shex,shacl,schema
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
@@ -199,14 +199,15 @@
 * raw_graph (default None): a simple raw string containing the target graph.
 * url_graph_input (default None): use it to provide a URL of some downloadable RDF content available online to be used as target graph.
 * list_of_url_input (default None): use it to provide several URLs of downloadable RDF content available online to be used as target graph.
 * url_endpoint (default None): it expects the URL of an SPARQL endpoint. Use it if you want to get some relevant triples form that endpoint instead of providing a whole RDF graph. In this case, the triples will be those ones whose subject is one of the nodes used to build the shapes (instances of a target class, result of a node selector in a shape map).
 * depth_for_building_subgraph (default 1): use this param just in case you are working against a SPARQL endpoint. This integer indicates the max distance from any seed node to consider in order to track a subgraph from the endpoint. Please, remind that a high depth can cause a massive number of queries and have a high performance cost. 
 * track_classes_for_entities_at_last_depth_level (default True): use this param just in case you are working against a SPARQL endpoint. If it set to True, it makes a step further to the distance to the seed nodes indicated in the param depth. However, it will just look for triples related to typing, not the whole neighborhood of the nodes in the last level of depth.
 * limit_remote_instances (default -1). Use this param if you are working against an endpoint using the param target_classes. If it is set to a positive number, sheXer will just get limit_remote_instances instances for each class from the endpoint (by adding LIMIT at the end of the sparql query). This is useful when working with big sources with tons on instances, causing too many or too heavy SPARQL queries to retrieve  all the content. 
+* disable_endpoint_cache (default False). By default, if sheXer is told to consume triples from an endpoint, it will make some SPARQL queries and store the results in a local graph. If this parameter is set to True, sheXer won't save that content locally. This will help to reduce main memory usage, but will decrease the performance, as sheXer will need to make more SPARQL queries to the endpoint.
 * namespaces_dict (default None): dictionary in which the keys are namespaces and the values are their expected prefixes in the outputs. 
 * input_format (default "NT"): the format of the graph which is going to be computed. The default value is const.NT. IMPORTANT: currently, sheXer does not guess input format, so ensure you specify the format here in case you are not providing n-triples content. In case you provide a combined input (several files, several URLs...) they all should have the same format. If you work against an endpoit, then this param do not have any effect.
 * compression_mode (default None). Only when you are working with local files, if they are compressed, you do not need to uncompress to parse them. Currently supported formats are ZIP and GZ. Set compression_format to "zip" or "gz" to work with such files. Each gz file will be assumed to contain a single graph file. Each zip file will be assumed to be a directory containing one or more graph files. In case the zip contains several files, they will be all parsed and merged (they should have the same format, indicated with input_format). In every case, sheXer won't write any uncompressed content to your disk.
 
 #### Params to tune the shexing process
 
 All this parameters have a default value so you do not need to use any of them. But you can modify the schema extraction in many different ways.
```

### Comparing `shexer-2.0.9/README.md` & `shexer-2.1.0/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -177,14 +177,15 @@
 * raw_graph (default None): a simple raw string containing the target graph.
 * url_graph_input (default None): use it to provide a URL of some downloadable RDF content available online to be used as target graph.
 * list_of_url_input (default None): use it to provide several URLs of downloadable RDF content available online to be used as target graph.
 * url_endpoint (default None): it expects the URL of an SPARQL endpoint. Use it if you want to get some relevant triples form that endpoint instead of providing a whole RDF graph. In this case, the triples will be those ones whose subject is one of the nodes used to build the shapes (instances of a target class, result of a node selector in a shape map).
 * depth_for_building_subgraph (default 1): use this param just in case you are working against a SPARQL endpoint. This integer indicates the max distance from any seed node to consider in order to track a subgraph from the endpoint. Please, remind that a high depth can cause a massive number of queries and have a high performance cost. 
 * track_classes_for_entities_at_last_depth_level (default True): use this param just in case you are working against a SPARQL endpoint. If it set to True, it makes a step further to the distance to the seed nodes indicated in the param depth. However, it will just look for triples related to typing, not the whole neighborhood of the nodes in the last level of depth.
 * limit_remote_instances (default -1). Use this param if you are working against an endpoint using the param target_classes. If it is set to a positive number, sheXer will just get limit_remote_instances instances for each class from the endpoint (by adding LIMIT at the end of the sparql query). This is useful when working with big sources with tons on instances, causing too many or too heavy SPARQL queries to retrieve  all the content. 
+* disable_endpoint_cache (default False). By default, if sheXer is told to consume triples from an endpoint, it will make some SPARQL queries and store the results in a local graph. If this parameter is set to True, sheXer won't save that content locally. This will help to reduce main memory usage, but will decrease the performance, as sheXer will need to make more SPARQL queries to the endpoint.
 * namespaces_dict (default None): dictionary in which the keys are namespaces and the values are their expected prefixes in the outputs. 
 * input_format (default "NT"): the format of the graph which is going to be computed. The default value is const.NT. IMPORTANT: currently, sheXer does not guess input format, so ensure you specify the format here in case you are not providing n-triples content. In case you provide a combined input (several files, several URLs...) they all should have the same format. If you work against an endpoit, then this param do not have any effect.
 * compression_mode (default None). Only when you are working with local files, if they are compressed, you do not need to uncompress to parse them. Currently supported formats are ZIP and GZ. Set compression_format to "zip" or "gz" to work with such files. Each gz file will be assumed to contain a single graph file. Each zip file will be assumed to be a directory containing one or more graph files. In case the zip contains several files, they will be all parsed and merged (they should have the same format, indicated with input_format). In every case, sheXer won't write any uncompressed content to your disk.
 
 #### Params to tune the shexing process
 
 All this parameters have a default value so you do not need to use any of them. But you can modify the schema extraction in many different ways.
```

### Comparing `shexer-2.0.9/setup.py` & `shexer-2.1.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,20 +4,20 @@
 def read(file_path):
 	with open(file_path, "r") as in_stream:
 		return in_stream.read()
 
 setup(
   name = 'shexer',
   packages = find_packages(exclude=["*.local_code.*"]), # this must be the same as the name above
-  version = '2.0.9',
+  version = '2.1.0',
   description = 'Automatic schema extraction for RDF graphs',
   author = 'Daniel Fernandez-Alvarez',
   author_email = 'danifdezalvarez@gmail.com',
   url = 'https://github.com/DaniFdezAlvarez/shexer',
-  download_url = 'https://github.com/DaniFdezAlvarez/shexer/archive/2.0.9.tar.gz',
+  download_url = 'https://github.com/DaniFdezAlvarez/shexer/archive/2.1.0.tar.gz',
   keywords = ['testing', 'shexer', 'shexerp3', "rdf", "shex", "shacl", "schema"],
   long_description = read('README.md'),
   long_description_content_type='text/markdown',
   classifiers=[
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
```

### Comparing `shexer-2.0.9/shexer/consts.py` & `shexer-2.1.0/shexer/consts.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/core/instances/abstract_instance_tracker.py` & `shexer-2.1.0/shexer/core/instances/abstract_instance_tracker.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/core/instances/annotators/annotator_tracking_instances.py` & `shexer-2.1.0/shexer/core/instances/annotators/annotator_tracking_instances.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/core/instances/annotators/base_annotator.py` & `shexer-2.1.0/shexer/core/instances/annotators/base_annotator.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/core/instances/annotators/strategy_mode/all_classes_mode.py` & `shexer-2.1.0/shexer/core/instances/annotators/strategy_mode/all_classes_mode.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/core/instances/annotators/strategy_mode/base_strategy_mode.py` & `shexer-2.1.0/shexer/core/instances/annotators/strategy_mode/base_strategy_mode.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/core/instances/annotators/strategy_mode/compound_strategy_mode.py` & `shexer-2.1.0/shexer/core/instances/annotators/strategy_mode/compound_strategy_mode.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/core/instances/annotators/strategy_mode/shape_qualifiers_mode.py` & `shexer-2.1.0/shexer/core/instances/annotators/strategy_mode/shape_qualifiers_mode.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/core/instances/annotators/strategy_mode/target_classes_mode.py` & `shexer-2.1.0/shexer/core/instances/annotators/strategy_mode/target_classes_mode.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/core/instances/instance_tracker.py` & `shexer-2.1.0/shexer/core/instances/instance_tracker.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/core/instances/mappings/shape_map_instance_tracker.py` & `shexer-2.1.0/shexer/core/instances/mappings/shape_map_instance_tracker.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/core/instances/mix/mixed_instance_tracker.py` & `shexer-2.1.0/shexer/core/instances/mix/mixed_instance_tracker.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/core/profiling/class_profiler.py` & `shexer-2.1.0/shexer/io/shex/formater/shex_serializer.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,150 +1,161 @@
-from shexer.utils.target_elements import determine_original_target_nodes_if_needed
+from shexer.core.profiling.class_profiler import RDF_TYPE_STR
+
 from shexer.model.property import Property
 from shexer.utils.uri import remove_corners
-from shexer.utils.target_elements import tune_target_classes_if_needed
-from shexer.consts import SHAPES_DEFAULT_NAMESPACE
-from shexer.utils.log import log_msg
-from shexer.core.profiling.strategy.direct_features_strategy import DirectFeaturesStrategy
-from shexer.core.profiling.strategy.include_reverse_features_strategy import IncludeReverseFeaturesStrategy
-from shexer.core.profiling.consts import RDF_TYPE_STR
-
-
-
-
-class ClassProfiler(object):
-
-    def __init__(self, triples_yielder, instances_dict, instantiation_property_str=RDF_TYPE_STR,
-                 remove_empty_shapes=True, original_target_classes=None, original_shape_map=None,
-                 shapes_namespace=SHAPES_DEFAULT_NAMESPACE, inverse_paths=False):
-        self._triples_yielder = triples_yielder
-        self._instances_dict = instances_dict  # TODO  refactor: change name once working again
-        # self._instances_shape_dict = {}
-        self._shapes_namespace = shapes_namespace
-        self._shape_names_dict = {}  # Will be filled during execution
-        self._relevant_triples = 0
+from shexer.utils.shapes import prefixize_shape_name_if_possible
+from shexer.io.shex.formater.consts import SPACES_LEVEL_INDENTATION
+from shexer.io.wikidata import wikidata_annotation
+from shexer.io.file import read_file
+from shexer.consts import RATIO_INSTANCES, ABSOLUTE_INSTANCES, MIXED_INSTANCES
+
+from wlighter import SHEXC_FORMAT
+
+_MODES_REPORT_INSTANCES = [ABSOLUTE_INSTANCES, MIXED_INSTANCES]
+
+class ShexSerializer(object):
+
+    def __init__(self, target_file, shapes_list, namespaces_dict=None, string_return=False,
+                 instantiation_property_str=RDF_TYPE_STR, disable_comments=False, wikidata_annotation=False,
+                 instances_report_mode=RATIO_INSTANCES, detect_minimal_iri=False):
+        self._target_file = target_file
+        self._shapes_list = shapes_list
+        self._lines_buffer = []
+        self._namespaces_dict = namespaces_dict if namespaces_dict is not None else {}
+        self._string_return = string_return
         self._instantiation_property_str = self._decide_instantiation_property(instantiation_property_str)
-        self._remove_empty_shapes = remove_empty_shapes
-        self._original_raw_target_classes = original_target_classes
-        self._classes_shape_dict = {}  # Will be filled later
-        self._class_counts = {}  # Will be filled later
-        self._original_target_nodes = determine_original_target_nodes_if_needed(remove_empty_shapes=remove_empty_shapes,
-                                                                                original_target_classes=original_target_classes,
-                                                                                original_shape_map=original_shape_map,
-                                                                                shapes_namespace=shapes_namespace)
-        self._strategy = DirectFeaturesStrategy(class_profiler=self) if not inverse_paths \
-            else IncludeReverseFeaturesStrategy(class_profiler=self)
-
-
-    def profile_classes(self, verbose):
-        log_msg(verbose=verbose,
-                msg="Starting class profiler...")
-        self._init_class_counts_and_shape_dict()
-        log_msg(verbose=verbose,
-                msg="Instance counts completed. Annotating instance features...")
-        self._adapt_instances_dict()
-        self._build_shape_of_instances()
-        log_msg(verbose=verbose,
-                msg="Instance features annotated. Number of relevant triples computed: {}. "
-                    "Building shape profiles...".format(self._relevant_triples))
-
-        self._build_class_profile()
-        log_msg(verbose=verbose,
-                msg="Draft shape profiles built. Cleaning shape profiles...")
-        self._clean_class_profile()
-        log_msg(verbose=verbose,
-                msg="Shape profiles done. Working with {} shapes.".format(len(self._classes_shape_dict)))
-        return self._classes_shape_dict, self._class_counts
-
-    def get_target_classes_dict(self):
-        return self._instances_dict
+        self._disable_comments = disable_comments
+        self._wikidata_annotation = wikidata_annotation
+        self._instances_report_mode = instances_report_mode
+        self._detect_minimal_iri = detect_minimal_iri
+
+        self._string_result = ""
+
+    def serialize_shapes(self):
+
+        self._reset_target_file()
+        self._serialize_namespaces()
+        for a_shape in self._shapes_list:
+            self._serialize_shape(a_shape)
+        self._flush()
+        if self._wikidata_annotation:
+            self._annotate_wikidata_ids_in_result()
+        if self._string_return:
+            return self._string_result
 
     @staticmethod
     def _decide_instantiation_property(instantiation_property_str):
         if instantiation_property_str == None:
             return RDF_TYPE_STR
         if type(instantiation_property_str) == Property:
             return str(instantiation_property_str)
         if type(instantiation_property_str) == str:
             return remove_corners(a_uri=instantiation_property_str,
                                   raise_error_if_no_corners=False)
         raise ValueError("Unrecognized param type to define instantiation property")
 
+    def _annotate_wikidata_ids_in_result(self):
+        self._string_result =  wikidata_annotation(raw_input=self._get_raw_input_for_wikidata_annotation(),
+                                                   string_return=self._string_return,
+                                                   out_file=self._target_file,
+                                                   format=SHEXC_FORMAT,
+                                                   rdfs_comments=True)
+
+    def _get_raw_input_for_wikidata_annotation(self):
+        if self._string_return:
+            return self._string_result
+        return read_file(self._target_file)
+
+
+    def _serialize_namespaces(self):
+        for a_namespace in self._namespaces_dict:
+            self._write_line(self._prefix_line(a_namespace), 0)
+        self._write_line("", 0)
+
+    def _prefix_line(self, namespace_key):
+        return "PREFIX " + self._namespaces_dict[namespace_key] + ": <" + namespace_key + ">"
+
+    def _serialize_empty_namespace(self):
+        self._write_line("PREFIX : <http://weso.es/shapes/>")
+
+    def _serialize_shape(self, a_shape):
+        self._serialize_shape_name(a_shape)
+        self._serialize_opening_of_rules()
+        self._serialize_shape_rules(a_shape)
+        self._serialize_closure_of_rule()
+        self._serialize_shape_gap()
+
+    def _flush(self):
+        self._write_lines_buffer()
+
+    def _write_line(self, a_line, indent_level=0):
+        self._lines_buffer.append(self._indentation_spaces(indent_level) + a_line + "\n")
+        if len(self._lines_buffer) >= 5000:
+            self._write_lines_buffer()
+            self._lines_buffer = []
 
-    def _init_class_counts_and_shape_dict(self):
-        """
-        IMPORTANT: this method should be called before adapting the instances_dict
-
-        :return:
-        """
-        # self._classes_shape_dict
-        self._init_original_targets()
-        self._init_annotated_targets()
-
-
-    def _init_annotated_targets(self):
-        self._strategy.init_annotated_targets()
-
-    def _init_original_targets(self):
-        self._strategy.init_original_targets()
-
-    def _build_class_profile(self):
-        for an_instance in self._instances_dict:
-            self._strategy.annotate_instance_features(an_instance)
-
-    def _clean_class_profile(self):
-        if not self._remove_empty_shapes:
+    def _reset_target_file(self):
+        if self._string_return:
             return
-        shapes_to_remove = self._detect_shapes_to_remove()
-
-        while(len(shapes_to_remove) != 0):
-            self._iteration_remove_empty_shapes(shapes_to_remove)
-            shapes_to_remove = self._detect_shapes_to_remove()
-
-    def _detect_shapes_to_remove(self):
-        shapes_to_remove = set()
-        for a_shape_key in self._classes_shape_dict:
-            if not self._is_original_target_shape(a_shape_key):
-                if not self._has_it_annotated_features(a_shape_key):
-                    shapes_to_remove.add(a_shape_key)
-        return shapes_to_remove
-
-    def _is_original_target_shape(self, shape_label):
-        return shape_label in self._original_target_nodes
-
-    def _has_it_annotated_features(self, shape_label):
-        return self._strategy.has_shape_annotated_features(shape_label)
-
-    def _iteration_remove_empty_shapes(self, target_shapes):
-        for a_shape_label_key in self._classes_shape_dict:
-            for a_prop_key in self._classes_shape_dict[a_shape_label_key]:
-                # print(self._classes_shape_dict[a_shape_label_key][a_prop_key])
-                for a_shape_to_remove in target_shapes:
-                    if a_shape_to_remove in self._classes_shape_dict[a_shape_label_key][a_prop_key]:
-                        del self._classes_shape_dict[a_shape_label_key][a_prop_key][a_shape_to_remove]
-        for a_shape_to_remove in target_shapes:
-            if a_shape_to_remove in self._classes_shape_dict:
-                del self._classes_shape_dict[a_shape_to_remove]
-
-    def _build_shape_of_instances(self):
-        for a_triple in self._yield_relevant_triples():
-            self._relevant_triples += 1
-            self._annotate_feature_of_target_instance(a_triple)
-
-    def _annotate_feature_of_target_instance(self, a_triple):
-        self._strategy.annotate_triple_features(a_triple)
-
-    def _adapt_instances_dict(self):
-        self._strategy.adapt_instances_dict()
-
-    def _adapt_entry_dict_if_needed(self, str_subj):
-        if type(self._instances_dict[str_subj]) == list:
-            self._instances_dict[str_subj] = (self._instances_dict[str_subj], {})
-
-    def _yield_relevant_triples(self):
-        for a_triple in self._triples_yielder.yield_triples():
-            if self._strategy.is_a_relevant_triple(a_triple):
-                yield a_triple
-
-
+        with open(self._target_file, "w") as out_stream:
+            out_stream.write("")  # Is this necessary? maybe enough to open it in 'w' mode?
 
+    def _write_lines_buffer(self):
+        if self._string_return:
+            self._string_result += "".join(self._lines_buffer)
+        else:
+            with open(self._target_file, "a") as out_stream:
+                for a_line in self._lines_buffer:
+                    out_stream.write(a_line)
+
+    def _indentation_spaces(self, indent_level):
+        result = ""
+        for i in range(0, indent_level):
+            result += SPACES_LEVEL_INDENTATION
+        return result
 
+    def _serialize_shape_rules(self, a_shape):
+        if a_shape.n_statements == 0:
+            return
+        statements = [a_statement for a_statement in a_shape.yield_statements()]
+        for i in range(0, len(statements) - 1):
+            for line_indent_tuple in statements[i]. \
+                    get_tuples_to_serialize_line_indent_level(is_last_statement_of_shape=False,
+                                                              namespaces_dict=self._namespaces_dict):
+                self._write_line(a_line=line_indent_tuple[0],
+                                 indent_level=line_indent_tuple[1])
+        for line_indent_tuple in statements[len(statements) - 1]. \
+                get_tuples_to_serialize_line_indent_level(is_last_statement_of_shape=True,
+                                                          namespaces_dict=self._namespaces_dict):
+            self._write_line(a_line=line_indent_tuple[0],
+                             indent_level=line_indent_tuple[1])
+
+    def _serialize_shape_name(self, a_shape):
+        self._write_line(
+
+            prefixize_shape_name_if_possible(a_shape_name=a_shape.name,
+                                             namespaces_prefix_dict=self._namespaces_dict) +
+            self._minimal_iri(a_shape=a_shape) +
+            self._instance_count(a_shape)
+        )
+
+    def _minimal_iri(self, a_shape):
+        if not self._detect_minimal_iri or a_shape.iri_pattern is None:
+            return ""
+        return "  [{}~]  AND".format(a_shape.iri_pattern)
+
+    def _instance_count(self, a_shape):
+        return "   # {} instance{}".format(a_shape.n_instances,
+                                           "" if a_shape.n_instances == 1 else "s") \
+            if self._instances_report_mode in _MODES_REPORT_INSTANCES and \
+                     not self._disable_comments \
+            else ""
+
+    def _serialize_opening_of_rules(self):
+        self._write_line("{")
+
+    def _serialize_closure_of_rule(self):
+        self._write_line("}")
+
+    def _serialize_shape_gap(self):
+        self._write_line("")
+        self._write_line("")
```

### Comparing `shexer-2.0.9/shexer/core/profiling/strategy/abstract_strategy.py` & `shexer-2.1.0/shexer/core/profiling/strategy/abstract_feature_direction_strategy.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from shexer.utils.shapes import build_shapes_name_for_class_uri
 from shexer.core.profiling.consts import POS_CLASSES, _S, _P, _O, POS_FEATURES_DIRECT, _ONE_TO_MANY, POS_FEATURES_INVERSE
 from shexer.model.IRI import IRI_ELEM_TYPE, IRI
 
-class AbstractStrategy(object):
+class AbstractFeatureDirectionStrategy(object):
 
     def __init__(self, class_profiler):
         self._class_profiler = class_profiler
         self._i_dict = self._class_profiler._instances_dict
         self._c_shapes_dict = self._class_profiler._classes_shape_dict
         self._c_counts = self._class_profiler._class_counts
         self._shape_names_dict = self._class_profiler._shape_names_dict
```

### Comparing `shexer-2.0.9/shexer/core/profiling/strategy/direct_features_strategy.py` & `shexer-2.1.0/shexer/core/profiling/strategy/direct_features_strategy.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 
-from shexer.core.profiling.strategy.abstract_strategy import AbstractStrategy
+from shexer.core.profiling.strategy.abstract_feature_direction_strategy import AbstractFeatureDirectionStrategy
 from shexer.core.profiling.consts import _S
 
 
-class DirectFeaturesStrategy(AbstractStrategy):
+class DirectFeaturesStrategy(AbstractFeatureDirectionStrategy):
 
     def __init__(self, class_profiler):
         super().__init__(class_profiler)
 
 
     def adapt_instances_dict(self):
         for a_subj_key in self._i_dict:
```

### Comparing `shexer-2.0.9/shexer/core/profiling/strategy/include_reverse_features_strategy.py` & `shexer-2.1.0/shexer/core/profiling/strategy/include_reverse_features_strategy.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
-from shexer.core.profiling.strategy.abstract_strategy import AbstractStrategy
+from shexer.core.profiling.strategy.abstract_feature_direction_strategy import AbstractFeatureDirectionStrategy
 from shexer.core.profiling.consts import _S, _P, _O, POS_FEATURES_INVERSE, POS_CLASSES
 from shexer.model.IRI import IRI_ELEM_TYPE
 
 _C_MAP_POS_DIRECT = 0
 _C_MAP_POS_INVERSE = 1
 
 
-class IncludeReverseFeaturesStrategy(AbstractStrategy):
+class IncludeReverseFeaturesStrategy(AbstractFeatureDirectionStrategy):
 
 
     def adapt_instances_dict(self):
         for a_subj_key in self._i_dict:
             self._i_dict[a_subj_key] = (self._i_dict[a_subj_key], {}, {})
 
     def __init__(self, class_profiler):
```

### Comparing `shexer-2.0.9/shexer/core/shexing/class_shexer.py` & `shexer-2.1.0/shexer/core/shexing/class_shexer.py`

 * *Files 9% similar despite different names*

```diff
@@ -13,18 +13,21 @@
     def __init__(self, class_counts_dict, class_profile_dict=None, class_profile_json_file=None,
                  remove_empty_shapes=True, original_target_classes=None, original_shape_map=None,
                  discard_useless_constraints_with_positive_closure=True, keep_less_specific=True,
                  all_compliant_mode=True, instantiation_property=RDF_TYPE, disable_or_statements=True,
                  disable_comments=False, namespaces_dict=None, tolerance_to_keep_similar_rules=0,
                  allow_opt_cardinality=True, disable_exact_cardinality=False,
                  shapes_namespace=SHAPES_DEFAULT_NAMESPACE, inverse_paths=False,
-                 decimals=-1, instances_report_mode=RATIO_INSTANCES):
+                 decimals=-1, instances_report_mode=RATIO_INSTANCES, detect_minimal_iri=False,
+                 class_min_iris_dict=None):
         self._class_counts_dict = class_counts_dict
         self._class_profile_dict = class_profile_dict if class_profile_dict is not None else self._load_class_profile_dict_from_file(
             class_profile_json_file)
+        self._class_min_iris_dict = class_min_iris_dict
+
         self._shapes_list = []
         self._remove_empty_shapes = remove_empty_shapes
         self._all_compliant_mode = all_compliant_mode
         self._disable_or_statements = disable_or_statements
         self._instantiation_property_str = str(instantiation_property)
         self._disable_comments = disable_comments
         self._discard_useless_positive_closures = discard_useless_constraints_with_positive_closure
@@ -32,14 +35,15 @@
         self._keep_less_specific = keep_less_specific
         self._tolerance = tolerance_to_keep_similar_rules
         self._allow_opt_cardinality = allow_opt_cardinality
         self._disable_exact_cardinality = disable_exact_cardinality
         self._shapes_namespace = shapes_namespace
         self._decimals = decimals
         self._instances_report_mode = instances_report_mode
+        self._detect_minimal_iri = detect_minimal_iri
 
         self._original_target_nodes = determine_original_target_nodes_if_needed(remove_empty_shapes=remove_empty_shapes,
                                                                                 original_target_classes=original_target_classes,
                                                                                 original_shape_map=original_shape_map,
                                                                                 shapes_namespace=shapes_namespace)
         self._strategy = DirectShexingStrategy(self) if not inverse_paths \
             else DirectAndInverseShexingStrategy(self)
```

### Comparing `shexer-2.0.9/shexer/core/shexing/strategy/asbtract_shexing_strategy.py` & `shexer-2.1.0/shexer/core/shexing/strategy/abstract_shexing_strategy.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from shexer.model.statement import POSITIVE_CLOSURE, KLEENE_CLOSURE, OPT_CARDINALITY
 from shexer.model.IRI import IRI_ELEM_TYPE
 from shexer.model.fixed_prop_choice_statement import FixedPropChoiceStatement
 from shexer.io.shex.formater.statement_serializers.st_serializers_factory import StSerializerFactory
-from shexer.io.shex.formater.statement_serializers.fixed_prop_choice_statement_serializer import \
-    FixedPropChoiceStatementSerializer  # TODO: REPFACTOR
+from shexer.core.shexing.strategy.minimal_iri_strategy.annotate_min_iri_strategy import AnnotateMinIriStrategy
+from shexer.core.shexing.strategy.minimal_iri_strategy.ignore_min_iri_strategy import IgnoreMinIriStrategy
 
 
 _DIRECT_ST_SERIALIZER = 0
 _INVERSE_ST_SERIALIZER = 1
 
 
 class AbstractShexingStrategy(object):
@@ -21,21 +21,30 @@
         self._keep_less_specific = self._class_shexer._keep_less_specific
         self._discard_useless_positive_closures = self._class_shexer._discard_useless_positive_closures
         self._tolerance = self._class_shexer._tolerance
         self._disable_or_statements = self._class_shexer._disable_or_statements
         self._all_compliant_mode = self._class_shexer._all_compliant_mode
         self._disable_exact_cardinality = self._class_shexer._disable_exact_cardinality
 
+        self._strategy_min_iri = AnnotateMinIriStrategy(class_shexer._class_min_iris_dict) \
+            if class_shexer._detect_minimal_iri \
+            else IgnoreMinIriStrategy()
+
         self._statement_serializer_factory = StSerializerFactory(freq_mode=class_shexer._instances_report_mode,
                                                                  decimals=class_shexer._decimals,
                                                                  instantiation_property_str=self._instantiation_property_str,
                                                                  disable_comments=self._disable_comments)
 
 
     def yield_base_shapes(self, acceptance_threshold):
+        for a_shape in self._yield_base_shapes_direction_aware(acceptance_threshold=acceptance_threshold):
+            self._strategy_min_iri.annotate_shape_iri(a_shape)
+            yield a_shape
+
+    def _yield_base_shapes_direction_aware(self, acceptance_threshold):
         raise NotImplementedError()
 
     def set_valid_shape_constraints(self, shape):
         raise NotImplementedError()
 
     def remove_statements_to_gone_shapes(self, shape, shape_names_to_remove):
         raise NotImplementedError()
```

### Comparing `shexer-2.0.9/shexer/core/shexing/strategy/direct_and_inverse_shexing_strategy.py` & `shexer-2.1.0/shexer/core/shexing/strategy/direct_and_inverse_shexing_strategy.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from shexer.core.shexing.strategy.asbtract_shexing_strategy import AbstractShexingStrategy
+from shexer.core.shexing.strategy.abstract_shexing_strategy import AbstractShexingStrategy
 from shexer.utils.shapes import build_shapes_name_for_class_uri
 from shexer.model.statement import Statement
 from shexer.model.shape import Shape
 
 _POS_FEATURES_DIRECT = 0
 _POS_FEATURES_INVERSE = 1
 
@@ -19,15 +19,15 @@
         shape.direct_statements = self._statements_without_shapes_to_remove(
             original_statements=shape.direct_statements,
             shape_names_to_remove=shape_names_to_remove)
         shape.inverse_statements = self._statements_without_shapes_to_remove(
             original_statements=shape.inverse_statements,
             shape_names_to_remove=shape_names_to_remove)
 
-    def yield_base_shapes(self, acceptance_threshold):
+    def _yield_base_shapes_direction_aware(self, acceptance_threshold):
         for a_class_key in self._class_profile_dict:
             name = build_shapes_name_for_class_uri(class_uri=a_class_key,
                                                    shapes_namespace=self._shapes_namespace)
             number_of_instances = float(self._class_counts_dict[a_class_key])
 
             direct_statements = self._build_base_direct_statements(acceptance_threshold, a_class_key,
                                                                    number_of_instances)
```

### Comparing `shexer-2.0.9/shexer/core/shexing/strategy/direct_shexing_strategy.py` & `shexer-2.1.0/shexer/core/shexing/strategy/direct_shexing_strategy.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from shexer.core.shexing.strategy.asbtract_shexing_strategy import AbstractShexingStrategy
+from shexer.core.shexing.strategy.abstract_shexing_strategy import AbstractShexingStrategy
 from shexer.utils.shapes import build_shapes_name_for_class_uri
 from shexer.model.statement import Statement
 from shexer.model.shape import Shape
 
 class DirectShexingStrategy(AbstractShexingStrategy):
 
     def __init__(self, class_shexer):
@@ -17,15 +17,15 @@
 
     def set_valid_shape_constraints(self, shape):
         valid_statements = self._select_valid_statements_of_shape(shape.direct_statements)
         self._tune_list_of_valid_statements(valid_statements=valid_statements)
         shape.statements = valid_statements
 
 
-    def yield_base_shapes(self, acceptance_threshold):
+    def _yield_base_shapes_direction_aware(self, acceptance_threshold):
         for a_class_key in self._class_profile_dict:
             name = build_shapes_name_for_class_uri(class_uri=a_class_key,
                                                    shapes_namespace=self._shapes_namespace)
             number_of_instances = float(self._class_counts_dict[a_class_key])
             statements = []
             for a_prop_key in self._class_profile_dict[a_class_key]:
                 for a_type_key in self._class_profile_dict[a_class_key][a_prop_key]:
```

### Comparing `shexer-2.0.9/shexer/io/graph/yielder/base_triples_yielder.py` & `shexer-2.1.0/shexer/io/graph/yielder/base_triples_yielder.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/graph/yielder/big_ttl_triples_yielder.py` & `shexer-2.1.0/shexer/io/graph/yielder/big_ttl_triples_yielder.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/graph/yielder/filter/filter_namespaces_triple_yielder.py` & `shexer-2.1.0/shexer/io/graph/yielder/filter/filter_namespaces_triple_yielder.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/graph/yielder/multi_big_ttl_files_triple_yielder.py` & `shexer-2.1.0/shexer/io/graph/yielder/multi_big_ttl_files_triple_yielder.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/graph/yielder/multi_nt_triples_yielder.py` & `shexer-2.1.0/shexer/io/graph/yielder/multi_nt_triples_yielder.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/graph/yielder/multi_rdflib_triple_yielder.py` & `shexer-2.1.0/shexer/io/graph/yielder/multi_rdflib_triple_yielder.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/graph/yielder/multi_tsv_nt_triples_yielder.py` & `shexer-2.1.0/shexer/io/graph/yielder/multi_tsv_nt_triples_yielder.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/graph/yielder/multifile_base_triples_yielder.py` & `shexer-2.1.0/shexer/io/graph/yielder/multifile_base_triples_yielder.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/graph/yielder/nt_triples_yielder.py` & `shexer-2.1.0/shexer/io/graph/yielder/nt_triples_yielder.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/graph/yielder/rdflib_triple_yielder.py` & `shexer-2.1.0/shexer/io/graph/yielder/rdflib_triple_yielder.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/graph/yielder/remote/sgraph_from_selectors_triple_yielder.py` & `shexer-2.1.0/shexer/io/graph/yielder/remote/sgraph_from_selectors_triple_yielder.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/graph/yielder/tsv_nt_triples_yielder.py` & `shexer-2.1.0/shexer/io/graph/yielder/tsv_nt_triples_yielder.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/shacl/formater/shacl_serializer.py` & `shexer-2.1.0/shexer/io/shacl/formater/shacl_serializer.py`

 * *Files 1% similar despite different names*

```diff
@@ -27,14 +27,16 @@
 
 _R_SHACL_DATATYPE_PROP = URIRef(_SHACL_NAMESPACE + "dataType")
 _R_SHACL_NODEKIND_PROP = URIRef(_SHACL_NAMESPACE + "nodeKind")
 _R_SHACL_NODE_PROP = URIRef(_SHACL_NAMESPACE + "node")
 
 _R_SHACL_IN_PROP = URIRef(_SHACL_NAMESPACE + "in")
 
+_R_SHACL_PATTERN_PROP = URIRef(_SHACL_NAMESPACE + "pattern")
+
 _R_SHACL_NODEKIND_IRI = URIRef(_SHACL_NAMESPACE + "IRI")
 _R_SHACL_NODEKIND_LITERAL = URIRef(_SHACL_NAMESPACE + "Literal")
 _R_SHACL_NODEKIND_BNODE = URIRef(_SHACL_NAMESPACE + "BlankNode")
 _R_SHACL_NODEKIND_DOT = None
 
 _R_LANG_STRING = URIRef("http://www.w3.org/2000/01/rdf-schema#langString")
 
@@ -46,21 +48,23 @@
                   DOT_ELEM_TYPE: _R_SHACL_NODEKIND_BNODE,
                   BNODE_ELEM_TYPE: _R_SHACL_NODEKIND_DOT}
 
 
 class ShaclSerializer(object):
 
     def __init__(self, target_file, shapes_list, namespaces_dict=None, string_return=False,
-                 instantiation_property_str=RDF_TYPE_STR, wikidata_annotation=False):
+                 instantiation_property_str=RDF_TYPE_STR, wikidata_annotation=False,
+                 detect_minimal_iri=False):
         self._target_file = target_file
         self._namespaces_dict = namespaces_dict if namespaces_dict is not None else {}
         self._shapes_list = shapes_list
         self._string_return = string_return
         self._instantiation_property_str = instantiation_property_str
         self._wikidata_annotation = wikidata_annotation
+        self._detect_minimal_iri=detect_minimal_iri
 
         self._g_shapes = Graph()
 
         # self._uri_dict = {}
 
     def serialize_shapes(self):
         self._add_namespaces()
@@ -109,23 +113,35 @@
             self._add_shape(a_shape)
 
     def _add_shape(self, shape):
         r_shape_uri = self._generate_shape_uri(shape_name=shape.name)
         self._add_shape_uri(r_shape_uri=r_shape_uri)
         self._add_target_class(r_shape_uri=r_shape_uri,
                                shape=shape)
+        self._add_min_iri(r_shape_uri=r_shape_uri,
+                          shape=shape)
         self._add_shape_constraints(shape=shape,
                                     r_shape_uri=r_shape_uri)
 
+
     def _add_target_class(self, shape, r_shape_uri):
         if shape.class_uri is not None:
             self._add_triple(r_shape_uri,
                              _R_SHACL_TARGET_CLASS_PROP,
                              URIRef(shape.class_uri))  # TODO check if this is always an abs. URI, not sure
 
+    def _add_min_iri (self, shape, r_shape_uri):
+        if shape.iri_pattern is not None:
+            self._add_triple(r_shape_uri,
+                             _R_SHACL_PATTERN_PROP,
+                             self._literal_iri_pattern(shape))
+
+    def _literal_iri_pattern(self, shape):
+        return Literal("^{}".format(shape.iri_pattern))
+
     def _add_shape_constraints(self, shape, r_shape_uri):
         for a_statement in shape.yield_statements():
             self._add_constraint(statement=a_statement,
                                  r_shape_uri=r_shape_uri)
 
     def _is_instantiation_property(self, str_property):
         return str_property == self._instantiation_property_str
```

### Comparing `shexer-2.0.9/shexer/io/shape_map/label/shape_map_label_parser.py` & `shexer-2.1.0/shexer/io/shape_map/label/shape_map_label_parser.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/shape_map/node_selector/node_selector_parser.py` & `shexer-2.1.0/shexer/io/shape_map/node_selector/node_selector_parser.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/shape_map/shape_map_parser.py` & `shexer-2.1.0/shexer/io/shape_map/shape_map_parser.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/shex/formater/statement_serializers/base_statement_serializer.py` & `shexer-2.1.0/shexer/io/shex/formater/statement_serializers/base_statement_serializer.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/shex/formater/statement_serializers/fixed_prop_choice_statement_serializer.py` & `shexer-2.1.0/shexer/io/shex/formater/statement_serializers/fixed_prop_choice_statement_serializer.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/shex/formater/statement_serializers/frequency_strategy/mixed_frequency_strategy.py` & `shexer-2.1.0/shexer/io/shex/formater/statement_serializers/frequency_strategy/mixed_frequency_strategy.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/shex/formater/statement_serializers/frequency_strategy/ratio_freq_serializer.py` & `shexer-2.1.0/shexer/io/shex/formater/statement_serializers/frequency_strategy/ratio_freq_serializer.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/shex/formater/statement_serializers/inverse_statement_serializer.py` & `shexer-2.1.0/shexer/io/shex/formater/statement_serializers/inverse_statement_serializer.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/shex/formater/statement_serializers/st_serializers_factory.py` & `shexer-2.1.0/shexer/io/shex/formater/statement_serializers/st_serializers_factory.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/io/sparql/query.py` & `shexer-2.1.0/shexer/io/sparql/query.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/model/IRI.py` & `shexer-2.1.0/shexer/model/IRI.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/model/Macro.py` & `shexer-2.1.0/shexer/model/Macro.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/model/fixed_prop_choice_statement.py` & `shexer-2.1.0/shexer/model/fixed_prop_choice_statement.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/model/graph/abstract_sgraph.py` & `shexer-2.1.0/shexer/model/graph/abstract_sgraph.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/model/graph/endpoint_sgraph.py` & `shexer-2.1.0/shexer/model/graph/endpoint_sgraph.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/model/graph/rdflib_sgraph.py` & `shexer-2.1.0/shexer/model/graph/rdflib_sgraph.py`

 * *Files 2% similar despite different names*

```diff
@@ -110,20 +110,19 @@
             result.parse(source=source, format=format)
         else:
             result.parse(data=raw_graph, format=format)
         return result
 
     def _add_lang_if_needed(self, rdflib_obj):
         """
-        It return a string representation with lang if it is a langString
+        It returns a string representation with lang if it is a langString
         :param rdflib_obj:
         :return:
         """
-        result = str(rdflib_obj)
         if type(rdflib_obj) == Literal and rdflib_obj.language is not None:
-            result = '"' + result + '"@' + rdflib_obj.language
-        return result
+           return '"' + str(rdflib_obj) + '"@' + rdflib_obj.language
+        return rdflib_obj
 
     def _add_URI_corners_if_needed(self, rdflib_obj):
         if type(rdflib_obj) == URIRef:
             return "<"+ str(rdflib_obj) + ">"
         return str(rdflib_obj)
```

### Comparing `shexer-2.0.9/shexer/model/hierarchy_tree.py` & `shexer-2.1.0/shexer/model/hierarchy_tree.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/model/node_selector.py` & `shexer-2.1.0/shexer/model/node_selector.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/model/shape.py` & `shexer-2.1.0/shexer/model/shape.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,21 +1,22 @@
 STARTING_CHAR_FOR_SHAPE_NAME = "@"
 
 
 class Shape(object):
 
-    def __init__(self, name, class_uri, statements, n_instances):
+    def __init__(self, name, class_uri, statements, n_instances, iri_pattern=None):
         self._name = name
         self._class_uri = class_uri
         self._statements = statements if statements is not None else []
         self._n_instances = n_instances
         # self._inverse_statements = inverse_statements if inverse_statements is not None else []
         self._sorting_callback = lambda x: x.probability
         self._n_direct_statements = self._count_direct_statements(statements)
         self._n_inverse_statements = len(statements) - self._n_direct_statements
+        self._iri_pattern = iri_pattern
 
     @property
     def name(self):
         return self._name
 
     @property
     def class_uri(self):
@@ -34,14 +35,22 @@
         return self._n_inverse_statements
 
     @property
     def n_instances(self):
         return self._n_instances
 
     @property
+    def iri_pattern(self):
+        return self._iri_pattern
+
+    @iri_pattern.setter
+    def iri_pattern(self, value):
+        self._iri_pattern = value
+
+    @property
     def statements(self):
         return self._statements
 
     @property
     def direct_statements(self):
         return [a_statement for a_statement in self._statements if not a_statement.is_inverse]
```

### Comparing `shexer-2.0.9/shexer/model/shape_map.py` & `shexer-2.1.0/shexer/model/shape_map.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/model/statement.py` & `shexer-2.1.0/shexer/model/statement.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/shaper.py` & `shexer-2.1.0/shexer/shaper.py`

 * *Files 16% similar despite different names*

```diff
@@ -53,31 +53,59 @@
                  limit_remote_instances=-1,
                  wikidata_annotation=False,
                  inverse_paths=False,
                  compression_mode=None,
                  decimals=-1,
                  instances_report_mode=RATIO_INSTANCES,
                  disable_endpoint_cache=False,
+                 detect_minimal_iri=False
                  ):
         """
 
         :param target_classes:
         :param file_target_classes:
         :param input_format:
         :param instances_file_input:
         :param graph_file_input:
         :param graph_list_of_files_input:
+        :param raw_graph:
+        :param url_graph_input:
+        :param rdflib_graph:
+        :param list_of_url_input:
         :param namespaces_dict:
-        :param namespaces_dict_file:
         :param instantiation_property:
         :param namespaces_to_ignore:
         :param infer_numeric_types_for_untyped_literals:
         :param discard_useless_constraints_with_positive_closure:
         :param all_instances_are_compliant_mode:
         :param keep_less_specific:
+        :param all_classes_mode:
+        :param shape_map_file:
+        :param shape_map_raw:
+        :param depth_for_building_subgraph:
+        :param track_classes_for_entities_at_last_depth_level:
+        :param strict_syntax_with_corners:
+        :param url_endpoint:
+        :param shape_map_format:
+        :param shape_qualifiers_mode:
+        :param namespaces_for_qualifier_props:
+        :param remove_empty_shapes:
+        :param disable_comments:
+        :param disable_or_statements:
+        :param allow_opt_cardinality:
+        :param disable_exact_cardinality:
+        :param shapes_namespace:
+        :param limit_remote_instances:
+        :param wikidata_annotation:
+        :param inverse_paths:
+        :param compression_mode:
+        :param decimals:
+        :param instances_report_mode:
+        :param disable_endpoint_cache:
+        :param detect_minimal_iri:
         """
 
         check_just_one_not_none((graph_file_input, "graph_file_input"),
                                 (graph_list_of_files_input, "graph_list_of_files_input"),
                                 (raw_graph, "raw_graph"),
                                 (url_graph_input, "url_input"),
                                 (list_of_url_input, "list_of_url_input"),
@@ -106,15 +134,14 @@
         self._instances_file_input = instances_file_input
         self._graph_file_input = graph_file_input
         self._graph_list_of_files_input = graph_list_of_files_input
         self._url_graph_input = url_graph_input
         self._list_of_url_input = list_of_url_input
         self._rdflib_graph = rdflib_graph
         self._namespaces_dict = namespaces_dict if namespaces_dict is not None else {}
-        # self._namespaces_dict_file = namespaces_dict_file  # TODO Need to parse this
         self._instantiation_property = instantiation_property
         self._namespaces_to_ignore = namespaces_to_ignore
         self._infer_numeric_types_for_untyped_literals = infer_numeric_types_for_untyped_literals
         self._discard_useles_constraints_with_positive_closure = discard_useless_constraints_with_positive_closure
         self._all_compliant_mode = all_instances_are_compliant_mode
         self._keep_less_specific = keep_less_specific
         self._raw_graph = raw_graph
@@ -129,14 +156,15 @@
         self._disable_comments = disable_comments
         self._disable_or_statements = disable_or_statements
         self._allow_opt_cardinality = allow_opt_cardinality
         self._disable_exact_cardinality = disable_exact_cardinality
         self._limit_remote_instances = limit_remote_instances
         self._wikidata_annotation = wikidata_annotation
         self._inverse_paths = inverse_paths
+        self._detect_minimal_iri = detect_minimal_iri
 
         self._compression_mode = compression_mode
 
         self._depth_for_building_subgraph = depth_for_building_subgraph
         self._track_classes_for_entities_at_last_depth_level = track_classes_for_entities_at_last_depth_level
         self._url_endpoint = url_endpoint
         self._strict_syntax_with_corners = strict_syntax_with_corners
@@ -169,14 +197,15 @@
 
 
         self._instance_tracker = None
         self._target_classes_dict = None
         self._class_profiler = None
         self._profile = None
         self._class_counts = None
+        self._class_min_iris = None
         self._class_shexer = None
         self._shape_list = None
 
     def profile_graph(self, string_output=False, output_file=None, verbose=False):
         self._check_correct_output_params(string_output, output_file)
         if self._target_classes_dict is None:
             self._launch_instance_tracker(verbose=verbose)
@@ -222,15 +251,15 @@
     def _add_shapes_namespaces_to_namespaces_dict(self):
         self._namespaces_dict[self._shapes_namespace] = \
             find_adequate_prefix_for_shapes_namespaces(self._namespaces_dict)
 
     def _launch_class_profiler(self, verbose=False):
         if self._class_profiler is None:
             self._class_profiler = self._build_class_profiler()
-        self._profile, self._class_counts = self._class_profiler.profile_classes(verbose=verbose)
+        self._profile, self._class_counts, self._class_min_iris = self._class_profiler.profile_classes(verbose=verbose)
 
     def _launch_class_shexer(self, acceptance_threshold, verbose=False):
         if self._class_shexer is None:
             self._class_shexer = self._build_class_shexer()
         self._shape_list = self._class_shexer.shex_classes(acceptance_threshold=acceptance_threshold,
                                                            verbose=verbose)
 
@@ -254,27 +283,30 @@
                                 disable_comments=self._disable_comments,
                                 namespaces_dict=self._namespaces_dict,
                                 allow_opt_cardinality=self._allow_opt_cardinality,
                                 disable_exact_cardinality=self._disable_exact_cardinality,
                                 shapes_namespace=self._shapes_namespace,
                                 inverse_paths=self._inverse_paths,
                                 decimals=self._decimals,
-                                instances_report_mode=self._instances_report_mode
+                                instances_report_mode=self._instances_report_mode,
+                                detect_minimal_iri=self._detect_minimal_iri,
+                                class_min_iris=self._class_min_iris
                                 )
 
     def _build_shapes_serializer(self, target_file, string_return, output_format):
         return get_shape_serializer(shapes_list=self._shape_list,
                                     target_file=target_file,
                                     string_return=string_return,
                                     namespaces_dict=self._namespaces_dict,
                                     output_format=output_format,
                                     instantiation_property=self._instantiation_property,
                                     disable_comments=self._disable_comments,
                                     wikidata_annotation=self._wikidata_annotation,
-                                    instances_report_mode=self._instances_report_mode)
+                                    instances_report_mode=self._instances_report_mode,
+                                    detect_minimal_iri=self._detect_minimal_iri)
 
     def _build_class_profiler(self):
         return get_class_profiler(target_classes_dict=self._target_classes_dict,
                                   source_file=self._graph_file_input,
                                   list_of_source_files=self._graph_list_of_files_input,
                                   input_format=self._input_format,
                                   instantiation_property_str=self._instantiation_property,
@@ -296,15 +328,16 @@
                                   built_remote_graph=self._built_remote_graph,
                                   built_shape_map=self._built_shape_map,
                                   remove_empty_shapes=self._remove_empty_shapes,
                                   limit_remote_instances=self._limit_remote_instances,
                                   inverse_paths=self._inverse_paths,
                                   all_classes_mode=self._all_classes_mode,
                                   compression_mode=self._compression_mode,
-                                  disable_endpoint_cache=self._disable_endpoint_cache)
+                                  disable_endpoint_cache=self._disable_endpoint_cache,
+                                  detect_minimal_iri=self._detect_minimal_iri)
 
 
     def _build_instance_tracker(self):
         return get_instance_tracker(instances_file_input=self._instances_file_input,
                                     graph_file_input=self._graph_file_input,
                                     graph_list_of_files_input=self._graph_list_of_files_input,
                                     target_classes=self._target_classes,
```

### Comparing `shexer-2.0.9/shexer/utils/compression.py` & `shexer-2.1.0/shexer/utils/compression.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/utils/factories/class_profiler_factory.py` & `shexer-2.1.0/shexer/utils/factories/class_profiler_factory.py`

 * *Files 2% similar despite different names*

```diff
@@ -24,15 +24,16 @@
                        built_remote_graph=None,
                        built_shape_map=None,
                        remove_empty_shapes=True,
                        limit_remote_instances=-1,
                        inverse_paths=False,
                        all_classes_mode=False,
                        compression_mode=None,
-                       disable_endpoint_cache=None):
+                       disable_endpoint_cache=None,
+                       detect_minimal_iri=False):
     yielder = get_triple_yielder(source_file=source_file,
                                  list_of_source_files=list_of_source_files,
                                  input_format=input_format,
                                  namespaces_to_ignore=namespaces_to_ignore,
                                  raw_graph=raw_graph,
                                  allow_untyped_numbers=infer_numeric_types_for_untyped_literals,
                                  namespaces_dict=namespaces_dict,
@@ -62,8 +63,9 @@
                          original_target_classes=None
                          if target_classes is None
                          else tune_target_classes_if_needed(
                              list_target_classes=target_classes,
                              prefix_namespaces_dict=reverse_keys_and_values(namespaces_dict)),
                          original_shape_map=built_shape_map,
                          remove_empty_shapes=remove_empty_shapes,
-                         inverse_paths=inverse_paths)
+                         inverse_paths=inverse_paths,
+                         detect_minimal_iri=detect_minimal_iri)
```

### Comparing `shexer-2.0.9/shexer/utils/factories/class_shexer_factory.py` & `shexer-2.1.0/shexer/utils/factories/class_shexer_factory.py`

 * *Files 16% similar despite different names*

```diff
@@ -15,15 +15,17 @@
                      disable_comments=False,
                      namespaces_dict=None,
                      allow_opt_cardinality=True,
                      disable_exact_cardinality=False,
                      shapes_namespace=SHAPES_DEFAULT_NAMESPACE,
                      inverse_paths=False,
                      decimals=-1,
-                     instances_report_mode=RATIO_INSTANCES):
+                     instances_report_mode=RATIO_INSTANCES,
+                     detect_minimal_iri=False,
+                     class_min_iris=None):
 
     return ClassShexer(
         class_counts_dict=class_counts,
         class_profile_dict=class_profile_dict,
         class_profile_json_file=None,
         remove_empty_shapes=remove_empty_shapes,
         original_target_classes=original_target_classes,
@@ -36,9 +38,11 @@
         disable_comments=disable_comments,
         namespaces_dict=namespaces_dict,
         allow_opt_cardinality=allow_opt_cardinality,
         disable_exact_cardinality=disable_exact_cardinality,
         shapes_namespace=shapes_namespace,
         inverse_paths=inverse_paths,
         instances_report_mode=instances_report_mode,
-        decimals=decimals
+        decimals=decimals,
+        detect_minimal_iri=detect_minimal_iri,
+        class_min_iris_dict=class_min_iris
     )
```

### Comparing `shexer-2.0.9/shexer/utils/factories/h_tree.py` & `shexer-2.1.0/shexer/utils/factories/h_tree.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/utils/factories/instance_tracker_factory.py` & `shexer-2.1.0/shexer/utils/factories/instance_tracker_factory.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/utils/factories/shape_map_factory.py` & `shexer-2.1.0/shexer/utils/factories/shape_map_factory.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/utils/factories/shape_map_parser_factory.py` & `shexer-2.1.0/shexer/utils/factories/shape_map_parser_factory.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/utils/factories/triple_yielders_factory.py` & `shexer-2.1.0/shexer/utils/factories/triple_yielders_factory.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/utils/namespaces.py` & `shexer-2.1.0/shexer/utils/namespaces.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/utils/obj_references.py` & `shexer-2.1.0/shexer/utils/obj_references.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/utils/shapes.py` & `shexer-2.1.0/shexer/utils/shapes.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/utils/target_elements.py` & `shexer-2.1.0/shexer/utils/target_elements.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/utils/translators/list_of_classes_to_shape_map.py` & `shexer-2.1.0/shexer/utils/translators/list_of_classes_to_shape_map.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/utils/triple_yielders.py` & `shexer-2.1.0/shexer/utils/triple_yielders.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/shexer/utils/uri.py` & `shexer-2.1.0/shexer/utils/uri.py`

 * *Files 8% similar despite different names*

```diff
@@ -35,14 +35,31 @@
     return "<" + a_uri + ">"
 
 def add_corners_if_needed(a_uri):
     if a_uri.startswith("<"):
         return a_uri
     return add_corners(a_uri)
 
+def longest_common_prefix(uri1, uri2):
+    """
+    It returns an str containing the longest possible common initial part of uri1 and uri2
+
+    :param uri1:
+    :param uri2:
+
+    :return:
+    """
+
+    if len(uri1) == 0 or len(uri2) == 0:
+        return ""
+    shortest = len(uri1) if len(uri1) < len(uri2) else len(uri2)
+    for i in range(shortest):
+        if uri1[i] != uri2[i]:
+            return uri1[:i]
+    return uri1[:shortest]
 
 def add_corners_if_it_is_an_uri(a_candidate_uri):
     if a_candidate_uri.startswith("http://") or a_candidate_uri.startswith("https://"):  # TODO, check this!
         return "<" + a_candidate_uri + ">"
     return a_candidate_uri
```

### Comparing `shexer-2.0.9/shexer.egg-info/PKG-INFO` & `shexer-2.1.0/shexer.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: shexer
-Version: 2.0.9
+Version: 2.1.0
 Summary: Automatic schema extraction for RDF graphs
 Home-page: https://github.com/DaniFdezAlvarez/shexer
 Author: Daniel Fernandez-Alvarez
 Author-email: danifdezalvarez@gmail.com
 License: UNKNOWN
-Download-URL: https://github.com/DaniFdezAlvarez/shexer/archive/2.0.9.tar.gz
+Download-URL: https://github.com/DaniFdezAlvarez/shexer/archive/2.1.0.tar.gz
 Keywords: testing,shexer,shexerp3,rdf,shex,shacl,schema
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
@@ -199,14 +199,15 @@
 * raw_graph (default None): a simple raw string containing the target graph.
 * url_graph_input (default None): use it to provide a URL of some downloadable RDF content available online to be used as target graph.
 * list_of_url_input (default None): use it to provide several URLs of downloadable RDF content available online to be used as target graph.
 * url_endpoint (default None): it expects the URL of an SPARQL endpoint. Use it if you want to get some relevant triples form that endpoint instead of providing a whole RDF graph. In this case, the triples will be those ones whose subject is one of the nodes used to build the shapes (instances of a target class, result of a node selector in a shape map).
 * depth_for_building_subgraph (default 1): use this param just in case you are working against a SPARQL endpoint. This integer indicates the max distance from any seed node to consider in order to track a subgraph from the endpoint. Please, remind that a high depth can cause a massive number of queries and have a high performance cost. 
 * track_classes_for_entities_at_last_depth_level (default True): use this param just in case you are working against a SPARQL endpoint. If it set to True, it makes a step further to the distance to the seed nodes indicated in the param depth. However, it will just look for triples related to typing, not the whole neighborhood of the nodes in the last level of depth.
 * limit_remote_instances (default -1). Use this param if you are working against an endpoint using the param target_classes. If it is set to a positive number, sheXer will just get limit_remote_instances instances for each class from the endpoint (by adding LIMIT at the end of the sparql query). This is useful when working with big sources with tons on instances, causing too many or too heavy SPARQL queries to retrieve  all the content. 
+* disable_endpoint_cache (default False). By default, if sheXer is told to consume triples from an endpoint, it will make some SPARQL queries and store the results in a local graph. If this parameter is set to True, sheXer won't save that content locally. This will help to reduce main memory usage, but will decrease the performance, as sheXer will need to make more SPARQL queries to the endpoint.
 * namespaces_dict (default None): dictionary in which the keys are namespaces and the values are their expected prefixes in the outputs. 
 * input_format (default "NT"): the format of the graph which is going to be computed. The default value is const.NT. IMPORTANT: currently, sheXer does not guess input format, so ensure you specify the format here in case you are not providing n-triples content. In case you provide a combined input (several files, several URLs...) they all should have the same format. If you work against an endpoit, then this param do not have any effect.
 * compression_mode (default None). Only when you are working with local files, if they are compressed, you do not need to uncompress to parse them. Currently supported formats are ZIP and GZ. Set compression_format to "zip" or "gz" to work with such files. Each gz file will be assumed to contain a single graph file. Each zip file will be assumed to be a directory containing one or more graph files. In case the zip contains several files, they will be all parsed and merged (they should have the same format, indicated with input_format). In every case, sheXer won't write any uncompressed content to your disk.
 
 #### Params to tune the shexing process
 
 All this parameters have a default value so you do not need to use any of them. But you can modify the schema extraction in many different ways.
```

### Comparing `shexer-2.0.9/shexer.egg-info/SOURCES.txt` & `shexer-2.1.0/shexer.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -29,23 +29,27 @@
 shexer/core/instances/mappings/shape_map_instance_tracker.py
 shexer/core/instances/mix/__init__.py
 shexer/core/instances/mix/mixed_instance_tracker.py
 shexer/core/profiling/__init__.py
 shexer/core/profiling/class_profiler.py
 shexer/core/profiling/consts.py
 shexer/core/profiling/strategy/__init__.py
-shexer/core/profiling/strategy/abstract_strategy.py
+shexer/core/profiling/strategy/abstract_feature_direction_strategy.py
 shexer/core/profiling/strategy/direct_features_strategy.py
 shexer/core/profiling/strategy/include_reverse_features_strategy.py
 shexer/core/shexing/__init__.py
 shexer/core/shexing/class_shexer.py
 shexer/core/shexing/strategy/__init__.py
-shexer/core/shexing/strategy/asbtract_shexing_strategy.py
+shexer/core/shexing/strategy/abstract_shexing_strategy.py
 shexer/core/shexing/strategy/direct_and_inverse_shexing_strategy.py
 shexer/core/shexing/strategy/direct_shexing_strategy.py
+shexer/core/shexing/strategy/minimal_iri_strategy/__init__.py
+shexer/core/shexing/strategy/minimal_iri_strategy/abstract_min_iri_strategy.py
+shexer/core/shexing/strategy/minimal_iri_strategy/annotate_min_iri_strategy.py
+shexer/core/shexing/strategy/minimal_iri_strategy/ignore_min_iri_strategy.py
 shexer/io/__init__.py
 shexer/io/file.py
 shexer/io/wikidata.py
 shexer/io/graph/__init__.py
 shexer/io/graph/yielder/__init__.py
 shexer/io/graph/yielder/base_triples_yielder.py
 shexer/io/graph/yielder/big_ttl_triples_yielder.py
@@ -141,14 +145,15 @@
 test/const.py
 test/t_utils.py
 test/test_all_classes_mode.py
 test/test_allow_opt_cardinality.py
 test/test_compression_mode.py
 test/test_decimals.py
 test/test_depth_for_building_subgraph.py
+test/test_detect_minimal_iri.py
 test/test_disable_comments.py
 test/test_disable_endpoint_cache.py
 test/test_disable_exact_cardinality.py
 test/test_disable_or_statements.py
 test/test_discard_and_compliant.py
 test/test_file_target_classes.py
 test/test_graph_file_input.py
@@ -178,11 +183,12 @@
 test/test_url_graph.py
 test/test_wikidata_annotation.py
 test/test_bugs/__init__.py
 test/test_bugs/test_no_sharp_in_auto_shape_names.py
 test/test_shacl/__init__.py
 test/test_shacl/test_annotation.py
 test/test_shacl/test_class_selection.py
+test/test_shacl/test_detect_minimal_iri.py
 test/test_shacl/test_literal_types.py
 ws/__init__.py
 ws/shexer_rest.py
 ws/wsgi.py
```

### Comparing `shexer-2.0.9/test/const.py` & `shexer-2.1.0/test/const.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/t_utils.py` & `shexer-2.1.0/test/t_utils.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_all_classes_mode.py` & `shexer-2.1.0/test/test_all_classes_mode.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_allow_opt_cardinality.py` & `shexer-2.1.0/test/test_allow_opt_cardinality.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_bugs/test_no_sharp_in_auto_shape_names.py` & `shexer-2.1.0/test/test_bugs/test_no_sharp_in_auto_shape_names.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_compression_mode.py` & `shexer-2.1.0/test/test_compression_mode.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_decimals.py` & `shexer-2.1.0/test/test_decimals.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_depth_for_building_subgraph.py` & `shexer-2.1.0/test/test_depth_for_building_subgraph.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_disable_comments.py` & `shexer-2.1.0/test/test_disable_comments.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_disable_endpoint_cache.py` & `shexer-2.1.0/test/test_disable_endpoint_cache.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_disable_exact_cardinality.py` & `shexer-2.1.0/test/test_disable_exact_cardinality.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_disable_or_statements.py` & `shexer-2.1.0/test/test_disable_or_statements.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_discard_and_compliant.py` & `shexer-2.1.0/test/test_discard_and_compliant.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_file_target_classes.py` & `shexer-2.1.0/test/test_file_target_classes.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_graph_file_input.py` & `shexer-2.1.0/test/test_graph_file_input.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_graph_list_of_file_inputs.py` & `shexer-2.1.0/test/test_graph_list_of_file_inputs.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_infer_numeric_types_for_untyped_literals.py` & `shexer-2.1.0/test/test_infer_numeric_types_for_untyped_literals.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_input_format.py` & `shexer-2.1.0/test/test_input_format.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_instances_file_input.py` & `shexer-2.1.0/test/test_instances_file_input.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_instances_report.py` & `shexer-2.1.0/test/test_instances_report.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_instantiation_property.py` & `shexer-2.1.0/test/test_instantiation_property.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_inverse_paths.py` & `shexer-2.1.0/test/test_inverse_paths.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_keep_less_specific.py` & `shexer-2.1.0/test/test_keep_less_specific.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_list_of_url_input.py` & `shexer-2.1.0/test/test_list_of_url_input.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_namespaces_dict.py` & `shexer-2.1.0/test/test_namespaces_dict.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_namespaces_to_ignore.py` & `shexer-2.1.0/test/test_namespaces_to_ignore.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_raw_graph.py` & `shexer-2.1.0/test/test_raw_graph.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_raw_shape_map.py` & `shexer-2.1.0/test/test_raw_shape_map.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_rdflib_graph.py` & `shexer-2.1.0/test/test_rdflib_graph.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_remove_empty_sahpes.py` & `shexer-2.1.0/test/test_remove_empty_sahpes.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_shacl/test_annotation.py` & `shexer-2.1.0/test/test_shacl/test_annotation.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_shacl/test_class_selection.py` & `shexer-2.1.0/test/test_shacl/test_class_selection.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_shacl/test_literal_types.py` & `shexer-2.1.0/test/test_shacl/test_literal_types.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_shape_map_file.py` & `shexer-2.1.0/test/test_shape_map_file.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_shape_map_format.py` & `shexer-2.1.0/test/test_shape_map_format.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_shape_qualifiers_mode.py` & `shexer-2.1.0/test/test_shape_qualifiers_mode.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_shapes_namespaces.py` & `shexer-2.1.0/test/test_shapes_namespaces.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_sort.py` & `shexer-2.1.0/test/test_sort.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_target_classes.py` & `shexer-2.1.0/test/test_target_classes.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_threshold.py` & `shexer-2.1.0/test/test_threshold.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_url_endpoint.py` & `shexer-2.1.0/test/test_url_endpoint.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_url_graph.py` & `shexer-2.1.0/test/test_url_graph.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/test/test_wikidata_annotation.py` & `shexer-2.1.0/test/test_wikidata_annotation.py`

 * *Files identical despite different names*

### Comparing `shexer-2.0.9/ws/shexer_rest.py` & `shexer-2.1.0/ws/shexer_rest.py`

 * *Files identical despite different names*

