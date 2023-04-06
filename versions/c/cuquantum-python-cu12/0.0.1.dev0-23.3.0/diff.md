# Comparing `tmp/cuquantum_python_cu12-0.0.1.dev0-py3-none-manylinux2014_x86_64.whl.zip` & `tmp/cuquantum_python_cu12-23.3.0-cp39-cp39-manylinux2014_x86_64.whl.zip`

## zipinfo {}

```diff
@@ -1,7 +1,53 @@
-Zip file size: 6242 bytes, number of entries: 5
--rw-rw-r--  2.0 unx    11004 b- defN 23-Feb-16 18:55 cuquantum_python_cu12-0.0.1.dev0.dist-info/LICENSE
--rw-rw-r--  2.0 unx      350 b- defN 23-Feb-16 18:55 cuquantum_python_cu12-0.0.1.dev0.dist-info/METADATA
--rw-rw-r--  2.0 unx      109 b- defN 23-Feb-16 18:55 cuquantum_python_cu12-0.0.1.dev0.dist-info/WHEEL
--rw-rw-r--  2.0 unx        1 b- defN 23-Feb-16 18:55 cuquantum_python_cu12-0.0.1.dev0.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx      481 b- defN 23-Feb-16 18:55 cuquantum_python_cu12-0.0.1.dev0.dist-info/RECORD
-5 files, 11945 bytes uncompressed, 5332 bytes compressed:  55.4%
+Zip file size: 1880240 bytes, number of entries: 51
+-rw-r--r--  2.0 unx      101 b- defN 23-Mar-30 06:23 cuquantum/__init__.pxd
+-rw-r--r--  2.0 unx     1525 b- defN 23-Mar-30 06:23 cuquantum/__init__.py
+-rw-r--r--  2.0 unx     3767 b- defN 23-Mar-30 06:23 cuquantum/__main__.py
+-rw-r--r--  2.0 unx      295 b- defN 23-Mar-30 06:23 cuquantum/_version.py
+-rwxr-xr-x  2.0 unx   307200 b- defN 23-Mar-30 06:23 cuquantum/utils.cpython-39-x86_64-linux-gnu.so
+-rw-r--r--  2.0 unx     1142 b- defN 23-Mar-30 06:23 cuquantum/utils.pxd
+-rw-r--r--  2.0 unx     4057 b- defN 23-Mar-30 06:23 cuquantum/utils.pyx
+-rw-r--r--  2.0 unx      148 b- defN 23-Mar-30 06:23 cuquantum/custatevec/__init__.py
+-rwxr-xr-x  2.0 unx  3811816 b- defN 23-Mar-30 06:23 cuquantum/custatevec/custatevec.cpython-39-x86_64-linux-gnu.so
+-rw-r--r--  2.0 unx     3800 b- defN 23-Mar-30 06:23 cuquantum/custatevec/custatevec.pxd
+-rw-r--r--  2.0 unx   109360 b- defN 23-Mar-30 06:23 cuquantum/custatevec/custatevec.pyx
+-rw-r--r--  2.0 unx      467 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/__init__.py
+-rw-r--r--  2.0 unx    18453 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/circuit_converter.py
+-rw-r--r--  2.0 unx    10604 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/configuration.py
+-rwxr-xr-x  2.0 unx  2814496 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/cutensornet.cpython-39-x86_64-linux-gnu.so
+-rw-r--r--  2.0 unx     7540 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/cutensornet.pxd
+-rw-r--r--  2.0 unx   100156 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/cutensornet.pyx
+-rw-r--r--  2.0 unx     5398 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/memory.py
+-rw-r--r--  2.0 unx    21174 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/tensor.py
+-rw-r--r--  2.0 unx    52976 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/tensor_network.py
+-rw-r--r--  2.0 unx      101 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/__init__.py
+-rw-r--r--  2.0 unx     7458 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/circuit_converter_utils.py
+-rw-r--r--  2.0 unx     2811 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/circuit_parser_utils_cirq.py
+-rw-r--r--  2.0 unx     4577 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/circuit_parser_utils_qiskit.py
+-rw-r--r--  2.0 unx    16912 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/decomposition_utils.py
+-rw-r--r--  2.0 unx    15117 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/einsum_parser.py
+-rw-r--r--  2.0 unx     4124 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/enum_utils.py
+-rw-r--r--  2.0 unx     1429 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/formatters.py
+-rw-r--r--  2.0 unx     1230 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/mem_limit.py
+-rw-r--r--  2.0 unx     9378 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/optimizer_ifc.py
+-rw-r--r--  2.0 unx     1564 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/package_ifc.py
+-rw-r--r--  2.0 unx      919 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/package_ifc_cupy.py
+-rw-r--r--  2.0 unx      821 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/package_ifc_torch.py
+-rw-r--r--  2.0 unx      410 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/package_wrapper.py
+-rw-r--r--  2.0 unx     2230 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/tensor_ifc.py
+-rw-r--r--  2.0 unx     3113 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/tensor_ifc_cupy.py
+-rw-r--r--  2.0 unx     2348 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/tensor_ifc_numpy.py
+-rw-r--r--  2.0 unx     2699 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/tensor_ifc_torch.py
+-rw-r--r--  2.0 unx     3729 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/tensor_wrapper.py
+-rw-r--r--  2.0 unx     2330 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/typemaps.py
+-rw-r--r--  2.0 unx    17332 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/_internal/utils.py
+-rw-r--r--  2.0 unx      155 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/experimental/__init__.py
+-rw-r--r--  2.0 unx     4809 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/experimental/configuration.py
+-rw-r--r--  2.0 unx    22283 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/experimental/tensor_network.py
+-rw-r--r--  2.0 unx       96 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/experimental/_internal/__init__.py
+-rw-r--r--  2.0 unx     1923 b- defN 23-Mar-30 06:23 cuquantum/cutensornet/experimental/_internal/utils.py
+-rw-r--r--  2.0 unx     1522 b- defN 23-Mar-30 06:23 cuquantum_python_cu12-23.3.0.dist-info/LICENSE
+-rw-r--r--  2.0 unx     8168 b- defN 23-Mar-30 06:23 cuquantum_python_cu12-23.3.0.dist-info/METADATA
+-rw-r--r--  2.0 unx      111 b- defN 23-Mar-30 06:23 cuquantum_python_cu12-23.3.0.dist-info/WHEEL
+-rw-r--r--  2.0 unx       10 b- defN 23-Mar-30 06:23 cuquantum_python_cu12-23.3.0.dist-info/top_level.txt
+-rw-rw-r--  2.0 unx     5071 b- defN 23-Mar-30 06:23 cuquantum_python_cu12-23.3.0.dist-info/RECORD
+51 files, 7419255 bytes uncompressed, 1871918 bytes compressed:  74.8%
```

## zipnote {}

```diff
@@ -1,16 +1,154 @@
-Filename: cuquantum_python_cu12-0.0.1.dev0.dist-info/LICENSE
+Filename: cuquantum/__init__.pxd
 Comment: 
 
-Filename: cuquantum_python_cu12-0.0.1.dev0.dist-info/METADATA
+Filename: cuquantum/__init__.py
 Comment: 
 
-Filename: cuquantum_python_cu12-0.0.1.dev0.dist-info/WHEEL
+Filename: cuquantum/__main__.py
 Comment: 
 
-Filename: cuquantum_python_cu12-0.0.1.dev0.dist-info/top_level.txt
+Filename: cuquantum/_version.py
 Comment: 
 
-Filename: cuquantum_python_cu12-0.0.1.dev0.dist-info/RECORD
+Filename: cuquantum/utils.cpython-39-x86_64-linux-gnu.so
+Comment: 
+
+Filename: cuquantum/utils.pxd
+Comment: 
+
+Filename: cuquantum/utils.pyx
+Comment: 
+
+Filename: cuquantum/custatevec/__init__.py
+Comment: 
+
+Filename: cuquantum/custatevec/custatevec.cpython-39-x86_64-linux-gnu.so
+Comment: 
+
+Filename: cuquantum/custatevec/custatevec.pxd
+Comment: 
+
+Filename: cuquantum/custatevec/custatevec.pyx
+Comment: 
+
+Filename: cuquantum/cutensornet/__init__.py
+Comment: 
+
+Filename: cuquantum/cutensornet/circuit_converter.py
+Comment: 
+
+Filename: cuquantum/cutensornet/configuration.py
+Comment: 
+
+Filename: cuquantum/cutensornet/cutensornet.cpython-39-x86_64-linux-gnu.so
+Comment: 
+
+Filename: cuquantum/cutensornet/cutensornet.pxd
+Comment: 
+
+Filename: cuquantum/cutensornet/cutensornet.pyx
+Comment: 
+
+Filename: cuquantum/cutensornet/memory.py
+Comment: 
+
+Filename: cuquantum/cutensornet/tensor.py
+Comment: 
+
+Filename: cuquantum/cutensornet/tensor_network.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/__init__.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/circuit_converter_utils.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/circuit_parser_utils_cirq.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/circuit_parser_utils_qiskit.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/decomposition_utils.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/einsum_parser.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/enum_utils.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/formatters.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/mem_limit.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/optimizer_ifc.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/package_ifc.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/package_ifc_cupy.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/package_ifc_torch.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/package_wrapper.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/tensor_ifc.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/tensor_ifc_cupy.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/tensor_ifc_numpy.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/tensor_ifc_torch.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/tensor_wrapper.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/typemaps.py
+Comment: 
+
+Filename: cuquantum/cutensornet/_internal/utils.py
+Comment: 
+
+Filename: cuquantum/cutensornet/experimental/__init__.py
+Comment: 
+
+Filename: cuquantum/cutensornet/experimental/configuration.py
+Comment: 
+
+Filename: cuquantum/cutensornet/experimental/tensor_network.py
+Comment: 
+
+Filename: cuquantum/cutensornet/experimental/_internal/__init__.py
+Comment: 
+
+Filename: cuquantum/cutensornet/experimental/_internal/utils.py
+Comment: 
+
+Filename: cuquantum_python_cu12-23.3.0.dist-info/LICENSE
+Comment: 
+
+Filename: cuquantum_python_cu12-23.3.0.dist-info/METADATA
+Comment: 
+
+Filename: cuquantum_python_cu12-23.3.0.dist-info/WHEEL
+Comment: 
+
+Filename: cuquantum_python_cu12-23.3.0.dist-info/top_level.txt
+Comment: 
+
+Filename: cuquantum_python_cu12-23.3.0.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

