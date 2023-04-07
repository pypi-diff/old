# Comparing `tmp/span_marker-0.2.0.tar.gz` & `tmp/span_marker-0.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "span_marker-0.2.0.tar", last modified: Thu Apr  6 16:38:24 2023, max compression
+gzip compressed data, was "span_marker-0.2.1.tar", last modified: Fri Apr  7 14:01:25 2023, max compression
```

## Comparing `span_marker-0.2.0.tar` & `span_marker-0.2.1.tar`

### file list

```diff
@@ -1,27 +1,28 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 16:38:24.208481 span_marker-0.2.0/
--rw-rw-rw-   0        0        0     1088 2023-03-28 09:30:50.000000 span_marker-0.2.0/LICENSE
--rw-rw-rw-   0        0        0     4282 2023-04-06 16:38:24.207477 span_marker-0.2.0/PKG-INFO
--rw-rw-rw-   0        0        0     3705 2023-04-06 15:23:05.000000 span_marker-0.2.0/README.md
--rw-rw-rw-   0        0        0     2305 2023-04-06 15:01:25.000000 span_marker-0.2.0/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 16:38:24.208481 span_marker-0.2.0/setup.cfg
--rw-rw-rw-   0        0        0       41 2023-03-28 09:28:01.000000 span_marker-0.2.0/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-06 16:38:24.194916 span_marker-0.2.0/span_marker/
--rw-rw-rw-   0        0        0      352 2023-04-06 16:37:29.000000 span_marker-0.2.0/span_marker/__init__.py
--rw-rw-rw-   0        0        0     4825 2023-04-06 07:35:29.000000 span_marker-0.2.0/span_marker/configuration.py
--rw-rw-rw-   0        0        0     5389 2023-04-06 13:34:33.000000 span_marker-0.2.0/span_marker/data_collator.py
--rw-rw-rw-   0        0        0     4295 2023-04-06 07:35:29.000000 span_marker-0.2.0/span_marker/evaluation.py
--rw-rw-rw-   0        0        0     4831 2023-04-06 07:35:29.000000 span_marker-0.2.0/span_marker/label_normalizer.py
--rw-rw-rw-   0        0        0    18246 2023-04-06 14:00:45.000000 span_marker-0.2.0/span_marker/modeling.py
--rw-rw-rw-   0        0        0     1686 2023-04-06 14:00:45.000000 span_marker-0.2.0/span_marker/output.py
--rw-rw-rw-   0        0        0     6313 2023-04-06 09:12:18.000000 span_marker-0.2.0/span_marker/tokenizer.py
--rw-rw-rw-   0        0        0    11036 2023-04-06 14:00:45.000000 span_marker-0.2.0/span_marker/trainer.py
-drwxrwxrwx   0        0        0        0 2023-04-06 16:38:24.205424 span_marker-0.2.0/span_marker.egg-info/
--rw-rw-rw-   0        0        0     4282 2023-04-06 16:38:24.000000 span_marker-0.2.0/span_marker.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      522 2023-04-06 16:38:24.000000 span_marker-0.2.0/span_marker.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 16:38:24.000000 span_marker-0.2.0/span_marker.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      182 2023-04-06 16:38:24.000000 span_marker-0.2.0/span_marker.egg-info/requires.txt
--rw-rw-rw-   0        0        0       12 2023-04-06 16:38:24.000000 span_marker-0.2.0/span_marker.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-04-06 16:38:24.207477 span_marker-0.2.0/tests/
--rw-rw-rw-   0        0        0      961 2023-04-06 07:35:29.000000 span_marker-0.2.0/tests/test_configuration.py
--rw-rw-rw-   0        0        0     3534 2023-04-06 07:35:29.000000 span_marker-0.2.0/tests/test_modeling.py
--rw-rw-rw-   0        0        0     3992 2023-04-06 07:35:29.000000 span_marker-0.2.0/tests/test_trainer.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:01:25.193067 span_marker-0.2.1/
+-rw-rw-rw-   0        0        0     1088 2023-03-28 09:30:50.000000 span_marker-0.2.1/LICENSE
+-rw-rw-rw-   0        0        0     4407 2023-04-07 14:01:25.193067 span_marker-0.2.1/PKG-INFO
+-rw-rw-rw-   0        0        0     3830 2023-04-07 10:47:40.000000 span_marker-0.2.1/README.md
+-rw-rw-rw-   0        0        0     2305 2023-04-06 15:01:25.000000 span_marker-0.2.1/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 14:01:25.193067 span_marker-0.2.1/setup.cfg
+-rw-rw-rw-   0        0        0       41 2023-03-28 09:28:01.000000 span_marker-0.2.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:01:25.178905 span_marker-0.2.1/span_marker/
+-rw-rw-rw-   0        0        0      352 2023-04-07 13:58:03.000000 span_marker-0.2.1/span_marker/__init__.py
+-rw-rw-rw-   0        0        0     4901 2023-04-07 13:40:17.000000 span_marker-0.2.1/span_marker/configuration.py
+-rw-rw-rw-   0        0        0     5389 2023-04-06 13:34:33.000000 span_marker-0.2.1/span_marker/data_collator.py
+-rw-rw-rw-   0        0        0     4295 2023-04-06 07:35:29.000000 span_marker-0.2.1/span_marker/evaluation.py
+-rw-rw-rw-   0        0        0     4831 2023-04-06 07:35:29.000000 span_marker-0.2.1/span_marker/label_normalizer.py
+-rw-rw-rw-   0        0        0     1086 2023-04-07 13:56:16.000000 span_marker-0.2.1/span_marker/model_card.py
+-rw-rw-rw-   0        0        0    20210 2023-04-07 13:56:16.000000 span_marker-0.2.1/span_marker/modeling.py
+-rw-rw-rw-   0        0        0     1686 2023-04-06 14:00:45.000000 span_marker-0.2.1/span_marker/output.py
+-rw-rw-rw-   0        0        0     6313 2023-04-07 12:12:36.000000 span_marker-0.2.1/span_marker/tokenizer.py
+-rw-rw-rw-   0        0        0    11036 2023-04-06 14:00:45.000000 span_marker-0.2.1/span_marker/trainer.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:01:25.191066 span_marker-0.2.1/span_marker.egg-info/
+-rw-rw-rw-   0        0        0     4407 2023-04-07 14:01:25.000000 span_marker-0.2.1/span_marker.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      548 2023-04-07 14:01:25.000000 span_marker-0.2.1/span_marker.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 14:01:25.000000 span_marker-0.2.1/span_marker.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      182 2023-04-07 14:01:25.000000 span_marker-0.2.1/span_marker.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       12 2023-04-07 14:01:25.000000 span_marker-0.2.1/span_marker.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 14:01:25.192067 span_marker-0.2.1/tests/
+-rw-rw-rw-   0        0        0      961 2023-04-06 07:35:29.000000 span_marker-0.2.1/tests/test_configuration.py
+-rw-rw-rw-   0        0        0     3534 2023-04-06 07:35:29.000000 span_marker-0.2.1/tests/test_modeling.py
+-rw-rw-rw-   0        0        0     3992 2023-04-06 07:35:29.000000 span_marker-0.2.1/tests/test_trainer.py
```

### Comparing `span_marker-0.2.0/LICENSE` & `span_marker-0.2.1/LICENSE`

 * *Files identical despite different names*

### Comparing `span_marker-0.2.0/PKG-INFO` & `span_marker-0.2.1/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: span_marker
-Version: 0.2.0
+Version: 0.2.1
 Summary: Few-Shot Named Entity Recognition using Span Markers
 Author: Tom Aarsen
 Maintainer: Tom Aarsen
 Project-URL: Documentation, https://tomaarsen.github.io/SpanMarkerNER
 Project-URL: Repository, https://github.com/tomaarsen/SpanMarkerNER
 Keywords: data-science,natural-language-processing,artificial-intelligence,mlops,nlp,machine-learning,transformers
 Requires-Python: >=3.7
@@ -83,10 +83,11 @@
 
 Because this work is based on [PL-Marker](https://arxiv.org/pdf/2109.06067v5.pdf), you may expect similar results to its [Papers with Code Leaderboard](https://paperswithcode.com/paper/pack-together-entity-and-relation-extraction) results. Tests, documentation and further information on expected performance will come soon.
 
 ## Pretrained Models
 
 * [`tomaarsen/span-marker-bert-base-fewnerd-fine-super`](https://huggingface.co/tomaarsen/span-marker-bert-base-fewnerd-fine-super) is a model that I have trained in just 4 hours on the finegrained, supervised [Few-NERD dataset](https://huggingface.co/datasets/DFKI-SLT/few-nerd). It reached a 0.7020 Test F1, competitive in the all-time [Few-NERD leaderboard](https://paperswithcode.com/sota/named-entity-recognition-on-few-nerd-sup). My training script resembles the one that you can see above.
   * See this [Weights and Biases report](https://api.wandb.ai/links/tomaarsen/dm21vbbm) for training details.
+  * Try the model out online using this [🤗 Space](https://tomaarsen-span-marker-bert-base-fewnerd-fine-super.hf.space/).
 
 ## Changelog
 See [CHANGELOG.md](CHANGELOG.md) for news on all SpanMarker versions.
```

### Comparing `span_marker-0.2.0/README.md` & `span_marker-0.2.1/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -67,10 +67,11 @@
 
 Because this work is based on [PL-Marker](https://arxiv.org/pdf/2109.06067v5.pdf), you may expect similar results to its [Papers with Code Leaderboard](https://paperswithcode.com/paper/pack-together-entity-and-relation-extraction) results. Tests, documentation and further information on expected performance will come soon.
 
 ## Pretrained Models
 
 * [`tomaarsen/span-marker-bert-base-fewnerd-fine-super`](https://huggingface.co/tomaarsen/span-marker-bert-base-fewnerd-fine-super) is a model that I have trained in just 4 hours on the finegrained, supervised [Few-NERD dataset](https://huggingface.co/datasets/DFKI-SLT/few-nerd). It reached a 0.7020 Test F1, competitive in the all-time [Few-NERD leaderboard](https://paperswithcode.com/sota/named-entity-recognition-on-few-nerd-sup). My training script resembles the one that you can see above.
   * See this [Weights and Biases report](https://api.wandb.ai/links/tomaarsen/dm21vbbm) for training details.
+  * Try the model out online using this [🤗 Space](https://tomaarsen-span-marker-bert-base-fewnerd-fine-super.hf.space/).
 
 ## Changelog
 See [CHANGELOG.md](CHANGELOG.md) for news on all SpanMarker versions.
```

### Comparing `span_marker-0.2.0/pyproject.toml` & `span_marker-0.2.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `span_marker-0.2.0/span_marker/configuration.py` & `span_marker-0.2.1/span_marker/configuration.py`

 * *Files 2% similar despite different names*

```diff
@@ -17,14 +17,15 @@
         **kwargs,
     ) -> None:
         self.encoder = encoder_config
         self.model_max_length = model_max_length
         self.model_max_length_default = 512
         self.marker_max_length = marker_max_length
         self.entity_max_length = entity_max_length
+        self.span_marker_version = kwargs.pop("span_marker_version", None)
         super().__init__(**kwargs)
 
         # label2id and id2label are automatically set by super().__init__, but we want to rely on
         # the encoder configs instead if we can, so we delete them under two conditions
         # 1. if they're the default ({0: "LABEL_0", 1: "LABEL_1"})
         # 2. if they're identical to the encoder label2id
         span_marker_label2id = super().__getattribute__("label2id")
```

### Comparing `span_marker-0.2.0/span_marker/data_collator.py` & `span_marker-0.2.1/span_marker/data_collator.py`

 * *Files identical despite different names*

### Comparing `span_marker-0.2.0/span_marker/evaluation.py` & `span_marker-0.2.1/span_marker/evaluation.py`

 * *Files identical despite different names*

### Comparing `span_marker-0.2.0/span_marker/label_normalizer.py` & `span_marker-0.2.1/span_marker/label_normalizer.py`

 * *Files identical despite different names*

### Comparing `span_marker-0.2.0/span_marker/modeling.py` & `span_marker-0.2.1/span_marker/modeling.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,16 +1,18 @@
 import os
-from typing import Dict, List, Optional, Type, TypeVar, Union
+from typing import Callable, Dict, List, Optional, Type, TypeVar, Union
 
 import torch
 from torch import nn
 from transformers import AutoConfig, AutoModel, PretrainedConfig, PreTrainedModel
 
+from span_marker import __version__ as span_marker_version
 from span_marker.configuration import SpanMarkerConfig
 from span_marker.data_collator import SpanMarkerDataCollator
+from span_marker.model_card import MODEL_CARD_TEMPLATE
 from span_marker.output import SpanMarkerOutput
 from span_marker.tokenizer import SpanMarkerTokenizer
 
 T = TypeVar("T", bound="SpanMarkerModel")
 
 
 class SpanMarkerModel(PreTrainedModel):
@@ -201,26 +203,27 @@
         # then initialize it and create the SpanMarker config and model using the encoder and its config.
         else:
             encoder = AutoModel.from_pretrained(pretrained_model_name_or_path, *model_args, config=config)
             if labels is None:
                 raise ValueError(
                     "Please provide a `labels` list to `SpanMarkerModel.from_pretrained()`, e.g.\n"
                     ">>> SpanMarkerModel.from_pretrained(\n"
-                    '...     "bert-base-cased",\n'
+                    f'...     "{pretrained_model_name_or_path}",\n'
                     '...     labels=["O", "B-PER", "I-PER", "B-ORG", "I-ORG", ...]\n'
                     "... )\n"
                     "or\n"
                     ">>> SpanMarkerModel.from_pretrained(\n"
-                    '...     "bert-base-cased",\n'
+                    f'...     "{pretrained_model_name_or_path}",\n'
                     '...     labels=["O", "PER", "ORG", "LOC", "MISC"]\n'
                     "... )"
                 )
             config.id2label = dict(enumerate(labels))
             config.label2id = {v: k for k, v in config.id2label.items()}
-            config = cls.config_class(encoder_config=config.to_dict())
+            # Set the span_marker version for freshly initialized models
+            config = cls.config_class(encoder_config=config.to_dict(), span_marker_version=span_marker_version)
             model = cls(config, encoder, *model_args, **kwargs)
 
         # Pass the tokenizer directly to the model for convenience, this way the user doesn't have to
         # make it themselves.
         tokenizer = SpanMarkerTokenizer.from_pretrained(
             config.encoder.get("_name_or_path", pretrained_model_name_or_path), config=config, **kwargs
         )
@@ -334,7 +337,51 @@
 
                 if not allow_overlapping:
                     word_selected[word_start_index:word_end_index] = [True] * (word_end_index - word_start_index)
         return sorted(
             output,
             key=lambda entity: entity["char_start_index"] if isinstance(sentence, str) else entity["word_start_index"],
         )
+
+    def save_pretrained(
+        self,
+        save_directory: Union[str, os.PathLike],
+        is_main_process: bool = True,
+        state_dict: Optional[dict] = None,
+        save_function: Callable = torch.save,
+        push_to_hub: bool = False,
+        max_shard_size: Union[int, str] = "10GB",
+        safe_serialization: bool = False,
+        variant: Optional[str] = None,
+        **kwargs,
+    ) -> None:
+        super().save_pretrained(
+            save_directory,
+            is_main_process=is_main_process,
+            state_dict=state_dict,
+            save_function=save_function,
+            push_to_hub=push_to_hub,
+            max_shard_size=max_shard_size,
+            safe_serialization=safe_serialization,
+            variant=variant,
+            **kwargs,
+        )
+        self.tokenizer.save_pretrained(
+            save_directory,
+            is_main_process=is_main_process,
+            state_dict=state_dict,
+            save_function=save_function,
+            push_to_hub=push_to_hub,
+            max_shard_size=max_shard_size,
+            safe_serialization=safe_serialization,
+            variant=variant,
+            **kwargs,
+        )
+        if "_name_or_path" in self.config.encoder:
+            encoder_name_or_path = repr(self.config.encoder["_name_or_path"])
+        else:
+            encoder_name_or_path = "an unknown model"
+        model_card_content = MODEL_CARD_TEMPLATE.format(
+            model_name=save_directory, encoder_name_or_path=encoder_name_or_path
+        )
+        with open(os.path.join(save_directory, "README.md"), "w", encoding="utf-8") as f:
+            f.write(model_card_content)
```

### Comparing `span_marker-0.2.0/span_marker/output.py` & `span_marker-0.2.1/span_marker/output.py`

 * *Files identical despite different names*

### Comparing `span_marker-0.2.0/span_marker/tokenizer.py` & `span_marker-0.2.1/span_marker/tokenizer.py`

 * *Files identical despite different names*

### Comparing `span_marker-0.2.0/span_marker/trainer.py` & `span_marker-0.2.1/span_marker/trainer.py`

 * *Files identical despite different names*

### Comparing `span_marker-0.2.0/span_marker.egg-info/PKG-INFO` & `span_marker-0.2.1/span_marker.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: span-marker
-Version: 0.2.0
+Version: 0.2.1
 Summary: Few-Shot Named Entity Recognition using Span Markers
 Author: Tom Aarsen
 Maintainer: Tom Aarsen
 Project-URL: Documentation, https://tomaarsen.github.io/SpanMarkerNER
 Project-URL: Repository, https://github.com/tomaarsen/SpanMarkerNER
 Keywords: data-science,natural-language-processing,artificial-intelligence,mlops,nlp,machine-learning,transformers
 Requires-Python: >=3.7
@@ -83,10 +83,11 @@
 
 Because this work is based on [PL-Marker](https://arxiv.org/pdf/2109.06067v5.pdf), you may expect similar results to its [Papers with Code Leaderboard](https://paperswithcode.com/paper/pack-together-entity-and-relation-extraction) results. Tests, documentation and further information on expected performance will come soon.
 
 ## Pretrained Models
 
 * [`tomaarsen/span-marker-bert-base-fewnerd-fine-super`](https://huggingface.co/tomaarsen/span-marker-bert-base-fewnerd-fine-super) is a model that I have trained in just 4 hours on the finegrained, supervised [Few-NERD dataset](https://huggingface.co/datasets/DFKI-SLT/few-nerd). It reached a 0.7020 Test F1, competitive in the all-time [Few-NERD leaderboard](https://paperswithcode.com/sota/named-entity-recognition-on-few-nerd-sup). My training script resembles the one that you can see above.
   * See this [Weights and Biases report](https://api.wandb.ai/links/tomaarsen/dm21vbbm) for training details.
+  * Try the model out online using this [🤗 Space](https://tomaarsen-span-marker-bert-base-fewnerd-fine-super.hf.space/).
 
 ## Changelog
 See [CHANGELOG.md](CHANGELOG.md) for news on all SpanMarker versions.
```

### Comparing `span_marker-0.2.0/span_marker.egg-info/SOURCES.txt` & `span_marker-0.2.1/span_marker.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -3,14 +3,15 @@
 pyproject.toml
 setup.py
 span_marker/__init__.py
 span_marker/configuration.py
 span_marker/data_collator.py
 span_marker/evaluation.py
 span_marker/label_normalizer.py
+span_marker/model_card.py
 span_marker/modeling.py
 span_marker/output.py
 span_marker/tokenizer.py
 span_marker/trainer.py
 span_marker.egg-info/PKG-INFO
 span_marker.egg-info/SOURCES.txt
 span_marker.egg-info/dependency_links.txt
```

### Comparing `span_marker-0.2.0/tests/test_configuration.py` & `span_marker-0.2.1/tests/test_configuration.py`

 * *Files identical despite different names*

### Comparing `span_marker-0.2.0/tests/test_modeling.py` & `span_marker-0.2.1/tests/test_modeling.py`

 * *Files identical despite different names*

### Comparing `span_marker-0.2.0/tests/test_trainer.py` & `span_marker-0.2.1/tests/test_trainer.py`

 * *Files identical despite different names*

