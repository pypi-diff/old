# Comparing `tmp/squidasm-0.9.0a1.tar.gz` & `tmp/squidasm-0.9.0a2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "squidasm-0.9.0a1.tar", last modified: Tue May 10 12:53:21 2022, max compression
+gzip compressed data, was "squidasm-0.9.0a2.tar", last modified: Fri May 20 14:43:45 2022, max compression
```

## Comparing `squidasm-0.9.0a1.tar` & `squidasm-0.9.0a2.tar`

### file list

```diff
@@ -1,167 +1,169 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.427284 squidasm-0.9.0a1/
--rw-r--r--   0 runner    (1001) docker     (121)      371 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/.flake8
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.411284 squidasm-0.9.0a1/.github/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.415284 squidasm-0.9.0a1/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (121)     1157 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/.github/workflows/actions.yaml
--rw-r--r--   0 runner    (1001) docker     (121)     1053 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/.github/workflows/publish.yaml
--rw-r--r--   0 runner    (1001) docker     (121)      126 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/.gitignore
--rw-r--r--   0 runner    (1001) docker     (121)     1715 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/.gitlab-ci.yml
--rw-r--r--   0 runner    (1001) docker     (121)     3203 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/CHANGELOG.md
--rw-r--r--   0 runner    (1001) docker     (121)     1063 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      169 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     2069 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/Makefile
--rw-r--r--   0 runner    (1001) docker     (121)     4415 2022-05-10 12:53:21.427284 squidasm-0.9.0a1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     4059 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.415284 squidasm-0.9.0a1/docs/
--rw-r--r--   0 runner    (1001) docker     (121)      854 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/docs/Makefile
--rw-r--r--   0 runner    (1001) docker     (121)      474 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/docs/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      161 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/docs/api.rst
--rw-r--r--   0 runner    (1001) docker     (121)     2240 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/docs/conf.py
--rw-r--r--   0 runner    (1001) docker     (121)      481 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/docs/index.rst
--rw-r--r--   0 runner    (1001) docker     (121)      160 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/docs/installation.rst
--rw-r--r--   0 runner    (1001) docker     (121)      760 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/docs/make.bat
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.415284 squidasm-0.9.0a1/docs/modules/
--rw-r--r--   0 runner    (1001) docker     (121)      739 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/docs/modules/processor.rst
--rw-r--r--   0 runner    (1001) docker     (121)       52 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/docs/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)      191 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/docs/usage.rst
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.415284 squidasm-0.9.0a1/examples/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.415284 squidasm-0.9.0a1/examples/raw_subroutines/
--rw-r--r--   0 runner    (1001) docker     (121)     5748 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/raw_subroutines/example_bqc_subrt.py
--rw-r--r--   0 runner    (1001) docker     (121)     4918 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/raw_subroutines/example_ll_subrt.py
--rw-r--r--   0 runner    (1001) docker     (121)     1094 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/run_examples.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.411284 squidasm-0.9.0a1/examples/singlethread/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.415284 squidasm-0.9.0a1/examples/singlethread/bqc/
--rw-r--r--   0 runner    (1001) docker     (121)     2932 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/singlethread/bqc/app_client.py
--rw-r--r--   0 runner    (1001) docker     (121)     1799 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/singlethread/bqc/app_server.py
--rw-r--r--   0 runner    (1001) docker     (121)      583 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/singlethread/bqc/nv.yaml
--rw-r--r--   0 runner    (1001) docker     (121)     1527 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/singlethread/bqc/run.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.411284 squidasm-0.9.0a1/examples/stack/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/examples/stack/bqc/
--rw-r--r--   0 runner    (1001) docker     (121)     1128 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/bqc/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      587 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/bqc/config.yaml
--rw-r--r--   0 runner    (1001) docker     (121)      528 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/bqc/config_nv.yaml
--rw-r--r--   0 runner    (1001) docker     (121)     6819 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/bqc/example_bqc.py
--rw-r--r--   0 runner    (1001) docker     (121)     7034 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/bqc/example_bqc_nv.py
--rw-r--r--   0 runner    (1001) docker     (121)     4722 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/bqc/example_nv.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/examples/stack/bqc/fig/
--rw-r--r--   0 runner    (1001) docker     (121)    17137 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/bqc/fig/5_6_effective.png
--rw-r--r--   0 runner    (1001) docker     (121)    96935 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/bqc/fig/5_6_generic.png
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/examples/stack/fidelity_constraint/
--rw-r--r--   0 runner    (1001) docker     (121)      537 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/fidelity_constraint/config.yaml
--rw-r--r--   0 runner    (1001) docker     (121)      529 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/fidelity_constraint/config_nv.yaml
--rw-r--r--   0 runner    (1001) docker     (121)     7242 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/fidelity_constraint/example_bqc_nv_constraint.py
--rw-r--r--   0 runner    (1001) docker     (121)     3603 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/fidelity_constraint/example_fidelity.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/examples/stack/link_layer/
--rw-r--r--   0 runner    (1001) docker     (121)      980 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/link_layer/config.yaml
--rw-r--r--   0 runner    (1001) docker     (121)     3688 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/link_layer/example_link_layer_ck.py
--rw-r--r--   0 runner    (1001) docker     (121)     2903 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/link_layer/example_link_layer_md.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/examples/stack/link_layer_custom_subrt/
--rw-r--r--   0 runner    (1001) docker     (121)     5627 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/link_layer_custom_subrt/client.nqasm
--rw-r--r--   0 runner    (1001) docker     (121)     7209 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/link_layer_custom_subrt/example_ll_custom_subrt.py
--rw-r--r--   0 runner    (1001) docker     (121)     4167 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/link_layer_custom_subrt/server.nqasm
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/examples/stack/partial_bqc/
--rw-r--r--   0 runner    (1001) docker     (121)     3182 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/partial_bqc/example_bqc_5_2.py
--rw-r--r--   0 runner    (1001) docker     (121)     3023 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/partial_bqc/example_bqc_5_3.py
--rw-r--r--   0 runner    (1001) docker     (121)     3696 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/partial_bqc/example_bqc_5_4.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/examples/stack/qkd/
--rw-r--r--   0 runner    (1001) docker     (121)      218 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/qkd/config.yaml
--rw-r--r--   0 runner    (1001) docker     (121)     9714 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/qkd/example_qkd.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/examples/stack/single_node/
--rw-r--r--   0 runner    (1001) docker     (121)     1555 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/single_node/single_node.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/examples/stack/teleport/
--rw-r--r--   0 runner    (1001) docker     (121)     3584 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/examples/stack/teleport/example_teleport.py
--rw-r--r--   0 runner    (1001) docker     (121)       87 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/mypy.ini
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/pydynaa/
--rw-r--r--   0 runner    (1001) docker     (121)      619 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/pydynaa/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (121)      584 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)      862 2022-05-10 12:53:21.427284 squidasm-0.9.0a1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)       81 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/squidasm/
--rw-r--r--   0 runner    (1001) docker     (121)      174 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/squidasm/nqasm/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/nqasm/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/squidasm/nqasm/executor/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/nqasm/executor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9651 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/nqasm/executor/base.py
--rw-r--r--   0 runner    (1001) docker     (121)     3321 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/nqasm/executor/nv.py
--rw-r--r--   0 runner    (1001) docker     (121)     1919 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/nqasm/executor/vanilla.py
--rw-r--r--   0 runner    (1001) docker     (121)     3937 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/nqasm/multithread.py
--rw-r--r--   0 runner    (1001) docker     (121)     7635 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/nqasm/netstack.py
--rw-r--r--   0 runner    (1001) docker     (121)     2831 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/nqasm/output.py
--rw-r--r--   0 runner    (1001) docker     (121)     9025 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/nqasm/qnodeos.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/squidasm/nqasm/singlethread/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/nqasm/singlethread/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5438 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/nqasm/singlethread/connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     1506 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/nqasm/singlethread/csocket.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.423284 squidasm-0.9.0a1/squidasm/run/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.423284 squidasm-0.9.0a1/squidasm/run/multithread/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/multithread/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8891 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/multithread/runtime_mgr.py
--rw-r--r--   0 runner    (1001) docker     (121)     3448 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/multithread/simulate.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.423284 squidasm-0.9.0a1/squidasm/run/singlethread/
--rw-r--r--   0 runner    (1001) docker     (121)       93 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/singlethread/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1621 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/singlethread/context.py
--rw-r--r--   0 runner    (1001) docker     (121)     8760 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/singlethread/protocols.py
--rw-r--r--   0 runner    (1001) docker     (121)     4685 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/singlethread/run.py
--rw-r--r--   0 runner    (1001) docker     (121)     1796 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/singlethread/util.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.423284 squidasm-0.9.0a1/squidasm/run/stack/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/stack/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6646 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/stack/build.py
--rw-r--r--   0 runner    (1001) docker     (121)     5065 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/stack/config.py
--rw-r--r--   0 runner    (1001) docker     (121)     5991 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/run/stack/run.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.423284 squidasm-0.9.0a1/squidasm/sim/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4734 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/glob.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.423284 squidasm-0.9.0a1/squidasm/sim/network/
--rw-r--r--   0 runner    (1001) docker     (121)       91 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/network/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    23232 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/network/network.py
--rw-r--r--   0 runner    (1001) docker     (121)     7717 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/network/nv_config.py
--rw-r--r--   0 runner    (1001) docker     (121)     2225 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/queues.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.423284 squidasm-0.9.0a1/squidasm/sim/stack/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.427284 squidasm-0.9.0a1/squidasm/sim/stack/arch/
--rw-r--r--   0 runner    (1001) docker     (121)       27 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/arch/ARCH.md
--rw-r--r--   0 runner    (1001) docker     (121)     5867 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/arch/arch.drawio
--rw-r--r--   0 runner    (1001) docker     (121)    56612 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/arch/arch.png
--rw-r--r--   0 runner    (1001) docker     (121)     9360 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/arch/comn.drawio
--rw-r--r--   0 runner    (1001) docker     (121)    34489 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/arch/comn.png
--rw-r--r--   0 runner    (1001) docker     (121)    13288 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/common.py
--rw-r--r--   0 runner    (1001) docker     (121)     3501 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/connection.py
--rw-r--r--   0 runner    (1001) docker     (121)     1569 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/context.py
--rw-r--r--   0 runner    (1001) docker     (121)     1618 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/csocket.py
--rw-r--r--   0 runner    (1001) docker     (121)     3615 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/egp.py
--rw-r--r--   0 runner    (1001) docker     (121)     1552 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/globals.py
--rw-r--r--   0 runner    (1001) docker     (121)    10221 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/handler.py
--rw-r--r--   0 runner    (1001) docker     (121)     6895 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/host.py
--rw-r--r--   0 runner    (1001) docker     (121)    31371 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/netstack.py
--rw-r--r--   0 runner    (1001) docker     (121)    35811 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/processor.py
--rw-r--r--   0 runner    (1001) docker     (121)     1323 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/program.py
--rw-r--r--   0 runner    (1001) docker     (121)     6360 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/qnos.py
--rw-r--r--   0 runner    (1001) docker     (121)      351 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/signals.py
--rw-r--r--   0 runner    (1001) docker     (121)     7822 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/sim/stack/stack.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.427284 squidasm-0.9.0a1/squidasm/util/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/util/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3337 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/util/ns.py
--rw-r--r--   0 runner    (1001) docker     (121)     2173 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/util/sim.py
--rw-r--r--   0 runner    (1001) docker     (121)      520 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/squidasm/util/thread.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.419284 squidasm-0.9.0a1/squidasm.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     4415 2022-05-10 12:53:20.000000 squidasm-0.9.0a1/squidasm.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3926 2022-05-10 12:53:21.000000 squidasm-0.9.0a1/squidasm.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-10 12:53:20.000000 squidasm-0.9.0a1/squidasm.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      290 2022-05-10 12:53:21.000000 squidasm-0.9.0a1/squidasm.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        9 2022-05-10 12:53:21.000000 squidasm-0.9.0a1/squidasm.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.427284 squidasm-0.9.0a1/tests/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-10 12:53:21.427284 squidasm-0.9.0a1/tests/stack/
--rw-r--r--   0 runner    (1001) docker     (121)     1257 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/tests/stack/test_components.py
--rw-r--r--   0 runner    (1001) docker     (121)     5273 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/tests/stack/test_handler.py
--rw-r--r--   0 runner    (1001) docker     (121)    15828 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/tests/stack/test_processor.py
--rw-r--r--   0 runner    (1001) docker     (121)     8852 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/tests/stack/test_sdk.py
--rw-r--r--   0 runner    (1001) docker     (121)     5768 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/tests/stack/test_single_node.py
--rw-r--r--   0 runner    (1001) docker     (121)    22738 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/tests/stack/test_two_nodes.py
--rw-r--r--   0 runner    (1001) docker     (121)     4031 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/tests/test_async_scenarios.py
--rw-r--r--   0 runner    (1001) docker     (121)     1365 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/tests/test_executor.py
--rw-r--r--   0 runner    (1001) docker     (121)     3310 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/tests/test_ns_util.py
--rw-r--r--   0 runner    (1001) docker     (121)     1612 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/tests/test_qnodeos.py
--rw-r--r--   0 runner    (1001) docker     (121)     2464 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/tests/test_run.py
--rw-r--r--   0 runner    (1001) docker     (121)      514 2022-05-10 12:53:11.000000 squidasm-0.9.0a1/tests/test_simulate.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.014455 squidasm-0.9.0a2/
+-rw-r--r--   0 runner    (1001) docker     (121)      371 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/.flake8
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.002456 squidasm-0.9.0a2/.github/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.002456 squidasm-0.9.0a2/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (121)     1175 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/.github/workflows/actions.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)     1112 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/.github/workflows/publish.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)      126 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (121)     1715 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/.gitlab-ci.yml
+-rw-r--r--   0 runner    (1001) docker     (121)     3203 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/CHANGELOG.md
+-rw-r--r--   0 runner    (1001) docker     (121)     1063 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      169 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     2082 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/Makefile
+-rw-r--r--   0 runner    (1001) docker     (121)     4396 2022-05-20 14:43:45.014455 squidasm-0.9.0a2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     4059 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.002456 squidasm-0.9.0a2/docs/
+-rw-r--r--   0 runner    (1001) docker     (121)      854 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/docs/Makefile
+-rw-r--r--   0 runner    (1001) docker     (121)      474 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/docs/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      161 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/docs/api.rst
+-rw-r--r--   0 runner    (1001) docker     (121)     2240 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/docs/conf.py
+-rw-r--r--   0 runner    (1001) docker     (121)      481 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/docs/index.rst
+-rw-r--r--   0 runner    (1001) docker     (121)      160 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/docs/installation.rst
+-rw-r--r--   0 runner    (1001) docker     (121)      760 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/docs/make.bat
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.002456 squidasm-0.9.0a2/docs/modules/
+-rw-r--r--   0 runner    (1001) docker     (121)      739 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/docs/modules/processor.rst
+-rw-r--r--   0 runner    (1001) docker     (121)       52 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/docs/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      191 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/docs/usage.rst
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.002456 squidasm-0.9.0a2/examples/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/examples/raw_subroutines/
+-rw-r--r--   0 runner    (1001) docker     (121)     5748 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/raw_subroutines/example_bqc_subrt.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4918 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/raw_subroutines/example_ll_subrt.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1094 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/run_examples.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.002456 squidasm-0.9.0a2/examples/singlethread/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/examples/singlethread/bqc/
+-rw-r--r--   0 runner    (1001) docker     (121)     2936 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/singlethread/bqc/app_client.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1803 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/singlethread/bqc/app_server.py
+-rw-r--r--   0 runner    (1001) docker     (121)      583 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/singlethread/bqc/nv.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)     1703 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/singlethread/bqc/run.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.002456 squidasm-0.9.0a2/examples/stack/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/examples/stack/bqc/
+-rw-r--r--   0 runner    (1001) docker     (121)     1128 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/bqc/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      587 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/bqc/config.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)      528 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/bqc/config_nv.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)     6773 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/bqc/example_bqc.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6985 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/bqc/example_bqc_nv.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4680 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/bqc/example_nv.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/examples/stack/bqc/fig/
+-rw-r--r--   0 runner    (1001) docker     (121)    17137 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/bqc/fig/5_6_effective.png
+-rw-r--r--   0 runner    (1001) docker     (121)    96935 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/bqc/fig/5_6_generic.png
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/examples/stack/fidelity_constraint/
+-rw-r--r--   0 runner    (1001) docker     (121)      537 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/fidelity_constraint/config.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)      529 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/fidelity_constraint/config_nv.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)     7185 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/fidelity_constraint/example_bqc_nv_constraint.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3564 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/fidelity_constraint/example_fidelity.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/examples/stack/link_layer/
+-rw-r--r--   0 runner    (1001) docker     (121)      980 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/link_layer/config.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)     3688 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/link_layer/example_link_layer_ck.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2905 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/link_layer/example_link_layer_md.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/examples/stack/link_layer_custom_subrt/
+-rw-r--r--   0 runner    (1001) docker     (121)     5627 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/link_layer_custom_subrt/client.nqasm
+-rw-r--r--   0 runner    (1001) docker     (121)     7225 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/link_layer_custom_subrt/example_ll_custom_subrt.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4167 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/link_layer_custom_subrt/server.nqasm
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/examples/stack/partial_bqc/
+-rw-r--r--   0 runner    (1001) docker     (121)     3083 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/partial_bqc/example_bqc_5_2.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3023 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/partial_bqc/example_bqc_5_3.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3696 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/partial_bqc/example_bqc_5_4.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/examples/stack/precompilation/
+-rw-r--r--   0 runner    (1001) docker     (121)     4419 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/precompilation/example_bqc_5_4_precompiled.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/examples/stack/qkd/
+-rw-r--r--   0 runner    (1001) docker     (121)      218 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/qkd/config.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)     9714 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/qkd/example_qkd.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/examples/stack/single_node/
+-rw-r--r--   0 runner    (1001) docker     (121)     1564 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/single_node/single_node.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/examples/stack/teleport/
+-rw-r--r--   0 runner    (1001) docker     (121)     3584 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/examples/stack/teleport/example_teleport.py
+-rw-r--r--   0 runner    (1001) docker     (121)       87 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/mypy.ini
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/pydynaa/
+-rw-r--r--   0 runner    (1001) docker     (121)      619 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/pydynaa/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (121)      584 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)      867 2022-05-20 14:43:45.014455 squidasm-0.9.0a2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)       81 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/squidasm/
+-rw-r--r--   0 runner    (1001) docker     (121)      174 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/squidasm/nqasm/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/nqasm/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.010455 squidasm-0.9.0a2/squidasm/nqasm/executor/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/nqasm/executor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9651 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/nqasm/executor/base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3321 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/nqasm/executor/nv.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1919 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/nqasm/executor/vanilla.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3945 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/nqasm/multithread.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7635 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/nqasm/netstack.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2831 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/nqasm/output.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9025 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/nqasm/qnodeos.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.010455 squidasm-0.9.0a2/squidasm/nqasm/singlethread/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/nqasm/singlethread/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5466 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/nqasm/singlethread/connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1506 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/nqasm/singlethread/csocket.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.010455 squidasm-0.9.0a2/squidasm/run/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.010455 squidasm-0.9.0a2/squidasm/run/multithread/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/multithread/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8891 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/multithread/runtime_mgr.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3448 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/multithread/simulate.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.010455 squidasm-0.9.0a2/squidasm/run/singlethread/
+-rw-r--r--   0 runner    (1001) docker     (121)       93 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/singlethread/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1621 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/singlethread/context.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8760 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/singlethread/protocols.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4685 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/singlethread/run.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1796 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/singlethread/util.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.010455 squidasm-0.9.0a2/squidasm/run/stack/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/stack/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6646 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/stack/build.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5065 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/stack/config.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5991 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/run/stack/run.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.010455 squidasm-0.9.0a2/squidasm/sim/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4734 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/glob.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.010455 squidasm-0.9.0a2/squidasm/sim/network/
+-rw-r--r--   0 runner    (1001) docker     (121)       91 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/network/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23232 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/network/network.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7717 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/network/nv_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2225 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/queues.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.010455 squidasm-0.9.0a2/squidasm/sim/stack/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.010455 squidasm-0.9.0a2/squidasm/sim/stack/arch/
+-rw-r--r--   0 runner    (1001) docker     (121)       27 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/arch/ARCH.md
+-rw-r--r--   0 runner    (1001) docker     (121)     5867 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/arch/arch.drawio
+-rw-r--r--   0 runner    (1001) docker     (121)    56612 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/arch/arch.png
+-rw-r--r--   0 runner    (1001) docker     (121)     9360 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/arch/comn.drawio
+-rw-r--r--   0 runner    (1001) docker     (121)    34489 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/arch/comn.png
+-rw-r--r--   0 runner    (1001) docker     (121)    13288 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/common.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3918 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/connection.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1569 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/context.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1618 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/csocket.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3615 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/egp.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1552 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/globals.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10221 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/handler.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6939 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/host.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31344 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/netstack.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35819 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/processor.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1323 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/program.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6360 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/qnos.py
+-rw-r--r--   0 runner    (1001) docker     (121)      351 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/signals.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7822 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/sim/stack/stack.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.014455 squidasm-0.9.0a2/squidasm/util/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/util/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3337 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/util/ns.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2173 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/util/sim.py
+-rw-r--r--   0 runner    (1001) docker     (121)      520 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/squidasm/util/thread.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.006456 squidasm-0.9.0a2/squidasm.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     4396 2022-05-20 14:43:44.000000 squidasm-0.9.0a2/squidasm.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     3987 2022-05-20 14:43:44.000000 squidasm-0.9.0a2/squidasm.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-20 14:43:44.000000 squidasm-0.9.0a2/squidasm.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      295 2022-05-20 14:43:44.000000 squidasm-0.9.0a2/squidasm.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        9 2022-05-20 14:43:44.000000 squidasm-0.9.0a2/squidasm.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.014455 squidasm-0.9.0a2/tests/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-20 14:43:45.014455 squidasm-0.9.0a2/tests/stack/
+-rw-r--r--   0 runner    (1001) docker     (121)     1257 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/tests/stack/test_components.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5273 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/tests/stack/test_handler.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15828 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/tests/stack/test_processor.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8852 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/tests/stack/test_sdk.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5768 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/tests/stack/test_single_node.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22738 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/tests/stack/test_two_nodes.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4031 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/tests/test_async_scenarios.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1365 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/tests/test_executor.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3310 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/tests/test_ns_util.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1612 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/tests/test_qnodeos.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2464 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/tests/test_run.py
+-rw-r--r--   0 runner    (1001) docker     (121)      514 2022-05-20 14:43:33.000000 squidasm-0.9.0a2/tests/test_simulate.py
```

### Comparing `squidasm-0.9.0a1/.github/workflows/actions.yaml` & `squidasm-0.9.0a2/.github/workflows/actions.yaml`

 * *Files 26% similar despite different names*

```diff
@@ -11,39 +11,39 @@
     - uses: actions/setup-python@master
       with:
         python-version: 3.8
     - env:
           NETSQUIDPYPI_USER: ${{ secrets.NETSQUIDPYPI_USER }}
           NETSQUIDPYPI_PWD: ${{ secrets.NETSQUIDPYPI_PWD }}
       run: |
-        make install
+        make install-tests
         make lint
 
   tests:
     name: Run tests  
     runs-on: ubuntu-latest
     steps:
     - uses: actions/checkout@master
     - uses: actions/setup-python@master
       with:
         python-version: 3.8
     - env:
           NETSQUIDPYPI_USER: ${{ secrets.NETSQUIDPYPI_USER }}
           NETSQUIDPYPI_PWD: ${{ secrets.NETSQUIDPYPI_PWD }}
       run: |
-        make install
+        make install-tests
         make tests
 
   examples:
     name: Run examples
     runs-on: ubuntu-latest
     steps:
     - uses: actions/checkout@master
     - uses: actions/setup-python@master
       with:
         python-version: 3.8
     - env:
           NETSQUIDPYPI_USER: ${{ secrets.NETSQUIDPYPI_USER }}
           NETSQUIDPYPI_PWD: ${{ secrets.NETSQUIDPYPI_PWD }}
       run: |
-        make install
+        make install-tests
         make examples
```

### Comparing `squidasm-0.9.0a1/.github/workflows/publish.yaml` & `squidasm-0.9.0a2/.github/workflows/publish.yaml`

 * *Files 9% similar despite different names*

```diff
@@ -22,16 +22,17 @@
         python -m
         build
         --sdist
         --wheel
         --outdir dist/
         .
     - name: Publish distribution 📦 to Test PyPI
+      if: startsWith(github.ref, 'refs/tags')
       uses: pypa/gh-action-pypi-publish@master
       with:
         password: ${{ secrets.TEST_PYPI_API_TOKEN }}
         repository_url: https://test.pypi.org/legacy/
     - name: Publish distribution 📦 to PyPI
-      if: startsWith(github.ref, 'refs/tags')
+      if: success() && startsWith(github.ref, 'refs/tags')
       uses: pypa/gh-action-pypi-publish@master
       with:
         password: ${{ secrets.PYPI_API_TOKEN }}
```

### Comparing `squidasm-0.9.0a1/.gitlab-ci.yml` & `squidasm-0.9.0a2/.gitlab-ci.yml`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/CHANGELOG.md` & `squidasm-0.9.0a2/CHANGELOG.md`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/LICENSE` & `squidasm-0.9.0a2/LICENSE`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/Makefile` & `squidasm-0.9.0a2/Makefile`

 * *Files 9% similar despite different names*

```diff
@@ -56,15 +56,15 @@
 docs html:
 	@${MAKE} -C docs html
 
 install: _check_variables
 	@$(PYTHON3) -m pip install -e . ${PIP_FLAGS}
 
 install-tests: _check_variables
-	@$(PYTHON3) -m pip install -e .[tests]
+	@$(PYTHON3) -m pip install -e .[tests] ${PIP_FLAGS}
 
 verify: clean test-deps python-deps lint tests examples _verified
 
 _verified:
 	@echo "Everything works!"
 
 .PHONY: clean lint test-deps python-deps tests verify install examples docs
```

### Comparing `squidasm-0.9.0a1/PKG-INFO` & `squidasm-0.9.0a2/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,15 @@
 Metadata-Version: 2.1
 Name: squidasm
-Version: 0.9.0a1
+Version: 0.9.0a2
 Summary: NetSquid simulator for quantum networks running NetQASM applications
 Home-page: https://github.com/QuTech-Delft/squidasm
 Author: QuTech
 Author-email: b.vandervecht@tudelft.nl
 License: MIT
-Platform: UNKNOWN
 Description-Content-Type: text/markdown
 Provides-Extra: tests
 License-File: LICENSE
 
 # SquidASM
 
 This is SquidASM, a simulator based on NetSquid that can execute applications written using NetQASM.
@@ -98,8 +97,7 @@
 Before code is pushed, make sure that the `make lint` command succeeds, which runs `black`, `isort` and `flake8`.
 
 
 # Contributors
 In alphabetical order:
 - Axel Dahlberg
 - Bart van der Vecht (b.vandervecht[at]tudelft.nl)
-
```

### Comparing `squidasm-0.9.0a1/README.md` & `squidasm-0.9.0a2/README.md`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/docs/Makefile` & `squidasm-0.9.0a2/docs/Makefile`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/docs/conf.py` & `squidasm-0.9.0a2/docs/conf.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/docs/make.bat` & `squidasm-0.9.0a2/docs/make.bat`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/docs/modules/processor.rst` & `squidasm-0.9.0a2/docs/modules/processor.rst`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/raw_subroutines/example_bqc_subrt.py` & `squidasm-0.9.0a2/examples/raw_subroutines/example_bqc_subrt.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/raw_subroutines/example_ll_subrt.py` & `squidasm-0.9.0a2/examples/raw_subroutines/example_ll_subrt.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/run_examples.py` & `squidasm-0.9.0a2/examples/run_examples.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/singlethread/bqc/app_client.py` & `squidasm-0.9.0a2/examples/singlethread/bqc/app_client.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import math
 
 from netqasm.sdk import EPRSocket
-from netqasm.sdk.compiling import NVSubroutineCompiler
 from netqasm.sdk.connection import DebugConnection
 from netqasm.sdk.external import NetQASMConnection, Socket
+from netqasm.sdk.transpile import NVSubroutineTranspiler
 
 
 def main(
     app_config={"addr": "192.168.2.215", "port": 1275, "dev": "", "debug": False},
     inputs={
         "alpha": math.pi / 2,
         "beta": math.pi / 2,
@@ -40,15 +40,15 @@
     epr_socket = EPRSocket("server", min_fidelity=75)
 
     # Initialize the connection
     kwargs = {
         "app_name": "client",
         "log_config": None,
         "epr_sockets": [epr_socket],
-        "compiler": NVSubroutineCompiler,
+        "compiler": NVSubroutineTranspiler,
         "return_arrays": False,
     }
 
     # Initialize the connection
     if not app_config["debug"]:
         client = NetQASMConnection(
             **kwargs,
```

### Comparing `squidasm-0.9.0a1/examples/singlethread/bqc/app_server.py` & `squidasm-0.9.0a2/examples/singlethread/bqc/app_server.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from netqasm.sdk import EPRSocket
-from netqasm.sdk.compiling import NVSubroutineCompiler
 from netqasm.sdk.connection import DebugConnection
 from netqasm.sdk.external import NetQASMConnection, Socket
+from netqasm.sdk.transpile import NVSubroutineTranspiler
 
 
 def main(
     app_config={"addr": "192.168.2.215", "port": 1275, "dev": "", "debug": False},
     inputs={},
 ):
 
@@ -15,15 +15,15 @@
     epr_socket = EPRSocket("client", min_fidelity=75)
 
     # Initialize the connection
     kwargs = {
         "app_name": "server",
         "log_config": None,
         "epr_sockets": [epr_socket],
-        "compiler": NVSubroutineCompiler,
+        "compiler": NVSubroutineTranspiler,
         "return_arrays": False,
     }
 
     # Initialize the connection
     if not app_config["debug"]:
         server = NetQASMConnection(
             **kwargs,
```

### Comparing `squidasm-0.9.0a1/examples/singlethread/bqc/nv.yaml` & `squidasm-0.9.0a2/examples/singlethread/bqc/nv.yaml`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/singlethread/bqc/run.py` & `squidasm-0.9.0a2/examples/singlethread/bqc/run.py`

 * *Files 14% similar despite different names*

```diff
@@ -25,14 +25,18 @@
     NetSquidContext.set_nodes({0: "server", 1: "client"})
 
     client = "./app_client.py"
     server = "./app_server.py"
 
     start = time.perf_counter()
 
+    # NOTE: this example is broken. It will however be removed anyway when #18 is addressed
+    # (which removes the deprecated singlethread simulator altogether).
+    return
+
     num = 20
     results = run_files(
         num=num,
         network=network,
         filenames={"client": client, "server": server},
         insert_yields=True,  # add required `yield from` keywords to source
     )
```

### Comparing `squidasm-0.9.0a1/examples/stack/bqc/README.md` & `squidasm-0.9.0a2/examples/stack/bqc/README.md`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/bqc/config.yaml` & `squidasm-0.9.0a2/examples/stack/bqc/config.yaml`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/bqc/config_nv.yaml` & `squidasm-0.9.0a2/examples/stack/bqc/config_nv.yaml`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/bqc/example_bqc.py` & `squidasm-0.9.0a2/examples/stack/bqc/example_bqc.py`

 * *Files 8% similar despite different names*

```diff
@@ -239,15 +239,14 @@
     frac_fail = round(num_fails / num_times, 2)
     print(f"fail rate: {frac_fail}")
 
 
 if __name__ == "__main__":
     num_times = 1
     LogManager.set_log_level("WARNING")
-    LogManager.log_to_file("example_bqc.log")
     # ns.set_qstate_formalism(ns.qubits.qformalism.QFormalism.DM)
 
     cfg_file = os.path.join(os.path.dirname(__file__), "config.yaml")
     cfg = StackNetworkConfig.from_file(cfg_file)
 
     computation_round(cfg, num_times, alpha=PI_OVER_2, beta=PI_OVER_2)
     trap_round(cfg, num_times, dummy=1)
```

### Comparing `squidasm-0.9.0a1/examples/stack/bqc/example_bqc_nv.py` & `squidasm-0.9.0a2/examples/stack/bqc/example_bqc_nv.py`

 * *Files 2% similar despite different names*

```diff
@@ -236,15 +236,14 @@
     print(f"fail rate: {frac_fail}")
 
 
 if __name__ == "__main__":
     num_times = 100
     LogManager.set_log_level("WARNING")
 
-    LogManager.log_to_file("example_bqc_nv.log")
     ns.set_qstate_formalism(ns.qubits.qformalism.QFormalism.DM)
 
     cfg_file = os.path.join(os.path.dirname(__file__), "config_nv.yaml")
     cfg = StackNetworkConfig.from_file(cfg_file)
     cfg.stacks[0].qdevice_cfg = NVQDeviceConfig.perfect_config()
     cfg.stacks[1].qdevice_cfg = NVQDeviceConfig.perfect_config()
```

### Comparing `squidasm-0.9.0a1/examples/stack/bqc/example_nv.py` & `squidasm-0.9.0a2/examples/stack/bqc/example_nv.py`

 * *Files 4% similar despite different names*

```diff
@@ -158,15 +158,14 @@
     print(f"epr2 errors: {epr2_errors}")
 
 
 if __name__ == "__main__":
     num_times = 100
     LogManager.set_log_level("WARNING")
 
-    LogManager.log_to_file("dump_nv.log")
     ns.set_qstate_formalism(ns.qubits.qformalism.QFormalism.DM)
 
     cfg_file = os.path.join(os.path.dirname(__file__), "config_nv.yaml")
     cfg = StackNetworkConfig.from_file(cfg_file)
     cfg.stacks[0].qdevice_cfg = NVQDeviceConfig.perfect_config()
     cfg.stacks[1].qdevice_cfg = NVQDeviceConfig.perfect_config()
```

### Comparing `squidasm-0.9.0a1/examples/stack/bqc/fig/5_6_effective.png` & `squidasm-0.9.0a2/examples/stack/bqc/fig/5_6_effective.png`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/bqc/fig/5_6_generic.png` & `squidasm-0.9.0a2/examples/stack/bqc/fig/5_6_generic.png`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/fidelity_constraint/config.yaml` & `squidasm-0.9.0a2/examples/stack/fidelity_constraint/config.yaml`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/fidelity_constraint/config_nv.yaml` & `squidasm-0.9.0a2/examples/stack/fidelity_constraint/config_nv.yaml`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/fidelity_constraint/example_bqc_nv_constraint.py` & `squidasm-0.9.0a2/examples/stack/fidelity_constraint/example_bqc_nv_constraint.py`

 * *Files 4% similar despite different names*

```diff
@@ -242,15 +242,14 @@
     print(f"fail rate: {frac_fail}")
 
 
 if __name__ == "__main__":
     num_times = 50
     LogManager.set_log_level("WARNING")
 
-    LogManager.log_to_file("dump_bqc_nv_constraint.log")
     ns.set_qstate_formalism(ns.qubits.qformalism.QFormalism.DM)
 
     cfg_file = os.path.join(os.path.dirname(__file__), "config_nv.yaml")
     cfg = StackNetworkConfig.from_file(cfg_file)
     cfg.stacks[0].qdevice_cfg = NVQDeviceConfig.perfect_config()
     cfg.stacks[1].qdevice_cfg = NVQDeviceConfig.perfect_config()
```

### Comparing `squidasm-0.9.0a1/examples/stack/fidelity_constraint/example_fidelity.py` & `squidasm-0.9.0a2/examples/stack/fidelity_constraint/example_fidelity.py`

 * *Files 9% similar despite different names*

```diff
@@ -132,14 +132,13 @@
         cfg, {"client": client_program, "server": server_program}, num_times=num_times
     )
 
 
 if __name__ == "__main__":
     num_times = 1
     LogManager.set_log_level("WARNING")
-    LogManager.log_to_file("dump.log")
     ns.set_qstate_formalism(ns.qubits.qformalism.QFormalism.DM)
 
     cfg_file = os.path.join(os.path.dirname(__file__), "config.yaml")
     cfg = StackNetworkConfig.from_file(cfg_file)
 
     run_app(cfg, num_times, alpha=PI_OVER_2, beta=PI_OVER_2)
```

### Comparing `squidasm-0.9.0a1/examples/stack/link_layer/config.yaml` & `squidasm-0.9.0a2/examples/stack/link_layer/config.yaml`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/link_layer/example_link_layer_ck.py` & `squidasm-0.9.0a2/examples/stack/link_layer/example_link_layer_ck.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/link_layer/example_link_layer_md.py` & `squidasm-0.9.0a2/examples/stack/link_layer/example_link_layer_md.py`

 * *Files 1% similar despite different names*

```diff
@@ -71,15 +71,15 @@
 
         outcomes = [int(r.measurement_outcome) for r in results]
 
         return outcomes
 
 
 if __name__ == "__main__":
-    LogManager.set_log_level("DEBUG")
+    LogManager.set_log_level("WARNING")
 
     num_times = 1
     cfg = StackNetworkConfig.from_file(
         os.path.join(os.getcwd(), os.path.dirname(__file__), "config.yaml")
     )
 
     num_pairs = 10
```

### Comparing `squidasm-0.9.0a1/examples/stack/link_layer_custom_subrt/client.nqasm` & `squidasm-0.9.0a2/examples/stack/link_layer_custom_subrt/client.nqasm`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/link_layer_custom_subrt/example_ll_custom_subrt.py` & `squidasm-0.9.0a2/examples/stack/link_layer_custom_subrt/example_ll_custom_subrt.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 import os
 from math import pi
 from typing import Any, Dict, Generator
 
-from netqasm.lang.parsing.text import parse_text_presubroutine
+from netqasm.lang.parsing.text import parse_text_protosubroutine
 from netqasm.sdk import Qubit
 from netqasm.sdk.futures import Array
 
 from pydynaa import EventExpression
 from squidasm.run.stack.config import (
     LinkConfig,
     NVQDeviceConfig,
@@ -16,20 +16,20 @@
 from squidasm.run.stack.run import run
 from squidasm.sim.stack.common import LogManager
 from squidasm.sim.stack.program import Program, ProgramContext, ProgramMeta
 
 client_subrt_path = os.path.join(os.path.dirname(__file__), "client.nqasm")
 with open(client_subrt_path) as f:
     client_subrt_text = f.read()
-CLIENT_SUBRT = parse_text_presubroutine(client_subrt_text)
+CLIENT_SUBRT = parse_text_protosubroutine(client_subrt_text)
 
 server_subrt_path = os.path.join(os.path.dirname(__file__), "server.nqasm")
 with open(server_subrt_path) as f:
     server_subrt_text = f.read()
-SERVER_SUBRT = parse_text_presubroutine(server_subrt_text)
+SERVER_SUBRT = parse_text_protosubroutine(server_subrt_text)
 
 MIN_FIDELITY_LIST = [60, 65]
 
 USE_CUSTOM_SUBROUTINES = True
 
 
 class FidelityVsRateProgram(Program):
@@ -105,15 +105,15 @@
             max_qubits=1,
         )
 
     def run(
         self, context: ProgramContext
     ) -> Generator[EventExpression, None, Dict[str, Any]]:
         if USE_CUSTOM_SUBROUTINES:
-            yield from context.connection.commit_subroutine(CLIENT_SUBRT)
+            yield from context.connection.commit_protosubroutine(CLIENT_SUBRT)
             return {
                 "fidelity 60": context.connection.shared_memory.get_array(0),
                 "fidelity 65": context.connection.shared_memory.get_array(1),
             }
         else:
             outcomes = self._create_outcomes_dict(context)
 
@@ -152,15 +152,15 @@
             max_qubits=1,
         )
 
     def run(
         self, context: ProgramContext
     ) -> Generator[EventExpression, None, Dict[str, Any]]:
         if USE_CUSTOM_SUBROUTINES:
-            yield from context.connection.commit_subroutine(SERVER_SUBRT)
+            yield from context.connection.commit_protosubroutine(SERVER_SUBRT)
             return {
                 "fidelity 60": context.connection.shared_memory.get_array(0),
                 "fidelity 65": context.connection.shared_memory.get_array(1),
             }
         else:
             outcomes = self._create_outcomes_dict(context)
```

### Comparing `squidasm-0.9.0a1/examples/stack/link_layer_custom_subrt/server.nqasm` & `squidasm-0.9.0a2/examples/stack/link_layer_custom_subrt/server.nqasm`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/partial_bqc/example_bqc_5_2.py` & `squidasm-0.9.0a2/examples/stack/partial_bqc/example_bqc_5_2.py`

 * *Files 24% similar despite different names*

```diff
@@ -8,15 +8,14 @@
 from squidasm.run.stack.config import (
     GenericQDeviceConfig,
     LinkConfig,
     StackConfig,
     StackNetworkConfig,
 )
 from squidasm.run.stack.run import run
-from squidasm.sim.stack.common import LogManager
 from squidasm.sim.stack.csocket import ClassicalSocket
 from squidasm.sim.stack.program import Program, ProgramContext, ProgramMeta
 
 
 class ClientProgram(Program):
     PEER = "server"
 
@@ -92,15 +91,14 @@
         yield from conn.flush()
         m2 = int(m2)
 
         return {"m1": m1, "m2": m2}
 
 
 if __name__ == "__main__":
-    LogManager.log_to_file("example_bqc_5_2.log")
 
     client_stack = StackConfig(
         name="client",
         qdevice_typ="generic",
         qdevice_cfg=GenericQDeviceConfig.perfect_config(),
     )
     server_stack = StackConfig(
```

### Comparing `squidasm-0.9.0a1/examples/stack/partial_bqc/example_bqc_5_3.py` & `squidasm-0.9.0a2/examples/stack/partial_bqc/example_bqc_5_3.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/partial_bqc/example_bqc_5_4.py` & `squidasm-0.9.0a2/examples/stack/partial_bqc/example_bqc_5_4.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/qkd/example_qkd.py` & `squidasm-0.9.0a2/examples/stack/qkd/example_qkd.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/examples/stack/single_node/single_node.py` & `squidasm-0.9.0a2/examples/stack/single_node/single_node.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 from typing import Any, Dict, Generator
 
-from netqasm.lang.parsing.text import parse_text_presubroutine
+from netqasm.lang.parsing.text import parse_text_protosubroutine
 from netqasm.sdk.qubit import Qubit
 
 from pydynaa import EventExpression
 from squidasm.run.stack.config import NVQDeviceConfig, StackConfig, StackNetworkConfig
 from squidasm.run.stack.run import run
 from squidasm.sim.stack.common import LogManager
 from squidasm.sim.stack.program import Program, ProgramContext, ProgramMeta
@@ -39,16 +39,16 @@
         self, context: ProgramContext
     ) -> Generator[EventExpression, None, Dict[str, Any]]:
         conn = context.connection
 
         q = Qubit(conn)
         m = q.measure()
         # yield from conn.flush()
-        subrt = parse_text_presubroutine(SUBRT)
-        yield from conn.commit_subroutine(subrt)
+        subrt = parse_text_protosubroutine(SUBRT)
+        yield from conn.commit_protosubroutine(subrt)
 
         return {"m": int(m)}
 
 
 if __name__ == "__main__":
     LogManager.set_log_level("WARNING")
```

### Comparing `squidasm-0.9.0a1/examples/stack/teleport/example_teleport.py` & `squidasm-0.9.0a2/examples/stack/teleport/example_teleport.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/pydynaa/__init__.pyi` & `squidasm-0.9.0a2/pydynaa/__init__.pyi`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/pyproject.toml` & `squidasm-0.9.0a2/pyproject.toml`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/setup.cfg` & `squidasm-0.9.0a2/setup.cfg`

 * *Files 2% similar despite different names*

```diff
@@ -18,15 +18,15 @@
 	numpy >=1.22, <1.23
 	scipy >=1.8, <1.9
 	pydantic >=1.8.2
 	pydynaa >=0.3, <1.0
 	netsquid >=1.0.6, <2.0
 	netsquid-magic >=12.1, <13.0.0
 	netsquid-nv >=8.0, <9.0
-	netqasm >=0.9
+	netqasm ==0.11.0a3
 
 [options.extras_require]
 tests = 
 	pytest >=7.1, <8.0
 	types-PyYAML >=6.0, <7.0
 	flake8 >=4.0, <5.0
 	isort >=5.10, <5.11
```

### Comparing `squidasm-0.9.0a1/squidasm/nqasm/executor/base.py` & `squidasm-0.9.0a2/squidasm/nqasm/executor/base.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/nqasm/executor/nv.py` & `squidasm-0.9.0a2/squidasm/nqasm/executor/nv.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/nqasm/executor/vanilla.py` & `squidasm-0.9.0a2/squidasm/nqasm/executor/vanilla.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/nqasm/multithread.py` & `squidasm-0.9.0a2/squidasm/nqasm/multithread.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,58 +1,58 @@
 from __future__ import annotations
 
 from threading import Thread
 from typing import TYPE_CHECKING, Callable, List, Optional, Type
 
 from netqasm.lang.instr.flavour import NVFlavour
-from netqasm.sdk.compiling import NVSubroutineCompiler
 from netqasm.sdk.connection import BaseNetQASMConnection
 from netqasm.sdk.network import NetworkInfo
+from netqasm.sdk.transpile import NVSubroutineTranspiler
 
 from squidasm.sim.glob import (
     get_node_id,
     get_node_id_for_app,
     get_node_name,
     get_node_name_for_app,
     get_running_backend,
 )
 from squidasm.sim.queues import QueueManager
 
 if TYPE_CHECKING:
-    from netqasm.sdk.compiling import SubroutineCompiler
     from netqasm.sdk.config import LogConfig
     from netqasm.sdk.epr_socket import EPRSocket
+    from netqasm.sdk.transpile import SubroutineTranspiler
 
     from squidasm.sim.queues import TaskQueue
 
 
 class NetSquidConnection(BaseNetQASMConnection):
     def __init__(
         self,
         app_name: str,
         app_id: Optional[int] = None,
         max_qubits: int = 5,
         log_config: LogConfig = None,
         epr_sockets: Optional[List[EPRSocket]] = None,
-        compiler: Optional[Type[SubroutineCompiler]] = None,
+        compiler: Optional[Type[SubroutineTranspiler]] = None,
         return_arrays: bool = True,
         **kwargs,
     ) -> None:
         node_name = get_node_name_for_app(app_name)
 
         self._message_queue: TaskQueue = QueueManager.get_queue(node_name)
 
         if compiler is None:
             backend = get_running_backend()
             if backend is None:
                 raise RuntimeError("Backend is None")
             subroutine_handler = backend.subroutine_handlers[node_name]
             flavour = subroutine_handler.flavour
             if isinstance(flavour, NVFlavour):
-                compiler = NVSubroutineCompiler
+                compiler = NVSubroutineTranspiler
 
         super().__init__(
             app_name=app_name,
             node_name=node_name,
             app_id=app_id,
             max_qubits=max_qubits,
             log_config=log_config,
```

### Comparing `squidasm-0.9.0a1/squidasm/nqasm/netstack.py` & `squidasm-0.9.0a2/squidasm/nqasm/netstack.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/nqasm/output.py` & `squidasm-0.9.0a2/squidasm/nqasm/output.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/nqasm/qnodeos.py` & `squidasm-0.9.0a2/squidasm/nqasm/qnodeos.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/nqasm/singlethread/connection.py` & `squidasm-0.9.0a2/squidasm/nqasm/singlethread/connection.py`

 * *Files 11% similar despite different names*

```diff
@@ -11,42 +11,42 @@
 )
 from netqasm.logging.glob import get_netqasm_logger
 from netqasm.sdk.build_types import GenericHardwareConfig, HardwareConfig
 from netqasm.sdk.builder import Builder
 from netqasm.sdk.connection import (
     BaseNetQASMConnection,
     NetworkInfo,
-    PreSubroutine,
+    ProtoSubroutine,
     T_Message,
 )
 from netqasm.sdk.shared_memory import SharedMemory
 
 from pydynaa import EventExpression
 from squidasm.run.singlethread.context import NetSquidContext
 from squidasm.run.singlethread.protocols import (
     SUBRT_FINISHED,
     HostProtocol,
     NewResultEvent,
 )
 
 if TYPE_CHECKING:
-    from netqasm.sdk.compiling import SubroutineCompiler
+    from netqasm.sdk.transpile import SubroutineTranspiler
     from netqasm.sdk.epr_socket import EPRSocket
 
 from squidasm.run.singlethread.context import NetSquidNetworkInfo
 
 
 class NetSquidConnection(BaseNetQASMConnection):
     def __init__(
         self,
         app_name: str,
         max_qubits: int = 5,
         hardware_config: Optional[HardwareConfig] = None,
         epr_sockets: Optional[List[EPRSocket]] = None,
-        compiler: Optional[Type[SubroutineCompiler]] = None,
+        compiler: Optional[Type[SubroutineTranspiler]] = None,
         **kwargs,
     ) -> None:
         self._app_name = app_name
         self._app_id = 0
         self._node_name = app_name
         self._max_qubits = max_qubits
         self._epr_sockets = [] if epr_sockets is None else epr_sockets
@@ -120,28 +120,28 @@
                 remote_node_id=sck.remote_node_id,
                 remote_epr_socket_id=sck.remote_epr_socket_id,
                 min_fidelity=sck.min_fidelity,
             )
         )
         yield from self._wait_for_results()
 
-    def commit_subroutine(
+    def commit_protosubroutine(
         self,
-        presubroutine: PreSubroutine,
+        protosubroutine: ProtoSubroutine,
         block: bool = True,
         callback: Optional[Callable] = None,
     ) -> Generator[EventExpression, None, None]:
         for sck, opened in self._epr_sck_status.items():
             if not opened:
                 yield from self._commit_open_epr_socket(sck)
                 self._epr_sck_status[sck] = True
 
-        self._logger.debug(f"Flushing presubroutine:\n{presubroutine}")
+        self._logger.debug(f"Flushing protosubroutine:\n{protosubroutine}")
 
-        subroutine = self._builder.subrt_compile_subroutine(presubroutine)
+        subroutine = self._builder.subrt_compile_subroutine(protosubroutine)
         self._logger.info(f"Flushing compiled subroutine:\n{subroutine}")
 
         self._commit_message(
             msg=SubroutineMessage(subroutine=subroutine),
             block=block,
             callback=callback,
         )
@@ -153,16 +153,16 @@
     def flush(
         self, block: bool = True, callback: Optional[Callable] = None
     ) -> Generator[EventExpression, None, None]:
         subroutine = self._builder.subrt_pop_pending_subroutine()
         if subroutine is None:
             return
 
-        yield from self.commit_subroutine(
-            presubroutine=subroutine,
+        yield from self.commit_protosubroutine(
+            protosubroutine=subroutine,
             block=block,
             callback=callback,
         )
 
     def _commit_serialized_message(
         self, raw_msg: bytes, block: bool = True, callback: Optional[Callable] = None
     ) -> None:
```

### Comparing `squidasm-0.9.0a1/squidasm/nqasm/singlethread/csocket.py` & `squidasm-0.9.0a2/squidasm/nqasm/singlethread/csocket.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/run/multithread/runtime_mgr.py` & `squidasm-0.9.0a2/squidasm/run/multithread/runtime_mgr.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/run/multithread/simulate.py` & `squidasm-0.9.0a2/squidasm/run/multithread/simulate.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/run/singlethread/context.py` & `squidasm-0.9.0a2/squidasm/run/singlethread/context.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/run/singlethread/protocols.py` & `squidasm-0.9.0a2/squidasm/run/singlethread/protocols.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/run/singlethread/run.py` & `squidasm-0.9.0a2/squidasm/run/singlethread/run.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/run/singlethread/util.py` & `squidasm-0.9.0a2/squidasm/run/singlethread/util.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/run/stack/build.py` & `squidasm-0.9.0a2/squidasm/run/stack/build.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/run/stack/config.py` & `squidasm-0.9.0a2/squidasm/run/stack/config.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/run/stack/run.py` & `squidasm-0.9.0a2/squidasm/run/stack/run.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/glob.py` & `squidasm-0.9.0a2/squidasm/sim/glob.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/network/network.py` & `squidasm-0.9.0a2/squidasm/sim/network/network.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/network/nv_config.py` & `squidasm-0.9.0a2/squidasm/sim/network/nv_config.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/queues.py` & `squidasm-0.9.0a2/squidasm/sim/queues.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/arch/arch.drawio` & `squidasm-0.9.0a2/squidasm/sim/stack/arch/arch.drawio`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/arch/arch.png` & `squidasm-0.9.0a2/squidasm/sim/stack/arch/arch.png`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/arch/comn.drawio` & `squidasm-0.9.0a2/squidasm/sim/stack/arch/comn.drawio`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/arch/comn.png` & `squidasm-0.9.0a2/squidasm/sim/stack/arch/comn.png`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/common.py` & `squidasm-0.9.0a2/squidasm/sim/stack/common.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/connection.py` & `squidasm-0.9.0a2/squidasm/sim/stack/connection.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,27 +1,28 @@
 from __future__ import annotations
 
 import logging
 from typing import TYPE_CHECKING, Callable, Generator, Optional, Type
 
 from netqasm.backend.messages import SubroutineMessage
+from netqasm.lang.subroutine import Subroutine
 from netqasm.sdk.build_types import GenericHardwareConfig, HardwareConfig
 from netqasm.sdk.builder import Builder
 from netqasm.sdk.connection import (
     BaseNetQASMConnection,
     NetworkInfo,
-    PreSubroutine,
+    ProtoSubroutine,
     T_Message,
 )
 from netqasm.sdk.shared_memory import SharedMemory
 
 from pydynaa import EventExpression
 
 if TYPE_CHECKING:
-    from netqasm.sdk.compiling import SubroutineCompiler
+    from netqasm.sdk.transpile import SubroutineTranspiler
     from squidasm.sim.stack.host import Host
 
 from squidasm.sim.stack.common import LogManager
 
 from .context import NetSquidNetworkInfo
 
 
@@ -29,15 +30,15 @@
     def __init__(
         self,
         host: Host,
         app_id: int,
         app_name: str,
         max_qubits: int = 5,
         hardware_config: Optional[HardwareConfig] = None,
-        compiler: Optional[Type[SubroutineCompiler]] = None,
+        compiler: Optional[Type[SubroutineTranspiler]] = None,
         **kwargs,
     ) -> None:
         self._app_name = app_name
         self._app_id = app_id
         self._node_name = app_name
         self._max_qubits = max_qubits
 
@@ -71,45 +72,54 @@
     def _commit_message(
         self, msg: T_Message, block: bool = True, callback: Optional[Callable] = None
     ) -> None:
         assert isinstance(msg, SubroutineMessage)
         self._logger.debug(f"Committing message {msg}")
         self._host.send_qnos_msg(bytes(msg))
 
-    def commit_subroutine(
+    def commit_protosubroutine(
         self,
-        presubroutine: PreSubroutine,
+        protosubroutine: ProtoSubroutine,
         block: bool = True,
         callback: Optional[Callable] = None,
     ) -> Generator[EventExpression, None, None]:
-        self._logger.info(f"Flushing presubroutine:\n{presubroutine}")
+        self._logger.info(f"Flushing protosubroutine:\n{protosubroutine}")
 
-        subroutine = self._builder.subrt_compile_subroutine(presubroutine)
+        subroutine = self._builder.subrt_compile_subroutine(protosubroutine)
         self._logger.info(f"Flushing compiled subroutine:\n{subroutine}")
 
+        yield from self.commit_subroutine(subroutine, block, callback)
+        self._builder._reset()
+
+    def commit_subroutine(
+        self,
+        subroutine: Subroutine,
+        block: bool = True,
+        callback: Optional[Callable] = None,
+    ) -> Generator[EventExpression, None, None]:
+        self._logger.info(f"Commiting compiled subroutine:\n{subroutine}")
+
         self._commit_message(
             msg=SubroutineMessage(subroutine=subroutine),
             block=block,
             callback=callback,
         )
 
         result = yield from self._host.receive_qnos_msg()
         self._shared_memory = result
 
-        self._builder._reset()
-
     def flush(
         self, block: bool = True, callback: Optional[Callable] = None
     ) -> Generator[EventExpression, None, None]:
         subroutine = self._builder.subrt_pop_pending_subroutine()
         if subroutine is None:
             return
 
-        yield from self.commit_subroutine(
-            presubroutine=subroutine,
+        yield from self.commit_protosubroutine(
+            protosubroutine=subroutine,
             block=block,
             callback=callback,
         )
 
     def _commit_serialized_message(
         self, raw_msg: bytes, block: bool = True, callback: Optional[Callable] = None
     ) -> None:
```

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/context.py` & `squidasm-0.9.0a2/squidasm/sim/stack/context.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/csocket.py` & `squidasm-0.9.0a2/squidasm/sim/stack/csocket.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/egp.py` & `squidasm-0.9.0a2/squidasm/sim/stack/egp.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/globals.py` & `squidasm-0.9.0a2/squidasm/sim/stack/globals.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/handler.py` & `squidasm-0.9.0a2/squidasm/sim/stack/handler.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/host.py` & `squidasm-0.9.0a2/squidasm/sim/stack/host.py`

 * *Files 4% similar despite different names*

```diff
@@ -3,16 +3,16 @@
 from typing import Any, Dict, Generator, List, Optional, Type
 
 from netqasm.backend.messages import (
     InitNewAppMessage,
     OpenEPRSocketMessage,
     StopAppMessage,
 )
-from netqasm.sdk.compiling import NVSubroutineCompiler, SubroutineCompiler
 from netqasm.sdk.epr_socket import EPRSocket
+from netqasm.sdk.transpile import NVSubroutineTranspiler, SubroutineTranspiler
 from netsquid.components.component import Component, Port
 from netsquid.nodes import Node
 
 from pydynaa import EventExpression
 from squidasm.sim.stack.common import ComponentProtocol, PortListener
 from squidasm.sim.stack.connection import QnosConnection
 from squidasm.sim.stack.context import NetSquidContext
@@ -70,35 +70,37 @@
         )
         self.add_listener(
             "peer",
             PortListener(self._comp.ports["peer_in"], SIGNAL_HOST_HOST_MSG),
         )
 
         if qdevice_type == "nv":
-            self._compiler: Optional[Type[SubroutineCompiler]] = NVSubroutineCompiler
+            self._compiler: Optional[
+                Type[SubroutineTranspiler]
+            ] = NVSubroutineTranspiler
         elif qdevice_type == "generic":
-            self._compiler: Optional[Type[SubroutineCompiler]] = None
+            self._compiler: Optional[Type[SubroutineTranspiler]] = None
         else:
             raise ValueError
 
         # Program that is currently being executed.
         self._program: Optional[Program] = None
 
         # Number of times the current program still needs to be run.
         self._num_pending: int = 0
 
         # Results of program runs so far.
         self._program_results: List[Dict[str, Any]] = []
 
     @property
-    def compiler(self) -> Optional[Type[SubroutineCompiler]]:
+    def compiler(self) -> Optional[Type[SubroutineTranspiler]]:
         return self._compiler
 
     @compiler.setter
-    def compiler(self, typ: Optional[Type[SubroutineCompiler]]) -> None:
+    def compiler(self, typ: Optional[Type[SubroutineTranspiler]]) -> None:
         self._compiler = typ
 
     def send_qnos_msg(self, msg: bytes) -> None:
         self._comp.qnos_out_port.tx_output(msg)
 
     def receive_qnos_msg(self) -> Generator[EventExpression, None, str]:
         return (yield from self._receive_msg("qnos", SIGNAL_HAND_HOST_MSG))
```

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/netstack.py` & `squidasm-0.9.0a2/squidasm/sim/stack/netstack.py`

 * *Files 0% similar despite different names*

```diff
@@ -526,15 +526,14 @@
         """
         assert isinstance(request, ReqCreateAndKeep)
 
         num_pairs = request.number
 
         self._logger.info(f"putting CK request to EGP for {num_pairs} pairs")
         self._logger.info(f"splitting request into {num_pairs} 1-pair requests")
-        request.number = 1
 
         start_time = ns.sim_time()
 
         for pair_index in range(num_pairs):
             self._logger.info(f"trying to allocate comm qubit for pair {pair_index}")
             while True:
                 try:
```

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/processor.py` & `squidasm-0.9.0a2/squidasm/sim/stack/processor.py`

 * *Files 1% similar despite different names*

```diff
@@ -170,16 +170,16 @@
         self, subroutine: Subroutine
     ) -> Generator[EventExpression, None, None]:
         """Execute a NetQASM subroutine on this processor."""
         app_id = subroutine.app_id
         assert app_id in self.app_memories
         app_mem = self.app_memories[app_id]
         app_mem.set_prog_counter(0)
-        while app_mem.prog_counter < len(subroutine.commands):
-            instr = subroutine.commands[app_mem.prog_counter]
+        while app_mem.prog_counter < len(subroutine.instructions):
+            instr = subroutine.instructions[app_mem.prog_counter]
             self._logger.debug(
                 f"{ns.sim_time()} interpreting instruction {instr} at line {app_mem.prog_counter}"
             )
 
             if (
                 isinstance(instr, core.JmpInstruction)
                 or isinstance(instr, core.BranchUnaryInstruction)
```

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/program.py` & `squidasm-0.9.0a2/squidasm/sim/stack/program.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/qnos.py` & `squidasm-0.9.0a2/squidasm/sim/stack/qnos.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/sim/stack/stack.py` & `squidasm-0.9.0a2/squidasm/sim/stack/stack.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/util/ns.py` & `squidasm-0.9.0a2/squidasm/util/ns.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/util/sim.py` & `squidasm-0.9.0a2/squidasm/util/sim.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm/util/thread.py` & `squidasm-0.9.0a2/squidasm/util/thread.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/squidasm.egg-info/PKG-INFO` & `squidasm-0.9.0a2/squidasm.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,15 @@
 Metadata-Version: 2.1
 Name: squidasm
-Version: 0.9.0a1
+Version: 0.9.0a2
 Summary: NetSquid simulator for quantum networks running NetQASM applications
 Home-page: https://github.com/QuTech-Delft/squidasm
 Author: QuTech
 Author-email: b.vandervecht@tudelft.nl
 License: MIT
-Platform: UNKNOWN
 Description-Content-Type: text/markdown
 Provides-Extra: tests
 License-File: LICENSE
 
 # SquidASM
 
 This is SquidASM, a simulator based on NetSquid that can execute applications written using NetQASM.
@@ -98,8 +97,7 @@
 Before code is pushed, make sure that the `make lint` command succeeds, which runs `black`, `isort` and `flake8`.
 
 
 # Contributors
 In alphabetical order:
 - Axel Dahlberg
 - Bart van der Vecht (b.vandervecht[at]tudelft.nl)
-
```

### Comparing `squidasm-0.9.0a1/squidasm.egg-info/SOURCES.txt` & `squidasm-0.9.0a2/squidasm.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -46,14 +46,15 @@
 examples/stack/link_layer/example_link_layer_md.py
 examples/stack/link_layer_custom_subrt/client.nqasm
 examples/stack/link_layer_custom_subrt/example_ll_custom_subrt.py
 examples/stack/link_layer_custom_subrt/server.nqasm
 examples/stack/partial_bqc/example_bqc_5_2.py
 examples/stack/partial_bqc/example_bqc_5_3.py
 examples/stack/partial_bqc/example_bqc_5_4.py
+examples/stack/precompilation/example_bqc_5_4_precompiled.py
 examples/stack/qkd/config.yaml
 examples/stack/qkd/example_qkd.py
 examples/stack/single_node/single_node.py
 examples/stack/teleport/example_teleport.py
 pydynaa/__init__.pyi
 squidasm/__init__.py
 squidasm.egg-info/PKG-INFO
```

### Comparing `squidasm-0.9.0a1/tests/stack/test_components.py` & `squidasm-0.9.0a2/tests/stack/test_components.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/tests/stack/test_handler.py` & `squidasm-0.9.0a2/tests/stack/test_handler.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/tests/stack/test_processor.py` & `squidasm-0.9.0a2/tests/stack/test_processor.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/tests/stack/test_sdk.py` & `squidasm-0.9.0a2/tests/stack/test_sdk.py`

 * *Files 5% similar despite different names*

```diff
@@ -5,19 +5,20 @@
 from netqasm.sdk.qubit import Qubit
 from netsquid.components import QuantumProcessor
 from netsquid.qubits import ketstates, qubitapi
 from netsquid_magic.link_layer import (
     MagicLinkLayerProtocolWithSignaling,
     SingleClickTranslationUnit,
 )
-from netsquid_nv.magic_distributor import NVSingleClickMagicDistributor
+from netsquid_magic.magic_distributor import DepolariseWithFailureMagicDistributor
 
 from pydynaa import EventExpression
 from squidasm.run.stack.build import build_nv_qdevice
 from squidasm.run.stack.config import NVQDeviceConfig
+from squidasm.sim.stack.common import LogManager
 from squidasm.sim.stack.context import NetSquidContext
 from squidasm.sim.stack.program import Program, ProgramContext, ProgramMeta
 from squidasm.sim.stack.stack import NodeStack
 
 
 class TestSdkSingleNode(unittest.TestCase):
     def setUp(self) -> None:
@@ -29,14 +30,15 @@
 
         self._program: Optional[Program] = None
 
     def tearDown(self) -> None:
         assert self._program is not None
         self._node.host.enqueue_program(self._program, 1)
         self._node.start()
+        LogManager.set_log_level("INFO")
         ns.sim_run()
         if self._check_qmem:
             self._check_qmem(self._node.qdevice)
 
     def test_1(self):
         class TestProgram(Program):
             @property
@@ -147,22 +149,18 @@
 
         self._prog_alice: Optional[Program] = None
         self._prog_bob: Optional[Program] = None
 
     def tearDown(self) -> None:
         assert self._prog_alice is not None
         assert self._prog_bob is not None
-        # link_dist = PerfectStateMagicDistributor(
-        #     nodes=[self._alice.node, self._bob.node]
-        # )
-        link_dist = NVSingleClickMagicDistributor(
+        link_dist = DepolariseWithFailureMagicDistributor(
             nodes=[self._alice.node, self._bob.node],
-            length_A=0.001,
-            length_B=0.001,
-            full_cycle=0.001,
+            prob_max_mixed=0.1,
+            prob_success=0.5,
             t_cycle=10,
         )
         link_prot = MagicLinkLayerProtocolWithSignaling(
             nodes=[self._alice.node, self._bob.node],
             magic_distributor=link_dist,
             translation_unit=SingleClickTranslationUnit(),
         )
@@ -204,22 +202,22 @@
                 conn = context.connection
                 epr_socket = context.epr_sockets["bob"]
 
                 csocket = context.csockets["bob"]
                 msg = yield from csocket.recv()
                 print(f"got message from bob: {msg}")
 
-                q = Qubit(conn)
-                q.X()
-                m = q.measure()
-                yield from conn.flush()
+                # q = Qubit(conn)
+                # q.X()
+                # m = q.measure()
+                # yield from conn.flush()
 
-                print(f"m = {m}")
+                # print(f"m = {m}")
 
-                q = epr_socket.create()[0]
+                q = epr_socket.create_keep()[0]
                 epr_outcome = q.measure()
                 yield from conn.flush()
                 print(f"epr_outcome = {epr_outcome}")
 
         class ServerProgram(Program):
             @property
             def meta(self) -> ProgramMeta:
@@ -236,24 +234,24 @@
             ) -> Generator[EventExpression, None, Dict[str, Any]]:
                 conn = context.connection
                 epr_socket = context.epr_sockets["alice"]
                 csocket = context.csockets["alice"]
 
                 csocket.send("hello")
 
-                q = Qubit(conn)
-                q.X()
-                m = q.measure()
-                print(f"time before measuring: {ns.sim_time()}")
-                yield from conn.flush()
-                print(f"time after measuring: {ns.sim_time()}")
+                # q = Qubit(conn)
+                # q.X()
+                # m = q.measure()
+                # print(f"time before measuring: {ns.sim_time()}")
+                # yield from conn.flush()
+                # print(f"time after measuring: {ns.sim_time()}")
 
-                print(f"m = {m}")
+                # print(f"m = {m}")
 
-                q = epr_socket.recv()[0]
+                q = epr_socket.recv_keep()[0]
                 epr_outcome = q.measure()
                 yield from conn.flush()
                 print(f"epr_outcome = {epr_outcome}")
 
         self._prog_alice = ClientProgram()
         self._prog_bob = ServerProgram()
         self._check_qmem = None
```

### Comparing `squidasm-0.9.0a1/tests/stack/test_single_node.py` & `squidasm-0.9.0a2/tests/stack/test_single_node.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/tests/stack/test_two_nodes.py` & `squidasm-0.9.0a2/tests/stack/test_two_nodes.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/tests/test_async_scenarios.py` & `squidasm-0.9.0a2/tests/test_async_scenarios.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/tests/test_executor.py` & `squidasm-0.9.0a2/tests/test_executor.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/tests/test_ns_util.py` & `squidasm-0.9.0a2/tests/test_ns_util.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/tests/test_qnodeos.py` & `squidasm-0.9.0a2/tests/test_qnodeos.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/tests/test_run.py` & `squidasm-0.9.0a2/tests/test_run.py`

 * *Files identical despite different names*

### Comparing `squidasm-0.9.0a1/tests/test_simulate.py` & `squidasm-0.9.0a2/tests/test_simulate.py`

 * *Files identical despite different names*

