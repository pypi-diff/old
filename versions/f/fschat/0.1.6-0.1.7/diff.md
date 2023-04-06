# Comparing `tmp/fschat-0.1.6.tar.gz` & `tmp/fschat-0.1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "fschat-0.1.6.tar", last modified: Thu Apr  6 15:41:37 2023, max compression
+gzip compressed data, was "fschat-0.1.7.tar", last modified: Thu Apr  6 18:46:24 2023, max compression
```

## Comparing `fschat-0.1.6.tar` & `fschat-0.1.7.tar`

### file list

```diff
@@ -1,50 +1,51 @@
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 15:41:37.963410 fschat-0.1.6/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    11357 2023-04-03 18:06:47.000000 fschat-0.1.6/LICENSE
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10108 2023-04-06 15:41:37.963410 fschat-0.1.6/PKG-INFO
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9634 2023-04-06 14:45:10.000000 fschat-0.1.6/README.md
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 15:41:37.959411 fschat-0.1.6/fastchat/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       88 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/constants.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6432 2023-04-06 02:45:48.000000 fschat-0.1.6/fastchat/conversation.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 15:41:37.959411 fschat-0.1.6/fastchat/data/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/data/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1819 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/data/alpaca-converter.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4465 2023-04-06 02:45:48.000000 fschat-0.1.6/fastchat/data/clean_sharegpt.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      615 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/data/inspect.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2684 2023-04-06 02:45:48.000000 fschat-0.1.6/fastchat/data/optional_clean.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      475 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/data/pretty_json.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3403 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/data/split_long_conversation.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 15:41:37.959411 fschat-0.1.6/fastchat/eval/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5042 2023-04-06 05:27:02.000000 fschat-0.1.6/fastchat/eval/eval_gpt_review.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3661 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/eval/generate_webpage_data_from_table.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3054 2023-04-06 05:27:02.000000 fschat-0.1.6/fastchat/eval/get_model_answer.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2345 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/eval/qa_baseline_gpt35.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 15:41:37.959411 fschat-0.1.6/fastchat/model/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/model/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1904 2023-04-06 15:41:16.000000 fschat-0.1.6/fastchat/model/apply_delta.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2167 2023-04-06 15:41:16.000000 fschat-0.1.6/fastchat/model/make_delta.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 15:41:37.959411 fschat-0.1.6/fastchat/serve/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/serve/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6201 2023-04-06 15:35:02.000000 fschat-0.1.6/fastchat/serve/cli.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9942 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/serve/controller.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2717 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/serve/gradio_css.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7343 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/serve/gradio_patch.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16246 2023-04-06 05:27:02.000000 fschat-0.1.6/fastchat/serve/gradio_web_server.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8756 2023-04-06 14:49:35.000000 fschat-0.1.6/fastchat/serve/model_worker.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3997 2023-04-06 14:44:46.000000 fschat-0.1.6/fastchat/serve/monkey_patch_non_inplace.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      734 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/serve/register_worker.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2028 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/serve/test_message.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 15:41:37.963410 fschat-0.1.6/fastchat/train/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3982 2023-04-06 14:12:17.000000 fschat-0.1.6/fastchat/train/llama_flash_attn_monkey_patch.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    12308 2023-04-06 13:02:10.000000 fschat-0.1.6/fastchat/train/train.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3657 2023-04-06 05:27:02.000000 fschat-0.1.6/fastchat/train/train_lora.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      420 2023-04-03 18:06:47.000000 fschat-0.1.6/fastchat/train/train_mem.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3988 2023-04-06 14:12:04.000000 fschat-0.1.6/fastchat/utils.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 15:41:37.963410 fschat-0.1.6/fschat.egg-info/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10108 2023-04-06 15:41:37.000000 fschat-0.1.6/fschat.egg-info/PKG-INFO
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1166 2023-04-06 15:41:37.000000 fschat-0.1.6/fschat.egg-info/SOURCES.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2023-04-06 15:41:37.000000 fschat-0.1.6/fschat.egg-info/dependency_links.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      115 2023-04-06 15:41:37.000000 fschat-0.1.6/fschat.egg-info/requires.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       21 2023-04-06 15:41:37.000000 fschat-0.1.6/fschat.egg-info/top_level.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      938 2023-04-06 15:41:21.000000 fschat-0.1.6/pyproject.toml
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       38 2023-04-06 15:41:37.963410 fschat-0.1.6/setup.cfg
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 18:46:24.074892 fschat-0.1.7/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    11357 2023-04-03 18:06:47.000000 fschat-0.1.7/LICENSE
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10443 2023-04-06 18:46:24.074892 fschat-0.1.7/PKG-INFO
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9969 2023-04-06 18:43:48.000000 fschat-0.1.7/README.md
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 18:46:24.070892 fschat-0.1.7/fastchat/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       88 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/constants.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6432 2023-04-06 02:45:48.000000 fschat-0.1.7/fastchat/conversation.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 18:46:24.070892 fschat-0.1.7/fastchat/data/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/data/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1819 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/data/alpaca-converter.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4465 2023-04-06 02:45:48.000000 fschat-0.1.7/fastchat/data/clean_sharegpt.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      615 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/data/inspect.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2684 2023-04-06 02:45:48.000000 fschat-0.1.7/fastchat/data/optional_clean.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      475 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/data/pretty_json.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3403 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/data/split_long_conversation.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 18:46:24.070892 fschat-0.1.7/fastchat/eval/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5042 2023-04-06 05:27:02.000000 fschat-0.1.7/fastchat/eval/eval_gpt_review.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3661 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/eval/generate_webpage_data_from_table.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3054 2023-04-06 05:27:02.000000 fschat-0.1.7/fastchat/eval/get_model_answer.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2345 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/eval/qa_baseline_gpt35.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 18:46:24.070892 fschat-0.1.7/fastchat/model/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/model/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1904 2023-04-06 15:41:16.000000 fschat-0.1.7/fastchat/model/apply_delta.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2167 2023-04-06 15:41:16.000000 fschat-0.1.7/fastchat/model/make_delta.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 18:46:24.070892 fschat-0.1.7/fastchat/serve/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/serve/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6388 2023-04-06 18:35:15.000000 fschat-0.1.7/fastchat/serve/cli.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3632 2023-04-06 18:35:15.000000 fschat-0.1.7/fastchat/serve/compression.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9942 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/serve/controller.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2717 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/serve/gradio_css.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7343 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/serve/gradio_patch.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16246 2023-04-06 05:27:02.000000 fschat-0.1.7/fastchat/serve/gradio_web_server.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8756 2023-04-06 14:49:35.000000 fschat-0.1.7/fastchat/serve/model_worker.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3997 2023-04-06 14:44:46.000000 fschat-0.1.7/fastchat/serve/monkey_patch_non_inplace.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      734 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/serve/register_worker.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2028 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/serve/test_message.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 18:46:24.074892 fschat-0.1.7/fastchat/train/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3982 2023-04-06 14:12:17.000000 fschat-0.1.7/fastchat/train/llama_flash_attn_monkey_patch.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    12308 2023-04-06 13:02:10.000000 fschat-0.1.7/fastchat/train/train.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3657 2023-04-06 05:27:02.000000 fschat-0.1.7/fastchat/train/train_lora.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      420 2023-04-03 18:06:47.000000 fschat-0.1.7/fastchat/train/train_mem.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3988 2023-04-06 14:12:04.000000 fschat-0.1.7/fastchat/utils.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-04-06 18:46:24.074892 fschat-0.1.7/fschat.egg-info/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10443 2023-04-06 18:46:24.000000 fschat-0.1.7/fschat.egg-info/PKG-INFO
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1196 2023-04-06 18:46:24.000000 fschat-0.1.7/fschat.egg-info/SOURCES.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2023-04-06 18:46:24.000000 fschat-0.1.7/fschat.egg-info/dependency_links.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      115 2023-04-06 18:46:24.000000 fschat-0.1.7/fschat.egg-info/requires.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       21 2023-04-06 18:46:24.000000 fschat-0.1.7/fschat.egg-info/top_level.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      938 2023-04-06 18:46:15.000000 fschat-0.1.7/pyproject.toml
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       38 2023-04-06 18:46:24.074892 fschat-0.1.7/setup.cfg
```

### Comparing `fschat-0.1.6/LICENSE` & `fschat-0.1.7/LICENSE`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/PKG-INFO` & `fschat-0.1.7/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fschat
-Version: 0.1.6
+Version: 0.1.7
 Summary: An open platform for training, serving, and evaluating large language model based chatbots.
 Project-URL: Homepage, https://github.com/lm-sys/fastchat
 Project-URL: Bug Tracker, https://github.com/lm-sys/fastchat/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
@@ -60,15 +60,15 @@
 ```
 
 ## Vicuna Weights
 We release [Vicuna](https://vicuna.lmsys.org/) weights as delta weights to comply with the LLaMA model license.
 You can add our delta to the original LLaMA weights to obtain the Vicuna weights. Instructions:
 
 1. Get the original LLaMA weights in the huggingface format by following the instructions [here](https://huggingface.co/docs/transformers/main/model_doc/llama).
-2. Use the following scripts to get Vicuna weights by applying our delta. It will automatically download delta weights from our Hugging Face account.
+2. Use the following scripts to get Vicuna weights by applying our delta. They will automatically download delta weights from our Hugging Face account.
 
 **NOTE**:
 Our released weights are only compatible with the latest main branch of huggingface/transformers.
 We install the correct version of transformers when fastchat is installed.
 
 ### Vicuna-13B
 This conversion command needs around 60 GB of CPU RAM.
@@ -76,47 +76,52 @@
 python3 -m fastchat.model.apply_delta \
     --base /path/to/llama-13b \
     --target /output/path/to/vicuna-13b \
     --delta lmsys/vicuna-13b-delta-v0
 ```
 
 ### Vicuna-7B
-Coming soon.
+This conversion command needs around 30 GB of CPU RAM.
+```bash
+python3 -m fastchat.model.apply_delta \
+    --base /path/to/llama-7b \
+    --target /output/path/to/vicuna-7b \
+    --delta lmsys/vicuna-7b-delta-v0
+```
 
 ## Inference with Command Line Interface
 
 ### Single GPU
-The command below requires around 28GB of GPU memory for Vicuna-13B.
+The command below requires around 28GB of GPU memory for Vicuna-13B and 14GB of GPU memory for Vicuna-7B.
 ```
 python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights
 ```
 
 ### Multiple GPUs
 If you do not have enough GPU memory, you can use model parallelism to aggregate memory from multiple GPUs on the same machine.
 ```
 python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --num-gpus 2
 ```
 
 ### CPU Only
-This runs on the CPU only and does not require GPU. It requires around 60GB of CPU memory for Vicuna-13B.
+This runs on the CPU only and does not require GPU. It requires around 60GB of CPU memory for Vicuna-13B and around 30GB of CPU memory for Vicuna-7B.
 ```
 python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --device cpu
 ```
 
 ### Metal Backend (Mac computers with Apple silicon or AMD GPUs)
+Use `--device mps` to enable GPU acceleration on Mac computers and use `--load-8bit` to turn on 8-bit compression.
 ```
-python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --device mps
+python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --device mps --load-8bit
 ```
 
 ### Others (Quantization, Low-end Devices, and More Platforms)
-
-You can load in 8-bit mode to reduce GPU memory usage with slightly degraded model quality.
-It is tested on a single 4090 and requires around 18GB of GPU memory for Vicuna-13B.
-Note that this mode only works on a single GPU.
-You are also required to install `bitsandbytes` according to the printed messages.
+If you do not have enough memory, you can enable 8-bit compression by adding `--load-8bit` to commands above.
+It works with CPU, GPU, and Metal.
+This can reduce the memory usage by around half with slightly degraded model quality.
 
 ```
 python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --load-8bit
 ```
 
 Besides, we are actively exploring more methods to make the model easier to run on more platforms.
 Contributions and pull requests are welcome.
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: fschat Version: 0.1.6 Summary: An open platform for
+Metadata-Version: 2.1 Name: fschat Version: 0.1.7 Summary: An open platform for
 training, serving, and evaluating large language model based chatbots. Project-
 URL: Homepage, https://github.com/lm-sys/fastchat Project-URL: Bug Tracker,
 https://github.com/lm-sys/fastchat/issues Classifier: Programming Language ::
 Python :: 3 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Python: >=3.8 Description-Content-Type: text/markdown License-File:
 LICENSE # FastChat An open platform for training, serving, and evaluating large
 language model based chatbots. ## Release
@@ -23,40 +23,44 @@
 Install Package ```bash pip3 install --upgrade pip # enable PEP 660 support
 pip3 install -e . ``` ## Vicuna Weights We release [Vicuna](https://
 vicuna.lmsys.org/) weights as delta weights to comply with the LLaMA model
 license. You can add our delta to the original LLaMA weights to obtain the
 Vicuna weights. Instructions: 1. Get the original LLaMA weights in the
 huggingface format by following the instructions [here](https://huggingface.co/
 docs/transformers/main/model_doc/llama). 2. Use the following scripts to get
-Vicuna weights by applying our delta. It will automatically download delta
+Vicuna weights by applying our delta. They will automatically download delta
 weights from our Hugging Face account. **NOTE**: Our released weights are only
 compatible with the latest main branch of huggingface/transformers. We install
 the correct version of transformers when fastchat is installed. ### Vicuna-13B
 This conversion command needs around 60 GB of CPU RAM. ```bash python3 -
 m fastchat.model.apply_delta \ --base /path/to/llama-13b \ --target /output/
-path/to/vicuna-13b \ --delta lmsys/vicuna-13b-delta-v0 ``` ### Vicuna-7B Coming
-soon. ## Inference with Command Line Interface ### Single GPU The command below
-requires around 28GB of GPU memory for Vicuna-13B. ``` python3 -
+path/to/vicuna-13b \ --delta lmsys/vicuna-13b-delta-v0 ``` ### Vicuna-7B This
+conversion command needs around 30 GB of CPU RAM. ```bash python3 -
+m fastchat.model.apply_delta \ --base /path/to/llama-7b \ --target /output/
+path/to/vicuna-7b \ --delta lmsys/vicuna-7b-delta-v0 ``` ## Inference with
+Command Line Interface ### Single GPU The command below requires around 28GB of
+GPU memory for Vicuna-13B and 14GB of GPU memory for Vicuna-7B. ``` python3 -
 m fastchat.serve.cli --model-name /path/to/vicuna/weights ``` ### Multiple GPUs
 If you do not have enough GPU memory, you can use model parallelism to
 aggregate memory from multiple GPUs on the same machine. ``` python3 -
 m fastchat.serve.cli --model-name /path/to/vicuna/weights --num-gpus 2 ``` ###
 CPU Only This runs on the CPU only and does not require GPU. It requires around
-60GB of CPU memory for Vicuna-13B. ``` python3 -m fastchat.serve.cli --model-
-name /path/to/vicuna/weights --device cpu ``` ### Metal Backend (Mac computers
-with Apple silicon or AMD GPUs) ``` python3 -m fastchat.serve.cli --model-name
-/path/to/vicuna/weights --device mps ``` ### Others (Quantization, Low-end
-Devices, and More Platforms) You can load in 8-bit mode to reduce GPU memory
-usage with slightly degraded model quality. It is tested on a single 4090 and
-requires around 18GB of GPU memory for Vicuna-13B. Note that this mode only
-works on a single GPU. You are also required to install `bitsandbytes`
-according to the printed messages. ``` python3 -m fastchat.serve.cli --model-
-name /path/to/vicuna/weights --load-8bit ``` Besides, we are actively exploring
-more methods to make the model easier to run on more platforms. Contributions
-and pull requests are welcome. ## Serving with Web GUI ### Launch a controller
+60GB of CPU memory for Vicuna-13B and around 30GB of CPU memory for Vicuna-7B.
+``` python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --device
+cpu ``` ### Metal Backend (Mac computers with Apple silicon or AMD GPUs) Use `-
+-device mps` to enable GPU acceleration on Mac computers and use `--load-8bit`
+to turn on 8-bit compression. ``` python3 -m fastchat.serve.cli --model-name /
+path/to/vicuna/weights --device mps --load-8bit ``` ### Others (Quantization,
+Low-end Devices, and More Platforms) If you do not have enough memory, you can
+enable 8-bit compression by adding `--load-8bit` to commands above. It works
+with CPU, GPU, and Metal. This can reduce the memory usage by around half with
+slightly degraded model quality. ``` python3 -m fastchat.serve.cli --model-name
+/path/to/vicuna/weights --load-8bit ``` Besides, we are actively exploring more
+methods to make the model easier to run on more platforms. Contributions and
+pull requests are welcome. ## Serving with Web GUI ### Launch a controller
 ```bash python3 -m fastchat.serve.controller ``` ### Launch a model worker
 ```bash python3 -m fastchat.serve.model_worker --model-path /path/to/vicuna/
 weights ``` Wait until the process finishes loading the model and you see
 "Uvicorn running on ...". ### Send a test message ```bash python3 -
 m fastchat.serve.test_message --model-name vicuna-13b ``` ### Launch a gradio
 web server. ```bash python3 -m fastchat.serve.gradio_web_server ``` ### You can
 open your browser and chat with a model now. ## Evaluation Our AI-enhanced
```

### Comparing `fschat-0.1.6/README.md` & `fschat-0.1.7/README.md`

 * *Files 5% similar despite different names*

```diff
@@ -48,15 +48,15 @@
 ```
 
 ## Vicuna Weights
 We release [Vicuna](https://vicuna.lmsys.org/) weights as delta weights to comply with the LLaMA model license.
 You can add our delta to the original LLaMA weights to obtain the Vicuna weights. Instructions:
 
 1. Get the original LLaMA weights in the huggingface format by following the instructions [here](https://huggingface.co/docs/transformers/main/model_doc/llama).
-2. Use the following scripts to get Vicuna weights by applying our delta. It will automatically download delta weights from our Hugging Face account.
+2. Use the following scripts to get Vicuna weights by applying our delta. They will automatically download delta weights from our Hugging Face account.
 
 **NOTE**:
 Our released weights are only compatible with the latest main branch of huggingface/transformers.
 We install the correct version of transformers when fastchat is installed.
 
 ### Vicuna-13B
 This conversion command needs around 60 GB of CPU RAM.
@@ -64,47 +64,52 @@
 python3 -m fastchat.model.apply_delta \
     --base /path/to/llama-13b \
     --target /output/path/to/vicuna-13b \
     --delta lmsys/vicuna-13b-delta-v0
 ```
 
 ### Vicuna-7B
-Coming soon.
+This conversion command needs around 30 GB of CPU RAM.
+```bash
+python3 -m fastchat.model.apply_delta \
+    --base /path/to/llama-7b \
+    --target /output/path/to/vicuna-7b \
+    --delta lmsys/vicuna-7b-delta-v0
+```
 
 ## Inference with Command Line Interface
 
 ### Single GPU
-The command below requires around 28GB of GPU memory for Vicuna-13B.
+The command below requires around 28GB of GPU memory for Vicuna-13B and 14GB of GPU memory for Vicuna-7B.
 ```
 python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights
 ```
 
 ### Multiple GPUs
 If you do not have enough GPU memory, you can use model parallelism to aggregate memory from multiple GPUs on the same machine.
 ```
 python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --num-gpus 2
 ```
 
 ### CPU Only
-This runs on the CPU only and does not require GPU. It requires around 60GB of CPU memory for Vicuna-13B.
+This runs on the CPU only and does not require GPU. It requires around 60GB of CPU memory for Vicuna-13B and around 30GB of CPU memory for Vicuna-7B.
 ```
 python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --device cpu
 ```
 
 ### Metal Backend (Mac computers with Apple silicon or AMD GPUs)
+Use `--device mps` to enable GPU acceleration on Mac computers and use `--load-8bit` to turn on 8-bit compression.
 ```
-python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --device mps
+python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --device mps --load-8bit
 ```
 
 ### Others (Quantization, Low-end Devices, and More Platforms)
-
-You can load in 8-bit mode to reduce GPU memory usage with slightly degraded model quality.
-It is tested on a single 4090 and requires around 18GB of GPU memory for Vicuna-13B.
-Note that this mode only works on a single GPU.
-You are also required to install `bitsandbytes` according to the printed messages.
+If you do not have enough memory, you can enable 8-bit compression by adding `--load-8bit` to commands above.
+It works with CPU, GPU, and Metal.
+This can reduce the memory usage by around half with slightly degraded model quality.
 
 ```
 python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --load-8bit
 ```
 
 Besides, we are actively exploring more methods to make the model easier to run on more platforms.
 Contributions and pull requests are welcome.
```

#### html2text {}

```diff
@@ -17,40 +17,44 @@
 Install Package ```bash pip3 install --upgrade pip # enable PEP 660 support
 pip3 install -e . ``` ## Vicuna Weights We release [Vicuna](https://
 vicuna.lmsys.org/) weights as delta weights to comply with the LLaMA model
 license. You can add our delta to the original LLaMA weights to obtain the
 Vicuna weights. Instructions: 1. Get the original LLaMA weights in the
 huggingface format by following the instructions [here](https://huggingface.co/
 docs/transformers/main/model_doc/llama). 2. Use the following scripts to get
-Vicuna weights by applying our delta. It will automatically download delta
+Vicuna weights by applying our delta. They will automatically download delta
 weights from our Hugging Face account. **NOTE**: Our released weights are only
 compatible with the latest main branch of huggingface/transformers. We install
 the correct version of transformers when fastchat is installed. ### Vicuna-13B
 This conversion command needs around 60 GB of CPU RAM. ```bash python3 -
 m fastchat.model.apply_delta \ --base /path/to/llama-13b \ --target /output/
-path/to/vicuna-13b \ --delta lmsys/vicuna-13b-delta-v0 ``` ### Vicuna-7B Coming
-soon. ## Inference with Command Line Interface ### Single GPU The command below
-requires around 28GB of GPU memory for Vicuna-13B. ``` python3 -
+path/to/vicuna-13b \ --delta lmsys/vicuna-13b-delta-v0 ``` ### Vicuna-7B This
+conversion command needs around 30 GB of CPU RAM. ```bash python3 -
+m fastchat.model.apply_delta \ --base /path/to/llama-7b \ --target /output/
+path/to/vicuna-7b \ --delta lmsys/vicuna-7b-delta-v0 ``` ## Inference with
+Command Line Interface ### Single GPU The command below requires around 28GB of
+GPU memory for Vicuna-13B and 14GB of GPU memory for Vicuna-7B. ``` python3 -
 m fastchat.serve.cli --model-name /path/to/vicuna/weights ``` ### Multiple GPUs
 If you do not have enough GPU memory, you can use model parallelism to
 aggregate memory from multiple GPUs on the same machine. ``` python3 -
 m fastchat.serve.cli --model-name /path/to/vicuna/weights --num-gpus 2 ``` ###
 CPU Only This runs on the CPU only and does not require GPU. It requires around
-60GB of CPU memory for Vicuna-13B. ``` python3 -m fastchat.serve.cli --model-
-name /path/to/vicuna/weights --device cpu ``` ### Metal Backend (Mac computers
-with Apple silicon or AMD GPUs) ``` python3 -m fastchat.serve.cli --model-name
-/path/to/vicuna/weights --device mps ``` ### Others (Quantization, Low-end
-Devices, and More Platforms) You can load in 8-bit mode to reduce GPU memory
-usage with slightly degraded model quality. It is tested on a single 4090 and
-requires around 18GB of GPU memory for Vicuna-13B. Note that this mode only
-works on a single GPU. You are also required to install `bitsandbytes`
-according to the printed messages. ``` python3 -m fastchat.serve.cli --model-
-name /path/to/vicuna/weights --load-8bit ``` Besides, we are actively exploring
-more methods to make the model easier to run on more platforms. Contributions
-and pull requests are welcome. ## Serving with Web GUI ### Launch a controller
+60GB of CPU memory for Vicuna-13B and around 30GB of CPU memory for Vicuna-7B.
+``` python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --device
+cpu ``` ### Metal Backend (Mac computers with Apple silicon or AMD GPUs) Use `-
+-device mps` to enable GPU acceleration on Mac computers and use `--load-8bit`
+to turn on 8-bit compression. ``` python3 -m fastchat.serve.cli --model-name /
+path/to/vicuna/weights --device mps --load-8bit ``` ### Others (Quantization,
+Low-end Devices, and More Platforms) If you do not have enough memory, you can
+enable 8-bit compression by adding `--load-8bit` to commands above. It works
+with CPU, GPU, and Metal. This can reduce the memory usage by around half with
+slightly degraded model quality. ``` python3 -m fastchat.serve.cli --model-name
+/path/to/vicuna/weights --load-8bit ``` Besides, we are actively exploring more
+methods to make the model easier to run on more platforms. Contributions and
+pull requests are welcome. ## Serving with Web GUI ### Launch a controller
 ```bash python3 -m fastchat.serve.controller ``` ### Launch a model worker
 ```bash python3 -m fastchat.serve.model_worker --model-path /path/to/vicuna/
 weights ``` Wait until the process finishes loading the model and you see
 "Uvicorn running on ...". ### Send a test message ```bash python3 -
 m fastchat.serve.test_message --model-name vicuna-13b ``` ### Launch a gradio
 web server. ```bash python3 -m fastchat.serve.gradio_web_server ``` ### You can
 open your browser and chat with a model now. ## Evaluation Our AI-enhanced
```

### Comparing `fschat-0.1.6/fastchat/conversation.py` & `fschat-0.1.7/fastchat/conversation.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/data/alpaca-converter.py` & `fschat-0.1.7/fastchat/data/alpaca-converter.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/data/clean_sharegpt.py` & `fschat-0.1.7/fastchat/data/clean_sharegpt.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/data/inspect.py` & `fschat-0.1.7/fastchat/data/inspect.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/data/optional_clean.py` & `fschat-0.1.7/fastchat/data/optional_clean.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/data/split_long_conversation.py` & `fschat-0.1.7/fastchat/data/split_long_conversation.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/eval/eval_gpt_review.py` & `fschat-0.1.7/fastchat/eval/eval_gpt_review.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/eval/generate_webpage_data_from_table.py` & `fschat-0.1.7/fastchat/eval/generate_webpage_data_from_table.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/eval/get_model_answer.py` & `fschat-0.1.7/fastchat/eval/get_model_answer.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/eval/qa_baseline_gpt35.py` & `fschat-0.1.7/fastchat/eval/qa_baseline_gpt35.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/model/apply_delta.py` & `fschat-0.1.7/fastchat/model/apply_delta.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/model/make_delta.py` & `fschat-0.1.7/fastchat/model/make_delta.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/serve/cli.py` & `fschat-0.1.7/fastchat/serve/cli.py`

 * *Files 5% similar despite different names*

```diff
@@ -5,14 +5,15 @@
 import argparse
 import time
 
 import torch
 from transformers import AutoTokenizer, AutoModelForCausalLM, LlamaTokenizer
 
 from fastchat.conversation import conv_templates, SeparatorStyle
+from fastchat.serve.compression import compress_module
 from fastchat.serve.monkey_patch_non_inplace import replace_llama_attn_with_non_inplace_operations
 
 
 def load_model(model_name, device, num_gpus, load_8bit=False):
     if device == "cpu":
         kwargs = {}
     elif device == "cuda":
@@ -28,30 +29,36 @@
                 num_gpus = int(num_gpus)
                 if num_gpus != 1:
                     kwargs.update({
                         "device_map": "auto",
                         "max_memory": {i: "13GiB" for i in range(num_gpus)},
                     })
     elif device == "mps":
-        # Avoid bugs in mps backend by not using in-place operations.
         kwargs = {"torch_dtype": torch.float16}
+        # Avoid bugs in mps backend by not using in-place operations.
         replace_llama_attn_with_non_inplace_operations()
     else:
         raise ValueError(f"Invalid device: {device}")
 
     tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
     model = AutoModelForCausalLM.from_pretrained(model_name,
         low_cpu_mem_usage=True, **kwargs)
 
     # calling model.cuda() mess up weights if loading 8-bit weights
     if device == "cuda" and num_gpus == 1 and not load_8bit:
         model.to("cuda")
     elif device == "mps":
         model.to("mps")
 
+    if (device == "mps" or device == "cpu") and load_8bit:
+        compress_module(model)
+
+    if args.debug:
+        print(model)
+
     return model, tokenizer
 
 
 @torch.inference_mode()
 def generate_stream(tokenizer, model, params, device,
                     context_len=2048, stream_interval=2):
     """Adapted from fastchat/serve/model_worker.py::generate_stream"""
```

### Comparing `fschat-0.1.6/fastchat/serve/controller.py` & `fschat-0.1.7/fastchat/serve/controller.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/serve/gradio_css.py` & `fschat-0.1.7/fastchat/serve/gradio_css.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/serve/gradio_patch.py` & `fschat-0.1.7/fastchat/serve/gradio_patch.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/serve/gradio_web_server.py` & `fschat-0.1.7/fastchat/serve/gradio_web_server.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/serve/model_worker.py` & `fschat-0.1.7/fastchat/serve/model_worker.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/serve/monkey_patch_non_inplace.py` & `fschat-0.1.7/fastchat/serve/monkey_patch_non_inplace.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/serve/register_worker.py` & `fschat-0.1.7/fastchat/serve/register_worker.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/serve/test_message.py` & `fschat-0.1.7/fastchat/serve/test_message.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/train/llama_flash_attn_monkey_patch.py` & `fschat-0.1.7/fastchat/train/llama_flash_attn_monkey_patch.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/train/train.py` & `fschat-0.1.7/fastchat/train/train.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/train/train_lora.py` & `fschat-0.1.7/fastchat/train/train_lora.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fastchat/utils.py` & `fschat-0.1.7/fastchat/utils.py`

 * *Files identical despite different names*

### Comparing `fschat-0.1.6/fschat.egg-info/PKG-INFO` & `fschat-0.1.7/fschat.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fschat
-Version: 0.1.6
+Version: 0.1.7
 Summary: An open platform for training, serving, and evaluating large language model based chatbots.
 Project-URL: Homepage, https://github.com/lm-sys/fastchat
 Project-URL: Bug Tracker, https://github.com/lm-sys/fastchat/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
@@ -60,15 +60,15 @@
 ```
 
 ## Vicuna Weights
 We release [Vicuna](https://vicuna.lmsys.org/) weights as delta weights to comply with the LLaMA model license.
 You can add our delta to the original LLaMA weights to obtain the Vicuna weights. Instructions:
 
 1. Get the original LLaMA weights in the huggingface format by following the instructions [here](https://huggingface.co/docs/transformers/main/model_doc/llama).
-2. Use the following scripts to get Vicuna weights by applying our delta. It will automatically download delta weights from our Hugging Face account.
+2. Use the following scripts to get Vicuna weights by applying our delta. They will automatically download delta weights from our Hugging Face account.
 
 **NOTE**:
 Our released weights are only compatible with the latest main branch of huggingface/transformers.
 We install the correct version of transformers when fastchat is installed.
 
 ### Vicuna-13B
 This conversion command needs around 60 GB of CPU RAM.
@@ -76,47 +76,52 @@
 python3 -m fastchat.model.apply_delta \
     --base /path/to/llama-13b \
     --target /output/path/to/vicuna-13b \
     --delta lmsys/vicuna-13b-delta-v0
 ```
 
 ### Vicuna-7B
-Coming soon.
+This conversion command needs around 30 GB of CPU RAM.
+```bash
+python3 -m fastchat.model.apply_delta \
+    --base /path/to/llama-7b \
+    --target /output/path/to/vicuna-7b \
+    --delta lmsys/vicuna-7b-delta-v0
+```
 
 ## Inference with Command Line Interface
 
 ### Single GPU
-The command below requires around 28GB of GPU memory for Vicuna-13B.
+The command below requires around 28GB of GPU memory for Vicuna-13B and 14GB of GPU memory for Vicuna-7B.
 ```
 python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights
 ```
 
 ### Multiple GPUs
 If you do not have enough GPU memory, you can use model parallelism to aggregate memory from multiple GPUs on the same machine.
 ```
 python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --num-gpus 2
 ```
 
 ### CPU Only
-This runs on the CPU only and does not require GPU. It requires around 60GB of CPU memory for Vicuna-13B.
+This runs on the CPU only and does not require GPU. It requires around 60GB of CPU memory for Vicuna-13B and around 30GB of CPU memory for Vicuna-7B.
 ```
 python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --device cpu
 ```
 
 ### Metal Backend (Mac computers with Apple silicon or AMD GPUs)
+Use `--device mps` to enable GPU acceleration on Mac computers and use `--load-8bit` to turn on 8-bit compression.
 ```
-python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --device mps
+python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --device mps --load-8bit
 ```
 
 ### Others (Quantization, Low-end Devices, and More Platforms)
-
-You can load in 8-bit mode to reduce GPU memory usage with slightly degraded model quality.
-It is tested on a single 4090 and requires around 18GB of GPU memory for Vicuna-13B.
-Note that this mode only works on a single GPU.
-You are also required to install `bitsandbytes` according to the printed messages.
+If you do not have enough memory, you can enable 8-bit compression by adding `--load-8bit` to commands above.
+It works with CPU, GPU, and Metal.
+This can reduce the memory usage by around half with slightly degraded model quality.
 
 ```
 python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --load-8bit
 ```
 
 Besides, we are actively exploring more methods to make the model easier to run on more platforms.
 Contributions and pull requests are welcome.
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: fschat Version: 0.1.6 Summary: An open platform for
+Metadata-Version: 2.1 Name: fschat Version: 0.1.7 Summary: An open platform for
 training, serving, and evaluating large language model based chatbots. Project-
 URL: Homepage, https://github.com/lm-sys/fastchat Project-URL: Bug Tracker,
 https://github.com/lm-sys/fastchat/issues Classifier: Programming Language ::
 Python :: 3 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Python: >=3.8 Description-Content-Type: text/markdown License-File:
 LICENSE # FastChat An open platform for training, serving, and evaluating large
 language model based chatbots. ## Release
@@ -23,40 +23,44 @@
 Install Package ```bash pip3 install --upgrade pip # enable PEP 660 support
 pip3 install -e . ``` ## Vicuna Weights We release [Vicuna](https://
 vicuna.lmsys.org/) weights as delta weights to comply with the LLaMA model
 license. You can add our delta to the original LLaMA weights to obtain the
 Vicuna weights. Instructions: 1. Get the original LLaMA weights in the
 huggingface format by following the instructions [here](https://huggingface.co/
 docs/transformers/main/model_doc/llama). 2. Use the following scripts to get
-Vicuna weights by applying our delta. It will automatically download delta
+Vicuna weights by applying our delta. They will automatically download delta
 weights from our Hugging Face account. **NOTE**: Our released weights are only
 compatible with the latest main branch of huggingface/transformers. We install
 the correct version of transformers when fastchat is installed. ### Vicuna-13B
 This conversion command needs around 60 GB of CPU RAM. ```bash python3 -
 m fastchat.model.apply_delta \ --base /path/to/llama-13b \ --target /output/
-path/to/vicuna-13b \ --delta lmsys/vicuna-13b-delta-v0 ``` ### Vicuna-7B Coming
-soon. ## Inference with Command Line Interface ### Single GPU The command below
-requires around 28GB of GPU memory for Vicuna-13B. ``` python3 -
+path/to/vicuna-13b \ --delta lmsys/vicuna-13b-delta-v0 ``` ### Vicuna-7B This
+conversion command needs around 30 GB of CPU RAM. ```bash python3 -
+m fastchat.model.apply_delta \ --base /path/to/llama-7b \ --target /output/
+path/to/vicuna-7b \ --delta lmsys/vicuna-7b-delta-v0 ``` ## Inference with
+Command Line Interface ### Single GPU The command below requires around 28GB of
+GPU memory for Vicuna-13B and 14GB of GPU memory for Vicuna-7B. ``` python3 -
 m fastchat.serve.cli --model-name /path/to/vicuna/weights ``` ### Multiple GPUs
 If you do not have enough GPU memory, you can use model parallelism to
 aggregate memory from multiple GPUs on the same machine. ``` python3 -
 m fastchat.serve.cli --model-name /path/to/vicuna/weights --num-gpus 2 ``` ###
 CPU Only This runs on the CPU only and does not require GPU. It requires around
-60GB of CPU memory for Vicuna-13B. ``` python3 -m fastchat.serve.cli --model-
-name /path/to/vicuna/weights --device cpu ``` ### Metal Backend (Mac computers
-with Apple silicon or AMD GPUs) ``` python3 -m fastchat.serve.cli --model-name
-/path/to/vicuna/weights --device mps ``` ### Others (Quantization, Low-end
-Devices, and More Platforms) You can load in 8-bit mode to reduce GPU memory
-usage with slightly degraded model quality. It is tested on a single 4090 and
-requires around 18GB of GPU memory for Vicuna-13B. Note that this mode only
-works on a single GPU. You are also required to install `bitsandbytes`
-according to the printed messages. ``` python3 -m fastchat.serve.cli --model-
-name /path/to/vicuna/weights --load-8bit ``` Besides, we are actively exploring
-more methods to make the model easier to run on more platforms. Contributions
-and pull requests are welcome. ## Serving with Web GUI ### Launch a controller
+60GB of CPU memory for Vicuna-13B and around 30GB of CPU memory for Vicuna-7B.
+``` python3 -m fastchat.serve.cli --model-name /path/to/vicuna/weights --device
+cpu ``` ### Metal Backend (Mac computers with Apple silicon or AMD GPUs) Use `-
+-device mps` to enable GPU acceleration on Mac computers and use `--load-8bit`
+to turn on 8-bit compression. ``` python3 -m fastchat.serve.cli --model-name /
+path/to/vicuna/weights --device mps --load-8bit ``` ### Others (Quantization,
+Low-end Devices, and More Platforms) If you do not have enough memory, you can
+enable 8-bit compression by adding `--load-8bit` to commands above. It works
+with CPU, GPU, and Metal. This can reduce the memory usage by around half with
+slightly degraded model quality. ``` python3 -m fastchat.serve.cli --model-name
+/path/to/vicuna/weights --load-8bit ``` Besides, we are actively exploring more
+methods to make the model easier to run on more platforms. Contributions and
+pull requests are welcome. ## Serving with Web GUI ### Launch a controller
 ```bash python3 -m fastchat.serve.controller ``` ### Launch a model worker
 ```bash python3 -m fastchat.serve.model_worker --model-path /path/to/vicuna/
 weights ``` Wait until the process finishes loading the model and you see
 "Uvicorn running on ...". ### Send a test message ```bash python3 -
 m fastchat.serve.test_message --model-name vicuna-13b ``` ### Launch a gradio
 web server. ```bash python3 -m fastchat.serve.gradio_web_server ``` ### You can
 open your browser and chat with a model now. ## Evaluation Our AI-enhanced
```

### Comparing `fschat-0.1.6/fschat.egg-info/SOURCES.txt` & `fschat-0.1.7/fschat.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -17,14 +17,15 @@
 fastchat/eval/get_model_answer.py
 fastchat/eval/qa_baseline_gpt35.py
 fastchat/model/__init__.py
 fastchat/model/apply_delta.py
 fastchat/model/make_delta.py
 fastchat/serve/__init__.py
 fastchat/serve/cli.py
+fastchat/serve/compression.py
 fastchat/serve/controller.py
 fastchat/serve/gradio_css.py
 fastchat/serve/gradio_patch.py
 fastchat/serve/gradio_web_server.py
 fastchat/serve/model_worker.py
 fastchat/serve/monkey_patch_non_inplace.py
 fastchat/serve/register_worker.py
```

### Comparing `fschat-0.1.6/pyproject.toml` & `fschat-0.1.7/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "fschat"
-version = "0.1.6"
+version = "0.1.7"
 description = "An open platform for training, serving, and evaluating large language model based chatbots."
 readme = "README.md"
 requires-python = ">=3.8"
 classifiers = [
     "Programming Language :: Python :: 3",
     "License :: OSI Approved :: Apache Software License",
 ]
```

