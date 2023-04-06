# Comparing `tmp/lmft-0.2.2.tar.gz` & `tmp/lmft-0.2.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lmft-0.2.2.tar", last modified: Mon Mar 27 13:40:41 2023, max compression
+gzip compressed data, was "lmft-0.2.5.tar", last modified: Thu Apr  6 12:51:39 2023, max compression
```

## Comparing `lmft-0.2.2.tar` & `lmft-0.2.5.tar`

### file list

```diff
@@ -1,26 +1,24 @@
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-03-27 13:40:41.519450 lmft-0.2.2/
--rw-r--r--   0 xuming     (501) staff       (20)    11357 2023-03-23 12:46:21.000000 lmft-0.2.2/LICENSE
--rw-r--r--   0 xuming     (501) staff       (20)     7917 2023-03-27 13:40:41.518949 lmft-0.2.2/PKG-INFO
--rw-r--r--   0 xuming     (501) staff       (20)     5698 2023-03-27 10:15:39.000000 lmft-0.2.2/README.md
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-03-27 13:40:41.514282 lmft-0.2.2/lmft/
--rw-r--r--   0 xuming     (501) staff       (20)      123 2023-03-26 06:46:31.000000 lmft-0.2.2/lmft/__init__.py
--rw-r--r--   0 xuming     (501) staff       (20)    20590 2023-03-27 13:36:50.000000 lmft-0.2.2/lmft/chatglm_model.py
--rw-r--r--   0 xuming     (501) staff       (20)    59426 2023-03-27 09:55:04.000000 lmft-0.2.2/lmft/chatglm_utils.py
--rw-r--r--   0 xuming     (501) staff       (20)     5720 2023-03-25 12:04:51.000000 lmft-0.2.2/lmft/clm_finetune_peft_gptneo_imdb.py
--rw-r--r--   0 xuming     (501) staff       (20)     7968 2023-03-25 05:40:49.000000 lmft-0.2.2/lmft/gpt2-sentiment.py
--rw-r--r--   0 xuming     (501) staff       (20)     9847 2023-03-26 01:40:05.000000 lmft-0.2.2/lmft/gpt2-sentiment_peft.py
--rw-r--r--   0 xuming     (501) staff       (20)    10995 2023-03-25 03:10:52.000000 lmft-0.2.2/lmft/gpt2_sentiment.py
--rw-r--r--   0 xuming     (501) staff       (20)     9959 2023-03-25 12:07:56.000000 lmft-0.2.2/lmft/gpt_neox_sentiment_trl_peft.py
--rw-r--r--   0 xuming     (501) staff       (20)      503 2023-03-26 13:46:10.000000 lmft-0.2.2/lmft/lmft.py
--rw-r--r--   0 xuming     (501) staff       (20)    28802 2023-03-27 09:55:04.000000 lmft-0.2.2/lmft/quantization.py
--rw-r--r--   0 xuming     (501) staff       (20)     6986 2023-03-25 05:40:49.000000 lmft-0.2.2/lmft/t5-sentiment.py
--rw-r--r--   0 xuming     (501) staff       (20)       84 2023-03-27 13:40:10.000000 lmft-0.2.2/lmft/version.py
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-03-27 13:40:41.518331 lmft-0.2.2/lmft.egg-info/
--rw-r--r--   0 xuming     (501) staff       (20)     7917 2023-03-27 13:40:41.000000 lmft-0.2.2/lmft.egg-info/PKG-INFO
--rw-r--r--   0 xuming     (501) staff       (20)      472 2023-03-27 13:40:41.000000 lmft-0.2.2/lmft.egg-info/SOURCES.txt
--rw-r--r--   0 xuming     (501) staff       (20)        1 2023-03-27 13:40:41.000000 lmft-0.2.2/lmft.egg-info/dependency_links.txt
--rw-r--r--   0 xuming     (501) staff       (20)        1 2023-03-23 14:03:16.000000 lmft-0.2.2/lmft.egg-info/not-zip-safe
--rw-r--r--   0 xuming     (501) staff       (20)       85 2023-03-27 13:40:41.000000 lmft-0.2.2/lmft.egg-info/requires.txt
--rw-r--r--   0 xuming     (501) staff       (20)        5 2023-03-27 13:40:41.000000 lmft-0.2.2/lmft.egg-info/top_level.txt
--rw-r--r--   0 xuming     (501) staff       (20)       38 2023-03-27 13:40:41.519649 lmft-0.2.2/setup.cfg
--rw-r--r--   0 xuming     (501) staff       (20)     2529 2023-03-25 12:56:12.000000 lmft-0.2.2/setup.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-06 12:51:39.965119 lmft-0.2.5/
+-rw-r--r--   0 xuming     (501) staff       (20)    11357 2023-03-23 12:46:21.000000 lmft-0.2.5/LICENSE
+-rw-r--r--   0 xuming     (501) staff       (20)     9898 2023-04-06 12:51:39.964682 lmft-0.2.5/PKG-INFO
+-rw-r--r--   0 xuming     (501) staff       (20)     7463 2023-04-06 09:53:56.000000 lmft-0.2.5/README.md
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-06 12:51:39.960976 lmft-0.2.5/lmft/
+-rw-r--r--   0 xuming     (501) staff       (20)      124 2023-04-06 09:39:26.000000 lmft-0.2.5/lmft/__init__.py
+-rw-r--r--   0 xuming     (501) staff       (20)    19758 2023-04-06 12:49:39.000000 lmft-0.2.5/lmft/chatglm_model.py
+-rw-r--r--   0 xuming     (501) staff       (20)     9909 2023-04-06 12:25:59.000000 lmft-0.2.5/lmft/chatglm_utils.py
+-rw-r--r--   0 xuming     (501) staff       (20)     7968 2023-03-25 05:40:49.000000 lmft-0.2.5/lmft/gpt2-sentiment.py
+-rw-r--r--   0 xuming     (501) staff       (20)     9847 2023-03-26 01:40:05.000000 lmft-0.2.5/lmft/gpt2-sentiment_peft.py
+-rw-r--r--   0 xuming     (501) staff       (20)    10995 2023-03-25 03:10:52.000000 lmft-0.2.5/lmft/gpt2_sentiment.py
+-rw-r--r--   0 xuming     (501) staff       (20)     9959 2023-03-25 12:07:56.000000 lmft-0.2.5/lmft/gpt_neox_sentiment_trl_peft.py
+-rw-r--r--   0 xuming     (501) staff       (20)      503 2023-03-26 13:46:10.000000 lmft-0.2.5/lmft/lmft.py
+-rw-r--r--   0 xuming     (501) staff       (20)     6986 2023-03-25 05:40:49.000000 lmft-0.2.5/lmft/t5-sentiment.py
+-rw-r--r--   0 xuming     (501) staff       (20)       84 2023-04-06 12:50:46.000000 lmft-0.2.5/lmft/version.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-06 12:51:39.964050 lmft-0.2.5/lmft.egg-info/
+-rw-r--r--   0 xuming     (501) staff       (20)     9898 2023-04-06 12:51:39.000000 lmft-0.2.5/lmft.egg-info/PKG-INFO
+-rw-r--r--   0 xuming     (501) staff       (20)      413 2023-04-06 12:51:39.000000 lmft-0.2.5/lmft.egg-info/SOURCES.txt
+-rw-r--r--   0 xuming     (501) staff       (20)        1 2023-04-06 12:51:39.000000 lmft-0.2.5/lmft.egg-info/dependency_links.txt
+-rw-r--r--   0 xuming     (501) staff       (20)        1 2023-03-23 14:03:16.000000 lmft-0.2.5/lmft.egg-info/not-zip-safe
+-rw-r--r--   0 xuming     (501) staff       (20)       94 2023-04-06 12:51:39.000000 lmft-0.2.5/lmft.egg-info/requires.txt
+-rw-r--r--   0 xuming     (501) staff       (20)        5 2023-04-06 12:51:39.000000 lmft-0.2.5/lmft.egg-info/top_level.txt
+-rw-r--r--   0 xuming     (501) staff       (20)       38 2023-04-06 12:51:39.965334 lmft-0.2.5/setup.cfg
+-rw-r--r--   0 xuming     (501) staff       (20)     2538 2023-04-06 12:50:46.000000 lmft-0.2.5/setup.py
```

### Comparing `lmft-0.2.2/LICENSE` & `lmft-0.2.5/LICENSE`

 * *Files identical despite different names*

### Comparing `lmft-0.2.2/PKG-INFO` & `lmft-0.2.5/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lmft
-Version: 0.2.2
+Version: 0.2.5
 Summary: Language Model Fine-tuning Toolkit (LMFT)
 Home-page: https://github.com/shibing624/lmft
 Author: XuMing
 Author-email: xuming624@qq.com
 License: Apache License 2.0
 Description: [![PyPI version](https://badge.fury.io/py/lmft.svg)](https://badge.fury.io/py/lmft)
         [![Downloads](https://pepy.tech/badge/lmft)](https://pepy.tech/project/lmft)
@@ -15,15 +15,15 @@
         [![GitHub issues](https://img.shields.io/github/issues/shibing624/lmft.svg)](https://github.com/shibing624/lmft/issues)
         [![Wechat Group](http://vlog.sfyc.ltd/wechat_everyday/wxgroup_logo.png?imageView2/0/w/60/h/20)](#Contact)
         
         # LMFT: Language Model Fine-Tuning
         Language Model Fine-Tuning, for ChatGLM, BELLE, LLaMA fine-tuning.
         
         
-        **lmft**实现了ChatGLM-6B的模型finetune。
+        **lmft**实现了ChatGLM-6B的模型FineTune。
         
         
         **Guide**
         - [Feature](#Feature)
         - [Evaluation](#Evaluation)
         - [Demo](#Demo)
         - [Install](#install)
@@ -32,23 +32,22 @@
         - [Reference](#reference)
         
         
         # Feature
         ### ChatGLM
         #### [THUDM/chatglm-6b](https://huggingface.co/THUDM/chatglm-6b) 模型的Finetune训练
         
-        [THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)放出的默认模型，模型以 FP16 精度加载，模型运行需要 13GB 显存，训练需要 29GB 显存。
-        #### [THUDM/chatglm-6b-int4-qe](https://huggingface.co/THUDM/chatglm-6b-int4-qe) 模型的Finetune训练
-        
-        [THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)放出的int4并对Embedding量化后的模型，模型运行需要 4.3GB 显存，训练需要 8GB 以上显存。
+        [THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)放出的默认模型，模型以 FP16 精度加载，模型运行需要 13GB 显存，训练需要 22GB 显存(batch_size=2)。
         
         
         # Evaluation
         
-        ### 对话生成
+        ### 纠错能力比较
+        
+        ### 对话能力比较
         
         # Demo
         
         HuggingFace Demo: https://huggingface.co/spaces/shibing624/lmft
         
         ![](docs/hf.png)
         
@@ -69,70 +68,96 @@
         
         git clone https://github.com/shibing624/lmft.git
         cd lmft
         pip install --no-deps .
         ```
         
         # Usage
+        ## Use LoRA model
+        release lora model: 
+        1. 中文拼写纠错（CSC）模型 [shibing624/chatglm-6b-csc-zh-lora](https://huggingface.co/shibing624/chatglm-6b-csc-zh-lora)
+        
+        
+        ```python
+        from lmft import ChatGlmModel
+        model = ChatGlmModel("chatglm", "THUDM/chatglm-6b", lora_name="shibing624/chatglm-6b-csc-zh-lora")
+        r = model.predict(["对下面中文拼写纠错：\n少先队员因该为老人让坐。\n答："])
+        print(r) # ['少先队员应该为老人让座。\n错误字：因，坐']
+        ```
         
         ## 训练ChatGLM-6B模型
         
-        example: [examples/train_chatglm_demo.py](examples/train_chatglm_demo.py)
+        支持自定义数据集，数据集格式参考[examples/data/test.tsv](examples/data/test.tsv)。
+        
+        
+        example: [examples/training_chatglm_demo.py](examples/training_chatglm_demo.py)
         
         ```python
         import sys
         
         sys.path.append('..')
-        from lmft import ChatGLMTune
+        from lmft import ChatGlmModel
         
         
         def finetune_demo():
-            m = ChatGLMTune('chatglm', "THUDM/chatglm-6b", args={'use_lora': True})
+            m = ChatGlmModel('chatglm', "THUDM/chatglm-6b", args={'use_lora': True})
             m.train_model(train_data='shibing624/alpaca-zh')
-            r = m.predict(['你是谁', '三原色是啥'])
+            r = m.predict(['给出三个保持健康的秘诀。', '描述原子的结构。'])
             print(r)
             response, history = m.chat("你好", history=[])
             print(response)
             response, history = m.chat("晚上睡不着应该怎么办", history=history)
             print(response)
         
         
         def origin_chat_demo():
-            m = ChatGLMTune('chatglm', "THUDM/chatglm-6b", args={'use_lora': False})
+            m = ChatGlmModel('chatglm', "THUDM/chatglm-6b", args={'use_lora': False})
             response, history = m.chat("你好", history=[])
             print(response)
             response, history = m.chat("晚上睡不着应该怎么办", history=history)
             print(response)
         
         
         if __name__ == '__main__':
             origin_chat_demo()
             finetune_demo()
         ```
         
         output:
         ```
-        问:hi
-        答:hi 
+        问:你好
+        答:你好
         
         [Round 1]
         问:晚上睡不着应该怎么办
         答: 想要在晚上入睡,但并不容易,可以参考下述技巧:
         1. 睡前放松:尝试进行一些放松的活动,如冥想、深呼吸或瑜伽,帮助放松身心,减轻压力和焦虑。
         2. 创造一个舒适的睡眠环境:保持房间安静、黑暗和凉爽,使用舒适的床垫和枕头,确保床铺干净整洁。
         3. 规律的睡眠时间表:保持规律的睡眠时间表,尽可能在同一时间上床,并创造一个固定的起床时间。
         4. 避免刺激性食物和饮料:避免在睡前饮用含咖啡因的饮料,如咖啡、茶和可乐,以及吃辛辣、油腻或难以消化的食物。
         5. 避免过度使用电子设备:避免在睡前使用电子设备,如手机、电视和电脑。这些设备会发出蓝光,干扰睡眠。
         如果尝试了这些技巧仍然无法入睡,建议咨询医生或睡眠专家,获取更专业的建议和帮助。
         ```
         
         
-        #### dataset
-        1. [0.5M生成的中文ChatGPT结果数据](https://huggingface.co/datasets/BelleGroup/generated_train_0.5M_CN)
-        2. [50k English Stanford Alpaca dataset](https://github.com/tatsu-lab/stanford_alpaca#data-release)
+        ## Dataset
+        1. 50万条中文ChatGPT指令数据集：[BelleGroup/train_0.5M_CN](https://huggingface.co/datasets/BelleGroup/train_0.5M_CN)
+        2. 100万条中文ChatGPT指令数据集：[BelleGroup/train_1M_CN](https://huggingface.co/datasets/BelleGroup/train_1M_CN)
+        3. 5万条英文ChatGPT指令数据集：[50k English Stanford Alpaca dataset](https://github.com/tatsu-lab/stanford_alpaca#data-release)
+        4. 2万条中文ChatGPT指令数据集：[shibing624/alpaca-zh](https://huggingface.co/datasets/shibing624/alpaca-zh)
+        5. 69万条中文指令数据集(Belle50万条+Guanaco19万条)：[Chinese-Vicuna/guanaco_belle_merge_v1.0](https://huggingface.co/datasets/Chinese-Vicuna/guanaco_belle_merge_v1.0)
+        
+        ## FAQ
+        1. 问：为啥没有`int4`量化模型的Finetune训练？
+        
+        答：THUDM放出了2个int4量化模型，分别是 [THUDM/chatglm-6b-int4](https://huggingface.co/THUDM/chatglm-6b-int4) 和 
+        [THUDM/chatglm-6b-int4-qe](https://huggingface.co/THUDM/chatglm-6b-int4-qe) 模型，是基于
+        [THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) 的int4并对Embedding量化后的模型，模型运行仅需要 4.3GB 显存。
+        
+        训练方法参考官方给出的[P-tuning方法](https://github.com/THUDM/ChatGLM-6B/blob/main/ptuning/README.md)，INT4 量化模型的训练最低只需 6.7G 显存。
         
         
         # Contact
         
         - Issue(建议)：[![GitHub issues](https://img.shields.io/github/issues/shibing624/lmft.svg)](https://github.com/shibing624/lmft/issues)
         - 邮件我：xuming: xuming624@qq.com
         - 微信我：加我*微信号：xuming624, 备注：姓名-公司-NLP* 进NLP交流群。
@@ -160,16 +185,18 @@
           howpublished = {\url{https://github.com/shibing624/lmft}},
         }
         ```
         
         # License
         
         
-        授权协议为 [The Apache License 2.0](LICENSE)，可免费用做商业用途。请在产品说明中附加lmft的链接和授权协议。
+        lmft授权协议为 [The Apache License 2.0](LICENSE)，可免费用做商业用途。请在产品说明中附加lmft的链接和授权协议。
         
+        - ChatGLM-6B的模型权重仅限学术研究用，具体见[MODEL_LICENSE](https://github.com/THUDM/ChatGLM-6B/blob/main/MODEL_LICENSE)
+        - LLAMA的模型权重仅限学术研究用，具体见[LICENSE](https://huggingface.co/decapoda-research/llama-13b-hf/blob/main/LICENSE)
         
         # Contribute
         项目代码还很粗糙，如果大家对代码有所改进，欢迎提交回本项目，在提交之前，注意以下两点：
         
          - 在`tests`添加相应的单元测试
          - 使用`python -m pytest -v`来运行所有单元测试，确保所有单测都是通过的
```

### Comparing `lmft-0.2.2/README.md` & `lmft-0.2.5/README.md`

 * *Files 17% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 [![GitHub issues](https://img.shields.io/github/issues/shibing624/lmft.svg)](https://github.com/shibing624/lmft/issues)
 [![Wechat Group](http://vlog.sfyc.ltd/wechat_everyday/wxgroup_logo.png?imageView2/0/w/60/h/20)](#Contact)
 
 # LMFT: Language Model Fine-Tuning
 Language Model Fine-Tuning, for ChatGLM, BELLE, LLaMA fine-tuning.
 
 
-**lmft**实现了ChatGLM-6B的模型finetune。
+**lmft**实现了ChatGLM-6B的模型FineTune。
 
 
 **Guide**
 - [Feature](#Feature)
 - [Evaluation](#Evaluation)
 - [Demo](#Demo)
 - [Install](#install)
@@ -24,23 +24,22 @@
 - [Reference](#reference)
 
 
 # Feature
 ### ChatGLM
 #### [THUDM/chatglm-6b](https://huggingface.co/THUDM/chatglm-6b) 模型的Finetune训练
 
-[THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)放出的默认模型，模型以 FP16 精度加载，模型运行需要 13GB 显存，训练需要 29GB 显存。
-#### [THUDM/chatglm-6b-int4-qe](https://huggingface.co/THUDM/chatglm-6b-int4-qe) 模型的Finetune训练
-
-[THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)放出的int4并对Embedding量化后的模型，模型运行需要 4.3GB 显存，训练需要 8GB 以上显存。
+[THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)放出的默认模型，模型以 FP16 精度加载，模型运行需要 13GB 显存，训练需要 22GB 显存(batch_size=2)。
 
 
 # Evaluation
 
-### 对话生成
+### 纠错能力比较
+
+### 对话能力比较
 
 # Demo
 
 HuggingFace Demo: https://huggingface.co/spaces/shibing624/lmft
 
 ![](docs/hf.png)
 
@@ -61,70 +60,96 @@
 
 git clone https://github.com/shibing624/lmft.git
 cd lmft
 pip install --no-deps .
 ```
 
 # Usage
+## Use LoRA model
+release lora model: 
+1. 中文拼写纠错（CSC）模型 [shibing624/chatglm-6b-csc-zh-lora](https://huggingface.co/shibing624/chatglm-6b-csc-zh-lora)
+
+
+```python
+from lmft import ChatGlmModel
+model = ChatGlmModel("chatglm", "THUDM/chatglm-6b", lora_name="shibing624/chatglm-6b-csc-zh-lora")
+r = model.predict(["对下面中文拼写纠错：\n少先队员因该为老人让坐。\n答："])
+print(r) # ['少先队员应该为老人让座。\n错误字：因，坐']
+```
 
 ## 训练ChatGLM-6B模型
 
-example: [examples/train_chatglm_demo.py](examples/train_chatglm_demo.py)
+支持自定义数据集，数据集格式参考[examples/data/test.tsv](examples/data/test.tsv)。
+
+
+example: [examples/training_chatglm_demo.py](examples/training_chatglm_demo.py)
 
 ```python
 import sys
 
 sys.path.append('..')
-from lmft import ChatGLMTune
+from lmft import ChatGlmModel
 
 
 def finetune_demo():
-    m = ChatGLMTune('chatglm', "THUDM/chatglm-6b", args={'use_lora': True})
+    m = ChatGlmModel('chatglm', "THUDM/chatglm-6b", args={'use_lora': True})
     m.train_model(train_data='shibing624/alpaca-zh')
-    r = m.predict(['你是谁', '三原色是啥'])
+    r = m.predict(['给出三个保持健康的秘诀。', '描述原子的结构。'])
     print(r)
     response, history = m.chat("你好", history=[])
     print(response)
     response, history = m.chat("晚上睡不着应该怎么办", history=history)
     print(response)
 
 
 def origin_chat_demo():
-    m = ChatGLMTune('chatglm', "THUDM/chatglm-6b", args={'use_lora': False})
+    m = ChatGlmModel('chatglm', "THUDM/chatglm-6b", args={'use_lora': False})
     response, history = m.chat("你好", history=[])
     print(response)
     response, history = m.chat("晚上睡不着应该怎么办", history=history)
     print(response)
 
 
 if __name__ == '__main__':
     origin_chat_demo()
     finetune_demo()
 ```
 
 output:
 ```
-问:hi
-答:hi 
+问:你好
+答:你好
 
 [Round 1]
 问:晚上睡不着应该怎么办
 答: 想要在晚上入睡,但并不容易,可以参考下述技巧:
 1. 睡前放松:尝试进行一些放松的活动,如冥想、深呼吸或瑜伽,帮助放松身心,减轻压力和焦虑。
 2. 创造一个舒适的睡眠环境:保持房间安静、黑暗和凉爽,使用舒适的床垫和枕头,确保床铺干净整洁。
 3. 规律的睡眠时间表:保持规律的睡眠时间表,尽可能在同一时间上床,并创造一个固定的起床时间。
 4. 避免刺激性食物和饮料:避免在睡前饮用含咖啡因的饮料,如咖啡、茶和可乐,以及吃辛辣、油腻或难以消化的食物。
 5. 避免过度使用电子设备:避免在睡前使用电子设备,如手机、电视和电脑。这些设备会发出蓝光,干扰睡眠。
 如果尝试了这些技巧仍然无法入睡,建议咨询医生或睡眠专家,获取更专业的建议和帮助。
 ```
 
 
-#### dataset
-1. [0.5M生成的中文ChatGPT结果数据](https://huggingface.co/datasets/BelleGroup/generated_train_0.5M_CN)
-2. [50k English Stanford Alpaca dataset](https://github.com/tatsu-lab/stanford_alpaca#data-release)
+## Dataset
+1. 50万条中文ChatGPT指令数据集：[BelleGroup/train_0.5M_CN](https://huggingface.co/datasets/BelleGroup/train_0.5M_CN)
+2. 100万条中文ChatGPT指令数据集：[BelleGroup/train_1M_CN](https://huggingface.co/datasets/BelleGroup/train_1M_CN)
+3. 5万条英文ChatGPT指令数据集：[50k English Stanford Alpaca dataset](https://github.com/tatsu-lab/stanford_alpaca#data-release)
+4. 2万条中文ChatGPT指令数据集：[shibing624/alpaca-zh](https://huggingface.co/datasets/shibing624/alpaca-zh)
+5. 69万条中文指令数据集(Belle50万条+Guanaco19万条)：[Chinese-Vicuna/guanaco_belle_merge_v1.0](https://huggingface.co/datasets/Chinese-Vicuna/guanaco_belle_merge_v1.0)
+
+## FAQ
+1. 问：为啥没有`int4`量化模型的Finetune训练？
+
+答：THUDM放出了2个int4量化模型，分别是 [THUDM/chatglm-6b-int4](https://huggingface.co/THUDM/chatglm-6b-int4) 和 
+[THUDM/chatglm-6b-int4-qe](https://huggingface.co/THUDM/chatglm-6b-int4-qe) 模型，是基于
+[THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) 的int4并对Embedding量化后的模型，模型运行仅需要 4.3GB 显存。
+
+训练方法参考官方给出的[P-tuning方法](https://github.com/THUDM/ChatGLM-6B/blob/main/ptuning/README.md)，INT4 量化模型的训练最低只需 6.7G 显存。
 
 
 # Contact
 
 - Issue(建议)：[![GitHub issues](https://img.shields.io/github/issues/shibing624/lmft.svg)](https://github.com/shibing624/lmft/issues)
 - 邮件我：xuming: xuming624@qq.com
 - 微信我：加我*微信号：xuming624, 备注：姓名-公司-NLP* 进NLP交流群。
@@ -152,16 +177,18 @@
   howpublished = {\url{https://github.com/shibing624/lmft}},
 }
 ```
 
 # License
 
 
-授权协议为 [The Apache License 2.0](LICENSE)，可免费用做商业用途。请在产品说明中附加lmft的链接和授权协议。
+lmft授权协议为 [The Apache License 2.0](LICENSE)，可免费用做商业用途。请在产品说明中附加lmft的链接和授权协议。
 
+- ChatGLM-6B的模型权重仅限学术研究用，具体见[MODEL_LICENSE](https://github.com/THUDM/ChatGLM-6B/blob/main/MODEL_LICENSE)
+- LLAMA的模型权重仅限学术研究用，具体见[LICENSE](https://huggingface.co/decapoda-research/llama-13b-hf/blob/main/LICENSE)
 
 # Contribute
 项目代码还很粗糙，如果大家对代码有所改进，欢迎提交回本项目，在提交之前，注意以下两点：
 
  - 在`tests`添加相应的单元测试
  - 使用`python -m pytest -v`来运行所有单元测试，确保所有单测都是通过的
```

### Comparing `lmft-0.2.2/lmft/chatglm_model.py` & `lmft-0.2.5/lmft/chatglm_model.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,94 +1,66 @@
 # -*- coding: utf-8 -*-
 """
 @author:XuMing(xuming624@qq.com)
 @description:
 """
 import os
+import re
 import random
 from typing import Tuple, List
 
 import numpy as np
 import torch
 import torch.nn as nn
-from datasets import load_dataset
 from loguru import logger
-from peft import get_peft_model, LoraConfig, TaskType
+from peft import get_peft_model, LoraConfig, TaskType, PeftModel
 from tqdm.auto import tqdm
-from transformers import AutoConfig, AutoTokenizer, Trainer
-from transformers import TrainingArguments
-from transformers.generation.utils import LogitsProcessorList
+from transformers import Trainer, TrainingArguments, AutoTokenizer, AutoModel, AutoConfig
 from transformers.trainer import TRAINING_ARGS_NAME
-
 from .chatglm_utils import (
-    ChatGLMForConditionalGeneration,
     ChatGLMArgs,
-    InvalidScoreLogitsProcessor,
+    load_hf_dataset,
+    ChatGLMDataset,
 )
 
 try:
     import wandb
 
     wandb_available = True
 except ImportError:
     wandb_available = False
 
 has_cuda = torch.cuda.is_available()
 os.environ["TOKENIZERS_PARALLELISM"] = "FALSE"
 os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
 
 MODEL_CLASSES = {
-    "chatglm": (AutoConfig, ChatGLMForConditionalGeneration, AutoTokenizer),
+    "chatglm": (AutoConfig, AutoModel, AutoTokenizer),
 }
 
 
-def save_tunable_parameters(model, path):
-    saved_params = {
-        k: v.to("cpu") for k, v in model.named_parameters() if v.requires_grad
-    }
-    torch.save(saved_params, path)
-
-
-class FinetuneTrainer(Trainer):
-    def compute_loss(self, model, inputs, return_outputs=False):
-        return model(
-            input_ids=inputs["input_ids"],
-            attention_mask=inputs["attention_mask"],
-            position_ids=inputs["position_ids"],
-            labels=inputs["labels"],
-        ).loss
-
-    def save_model(self, output_dir=None, _internal_call=False, lora_name='lora.pt'):
-        os.makedirs(output_dir, exist_ok=True)
-        torch.save(self.args, os.path.join(output_dir, TRAINING_ARGS_NAME))
-        save_tunable_parameters(self.model, os.path.join(output_dir, lora_name))
-
-
-class CastOutputToFloat(nn.Sequential):
-    def forward(self, x):
-        return super().forward(x).to(torch.float32)
-
-
-class ChatGLMTune:
+class ChatGlmModel:
     def __init__(
             self,
             model_type,
             model_name,
+            lora_name=None,
             args=None,
             use_cuda=has_cuda,
             cuda_device=-1,
             **kwargs,
     ):
 
         """
         Initializes a ChatGLMModel model.
 
         Args:
             model_type: The type of model (chatglm)
             model_name: The exact architecture and trained weights to use. This may be a Hugging Face Transformers compatible pre-trained model, a community model, or the path to a directory containing model files.
+            lora_name (optional): Lora name
             args (optional): Default args will be used if this parameter is not provided. If provided, it should be a dict containing the args that should be changed in the default args.
             use_cuda (optional): Use GPU if available. Setting to False will force model to use CPU only.
             cuda_device (optional): Specific GPU that should be used. Will use the first available GPU by default.
             **kwargs (optional): For providing proxies, force_download, resume_download, cache_dir and other options specific to the 'from_pretrained' implementation where this will be supplied.
         """  # noqa: ignore flake8"
         model_type = model_type.lower()
         self.args = self._load_model_args(model_name)
@@ -116,148 +88,72 @@
                 raise ValueError(
                     "'use_cuda' set to True when cuda is unavailable."
                     "Make sure CUDA is available or set `use_cuda=False`."
                 )
         else:
             self.device = "cpu"
         logger.debug(f"Device: {self.device}")
+        if not use_cuda:
+            self.args.fp16 = False
 
         self.results = {}
         config_class, model_class, tokenizer_class = MODEL_CLASSES[model_type]
         if model_name is None:
             model_name = "THUDM/chatglm-6b"
-        if torch.cuda.is_available():
-            self.model = model_class.from_pretrained(model_name,
-                                                     trust_remote_code=True).half().cuda()
+        config = AutoConfig.from_pretrained(model_name, trust_remote_code=True, **kwargs)
+        if use_cuda and torch.cuda.is_available():
+            self.model = model_class.from_pretrained(model_name, config=config, trust_remote_code=True)
+            if self.args.quantization_bit is not None:
+                logger.debug(f"Quantized to {self.args.quantization_bit} bit")
+                self.model = self.model.quantize(self.args.quantization_bit)
+            if self.args.fp16:
+                self.model = self.model.half().cuda()
         else:
-            self.model = model_class.from_pretrained(model_name, trust_remote_code=True).float()
+            self.model = model_class.from_pretrained(model_name, config=config, trust_remote_code=True).float()
 
         self.tokenizer_class = tokenizer_class
         if self.args.tokenizer_name:
             self.tokenizer = tokenizer_class.from_pretrained(self.args.tokenizer_name, trust_remote_code=True)
         else:
-            self.tokenizer = tokenizer_class.from_pretrained(model_name, trust_remote_code=True, **kwargs)
+            self.tokenizer = tokenizer_class.from_pretrained(model_name, trust_remote_code=True)
             self.args.tokenizer_name = self.args.model_name
 
-        if not use_cuda:
-            self.args.fp16 = False
-
         self.args.model_type = model_type
         if model_name is None:
             self.args.model_name = "ChatGLM_from_scratch"
         else:
             self.args.model_name = model_name
-        self.lora_loaded = False
-
-    @staticmethod
-    def get_masks_and_position_ids(seq_len, context_length, device, gmask=False, position_encoding_2d=True):
-        mask_position = (
-                seq_len - 2
-        )  # is equal to `seq.index(mask_token)` or `seq.index(150001)`
-        attention_mask = torch.ones((1, context_length, context_length), device=device)
-        attention_mask.tril_()
-        attention_mask[..., : mask_position - 1] = 1
-        attention_mask = (attention_mask < 0.5).bool()
-
-        if position_encoding_2d:
-            seq_length = seq_len - 1  # is equal to `seq_length = seq.index(150004)`
-            position_ids = torch.arange(context_length, dtype=torch.long, device=device)
-            if not gmask:
-                position_ids[seq_length:] = mask_position
-            block_position_ids = torch.cat(
-                (
-                    torch.zeros(seq_length, dtype=torch.long, device=device),
-                    torch.arange(
-                        context_length - seq_length, dtype=torch.long, device=device
-                    )
-                    + 1,
-                )
-            )
-            position_ids = torch.stack((position_ids, block_position_ids), dim=0)
-        else:
-            position_ids = torch.arange(context_length, dtype=torch.long, device=device)
-            if not gmask:
-                position_ids[context_length - 1:] = mask_position
-        return attention_mask, position_ids
-
-    def build_dataset(self, dataset_name_or_path="shibing624/alpaca-zh", max_seq_length=512):
-        """
-        Build dataset for training. This builds the dataset from `load_dataset`, one should
-        customize this function to train the model on its own dataset.
-
-        Args:
-            dataset_name_or_path (`str`):
-                The name of the dataset to be loaded.
 
-        Returns:
-            dataloader (`torch.utils.data.DataLoader`):
-                The dataloader for the dataset.
-        """
-        # load datasets
-        if os.path.exists(dataset_name_or_path):
-            ds = load_dataset("json", data_files=dataset_name_or_path)
-            ds = ds['train']
-        else:
-            ds = load_dataset(dataset_name_or_path, split="train")
-        if self.args.debug:
-            ds = ds.select(range(20))
-        ds = ds.rename_columns({"output": "target"})
-        ds = ds.filter(lambda x: len(x["target"]) > 0, batched=False)
-
-        def tokenize(example):
-            prompt = f"Instruction: {example['instruction']}\n"
-            if example.get("input", ""):
-                prompt += f"Input: {example['input']}\n"
-            prompt += "Answer: "
-            example['prompt'] = prompt
-            prompt_ids = self.tokenizer.encode(prompt, max_length=max_seq_length, truncation=True)
-            target_ids = self.tokenizer.encode(example["target"], max_length=max_seq_length, truncation=True,
-                                               add_special_tokens=False)
-            input_ids = prompt_ids + target_ids + [self.tokenizer.eos_token_id]
-            example["input_ids"] = input_ids[:max_seq_length]
-            example["seq_len"] = len(prompt_ids)
-            return example
+        self.lora_name = lora_name
+        self.lora_loaded = False
 
-        ds = ds.map(tokenize, batched=False)
-        return ds
 
     def data_collator(self, batch):
-        len_ids = [len(example["input_ids"]) for example in batch]
+        len_ids = [len(example) for example in batch]
         longest = max(len_ids)
         input_ids = []
-        attention_mask_list = []
-        position_ids_list = []
         labels_list = []
         for ids_l, feature in sorted(zip(len_ids, batch), key=lambda x: -x[0]):
-            ids = feature["input_ids"]
-            seq_len = ids.index(self.tokenizer.bos_token_id)
+            ids = list(feature)
+            seq_len = ids.index(self.tokenizer.bos_token_id) + 1  # is equal to `seq_len = seq.index(150004) + 1`
             label_pad_token_id = -100
             labels = (
                     [label_pad_token_id] * (seq_len - 1)
                     + ids[(seq_len - 1):]
                     + [label_pad_token_id] * (longest - ids_l)
             )
             ids = ids + [self.tokenizer.pad_token_id] * (longest - ids_l)
             _ids = torch.LongTensor(ids)
-            attention_mask, position_ids = self.get_masks_and_position_ids(
-                seq_len, longest, _ids.device, gmask=False
-            )
             labels_list.append(torch.LongTensor(labels))
             input_ids.append(_ids)
-            attention_mask_list.append(attention_mask)
-            position_ids_list.append(position_ids)
         input_ids = torch.stack(input_ids)
         labels = torch.stack(labels_list)
-        attention_mask = torch.stack(attention_mask_list)
-        position_ids = torch.stack(position_ids_list)
         return {
             "input_ids": input_ids,
             "labels": labels,
-            "attention_mask": attention_mask,
-            "position_ids": position_ids,
         }
 
     def train_model(
             self,
             train_data,
             output_dir=None,
             args=None,
@@ -265,15 +161,18 @@
             verbose=True,
             **kwargs,
     ):
         """
         Trains the model using 'train_data'
 
         Args:
-            train_data: datasets Dataset object or path to file containing training data
+            train_data: Pandas DataFrame containing the 3 columns - `instruction`, `input`, `output`.
+                        - `instruction`: The instruction text. (E.g. `"correct the following:"`)
+                        - `input`: The input text sequence. `instruction` is automatically prepended to form the full input. (<instruction> `\n` <input>)
+                        - `output`: The target sequence
             output_dir: The directory where model files will be saved. If not given, self.args.output_dir will be used.
             show_running_loss (optional): Set to False to prevent running loss from being printed to console. Defaults to True.
             args (optional): Optional changes to the args dict of the model. Any changes made will persist for the model.
             eval_data (optional): A DataFrame against which evaluation will be performed when evaluate_during_training is enabled. Is required if evaluate_during_training is enabled.
             **kwargs: Additional metrics that should be used. Pass in the metrics as keyword arguments (name of metric: function to use).
                         A metric function should take in two parameters. The first parameter will be the true labels, and the second parameter will be the predictions. Both inputs
                         will be lists of strings. Note that this will slow down training significantly as the predicted sequences need to be generated.
@@ -317,20 +216,20 @@
                 task_type=TaskType.CAUSAL_LM,
                 inference_mode=False,
                 r=self.args.lora_rank,
                 lora_alpha=self.args.lora_alpha,
                 lora_dropout=self.args.lora_dropout,
             )
             self.model = get_peft_model(self.model, peft_config)
+            print_trainable_parameters(self.model)
             self.lora_loaded = True
         self._move_model_to_device()
-        os.makedirs(output_dir, exist_ok=True)
-
         # load dataset
-        train_dataset = self.build_dataset(train_data, max_seq_length=self.args.max_seq_length)
+        train_dataset = self.load_and_cache_examples(train_data, verbose=verbose)
+        os.makedirs(output_dir, exist_ok=True)
         logger.debug(f"dataset: {train_dataset} first row: {next(iter(train_dataset))}")
 
         # start train
         training_args = TrainingArguments(
             output_dir=self.args.output_dir,
             auto_find_batch_size=True,
             learning_rate=self.args.learning_rate,
@@ -343,128 +242,183 @@
             gradient_accumulation_steps=self.args.gradient_accumulation_steps,
             save_steps=self.args.save_steps,
             save_total_limit=self.args.save_total_limit,
             fp16=self.args.fp16,
             remove_unused_columns=self.args.remove_unused_columns,
             overwrite_output_dir=self.args.overwrite_output_dir,
             do_train=True,
+            no_cuda=True if self.device == "cpu" else False,
         )
         logger.debug(f"training_args: {training_args}")
         trainer = FinetuneTrainer(
             model=self.model,
             train_dataset=train_dataset,
             args=training_args,
             tokenizer=self.tokenizer,
             data_collator=self.data_collator,
         )
-        trainer.train()
+        (global_step, training_loss, metrics) = trainer.train()
 
         self.save_model(model=self.model)
 
         if verbose:
             logger.info(
                 " Training of {} model complete. Saved to {}.".format(
                     self.args.model_name, output_dir
                 )
             )
+        return global_step, training_loss
 
     def load_lora(self):
         if self.args.use_lora:
-            lora_path = os.path.join(self.args.output_dir, self.args.lora_name)
-            if lora_path and os.path.exists(lora_path):
-                # infer with trained lora model
-                peft_config = LoraConfig(
-                    task_type=TaskType.CAUSAL_LM,
-                    inference_mode=True,
-                    r=self.args.lora_rank,
-                    lora_alpha=self.args.lora_alpha,
-                    lora_dropout=self.args.lora_dropout,
-                )
-                self.model = get_peft_model(self.model, peft_config)
-                self.model.load_state_dict(torch.load(lora_path), strict=False)
-                logger.info(f"Loaded lora model from {lora_path}")
+            if self.lora_name and self.lora_name.startswith('shibing624'):
+                self.model = PeftModel.from_pretrained(self.model, self.lora_name)
+                logger.info(f"Loaded lora model from {self.lora_name}")
                 self.lora_loaded = True
+            else:
+                lora_path = os.path.join(self.args.output_dir, self.args.lora_name)
+                if lora_path and os.path.exists(lora_path):
+                    # infer with trained lora model
+                    self.model = PeftModel.from_pretrained(self.model, self.args.output_dir)
+                    logger.info(f"Loaded lora model from {lora_path}")
+                    self.lora_loaded = True
+
+    def process_response(self, response):
+        response = response.strip().replace("[[训练时间]]", "2023年")
+        punkts = [
+            [",", "，"],
+            ["!", "！"],
+            [":", "："],
+            [";", "；"],
+            ["\?", "？"],
+        ]
+        for item in punkts:
+            response = re.sub(r"([\u4e00-\u9fff])%s" % item[0], r"\1%s" % item[1], response)
+            response = re.sub(r"%s([\u4e00-\u9fff])" % item[0], r"%s\1" % item[1], response)
+        return response
 
     @torch.no_grad()
-    def chat(self, query: str, history: List[Tuple[str, str]] = None, logits_processor=None, **kwargs):
-        """
-        Chat with the model
-        :param query:
-        :param history:
-        :param logits_processor:
-        :param kwargs:
-        :return: response, history
-        """
-        self._move_model_to_device()
-        self.model.eval()
-        if history is None:
-            history = []
-        if not history:
-            prompt = query
-        else:
-            prompt = ""
-            for i, (old_query, response) in enumerate(history):
-                prompt += "[Round {}]\n问：{}\n答：{}\n".format(i, old_query, response)
-            prompt += "[Round {}]\n问：{}\n答：".format(len(history), query)
-        response = self.predict([prompt], logits_processor=logits_processor, **kwargs)[0]
-        response = response.strip()
-        history = history + [(query, response)]
-        return response, history
-
-    @torch.no_grad()
-    def predict(self, sentences, logits_processor=None, **kwargs):
+    def predict(self, sentences, keep_prompt=False, max_length=None, **kwargs):
         """
         Performs predictions on a list of text.
 
         Args:
             sentences: A python list of text (str) to be sent to the model for prediction. 
-            logits_processor: A LogitsProcessor object that will be applied to the model's
+            keep_prompt: Whether to keep the prompt in the generated text.
+            max_length: The maximum length of the generated text.
 
         Returns:
             preds: A python list of the generated sequences.
         """  # noqa: ignore flake8"
 
         if not self.lora_loaded:
             self.load_lora()
         self._move_model_to_device()
         if torch.cuda.is_available() and self.args.fp16:
             self.model = self.model.half().cuda()
         self.model.eval()
 
         all_outputs = []
-        if logits_processor is None:
-            logits_processor = LogitsProcessorList()
-        logits_processor.append(InvalidScoreLogitsProcessor())
         # Batching
         for batch in tqdm(
                 [
                     sentences[i: i + self.args.eval_batch_size]
                     for i in range(0, len(sentences), self.args.eval_batch_size)
                 ],
                 desc="Generating outputs",
                 disable=self.args.silent,
         ):
             inputs = self.tokenizer(batch, padding=True, return_tensors='pt').to(self.device)
             gen_kwargs = {
-                "max_length": self.args.max_length,
+                "max_length": max_length if max_length else self.args.max_length,
                 "num_beams": self.args.num_beams,
                 "do_sample": self.args.do_sample,
                 "top_p": self.args.top_p,
                 "temperature": self.args.temperature,
-                "logits_processor": logits_processor,
+                "eos_token_id": self.tokenizer.eos_token_id,
                 **kwargs
             }
             outputs = self.model.generate(**inputs, **gen_kwargs)
-            all_outputs.extend(outputs.cpu().numpy())
-        outputs = [self.tokenizer.decode(output_id) for output_id in all_outputs]
-        return outputs
+            for idx, (prompt_text, generated_sequence) in enumerate(zip(batch, outputs)):
+                # Decode text
+                text = self.tokenizer.decode(generated_sequence)
+                prompt_len = len(prompt_text)
+                gen_text = text[prompt_len:]
+                gen_text = self.process_response(gen_text)
+                if keep_prompt:
+                    total_sequence = prompt_text + gen_text
+                else:
+                    total_sequence = gen_text
+                all_outputs.append(total_sequence)
+        return all_outputs
+
+    @torch.no_grad()
+    def chat(self, query: str, history: List[Tuple[str, str]] = None,
+             keep_prompt=False, max_length=128, **kwargs):
+        """
+        Chat with the model
+        :param query:
+        :param history:
+        :param keep_prompt:
+        :param max_length:
+        :param kwargs:
+        :return: response, history
+        """
+        self._move_model_to_device()
+        self.model.eval()
+        if history is None:
+            history = []
+        if not history:
+            prompt = query
+        else:
+            prompt = ""
+            for i, (old_query, response) in enumerate(history):
+                prompt += "[Round {}]\n问：{}\n答：{}\n".format(i, old_query, response)
+            prompt += "[Round {}]\n问：{}\n答：".format(len(history), query)
+        response = self.predict([prompt], keep_prompt=keep_prompt, max_length=len(prompt) + max_length, **kwargs)[0]
+        history = history + [(query, response)]
+        return response, history
 
     def _move_model_to_device(self):
         self.model.to(self.device)
 
+    def load_and_cache_examples(
+            self, data, evaluate=False, no_cache=False, verbose=True, silent=False
+    ):
+        """
+        Creates a ChatGLMDataset from data.
+
+        Utility function for train() and eval() methods. Not intended to be used directly.
+        """
+
+        tokenizer = self.tokenizer
+        args = self.args
+
+        if not no_cache:
+            no_cache = args.no_cache
+
+        if not no_cache:
+            os.makedirs(self.args.cache_dir, exist_ok=True)
+
+        mode = "dev" if evaluate else "train"
+
+        if self.args.use_hf_datasets:
+            dataset = load_hf_dataset(data, tokenizer, self.args)
+            return dataset
+        elif args.dataset_class:
+            CustomDataset = args.dataset_class
+            return CustomDataset(tokenizer, args, data, mode)
+        else:
+            return ChatGLMDataset(
+                tokenizer,
+                self.args,
+                data,
+                mode,
+            )
+
     def save_model(
             self, output_dir=None, optimizer=None, scheduler=None, model=None, results=None
     ):
         if not output_dir:
             output_dir = self.args.output_dir
         os.makedirs(output_dir, exist_ok=True)
 
@@ -478,17 +432,15 @@
                 torch.save(
                     optimizer.state_dict(), os.path.join(output_dir, "optimizer.pt")
                 )
                 torch.save(
                     scheduler.state_dict(), os.path.join(output_dir, "scheduler.pt")
                 )
             # save model
-            save_tunable_parameters(
-                self.model, os.path.join(self.args.output_dir, self.args.lora_name)
-            )
+            self.save_model_args(output_dir)
 
         if results:
             output_eval_file = os.path.join(output_dir, "eval_results.txt")
             with open(output_eval_file, "w") as writer:
                 for key in sorted(results.keys()):
                     writer.write("{} = {}\n".format(key, str(results[key])))
 
@@ -499,7 +451,43 @@
     def _load_model_args(self, input_dir):
         args = ChatGLMArgs()
         args.load(input_dir)
         return args
 
     def get_named_parameters(self):
         return [n for n, p in self.model.named_parameters()]
+
+
+class FinetuneTrainer(Trainer):
+    def compute_loss(self, model, inputs, return_outputs=False):
+        return model(
+            input_ids=inputs["input_ids"],
+            labels=inputs["labels"],
+        ).loss
+
+    def save_model(self, output_dir=None, _internal_call=False, lora_name='adapter_model.bin'):
+        os.makedirs(output_dir, exist_ok=True)
+        torch.save(self.args, os.path.join(output_dir, TRAINING_ARGS_NAME))
+        saved_params = {
+            k: v.to("cpu") for k, v in self.model.named_parameters() if v.requires_grad
+        }
+        torch.save(saved_params, os.path.join(output_dir, lora_name))
+
+
+class CastOutputToFloat(nn.Sequential):
+    def forward(self, x):
+        return super().forward(x).to(torch.float32)
+
+
+def print_trainable_parameters(model):
+    """
+    Prints the number of trainable parameters in the model.
+    """
+    trainable_params = 0
+    all_param = 0
+    for _, param in model.named_parameters():
+        all_param += param.numel()
+        if param.requires_grad:
+            trainable_params += param.numel()
+    logger.debug(
+        f"trainable params: {trainable_params} || all params: {all_param} || trainable%: {100 * trainable_params / all_param}"
+    )
```

### Comparing `lmft-0.2.2/lmft/gpt2-sentiment.py` & `lmft-0.2.5/lmft/gpt2-sentiment.py`

 * *Files identical despite different names*

### Comparing `lmft-0.2.2/lmft/gpt2-sentiment_peft.py` & `lmft-0.2.5/lmft/gpt2-sentiment_peft.py`

 * *Files identical despite different names*

### Comparing `lmft-0.2.2/lmft/gpt2_sentiment.py` & `lmft-0.2.5/lmft/gpt2_sentiment.py`

 * *Files identical despite different names*

### Comparing `lmft-0.2.2/lmft/gpt_neox_sentiment_trl_peft.py` & `lmft-0.2.5/lmft/gpt_neox_sentiment_trl_peft.py`

 * *Files identical despite different names*

### Comparing `lmft-0.2.2/lmft/t5-sentiment.py` & `lmft-0.2.5/lmft/t5-sentiment.py`

 * *Files identical despite different names*

### Comparing `lmft-0.2.2/lmft.egg-info/PKG-INFO` & `lmft-0.2.5/lmft.egg-info/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lmft
-Version: 0.2.2
+Version: 0.2.5
 Summary: Language Model Fine-tuning Toolkit (LMFT)
 Home-page: https://github.com/shibing624/lmft
 Author: XuMing
 Author-email: xuming624@qq.com
 License: Apache License 2.0
 Description: [![PyPI version](https://badge.fury.io/py/lmft.svg)](https://badge.fury.io/py/lmft)
         [![Downloads](https://pepy.tech/badge/lmft)](https://pepy.tech/project/lmft)
@@ -15,15 +15,15 @@
         [![GitHub issues](https://img.shields.io/github/issues/shibing624/lmft.svg)](https://github.com/shibing624/lmft/issues)
         [![Wechat Group](http://vlog.sfyc.ltd/wechat_everyday/wxgroup_logo.png?imageView2/0/w/60/h/20)](#Contact)
         
         # LMFT: Language Model Fine-Tuning
         Language Model Fine-Tuning, for ChatGLM, BELLE, LLaMA fine-tuning.
         
         
-        **lmft**实现了ChatGLM-6B的模型finetune。
+        **lmft**实现了ChatGLM-6B的模型FineTune。
         
         
         **Guide**
         - [Feature](#Feature)
         - [Evaluation](#Evaluation)
         - [Demo](#Demo)
         - [Install](#install)
@@ -32,23 +32,22 @@
         - [Reference](#reference)
         
         
         # Feature
         ### ChatGLM
         #### [THUDM/chatglm-6b](https://huggingface.co/THUDM/chatglm-6b) 模型的Finetune训练
         
-        [THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)放出的默认模型，模型以 FP16 精度加载，模型运行需要 13GB 显存，训练需要 29GB 显存。
-        #### [THUDM/chatglm-6b-int4-qe](https://huggingface.co/THUDM/chatglm-6b-int4-qe) 模型的Finetune训练
-        
-        [THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)放出的int4并对Embedding量化后的模型，模型运行需要 4.3GB 显存，训练需要 8GB 以上显存。
+        [THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)放出的默认模型，模型以 FP16 精度加载，模型运行需要 13GB 显存，训练需要 22GB 显存(batch_size=2)。
         
         
         # Evaluation
         
-        ### 对话生成
+        ### 纠错能力比较
+        
+        ### 对话能力比较
         
         # Demo
         
         HuggingFace Demo: https://huggingface.co/spaces/shibing624/lmft
         
         ![](docs/hf.png)
         
@@ -69,70 +68,96 @@
         
         git clone https://github.com/shibing624/lmft.git
         cd lmft
         pip install --no-deps .
         ```
         
         # Usage
+        ## Use LoRA model
+        release lora model: 
+        1. 中文拼写纠错（CSC）模型 [shibing624/chatglm-6b-csc-zh-lora](https://huggingface.co/shibing624/chatglm-6b-csc-zh-lora)
+        
+        
+        ```python
+        from lmft import ChatGlmModel
+        model = ChatGlmModel("chatglm", "THUDM/chatglm-6b", lora_name="shibing624/chatglm-6b-csc-zh-lora")
+        r = model.predict(["对下面中文拼写纠错：\n少先队员因该为老人让坐。\n答："])
+        print(r) # ['少先队员应该为老人让座。\n错误字：因，坐']
+        ```
         
         ## 训练ChatGLM-6B模型
         
-        example: [examples/train_chatglm_demo.py](examples/train_chatglm_demo.py)
+        支持自定义数据集，数据集格式参考[examples/data/test.tsv](examples/data/test.tsv)。
+        
+        
+        example: [examples/training_chatglm_demo.py](examples/training_chatglm_demo.py)
         
         ```python
         import sys
         
         sys.path.append('..')
-        from lmft import ChatGLMTune
+        from lmft import ChatGlmModel
         
         
         def finetune_demo():
-            m = ChatGLMTune('chatglm', "THUDM/chatglm-6b", args={'use_lora': True})
+            m = ChatGlmModel('chatglm', "THUDM/chatglm-6b", args={'use_lora': True})
             m.train_model(train_data='shibing624/alpaca-zh')
-            r = m.predict(['你是谁', '三原色是啥'])
+            r = m.predict(['给出三个保持健康的秘诀。', '描述原子的结构。'])
             print(r)
             response, history = m.chat("你好", history=[])
             print(response)
             response, history = m.chat("晚上睡不着应该怎么办", history=history)
             print(response)
         
         
         def origin_chat_demo():
-            m = ChatGLMTune('chatglm', "THUDM/chatglm-6b", args={'use_lora': False})
+            m = ChatGlmModel('chatglm', "THUDM/chatglm-6b", args={'use_lora': False})
             response, history = m.chat("你好", history=[])
             print(response)
             response, history = m.chat("晚上睡不着应该怎么办", history=history)
             print(response)
         
         
         if __name__ == '__main__':
             origin_chat_demo()
             finetune_demo()
         ```
         
         output:
         ```
-        问:hi
-        答:hi 
+        问:你好
+        答:你好
         
         [Round 1]
         问:晚上睡不着应该怎么办
         答: 想要在晚上入睡,但并不容易,可以参考下述技巧:
         1. 睡前放松:尝试进行一些放松的活动,如冥想、深呼吸或瑜伽,帮助放松身心,减轻压力和焦虑。
         2. 创造一个舒适的睡眠环境:保持房间安静、黑暗和凉爽,使用舒适的床垫和枕头,确保床铺干净整洁。
         3. 规律的睡眠时间表:保持规律的睡眠时间表,尽可能在同一时间上床,并创造一个固定的起床时间。
         4. 避免刺激性食物和饮料:避免在睡前饮用含咖啡因的饮料,如咖啡、茶和可乐,以及吃辛辣、油腻或难以消化的食物。
         5. 避免过度使用电子设备:避免在睡前使用电子设备,如手机、电视和电脑。这些设备会发出蓝光,干扰睡眠。
         如果尝试了这些技巧仍然无法入睡,建议咨询医生或睡眠专家,获取更专业的建议和帮助。
         ```
         
         
-        #### dataset
-        1. [0.5M生成的中文ChatGPT结果数据](https://huggingface.co/datasets/BelleGroup/generated_train_0.5M_CN)
-        2. [50k English Stanford Alpaca dataset](https://github.com/tatsu-lab/stanford_alpaca#data-release)
+        ## Dataset
+        1. 50万条中文ChatGPT指令数据集：[BelleGroup/train_0.5M_CN](https://huggingface.co/datasets/BelleGroup/train_0.5M_CN)
+        2. 100万条中文ChatGPT指令数据集：[BelleGroup/train_1M_CN](https://huggingface.co/datasets/BelleGroup/train_1M_CN)
+        3. 5万条英文ChatGPT指令数据集：[50k English Stanford Alpaca dataset](https://github.com/tatsu-lab/stanford_alpaca#data-release)
+        4. 2万条中文ChatGPT指令数据集：[shibing624/alpaca-zh](https://huggingface.co/datasets/shibing624/alpaca-zh)
+        5. 69万条中文指令数据集(Belle50万条+Guanaco19万条)：[Chinese-Vicuna/guanaco_belle_merge_v1.0](https://huggingface.co/datasets/Chinese-Vicuna/guanaco_belle_merge_v1.0)
+        
+        ## FAQ
+        1. 问：为啥没有`int4`量化模型的Finetune训练？
+        
+        答：THUDM放出了2个int4量化模型，分别是 [THUDM/chatglm-6b-int4](https://huggingface.co/THUDM/chatglm-6b-int4) 和 
+        [THUDM/chatglm-6b-int4-qe](https://huggingface.co/THUDM/chatglm-6b-int4-qe) 模型，是基于
+        [THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) 的int4并对Embedding量化后的模型，模型运行仅需要 4.3GB 显存。
+        
+        训练方法参考官方给出的[P-tuning方法](https://github.com/THUDM/ChatGLM-6B/blob/main/ptuning/README.md)，INT4 量化模型的训练最低只需 6.7G 显存。
         
         
         # Contact
         
         - Issue(建议)：[![GitHub issues](https://img.shields.io/github/issues/shibing624/lmft.svg)](https://github.com/shibing624/lmft/issues)
         - 邮件我：xuming: xuming624@qq.com
         - 微信我：加我*微信号：xuming624, 备注：姓名-公司-NLP* 进NLP交流群。
@@ -160,16 +185,18 @@
           howpublished = {\url{https://github.com/shibing624/lmft}},
         }
         ```
         
         # License
         
         
-        授权协议为 [The Apache License 2.0](LICENSE)，可免费用做商业用途。请在产品说明中附加lmft的链接和授权协议。
+        lmft授权协议为 [The Apache License 2.0](LICENSE)，可免费用做商业用途。请在产品说明中附加lmft的链接和授权协议。
         
+        - ChatGLM-6B的模型权重仅限学术研究用，具体见[MODEL_LICENSE](https://github.com/THUDM/ChatGLM-6B/blob/main/MODEL_LICENSE)
+        - LLAMA的模型权重仅限学术研究用，具体见[LICENSE](https://huggingface.co/decapoda-research/llama-13b-hf/blob/main/LICENSE)
         
         # Contribute
         项目代码还很粗糙，如果大家对代码有所改进，欢迎提交回本项目，在提交之前，注意以下两点：
         
          - 在`tests`添加相应的单元测试
          - 使用`python -m pytest -v`来运行所有单元测试，确保所有单测都是通过的
```

### Comparing `lmft-0.2.2/setup.py` & `lmft-0.2.5/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -29,16 +29,16 @@
     packages=find_packages(),
     include_package_data=True,
     entry_points={},
     python_requires=">=3.7.0",
     keywords='lmft,GPT2,transformers,pytorch,language model',
     install_requires=[
         "loguru",
-        "trl",
-        "transformers",
+        "peft",
+        "transformers>=4.27.1",
         "datasets",
         "tqdm",
     ],
     extras_require=extras,
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Intended Audience :: Developers",
```

