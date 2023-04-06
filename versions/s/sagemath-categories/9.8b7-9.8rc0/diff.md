# Comparing `tmp/sagemath-categories-9.8b7.tar.gz` & `tmp/sagemath-categories-9.8rc0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sagemath-categories-9.8b7.tar", last modified: Thu Jan 19 06:51:51 2023, max compression
+gzip compressed data, was "sagemath-categories-9.8rc0.tar", last modified: Sun Jan 29 23:47:18 2023, max compression
```

## Comparing `sagemath-categories-9.8b7.tar` & `sagemath-categories-9.8rc0.tar`

### file list

```diff
@@ -1,239 +1,239 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:51.762921 sagemath-categories-9.8b7/
--rw-r--r--   0 runner    (1001) docker     (123)     1585 2023-01-19 06:47:53.000000 sagemath-categories-9.8b7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1660 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/MANIFEST.in.m4
--rw-r--r--   0 runner    (1001) docker     (123)     3208 2023-01-19 06:51:51.762921 sagemath-categories-9.8b7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/VERSION.txt
--rw-r--r--   0 runner    (1001) docker     (123)      321 2023-01-19 06:47:53.000000 sagemath-categories-9.8b7/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      418 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/pyproject.toml.m4
--rw-r--r--   0 runner    (1001) docker     (123)      314 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/requirements.txt.m4
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:51.738921 sagemath-categories-9.8b7/sage/
--rw-r--r--   0 runner    (1001) docker     (123)      123 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/all__sagemath_categories.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:51.758921 sagemath-categories-9.8b7/sage/categories/
--rw-r--r--   0 runner    (1001) docker     (123)     2786 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/additive_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    38961 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/additive_magmas.py
--rw-r--r--   0 runner    (1001) docker     (123)     3475 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/additive_monoids.py
--rw-r--r--   0 runner    (1001) docker     (123)     7074 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/additive_semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)     7670 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/affine_weyl_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     2926 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/algebra_ideals.py
--rw-r--r--   0 runner    (1001) docker     (123)     3145 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/algebra_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)    10110 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)    15205 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     5801 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/all.py
--rw-r--r--   0 runner    (1001) docker     (123)      883 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/all__sagemath_objects.py
--rw-r--r--   0 runner    (1001) docker     (123)     1052 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/aperiodic_semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)     1692 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/associative_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     2943 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/bialgebras.py
--rw-r--r--   0 runner    (1001) docker     (123)    15468 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/bialgebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     6702 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/bimodules.py
--rw-r--r--   0 runner    (1001) docker     (123)     8988 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/chain_complexes.py
--rw-r--r--   0 runner    (1001) docker     (123)    20657 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/classical_crystals.py
--rw-r--r--   0 runner    (1001) docker     (123)    14142 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/coalgebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     9145 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/coalgebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     1523 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/coercion_methods.pyx
--rw-r--r--   0 runner    (1001) docker     (123)     3946 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/commutative_additive_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     1500 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/commutative_additive_monoids.py
--rw-r--r--   0 runner    (1001) docker     (123)     1567 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/commutative_additive_semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)     2790 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/commutative_algebra_ideals.py
--rw-r--r--   0 runner    (1001) docker     (123)     3231 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/commutative_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     1912 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/commutative_ring_ideals.py
--rw-r--r--   0 runner    (1001) docker     (123)    14142 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/commutative_rings.py
--rw-r--r--   0 runner    (1001) docker     (123)     8523 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/complete_discrete_valuation.py
--rw-r--r--   0 runner    (1001) docker     (123)     5025 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/complex_reflection_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    50577 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/complex_reflection_or_generalized_coxeter_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     7486 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/coxeter_group_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)   121799 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/coxeter_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)   103540 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/crystals.py
--rw-r--r--   0 runner    (1001) docker     (123)     6539 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/cw_complexes.py
--rw-r--r--   0 runner    (1001) docker     (123)     9990 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/discrete_valuation.py
--rw-r--r--   0 runner    (1001) docker     (123)     3831 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/distributive_magmas_and_additive_magmas.py
--rw-r--r--   0 runner    (1001) docker     (123)     3516 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/division_rings.py
--rw-r--r--   0 runner    (1001) docker     (123)     2776 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/domains.py
--rw-r--r--   0 runner    (1001) docker     (123)     1218 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/dual.py
--rw-r--r--   0 runner    (1001) docker     (123)    41551 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/enumerated_sets.py
--rw-r--r--   0 runner    (1001) docker     (123)     8877 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/euclidean_domains.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:51.758921 sagemath-categories-9.8b7/sage/categories/examples/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3620 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     4614 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/commutative_additive_monoids.py
--rw-r--r--   0 runner    (1001) docker     (123)     7067 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/commutative_additive_semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)      166 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/coxeter_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     8178 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/crystals.py
--rw-r--r--   0 runner    (1001) docker     (123)     5029 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/cw_complexes.py
--rw-r--r--   0 runner    (1001) docker     (123)     6459 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/facade_sets.py
--rw-r--r--   0 runner    (1001) docker     (123)     7016 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/filtered_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     5386 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/filtered_modules_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     7543 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/finite_coxeter_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     4676 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/finite_dimensional_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)    12957 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/finite_dimensional_lie_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     6841 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/finite_enumerated_sets.py
--rw-r--r--   0 runner    (1001) docker     (123)     4841 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/finite_monoids.py
--rw-r--r--   0 runner    (1001) docker     (123)     6363 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/finite_semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)     5467 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/finite_weyl_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     4435 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/graded_connected_hopf_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     5978 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/graded_modules_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     3285 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/graphs.py
--rw-r--r--   0 runner    (1001) docker     (123)     4811 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/hopf_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     5935 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/infinite_enumerated_sets.py
--rw-r--r--   0 runner    (1001) docker     (123)    10628 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/lie_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     6420 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/lie_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     4479 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/magmas.py
--rw-r--r--   0 runner    (1001) docker     (123)     2719 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/manifolds.py
--rw-r--r--   0 runner    (1001) docker     (123)     4424 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/monoids.py
--rw-r--r--   0 runner    (1001) docker     (123)     5515 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/posets.py
--rw-r--r--   0 runner    (1001) docker     (123)    17201 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)     6845 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/semigroups_cython.pyx
--rw-r--r--   0 runner    (1001) docker     (123)    21264 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/sets_cat.py
--rw-r--r--   0 runner    (1001) docker     (123)     2583 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/sets_with_grading.py
--rw-r--r--   0 runner    (1001) docker     (123)    20007 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/examples/with_realizations.py
--rw-r--r--   0 runner    (1001) docker     (123)    27312 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/fields.py
--rw-r--r--   0 runner    (1001) docker     (123)     2147 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/filtered_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)    22828 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/filtered_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     5204 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/filtered_hopf_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     5677 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/filtered_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)    43940 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/filtered_modules_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)    53582 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_complex_reflection_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    36971 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_coxeter_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     3603 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_crystals.py
--rw-r--r--   0 runner    (1001) docker     (123)    65623 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_dimensional_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     1223 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_dimensional_bialgebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     1228 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_dimensional_coalgebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     9198 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_dimensional_graded_lie_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     1327 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_dimensional_hopf_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)    66887 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_dimensional_lie_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)    31409 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_dimensional_modules_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     6304 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_dimensional_nilpotent_lie_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)    11048 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_dimensional_semisimple_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)    28089 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_enumerated_sets.py
--rw-r--r--   0 runner    (1001) docker     (123)     3025 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_fields.py
--rw-r--r--   0 runner    (1001) docker     (123)     9273 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     8691 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_lattice_posets.py
--rw-r--r--   0 runner    (1001) docker     (123)    10090 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_monoids.py
--rw-r--r--   0 runner    (1001) docker     (123)    12927 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_permutation_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    83826 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_posets.py
--rw-r--r--   0 runner    (1001) docker     (123)     4908 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)     2848 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_sets.py
--rw-r--r--   0 runner    (1001) docker     (123)      999 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finite_weyl_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     3781 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finitely_generated_lambda_bracket_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     4041 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finitely_generated_lie_conformal_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     1653 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finitely_generated_magmas.py
--rw-r--r--   0 runner    (1001) docker     (123)     8019 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/finitely_generated_semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)     2192 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/function_fields.py
--rw-r--r--   0 runner    (1001) docker     (123)     2190 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/g_sets.py
--rw-r--r--   0 runner    (1001) docker     (123)     1646 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/gcd_domains.py
--rw-r--r--   0 runner    (1001) docker     (123)     3476 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/generalized_coxeter_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     2843 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     9278 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)      980 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_bialgebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_bialgebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     2301 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_coalgebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     1921 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_coalgebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     1380 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_hopf_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     6097 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_hopf_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     3169 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_lie_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     1623 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_lie_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     2364 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_lie_conformal_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     4710 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)    14109 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graded_modules_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     4006 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/graphs.py
--rw-r--r--   0 runner    (1001) docker     (123)    15552 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/group_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     2640 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/groupoid.py
--rw-r--r--   0 runner    (1001) docker     (123)    25595 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     2519 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/h_trivial_semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)     7202 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/hecke_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)    40213 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/highest_weight_crystals.py
--rw-r--r--   0 runner    (1001) docker     (123)     7314 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/hopf_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)    11314 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/hopf_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     3660 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/infinite_enumerated_sets.py
--rw-r--r--   0 runner    (1001) docker     (123)     4808 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/integral_domains.py
--rw-r--r--   0 runner    (1001) docker     (123)     1117 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/j_trivial_semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)     2723 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/kac_moody_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     1997 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/l_trivial_semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)     9042 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/lambda_bracket_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     3497 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/lambda_bracket_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     2523 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/lattice_posets.py
--rw-r--r--   0 runner    (1001) docker     (123)     1375 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/left_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)    35961 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/lie_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     8985 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/lie_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)    13316 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/lie_conformal_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     5298 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/lie_conformal_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     2282 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/lie_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    50214 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/loop_crystals.py
--rw-r--r--   0 runner    (1001) docker     (123)    43981 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/magmas.py
--rw-r--r--   0 runner    (1001) docker     (123)     5601 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/magmas_and_additive_magmas.py
--rw-r--r--   0 runner    (1001) docker     (123)    12705 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/magmatic_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)    11435 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/manifolds.py
--rw-r--r--   0 runner    (1001) docker     (123)     1129 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/matrix_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)    14491 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/metric_spaces.py
--rw-r--r--   0 runner    (1001) docker     (123)     2281 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/modular_abelian_varieties.py
--rw-r--r--   0 runner    (1001) docker     (123)    37564 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/modules.py
--rw-r--r--   0 runner    (1001) docker     (123)    94826 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/modules_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     1200 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/monoid_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)    25356 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/monoids.py
--rw-r--r--   0 runner    (1001) docker     (123)     8639 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/number_fields.py
--rw-r--r--   0 runner    (1001) docker     (123)     1422 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/partially_ordered_monoids.py
--rw-r--r--   0 runner    (1001) docker     (123)     1979 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/permutation_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     1101 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/pointed_sets.py
--rw-r--r--   0 runner    (1001) docker     (123)     2895 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/polyhedra.py
--rw-r--r--   0 runner    (1001) docker     (123)     9919 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/poor_man_map.py
--rw-r--r--   0 runner    (1001) docker     (123)    23895 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/posets.py
--rw-r--r--   0 runner    (1001) docker     (123)     4562 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/principal_ideal_domains.py
--rw-r--r--   0 runner    (1001) docker     (123)    23944 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/quantum_group_representations.py
--rw-r--r--   0 runner    (1001) docker     (123)    27079 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/quotient_fields.py
--rw-r--r--   0 runner    (1001) docker     (123)     1508 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/r_trivial_semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)    35645 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/regular_crystals.py
--rw-r--r--   0 runner    (1001) docker     (123)     5905 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/regular_supercrystals.py
--rw-r--r--   0 runner    (1001) docker     (123)     1389 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/right_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)     2176 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/ring_ideals.py
--rw-r--r--   0 runner    (1001) docker     (123)    53766 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/rings.py
--rw-r--r--   0 runner    (1001) docker     (123)     1841 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/rngs.py
--rw-r--r--   0 runner    (1001) docker     (123)     5956 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/schemes.py
--rw-r--r--   0 runner    (1001) docker     (123)    38092 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/semigroups.py
--rw-r--r--   0 runner    (1001) docker     (123)     1737 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/semirings.py
--rw-r--r--   0 runner    (1001) docker     (123)     3559 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/semisimple_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     8127 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/sets_with_grading.py
--rw-r--r--   0 runner    (1001) docker     (123)     1384 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/shephard_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     4387 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/signed_tensor.py
--rw-r--r--   0 runner    (1001) docker     (123)     4060 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/simplicial_complexes.py
--rw-r--r--   0 runner    (1001) docker     (123)    23083 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/simplicial_sets.py
--rw-r--r--   0 runner    (1001) docker     (123)     5219 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/super_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     5262 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/super_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     4724 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/super_hopf_algebras_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     6969 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/super_lie_conformal_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     7951 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/super_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)     6236 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/super_modules_with_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     3616 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/supercommutative_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)    17163 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/supercrystals.py
--rw-r--r--   0 runner    (1001) docker     (123)     3734 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/tensor.py
--rw-r--r--   0 runner    (1001) docker     (123)     5926 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/topological_spaces.py
--rw-r--r--   0 runner    (1001) docker     (123)     9018 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/triangular_kac_moody_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     1938 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/tutorial.py
--rw-r--r--   0 runner    (1001) docker     (123)     9625 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/unique_factorization_domains.py
--rw-r--r--   0 runner    (1001) docker     (123)    15211 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/unital_algebras.py
--rw-r--r--   0 runner    (1001) docker     (123)     5566 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/vector_bundles.py
--rw-r--r--   0 runner    (1001) docker     (123)    12646 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/vector_spaces.py
--rw-r--r--   0 runner    (1001) docker     (123)    35576 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/sage/categories/weyl_groups.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:51.762921 sagemath-categories-9.8b7/sage/rings/
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-01-19 06:47:41.000000 sagemath-categories-9.8b7/sage/rings/all__sagemath_categories.py
--rw-r--r--   0 runner    (1001) docker     (123)    55933 2023-01-19 06:47:41.000000 sagemath-categories-9.8b7/sage/rings/ideal.py
--rw-r--r--   0 runner    (1001) docker     (123)      752 2023-01-19 06:47:41.000000 sagemath-categories-9.8b7/sage/rings/ring.pxd
--rw-r--r--   0 runner    (1001) docker     (123)    78717 2023-01-19 06:47:41.000000 sagemath-categories-9.8b7/sage/rings/ring.pyx
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:51.762921 sagemath-categories-9.8b7/sage/typeset/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-19 06:47:41.000000 sagemath-categories-9.8b7/sage/typeset/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      153 2023-01-19 06:47:41.000000 sagemath-categories-9.8b7/sage/typeset/all.py
--rw-r--r--   0 runner    (1001) docker     (123)    11982 2023-01-19 06:47:41.000000 sagemath-categories-9.8b7/sage/typeset/ascii_art.py
--rw-r--r--   0 runner    (1001) docker     (123)    23537 2023-01-19 06:47:41.000000 sagemath-categories-9.8b7/sage/typeset/character_art.py
--rw-r--r--   0 runner    (1001) docker     (123)    19911 2023-01-19 06:47:41.000000 sagemath-categories-9.8b7/sage/typeset/character_art_factory.py
--rw-r--r--   0 runner    (1001) docker     (123)    10543 2023-01-19 06:47:41.000000 sagemath-categories-9.8b7/sage/typeset/symbols.py
--rw-r--r--   0 runner    (1001) docker     (123)     6459 2023-01-19 06:47:41.000000 sagemath-categories-9.8b7/sage/typeset/unicode_art.py
--rw-r--r--   0 runner    (1001) docker     (123)     2572 2023-01-19 06:47:41.000000 sagemath-categories-9.8b7/sage/typeset/unicode_characters.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:51.762921 sagemath-categories-9.8b7/sagemath_categories.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3208 2023-01-19 06:51:50.000000 sagemath-categories-9.8b7/sagemath_categories.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     8944 2023-01-19 06:51:51.000000 sagemath-categories-9.8b7/sagemath_categories.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-19 06:51:50.000000 sagemath-categories-9.8b7/sagemath_categories.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       46 2023-01-19 06:51:50.000000 sagemath-categories-9.8b7/sagemath_categories.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-19 06:51:50.000000 sagemath-categories-9.8b7/sagemath_categories.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1139 2023-01-19 06:51:51.762921 sagemath-categories-9.8b7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1251 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/setup.cfg.m4
--rw-r--r--   0 runner    (1001) docker     (123)     1647 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/setup.py
--rw-r--r--   0 runner    (1001) docker     (123)     2595 2023-01-19 06:47:40.000000 sagemath-categories-9.8b7/tox.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:18.109627 sagemath-categories-9.8rc0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1585 2023-01-29 23:43:57.000000 sagemath-categories-9.8rc0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1660 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/MANIFEST.in.m4
+-rw-r--r--   0 runner    (1001) docker     (123)     3209 2023-01-29 23:47:18.109627 sagemath-categories-9.8rc0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/VERSION.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      324 2023-01-29 23:43:57.000000 sagemath-categories-9.8rc0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      418 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/pyproject.toml.m4
+-rw-r--r--   0 runner    (1001) docker     (123)      314 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/requirements.txt.m4
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:18.085627 sagemath-categories-9.8rc0/sage/
+-rw-r--r--   0 runner    (1001) docker     (123)      123 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/all__sagemath_categories.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:18.101627 sagemath-categories-9.8rc0/sage/categories/
+-rw-r--r--   0 runner    (1001) docker     (123)     2786 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/additive_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38961 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/additive_magmas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3475 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/additive_monoids.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7074 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/additive_semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7670 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/affine_weyl_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2926 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/algebra_ideals.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3145 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/algebra_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10110 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15205 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5801 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/all.py
+-rw-r--r--   0 runner    (1001) docker     (123)      883 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/all__sagemath_objects.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1052 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/aperiodic_semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1692 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/associative_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2943 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/bialgebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15468 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/bialgebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6702 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/bimodules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8988 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/chain_complexes.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20657 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/classical_crystals.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14142 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/coalgebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9145 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/coalgebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1523 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/coercion_methods.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)     3946 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/commutative_additive_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1500 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/commutative_additive_monoids.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1567 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/commutative_additive_semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2790 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/commutative_algebra_ideals.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3231 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/commutative_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1912 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/commutative_ring_ideals.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14142 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/commutative_rings.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8523 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/complete_discrete_valuation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5025 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/complex_reflection_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    50577 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/complex_reflection_or_generalized_coxeter_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7486 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/coxeter_group_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)   121799 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/coxeter_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)   103540 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/crystals.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6539 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/cw_complexes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9990 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/discrete_valuation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3831 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/distributive_magmas_and_additive_magmas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3516 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/division_rings.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2776 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/domains.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1218 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/dual.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41551 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/enumerated_sets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8877 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/euclidean_domains.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:18.101627 sagemath-categories-9.8rc0/sage/categories/examples/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3620 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4614 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/commutative_additive_monoids.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7067 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/commutative_additive_semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)      166 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/coxeter_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8178 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/crystals.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5029 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/cw_complexes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6459 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/facade_sets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7016 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/filtered_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5386 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/filtered_modules_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7543 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/finite_coxeter_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4676 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/finite_dimensional_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12957 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/finite_dimensional_lie_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6841 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/finite_enumerated_sets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4841 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/finite_monoids.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6363 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/finite_semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5467 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/finite_weyl_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4435 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/graded_connected_hopf_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5978 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/graded_modules_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3285 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/graphs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4811 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/hopf_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5935 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/infinite_enumerated_sets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10628 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/lie_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6420 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/lie_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4479 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/magmas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2719 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/manifolds.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4424 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/monoids.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5515 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/posets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17201 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6845 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/semigroups_cython.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)    21264 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/sets_cat.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2583 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/sets_with_grading.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20007 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/examples/with_realizations.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27312 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2147 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/filtered_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22828 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/filtered_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5204 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/filtered_hopf_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5677 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/filtered_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)    43940 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/filtered_modules_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    53582 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_complex_reflection_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36971 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_coxeter_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3603 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_crystals.py
+-rw-r--r--   0 runner    (1001) docker     (123)    65623 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_dimensional_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1223 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_dimensional_bialgebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1228 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_dimensional_coalgebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9198 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_dimensional_graded_lie_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1327 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_dimensional_hopf_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    66887 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_dimensional_lie_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31409 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_dimensional_modules_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6304 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_dimensional_nilpotent_lie_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11048 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_dimensional_semisimple_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28089 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_enumerated_sets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3025 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9273 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8691 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_lattice_posets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10090 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_monoids.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12927 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_permutation_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    83826 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_posets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4908 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2848 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_sets.py
+-rw-r--r--   0 runner    (1001) docker     (123)      999 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finite_weyl_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3781 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finitely_generated_lambda_bracket_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4041 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finitely_generated_lie_conformal_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1653 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finitely_generated_magmas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8019 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/finitely_generated_semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2192 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/function_fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2190 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/g_sets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1646 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/gcd_domains.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3476 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/generalized_coxeter_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2843 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9278 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)      980 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_bialgebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_bialgebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2301 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_coalgebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1921 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_coalgebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1380 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_hopf_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6097 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_hopf_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3169 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_lie_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1623 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_lie_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2364 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_lie_conformal_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4710 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14109 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graded_modules_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4006 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/graphs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15552 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/group_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2640 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/groupoid.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25595 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2519 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/h_trivial_semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7202 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/hecke_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40213 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/highest_weight_crystals.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7314 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/hopf_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11314 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/hopf_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3660 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/infinite_enumerated_sets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4808 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/integral_domains.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1117 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/j_trivial_semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2723 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/kac_moody_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1997 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/l_trivial_semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9042 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/lambda_bracket_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3497 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/lambda_bracket_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2523 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/lattice_posets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1375 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/left_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35961 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/lie_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8985 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/lie_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13316 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/lie_conformal_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5298 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/lie_conformal_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2282 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/lie_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    50214 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/loop_crystals.py
+-rw-r--r--   0 runner    (1001) docker     (123)    43981 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/magmas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5601 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/magmas_and_additive_magmas.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12705 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/magmatic_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11435 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/manifolds.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1129 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/matrix_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14491 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/metric_spaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2281 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/modular_abelian_varieties.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37564 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)    94826 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/modules_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1200 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/monoid_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25356 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/monoids.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8639 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/number_fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1422 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/partially_ordered_monoids.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1979 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/permutation_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1101 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/pointed_sets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2895 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/polyhedra.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9919 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/poor_man_map.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23895 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/posets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4562 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/principal_ideal_domains.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23944 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/quantum_group_representations.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27079 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/quotient_fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1508 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/r_trivial_semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35645 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/regular_crystals.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5905 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/regular_supercrystals.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1389 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/right_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2176 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/ring_ideals.py
+-rw-r--r--   0 runner    (1001) docker     (123)    53766 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/rings.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1841 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/rngs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5956 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/schemes.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38092 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/semigroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1737 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/semirings.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3559 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/semisimple_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8127 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/sets_with_grading.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1384 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/shephard_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4387 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/signed_tensor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4060 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/simplicial_complexes.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23083 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/simplicial_sets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5219 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/super_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5262 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/super_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4724 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/super_hopf_algebras_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6969 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/super_lie_conformal_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7951 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/super_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6236 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/super_modules_with_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3616 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/supercommutative_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17163 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/supercrystals.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3734 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/tensor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5926 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/topological_spaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9018 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/triangular_kac_moody_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1938 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/tutorial.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9625 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/unique_factorization_domains.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15211 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/unital_algebras.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5566 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/vector_bundles.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12646 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/vector_spaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35576 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/categories/weyl_groups.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:18.101627 sagemath-categories-9.8rc0/sage/rings/
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/rings/all__sagemath_categories.py
+-rw-r--r--   0 runner    (1001) docker     (123)    55933 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/rings/ideal.py
+-rw-r--r--   0 runner    (1001) docker     (123)      752 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/rings/ring.pxd
+-rw-r--r--   0 runner    (1001) docker     (123)    78717 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/rings/ring.pyx
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:18.109627 sagemath-categories-9.8rc0/sage/typeset/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/typeset/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      153 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/typeset/all.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11982 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/typeset/ascii_art.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23537 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/typeset/character_art.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19911 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/typeset/character_art_factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10543 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/typeset/symbols.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6459 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/typeset/unicode_art.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2572 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/sage/typeset/unicode_characters.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:18.109627 sagemath-categories-9.8rc0/sagemath_categories.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3209 2023-01-29 23:47:16.000000 sagemath-categories-9.8rc0/sagemath_categories.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8944 2023-01-29 23:47:18.000000 sagemath-categories-9.8rc0/sagemath_categories.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-29 23:47:16.000000 sagemath-categories-9.8rc0/sagemath_categories.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       47 2023-01-29 23:47:16.000000 sagemath-categories-9.8rc0/sagemath_categories.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-29 23:47:16.000000 sagemath-categories-9.8rc0/sagemath_categories.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1140 2023-01-29 23:47:18.109627 sagemath-categories-9.8rc0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1251 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/setup.cfg.m4
+-rw-r--r--   0 runner    (1001) docker     (123)     1338 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2595 2023-01-29 23:43:48.000000 sagemath-categories-9.8rc0/tox.ini
```

### Comparing `sagemath-categories-9.8b7/MANIFEST.in` & `sagemath-categories-9.8rc0/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/MANIFEST.in.m4` & `sagemath-categories-9.8rc0/MANIFEST.in.m4`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/PKG-INFO` & `sagemath-categories-9.8rc0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sagemath-categories
-Version: 9.8b7
+Version: 9.8rc0
 Summary: Sage: Open Source Mathematics Software: Sage categories and basic rings
 Home-page: https://www.sagemath.org
 Author: The Sage Developers
 Author-email: sage-support@googlegroups.com
 License: GNU General Public License (GPL) v2 or later
 Classifier: Development Status :: 6 - Mature
 Classifier: Intended Audience :: Education
```

### Comparing `sagemath-categories-9.8b7/README.rst` & `sagemath-categories-9.8rc0/README.rst`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/additive_groups.py` & `sagemath-categories-9.8rc0/sage/categories/additive_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/additive_magmas.py` & `sagemath-categories-9.8rc0/sage/categories/additive_magmas.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/additive_monoids.py` & `sagemath-categories-9.8rc0/sage/categories/additive_monoids.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/additive_semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/additive_semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/affine_weyl_groups.py` & `sagemath-categories-9.8rc0/sage/categories/affine_weyl_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/algebra_ideals.py` & `sagemath-categories-9.8rc0/sage/categories/algebra_ideals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/algebra_modules.py` & `sagemath-categories-9.8rc0/sage/categories/algebra_modules.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/algebras.py` & `sagemath-categories-9.8rc0/sage/categories/algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/all.py` & `sagemath-categories-9.8rc0/sage/categories/all.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/all__sagemath_objects.py` & `sagemath-categories-9.8rc0/sage/categories/all__sagemath_objects.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/aperiodic_semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/aperiodic_semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/associative_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/associative_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/bialgebras.py` & `sagemath-categories-9.8rc0/sage/categories/bialgebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/bialgebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/bialgebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/bimodules.py` & `sagemath-categories-9.8rc0/sage/categories/bimodules.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/chain_complexes.py` & `sagemath-categories-9.8rc0/sage/categories/chain_complexes.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/classical_crystals.py` & `sagemath-categories-9.8rc0/sage/categories/classical_crystals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/coalgebras.py` & `sagemath-categories-9.8rc0/sage/categories/coalgebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/coalgebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/coalgebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/coercion_methods.pyx` & `sagemath-categories-9.8rc0/sage/categories/coercion_methods.pyx`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/commutative_additive_groups.py` & `sagemath-categories-9.8rc0/sage/categories/commutative_additive_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/commutative_additive_monoids.py` & `sagemath-categories-9.8rc0/sage/categories/commutative_additive_monoids.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/commutative_additive_semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/commutative_additive_semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/commutative_algebra_ideals.py` & `sagemath-categories-9.8rc0/sage/categories/commutative_algebra_ideals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/commutative_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/commutative_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/commutative_ring_ideals.py` & `sagemath-categories-9.8rc0/sage/categories/commutative_ring_ideals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/commutative_rings.py` & `sagemath-categories-9.8rc0/sage/categories/commutative_rings.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/complete_discrete_valuation.py` & `sagemath-categories-9.8rc0/sage/categories/complete_discrete_valuation.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/complex_reflection_groups.py` & `sagemath-categories-9.8rc0/sage/categories/complex_reflection_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/complex_reflection_or_generalized_coxeter_groups.py` & `sagemath-categories-9.8rc0/sage/categories/complex_reflection_or_generalized_coxeter_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/coxeter_group_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/coxeter_group_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/coxeter_groups.py` & `sagemath-categories-9.8rc0/sage/categories/coxeter_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/crystals.py` & `sagemath-categories-9.8rc0/sage/categories/crystals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/cw_complexes.py` & `sagemath-categories-9.8rc0/sage/categories/cw_complexes.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/discrete_valuation.py` & `sagemath-categories-9.8rc0/sage/categories/discrete_valuation.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/distributive_magmas_and_additive_magmas.py` & `sagemath-categories-9.8rc0/sage/categories/distributive_magmas_and_additive_magmas.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/division_rings.py` & `sagemath-categories-9.8rc0/sage/categories/division_rings.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/domains.py` & `sagemath-categories-9.8rc0/sage/categories/domains.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/dual.py` & `sagemath-categories-9.8rc0/sage/categories/dual.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/enumerated_sets.py` & `sagemath-categories-9.8rc0/sage/categories/enumerated_sets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/euclidean_domains.py` & `sagemath-categories-9.8rc0/sage/categories/euclidean_domains.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/examples/algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/commutative_additive_monoids.py` & `sagemath-categories-9.8rc0/sage/categories/examples/commutative_additive_monoids.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/commutative_additive_semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/examples/commutative_additive_semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/crystals.py` & `sagemath-categories-9.8rc0/sage/categories/examples/crystals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/cw_complexes.py` & `sagemath-categories-9.8rc0/sage/categories/examples/cw_complexes.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/facade_sets.py` & `sagemath-categories-9.8rc0/sage/categories/examples/facade_sets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/filtered_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/examples/filtered_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/filtered_modules_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/examples/filtered_modules_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/finite_coxeter_groups.py` & `sagemath-categories-9.8rc0/sage/categories/examples/finite_coxeter_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/finite_dimensional_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/examples/finite_dimensional_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/finite_dimensional_lie_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/examples/finite_dimensional_lie_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/finite_enumerated_sets.py` & `sagemath-categories-9.8rc0/sage/categories/examples/finite_enumerated_sets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/finite_monoids.py` & `sagemath-categories-9.8rc0/sage/categories/examples/finite_monoids.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/finite_semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/examples/finite_semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/finite_weyl_groups.py` & `sagemath-categories-9.8rc0/sage/categories/examples/finite_weyl_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/graded_connected_hopf_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/examples/graded_connected_hopf_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/graded_modules_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/examples/graded_modules_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/graphs.py` & `sagemath-categories-9.8rc0/sage/categories/examples/graphs.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/hopf_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/examples/hopf_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/infinite_enumerated_sets.py` & `sagemath-categories-9.8rc0/sage/categories/examples/infinite_enumerated_sets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/lie_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/examples/lie_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/lie_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/examples/lie_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/magmas.py` & `sagemath-categories-9.8rc0/sage/categories/examples/magmas.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/manifolds.py` & `sagemath-categories-9.8rc0/sage/categories/examples/manifolds.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/monoids.py` & `sagemath-categories-9.8rc0/sage/categories/examples/monoids.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/posets.py` & `sagemath-categories-9.8rc0/sage/categories/examples/posets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/examples/semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/semigroups_cython.pyx` & `sagemath-categories-9.8rc0/sage/categories/examples/semigroups_cython.pyx`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/sets_cat.py` & `sagemath-categories-9.8rc0/sage/categories/examples/sets_cat.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/sets_with_grading.py` & `sagemath-categories-9.8rc0/sage/categories/examples/sets_with_grading.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/examples/with_realizations.py` & `sagemath-categories-9.8rc0/sage/categories/examples/with_realizations.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/fields.py` & `sagemath-categories-9.8rc0/sage/categories/fields.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/filtered_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/filtered_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/filtered_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/filtered_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/filtered_hopf_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/filtered_hopf_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/filtered_modules.py` & `sagemath-categories-9.8rc0/sage/categories/filtered_modules.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/filtered_modules_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/filtered_modules_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_complex_reflection_groups.py` & `sagemath-categories-9.8rc0/sage/categories/finite_complex_reflection_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_coxeter_groups.py` & `sagemath-categories-9.8rc0/sage/categories/finite_coxeter_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_crystals.py` & `sagemath-categories-9.8rc0/sage/categories/finite_crystals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_dimensional_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/finite_dimensional_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_dimensional_bialgebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/finite_dimensional_bialgebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_dimensional_coalgebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/finite_dimensional_coalgebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_dimensional_graded_lie_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/finite_dimensional_graded_lie_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_dimensional_hopf_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/finite_dimensional_hopf_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_dimensional_lie_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/finite_dimensional_lie_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_dimensional_modules_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/finite_dimensional_modules_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_dimensional_nilpotent_lie_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/finite_dimensional_nilpotent_lie_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_dimensional_semisimple_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/finite_dimensional_semisimple_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_enumerated_sets.py` & `sagemath-categories-9.8rc0/sage/categories/finite_enumerated_sets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_fields.py` & `sagemath-categories-9.8rc0/sage/categories/finite_fields.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_groups.py` & `sagemath-categories-9.8rc0/sage/categories/finite_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_lattice_posets.py` & `sagemath-categories-9.8rc0/sage/categories/finite_lattice_posets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_monoids.py` & `sagemath-categories-9.8rc0/sage/categories/finite_monoids.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_permutation_groups.py` & `sagemath-categories-9.8rc0/sage/categories/finite_permutation_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_posets.py` & `sagemath-categories-9.8rc0/sage/categories/finite_posets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/finite_semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_sets.py` & `sagemath-categories-9.8rc0/sage/categories/finite_sets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finite_weyl_groups.py` & `sagemath-categories-9.8rc0/sage/categories/finite_weyl_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finitely_generated_lambda_bracket_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/finitely_generated_lambda_bracket_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finitely_generated_lie_conformal_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/finitely_generated_lie_conformal_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finitely_generated_magmas.py` & `sagemath-categories-9.8rc0/sage/categories/finitely_generated_magmas.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/finitely_generated_semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/finitely_generated_semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/function_fields.py` & `sagemath-categories-9.8rc0/sage/categories/function_fields.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/g_sets.py` & `sagemath-categories-9.8rc0/sage/categories/g_sets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/gcd_domains.py` & `sagemath-categories-9.8rc0/sage/categories/gcd_domains.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/generalized_coxeter_groups.py` & `sagemath-categories-9.8rc0/sage/categories/generalized_coxeter_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/graded_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/graded_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_bialgebras.py` & `sagemath-categories-9.8rc0/sage/categories/graded_bialgebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_bialgebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/graded_bialgebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_coalgebras.py` & `sagemath-categories-9.8rc0/sage/categories/graded_coalgebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_coalgebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/graded_coalgebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_hopf_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/graded_hopf_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_hopf_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/graded_hopf_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_lie_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/graded_lie_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_lie_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/graded_lie_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_lie_conformal_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/graded_lie_conformal_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_modules.py` & `sagemath-categories-9.8rc0/sage/categories/graded_modules.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graded_modules_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/graded_modules_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/graphs.py` & `sagemath-categories-9.8rc0/sage/categories/graphs.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/group_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/group_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/groupoid.py` & `sagemath-categories-9.8rc0/sage/categories/groupoid.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/groups.py` & `sagemath-categories-9.8rc0/sage/categories/groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/h_trivial_semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/h_trivial_semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/hecke_modules.py` & `sagemath-categories-9.8rc0/sage/categories/hecke_modules.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/highest_weight_crystals.py` & `sagemath-categories-9.8rc0/sage/categories/highest_weight_crystals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/hopf_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/hopf_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/hopf_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/hopf_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/infinite_enumerated_sets.py` & `sagemath-categories-9.8rc0/sage/categories/infinite_enumerated_sets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/integral_domains.py` & `sagemath-categories-9.8rc0/sage/categories/integral_domains.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/j_trivial_semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/j_trivial_semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/kac_moody_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/kac_moody_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/l_trivial_semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/l_trivial_semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/lambda_bracket_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/lambda_bracket_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/lambda_bracket_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/lambda_bracket_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/lattice_posets.py` & `sagemath-categories-9.8rc0/sage/categories/lattice_posets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/left_modules.py` & `sagemath-categories-9.8rc0/sage/categories/left_modules.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/lie_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/lie_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/lie_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/lie_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/lie_conformal_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/lie_conformal_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/lie_conformal_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/lie_conformal_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/lie_groups.py` & `sagemath-categories-9.8rc0/sage/categories/lie_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/loop_crystals.py` & `sagemath-categories-9.8rc0/sage/categories/loop_crystals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/magmas.py` & `sagemath-categories-9.8rc0/sage/categories/magmas.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/magmas_and_additive_magmas.py` & `sagemath-categories-9.8rc0/sage/categories/magmas_and_additive_magmas.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/magmatic_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/magmatic_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/manifolds.py` & `sagemath-categories-9.8rc0/sage/categories/manifolds.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/matrix_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/matrix_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/metric_spaces.py` & `sagemath-categories-9.8rc0/sage/categories/metric_spaces.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/modular_abelian_varieties.py` & `sagemath-categories-9.8rc0/sage/categories/modular_abelian_varieties.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/modules.py` & `sagemath-categories-9.8rc0/sage/categories/modules.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/modules_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/modules_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/monoid_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/monoid_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/monoids.py` & `sagemath-categories-9.8rc0/sage/categories/monoids.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/number_fields.py` & `sagemath-categories-9.8rc0/sage/categories/number_fields.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/partially_ordered_monoids.py` & `sagemath-categories-9.8rc0/sage/categories/partially_ordered_monoids.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/permutation_groups.py` & `sagemath-categories-9.8rc0/sage/categories/permutation_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/pointed_sets.py` & `sagemath-categories-9.8rc0/sage/categories/pointed_sets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/polyhedra.py` & `sagemath-categories-9.8rc0/sage/categories/polyhedra.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/poor_man_map.py` & `sagemath-categories-9.8rc0/sage/categories/poor_man_map.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/posets.py` & `sagemath-categories-9.8rc0/sage/categories/posets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/principal_ideal_domains.py` & `sagemath-categories-9.8rc0/sage/categories/principal_ideal_domains.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/quantum_group_representations.py` & `sagemath-categories-9.8rc0/sage/categories/quantum_group_representations.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/quotient_fields.py` & `sagemath-categories-9.8rc0/sage/categories/quotient_fields.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/r_trivial_semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/r_trivial_semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/regular_crystals.py` & `sagemath-categories-9.8rc0/sage/categories/regular_crystals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/regular_supercrystals.py` & `sagemath-categories-9.8rc0/sage/categories/regular_supercrystals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/right_modules.py` & `sagemath-categories-9.8rc0/sage/categories/right_modules.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/ring_ideals.py` & `sagemath-categories-9.8rc0/sage/categories/ring_ideals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/rings.py` & `sagemath-categories-9.8rc0/sage/categories/rings.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/rngs.py` & `sagemath-categories-9.8rc0/sage/categories/rngs.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/schemes.py` & `sagemath-categories-9.8rc0/sage/categories/schemes.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/semigroups.py` & `sagemath-categories-9.8rc0/sage/categories/semigroups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/semirings.py` & `sagemath-categories-9.8rc0/sage/categories/semirings.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/semisimple_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/semisimple_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/sets_with_grading.py` & `sagemath-categories-9.8rc0/sage/categories/sets_with_grading.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/shephard_groups.py` & `sagemath-categories-9.8rc0/sage/categories/shephard_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/signed_tensor.py` & `sagemath-categories-9.8rc0/sage/categories/signed_tensor.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/simplicial_complexes.py` & `sagemath-categories-9.8rc0/sage/categories/simplicial_complexes.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/simplicial_sets.py` & `sagemath-categories-9.8rc0/sage/categories/simplicial_sets.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/super_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/super_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/super_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/super_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/super_hopf_algebras_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/super_hopf_algebras_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/super_lie_conformal_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/super_lie_conformal_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/super_modules.py` & `sagemath-categories-9.8rc0/sage/categories/super_modules.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/super_modules_with_basis.py` & `sagemath-categories-9.8rc0/sage/categories/super_modules_with_basis.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/supercommutative_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/supercommutative_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/supercrystals.py` & `sagemath-categories-9.8rc0/sage/categories/supercrystals.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/tensor.py` & `sagemath-categories-9.8rc0/sage/categories/tensor.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/topological_spaces.py` & `sagemath-categories-9.8rc0/sage/categories/topological_spaces.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/triangular_kac_moody_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/triangular_kac_moody_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/tutorial.py` & `sagemath-categories-9.8rc0/sage/categories/tutorial.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/unique_factorization_domains.py` & `sagemath-categories-9.8rc0/sage/categories/unique_factorization_domains.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/unital_algebras.py` & `sagemath-categories-9.8rc0/sage/categories/unital_algebras.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/vector_bundles.py` & `sagemath-categories-9.8rc0/sage/categories/vector_bundles.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/vector_spaces.py` & `sagemath-categories-9.8rc0/sage/categories/vector_spaces.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/categories/weyl_groups.py` & `sagemath-categories-9.8rc0/sage/categories/weyl_groups.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/rings/ideal.py` & `sagemath-categories-9.8rc0/sage/rings/ideal.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/rings/ring.pxd` & `sagemath-categories-9.8rc0/sage/rings/ring.pxd`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/rings/ring.pyx` & `sagemath-categories-9.8rc0/sage/rings/ring.pyx`

 * *Files 0% similar despite different names*

```diff
@@ -1379,15 +1379,15 @@
         """
         from sage.rings.polynomial.polynomial_element import Polynomial
         if not isinstance(poly, Polynomial):
             try:
                 poly = poly.polynomial(self)
             except (AttributeError, TypeError):
                 raise TypeError("polynomial (=%s) must be a polynomial." % repr(poly))
-        if not names is None:
+        if names is not None:
             name = names
         if isinstance(name, tuple):
             name = name[0]
         if name is None:
             name = str(poly.parent().gen(0))
         for key, val in kwds.items():
             if key not in ['structure', 'implementation', 'prec', 'embedding', 'latex_name', 'latex_names']:
```

### Comparing `sagemath-categories-9.8b7/sage/typeset/ascii_art.py` & `sagemath-categories-9.8rc0/sage/typeset/ascii_art.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/typeset/character_art.py` & `sagemath-categories-9.8rc0/sage/typeset/character_art.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/typeset/character_art_factory.py` & `sagemath-categories-9.8rc0/sage/typeset/character_art_factory.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/typeset/symbols.py` & `sagemath-categories-9.8rc0/sage/typeset/symbols.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/typeset/unicode_art.py` & `sagemath-categories-9.8rc0/sage/typeset/unicode_art.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sage/typeset/unicode_characters.py` & `sagemath-categories-9.8rc0/sage/typeset/unicode_characters.py`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/sagemath_categories.egg-info/PKG-INFO` & `sagemath-categories-9.8rc0/sagemath_categories.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sagemath-categories
-Version: 9.8b7
+Version: 9.8rc0
 Summary: Sage: Open Source Mathematics Software: Sage categories and basic rings
 Home-page: https://www.sagemath.org
 Author: The Sage Developers
 Author-email: sage-support@googlegroups.com
 License: GNU General Public License (GPL) v2 or later
 Classifier: Development Status :: 6 - Mature
 Classifier: Intended Audience :: Education
```

### Comparing `sagemath-categories-9.8b7/sagemath_categories.egg-info/SOURCES.txt` & `sagemath-categories-9.8rc0/sagemath_categories.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/setup.cfg` & `sagemath-categories-9.8rc0/setup.cfg`

 * *Files 8% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 	Programming Language :: Python :: 3.11
 	Programming Language :: Python :: Implementation :: CPython
 	Topic :: Scientific/Engineering :: Mathematics
 
 [options]
 python_requires = >=3.8, <3.12
 install_requires = 
-	sagemath-objects ~= 9.8b7
+	sagemath-objects ~= 9.8rc0
 
 [options.extras_require]
 test = sagemath-repl
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `sagemath-categories-9.8b7/setup.cfg.m4` & `sagemath-categories-9.8rc0/setup.cfg.m4`

 * *Files identical despite different names*

### Comparing `sagemath-categories-9.8b7/setup.py` & `sagemath-categories-9.8rc0/setup.py`

 * *Files 24% similar despite different names*

```diff
@@ -10,49 +10,36 @@
     import multiprocessing
     multiprocessing.set_start_method('fork', force=True)
 
 # PEP 517 builds do not have . in sys.path
 import sys
 sys.path.insert(0, os.path.dirname(__file__))
 
-if len(sys.argv) > 1 and (sys.argv[1] == "sdist" or sys.argv[1] == "egg_info"):
-    sdist = True
-else:
-    sdist = False
-
-if sdist:
-    cmdclass = {}
-else:
-    from sage_setup.excepthook import excepthook
-    sys.excepthook = excepthook
-
-    from sage_setup.setenv import setenv
-    setenv()
-
-    import sage.env
-    sage.env.default_required_modules = sage.env.default_optional_modules = ()
-
-    from sage_setup.command.sage_build_cython import sage_build_cython
-    from sage_setup.command.sage_build_ext import sage_build_ext
-
-    cmdclass = dict(build_cython=sage_build_cython,
-                    build_ext=sage_build_ext)
-
-if sdist:
-    python_packages = []
-    python_modules = []
-    cython_modules = []
-else:
-    from sage_setup.find import find_python_sources
-    python_packages, python_modules, cython_modules = find_python_sources(
-        '.', ['sage'])   # for now, we do the filtering using MANIFEST
-
-    log.warn('python_packages = {0}'.format(python_packages))
-    log.warn('python_modules = {0}'.format(python_modules))
-    log.warn('cython_modules = {0}'.format(cython_modules))
+from sage_setup.excepthook import excepthook
+sys.excepthook = excepthook
+
+from sage_setup.setenv import setenv
+setenv()
+
+import sage.env
+sage.env.default_required_modules = sage.env.default_optional_modules = ()
+
+from sage_setup.command.sage_build_cython import sage_build_cython
+from sage_setup.command.sage_build_ext import sage_build_ext
+
+cmdclass = dict(build_cython=sage_build_cython,
+                build_ext=sage_build_ext)
+
+from sage_setup.find import find_python_sources
+python_packages, python_modules, cython_modules = find_python_sources(
+    '.', ['sage'])   # for now, we do the filtering using MANIFEST
+
+log.warn('python_packages = {0}'.format(python_packages))
+log.warn('python_modules = {0}'.format(python_modules))
+log.warn('cython_modules = {0}'.format(cython_modules))
 
 setup(
     cmdclass = cmdclass,
     packages = python_packages,
     py_modules  = python_modules,
     ext_modules = cython_modules,
 )
```

### Comparing `sagemath-categories-9.8b7/tox.ini` & `sagemath-categories-9.8rc0/tox.ini`

 * *Files 2% similar despite different names*

```diff
@@ -35,15 +35,15 @@
     # Sage scripts such as sage-runtests like to use $HOME/.sage
                              HOME={envdir}
     # We supply pip options by environment variables so that they
     # apply both to the installation of the dependencies and of the package
     sagewheels:              PIP_FIND_LINKS=file://{env:SAGE_SPKG_WHEELS:{env:SAGE_VENV:{toxinidir}/../../../../venv}/var/lib/sage/wheels}
     nopypi:                  PIP_NO_INDEX=true
 
-whitelist_externals =
+allowlist_externals =
     bash
 
 commands =
     # Beware of the treacherous non-src layout. "./sage/" shadows the install sage package.
     {envpython} -c 'import sys; "" in sys.path and sys.path.remove(""); import sage.cpython.builtin_types, sage.cpython.cython_metaclass, sage.cpython.debug, sage.structure.all, sage.categories.all'
 
     # Test that importing sage.categories.all initializes categories
```

