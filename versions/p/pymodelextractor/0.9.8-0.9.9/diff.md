# Comparing `tmp/pymodelextractor-0.9.8.tar.gz` & `tmp/pymodelextractor-0.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pymodelextractor-0.9.8.tar", max compression
+gzip compressed data, was "pymodelextractor-0.9.9.tar", max compression
```

## Comparing `pymodelextractor-0.9.8.tar` & `pymodelextractor-0.9.9.tar`

### file list

```diff
@@ -1,60 +1,60 @@
--rw-r--r--   0        0        0    11357 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/LICENSE
--rwxr-xr-x   0        0        0        0 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/__init__.py
--rw-r--r--   0        0        0        0 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/exceptions/__init__.py
--rw-r--r--   0        0        0       59 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/exceptions/number_of_states_exceeded_exception.py
--rw-r--r--   0        0        0       56 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/exceptions/query_length_exceeded_exception.py
--rwxr-xr-x   0        0        0        0 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/learners/__init__.py
--rwxr-xr-x   0        0        0      301 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/learners/learner.py
--rwxr-xr-x   0        0        0      480 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/learners/learning_result.py
--rwxr-xr-x   0        0        0        0 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/__init__.py
--rw-r--r--   0        0        0     2143 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/bounded_lstar_learner.py
--rw-r--r--   0        0        0     3109 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/bounded_pdfa_lstar_learner.py
--rwxr-xr-x   0        0        0     8349 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/lambda_star_learner.py
--rw-r--r--   0        0        0     6475 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/lstar_learner.py
--rw-r--r--   0        0        0     4649 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/lstarcol_learner.py
--rwxr-xr-x   0        0        0     3274 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/observation_table.py
--rw-r--r--   0        0        0     7105 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/pdfa_lstar_learner.py
--rw-r--r--   0        0        0     7499 2022-02-21 15:30:36.424315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/pdfa_lstarcol_learner.py
--rw-r--r--   0        0        0     5085 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/pdfa_observation_table.py
--rwxr-xr-x   0        0        0        0 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/translators/__init__.py
--rwxr-xr-x   0        0        0     2793 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/translators/fa_observation_table_translator.py
--rwxr-xr-x   0        0        0      472 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/translators/observation_table_translator.py
--rw-r--r--   0        0        0     9217 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/translators/pdfa_lstar_observation_table_translator.py
--rw-r--r--   0        0        0     5553 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/translators/pdfa_lstarcol_observation_table_translations.py
--rw-r--r--   0        0        0      890 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/translators/pdfa_observation_table_translator.py
--rw-r--r--   0        0        0     2958 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_tree_learners/bounded_pdfa_quantization_n_ary_tree_learner.py
--rw-r--r--   0        0        0     8576 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_tree_learners/kearns_vazirani_learner.py
--rw-r--r--   0        0        0    14681 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_tree_learners/pdfa_kearns_vazirani_learner.py
--rw-r--r--   0        0        0    16806 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_tree_learners/pdfa_n_ary_tree_learner.py
--rw-r--r--   0        0        0    16855 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/observation_tree_learners/pdfa_quantization_n_ary_tree_learner.py
--rw-r--r--   0        0        0      708 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/learners/pdfa_learner.py
--rw-r--r--   0        0        0     2578 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/run_tests.py
--rwxr-xr-x   0        0        0        0 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/teachers/__init__.py
--rwxr-xr-x   0        0        0     1664 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/teachers/automaton_teacher.py
--rw-r--r--   0        0        0     3755 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/teachers/pac_boolean_teacher.py
--rw-r--r--   0        0        0     4327 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/teachers/pac_probabilistic_teacher.py
--rw-r--r--   0        0        0     1821 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/teachers/pdfa_teacher.py
--rw-r--r--   0        0        0     2113 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/teachers/probabilistic_teacher.py
--rw-r--r--   0        0        0     2895 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/teachers/sample_probabilistic_teacher.py
--rwxr-xr-x   0        0        0     1405 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/teachers/teacher.py
--rw-r--r--   0        0        0        0 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/__init__.py
--rw-r--r--   0        0        0        0 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/__init__.py
--rw-r--r--   0        0        0     3290 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_bounded_lstar_learner.py
--rw-r--r--   0        0        0     4225 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_bounded_pdfa_lstar_learner.py
--rw-r--r--   0        0        0    14562 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_bounded_pdfa_quantization_n_ary_tree_learner.py
--rw-r--r--   0        0        0     2693 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_kearns_vazirani_learner.py
--rw-r--r--   0        0        0     1979 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_lambda_star_learner.py
--rw-r--r--   0        0        0     2653 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_lstar_learner.py
--rw-r--r--   0        0        0     2665 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_lstarcol_learner.py
--rw-r--r--   0        0        0     2186 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pac_boolean_model_teacher.py
--rw-r--r--   0        0        0    10439 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_kearns_vazirani_learner.py
--rw-r--r--   0        0        0     3634 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_lstar_learner.py
--rw-r--r--   0        0        0     3632 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_lstarcol_learner.py
--rw-r--r--   0        0        0    13071 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_n_ary_tree_learner.py
--rw-r--r--   0        0        0    13977 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_quantization_n_ary_tree_learner.py
--rw-r--r--   0        0        0     3114 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_quantization_n_ary_tree_learner_metrics.py
--rw-r--r--   0        0        0     8345 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_teachers_pdfa_lstar.py
--rw-r--r--   0        0        0     8359 2022-02-21 15:30:36.428315 pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_teachers_pdfa_lstar_col.py
--rwxr-xr-x   0        0        0      446 2022-02-21 15:30:45.476438 pymodelextractor-0.9.8/pyproject.toml
--rw-r--r--   0        0        0      961 2022-02-21 15:30:46.484043 pymodelextractor-0.9.8/setup.py
--rw-r--r--   0        0        0      427 2022-02-21 15:30:46.484812 pymodelextractor-0.9.8/PKG-INFO
+-rw-r--r--   0        0        0    11357 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/LICENSE
+-rwxr-xr-x   0        0        0        0 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/__init__.py
+-rw-r--r--   0        0        0        0 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/exceptions/__init__.py
+-rw-r--r--   0        0        0       59 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/exceptions/number_of_states_exceeded_exception.py
+-rw-r--r--   0        0        0       56 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/exceptions/query_length_exceeded_exception.py
+-rwxr-xr-x   0        0        0        0 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/__init__.py
+-rwxr-xr-x   0        0        0      301 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/learner.py
+-rwxr-xr-x   0        0        0      480 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/learning_result.py
+-rwxr-xr-x   0        0        0        0 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/__init__.py
+-rw-r--r--   0        0        0     2143 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/bounded_lstar_learner.py
+-rw-r--r--   0        0        0     3109 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/bounded_pdfa_lstar_learner.py
+-rwxr-xr-x   0        0        0     8349 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/lambda_star_learner.py
+-rw-r--r--   0        0        0     6475 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/lstar_learner.py
+-rw-r--r--   0        0        0     4649 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/lstarcol_learner.py
+-rwxr-xr-x   0        0        0     3274 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/observation_table.py
+-rw-r--r--   0        0        0     7105 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/pdfa_lstar_learner.py
+-rw-r--r--   0        0        0     7499 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/pdfa_lstarcol_learner.py
+-rw-r--r--   0        0        0     5085 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/pdfa_observation_table.py
+-rwxr-xr-x   0        0        0        0 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/translators/__init__.py
+-rwxr-xr-x   0        0        0     2793 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/translators/fa_observation_table_translator.py
+-rwxr-xr-x   0        0        0      472 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/translators/observation_table_translator.py
+-rw-r--r--   0        0        0     9217 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/translators/pdfa_lstar_observation_table_translator.py
+-rw-r--r--   0        0        0     5553 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/translators/pdfa_lstarcol_observation_table_translations.py
+-rw-r--r--   0        0        0      890 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/translators/pdfa_observation_table_translator.py
+-rw-r--r--   0        0        0     2958 2022-02-21 20:31:10.745612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_tree_learners/bounded_pdfa_quantization_n_ary_tree_learner.py
+-rw-r--r--   0        0        0     8576 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_tree_learners/kearns_vazirani_learner.py
+-rw-r--r--   0        0        0    14681 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_tree_learners/pdfa_kearns_vazirani_learner.py
+-rw-r--r--   0        0        0    16806 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_tree_learners/pdfa_n_ary_tree_learner.py
+-rw-r--r--   0        0        0    16855 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/learners/observation_tree_learners/pdfa_quantization_n_ary_tree_learner.py
+-rw-r--r--   0        0        0      708 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/learners/pdfa_learner.py
+-rw-r--r--   0        0        0     2578 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/run_tests.py
+-rwxr-xr-x   0        0        0        0 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/teachers/__init__.py
+-rwxr-xr-x   0        0        0     1664 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/teachers/automaton_teacher.py
+-rw-r--r--   0        0        0     3755 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/teachers/pac_boolean_teacher.py
+-rw-r--r--   0        0        0     4327 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/teachers/pac_probabilistic_teacher.py
+-rw-r--r--   0        0        0     1821 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/teachers/pdfa_teacher.py
+-rw-r--r--   0        0        0     2113 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/teachers/probabilistic_teacher.py
+-rw-r--r--   0        0        0     2895 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/teachers/sample_probabilistic_teacher.py
+-rwxr-xr-x   0        0        0     1405 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/teachers/teacher.py
+-rw-r--r--   0        0        0        0 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/__init__.py
+-rw-r--r--   0        0        0        0 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/__init__.py
+-rw-r--r--   0        0        0     3290 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_bounded_lstar_learner.py
+-rw-r--r--   0        0        0     4225 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_bounded_pdfa_lstar_learner.py
+-rw-r--r--   0        0        0    14562 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_bounded_pdfa_quantization_n_ary_tree_learner.py
+-rw-r--r--   0        0        0     2693 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_kearns_vazirani_learner.py
+-rw-r--r--   0        0        0     1979 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_lambda_star_learner.py
+-rw-r--r--   0        0        0     2653 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_lstar_learner.py
+-rw-r--r--   0        0        0     2665 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_lstarcol_learner.py
+-rw-r--r--   0        0        0     2186 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pac_boolean_model_teacher.py
+-rw-r--r--   0        0        0    10439 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_kearns_vazirani_learner.py
+-rw-r--r--   0        0        0     3634 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_lstar_learner.py
+-rw-r--r--   0        0        0     3632 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_lstarcol_learner.py
+-rw-r--r--   0        0        0    13071 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_n_ary_tree_learner.py
+-rw-r--r--   0        0        0    13977 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_quantization_n_ary_tree_learner.py
+-rw-r--r--   0        0        0     3114 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_quantization_n_ary_tree_learner_metrics.py
+-rw-r--r--   0        0        0     8345 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_teachers_pdfa_lstar.py
+-rw-r--r--   0        0        0     8359 2022-02-21 20:31:10.749612 pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_teachers_pdfa_lstar_col.py
+-rwxr-xr-x   0        0        0      446 2022-02-21 20:31:19.777613 pymodelextractor-0.9.9/pyproject.toml
+-rw-r--r--   0        0        0      961 2022-02-21 20:31:20.834802 pymodelextractor-0.9.9/setup.py
+-rw-r--r--   0        0        0      427 2022-02-21 20:31:20.835411 pymodelextractor-0.9.9/PKG-INFO
```

### Comparing `pymodelextractor-0.9.8/LICENSE` & `pymodelextractor-0.9.9/LICENSE`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/bounded_lstar_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/bounded_lstar_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/bounded_pdfa_lstar_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/bounded_pdfa_lstar_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/lambda_star_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/lambda_star_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/lstar_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/lstar_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/lstarcol_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/lstarcol_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/observation_table.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/observation_table.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/pdfa_lstar_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/pdfa_lstar_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/pdfa_lstarcol_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/pdfa_lstarcol_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/pdfa_observation_table.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/pdfa_observation_table.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/translators/fa_observation_table_translator.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/translators/fa_observation_table_translator.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/translators/pdfa_lstar_observation_table_translator.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/translators/pdfa_lstar_observation_table_translator.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/translators/pdfa_lstarcol_observation_table_translations.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/translators/pdfa_lstarcol_observation_table_translations.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_table_learners/translators/pdfa_observation_table_translator.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_table_learners/translators/pdfa_observation_table_translator.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_tree_learners/bounded_pdfa_quantization_n_ary_tree_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_tree_learners/bounded_pdfa_quantization_n_ary_tree_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_tree_learners/kearns_vazirani_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_tree_learners/kearns_vazirani_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_tree_learners/pdfa_kearns_vazirani_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_tree_learners/pdfa_kearns_vazirani_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_tree_learners/pdfa_n_ary_tree_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_tree_learners/pdfa_n_ary_tree_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/observation_tree_learners/pdfa_quantization_n_ary_tree_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/observation_tree_learners/pdfa_quantization_n_ary_tree_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/learners/pdfa_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/learners/pdfa_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/run_tests.py` & `pymodelextractor-0.9.9/pymodelextractor/run_tests.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/teachers/automaton_teacher.py` & `pymodelextractor-0.9.9/pymodelextractor/teachers/automaton_teacher.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/teachers/pac_boolean_teacher.py` & `pymodelextractor-0.9.9/pymodelextractor/teachers/pac_boolean_teacher.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/teachers/pac_probabilistic_teacher.py` & `pymodelextractor-0.9.9/pymodelextractor/teachers/pac_probabilistic_teacher.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/teachers/pdfa_teacher.py` & `pymodelextractor-0.9.9/pymodelextractor/teachers/pdfa_teacher.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/teachers/probabilistic_teacher.py` & `pymodelextractor-0.9.9/pymodelextractor/teachers/probabilistic_teacher.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/teachers/sample_probabilistic_teacher.py` & `pymodelextractor-0.9.9/pymodelextractor/teachers/sample_probabilistic_teacher.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/teachers/teacher.py` & `pymodelextractor-0.9.9/pymodelextractor/teachers/teacher.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_bounded_lstar_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_bounded_lstar_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_bounded_pdfa_lstar_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_bounded_pdfa_lstar_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_bounded_pdfa_quantization_n_ary_tree_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_bounded_pdfa_quantization_n_ary_tree_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_kearns_vazirani_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_kearns_vazirani_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_lambda_star_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_lambda_star_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_lstar_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_lstar_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_lstarcol_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_lstarcol_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pac_boolean_model_teacher.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pac_boolean_model_teacher.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_kearns_vazirani_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_kearns_vazirani_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_lstar_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_lstar_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_lstarcol_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_lstarcol_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_n_ary_tree_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_n_ary_tree_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_quantization_n_ary_tree_learner.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_quantization_n_ary_tree_learner.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_quantization_n_ary_tree_learner_metrics.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_quantization_n_ary_tree_learner_metrics.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_teachers_pdfa_lstar.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_teachers_pdfa_lstar.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/pymodelextractor/tests/learners_tests/test_pdfa_teachers_pdfa_lstar_col.py` & `pymodelextractor-0.9.9/pymodelextractor/tests/learners_tests/test_pdfa_teachers_pdfa_lstar_col.py`

 * *Files identical despite different names*

### Comparing `pymodelextractor-0.9.8/setup.py` & `pymodelextractor-0.9.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,19 +12,19 @@
  'pymodelextractor.tests',
  'pymodelextractor.tests.learners_tests']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['pythautomata>=0.16.4,<0.17.0']
+['pythautomata>=0.16.5,<0.17.0']
 
 setup_kwargs = {
     'name': 'pymodelextractor',
-    'version': '0.9.8',
+    'version': '0.9.9',
     'description': '',
     'long_description': None,
     'author': 'Federico VIlensky',
     'author_email': 'fedevilensky@gmail.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': None,
```

