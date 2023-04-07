# Comparing `tmp/e3nn_jax-0.9.1.tar.gz` & `tmp/e3nn_jax-0.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "e3nn_jax-0.9.1.tar", last modified: Tue Sep 27 19:03:53 2022, max compression
+gzip compressed data, was "e3nn_jax-0.9.2.tar", last modified: Thu Sep 29 22:54:24 2022, max compression
```

## Comparing `e3nn_jax-0.9.1.tar` & `e3nn_jax-0.9.2.tar`

### file list

```diff
@@ -1,81 +1,82 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-27 19:03:53.335562 e3nn_jax-0.9.1/
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     2674 2022-09-27 19:03:53.335562 e3nn_jax-0.9.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1672 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-27 19:03:53.319560 e3nn_jax-0.9.1/e3nn_jax/
--rw-r--r--   0 runner    (1001) docker     (121)     4013 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-27 19:03:53.331561 e3nn_jax-0.9.1/e3nn_jax/_src/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3619 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/activation.py
--rw-r--r--   0 runner    (1001) docker     (121)      785 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/activation_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     7994 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/batchnorm.py
--rw-r--r--   0 runner    (1001) docker     (121)     3513 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/batchnorm_test.py
--rw-r--r--   0 runner    (1001) docker     (121)      503 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/config.py
--rw-r--r--   0 runner    (1001) docker     (121)      910 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/config_test.py
--rw-r--r--   0 runner    (1001) docker     (121)    24295 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/core_tensor_product.py
--rw-r--r--   0 runner    (1001) docker     (121)     6031 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/core_tensor_product_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     2307 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/dropout.py
--rw-r--r--   0 runner    (1001) docker     (121)      729 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/dropout_test.py
--rw-r--r--   0 runner    (1001) docker     (121)      435 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/einsum.py
--rw-r--r--   0 runner    (1001) docker     (121)      856 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/einsum_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     3465 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/gate.py
--rw-r--r--   0 runner    (1001) docker     (121)      434 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/gate_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     3449 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/grad.py
--rw-r--r--   0 runner    (1001) docker     (121)     1569 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/grad_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     3697 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/graph_util.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/graph_util_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     3189 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/instruction.py
--rw-r--r--   0 runner    (1001) docker     (121)    23239 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/irreps.py
--rw-r--r--   0 runner    (1001) docker     (121)    46624 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/irreps_array.py
--rw-r--r--   0 runner    (1001) docker     (121)     6048 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/irreps_array_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     2794 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/irreps_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     8838 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/linear.py
--rw-r--r--   0 runner    (1001) docker     (121)     2179 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/linear_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     1287 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/mlp.py
--rw-r--r--   0 runner    (1001) docker     (121)     1544 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/perm_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     2390 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/poly_envelope.py
--rw-r--r--   0 runner    (1001) docker     (121)    13574 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/reduced_tensor_product.py
--rw-r--r--   0 runner    (1001) docker     (121)     1563 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/reduced_tensor_product_test.py
--rw-r--r--   0 runner    (1001) docker     (121)    15532 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/rotation.py
--rw-r--r--   0 runner    (1001) docker     (121)     3894 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/rotation_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     2982 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/so3.py
--rw-r--r--   0 runner    (1001) docker     (121)     2790 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/soft_one_hot_linspace.py
--rw-r--r--   0 runner    (1001) docker     (121)    16393 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/spherical_harmonics.py
--rw-r--r--   0 runner    (1001) docker     (121)     4654 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/spherical_harmonics_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     2244 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/su2.py
--rw-r--r--   0 runner    (1001) docker     (121)    12355 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/tensor_products.py
--rw-r--r--   0 runner    (1001) docker     (121)     1281 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/tensor_products_test.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-27 19:03:53.331561 e3nn_jax-0.9.1/e3nn_jax/_src/util/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/util/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1865 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/util/decorators.py
--rw-r--r--   0 runner    (1001) docker     (121)      645 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/util/jit.py
--rw-r--r--   0 runner    (1001) docker     (121)      118 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/util/jit_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     4448 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/util/math_numpy.py
--rw-r--r--   0 runner    (1001) docker     (121)     6561 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/util/optimize_jaxpr.py
--rw-r--r--   0 runner    (1001) docker     (121)      233 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/util/prod.py
--rw-r--r--   0 runner    (1001) docker     (121)      486 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/util/sympy.py
--rw-r--r--   0 runner    (1001) docker     (121)     1349 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/util/test.py
--rw-r--r--   0 runner    (1001) docker     (121)     2474 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/_src/wigner_test.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-27 19:03:53.335562 e3nn_jax-0.9.1/e3nn_jax/experimental/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/experimental/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5546 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/experimental/point_convolution.py
--rw-r--r--   0 runner    (1001) docker     (121)     1213 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/experimental/point_convolution_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     5547 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/experimental/transformer.py
--rw-r--r--   0 runner    (1001) docker     (121)     1488 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/experimental/transformer_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     7013 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/experimental/voxel_convolution.py
--rw-r--r--   0 runner    (1001) docker     (121)     2573 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/experimental/voxel_convolution_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     4078 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/experimental/voxel_pooling.py
--rw-r--r--   0 runner    (1001) docker     (121)      857 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/experimental/voxel_pooling_test.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-27 19:03:53.335562 e3nn_jax-0.9.1/e3nn_jax/irrep/
--rw-r--r--   0 runner    (1001) docker     (121)      900 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/irrep/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2339 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/perm.py
--rw-r--r--   0 runner    (1001) docker     (121)      129 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/e3nn_jax/util.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-27 19:03:53.319560 e3nn_jax-0.9.1/e3nn_jax.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2674 2022-09-27 19:03:53.000000 e3nn_jax-0.9.1/e3nn_jax.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2169 2022-09-27 19:03:53.000000 e3nn_jax-0.9.1/e3nn_jax.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-27 19:03:53.000000 e3nn_jax-0.9.1/e3nn_jax.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       31 2022-09-27 19:03:53.000000 e3nn_jax-0.9.1/e3nn_jax.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        9 2022-09-27 19:03:53.000000 e3nn_jax-0.9.1/e3nn_jax.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      201 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)      235 2022-09-27 19:03:53.335562 e3nn_jax-0.9.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1628 2022-09-27 19:03:44.000000 e3nn_jax-0.9.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-29 22:54:24.519101 e3nn_jax-0.9.2/
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)     2674 2022-09-29 22:54:24.519101 e3nn_jax-0.9.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1672 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-29 22:54:24.515101 e3nn_jax-0.9.2/e3nn_jax/
+-rw-r--r--   0 runner    (1001) docker     (121)     4013 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-29 22:54:24.519101 e3nn_jax-0.9.2/e3nn_jax/_src/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3619 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/activation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      785 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/activation_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7994 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/batchnorm.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3513 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/batchnorm_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)      503 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/config.py
+-rw-r--r--   0 runner    (1001) docker     (121)      910 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/config_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24295 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/core_tensor_product.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6031 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/core_tensor_product_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2307 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/dropout.py
+-rw-r--r--   0 runner    (1001) docker     (121)      729 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/dropout_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)      435 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/einsum.py
+-rw-r--r--   0 runner    (1001) docker     (121)      856 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/einsum_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3465 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/gate.py
+-rw-r--r--   0 runner    (1001) docker     (121)      434 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/gate_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3449 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/grad.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1569 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/grad_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3697 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/graph_util.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/graph_util_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3189 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/instruction.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23239 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/irreps.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46624 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/irreps_array.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6048 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/irreps_array_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2794 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/irreps_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8838 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/linear.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2179 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/linear_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1287 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/mlp.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1544 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/perm_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2455 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/poly_envelope.py
+-rw-r--r--   0 runner    (1001) docker     (121)      966 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/poly_envelope_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13574 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/reduced_tensor_product.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1563 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/reduced_tensor_product_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15532 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/rotation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3894 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/rotation_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2982 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/so3.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2790 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/soft_one_hot_linspace.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16386 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/spherical_harmonics.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4654 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/spherical_harmonics_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2244 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/su2.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12355 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/tensor_products.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1281 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/tensor_products_test.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-29 22:54:24.519101 e3nn_jax-0.9.2/e3nn_jax/_src/util/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/util/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1865 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/util/decorators.py
+-rw-r--r--   0 runner    (1001) docker     (121)      645 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/util/jit.py
+-rw-r--r--   0 runner    (1001) docker     (121)      118 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/util/jit_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4448 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/util/math_numpy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6561 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/util/optimize_jaxpr.py
+-rw-r--r--   0 runner    (1001) docker     (121)      233 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/util/prod.py
+-rw-r--r--   0 runner    (1001) docker     (121)      486 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/util/sympy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1349 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/util/test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2474 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/_src/wigner_test.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-29 22:54:24.519101 e3nn_jax-0.9.2/e3nn_jax/experimental/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/experimental/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5546 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/experimental/point_convolution.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1213 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/experimental/point_convolution_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5547 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/experimental/transformer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1488 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/experimental/transformer_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7013 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/experimental/voxel_convolution.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2573 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/experimental/voxel_convolution_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4078 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/experimental/voxel_pooling.py
+-rw-r--r--   0 runner    (1001) docker     (121)      857 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/experimental/voxel_pooling_test.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-29 22:54:24.519101 e3nn_jax-0.9.2/e3nn_jax/irrep/
+-rw-r--r--   0 runner    (1001) docker     (121)      900 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/irrep/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2339 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/perm.py
+-rw-r--r--   0 runner    (1001) docker     (121)      129 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/e3nn_jax/util.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-29 22:54:24.515101 e3nn_jax-0.9.2/e3nn_jax.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     2674 2022-09-29 22:54:24.000000 e3nn_jax-0.9.2/e3nn_jax.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2205 2022-09-29 22:54:24.000000 e3nn_jax-0.9.2/e3nn_jax.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-29 22:54:24.000000 e3nn_jax-0.9.2/e3nn_jax.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       31 2022-09-29 22:54:24.000000 e3nn_jax-0.9.2/e3nn_jax.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        9 2022-09-29 22:54:24.000000 e3nn_jax-0.9.2/e3nn_jax.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      201 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)      235 2022-09-29 22:54:24.519101 e3nn_jax-0.9.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1628 2022-09-29 22:54:17.000000 e3nn_jax-0.9.2/setup.py
```

### Comparing `e3nn_jax-0.9.1/LICENSE` & `e3nn_jax-0.9.2/LICENSE`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/PKG-INFO` & `e3nn_jax-0.9.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: e3nn_jax
-Version: 0.9.1
+Version: 0.9.2
 Summary: Equivariant convolutional neural networks for the group E(3) of 3 dimensional rotations, translations, and mirrors.
 Home-page: https://e3nn.org
 License: MIT
 Description: # e3nn-jax [![Coverage Status](https://coveralls.io/repos/github/e3nn/e3nn-jax/badge.svg?branch=main)](https://coveralls.io/github/e3nn/e3nn-jax?branch=main)
         
         # [Documentation](https://e3nn-jax.readthedocs.io/en/latest) [![Documentation Status](https://readthedocs.org/projects/e3nn-jax/badge/?version=latest)](https://e3nn-jax.readthedocs.io/en/latest/?badge=latest)
```

### Comparing `e3nn_jax-0.9.1/README.md` & `e3nn_jax-0.9.2/README.md`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/__init__.py` & `e3nn_jax-0.9.2/e3nn_jax/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-__version__ = "0.9.1"
+__version__ = "0.9.2"
 
 from e3nn_jax._src.config import config
 from e3nn_jax._src.rotation import (
     rand_matrix,
     identity_angles,
     rand_angles,
     compose_angles,
```

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/activation.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/activation.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/activation_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/activation_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/batchnorm.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/batchnorm.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/batchnorm_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/batchnorm_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/config_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/config_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/core_tensor_product.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/core_tensor_product.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/core_tensor_product_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/core_tensor_product_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/dropout.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/dropout.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/dropout_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/dropout_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/einsum_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/einsum_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/gate.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/gate.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/grad.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/grad.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/grad_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/grad_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/graph_util.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/graph_util.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/instruction.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/instruction.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/irreps.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/irreps.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/irreps_array.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/irreps_array.py`

 * *Files 0% similar despite different names*

```diff
@@ -1169,15 +1169,15 @@
 
             def fn(x, y, mul, ir):
                 if x is not None and y is not None:
                     return x.at[index + (slice(None),)].add(y)
                 if x is not None and y is None:
                     return x
                 if x is None and y is not None:
-                    return jnp.zeros(self.shape[:-1] + (mul, ir.dim), dtype=self.array.dtype).at[index + (slice(None),)].set(y)
+                    return jnp.zeros(self.shape[:-1] + (mul, ir.dim), dtype=self.array.dtype).at[index + (slice(None),)].add(y)
                 if x is None and y is None:
                     return None
 
             return IrrepsArray(
                 self.irreps,
                 array=self.array.at[index].add(values.array),
                 list=[fn(x, y, mul, ir) for (mul, ir), x, y in zip(self.irreps, self.list, values.list)],
```

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/irreps_array_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/irreps_array_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/irreps_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/irreps_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/linear.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/linear.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/linear_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/linear_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/mlp.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/mlp.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/perm_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/perm_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/poly_envelope.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/poly_envelope.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 from functools import lru_cache
 from math import factorial
 from typing import Callable
 
 import jax
-from jax import jit
 from jax import numpy as jnp
 
 
 def u(p: int, x: jnp.ndarray) -> jnp.ndarray:
+    r"""Equivalent to :func:`poly_envelope` with ``n0 = p-1`` and ``n1 = 2``."""
     return 1 - (p + 1) * (p + 2) / 2 * x**p + p * (p + 2) * x ** (p + 1) - p * (p + 1) / 2 * x ** (p + 2)
 
 
 def _constraint(x: float, derivative: int, degree: int):
     return [0 if derivative > N else factorial(N) // factorial(N - derivative) * x ** (N - derivative) for N in range(degree)]
 
 
@@ -26,15 +26,15 @@
             [_constraint(x, derivative, degree) for x, derivative, _ in sorted(constraints)],
             dtype=jnp.float64,
         )
         B = jnp.array([y for _, _, y in sorted(constraints)], dtype=jnp.float64)
         c = jnp.linalg.solve(A, B)
 
         jax.config.update("jax_enable_x64", jax_enable_x64)
-    return jit(lambda x: jnp.polyval(c[::-1], x))
+    return jax.jit(lambda x: jnp.polyval(c[::-1], x))
 
 
 def poly_envelope(n0: int, n1: int) -> Callable[[float], float]:
     r"""Polynomial envelope function with ``n0`` and ``n1`` derivatives euqal to 0 at ``x=0`` and ``x=1`` respectively.
 
     Small documentation available at ``https://mariogeiger.ch/polynomial_envelope_for_gnn.pdf``.
     This is a generalization of :math:`u_p(x)`.
```

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/reduced_tensor_product.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/reduced_tensor_product.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/reduced_tensor_product_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/reduced_tensor_product_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/rotation.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/rotation.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/rotation_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/rotation_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/so3.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/so3.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/soft_one_hot_linspace.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/soft_one_hot_linspace.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/spherical_harmonics.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/spherical_harmonics.py`

 * *Files 1% similar despite different names*

```diff
@@ -191,14 +191,15 @@
 @partial(jax.custom_jvp, nondiff_argnums=(0, 2, 3))
 def _custom_jvp_spherical_harmonics(
     ls: Tuple[int, ...], x: jnp.ndarray, normalization: str, algorithm: Tuple[str]
 ) -> List[jnp.ndarray]:
     return _spherical_harmonics(ls, x, normalization, algorithm)
 
 
+@_custom_jvp_spherical_harmonics.defjvp
 def _jvp(
     ls: Tuple[int, ...], normalization: str, algorithm: Tuple[str], primals: Tuple[jnp.ndarray], tangents: Tuple[jnp.ndarray]
 ) -> List[jnp.ndarray]:
     (x,) = primals
     (x_dot,) = tangents
 
     js = tuple(max(0, l - 1) for l in ls)
@@ -225,17 +226,14 @@
                 axis=-1,
             )
         raise ValueError("Unknown algorithm: must be 'dense' or 'sparse'")
 
     return out, [h(l, r) if l > 0 else jnp.zeros_like(r) for l, r in zip(ls, res)]
 
 
-_custom_jvp_spherical_harmonics.defjvp(_jvp)
-
-
 def _recursive_spherical_harmonics(
     l: int, context: Dict[int, jnp.ndarray], input: jnp.ndarray, normalization: str, algorithm: Tuple[str]
 ) -> sympy.Array:
     context.update(dict(jnp=jnp, clebsch_gordan=clebsch_gordan))
 
     if l == 0:
         if 0 not in context:
```

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/spherical_harmonics_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/spherical_harmonics_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/su2.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/su2.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/tensor_products.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/tensor_products.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/tensor_products_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/tensor_products_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/util/decorators.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/util/decorators.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/util/jit.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/util/jit.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/util/math_numpy.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/util/math_numpy.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/util/optimize_jaxpr.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/util/optimize_jaxpr.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/util/test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/util/test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/_src/wigner_test.py` & `e3nn_jax-0.9.2/e3nn_jax/_src/wigner_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/experimental/point_convolution.py` & `e3nn_jax-0.9.2/e3nn_jax/experimental/point_convolution.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/experimental/point_convolution_test.py` & `e3nn_jax-0.9.2/e3nn_jax/experimental/point_convolution_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/experimental/transformer.py` & `e3nn_jax-0.9.2/e3nn_jax/experimental/transformer.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/experimental/transformer_test.py` & `e3nn_jax-0.9.2/e3nn_jax/experimental/transformer_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/experimental/voxel_convolution.py` & `e3nn_jax-0.9.2/e3nn_jax/experimental/voxel_convolution.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/experimental/voxel_convolution_test.py` & `e3nn_jax-0.9.2/e3nn_jax/experimental/voxel_convolution_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/experimental/voxel_pooling.py` & `e3nn_jax-0.9.2/e3nn_jax/experimental/voxel_pooling.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/experimental/voxel_pooling_test.py` & `e3nn_jax-0.9.2/e3nn_jax/experimental/voxel_pooling_test.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/irrep/__init__.py` & `e3nn_jax-0.9.2/e3nn_jax/irrep/__init__.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax/perm.py` & `e3nn_jax-0.9.2/e3nn_jax/perm.py`

 * *Files identical despite different names*

### Comparing `e3nn_jax-0.9.1/e3nn_jax.egg-info/PKG-INFO` & `e3nn_jax-0.9.2/e3nn_jax.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: e3nn-jax
-Version: 0.9.1
+Version: 0.9.2
 Summary: Equivariant convolutional neural networks for the group E(3) of 3 dimensional rotations, translations, and mirrors.
 Home-page: https://e3nn.org
 License: MIT
 Description: # e3nn-jax [![Coverage Status](https://coveralls.io/repos/github/e3nn/e3nn-jax/badge.svg?branch=main)](https://coveralls.io/github/e3nn/e3nn-jax?branch=main)
         
         # [Documentation](https://e3nn-jax.readthedocs.io/en/latest) [![Documentation Status](https://readthedocs.org/projects/e3nn-jax/badge/?version=latest)](https://e3nn-jax.readthedocs.io/en/latest/?badge=latest)
```

### Comparing `e3nn_jax-0.9.1/e3nn_jax.egg-info/SOURCES.txt` & `e3nn_jax-0.9.2/e3nn_jax.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -36,14 +36,15 @@
 e3nn_jax/_src/irreps_array_test.py
 e3nn_jax/_src/irreps_test.py
 e3nn_jax/_src/linear.py
 e3nn_jax/_src/linear_test.py
 e3nn_jax/_src/mlp.py
 e3nn_jax/_src/perm_test.py
 e3nn_jax/_src/poly_envelope.py
+e3nn_jax/_src/poly_envelope_test.py
 e3nn_jax/_src/reduced_tensor_product.py
 e3nn_jax/_src/reduced_tensor_product_test.py
 e3nn_jax/_src/rotation.py
 e3nn_jax/_src/rotation_test.py
 e3nn_jax/_src/so3.py
 e3nn_jax/_src/soft_one_hot_linspace.py
 e3nn_jax/_src/spherical_harmonics.py
```

### Comparing `e3nn_jax-0.9.1/setup.py` & `e3nn_jax-0.9.2/setup.py`

 * *Files identical despite different names*

