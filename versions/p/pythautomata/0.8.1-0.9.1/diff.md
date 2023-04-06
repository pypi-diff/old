# Comparing `tmp/pythautomata-0.8.1.tar.gz` & `tmp/pythautomata-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pythautomata-0.8.1.tar", max compression
+gzip compressed data, was "pythautomata-0.9.1.tar", max compression
```

## Comparing `pythautomata-0.8.1.tar` & `pythautomata-0.9.1.tar`

### file list

```diff
@@ -1,79 +1,79 @@
--rw-r--r--   0        0        0    11357 2021-11-20 03:05:45.774215 pythautomata-0.8.1/LICENSE
--rw-r--r--   0        0        0     1033 2021-11-20 03:05:45.774215 pythautomata-0.8.1/README.md
--rw-r--r--   0        0        0      633 2021-11-20 03:05:57.150348 pythautomata-0.8.1/pyproject.toml
--rw-r--r--   0        0        0        0 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/__init__.py
--rw-r--r--   0        0        0        0 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/abstract/__init__.py
--rw-r--r--   0        0        0     2830 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/abstract/finite_automaton.py
--rw-r--r--   0        0        0      692 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/abstract/model_exporting_strategy.py
--rw-r--r--   0        0        0      533 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/abstract/pdfa_model_exporting_strategy.py
--rw-r--r--   0        0        0     1070 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/abstract/probabilistic_model.py
--rw-r--r--   0        0        0        0 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/automata/__init__.py
--rw-r--r--   0        0        0     2773 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/automata/deterministic_finite_automaton.py
--rw-r--r--   0        0        0     2592 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/automata/non_deterministic_finite_automaton.py
--rw-r--r--   0        0        0     1844 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/automata/symbolic_finite_automaton.py
--rw-r--r--   0        0        0     2912 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/automata/wheighted_automaton_definition/probabilistic_deterministic_finite_automaton.py
--rw-r--r--   0        0        0     5636 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/automata/wheighted_automaton_definition/weighted_automaton.py
--rw-r--r--   0        0        0     4456 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/automata/wheighted_automaton_definition/weighted_state.py
--rw-r--r--   0        0        0      511 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/automata/wheighted_automaton_definition/weighted_transition.py
--rw-r--r--   0        0        0        0 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/automata_definitions/__init__.py
--rw-r--r--   0        0        0     4918 2021-11-20 03:05:45.774215 pythautomata-0.8.1/pythautomata/automata_definitions/bollig_habermehl_kern_leucker_automata.py
--rw-r--r--   0        0        0     7654 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/automata_definitions/omlin_giles_automata.py
--rw-r--r--   0        0        0    41770 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/automata_definitions/other_automata.py
--rw-r--r--   0        0        0     7826 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/automata_definitions/sample_nfas.py
--rw-r--r--   0        0        0     9879 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/automata_definitions/tomitas_grammars.py
--rw-r--r--   0        0        0     2166 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/automata_definitions/tomitas_grammars_modifications.py
--rw-r--r--   0        0        0     8925 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/automata_definitions/weighted_tomitas_grammars.py
--rw-r--r--   0        0        0        0 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/base_types/__init__.py
--rw-r--r--   0        0        0      987 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/base_types/alphabet.py
--rw-r--r--   0        0        0      403 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/base_types/guard.py
--rw-r--r--   0        0        0     2448 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/base_types/sequence.py
--rw-r--r--   0        0        0     2211 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/base_types/state.py
--rw-r--r--   0        0        0     2575 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/base_types/symbol.py
--rw-r--r--   0        0        0     2380 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/base_types/symbolic_state.py
--rw-r--r--   0        0        0      776 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/boolean_algebra_learner/boolean_algebra_learner.py
--rw-r--r--   0        0        0     4731 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/boolean_algebra_learner/closed_discrete_interval_learner.py
--rw-r--r--   0        0        0      846 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/boolean_algebra_learner/equality_learner.py
--rw-r--r--   0        0        0      205 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/exceptions/model_importing_error.py
--rw-r--r--   0        0        0      261 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/exceptions/non_deterministic_states_exception.py
--rw-r--r--   0        0        0      185 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/exceptions/none_state_exception.py
--rw-r--r--   0        0        0       48 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/exceptions/python_automata_exception.py
--rw-r--r--   0        0        0      184 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/exceptions/unexpected_type_exception.py
--rw-r--r--   0        0        0      217 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/exceptions/unknown_symbols_exception.py
--rw-r--r--   0        0        0      485 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/guards/and_guard.py
--rw-r--r--   0        0        0      448 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/guards/closed_interval_guard.py
--rw-r--r--   0        0        0      354 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/guards/equality_guard.py
--rw-r--r--   0        0        0      461 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/guards/intersection_guard.py
--rw-r--r--   0        0        0      393 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/guards/negation_guard.py
--rw-r--r--   0        0        0      483 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/guards/or_guard.py
--rw-r--r--   0        0        0      454 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/guards/union_guard.py
--rw-r--r--   0        0        0     1931 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/model_comparators/dfa_comparison_strategy.py
--rw-r--r--   0        0        0     6764 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/model_comparators/hopcroft_karp_comparison_strategy.py
--rw-r--r--   0        0        0     2126 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/model_comparators/wfa_comparison_strategy.py
--rw-r--r--   0        0        0        0 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/model_exporters/__init__.py
--rw-r--r--   0        0        0      538 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/model_exporters/dot_exporting_strategy.py
--rw-r--r--   0        0        0     1644 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/model_exporters/encoded_file_exporting_strategy.py
--rw-r--r--   0        0        0     2690 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/model_exporters/image_exporting_strategy.py
--rw-r--r--   0        0        0     2368 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/model_exporters/image_exporting_strategy_without_hole_state.py
--rw-r--r--   0        0        0     1598 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/model_exporters/wfa_image_exporter.py
--rw-r--r--   0        0        0     1190 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/run_tests.py
--rw-r--r--   0        0        0        0 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/tests/__init__.py
--rw-r--r--   0        0        0     7691 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/tests/test_automata_comparison.py
--rw-r--r--   0        0        0     1894 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/tests/test_automata_convertor.py
--rw-r--r--   0        0        0     1245 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/tests/test_automata_definitions.py
--rw-r--r--   0        0        0     1650 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/tests/test_dfa_operations.py
--rw-r--r--   0        0        0     2720 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/tests/test_minimizer.py
--rw-r--r--   0        0        0     1296 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/tests/test_pdfa_generator.py
--rw-r--r--   0        0        0      892 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/tests/test_sequence.py
--rw-r--r--   0        0        0     1810 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/tests/test_simple_DFA_generator.py
--rw-r--r--   0        0        0        0 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/utilities/__init__.py
--rw-r--r--   0        0        0     2654 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/utilities/abbadingo_one_dfa_generator.py
--rw-r--r--   0        0        0     6599 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/utilities/automata_converter.py
--rw-r--r--   0        0        0     7725 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/utilities/dfa_minimizer.py
--rw-r--r--   0        0        0     6343 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/utilities/dfa_operations.py
--rw-r--r--   0        0        0     3964 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/utilities/encoded_file_importer.py
--rw-r--r--   0        0        0     2244 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/utilities/pdfa_generator.py
--rw-r--r--   0        0        0      871 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/utilities/pdfa_operations.py
--rw-r--r--   0        0        0     3363 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/utilities/sequence_generator.py
--rw-r--r--   0        0        0     2880 2021-11-20 03:05:45.778216 pythautomata-0.8.1/pythautomata/utilities/simple_dfa_generator.py
--rw-r--r--   0        0        0     2108 2021-11-20 03:05:58.263474 pythautomata-0.8.1/setup.py
--rw-r--r--   0        0        0     1475 2021-11-20 03:05:58.263872 pythautomata-0.8.1/PKG-INFO
+-rw-r--r--   0        0        0    11357 2021-11-23 17:35:53.395931 pythautomata-0.9.1/LICENSE
+-rw-r--r--   0        0        0     1033 2021-11-23 17:35:53.395931 pythautomata-0.9.1/README.md
+-rw-r--r--   0        0        0      633 2021-11-23 17:36:18.038019 pythautomata-0.9.1/pyproject.toml
+-rw-r--r--   0        0        0        0 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/__init__.py
+-rw-r--r--   0        0        0        0 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/abstract/__init__.py
+-rw-r--r--   0        0        0     2830 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/abstract/finite_automaton.py
+-rw-r--r--   0        0        0      692 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/abstract/model_exporting_strategy.py
+-rw-r--r--   0        0        0      533 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/abstract/pdfa_model_exporting_strategy.py
+-rw-r--r--   0        0        0     1070 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/abstract/probabilistic_model.py
+-rw-r--r--   0        0        0        0 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata/__init__.py
+-rw-r--r--   0        0        0     2773 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata/deterministic_finite_automaton.py
+-rw-r--r--   0        0        0     2592 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata/non_deterministic_finite_automaton.py
+-rw-r--r--   0        0        0     1844 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata/symbolic_finite_automaton.py
+-rw-r--r--   0        0        0     2920 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata/wheighted_automaton_definition/probabilistic_deterministic_finite_automaton.py
+-rw-r--r--   0        0        0     5646 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata/wheighted_automaton_definition/weighted_automaton.py
+-rw-r--r--   0        0        0     4456 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata/wheighted_automaton_definition/weighted_state.py
+-rw-r--r--   0        0        0      511 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata/wheighted_automaton_definition/weighted_transition.py
+-rw-r--r--   0        0        0        0 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata_definitions/__init__.py
+-rw-r--r--   0        0        0     4918 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata_definitions/bollig_habermehl_kern_leucker_automata.py
+-rw-r--r--   0        0        0     7654 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata_definitions/omlin_giles_automata.py
+-rw-r--r--   0        0        0    41770 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata_definitions/other_automata.py
+-rw-r--r--   0        0        0     7826 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata_definitions/sample_nfas.py
+-rw-r--r--   0        0        0     9879 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata_definitions/tomitas_grammars.py
+-rw-r--r--   0        0        0     2166 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata_definitions/tomitas_grammars_modifications.py
+-rw-r--r--   0        0        0     8575 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/automata_definitions/weighted_tomitas_grammars.py
+-rw-r--r--   0        0        0        0 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/base_types/__init__.py
+-rw-r--r--   0        0        0      987 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/base_types/alphabet.py
+-rw-r--r--   0        0        0      403 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/base_types/guard.py
+-rw-r--r--   0        0        0     2448 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/base_types/sequence.py
+-rw-r--r--   0        0        0     2211 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/base_types/state.py
+-rw-r--r--   0        0        0     2575 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/base_types/symbol.py
+-rw-r--r--   0        0        0     2380 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/base_types/symbolic_state.py
+-rw-r--r--   0        0        0      776 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/boolean_algebra_learner/boolean_algebra_learner.py
+-rw-r--r--   0        0        0     4731 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/boolean_algebra_learner/closed_discrete_interval_learner.py
+-rw-r--r--   0        0        0      846 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/boolean_algebra_learner/equality_learner.py
+-rw-r--r--   0        0        0      205 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/exceptions/model_importing_error.py
+-rw-r--r--   0        0        0      261 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/exceptions/non_deterministic_states_exception.py
+-rw-r--r--   0        0        0      185 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/exceptions/none_state_exception.py
+-rw-r--r--   0        0        0       48 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/exceptions/python_automata_exception.py
+-rw-r--r--   0        0        0      184 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/exceptions/unexpected_type_exception.py
+-rw-r--r--   0        0        0      217 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/exceptions/unknown_symbols_exception.py
+-rw-r--r--   0        0        0      485 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/guards/and_guard.py
+-rw-r--r--   0        0        0      448 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/guards/closed_interval_guard.py
+-rw-r--r--   0        0        0      354 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/guards/equality_guard.py
+-rw-r--r--   0        0        0      461 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/guards/intersection_guard.py
+-rw-r--r--   0        0        0      393 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/guards/negation_guard.py
+-rw-r--r--   0        0        0      483 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/guards/or_guard.py
+-rw-r--r--   0        0        0      454 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/guards/union_guard.py
+-rw-r--r--   0        0        0     1931 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/model_comparators/dfa_comparison_strategy.py
+-rw-r--r--   0        0        0     6764 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/model_comparators/hopcroft_karp_comparison_strategy.py
+-rw-r--r--   0        0        0     2126 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/model_comparators/wfa_comparison_strategy.py
+-rw-r--r--   0        0        0        0 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/model_exporters/__init__.py
+-rw-r--r--   0        0        0      538 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/model_exporters/dot_exporting_strategy.py
+-rw-r--r--   0        0        0     1644 2021-11-23 17:35:53.395931 pythautomata-0.9.1/pythautomata/model_exporters/encoded_file_exporting_strategy.py
+-rw-r--r--   0        0        0     2690 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/model_exporters/image_exporting_strategy.py
+-rw-r--r--   0        0        0     2368 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/model_exporters/image_exporting_strategy_without_hole_state.py
+-rw-r--r--   0        0        0     1598 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/model_exporters/wfa_image_exporter.py
+-rw-r--r--   0        0        0     1196 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/run_tests.py
+-rw-r--r--   0        0        0        0 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/tests/__init__.py
+-rw-r--r--   0        0        0     7691 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/tests/test_automata_comparison.py
+-rw-r--r--   0        0        0     1894 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/tests/test_automata_convertor.py
+-rw-r--r--   0        0        0     1245 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/tests/test_automata_definitions.py
+-rw-r--r--   0        0        0     1650 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/tests/test_dfa_operations.py
+-rw-r--r--   0        0        0     2720 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/tests/test_minimizer.py
+-rw-r--r--   0        0        0     1296 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/tests/test_pdfa_generator.py
+-rw-r--r--   0        0        0      892 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/tests/test_sequence.py
+-rw-r--r--   0        0        0     1810 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/tests/test_simple_DFA_generator.py
+-rw-r--r--   0        0        0        0 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/utilities/__init__.py
+-rw-r--r--   0        0        0     2654 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/utilities/abbadingo_one_dfa_generator.py
+-rw-r--r--   0        0        0     6599 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/utilities/automata_converter.py
+-rw-r--r--   0        0        0     7725 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/utilities/dfa_minimizer.py
+-rw-r--r--   0        0        0     6343 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/utilities/dfa_operations.py
+-rw-r--r--   0        0        0     3964 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/utilities/encoded_file_importer.py
+-rw-r--r--   0        0        0     2214 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/utilities/pdfa_generator.py
+-rw-r--r--   0        0        0      871 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/utilities/pdfa_operations.py
+-rw-r--r--   0        0        0     3363 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/utilities/sequence_generator.py
+-rw-r--r--   0        0        0     2880 2021-11-23 17:35:53.399932 pythautomata-0.9.1/pythautomata/utilities/simple_dfa_generator.py
+-rw-r--r--   0        0        0     2108 2021-11-23 17:36:19.133404 pythautomata-0.9.1/setup.py
+-rw-r--r--   0        0        0     1475 2021-11-23 17:36:19.133971 pythautomata-0.9.1/PKG-INFO
```

### Comparing `pythautomata-0.8.1/LICENSE` & `pythautomata-0.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/README.md` & `pythautomata-0.9.1/README.md`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pyproject.toml` & `pythautomata-0.9.1/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "pythautomata"
-version = "0.8.1"
+version = "0.9.1"
 description = "ORT's implementation of various kinds of automata"
 authors = ["Federico Vilensky <fedevilensky@gmail.com>", "Franz Mayr", "Ramiro Visca", "Federico Pan", "Sebastián Uriarte", "Pablo Morales", "Kevin Chacon", "Diego Zuluaga"]
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.9"
 graphviz = "*"
```

### Comparing `pythautomata-0.8.1/pythautomata/abstract/finite_automaton.py` & `pythautomata-0.9.1/pythautomata/abstract/finite_automaton.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/abstract/model_exporting_strategy.py` & `pythautomata-0.9.1/pythautomata/abstract/model_exporting_strategy.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/abstract/pdfa_model_exporting_strategy.py` & `pythautomata-0.9.1/pythautomata/abstract/pdfa_model_exporting_strategy.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/abstract/probabilistic_model.py` & `pythautomata-0.9.1/pythautomata/abstract/probabilistic_model.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/automata/deterministic_finite_automaton.py` & `pythautomata-0.9.1/pythautomata/automata/deterministic_finite_automaton.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/automata/non_deterministic_finite_automaton.py` & `pythautomata-0.9.1/pythautomata/automata/non_deterministic_finite_automaton.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/automata/symbolic_finite_automaton.py` & `pythautomata-0.9.1/pythautomata/automata/symbolic_finite_automaton.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/automata/wheighted_automaton_definition/probabilistic_deterministic_finite_automaton.py` & `pythautomata-0.9.1/pythautomata/automata/wheighted_automaton_definition/probabilistic_deterministic_finite_automaton.py`

 * *Files 1% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
 from pythautomata.base_types.alphabet import Alphabet
 from pythautomata.base_types.sequence import Sequence
 from pythautomata.base_types.symbol import Symbol
 from pythautomata.model_exporters.wfa_image_exporter import WFAImageExporter
 
 
-def is_probabilistic(weighted_states: set[WeightedState], alphabet: Alphabet):
+def is_probabilistic(weighted_states: set[WeightedState], alphabet: Alphabet) -> bool:
     initial_states = list(filter(lambda state: state.initial_weight != 0, weighted_states))
     if len(initial_states) != 1:
         return False
     for weighted_state in weighted_states:
         total_weight = weighted_state.final_weight
         for symbol in alphabet.symbols:
             transitions_for_symbol = weighted_state.transitions_list[symbol]
```

### Comparing `pythautomata-0.8.1/pythautomata/automata/wheighted_automaton_definition/weighted_automaton.py` & `pythautomata-0.9.1/pythautomata/automata/wheighted_automaton_definition/weighted_automaton.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 from itertools import chain
 from pythautomata.base_types.alphabet import Alphabet
 from pythautomata.base_types.sequence import Sequence
 from decimal import Decimal
 
 from pythautomata.abstract.pdfa_model_exporting_strategy import PDFAModelExportingStrategy
 from pythautomata.model_exporters.wfa_image_exporter import WFAImageExporter
-from ...base_types.symbol import Symbol
+from pythautomata.base_types.symbol import Symbol
 
 epsilon = Sequence()
 
 
 class WeightedAutomaton:
 
     @property
```

### Comparing `pythautomata-0.8.1/pythautomata/automata/wheighted_automaton_definition/weighted_state.py` & `pythautomata-0.9.1/pythautomata/automata/wheighted_automaton_definition/weighted_state.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/automata_definitions/bollig_habermehl_kern_leucker_automata.py` & `pythautomata-0.9.1/pythautomata/automata_definitions/bollig_habermehl_kern_leucker_automata.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/automata_definitions/omlin_giles_automata.py` & `pythautomata-0.9.1/pythautomata/automata_definitions/omlin_giles_automata.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/automata_definitions/other_automata.py` & `pythautomata-0.9.1/pythautomata/automata_definitions/other_automata.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/automata_definitions/sample_nfas.py` & `pythautomata-0.9.1/pythautomata/automata_definitions/sample_nfas.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/automata_definitions/tomitas_grammars.py` & `pythautomata-0.9.1/pythautomata/automata_definitions/tomitas_grammars.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/automata_definitions/tomitas_grammars_modifications.py` & `pythautomata-0.9.1/pythautomata/automata_definitions/tomitas_grammars_modifications.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/automata_definitions/weighted_tomitas_grammars.py` & `pythautomata-0.9.1/pythautomata/automata_definitions/weighted_tomitas_grammars.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,13 +1,12 @@
-from pythautomata.base_types.state import State
 from pythautomata.base_types.symbol import SymbolStr
 from pythautomata.base_types.alphabet import Alphabet
-from pythautomata.automata.wheighted_automaton_definition.weighted_automaton import WeightedAutomaton
+from pythautomata.automata.wheighted_automaton_definition.probabilistic_deterministic_finite_automaton import \
+     ProbabilisticDeterministicFiniteAutomaton
 from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
-from pythautomata.model_comparators.hopcroft_karp_comparison_strategy import HopcroftKarpComparisonStrategy as HopcroftKarpComparisonStrategy
 
 binaryAlphabet = Alphabet(frozenset((SymbolStr('0'), SymbolStr('1'))))
 zero = binaryAlphabet['0']
 one = binaryAlphabet['1']
 
 
 class WeightedTomitasGrammars:
@@ -84,16 +83,15 @@
 
         q0.add_transition(zero, q1, 0.665)
         q0.add_transition(one, q0, 0.285)
         q1.add_transition(zero, q1, 0.285)
         q1.add_transition(one, q1, 0.665)
 
         states = {q0, q1}
-        #comparator = HopcroftKarpComparisonStrategy()
-        return WeightedAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas1")
+        return ProbabilisticDeterministicFiniteAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas1")
 
     @staticmethod
     def get_automaton_2():
         """
         method with specification of automaton 2 from the paper       
 
         Returns
@@ -109,16 +107,15 @@
         q0.add_transition(one, q1, 0.285)
         q1.add_transition(zero, q0, 0.285)
         q1.add_transition(one, q2, 0.665)
         q2.add_transition(zero, q2, 0.285)
         q2.add_transition(one, q2, 0.665)
 
         states = {q0, q1, q2}
-        #comparator = HopcroftKarpComparisonStrategy()
-        return WeightedAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas2")
+        return ProbabilisticDeterministicFiniteAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas2")
 
     @staticmethod
     def get_automaton_3():
         """
         method with specification of automaton 3 from the paper       
 
         Returns
@@ -140,16 +137,15 @@
         q2.add_transition(one, q4, 0.665)
         q3.add_transition(zero, q2, 0.665)
         q3.add_transition(one, q3, 0.285)
         q4.add_transition(zero, q4, 0.285)
         q4.add_transition(one, q4, 0.665)
 
         states = {q0, q1, q2, q3, q4}
-        #comparator = HopcroftKarpComparisonStrategy()
-        return WeightedAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas3")
+        return ProbabilisticDeterministicFiniteAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas3")
 
     @staticmethod
     def get_automaton_4():
         """
         method with specification of automaton 4 from the paper       
 
         Returns
@@ -168,16 +164,15 @@
         q1.add_transition(one, q0, 0.285)
         q2.add_transition(zero, q3, 0.665)
         q2.add_transition(one, q0, 0.285)
         q3.add_transition(zero, q3, 0.285)
         q3.add_transition(one, q3, 0.665)
 
         states = {q0, q1, q2, q3}
-        #comparator = HopcroftKarpComparisonStrategy()
-        return WeightedAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas4")
+        return ProbabilisticDeterministicFiniteAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas4")
 
     @staticmethod
     def get_automaton_5():
         """
         method with specification of automaton 5 from the paper       
 
         Returns
@@ -196,16 +191,15 @@
         q1.add_transition(one, q0, 0.665)
         q2.add_transition(zero, q1, 0.285)
         q2.add_transition(one, q3, 0.665)
         q3.add_transition(zero, q0, 0.285)
         q3.add_transition(one, q2, 0.665)
 
         states = {q0, q1, q2, q3}
-        #comparator = HopcroftKarpComparisonStrategy()
-        return WeightedAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas5")
+        return ProbabilisticDeterministicFiniteAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas5")
 
     @staticmethod
     def get_automaton_6():
         """
         method with specification of automaton 6 from the paper       
 
         Returns
@@ -221,16 +215,15 @@
         q0.add_transition(one, q1, 0.285)
         q1.add_transition(zero, q0, 0.285)
         q1.add_transition(one, q2, 0.665)
         q2.add_transition(zero, q1, 0.285)
         q2.add_transition(one, q0, 0.665)
 
         states = {q0, q1, q2}
-        #comparator = HopcroftKarpComparisonStrategy()
-        return WeightedAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas6")
+        return ProbabilisticDeterministicFiniteAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas6")
 
     @staticmethod
     def get_automaton_7():
         """
         method with specification of automaton 7 from the paper       
 
         Returns
@@ -252,9 +245,8 @@
         q2.add_transition(one, q3, 0.285)
         q3.add_transition(zero, q4, 0.665)
         q3.add_transition(one, q3, 0.285)
         q4.add_transition(zero, q4, 0.285)
         q4.add_transition(one, q4, 0.665)
 
         states = {q0, q1, q2, q3, q4}
-        #comparator = HopcroftKarpComparisonStrategy()
-        return WeightedAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas7")
+        return ProbabilisticDeterministicFiniteAutomaton(binaryAlphabet, states, SymbolStr("$"), "WeightedTomitas7")
```

### Comparing `pythautomata-0.8.1/pythautomata/base_types/alphabet.py` & `pythautomata-0.9.1/pythautomata/base_types/alphabet.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/base_types/sequence.py` & `pythautomata-0.9.1/pythautomata/base_types/sequence.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/base_types/state.py` & `pythautomata-0.9.1/pythautomata/base_types/state.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/base_types/symbol.py` & `pythautomata-0.9.1/pythautomata/base_types/symbol.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/base_types/symbolic_state.py` & `pythautomata-0.9.1/pythautomata/base_types/symbolic_state.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/boolean_algebra_learner/boolean_algebra_learner.py` & `pythautomata-0.9.1/pythautomata/boolean_algebra_learner/boolean_algebra_learner.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/boolean_algebra_learner/closed_discrete_interval_learner.py` & `pythautomata-0.9.1/pythautomata/boolean_algebra_learner/closed_discrete_interval_learner.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/boolean_algebra_learner/equality_learner.py` & `pythautomata-0.9.1/pythautomata/boolean_algebra_learner/equality_learner.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/model_comparators/dfa_comparison_strategy.py` & `pythautomata-0.9.1/pythautomata/model_comparators/dfa_comparison_strategy.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/model_comparators/hopcroft_karp_comparison_strategy.py` & `pythautomata-0.9.1/pythautomata/model_comparators/hopcroft_karp_comparison_strategy.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/model_comparators/wfa_comparison_strategy.py` & `pythautomata-0.9.1/pythautomata/model_comparators/wfa_comparison_strategy.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/model_exporters/dot_exporting_strategy.py` & `pythautomata-0.9.1/pythautomata/model_exporters/dot_exporting_strategy.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/model_exporters/encoded_file_exporting_strategy.py` & `pythautomata-0.9.1/pythautomata/model_exporters/encoded_file_exporting_strategy.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/model_exporters/image_exporting_strategy.py` & `pythautomata-0.9.1/pythautomata/model_exporters/image_exporting_strategy.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/model_exporters/image_exporting_strategy_without_hole_state.py` & `pythautomata-0.9.1/pythautomata/model_exporters/image_exporting_strategy_without_hole_state.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/model_exporters/wfa_image_exporter.py` & `pythautomata-0.9.1/pythautomata/model_exporters/wfa_image_exporter.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/run_tests.py` & `pythautomata-0.9.1/pythautomata/run_tests.py`

 * *Files 16% similar despite different names*

```diff
@@ -5,21 +5,23 @@
 from pythautomata.tests.test_pdfa_generator import TestPDFAGenerator
 from pythautomata.tests.test_simple_DFA_generator import TestSimpleDFAGenerator
 from pythautomata.tests.test_automata_comparison import TestAutomataComparison
 from pythautomata.tests.test_sequence import TestSequence
 from pythautomata.tests.test_dfa_operations import TestDFAOperations
 from pythautomata.tests.test_automata_definitions import TestAutomataDefinitions
 
+
 def get_all_tests():
     return [TestPDFAGenerator, TestMinimizer, TestAutomataConvertor, 
     TestSimpleDFAGenerator, TestAutomataComparison, TestSequence,
     TestDFAOperations, TestAutomataDefinitions]
 
+
 def run():
-    test_classes_to_run = get_all_tests()
+    test_classes_to_run = [TestPDFAGenerator]
     loader = TestLoader()
     suites_list = []
     for test_class in test_classes_to_run:
         suite = loader.loadTestsFromTestCase(test_class)
         suites_list.append(suite)
     meta_suite = TestSuite(suites_list)
     TextTestRunner().run(meta_suite)
```

### Comparing `pythautomata-0.8.1/pythautomata/tests/test_automata_comparison.py` & `pythautomata-0.9.1/pythautomata/tests/test_automata_comparison.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/tests/test_automata_convertor.py` & `pythautomata-0.9.1/pythautomata/tests/test_automata_convertor.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/tests/test_automata_definitions.py` & `pythautomata-0.9.1/pythautomata/tests/test_automata_definitions.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/tests/test_dfa_operations.py` & `pythautomata-0.9.1/pythautomata/tests/test_dfa_operations.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/tests/test_minimizer.py` & `pythautomata-0.9.1/pythautomata/tests/test_minimizer.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/tests/test_pdfa_generator.py` & `pythautomata-0.9.1/pythautomata/tests/test_pdfa_generator.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/tests/test_sequence.py` & `pythautomata-0.9.1/pythautomata/tests/test_sequence.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/tests/test_simple_DFA_generator.py` & `pythautomata-0.9.1/pythautomata/tests/test_simple_DFA_generator.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/utilities/abbadingo_one_dfa_generator.py` & `pythautomata-0.9.1/pythautomata/utilities/abbadingo_one_dfa_generator.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/utilities/automata_converter.py` & `pythautomata-0.9.1/pythautomata/utilities/automata_converter.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/utilities/dfa_minimizer.py` & `pythautomata-0.9.1/pythautomata/utilities/dfa_minimizer.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/utilities/dfa_operations.py` & `pythautomata-0.9.1/pythautomata/utilities/dfa_operations.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/utilities/encoded_file_importer.py` & `pythautomata-0.9.1/pythautomata/utilities/encoded_file_importer.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/utilities/pdfa_generator.py` & `pythautomata-0.9.1/pythautomata/utilities/pdfa_generator.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 import random
-from decimal import Decimal
 
 from pythautomata.automata.deterministic_finite_automaton import DeterministicFiniteAutomaton
 from pythautomata.automata.wheighted_automaton_definition.probabilistic_deterministic_finite_automaton import \
      ProbabilisticDeterministicFiniteAutomaton
 from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
-from pythautomata.base_types.sequence import Sequence
+from pythautomata.base_types.symbol import SymbolStr
 
 
 def pdfa_from_dfa(dfa: DeterministicFiniteAutomaton) -> ProbabilisticDeterministicFiniteAutomaton:
     """
     Function that transforms a DFA to a PDFA with random probability distributions for each state.
 
     Parameters
@@ -22,15 +21,15 @@
 
     """
     alphabet_length = len(dfa.alphabet)
     wfa_states_dict = {state.name: __dfa_state_to_pdfa_state(state.name, state.name == dfa.initial_state.name) for state
                        in dfa.states}
     for state in dfa.states:
         __add_transitions(alphabet_length, state, wfa_states_dict)
-    terminal_symbol = Sequence(['$'])
+    terminal_symbol = SymbolStr('$')
     return ProbabilisticDeterministicFiniteAutomaton(dfa.alphabet, set(wfa_states_dict.values()), terminal_symbol)
 
 
 def __dfa_state_to_pdfa_state(name, initial):
     initial_prob = 1 if initial else 0
     final_prob = __get_prob_not_zero(0)
     wfa_state = WeightedState(name, initial_prob, final_prob)
```

### Comparing `pythautomata-0.8.1/pythautomata/utilities/pdfa_operations.py` & `pythautomata-0.9.1/pythautomata/utilities/pdfa_operations.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/utilities/sequence_generator.py` & `pythautomata-0.9.1/pythautomata/utilities/sequence_generator.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/pythautomata/utilities/simple_dfa_generator.py` & `pythautomata-0.9.1/pythautomata/utilities/simple_dfa_generator.py`

 * *Files identical despite different names*

### Comparing `pythautomata-0.8.1/setup.py` & `pythautomata-0.9.1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -20,15 +20,15 @@
 {'': ['*']}
 
 install_requires = \
 ['graphviz', 'numpy']
 
 setup_kwargs = {
     'name': 'pythautomata',
-    'version': '0.8.1',
+    'version': '0.9.1',
     'description': "ORT's implementation of various kinds of automata",
     'long_description': '# Pythautomata\n\nPythautomata is a Python library for modeling finite state systems.\n\n## A**bout**\nPythautomata is developed at the [](http://www.cs.tu-dortmund.de/)Department of Artificial Intelligence and Big Data of the Universidad ORT Uruguay. Its main goal is to provide implementations for the structures needed for working in the Model Extraction Framework.\n\nModels present in the framework are:\n\n- DFA\n- NFA\n- WFA/PDFA\n- SFA (work in progress)\n\nAll of these can be exported in different manners, like pickle or to visual representations using Graphviz. Besides the structure representations a number of algorithms of interest are implemented, to name a few:\n\n- FSA minimization\n- FSA comparison using Hopcroft Karp equivalence\n- FSA intersection (and other boolean operations)\n\n\n## **Installation**\n\n```\npip install pythautomata\n```\n\n\n\n## **Documentation**\n\n- [**API Documentation:**](https://neuralchecker.github.io/pythautomata/index.html)\n\n\n## **Maintainers**\n\nFederico Vilensky\n\nFranz Mayr\n\nFederico Pan\n\n\n## Colaborators\n',
     'author': 'Federico Vilensky',
     'author_email': 'fedevilensky@gmail.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': None,
```

### Comparing `pythautomata-0.8.1/PKG-INFO` & `pythautomata-0.9.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pythautomata
-Version: 0.8.1
+Version: 0.9.1
 Summary: ORT's implementation of various kinds of automata
 Author: Federico Vilensky
 Author-email: fedevilensky@gmail.com
 Requires-Python: >=3.9,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.9
```

