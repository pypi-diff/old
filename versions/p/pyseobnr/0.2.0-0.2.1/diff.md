# Comparing `tmp/pyseobnr-0.2.0.tar.gz` & `tmp/pyseobnr-0.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyseobnr-0.2.0.tar", last modified: Thu Apr  6 09:21:05 2023, max compression
+gzip compressed data, was "pyseobnr-0.2.1.tar", last modified: Thu Apr  6 13:22:12 2023, max compression
```

## Comparing `pyseobnr-0.2.0.tar` & `pyseobnr-0.2.1.tar`

### file list

```diff
@@ -1,152 +1,152 @@
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.619714 pyseobnr-0.2.0/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)       54 2023-03-31 13:47:50.000000 pyseobnr-0.2.0/.gitignore
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     1949 2023-04-03 16:03:36.000000 pyseobnr-0.2.0/.gitlab-ci.yml
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      452 2023-03-31 13:47:50.000000 pyseobnr-0.2.0/.pre-commit-config.yaml
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      319 2023-03-31 13:47:50.000000 pyseobnr-0.2.0/AUTHORS.md
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      309 2023-04-06 09:02:01.000000 pyseobnr-0.2.0/CHANGELOG.md
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     4458 2023-03-31 13:47:50.000000 pyseobnr-0.2.0/CONTRIBUTING.md
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    35147 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/LICENSE
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     5875 2023-04-06 09:21:05.000000 pyseobnr-0.2.0/PKG-INFO
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     5278 2023-04-06 09:00:37.000000 pyseobnr-0.2.0/README.rst
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.043703 pyseobnr-0.2.0/docs/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      580 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/docs/Makefile
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     2253 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/docs/conf.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      757 2023-04-06 09:00:37.000000 pyseobnr-0.2.0/docs/index.rst
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.055703 pyseobnr-0.2.0/docs/source/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     3694 2023-03-31 13:47:50.000000 pyseobnr-0.2.0/docs/source/basic_usage.rst
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     1767 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/docs/source/expert_mode.rst
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     1558 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/docs/source/installation.rst
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.063703 pyseobnr-0.2.0/docs/templates/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      639 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/docs/templates/custom-class-template.rst
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     1465 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/docs/templates/custom-module-template.rst
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     1588 2023-04-06 09:00:37.000000 pyseobnr-0.2.0/pyproject.toml
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.075703 pyseobnr-0.2.0/pyseobnr/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      238 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/__init__.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      160 2023-04-06 09:21:04.000000 pyseobnr-0.2.0/pyseobnr/_version.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.111704 pyseobnr-0.2.0/pyseobnr/auxiliary/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/__init__.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.123705 pyseobnr-0.2.0/pyseobnr/auxiliary/external_models/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      122 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/external_models/__init__.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     3727 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/external_models/default_settings.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    19281 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/external_models/external_models.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.131705 pyseobnr-0.2.0/pyseobnr/auxiliary/interpolate/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/interpolate/__init__.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      362 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/interpolate/vector_spline.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.139705 pyseobnr-0.2.0/pyseobnr/auxiliary/mode_mixing/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/mode_mixing/__init__.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    15933 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/mode_mixing/auxiliary_functions_modemixing.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.247707 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     8717 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/EOB_matches.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    16819 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/NRSur_IV_difference.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    10669 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/NRSur_matches.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    10093 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/NR_mismatches.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    13095 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      708 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM.sh
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    14920 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM_commentedMatch.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      710 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM_commentedMatch.sh
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     2070 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/amp_hierarchy_test_prec_submission.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     4831 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/amplitude_hierarchy_test.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     8559 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/amplitude_hierarchy_test_precessing.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     2804 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/attachment_smoothness_test.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     6378 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/battery_of_tests.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.263707 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/metrics/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)       48 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/metrics/__init__.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      389 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/metrics/default_settings.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     8405 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/metrics/metrics.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     9059 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/metrics/unfaithfulness_mode_by_mode.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    16633 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/mismatch_PA_polarization_precession.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      766 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/mismatch_PA_polarization_precession.sh
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     4114 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/mismatch_fixed_waveform_test.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    11573 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/mismatch_pert_polarization_aligned.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    15786 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/mismatch_pert_polarization_precession.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      737 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/mismatch_pert_polarization_precession.sh
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     7490 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/monotonicity_test.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     3720 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/parameters.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     8464 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/phenom_matches.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     3706 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/reference_smoothness_test.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     2322 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/single_waveform_tests.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     7088 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/smoothness_q_chi.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.271707 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/templates/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      546 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/templates/slurm.jinja
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    18240 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/v5P_NR_coprecessing_match.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.275708 pyseobnr-0.2.0/pyseobnr/eob/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)       51 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/__init__.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.387710 pyseobnr-0.2.0/pyseobnr/eob/dynamics/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/__init__.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     4538 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/initial_conditions_aligned_opt.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     6663 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/initial_conditions_aligned_precessing.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     4612 2023-03-30 17:57:27.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/initial_conditions_precessing_postadiabatic.py
--rwxr-xr-x   0 sossokine  (2188) cluster   (1111)     8881 2023-04-06 09:00:37.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/integrate_ode.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    22408 2023-04-06 09:00:37.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/integrate_ode_prec.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    30318 2023-03-30 20:01:42.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/pn_evolution_opt.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)  1501092 2023-04-06 09:20:52.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C.c
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      480 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C.pxd
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    20902 2023-04-06 09:00:37.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C.pyx
--rw-r--r--   0 sossokine  (2188) cluster   (1111)  1239419 2023-04-06 09:20:53.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C_fast.c
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    12302 2023-04-06 09:00:37.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C_fast.pyx
--rw-r--r--   0 sossokine  (2188) cluster   (1111)  1739532 2023-04-06 09:20:54.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C_prec.c
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    52384 2023-04-06 09:00:37.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C_prec.pyx
--rw-r--r--   0 sossokine  (2188) cluster   (1111)  1070464 2023-04-06 09:20:56.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/rhs_aligned.c
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     2655 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/rhs_aligned.pyx
--rw-r--r--   0 sossokine  (2188) cluster   (1111)  1014991 2023-04-06 09:20:57.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/rhs_precessing.c
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      360 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/rhs_precessing.pxd
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     2379 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/dynamics/rhs_precessing.pyx
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.000000 pyseobnr-0.2.0/pyseobnr/eob/fits/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     9588 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/fits/EOB_fits.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     1956 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/fits/GSF_fits.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    30704 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/fits/IV_fits.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    14275 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/fits/MR_fits.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      155 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/fits/__init__.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     5383 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/fits/fits_Hamiltonian.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)  2339148 2023-04-06 09:20:59.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Ham_AvgS2precess_simple_cython_PA_AD.c
--rw-r--r--   0 sossokine  (2188) cluster   (1111)   137434 2023-03-30 17:57:27.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Ham_AvgS2precess_simple_cython_PA_AD.pyx
--rw-r--r--   0 sossokine  (2188) cluster   (1111)  2217747 2023-04-06 09:21:01.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C.c
--rw-r--r--   0 sossokine  (2188) cluster   (1111)   119553 2023-03-30 17:57:27.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C.pyx
--rw-r--r--   0 sossokine  (2188) cluster   (1111)   939499 2023-03-31 14:00:27.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Hamiltonian_C.c
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      798 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Hamiltonian_C.pxd
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      914 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Hamiltonian_C.pyx
--rw-r--r--   0 sossokine  (2188) cluster   (1111)   989569 2023-03-31 14:00:28.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Hamiltonian_v5PHM_C.c
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     1253 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Hamiltonian_v5PHM_C.pxd
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     1342 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Hamiltonian_v5PHM_C.pyx
--rw-r--r--   0 sossokine  (2188) cluster   (1111)       55 2023-04-04 16:17:02.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/__init__.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     1235 2023-04-04 16:17:02.000000 pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/hamiltonian.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.000000 pyseobnr-0.2.0/pyseobnr/eob/utils/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/utils/__init__.pxd
--rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/utils/__init__.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)  1279061 2023-04-06 09:21:02.000000 pyseobnr-0.2.0/pyseobnr/eob/utils/containers.c
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     2286 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/utils/containers.pxd
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     4329 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/utils/containers.pyx
--rw-r--r--   0 sossokine  (2188) cluster   (1111)       37 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/utils/eob_parameters.h
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     1409 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/utils/math_ops_opt.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    23772 2023-04-04 16:17:02.000000 pyseobnr-0.2.0/pyseobnr/eob/utils/utils_precession_opt.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      784 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/utils/waveform_ops.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.000000 pyseobnr-0.2.0/pyseobnr/eob/waveform/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)       27 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/waveform/__init__.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     3680 2023-03-30 17:57:27.000000 pyseobnr-0.2.0/pyseobnr/eob/waveform/compute_MR.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    20048 2023-04-06 09:00:37.000000 pyseobnr-0.2.0/pyseobnr/eob/waveform/compute_hlms.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)  1585176 2023-04-06 09:20:55.000000 pyseobnr-0.2.0/pyseobnr/eob/waveform/waveform.c
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      624 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/eob/waveform/waveform.pxd
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    85029 2023-03-30 17:57:27.000000 pyseobnr-0.2.0/pyseobnr/eob/waveform/waveform.pyx
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    25863 2023-03-30 17:57:27.000000 pyseobnr-0.2.0/pyseobnr/generate_waveform.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.000000 pyseobnr-0.2.0/pyseobnr/models/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)    52496 2023-04-06 09:00:37.000000 pyseobnr-0.2.0/pyseobnr/models/SEOBNRv5HM.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/models/__init__.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      280 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/pyseobnr/models/model.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.000000 pyseobnr-0.2.0/pyseobnr.egg-info/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     5875 2023-04-06 09:21:04.000000 pyseobnr-0.2.0/pyseobnr.egg-info/PKG-INFO
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     5441 2023-04-06 09:21:04.000000 pyseobnr-0.2.0/pyseobnr.egg-info/SOURCES.txt
--rw-r--r--   0 sossokine  (2188) cluster   (1111)        1 2023-04-06 09:21:04.000000 pyseobnr-0.2.0/pyseobnr.egg-info/dependency_links.txt
--rw-r--r--   0 sossokine  (2188) cluster   (1111)        1 2023-03-31 14:00:31.000000 pyseobnr-0.2.0/pyseobnr.egg-info/not-zip-safe
--rw-r--r--   0 sossokine  (2188) cluster   (1111)      326 2023-04-06 09:21:04.000000 pyseobnr-0.2.0/pyseobnr.egg-info/requires.txt
--rw-r--r--   0 sossokine  (2188) cluster   (1111)        9 2023-04-06 09:21:04.000000 pyseobnr-0.2.0/pyseobnr.egg-info/top_level.txt
--rw-r--r--   0 sossokine  (2188) cluster   (1111)       38 2023-04-06 09:21:05.000000 pyseobnr-0.2.0/setup.cfg
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     2918 2023-04-05 21:14:32.000000 pyseobnr-0.2.0/setup.py
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:04.000000 pyseobnr-0.2.0/test/
-drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 09:21:05.000000 pyseobnr-0.2.0/test/regression_tests/
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     3386 2023-03-30 17:57:27.000000 pyseobnr-0.2.0/test/regression_tests/regenerate_SEOBNRv5HM.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     3413 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/test/regression_tests/regenerate_SEOBNRv5PHM.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     4458 2023-03-30 17:57:27.000000 pyseobnr-0.2.0/test/regression_tests/template_v5HM_tests.jinja
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     4494 2023-03-27 07:53:18.000000 pyseobnr-0.2.0/test/regression_tests/template_v5PHM_tests.jinja
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     4591 2023-03-30 17:57:27.000000 pyseobnr-0.2.0/test/regression_tests/test_SEOBNRv5HM.py
--rw-r--r--   0 sossokine  (2188) cluster   (1111)     4625 2023-03-30 17:57:27.000000 pyseobnr-0.2.0/test/regression_tests/test_SEOBNRv5PHM.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:12.313952 pyseobnr-0.2.1/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)       54 2023-03-31 13:47:50.000000 pyseobnr-0.2.1/.gitignore
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     1949 2023-04-03 16:03:36.000000 pyseobnr-0.2.1/.gitlab-ci.yml
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      452 2023-03-31 13:47:50.000000 pyseobnr-0.2.1/.pre-commit-config.yaml
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      319 2023-03-31 13:47:50.000000 pyseobnr-0.2.1/AUTHORS.md
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      309 2023-04-06 09:02:01.000000 pyseobnr-0.2.1/CHANGELOG.md
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     4458 2023-03-31 13:47:50.000000 pyseobnr-0.2.1/CONTRIBUTING.md
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    35147 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/LICENSE
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     5875 2023-04-06 13:22:12.000000 pyseobnr-0.2.1/PKG-INFO
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     5278 2023-04-06 09:00:37.000000 pyseobnr-0.2.1/README.rst
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.689939 pyseobnr-0.2.1/docs/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      580 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/docs/Makefile
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     2253 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/docs/conf.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      757 2023-04-06 09:00:37.000000 pyseobnr-0.2.1/docs/index.rst
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.701939 pyseobnr-0.2.1/docs/source/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     3694 2023-03-31 13:47:50.000000 pyseobnr-0.2.1/docs/source/basic_usage.rst
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     1767 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/docs/source/expert_mode.rst
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     1558 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/docs/source/installation.rst
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.713939 pyseobnr-0.2.1/docs/templates/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      639 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/docs/templates/custom-class-template.rst
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     1465 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/docs/templates/custom-module-template.rst
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     1588 2023-04-06 09:00:37.000000 pyseobnr-0.2.1/pyproject.toml
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.725939 pyseobnr-0.2.1/pyseobnr/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      238 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/__init__.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      160 2023-04-06 13:22:11.000000 pyseobnr-0.2.1/pyseobnr/_version.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.761940 pyseobnr-0.2.1/pyseobnr/auxiliary/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/__init__.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.773940 pyseobnr-0.2.1/pyseobnr/auxiliary/external_models/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      122 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/external_models/__init__.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     3727 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/external_models/default_settings.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    19281 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/external_models/external_models.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.781941 pyseobnr-0.2.1/pyseobnr/auxiliary/interpolate/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/interpolate/__init__.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      362 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/interpolate/vector_spline.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.789941 pyseobnr-0.2.1/pyseobnr/auxiliary/mode_mixing/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/mode_mixing/__init__.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    15933 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/mode_mixing/auxiliary_functions_modemixing.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.905943 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     8717 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/EOB_matches.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    16819 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/NRSur_IV_difference.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    10669 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/NRSur_matches.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    10093 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/NR_mismatches.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    13095 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      708 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM.sh
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    14920 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM_commentedMatch.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      710 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM_commentedMatch.sh
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     2070 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/amp_hierarchy_test_prec_submission.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     4831 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/amplitude_hierarchy_test.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     8559 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/amplitude_hierarchy_test_precessing.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     2804 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/attachment_smoothness_test.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     6378 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/battery_of_tests.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.925943 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/metrics/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)       48 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/metrics/__init__.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      389 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/metrics/default_settings.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     8405 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/metrics/metrics.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     9059 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/metrics/unfaithfulness_mode_by_mode.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    16633 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/mismatch_PA_polarization_precession.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      766 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/mismatch_PA_polarization_precession.sh
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     4114 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/mismatch_fixed_waveform_test.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    11573 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/mismatch_pert_polarization_aligned.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    15786 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/mismatch_pert_polarization_precession.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      737 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/mismatch_pert_polarization_precession.sh
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     7490 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/monotonicity_test.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     3720 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/parameters.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     8464 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/phenom_matches.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     3706 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/reference_smoothness_test.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     2322 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/single_waveform_tests.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     7088 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/smoothness_q_chi.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.929944 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/templates/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      546 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/templates/slurm.jinja
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    18240 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/v5P_NR_coprecessing_match.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.933944 pyseobnr-0.2.1/pyseobnr/eob/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)       51 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/__init__.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:12.061946 pyseobnr-0.2.1/pyseobnr/eob/dynamics/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/__init__.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     4538 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/initial_conditions_aligned_opt.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     6663 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/initial_conditions_aligned_precessing.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     4612 2023-03-30 17:57:27.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/initial_conditions_precessing_postadiabatic.py
+-rwxr-xr-x   0 sossokine  (2188) cluster   (1111)     8881 2023-04-06 09:00:37.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/integrate_ode.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    22408 2023-04-06 09:00:37.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/integrate_ode_prec.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    30318 2023-03-30 20:01:42.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/pn_evolution_opt.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)  1501092 2023-04-06 13:21:59.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C.c
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      480 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C.pxd
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    20902 2023-04-06 09:00:37.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C.pyx
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)  1239419 2023-04-06 13:22:00.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C_fast.c
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    12302 2023-04-06 09:00:37.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C_fast.pyx
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)  1739532 2023-04-06 13:22:01.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C_prec.c
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    52384 2023-04-06 09:00:37.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C_prec.pyx
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)  1070464 2023-04-06 13:22:03.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/rhs_aligned.c
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     2655 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/rhs_aligned.pyx
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)  1014991 2023-04-06 13:22:04.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/rhs_precessing.c
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      360 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/rhs_precessing.pxd
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     2379 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/dynamics/rhs_precessing.pyx
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:12.000000 pyseobnr-0.2.1/pyseobnr/eob/fits/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     9588 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/fits/EOB_fits.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     1956 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/fits/GSF_fits.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    30704 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/fits/IV_fits.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    14275 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/fits/MR_fits.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      155 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/fits/__init__.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     5383 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/fits/fits_Hamiltonian.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:12.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)  2339148 2023-04-06 13:22:06.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Ham_AvgS2precess_simple_cython_PA_AD.c
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)   137434 2023-03-30 17:57:27.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Ham_AvgS2precess_simple_cython_PA_AD.pyx
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)  2217747 2023-04-06 13:22:07.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C.c
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)   119553 2023-03-30 17:57:27.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C.pyx
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)   939499 2023-03-31 14:00:27.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Hamiltonian_C.c
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      798 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Hamiltonian_C.pxd
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      914 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Hamiltonian_C.pyx
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)   989569 2023-03-31 14:00:28.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Hamiltonian_v5PHM_C.c
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     1253 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Hamiltonian_v5PHM_C.pxd
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     1342 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Hamiltonian_v5PHM_C.pyx
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)       55 2023-04-04 16:17:02.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/__init__.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     1235 2023-04-04 16:17:02.000000 pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/hamiltonian.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:12.000000 pyseobnr-0.2.1/pyseobnr/eob/utils/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/utils/__init__.pxd
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/utils/__init__.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)  1279061 2023-04-06 13:22:08.000000 pyseobnr-0.2.1/pyseobnr/eob/utils/containers.c
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     2286 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/utils/containers.pxd
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     4329 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/utils/containers.pyx
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)       37 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/utils/eob_parameters.h
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     1409 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/utils/math_ops_opt.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    23772 2023-04-04 16:17:02.000000 pyseobnr-0.2.1/pyseobnr/eob/utils/utils_precession_opt.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      784 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/utils/waveform_ops.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:12.000000 pyseobnr-0.2.1/pyseobnr/eob/waveform/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)       27 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/waveform/__init__.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     3680 2023-03-30 17:57:27.000000 pyseobnr-0.2.1/pyseobnr/eob/waveform/compute_MR.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    20048 2023-04-06 09:00:37.000000 pyseobnr-0.2.1/pyseobnr/eob/waveform/compute_hlms.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)  1585176 2023-04-06 13:22:02.000000 pyseobnr-0.2.1/pyseobnr/eob/waveform/waveform.c
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      624 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/eob/waveform/waveform.pxd
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    85029 2023-03-30 17:57:27.000000 pyseobnr-0.2.1/pyseobnr/eob/waveform/waveform.pyx
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    25863 2023-03-30 17:57:27.000000 pyseobnr-0.2.1/pyseobnr/generate_waveform.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:12.000000 pyseobnr-0.2.1/pyseobnr/models/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)    52496 2023-04-06 09:00:37.000000 pyseobnr-0.2.1/pyseobnr/models/SEOBNRv5HM.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)        0 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/models/__init__.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      280 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/pyseobnr/models/model.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.000000 pyseobnr-0.2.1/pyseobnr.egg-info/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     5875 2023-04-06 13:22:11.000000 pyseobnr-0.2.1/pyseobnr.egg-info/PKG-INFO
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     5441 2023-04-06 13:22:11.000000 pyseobnr-0.2.1/pyseobnr.egg-info/SOURCES.txt
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)        1 2023-04-06 13:22:11.000000 pyseobnr-0.2.1/pyseobnr.egg-info/dependency_links.txt
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)        1 2023-03-31 14:00:31.000000 pyseobnr-0.2.1/pyseobnr.egg-info/not-zip-safe
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)      326 2023-04-06 13:22:11.000000 pyseobnr-0.2.1/pyseobnr.egg-info/requires.txt
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)        9 2023-04-06 13:22:11.000000 pyseobnr-0.2.1/pyseobnr.egg-info/top_level.txt
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)       38 2023-04-06 13:22:12.000000 pyseobnr-0.2.1/setup.cfg
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     2918 2023-04-05 21:14:32.000000 pyseobnr-0.2.1/setup.py
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:11.000000 pyseobnr-0.2.1/test/
+drwxr-xr-x   0 sossokine  (2188) cluster   (1111)        0 2023-04-06 13:22:12.000000 pyseobnr-0.2.1/test/regression_tests/
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     3386 2023-03-30 17:57:27.000000 pyseobnr-0.2.1/test/regression_tests/regenerate_SEOBNRv5HM.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     3413 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/test/regression_tests/regenerate_SEOBNRv5PHM.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     4458 2023-03-30 17:57:27.000000 pyseobnr-0.2.1/test/regression_tests/template_v5HM_tests.jinja
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     4494 2023-03-27 07:53:18.000000 pyseobnr-0.2.1/test/regression_tests/template_v5PHM_tests.jinja
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     4592 2023-04-06 13:05:51.000000 pyseobnr-0.2.1/test/regression_tests/test_SEOBNRv5HM.py
+-rw-r--r--   0 sossokine  (2188) cluster   (1111)     4628 2023-04-06 13:06:09.000000 pyseobnr-0.2.1/test/regression_tests/test_SEOBNRv5PHM.py
```

### Comparing `pyseobnr-0.2.0/.gitlab-ci.yml` & `pyseobnr-0.2.1/.gitlab-ci.yml`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/CONTRIBUTING.md` & `pyseobnr-0.2.1/CONTRIBUTING.md`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/LICENSE` & `pyseobnr-0.2.1/LICENSE`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/PKG-INFO` & `pyseobnr-0.2.1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyseobnr
-Version: 0.2.0
+Version: 0.2.1
 Summary: Gravitational wave modelling within the effective-one-body framework
 Author-email: Serguei Ossokine <serguei.ossokine@tutanota.com>, Lorenzo Pompili <lorenzo.pompili@ligo.org>, Deyan Mihaylov <deyan.mihaylov@ligo.org>, Antoni Ramos Buades <antoni.ramos-buades@ligo.org>, Michael Puerrer <michael.puerrer@ligo.org>, Hector Estelles <hector.estelles@ligo.org>
 License: GPL-3.0-or-later
 Requires-Python: >=3.8
 Description-Content-Type: text/x-rst
 Provides-Extra: checks
 Provides-Extra: docs
```

### Comparing `pyseobnr-0.2.0/README.rst` & `pyseobnr-0.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/docs/Makefile` & `pyseobnr-0.2.1/docs/Makefile`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/docs/conf.py` & `pyseobnr-0.2.1/docs/conf.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/docs/index.rst` & `pyseobnr-0.2.1/docs/index.rst`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/docs/source/basic_usage.rst` & `pyseobnr-0.2.1/docs/source/basic_usage.rst`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/docs/source/expert_mode.rst` & `pyseobnr-0.2.1/docs/source/expert_mode.rst`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/docs/source/installation.rst` & `pyseobnr-0.2.1/docs/source/installation.rst`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/docs/templates/custom-class-template.rst` & `pyseobnr-0.2.1/docs/templates/custom-class-template.rst`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/docs/templates/custom-module-template.rst` & `pyseobnr-0.2.1/docs/templates/custom-module-template.rst`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyproject.toml` & `pyseobnr-0.2.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/external_models/default_settings.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/external_models/default_settings.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/external_models/external_models.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/external_models/external_models.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/mode_mixing/auxiliary_functions_modemixing.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/mode_mixing/auxiliary_functions_modemixing.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/EOB_matches.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/EOB_matches.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/NRSur_IV_difference.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/NRSur_IV_difference.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/NRSur_matches.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/NRSur_matches.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/NR_mismatches.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/NR_mismatches.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM.sh` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM.sh`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM_commentedMatch.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM_commentedMatch.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM_commentedMatch.sh` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/aligned_matches_v5PHM_commentedMatch.sh`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/amp_hierarchy_test_prec_submission.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/amp_hierarchy_test_prec_submission.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/amplitude_hierarchy_test.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/amplitude_hierarchy_test.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/amplitude_hierarchy_test_precessing.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/amplitude_hierarchy_test_precessing.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/attachment_smoothness_test.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/attachment_smoothness_test.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/battery_of_tests.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/battery_of_tests.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/metrics/metrics.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/metrics/metrics.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/metrics/unfaithfulness_mode_by_mode.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/metrics/unfaithfulness_mode_by_mode.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/mismatch_PA_polarization_precession.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/mismatch_PA_polarization_precession.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/mismatch_PA_polarization_precession.sh` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/mismatch_PA_polarization_precession.sh`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/mismatch_fixed_waveform_test.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/mismatch_fixed_waveform_test.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/mismatch_pert_polarization_aligned.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/mismatch_pert_polarization_aligned.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/mismatch_pert_polarization_precession.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/mismatch_pert_polarization_precession.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/mismatch_pert_polarization_precession.sh` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/mismatch_pert_polarization_precession.sh`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/monotonicity_test.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/monotonicity_test.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/parameters.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/parameters.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/phenom_matches.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/phenom_matches.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/reference_smoothness_test.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/reference_smoothness_test.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/single_waveform_tests.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/single_waveform_tests.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/smoothness_q_chi.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/smoothness_q_chi.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/templates/slurm.jinja` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/templates/slurm.jinja`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/auxiliary/sanity_checks/v5P_NR_coprecessing_match.py` & `pyseobnr-0.2.1/pyseobnr/auxiliary/sanity_checks/v5P_NR_coprecessing_match.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/initial_conditions_aligned_opt.py` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/initial_conditions_aligned_opt.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/initial_conditions_aligned_precessing.py` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/initial_conditions_aligned_precessing.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/initial_conditions_precessing_postadiabatic.py` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/initial_conditions_precessing_postadiabatic.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/integrate_ode.py` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/integrate_ode.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/integrate_ode_prec.py` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/integrate_ode_prec.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/pn_evolution_opt.py` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/pn_evolution_opt.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C.c` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C.c`

 * *Files 0% similar despite different names*

```diff
@@ -8,15 +8,15 @@
         ],
         "extra_compile_args": [
             "-O3"
         ],
         "include_dirs": [
             "pyseobnr/eob/utils",
             "./pyseobnr/eob/utils",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include",
             "pyseobnr/eob/hamiltonian"
         ],
         "name": "pyseobnr.eob.dynamics.postadiabatic_C",
         "sources": [
             "pyseobnr/eob/dynamics/postadiabatic_C.pyx"
         ]
     },
```

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C.pyx` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C.pyx`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C_fast.c` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C_fast.c`

 * *Files 0% similar despite different names*

```diff
@@ -8,15 +8,15 @@
         ],
         "extra_compile_args": [
             "-O3"
         ],
         "include_dirs": [
             "pyseobnr/eob/utils",
             "./pyseobnr/eob/utils",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include",
             "pyseobnr/eob/hamiltonian"
         ],
         "name": "pyseobnr.eob.dynamics.postadiabatic_C_fast",
         "sources": [
             "pyseobnr/eob/dynamics/postadiabatic_C_fast.pyx"
         ]
     },
```

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C_fast.pyx` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C_fast.pyx`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C_prec.c` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C_prec.c`

 * *Files 0% similar despite different names*

```diff
@@ -8,15 +8,15 @@
         ],
         "extra_compile_args": [
             "-O3"
         ],
         "include_dirs": [
             "pyseobnr/eob/utils",
             "./pyseobnr/eob/utils",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include",
             "pyseobnr/eob/hamiltonian"
         ],
         "name": "pyseobnr.eob.dynamics.postadiabatic_C_prec",
         "sources": [
             "pyseobnr/eob/dynamics/postadiabatic_C_prec.pyx"
         ]
     },
```

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/postadiabatic_C_prec.pyx` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/postadiabatic_C_prec.pyx`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/rhs_aligned.c` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/rhs_aligned.c`

 * *Files 1% similar despite different names*

```diff
@@ -6,28 +6,28 @@
         "define_macros": [
             [
                 "CYTHON_TRACE",
                 "1"
             ]
         ],
         "depends": [
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h",
             "pyseobnr/eob/utils/eob_parameters.h"
         ],
         "extra_compile_args": [
             "-O3"
         ],
         "include_dirs": [
             "pyseobnr/eob/utils",
             "./pyseobnr/eob/utils",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include"
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include"
         ],
         "name": "pyseobnr.eob.dynamics.rhs_aligned",
         "sources": [
             "pyseobnr/eob/dynamics/rhs_aligned.pyx"
         ]
     },
     "module_name": "pyseobnr.eob.dynamics.rhs_aligned"
@@ -1129,195 +1129,195 @@
   char enc_type;
   char new_packmode;
   char enc_packmode;
   char is_valid_array;
 } __Pyx_BufFmt_Context;
 
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":689
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":689
  * # in Cython to enable them only on the right systems.
  * 
  * ctypedef npy_int8       int8_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t
  */
 typedef npy_int8 __pyx_t_5numpy_int8_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":690
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":690
  * 
  * ctypedef npy_int8       int8_t
  * ctypedef npy_int16      int16_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int32      int32_t
  * ctypedef npy_int64      int64_t
  */
 typedef npy_int16 __pyx_t_5numpy_int16_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":691
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":691
  * ctypedef npy_int8       int8_t
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int64      int64_t
  * #ctypedef npy_int96      int96_t
  */
 typedef npy_int32 __pyx_t_5numpy_int32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":692
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":692
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t
  * ctypedef npy_int64      int64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_int96      int96_t
  * #ctypedef npy_int128     int128_t
  */
 typedef npy_int64 __pyx_t_5numpy_int64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":696
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":696
  * #ctypedef npy_int128     int128_t
  * 
  * ctypedef npy_uint8      uint8_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t
  */
 typedef npy_uint8 __pyx_t_5numpy_uint8_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":697
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":697
  * 
  * ctypedef npy_uint8      uint8_t
  * ctypedef npy_uint16     uint16_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint32     uint32_t
  * ctypedef npy_uint64     uint64_t
  */
 typedef npy_uint16 __pyx_t_5numpy_uint16_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":698
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":698
  * ctypedef npy_uint8      uint8_t
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint64     uint64_t
  * #ctypedef npy_uint96     uint96_t
  */
 typedef npy_uint32 __pyx_t_5numpy_uint32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":699
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":699
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t
  * ctypedef npy_uint64     uint64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_uint96     uint96_t
  * #ctypedef npy_uint128    uint128_t
  */
 typedef npy_uint64 __pyx_t_5numpy_uint64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":703
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":703
  * #ctypedef npy_uint128    uint128_t
  * 
  * ctypedef npy_float32    float32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_float64    float64_t
  * #ctypedef npy_float80    float80_t
  */
 typedef npy_float32 __pyx_t_5numpy_float32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":704
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":704
  * 
  * ctypedef npy_float32    float32_t
  * ctypedef npy_float64    float64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_float80    float80_t
  * #ctypedef npy_float128   float128_t
  */
 typedef npy_float64 __pyx_t_5numpy_float64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":713
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":713
  * # The int types are mapped a bit surprising --
  * # numpy.int corresponds to 'l' and numpy.long to 'q'
  * ctypedef npy_long       int_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longlong   long_t
  * ctypedef npy_longlong   longlong_t
  */
 typedef npy_long __pyx_t_5numpy_int_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":714
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":714
  * # numpy.int corresponds to 'l' and numpy.long to 'q'
  * ctypedef npy_long       int_t
  * ctypedef npy_longlong   long_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longlong   longlong_t
  * 
  */
 typedef npy_longlong __pyx_t_5numpy_long_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":715
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":715
  * ctypedef npy_long       int_t
  * ctypedef npy_longlong   long_t
  * ctypedef npy_longlong   longlong_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_ulong      uint_t
  */
 typedef npy_longlong __pyx_t_5numpy_longlong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":717
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":717
  * ctypedef npy_longlong   longlong_t
  * 
  * ctypedef npy_ulong      uint_t             # <<<<<<<<<<<<<<
  * ctypedef npy_ulonglong  ulong_t
  * ctypedef npy_ulonglong  ulonglong_t
  */
 typedef npy_ulong __pyx_t_5numpy_uint_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":718
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":718
  * 
  * ctypedef npy_ulong      uint_t
  * ctypedef npy_ulonglong  ulong_t             # <<<<<<<<<<<<<<
  * ctypedef npy_ulonglong  ulonglong_t
  * 
  */
 typedef npy_ulonglong __pyx_t_5numpy_ulong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":719
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":719
  * ctypedef npy_ulong      uint_t
  * ctypedef npy_ulonglong  ulong_t
  * ctypedef npy_ulonglong  ulonglong_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_intp       intp_t
  */
 typedef npy_ulonglong __pyx_t_5numpy_ulonglong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":721
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":721
  * ctypedef npy_ulonglong  ulonglong_t
  * 
  * ctypedef npy_intp       intp_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uintp      uintp_t
  * 
  */
 typedef npy_intp __pyx_t_5numpy_intp_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":722
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":722
  * 
  * ctypedef npy_intp       intp_t
  * ctypedef npy_uintp      uintp_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_double     float_t
  */
 typedef npy_uintp __pyx_t_5numpy_uintp_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":724
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":724
  * ctypedef npy_uintp      uintp_t
  * 
  * ctypedef npy_double     float_t             # <<<<<<<<<<<<<<
  * ctypedef npy_double     double_t
  * ctypedef npy_longdouble longdouble_t
  */
 typedef npy_double __pyx_t_5numpy_float_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":725
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":725
  * 
  * ctypedef npy_double     float_t
  * ctypedef npy_double     double_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longdouble longdouble_t
  * 
  */
 typedef npy_double __pyx_t_5numpy_double_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":726
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":726
  * ctypedef npy_double     float_t
  * ctypedef npy_double     double_t
  * ctypedef npy_longdouble longdouble_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_cfloat      cfloat_t
  */
 typedef npy_longdouble __pyx_t_5numpy_longdouble_t;
@@ -1370,42 +1370,42 @@
  *     cpdef (double,double) RR(self, double[::1] q,double[::1] p,double omega,double omega_circ,double H,EOBParams eob_par)
  */
 struct __pyx_ctuple_double__and_double {
   double f0;
   double f1;
 };
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":728
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":728
  * ctypedef npy_longdouble longdouble_t
  * 
  * ctypedef npy_cfloat      cfloat_t             # <<<<<<<<<<<<<<
  * ctypedef npy_cdouble     cdouble_t
  * ctypedef npy_clongdouble clongdouble_t
  */
 typedef npy_cfloat __pyx_t_5numpy_cfloat_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":729
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":729
  * 
  * ctypedef npy_cfloat      cfloat_t
  * ctypedef npy_cdouble     cdouble_t             # <<<<<<<<<<<<<<
  * ctypedef npy_clongdouble clongdouble_t
  * 
  */
 typedef npy_cdouble __pyx_t_5numpy_cdouble_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":730
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":730
  * ctypedef npy_cfloat      cfloat_t
  * ctypedef npy_cdouble     cdouble_t
  * ctypedef npy_clongdouble clongdouble_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_cdouble     complex_t
  */
 typedef npy_clongdouble __pyx_t_5numpy_clongdouble_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":732
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":732
  * ctypedef npy_clongdouble clongdouble_t
  * 
  * ctypedef npy_cdouble     complex_t             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew1(a):
  */
 typedef npy_cdouble __pyx_t_5numpy_complex_t;
@@ -4185,15 +4185,15 @@
   __PYX_XDEC_MEMVIEW(&__pyx_v_dynamics, 1);
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
 
@@ -4204,30 +4204,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew1", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew1", __pyx_f[1], 734, 0, __PYX_ERR(1, 734, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":735
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":735
  * 
  * cdef inline object PyArray_MultiIterNew1(a):
  *     return PyArray_MultiIterNew(1, <void*>a)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):
  */
   __Pyx_TraceLine(735,0,__PYX_ERR(1, 735, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(1, ((void *)__pyx_v_a)); if (unlikely(!__pyx_t_1)) __PYX_ERR(1, 735, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
 
@@ -4239,15 +4239,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
 
@@ -4258,30 +4258,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew2", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew2", __pyx_f[1], 737, 0, __PYX_ERR(1, 737, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":738
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":738
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):
  */
   __Pyx_TraceLine(738,0,__PYX_ERR(1, 738, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(2, ((void *)__pyx_v_a), ((void *)__pyx_v_b)); if (unlikely(!__pyx_t_1)) __PYX_ERR(1, 738, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
 
@@ -4293,15 +4293,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
 
@@ -4312,30 +4312,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew3", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew3", __pyx_f[1], 740, 0, __PYX_ERR(1, 740, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":741
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":741
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
  */
   __Pyx_TraceLine(741,0,__PYX_ERR(1, 741, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(3, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c)); if (unlikely(!__pyx_t_1)) __PYX_ERR(1, 741, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
 
@@ -4347,15 +4347,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
 
@@ -4366,30 +4366,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew4", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew4", __pyx_f[1], 743, 0, __PYX_ERR(1, 743, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":744
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":744
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
  */
   __Pyx_TraceLine(744,0,__PYX_ERR(1, 744, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(4, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d)); if (unlikely(!__pyx_t_1)) __PYX_ERR(1, 744, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
 
@@ -4401,15 +4401,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
 
@@ -4420,30 +4420,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew5", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew5", __pyx_f[1], 746, 0, __PYX_ERR(1, 746, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":747
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":747
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)             # <<<<<<<<<<<<<<
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  */
   __Pyx_TraceLine(747,0,__PYX_ERR(1, 747, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(5, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d), ((void *)__pyx_v_e)); if (unlikely(!__pyx_t_1)) __PYX_ERR(1, 747, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
 
@@ -4455,15 +4455,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
 
@@ -4474,63 +4474,63 @@
   int __pyx_t_1;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyDataType_SHAPE", 0);
   __Pyx_TraceCall("PyDataType_SHAPE", __pyx_f[1], 749, 0, __PYX_ERR(1, 749, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":750
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":750
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
  *         return <tuple>d.subarray.shape
  *     else:
  */
   __Pyx_TraceLine(750,0,__PYX_ERR(1, 750, __pyx_L1_error))
   __pyx_t_1 = (PyDataType_HASSUBARRAY(__pyx_v_d) != 0);
   if (__pyx_t_1) {
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":751
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":751
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape             # <<<<<<<<<<<<<<
  *     else:
  *         return ()
  */
     __Pyx_TraceLine(751,0,__PYX_ERR(1, 751, __pyx_L1_error))
     __Pyx_XDECREF(__pyx_r);
     __Pyx_INCREF(((PyObject*)__pyx_v_d->subarray->shape));
     __pyx_r = ((PyObject*)__pyx_v_d->subarray->shape);
     goto __pyx_L0;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":750
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":750
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
  *         return <tuple>d.subarray.shape
  *     else:
  */
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":753
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":753
  *         return <tuple>d.subarray.shape
  *     else:
  *         return ()             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(753,0,__PYX_ERR(1, 753, __pyx_L1_error))
   /*else*/ {
     __Pyx_XDECREF(__pyx_r);
     __Pyx_INCREF(__pyx_empty_tuple);
     __pyx_r = __pyx_empty_tuple;
     goto __pyx_L0;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
 
@@ -4541,15 +4541,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
 
@@ -4558,35 +4558,35 @@
   __Pyx_RefNannyDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("set_array_base", 0);
   __Pyx_TraceCall("set_array_base", __pyx_f[1], 928, 0, __PYX_ERR(1, 928, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":929
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":929
  * 
  * cdef inline void set_array_base(ndarray arr, object base):
  *     Py_INCREF(base) # important to do this before stealing the reference below!             # <<<<<<<<<<<<<<
  *     PyArray_SetBaseObject(arr, base)
  * 
  */
   __Pyx_TraceLine(929,0,__PYX_ERR(1, 929, __pyx_L1_error))
   Py_INCREF(__pyx_v_base);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":930
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":930
  * cdef inline void set_array_base(ndarray arr, object base):
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object get_array_base(ndarray arr):
  */
   __Pyx_TraceLine(930,0,__PYX_ERR(1, 930, __pyx_L1_error))
   (void)(PyArray_SetBaseObject(__pyx_v_arr, __pyx_v_base));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
 
@@ -4595,15 +4595,15 @@
   __pyx_L1_error:;
   __Pyx_WriteUnraisable("numpy.set_array_base", __pyx_clineno, __pyx_lineno, __pyx_filename, 1, 0);
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
 
@@ -4615,70 +4615,70 @@
   int __pyx_t_1;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("get_array_base", 0);
   __Pyx_TraceCall("get_array_base", __pyx_f[1], 932, 0, __PYX_ERR(1, 932, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":933
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":933
  * 
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)             # <<<<<<<<<<<<<<
  *     if base is NULL:
  *         return None
  */
   __Pyx_TraceLine(933,0,__PYX_ERR(1, 933, __pyx_L1_error))
   __pyx_v_base = PyArray_BASE(__pyx_v_arr);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":934
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":934
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)
  *     if base is NULL:             # <<<<<<<<<<<<<<
  *         return None
  *     return <object>base
  */
   __Pyx_TraceLine(934,0,__PYX_ERR(1, 934, __pyx_L1_error))
   __pyx_t_1 = ((__pyx_v_base == NULL) != 0);
   if (__pyx_t_1) {
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":935
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":935
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  *         return None             # <<<<<<<<<<<<<<
  *     return <object>base
  * 
  */
     __Pyx_TraceLine(935,0,__PYX_ERR(1, 935, __pyx_L1_error))
     __Pyx_XDECREF(__pyx_r);
     __pyx_r = Py_None; __Pyx_INCREF(Py_None);
     goto __pyx_L0;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":934
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":934
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)
  *     if base is NULL:             # <<<<<<<<<<<<<<
  *         return None
  *     return <object>base
  */
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":936
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":936
  *     if base is NULL:
  *         return None
  *     return <object>base             # <<<<<<<<<<<<<<
  * 
  * # Versions of the import_* functions which are more suitable for
  */
   __Pyx_TraceLine(936,0,__PYX_ERR(1, 936, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __Pyx_INCREF(((PyObject *)__pyx_v_base));
   __pyx_r = ((PyObject *)__pyx_v_base);
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
 
@@ -4689,15 +4689,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
 
@@ -4715,15 +4715,15 @@
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_array", 0);
   __Pyx_TraceCall("import_array", __pyx_f[1], 940, 0, __PYX_ERR(1, 940, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
   __Pyx_TraceLine(941,0,__PYX_ERR(1, 941, __pyx_L1_error))
@@ -4732,39 +4732,39 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":942
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":942
  * cdef inline int import_array() except -1:
  *     try:
  *         __pyx_import_array()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")
  */
       __Pyx_TraceLine(942,0,__PYX_ERR(1, 942, __pyx_L3_error))
       __pyx_t_4 = _import_array(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(1, 942, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":943
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":943
  *     try:
  *         __pyx_import_array()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  */
     __Pyx_TraceLine(943,0,__PYX_ERR(1, 943, __pyx_L5_except_error))
@@ -4772,15 +4772,15 @@
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_array", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(1, 943, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":944
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":944
  *         __pyx_import_array()
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_umath() except -1:
  */
       __Pyx_TraceLine(944,0,__PYX_ERR(1, 944, __pyx_L5_except_error))
@@ -4789,30 +4789,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(1, 944, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
 
@@ -4828,15 +4828,15 @@
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -4854,15 +4854,15 @@
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_umath", 0);
   __Pyx_TraceCall("import_umath", __pyx_f[1], 946, 0, __PYX_ERR(1, 946, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
   __Pyx_TraceLine(947,0,__PYX_ERR(1, 947, __pyx_L1_error))
@@ -4871,39 +4871,39 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":948
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":948
  * cdef inline int import_umath() except -1:
  *     try:
  *         _import_umath()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")
  */
       __Pyx_TraceLine(948,0,__PYX_ERR(1, 948, __pyx_L3_error))
       __pyx_t_4 = _import_umath(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(1, 948, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":949
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":949
  *     try:
  *         _import_umath()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  */
     __Pyx_TraceLine(949,0,__PYX_ERR(1, 949, __pyx_L5_except_error))
@@ -4911,15 +4911,15 @@
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_umath", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(1, 949, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":950
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":950
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_ufunc() except -1:
  */
       __Pyx_TraceLine(950,0,__PYX_ERR(1, 950, __pyx_L5_except_error))
@@ -4928,30 +4928,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(1, 950, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -4967,15 +4967,15 @@
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -4993,15 +4993,15 @@
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_ufunc", 0);
   __Pyx_TraceCall("import_ufunc", __pyx_f[1], 952, 0, __PYX_ERR(1, 952, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
   __Pyx_TraceLine(953,0,__PYX_ERR(1, 953, __pyx_L1_error))
@@ -5010,39 +5010,39 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":954
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":954
  * cdef inline int import_ufunc() except -1:
  *     try:
  *         _import_umath()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")
  */
       __Pyx_TraceLine(954,0,__PYX_ERR(1, 954, __pyx_L3_error))
       __pyx_t_4 = _import_umath(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(1, 954, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":955
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":955
  *     try:
  *         _import_umath()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  */
     __Pyx_TraceLine(955,0,__PYX_ERR(1, 955, __pyx_L5_except_error))
@@ -5050,15 +5050,15 @@
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_ufunc", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(1, 955, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":956
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":956
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef extern from *:
  */
       __Pyx_TraceLine(956,0,__PYX_ERR(1, 956, __pyx_L5_except_error))
@@ -5067,30 +5067,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(1, 956, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -5106,15 +5106,15 @@
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
 
@@ -5124,26 +5124,26 @@
   __Pyx_RefNannyDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("is_timedelta64_object", 0);
   __Pyx_TraceCall("is_timedelta64_object", __pyx_f[1], 966, 0, __PYX_ERR(1, 966, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":978
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":978
  *     bool
  *     """
  *     return PyObject_TypeCheck(obj, &PyTimedeltaArrType_Type)             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(978,0,__PYX_ERR(1, 978, __pyx_L1_error))
   __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyTimedeltaArrType_Type));
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
 
@@ -5153,15 +5153,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
 
@@ -5171,26 +5171,26 @@
   __Pyx_RefNannyDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("is_datetime64_object", 0);
   __Pyx_TraceCall("is_datetime64_object", __pyx_f[1], 981, 0, __PYX_ERR(1, 981, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":993
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":993
  *     bool
  *     """
  *     return PyObject_TypeCheck(obj, &PyDatetimeArrType_Type)             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(993,0,__PYX_ERR(1, 993, __pyx_L1_error))
   __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyDatetimeArrType_Type));
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
 
@@ -5200,15 +5200,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
 
@@ -5216,26 +5216,26 @@
   npy_datetime __pyx_r;
   __Pyx_TraceDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_TraceCall("get_datetime64_value", __pyx_f[1], 996, 1, __PYX_ERR(1, 996, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1003
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1003
  *     also needed.  That can be found using `get_datetime64_unit`.
  *     """
  *     return (<PyDatetimeScalarObject*>obj).obval             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(1003,1,__PYX_ERR(1, 1003, __pyx_L1_error))
   __pyx_r = ((PyDatetimeScalarObject *)__pyx_v_obj)->obval;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
 
@@ -5244,15 +5244,15 @@
   __Pyx_WriteUnraisable("numpy.get_datetime64_value", __pyx_clineno, __pyx_lineno, __pyx_filename, 1, 1);
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 1);
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
 
@@ -5260,26 +5260,26 @@
   npy_timedelta __pyx_r;
   __Pyx_TraceDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_TraceCall("get_timedelta64_value", __pyx_f[1], 1006, 1, __PYX_ERR(1, 1006, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1010
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1010
  *     returns the int64 value underlying scalar numpy timedelta64 object
  *     """
  *     return (<PyTimedeltaScalarObject*>obj).obval             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(1010,1,__PYX_ERR(1, 1010, __pyx_L1_error))
   __pyx_r = ((PyTimedeltaScalarObject *)__pyx_v_obj)->obval;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
 
@@ -5288,15 +5288,15 @@
   __Pyx_WriteUnraisable("numpy.get_timedelta64_value", __pyx_clineno, __pyx_lineno, __pyx_filename, 1, 1);
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 1);
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
 
@@ -5304,24 +5304,24 @@
   NPY_DATETIMEUNIT __pyx_r;
   __Pyx_TraceDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_TraceCall("get_datetime64_unit", __pyx_f[1], 1013, 1, __PYX_ERR(1, 1013, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1017
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1017
  *     returns the unit part of the dtype for a numpy datetime64 object.
  *     """
  *     return <NPY_DATETIMEUNIT>(<PyDatetimeScalarObject*>obj).obmeta.base             # <<<<<<<<<<<<<<
  */
   __Pyx_TraceLine(1017,1,__PYX_ERR(1, 1017, __pyx_L1_error))
   __pyx_r = ((NPY_DATETIMEUNIT)((PyDatetimeScalarObject *)__pyx_v_obj)->obmeta.base);
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
 
@@ -20878,26 +20878,26 @@
   return -1;
 }
 
 static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
   __Pyx_RefNannyDeclarations
   __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":944
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":944
  *         __pyx_import_array()
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_umath() except -1:
  */
   __pyx_tuple__3 = PyTuple_Pack(1, __pyx_kp_u_numpy_core_multiarray_failed_to); if (unlikely(!__pyx_tuple__3)) __PYX_ERR(1, 944, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_tuple__3);
   __Pyx_GIVEREF(__pyx_tuple__3);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":950
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":950
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_ufunc() except -1:
  */
   __pyx_tuple__4 = PyTuple_Pack(1, __pyx_kp_u_numpy_core_umath_failed_to_impor); if (unlikely(!__pyx_tuple__4)) __PYX_ERR(1, 950, __pyx_L1_error)
@@ -21701,165 +21701,165 @@
  */
   __Pyx_TraceLine(1,0,__PYX_ERR(0, 1, __pyx_L1_error))
   __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 1, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_1) < 0) __PYX_ERR(0, 1, __pyx_L1_error)
   __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
   __Pyx_TraceLine(734,0,__PYX_ERR(1, 734, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
   __Pyx_TraceLine(737,0,__PYX_ERR(1, 737, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
   __Pyx_TraceLine(740,0,__PYX_ERR(1, 740, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
   __Pyx_TraceLine(743,0,__PYX_ERR(1, 743, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
   __Pyx_TraceLine(746,0,__PYX_ERR(1, 746, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
   __Pyx_TraceLine(749,0,__PYX_ERR(1, 749, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
   __Pyx_TraceLine(928,0,__PYX_ERR(1, 928, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
   __Pyx_TraceLine(932,0,__PYX_ERR(1, 932, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
   __Pyx_TraceLine(940,0,__PYX_ERR(1, 940, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
   __Pyx_TraceLine(946,0,__PYX_ERR(1, 946, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
   __Pyx_TraceLine(952,0,__PYX_ERR(1, 952, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
   __Pyx_TraceLine(966,0,__PYX_ERR(1, 966, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
   __Pyx_TraceLine(981,0,__PYX_ERR(1, 981, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
   __Pyx_TraceLine(996,0,__PYX_ERR(1, 996, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
   __Pyx_TraceLine(1006,0,__PYX_ERR(1, 1006, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
   __Pyx_TraceLine(1013,0,__PYX_ERR(1, 1013, __pyx_L1_error))
```

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/rhs_aligned.pyx` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/rhs_aligned.pyx`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/rhs_precessing.c` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/rhs_precessing.c`

 * *Files 2% similar despite different names*

```diff
@@ -1,28 +1,28 @@
 /* Generated by Cython 0.29.34 */
 
 /* BEGIN: Cython Metadata
 {
     "distutils": {
         "depends": [
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/npy_math.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/npy_math.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h",
             "pyseobnr/eob/utils/eob_parameters.h"
         ],
         "extra_compile_args": [
             "-O3"
         ],
         "include_dirs": [
             "pyseobnr/eob/utils",
             "./pyseobnr/eob/utils",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include"
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include"
         ],
         "name": "pyseobnr.eob.dynamics.rhs_precessing",
         "sources": [
             "pyseobnr/eob/dynamics/rhs_precessing.pyx"
         ]
     },
     "module_name": "pyseobnr.eob.dynamics.rhs_precessing"
@@ -1125,195 +1125,195 @@
   char enc_type;
   char new_packmode;
   char enc_packmode;
   char is_valid_array;
 } __Pyx_BufFmt_Context;
 
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":689
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":689
  * # in Cython to enable them only on the right systems.
  * 
  * ctypedef npy_int8       int8_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t
  */
 typedef npy_int8 __pyx_t_5numpy_int8_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":690
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":690
  * 
  * ctypedef npy_int8       int8_t
  * ctypedef npy_int16      int16_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int32      int32_t
  * ctypedef npy_int64      int64_t
  */
 typedef npy_int16 __pyx_t_5numpy_int16_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":691
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":691
  * ctypedef npy_int8       int8_t
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int64      int64_t
  * #ctypedef npy_int96      int96_t
  */
 typedef npy_int32 __pyx_t_5numpy_int32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":692
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":692
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t
  * ctypedef npy_int64      int64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_int96      int96_t
  * #ctypedef npy_int128     int128_t
  */
 typedef npy_int64 __pyx_t_5numpy_int64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":696
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":696
  * #ctypedef npy_int128     int128_t
  * 
  * ctypedef npy_uint8      uint8_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t
  */
 typedef npy_uint8 __pyx_t_5numpy_uint8_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":697
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":697
  * 
  * ctypedef npy_uint8      uint8_t
  * ctypedef npy_uint16     uint16_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint32     uint32_t
  * ctypedef npy_uint64     uint64_t
  */
 typedef npy_uint16 __pyx_t_5numpy_uint16_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":698
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":698
  * ctypedef npy_uint8      uint8_t
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint64     uint64_t
  * #ctypedef npy_uint96     uint96_t
  */
 typedef npy_uint32 __pyx_t_5numpy_uint32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":699
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":699
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t
  * ctypedef npy_uint64     uint64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_uint96     uint96_t
  * #ctypedef npy_uint128    uint128_t
  */
 typedef npy_uint64 __pyx_t_5numpy_uint64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":703
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":703
  * #ctypedef npy_uint128    uint128_t
  * 
  * ctypedef npy_float32    float32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_float64    float64_t
  * #ctypedef npy_float80    float80_t
  */
 typedef npy_float32 __pyx_t_5numpy_float32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":704
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":704
  * 
  * ctypedef npy_float32    float32_t
  * ctypedef npy_float64    float64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_float80    float80_t
  * #ctypedef npy_float128   float128_t
  */
 typedef npy_float64 __pyx_t_5numpy_float64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":713
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":713
  * # The int types are mapped a bit surprising --
  * # numpy.int corresponds to 'l' and numpy.long to 'q'
  * ctypedef npy_long       int_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longlong   long_t
  * ctypedef npy_longlong   longlong_t
  */
 typedef npy_long __pyx_t_5numpy_int_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":714
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":714
  * # numpy.int corresponds to 'l' and numpy.long to 'q'
  * ctypedef npy_long       int_t
  * ctypedef npy_longlong   long_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longlong   longlong_t
  * 
  */
 typedef npy_longlong __pyx_t_5numpy_long_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":715
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":715
  * ctypedef npy_long       int_t
  * ctypedef npy_longlong   long_t
  * ctypedef npy_longlong   longlong_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_ulong      uint_t
  */
 typedef npy_longlong __pyx_t_5numpy_longlong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":717
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":717
  * ctypedef npy_longlong   longlong_t
  * 
  * ctypedef npy_ulong      uint_t             # <<<<<<<<<<<<<<
  * ctypedef npy_ulonglong  ulong_t
  * ctypedef npy_ulonglong  ulonglong_t
  */
 typedef npy_ulong __pyx_t_5numpy_uint_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":718
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":718
  * 
  * ctypedef npy_ulong      uint_t
  * ctypedef npy_ulonglong  ulong_t             # <<<<<<<<<<<<<<
  * ctypedef npy_ulonglong  ulonglong_t
  * 
  */
 typedef npy_ulonglong __pyx_t_5numpy_ulong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":719
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":719
  * ctypedef npy_ulong      uint_t
  * ctypedef npy_ulonglong  ulong_t
  * ctypedef npy_ulonglong  ulonglong_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_intp       intp_t
  */
 typedef npy_ulonglong __pyx_t_5numpy_ulonglong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":721
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":721
  * ctypedef npy_ulonglong  ulonglong_t
  * 
  * ctypedef npy_intp       intp_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uintp      uintp_t
  * 
  */
 typedef npy_intp __pyx_t_5numpy_intp_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":722
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":722
  * 
  * ctypedef npy_intp       intp_t
  * ctypedef npy_uintp      uintp_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_double     float_t
  */
 typedef npy_uintp __pyx_t_5numpy_uintp_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":724
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":724
  * ctypedef npy_uintp      uintp_t
  * 
  * ctypedef npy_double     float_t             # <<<<<<<<<<<<<<
  * ctypedef npy_double     double_t
  * ctypedef npy_longdouble longdouble_t
  */
 typedef npy_double __pyx_t_5numpy_float_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":725
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":725
  * 
  * ctypedef npy_double     float_t
  * ctypedef npy_double     double_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longdouble longdouble_t
  * 
  */
 typedef npy_double __pyx_t_5numpy_double_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":726
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":726
  * ctypedef npy_double     float_t
  * ctypedef npy_double     double_t
  * ctypedef npy_longdouble longdouble_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_cfloat      cfloat_t
  */
 typedef npy_longdouble __pyx_t_5numpy_longdouble_t;
@@ -1375,42 +1375,42 @@
  *     cpdef (double,double) RR(self, double[::1] q,double[::1] p,double omega,double omega_circ,double H,EOBParams eob_par)
  */
 struct __pyx_ctuple_double__and_double {
   double f0;
   double f1;
 };
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":728
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":728
  * ctypedef npy_longdouble longdouble_t
  * 
  * ctypedef npy_cfloat      cfloat_t             # <<<<<<<<<<<<<<
  * ctypedef npy_cdouble     cdouble_t
  * ctypedef npy_clongdouble clongdouble_t
  */
 typedef npy_cfloat __pyx_t_5numpy_cfloat_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":729
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":729
  * 
  * ctypedef npy_cfloat      cfloat_t
  * ctypedef npy_cdouble     cdouble_t             # <<<<<<<<<<<<<<
  * ctypedef npy_clongdouble clongdouble_t
  * 
  */
 typedef npy_cdouble __pyx_t_5numpy_cdouble_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":730
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":730
  * ctypedef npy_cfloat      cfloat_t
  * ctypedef npy_cdouble     cdouble_t
  * ctypedef npy_clongdouble clongdouble_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_cdouble     complex_t
  */
 typedef npy_clongdouble __pyx_t_5numpy_clongdouble_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":732
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":732
  * ctypedef npy_clongdouble clongdouble_t
  * 
  * ctypedef npy_cdouble     complex_t             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew1(a):
  */
 typedef npy_cdouble __pyx_t_5numpy_complex_t;
@@ -3617,15 +3617,15 @@
   __PYX_XDEC_MEMVIEW(&__pyx_v_z, 1);
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
 
@@ -3636,30 +3636,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew1", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew1", __pyx_f[1], 734, 0, __PYX_ERR(1, 734, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":735
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":735
  * 
  * cdef inline object PyArray_MultiIterNew1(a):
  *     return PyArray_MultiIterNew(1, <void*>a)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):
  */
   __Pyx_TraceLine(735,0,__PYX_ERR(1, 735, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(1, ((void *)__pyx_v_a)); if (unlikely(!__pyx_t_1)) __PYX_ERR(1, 735, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
 
@@ -3671,15 +3671,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
 
@@ -3690,30 +3690,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew2", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew2", __pyx_f[1], 737, 0, __PYX_ERR(1, 737, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":738
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":738
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):
  */
   __Pyx_TraceLine(738,0,__PYX_ERR(1, 738, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(2, ((void *)__pyx_v_a), ((void *)__pyx_v_b)); if (unlikely(!__pyx_t_1)) __PYX_ERR(1, 738, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
 
@@ -3725,15 +3725,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
 
@@ -3744,30 +3744,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew3", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew3", __pyx_f[1], 740, 0, __PYX_ERR(1, 740, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":741
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":741
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
  */
   __Pyx_TraceLine(741,0,__PYX_ERR(1, 741, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(3, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c)); if (unlikely(!__pyx_t_1)) __PYX_ERR(1, 741, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
 
@@ -3779,15 +3779,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
 
@@ -3798,30 +3798,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew4", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew4", __pyx_f[1], 743, 0, __PYX_ERR(1, 743, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":744
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":744
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
  */
   __Pyx_TraceLine(744,0,__PYX_ERR(1, 744, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(4, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d)); if (unlikely(!__pyx_t_1)) __PYX_ERR(1, 744, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
 
@@ -3833,15 +3833,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
 
@@ -3852,30 +3852,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew5", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew5", __pyx_f[1], 746, 0, __PYX_ERR(1, 746, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":747
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":747
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)             # <<<<<<<<<<<<<<
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  */
   __Pyx_TraceLine(747,0,__PYX_ERR(1, 747, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(5, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d), ((void *)__pyx_v_e)); if (unlikely(!__pyx_t_1)) __PYX_ERR(1, 747, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
 
@@ -3887,15 +3887,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
 
@@ -3906,63 +3906,63 @@
   int __pyx_t_1;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyDataType_SHAPE", 0);
   __Pyx_TraceCall("PyDataType_SHAPE", __pyx_f[1], 749, 0, __PYX_ERR(1, 749, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":750
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":750
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
  *         return <tuple>d.subarray.shape
  *     else:
  */
   __Pyx_TraceLine(750,0,__PYX_ERR(1, 750, __pyx_L1_error))
   __pyx_t_1 = (PyDataType_HASSUBARRAY(__pyx_v_d) != 0);
   if (__pyx_t_1) {
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":751
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":751
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape             # <<<<<<<<<<<<<<
  *     else:
  *         return ()
  */
     __Pyx_TraceLine(751,0,__PYX_ERR(1, 751, __pyx_L1_error))
     __Pyx_XDECREF(__pyx_r);
     __Pyx_INCREF(((PyObject*)__pyx_v_d->subarray->shape));
     __pyx_r = ((PyObject*)__pyx_v_d->subarray->shape);
     goto __pyx_L0;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":750
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":750
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
  *         return <tuple>d.subarray.shape
  *     else:
  */
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":753
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":753
  *         return <tuple>d.subarray.shape
  *     else:
  *         return ()             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(753,0,__PYX_ERR(1, 753, __pyx_L1_error))
   /*else*/ {
     __Pyx_XDECREF(__pyx_r);
     __Pyx_INCREF(__pyx_empty_tuple);
     __pyx_r = __pyx_empty_tuple;
     goto __pyx_L0;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
 
@@ -3973,15 +3973,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
 
@@ -3990,35 +3990,35 @@
   __Pyx_RefNannyDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("set_array_base", 0);
   __Pyx_TraceCall("set_array_base", __pyx_f[1], 928, 0, __PYX_ERR(1, 928, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":929
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":929
  * 
  * cdef inline void set_array_base(ndarray arr, object base):
  *     Py_INCREF(base) # important to do this before stealing the reference below!             # <<<<<<<<<<<<<<
  *     PyArray_SetBaseObject(arr, base)
  * 
  */
   __Pyx_TraceLine(929,0,__PYX_ERR(1, 929, __pyx_L1_error))
   Py_INCREF(__pyx_v_base);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":930
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":930
  * cdef inline void set_array_base(ndarray arr, object base):
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object get_array_base(ndarray arr):
  */
   __Pyx_TraceLine(930,0,__PYX_ERR(1, 930, __pyx_L1_error))
   (void)(PyArray_SetBaseObject(__pyx_v_arr, __pyx_v_base));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
 
@@ -4027,15 +4027,15 @@
   __pyx_L1_error:;
   __Pyx_WriteUnraisable("numpy.set_array_base", __pyx_clineno, __pyx_lineno, __pyx_filename, 1, 0);
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
 
@@ -4047,70 +4047,70 @@
   int __pyx_t_1;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("get_array_base", 0);
   __Pyx_TraceCall("get_array_base", __pyx_f[1], 932, 0, __PYX_ERR(1, 932, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":933
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":933
  * 
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)             # <<<<<<<<<<<<<<
  *     if base is NULL:
  *         return None
  */
   __Pyx_TraceLine(933,0,__PYX_ERR(1, 933, __pyx_L1_error))
   __pyx_v_base = PyArray_BASE(__pyx_v_arr);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":934
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":934
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)
  *     if base is NULL:             # <<<<<<<<<<<<<<
  *         return None
  *     return <object>base
  */
   __Pyx_TraceLine(934,0,__PYX_ERR(1, 934, __pyx_L1_error))
   __pyx_t_1 = ((__pyx_v_base == NULL) != 0);
   if (__pyx_t_1) {
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":935
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":935
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  *         return None             # <<<<<<<<<<<<<<
  *     return <object>base
  * 
  */
     __Pyx_TraceLine(935,0,__PYX_ERR(1, 935, __pyx_L1_error))
     __Pyx_XDECREF(__pyx_r);
     __pyx_r = Py_None; __Pyx_INCREF(Py_None);
     goto __pyx_L0;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":934
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":934
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)
  *     if base is NULL:             # <<<<<<<<<<<<<<
  *         return None
  *     return <object>base
  */
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":936
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":936
  *     if base is NULL:
  *         return None
  *     return <object>base             # <<<<<<<<<<<<<<
  * 
  * # Versions of the import_* functions which are more suitable for
  */
   __Pyx_TraceLine(936,0,__PYX_ERR(1, 936, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __Pyx_INCREF(((PyObject *)__pyx_v_base));
   __pyx_r = ((PyObject *)__pyx_v_base);
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
 
@@ -4121,15 +4121,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
 
@@ -4147,15 +4147,15 @@
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_array", 0);
   __Pyx_TraceCall("import_array", __pyx_f[1], 940, 0, __PYX_ERR(1, 940, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
   __Pyx_TraceLine(941,0,__PYX_ERR(1, 941, __pyx_L1_error))
@@ -4164,39 +4164,39 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":942
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":942
  * cdef inline int import_array() except -1:
  *     try:
  *         __pyx_import_array()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")
  */
       __Pyx_TraceLine(942,0,__PYX_ERR(1, 942, __pyx_L3_error))
       __pyx_t_4 = _import_array(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(1, 942, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":943
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":943
  *     try:
  *         __pyx_import_array()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  */
     __Pyx_TraceLine(943,0,__PYX_ERR(1, 943, __pyx_L5_except_error))
@@ -4204,15 +4204,15 @@
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_array", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(1, 943, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":944
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":944
  *         __pyx_import_array()
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_umath() except -1:
  */
       __Pyx_TraceLine(944,0,__PYX_ERR(1, 944, __pyx_L5_except_error))
@@ -4221,30 +4221,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(1, 944, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
 
@@ -4260,15 +4260,15 @@
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -4286,15 +4286,15 @@
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_umath", 0);
   __Pyx_TraceCall("import_umath", __pyx_f[1], 946, 0, __PYX_ERR(1, 946, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
   __Pyx_TraceLine(947,0,__PYX_ERR(1, 947, __pyx_L1_error))
@@ -4303,39 +4303,39 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":948
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":948
  * cdef inline int import_umath() except -1:
  *     try:
  *         _import_umath()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")
  */
       __Pyx_TraceLine(948,0,__PYX_ERR(1, 948, __pyx_L3_error))
       __pyx_t_4 = _import_umath(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(1, 948, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":949
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":949
  *     try:
  *         _import_umath()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  */
     __Pyx_TraceLine(949,0,__PYX_ERR(1, 949, __pyx_L5_except_error))
@@ -4343,15 +4343,15 @@
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_umath", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(1, 949, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":950
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":950
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_ufunc() except -1:
  */
       __Pyx_TraceLine(950,0,__PYX_ERR(1, 950, __pyx_L5_except_error))
@@ -4360,30 +4360,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(1, 950, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -4399,15 +4399,15 @@
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -4425,15 +4425,15 @@
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_ufunc", 0);
   __Pyx_TraceCall("import_ufunc", __pyx_f[1], 952, 0, __PYX_ERR(1, 952, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
   __Pyx_TraceLine(953,0,__PYX_ERR(1, 953, __pyx_L1_error))
@@ -4442,39 +4442,39 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":954
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":954
  * cdef inline int import_ufunc() except -1:
  *     try:
  *         _import_umath()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")
  */
       __Pyx_TraceLine(954,0,__PYX_ERR(1, 954, __pyx_L3_error))
       __pyx_t_4 = _import_umath(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(1, 954, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":955
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":955
  *     try:
  *         _import_umath()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  */
     __Pyx_TraceLine(955,0,__PYX_ERR(1, 955, __pyx_L5_except_error))
@@ -4482,15 +4482,15 @@
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_ufunc", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(1, 955, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":956
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":956
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef extern from *:
  */
       __Pyx_TraceLine(956,0,__PYX_ERR(1, 956, __pyx_L5_except_error))
@@ -4499,30 +4499,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(1, 956, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -4538,15 +4538,15 @@
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
 
@@ -4556,26 +4556,26 @@
   __Pyx_RefNannyDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("is_timedelta64_object", 0);
   __Pyx_TraceCall("is_timedelta64_object", __pyx_f[1], 966, 0, __PYX_ERR(1, 966, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":978
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":978
  *     bool
  *     """
  *     return PyObject_TypeCheck(obj, &PyTimedeltaArrType_Type)             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(978,0,__PYX_ERR(1, 978, __pyx_L1_error))
   __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyTimedeltaArrType_Type));
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
 
@@ -4585,15 +4585,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
 
@@ -4603,26 +4603,26 @@
   __Pyx_RefNannyDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("is_datetime64_object", 0);
   __Pyx_TraceCall("is_datetime64_object", __pyx_f[1], 981, 0, __PYX_ERR(1, 981, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":993
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":993
  *     bool
  *     """
  *     return PyObject_TypeCheck(obj, &PyDatetimeArrType_Type)             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(993,0,__PYX_ERR(1, 993, __pyx_L1_error))
   __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyDatetimeArrType_Type));
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
 
@@ -4632,15 +4632,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
 
@@ -4648,26 +4648,26 @@
   npy_datetime __pyx_r;
   __Pyx_TraceDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_TraceCall("get_datetime64_value", __pyx_f[1], 996, 1, __PYX_ERR(1, 996, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1003
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1003
  *     also needed.  That can be found using `get_datetime64_unit`.
  *     """
  *     return (<PyDatetimeScalarObject*>obj).obval             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(1003,1,__PYX_ERR(1, 1003, __pyx_L1_error))
   __pyx_r = ((PyDatetimeScalarObject *)__pyx_v_obj)->obval;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
 
@@ -4676,15 +4676,15 @@
   __Pyx_WriteUnraisable("numpy.get_datetime64_value", __pyx_clineno, __pyx_lineno, __pyx_filename, 1, 1);
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 1);
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
 
@@ -4692,26 +4692,26 @@
   npy_timedelta __pyx_r;
   __Pyx_TraceDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_TraceCall("get_timedelta64_value", __pyx_f[1], 1006, 1, __PYX_ERR(1, 1006, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1010
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1010
  *     returns the int64 value underlying scalar numpy timedelta64 object
  *     """
  *     return (<PyTimedeltaScalarObject*>obj).obval             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(1010,1,__PYX_ERR(1, 1010, __pyx_L1_error))
   __pyx_r = ((PyTimedeltaScalarObject *)__pyx_v_obj)->obval;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
 
@@ -4720,15 +4720,15 @@
   __Pyx_WriteUnraisable("numpy.get_timedelta64_value", __pyx_clineno, __pyx_lineno, __pyx_filename, 1, 1);
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 1);
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
 
@@ -4736,24 +4736,24 @@
   NPY_DATETIMEUNIT __pyx_r;
   __Pyx_TraceDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_TraceCall("get_datetime64_unit", __pyx_f[1], 1013, 1, __PYX_ERR(1, 1013, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1017
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1017
  *     returns the unit part of the dtype for a numpy datetime64 object.
  *     """
  *     return <NPY_DATETIMEUNIT>(<PyDatetimeScalarObject*>obj).obmeta.base             # <<<<<<<<<<<<<<
  */
   __Pyx_TraceLine(1017,1,__PYX_ERR(1, 1017, __pyx_L1_error))
   __pyx_r = ((NPY_DATETIMEUNIT)((PyDatetimeScalarObject *)__pyx_v_obj)->obmeta.base);
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
 
@@ -20293,26 +20293,26 @@
   return -1;
 }
 
 static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
   __Pyx_RefNannyDeclarations
   __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":944
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":944
  *         __pyx_import_array()
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_umath() except -1:
  */
   __pyx_tuple_ = PyTuple_Pack(1, __pyx_kp_u_numpy_core_multiarray_failed_to); if (unlikely(!__pyx_tuple_)) __PYX_ERR(1, 944, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_tuple_);
   __Pyx_GIVEREF(__pyx_tuple_);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":950
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":950
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_ufunc() except -1:
  */
   __pyx_tuple__2 = PyTuple_Pack(1, __pyx_kp_u_numpy_core_umath_failed_to_impor); if (unlikely(!__pyx_tuple__2)) __PYX_ERR(1, 950, __pyx_L1_error)
@@ -21119,165 +21119,165 @@
  */
   __Pyx_TraceLine(1,0,__PYX_ERR(0, 1, __pyx_L1_error))
   __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 1, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_1) < 0) __PYX_ERR(0, 1, __pyx_L1_error)
   __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
   __Pyx_TraceLine(734,0,__PYX_ERR(1, 734, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
   __Pyx_TraceLine(737,0,__PYX_ERR(1, 737, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
   __Pyx_TraceLine(740,0,__PYX_ERR(1, 740, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
   __Pyx_TraceLine(743,0,__PYX_ERR(1, 743, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
   __Pyx_TraceLine(746,0,__PYX_ERR(1, 746, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
   __Pyx_TraceLine(749,0,__PYX_ERR(1, 749, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
   __Pyx_TraceLine(928,0,__PYX_ERR(1, 928, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
   __Pyx_TraceLine(932,0,__PYX_ERR(1, 932, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
   __Pyx_TraceLine(940,0,__PYX_ERR(1, 940, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
   __Pyx_TraceLine(946,0,__PYX_ERR(1, 946, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
   __Pyx_TraceLine(952,0,__PYX_ERR(1, 952, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
   __Pyx_TraceLine(966,0,__PYX_ERR(1, 966, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
   __Pyx_TraceLine(981,0,__PYX_ERR(1, 981, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
   __Pyx_TraceLine(996,0,__PYX_ERR(1, 996, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
   __Pyx_TraceLine(1006,0,__PYX_ERR(1, 1006, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
   __Pyx_TraceLine(1013,0,__PYX_ERR(1, 1013, __pyx_L1_error))
```

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/dynamics/rhs_precessing.pyx` & `pyseobnr-0.2.1/pyseobnr/eob/dynamics/rhs_precessing.pyx`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/fits/EOB_fits.py` & `pyseobnr-0.2.1/pyseobnr/eob/fits/EOB_fits.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/fits/GSF_fits.py` & `pyseobnr-0.2.1/pyseobnr/eob/fits/GSF_fits.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/fits/IV_fits.py` & `pyseobnr-0.2.1/pyseobnr/eob/fits/IV_fits.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/fits/MR_fits.py` & `pyseobnr-0.2.1/pyseobnr/eob/fits/MR_fits.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/fits/fits_Hamiltonian.py` & `pyseobnr-0.2.1/pyseobnr/eob/fits/fits_Hamiltonian.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Ham_AvgS2precess_simple_cython_PA_AD.c` & `pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Ham_AvgS2precess_simple_cython_PA_AD.c`

 * *Files 1% similar despite different names*

```diff
@@ -1,27 +1,27 @@
 /* Generated by Cython 0.29.34 */
 
 /* BEGIN: Cython Metadata
 {
     "distutils": {
         "depends": [
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h",
             "pyseobnr/eob/utils/eob_parameters.h"
         ],
         "extra_compile_args": [
             "-O3"
         ],
         "include_dirs": [
             "pyseobnr/eob/utils",
             "./pyseobnr/eob/utils",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include",
             "pyseobnr/eob/hamiltonian"
         ],
         "name": "pyseobnr.eob.hamiltonian.Ham_AvgS2precess_simple_cython_PA_AD",
         "sources": [
             "pyseobnr/eob/hamiltonian/Ham_AvgS2precess_simple_cython_PA_AD.pyx"
         ]
     },
@@ -1123,195 +1123,195 @@
   char enc_type;
   char new_packmode;
   char enc_packmode;
   char is_valid_array;
 } __Pyx_BufFmt_Context;
 
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":689
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":689
  * # in Cython to enable them only on the right systems.
  * 
  * ctypedef npy_int8       int8_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t
  */
 typedef npy_int8 __pyx_t_5numpy_int8_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":690
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":690
  * 
  * ctypedef npy_int8       int8_t
  * ctypedef npy_int16      int16_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int32      int32_t
  * ctypedef npy_int64      int64_t
  */
 typedef npy_int16 __pyx_t_5numpy_int16_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":691
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":691
  * ctypedef npy_int8       int8_t
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int64      int64_t
  * #ctypedef npy_int96      int96_t
  */
 typedef npy_int32 __pyx_t_5numpy_int32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":692
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":692
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t
  * ctypedef npy_int64      int64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_int96      int96_t
  * #ctypedef npy_int128     int128_t
  */
 typedef npy_int64 __pyx_t_5numpy_int64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":696
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":696
  * #ctypedef npy_int128     int128_t
  * 
  * ctypedef npy_uint8      uint8_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t
  */
 typedef npy_uint8 __pyx_t_5numpy_uint8_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":697
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":697
  * 
  * ctypedef npy_uint8      uint8_t
  * ctypedef npy_uint16     uint16_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint32     uint32_t
  * ctypedef npy_uint64     uint64_t
  */
 typedef npy_uint16 __pyx_t_5numpy_uint16_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":698
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":698
  * ctypedef npy_uint8      uint8_t
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint64     uint64_t
  * #ctypedef npy_uint96     uint96_t
  */
 typedef npy_uint32 __pyx_t_5numpy_uint32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":699
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":699
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t
  * ctypedef npy_uint64     uint64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_uint96     uint96_t
  * #ctypedef npy_uint128    uint128_t
  */
 typedef npy_uint64 __pyx_t_5numpy_uint64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":703
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":703
  * #ctypedef npy_uint128    uint128_t
  * 
  * ctypedef npy_float32    float32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_float64    float64_t
  * #ctypedef npy_float80    float80_t
  */
 typedef npy_float32 __pyx_t_5numpy_float32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":704
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":704
  * 
  * ctypedef npy_float32    float32_t
  * ctypedef npy_float64    float64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_float80    float80_t
  * #ctypedef npy_float128   float128_t
  */
 typedef npy_float64 __pyx_t_5numpy_float64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":713
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":713
  * # The int types are mapped a bit surprising --
  * # numpy.int corresponds to 'l' and numpy.long to 'q'
  * ctypedef npy_long       int_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longlong   long_t
  * ctypedef npy_longlong   longlong_t
  */
 typedef npy_long __pyx_t_5numpy_int_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":714
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":714
  * # numpy.int corresponds to 'l' and numpy.long to 'q'
  * ctypedef npy_long       int_t
  * ctypedef npy_longlong   long_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longlong   longlong_t
  * 
  */
 typedef npy_longlong __pyx_t_5numpy_long_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":715
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":715
  * ctypedef npy_long       int_t
  * ctypedef npy_longlong   long_t
  * ctypedef npy_longlong   longlong_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_ulong      uint_t
  */
 typedef npy_longlong __pyx_t_5numpy_longlong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":717
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":717
  * ctypedef npy_longlong   longlong_t
  * 
  * ctypedef npy_ulong      uint_t             # <<<<<<<<<<<<<<
  * ctypedef npy_ulonglong  ulong_t
  * ctypedef npy_ulonglong  ulonglong_t
  */
 typedef npy_ulong __pyx_t_5numpy_uint_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":718
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":718
  * 
  * ctypedef npy_ulong      uint_t
  * ctypedef npy_ulonglong  ulong_t             # <<<<<<<<<<<<<<
  * ctypedef npy_ulonglong  ulonglong_t
  * 
  */
 typedef npy_ulonglong __pyx_t_5numpy_ulong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":719
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":719
  * ctypedef npy_ulong      uint_t
  * ctypedef npy_ulonglong  ulong_t
  * ctypedef npy_ulonglong  ulonglong_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_intp       intp_t
  */
 typedef npy_ulonglong __pyx_t_5numpy_ulonglong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":721
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":721
  * ctypedef npy_ulonglong  ulonglong_t
  * 
  * ctypedef npy_intp       intp_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uintp      uintp_t
  * 
  */
 typedef npy_intp __pyx_t_5numpy_intp_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":722
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":722
  * 
  * ctypedef npy_intp       intp_t
  * ctypedef npy_uintp      uintp_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_double     float_t
  */
 typedef npy_uintp __pyx_t_5numpy_uintp_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":724
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":724
  * ctypedef npy_uintp      uintp_t
  * 
  * ctypedef npy_double     float_t             # <<<<<<<<<<<<<<
  * ctypedef npy_double     double_t
  * ctypedef npy_longdouble longdouble_t
  */
 typedef npy_double __pyx_t_5numpy_float_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":725
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":725
  * 
  * ctypedef npy_double     float_t
  * ctypedef npy_double     double_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longdouble longdouble_t
  * 
  */
 typedef npy_double __pyx_t_5numpy_double_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":726
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":726
  * ctypedef npy_double     float_t
  * ctypedef npy_double     double_t
  * ctypedef npy_longdouble longdouble_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_cfloat      cfloat_t
  */
 typedef npy_longdouble __pyx_t_5numpy_longdouble_t;
@@ -1349,42 +1349,42 @@
 struct __pyx_obj_8pyseobnr_3eob_11hamiltonian_19Hamiltonian_v5PHM_C_Hamiltonian_v5PHM_C;
 struct __pyx_obj_8pyseobnr_3eob_11hamiltonian_36Ham_AvgS2precess_simple_cython_PA_AD_Ham_AvgS2precess_simple_cython_PA_AD;
 struct __pyx_array_obj;
 struct __pyx_MemviewEnum_obj;
 struct __pyx_memoryview_obj;
 struct __pyx_memoryviewslice_obj;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":728
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":728
  * ctypedef npy_longdouble longdouble_t
  * 
  * ctypedef npy_cfloat      cfloat_t             # <<<<<<<<<<<<<<
  * ctypedef npy_cdouble     cdouble_t
  * ctypedef npy_clongdouble clongdouble_t
  */
 typedef npy_cfloat __pyx_t_5numpy_cfloat_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":729
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":729
  * 
  * ctypedef npy_cfloat      cfloat_t
  * ctypedef npy_cdouble     cdouble_t             # <<<<<<<<<<<<<<
  * ctypedef npy_clongdouble clongdouble_t
  * 
  */
 typedef npy_cdouble __pyx_t_5numpy_cdouble_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":730
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":730
  * ctypedef npy_cfloat      cfloat_t
  * ctypedef npy_cdouble     cdouble_t
  * ctypedef npy_clongdouble clongdouble_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_cdouble     complex_t
  */
 typedef npy_clongdouble __pyx_t_5numpy_clongdouble_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":732
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":732
  * ctypedef npy_clongdouble clongdouble_t
  * 
  * ctypedef npy_cdouble     complex_t             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew1(a):
  */
 typedef npy_cdouble __pyx_t_5numpy_complex_t;
@@ -26315,15 +26315,15 @@
   __pyx_r = NULL;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
 
@@ -26334,30 +26334,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew1", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew1", __pyx_f[2], 734, 0, __PYX_ERR(2, 734, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":735
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":735
  * 
  * cdef inline object PyArray_MultiIterNew1(a):
  *     return PyArray_MultiIterNew(1, <void*>a)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):
  */
   __Pyx_TraceLine(735,0,__PYX_ERR(2, 735, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(1, ((void *)__pyx_v_a)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 735, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
 
@@ -26369,15 +26369,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
 
@@ -26388,30 +26388,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew2", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew2", __pyx_f[2], 737, 0, __PYX_ERR(2, 737, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":738
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":738
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):
  */
   __Pyx_TraceLine(738,0,__PYX_ERR(2, 738, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(2, ((void *)__pyx_v_a), ((void *)__pyx_v_b)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 738, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
 
@@ -26423,15 +26423,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
 
@@ -26442,30 +26442,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew3", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew3", __pyx_f[2], 740, 0, __PYX_ERR(2, 740, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":741
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":741
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
  */
   __Pyx_TraceLine(741,0,__PYX_ERR(2, 741, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(3, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 741, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
 
@@ -26477,15 +26477,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
 
@@ -26496,30 +26496,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew4", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew4", __pyx_f[2], 743, 0, __PYX_ERR(2, 743, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":744
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":744
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
  */
   __Pyx_TraceLine(744,0,__PYX_ERR(2, 744, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(4, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 744, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
 
@@ -26531,15 +26531,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
 
@@ -26550,30 +26550,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew5", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew5", __pyx_f[2], 746, 0, __PYX_ERR(2, 746, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":747
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":747
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)             # <<<<<<<<<<<<<<
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  */
   __Pyx_TraceLine(747,0,__PYX_ERR(2, 747, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(5, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d), ((void *)__pyx_v_e)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 747, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
 
@@ -26585,15 +26585,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
 
@@ -26604,63 +26604,63 @@
   int __pyx_t_1;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyDataType_SHAPE", 0);
   __Pyx_TraceCall("PyDataType_SHAPE", __pyx_f[2], 749, 0, __PYX_ERR(2, 749, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":750
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":750
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
  *         return <tuple>d.subarray.shape
  *     else:
  */
   __Pyx_TraceLine(750,0,__PYX_ERR(2, 750, __pyx_L1_error))
   __pyx_t_1 = (PyDataType_HASSUBARRAY(__pyx_v_d) != 0);
   if (__pyx_t_1) {
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":751
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":751
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape             # <<<<<<<<<<<<<<
  *     else:
  *         return ()
  */
     __Pyx_TraceLine(751,0,__PYX_ERR(2, 751, __pyx_L1_error))
     __Pyx_XDECREF(__pyx_r);
     __Pyx_INCREF(((PyObject*)__pyx_v_d->subarray->shape));
     __pyx_r = ((PyObject*)__pyx_v_d->subarray->shape);
     goto __pyx_L0;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":750
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":750
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
  *         return <tuple>d.subarray.shape
  *     else:
  */
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":753
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":753
  *         return <tuple>d.subarray.shape
  *     else:
  *         return ()             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(753,0,__PYX_ERR(2, 753, __pyx_L1_error))
   /*else*/ {
     __Pyx_XDECREF(__pyx_r);
     __Pyx_INCREF(__pyx_empty_tuple);
     __pyx_r = __pyx_empty_tuple;
     goto __pyx_L0;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
 
@@ -26671,15 +26671,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
 
@@ -26688,35 +26688,35 @@
   __Pyx_RefNannyDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("set_array_base", 0);
   __Pyx_TraceCall("set_array_base", __pyx_f[2], 928, 0, __PYX_ERR(2, 928, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":929
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":929
  * 
  * cdef inline void set_array_base(ndarray arr, object base):
  *     Py_INCREF(base) # important to do this before stealing the reference below!             # <<<<<<<<<<<<<<
  *     PyArray_SetBaseObject(arr, base)
  * 
  */
   __Pyx_TraceLine(929,0,__PYX_ERR(2, 929, __pyx_L1_error))
   Py_INCREF(__pyx_v_base);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":930
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":930
  * cdef inline void set_array_base(ndarray arr, object base):
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object get_array_base(ndarray arr):
  */
   __Pyx_TraceLine(930,0,__PYX_ERR(2, 930, __pyx_L1_error))
   (void)(PyArray_SetBaseObject(__pyx_v_arr, __pyx_v_base));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
 
@@ -26725,15 +26725,15 @@
   __pyx_L1_error:;
   __Pyx_WriteUnraisable("numpy.set_array_base", __pyx_clineno, __pyx_lineno, __pyx_filename, 1, 0);
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
 
@@ -26745,70 +26745,70 @@
   int __pyx_t_1;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("get_array_base", 0);
   __Pyx_TraceCall("get_array_base", __pyx_f[2], 932, 0, __PYX_ERR(2, 932, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":933
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":933
  * 
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)             # <<<<<<<<<<<<<<
  *     if base is NULL:
  *         return None
  */
   __Pyx_TraceLine(933,0,__PYX_ERR(2, 933, __pyx_L1_error))
   __pyx_v_base = PyArray_BASE(__pyx_v_arr);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":934
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":934
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)
  *     if base is NULL:             # <<<<<<<<<<<<<<
  *         return None
  *     return <object>base
  */
   __Pyx_TraceLine(934,0,__PYX_ERR(2, 934, __pyx_L1_error))
   __pyx_t_1 = ((__pyx_v_base == NULL) != 0);
   if (__pyx_t_1) {
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":935
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":935
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  *         return None             # <<<<<<<<<<<<<<
  *     return <object>base
  * 
  */
     __Pyx_TraceLine(935,0,__PYX_ERR(2, 935, __pyx_L1_error))
     __Pyx_XDECREF(__pyx_r);
     __pyx_r = Py_None; __Pyx_INCREF(Py_None);
     goto __pyx_L0;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":934
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":934
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)
  *     if base is NULL:             # <<<<<<<<<<<<<<
  *         return None
  *     return <object>base
  */
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":936
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":936
  *     if base is NULL:
  *         return None
  *     return <object>base             # <<<<<<<<<<<<<<
  * 
  * # Versions of the import_* functions which are more suitable for
  */
   __Pyx_TraceLine(936,0,__PYX_ERR(2, 936, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __Pyx_INCREF(((PyObject *)__pyx_v_base));
   __pyx_r = ((PyObject *)__pyx_v_base);
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
 
@@ -26819,15 +26819,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
 
@@ -26845,15 +26845,15 @@
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_array", 0);
   __Pyx_TraceCall("import_array", __pyx_f[2], 940, 0, __PYX_ERR(2, 940, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
   __Pyx_TraceLine(941,0,__PYX_ERR(2, 941, __pyx_L1_error))
@@ -26862,39 +26862,39 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":942
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":942
  * cdef inline int import_array() except -1:
  *     try:
  *         __pyx_import_array()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")
  */
       __Pyx_TraceLine(942,0,__PYX_ERR(2, 942, __pyx_L3_error))
       __pyx_t_4 = _import_array(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(2, 942, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":943
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":943
  *     try:
  *         __pyx_import_array()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  */
     __Pyx_TraceLine(943,0,__PYX_ERR(2, 943, __pyx_L5_except_error))
@@ -26902,15 +26902,15 @@
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_array", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(2, 943, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":944
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":944
  *         __pyx_import_array()
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_umath() except -1:
  */
       __Pyx_TraceLine(944,0,__PYX_ERR(2, 944, __pyx_L5_except_error))
@@ -26919,30 +26919,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(2, 944, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
 
@@ -26958,15 +26958,15 @@
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -26984,15 +26984,15 @@
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_umath", 0);
   __Pyx_TraceCall("import_umath", __pyx_f[2], 946, 0, __PYX_ERR(2, 946, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
   __Pyx_TraceLine(947,0,__PYX_ERR(2, 947, __pyx_L1_error))
@@ -27001,39 +27001,39 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":948
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":948
  * cdef inline int import_umath() except -1:
  *     try:
  *         _import_umath()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")
  */
       __Pyx_TraceLine(948,0,__PYX_ERR(2, 948, __pyx_L3_error))
       __pyx_t_4 = _import_umath(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(2, 948, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":949
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":949
  *     try:
  *         _import_umath()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  */
     __Pyx_TraceLine(949,0,__PYX_ERR(2, 949, __pyx_L5_except_error))
@@ -27041,15 +27041,15 @@
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_umath", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(2, 949, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":950
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":950
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_ufunc() except -1:
  */
       __Pyx_TraceLine(950,0,__PYX_ERR(2, 950, __pyx_L5_except_error))
@@ -27058,30 +27058,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(2, 950, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -27097,15 +27097,15 @@
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -27123,15 +27123,15 @@
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_ufunc", 0);
   __Pyx_TraceCall("import_ufunc", __pyx_f[2], 952, 0, __PYX_ERR(2, 952, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
   __Pyx_TraceLine(953,0,__PYX_ERR(2, 953, __pyx_L1_error))
@@ -27140,39 +27140,39 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":954
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":954
  * cdef inline int import_ufunc() except -1:
  *     try:
  *         _import_umath()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")
  */
       __Pyx_TraceLine(954,0,__PYX_ERR(2, 954, __pyx_L3_error))
       __pyx_t_4 = _import_umath(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(2, 954, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":955
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":955
  *     try:
  *         _import_umath()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  */
     __Pyx_TraceLine(955,0,__PYX_ERR(2, 955, __pyx_L5_except_error))
@@ -27180,15 +27180,15 @@
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_ufunc", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(2, 955, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":956
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":956
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef extern from *:
  */
       __Pyx_TraceLine(956,0,__PYX_ERR(2, 956, __pyx_L5_except_error))
@@ -27197,30 +27197,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(2, 956, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -27236,15 +27236,15 @@
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
 
@@ -27254,26 +27254,26 @@
   __Pyx_RefNannyDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("is_timedelta64_object", 0);
   __Pyx_TraceCall("is_timedelta64_object", __pyx_f[2], 966, 0, __PYX_ERR(2, 966, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":978
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":978
  *     bool
  *     """
  *     return PyObject_TypeCheck(obj, &PyTimedeltaArrType_Type)             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(978,0,__PYX_ERR(2, 978, __pyx_L1_error))
   __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyTimedeltaArrType_Type));
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
 
@@ -27283,15 +27283,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
 
@@ -27301,26 +27301,26 @@
   __Pyx_RefNannyDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("is_datetime64_object", 0);
   __Pyx_TraceCall("is_datetime64_object", __pyx_f[2], 981, 0, __PYX_ERR(2, 981, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":993
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":993
  *     bool
  *     """
  *     return PyObject_TypeCheck(obj, &PyDatetimeArrType_Type)             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(993,0,__PYX_ERR(2, 993, __pyx_L1_error))
   __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyDatetimeArrType_Type));
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
 
@@ -27330,15 +27330,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
 
@@ -27346,26 +27346,26 @@
   npy_datetime __pyx_r;
   __Pyx_TraceDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_TraceCall("get_datetime64_value", __pyx_f[2], 996, 1, __PYX_ERR(2, 996, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1003
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1003
  *     also needed.  That can be found using `get_datetime64_unit`.
  *     """
  *     return (<PyDatetimeScalarObject*>obj).obval             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(1003,1,__PYX_ERR(2, 1003, __pyx_L1_error))
   __pyx_r = ((PyDatetimeScalarObject *)__pyx_v_obj)->obval;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
 
@@ -27374,15 +27374,15 @@
   __Pyx_WriteUnraisable("numpy.get_datetime64_value", __pyx_clineno, __pyx_lineno, __pyx_filename, 1, 1);
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 1);
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
 
@@ -27390,26 +27390,26 @@
   npy_timedelta __pyx_r;
   __Pyx_TraceDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_TraceCall("get_timedelta64_value", __pyx_f[2], 1006, 1, __PYX_ERR(2, 1006, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1010
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1010
  *     returns the int64 value underlying scalar numpy timedelta64 object
  *     """
  *     return (<PyTimedeltaScalarObject*>obj).obval             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(1010,1,__PYX_ERR(2, 1010, __pyx_L1_error))
   __pyx_r = ((PyTimedeltaScalarObject *)__pyx_v_obj)->obval;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
 
@@ -27418,15 +27418,15 @@
   __Pyx_WriteUnraisable("numpy.get_timedelta64_value", __pyx_clineno, __pyx_lineno, __pyx_filename, 1, 1);
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 1);
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
 
@@ -27434,24 +27434,24 @@
   NPY_DATETIMEUNIT __pyx_r;
   __Pyx_TraceDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_TraceCall("get_datetime64_unit", __pyx_f[2], 1013, 1, __PYX_ERR(2, 1013, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1017
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1017
  *     returns the unit part of the dtype for a numpy datetime64 object.
  *     """
  *     return <NPY_DATETIMEUNIT>(<PyDatetimeScalarObject*>obj).obmeta.base             # <<<<<<<<<<<<<<
  */
   __Pyx_TraceLine(1017,1,__PYX_ERR(2, 1017, __pyx_L1_error))
   __pyx_r = ((NPY_DATETIMEUNIT)((PyDatetimeScalarObject *)__pyx_v_obj)->obmeta.base);
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
 
@@ -42593,26 +42593,26 @@
  * def __setstate_cython__(self, __pyx_state):
  *     raise TypeError("no default __reduce__ due to non-trivial __cinit__")             # <<<<<<<<<<<<<<
  */
   __pyx_tuple__3 = PyTuple_Pack(1, __pyx_kp_s_no_default___reduce___due_to_non); if (unlikely(!__pyx_tuple__3)) __PYX_ERR(0, 4, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_tuple__3);
   __Pyx_GIVEREF(__pyx_tuple__3);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":944
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":944
  *         __pyx_import_array()
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_umath() except -1:
  */
   __pyx_tuple__4 = PyTuple_Pack(1, __pyx_kp_u_numpy_core_multiarray_failed_to); if (unlikely(!__pyx_tuple__4)) __PYX_ERR(2, 944, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_tuple__4);
   __Pyx_GIVEREF(__pyx_tuple__4);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":950
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":950
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_ufunc() except -1:
  */
   __pyx_tuple__5 = PyTuple_Pack(1, __pyx_kp_u_numpy_core_umath_failed_to_impor); if (unlikely(!__pyx_tuple__5)) __PYX_ERR(2, 950, __pyx_L1_error)
@@ -43435,165 +43435,165 @@
  */
   __Pyx_TraceLine(2,0,__PYX_ERR(1, 2, __pyx_L1_error))
   __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(1, 2, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_1) < 0) __PYX_ERR(1, 2, __pyx_L1_error)
   __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
   __Pyx_TraceLine(734,0,__PYX_ERR(2, 734, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
   __Pyx_TraceLine(737,0,__PYX_ERR(2, 737, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
   __Pyx_TraceLine(740,0,__PYX_ERR(2, 740, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
   __Pyx_TraceLine(743,0,__PYX_ERR(2, 743, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
   __Pyx_TraceLine(746,0,__PYX_ERR(2, 746, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
   __Pyx_TraceLine(749,0,__PYX_ERR(2, 749, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
   __Pyx_TraceLine(928,0,__PYX_ERR(2, 928, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
   __Pyx_TraceLine(932,0,__PYX_ERR(2, 932, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
   __Pyx_TraceLine(940,0,__PYX_ERR(2, 940, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
   __Pyx_TraceLine(946,0,__PYX_ERR(2, 946, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
   __Pyx_TraceLine(952,0,__PYX_ERR(2, 952, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
   __Pyx_TraceLine(966,0,__PYX_ERR(2, 966, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
   __Pyx_TraceLine(981,0,__PYX_ERR(2, 981, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
   __Pyx_TraceLine(996,0,__PYX_ERR(2, 996, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
   __Pyx_TraceLine(1006,0,__PYX_ERR(2, 1006, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
   __Pyx_TraceLine(1013,0,__PYX_ERR(2, 1013, __pyx_L1_error))
```

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Ham_AvgS2precess_simple_cython_PA_AD.pyx` & `pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Ham_AvgS2precess_simple_cython_PA_AD.pyx`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C.c` & `pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C.c`

 * *Files 2% similar despite different names*

```diff
@@ -6,28 +6,28 @@
         "define_macros": [
             [
                 "CYTHON_TRACE",
                 "1"
             ]
         ],
         "depends": [
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h",
             "pyseobnr/eob/utils/eob_parameters.h"
         ],
         "extra_compile_args": [
             "-O3"
         ],
         "include_dirs": [
             "pyseobnr/eob/utils",
             "./pyseobnr/eob/utils",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include"
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include"
         ],
         "name": "pyseobnr.eob.hamiltonian.Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C",
         "sources": [
             "pyseobnr/eob/hamiltonian/Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C.pyx"
         ]
     },
     "module_name": "pyseobnr.eob.hamiltonian.Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C"
@@ -1128,195 +1128,195 @@
   char enc_type;
   char new_packmode;
   char enc_packmode;
   char is_valid_array;
 } __Pyx_BufFmt_Context;
 
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":689
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":689
  * # in Cython to enable them only on the right systems.
  * 
  * ctypedef npy_int8       int8_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t
  */
 typedef npy_int8 __pyx_t_5numpy_int8_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":690
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":690
  * 
  * ctypedef npy_int8       int8_t
  * ctypedef npy_int16      int16_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int32      int32_t
  * ctypedef npy_int64      int64_t
  */
 typedef npy_int16 __pyx_t_5numpy_int16_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":691
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":691
  * ctypedef npy_int8       int8_t
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int64      int64_t
  * #ctypedef npy_int96      int96_t
  */
 typedef npy_int32 __pyx_t_5numpy_int32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":692
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":692
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t
  * ctypedef npy_int64      int64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_int96      int96_t
  * #ctypedef npy_int128     int128_t
  */
 typedef npy_int64 __pyx_t_5numpy_int64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":696
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":696
  * #ctypedef npy_int128     int128_t
  * 
  * ctypedef npy_uint8      uint8_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t
  */
 typedef npy_uint8 __pyx_t_5numpy_uint8_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":697
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":697
  * 
  * ctypedef npy_uint8      uint8_t
  * ctypedef npy_uint16     uint16_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint32     uint32_t
  * ctypedef npy_uint64     uint64_t
  */
 typedef npy_uint16 __pyx_t_5numpy_uint16_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":698
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":698
  * ctypedef npy_uint8      uint8_t
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint64     uint64_t
  * #ctypedef npy_uint96     uint96_t
  */
 typedef npy_uint32 __pyx_t_5numpy_uint32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":699
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":699
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t
  * ctypedef npy_uint64     uint64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_uint96     uint96_t
  * #ctypedef npy_uint128    uint128_t
  */
 typedef npy_uint64 __pyx_t_5numpy_uint64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":703
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":703
  * #ctypedef npy_uint128    uint128_t
  * 
  * ctypedef npy_float32    float32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_float64    float64_t
  * #ctypedef npy_float80    float80_t
  */
 typedef npy_float32 __pyx_t_5numpy_float32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":704
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":704
  * 
  * ctypedef npy_float32    float32_t
  * ctypedef npy_float64    float64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_float80    float80_t
  * #ctypedef npy_float128   float128_t
  */
 typedef npy_float64 __pyx_t_5numpy_float64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":713
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":713
  * # The int types are mapped a bit surprising --
  * # numpy.int corresponds to 'l' and numpy.long to 'q'
  * ctypedef npy_long       int_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longlong   long_t
  * ctypedef npy_longlong   longlong_t
  */
 typedef npy_long __pyx_t_5numpy_int_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":714
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":714
  * # numpy.int corresponds to 'l' and numpy.long to 'q'
  * ctypedef npy_long       int_t
  * ctypedef npy_longlong   long_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longlong   longlong_t
  * 
  */
 typedef npy_longlong __pyx_t_5numpy_long_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":715
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":715
  * ctypedef npy_long       int_t
  * ctypedef npy_longlong   long_t
  * ctypedef npy_longlong   longlong_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_ulong      uint_t
  */
 typedef npy_longlong __pyx_t_5numpy_longlong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":717
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":717
  * ctypedef npy_longlong   longlong_t
  * 
  * ctypedef npy_ulong      uint_t             # <<<<<<<<<<<<<<
  * ctypedef npy_ulonglong  ulong_t
  * ctypedef npy_ulonglong  ulonglong_t
  */
 typedef npy_ulong __pyx_t_5numpy_uint_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":718
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":718
  * 
  * ctypedef npy_ulong      uint_t
  * ctypedef npy_ulonglong  ulong_t             # <<<<<<<<<<<<<<
  * ctypedef npy_ulonglong  ulonglong_t
  * 
  */
 typedef npy_ulonglong __pyx_t_5numpy_ulong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":719
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":719
  * ctypedef npy_ulong      uint_t
  * ctypedef npy_ulonglong  ulong_t
  * ctypedef npy_ulonglong  ulonglong_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_intp       intp_t
  */
 typedef npy_ulonglong __pyx_t_5numpy_ulonglong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":721
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":721
  * ctypedef npy_ulonglong  ulonglong_t
  * 
  * ctypedef npy_intp       intp_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uintp      uintp_t
  * 
  */
 typedef npy_intp __pyx_t_5numpy_intp_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":722
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":722
  * 
  * ctypedef npy_intp       intp_t
  * ctypedef npy_uintp      uintp_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_double     float_t
  */
 typedef npy_uintp __pyx_t_5numpy_uintp_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":724
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":724
  * ctypedef npy_uintp      uintp_t
  * 
  * ctypedef npy_double     float_t             # <<<<<<<<<<<<<<
  * ctypedef npy_double     double_t
  * ctypedef npy_longdouble longdouble_t
  */
 typedef npy_double __pyx_t_5numpy_float_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":725
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":725
  * 
  * ctypedef npy_double     float_t
  * ctypedef npy_double     double_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longdouble longdouble_t
  * 
  */
 typedef npy_double __pyx_t_5numpy_double_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":726
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":726
  * ctypedef npy_double     float_t
  * ctypedef npy_double     double_t
  * ctypedef npy_longdouble longdouble_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_cfloat      cfloat_t
  */
 typedef npy_longdouble __pyx_t_5numpy_longdouble_t;
@@ -1354,42 +1354,42 @@
 struct __pyx_obj_8pyseobnr_3eob_11hamiltonian_13Hamiltonian_C_Hamiltonian_C;
 struct __pyx_obj_8pyseobnr_3eob_11hamiltonian_39Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C_Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C;
 struct __pyx_array_obj;
 struct __pyx_MemviewEnum_obj;
 struct __pyx_memoryview_obj;
 struct __pyx_memoryviewslice_obj;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":728
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":728
  * ctypedef npy_longdouble longdouble_t
  * 
  * ctypedef npy_cfloat      cfloat_t             # <<<<<<<<<<<<<<
  * ctypedef npy_cdouble     cdouble_t
  * ctypedef npy_clongdouble clongdouble_t
  */
 typedef npy_cfloat __pyx_t_5numpy_cfloat_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":729
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":729
  * 
  * ctypedef npy_cfloat      cfloat_t
  * ctypedef npy_cdouble     cdouble_t             # <<<<<<<<<<<<<<
  * ctypedef npy_clongdouble clongdouble_t
  * 
  */
 typedef npy_cdouble __pyx_t_5numpy_cdouble_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":730
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":730
  * ctypedef npy_cfloat      cfloat_t
  * ctypedef npy_cdouble     cdouble_t
  * ctypedef npy_clongdouble clongdouble_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_cdouble     complex_t
  */
 typedef npy_clongdouble __pyx_t_5numpy_clongdouble_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":732
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":732
  * ctypedef npy_clongdouble clongdouble_t
  * 
  * ctypedef npy_cdouble     complex_t             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew1(a):
  */
 typedef npy_cdouble __pyx_t_5numpy_complex_t;
@@ -22991,15 +22991,15 @@
   __pyx_r = NULL;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
 
@@ -23010,30 +23010,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew1", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew1", __pyx_f[2], 734, 0, __PYX_ERR(2, 734, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":735
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":735
  * 
  * cdef inline object PyArray_MultiIterNew1(a):
  *     return PyArray_MultiIterNew(1, <void*>a)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):
  */
   __Pyx_TraceLine(735,0,__PYX_ERR(2, 735, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(1, ((void *)__pyx_v_a)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 735, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
 
@@ -23045,15 +23045,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
 
@@ -23064,30 +23064,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew2", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew2", __pyx_f[2], 737, 0, __PYX_ERR(2, 737, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":738
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":738
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):
  */
   __Pyx_TraceLine(738,0,__PYX_ERR(2, 738, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(2, ((void *)__pyx_v_a), ((void *)__pyx_v_b)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 738, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
 
@@ -23099,15 +23099,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
 
@@ -23118,30 +23118,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew3", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew3", __pyx_f[2], 740, 0, __PYX_ERR(2, 740, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":741
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":741
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
  */
   __Pyx_TraceLine(741,0,__PYX_ERR(2, 741, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(3, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 741, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
 
@@ -23153,15 +23153,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
 
@@ -23172,30 +23172,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew4", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew4", __pyx_f[2], 743, 0, __PYX_ERR(2, 743, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":744
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":744
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
  */
   __Pyx_TraceLine(744,0,__PYX_ERR(2, 744, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(4, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 744, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
 
@@ -23207,15 +23207,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
 
@@ -23226,30 +23226,30 @@
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew5", 0);
   __Pyx_TraceCall("PyArray_MultiIterNew5", __pyx_f[2], 746, 0, __PYX_ERR(2, 746, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":747
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":747
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)             # <<<<<<<<<<<<<<
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  */
   __Pyx_TraceLine(747,0,__PYX_ERR(2, 747, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(5, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d), ((void *)__pyx_v_e)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 747, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
 
@@ -23261,15 +23261,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
 
@@ -23280,63 +23280,63 @@
   int __pyx_t_1;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyDataType_SHAPE", 0);
   __Pyx_TraceCall("PyDataType_SHAPE", __pyx_f[2], 749, 0, __PYX_ERR(2, 749, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":750
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":750
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
  *         return <tuple>d.subarray.shape
  *     else:
  */
   __Pyx_TraceLine(750,0,__PYX_ERR(2, 750, __pyx_L1_error))
   __pyx_t_1 = (PyDataType_HASSUBARRAY(__pyx_v_d) != 0);
   if (__pyx_t_1) {
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":751
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":751
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape             # <<<<<<<<<<<<<<
  *     else:
  *         return ()
  */
     __Pyx_TraceLine(751,0,__PYX_ERR(2, 751, __pyx_L1_error))
     __Pyx_XDECREF(__pyx_r);
     __Pyx_INCREF(((PyObject*)__pyx_v_d->subarray->shape));
     __pyx_r = ((PyObject*)__pyx_v_d->subarray->shape);
     goto __pyx_L0;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":750
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":750
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
  *         return <tuple>d.subarray.shape
  *     else:
  */
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":753
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":753
  *         return <tuple>d.subarray.shape
  *     else:
  *         return ()             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(753,0,__PYX_ERR(2, 753, __pyx_L1_error))
   /*else*/ {
     __Pyx_XDECREF(__pyx_r);
     __Pyx_INCREF(__pyx_empty_tuple);
     __pyx_r = __pyx_empty_tuple;
     goto __pyx_L0;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
 
@@ -23347,15 +23347,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
 
@@ -23364,35 +23364,35 @@
   __Pyx_RefNannyDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("set_array_base", 0);
   __Pyx_TraceCall("set_array_base", __pyx_f[2], 928, 0, __PYX_ERR(2, 928, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":929
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":929
  * 
  * cdef inline void set_array_base(ndarray arr, object base):
  *     Py_INCREF(base) # important to do this before stealing the reference below!             # <<<<<<<<<<<<<<
  *     PyArray_SetBaseObject(arr, base)
  * 
  */
   __Pyx_TraceLine(929,0,__PYX_ERR(2, 929, __pyx_L1_error))
   Py_INCREF(__pyx_v_base);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":930
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":930
  * cdef inline void set_array_base(ndarray arr, object base):
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object get_array_base(ndarray arr):
  */
   __Pyx_TraceLine(930,0,__PYX_ERR(2, 930, __pyx_L1_error))
   (void)(PyArray_SetBaseObject(__pyx_v_arr, __pyx_v_base));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
 
@@ -23401,15 +23401,15 @@
   __pyx_L1_error:;
   __Pyx_WriteUnraisable("numpy.set_array_base", __pyx_clineno, __pyx_lineno, __pyx_filename, 1, 0);
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
 
@@ -23421,70 +23421,70 @@
   int __pyx_t_1;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("get_array_base", 0);
   __Pyx_TraceCall("get_array_base", __pyx_f[2], 932, 0, __PYX_ERR(2, 932, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":933
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":933
  * 
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)             # <<<<<<<<<<<<<<
  *     if base is NULL:
  *         return None
  */
   __Pyx_TraceLine(933,0,__PYX_ERR(2, 933, __pyx_L1_error))
   __pyx_v_base = PyArray_BASE(__pyx_v_arr);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":934
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":934
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)
  *     if base is NULL:             # <<<<<<<<<<<<<<
  *         return None
  *     return <object>base
  */
   __Pyx_TraceLine(934,0,__PYX_ERR(2, 934, __pyx_L1_error))
   __pyx_t_1 = ((__pyx_v_base == NULL) != 0);
   if (__pyx_t_1) {
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":935
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":935
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  *         return None             # <<<<<<<<<<<<<<
  *     return <object>base
  * 
  */
     __Pyx_TraceLine(935,0,__PYX_ERR(2, 935, __pyx_L1_error))
     __Pyx_XDECREF(__pyx_r);
     __pyx_r = Py_None; __Pyx_INCREF(Py_None);
     goto __pyx_L0;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":934
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":934
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)
  *     if base is NULL:             # <<<<<<<<<<<<<<
  *         return None
  *     return <object>base
  */
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":936
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":936
  *     if base is NULL:
  *         return None
  *     return <object>base             # <<<<<<<<<<<<<<
  * 
  * # Versions of the import_* functions which are more suitable for
  */
   __Pyx_TraceLine(936,0,__PYX_ERR(2, 936, __pyx_L1_error))
   __Pyx_XDECREF(__pyx_r);
   __Pyx_INCREF(((PyObject *)__pyx_v_base));
   __pyx_r = ((PyObject *)__pyx_v_base);
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
 
@@ -23495,15 +23495,15 @@
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
 
@@ -23521,15 +23521,15 @@
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_array", 0);
   __Pyx_TraceCall("import_array", __pyx_f[2], 940, 0, __PYX_ERR(2, 940, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
   __Pyx_TraceLine(941,0,__PYX_ERR(2, 941, __pyx_L1_error))
@@ -23538,39 +23538,39 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":942
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":942
  * cdef inline int import_array() except -1:
  *     try:
  *         __pyx_import_array()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")
  */
       __Pyx_TraceLine(942,0,__PYX_ERR(2, 942, __pyx_L3_error))
       __pyx_t_4 = _import_array(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(2, 942, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":943
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":943
  *     try:
  *         __pyx_import_array()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  */
     __Pyx_TraceLine(943,0,__PYX_ERR(2, 943, __pyx_L5_except_error))
@@ -23578,15 +23578,15 @@
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_array", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(2, 943, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":944
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":944
  *         __pyx_import_array()
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_umath() except -1:
  */
       __Pyx_TraceLine(944,0,__PYX_ERR(2, 944, __pyx_L5_except_error))
@@ -23595,30 +23595,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(2, 944, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
 
@@ -23634,15 +23634,15 @@
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -23660,15 +23660,15 @@
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_umath", 0);
   __Pyx_TraceCall("import_umath", __pyx_f[2], 946, 0, __PYX_ERR(2, 946, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
   __Pyx_TraceLine(947,0,__PYX_ERR(2, 947, __pyx_L1_error))
@@ -23677,39 +23677,39 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":948
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":948
  * cdef inline int import_umath() except -1:
  *     try:
  *         _import_umath()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")
  */
       __Pyx_TraceLine(948,0,__PYX_ERR(2, 948, __pyx_L3_error))
       __pyx_t_4 = _import_umath(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(2, 948, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":949
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":949
  *     try:
  *         _import_umath()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  */
     __Pyx_TraceLine(949,0,__PYX_ERR(2, 949, __pyx_L5_except_error))
@@ -23717,15 +23717,15 @@
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_umath", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(2, 949, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":950
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":950
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_ufunc() except -1:
  */
       __Pyx_TraceLine(950,0,__PYX_ERR(2, 950, __pyx_L5_except_error))
@@ -23734,30 +23734,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(2, 950, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -23773,15 +23773,15 @@
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -23799,15 +23799,15 @@
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_ufunc", 0);
   __Pyx_TraceCall("import_ufunc", __pyx_f[2], 952, 0, __PYX_ERR(2, 952, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
   __Pyx_TraceLine(953,0,__PYX_ERR(2, 953, __pyx_L1_error))
@@ -23816,39 +23816,39 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":954
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":954
  * cdef inline int import_ufunc() except -1:
  *     try:
  *         _import_umath()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")
  */
       __Pyx_TraceLine(954,0,__PYX_ERR(2, 954, __pyx_L3_error))
       __pyx_t_4 = _import_umath(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(2, 954, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":955
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":955
  *     try:
  *         _import_umath()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  */
     __Pyx_TraceLine(955,0,__PYX_ERR(2, 955, __pyx_L5_except_error))
@@ -23856,15 +23856,15 @@
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_ufunc", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(2, 955, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":956
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":956
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef extern from *:
  */
       __Pyx_TraceLine(956,0,__PYX_ERR(2, 956, __pyx_L5_except_error))
@@ -23873,30 +23873,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(2, 956, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -23912,15 +23912,15 @@
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
 
@@ -23930,26 +23930,26 @@
   __Pyx_RefNannyDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("is_timedelta64_object", 0);
   __Pyx_TraceCall("is_timedelta64_object", __pyx_f[2], 966, 0, __PYX_ERR(2, 966, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":978
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":978
  *     bool
  *     """
  *     return PyObject_TypeCheck(obj, &PyTimedeltaArrType_Type)             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(978,0,__PYX_ERR(2, 978, __pyx_L1_error))
   __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyTimedeltaArrType_Type));
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
 
@@ -23959,15 +23959,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
 
@@ -23977,26 +23977,26 @@
   __Pyx_RefNannyDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("is_datetime64_object", 0);
   __Pyx_TraceCall("is_datetime64_object", __pyx_f[2], 981, 0, __PYX_ERR(2, 981, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":993
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":993
  *     bool
  *     """
  *     return PyObject_TypeCheck(obj, &PyDatetimeArrType_Type)             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(993,0,__PYX_ERR(2, 993, __pyx_L1_error))
   __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyDatetimeArrType_Type));
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
 
@@ -24006,15 +24006,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
 
@@ -24022,26 +24022,26 @@
   npy_datetime __pyx_r;
   __Pyx_TraceDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_TraceCall("get_datetime64_value", __pyx_f[2], 996, 1, __PYX_ERR(2, 996, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1003
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1003
  *     also needed.  That can be found using `get_datetime64_unit`.
  *     """
  *     return (<PyDatetimeScalarObject*>obj).obval             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(1003,1,__PYX_ERR(2, 1003, __pyx_L1_error))
   __pyx_r = ((PyDatetimeScalarObject *)__pyx_v_obj)->obval;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
 
@@ -24050,15 +24050,15 @@
   __Pyx_WriteUnraisable("numpy.get_datetime64_value", __pyx_clineno, __pyx_lineno, __pyx_filename, 1, 1);
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 1);
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
 
@@ -24066,26 +24066,26 @@
   npy_timedelta __pyx_r;
   __Pyx_TraceDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_TraceCall("get_timedelta64_value", __pyx_f[2], 1006, 1, __PYX_ERR(2, 1006, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1010
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1010
  *     returns the int64 value underlying scalar numpy timedelta64 object
  *     """
  *     return (<PyTimedeltaScalarObject*>obj).obval             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __Pyx_TraceLine(1010,1,__PYX_ERR(2, 1010, __pyx_L1_error))
   __pyx_r = ((PyTimedeltaScalarObject *)__pyx_v_obj)->obval;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
 
@@ -24094,15 +24094,15 @@
   __Pyx_WriteUnraisable("numpy.get_timedelta64_value", __pyx_clineno, __pyx_lineno, __pyx_filename, 1, 1);
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_TraceReturn(Py_None, 1);
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
 
@@ -24110,24 +24110,24 @@
   NPY_DATETIMEUNIT __pyx_r;
   __Pyx_TraceDeclarations
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_TraceCall("get_datetime64_unit", __pyx_f[2], 1013, 1, __PYX_ERR(2, 1013, __pyx_L1_error));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1017
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1017
  *     returns the unit part of the dtype for a numpy datetime64 object.
  *     """
  *     return <NPY_DATETIMEUNIT>(<PyDatetimeScalarObject*>obj).obmeta.base             # <<<<<<<<<<<<<<
  */
   __Pyx_TraceLine(1017,1,__PYX_ERR(2, 1017, __pyx_L1_error))
   __pyx_r = ((NPY_DATETIMEUNIT)((PyDatetimeScalarObject *)__pyx_v_obj)->obmeta.base);
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
 
@@ -39527,26 +39527,26 @@
  * def __setstate_cython__(self, __pyx_state):
  *     raise TypeError("no default __reduce__ due to non-trivial __cinit__")             # <<<<<<<<<<<<<<
  */
   __pyx_tuple__12 = PyTuple_Pack(1, __pyx_kp_s_no_default___reduce___due_to_non); if (unlikely(!__pyx_tuple__12)) __PYX_ERR(0, 4, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_tuple__12);
   __Pyx_GIVEREF(__pyx_tuple__12);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":944
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":944
  *         __pyx_import_array()
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_umath() except -1:
  */
   __pyx_tuple__13 = PyTuple_Pack(1, __pyx_kp_u_numpy_core_multiarray_failed_to); if (unlikely(!__pyx_tuple__13)) __PYX_ERR(2, 944, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_tuple__13);
   __Pyx_GIVEREF(__pyx_tuple__13);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":950
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":950
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_ufunc() except -1:
  */
   __pyx_tuple__14 = PyTuple_Pack(1, __pyx_kp_u_numpy_core_umath_failed_to_impor); if (unlikely(!__pyx_tuple__14)) __PYX_ERR(2, 950, __pyx_L1_error)
@@ -40542,165 +40542,165 @@
  */
   __Pyx_TraceLine(2,0,__PYX_ERR(1, 2, __pyx_L1_error))
   __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(1, 2, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_1) < 0) __PYX_ERR(1, 2, __pyx_L1_error)
   __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
   __Pyx_TraceLine(734,0,__PYX_ERR(2, 734, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
   __Pyx_TraceLine(737,0,__PYX_ERR(2, 737, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
   __Pyx_TraceLine(740,0,__PYX_ERR(2, 740, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
   __Pyx_TraceLine(743,0,__PYX_ERR(2, 743, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
   __Pyx_TraceLine(746,0,__PYX_ERR(2, 746, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
   __Pyx_TraceLine(749,0,__PYX_ERR(2, 749, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
   __Pyx_TraceLine(928,0,__PYX_ERR(2, 928, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
   __Pyx_TraceLine(932,0,__PYX_ERR(2, 932, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
   __Pyx_TraceLine(940,0,__PYX_ERR(2, 940, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
   __Pyx_TraceLine(946,0,__PYX_ERR(2, 946, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
   __Pyx_TraceLine(952,0,__PYX_ERR(2, 952, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
   __Pyx_TraceLine(966,0,__PYX_ERR(2, 966, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
   __Pyx_TraceLine(981,0,__PYX_ERR(2, 981, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
   __Pyx_TraceLine(996,0,__PYX_ERR(2, 996, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
   __Pyx_TraceLine(1006,0,__PYX_ERR(2, 1006, __pyx_L1_error))
 
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
   __Pyx_TraceLine(1013,0,__PYX_ERR(2, 1013, __pyx_L1_error))
```

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C.pyx` & `pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Ham_align_a6_apm_AP15_DP23_gaugeL_Tay_C.pyx`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Hamiltonian_C.c` & `pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Hamiltonian_C.c`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Hamiltonian_C.pxd` & `pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Hamiltonian_C.pxd`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Hamiltonian_C.pyx` & `pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Hamiltonian_C.pyx`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Hamiltonian_v5PHM_C.c` & `pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Hamiltonian_v5PHM_C.c`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Hamiltonian_v5PHM_C.pxd` & `pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Hamiltonian_v5PHM_C.pxd`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/Hamiltonian_v5PHM_C.pyx` & `pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/Hamiltonian_v5PHM_C.pyx`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/hamiltonian/hamiltonian.py` & `pyseobnr-0.2.1/pyseobnr/eob/hamiltonian/hamiltonian.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/utils/containers.c` & `pyseobnr-0.2.1/pyseobnr/eob/utils/containers.c`

 * *Files 1% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 /* Generated by Cython 0.29.34 */
 
 /* BEGIN: Cython Metadata
 {
     "distutils": {
         "depends": [
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h",
             "pyseobnr/eob/utils/eob_parameters.h"
         ],
         "include_dirs": [
             "pyseobnr/eob/utils",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include"
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include"
         ],
         "name": "pyseobnr.eob.utils.containers",
         "sources": [
             "pyseobnr/eob/utils/containers.pyx"
         ]
     },
     "module_name": "pyseobnr.eob.utils.containers"
@@ -1117,195 +1117,195 @@
   char enc_type;
   char new_packmode;
   char enc_packmode;
   char is_valid_array;
 } __Pyx_BufFmt_Context;
 
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":689
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":689
  * # in Cython to enable them only on the right systems.
  * 
  * ctypedef npy_int8       int8_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t
  */
 typedef npy_int8 __pyx_t_5numpy_int8_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":690
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":690
  * 
  * ctypedef npy_int8       int8_t
  * ctypedef npy_int16      int16_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int32      int32_t
  * ctypedef npy_int64      int64_t
  */
 typedef npy_int16 __pyx_t_5numpy_int16_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":691
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":691
  * ctypedef npy_int8       int8_t
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int64      int64_t
  * #ctypedef npy_int96      int96_t
  */
 typedef npy_int32 __pyx_t_5numpy_int32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":692
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":692
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t
  * ctypedef npy_int64      int64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_int96      int96_t
  * #ctypedef npy_int128     int128_t
  */
 typedef npy_int64 __pyx_t_5numpy_int64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":696
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":696
  * #ctypedef npy_int128     int128_t
  * 
  * ctypedef npy_uint8      uint8_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t
  */
 typedef npy_uint8 __pyx_t_5numpy_uint8_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":697
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":697
  * 
  * ctypedef npy_uint8      uint8_t
  * ctypedef npy_uint16     uint16_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint32     uint32_t
  * ctypedef npy_uint64     uint64_t
  */
 typedef npy_uint16 __pyx_t_5numpy_uint16_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":698
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":698
  * ctypedef npy_uint8      uint8_t
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint64     uint64_t
  * #ctypedef npy_uint96     uint96_t
  */
 typedef npy_uint32 __pyx_t_5numpy_uint32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":699
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":699
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t
  * ctypedef npy_uint64     uint64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_uint96     uint96_t
  * #ctypedef npy_uint128    uint128_t
  */
 typedef npy_uint64 __pyx_t_5numpy_uint64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":703
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":703
  * #ctypedef npy_uint128    uint128_t
  * 
  * ctypedef npy_float32    float32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_float64    float64_t
  * #ctypedef npy_float80    float80_t
  */
 typedef npy_float32 __pyx_t_5numpy_float32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":704
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":704
  * 
  * ctypedef npy_float32    float32_t
  * ctypedef npy_float64    float64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_float80    float80_t
  * #ctypedef npy_float128   float128_t
  */
 typedef npy_float64 __pyx_t_5numpy_float64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":713
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":713
  * # The int types are mapped a bit surprising --
  * # numpy.int corresponds to 'l' and numpy.long to 'q'
  * ctypedef npy_long       int_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longlong   long_t
  * ctypedef npy_longlong   longlong_t
  */
 typedef npy_long __pyx_t_5numpy_int_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":714
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":714
  * # numpy.int corresponds to 'l' and numpy.long to 'q'
  * ctypedef npy_long       int_t
  * ctypedef npy_longlong   long_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longlong   longlong_t
  * 
  */
 typedef npy_longlong __pyx_t_5numpy_long_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":715
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":715
  * ctypedef npy_long       int_t
  * ctypedef npy_longlong   long_t
  * ctypedef npy_longlong   longlong_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_ulong      uint_t
  */
 typedef npy_longlong __pyx_t_5numpy_longlong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":717
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":717
  * ctypedef npy_longlong   longlong_t
  * 
  * ctypedef npy_ulong      uint_t             # <<<<<<<<<<<<<<
  * ctypedef npy_ulonglong  ulong_t
  * ctypedef npy_ulonglong  ulonglong_t
  */
 typedef npy_ulong __pyx_t_5numpy_uint_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":718
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":718
  * 
  * ctypedef npy_ulong      uint_t
  * ctypedef npy_ulonglong  ulong_t             # <<<<<<<<<<<<<<
  * ctypedef npy_ulonglong  ulonglong_t
  * 
  */
 typedef npy_ulonglong __pyx_t_5numpy_ulong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":719
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":719
  * ctypedef npy_ulong      uint_t
  * ctypedef npy_ulonglong  ulong_t
  * ctypedef npy_ulonglong  ulonglong_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_intp       intp_t
  */
 typedef npy_ulonglong __pyx_t_5numpy_ulonglong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":721
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":721
  * ctypedef npy_ulonglong  ulonglong_t
  * 
  * ctypedef npy_intp       intp_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uintp      uintp_t
  * 
  */
 typedef npy_intp __pyx_t_5numpy_intp_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":722
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":722
  * 
  * ctypedef npy_intp       intp_t
  * ctypedef npy_uintp      uintp_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_double     float_t
  */
 typedef npy_uintp __pyx_t_5numpy_uintp_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":724
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":724
  * ctypedef npy_uintp      uintp_t
  * 
  * ctypedef npy_double     float_t             # <<<<<<<<<<<<<<
  * ctypedef npy_double     double_t
  * ctypedef npy_longdouble longdouble_t
  */
 typedef npy_double __pyx_t_5numpy_float_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":725
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":725
  * 
  * ctypedef npy_double     float_t
  * ctypedef npy_double     double_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longdouble longdouble_t
  * 
  */
 typedef npy_double __pyx_t_5numpy_double_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":726
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":726
  * ctypedef npy_double     float_t
  * ctypedef npy_double     double_t
  * ctypedef npy_longdouble longdouble_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_cfloat      cfloat_t
  */
 typedef npy_longdouble __pyx_t_5numpy_longdouble_t;
@@ -1341,42 +1341,42 @@
 struct __pyx_obj_8pyseobnr_3eob_5utils_10containers_FluxParams;
 struct __pyx_obj_8pyseobnr_3eob_5utils_10containers_EOBParams;
 struct __pyx_array_obj;
 struct __pyx_MemviewEnum_obj;
 struct __pyx_memoryview_obj;
 struct __pyx_memoryviewslice_obj;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":728
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":728
  * ctypedef npy_longdouble longdouble_t
  * 
  * ctypedef npy_cfloat      cfloat_t             # <<<<<<<<<<<<<<
  * ctypedef npy_cdouble     cdouble_t
  * ctypedef npy_clongdouble clongdouble_t
  */
 typedef npy_cfloat __pyx_t_5numpy_cfloat_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":729
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":729
  * 
  * ctypedef npy_cfloat      cfloat_t
  * ctypedef npy_cdouble     cdouble_t             # <<<<<<<<<<<<<<
  * ctypedef npy_clongdouble clongdouble_t
  * 
  */
 typedef npy_cdouble __pyx_t_5numpy_cdouble_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":730
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":730
  * ctypedef npy_cfloat      cfloat_t
  * ctypedef npy_cdouble     cdouble_t
  * ctypedef npy_clongdouble clongdouble_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_cdouble     complex_t
  */
 typedef npy_clongdouble __pyx_t_5numpy_clongdouble_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":732
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":732
  * ctypedef npy_clongdouble clongdouble_t
  * 
  * ctypedef npy_cdouble     complex_t             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew1(a):
  */
 typedef npy_cdouble __pyx_t_5numpy_complex_t;
@@ -10036,15 +10036,15 @@
   __Pyx_AddTraceback("pyseobnr.eob.utils.containers.EOBParams.__setstate_cython__", __pyx_clineno, __pyx_lineno, __pyx_filename);
   __pyx_r = NULL;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
 
@@ -10053,29 +10053,29 @@
   __Pyx_RefNannyDeclarations
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew1", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":735
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":735
  * 
  * cdef inline object PyArray_MultiIterNew1(a):
  *     return PyArray_MultiIterNew(1, <void*>a)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):
  */
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(1, ((void *)__pyx_v_a)); if (unlikely(!__pyx_t_1)) __PYX_ERR(3, 735, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
 
@@ -10086,15 +10086,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
 
@@ -10103,29 +10103,29 @@
   __Pyx_RefNannyDeclarations
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew2", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":738
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":738
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):
  */
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(2, ((void *)__pyx_v_a), ((void *)__pyx_v_b)); if (unlikely(!__pyx_t_1)) __PYX_ERR(3, 738, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
 
@@ -10136,15 +10136,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
 
@@ -10153,29 +10153,29 @@
   __Pyx_RefNannyDeclarations
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew3", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":741
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":741
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
  */
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(3, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c)); if (unlikely(!__pyx_t_1)) __PYX_ERR(3, 741, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
 
@@ -10186,15 +10186,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
 
@@ -10203,29 +10203,29 @@
   __Pyx_RefNannyDeclarations
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew4", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":744
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":744
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
  */
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(4, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d)); if (unlikely(!__pyx_t_1)) __PYX_ERR(3, 744, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
 
@@ -10236,15 +10236,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
 
@@ -10253,29 +10253,29 @@
   __Pyx_RefNannyDeclarations
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew5", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":747
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":747
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)             # <<<<<<<<<<<<<<
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  */
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(5, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d), ((void *)__pyx_v_e)); if (unlikely(!__pyx_t_1)) __PYX_ERR(3, 747, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
 
@@ -10286,212 +10286,212 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
 
 static CYTHON_INLINE PyObject *__pyx_f_5numpy_PyDataType_SHAPE(PyArray_Descr *__pyx_v_d) {
   PyObject *__pyx_r = NULL;
   __Pyx_RefNannyDeclarations
   int __pyx_t_1;
   __Pyx_RefNannySetupContext("PyDataType_SHAPE", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":750
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":750
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
  *         return <tuple>d.subarray.shape
  *     else:
  */
   __pyx_t_1 = (PyDataType_HASSUBARRAY(__pyx_v_d) != 0);
   if (__pyx_t_1) {
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":751
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":751
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape             # <<<<<<<<<<<<<<
  *     else:
  *         return ()
  */
     __Pyx_XDECREF(__pyx_r);
     __Pyx_INCREF(((PyObject*)__pyx_v_d->subarray->shape));
     __pyx_r = ((PyObject*)__pyx_v_d->subarray->shape);
     goto __pyx_L0;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":750
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":750
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
  *         return <tuple>d.subarray.shape
  *     else:
  */
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":753
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":753
  *         return <tuple>d.subarray.shape
  *     else:
  *         return ()             # <<<<<<<<<<<<<<
  * 
  * 
  */
   /*else*/ {
     __Pyx_XDECREF(__pyx_r);
     __Pyx_INCREF(__pyx_empty_tuple);
     __pyx_r = __pyx_empty_tuple;
     goto __pyx_L0;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
 
   /* function exit code */
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
 
 static CYTHON_INLINE void __pyx_f_5numpy_set_array_base(PyArrayObject *__pyx_v_arr, PyObject *__pyx_v_base) {
   __Pyx_RefNannyDeclarations
   __Pyx_RefNannySetupContext("set_array_base", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":929
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":929
  * 
  * cdef inline void set_array_base(ndarray arr, object base):
  *     Py_INCREF(base) # important to do this before stealing the reference below!             # <<<<<<<<<<<<<<
  *     PyArray_SetBaseObject(arr, base)
  * 
  */
   Py_INCREF(__pyx_v_base);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":930
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":930
  * cdef inline void set_array_base(ndarray arr, object base):
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object get_array_base(ndarray arr):
  */
   (void)(PyArray_SetBaseObject(__pyx_v_arr, __pyx_v_base));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
 
   /* function exit code */
   __Pyx_RefNannyFinishContext();
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
 
 static CYTHON_INLINE PyObject *__pyx_f_5numpy_get_array_base(PyArrayObject *__pyx_v_arr) {
   PyObject *__pyx_v_base;
   PyObject *__pyx_r = NULL;
   __Pyx_RefNannyDeclarations
   int __pyx_t_1;
   __Pyx_RefNannySetupContext("get_array_base", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":933
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":933
  * 
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)             # <<<<<<<<<<<<<<
  *     if base is NULL:
  *         return None
  */
   __pyx_v_base = PyArray_BASE(__pyx_v_arr);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":934
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":934
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)
  *     if base is NULL:             # <<<<<<<<<<<<<<
  *         return None
  *     return <object>base
  */
   __pyx_t_1 = ((__pyx_v_base == NULL) != 0);
   if (__pyx_t_1) {
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":935
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":935
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  *         return None             # <<<<<<<<<<<<<<
  *     return <object>base
  * 
  */
     __Pyx_XDECREF(__pyx_r);
     __pyx_r = Py_None; __Pyx_INCREF(Py_None);
     goto __pyx_L0;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":934
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":934
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)
  *     if base is NULL:             # <<<<<<<<<<<<<<
  *         return None
  *     return <object>base
  */
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":936
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":936
  *     if base is NULL:
  *         return None
  *     return <object>base             # <<<<<<<<<<<<<<
  * 
  * # Versions of the import_* functions which are more suitable for
  */
   __Pyx_XDECREF(__pyx_r);
   __Pyx_INCREF(((PyObject *)__pyx_v_base));
   __pyx_r = ((PyObject *)__pyx_v_base);
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
 
   /* function exit code */
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
 
@@ -10507,15 +10507,15 @@
   PyObject *__pyx_t_7 = NULL;
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_array", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
   {
@@ -10523,53 +10523,53 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":942
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":942
  * cdef inline int import_array() except -1:
  *     try:
  *         __pyx_import_array()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")
  */
       __pyx_t_4 = _import_array(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(3, 942, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":943
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":943
  *     try:
  *         __pyx_import_array()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  */
     __pyx_t_4 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_array", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(3, 943, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":944
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":944
  *         __pyx_import_array()
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_umath() except -1:
  */
       __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_ImportError, __pyx_tuple__16, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(3, 944, __pyx_L5_except_error)
@@ -10577,30 +10577,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(3, 944, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
 
@@ -10615,15 +10615,15 @@
   __Pyx_AddTraceback("numpy.import_array", __pyx_clineno, __pyx_lineno, __pyx_filename);
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -10639,15 +10639,15 @@
   PyObject *__pyx_t_7 = NULL;
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_umath", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
   {
@@ -10655,53 +10655,53 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":948
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":948
  * cdef inline int import_umath() except -1:
  *     try:
  *         _import_umath()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")
  */
       __pyx_t_4 = _import_umath(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(3, 948, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":949
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":949
  *     try:
  *         _import_umath()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  */
     __pyx_t_4 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_umath", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(3, 949, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":950
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":950
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_ufunc() except -1:
  */
       __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_ImportError, __pyx_tuple__17, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(3, 950, __pyx_L5_except_error)
@@ -10709,30 +10709,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(3, 950, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -10747,15 +10747,15 @@
   __Pyx_AddTraceback("numpy.import_umath", __pyx_clineno, __pyx_lineno, __pyx_filename);
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -10771,15 +10771,15 @@
   PyObject *__pyx_t_7 = NULL;
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_ufunc", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
   {
@@ -10787,53 +10787,53 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":954
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":954
  * cdef inline int import_ufunc() except -1:
  *     try:
  *         _import_umath()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")
  */
       __pyx_t_4 = _import_umath(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(3, 954, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":955
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":955
  *     try:
  *         _import_umath()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  */
     __pyx_t_4 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_ufunc", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(3, 955, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":956
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":956
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef extern from *:
  */
       __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_ImportError, __pyx_tuple__17, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(3, 956, __pyx_L5_except_error)
@@ -10841,30 +10841,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(3, 956, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -10879,176 +10879,176 @@
   __Pyx_AddTraceback("numpy.import_ufunc", __pyx_clineno, __pyx_lineno, __pyx_filename);
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
 
 static CYTHON_INLINE int __pyx_f_5numpy_is_timedelta64_object(PyObject *__pyx_v_obj) {
   int __pyx_r;
   __Pyx_RefNannyDeclarations
   __Pyx_RefNannySetupContext("is_timedelta64_object", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":978
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":978
  *     bool
  *     """
  *     return PyObject_TypeCheck(obj, &PyTimedeltaArrType_Type)             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyTimedeltaArrType_Type));
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
 
   /* function exit code */
   __pyx_L0:;
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
 
 static CYTHON_INLINE int __pyx_f_5numpy_is_datetime64_object(PyObject *__pyx_v_obj) {
   int __pyx_r;
   __Pyx_RefNannyDeclarations
   __Pyx_RefNannySetupContext("is_datetime64_object", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":993
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":993
  *     bool
  *     """
  *     return PyObject_TypeCheck(obj, &PyDatetimeArrType_Type)             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyDatetimeArrType_Type));
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
 
   /* function exit code */
   __pyx_L0:;
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
 
 static CYTHON_INLINE npy_datetime __pyx_f_5numpy_get_datetime64_value(PyObject *__pyx_v_obj) {
   npy_datetime __pyx_r;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1003
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1003
  *     also needed.  That can be found using `get_datetime64_unit`.
  *     """
  *     return (<PyDatetimeScalarObject*>obj).obval             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __pyx_r = ((PyDatetimeScalarObject *)__pyx_v_obj)->obval;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
 
   /* function exit code */
   __pyx_L0:;
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
 
 static CYTHON_INLINE npy_timedelta __pyx_f_5numpy_get_timedelta64_value(PyObject *__pyx_v_obj) {
   npy_timedelta __pyx_r;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1010
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1010
  *     returns the int64 value underlying scalar numpy timedelta64 object
  *     """
  *     return (<PyTimedeltaScalarObject*>obj).obval             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __pyx_r = ((PyTimedeltaScalarObject *)__pyx_v_obj)->obval;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
 
   /* function exit code */
   __pyx_L0:;
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
 
 static CYTHON_INLINE NPY_DATETIMEUNIT __pyx_f_5numpy_get_datetime64_unit(PyObject *__pyx_v_obj) {
   NPY_DATETIMEUNIT __pyx_r;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1017
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1017
  *     returns the unit part of the dtype for a numpy datetime64 object.
  *     """
  *     return <NPY_DATETIMEUNIT>(<PyDatetimeScalarObject*>obj).obmeta.base             # <<<<<<<<<<<<<<
  */
   __pyx_r = ((NPY_DATETIMEUNIT)((PyDatetimeScalarObject *)__pyx_v_obj)->obmeta.base);
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
 
@@ -26577,26 +26577,26 @@
  * def __setstate_cython__(self, __pyx_state):
  *     raise TypeError("no default __reduce__ due to non-trivial __cinit__")             # <<<<<<<<<<<<<<
  */
   __pyx_tuple__15 = PyTuple_Pack(1, __pyx_kp_s_no_default___reduce___due_to_non); if (unlikely(!__pyx_tuple__15)) __PYX_ERR(0, 4, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_tuple__15);
   __Pyx_GIVEREF(__pyx_tuple__15);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":944
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":944
  *         __pyx_import_array()
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_umath() except -1:
  */
   __pyx_tuple__16 = PyTuple_Pack(1, __pyx_kp_u_numpy_core_multiarray_failed_to); if (unlikely(!__pyx_tuple__16)) __PYX_ERR(3, 944, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_tuple__16);
   __Pyx_GIVEREF(__pyx_tuple__16);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":950
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":950
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_ufunc() except -1:
  */
   __pyx_tuple__17 = PyTuple_Pack(1, __pyx_kp_u_numpy_core_umath_failed_to_impor); if (unlikely(!__pyx_tuple__17)) __PYX_ERR(3, 950, __pyx_L1_error)
```

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/utils/containers.pxd` & `pyseobnr-0.2.1/pyseobnr/eob/utils/containers.pxd`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/utils/containers.pyx` & `pyseobnr-0.2.1/pyseobnr/eob/utils/containers.pyx`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/utils/math_ops_opt.py` & `pyseobnr-0.2.1/pyseobnr/eob/utils/math_ops_opt.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/utils/utils_precession_opt.py` & `pyseobnr-0.2.1/pyseobnr/eob/utils/utils_precession_opt.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/utils/waveform_ops.py` & `pyseobnr-0.2.1/pyseobnr/eob/utils/waveform_ops.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/waveform/compute_MR.py` & `pyseobnr-0.2.1/pyseobnr/eob/waveform/compute_MR.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/waveform/compute_hlms.py` & `pyseobnr-0.2.1/pyseobnr/eob/waveform/compute_hlms.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/waveform/waveform.c` & `pyseobnr-0.2.1/pyseobnr/eob/waveform/waveform.c`

 * *Files 1% similar despite different names*

```diff
@@ -1,27 +1,27 @@
 /* Generated by Cython 0.29.34 */
 
 /* BEGIN: Cython Metadata
 {
     "distutils": {
         "depends": [
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/arrayobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/arrayscalars.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ndarrayobject.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ndarraytypes.h",
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include/numpy/ufuncobject.h",
             "pyseobnr/eob/utils/eob_parameters.h"
         ],
         "extra_compile_args": [
             "-O3"
         ],
         "include_dirs": [
             "pyseobnr/eob/utils",
             "./pyseobnr/eob/utils",
-            "/local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/core/include"
+            "/local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/core/include"
         ],
         "name": "pyseobnr.eob.waveform.waveform",
         "sources": [
             "pyseobnr/eob/waveform/waveform.pyx"
         ]
     },
     "module_name": "pyseobnr.eob.waveform.waveform"
@@ -1141,195 +1141,195 @@
  * ctypedef float s
  * ctypedef double d             # <<<<<<<<<<<<<<
  * ctypedef float complex c
  * ctypedef double complex z
  */
 typedef double __pyx_t_5scipy_6linalg_11cython_blas_d;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":689
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":689
  * # in Cython to enable them only on the right systems.
  * 
  * ctypedef npy_int8       int8_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t
  */
 typedef npy_int8 __pyx_t_5numpy_int8_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":690
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":690
  * 
  * ctypedef npy_int8       int8_t
  * ctypedef npy_int16      int16_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int32      int32_t
  * ctypedef npy_int64      int64_t
  */
 typedef npy_int16 __pyx_t_5numpy_int16_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":691
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":691
  * ctypedef npy_int8       int8_t
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_int64      int64_t
  * #ctypedef npy_int96      int96_t
  */
 typedef npy_int32 __pyx_t_5numpy_int32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":692
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":692
  * ctypedef npy_int16      int16_t
  * ctypedef npy_int32      int32_t
  * ctypedef npy_int64      int64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_int96      int96_t
  * #ctypedef npy_int128     int128_t
  */
 typedef npy_int64 __pyx_t_5numpy_int64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":696
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":696
  * #ctypedef npy_int128     int128_t
  * 
  * ctypedef npy_uint8      uint8_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t
  */
 typedef npy_uint8 __pyx_t_5numpy_uint8_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":697
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":697
  * 
  * ctypedef npy_uint8      uint8_t
  * ctypedef npy_uint16     uint16_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint32     uint32_t
  * ctypedef npy_uint64     uint64_t
  */
 typedef npy_uint16 __pyx_t_5numpy_uint16_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":698
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":698
  * ctypedef npy_uint8      uint8_t
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uint64     uint64_t
  * #ctypedef npy_uint96     uint96_t
  */
 typedef npy_uint32 __pyx_t_5numpy_uint32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":699
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":699
  * ctypedef npy_uint16     uint16_t
  * ctypedef npy_uint32     uint32_t
  * ctypedef npy_uint64     uint64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_uint96     uint96_t
  * #ctypedef npy_uint128    uint128_t
  */
 typedef npy_uint64 __pyx_t_5numpy_uint64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":703
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":703
  * #ctypedef npy_uint128    uint128_t
  * 
  * ctypedef npy_float32    float32_t             # <<<<<<<<<<<<<<
  * ctypedef npy_float64    float64_t
  * #ctypedef npy_float80    float80_t
  */
 typedef npy_float32 __pyx_t_5numpy_float32_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":704
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":704
  * 
  * ctypedef npy_float32    float32_t
  * ctypedef npy_float64    float64_t             # <<<<<<<<<<<<<<
  * #ctypedef npy_float80    float80_t
  * #ctypedef npy_float128   float128_t
  */
 typedef npy_float64 __pyx_t_5numpy_float64_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":713
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":713
  * # The int types are mapped a bit surprising --
  * # numpy.int corresponds to 'l' and numpy.long to 'q'
  * ctypedef npy_long       int_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longlong   long_t
  * ctypedef npy_longlong   longlong_t
  */
 typedef npy_long __pyx_t_5numpy_int_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":714
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":714
  * # numpy.int corresponds to 'l' and numpy.long to 'q'
  * ctypedef npy_long       int_t
  * ctypedef npy_longlong   long_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longlong   longlong_t
  * 
  */
 typedef npy_longlong __pyx_t_5numpy_long_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":715
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":715
  * ctypedef npy_long       int_t
  * ctypedef npy_longlong   long_t
  * ctypedef npy_longlong   longlong_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_ulong      uint_t
  */
 typedef npy_longlong __pyx_t_5numpy_longlong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":717
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":717
  * ctypedef npy_longlong   longlong_t
  * 
  * ctypedef npy_ulong      uint_t             # <<<<<<<<<<<<<<
  * ctypedef npy_ulonglong  ulong_t
  * ctypedef npy_ulonglong  ulonglong_t
  */
 typedef npy_ulong __pyx_t_5numpy_uint_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":718
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":718
  * 
  * ctypedef npy_ulong      uint_t
  * ctypedef npy_ulonglong  ulong_t             # <<<<<<<<<<<<<<
  * ctypedef npy_ulonglong  ulonglong_t
  * 
  */
 typedef npy_ulonglong __pyx_t_5numpy_ulong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":719
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":719
  * ctypedef npy_ulong      uint_t
  * ctypedef npy_ulonglong  ulong_t
  * ctypedef npy_ulonglong  ulonglong_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_intp       intp_t
  */
 typedef npy_ulonglong __pyx_t_5numpy_ulonglong_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":721
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":721
  * ctypedef npy_ulonglong  ulonglong_t
  * 
  * ctypedef npy_intp       intp_t             # <<<<<<<<<<<<<<
  * ctypedef npy_uintp      uintp_t
  * 
  */
 typedef npy_intp __pyx_t_5numpy_intp_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":722
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":722
  * 
  * ctypedef npy_intp       intp_t
  * ctypedef npy_uintp      uintp_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_double     float_t
  */
 typedef npy_uintp __pyx_t_5numpy_uintp_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":724
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":724
  * ctypedef npy_uintp      uintp_t
  * 
  * ctypedef npy_double     float_t             # <<<<<<<<<<<<<<
  * ctypedef npy_double     double_t
  * ctypedef npy_longdouble longdouble_t
  */
 typedef npy_double __pyx_t_5numpy_float_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":725
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":725
  * 
  * ctypedef npy_double     float_t
  * ctypedef npy_double     double_t             # <<<<<<<<<<<<<<
  * ctypedef npy_longdouble longdouble_t
  * 
  */
 typedef npy_double __pyx_t_5numpy_double_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":726
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":726
  * ctypedef npy_double     float_t
  * ctypedef npy_double     double_t
  * ctypedef npy_longdouble longdouble_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_cfloat      cfloat_t
  */
 typedef npy_longdouble __pyx_t_5numpy_longdouble_t;
@@ -1448,42 +1448,42 @@
   int derivative;
 };
 struct __pyx_fuse_1__pyx_opt_args_5scipy_7special_14cython_special_spherical_kn {
   int __pyx_n;
   int derivative;
 };
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":728
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":728
  * ctypedef npy_longdouble longdouble_t
  * 
  * ctypedef npy_cfloat      cfloat_t             # <<<<<<<<<<<<<<
  * ctypedef npy_cdouble     cdouble_t
  * ctypedef npy_clongdouble clongdouble_t
  */
 typedef npy_cfloat __pyx_t_5numpy_cfloat_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":729
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":729
  * 
  * ctypedef npy_cfloat      cfloat_t
  * ctypedef npy_cdouble     cdouble_t             # <<<<<<<<<<<<<<
  * ctypedef npy_clongdouble clongdouble_t
  * 
  */
 typedef npy_cdouble __pyx_t_5numpy_cdouble_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":730
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":730
  * ctypedef npy_cfloat      cfloat_t
  * ctypedef npy_cdouble     cdouble_t
  * ctypedef npy_clongdouble clongdouble_t             # <<<<<<<<<<<<<<
  * 
  * ctypedef npy_cdouble     complex_t
  */
 typedef npy_clongdouble __pyx_t_5numpy_clongdouble_t;
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":732
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":732
  * ctypedef npy_clongdouble clongdouble_t
  * 
  * ctypedef npy_cdouble     complex_t             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew1(a):
  */
 typedef npy_cdouble __pyx_t_5numpy_complex_t;
@@ -16270,15 +16270,15 @@
   __PYX_XDEC_MEMVIEW(&__pyx_v_result, 1);
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_TraceReturn(__pyx_r, 0);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
 
@@ -16287,29 +16287,29 @@
   __Pyx_RefNannyDeclarations
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew1", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":735
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":735
  * 
  * cdef inline object PyArray_MultiIterNew1(a):
  *     return PyArray_MultiIterNew(1, <void*>a)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):
  */
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(1, ((void *)__pyx_v_a)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 735, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":734
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":734
  * ctypedef npy_cdouble     complex_t
  * 
  * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  */
 
@@ -16320,15 +16320,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
 
@@ -16337,29 +16337,29 @@
   __Pyx_RefNannyDeclarations
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew2", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":738
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":738
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):
  */
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(2, ((void *)__pyx_v_a), ((void *)__pyx_v_b)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 738, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":737
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":737
  *     return PyArray_MultiIterNew(1, <void*>a)
  * 
  * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  */
 
@@ -16370,15 +16370,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
 
@@ -16387,29 +16387,29 @@
   __Pyx_RefNannyDeclarations
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew3", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":741
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":741
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
  */
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(3, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 741, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":740
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":740
  *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
  * 
  * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  */
 
@@ -16420,15 +16420,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
 
@@ -16437,29 +16437,29 @@
   __Pyx_RefNannyDeclarations
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew4", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":744
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":744
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
  */
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(4, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 744, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":743
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":743
  *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
  * 
  * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  */
 
@@ -16470,15 +16470,15 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
 
@@ -16487,29 +16487,29 @@
   __Pyx_RefNannyDeclarations
   PyObject *__pyx_t_1 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("PyArray_MultiIterNew5", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":747
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":747
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)             # <<<<<<<<<<<<<<
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  */
   __Pyx_XDECREF(__pyx_r);
   __pyx_t_1 = PyArray_MultiIterNew(5, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d), ((void *)__pyx_v_e)); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 747, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_t_1);
   __pyx_r = __pyx_t_1;
   __pyx_t_1 = 0;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":746
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":746
  *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
  * 
  * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  */
 
@@ -16520,212 +16520,212 @@
   __pyx_r = 0;
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
 
 static CYTHON_INLINE PyObject *__pyx_f_5numpy_PyDataType_SHAPE(PyArray_Descr *__pyx_v_d) {
   PyObject *__pyx_r = NULL;
   __Pyx_RefNannyDeclarations
   int __pyx_t_1;
   __Pyx_RefNannySetupContext("PyDataType_SHAPE", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":750
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":750
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
  *         return <tuple>d.subarray.shape
  *     else:
  */
   __pyx_t_1 = (PyDataType_HASSUBARRAY(__pyx_v_d) != 0);
   if (__pyx_t_1) {
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":751
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":751
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape             # <<<<<<<<<<<<<<
  *     else:
  *         return ()
  */
     __Pyx_XDECREF(__pyx_r);
     __Pyx_INCREF(((PyObject*)__pyx_v_d->subarray->shape));
     __pyx_r = ((PyObject*)__pyx_v_d->subarray->shape);
     goto __pyx_L0;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":750
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":750
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):
  *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
  *         return <tuple>d.subarray.shape
  *     else:
  */
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":753
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":753
  *         return <tuple>d.subarray.shape
  *     else:
  *         return ()             # <<<<<<<<<<<<<<
  * 
  * 
  */
   /*else*/ {
     __Pyx_XDECREF(__pyx_r);
     __Pyx_INCREF(__pyx_empty_tuple);
     __pyx_r = __pyx_empty_tuple;
     goto __pyx_L0;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":749
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":749
  *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
  * 
  * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
  *     if PyDataType_HASSUBARRAY(d):
  *         return <tuple>d.subarray.shape
  */
 
   /* function exit code */
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
 
 static CYTHON_INLINE void __pyx_f_5numpy_set_array_base(PyArrayObject *__pyx_v_arr, PyObject *__pyx_v_base) {
   __Pyx_RefNannyDeclarations
   __Pyx_RefNannySetupContext("set_array_base", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":929
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":929
  * 
  * cdef inline void set_array_base(ndarray arr, object base):
  *     Py_INCREF(base) # important to do this before stealing the reference below!             # <<<<<<<<<<<<<<
  *     PyArray_SetBaseObject(arr, base)
  * 
  */
   Py_INCREF(__pyx_v_base);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":930
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":930
  * cdef inline void set_array_base(ndarray arr, object base):
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)             # <<<<<<<<<<<<<<
  * 
  * cdef inline object get_array_base(ndarray arr):
  */
   (void)(PyArray_SetBaseObject(__pyx_v_arr, __pyx_v_base));
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":928
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":928
  *     int _import_umath() except -1
  * 
  * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
  *     Py_INCREF(base) # important to do this before stealing the reference below!
  *     PyArray_SetBaseObject(arr, base)
  */
 
   /* function exit code */
   __Pyx_RefNannyFinishContext();
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
 
 static CYTHON_INLINE PyObject *__pyx_f_5numpy_get_array_base(PyArrayObject *__pyx_v_arr) {
   PyObject *__pyx_v_base;
   PyObject *__pyx_r = NULL;
   __Pyx_RefNannyDeclarations
   int __pyx_t_1;
   __Pyx_RefNannySetupContext("get_array_base", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":933
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":933
  * 
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)             # <<<<<<<<<<<<<<
  *     if base is NULL:
  *         return None
  */
   __pyx_v_base = PyArray_BASE(__pyx_v_arr);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":934
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":934
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)
  *     if base is NULL:             # <<<<<<<<<<<<<<
  *         return None
  *     return <object>base
  */
   __pyx_t_1 = ((__pyx_v_base == NULL) != 0);
   if (__pyx_t_1) {
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":935
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":935
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  *         return None             # <<<<<<<<<<<<<<
  *     return <object>base
  * 
  */
     __Pyx_XDECREF(__pyx_r);
     __pyx_r = Py_None; __Pyx_INCREF(Py_None);
     goto __pyx_L0;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":934
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":934
  * cdef inline object get_array_base(ndarray arr):
  *     base = PyArray_BASE(arr)
  *     if base is NULL:             # <<<<<<<<<<<<<<
  *         return None
  *     return <object>base
  */
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":936
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":936
  *     if base is NULL:
  *         return None
  *     return <object>base             # <<<<<<<<<<<<<<
  * 
  * # Versions of the import_* functions which are more suitable for
  */
   __Pyx_XDECREF(__pyx_r);
   __Pyx_INCREF(((PyObject *)__pyx_v_base));
   __pyx_r = ((PyObject *)__pyx_v_base);
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":932
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":932
  *     PyArray_SetBaseObject(arr, base)
  * 
  * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
  *     base = PyArray_BASE(arr)
  *     if base is NULL:
  */
 
   /* function exit code */
   __pyx_L0:;
   __Pyx_XGIVEREF(__pyx_r);
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
 
@@ -16741,15 +16741,15 @@
   PyObject *__pyx_t_7 = NULL;
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_array", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
   {
@@ -16757,53 +16757,53 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":942
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":942
  * cdef inline int import_array() except -1:
  *     try:
  *         __pyx_import_array()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")
  */
       __pyx_t_4 = _import_array(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(2, 942, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":943
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":943
  *     try:
  *         __pyx_import_array()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  */
     __pyx_t_4 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_array", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(2, 943, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":944
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":944
  *         __pyx_import_array()
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_umath() except -1:
  */
       __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_ImportError, __pyx_tuple__7, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(2, 944, __pyx_L5_except_error)
@@ -16811,30 +16811,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(2, 944, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":941
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":941
  * # Cython code.
  * cdef inline int import_array() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         __pyx_import_array()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":940
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":940
  * # Versions of the import_* functions which are more suitable for
  * # Cython code.
  * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         __pyx_import_array()
  */
 
@@ -16849,15 +16849,15 @@
   __Pyx_AddTraceback("numpy.import_array", __pyx_clineno, __pyx_lineno, __pyx_filename);
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -16873,15 +16873,15 @@
   PyObject *__pyx_t_7 = NULL;
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_umath", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
   {
@@ -16889,53 +16889,53 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":948
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":948
  * cdef inline int import_umath() except -1:
  *     try:
  *         _import_umath()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")
  */
       __pyx_t_4 = _import_umath(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(2, 948, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":949
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":949
  *     try:
  *         _import_umath()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  */
     __pyx_t_4 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_umath", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(2, 949, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":950
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":950
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_ufunc() except -1:
  */
       __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_ImportError, __pyx_tuple__8, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(2, 950, __pyx_L5_except_error)
@@ -16943,30 +16943,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(2, 950, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":947
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":947
  * 
  * cdef inline int import_umath() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":946
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":946
  *         raise ImportError("numpy.core.multiarray failed to import")
  * 
  * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -16981,15 +16981,15 @@
   __Pyx_AddTraceback("numpy.import_umath", __pyx_clineno, __pyx_lineno, __pyx_filename);
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -17005,15 +17005,15 @@
   PyObject *__pyx_t_7 = NULL;
   PyObject *__pyx_t_8 = NULL;
   int __pyx_lineno = 0;
   const char *__pyx_filename = NULL;
   int __pyx_clineno = 0;
   __Pyx_RefNannySetupContext("import_ufunc", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
   {
@@ -17021,53 +17021,53 @@
     __Pyx_PyThreadState_assign
     __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
     __Pyx_XGOTREF(__pyx_t_1);
     __Pyx_XGOTREF(__pyx_t_2);
     __Pyx_XGOTREF(__pyx_t_3);
     /*try:*/ {
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":954
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":954
  * cdef inline int import_ufunc() except -1:
  *     try:
  *         _import_umath()             # <<<<<<<<<<<<<<
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")
  */
       __pyx_t_4 = _import_umath(); if (unlikely(__pyx_t_4 == ((int)-1))) __PYX_ERR(2, 954, __pyx_L3_error)
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     }
     __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
     __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
     __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
     goto __pyx_L8_try_end;
     __pyx_L3_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":955
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":955
  *     try:
  *         _import_umath()
  *     except Exception:             # <<<<<<<<<<<<<<
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  */
     __pyx_t_4 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
     if (__pyx_t_4) {
       __Pyx_AddTraceback("numpy.import_ufunc", __pyx_clineno, __pyx_lineno, __pyx_filename);
       if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(2, 955, __pyx_L5_except_error)
       __Pyx_GOTREF(__pyx_t_5);
       __Pyx_GOTREF(__pyx_t_6);
       __Pyx_GOTREF(__pyx_t_7);
 
-      /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":956
+      /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":956
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef extern from *:
  */
       __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_ImportError, __pyx_tuple__8, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(2, 956, __pyx_L5_except_error)
@@ -17075,30 +17075,30 @@
       __Pyx_Raise(__pyx_t_8, 0, 0, 0);
       __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
       __PYX_ERR(2, 956, __pyx_L5_except_error)
     }
     goto __pyx_L5_except_error;
     __pyx_L5_except_error:;
 
-    /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":953
+    /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":953
  * 
  * cdef inline int import_ufunc() except -1:
  *     try:             # <<<<<<<<<<<<<<
  *         _import_umath()
  *     except Exception:
  */
     __Pyx_XGIVEREF(__pyx_t_1);
     __Pyx_XGIVEREF(__pyx_t_2);
     __Pyx_XGIVEREF(__pyx_t_3);
     __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
     goto __pyx_L1_error;
     __pyx_L8_try_end:;
   }
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":952
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":952
  *         raise ImportError("numpy.core.umath failed to import")
  * 
  * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
  *     try:
  *         _import_umath()
  */
 
@@ -17113,176 +17113,176 @@
   __Pyx_AddTraceback("numpy.import_ufunc", __pyx_clineno, __pyx_lineno, __pyx_filename);
   __pyx_r = -1;
   __pyx_L0:;
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
 
 static CYTHON_INLINE int __pyx_f_5numpy_is_timedelta64_object(PyObject *__pyx_v_obj) {
   int __pyx_r;
   __Pyx_RefNannyDeclarations
   __Pyx_RefNannySetupContext("is_timedelta64_object", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":978
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":978
  *     bool
  *     """
  *     return PyObject_TypeCheck(obj, &PyTimedeltaArrType_Type)             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyTimedeltaArrType_Type));
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":966
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":966
  * 
  * 
  * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.timedelta64)`
  */
 
   /* function exit code */
   __pyx_L0:;
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
 
 static CYTHON_INLINE int __pyx_f_5numpy_is_datetime64_object(PyObject *__pyx_v_obj) {
   int __pyx_r;
   __Pyx_RefNannyDeclarations
   __Pyx_RefNannySetupContext("is_datetime64_object", 0);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":993
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":993
  *     bool
  *     """
  *     return PyObject_TypeCheck(obj, &PyDatetimeArrType_Type)             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyDatetimeArrType_Type));
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":981
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":981
  * 
  * 
  * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
  *     """
  *     Cython equivalent of `isinstance(obj, np.datetime64)`
  */
 
   /* function exit code */
   __pyx_L0:;
   __Pyx_RefNannyFinishContext();
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
 
 static CYTHON_INLINE npy_datetime __pyx_f_5numpy_get_datetime64_value(PyObject *__pyx_v_obj) {
   npy_datetime __pyx_r;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1003
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1003
  *     also needed.  That can be found using `get_datetime64_unit`.
  *     """
  *     return (<PyDatetimeScalarObject*>obj).obval             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __pyx_r = ((PyDatetimeScalarObject *)__pyx_v_obj)->obval;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":996
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":996
  * 
  * 
  * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy datetime64 object
  */
 
   /* function exit code */
   __pyx_L0:;
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
 
 static CYTHON_INLINE npy_timedelta __pyx_f_5numpy_get_timedelta64_value(PyObject *__pyx_v_obj) {
   npy_timedelta __pyx_r;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1010
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1010
  *     returns the int64 value underlying scalar numpy timedelta64 object
  *     """
  *     return (<PyTimedeltaScalarObject*>obj).obval             # <<<<<<<<<<<<<<
  * 
  * 
  */
   __pyx_r = ((PyTimedeltaScalarObject *)__pyx_v_obj)->obval;
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1006
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1006
  * 
  * 
  * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the int64 value underlying scalar numpy timedelta64 object
  */
 
   /* function exit code */
   __pyx_L0:;
   return __pyx_r;
 }
 
-/* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+/* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
 
 static CYTHON_INLINE NPY_DATETIMEUNIT __pyx_f_5numpy_get_datetime64_unit(PyObject *__pyx_v_obj) {
   NPY_DATETIMEUNIT __pyx_r;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1017
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1017
  *     returns the unit part of the dtype for a numpy datetime64 object.
  *     """
  *     return <NPY_DATETIMEUNIT>(<PyDatetimeScalarObject*>obj).obmeta.base             # <<<<<<<<<<<<<<
  */
   __pyx_r = ((NPY_DATETIMEUNIT)((PyDatetimeScalarObject *)__pyx_v_obj)->obmeta.base);
   goto __pyx_L0;
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":1013
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":1013
  * 
  * 
  * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
  *     """
  *     returns the unit part of the dtype for a numpy datetime64 object.
  */
 
@@ -31971,26 +31971,26 @@
  * 
  *         # when the amplitude at merger is too small a positive sign is better
  */
   __pyx_tuple__6 = PyTuple_Pack(2, __pyx_int_2, __pyx_int_2); if (unlikely(!__pyx_tuple__6)) __PYX_ERR(0, 2380, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_tuple__6);
   __Pyx_GIVEREF(__pyx_tuple__6);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":944
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":944
  *         __pyx_import_array()
  *     except Exception:
  *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_umath() except -1:
  */
   __pyx_tuple__7 = PyTuple_Pack(1, __pyx_kp_u_numpy_core_multiarray_failed_to); if (unlikely(!__pyx_tuple__7)) __PYX_ERR(2, 944, __pyx_L1_error)
   __Pyx_GOTREF(__pyx_tuple__7);
   __Pyx_GIVEREF(__pyx_tuple__7);
 
-  /* "../../../../local/tmp/sossokine/build-env-x4kh4ujn/lib/python3.9/site-packages/numpy/__init__.pxd":950
+  /* "../../../../local/tmp/sossokine/build-env-97bjv28w/lib/python3.9/site-packages/numpy/__init__.pxd":950
  *         _import_umath()
  *     except Exception:
  *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
  * 
  * cdef inline int import_ufunc() except -1:
  */
   __pyx_tuple__8 = PyTuple_Pack(1, __pyx_kp_u_numpy_core_umath_failed_to_impor); if (unlikely(!__pyx_tuple__8)) __PYX_ERR(2, 950, __pyx_L1_error)
```

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/waveform/waveform.pxd` & `pyseobnr-0.2.1/pyseobnr/eob/waveform/waveform.pxd`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/eob/waveform/waveform.pyx` & `pyseobnr-0.2.1/pyseobnr/eob/waveform/waveform.pyx`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/generate_waveform.py` & `pyseobnr-0.2.1/pyseobnr/generate_waveform.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr/models/SEOBNRv5HM.py` & `pyseobnr-0.2.1/pyseobnr/models/SEOBNRv5HM.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/pyseobnr.egg-info/PKG-INFO` & `pyseobnr-0.2.1/pyseobnr.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyseobnr
-Version: 0.2.0
+Version: 0.2.1
 Summary: Gravitational wave modelling within the effective-one-body framework
 Author-email: Serguei Ossokine <serguei.ossokine@tutanota.com>, Lorenzo Pompili <lorenzo.pompili@ligo.org>, Deyan Mihaylov <deyan.mihaylov@ligo.org>, Antoni Ramos Buades <antoni.ramos-buades@ligo.org>, Michael Puerrer <michael.puerrer@ligo.org>, Hector Estelles <hector.estelles@ligo.org>
 License: GPL-3.0-or-later
 Requires-Python: >=3.8
 Description-Content-Type: text/x-rst
 Provides-Extra: checks
 Provides-Extra: docs
```

### Comparing `pyseobnr-0.2.0/pyseobnr.egg-info/SOURCES.txt` & `pyseobnr-0.2.1/pyseobnr.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/setup.py` & `pyseobnr-0.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/test/regression_tests/regenerate_SEOBNRv5HM.py` & `pyseobnr-0.2.1/test/regression_tests/regenerate_SEOBNRv5HM.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/test/regression_tests/regenerate_SEOBNRv5PHM.py` & `pyseobnr-0.2.1/test/regression_tests/regenerate_SEOBNRv5PHM.py`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/test/regression_tests/template_v5HM_tests.jinja` & `pyseobnr-0.2.1/test/regression_tests/template_v5HM_tests.jinja`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/test/regression_tests/template_v5PHM_tests.jinja` & `pyseobnr-0.2.1/test/regression_tests/template_v5PHM_tests.jinja`

 * *Files identical despite different names*

### Comparing `pyseobnr-0.2.0/test/regression_tests/test_SEOBNRv5HM.py` & `pyseobnr-0.2.1/test/regression_tests/test_SEOBNRv5HM.py`

 * *Files 1% similar despite different names*

```diff
@@ -140,9 +140,9 @@
     expected_result = np.array(
 	[8.576872303281181e-20,3.558536004410046e+04,6.901107038290343e-20,
  3.730612207787991e+04]
     )
 
     new_result = np.array(gen_test_data("FD"))
     np.testing.assert_allclose(
-        new_result, expected_result, rtol=2.2e-4, err_msg="SEOBNRv5HM FD test failed"
-    )
+        new_result, expected_result, rtol=4.5e-4, err_msg="SEOBNRv5HM FD test failed"
+    )
```

### Comparing `pyseobnr-0.2.0/test/regression_tests/test_SEOBNRv5PHM.py` & `pyseobnr-0.2.1/test/regression_tests/test_SEOBNRv5PHM.py`

 * *Files 1% similar despite different names*

```diff
@@ -119,15 +119,15 @@
 
     """
 
     expected_result = np.array([9.286455953988354e-18,8.842800671532437e-18])
 
     new_result = np.array(gen_test_data("TD"))
     np.testing.assert_allclose(
-        new_result, expected_result, rtol=1e-4, err_msg="SEOBNRv5HM TD test failed"
+        new_result, expected_result, rtol=1e-4, err_msg="SEOBNRv5PHM TD test failed"
     )
 
 
 def test_SEOBNRv5PHM_diff_FD():
     """
     This test checks that SEOBNRv5HM hasn't changed in frequency domain.
     It does this by generating two SEOBNRv5HM waveforms and computing
@@ -143,9 +143,9 @@
     expected_result = np.array(
 	[9.652274107044372e-20,3.391378195301547e+04,8.605764565737375e-20,
  3.440922572212310e+04]
     )
 
     new_result = np.array(gen_test_data("FD"))
     np.testing.assert_allclose(
-        new_result, expected_result, rtol=2.0e-4, err_msg="SEOBNRv5HM FD test failed"
-    )
+        new_result, expected_result, rtol=4.5e-4, err_msg="SEOBNRv5PHM FD test failed"
+    )
```

