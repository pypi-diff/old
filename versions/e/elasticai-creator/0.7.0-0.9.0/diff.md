# Comparing `tmp/elasticai.creator-0.7.0.tar.gz` & `tmp/elasticai.creator-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "elasticai.creator-0.7.0.tar", max compression
+gzip compressed data, was "elasticai.creator-0.9.0.tar", max compression
```

## Comparing `elasticai.creator-0.7.0.tar` & `elasticai.creator-0.9.0.tar`

### file list

```diff
@@ -1,128 +1,98 @@
--rw-r--r--   0        0        0     1079 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/LICENSE
--rw-r--r--   0        0        0     8573 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/README.md
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/__init__.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/__init__.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/brevitas/__init__.py
--rw-r--r--   0        0        0     4467 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/brevitas/brevitas_model_comparison.py
--rw-r--r--   0        0        0     1957 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/brevitas/brevitas_quantizers.py
--rw-r--r--   0        0        0     2659 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/brevitas/brevitas_representation.py
--rw-r--r--   0        0        0      509 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/brevitas/translation_functions/__init__.py
--rw-r--r--   0        0        0     2265 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/brevitas/translation_functions/conv.py
--rw-r--r--   0        0        0      270 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/brevitas/translation_functions/identity.py
--rw-r--r--   0        0        0      757 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/brevitas/translation_functions/linear.py
--rw-r--r--   0        0        0      768 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/brevitas/translation_functions/quantizers.py
--rw-r--r--   0        0        0      866 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/brevitas/translation_functions/translation_function_tools.py
--rw-r--r--   0        0        0     1456 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/brevitas/translation_mapping.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/examples/__init__.py
--rw-r--r--   0        0        0     4305 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/examples/basic.py
--rw-r--r--   0        0        0     5231 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_all_vhd_files_for_lstm_cell.py
--rw-r--r--   0        0        0     3084 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_lstm_cell_testbench.py
--rw-r--r--   0        0        0     1371 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_rom_vhd.py
--rw-r--r--   0        0        0     1082 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_sigmoid_testbench.py
--rw-r--r--   0        0        0      986 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_sigmoid_vhd.py
--rw-r--r--   0        0        0     1126 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_tanh_testbench.py
--rw-r--r--   0        0        0      942 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_tanh_vhd.py
--rw-r--r--   0        0        0      376 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/examples/parametrize_convolution.py
--rw-r--r--   0        0        0     1583 2022-06-05 13:03:18.794354 elasticai.creator-0.7.0/elasticai/creator/examples/precompute_convolution.py
--rw-r--r--   0        0        0      649 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/examples/precompute_sigmoid_layer.py
--rw-r--r--   0        0        0     5137 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/examples/qlstm.py
--rw-r--r--   0        0        0     4809 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/examples/simple_qlstm_part_of_speech_tagging.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/__init__.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/brevitas_representation/__init__.py
--rw-r--r--   0        0        0     1370 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/brevitas_representation/conv_params_comparison.py
--rw-r--r--   0        0        0     3294 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/brevitas_representation/test_brevitas_model_comparison.py
--rw-r--r--   0        0        0      250 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/brevitas_representation/test_brevitas_model_equals.py
--rw-r--r--   0        0        0     3338 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/brevitas_representation/test_conv1d.py
--rw-r--r--   0        0        0     3339 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/brevitas_representation/test_conv2d.py
--rw-r--r--   0        0        0     4077 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/brevitas_representation/test_depthwise_conv1d.py
--rw-r--r--   0        0        0     2955 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/brevitas_representation/test_linear.py
--rw-r--r--   0        0        0     1114 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/brevitas_representation/test_quantizers.py
--rw-r--r--   0        0        0     2306 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/test_jit.py
--rw-r--r--   0        0        0     6004 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/test_onnx_export.py
--rw-r--r--   0        0        0     2277 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/test_translation_function_tools.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/__init__.py
--rw-r--r--   0        0        0     6090 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/expected_lstm_cell_testbench.vhd
--rw-r--r--   0        0        0     2654 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/test_generate_lstm_cell_testbench_vhd.py
--rw-r--r--   0        0        0     2125 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/test_generate_rom_vhd.py
--rw-r--r--   0        0        0     3324 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/test_generate_sigmoid_testbench_vhd.py
--rw-r--r--   0        0        0     7334 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/test_generate_sigmoid_vhd.py
--rw-r--r--   0        0        0     4500 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/test_generate_tanh_testbench_vhd.py
--rw-r--r--   0        0        0    24720 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/test_generate_tanh_vhd.py
--rw-r--r--   0        0        0      835 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/vhdl_file_test_case.py
--rw-r--r--   0        0        0       42 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/mlframework/__init__.py
--rw-r--r--   0        0        0      705 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/mlframework/typing.py
--rw-r--r--   0        0        0     1906 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/onnx.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/precomputation/__init__.py
--rw-r--r--   0        0        0     8019 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/precomputation/breakdown.py
--rw-r--r--   0        0        0     5600 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/precomputation/input_domains.py
--rw-r--r--   0        0        0     2944 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/precomputation/io_table.py
--rw-r--r--   0        0        0     1463 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/precomputation/metaprogramming.py
--rw-r--r--   0        0        0     5029 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/precomputation/precomputation.py
--rw-r--r--   0        0        0    13156 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/qat/QRigL.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/qat/__init__.py
--rw-r--r--   0        0        0     6711 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/qat/blocks.py
--rw-r--r--   0        0        0      318 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/qat/constraints.py
--rw-r--r--   0        0        0      939 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/qat/functional.py
--rw-r--r--   0        0        0    20804 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/qat/layers.py
--rw-r--r--   0        0        0     2944 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/qat/masks.py
--rw-r--r--   0        0        0      161 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/representations.py
--rw-r--r--   0        0        0     1121 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/resource_utils.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/systemTests/__init__.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/systemTests/brevitas_representation/__init__.py
--rw-r--r--   0        0        0     3667 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/systemTests/brevitas_representation/models_definition.py
--rw-r--r--   0        0        0     1396 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/systemTests/brevitas_representation/test_brevitas_representation.py
--rw-r--r--   0        0        0     1617 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/systemTests/brevitas_representation/test_input.py
--rw-r--r--   0        0        0     1898 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/systemTests/brevitas_representation/test_onnx_export.py
--rw-r--r--   0        0        0     1042 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tags_utils.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/__init__.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/brevitas_representation/__init__.py
--rw-r--r--   0        0        0     3005 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/brevitas_representation/test_brevitas_model_comparison.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/precomputation/__init__.py
--rw-r--r--   0        0        0     7347 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/precomputation/test_derive_data_sets.py
--rw-r--r--   0        0        0     2629 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/precomputation/test_io_table.py
--rw-r--r--   0        0        0     1010 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/precomputation/test_metaprogramming.py
--rw-r--r--   0        0        0     2925 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/precomputation/test_precomputation.py
--rw-r--r--   0        0        0     1265 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/precomputation/test_tags.py
--rw-r--r--   0        0        0      215 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/precomputation/test_truth_table.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/qat/__init__.py
--rw-r--r--   0        0        0     5935 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/qat/test_QRigL.py
--rw-r--r--   0        0        0     4536 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/qat/test_block.py
--rw-r--r--   0        0        0     7783 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/qat/test_breakdown.py
--rw-r--r--   0        0        0     1595 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/qat/test_functional.py
--rw-r--r--   0        0        0    18726 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/qat/test_layer.py
--rw-r--r--   0        0        0     2145 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/qat/test_masks.py
--rw-r--r--   0        0        0      405 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/tensor_test_case.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/__init__.py
--rw-r--r--   0        0        0    10780 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/test_language.py
--rw-r--r--   0        0        0     6912 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/test_language_testbench.py
--rw-r--r--   0        0        0    15998 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/test_number_representations.py
--rw-r--r--   0        0        0     2024 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/test_precomputed_scalar_function_process.py
--rw-r--r--   0        0        0     3214 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/test_templates.py
--rw-r--r--   0        0        0     1006 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/vhdl_file_testcase.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/__init__.py
--rw-r--r--   0        0        0     3897 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/generator_functions_for_lstm_layer.py
--rw-r--r--   0        0        0     4788 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/generator_functions_for_one_lstm_cell.py
--rw-r--r--   0        0        0       62 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/io_table.py
--rw-r--r--   0        0        0    16929 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/language.py
--rw-r--r--   0        0        0      778 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/language_testbench.py
--rw-r--r--   0        0        0    13838 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/lstm_testbench_generator.py
--rw-r--r--   0        0        0    11587 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/number_representations.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/precomputed_convs/__init__.py
--rw-r--r--   0        0        0    12210 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/precomputed_scalar_function.py
--rw-r--r--   0        0        0     1553 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/rom.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/__init__.py
--rw-r--r--   0        0        0     3982 2022-06-05 13:03:18.798354 elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/dual_port_2_clock_ram.vhd
--rw-r--r--   0        0        0    17024 2022-06-05 13:03:18.802354 elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/lstm_cell.vhd
--rw-r--r--   0        0        0     2821 2022-06-05 13:03:18.802354 elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/lstm_common.vhd
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.802354 elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/precomputed_convs/__init__.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.802354 elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/precomputed_convs/top.tpl.vhd
--rw-r--r--   0        0        0      448 2022-06-05 13:03:18.802354 elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/precomputed_convs/truth_table.tpl.vhd
--rw-r--r--   0        0        0      891 2022-06-05 13:03:18.802354 elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/rom.tpl.vhd
--rw-r--r--   0        0        0      923 2022-06-05 13:03:18.802354 elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/utils.py
--rw-r--r--   0        0        0     3692 2022-06-05 13:03:18.802354 elasticai.creator-0.7.0/elasticai/creator/vhdl/truth_table.py
--rw-r--r--   0        0        0        0 2022-06-05 13:03:18.802354 elasticai.creator-0.7.0/elasticai/creator/vhdl/vhdl_formatter/__init__.py
--rw-r--r--   0        0        0       79 2022-06-05 13:03:18.802354 elasticai.creator-0.7.0/elasticai/creator/vhdl/vhdl_formatter/config.json
--rw-r--r--   0        0        0      708 2022-06-05 13:03:18.802354 elasticai.creator-0.7.0/elasticai/creator/vhdl/vhdl_formatter/vhdl_formatter.py
--rw-r--r--   0        0        0     1741 2022-06-05 13:03:26.538357 elasticai.creator-0.7.0/pyproject.toml
--rw-r--r--   0        0        0    10753 2022-06-05 13:03:38.158149 elasticai.creator-0.7.0/setup.py
--rw-r--r--   0        0        0     9598 2022-06-05 13:03:38.159208 elasticai.creator-0.7.0/PKG-INFO
+-rw-r--r--   0        0        0     1079 2022-05-22 12:40:11.756915 elasticai.creator-0.9.0/LICENSE
+-rw-r--r--   0        0        0     8303 2022-06-09 17:56:49.995878 elasticai.creator-0.9.0/README.md
+-rw-r--r--   0        0        0        0 2022-05-09 17:11:40.504756 elasticai.creator-0.9.0/elasticai/__init__.py
+-rw-r--r--   0        0        0        0 2022-05-09 17:11:40.504756 elasticai.creator-0.9.0/elasticai/creator/__init__.py
+-rw-r--r--   0        0        0        0 2022-05-09 17:11:40.504756 elasticai.creator-0.9.0/elasticai/creator/examples/__init__.py
+-rw-r--r--   0        0        0     4305 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/examples/basic.py
+-rw-r--r--   0        0        0     4644 2022-06-25 13:28:12.387905 elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_all_vhd_files_for_lstm_cell.py
+-rw-r--r--   0        0        0     3434 2022-06-25 13:28:12.387905 elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_lstm_cell_testbench.py
+-rw-r--r--   0        0        0     1171 2022-06-25 13:28:12.387905 elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_rom_vhd.py
+-rw-r--r--   0        0        0     1237 2022-06-25 13:28:12.387905 elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_sigmoid_testbench.py
+-rw-r--r--   0        0        0     1130 2022-06-25 13:28:12.387905 elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_sigmoid_vhd.py
+-rw-r--r--   0        0        0     1267 2022-06-25 13:28:12.387905 elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_tanh_testbench.py
+-rw-r--r--   0        0        0     1110 2022-06-25 13:28:12.387905 elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_tanh_vhd.py
+-rw-r--r--   0        0        0      376 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/examples/parametrize_convolution.py
+-rw-r--r--   0        0        0     1583 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/examples/precompute_convolution.py
+-rw-r--r--   0        0        0      649 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/examples/precompute_sigmoid_layer.py
+-rw-r--r--   0        0        0     5137 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/examples/qlstm.py
+-rw-r--r--   0        0        0     4809 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/examples/simple_qlstm_part_of_speech_tagging.py
+-rw-r--r--   0        0        0        0 2022-05-09 17:11:40.508756 elasticai.creator-0.9.0/elasticai/creator/integrationTests/__init__.py
+-rw-r--r--   0        0        0     2306 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/integrationTests/test_jit.py
+-rw-r--r--   0        0        0     6064 2022-06-09 17:56:49.995878 elasticai.creator-0.9.0/elasticai/creator/integrationTests/test_onnx_export.py
+-rw-r--r--   0        0        0        0 2022-05-09 17:11:40.508756 elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/__init__.py
+-rw-r--r--   0        0        0     6090 2022-06-25 13:28:12.387905 elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/expected_lstm_cell_testbench.vhd
+-rw-r--r--   0        0        0     3424 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/test_generate_lstm_cell_testbench_vhd.py
+-rw-r--r--   0        0        0     1798 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/test_generate_rom_vhd.py
+-rw-r--r--   0        0        0     3483 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/test_generate_sigmoid_testbench_vhd.py
+-rw-r--r--   0        0        0     7477 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/test_generate_sigmoid_vhd.py
+-rw-r--r--   0        0        0     4631 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/test_generate_tanh_testbench_vhd.py
+-rw-r--r--   0        0        0    24921 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/test_generate_tanh_vhd.py
+-rw-r--r--   0        0        0      848 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/vhdl_file_test_case.py
+-rw-r--r--   0        0        0       42 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/mlframework/__init__.py
+-rw-r--r--   0        0        0      705 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/mlframework/typing.py
+-rw-r--r--   0        0        0     1906 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/onnx.py
+-rw-r--r--   0        0        0        0 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/precomputation/__init__.py
+-rw-r--r--   0        0        0     8019 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/precomputation/breakdown.py
+-rw-r--r--   0        0        0     5600 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/precomputation/input_domains.py
+-rw-r--r--   0        0        0     2944 2022-06-17 08:56:18.457555 elasticai.creator-0.9.0/elasticai/creator/precomputation/io_table.py
+-rw-r--r--   0        0        0     1463 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/precomputation/metaprogramming.py
+-rw-r--r--   0        0        0     5083 2022-06-09 17:56:49.995878 elasticai.creator-0.9.0/elasticai/creator/precomputation/precomputation.py
+-rw-r--r--   0        0        0    13156 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/qat/QRigL.py
+-rw-r--r--   0        0        0        0 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/qat/__init__.py
+-rw-r--r--   0        0        0     6711 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/qat/blocks.py
+-rw-r--r--   0        0        0      318 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/qat/constraints.py
+-rw-r--r--   0        0        0      939 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/qat/functional.py
+-rw-r--r--   0        0        0    20804 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/qat/layers.py
+-rw-r--r--   0        0        0     2944 2022-05-26 10:10:38.904466 elasticai.creator-0.9.0/elasticai/creator/qat/masks.py
+-rw-r--r--   0        0        0       75 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/representations.py
+-rw-r--r--   0        0        0     1090 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/resource_utils.py
+-rw-r--r--   0        0        0     1042 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tags_utils.py
+-rw-r--r--   0        0        0        0 2022-05-09 17:11:40.508756 elasticai.creator-0.9.0/elasticai/creator/tests/__init__.py
+-rw-r--r--   0        0        0        0 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/precomputation/__init__.py
+-rw-r--r--   0        0        0     7347 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/precomputation/test_derive_data_sets.py
+-rw-r--r--   0        0        0     2629 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/precomputation/test_io_table.py
+-rw-r--r--   0        0        0     1010 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/precomputation/test_metaprogramming.py
+-rw-r--r--   0        0        0     2920 2022-06-09 17:56:49.995878 elasticai.creator-0.9.0/elasticai/creator/tests/precomputation/test_precomputation.py
+-rw-r--r--   0        0        0     1265 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/precomputation/test_tags.py
+-rw-r--r--   0        0        0      215 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/precomputation/test_truth_table.py
+-rw-r--r--   0        0        0        0 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/qat/__init__.py
+-rw-r--r--   0        0        0     5935 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/qat/test_QRigL.py
+-rw-r--r--   0        0        0     4536 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/qat/test_block.py
+-rw-r--r--   0        0        0     7783 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/qat/test_breakdown.py
+-rw-r--r--   0        0        0     1595 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/qat/test_functional.py
+-rw-r--r--   0        0        0    18726 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/qat/test_layer.py
+-rw-r--r--   0        0        0     2145 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/qat/test_masks.py
+-rw-r--r--   0        0        0      405 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/tensor_test_case.py
+-rw-r--r--   0        0        0        0 2022-05-09 17:11:40.512757 elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/__init__.py
+-rw-r--r--   0        0        0    11085 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/test_language.py
+-rw-r--r--   0        0        0     7411 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/test_language_testbench.py
+-rw-r--r--   0        0        0    15102 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/test_number_representations.py
+-rw-r--r--   0        0        0     2458 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/test_precomputed_scalar_function_process.py
+-rw-r--r--   0        0        0     3214 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/test_templates.py
+-rw-r--r--   0        0        0     1006 2022-05-09 17:11:40.512757 elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/vhdl_file_testcase.py
+-rw-r--r--   0        0        0        0 2022-05-09 17:11:40.512757 elasticai.creator-0.9.0/elasticai/creator/vhdl/__init__.py
+-rw-r--r--   0        0        0     4580 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/vhdl/generator_functions_for_lstm.py
+-rw-r--r--   0        0        0       62 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/io_table.py
+-rw-r--r--   0        0        0    17063 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/vhdl/language.py
+-rw-r--r--   0        0        0      778 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/language_testbench.py
+-rw-r--r--   0        0        0    14131 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/vhdl/lstm_testbench_generator.py
+-rw-r--r--   0        0        0     9784 2022-06-25 13:28:12.391904 elasticai.creator-0.9.0/elasticai/creator/vhdl/number_representations.py
+-rw-r--r--   0        0        0        0 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/precomputed_convs/__init__.py
+-rw-r--r--   0        0        0    11999 2022-06-25 13:28:12.395904 elasticai.creator-0.9.0/elasticai/creator/vhdl/precomputed_scalar_function.py
+-rw-r--r--   0        0        0     1781 2022-06-25 13:28:12.395904 elasticai.creator-0.9.0/elasticai/creator/vhdl/rom.py
+-rw-r--r--   0        0        0        0 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/__init__.py
+-rw-r--r--   0        0        0     3982 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/dual_port_2_clock_ram.vhd
+-rw-r--r--   0        0        0    17024 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/lstm_cell.vhd
+-rw-r--r--   0        0        0     2821 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/lstm_common.vhd
+-rw-r--r--   0        0        0        0 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/precomputed_convs/__init__.py
+-rw-r--r--   0        0        0        0 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/precomputed_convs/top.tpl.vhd
+-rw-r--r--   0        0        0      448 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/precomputed_convs/truth_table.tpl.vhd
+-rw-r--r--   0        0        0      891 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/rom.tpl.vhd
+-rw-r--r--   0        0        0      923 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/utils.py
+-rw-r--r--   0        0        0     3692 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/truth_table.py
+-rw-r--r--   0        0        0        0 2022-05-09 17:11:40.512757 elasticai.creator-0.9.0/elasticai/creator/vhdl/vhdl_formatter/__init__.py
+-rw-r--r--   0        0        0       79 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/vhdl_formatter/config.json
+-rw-r--r--   0        0        0      708 2022-05-26 10:10:38.908466 elasticai.creator-0.9.0/elasticai/creator/vhdl/vhdl_formatter/vhdl_formatter.py
+-rw-r--r--   0        0        0     1663 2022-06-25 13:28:12.395904 elasticai.creator-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0    10176 2022-06-25 13:45:20.460888 elasticai.creator-0.9.0/setup.py
+-rw-r--r--   0        0        0     9300 2022-06-25 13:45:20.461211 elasticai.creator-0.9.0/PKG-INFO
```

### Comparing `elasticai.creator-0.7.0/LICENSE` & `elasticai.creator-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/README.md` & `elasticai.creator-0.9.0/README.md`

 * *Files 8% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 # ElasticAi.creator
 
 Design, train and compile neural networks optimized specifically for FPGAs.
 Obtaining a final model is typically a three stage process.
-* design and train it using the layers provided in the `elasticai.creator` package.
+* design and train it using the layers provided in the `elasticai.creator.qat` package.
 * translate the model to a target representation, e.g. VHDL
 * compile the intermediate representation with a third party tool, e.g. Xilinx Vivado (TM)
 
-This version currently only supports [Brevitas](https://github.com/Xilinx/brevitas) and parts of VHDL as target representations.
+This version currently only supports parts of VHDL as target representations.
 
 The project is part of the elastic ai ecosystem developed by the Embedded Systems Department of the University Duisburg-Essen. For more details checkout the slides at [researchgate](https://www.researchgate.net/publication/356372207_In-Situ_Artificial_Intelligence_for_Self-_Devices_The_Elastic_AI_Ecosystem_Tutorial).
 
 
 ## Table of contents
 
 - [Users Guide](#users-guide)
@@ -28,16 +28,16 @@
 ```
 
 
 ## Structure of the Project
 
 The structure of the project is as follows.
 The [creator](elasticai/creator) folder includes all main concepts of our project, especially the qtorch implementation which is our implementation of quantized PyTorch layer.
-It also includes the supported target representations, like the subfolder [brevitas](elasticai/creator/brevitas) is for the translation to Brevitas or the subfolder [vhdl](elasticai/creator/vhdl) for the translation to Vhdl.
-Additionally, we have folders for [unit tests](elasticai/creator/tests), [integration tests](elasticai/creator/integrationTests) and [system tests](elasticai/creator/systemTests).
+It also includes the supported target representations, like the subfolder [vhdl](elasticai/creator/vhdl) is for the translation to vhdl.
+Additionally, we have folders for [unit tests](elasticai/creator/tests) and [integration tests](elasticai/creator/integrationTests).
 
 
 ## General Limitations
 
 By now we only support Sequential models for our translations.
 
 ## Developers Guide
@@ -52,14 +52,21 @@
 pip install pre-commit
 poetry install -D
 pre-commit install
 npm install --save-dev @commitlint/{config-conventional,cli}
 sudo apt install ghdl
 ```
 
+### Install/Compile ONNX dependency
+```bash
+sudo apt install python3-dev libprotobuf-dev protobuf-compiler
+export CMAKE_ARGS="-DONNX_USE_PROTOBUF_SHARED_LIBS=ON"
+poetry install --extras onnx
+```
+
 ### Commit Message Scopes
 
 - **qat**: quantization-aware-training
   - Examples: `QConv1D`, `QLSTM`, autograd functions, etc.
 - **readme**
 - **precomputation**: entities that deal with the precomputation of ML components
   - Examples: the `precomputable` decorator or the `IOTable` class
@@ -67,19 +74,19 @@
   - Examples: `vhdl.TruthTable`, `vhdl.LSTMCell`
 - **gh-workflow**
 - **pyproject**: changes to the `pyproject.toml` file will typically either update run or dev dependencies
 - **typing**: changing type annotations and changes to code to allow consistent type annotations
 - **pre-commit**
 
 ### Adding new translation targets
-New translation targets should be located in their own folder, e.g. Brevitas for translating from any language to Brevitas.
+New translation targets should be located in their own folder, e.g. vhdl for translating from any language to vhdl.
 Workflow for adding a new translation:
 1. Obtain a structure, such as a list in a sequential case, which will describe the connection between every component.
 2. Identify and label relevant structures, in the base cases it can be simply separate layers.
-3. Map each structure to its function which will convert it, like for [example](elasticai/creator/brevitas/translation_mapping.py).
+3. Map each structure to its function which will convert it.
 4. Do such conversions.
 5. Recreate connections based on 1.
 
 Each sub-step should be separable and it helps for testing if common functions are wrapped around an adapter.
 
 ### Syntax Checking
 
@@ -123,16 +130,15 @@
 
 
 #### Diectory structure and file names
 Files containing tests for a python module should be located in a test directory for the sake of separation of concerns.
 Each file in the test directory should contain tests for one and only one class/function defined in the module.
 Files containing tests should be named according to the rubric
 `test_ClassName.py`.
-Next, if needed for more specific tests define a class which is a subclass of unittest.TestCase like [test_brevitas_model_comparison](elasticai/creator/integrationTests/brevitas_representation/test_brevitas_model_comparison.py) in the integration tests folder.
-Then subclass it, in this class define a setUp method (and possibly tearDown) to create the global environment.
+Next, if needed for more specific tests define a class. Then subclass it, in this class define a setUp method (and possibly tearDown) to create the global environment.
 It avoids introducing the category of bugs associated with copying and pasting code for reuse.
 This class should be named similarly to the file name.
 There's a category of bugs that appear if  the initialization parameters defined at the top of the test file are directly used: some tests require the initialization parameters to be changed slightly.
 Its possible to define a parameter and have it change in memory as a result of a test.
 Subsequent tests will therefore throw errors.
 Each class contains methods that implement a test.
 These methods are named according to the rubric
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/examples/basic.py` & `elasticai.creator-0.9.0/elasticai/creator/examples/basic.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_all_vhd_files_for_lstm_cell.py` & `elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_all_vhd_files_for_lstm_cell.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,22 +1,23 @@
 import os
-import random
 from argparse import ArgumentParser
+from functools import partial
 
 import numpy as np
 import torch
 
 from elasticai.creator.qat.layers import QLSTMCell
 from elasticai.creator.resource_utils import copy_file
-from elasticai.creator.vhdl.generator_functions_for_one_lstm_cell import (
-    define_weights_and_bias,
+from elasticai.creator.vhdl.generator_functions_for_lstm import (
+    extract_fixed_point_weights_and_bias,
     generate_rom_file,
-    inference_model,
+    inference_model_on_random_data,
 )
 from elasticai.creator.vhdl.lstm_testbench_generator import LSTMCellTestBench
+from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point
 from elasticai.creator.vhdl.precomputed_scalar_function import Sigmoid, Tanh
 from elasticai.creator.vhdl.vhdl_formatter.vhdl_formatter import format_vhdl
 
 """
 this module generates all vhd files for a single lstm cell
 """
 
@@ -34,15 +35,15 @@
         input_size=input_size,
         hidden_size=hidden_size,
         state_quantizer=lambda x: x,
         weight_quantizer=lambda x: x,
     )
 
 
-if __name__ == "__main__":
+def main() -> None:
     arg_parser = ArgumentParser()
     arg_parser.add_argument(
         "--path",
         help="path to folder for generated vhd files",
         required=True,
     )
     args = arg_parser.parse_args()
@@ -50,113 +51,91 @@
         os.mkdir(args.path)
 
     def destination_path(file_name: str) -> str:
         return os.path.join(args.path, file_name)
 
     # set the current values
     torch.manual_seed(0)
-    random.seed(0)
-    current_frac_bits = 8
-    current_nbits = 16
-    current_input_size = 1
-    current_hidden_size = 20
-    current_len_weights = (
-        current_input_size + current_hidden_size
-    ) * current_hidden_size
-    current_len_bias = current_hidden_size
-
-    lstm_cell = define_lstm_cell(current_input_size, current_hidden_size)
-    weights_list, bias_list = define_weights_and_bias(
-        lstm_cell,
-        current_frac_bits,
-        current_len_weights,
-        current_len_bias,
+    frac_bits = 8
+    total_bits = 16
+    input_size = 1
+    hidden_size = 20
+
+    to_fp = partial(
+        float_values_to_fixed_point, total_bits=total_bits, frac_bits=frac_bits
     )
-    print("weights_list", weights_list)
-    print("bias_list", bias_list)
-    x_h_test_input, c_test_input, h_output = inference_model(
-        lstm_cell,
-        current_frac_bits,
-        current_input_size,
-        current_hidden_size,
+
+    lstm_cell = define_lstm_cell(input_size, hidden_size)
+
+    weights_list, bias_list = extract_fixed_point_weights_and_bias(
+        lstm_cell, total_bits, frac_bits
     )
-    print("x_h_test_input", x_h_test_input)
-    print("c_test_input", c_test_input)
-    print("h_output", h_output)
+    print("weights_list:", [list(map(lambda x: x.to_hex(), w)) for w in weights_list])
+    print("bias_list:", [list(map(lambda x: x.to_hex(), b)) for b in bias_list])
 
-    # generate source files for use-case
+    x_h_test_input, c_test_input, h_output = inference_model_on_random_data(
+        lstm_cell, total_bits, frac_bits
+    )
+    print("x_h_test_input:", list(map(lambda x: x.to_hex(), x_h_test_input)))
+    print("c_test_input:", list(map(lambda x: x.to_hex(), c_test_input)))
+    print("h_output:", list(map(lambda x: x.to_hex(), h_output)))
 
-    # generate weights source files
-    weight_name_index_dict = {0: "wi", 1: "wf", 2: "wg", 3: "wo"}
-    for key, value in weight_name_index_dict.items():
-        generate_rom_file(
-            file_path=destination_path(f"{value}_rom.vhd"),
-            weights_or_bias_list=weights_list,
-            nbits=current_nbits,
-            name=value,
-            index=key,
-        )
+    # generate source files for use-case
 
-    # generate bias source files
-    bias_name_index_dict = {0: "bi", 1: "bf", 2: "bg", 3: "bo"}
-    for key, value in bias_name_index_dict.items():
+    # generate weight and bias source files
+    weight_names = ["wi", "wf", "wg", "wo", "bi", "bf", "bg", "bo"]
+    for name, values in zip(weight_names, weights_list + bias_list):
         generate_rom_file(
-            file_path=destination_path(f"{value}_rom.vhd"),
-            weights_or_bias_list=bias_list,
-            nbits=current_nbits,
-            name=value,
-            index=key,
+            file_path=destination_path(f"{name}_rom.vhd"),
+            rom_name=f"{name}_rom",
+            values=values,
+            resource_option="auto",
         )
 
     # generate sigmoid and tanh activation source files
     file_path_sigmoid = destination_path("sigmoid.vhd")
     with open(file_path_sigmoid, "w") as writer:
         sigmoid = Sigmoid(
-            data_width=current_nbits,
-            frac_width=current_frac_bits,
-            x=np.linspace(-2.5, 2.5, 256),
+            x=to_fp(np.linspace(-2.5, 2.5, 256).tolist()),
         )
         sigmoid_code = sigmoid()
         for line in sigmoid_code:
             writer.write(line + "\n")
 
     file_path_tanh = destination_path("tanh.vhd")
     with open(file_path_tanh, "w") as writer:
         tanh = Tanh(
-            data_width=current_nbits,
-            frac_width=current_frac_bits,
-            x=np.linspace(-1, 1, 256),
+            x=to_fp(np.linspace(-1, 1, 256).tolist()),
         )
         tanh_code = tanh()
         for line in tanh_code:
             writer.write(line + "\n")
 
     # generate testbench file for use-case
     file_path_testbench = destination_path("lstm_cell_tb.vhd")
     with open(file_path_testbench, "w") as writer:
         lstm_cell_tb = LSTMCellTestBench(
-            data_width=current_nbits,
-            frac_width=current_frac_bits,
-            input_size=current_input_size,
-            hidden_size=current_hidden_size,
+            input_size=input_size,
+            hidden_size=hidden_size,
             test_x_h_data=x_h_test_input,
             test_c_data=c_test_input,
-            h_out=list(h_output),
+            h_out=h_output,
             component_name="lstm_cell",
         )
         lstm_cell_code = lstm_cell_tb()
         for line in lstm_cell_code:
             writer.write(line + "\n")
 
-    for value in weight_name_index_dict.values():
-        format_vhdl(file_path=destination_path(f"{value}_rom.vhd"))
-
-    for value in bias_name_index_dict.values():
-        format_vhdl(file_path=destination_path(f"{value}_rom.vhd"))
+    for name in weight_names:
+        format_vhdl(file_path=destination_path(f"{name}_rom.vhd"))
 
     format_vhdl(file_path=file_path_sigmoid)
     format_vhdl(file_path=file_path_tanh)
     format_vhdl(file_path=file_path_testbench)
 
     # copy static files
     for file in ["dual_port_2_clock_ram.vhd", "lstm_cell.vhd", "lstm_common.vhd"]:
         copy_file("elasticai.creator.vhdl.templates", file, destination_path(file))
+
+
+if __name__ == "__main__":
+    main()
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_lstm_cell_testbench.py` & `elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/test_generate_lstm_cell_testbench_vhd.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,127 +1,121 @@
-import os
-from argparse import ArgumentParser
+from functools import partial
 
+from elasticai.creator.integrationTests.vhdl.vhdl_file_test_case import VHDLFileTestCase
 from elasticai.creator.vhdl.lstm_testbench_generator import LSTMCellTestBench
-from elasticai.creator.vhdl.vhdl_formatter.vhdl_formatter import format_vhdl
+from elasticai.creator.vhdl.number_representations import (
+    float_values_to_fixed_point,
+    int_values_to_fixed_point,
+)
 
 
-def main() -> None:
-    arg_parser = ArgumentParser()
-    arg_parser.add_argument(
-        "--path",
-        help="path to folder for generated vhd files",
-        required=True,
-    )
-    args = arg_parser.parse_args()
-    if not os.path.isdir(args.path):
-        os.mkdir(args.path)
-    component_name = "lstm_cell_tb"
-    file_path = os.path.join(args.path, f"{component_name}.vhd")
+class LSTMCellTestBenchTest(VHDLFileTestCase):
+    maxDiff = None
+
+    def test_compare_files(self) -> None:
+        fp_args = dict(total_bits=16, frac_bits=8)
+        ints_to_fp = partial(int_values_to_fixed_point, **fp_args)
+        floats_to_fp = partial(float_values_to_fixed_point, **fp_args)
 
-    with open(file_path, "w") as writer:
         lstm_cell = LSTMCellTestBench(
-            data_width=16,
-            frac_width=8,
             input_size=5,
             hidden_size=20,
-            test_x_h_data=[
-                0x018A,
-                0xFFB5,
-                0xFDD3,
-                0x0091,
-                0xFEEB,
-                0x0099,
-                0xFE72,
-                0xFFA9,
-                0x01DA,
-                0xFFC9,
-                0xFF42,
-                0x0090,
-                0x0042,
-                0xFFD4,
-                0xFF53,
-                0x00F0,
-                0x007D,
-                0x0134,
-                0x0015,
-                0xFECD,
-                0xFFFF,
-                0xFF7C,
-                0xFFB2,
-                0xFE6C,
-                0x01B4,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-            ],
-            test_c_data=[
-                0x0034,
-                0xFF8D,
-                0xFF6E,
-                0xFF72,
-                0xFEE0,
-                0xFFAF,
-                0xFEE9,
-                0xFFEB,
-                0xFFE9,
-                0x00AF,
-                0xFF2A,
-                0x0000,
-                0xFF40,
-                0x002F,
-                0x009F,
-                0x00A3,
-                0xFFC2,
-                0x024D,
-                0xFE1F,
-                0xFFF4,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-                0x0000,
-            ],
-            h_out=[
-                34,
-                -80,
-                -32,
-                -28,
-                -88,
-                11,
-                -60,
-                6,
-                -16,
-                18,
-                -32,
-                46,
-                -77,
-                15,
-                70,
-                27,
-                13,
-                112,
-                -156,
-                3,
-            ],
-            component_name=component_name,
+            component_name="lstm_cell",
+            test_x_h_data=ints_to_fp(
+                [
+                    0x018A,
+                    0xFFB5,
+                    0xFDD3,
+                    0x0091,
+                    0xFEEB,
+                    0x0099,
+                    0xFE72,
+                    0xFFA9,
+                    0x01DA,
+                    0xFFC9,
+                    0xFF42,
+                    0x0090,
+                    0x0042,
+                    0xFFD4,
+                    0xFF53,
+                    0x00F0,
+                    0x007D,
+                    0x0134,
+                    0x0015,
+                    0xFECD,
+                    0xFFFF,
+                    0xFF7C,
+                    0xFFB2,
+                    0xFE6C,
+                    0x01B4,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                ]
+            ),
+            test_c_data=ints_to_fp(
+                [
+                    0x0034,
+                    0xFF8D,
+                    0xFF6E,
+                    0xFF72,
+                    0xFEE0,
+                    0xFFAF,
+                    0xFEE9,
+                    0xFFEB,
+                    0xFFE9,
+                    0x00AF,
+                    0xFF2A,
+                    0x0000,
+                    0xFF40,
+                    0x002F,
+                    0x009F,
+                    0x00A3,
+                    0xFFC2,
+                    0x024D,
+                    0xFE1F,
+                    0xFFF4,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                    0x0000,
+                ]
+            ),
+            h_out=floats_to_fp(
+                [
+                    34,
+                    -80,
+                    -32,
+                    -28,
+                    -88,
+                    11,
+                    -60,
+                    6,
+                    -16,
+                    18,
+                    -32,
+                    46,
+                    -77,
+                    15,
+                    70,
+                    27,
+                    13,
+                    112,
+                    -126,
+                    3,
+                ]
+            ),
         )
         lstm_cell_code = lstm_cell()
-        for line in lstm_cell_code:
-            writer.write(line + "\n")
-
-    format_vhdl(file_path=file_path)
-
-
-if __name__ == "__main__":
-    main()
+        self.compareToFile("expected_lstm_cell_testbench.vhd", lstm_cell_code)
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_rom_vhd.py` & `elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_rom_vhd.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,15 +1,11 @@
 import os
 from argparse import ArgumentParser
 
-import numpy as np
-
-from elasticai.creator.vhdl.number_representations import (
-    FloatToSignedFixedPointConverter,
-)
+from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point
 from elasticai.creator.vhdl.rom import Rom
 from elasticai.creator.vhdl.vhdl_formatter.vhdl_formatter import format_vhdl
 
 
 def main():
     arg_parser = ArgumentParser()
     arg_parser.add_argument(
@@ -22,26 +18,22 @@
         os.mkdir(args.path)
     rom_name = "bi_rom"
     file_path = os.path.join(args.path, f"{rom_name}.vhd")
 
     data_width = 12
     frac_width = 4
     # biases for the input gate
-    Bi = np.array([1.1])
-
-    floats_to_signed_fixed_point_converter = FloatToSignedFixedPointConverter(
-        bits_used_for_fraction=frac_width, strict=False
-    )
-    array_value = [floats_to_signed_fixed_point_converter(x) for x in Bi]
+    bi = [1.1]
 
     with open(file_path, "w") as writer:
         rom = Rom(
             rom_name=rom_name,
-            data_width=data_width,
-            values=array_value,
+            values=float_values_to_fixed_point(
+                bi, total_bits=data_width, frac_bits=frac_width
+            ),
             resource_option="auto",
         )
         for line in rom():
             writer.write(line)
             if line[-1] != "\n":
                 writer.write("\n")
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_sigmoid_testbench.py` & `elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_tanh_testbench.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,10 +1,12 @@
 import os
 from argparse import ArgumentParser
+from functools import partial
 
+from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point
 from elasticai.creator.vhdl.precomputed_scalar_function import (
     PrecomputedScalarTestBench,
 )
 from elasticai.creator.vhdl.vhdl_formatter.vhdl_formatter import format_vhdl
 
 
 def main() -> None:
@@ -13,27 +15,27 @@
         "--path",
         help="path to folder for generated vhd files",
         required=True,
     )
     args = arg_parser.parse_args()
     if not os.path.isdir(args.path):
         os.mkdir(args.path)
-    component_name = "sigmoid_tb"
+    component_name = "tanh_tb"
     file_path = os.path.join(args.path, f"{component_name}.vhd")
 
+    to_fp = partial(float_values_to_fixed_point, total_bits=16, frac_bits=2)
+
     with open(file_path, "w") as writer:
-        sigmoid = PrecomputedScalarTestBench(
+        tanh = PrecomputedScalarTestBench(
             component_name=component_name,
-            data_width=16,
-            frac_width=8,
-            x_list_for_testing=[-1281, -1000, -500],
-            y_list_for_testing=[0, 4, 28],
+            x_list_for_testing=to_fp([-1281, -1000, -500, 0, 500, 800, 1024]),
+            y_list_for_testing=to_fp([-256, -255, -246, 0, 245, 254, 255]),
         )
-        sigmoid_code = sigmoid()
-        for line in sigmoid_code:
+        tanh_code = tanh()
+        for line in tanh_code:
             writer.write(line + "\n")
 
     format_vhdl(file_path=file_path)
 
 
 if __name__ == "__main__":
     main()
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_sigmoid_vhd.py` & `elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_sigmoid_testbench.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,35 +1,38 @@
 import os
 from argparse import ArgumentParser
+from functools import partial
 
-import numpy as np
-
-from elasticai.creator.vhdl.precomputed_scalar_function import Sigmoid
+from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point
+from elasticai.creator.vhdl.precomputed_scalar_function import (
+    PrecomputedScalarTestBench,
+)
 from elasticai.creator.vhdl.vhdl_formatter.vhdl_formatter import format_vhdl
 
 
-def main():
+def main() -> None:
     arg_parser = ArgumentParser()
     arg_parser.add_argument(
         "--path",
         help="path to folder for generated vhd files",
         required=True,
     )
     args = arg_parser.parse_args()
     if not os.path.isdir(args.path):
         os.mkdir(args.path)
-    component_name = "sigmoid"
+    component_name = "sigmoid_tb"
     file_path = os.path.join(args.path, f"{component_name}.vhd")
 
+    to_fp = partial(float_values_to_fixed_point, total_bits=16, frac_bits=2)
+
     with open(file_path, "w") as writer:
-        sigmoid = Sigmoid(
+        sigmoid = PrecomputedScalarTestBench(
             component_name=component_name,
-            data_width=16,
-            frac_width=8,
-            x=np.linspace(-5, 5, 66),
+            x_list_for_testing=to_fp([-1281, -1000, -500]),
+            y_list_for_testing=to_fp([0, 4, 28]),
         )
         sigmoid_code = sigmoid()
         for line in sigmoid_code:
             writer.write(line + "\n")
 
     format_vhdl(file_path=file_path)
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/examples/generate_vhdl_files/generate_tanh_vhd.py` & `elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_tanh_vhd.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 import os
 from argparse import ArgumentParser
 
 import numpy as np
 
+from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point
 from elasticai.creator.vhdl.precomputed_scalar_function import Tanh
 from elasticai.creator.vhdl.vhdl_formatter.vhdl_formatter import format_vhdl
 
 
 def main():
     arg_parser = ArgumentParser()
     arg_parser.add_argument(
@@ -16,22 +17,26 @@
     )
     args = arg_parser.parse_args()
     if not os.path.isdir(args.path):
         os.mkdir(args.path)
     component_name = "tanh"
     file_path = os.path.join(args.path, f"{component_name}.vhd")
 
+    # noinspection PyTypeChecker
+    data = float_values_to_fixed_point(
+        np.linspace(-5, 5, 259).tolist(), total_bits=16, frac_bits=8
+    )
+
     tanh = Tanh(
         component_name=component_name,
-        data_width=16,
-        frac_width=8,
-        x=np.linspace(-5, 5, 259),
+        x=data,
     )
+    tanh_code = tanh()
+
     with open(file_path, "w") as writer:
-        tanh_code = tanh()
         for line in tanh_code:
             writer.write(line + "\n")
 
     format_vhdl(file_path=file_path)
 
 
 if __name__ == "__main__":
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/examples/precompute_convolution.py` & `elasticai.creator-0.9.0/elasticai/creator/examples/precompute_convolution.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/examples/precompute_sigmoid_layer.py` & `elasticai.creator-0.9.0/elasticai/creator/examples/precompute_sigmoid_layer.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/examples/qlstm.py` & `elasticai.creator-0.9.0/elasticai/creator/examples/qlstm.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/examples/simple_qlstm_part_of_speech_tagging.py` & `elasticai.creator-0.9.0/elasticai/creator/examples/simple_qlstm_part_of_speech_tagging.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/integrationTests/test_jit.py` & `elasticai.creator-0.9.0/elasticai/creator/integrationTests/test_jit.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/integrationTests/test_onnx_export.py` & `elasticai.creator-0.9.0/elasticai/creator/integrationTests/test_onnx_export.py`

 * *Files 3% similar despite different names*

```diff
@@ -4,14 +4,19 @@
 import onnx
 import torch
 
 from elasticai.creator.onnx import ModuleWrapper
 from elasticai.creator.tags_utils import tag
 from elasticai.creator.tests.tensor_test_case import TensorTestCase
 
+ONNX_HEADER = """ir_version: 4
+producer_name: "pytorch"
+producer_version: "1.11.0"
+"""
+
 
 class OnnxExportTest(TensorTestCase):
     """
     For documentation of the model returned by the onnx load function refer to
     https://github.com/onnx/onnx/blob/master/docs/IR.md
 
     TODO:
@@ -36,23 +41,23 @@
             buffer.seek(0)
             model = onnx.load(buffer)
 
         self.assertEqual(expected, "{}".format(model))
 
     @classmethod
     def get_simple_string_representation(cls, operation_name, domain) -> str:
-        template = """ir_version: 7
-producer_name: "pytorch"
-producer_version: "1.10"
-graph {
+        template = (
+            ONNX_HEADER
+            + """graph {
   node {
     output: "1"
     name: "Wrapper_0"
     op_type: "Wrapper"
 """
+        )
         attributes = cls.build_attributes(
             """name: "operation_name"
       s: "{operation_name}"
       type: STRING""".format(
                 operation_name=operation_name
             )
         )
@@ -152,18 +157,17 @@
             )
             buffer.seek(0)
             model = onnx.load(buffer)
         self.assertEqual(expected_string, "{}".format(model))
 
     @staticmethod
     def get_string_representation_with_tag(operation_name, input_shape) -> str:
-        template = """ir_version: 7
-producer_name: "pytorch"
-producer_version: "1.10"
-graph {{
+        template = (
+            ONNX_HEADER
+            + """graph {{
   node {{
     output: "1"
     name: "Wrapper_0"
     op_type: "Wrapper"
     attribute {{
       name: "input_shape"
 {input_shape}
@@ -194,14 +198,15 @@
   version: 9
 }}
 opset_import {{
   domain: "elasticai.creator"
   version: 1
 }}
 """
+        )
         template = template.format(
             operation_name=operation_name, input_shape=input_shape
         )
         return template
 
     @staticmethod
     def build_attributes(*args: str) -> str:
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/expected_lstm_cell_testbench.vhd` & `elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/expected_lstm_cell_testbench.vhd`

 * *Files 1% similar despite different names*

```diff
@@ -147,15 +147,15 @@
             end loop;
 
             enable <= '1';
             wait until done = '1';
             wait for 1*clk_period;
             enable <= '0';
 
-            -- reference h_out: [34, -80, -32, -28, -88, 11, -60, 6, -16, 18, -32, 46, -77, 15, 70, 27, 13, 112, -156, 3];
+            -- reference h_out: [34, -80, -32, -28, -88, 11, -60, 6, -16, 18, -32, 46, -77, 15, 70, 27, 13, 112, -126, 3];
             for ii in 0 to 19 loop h_out_addr <= std_logic_vector(to_unsigned(ii, HIDDEN_ADDR_WIDTH));
                 h_out_en <= '1';
                 wait for 2*clk_period;
                 report "The value of h_out(" & integer'image(ii)& ") is " & integer'image(to_integer(signed(h_out_data)));
             end loop;
 
             wait for 10*clk_period;
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/test_generate_lstm_cell_testbench_vhd.py` & `elasticai.creator-0.9.0/elasticai/creator/examples/generate_vhdl_files/generate_lstm_cell_testbench.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,22 +1,41 @@
-from elasticai.creator.integrationTests.vhdl.vhdl_file_test_case import VHDLFileTestCase
+import os
+from argparse import ArgumentParser
+from functools import partial
+
 from elasticai.creator.vhdl.lstm_testbench_generator import LSTMCellTestBench
+from elasticai.creator.vhdl.number_representations import (
+    float_values_to_fixed_point,
+    int_values_to_fixed_point,
+)
+from elasticai.creator.vhdl.vhdl_formatter.vhdl_formatter import format_vhdl
+
 
+def main() -> None:
+    arg_parser = ArgumentParser()
+    arg_parser.add_argument(
+        "--path",
+        help="path to folder for generated vhd files",
+        required=True,
+    )
+    args = arg_parser.parse_args()
+    if not os.path.isdir(args.path):
+        os.mkdir(args.path)
+    component_name = "lstm_cell_tb"
+    file_path = os.path.join(args.path, f"{component_name}.vhd")
 
-class LSTMCellTestBenchTest(VHDLFileTestCase):
-    maxDiff = None
+    fp_args = dict(total_bits=16, frac_bits=8)
+    ints_to_fp = partial(int_values_to_fixed_point, **fp_args)
+    floats_to_fp = partial(float_values_to_fixed_point, **fp_args)
 
-    def test_compare_files(self) -> None:
-        lstm_cell = LSTMCellTestBench(
-            data_width=16,
-            frac_width=8,
-            input_size=5,
-            hidden_size=20,
-            component_name="lstm_cell",
-            test_x_h_data=[
+    lstm_cell = LSTMCellTestBench(
+        input_size=5,
+        hidden_size=20,
+        test_x_h_data=ints_to_fp(
+            [
                 0x018A,
                 0xFFB5,
                 0xFDD3,
                 0x0091,
                 0xFEEB,
                 0x0099,
                 0xFE72,
@@ -41,16 +60,18 @@
                 0x0000,
                 0x0000,
                 0x0000,
                 0x0000,
                 0x0000,
                 0x0000,
                 0x0000,
-            ],
-            test_c_data=[
+            ]
+        ),
+        test_c_data=ints_to_fp(
+            [
                 0x0034,
                 0xFF8D,
                 0xFF6E,
                 0xFF72,
                 0xFEE0,
                 0xFFAF,
                 0xFEE9,
@@ -75,16 +96,18 @@
                 0x0000,
                 0x0000,
                 0x0000,
                 0x0000,
                 0x0000,
                 0x0000,
                 0x0000,
-            ],
-            h_out=[
+            ]
+        ),
+        h_out=floats_to_fp(
+            [
                 34,
                 -80,
                 -32,
                 -28,
                 -88,
                 11,
                 -60,
@@ -95,13 +118,24 @@
                 46,
                 -77,
                 15,
                 70,
                 27,
                 13,
                 112,
-                -156,
+                -126,
                 3,
-            ],
-        )
-        lstm_cell_code = lstm_cell()
-        self.compareToFile("expected_lstm_cell_testbench.vhd", lstm_cell_code)
+            ]
+        ),
+        component_name=component_name,
+    )
+    lstm_cell_code = lstm_cell()
+
+    with open(file_path, "w") as writer:
+        for line in lstm_cell_code:
+            writer.write(line + "\n")
+
+    format_vhdl(file_path=file_path)
+
+
+if __name__ == "__main__":
+    main()
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/test_generate_rom_vhd.py` & `elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/test_generate_rom_vhd.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,32 +1,20 @@
-import numpy as np
-
 from elasticai.creator.tests.vhdl.vhdl_file_testcase import GeneratedVHDLCodeTest
-from elasticai.creator.vhdl.number_representations import (
-    FloatToSignedFixedPointConverter,
-)
+from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point
 from elasticai.creator.vhdl.rom import Rom
 
 
 class GenerateROMVhdTest(GeneratedVHDLCodeTest):
     def test_compare_files(self) -> None:
-        rom_name = "rom_bi"
-        data_width = 12
-        frac_width = 4
         # biases for the input gate
-        Bi = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6])
-        floats_to_signed_fixed_point_converter = FloatToSignedFixedPointConverter(
-            bits_used_for_fraction=frac_width, strict=False
-        )
-        values = [floats_to_signed_fixed_point_converter(x) for x in Bi]
+        bi = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
 
         generate_rom = Rom(
-            rom_name=rom_name,
-            data_width=data_width,
-            values=values,
+            rom_name="rom_bi",
+            values=float_values_to_fixed_point(bi, total_bits=12, frac_bits=4),
             resource_option="auto",
         )
         generated_code = list(generate_rom())
 
         expected_code = [
             "library ieee;",
             "use ieee.std_logic_1164.all;",
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/test_generate_sigmoid_testbench_vhd.py` & `elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/test_generate_sigmoid_testbench_vhd.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,8 +1,11 @@
+from functools import partial
+
 from elasticai.creator.tests.vhdl.vhdl_file_testcase import GeneratedVHDLCodeTest
+from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point
 from elasticai.creator.vhdl.precomputed_scalar_function import (
     PrecomputedScalarTestBench,
 )
 
 
 class SigmoidTestBenchTest(GeneratedVHDLCodeTest):
     def test_compare_files(self) -> None:
@@ -11,15 +14,15 @@
         use ieee.std_logic_1164.all;
         use ieee.numeric_std.all;
         use ieee.math_real.all;
 
         entity sigmoid_tb is
             generic (
                 DATA_WIDTH : integer := 16;
-                FRAC_WIDTH : integer := 8
+                FRAC_WIDTH : integer := 0
             );
             port (
                 clk : out std_logic
             );
         end entity sigmoid_tb;
 
         architecture rtl of sigmoid_tb is
@@ -27,15 +30,15 @@
             signal clk_period : time := 1 ns;
             signal test_input : signed(16-1 downto 0):=(others=>'0');
             signal test_output : signed(16-1 downto 0);
 
             component sigmoid is
                 generic (
                     DATA_WIDTH : integer := 16;
-                    FRAC_WIDTH : integer := 8
+                    FRAC_WIDTH : integer := 0
                 );
                 port (
                     x : in signed(DATA_WIDTH-1 downto 0);
                     y : out signed(DATA_WIDTH-1 downto 0)
                 );
             end component sigmoid;
 
@@ -80,19 +83,18 @@
 
                 wait;
 
             end process test_process;
 
         end architecture rtl;
         """
+        to_fp = partial(float_values_to_fixed_point, total_bits=16, frac_bits=0)
         sigmoid = PrecomputedScalarTestBench(
-            data_width=16,
-            frac_width=8,
             component_name="sigmoid",
-            x_list_for_testing=[-1281, -1000, -500],
-            y_list_for_testing=[0, 4, 28],
+            x_list_for_testing=to_fp([-1281, -1000, -500]),
+            y_list_for_testing=to_fp([0, 4, 28]),
         )
         sigmoid_code = sigmoid()
         sigmoid_code_str = ""
         for line in sigmoid_code:
             sigmoid_code_str += line + "\n"
         self.check_generated_code(expected_code, sigmoid_code_str)
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/test_generate_sigmoid_vhd.py` & `elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/test_generate_sigmoid_vhd.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 import numpy as np
 
 from elasticai.creator.tests.vhdl.vhdl_file_testcase import GeneratedVHDLCodeTest
+from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point
 from elasticai.creator.vhdl.precomputed_scalar_function import Sigmoid
 
 
 class SigmoidTest(GeneratedVHDLCodeTest):
     def test_compare_files(self) -> None:
         expected_code = """-- A LUT version of sigmoid
         library ieee;
@@ -32,15 +33,15 @@
                 int_x := to_integer(x);
 
                 if int_x<-1280 then
                     y <= "0000000000000000"; -- 0
                 elsif int_x<-1240 then
                     y <= "0000000000000001"; -- 1
                 elsif int_x<-1201 then
-                    y <= "0000000000000001"; -- 1
+                    y <= "0000000000000010"; -- 2
                 elsif int_x<-1161 then
                     y <= "0000000000000010"; -- 2
                 elsif int_x<-1122 then
                     y <= "0000000000000010"; -- 2
                 elsif int_x<-1083 then
                     y <= "0000000000000011"; -- 3
                 elsif int_x<-1043 then
@@ -158,26 +159,25 @@
                 elsif int_x<1161 then
                     y <= "0000000011111100"; -- 252
                 elsif int_x<1201 then
                     y <= "0000000011111101"; -- 253
                 elsif int_x<1240 then
                     y <= "0000000011111101"; -- 253
                 elsif int_x<1280 then
-                    y <= "0000000011111110"; -- 254
+                    y <= "0000000011111101"; -- 253
                 else
                     y <= "0000000100000000"; -- 256
                 end if;
 
             end process sigmoid_process;
         end architecture rtl;
         """
-        sigmoid = Sigmoid(
-            data_width=16,
-            frac_width=8,
-            x=np.linspace(-5, 5, 66),
-            component_name="sigmoid",
+        # noinspection PyTypeChecker
+        data = float_values_to_fixed_point(
+            np.linspace(-5, 5, 66).tolist(), total_bits=16, frac_bits=8
         )
+        sigmoid = Sigmoid(x=data, component_name="sigmoid")
         sigmoid_code = sigmoid()
         sigmoid_code_str = ""
         for line in sigmoid_code:
             sigmoid_code_str += line + "\n"
         self.check_generated_code(expected_code, sigmoid_code_str)
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/test_generate_tanh_testbench_vhd.py` & `elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/test_generate_tanh_testbench_vhd.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,8 +1,11 @@
+from functools import partial
+
 from elasticai.creator.tests.vhdl.vhdl_file_testcase import GeneratedVHDLCodeTest
+from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point
 from elasticai.creator.vhdl.precomputed_scalar_function import (
     PrecomputedScalarTestBench,
 )
 
 
 class TanhTestBenchTest(GeneratedVHDLCodeTest):
     def test_compare_files(self) -> None:
@@ -11,15 +14,15 @@
         use ieee.std_logic_1164.all;
         use ieee.numeric_std.all;
         use ieee.math_real.all;
 
         entity tanh_tb is
             generic (
                 DATA_WIDTH : integer := 16;
-                FRAC_WIDTH : integer := 8
+                FRAC_WIDTH : integer := 0
             );
             port (
                 clk : out std_logic
             );
         end entity tanh_tb;
 
         architecture rtl of tanh_tb is
@@ -27,15 +30,15 @@
             signal clk_period : time := 1 ns;
             signal test_input : signed(16-1 downto 0):=(others=>'0');
             signal test_output : signed(16-1 downto 0);
 
             component tanh is
                 generic (
                     DATA_WIDTH : integer := 16;
-                    FRAC_WIDTH : integer := 8
+                    FRAC_WIDTH : integer := 0
                 );
                 port (
                     x : in signed(DATA_WIDTH-1 downto 0);
                     y : out signed(DATA_WIDTH-1 downto 0)
                 );
             end component tanh;
 
@@ -58,15 +61,15 @@
             test_process: process
             begin
                 report "======Simulation Start======" severity Note;
 
                 test_input <= to_signed(-1281,16);
                 wait for 1*clk_period;
                 report "The value of 'test_output' is " & integer'image(to_integer(unsigned(test_output)));
-                assert test_output="1111111100000000" report "The test case -1281 fail" severity failure;
+                assert test_output=-256 report "The test case -1281 fail" severity failure;
 
                 test_input <= to_signed(-1000,16);
                 wait for 1*clk_period;
                 report "The value of 'test_output' is " & integer'image(to_integer(unsigned(test_output)));
                 assert test_output=-255 report "The test case -1000 fail" severity failure;
 
                 test_input <= to_signed(-500,16);
@@ -100,19 +103,18 @@
 
                 wait;
 
             end process test_process;
 
         end architecture rtl;
         """
+        to_fp = partial(float_values_to_fixed_point, total_bits=16, frac_bits=0)
         tanh = PrecomputedScalarTestBench(
-            data_width=16,
-            frac_width=8,
             component_name="tanh",
-            x_list_for_testing=[-1281, -1000, -500, 0, 500, 800, 1024],
-            y_list_for_testing=["1111111100000000", -255, -246, 0, 245, 254, 255],
+            x_list_for_testing=to_fp([-1281, -1000, -500, 0, 500, 800, 1024]),
+            y_list_for_testing=to_fp([-256, -255, -246, 0, 245, 254, 255]),
         )
         tanh_code = tanh()
         tanh_code_str = ""
         for line in tanh_code:
             tanh_code_str += line + "\n"
         self.check_generated_code(expected_code, tanh_code_str)
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/test_generate_tanh_vhd.py` & `elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/test_generate_tanh_vhd.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 import numpy as np
 
 from elasticai.creator.tests.vhdl.vhdl_file_testcase import GeneratedVHDLCodeTest
+from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point
 from elasticai.creator.vhdl.precomputed_scalar_function import Tanh
 
 
 class GenerateTanhVhdTest(GeneratedVHDLCodeTest):
     def test_compare_files(self) -> None:
         expected_code = """library ieee;
         use ieee.std_logic_1164.all;
@@ -229,131 +230,131 @@
                 elsif int_x<-307 then
                     y <= "1111111100101000"; -- -216
                 elsif int_x<-297 then
                     y <= "1111111100101011"; -- -213
                 elsif int_x<-287 then
                     y <= "1111111100101110"; -- -210
                 elsif int_x<-277 then
-                    y <= "1111111100110001"; -- -207
+                    y <= "1111111100110010"; -- -206
                 elsif int_x<-267 then
                     y <= "1111111100110101"; -- -203
                 elsif int_x<-257 then
                     y <= "1111111100111001"; -- -199
                 elsif int_x<-248 then
                     y <= "1111111100111101"; -- -195
                 elsif int_x<-238 then
                     y <= "1111111101000001"; -- -191
                 elsif int_x<-228 then
-                    y <= "1111111101000101"; -- -187
+                    y <= "1111111101000110"; -- -186
                 elsif int_x<-218 then
                     y <= "1111111101001010"; -- -182
                 elsif int_x<-208 then
                     y <= "1111111101001111"; -- -177
                 elsif int_x<-198 then
                     y <= "1111111101010101"; -- -171
                 elsif int_x<-188 then
                     y <= "1111111101011010"; -- -166
                 elsif int_x<-178 then
                     y <= "1111111101100000"; -- -160
                 elsif int_x<-168 then
-                    y <= "1111111101100110"; -- -154
+                    y <= "1111111101100111"; -- -153
                 elsif int_x<-158 then
                     y <= "1111111101101101"; -- -147
                 elsif int_x<-148 then
-                    y <= "1111111101110011"; -- -141
+                    y <= "1111111101110100"; -- -140
                 elsif int_x<-138 then
-                    y <= "1111111101111010"; -- -134
+                    y <= "1111111101111011"; -- -133
                 elsif int_x<-128 then
                     y <= "1111111110000010"; -- -126
                 elsif int_x<-119 then
-                    y <= "1111111110001001"; -- -119
+                    y <= "1111111110001010"; -- -118
                 elsif int_x<-109 then
                     y <= "1111111110010001"; -- -111
                 elsif int_x<-99 then
                     y <= "1111111110011010"; -- -102
                 elsif int_x<-89 then
                     y <= "1111111110100010"; -- -94
                 elsif int_x<-79 then
                     y <= "1111111110101011"; -- -85
                 elsif int_x<-69 then
                     y <= "1111111110110100"; -- -76
                 elsif int_x<-59 then
                     y <= "1111111110111101"; -- -67
                 elsif int_x<-49 then
-                    y <= "1111111111000110"; -- -58
+                    y <= "1111111111000111"; -- -57
                 elsif int_x<-39 then
-                    y <= "1111111111001111"; -- -49
+                    y <= "1111111111010000"; -- -48
                 elsif int_x<-29 then
-                    y <= "1111111111011001"; -- -39
+                    y <= "1111111111011010"; -- -38
                 elsif int_x<-19 then
-                    y <= "1111111111100011"; -- -29
+                    y <= "1111111111100100"; -- -28
                 elsif int_x<-9 then
-                    y <= "1111111111101101"; -- -19
+                    y <= "1111111111101110"; -- -18
                 elsif int_x<0 then
-                    y <= "1111111111110111"; -- -9
+                    y <= "1111111111111000"; -- -8
                 elsif int_x<9 then
                     y <= "0000000000000000"; -- 0
                 elsif int_x<19 then
-                    y <= "0000000000001001"; -- 9
+                    y <= "0000000000001000"; -- 8
                 elsif int_x<29 then
-                    y <= "0000000000010011"; -- 19
+                    y <= "0000000000010010"; -- 18
                 elsif int_x<39 then
-                    y <= "0000000000011101"; -- 29
+                    y <= "0000000000011100"; -- 28
                 elsif int_x<49 then
-                    y <= "0000000000100111"; -- 39
+                    y <= "0000000000100110"; -- 38
                 elsif int_x<59 then
-                    y <= "0000000000110001"; -- 49
+                    y <= "0000000000110000"; -- 48
                 elsif int_x<69 then
-                    y <= "0000000000111010"; -- 58
+                    y <= "0000000000111001"; -- 57
                 elsif int_x<79 then
                     y <= "0000000001000011"; -- 67
                 elsif int_x<89 then
                     y <= "0000000001001100"; -- 76
                 elsif int_x<99 then
                     y <= "0000000001010101"; -- 85
                 elsif int_x<109 then
                     y <= "0000000001011110"; -- 94
                 elsif int_x<119 then
                     y <= "0000000001100110"; -- 102
                 elsif int_x<128 then
                     y <= "0000000001101111"; -- 111
                 elsif int_x<138 then
-                    y <= "0000000001110111"; -- 119
+                    y <= "0000000001110110"; -- 118
                 elsif int_x<148 then
                     y <= "0000000001111110"; -- 126
                 elsif int_x<158 then
-                    y <= "0000000010000110"; -- 134
+                    y <= "0000000010000101"; -- 133
                 elsif int_x<168 then
-                    y <= "0000000010001101"; -- 141
+                    y <= "0000000010001100"; -- 140
                 elsif int_x<178 then
                     y <= "0000000010010011"; -- 147
                 elsif int_x<188 then
-                    y <= "0000000010011010"; -- 154
+                    y <= "0000000010011001"; -- 153
                 elsif int_x<198 then
                     y <= "0000000010100000"; -- 160
                 elsif int_x<208 then
                     y <= "0000000010100110"; -- 166
                 elsif int_x<218 then
                     y <= "0000000010101011"; -- 171
                 elsif int_x<228 then
                     y <= "0000000010110001"; -- 177
                 elsif int_x<238 then
                     y <= "0000000010110110"; -- 182
                 elsif int_x<248 then
-                    y <= "0000000010111011"; -- 187
+                    y <= "0000000010111010"; -- 186
                 elsif int_x<257 then
                     y <= "0000000010111111"; -- 191
                 elsif int_x<267 then
                     y <= "0000000011000011"; -- 195
                 elsif int_x<277 then
                     y <= "0000000011000111"; -- 199
                 elsif int_x<287 then
                     y <= "0000000011001011"; -- 203
                 elsif int_x<297 then
-                    y <= "0000000011001111"; -- 207
+                    y <= "0000000011001110"; -- 206
                 elsif int_x<307 then
                     y <= "0000000011010010"; -- 210
                 elsif int_x<317 then
                     y <= "0000000011010101"; -- 213
                 elsif int_x<327 then
                     y <= "0000000011011000"; -- 216
                 elsif int_x<337 then
@@ -552,15 +553,18 @@
                     y <= "0000000100000000"; -- 256
                 end if;
 
             end process tanh_process;
 
         end architecture rtl;
         """
-
-        tanh = Tanh(data_width=16, frac_width=8, x=np.linspace(-5, 5, 259))
+        # noinspection PyTypeChecker
+        data = float_values_to_fixed_point(
+            np.linspace(-5, 5, 259).tolist(), total_bits=16, frac_bits=8
+        )
+        tanh = Tanh(x=data)
         tanh_code = tanh()
         tanh_code_str = ""
         for line in tanh_code:
             tanh_code_str += line + "\n"
         self.check_generated_code(expected_code, tanh_code_str)
         # clean each file from empty lines and lines which are just comment
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/integrationTests/vhdl/vhdl_file_test_case.py` & `elasticai.creator-0.9.0/elasticai/creator/integrationTests/vhdl/vhdl_file_test_case.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,17 +1,17 @@
-import importlib.resources
 import unittest
 from itertools import filterfalse
 
+from elasticai.creator import resource_utils
 from elasticai.creator.vhdl.language import Code
 
 
 class VHDLFileTestCase(unittest.TestCase):
     def compareToFile(self, vhdl_file: str, generated_code: Code):
-        vhdl_code = importlib.resources.read_text(
+        vhdl_code = resource_utils.read_text(
             "elasticai.creator.integrationTests.vhdl", vhdl_file
         )
 
         def line_is_empty(line):
             return len(line) == 0
 
         vhdl_code = filterfalse(line_is_empty, map(str.strip, vhdl_code.splitlines()))
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/mlframework/typing.py` & `elasticai.creator-0.9.0/elasticai/creator/mlframework/typing.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/onnx.py` & `elasticai.creator-0.9.0/elasticai/creator/onnx.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/precomputation/breakdown.py` & `elasticai.creator-0.9.0/elasticai/creator/precomputation/breakdown.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/precomputation/input_domains.py` & `elasticai.creator-0.9.0/elasticai/creator/precomputation/input_domains.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/precomputation/io_table.py` & `elasticai.creator-0.9.0/elasticai/creator/precomputation/io_table.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/precomputation/metaprogramming.py` & `elasticai.creator-0.9.0/elasticai/creator/precomputation/metaprogramming.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/precomputation/precomputation.py` & `elasticai.creator-0.9.0/elasticai/creator/precomputation/precomputation.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 import json
 from typing import Callable, Sequence, Union
 
 import numpy as np
 import torch
 from torch import Tensor
 
-from elasticai.creator.tags_utils import Module, TaggedModule, get_tags, has_tag, tag
+from elasticai.creator.mlframework import Module
+from elasticai.creator.tags_utils import TaggedModule, get_tags, has_tag, tag
 
 _precomputable_tag = "precomputable"
 
 TensorLike = Union[Callable[[], "TensorLike"], torch.Tensor, np.ndarray]
 
 
 class Precomputation:
@@ -101,16 +102,16 @@
         Precomputation.from_precomputable_tagged(submodule)
         for submodule in filtered_submodules
     )
 
 
 def precomputable(
     input_shape: Sequence[int],
-    input_generator: Callable[[], Tensor],
-) -> Callable[[type[Module]], type[TaggedModule]]:
+    input_generator: Callable[[Sequence[float | int]], np.ndarray],
+) -> Callable[[Module], TaggedModule]:
     """Add all necessary information to allow later tools to precompute the specified module
 
     The arguments provided will be used to determine the input data that needs
     to be fed to the module to produce the precomputed input-output table.
 
             Example:
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/qat/QRigL.py` & `elasticai.creator-0.9.0/elasticai/creator/qat/QRigL.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/qat/blocks.py` & `elasticai.creator-0.9.0/elasticai/creator/qat/blocks.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/qat/functional.py` & `elasticai.creator-0.9.0/elasticai/creator/qat/functional.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/qat/layers.py` & `elasticai.creator-0.9.0/elasticai/creator/qat/layers.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/qat/masks.py` & `elasticai.creator-0.9.0/elasticai/creator/qat/masks.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/resource_utils.py` & `elasticai.creator-0.9.0/elasticai/creator/resource_utils.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 from importlib import resources
 from importlib.abc import Traversable
 from pathlib import PurePath
-from typing import Union
 
-PathType = Union[str, PurePath]
+PathType = str | PurePath
 
 
 def _get_file(package: resources.Package, file_name: str) -> Traversable:
     for resource in resources.files(package).iterdir():
         if resource.name == file_name:
             return resource
     raise FileNotFoundError(f"The file '{file_name}' does not exist.")
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tags_utils.py` & `elasticai.creator-0.9.0/elasticai/creator/tags_utils.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/precomputation/test_derive_data_sets.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/precomputation/test_derive_data_sets.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/precomputation/test_io_table.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/precomputation/test_io_table.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/precomputation/test_metaprogramming.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/precomputation/test_metaprogramming.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/precomputation/test_precomputation.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/precomputation/test_precomputation.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 import json
-from collections import Iterable
+from typing import Iterable
 
 import torch
 
 from elasticai.creator.precomputation.precomputation import (
     JSONEncoder,
     Precomputation,
     precomputable,
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/precomputation/test_tags.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/precomputation/test_tags.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/qat/test_QRigL.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/qat/test_QRigL.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/qat/test_block.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/qat/test_block.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/qat/test_breakdown.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/qat/test_breakdown.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/qat/test_functional.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/qat/test_functional.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/qat/test_layer.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/qat/test_layer.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/qat/test_masks.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/qat/test_masks.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/test_language.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/test_language.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,7 +1,8 @@
+from functools import partial
 from unittest import TestCase
 
 from elasticai.creator.vhdl.language import (
     Architecture,
     ContextClause,
     DataType,
     Entity,
@@ -10,14 +11,15 @@
     LibraryClause,
     Mode,
     PortMap,
     Procedure,
     Process,
     UseClause,
 )
+from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point
 from elasticai.creator.vhdl.precomputed_scalar_function import (
     precomputed_scalar_function_process,
 )
 
 
 class EntityTest(TestCase):
     def test_no_name_entity(self):
@@ -100,21 +102,24 @@
             "use work.all;",
         ]
         actual = list(lib())
         self.assertEqual(expected, actual)
 
 
 class ProcessTest(TestCase):
+    def setUp(self) -> None:
+        self.fp_list = partial(float_values_to_fixed_point, total_bits=16, frac_bits=8)
+
     # Note: the precomputed scalar function process is already tested, no need for trying more in- and outputs
     def test_process_empty(self):
         process = Process(
             identifier="some_name",
             input_name="some_input",
             lookup_table_generator_function=precomputed_scalar_function_process(
-                x_list=[], y_list=[0]
+                x=[], y=self.fp_list([0])
             ),
         )
         expected = [
             "some_name_process: process(some_input)",
             "begin",
             'y <= "0000000000000000";',
             "end process some_name_process;",
@@ -123,15 +128,15 @@
         self.assertEqual(expected, actual)
 
     def test_process_with_variables(self):
         process = Process(
             identifier="some_name",
             input_name="some_input",
             lookup_table_generator_function=precomputed_scalar_function_process(
-                x_list=[], y_list=[0]
+                x=[], y=self.fp_list([0])
             ),
         )
         process.process_declaration_list = ["variable some_variable_name: integer := 0"]
         process.process_statements_list = [
             "some_variable_name := to_integer(some_variable_name)"
         ]
         expected = [
@@ -215,15 +220,18 @@
             "end architecture rtl;",
         ]
         actual = list(a())
         self.assertSequenceEqual(expected, actual)
 
     def test_Architecture_with_architecture_part_as_process(self):
         def function():
-            yield "some code"
+            def generator():
+                yield "some code"
+
+            return generator
 
         dummy_process = Process(
             identifier="some name",
             lookup_table_generator_function=function(),
             input_name="x",
         )
         a = Architecture(design_unit="z")
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/test_language_testbench.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/test_language_testbench.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,67 +1,70 @@
+from functools import partial
 from unittest import TestCase
 
+from elasticai.creator.vhdl.language import hex_representation
 from elasticai.creator.vhdl.lstm_testbench_generator import TestCasesLSTMCommonGate
+from elasticai.creator.vhdl.number_representations import (
+    FixedPoint,
+    float_values_to_fixed_point,
+)
 from elasticai.creator.vhdl.precomputed_scalar_function import (
     TestCasesPrecomputedScalarFunction,
 )
 
 
 class TestCasesLSTMCommonGateTest(TestCase):
     def test_TestCasesLSTMCommonGate(self):
-        x_mem_list_for_testing = [
-            "some_string_00",
-            "some_string_01",
-            "some_string_02",
-        ]
-        w_mem_list_for_testing = [
-            "some_string_10",
-            "some_string_11",
-            "some_string_12",
-        ]
-        b_list_for_testing = ["some_string_20", "some_string_21", "some_string_22"]
-        y_list_for_testing = [1, 2, 3]
+        to_fp = partial(FixedPoint, total_bits=8, frac_bits=0)
+
+        def to_hex(value: FixedPoint) -> str:
+            return hex_representation(value.to_hex())
+
+        x_mem_list_for_testing = [to_fp(x) for x in range(0, 3)]
+        w_mem_list_for_testing = [to_fp(x) for x in range(10, 13)]
+        b_list_for_testing = [to_fp(x) for x in range(20, 23)]
+        y_list_for_testing = [to_fp(x) for x in range(30, 33)]
         y_variable_name = "out"
         test_cases_lstm_common_gate = TestCasesLSTMCommonGate(
             x_mem_list_for_testing=x_mem_list_for_testing,
             w_mem_list_for_testing=w_mem_list_for_testing,
             b_list_for_testing=b_list_for_testing,
             y_list_for_testing=y_list_for_testing,
             y_variable_name=y_variable_name,
         )
         expected = [
             f'report "======Simulation Start======" severity Note',
             f"vector_len <= to_unsigned(10, VECTOR_LEN_WIDTH)",
-            f"X_MEM <= ({x_mem_list_for_testing[0]})",
-            f"W_MEM <= ({w_mem_list_for_testing[0]})",
-            f"b <= {b_list_for_testing[0]}",
+            f"X_MEM <= ({to_hex(x_mem_list_for_testing[0])})",
+            f"W_MEM <= ({to_hex(w_mem_list_for_testing[0])})",
+            f"b <= {to_hex(b_list_for_testing[0])}",
             f"reset <= '1'",
             f"wait for 2*clk_period",
             f"wait until clock = '0'",
             f"reset <= '0'",
             f"wait until ready = '1'",
             f"report \"expected output is {y_list_for_testing[0]}, value of '{y_variable_name}' is \" & integer'image(to_integer(signed({y_variable_name})))",
             f'assert {y_variable_name}={y_list_for_testing[0]} report "The 0. test case fail" severity error',
             f"reset <= '1'",
             f"wait for 1*clk_period",
-            f"X_MEM <= ({x_mem_list_for_testing[1]})",
-            f"W_MEM <= ({w_mem_list_for_testing[1]})",
-            f"b <= {b_list_for_testing[1]}",
+            f"X_MEM <= ({to_hex(x_mem_list_for_testing[1])})",
+            f"W_MEM <= ({to_hex(w_mem_list_for_testing[1])})",
+            f"b <= {to_hex(b_list_for_testing[1])}",
             f"reset <= '1'",
             f"wait for 2*clk_period",
             f"wait until clock = '0'",
             f"reset <= '0'",
             f"wait until ready = '1'",
             f"report \"expected output is {y_list_for_testing[1]}, value of '{y_variable_name}' is \" & integer'image(to_integer(signed({y_variable_name})))",
             f'assert {y_variable_name}={y_list_for_testing[1]} report "The 1. test case fail" severity error',
             f"reset <= '1'",
             f"wait for 1*clk_period",
-            f"X_MEM <= ({x_mem_list_for_testing[2]})",
-            f"W_MEM <= ({w_mem_list_for_testing[2]})",
-            f"b <= {b_list_for_testing[2]}",
+            f"X_MEM <= ({to_hex(x_mem_list_for_testing[2])})",
+            f"W_MEM <= ({to_hex(w_mem_list_for_testing[2])})",
+            f"b <= {to_hex(b_list_for_testing[2])}",
             f"reset <= '1'",
             f"wait for 2*clk_period",
             f"wait until clock = '0'",
             f"reset <= '0'",
             f"wait until ready = '1'",
             f"report \"expected output is {y_list_for_testing[2]}, value of '{y_variable_name}' is \" & integer'image(to_integer(signed({y_variable_name})))",
             f'assert {y_variable_name}={y_list_for_testing[2]} report "The 2. test case fail" severity error',
@@ -96,56 +99,60 @@
             b_list_for_testing,
             y_list_for_testing,
             y_variable_name,
         )
 
 
 class TestCasesPrecomputedScalarFunctionTest(TestCase):
+    def setUp(self) -> None:
+        self.data_width, self.frac_width = 8, 0
+        self.fp_list = partial(
+            float_values_to_fixed_point,
+            total_bits=self.data_width,
+            frac_bits=self.frac_width,
+        )
+
     def test_TestCasesPrecomputedScalarFunction(self):
         x_list_for_testing = [1, 2, 3]
-        y_list_for_testing = [-5, "some_string", -3]
+        y_list_for_testing = [-5, -2, -3]
         x_variable_name = "x_name"
         y_variable_name = "y_name"
-        data_width = 3
         test_cases_precomputed_scalar_function = TestCasesPrecomputedScalarFunction(
-            x_list_for_testing=x_list_for_testing,
-            y_list_for_testing=y_list_for_testing,
+            x_list_for_testing=self.fp_list(x_list_for_testing),
+            y_list_for_testing=self.fp_list(y_list_for_testing),
             x_variable_name=x_variable_name,
             y_variable_name=y_variable_name,
-            data_width=data_width,
         )
         expected = [
             f'report "======Simulation Start======" severity Note',
-            f"{x_variable_name} <= to_signed({x_list_for_testing[0]},{data_width})",
+            f"{x_variable_name} <= to_signed({x_list_for_testing[0]},{self.data_width})",
             f"wait for 1*clk_period",
             f"report \"The value of '{y_variable_name}' is \" & integer'image(to_integer(unsigned({y_variable_name})))",
             f'assert {y_variable_name}={y_list_for_testing[0]} report "The test case {x_list_for_testing[0]} fail" severity failure',
-            f"{x_variable_name} <= to_signed({x_list_for_testing[1]},{data_width})",
+            f"{x_variable_name} <= to_signed({x_list_for_testing[1]},{self.data_width})",
             f"wait for 1*clk_period",
             f"report \"The value of '{y_variable_name}' is \" & integer'image(to_integer(unsigned({y_variable_name})))",
-            f'assert {y_variable_name}="{y_list_for_testing[1]}" report "The test case {x_list_for_testing[1]} fail" severity failure',
-            f"{x_variable_name} <= to_signed({x_list_for_testing[2]},{data_width})",
+            f'assert {y_variable_name}={y_list_for_testing[1]} report "The test case {x_list_for_testing[1]} fail" severity failure',
+            f"{x_variable_name} <= to_signed({x_list_for_testing[2]},{self.data_width})",
             f"wait for 1*clk_period",
             f"report \"The value of '{y_variable_name}' is \" & integer'image(to_integer(unsigned({y_variable_name})))",
             f'assert {y_variable_name}={y_list_for_testing[2]} report "The test case {x_list_for_testing[2]} fail" severity failure',
             f'report "======Simulation Success======" severity Note',
             f'report "Please check the output message." severity Note',
             f"wait",
         ]
         actual = list(test_cases_precomputed_scalar_function())
         self.assertSequenceEqual(expected, actual)
 
-    def test_TestCasesPrecomputedScalarFunction_different_lenghts_of_list(self):
+    def test_TestCasesPrecomputedScalarFunction_different_lengths_of_list(self):
         x_list_for_testing = [1, 2, 3]
         y_list_for_testing = [-5, -3]
         x_variable_name = "x_name"
         y_variable_name = "y_name"
-        data_width = 3
         self.assertRaises(
             AssertionError,
             TestCasesPrecomputedScalarFunction,
-            x_list_for_testing,
-            y_list_for_testing,
+            self.fp_list(x_list_for_testing),
+            self.fp_list(y_list_for_testing),
             x_variable_name,
             y_variable_name,
-            data_width,
         )
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/test_number_representations.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/test_number_representations.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,16 +1,15 @@
 from functools import partial
 from unittest import TestCase
 
 from elasticai.creator.vhdl.number_representations import (
     FixedPoint,
-    FloatToSignedFixedPointConverter,
     ToLogicEncoder,
-    hex_representation,
-    two_complements_representation,
+    float_values_to_fixed_point,
+    infer_total_and_frac_bits,
 )
 
 
 class FixedPointTest(TestCase):
     def test_zero(self):
         fp_value = FixedPoint(0, total_bits=1, frac_bits=0)
         self.assertEqual(0, int(fp_value))
@@ -37,71 +36,71 @@
 
     def test_fixed_point_to_float_minus_5_36(self):
         fp_value = FixedPoint(-5.36, total_bits=16, frac_bits=12)
         self.assertAlmostEqual(-5.36, float(fp_value), places=2)
 
     def test_to_hex_zero_with_one_bits(self):
         fp_value = FixedPoint(0, total_bits=1, frac_bits=0)
-        self.assertEqual('x"0"', fp_value.to_hex())
+        self.assertEqual("0", fp_value.to_hex())
 
     def test_to_hex_zero_with_six_bits(self):
         fp_value = FixedPoint(0, total_bits=6, frac_bits=0)
-        self.assertEqual('x"00"', fp_value.to_hex())
+        self.assertEqual("00", fp_value.to_hex())
 
     def test_to_hex_zero_with_sixteen_bits(self):
         fp_value = FixedPoint(0, total_bits=16, frac_bits=0)
-        self.assertEqual('x"0000"', fp_value.to_hex())
+        self.assertEqual("0000", fp_value.to_hex())
 
     def test_to_hex_minus_one_with_sixteen_bits(self):
         fp_value = FixedPoint(-1, total_bits=16, frac_bits=0)
-        self.assertEqual('x"ffff"', fp_value.to_hex())
+        self.assertEqual("ffff", fp_value.to_hex())
 
     def test_to_hex_minus_three_with_three_bits(self):
         fp_value = FixedPoint(-3, total_bits=3, frac_bits=0)
-        self.assertEqual('x"5"', fp_value.to_hex())
+        self.assertEqual("5", fp_value.to_hex())
 
     def test_to_hex_minus_254_with_sixteen_bits(self):
         fp_value = FixedPoint(-254, total_bits=16, frac_bits=0)
-        self.assertEqual('x"ff02"', fp_value.to_hex())
+        self.assertEqual("ff02", fp_value.to_hex())
 
     def test_to_hex_minus_19_5_with_16_bits(self):
         fp_value = FixedPoint(-19.5, total_bits=16, frac_bits=8)
-        self.assertEqual('x"ec80"', fp_value.to_hex())
+        self.assertEqual("ec80", fp_value.to_hex())
 
     def test_to_bin_zero_with_one_bits(self):
         fp_value = FixedPoint(0, total_bits=1, frac_bits=0)
-        self.assertEqual('"0"', fp_value.to_bin())
+        self.assertEqual("0", fp_value.to_bin())
 
     def test_to_bin_zero_with_three_bits(self):
         fp_value = FixedPoint(0, total_bits=3, frac_bits=0)
-        self.assertEqual('"000"', fp_value.to_bin())
+        self.assertEqual("000", fp_value.to_bin())
 
     def test_to_bin_five_with_four_bits(self):
         fp_value = FixedPoint(5, total_bits=4, frac_bits=0)
-        self.assertEqual('"0101"', fp_value.to_bin())
+        self.assertEqual("0101", fp_value.to_bin())
 
     def test_to_bin_minus_one_with_two_bits(self):
         fp_value = FixedPoint(-1, total_bits=2, frac_bits=0)
-        self.assertEqual('"11"', fp_value.to_bin())
+        self.assertEqual("11", fp_value.to_bin())
 
     def test_to_bin_minus_two_with_two_bits(self):
         fp_value = FixedPoint(-2, total_bits=2, frac_bits=0)
-        self.assertEqual('"10"', fp_value.to_bin())
+        self.assertEqual("10", fp_value.to_bin())
 
     def test_to_bin_minus_256_with_sixteen_bits(self):
         fp_value = FixedPoint(-256, total_bits=16, frac_bits=0)
-        self.assertEqual('"1111111100000000"', fp_value.to_bin())
+        self.assertEqual("1111111100000000", fp_value.to_bin())
 
     def test_to_bin_minus_254_with_sixteen_bits(self):
         fp_value = FixedPoint(-254, total_bits=16, frac_bits=0)
-        self.assertEqual('"1111111100000010"', fp_value.to_bin())
+        self.assertEqual("1111111100000010", fp_value.to_bin())
 
     def test_to_bin_minus_19_5_with_16_bits(self):
         fp_value = FixedPoint(-19.5, total_bits=16, frac_bits=8)
-        self.assertEqual('"1110110010000000"', fp_value.to_bin())
+        self.assertEqual("1110110010000000", fp_value.to_bin())
 
     def test_from_int(self):
         fp_value = FixedPoint.from_int(52388, total_bits=16, frac_bits=12)
         self.assertAlmostEqual(-3.21, float(fp_value), places=2)
 
     def test_repr(self):
         fp_value = FixedPoint(value=3.2, total_bits=8, frac_bits=4)
@@ -223,168 +222,129 @@
 
     def test_xor(self):
         fp1 = FixedPoint(5, total_bits=4, frac_bits=0)
         fp2 = FixedPoint(6, total_bits=4, frac_bits=0)
         result = FixedPoint(3, total_bits=4, frac_bits=0)
         self.assertEqual(result, fp1 ^ fp2)
 
+    def test_to_signed_int_positive_value(self):
+        fp = FixedPoint(5, total_bits=8, frac_bits=4)
+        self.assertEqual(80, fp.to_signed_int())
 
-class FixedPointConverterTest(TestCase):
-    def test_get_zero(self):
-        f = FloatToSignedFixedPointConverter(bits_used_for_fraction=0)
-        self.assertEqual(0, f(0))
-
-    def test_get_one_with_2bits_for_fraction(self):
-        f = FloatToSignedFixedPointConverter(bits_used_for_fraction=2)
-        self.assertEqual(1 << 2, f(1))
-
-    def test_get_one_with_3bits_for_fraction(self):
-        f = FloatToSignedFixedPointConverter(bits_used_for_fraction=3)
-        self.assertEqual(1 << 3, f(1))
-
-    def test_raise_error_if_not_convertible(self):
-        f = FloatToSignedFixedPointConverter(bits_used_for_fraction=0)
-        try:
-            f(0.5)
-            self.fail()
-        except ValueError as e:
-            self.assertEqual(
-                "0.5 not convertible to fixed point number using 0 bits for fractional part",
-                str(e),
-            )
+    def test_to_signed_int_negative_value(self):
+        fp = FixedPoint(-5, total_bits=8, frac_bits=4)
+        self.assertEqual(-80, fp.to_signed_int())
 
 
-class BinaryTwoComplementRepresentation(TestCase):
-    def test_zero_with_zero_bits(self):
+class InferTotalAndFracBits(TestCase):
+    def test_infer_empty_list(self):
         with self.assertRaises(ValueError):
-            _ = two_complements_representation(0, num_bits=0)
+            _, _ = infer_total_and_frac_bits([])
 
-    def test_five_with_minus_one_bits(self):
+    def test_infer_mixed_total_bits(self):
         with self.assertRaises(ValueError):
-            _ = two_complements_representation(5, num_bits=-1)
+            _, _ = infer_total_and_frac_bits(
+                [
+                    FixedPoint(0, total_bits=8, frac_bits=4),
+                    FixedPoint(0, total_bits=8, frac_bits=4),
+                    FixedPoint(0, total_bits=12, frac_bits=4),
+                    FixedPoint(0, total_bits=8, frac_bits=4),
+                ]
+            )
 
-    def test_zero_with_one_bits(self):
-        actual = two_complements_representation(0, num_bits=1)
-        expected = "0"
-        self.assertEqual(expected, actual)
-
-    def test_zero_with_three_bits(self):
-        actual = two_complements_representation(0, num_bits=3)
-        expected = "000"
-        self.assertEqual(expected, actual)
-
-    def test_five_with_four_bits(self):
-        actual = two_complements_representation(5, num_bits=4)
-        expected = "0101"
-        self.assertEqual(expected, actual)
-
-    def test_one(self):
-        actual = two_complements_representation(1, 1)
-        expected = "1"
-        self.assertEqual(expected, actual)
-
-    def test_minus_one(self):
-        actual = two_complements_representation(-1, 2)
-        expected = "11"
-        self.assertEqual(expected, actual)
-
-    def test_minus_two(self):
-        actual = two_complements_representation(-2, 2)
-        expected = "10"
-        self.assertEqual(expected, actual)
-
-    def test_two(self):
-        actual = two_complements_representation(2, 3)
-        expected = "010"
-        self.assertEqual(expected, actual)
-
-    def test_minus_four(self):
-        actual = two_complements_representation(-4, 3)
-        expected = "100"
-        self.assertEqual(expected, actual)
-
-    def test_minus_three_three_bit(self):
-        actual = two_complements_representation(-3, 3)
-        expected = "101"
-        self.assertEqual(expected, actual)
-
-    def test_minus_256_16_bit(self):
-        actual = two_complements_representation(-256, 16)
-        expected = "1111111100000000"
-        self.assertEqual(expected, actual)
-
-    def test_minus_254_16_bit(self):
-        actual = two_complements_representation(-254, 16)
-        expected = "1111111100000010"
-        self.assertEqual(expected, actual)
+    def test_infer_mixed_frac_bits(self):
+        with self.assertRaises(ValueError):
+            _, _ = infer_total_and_frac_bits(
+                [
+                    FixedPoint(0, total_bits=8, frac_bits=4),
+                    FixedPoint(0, total_bits=8, frac_bits=4),
+                    FixedPoint(0, total_bits=8, frac_bits=5),
+                    FixedPoint(0, total_bits=8, frac_bits=4),
+                ]
+            )
 
+    def test_infer_mixed_total_and_frac_bits(self):
+        with self.assertRaises(ValueError):
+            _, _ = infer_total_and_frac_bits(
+                [
+                    FixedPoint(0, total_bits=8, frac_bits=4),
+                    FixedPoint(0, total_bits=8, frac_bits=4),
+                    FixedPoint(0, total_bits=8, frac_bits=5),
+                    FixedPoint(0, total_bits=12, frac_bits=4),
+                ]
+            )
 
-class HexRepresentation(TestCase):
-    def test_zero_with_zero_bits(self):
+    def test_infer_valid_list(self):
+        total_bits, frac_bits = infer_total_and_frac_bits(
+            [
+                FixedPoint(0, total_bits=8, frac_bits=4),
+                FixedPoint(0, total_bits=8, frac_bits=4),
+            ]
+        )
+        self.assertEqual(8, total_bits)
+        self.assertEqual(4, frac_bits)
+
+    def test_infer_multiple_valid_lists(self):
+        values = [
+            FixedPoint(0, total_bits=8, frac_bits=4),
+            FixedPoint(0, total_bits=8, frac_bits=4),
+        ]
+        total_bits, frac_bits = infer_total_and_frac_bits(values, values, values)
+        self.assertEqual(8, total_bits)
+        self.assertEqual(4, frac_bits)
+
+    def test_infer_multiple_invalid_lists(self):
+        values1 = [
+            FixedPoint(0, total_bits=8, frac_bits=4),
+            FixedPoint(0, total_bits=8, frac_bits=4),
+        ]
+        values2 = [
+            FixedPoint(0, total_bits=12, frac_bits=4),
+            FixedPoint(0, total_bits=8, frac_bits=4),
+        ]
         with self.assertRaises(ValueError):
-            _ = hex_representation(0, num_bits=0)
+            _, _ = infer_total_and_frac_bits(values1, values2)
 
-    def test_five_with_minus_one_bits(self):
+    def test_infer_multiple_lists_with_empty_list(self):
+        values = [
+            FixedPoint(0, total_bits=8, frac_bits=4),
+            FixedPoint(0, total_bits=8, frac_bits=4),
+        ]
         with self.assertRaises(ValueError):
-            _ = hex_representation(5, num_bits=-1)
+            _, _ = infer_total_and_frac_bits(values, [])
+
 
-    def test_zero_with_one_bits(self):
-        actual = hex_representation(0, num_bits=1)
-        expected = 'x"0"'
-        self.assertEqual(expected, actual)
-
-    def test_zero_with_seven_bits(self):
-        actual = hex_representation(0, num_bits=7)
-        expected = 'x"00"'
-        self.assertEqual(expected, actual)
-
-    def test_one(self):
-        actual = hex_representation(1, 16)
-        expected = 'x"0001"'
-        self.assertEqual(expected, actual)
-
-    def test_minus_one(self):
-        actual = hex_representation(-1, 16)
-        expected = 'x"ffff"'
-        self.assertEqual(expected, actual)
-
-    def test_two(self):
-        actual = hex_representation(2, 16)
-        expected = 'x"0002"'
-        self.assertEqual(expected, actual)
-
-    def test_minus_two(self):
-        actual = hex_representation(-2, 16)
-        expected = 'x"fffe"'
-        self.assertEqual(expected, actual)
-
-    def test_minus_four_four_bit(self):
-        actual = hex_representation(-4, 4)
-        expected = 'x"c"'
-        self.assertEqual(expected, actual)
-
-    def test_minus_three_three_bit(self):
-        actual = hex_representation(-3, 3)
-        expected = 'x"5"'
-        self.assertEqual(expected, actual)
-
-    def test_minus_256_16_bit(self):
-        actual = hex_representation(-256, 16)
-        expected = 'x"ff00"'
-        self.assertEqual(expected, actual)
-
-    def test_minus_254_16_bit(self):
-        actual = hex_representation(-254, 16)
-        expected = 'x"ff02"'
-        self.assertEqual(expected, actual)
-
-    def test_255_with_12_bits(self):
-        actual = hex_representation(255, num_bits=12)
-        expected = 'x"0ff"'
-        self.assertEqual(expected, actual)
+class FloatValuesToFixedPointTest(TestCase):
+    def test_empty_list(self):
+        actual = float_values_to_fixed_point([], total_bits=8, frac_bits=4)
+        self.assertListEqual([], actual)
+
+    def test_full_list(self):
+        actual = float_values_to_fixed_point(
+            values=[1, 2, 3],
+            total_bits=8,
+            frac_bits=4,
+        )
+        target = [FixedPoint(value, total_bits=8, frac_bits=4) for value in range(1, 4)]
+        self.assertListEqual(target, actual)
+
+
+class IntValuesToFixedPointTest(TestCase):
+    def test_empty_list(self):
+        actual = float_values_to_fixed_point([], total_bits=8, frac_bits=0)
+        self.assertListEqual([], actual)
+
+    def test_full_list(self):
+        actual = float_values_to_fixed_point(
+            values=[1, 2, 3],
+            total_bits=8,
+            frac_bits=0,
+        )
+        target = [FixedPoint(value, total_bits=8, frac_bits=4) for value in range(1, 4)]
+        self.assertListEqual(target, actual)
 
 
 class NumberEncoderTest(TestCase):
     """
     Test Cases:
       - build new encoder from existing encoder ensuring compatibility of enumerations
         Use case scenario: Connecting the outputs of layer h_1 to the inputs of layer h_2, while we can consider the in-
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/test_precomputed_scalar_function_process.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/test_precomputed_scalar_function_process.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,44 +1,57 @@
 import unittest
+from functools import partial
 
+from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point
 from elasticai.creator.vhdl.precomputed_scalar_function import (
     precomputed_scalar_function_process,
 )
 
 
 class PrecomputedScalarFunctionProcessTest(unittest.TestCase):
+    def setUp(self) -> None:
+        self.fp_list = partial(float_values_to_fixed_point, total_bits=16, frac_bits=8)
+
     def test_empty_x_list_y_list_one_element(self) -> None:
         self.assertEqual(
-            list(precomputed_scalar_function_process(x_list=[], y_list=[1])),
+            list(precomputed_scalar_function_process(x=[], y=self.fp_list([1]))()),
             ['y <= "0000000100000000";'],
         )
 
     def test_empty_x_list_y_list_too_many_elements(self) -> None:
         with self.assertRaises(ValueError):
-            list(precomputed_scalar_function_process(x_list=[], y_list=[1, 2]))
+            list(precomputed_scalar_function_process(x=[], y=self.fp_list([1, 2]))())
 
     def test_empty_y_list(self) -> None:
         with self.assertRaises(ValueError):
-            list(precomputed_scalar_function_process(x_list=[], y_list=[]))
+            list(precomputed_scalar_function_process(x=[], y=[])())
 
     def test_x_list_lengths_not_suitable_for_y_list_lengths(self) -> None:
         with self.assertRaises(ValueError):
-            list(precomputed_scalar_function_process(x_list=[1, 2], y_list=[1]))
+            list(
+                precomputed_scalar_function_process(
+                    x=self.fp_list([1, 2]), y=self.fp_list([1])
+                )()
+            )
 
     def test_x_list_with_only_one_element(self) -> None:
         expected_code = [
             "if int_x<256 then",
             '\ty <= "0000000100000000"; -- 256',
             "else",
             '\ty <= "0000001000000000"; -- 512',
             "end if;",
         ]
         self.assertEqual(
             expected_code,
-            list(precomputed_scalar_function_process(x_list=[1], y_list=[1, 2])),
+            list(
+                precomputed_scalar_function_process(
+                    x=self.fp_list([1]), y=self.fp_list([1, 2])
+                )()
+            ),
         )
 
     def test_unsorted_x_list(self) -> None:
         expected_code = [
             "if int_x<256 then",
             '\ty <= "0000000100000000"; -- 256',
             "elsif int_x<512 then",
@@ -49,11 +62,11 @@
             '\ty <= "0000010000000000"; -- 1024',
             "end if;",
         ]
         self.assertEqual(
             expected_code,
             list(
                 precomputed_scalar_function_process(
-                    x_list=[3, 1, 2], y_list=[1, 2, 3, 4]
-                )
+                    x=self.fp_list([3, 1, 2]), y=self.fp_list([1, 2, 3, 4])
+                )()
             ),
         )
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/test_templates.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/test_templates.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/tests/vhdl/vhdl_file_testcase.py` & `elasticai.creator-0.9.0/elasticai/creator/tests/vhdl/vhdl_file_testcase.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/generator_functions_for_lstm_layer.py` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/generator_functions_for_lstm.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,109 +1,133 @@
-import random
 from functools import partial
 
 import numpy as np
 import torch
-from torch.nn import LSTM
+from torch.nn import LSTM, LSTMCell
 
 from elasticai.creator.vhdl.number_representations import (
-    FloatToSignedFixedPointConverter,
+    FixedPoint,
+    float_values_to_fixed_point,
 )
+from elasticai.creator.vhdl.rom import Rom
 
 
-def float_list_to_fixed_point(values: list[float], frac_bits: int) -> list[int]:
-    signed_fixed_point_converter = FloatToSignedFixedPointConverter(
-        bits_used_for_fraction=frac_bits, strict=False
-    )
-    return list(map(signed_fixed_point_converter, values))
+def generate_rom_file(
+    file_path: str,
+    rom_name: str,
+    values: list[FixedPoint],
+    resource_option: str,
+) -> None:
+    """
+    generates the rom files for a given list of values
+    Args:
+        file_path (str): paths where files should be stored
+        values (list[list[int]]): list with four lists with the fixed point values for each weight or bias
+        rom_name (str): name for the file
+        resource_option (str): resource option
+    """
+    with open(file_path, "w") as writer:
+        rom = Rom(
+            rom_name=rom_name,
+            values=values,
+            resource_option=resource_option,
+        )
+        rom_code = rom()
+        for line in rom_code:
+            writer.write(line + "\n")
 
 
-def inference_lstm_layer(
-    lstm_layer: LSTM,
+def inference_model_on_random_data(
+    lstm: LSTMCell | LSTM,
+    total_bits: int,
     frac_bits: int,
-    input_size: int,
-    hidden_size: int,
-) -> tuple[list[int], list[int], np.array]:
+) -> tuple[list[FixedPoint], list[FixedPoint], list[FixedPoint]]:
     """
-    do inference on the given multilayer LSTM
+    do inference on defined LSTM Cell or LSTM
     Args:
-        lstm_layer (QLSTMCell): current LSTM layer
-        frac_bits (int): number of fraction bits
-        input_size (int): input size of LSTM layer
-        hidden_size (int): hidden size of LSTM layer
+        lstm (LSTMCell | LSTM): current LSTM Cell or LSTM
+        total_bits (int): total number of bits for one fixed point number
+        frac_bits (int): number of fraction bits for one fixed point number
     Returns:
         returns three lists/arrays
-        the first and second list are the x_h input and cx of the lstm cell
+        the first and second list are the x_h input_data and cx of the lstm cell
         the third array is the hx of the lstm cell
     """
     torch.manual_seed(0)
-    random.seed(0)
 
-    input = torch.randn(2, 1, input_size)  # (time_steps, batch, input_size)
-    hx = torch.randn(1, hidden_size)  # (batch, hidden_size), this is the hidden states
-    cx = torch.randn(1, hidden_size)  # this the cell states
+    input_data = torch.randn(2, 1, lstm.input_size)  # (time_steps, batch, input_size)
+    hx = torch.randn(1, lstm.hidden_size)  # this is the hidden states
+    cx = torch.randn(1, lstm.hidden_size)  # this the cell states
+
+    x_h_input = np.hstack(([], [], []))
 
-    for i in range(input.size()[0]):
+    for i in range(input_data.size()[0]):
         x_h_input = np.hstack(
-            (input[i].detach().numpy().flatten(), hx.detach().numpy().flatten())
-        )
-        outputs, (hx, cx) = lstm_layer(input[i], (hx, cx))
-        c_array = cx.detach().numpy().flatten()
-        h_out_array = hx.detach().numpy().flatten()
-        return (
-            float_list_to_fixed_point(
-                x_h_input,
-                frac_bits=frac_bits,
-            ),
-            float_list_to_fixed_point(
-                c_array,
-                frac_bits=frac_bits,
-            ),
-            float_list_to_fixed_point(h_out_array, frac_bits=frac_bits),
+            (input_data[i].detach().numpy().flatten(), hx.detach().numpy().flatten())
         )
+        result = lstm(input_data[i], (hx, cx))
 
+        if isinstance(lstm, LSTMCell):
+            hx, cx = result
+        else:
+            _, (hx, cx) = result
 
-def define_weights_and_bias_of_lstm_layer(
-    lstm_layer: LSTM,
-    frac_bits: int,
-    len_weights: int,
-    len_bias: int,
-) -> tuple[list[list[int]], list[list[int]]]:
+    to_fp = partial(
+        float_values_to_fixed_point, total_bits=total_bits, frac_bits=frac_bits
+    )
+
+    return (
+        to_fp(x_h_input),
+        to_fp(cx.detach().numpy().flatten()),
+        to_fp(hx.detach().numpy().flatten()),
+    )
+
+
+def extract_fixed_point_weights_and_bias(
+    lstm: LSTMCell | LSTM, total_bits: int, frac_bits: int
+) -> tuple[list[list[FixedPoint]], list[list[FixedPoint]]]:
     """
     calculates the weights and bias for the 1st layer of the given multilayer LSTM
+    or the given LSTMCell
     Args:
-        lstm_layer (torch.nn.LSTM): current LSTM
-        frac_bits (int): number of fraction bits
-        len_weights (int): (input_size + hidden_size) * hidden_size
-        len_bias (int): hidden_size
+        lstm (LSTMCell | LSTM): current LSTM object
+        total_bits (int): total number of bits for one fixed point number
+        frac_bits (int): number of fraction bits for one fixed point number
     Returns:
         returns two lists, one for the weights and one for the bias
-        in each list are four list of strings with the hex numbers of the weights or bias
+        in each list are four list of FixedPoint numbers of the weights or bias
     """
-    for name, param in lstm_layer.named_parameters():
-        if name == "weight_ih_l0":
-            weight_ih = param.detach().numpy()
-        elif name == "weight_hh_l0":
-            weight_hh = param.detach().numpy()
-        elif name == "bias_ih_l0":
-            bias_ih = param.detach().numpy()
-        elif name == "bias_hh_l0":
-            bias_hh = param.detach().numpy()
+    if isinstance(lstm, LSTMCell):
+        weight_ih = lstm.weight_ih.detach().numpy()
+        weight_hh = lstm.weight_hh.detach().numpy()
+        bias_ih = lstm.bias_ih.detach().numpy()
+        bias_hh = lstm.bias_hh.detach().numpy()
+    else:
+        weight_ih = lstm.weight_ih_l0.detach().numpy()
+        weight_hh = lstm.weight_hh_l0.detach().numpy()
+        bias_ih = lstm.bias_ih_l0.detach().numpy()
+        bias_hh = lstm.bias_hh_l0.detach().numpy()
 
     weights = np.hstack((weight_ih, weight_hh)).flatten().flatten()
     bias = bias_hh + bias_ih
 
+    len_weights = (lstm.input_size + lstm.hidden_size) * lstm.hidden_size
+    len_bias = lstm.hidden_size
+
     wi = weights[len_weights * 0 : len_weights * 1]  # [Wii, Whi]
     wf = weights[len_weights * 1 : len_weights * 2]  # [Wif, Whf]
     wg = weights[len_weights * 2 : len_weights * 3]  # [Wig, Whg]
     wo = weights[len_weights * 3 : len_weights * 4]  # [Wio, Who]
 
     bi = bias[len_bias * 0 : len_bias * 1]  # B_ii+B_hi
     bf = bias[len_bias * 1 : len_bias * 2]  # B_if+B_hf
     bg = bias[len_bias * 2 : len_bias * 3]  # B_ig+B_hg
     bo = bias[len_bias * 3 : len_bias * 4]  # B_io+B_ho
 
-    to_fixed_point = partial(float_list_to_fixed_point, frac_bits=frac_bits)
-    fixed_point_weights = list(map(to_fixed_point, [wi, wf, wg, wo]))
-    fixed_point_bias = list(map(to_fixed_point, [bi, bf, bg, bo]))
+    to_fp = partial(
+        float_values_to_fixed_point, total_bits=total_bits, frac_bits=frac_bits
+    )
+
+    fixed_point_weights = list(map(to_fp, [wi, wf, wg, wo]))
+    fixed_point_bias = list(map(to_fp, [bi, bf, bg, bo]))
 
     return fixed_point_weights, fixed_point_bias
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/language.py` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/language.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,18 +5,17 @@
 formal grammar with our class names.
 
 The core of this module is the `CodeGenerator`. Code generators are callables that return `Code`.
 `Code` is an iterable of strings. Depending on complexity we define syntactic components of the vhdl
 grammar as `CodeGenerator`s. The class can then be used to set up and configure a function that yields lines
 of code as strings.
 """
-from collections import Sequence
 from enum import Enum
 from itertools import chain, filterfalse
-from typing import Callable, Iterable, Literal, Optional, Union
+from typing import Callable, Iterable, Literal, Optional, Sequence, Union
 
 Identifier = str
 Code = Iterable[str]
 CodeGenerator = Callable[[], Code]
 CodeGeneratorCompatible = Union[Code, CodeGenerator, str]
 
 
@@ -222,15 +221,15 @@
         if len(self.process_declaration_list) > 0:
             yield from _append_semicolons_to_lines(self.process_declaration_list)
 
     def _body(self) -> Code:
         if len(self.process_statements_list) > 0:
             yield from _append_semicolons_to_lines(self.process_statements_list)
         if self.lookup_table_generator_function:
-            yield from self.lookup_table_generator_function
+            yield from self.lookup_table_generator_function()
 
     def __call__(self) -> Code:
         if self.input:
             yield f"{self.identifier}_{Keywords.PROCESS.value}: {Keywords.PROCESS.value}({self.input})"
         else:
             yield f"{self.identifier}_{Keywords.PROCESS.value}: {Keywords.PROCESS.value}"
         yield from _filter_empty_lines(self._header())
@@ -520,7 +519,15 @@
             yield from _filter_empty_lines(_add_is(self._declaration_list_with_is()))
         yield f"{Keywords.BEGIN.value}"
         if len(self._statement_list) > 0:
             yield from _filter_empty_lines(
                 _add_semicolons(self._statement_list(), semicolon_last=True)
             )
         yield f"{Keywords.END.value} {self.identifier};"
+
+
+def hex_representation(hex_value: str) -> str:
+    return f'x"{hex_value}"'
+
+
+def bin_representation(bin_value: str) -> str:
+    return f'"{bin_value}"'
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/language_testbench.py` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/language_testbench.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/lstm_testbench_generator.py` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/lstm_testbench_generator.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,55 +1,58 @@
 import math
-from functools import partial
 from itertools import chain
 from typing import Iterable, Iterator
 
 from elasticai.creator.vhdl.language import (
     Architecture,
     Code,
     ContextClause,
     Entity,
     Keywords,
     LibraryClause,
     PortMap,
     Procedure,
     Process,
     UseClause,
+    hex_representation,
 )
 from elasticai.creator.vhdl.language_testbench import TestBenchBase
-from elasticai.creator.vhdl.number_representations import hex_representation
+from elasticai.creator.vhdl.number_representations import (
+    FixedPoint,
+    infer_total_and_frac_bits,
+)
 
 
 class LSTMCellTestBench:
     def __init__(
         self,
-        data_width: int,
-        frac_width: int,
         input_size: int,
         hidden_size: int,
-        test_x_h_data: list[int],
-        test_c_data: list[int],
-        h_out: list[int],
+        test_x_h_data: list[FixedPoint],
+        test_c_data: list[FixedPoint],
+        h_out: list[FixedPoint],
         component_name: str = None,
     ):
         self.component_name = self._get_lower_case_class_name_or_component_name(
             component_name=component_name
         )
-        self.data_width = data_width
-        self.frac_width = frac_width
         self.input_size = input_size
         self.hidden_size = hidden_size
         self.x_h_addr_width = math.ceil(math.log2(input_size + hidden_size))
-        self.hidden_addr_width = math.ceil(math.log2(hidden_size))
-        if self.hidden_addr_width == 0:
-            self.hidden_addr_width = 1
+        self.hidden_addr_width = max(1, math.ceil(math.log2(hidden_size)))
         self.w_addr_width = math.ceil(
             math.log2((input_size + hidden_size) * hidden_size)
         )
-        to_hex = partial(hex_representation, num_bits=data_width)
+        self.data_width, self.frac_width = infer_total_and_frac_bits(
+            test_x_h_data, test_c_data, h_out
+        )
+
+        def to_hex(value: FixedPoint) -> str:
+            return hex_representation(value.to_hex())
+
         self.test_x_h_data = list(map(to_hex, test_x_h_data))
         self.test_c_data = list(map(to_hex, test_c_data))
         self.h_out = h_out
 
     @classmethod
     def _get_lower_case_class_name_or_component_name(cls, component_name):
         if component_name is None:
@@ -247,30 +250,34 @@
         code = chain(library(), entity(), architecture())
         return code
 
 
 class TestCasesLSTMCommonGate(TestBenchBase):
     def __init__(
         self,
-        x_mem_list_for_testing: list[str],
-        w_mem_list_for_testing: list[str],
-        b_list_for_testing: list[str],
-        y_list_for_testing: list[int],
+        x_mem_list_for_testing: list[FixedPoint],
+        w_mem_list_for_testing: list[FixedPoint],
+        b_list_for_testing: list[FixedPoint],
+        y_list_for_testing: list[FixedPoint],
         y_variable_name: str = "y",
     ):
         assert (
             len(x_mem_list_for_testing)
             == len(w_mem_list_for_testing)
             == len(b_list_for_testing)
             == len(y_list_for_testing)
         )
-        self.x_mem_list_for_testing = x_mem_list_for_testing
-        self.w_mem_list_for_testing = w_mem_list_for_testing
-        self.y_list_for_testing = y_list_for_testing
-        self.b_list_for_testing = b_list_for_testing
+
+        def to_hex(value: FixedPoint) -> str:
+            return hex_representation(value.to_hex())
+
+        self.x_mem_list_for_testing = list(map(to_hex, x_mem_list_for_testing))
+        self.w_mem_list_for_testing = list(map(to_hex, w_mem_list_for_testing))
+        self.b_list_for_testing = list(map(to_hex, b_list_for_testing))
+        self.y_list_for_testing = list(map(int, y_list_for_testing))
         self.y_variable_name = y_variable_name
 
     def _body(self) -> Iterator[str]:
         counter = 0
         yield f"vector_len <= to_unsigned(10, VECTOR_LEN_WIDTH)"
         for x_mem_value, w_mem_value, b, y_value in zip(
             self.x_mem_list_for_testing,
@@ -296,16 +303,21 @@
             counter = counter + 1
 
     def __call__(self):
         yield from iter(self)
 
 
 class TestCasesLSTMCell(TestBenchBase):
-    def __init__(self, reference_h_out: list[int], input_size=0, hidden_size=0):
-        self.reference_h_out = reference_h_out
+    def __init__(
+        self,
+        reference_h_out: list[FixedPoint],
+        input_size: int = 0,
+        hidden_size: int = 0,
+    ):
+        self.reference_h_out = list(map(int, reference_h_out))
 
         assert (input_size != 0) and (
             hidden_size != 0
         ), "hidden_size and input_size is not set yet"
 
         self.len_of_x_h_vector = input_size + hidden_size
         self.len_of_cell_vector = hidden_size
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/number_representations.py` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/number_representations.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,9 +1,11 @@
 import math
-from typing import Any, Iterable, Iterator, Union
+from collections.abc import Sequence
+from itertools import chain
+from typing import Any, Iterable, Iterator
 
 
 class FixedPoint:
     __slots__ = ["_value", "_frac_bits", "_total_bits"]
 
     def __init__(
         self,
@@ -44,15 +46,15 @@
 
     def __ge__(self, other: Any) -> bool:
         return float(self) >= float(other)
 
     def __add__(self, other: "FixedPoint") -> "FixedPoint":
         FixedPoint._assert_is_compatible(self, other)
         return self._identical_fixed_point_from_int(
-            FixedPoint.discard_leading_bits(
+            FixedPoint._discard_leading_bits(
                 int(self) + int(other), num_bits=self._total_bits
             )
         )
 
     def __sub__(self, other: "FixedPoint") -> "FixedPoint":
         return self + (-other)
 
@@ -119,15 +121,15 @@
             )
 
     @staticmethod
     def _invert_int(value: int, num_bits: int) -> int:
         return value ^ int("1" * num_bits, 2)
 
     @staticmethod
-    def discard_leading_bits(value: int, num_bits: int) -> int:
+    def _discard_leading_bits(value: int, num_bits: int) -> int:
         return value & int("1" * num_bits, 2)
 
     @staticmethod
     def _calculate_two_complement(value: int, num_bits: int) -> int:
         return FixedPoint._invert_int(abs(value), num_bits) + 1
 
     @staticmethod
@@ -165,115 +167,56 @@
     @property
     def frac_bits(self) -> int:
         return self._frac_bits
 
     def bin_iter(self) -> Iterator[int]:
         return ((int(self) >> i) & 1 for i in range(self._total_bits))
 
+    def to_signed_int(self) -> int:
+        return int(abs(self)) * (-1 if self < 0 else 1)
+
     def to_bin(self) -> str:
-        return f'"{int(self):0{self._total_bits}b}"'
+        return f"{int(self):0{self._total_bits}b}"
 
     def to_hex(self) -> str:
-        return f'x"{int(self):0{math.ceil(self._total_bits / 4)}x}"'
-
+        return f"{int(self):0{math.ceil(self._total_bits / 4)}x}"
 
-class FloatToSignedFixedPointConverter:
-    """
-    Create a fixed point representation as an unsigned int data type using two complements.
 
-    We might want to have this create its own type `FixedPointNumber` in
-    the future. That way we could make sure that the conversion is idempotent
-    for numbers that are fixed point already.
-    """
-
-    def __init__(self, bits_used_for_fraction: int, strict=True):
-        self.bits_used_for_fraction = bits_used_for_fraction
-        self._strict = strict
-
-    @property
-    def one(self) -> int:
-        return 1 << self.bits_used_for_fraction
-
-    def __call__(self, x: float) -> int:
-        x_tmp = float(x)
-        x_tmp = x_tmp * self.one
-        if self._strict and not x_tmp.is_integer():
+def infer_total_and_frac_bits(*values: Sequence[FixedPoint]) -> tuple[int, int]:
+    if sum(len(value_list) == 0 for value_list in values) > 0:
+        raise ValueError("Cannot infer total bits and frac bits from an empty list.")
+    total_bits, frac_bits = values[0][0].total_bits, values[0][0].frac_bits
+    for value in chain(*values):
+        if value.total_bits != total_bits or value.frac_bits != frac_bits:
             raise ValueError(
-                f"{x} not convertible to fixed point number using {self.bits_used_for_fraction} bits for fractional part"
+                "Cannot infer total bits and frac bits from a list with mixed total bits or frac bits."
             )
-        return int(x_tmp)
-
-    def to_string(self, x: float) -> str:
-        return str(self.__call__(x))
+    return total_bits, frac_bits
 
 
-class FloatToBinaryFixedPointStringConverter:
-    def __init__(
-        self,
-        total_bit_width: int,
-        as_signed_fixed_point: FloatToSignedFixedPointConverter,
-    ):
-        self.total_bit_width = total_bit_width
-        self.as_signed_fixed_point = as_signed_fixed_point
-
-    def __call__(self, x: Union[float, int]) -> str:
-        signed_fixed_point = self.as_signed_fixed_point(x)
-        return two_complements_representation(signed_fixed_point, self.total_bit_width)
+def float_values_to_fixed_point(
+    values: list[float], total_bits: int, frac_bits: int
+) -> list[FixedPoint]:
+    return list(map(lambda x: FixedPoint(x, total_bits, frac_bits), values))
 
 
-class FloatToHexFixedPointStringConverter:
-    def __init__(
-        self,
-        total_bit_width: int,
-        as_signed_fixed_point: FloatToSignedFixedPointConverter,
-    ):
-        self.total_bit_width = total_bit_width
-        self.as_signed_fixed_point = as_signed_fixed_point
-
-    def __call__(self, x: Union[float, int]) -> str:
-        signed_fixed_point = self.as_signed_fixed_point(x)
-        return hex_representation(signed_fixed_point, self.total_bit_width)
+def int_values_to_fixed_point(
+    values: list[int], total_bits: int, frac_bits: int
+) -> list[FixedPoint]:
+    return list(map(lambda x: FixedPoint.from_int(x, total_bits, frac_bits), values))
 
 
 def _int_to_bin_str(number: int, bits: int) -> str:
     if number < 0:
         raise ValueError("Negative values are not supported.")
     if bits <= 0 or (number > 0 and math.log2(number) > bits):
         raise ValueError(f"The number {number} cannot be represented with {bits} bits.")
     return "{{0:0{number_of_bits}b}}".format(number_of_bits=bits).format(number)
 
 
-def _int_to_hex_str(number: int, bits: int) -> str:
-    if number < 0:
-        raise ValueError("Negative values are not supported.")
-    if bits <= 0 or (number > 0 and math.log2(number) > bits):
-        raise ValueError(f"The number {number} cannot be represented with {bits} bits.")
-    return 'x"{{:0{number_of_bits}x}}"'.format(
-        number_of_bits=math.ceil(bits / 4)
-    ).format(number)
-
-
-def _get_unsigned_int_version(x, number_of_bits):
-    if x < 0:
-        unsigned_int_version = (1 << number_of_bits) + x
-    else:
-        unsigned_int_version = x
-    return unsigned_int_version
-
-
-def hex_representation(x: int, num_bits: int) -> str:
-    unsigned_int_version = _get_unsigned_int_version(x, num_bits)
-    return _int_to_hex_str(unsigned_int_version, num_bits)
-
-
-def two_complements_representation(x, num_bits):
-    unsigned_int_version = _get_unsigned_int_version(x, num_bits)
-    return _int_to_bin_str(unsigned_int_version, num_bits)
-
-
 class ToLogicEncoder:
     """
     Throughout our implementations we have to deal with two different levels of representations for numbers:
     During training we typically need to apply mathematical operations and we do not care too much about how our numbers are encoded.
     E.g. in a scenario where we want to use two bit on hardware to represent our numbers, in our machine learning framework we
     might decide it is beneficial to use the numbers -3 and 4 for some reason. However, especially in the context of precomputed
     results, the hardware implementation does not need to know the numeric values, but instead just needs to be able to keep a
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/precomputed_scalar_function.py` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/precomputed_scalar_function.py`

 * *Files 9% similar despite different names*

```diff
@@ -13,99 +13,99 @@
     DataType,
     Entity,
     InterfaceVariable,
     LibraryClause,
     PortMap,
     Process,
     UseClause,
+    bin_representation,
 )
 from elasticai.creator.vhdl.language_testbench import TestBenchBase
 from elasticai.creator.vhdl.number_representations import (
-    FloatToBinaryFixedPointStringConverter,
-    FloatToSignedFixedPointConverter,
+    FixedPoint,
+    float_values_to_fixed_point,
+    infer_total_and_frac_bits,
 )
 
 
-def _vhdl_add_assignment(code: list, line_id: str, value: str, comment=None) -> None:
-    new_code_fragment = f'{line_id} <= "{value}";'
+def _vhdl_add_assignment(
+    code: list, line_id: str, value: str, comment: str = None
+) -> None:
+    new_code_fragment = f"{line_id} <= {bin_representation(value)};"
     if comment is not None:
         new_code_fragment += f" -- {comment}"
     code.append(new_code_fragment)
 
 
-def precomputed_scalar_function_process(x_list, y_list) -> CodeGenerator:
+def precomputed_scalar_function_process(
+    x: list[FixedPoint], y: list[FixedPoint]
+) -> CodeGenerator:
     """
         returns the string of a lookup table
     Args:
-        y_list : output List contains integers
-        x_list: input List contains integers
+        x (FixedPoint): input list
+        y (FixedPoint) : output list
     Returns:
         String of lookup table (if/elsif statements for vhdl file)
     """
-    as_signed_fixed_point = FloatToSignedFixedPointConverter(
-        bits_used_for_fraction=8, strict=False
-    )
-    as_binary_string = FloatToBinaryFixedPointStringConverter(
-        total_bit_width=16, as_signed_fixed_point=as_signed_fixed_point
-    )
-    x_list.sort()
+    x.sort()
     lines = []
-    if len(x_list) == 0 and len(y_list) == 1:
+    if len(x) == 0 and len(y) == 1:
         _vhdl_add_assignment(
             code=lines,
             line_id="y",
-            value=as_binary_string(y_list[0]),
+            value=y[0].to_bin(),
         )
-    elif len(x_list) != len(y_list) - 1:
+    elif len(x) != len(y) - 1:
         raise ValueError(
-            "x_list has to be one element shorter than y_list, but x_list has {} elements and y_list {} elements".format(
-                len(x_list), len(y_list)
-            )
+            f"x has to be one element shorter than y, but x has {len(x)} elements and y {len(y)} elements"
         )
     else:
-        smallest_possible_output = y_list[0]
-        biggest_possible_output = y_list[-1]
+        smallest_possible_output = y[0]
+        biggest_possible_output = y[-1]
 
         # first element
-        for x in x_list[:1]:
-            lines.append("if int_x<{0} then".format(as_signed_fixed_point(x)))
+        for x_value in x[:1]:
+            lines.append(f"if int_x<{x_value.to_signed_int()} then")
             _vhdl_add_assignment(
                 code=lines,
                 line_id="y",
-                value=as_binary_string(smallest_possible_output),
-                comment=as_signed_fixed_point(smallest_possible_output),
+                value=smallest_possible_output.to_bin(),
+                comment=str(smallest_possible_output.to_signed_int()),
             )
             lines[-1] = "\t" + lines[-1]
-        for current_x, current_y in zip(x_list[1:], y_list[1:-1]):
-            lines.append(
-                "elsif int_x<{0} then".format(as_signed_fixed_point(current_x))
-            )
+        for current_x, current_y in zip(x[1:], y[1:-1]):
+            lines.append(f"elsif int_x<{current_x.to_signed_int()} then")
             _vhdl_add_assignment(
                 code=lines,
                 line_id="y",
-                value=as_binary_string(current_y),
-                comment=as_signed_fixed_point(current_y),
+                value=current_y.to_bin(),
+                comment=str(current_y.to_signed_int()),
             )
             lines[-1] = "\t" + lines[-1]
         # last element only in y
-        for _ in y_list[-1:]:
+        for _ in y[-1:]:
             lines.append("else")
             _vhdl_add_assignment(
                 code=lines,
                 line_id="y",
-                value=as_binary_string(biggest_possible_output),
-                comment=as_signed_fixed_point(biggest_possible_output),
+                value=biggest_possible_output.to_bin(),
+                comment=str(biggest_possible_output.to_signed_int()),
             )
             lines[-1] = "\t" + lines[-1]
         if len(lines) != 0:
             lines.append("end if;")
+
     # build the string block
-    yield lines[0]
-    for line in lines[1:]:
-        yield line
+
+    def generator() -> Code:
+        for line in lines:
+            yield line
+
+    return generator
 
 
 class DataWidthVariable(InterfaceVariable):
     def __init__(self, value: int):
         super().__init__(
             identifier="DATA_WIDTH", identifier_type=DataType.INTEGER, value=f"{value}"
         )
@@ -116,31 +116,35 @@
         super().__init__(
             identifier="FRAC_WIDTH", identifier_type=DataType.INTEGER, value=f"{value}"
         )
 
 
 class PrecomputedScalarFunction:
     def __init__(
-        self, data_width, frac_width, x, y, component_name=None, process_instance=None
+        self,
+        x: list[FixedPoint],
+        y: list[FixedPoint],
+        component_name: str = None,
+        process_instance: Process = None,
     ):
         """
         We calculate the function with an algorithm equivalent to:
         ```
         def function(x: int, inputs: list[int], outputs: list[int]) -> int:
           for input, output in zip(inputs, outputs[:-1]):
             if x < input:
               return output
           return outputs[-1]
         ```
         """
         self.component_name = self._get_lower_case_class_name_or_component_name(
             component_name=component_name
         )
-        self.data_width = data_width
-        self.frac_width = frac_width
+
+        self.data_width, self.frac_width = infer_total_and_frac_bits(x, y)
         self.x = x
         self.y = y
         self.process_instance = process_instance
 
     @classmethod
     def _get_lower_case_class_name_or_component_name(cls, component_name):
         if component_name is None:
@@ -169,76 +173,67 @@
         entity.port_list = [
             "x : in signed(DATA_WIDTH-1 downto 0)",
             "y : out signed(DATA_WIDTH-1 downto 0)",
         ]
         process = Process(
             identifier=self.component_name,
             lookup_table_generator_function=precomputed_scalar_function_process(
-                x_list=self.x, y_list=self.y
+                x=self.x, y=self.y
             ),
             input_name="x",
         )
         process.process_declaration_list = ["variable int_x: integer := 0"]
         process.process_statements_list = ["int_x := to_integer(x)"]
         architecture = Architecture(
             design_unit=self.component_name,
         )
         architecture.architecture_statement_part = process
         code = chain(chain(library(), entity()), architecture())
         return code
 
 
 class Sigmoid(PrecomputedScalarFunction):
-    def __init__(self, data_width, frac_width, x, component_name=None):
-        x_list = torch.as_tensor(x)
+    def __init__(self, x: list[FixedPoint], component_name: str = None):
+        x_tensor = torch.as_tensor(list(map(float, x)))
         # calculate y always for the previous element, therefore the last input is not needed here
-        y_list = list(torch.nn.Sigmoid()(x_list[:-1]))
-        y_list.insert(0, 0)
-        # add last y value, therefore, x_list is one element shorter than y_list
-        y_list.append(1)
-        super(Sigmoid, self).__init__(
-            data_width=data_width,
-            frac_width=frac_width,
-            x=x,
-            y=y_list,
-            component_name=component_name,
-        )
+        y = torch.nn.Sigmoid()(x_tensor[:-1]).tolist()
+        y.insert(0, 0)
+        # add last y value, therefore, x_tensor is one element shorter than y_tensor
+        y.append(1)
+        y = float_values_to_fixed_point(y, *infer_total_and_frac_bits(x))
+
+        super(Sigmoid, self).__init__(x=x, y=y, component_name=component_name)
 
 
 class Tanh(PrecomputedScalarFunction):
-    def __init__(self, data_width, frac_width, x, component_name=None):
-        y_list = [-1]
+    def __init__(self, x: list[FixedPoint], component_name: str = None):
+        y_list = [-1.0]
         # calculate y always for the previous element, therefore the last input is not needed here
         for x_element in x[:-1]:
-            y_list.append(math.tanh(x_element))
+            y_list.append(math.tanh(float(x_element)))
         # add last y value, therefore, x_list is one element shorter than y_list
         y_list.append(1)
-        super(Tanh, self).__init__(
-            data_width=data_width,
-            frac_width=frac_width,
-            x=x,
-            y=y_list,
-            component_name=component_name,
-        )
+        y = float_values_to_fixed_point(y_list, *infer_total_and_frac_bits(x))
+
+        super(Tanh, self).__init__(x=x, y=y, component_name=component_name)
 
 
 class PrecomputedScalarTestBench:
     def __init__(
         self,
-        data_width: int,
-        frac_width: int,
-        x_list_for_testing: list,
-        y_list_for_testing: list,
+        x_list_for_testing: list[FixedPoint],
+        y_list_for_testing: list[FixedPoint],
         component_name: str = None,
     ):
         self.component_name = self._get_lower_case_class_name_or_component_name(
             component_name=component_name
         )
-        self.data_width = data_width
-        self.frac_width = frac_width
+        self.data_width, self.frac_width = infer_total_and_frac_bits(
+            x_list_for_testing, y_list_for_testing
+        )
         self.x_list_for_testing = x_list_for_testing
         self.y_list_for_testing = y_list_for_testing
 
     @classmethod
     def _get_lower_case_class_name_or_component_name(cls, component_name):
         if component_name is None:
             return cls.__name__.lower()
@@ -292,15 +287,14 @@
         uut_port_map = PortMap(map_name="uut", component_name=self.component_name)
         uut_port_map.signal_list.append("x => test_input")
         uut_port_map.signal_list.append("y => test_output")
 
         test_cases = TestCasesPrecomputedScalarFunction(
             x_list_for_testing=self.x_list_for_testing,
             y_list_for_testing=self.y_list_for_testing,
-            data_width=self.data_width,
         )
         test_process = Process(identifier="test")
         test_process.process_statements_list = [t for t in test_cases()]
 
         architecture = Architecture(
             design_unit=self.component_name + "_tb",
         )
@@ -318,26 +312,31 @@
         code = chain(library(), entity(), architecture())
         return code
 
 
 class TestCasesPrecomputedScalarFunction(TestBenchBase):
     def __init__(
         self,
-        x_list_for_testing: list[int],
-        y_list_for_testing: list[int],
+        x_list_for_testing: list[FixedPoint],
+        y_list_for_testing: list[FixedPoint],
         x_variable_name: str = "test_input",
         y_variable_name: str = "test_output",
-        data_width: int = 16,
     ):
         assert len(x_list_for_testing) == len(y_list_for_testing)
-        self.x_list_for_testing = x_list_for_testing
-        self.y_list_for_testing = y_list_for_testing
+        self.data_width, _ = infer_total_and_frac_bits(
+            x_list_for_testing, y_list_for_testing
+        )
+        self.x_list_for_testing = [
+            value.to_signed_int() for value in x_list_for_testing
+        ]
+        self.y_list_for_testing = [
+            value.to_signed_int() for value in y_list_for_testing
+        ]
         self.x_variable_name = x_variable_name
         self.y_variable_name = y_variable_name
-        self.data_width = data_width
 
     def __len__(self):
         return len(self.y_list_for_testing)
 
     def _body(self) -> Iterator[str]:
         for x_value, y_value in zip(self.x_list_for_testing, self.y_list_for_testing):
             yield f"{self.x_variable_name} <= to_signed({x_value},{self.data_width})"
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/rom.py` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/rom.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,32 +1,41 @@
 import math
-from functools import partial
+from collections.abc import Sequence
 
 from elasticai.creator.resource_utils import read_text
-from elasticai.creator.vhdl.number_representations import hex_representation
+from elasticai.creator.vhdl.language import hex_representation
+from elasticai.creator.vhdl.number_representations import (
+    FixedPoint,
+    infer_total_and_frac_bits,
+)
 
 
-def pad_with_zeros(numbers: list[int], target_length: int) -> list[int]:
-    return numbers + [0] * (target_length - len(numbers))
+def pad_with_zeros(numbers: list[FixedPoint], target_length: int) -> list[FixedPoint]:
+    zero = FixedPoint(0, *infer_total_and_frac_bits(numbers))
+    return numbers + [zero] * (target_length - len(numbers))
 
 
 class Rom:
     def __init__(
-        self, rom_name: str, data_width: int, values: list[int], resource_option: str
+        self,
+        rom_name: str,
+        values: Sequence[FixedPoint],
+        resource_option: str,
     ):
         self.rom_name = rom_name
-        self.data_width = data_width
+        self.data_width, _ = infer_total_and_frac_bits(values)
         self.addr_width = self._calculate_required_addr_width_to_access_items(values)
-        padded_values = pad_with_zeros(values, 2**self.addr_width)
-        to_hex = partial(hex_representation, num_bits=data_width)
-        self.hex_values = list(map(to_hex, padded_values))
+        padded_values = pad_with_zeros(list(values), 2**self.addr_width)
+        self.hex_values = list(
+            map(lambda fp: hex_representation(fp.to_hex()), padded_values)
+        )
         self.resource_option = resource_option
 
     @staticmethod
-    def _calculate_required_addr_width_to_access_items(items: list) -> int:
+    def _calculate_required_addr_width_to_access_items(items: Sequence) -> int:
         return max(1, math.ceil(math.log2(len(items))))
 
     def __call__(self):
         template = read_text("elasticai.creator.vhdl.templates", "rom.tpl.vhd")
 
         code = template.format(
             rom_name=self.rom_name,
```

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/dual_port_2_clock_ram.vhd` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/dual_port_2_clock_ram.vhd`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/lstm_cell.vhd` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/lstm_cell.vhd`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/lstm_common.vhd` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/lstm_common.vhd`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/rom.tpl.vhd` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/rom.tpl.vhd`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/templates/utils.py` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/templates/utils.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/truth_table.py` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/truth_table.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/elasticai/creator/vhdl/vhdl_formatter/vhdl_formatter.py` & `elasticai.creator-0.9.0/elasticai/creator/vhdl/vhdl_formatter/vhdl_formatter.py`

 * *Files identical despite different names*

### Comparing `elasticai.creator-0.7.0/setup.py` & `elasticai.creator-0.9.0/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,27 +1,21 @@
 # -*- coding: utf-8 -*-
 from setuptools import setup
 
 packages = \
 ['elasticai',
  'elasticai.creator',
- 'elasticai.creator.brevitas',
- 'elasticai.creator.brevitas.translation_functions',
  'elasticai.creator.examples',
  'elasticai.creator.examples.generate_vhdl_files',
  'elasticai.creator.integrationTests',
- 'elasticai.creator.integrationTests.brevitas_representation',
  'elasticai.creator.integrationTests.vhdl',
  'elasticai.creator.mlframework',
  'elasticai.creator.precomputation',
  'elasticai.creator.qat',
- 'elasticai.creator.systemTests',
- 'elasticai.creator.systemTests.brevitas_representation',
  'elasticai.creator.tests',
- 'elasticai.creator.tests.brevitas_representation',
  'elasticai.creator.tests.precomputation',
  'elasticai.creator.tests.qat',
  'elasticai.creator.tests.vhdl',
  'elasticai.creator.vhdl',
  'elasticai.creator.vhdl.precomputed_convs',
  'elasticai.creator.vhdl.templates',
  'elasticai.creator.vhdl.templates.precomputed_convs',
@@ -29,36 +23,35 @@
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
 ['MonkeyType>=21.5.0,<22.0.0',
  'bitarray>=2.3.5,<3.0.0',
- 'torch>=1.10.0,<2.0.0',
+ 'torch>=1.11.0,<2.0.0',
  'vsg>=3.9.0,<4.0.0']
 
 extras_require = \
-{'brevitas': ['brevitas>=0.7.0,<0.8.0',
-              'onnx>=1.10.2,<2.0.0',
-              'onnxoptimizer>=0.2.6,<0.3.0'],
- 'examples': ['torchvision>=0.11.2,<0.12.0'],
- 'systemtests': ['torchvision>=0.11.2,<0.12.0']}
+{':extra == "onnx"': ['numpy>=1.22.3,<2.0.0'],
+ 'examples': ['torchvision>=0.12.0,<0.13.0'],
+ 'onnx': ['protobuf>=3.16,<3.17', 'onnx>=1.11,<2.0'],
+ 'systemtests': ['torchvision>=0.12.0,<0.13.0']}
 
 setup_kwargs = {
     'name': 'elasticai.creator',
-    'version': '0.7.0',
+    'version': '0.9.0',
     'description': 'Design, train and compile neural networks optimized specifically for FPGAs.',
-    'long_description': '# ElasticAi.creator\n\nDesign, train and compile neural networks optimized specifically for FPGAs.\nObtaining a final model is typically a three stage process.\n* design and train it using the layers provided in the `elasticai.creator` package.\n* translate the model to a target representation, e.g. VHDL\n* compile the intermediate representation with a third party tool, e.g. Xilinx Vivado (TM)\n\nThis version currently only supports [Brevitas](https://github.com/Xilinx/brevitas) and parts of VHDL as target representations.\n\nThe project is part of the elastic ai ecosystem developed by the Embedded Systems Department of the University Duisburg-Essen. For more details checkout the slides at [researchgate](https://www.researchgate.net/publication/356372207_In-Situ_Artificial_Intelligence_for_Self-_Devices_The_Elastic_AI_Ecosystem_Tutorial).\n\n\n## Table of contents\n\n- [Users Guide](#users-guide)\n  - [Install](#install)\n- [Developers Guide](#developers-guide)\n  - [Install Dev Dependencies](#install-dev-dependencies)\n\n\n## Users Guide\n\n#### Install\nYou can install the ElasticAI.creator as a dependency using pip:\n```bash\npython3 -m pip install "elasticai.creator"\n```\n\n\n## Structure of the Project\n\nThe structure of the project is as follows.\nThe [creator](elasticai/creator) folder includes all main concepts of our project, especially the qtorch implementation which is our implementation of quantized PyTorch layer.\nIt also includes the supported target representations, like the subfolder [brevitas](elasticai/creator/brevitas) is for the translation to Brevitas or the subfolder [vhdl](elasticai/creator/vhdl) for the translation to Vhdl.\nAdditionally, we have folders for [unit tests](elasticai/creator/tests), [integration tests](elasticai/creator/integrationTests) and [system tests](elasticai/creator/systemTests).\n\n\n## General Limitations\n\nBy now we only support Sequential models for our translations.\n\n## Developers Guide\n### Install Dev Dependencies\n- [poetry](https://python-poetry.org/)\n- recommended:\n  - [pre-commit](https://pre-commit.com/)\n  - [commitlint](https://github.com/conventional-changelog/commitlint) to help following our [conventional commit](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#summary) guidelines\npoetry can be installed in the following way:\n```bash\npip install poetry\npip install pre-commit\npoetry install -D\npre-commit install\nnpm install --save-dev @commitlint/{config-conventional,cli}\nsudo apt install ghdl\n```\n\n### Commit Message Scopes\n\n- **qat**: quantization-aware-training\n  - Examples: `QConv1D`, `QLSTM`, autograd functions, etc.\n- **readme**\n- **precomputation**: entities that deal with the precomputation of ML components\n  - Examples: the `precomputable` decorator or the `IOTable` class\n- **vhdl**: vhdl code generation\n  - Examples: `vhdl.TruthTable`, `vhdl.LSTMCell`\n- **gh-workflow**\n- **pyproject**: changes to the `pyproject.toml` file will typically either update run or dev dependencies\n- **typing**: changing type annotations and changes to code to allow consistent type annotations\n- **pre-commit**\n\n### Adding new translation targets\nNew translation targets should be located in their own folder, e.g. Brevitas for translating from any language to Brevitas.\nWorkflow for adding a new translation:\n1. Obtain a structure, such as a list in a sequential case, which will describe the connection between every component.\n2. Identify and label relevant structures, in the base cases it can be simply separate layers.\n3. Map each structure to its function which will convert it, like for [example](elasticai/creator/brevitas/translation_mapping.py).\n4. Do such conversions.\n5. Recreate connections based on 1.\n\nEach sub-step should be separable and it helps for testing if common functions are wrapped around an adapter.\n\n### Syntax Checking\n\n[GHDL](https://ghdl.github.io/ghdl/) supports a [syntax checking](https://umarcor.github.io/ghdl/using/InvokingGHDL.html#check-syntax-s) which checks the syntax of a vhdl file without generating code.\nThe command is as follows:\n```\nghdl -s path/to/vhdl/file\n```\nSo, for example for checking the sigmoid source vhdl files in our project we can run:\n```\nghdl -s elasticai/creator/vhdl/source/sigmoid.vhd\n```\nFor checking all vhdl files together in our project we can just run:\n```\nghdl -s elasticai/creator/**/*.vhd\n```\n\n### Tests\n\nOur implementation is fully tested with unit, integration and system tests.\nPlease refer to the system tests as examples of how to use the Elastic Ai Creator Translator.\nYou can run one explicit test with the following statement:\n\n```python -m unittest discover -p "test_*.py" elasticai/creator/path/to/test.py```\n\nIf you want to run all tests, give the path to the tests:\n\n```python -m unittest discover -p "test_*.py" elasticai/creator/path/to/testfolder```\n\nYou can also run all tests together:\n\n```python -m unittest discover -p "test_*.py" elasticai/creator/translator/path/to/language/```\n\nIf you want to add more tests please refer to the Test Guidelines in the following.\n\n### Test style Guidelines\n\n#### File IO\nIn general try to avoid interaction with the filesystem. In most cases instead of writing to or reading from a file you can use a StringIO object or a StringReader.\nIf you absolutely have to create files, be sure to use pythons [tempfile](https://docs.python.org/3.9/library/tempfile.html) module and cleanup after the tests.\n\n\n#### Diectory structure and file names\nFiles containing tests for a python module should be located in a test directory for the sake of separation of concerns.\nEach file in the test directory should contain tests for one and only one class/function defined in the module.\nFiles containing tests should be named according to the rubric\n`test_ClassName.py`.\nNext, if needed for more specific tests define a class which is a subclass of unittest.TestCase like [test_brevitas_model_comparison](elasticai/creator/integrationTests/brevitas_representation/test_brevitas_model_comparison.py) in the integration tests folder.\nThen subclass it, in this class define a setUp method (and possibly tearDown) to create the global environment.\nIt avoids introducing the category of bugs associated with copying and pasting code for reuse.\nThis class should be named similarly to the file name.\nThere\'s a category of bugs that appear if  the initialization parameters defined at the top of the test file are directly used: some tests require the initialization parameters to be changed slightly.\nIts possible to define a parameter and have it change in memory as a result of a test.\nSubsequent tests will therefore throw errors.\nEach class contains methods that implement a test.\nThese methods are named according to the rubric\n`test_name_condition`\n\n#### Unit tests\nIn those tests each functionality of each function in the module is tested, it is the entry point  when adding new functions.\nIt assures that the function behaves correctly independently of others.\nEach test has to be fast, so use of heavier libraries is discouraged.\nThe input used is the minimal one needed to obtain a reproducible output.\nDependencies should be replaced with mocks as needed.\n\n#### Integration Tests\nHere the functions\' behaviour with other modules is tested.\nIn this repository each integration function is in the correspondent folder.\nThen the integration with a single class of the target, or the minimum amount of classes for a functionality, is tested in each separated file.\n\n#### System tests\nThose tests will use every component of the system, comprising multiple classes.\nThose tests include expected use cases and unexpected or stress tests.\n\n#### Adding new functionalities and tests required\nWhen adding new functions to an existing module, add unit tests in the correspondent file in the same order of the module, if a new module is created a new file should be created.\nWhen a bug is solved created the respective regression test to ensure that it will not return.\nProceed similarly with integration tests.\nCreating a new file if a functionality completely different from the others is created e.g. support for a new layer.\nSystem tests are added if support for a new library is added.\n\n#### Updating tests\nIf new functionalities are changed or removed the tests are expected to reflect that, generally the ordering is unit tests -> integration tests-> system tests.\nAlso, unit tests that change the dependencies should be checked, since this system is fairly small the internal dependencies are not always mocked.\n\nreferences: https://jrsmith3.github.io/python-testing-style-guidelines.html\n',
+    'long_description': '# ElasticAi.creator\n\nDesign, train and compile neural networks optimized specifically for FPGAs.\nObtaining a final model is typically a three stage process.\n* design and train it using the layers provided in the `elasticai.creator.qat` package.\n* translate the model to a target representation, e.g. VHDL\n* compile the intermediate representation with a third party tool, e.g. Xilinx Vivado (TM)\n\nThis version currently only supports parts of VHDL as target representations.\n\nThe project is part of the elastic ai ecosystem developed by the Embedded Systems Department of the University Duisburg-Essen. For more details checkout the slides at [researchgate](https://www.researchgate.net/publication/356372207_In-Situ_Artificial_Intelligence_for_Self-_Devices_The_Elastic_AI_Ecosystem_Tutorial).\n\n\n## Table of contents\n\n- [Users Guide](#users-guide)\n  - [Install](#install)\n- [Developers Guide](#developers-guide)\n  - [Install Dev Dependencies](#install-dev-dependencies)\n\n\n## Users Guide\n\n#### Install\nYou can install the ElasticAI.creator as a dependency using pip:\n```bash\npython3 -m pip install "elasticai.creator"\n```\n\n\n## Structure of the Project\n\nThe structure of the project is as follows.\nThe [creator](elasticai/creator) folder includes all main concepts of our project, especially the qtorch implementation which is our implementation of quantized PyTorch layer.\nIt also includes the supported target representations, like the subfolder [vhdl](elasticai/creator/vhdl) is for the translation to vhdl.\nAdditionally, we have folders for [unit tests](elasticai/creator/tests) and [integration tests](elasticai/creator/integrationTests).\n\n\n## General Limitations\n\nBy now we only support Sequential models for our translations.\n\n## Developers Guide\n### Install Dev Dependencies\n- [poetry](https://python-poetry.org/)\n- recommended:\n  - [pre-commit](https://pre-commit.com/)\n  - [commitlint](https://github.com/conventional-changelog/commitlint) to help following our [conventional commit](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#summary) guidelines\npoetry can be installed in the following way:\n```bash\npip install poetry\npip install pre-commit\npoetry install -D\npre-commit install\nnpm install --save-dev @commitlint/{config-conventional,cli}\nsudo apt install ghdl\n```\n\n### Install/Compile ONNX dependency\n```bash\nsudo apt install python3-dev libprotobuf-dev protobuf-compiler\nexport CMAKE_ARGS="-DONNX_USE_PROTOBUF_SHARED_LIBS=ON"\npoetry install --extras onnx\n```\n\n### Commit Message Scopes\n\n- **qat**: quantization-aware-training\n  - Examples: `QConv1D`, `QLSTM`, autograd functions, etc.\n- **readme**\n- **precomputation**: entities that deal with the precomputation of ML components\n  - Examples: the `precomputable` decorator or the `IOTable` class\n- **vhdl**: vhdl code generation\n  - Examples: `vhdl.TruthTable`, `vhdl.LSTMCell`\n- **gh-workflow**\n- **pyproject**: changes to the `pyproject.toml` file will typically either update run or dev dependencies\n- **typing**: changing type annotations and changes to code to allow consistent type annotations\n- **pre-commit**\n\n### Adding new translation targets\nNew translation targets should be located in their own folder, e.g. vhdl for translating from any language to vhdl.\nWorkflow for adding a new translation:\n1. Obtain a structure, such as a list in a sequential case, which will describe the connection between every component.\n2. Identify and label relevant structures, in the base cases it can be simply separate layers.\n3. Map each structure to its function which will convert it.\n4. Do such conversions.\n5. Recreate connections based on 1.\n\nEach sub-step should be separable and it helps for testing if common functions are wrapped around an adapter.\n\n### Syntax Checking\n\n[GHDL](https://ghdl.github.io/ghdl/) supports a [syntax checking](https://umarcor.github.io/ghdl/using/InvokingGHDL.html#check-syntax-s) which checks the syntax of a vhdl file without generating code.\nThe command is as follows:\n```\nghdl -s path/to/vhdl/file\n```\nSo, for example for checking the sigmoid source vhdl files in our project we can run:\n```\nghdl -s elasticai/creator/vhdl/source/sigmoid.vhd\n```\nFor checking all vhdl files together in our project we can just run:\n```\nghdl -s elasticai/creator/**/*.vhd\n```\n\n### Tests\n\nOur implementation is fully tested with unit, integration and system tests.\nPlease refer to the system tests as examples of how to use the Elastic Ai Creator Translator.\nYou can run one explicit test with the following statement:\n\n```python -m unittest discover -p "test_*.py" elasticai/creator/path/to/test.py```\n\nIf you want to run all tests, give the path to the tests:\n\n```python -m unittest discover -p "test_*.py" elasticai/creator/path/to/testfolder```\n\nYou can also run all tests together:\n\n```python -m unittest discover -p "test_*.py" elasticai/creator/translator/path/to/language/```\n\nIf you want to add more tests please refer to the Test Guidelines in the following.\n\n### Test style Guidelines\n\n#### File IO\nIn general try to avoid interaction with the filesystem. In most cases instead of writing to or reading from a file you can use a StringIO object or a StringReader.\nIf you absolutely have to create files, be sure to use pythons [tempfile](https://docs.python.org/3.9/library/tempfile.html) module and cleanup after the tests.\n\n\n#### Diectory structure and file names\nFiles containing tests for a python module should be located in a test directory for the sake of separation of concerns.\nEach file in the test directory should contain tests for one and only one class/function defined in the module.\nFiles containing tests should be named according to the rubric\n`test_ClassName.py`.\nNext, if needed for more specific tests define a class. Then subclass it, in this class define a setUp method (and possibly tearDown) to create the global environment.\nIt avoids introducing the category of bugs associated with copying and pasting code for reuse.\nThis class should be named similarly to the file name.\nThere\'s a category of bugs that appear if  the initialization parameters defined at the top of the test file are directly used: some tests require the initialization parameters to be changed slightly.\nIts possible to define a parameter and have it change in memory as a result of a test.\nSubsequent tests will therefore throw errors.\nEach class contains methods that implement a test.\nThese methods are named according to the rubric\n`test_name_condition`\n\n#### Unit tests\nIn those tests each functionality of each function in the module is tested, it is the entry point  when adding new functions.\nIt assures that the function behaves correctly independently of others.\nEach test has to be fast, so use of heavier libraries is discouraged.\nThe input used is the minimal one needed to obtain a reproducible output.\nDependencies should be replaced with mocks as needed.\n\n#### Integration Tests\nHere the functions\' behaviour with other modules is tested.\nIn this repository each integration function is in the correspondent folder.\nThen the integration with a single class of the target, or the minimum amount of classes for a functionality, is tested in each separated file.\n\n#### System tests\nThose tests will use every component of the system, comprising multiple classes.\nThose tests include expected use cases and unexpected or stress tests.\n\n#### Adding new functionalities and tests required\nWhen adding new functions to an existing module, add unit tests in the correspondent file in the same order of the module, if a new module is created a new file should be created.\nWhen a bug is solved created the respective regression test to ensure that it will not return.\nProceed similarly with integration tests.\nCreating a new file if a functionality completely different from the others is created e.g. support for a new layer.\nSystem tests are added if support for a new library is added.\n\n#### Updating tests\nIf new functionalities are changed or removed the tests are expected to reflect that, generally the ordering is unit tests -> integration tests-> system tests.\nAlso, unit tests that change the dependencies should be checked, since this system is fairly small the internal dependencies are not always mocked.\n\nreferences: https://jrsmith3.github.io/python-testing-style-guidelines.html\n',
     'author': 'Department Embedded Systems - University Duisburg Essen',
     'author_email': None,
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://github.com/es-ude/elastic-ai.creator',
     'packages': packages,
     'package_data': package_data,
     'install_requires': install_requires,
     'extras_require': extras_require,
-    'python_requires': '>=3.9,<3.10',
+    'python_requires': '>=3.10,<4.0',
 }
 
 
 setup(**setup_kwargs)
```

### Comparing `elasticai.creator-0.7.0/PKG-INFO` & `elasticai.creator-0.9.0/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,39 +1,39 @@
 Metadata-Version: 2.1
 Name: elasticai.creator
-Version: 0.7.0
+Version: 0.9.0
 Summary: Design, train and compile neural networks optimized specifically for FPGAs.
 Home-page: https://github.com/es-ude/elastic-ai.creator
 Author: Department Embedded Systems - University Duisburg Essen
-Requires-Python: >=3.9,<3.10
+Requires-Python: >=3.10,<4.0
 Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.9
-Provides-Extra: brevitas
+Classifier: Programming Language :: Python :: 3.10
 Provides-Extra: examples
+Provides-Extra: onnx
 Provides-Extra: systemtests
 Requires-Dist: MonkeyType (>=21.5.0,<22.0.0)
 Requires-Dist: bitarray (>=2.3.5,<3.0.0)
-Requires-Dist: brevitas (>=0.7.0,<0.8.0); extra == "brevitas"
-Requires-Dist: onnx (>=1.10.2,<2.0.0); extra == "brevitas"
-Requires-Dist: onnxoptimizer (>=0.2.6,<0.3.0); extra == "brevitas"
-Requires-Dist: torch (>=1.10.0,<2.0.0)
-Requires-Dist: torchvision (>=0.11.2,<0.12.0); extra == "examples" or extra == "systemtests"
+Requires-Dist: numpy (>=1.22.3,<2.0.0); extra == "onnx"
+Requires-Dist: onnx (>=1.11,<2.0); extra == "onnx"
+Requires-Dist: protobuf (>=3.16,<3.17); extra == "onnx"
+Requires-Dist: torch (>=1.11.0,<2.0.0)
+Requires-Dist: torchvision (>=0.12.0,<0.13.0); extra == "examples" or extra == "systemtests"
 Requires-Dist: vsg (>=3.9.0,<4.0.0)
 Project-URL: Repository, https://github.com/es-ude/elastic-ai.creator
 Description-Content-Type: text/markdown
 
 # ElasticAi.creator
 
 Design, train and compile neural networks optimized specifically for FPGAs.
 Obtaining a final model is typically a three stage process.
-* design and train it using the layers provided in the `elasticai.creator` package.
+* design and train it using the layers provided in the `elasticai.creator.qat` package.
 * translate the model to a target representation, e.g. VHDL
 * compile the intermediate representation with a third party tool, e.g. Xilinx Vivado (TM)
 
-This version currently only supports [Brevitas](https://github.com/Xilinx/brevitas) and parts of VHDL as target representations.
+This version currently only supports parts of VHDL as target representations.
 
 The project is part of the elastic ai ecosystem developed by the Embedded Systems Department of the University Duisburg-Essen. For more details checkout the slides at [researchgate](https://www.researchgate.net/publication/356372207_In-Situ_Artificial_Intelligence_for_Self-_Devices_The_Elastic_AI_Ecosystem_Tutorial).
 
 
 ## Table of contents
 
 - [Users Guide](#users-guide)
@@ -51,16 +51,16 @@
 ```
 
 
 ## Structure of the Project
 
 The structure of the project is as follows.
 The [creator](elasticai/creator) folder includes all main concepts of our project, especially the qtorch implementation which is our implementation of quantized PyTorch layer.
-It also includes the supported target representations, like the subfolder [brevitas](elasticai/creator/brevitas) is for the translation to Brevitas or the subfolder [vhdl](elasticai/creator/vhdl) for the translation to Vhdl.
-Additionally, we have folders for [unit tests](elasticai/creator/tests), [integration tests](elasticai/creator/integrationTests) and [system tests](elasticai/creator/systemTests).
+It also includes the supported target representations, like the subfolder [vhdl](elasticai/creator/vhdl) is for the translation to vhdl.
+Additionally, we have folders for [unit tests](elasticai/creator/tests) and [integration tests](elasticai/creator/integrationTests).
 
 
 ## General Limitations
 
 By now we only support Sequential models for our translations.
 
 ## Developers Guide
@@ -75,14 +75,21 @@
 pip install pre-commit
 poetry install -D
 pre-commit install
 npm install --save-dev @commitlint/{config-conventional,cli}
 sudo apt install ghdl
 ```
 
+### Install/Compile ONNX dependency
+```bash
+sudo apt install python3-dev libprotobuf-dev protobuf-compiler
+export CMAKE_ARGS="-DONNX_USE_PROTOBUF_SHARED_LIBS=ON"
+poetry install --extras onnx
+```
+
 ### Commit Message Scopes
 
 - **qat**: quantization-aware-training
   - Examples: `QConv1D`, `QLSTM`, autograd functions, etc.
 - **readme**
 - **precomputation**: entities that deal with the precomputation of ML components
   - Examples: the `precomputable` decorator or the `IOTable` class
@@ -90,19 +97,19 @@
   - Examples: `vhdl.TruthTable`, `vhdl.LSTMCell`
 - **gh-workflow**
 - **pyproject**: changes to the `pyproject.toml` file will typically either update run or dev dependencies
 - **typing**: changing type annotations and changes to code to allow consistent type annotations
 - **pre-commit**
 
 ### Adding new translation targets
-New translation targets should be located in their own folder, e.g. Brevitas for translating from any language to Brevitas.
+New translation targets should be located in their own folder, e.g. vhdl for translating from any language to vhdl.
 Workflow for adding a new translation:
 1. Obtain a structure, such as a list in a sequential case, which will describe the connection between every component.
 2. Identify and label relevant structures, in the base cases it can be simply separate layers.
-3. Map each structure to its function which will convert it, like for [example](elasticai/creator/brevitas/translation_mapping.py).
+3. Map each structure to its function which will convert it.
 4. Do such conversions.
 5. Recreate connections based on 1.
 
 Each sub-step should be separable and it helps for testing if common functions are wrapped around an adapter.
 
 ### Syntax Checking
 
@@ -146,16 +153,15 @@
 
 
 #### Diectory structure and file names
 Files containing tests for a python module should be located in a test directory for the sake of separation of concerns.
 Each file in the test directory should contain tests for one and only one class/function defined in the module.
 Files containing tests should be named according to the rubric
 `test_ClassName.py`.
-Next, if needed for more specific tests define a class which is a subclass of unittest.TestCase like [test_brevitas_model_comparison](elasticai/creator/integrationTests/brevitas_representation/test_brevitas_model_comparison.py) in the integration tests folder.
-Then subclass it, in this class define a setUp method (and possibly tearDown) to create the global environment.
+Next, if needed for more specific tests define a class. Then subclass it, in this class define a setUp method (and possibly tearDown) to create the global environment.
 It avoids introducing the category of bugs associated with copying and pasting code for reuse.
 This class should be named similarly to the file name.
 There's a category of bugs that appear if  the initialization parameters defined at the top of the test file are directly used: some tests require the initialization parameters to be changed slightly.
 Its possible to define a parameter and have it change in memory as a result of a test.
 Subsequent tests will therefore throw errors.
 Each class contains methods that implement a test.
 These methods are named according to the rubric
```

