# Comparing `tmp/liionpack-0.3.4.tar.gz` & `tmp/liionpack-0.3.5.tar.gz`

## Comparing `liionpack-0.3.4.tar` & `liionpack-0.3.5.tar`

### file list

```diff
@@ -1,88 +1,89 @@
--rw-r--r--   0        0        0       68 2020-02-02 00:00:00.000000 liionpack-0.3.4/.flake8
--rw-r--r--   0        0        0      270 2020-02-02 00:00:00.000000 liionpack-0.3.4/.readthedocs.yaml
--rw-r--r--   0        0        0     4434 2020-02-02 00:00:00.000000 liionpack-0.3.4/CHANGELOG.md
--rw-r--r--   0        0        0     6883 2020-02-02 00:00:00.000000 liionpack-0.3.4/asv.conf.json
--rw-r--r--   0        0        0      694 2020-02-02 00:00:00.000000 liionpack-0.3.4/environment.yml
--rw-r--r--   0        0        0     1044 2020-02-02 00:00:00.000000 liionpack-0.3.4/mkdocs.yml
--rw-r--r--   0        0        0      388 2020-02-02 00:00:00.000000 liionpack-0.3.4/.github/codecov.yml
--rw-r--r--   0        0        0     1683 2020-02-02 00:00:00.000000 liionpack-0.3.4/.github/ISSUE_TEMPLATE/bug_report.yml
--rw-r--r--   0        0        0      205 2020-02-02 00:00:00.000000 liionpack-0.3.4/.github/ISSUE_TEMPLATE/config.yml
--rw-r--r--   0        0        0      902 2020-02-02 00:00:00.000000 liionpack-0.3.4/.github/ISSUE_TEMPLATE/feature_request.yml
--rw-r--r--   0        0        0     2286 2020-02-02 00:00:00.000000 liionpack-0.3.4/.github/workflows/periodic_benchmarks.yml
--rw-r--r--   0        0        0     1640 2020-02-02 00:00:00.000000 liionpack-0.3.4/.github/workflows/publish_pypi.yml
--rw-r--r--   0        0        0     2986 2020-02-02 00:00:00.000000 liionpack-0.3.4/.github/workflows/run_benchmarks_over_history.yml
--rw-r--r--   0        0        0     3200 2020-02-02 00:00:00.000000 liionpack-0.3.4/.github/workflows/test_on_push.yml
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 liionpack-0.3.4/benchmarks/__init__.py
--rw-r--r--   0        0        0     3555 2020-02-02 00:00:00.000000 liionpack-0.3.4/benchmarks/benchmarks.py
--rw-r--r--   0        0        0      326 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/about.md
--rw-r--r--   0        0        0     5218 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/conduct.md
--rw-r--r--   0        0        0    17673 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/contributing.md
--rw-r--r--   0        0        0      536 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/index.md
--rw-r--r--   0        0        0     2244 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/install.md
--rw-r--r--   0        0        0   203695 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/liionpack.png
--rw-r--r--   0        0        0      730 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/mathjax-config.js
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/reference.md
--rw-r--r--   0        0        0       58 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/requirements.txt
--rw-r--r--   0        0        0   428208 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/examples/01 Getting Started.ipynb
--rw-r--r--   0        0        0   258064 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/examples/02 Using inputs.ipynb
--rw-r--r--   0        0        0   115177 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/examples/03 Experiments.ipynb
--rw-r--r--   0        0        0   320758 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/examples/04 Initial SoC.ipynb
--rw-r--r--   0        0        0   939974 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/examples/05 Drive cycles.ipynb
--rw-r--r--   0        0        0   894028 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/examples/06 Changing a model.ipynb
--rw-r--r--   0        0        0   131502 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/examples/07 Visualizing larger packs.ipynb
--rw-r--r--   0        0        0  1291981 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/examples/08 SEI degradation model.ipynb
--rw-r--r--   0        0        0   322325 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/examples/09 Terminal locations.ipynb
--rw-r--r--   0        0        0       85 2020-02-02 00:00:00.000000 liionpack-0.3.4/docs/stylesheets/extra.css
--rw-r--r--   0        0        0     1355 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/basic_16p2s.py
--rw-r--r--   0        0        0      997 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/big_circuit.py
--rw-r--r--   0        0        0     1506 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/different_initial_soc.py
--rw-r--r--   0        0        0      979 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/draw_circuit.py
--rw-r--r--   0        0        0      526 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/draw_terminals.py
--rw-r--r--   0        0        0      958 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/drive_cycle.py
--rw-r--r--   0        0        0     4027 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/drive_cycle_comparison.py
--rw-r--r--   0        0        0      637 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/load_4p1s.py
--rw-r--r--   0        0        0     1044 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/mixed_terminals.py
--rw-r--r--   0        0        0     1047 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/paper_example.py
--rw-r--r--   0        0        0     1494 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/save_output.py
--rw-r--r--   0        0        0     2217 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/step_external_variable.py
--rw-r--r--   0        0        0     1064 2020-02-02 00:00:00.000000 liionpack-0.3.4/examples/thermal_external.py
--rw-r--r--   0        0        0     1659 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/__init__.py
--rw-r--r--   0        0        0      230 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/definitions.py
--rw-r--r--   0        0        0     2198 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/logger.py
--rw-r--r--   0        0        0    25032 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/netlist_utils.py
--rw-r--r--   0        0        0    11346 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/plots.py
--rw-r--r--   0        0        0     1516 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/protocols.py
--rw-r--r--   0        0        0     2280 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/sim_utils.py
--rw-r--r--   0        0        0     3776 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/simulations.py
--rw-r--r--   0        0        0    15962 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/solver_utils.py
--rw-r--r--   0        0        0    25570 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/solvers.py
--rw-r--r--   0        0        0     5343 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/utils.py
--rw-r--r--   0        0        0     2749 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/circuits/4p1s.asc
--rw-r--r--   0        0        0      936 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/circuits/4p1s.cir
--rw-r--r--   0        0        0      468 2020-02-02 00:00:00.000000 liionpack-0.3.4/liionpack/circuits/4p1s.txt
--rw-r--r--   0        0        0     3521 2020-02-02 00:00:00.000000 liionpack-0.3.4/paper/paper.bib
--rw-r--r--   0        0        0    11210 2020-02-02 00:00:00.000000 liionpack-0.3.4/paper/paper.md
--rw-r--r--   0        0        0   100911 2020-02-02 00:00:00.000000 liionpack-0.3.4/paper/paper_figures/Figure_0.png
--rw-r--r--   0        0        0   113147 2020-02-02 00:00:00.000000 liionpack-0.3.4/paper/paper_figures/Figure_1.png
--rw-r--r--   0        0        0    40455 2020-02-02 00:00:00.000000 liionpack-0.3.4/paper/paper_figures/Figure_2.png
--rw-r--r--   0        0        0    33408 2020-02-02 00:00:00.000000 liionpack-0.3.4/paper/paper_figures/Figure_3.png
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/__init__.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/integration/__init__.py
--rw-r--r--   0        0        0     2430 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/integration/test_1p1s.py
--rw-r--r--   0        0        0     1248 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/integration/test_all_solvers.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/unit/__init__.py
--rw-r--r--   0        0        0     1313 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/unit/test_logger.py
--rw-r--r--   0        0        0     4963 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/unit/test_netlist_utils.py
--rw-r--r--   0        0        0     1629 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/unit/test_notebooks.py
--rw-r--r--   0        0        0     3527 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/unit/test_plots.py
--rw-r--r--   0        0        0     2856 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/unit/test_protocols.py
--rw-r--r--   0        0        0     1424 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/unit/test_sim_utils.py
--rw-r--r--   0        0        0      777 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/unit/test_simulations.py
--rw-r--r--   0        0        0     3570 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/unit/test_solver_utils.py
--rw-r--r--   0        0        0     4817 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/unit/test_solvers.py
--rw-r--r--   0        0        0     2703 2020-02-02 00:00:00.000000 liionpack-0.3.4/tests/unit/test_utils.py
--rw-r--r--   0        0        0     1300 2020-02-02 00:00:00.000000 liionpack-0.3.4/.gitignore
--rw-r--r--   0        0        0     1068 2020-02-02 00:00:00.000000 liionpack-0.3.4/LICENSE
--rw-r--r--   0        0        0     4537 2020-02-02 00:00:00.000000 liionpack-0.3.4/README.md
--rw-r--r--   0        0        0     1359 2020-02-02 00:00:00.000000 liionpack-0.3.4/pyproject.toml
--rw-r--r--   0        0        0     5924 2020-02-02 00:00:00.000000 liionpack-0.3.4/PKG-INFO
+-rw-r--r--   0        0        0       64 2020-02-02 00:00:00.000000 liionpack-0.3.5/.git-blame-ignore-revs
+-rw-r--r--   0        0        0      363 2020-02-02 00:00:00.000000 liionpack-0.3.5/.pre-commit-config.yaml
+-rw-r--r--   0        0        0      270 2020-02-02 00:00:00.000000 liionpack-0.3.5/.readthedocs.yaml
+-rw-r--r--   0        0        0     5307 2020-02-02 00:00:00.000000 liionpack-0.3.5/CHANGELOG.md
+-rw-r--r--   0        0        0     6883 2020-02-02 00:00:00.000000 liionpack-0.3.5/asv.conf.json
+-rw-r--r--   0        0        0      770 2020-02-02 00:00:00.000000 liionpack-0.3.5/environment.yml
+-rw-r--r--   0        0        0     1044 2020-02-02 00:00:00.000000 liionpack-0.3.5/mkdocs.yml
+-rw-r--r--   0        0        0      388 2020-02-02 00:00:00.000000 liionpack-0.3.5/.github/codecov.yml
+-rw-r--r--   0        0        0     1683 2020-02-02 00:00:00.000000 liionpack-0.3.5/.github/ISSUE_TEMPLATE/bug_report.yml
+-rw-r--r--   0        0        0      205 2020-02-02 00:00:00.000000 liionpack-0.3.5/.github/ISSUE_TEMPLATE/config.yml
+-rw-r--r--   0        0        0      902 2020-02-02 00:00:00.000000 liionpack-0.3.5/.github/ISSUE_TEMPLATE/feature_request.yml
+-rw-r--r--   0        0        0     2286 2020-02-02 00:00:00.000000 liionpack-0.3.5/.github/workflows/periodic_benchmarks.yml
+-rw-r--r--   0        0        0     1646 2020-02-02 00:00:00.000000 liionpack-0.3.5/.github/workflows/publish_pypi.yml
+-rw-r--r--   0        0        0     2986 2020-02-02 00:00:00.000000 liionpack-0.3.5/.github/workflows/run_benchmarks_over_history.yml
+-rw-r--r--   0        0        0     1861 2020-02-02 00:00:00.000000 liionpack-0.3.5/.github/workflows/test_on_push.yml
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 liionpack-0.3.5/benchmarks/__init__.py
+-rw-r--r--   0        0        0     3552 2020-02-02 00:00:00.000000 liionpack-0.3.5/benchmarks/benchmarks.py
+-rw-r--r--   0        0        0      326 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/about.md
+-rw-r--r--   0        0        0     5218 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/conduct.md
+-rw-r--r--   0        0        0    18625 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/contributing.md
+-rw-r--r--   0        0        0      536 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/index.md
+-rw-r--r--   0        0        0     2244 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/install.md
+-rw-r--r--   0        0        0   203695 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/liionpack.png
+-rw-r--r--   0        0        0      730 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/mathjax-config.js
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/reference.md
+-rw-r--r--   0        0        0       74 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/requirements.txt
+-rw-r--r--   0        0        0   428208 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/examples/01 Getting Started.ipynb
+-rw-r--r--   0        0        0   258064 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/examples/02 Using inputs.ipynb
+-rw-r--r--   0        0        0   115177 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/examples/03 Experiments.ipynb
+-rw-r--r--   0        0        0   320758 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/examples/04 Initial SoC.ipynb
+-rw-r--r--   0        0        0   939974 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/examples/05 Drive cycles.ipynb
+-rw-r--r--   0        0        0   894028 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/examples/06 Changing a model.ipynb
+-rw-r--r--   0        0        0   131502 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/examples/07 Visualizing larger packs.ipynb
+-rw-r--r--   0        0        0  1291981 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/examples/08 SEI degradation model.ipynb
+-rw-r--r--   0        0        0   322325 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/examples/09 Terminal locations.ipynb
+-rw-r--r--   0        0        0       85 2020-02-02 00:00:00.000000 liionpack-0.3.5/docs/stylesheets/extra.css
+-rw-r--r--   0        0        0     1274 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/basic_16p2s.py
+-rw-r--r--   0        0        0      997 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/big_circuit.py
+-rw-r--r--   0        0        0     1506 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/different_initial_soc.py
+-rw-r--r--   0        0        0      979 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/draw_circuit.py
+-rw-r--r--   0        0        0      526 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/draw_terminals.py
+-rw-r--r--   0        0        0      962 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/drive_cycle.py
+-rw-r--r--   0        0        0     4039 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/drive_cycle_comparison.py
+-rw-r--r--   0        0        0      637 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/load_4p1s.py
+-rw-r--r--   0        0        0     1044 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/mixed_terminals.py
+-rw-r--r--   0        0        0     1027 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/paper_example.py
+-rw-r--r--   0        0        0     1418 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/save_output.py
+-rw-r--r--   0        0        0     2218 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/step_external_variable.py
+-rw-r--r--   0        0        0      980 2020-02-02 00:00:00.000000 liionpack-0.3.5/examples/thermal_external.py
+-rw-r--r--   0        0        0     1659 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/__init__.py
+-rw-r--r--   0        0        0      230 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/definitions.py
+-rw-r--r--   0        0        0     2198 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/logger.py
+-rw-r--r--   0        0        0    25031 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/netlist_utils.py
+-rw-r--r--   0        0        0    11346 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/plots.py
+-rw-r--r--   0        0        0     1496 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/protocols.py
+-rw-r--r--   0        0        0     2280 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/sim_utils.py
+-rw-r--r--   0        0        0     3776 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/simulations.py
+-rw-r--r--   0        0        0    15962 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/solver_utils.py
+-rw-r--r--   0        0        0    18667 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/solvers.py
+-rw-r--r--   0        0        0     5343 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/utils.py
+-rw-r--r--   0        0        0     2749 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/circuits/4p1s.asc
+-rw-r--r--   0        0        0      936 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/circuits/4p1s.cir
+-rw-r--r--   0        0        0      468 2020-02-02 00:00:00.000000 liionpack-0.3.5/liionpack/circuits/4p1s.txt
+-rw-r--r--   0        0        0     3521 2020-02-02 00:00:00.000000 liionpack-0.3.5/paper/paper.bib
+-rw-r--r--   0        0        0    11210 2020-02-02 00:00:00.000000 liionpack-0.3.5/paper/paper.md
+-rw-r--r--   0        0        0   100911 2020-02-02 00:00:00.000000 liionpack-0.3.5/paper/paper_figures/Figure_0.png
+-rw-r--r--   0        0        0   113147 2020-02-02 00:00:00.000000 liionpack-0.3.5/paper/paper_figures/Figure_1.png
+-rw-r--r--   0        0        0    40455 2020-02-02 00:00:00.000000 liionpack-0.3.5/paper/paper_figures/Figure_2.png
+-rw-r--r--   0        0        0    33408 2020-02-02 00:00:00.000000 liionpack-0.3.5/paper/paper_figures/Figure_3.png
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/__init__.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/integration/__init__.py
+-rw-r--r--   0        0        0     2383 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/integration/test_1p1s.py
+-rw-r--r--   0        0        0     1250 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/integration/test_all_solvers.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/unit/__init__.py
+-rw-r--r--   0        0        0     1313 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/unit/test_logger.py
+-rw-r--r--   0        0        0     4963 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/unit/test_netlist_utils.py
+-rw-r--r--   0        0        0     1628 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/unit/test_notebooks.py
+-rw-r--r--   0        0        0     3527 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/unit/test_plots.py
+-rw-r--r--   0        0        0     2856 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/unit/test_protocols.py
+-rw-r--r--   0        0        0     1424 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/unit/test_sim_utils.py
+-rw-r--r--   0        0        0      781 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/unit/test_simulations.py
+-rw-r--r--   0        0        0     3570 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/unit/test_solver_utils.py
+-rw-r--r--   0        0        0     4817 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/unit/test_solvers.py
+-rw-r--r--   0        0        0     2702 2020-02-02 00:00:00.000000 liionpack-0.3.5/tests/unit/test_utils.py
+-rw-r--r--   0        0        0     1300 2020-02-02 00:00:00.000000 liionpack-0.3.5/.gitignore
+-rw-r--r--   0        0        0     1068 2020-02-02 00:00:00.000000 liionpack-0.3.5/LICENSE
+-rw-r--r--   0        0        0     4546 2020-02-02 00:00:00.000000 liionpack-0.3.5/README.md
+-rw-r--r--   0        0        0     1359 2020-02-02 00:00:00.000000 liionpack-0.3.5/pyproject.toml
+-rw-r--r--   0        0        0     5933 2020-02-02 00:00:00.000000 liionpack-0.3.5/PKG-INFO
```

### Comparing `liionpack-0.3.4/CHANGELOG.md` & `liionpack-0.3.5/CHANGELOG.md`

 * *Files 10% similar despite different names*

```diff
@@ -1,25 +1,58 @@
 # [Unreleased](https://github.com/pybamm-team/liionpack/)
 
-# [v0.3.4](https://github.com/pybamm-team/PyBaMM/tree/v0.3.4) - 2023-03-03
+## Features
+
+- ([#PR](link))
+
+## Bug fixes
+
+- ([#PR](link))
+
+## Breaking changes
+
+- ([#PR](link))
+
+# [v0.3.5](https://github.com/pybamm-team/liionpack/) - 2023-04-05
+
+## Features
+
+- Add pre commit and migrate to ruff ([#232](https://github.com/pybamm-team/liionpack/pull/232))
+
+## Bug fixes
+
+- Fix bug in cell currents being out of step ([#245](https://github.com/pybamm-team/liionpack/pull/245))
+- Test only on PyBaMM stable ([#229](https://github.com/pybamm-team/liionpack/pull/229))
+
+## Breaking changes
+
+- Handle change in variable name for next PyBaMM release ([#240](https://github.com/pybamm-team/liionpack/pull/240))
+
+## Chores
+
+- Update pre-commit hooks ([#247](https://github.com/pybamm-team/liionpack/pull/247))
+
+# [v.0.3.4](https://github.com/pybamm-team/liionpack/tree/v.0.3.4) - 2023-03-03
+
+## This version was yanked from PyPi due to an accidental early release that addressed changes coming into PyBaMM in version 23.3.
 
 ## Features
 
 -   Option to specify parallel-strings or series-groups when creating netlist ([#221](https://github.com/pybamm-team/liionpack/pull/221))
 
 ## Bug fixes
 
 -   Compatibility with PyBaMM version 23.2: remove timescale from model options and change a notebook so that particle radius is no longer an input. This is temporarily unavailable in PyBaMM for geometry parameters. ([#222](https://github.com/pybamm-team/liionpack/pull/221))
 
 ## Breaking changes
 
 -   Drop support for Python 3.7 ([#216](https://github.com/pybamm-team/liionpack/pull/216))
 
 
-# [v0.3.3](https://github.com/pybamm-team/PyBaMM/tree/v0.3.3) - 2023-01-05
+# [v0.3.3](https://github.com/pybamm-team/liionpack/tree/v0.3.3) - 2023-01-05
 ## Bug fixes
 
 -   Update the codecov.yaml with develop branch ([#180](https://github.com/pybamm-team/liionpack/pull/180))
 -   Update conda environment to pin minimum versions of PyBaMM and Python ([#169](https://github.com/pybamm-team/liionpack/pull/169))
 -   Fix benchmarking again ([#187](https://github.com/pybamm-team/liionpack/pull/187))
 -   Fix inconsistent results with Ray manager ([#189](https://github.com/pybamm-team/liionpack/pull/189))
 -   Deal with removal of external variables ([#192](https://github.com/pybamm-team/liionpack/pull/192))
@@ -32,27 +65,27 @@
 ## Features
 
 -   Update the contributing docs about branches ([#179](https://github.com/pybamm-team/liionpack/pull/179))
 -   Update push to pypi following master sunset ([#193](https://github.com/pybamm-team/liionpack/pull/193))
 -   Change default branch on github to develop to fix benchmarking issues ([#184](https://github.com/pybamm-team/liionpack/pull/184))
 -   Migrate to hatch packaging ([#182](https://github.com/pybamm-team/liionpack/pull/182))
 
-# [v0.3.2](https://github.com/pybamm-team/PyBaMM/tree/v0.3.2) - 2022-07-01
+# [v0.3.2](https://github.com/pybamm-team/liionpack/tree/v0.3.2) - 2022-07-01
 
 ## Bug fixes
 
 -   Fix logger message duplication ([#156](https://github.com/pybamm-team/liionpack/pull/156))
 -   Fix build after changes to variable names in PyBaMM concerning initial stoich ([#159](https://github.com/pybamm-team/liionpack/pull/159))
 -   Pin version of protobuf to fix docs ([#163](https://github.com/pybamm-team/liionpack/pull/163))
 
 ## Breaking changes
 
 -   Remove support for dask as it reduces dependencies and does not perform as well as ray for our use case ([#160](https://github.com/pybamm-team/liionpack/pull/160))
 
-# [v0.3.1](https://github.com/pybamm-team/PyBaMM/tree/v0.3.1) - 2022-05-24
+# [v0.3.1](https://github.com/pybamm-team/liionpack/tree/v0.3.1) - 2022-05-24
 
 ## Features
 
 -   Add functions for saving simulation output to csv and npz ([#145](https://github.com/pybamm-team/liionpack/pull/145))
 -   Internally change generation of ParameterValues to new PyBaMM format ([#134](https://github.com/pybamm-team/liionpack/pull/134))
 -   Change model timescale to a scalar so that scaling is consistent in batteries of different sizes for single model. Add external thermal simulation function. Update circuit solve vectorized to work with circuit topology with multiple similar resistors connected to single nodes. ([#124](https://github.com/pybamm-team/liionpack/pull/124))
 
@@ -61,15 +94,15 @@
 -   Fix build, update solution inistialisation ([#148](https://github.com/pybamm-team/liionpack/pull/148))
 -   Add jax install to github actions ([#154](https://github.com/pybamm-team/liionpack/pull/154))
 
 ## Breaking changes
 
 -   Change solver class names to camelcase. Does not break usage if using wrapper solve functions ([#132](https://github.com/pybamm-team/liionpack/pull/132))
 
-# [v0.3](https://github.com/pybamm-team/PyBaMM/tree/v0.3) - 2022-02-17
+# [v0.3](https://github.com/pybamm-team/liionpack/tree/v0.3) - 2022-02-17
 This is the first official version of liionpack.
 Please note that liionpack and PyBaMM are both still under active development, and so the API may change in the future.
 
 ## Features
 
 - Define a pack architecture with number of batteries in series and / parallel
 - Load a pack architecture from a SPICE netlist
```

### Comparing `liionpack-0.3.4/asv.conf.json` & `liionpack-0.3.5/asv.conf.json`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/environment.yml` & `liionpack-0.3.5/environment.yml`

 * *Files 23% similar despite different names*

```diff
@@ -23,13 +23,16 @@
   - numpy
   - scipy
   - matplotlib
   - pandas
   - ipython
   - jupyter
   - sympy
-  - flake8
   - pip
   - pip:
-    - pybamm>=23.2
+    - pybamm>=23.3
     - ipdb
+    - ruff
+    - mkdocstrings-python-legacy
+    - mkdocs-material
+    - mkdocs-jupyter
     - -e .
```

### Comparing `liionpack-0.3.4/mkdocs.yml` & `liionpack-0.3.5/mkdocs.yml`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/.github/ISSUE_TEMPLATE/bug_report.yml` & `liionpack-0.3.5/.github/ISSUE_TEMPLATE/bug_report.yml`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/.github/ISSUE_TEMPLATE/feature_request.yml` & `liionpack-0.3.5/.github/ISSUE_TEMPLATE/feature_request.yml`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/.github/workflows/periodic_benchmarks.yml` & `liionpack-0.3.5/.github/workflows/periodic_benchmarks.yml`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/.github/workflows/publish_pypi.yml` & `liionpack-0.3.5/.github/workflows/publish_pypi.yml`

 * *Files 2% similar despite different names*

```diff
@@ -43,22 +43,22 @@
       - name: Download package
         uses: actions/download-artifact@v2
         with:
           name: files
           path: dist
 
       - name: Publish on PyPI
-        if: github.event.inputs.target == 'pypi' && github.ref == 'refs/heads/main'
+        if: github.event.inputs.target == 'pypi' && github.ref == 'refs/heads/develop'
         uses: pypa/gh-action-pypi-publish@release/v1
         with:
           user: __token__
           password: ${{ secrets.PYPI_TOKEN }}
           packages_dir: dist/
 
       - name: Publish on TestPyPI
-        if: github.event.inputs.target == 'testpypi' && github.ref == 'refs/heads/main'
+        if: github.event.inputs.target == 'testpypi' && github.ref == 'refs/heads/develop'
         uses: pypa/gh-action-pypi-publish@release/v1
         with:
           user: __token__
           password: ${{ secrets.TESTPYPI_TOKEN }}
           packages_dir: dist/
           repository_url: https://test.pypi.org/legacy/
```

### Comparing `liionpack-0.3.4/.github/workflows/run_benchmarks_over_history.yml` & `liionpack-0.3.5/.github/workflows/run_benchmarks_over_history.yml`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/benchmarks/benchmarks.py` & `liionpack-0.3.5/benchmarks/benchmarks.py`

 * *Files 0% similar despite different names*

```diff
@@ -10,15 +10,14 @@
         self.sim = lp.basic_simulation()
 
     def time_solve_model(self):
         self.sim.solve([0, 1800])
 
 
 class SmallPack:
-
     timeout = 60
 
     def setup(self):
         self.netlist = lp.setup_circuit(Np=2, Ns=1, Rb=1e-4, Rc=1e-2)
         self.parameter_values = pybamm.ParameterValues("Chen2020")
         self.experiment = pybamm.Experiment(
             [
@@ -43,15 +42,14 @@
             experiment=self.experiment,
             initial_soc=0.5,
             nproc=2,
         )
 
 
 class MediumPack:
-
     timeout = 120
 
     def setup(self):
         self.netlist = lp.setup_circuit(Np=32, Ns=10, Rb=1e-4, Rc=1e-2)
         self.parameter_values = pybamm.ParameterValues("Chen2020")
         self.experiment = pybamm.Experiment(
             [
@@ -76,15 +74,14 @@
             experiment=self.experiment,
             initial_soc=0.5,
             nproc=2,
         )
 
 
 class LargePack:
-
     timeout = 600
 
     def setup(self):
         self.netlist = lp.setup_circuit(Np=64, Ns=10, Rb=1e-4, Rc=1e-2)
         self.parameter_values = pybamm.ParameterValues("Chen2020")
         self.experiment = pybamm.Experiment(
             [
```

### Comparing `liionpack-0.3.4/docs/conduct.md` & `liionpack-0.3.5/docs/conduct.md`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/contributing.md` & `liionpack-0.3.5/docs/contributing.md`

 * *Files 4% similar despite different names*

```diff
@@ -4,14 +4,31 @@
 
 If you're already familiar with our workflow, maybe have a quick look at the [pre-commit checks](#pre-commit-checks) directly below.
 
 ## Pre-commit checks
 
 Fork the repository and create a pull request. Github actions should check that tests are passing.
 
+### Installing and using pre-commit
+
+`liionpack` uses a set of `pre-commit` hooks and the `pre-commit` bot to format and prettify the codebase. The hooks can be installed locally using -
+
+```bash
+pip install pre-commit
+pre-commit install
+```
+
+This would run the checks every time a commit is created locally. The checks will only run on the files modified by that commit, but the checks can be triggered for all the files using -
+
+```bash
+pre-commit run --all-files
+```
+
+If you would like to skip the failing checks and push the code for further discussion, use the `--no-verify` option with `git commit`.
+
 ## Workflow
 
 We use [GIT](https://en.wikipedia.org/wiki/Git) and [GitHub](https://en.wikipedia.org/wiki/GitHub) to coordinate our work. When making any kind of update, we try to follow the procedure below.
 
 ### A. Before you begin
 
 1. Create an [issue](https://guides.github.com/features/issues/) where new proposals can be discussed before any coding is done.
@@ -40,22 +57,26 @@
 
 
 
 ## Coding style guidelines
 
 liionpack follows the [PEP8 recommendations](https://www.python.org/dev/peps/pep-0008/) for coding style. These are very common guidelines, and community tools have been developed to check how well projects implement them.
 
-### Flake8
+### Ruff
 
-We use [flake8](http://flake8.pycqa.org/en/latest/) to check our PEP8 adherence. To try this on your system, navigate to the liionpack directory in a console and type
+We use [ruff](https://github.com/charliermarsh/ruff) to check our PEP8 adherence. To try this on your system, navigate to the liionpack directory in a console and type
 
 ```bash
-flake8
+python -m pip install pre-commit
+pre-commit run ruff
 ```
 
+ruff is configured inside the file `pre-commit-config.yaml`, allowing us to ignore some errors. If you think this should be added or removed, please submit an [issue](#issues)
+
+When you commit your changes they will be checked against ruff automatically (see [infrastructure](#infrastructure)).
 
 ### Black
 
 We use [black](https://black.readthedocs.io/en/stable/) to automatically configure our code to adhere to PEP8. Black can be used in two ways:
 
 1. Command line: navigate to the liionpack directory in a console and type
 
@@ -63,15 +84,15 @@
 black {source_file_or_directory}
 ```
 
 2. Editor: black can be [configured](https://test-black.readthedocs.io/en/latest/editor_integration.html) to automatically reformat a python script each time the script is saved in an editor.
 
 If you want to use black in your editor, you may need to change the max line length in your editor settings.
 
-Even when code has been formatted by black, you should still make sure that it adheres to the PEP8 standard set by [Flake8](#flake8).
+Even when code has been formatted by black, you should still make sure that it adheres to the PEP8 standard set by [Ruff](#ruff).
 
 ### Naming
 
 Naming is hard. In general, we aim for descriptive class, method, and argument names. Avoid abbreviations when possible without making names overly long, so `mean` is better than `mu`, but a class name like `MyClass` is fine.
 
 Class names are CamelCase, and start with an upper case letter, for example `MyOtherClass`. Method and variable names are lower case, and use underscores for word separation, for example `x` or `iteration_count`.
 
@@ -169,15 +190,15 @@
 pybamm.citations.register("your_paper_bibtex_identifier")
 ```
 
 wherever code is called that uses that citation (for example, in functions or in the `__init__` method of a class such as a model or solver).
 
 ## Benchmarks
 
-A benchmark suite is located in the `benchmarks` directory at the root of the PyBaMM project. These benchmarks can be run using [airspeed velocity](https://asv.readthedocs.io/en/stable/) (`asv`).
+A benchmark suite is located in the `benchmarks` directory at the root of the liionpack project. These benchmarks can be run using [airspeed velocity](https://asv.readthedocs.io/en/stable/) (`asv`).
 
 ### Running the benchmarks
 First of all, you'll need `asv` installed:
 ```shell
 pip install asv
 ```
 
@@ -194,15 +215,15 @@
 
 Benchmarks can also be run over a range of commits. For instance, the following command runs the benchmark suite over every commit between a given commit with ID `commit_ID` and the tip of the `main` branch:
 ```shell
 asv run commit_ID..develop
 ```
 Further information on how to run benchmarks with `asv` can be found in the documentation at [Using airspeed velocity](https://asv.readthedocs.io/en/stable/using.html).
 
-`asv` is configured using a file `asv.conf.json` located at the root of the PyBaMM repository. See the [asv reference](https://asv.readthedocs.io/en/stable/reference.html) for details on available settings and options.
+`asv` is configured using a file `asv.conf.json` located at the root of the liionpack repository. See the [asv reference](https://asv.readthedocs.io/en/stable/reference.html) for details on available settings and options.
 
 Benchmark results are stored in a directory `results/` at the location of the configuration file. There is one result file per commit, per machine.
 
 ### Visualising benchmark results
 
 `asv` is able to generate a static website with a visualisation of the benchmarks results, i.e. the benchmark's duration as a function of the commit hash.
 To generate the website, use
@@ -210,15 +231,15 @@
 asv publish
 ```
 then, to view the website:
 ```shell
 asv preview
 ```
 
-Current benchmarks over PyBaMM's history can be viewed at https://pybamm-team.github.io/liionpack-bench/
+Current benchmarks over liionpack's history can be viewed at https://pybamm-team.github.io/liionpack-bench/
 
 ### Adding benchmarks
 
 To contribute benchmarks to liionpack, add a new benchmark function in one of the files in the `benchmarks/` directory.
 Benchmarks are distributed across multiple files, grouped by theme. You're welcome to add a new file if none of your benchmarks fit into one of the already existing files.
 Inside a benchmark file (e.g. `benchmarks/benchmarks.py`) benchmarks functions are grouped within classes.
```

### Comparing `liionpack-0.3.4/docs/index.md` & `liionpack-0.3.5/docs/index.md`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/install.md` & `liionpack-0.3.5/docs/install.md`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/liionpack.png` & `liionpack-0.3.5/docs/liionpack.png`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/mathjax-config.js` & `liionpack-0.3.5/docs/mathjax-config.js`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/examples/01 Getting Started.ipynb` & `liionpack-0.3.5/docs/examples/01 Getting Started.ipynb`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/examples/02 Using inputs.ipynb` & `liionpack-0.3.5/docs/examples/02 Using inputs.ipynb`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/examples/03 Experiments.ipynb` & `liionpack-0.3.5/docs/examples/03 Experiments.ipynb`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/examples/04 Initial SoC.ipynb` & `liionpack-0.3.5/docs/examples/04 Initial SoC.ipynb`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/examples/05 Drive cycles.ipynb` & `liionpack-0.3.5/docs/examples/05 Drive cycles.ipynb`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/examples/06 Changing a model.ipynb` & `liionpack-0.3.5/docs/examples/06 Changing a model.ipynb`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/examples/07 Visualizing larger packs.ipynb` & `liionpack-0.3.5/docs/examples/07 Visualizing larger packs.ipynb`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/examples/08 SEI degradation model.ipynb` & `liionpack-0.3.5/docs/examples/08 SEI degradation model.ipynb`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/docs/examples/09 Terminal locations.ipynb` & `liionpack-0.3.5/docs/examples/09 Terminal locations.ipynb`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/examples/basic_16p2s.py` & `liionpack-0.3.5/examples/basic_16p2s.py`

 * *Files 13% similar despite different names*

```diff
@@ -4,48 +4,52 @@
 """
 
 import liionpack as lp
 import pybamm
 import numpy as np
 import os
 
-lp.set_logging_level('NOTICE')
+lp.set_logging_level("NOTICE")
 
 # Define parameters
 Np = 16
 Ns = 2
 Iapp = 20
 
 # Generate the netlist
 netlist = lp.setup_circuit(Np=Np, Ns=Ns)
 
 # Define additional output variables
-output_variables = [
-    'Volume-averaged cell temperature [K]']
+output_variables = ["Volume-averaged cell temperature [K]"]
 
 # Define a cycling experiment using PyBaMM
-experiment = pybamm.Experiment([
-    f'Charge at {Iapp} A for 30 minutes',
-    'Rest for 15 minutes',
-    f'Discharge at {Iapp} A for 30 minutes',
-    'Rest for 30 minutes'],
-    period='10 seconds')
+experiment = pybamm.Experiment(
+    [
+        f"Charge at {Iapp} A for 30 minutes",
+        "Rest for 15 minutes",
+        f"Discharge at {Iapp} A for 30 minutes",
+        "Rest for 30 minutes",
+    ],
+    period="10 seconds",
+)
 
 # Define the PyBaMM parameters
 parameter_values = pybamm.ParameterValues("Chen2020")
 inputs = {"Total heat transfer coefficient [W.m-2.K-1]": np.ones(Np * Ns) * 10}
 
 # Solve the pack
-output = lp.solve(netlist=netlist,
-                  sim_func=lp.thermal_simulation,
-                  parameter_values=parameter_values,
-                  experiment=experiment,
-                  output_variables=output_variables,
-                  initial_soc=0.5,
-                  inputs=inputs,
-                  nproc=os.cpu_count(),
-                  manager='casadi')
+output = lp.solve(
+    netlist=netlist,
+    sim_func=lp.thermal_simulation,
+    parameter_values=parameter_values,
+    experiment=experiment,
+    output_variables=output_variables,
+    initial_soc=0.5,
+    inputs=inputs,
+    nproc=os.cpu_count(),
+    manager="casadi",
+)
 
 # Plot the pack and individual cell results
 lp.plot_pack(output)
 lp.plot_cells(output)
 lp.show_plots()
```

### Comparing `liionpack-0.3.4/examples/big_circuit.py` & `liionpack-0.3.5/examples/big_circuit.py`

 * *Files 3% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 """
 
 import liionpack as lp
 import pybamm
 import os
 import pickle
 
-lp.log_to_file('logger_info')
+lp.log_to_file("logger_info")
 
 
 if __name__ == "__main__":
     Np = 32
     Ns = 12
     Nspm = Np * Ns
     I_app = 5
@@ -37,9 +37,9 @@
     output = lp.solve(
         netlist=netlist,
         parameter_values=parameter_values,
         experiment=experiment,
         nproc=os.cpu_count(),
     )
 
-    with open('output.pickle', 'wb') as handle:
+    with open("output.pickle", "wb") as handle:
         pickle.dump(output, handle, protocol=pickle.HIGHEST_PROTOCOL)
```

### Comparing `liionpack-0.3.4/examples/different_initial_soc.py` & `liionpack-0.3.5/examples/different_initial_soc.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/examples/draw_circuit.py` & `liionpack-0.3.5/examples/draw_circuit.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/examples/draw_terminals.py` & `liionpack-0.3.5/examples/draw_terminals.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/examples/drive_cycle.py` & `liionpack-0.3.5/examples/drive_cycle.py`

 * *Files 1% similar despite different names*

```diff
@@ -23,22 +23,24 @@
 drive_cycle = pd.read_csv(
     "pybamm/input/drive_cycles/US06.csv", comment="#", header=None
 ).to_numpy()
 
 experiment = pybamm.Experiment(
     operating_conditions=["Run US06 (A)"],
     period="1 minute",
-    drive_cycles={"US06": drive_cycle})
+    drive_cycles={"US06": drive_cycle},
+)
 
 # PyBaMM parameters
 parameter_values = pybamm.ParameterValues("Chen2020")
 
 # Solve pack
 output = lp.solve(
     netlist=netlist,
     parameter_values=parameter_values,
     experiment=experiment,
-    initial_soc=0.5)
+    initial_soc=0.5,
+)
 
 # Plot results
 lp.plot_output(output)
 lp.show_plots()
```

### Comparing `liionpack-0.3.4/examples/drive_cycle_comparison.py` & `liionpack-0.3.5/examples/drive_cycle_comparison.py`

 * *Files 2% similar despite different names*

```diff
@@ -44,23 +44,25 @@
     # Solve pack
     output = lp.solve(
         netlist=netlist,
         parameter_values=parameter_values,
         experiment=experiment,
         output_variables=output_variables,
         initial_soc=init_SoC,
-        manager='casadi',
-        nproc=8)
+        manager="casadi",
+        nproc=8,
+    )
 
     parameter_values = pybamm.ParameterValues("Chen2020")
 
     sim = pybamm.Simulation(
         model=pybamm.lithium_ion.SPM(),
         experiment=experiment,
-        parameter_values=parameter_values)
+        parameter_values=parameter_values,
+    )
 
     sol = sim.solve(initial_soc=init_SoC)
 
     t_pybamm = sol["Time [s]"].entries
     t_liionpack = output["Time [s]"]
     v_pybamm = sol["Terminal voltage [V]"].entries
     v_liionpack = output["Terminal voltage [V]"]
```

### Comparing `liionpack-0.3.4/examples/load_4p1s.py` & `liionpack-0.3.5/examples/load_4p1s.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/examples/mixed_terminals.py` & `liionpack-0.3.5/examples/mixed_terminals.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/examples/paper_example.py` & `liionpack-0.3.5/examples/paper_example.py`

 * *Files 13% similar despite different names*

```diff
@@ -6,34 +6,39 @@
 import pybamm
 
 # Generate the netlist
 netlist = lp.setup_circuit(Np=4, Ns=1, Rb=1e-3, Rc=1e-2)
 
 # Define some additional variables to output
 output_variables = [
-    'X-averaged negative particle surface concentration [mol.m-3]',
-    'X-averaged positive particle surface concentration [mol.m-3]',
+    "X-averaged negative particle surface concentration [mol.m-3]",
+    "X-averaged positive particle surface concentration [mol.m-3]",
 ]
 
 # Cycling experiment, using PyBaMM
-experiment = pybamm.Experiment([
-    "Charge at 5 A for 30 minutes",
-    "Rest for 15 minutes",
-    "Discharge at 5 A for 30 minutes",
-    "Rest for 30 minutes"],
-    period="10 seconds")
+experiment = pybamm.Experiment(
+    [
+        "Charge at 5 A for 30 minutes",
+        "Rest for 15 minutes",
+        "Discharge at 5 A for 30 minutes",
+        "Rest for 30 minutes",
+    ],
+    period="10 seconds",
+)
 
 # PyBaMM battery parameters
 parameter_values = pybamm.ParameterValues("Chen2020")
 
 # Solve the pack problem
-output = lp.solve(netlist=netlist,
-                  parameter_values=parameter_values,
-                  experiment=experiment,
-                  output_variables=output_variables,
-                  initial_soc=0.5)
+output = lp.solve(
+    netlist=netlist,
+    parameter_values=parameter_values,
+    experiment=experiment,
+    output_variables=output_variables,
+    initial_soc=0.5,
+)
 
 # Display the results
 lp.plot_output(output, color="white")
 
 # Draw the circuit at final state
 lp.draw_circuit(netlist, cpt_size=1.0, node_spacing=2.2)
```

### Comparing `liionpack-0.3.4/examples/save_output.py` & `liionpack-0.3.5/examples/save_output.py`

 * *Files 10% similar despite different names*

```diff
@@ -13,39 +13,44 @@
 Ns = 2
 Iapp = 20
 
 # Generate the netlist
 netlist = lp.setup_circuit(Np=Np, Ns=Ns)
 
 # Define additional output variables
-output_variables = ['Volume-averaged cell temperature [K]']
+output_variables = ["Volume-averaged cell temperature [K]"]
 
 # Define a cycling experiment using PyBaMM
-experiment = pybamm.Experiment([
-    f'Charge at {Iapp} A for 30 minutes',
-    'Rest for 15 minutes',
-    f'Discharge at {Iapp} A for 30 minutes',
-    'Rest for 30 minutes'],
-    period='10 seconds')
+experiment = pybamm.Experiment(
+    [
+        f"Charge at {Iapp} A for 30 minutes",
+        "Rest for 15 minutes",
+        f"Discharge at {Iapp} A for 30 minutes",
+        "Rest for 30 minutes",
+    ],
+    period="10 seconds",
+)
 
 # Define the PyBaMM parameters
 chemistry = pybamm.parameter_sets.Chen2020
 parameter_values = pybamm.ParameterValues(chemistry=chemistry)
 inputs = {"Total heat transfer coefficient [W.m-2.K-1]": np.ones(Np * Ns) * 10}
 
 # Solve the pack
-output = lp.solve(netlist=netlist,
-                  sim_func=lp.thermal_simulation,
-                  parameter_values=parameter_values,
-                  experiment=experiment,
-                  output_variables=output_variables,
-                  initial_soc=0.5,
-                  inputs=inputs,
-                  nproc=os.cpu_count(),
-                  manager='casadi')
+output = lp.solve(
+    netlist=netlist,
+    sim_func=lp.thermal_simulation,
+    parameter_values=parameter_values,
+    experiment=experiment,
+    output_variables=output_variables,
+    initial_soc=0.5,
+    inputs=inputs,
+    nproc=os.cpu_count(),
+    manager="casadi",
+)
 
 # Save simulation output to CSV files
 lp.save_to_csv(output)
 
 # Save simulation output to Numpy npy files
 lp.save_to_npy(output)
```

### Comparing `liionpack-0.3.4/examples/step_external_variable.py` & `liionpack-0.3.5/examples/step_external_variable.py`

 * *Files 1% similar despite different names*

```diff
@@ -49,15 +49,15 @@
     sim_func=lp.thermal_external,
     parameter_values=parameter_values,
     experiment=experiment,
     output_variables=output_variables,
     inputs=inputs,
     nproc=2,
     initial_soc=0.5,
-    setup_only=True
+    setup_only=True,
 )
 
 
 def external_stepper(manager, T0):
     tic = ticker.time()
     # Do stepping
     lp.logger.notice("Starting step solve")
```

### Comparing `liionpack-0.3.4/examples/thermal_external.py` & `liionpack-0.3.5/examples/thermal_external.py`

 * *Files 22% similar despite different names*

```diff
@@ -2,40 +2,41 @@
 # External thermal example
 #
 
 import liionpack as lp
 import pybamm
 import numpy as np
 import matplotlib.pyplot as plt
-plt.close('all')
+
+plt.close("all")
 
 
 # Generate the netlist
 netlist = lp.setup_circuit(Np=4, Ns=1, Rb=1e-3, Rc=1e-2)
 
 # Define some additional variables to output
 output_variables = [
     "Volume-averaged cell temperature [K]",
-    "Volume-averaged total heating [W.m-3]"
+    "Volume-averaged total heating [W.m-3]",
 ]
 
 # Cycling experiment, using PyBaMM
-experiment = pybamm.Experiment([
-    "Discharge at 5 A for 5 minutes"],
-    period="10 seconds")
+experiment = pybamm.Experiment(["Discharge at 5 A for 5 minutes"], period="10 seconds")
 
 # PyBaMM battery parameters
 parameter_values = pybamm.ParameterValues("Chen2020")
 
 # Solve the pack problem
 temps = np.ones(4) * 300 + np.arange(4) * 10
 inputs = {"Input temperature [K]": temps}
-output = lp.solve(netlist=netlist,
-                  sim_func=lp.thermal_external,
-                  inputs=inputs,
-                  parameter_values=parameter_values,
-                  experiment=experiment,
-                  output_variables=output_variables,
-                  initial_soc=0.5)
+output = lp.solve(
+    netlist=netlist,
+    sim_func=lp.thermal_external,
+    inputs=inputs,
+    parameter_values=parameter_values,
+    experiment=experiment,
+    output_variables=output_variables,
+    initial_soc=0.5,
+)
 
 # Display the results
 lp.plot_output(output, color="white")
```

### Comparing `liionpack-0.3.4/liionpack/__init__.py` & `liionpack-0.3.5/liionpack/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -40,8 +40,8 @@
 from .definitions import MODULE_DIR
 from .definitions import CIRCUIT_DIR
 from .solvers import CasadiManager
 from .solvers import RayManager
 from .solvers import GenericActor
 from .solvers import RayActor
 
-__version__ = "0.3.4"
+__version__ = "0.3.5"
```

### Comparing `liionpack-0.3.4/liionpack/logger.py` & `liionpack-0.3.5/liionpack/logger.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/liionpack/netlist_utils.py` & `liionpack-0.3.5/liionpack/netlist_utils.py`

 * *Files 0% similar despite different names*

```diff
@@ -110,15 +110,15 @@
     Rc=1e-2,
     Rb=1e-4,
     Rt=1e-5,
     I=80.0,
     V=4.2,
     plot=False,
     terminals="left",
-    configuration="parallel-strings"
+    configuration="parallel-strings",
 ):
     """
     Define a netlist from a number of batteries in parallel and series
 
     Args:
         Np (int): Number of batteries in parallel.
         Ns (int): Number of batteries in series.
@@ -753,15 +753,15 @@
 
     Returns:
         None
 
 
     """
     lines = ["* " + filename]
-    for (i, r) in netlist.iterrows():
+    for i, r in netlist.iterrows():
         line = r.desc + " " + _fn(r.node1) + " " + _fn(r.node2) + " " + str(r.value)
         lines.append(line)
     lines.append(".op")
     lines.append(".backanno")
     lines.append(".end")
     with open(filename, "w") as f:
         for line in lines:
```

### Comparing `liionpack-0.3.4/liionpack/plots.py` & `liionpack-0.3.5/liionpack/plots.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/liionpack/protocols.py` & `liionpack-0.3.5/liionpack/protocols.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,13 +1,11 @@
 #
 # Experimental protocol
 #
 
-import numpy as np
-
 
 def generate_protocol_from_experiment(experiment, flatten=True):
     """
 
     Args:
         experiment (pybamm.Experiment):
             The experiment to generate the protocol from.
```

### Comparing `liionpack-0.3.4/liionpack/sim_utils.py` & `liionpack-0.3.5/liionpack/sim_utils.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/liionpack/simulations.py` & `liionpack-0.3.5/liionpack/simulations.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/liionpack/solver_utils.py` & `liionpack-0.3.5/liionpack/solver_utils.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/liionpack/solvers.py` & `liionpack-0.3.5/liionpack/solvers.py`

 * *Files 19% similar despite different names*

```diff
@@ -127,169 +127,14 @@
 
 class GenericManager:
     def __init__(
         self,
     ):
         pass
 
-    # def solve(
-    #     self,
-    #     netlist,
-    #     sim_func,
-    #     parameter_values,
-    #     experiment,
-    #     inputs,
-    #     external_variables,
-    #     output_variables,
-    #     initial_soc,
-    #     nproc,
-    # ):
-    #     self.netlist = netlist
-    #     self.sim_func = sim_func
-
-    #     self.parameter_values = parameter_values
-    #     self.check_current_function()
-    #     # Get netlist indices for resistors, voltage sources, current sources
-    #     Ri_map = netlist["desc"].str.find("Ri") > -1
-    #     V_map = netlist["desc"].str.find("V") > -1
-    #     I_map = netlist["desc"].str.find("I") > -1
-    #     Terminal_Node = np.array(netlist[I_map].node1)
-    #     Nspm = np.sum(V_map)
-
-    #     self.split_models(Nspm, nproc)
-
-    #     # Generate the protocol from the supplied experiment
-    #     protocol = lp.generate_protocol_from_experiment(experiment, flatten=True)
-    #     self.dt = experiment.period
-    #     Nsteps = len(protocol)
-    #     netlist.loc[I_map, ("value")] = protocol[0]
-    #     # Solve the circuit to initialise the electrochemical models
-    #     V_node, I_batt = lp.solve_circuit(netlist)
-
-    #     # The simulation output variables calculated at each step for each battery
-    #     # Must be a 0D variable i.e. battery wide volume average - or X-averaged for
-    #     # 1D model
-    #     self.variable_names = [
-    #         "Terminal voltage [V]",
-    #         "Measured battery open circuit voltage [V]",
-    #     ]
-    #     if output_variables is not None:
-    #         for out in output_variables:
-    #             if out not in self.variable_names:
-    #                 self.variable_names.append(out)
-    #         # variable_names = variable_names + output_variables
-    #     Nvar = len(self.variable_names)
-
-    #     # Storage variables for simulation data
-    #     self.shm_i_app = np.zeros([Nsteps, Nspm], dtype=float)
-    #     self.shm_Ri = np.zeros([Nsteps, Nspm], dtype=float)
-    #     self.output = np.zeros([Nvar, Nsteps, Nspm], dtype=float)
-
-    #     # Initialize currents in battery models
-    #     self.shm_i_app[0, :] = I_batt * -1
-
-    #     # Step forward in time
-    #     self.timestep = 0
-    #     V_terminal = []
-    #     record_times = []
-
-    #     v_cut_lower = parameter_values["Lower voltage cut-off [V]"]
-    #     v_cut_higher = parameter_values["Upper voltage cut-off [V]"]
-
-    #     # Handle the inputs
-    #     self.inputs = inputs
-    #     self.external_variables = external_variables
-    #     self.inputs_dict = lp.build_inputs_dict(
-    #         self.shm_i_app[0, :], self.inputs, self.external_variables
-    #     )
-    #     # Solver specific setup
-    #     self.setup_actors(nproc, self.inputs_dict, initial_soc)
-    #     # Get the initial state of the system
-    #     self.evaluate_actors()
-    #     sim_start_time = ticker.time()
-    #     lp.logger.notice("Starting step solve")
-    #     with tqdm(total=Nsteps, desc="Stepping simulation") as pbar:
-    #         step = 0
-    #         while step < Nsteps:
-    #             # 01 Calculate whether resting or restarting
-    #             self.resting = (
-    #                 step > 0 and protocol[step] == 0.0 and protocol[step - 1] == 0.0
-    #             )
-    #             self.restarting = (
-    #                 step > 0 and protocol[step] != 0.0 and protocol[step - 1] == 0.0
-    #             )
-    #             # 02 Get the actor output - Battery state info
-    #             self.get_actor_output(step)
-    #             # 03 Get the ocv and internal resistance
-    #             temp_v = self.output[0, step, :]
-    #             temp_ocv = self.output[1, step, :]
-    #             # When resting and rebalancing currents are small the internal
-    #             # resistance calculation can diverge as it's R = V / I
-    #             # At rest the internal resistance should not change greatly
-    #             # so for now just don't recalculate it.
-    #             if not self.resting and not self.restarting:
-    #                 temp_Ri = self.calculate_internal_resistance(step)
-    #             self.shm_Ri[step, :] = temp_Ri
-    #             # 04 Update netlist
-    #             netlist.loc[V_map, ("value")] = temp_ocv
-    #             netlist.loc[Ri_map, ("value")] = temp_Ri
-    #             netlist.loc[I_map, ("value")] = protocol[step]
-    #             lp.power_loss(netlist)
-    #             # 05a Solve the circuit with updated netlist
-    #             if step <= Nsteps:
-    #                 V_node, I_batt = lp.solve_circuit(netlist)
-    #                 record_times.append((step) * self.dt)
-    #                 V_terminal.append(V_node[Terminal_Node][0])
-    #             # 05b Update the external variables
-    #             self.update_external_variables()
-    #             if step < Nsteps - 1:
-    #                 # igore last step save the new currents and build inputs
-    #                 # for the next step
-    #                 I_app = I_batt[:] * -1
-    #                 self.shm_i_app[step + 1, :] = I_app
-    #                 self.inputs_dict = lp.build_inputs_dict(
-    #                     I_app, self.inputs, self.external_variables
-    #                 )
-    #             # 06 Check if voltage limits are reached and terminate
-    #             if np.any(temp_v < v_cut_lower):
-    #                 lp.logger.warning("Low voltage limit reached")
-    #                 break
-    #             if np.any(temp_v > v_cut_higher):
-    #                 lp.logger.warning("High voltage limit reached")
-    #                 break
-    #             # 07 Step the electrochemical system
-    #             self.step_actors()
-    #             # 08 increment the step and update progress bar
-    #             step += 1
-    #             self.timestep = step
-    #             pbar.update(1)
-
-    #     lp.logger.notice("Step solve finished")
-    #     self.cleanup()
-    #     self.shm_Ri = np.abs(self.shm_Ri)
-    #     # Collect outputs
-    #     self.all_output = {}
-    #     self.all_output["Time [s]"] = np.asarray(record_times)
-    #     self.all_output["Pack current [A]"] = np.asarray(protocol[: step + 1])
-    #     self.all_output["Pack terminal voltage [V]"] = np.asarray(V_terminal)
-    #     self.all_output["Cell current [A]"] = self.shm_i_app[: step + 1, :]
-    #     self.all_output["Cell internal resistance [Ohm]"] = self.shm_Ri[: step + 1, :]
-    #     for j in range(Nvar):
-    #         self.all_output[self.variable_names[j]] = self.output[j, : step + 1, :]
-
-    #     toc = ticker.time()
-
-    #     lp.logger.notice(
-    #         "Total stepping time " + str(np.around(toc - sim_start_time, 3)) + "s"
-    #     )
-    #     lp.logger.notice(
-    #         "Time per step " + str(np.around((toc - sim_start_time) / Nsteps, 3)) + "s"
-    #     )
-    #     return self.all_output
-
     def solve(
         self,
         netlist,
         sim_func,
         parameter_values,
         experiment,
         inputs,
@@ -321,15 +166,15 @@
         V_node, I_batt = lp.solve_circuit_vectorized(netlist)
 
         # The simulation output variables calculated at each step for each battery
         # Must be a 0D variable i.e. battery wide volume average - or X-averaged for
         # 1D model
         self.variable_names = [
             "Terminal voltage [V]",
-            "Measured battery open circuit voltage [V]",
+            "Surface open-circuit voltage [V]",
         ]
         if output_variables is not None:
             for out in output_variables:
                 if out not in self.variable_names:
                     self.variable_names.append(out)
             # variable_names = variable_names + output_variables
         self.Nvar = len(self.variable_names)
@@ -347,17 +192,15 @@
         self.record_times = np.zeros(self.Nsteps, dtype=np.float32)
 
         self.v_cut_lower = parameter_values["Lower voltage cut-off [V]"]
         self.v_cut_higher = parameter_values["Upper voltage cut-off [V]"]
 
         # Handle the inputs
         self.inputs = inputs
-        self.inputs_dict = lp.build_inputs_dict(
-            self.shm_i_app[0, :], self.inputs, None
-        )
+        self.inputs_dict = lp.build_inputs_dict(self.shm_i_app[0, :], self.inputs, None)
         # Solver specific setup
         self.setup_actors(nproc, self.inputs_dict, initial_soc)
         # Get the initial state of the system
         self.evaluate_actors()
         if not setup_only:
             self._step_solve_step(None)
             return self.step_output()
@@ -429,18 +272,17 @@
             V_node, I_batt = lp.solve_circuit_vectorized(self.netlist)
             self.record_times[step] = step * self.dt
             self.V_terminal[step] = V_node[self.Terminal_Node][0]
         if step < self.Nsteps - 1:
             # igore last step save the new currents and build inputs
             # for the next step
             I_app = I_batt[:] * -1
+            self.shm_i_app[step, :] = I_app
             self.shm_i_app[step + 1, :] = I_app
-            self.inputs_dict = lp.build_inputs_dict(
-                I_app, self.inputs, updated_inputs
-            )
+            self.inputs_dict = lp.build_inputs_dict(I_app, self.inputs, updated_inputs)
         # 06 Check if voltage limits are reached and terminate
         if np.any(temp_v < self.v_cut_lower):
             lp.logger.warning("Low voltage limit reached")
             vlims_ok = False
         if np.any(temp_v > self.v_cut_higher):
             lp.logger.warning("High voltage limit reached")
             vlims_ok = False
```

### Comparing `liionpack-0.3.4/liionpack/utils.py` & `liionpack-0.3.5/liionpack/utils.py`

 * *Files 4% similar despite different names*

```diff
@@ -98,15 +98,15 @@
 
     """
     for event in model.events:
         model.variables.update({"Event: " + event.name: event.expression})
     return model
 
 
-def save_to_csv(output, path='./csv-results'):
+def save_to_csv(output, path="./csv-results"):
     """
     Save simulation output to a CSV file for each output variable.
 
     Parameters
     ----------
     output : dict
         Simulation output dictionary.
@@ -122,19 +122,19 @@
 
     # Create folder path for saving files
     path = pathlib.Path(path)
     path.mkdir(exist_ok=True)
 
     # Save simulation output to CSV files
     for k, v in output.items():
-        filename = k.replace(' ', '_') + '.csv'
-        np.savetxt(path / filename, v, delimiter=', ')
+        filename = k.replace(" ", "_") + ".csv"
+        np.savetxt(path / filename, v, delimiter=", ")
 
 
-def save_to_npy(output, path='./npy-results'):
+def save_to_npy(output, path="./npy-results"):
     """
     Save simulation output to NumPy `.npy` files where each file represents an
     output variable.
 
     Parameters
     ----------
     output : dict
@@ -151,19 +151,19 @@
 
     # Create folder path for saving files
     path = pathlib.Path(path)
     path.mkdir(exist_ok=True)
 
     # Save simulation output to npy files
     for k, v in output.items():
-        filename = k.replace(' ', '_') + '.npy'
+        filename = k.replace(" ", "_") + ".npy"
         np.save(path / filename, v)
 
 
-def save_to_npzcomp(output, path='.'):
+def save_to_npzcomp(output, path="."):
     """
     Save simulation output to a compressed NumPy `output.npz` file. The saved
     file is a dictionary-like object where each key represents a simulation
     output variable.
 
     Parameters
     ----------
@@ -181,9 +181,9 @@
     """
 
     # Create a path for saving the file
     path = pathlib.Path(path)
     path.mkdir(exist_ok=True)
 
     # Save simulation output to a compressed npz file
-    filename = 'output.npz'
+    filename = "output.npz"
     np.savez_compressed(path / filename, **output)
```

### Comparing `liionpack-0.3.4/liionpack/circuits/4p1s.asc` & `liionpack-0.3.5/liionpack/circuits/4p1s.asc`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/liionpack/circuits/4p1s.cir` & `liionpack-0.3.5/liionpack/circuits/4p1s.cir`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/paper/paper.bib` & `liionpack-0.3.5/paper/paper.bib`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/paper/paper.md` & `liionpack-0.3.5/paper/paper.md`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/paper/paper_figures/Figure_0.png` & `liionpack-0.3.5/paper/paper_figures/Figure_0.png`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/paper/paper_figures/Figure_1.png` & `liionpack-0.3.5/paper/paper_figures/Figure_1.png`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/paper/paper_figures/Figure_2.png` & `liionpack-0.3.5/paper/paper_figures/Figure_2.png`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/paper/paper_figures/Figure_3.png` & `liionpack-0.3.5/paper/paper_figures/Figure_3.png`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/tests/integration/test_1p1s.py` & `liionpack-0.3.5/tests/integration/test_1p1s.py`

 * *Files 6% similar despite different names*

```diff
@@ -17,23 +17,23 @@
         parameter_values = pybamm.ParameterValues("Chen2020")
         # Cycling experiment
         experiment = pybamm.Experiment(
             [("Discharge at 1 A for 100 s or until 3.3 V",)] * 1, period="10 s"
         )
         # Solve pack
         output = lp.solve(
-            netlist=netlist,
-            parameter_values=parameter_values,
-            experiment=experiment
+            netlist=netlist, parameter_values=parameter_values, experiment=experiment
         )
 
         parameter_values = pybamm.ParameterValues("Chen2020")
-        sim = pybamm.Simulation(model=pybamm.lithium_ion.SPM(),
-                                parameter_values=parameter_values,
-                                experiment=experiment)
+        sim = pybamm.Simulation(
+            model=pybamm.lithium_ion.SPM(),
+            parameter_values=parameter_values,
+            experiment=experiment,
+        )
 
         sol = sim.solve()
         a = output["Terminal voltage [V]"].flatten()
         b = sol["Terminal voltage [V]"].entries
 
         assert np.allclose(a, b)
 
@@ -57,24 +57,26 @@
         )
         SoC = 0.5
         # Solve pack
         output = lp.solve(
             netlist=netlist,
             parameter_values=parameter_values,
             experiment=experiment,
-            initial_soc=SoC
+            initial_soc=SoC,
         )
 
         parameter_values = pybamm.ParameterValues("Chen2020")
-        sim = pybamm.Simulation(model=pybamm.lithium_ion.SPM(),
-                                parameter_values=parameter_values,
-                                experiment=experiment)
+        sim = pybamm.Simulation(
+            model=pybamm.lithium_ion.SPM(),
+            parameter_values=parameter_values,
+            experiment=experiment,
+        )
 
         sol = sim.solve(initial_soc=SoC)
         a = output["Terminal voltage [V]"].flatten()
         b = sol["Terminal voltage [V]"].entries
-        diff = np.abs(a - b)
+        diff = np.abs(a[:20] - b[:20])
         assert np.all(diff < 0.05)
 
 
 if __name__ == "__main__":
     unittest.main()
```

### Comparing `liionpack-0.3.4/tests/integration/test_all_solvers.py` & `liionpack-0.3.5/tests/integration/test_all_solvers.py`

 * *Files 1% similar despite different names*

```diff
@@ -23,24 +23,24 @@
         # Solve pack with casadi
         a = lp.solve(
             netlist=netlist,
             parameter_values=parameter_values,
             experiment=experiment,
             inputs=None,
             nproc=1,
-            manager="casadi"
+            manager="casadi",
         )
         # Solve pack with ray
         b = lp.solve(
             netlist=netlist,
             parameter_values=parameter_values,
             experiment=experiment,
             inputs=None,
             nproc=1,
-            manager="ray"
+            manager="ray",
         )
 
         v_a = a["Terminal voltage [V]"]
         v_b = b["Terminal voltage [V]"]
 
         assert np.allclose(v_a, v_b)
```

### Comparing `liionpack-0.3.4/tests/unit/test_logger.py` & `liionpack-0.3.5/tests/unit/test_logger.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/tests/unit/test_netlist_utils.py` & `liionpack-0.3.5/tests/unit/test_netlist_utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -133,15 +133,15 @@
         assert cct_lr.has_dc
         assert cct_rl.has_dc
         assert cct_m.has_dc
 
     def test_write_netlist(self):
         net = lp.setup_circuit(Np=1, Ns=2, Rb=1e-4, Rc=1e-2, Ri=1e-3, V=2.0, I=10.0)
         cwd = os.getcwd()
-        temp = os.path.join(cwd, 'temp.txt')
+        temp = os.path.join(cwd, "temp.txt")
         lp.write_netlist(net, temp)
         assert os.path.isfile(temp)
         os.remove(temp)
 
 
 if __name__ == "__main__":
     unittest.main()
```

### Comparing `liionpack-0.3.4/tests/unit/test_notebooks.py` & `liionpack-0.3.5/tests/unit/test_notebooks.py`

 * *Files 8% similar despite different names*

```diff
@@ -10,15 +10,14 @@
 import liionpack as lp
 
 
 class TestNotebooks(unittest.TestCase):
     def test_notebooks(self):
         examples_folder = os.path.join(lp.ROOT_DIR, "docs", "examples")
         for filename in os.listdir(examples_folder):
-
             if os.path.splitext(filename)[1] == ".ipynb":
                 print("-" * 80)
                 print("Testing notebook:", filename)
                 print("-" * 80)
 
                 # Load notebook, convert to python
                 path = os.path.join(examples_folder, filename)
```

### Comparing `liionpack-0.3.4/tests/unit/test_plots.py` & `liionpack-0.3.5/tests/unit/test_plots.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/tests/unit/test_protocols.py` & `liionpack-0.3.5/tests/unit/test_protocols.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/tests/unit/test_sim_utils.py` & `liionpack-0.3.5/tests/unit/test_sim_utils.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/tests/unit/test_simulations.py` & `liionpack-0.3.5/tests/unit/test_simulations.py`

 * *Files 2% similar despite different names*

```diff
@@ -7,16 +7,17 @@
     def test_basic_simulation(self):
         sim = lp.basic_simulation()
         sim.solve([0, 1800])
         assert sim.__class__ == pybamm.Simulation
 
     def test_thermal_simulation(self):
         sim = lp.thermal_simulation()
-        sim.solve([0, 1800],
-                  inputs={"Total heat transfer coefficient [W.m-2.K-1]": 1.0})
+        sim.solve(
+            [0, 1800], inputs={"Total heat transfer coefficient [W.m-2.K-1]": 1.0}
+        )
         assert sim.__class__ == pybamm.Simulation
 
     # def test_thermal_external(self):
     #     sim = lp.thermal_external()
     #     sim.solve([0, 1800],
     #               external_variables={"Volume-averaged cell temperature": 1.0})
     #     assert sim.__class__ == pybamm.Simulation
```

### Comparing `liionpack-0.3.4/tests/unit/test_solver_utils.py` & `liionpack-0.3.5/tests/unit/test_solver_utils.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/tests/unit/test_solvers.py` & `liionpack-0.3.5/tests/unit/test_solvers.py`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/tests/unit/test_utils.py` & `liionpack-0.3.5/tests/unit/test_utils.py`

 * *Files 12% similar despite different names*

```diff
@@ -3,19 +3,18 @@
 import pandas as pd
 import pathlib
 import pybamm
 import unittest
 
 
 class utilsTest(unittest.TestCase):
-
     def setUp(self):
         currents = [4, 5.2, 8, 10]
         volts = np.array([[3.5, 3.6], [3.54, 3.58]])
-        output = {'currents': currents, 'volts': volts}
+        output = {"currents": currents, "volts": volts}
 
         self.currents = currents
         self.volts = volts
         self.output = output
 
     def test_interp_current(self):
         d = {"Time": [0, 10], "Cells Total Current": [2.0, 4.0]}
@@ -37,56 +36,56 @@
         I_batt = np.array([1.0, 2.0])
         inputs = {"Electrode height [m]": [3.0, 4.0]}
         external_variables = {"Volume averaged cell temperature": [5.0, 6.0]}
         in_dict = lp.build_inputs_dict(I_batt, inputs, external_variables)
         assert len(in_dict) == 2
 
     def test_save_to_csv(self):
-        lp.save_to_csv(self.output, path='.')
+        lp.save_to_csv(self.output, path=".")
 
-        with open('currents.csv', 'r') as f:
+        with open("currents.csv", "r") as f:
             current = float(f.readline())
         self.assertEqual(self.currents[0], current)
 
-        with open('volts.csv', 'r') as f:
-            volts = list(map(float, f.readline().split(', ')))
+        with open("volts.csv", "r") as f:
+            volts = list(map(float, f.readline().split(", ")))
         self.assertEqual(self.volts[0][0], volts[0])
 
     def test_save_to_npy(self):
-        lp.save_to_npy(self.output, path='.')
+        lp.save_to_npy(self.output, path=".")
 
-        currents = np.load('currents.npy')
+        currents = np.load("currents.npy")
         self.assertEqual(self.currents[0], currents[0])
 
-        volts = np.load('volts.npy')
+        volts = np.load("volts.npy")
         self.assertEqual(self.volts[0, 0], volts[0, 0])
 
     def test_save_to_npz(self):
-        lp.save_to_npzcomp(self.output, path='.')
+        lp.save_to_npzcomp(self.output, path=".")
 
-        output = np.load('output.npz')
-        currents = output['currents']
+        output = np.load("output.npz")
+        currents = output["currents"]
         self.assertEqual(self.currents[0], currents[0])
 
-        output = np.load('output.npz')
-        volts = output['volts']
+        output = np.load("output.npz")
+        volts = output["volts"]
         self.assertEqual(self.volts[0, 0], volts[0, 0])
 
     def tearDown(self):
-        path = pathlib.Path('currents.csv')
+        path = pathlib.Path("currents.csv")
         path.unlink(missing_ok=True)
 
-        path = pathlib.Path('volts.csv')
+        path = pathlib.Path("volts.csv")
         path.unlink(missing_ok=True)
 
-        path = pathlib.Path('currents.npy')
+        path = pathlib.Path("currents.npy")
         path.unlink(missing_ok=True)
 
-        path = pathlib.Path('volts.npy')
+        path = pathlib.Path("volts.npy")
         path.unlink(missing_ok=True)
 
-        path = pathlib.Path('output.npz')
+        path = pathlib.Path("output.npz")
         path.unlink(missing_ok=True)
 
 
 if __name__ == "__main__":
     unittest.main()
```

### Comparing `liionpack-0.3.4/.gitignore` & `liionpack-0.3.5/.gitignore`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/LICENSE` & `liionpack-0.3.5/LICENSE`

 * *Files identical despite different names*

### Comparing `liionpack-0.3.4/README.md` & `liionpack-0.3.5/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 ![logo](https://raw.githubusercontent.com/pybamm-team/liionpack/main/docs/liionpack.png)
 
 #
 <div align="center">
 
 [![liionpack](https://github.com/pybamm-team/liionpack/actions/workflows/test_on_push.yml/badge.svg)](https://github.com/pybamm-team/liionpack/actions/workflows/test_on_push.yml)
-[![Documentation Status](https://readthedocs.org/projects/liionpack/badge/?version=main)](https://liionpack.readthedocs.io/en/main/?badge=main)
+[![Documentation Status](https://readthedocs.org/projects/liionpack/badge/?version=develop)](https://liionpack.readthedocs.io/en/develop/?badge=develop)
 [![codecov](https://codecov.io/gh/pybamm-team/liionpack/branch/main/graph/badge.svg)](https://codecov.io/gh/pybamm-team/liionpack)
 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pybamm-team/liionpack/blob/main/)
 [![DOI](https://joss.theoj.org/papers/10.21105/joss.04051/status.svg)](https://doi.org/10.21105/joss.04051)
 
 </div>
 
 # Overview of liionpack
```

### Comparing `liionpack-0.3.4/pyproject.toml` & `liionpack-0.3.5/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -30,15 +30,15 @@
     "lcapy",
     "matplotlib",
     "networkx",
     "numpy",
     "openpyxl",
     "pandas",
     "plotly",
-    "pybamm>=23.2",
+    "pybamm>=23.3",
     "ray",
     "redis",
     "scikit-spatial",
     "scipy",
     "textwrapper",
     "tqdm",
 ]
```

### Comparing `liionpack-0.3.4/PKG-INFO` & `liionpack-0.3.5/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: liionpack
-Version: 0.3.4
+Version: 0.3.5
 Summary: A battery pack simulator for PyBaMM
 Project-URL: Bug Tracker, https://github.com/pybamm-team/liionpack/issues
 Project-URL: Changelog, https://github.com/pybamm-team/liionpack/blob/develop/CHANGELOG.md
 Project-URL: Documentation, https://liionpack.readthedocs.io/en/latest/
 Project-URL: Homepage, https://github.com/pybamm-team/liionpack
 Author-email: Tom Tranter <t.g.tranter@gmail.com>
 License-Expression: MIT
@@ -24,30 +24,30 @@
 Requires-Dist: lcapy
 Requires-Dist: matplotlib
 Requires-Dist: networkx
 Requires-Dist: numpy
 Requires-Dist: openpyxl
 Requires-Dist: pandas
 Requires-Dist: plotly
-Requires-Dist: pybamm>=23.2
+Requires-Dist: pybamm>=23.3
 Requires-Dist: ray
 Requires-Dist: redis
 Requires-Dist: scikit-spatial
 Requires-Dist: scipy
 Requires-Dist: textwrapper
 Requires-Dist: tqdm
 Description-Content-Type: text/markdown
 
 ![logo](https://raw.githubusercontent.com/pybamm-team/liionpack/main/docs/liionpack.png)
 
 #
 <div align="center">
 
 [![liionpack](https://github.com/pybamm-team/liionpack/actions/workflows/test_on_push.yml/badge.svg)](https://github.com/pybamm-team/liionpack/actions/workflows/test_on_push.yml)
-[![Documentation Status](https://readthedocs.org/projects/liionpack/badge/?version=main)](https://liionpack.readthedocs.io/en/main/?badge=main)
+[![Documentation Status](https://readthedocs.org/projects/liionpack/badge/?version=develop)](https://liionpack.readthedocs.io/en/develop/?badge=develop)
 [![codecov](https://codecov.io/gh/pybamm-team/liionpack/branch/main/graph/badge.svg)](https://codecov.io/gh/pybamm-team/liionpack)
 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pybamm-team/liionpack/blob/main/)
 [![DOI](https://joss.theoj.org/papers/10.21105/joss.04051/status.svg)](https://doi.org/10.21105/joss.04051)
 
 </div>
 
 # Overview of liionpack
```

