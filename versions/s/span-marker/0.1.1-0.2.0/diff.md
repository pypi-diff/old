# Comparing `tmp/span_marker-0.1.1.tar.gz` & `tmp/span_marker-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "span_marker-0.1.1.tar", last modified: Fri Mar 31 08:25:52 2023, max compression
+gzip compressed data, was "span_marker-0.2.0.tar", last modified: Thu Apr  6 16:38:24 2023, max compression
```

## Comparing `span_marker-0.1.1.tar` & `span_marker-0.2.0.tar`

### file list

```diff
@@ -1,22 +1,27 @@
-drwxrwxrwx   0        0        0        0 2023-03-31 08:25:52.362422 span_marker-0.1.1/
--rw-rw-rw-   0        0        0     1088 2023-03-28 09:30:50.000000 span_marker-0.1.1/LICENSE
--rw-rw-rw-   0        0        0     3805 2023-03-31 08:25:52.361422 span_marker-0.1.1/PKG-INFO
--rw-rw-rw-   0        0        0     3254 2023-03-31 08:10:07.000000 span_marker-0.1.1/README.md
--rw-rw-rw-   0        0        0     2134 2023-03-30 18:40:21.000000 span_marker-0.1.1/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-03-31 08:25:52.362422 span_marker-0.1.1/setup.cfg
--rw-rw-rw-   0        0        0       41 2023-03-28 09:28:01.000000 span_marker-0.1.1/setup.py
-drwxrwxrwx   0        0        0        0 2023-03-31 08:25:52.350423 span_marker-0.1.1/span_marker/
--rw-rw-rw-   0        0        0      352 2023-03-31 08:24:53.000000 span_marker-0.1.1/span_marker/__init__.py
--rw-rw-rw-   0        0        0     4722 2023-03-30 12:05:00.000000 span_marker-0.1.1/span_marker/configuration.py
--rw-rw-rw-   0        0        0     3727 2023-03-29 13:01:07.000000 span_marker-0.1.1/span_marker/data_collator.py
--rw-rw-rw-   0        0        0     4504 2023-03-31 08:23:37.000000 span_marker-0.1.1/span_marker/evaluation.py
--rw-rw-rw-   0        0        0     4812 2023-03-30 07:38:30.000000 span_marker-0.1.1/span_marker/label_normalizer.py
--rw-rw-rw-   0        0        0    11365 2023-03-30 14:53:23.000000 span_marker-0.1.1/span_marker/modeling.py
--rw-rw-rw-   0        0        0     7027 2023-03-30 14:34:34.000000 span_marker-0.1.1/span_marker/tokenizer.py
--rw-rw-rw-   0        0        0     9591 2023-03-31 07:34:36.000000 span_marker-0.1.1/span_marker/trainer.py
-drwxrwxrwx   0        0        0        0 2023-03-31 08:25:52.361422 span_marker-0.1.1/span_marker.egg-info/
--rw-rw-rw-   0        0        0     3805 2023-03-31 08:25:52.000000 span_marker-0.1.1/span_marker.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      427 2023-03-31 08:25:52.000000 span_marker-0.1.1/span_marker.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-31 08:25:52.000000 span_marker-0.1.1/span_marker.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       89 2023-03-31 08:25:52.000000 span_marker-0.1.1/span_marker.egg-info/requires.txt
--rw-rw-rw-   0        0        0       12 2023-03-31 08:25:52.000000 span_marker-0.1.1/span_marker.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 16:38:24.208481 span_marker-0.2.0/
+-rw-rw-rw-   0        0        0     1088 2023-03-28 09:30:50.000000 span_marker-0.2.0/LICENSE
+-rw-rw-rw-   0        0        0     4282 2023-04-06 16:38:24.207477 span_marker-0.2.0/PKG-INFO
+-rw-rw-rw-   0        0        0     3705 2023-04-06 15:23:05.000000 span_marker-0.2.0/README.md
+-rw-rw-rw-   0        0        0     2305 2023-04-06 15:01:25.000000 span_marker-0.2.0/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-06 16:38:24.208481 span_marker-0.2.0/setup.cfg
+-rw-rw-rw-   0        0        0       41 2023-03-28 09:28:01.000000 span_marker-0.2.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 16:38:24.194916 span_marker-0.2.0/span_marker/
+-rw-rw-rw-   0        0        0      352 2023-04-06 16:37:29.000000 span_marker-0.2.0/span_marker/__init__.py
+-rw-rw-rw-   0        0        0     4825 2023-04-06 07:35:29.000000 span_marker-0.2.0/span_marker/configuration.py
+-rw-rw-rw-   0        0        0     5389 2023-04-06 13:34:33.000000 span_marker-0.2.0/span_marker/data_collator.py
+-rw-rw-rw-   0        0        0     4295 2023-04-06 07:35:29.000000 span_marker-0.2.0/span_marker/evaluation.py
+-rw-rw-rw-   0        0        0     4831 2023-04-06 07:35:29.000000 span_marker-0.2.0/span_marker/label_normalizer.py
+-rw-rw-rw-   0        0        0    18246 2023-04-06 14:00:45.000000 span_marker-0.2.0/span_marker/modeling.py
+-rw-rw-rw-   0        0        0     1686 2023-04-06 14:00:45.000000 span_marker-0.2.0/span_marker/output.py
+-rw-rw-rw-   0        0        0     6313 2023-04-06 09:12:18.000000 span_marker-0.2.0/span_marker/tokenizer.py
+-rw-rw-rw-   0        0        0    11036 2023-04-06 14:00:45.000000 span_marker-0.2.0/span_marker/trainer.py
+drwxrwxrwx   0        0        0        0 2023-04-06 16:38:24.205424 span_marker-0.2.0/span_marker.egg-info/
+-rw-rw-rw-   0        0        0     4282 2023-04-06 16:38:24.000000 span_marker-0.2.0/span_marker.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      522 2023-04-06 16:38:24.000000 span_marker-0.2.0/span_marker.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 16:38:24.000000 span_marker-0.2.0/span_marker.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      182 2023-04-06 16:38:24.000000 span_marker-0.2.0/span_marker.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       12 2023-04-06 16:38:24.000000 span_marker-0.2.0/span_marker.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 16:38:24.207477 span_marker-0.2.0/tests/
+-rw-rw-rw-   0        0        0      961 2023-04-06 07:35:29.000000 span_marker-0.2.0/tests/test_configuration.py
+-rw-rw-rw-   0        0        0     3534 2023-04-06 07:35:29.000000 span_marker-0.2.0/tests/test_modeling.py
+-rw-rw-rw-   0        0        0     3992 2023-04-06 07:35:29.000000 span_marker-0.2.0/tests/test_trainer.py
```

### Comparing `span_marker-0.1.1/LICENSE` & `span_marker-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `span_marker-0.1.1/PKG-INFO` & `span_marker-0.2.0/README.md`

 * *Files 21% similar despite different names*

```diff
@@ -1,38 +1,34 @@
-Metadata-Version: 2.1
-Name: span_marker
-Version: 0.1.1
-Summary: Few-Shot Named Entity Recognition using Span Markers
-Author: Tom Aarsen
-Maintainer: Tom Aarsen
-Project-URL: Homepage, https://github.com/tomaarsen/SpanMarkerNER
-Project-URL: Repository, https://github.com/tomaarsen/SpanMarkerNER
-Keywords: data-science,natural-language-processing,artificial-intelligence,mlops,nlp,machine-learning,transformers
-Requires-Python: >=3.7
-Description-Content-Type: text/markdown
-Provides-Extra: dev
-Provides-Extra: wandb
-License-File: LICENSE
-
-# SpanMarker for Named Entity Recognition
+<h1 align="center">
+SpanMarker for Named Entity Recognition
+</h1>
+<div align="center">
+
+[🤗 Models](https://huggingface.co/models?other=span-marker) |
+[🛠️ Getting Started In Google Colab](https://colab.research.google.com/github/tomaarsen/SpanMarkerNER/blob/main/notebooks/getting_started.ipynb) |
+[📄 Documentation](https://tomaarsen.github.io/SpanMarkerNER)
+</div>
 
 SpanMarker is a framework for training powerful Named Entity Recognition models using familiar encoders such as BERT, RoBERTa and DeBERTa.
 Tightly implemented on top of the [🤗 Transformers](https://github.com/huggingface/transformers/) library, SpanMarker can take advantage of its valuable functionality.
 <!-- like performance dashboard integration, automatic mixed precision, 8-bit inference-->
 
 Based on the [PL-Marker](https://arxiv.org/pdf/2109.06067.pdf) paper, SpanMarker breaks the mold through its accessibility and ease of use. Crucially, SpanMarker works out of the box with many common encoders such as `bert-base-cased` and `roberta-large`, and automatically works with datasets using the `IOB`, `IOB2`, `BIOES`, `BILOU` or no label annotation scheme.
 
+## Documentation
+Feel free to have a look at the [documentation](https://tomaarsen.github.io/SpanMarkerNER).
+
 ## Installation
-You may install the `span_marker` Python module via `pip` like so:
+You may install the [`span_marker`](https://pypi.org/project/span-marker) Python module via `pip` like so:
 ```
 pip install span_marker
 ```
 
 ## Quick Start
-Please have a look at our [Getting Started](examples/getting_started.ipynb) jupyter notebook for details on how SpanMarker is commonly used. That notebook explains the following snippet in more detail.
+Please have a look at our [Getting Started](notebooks/getting_started.ipynb) notebook for details on how SpanMarker is commonly used. It explains the following snippet in more detail.
 
 ```python
 from datasets import load_dataset
 from span_marker import SpanMarkerModel, Trainer
 from transformers import TrainingArguments
 
 dataset = load_dataset("DFKI-SLT/few-nerd", "supervised")
@@ -65,14 +61,16 @@
 trainer.train()
 trainer.save_model("my_span_marker_model/checkpoint-final")
 
 metrics = trainer.evaluate()
 print(metrics)
 ```
 
-For this work is based on [PL-Marker](https://arxiv.org/pdf/2109.06067v5.pdf), you may expect similar results to its [Papers with Code Leaderboard](https://paperswithcode.com/paper/pack-together-entity-and-relation-extraction). Tests, documentation and further information on expected performance will come soon.
+Because this work is based on [PL-Marker](https://arxiv.org/pdf/2109.06067v5.pdf), you may expect similar results to its [Papers with Code Leaderboard](https://paperswithcode.com/paper/pack-together-entity-and-relation-extraction) results. Tests, documentation and further information on expected performance will come soon.
 
 ## Pretrained Models
 
-* [`tomaarsen/span-marker-bert-base-fewnerd-fine-super`](https://huggingface.co/tomaarsen/span-marker-bert-base-fewnerd-fine-super) is a model that I have trained in just 4 hours on the finegrained, supervised [Few-NERD dataset](https://huggingface.co/datasets/DFKI-SLT/few-nerd). It reached a 0.7020 Test F1, competitive in the all-time [Few-NERD leaderboard](https://paperswithcode.com/sota/named-entity-recognition-on-few-nerd-sup).
-See this [Weights and Biases report](https://api.wandb.ai/links/tomaarsen/dm21vbbm) for details. You can observe the model inferences in this [Argilla dataset](https://argilla-span-marker.hf.space/datasets/team/span-marker-bert-base-fewnerd-fine-super) (username: `argilla`, password: `1234`).
+* [`tomaarsen/span-marker-bert-base-fewnerd-fine-super`](https://huggingface.co/tomaarsen/span-marker-bert-base-fewnerd-fine-super) is a model that I have trained in just 4 hours on the finegrained, supervised [Few-NERD dataset](https://huggingface.co/datasets/DFKI-SLT/few-nerd). It reached a 0.7020 Test F1, competitive in the all-time [Few-NERD leaderboard](https://paperswithcode.com/sota/named-entity-recognition-on-few-nerd-sup). My training script resembles the one that you can see above.
+  * See this [Weights and Biases report](https://api.wandb.ai/links/tomaarsen/dm21vbbm) for training details.
 
+## Changelog
+See [CHANGELOG.md](CHANGELOG.md) for news on all SpanMarker versions.
```

### Comparing `span_marker-0.1.1/README.md` & `span_marker-0.2.0/PKG-INFO`

 * *Files 21% similar despite different names*

```diff
@@ -1,23 +1,50 @@
-# SpanMarker for Named Entity Recognition
+Metadata-Version: 2.1
+Name: span_marker
+Version: 0.2.0
+Summary: Few-Shot Named Entity Recognition using Span Markers
+Author: Tom Aarsen
+Maintainer: Tom Aarsen
+Project-URL: Documentation, https://tomaarsen.github.io/SpanMarkerNER
+Project-URL: Repository, https://github.com/tomaarsen/SpanMarkerNER
+Keywords: data-science,natural-language-processing,artificial-intelligence,mlops,nlp,machine-learning,transformers
+Requires-Python: >=3.7
+Description-Content-Type: text/markdown
+Provides-Extra: dev
+Provides-Extra: docs
+Provides-Extra: wandb
+License-File: LICENSE
+
+<h1 align="center">
+SpanMarker for Named Entity Recognition
+</h1>
+<div align="center">
+
+[🤗 Models](https://huggingface.co/models?other=span-marker) |
+[🛠️ Getting Started In Google Colab](https://colab.research.google.com/github/tomaarsen/SpanMarkerNER/blob/main/notebooks/getting_started.ipynb) |
+[📄 Documentation](https://tomaarsen.github.io/SpanMarkerNER)
+</div>
 
 SpanMarker is a framework for training powerful Named Entity Recognition models using familiar encoders such as BERT, RoBERTa and DeBERTa.
 Tightly implemented on top of the [🤗 Transformers](https://github.com/huggingface/transformers/) library, SpanMarker can take advantage of its valuable functionality.
 <!-- like performance dashboard integration, automatic mixed precision, 8-bit inference-->
 
 Based on the [PL-Marker](https://arxiv.org/pdf/2109.06067.pdf) paper, SpanMarker breaks the mold through its accessibility and ease of use. Crucially, SpanMarker works out of the box with many common encoders such as `bert-base-cased` and `roberta-large`, and automatically works with datasets using the `IOB`, `IOB2`, `BIOES`, `BILOU` or no label annotation scheme.
 
+## Documentation
+Feel free to have a look at the [documentation](https://tomaarsen.github.io/SpanMarkerNER).
+
 ## Installation
-You may install the `span_marker` Python module via `pip` like so:
+You may install the [`span_marker`](https://pypi.org/project/span-marker) Python module via `pip` like so:
 ```
 pip install span_marker
 ```
 
 ## Quick Start
-Please have a look at our [Getting Started](examples/getting_started.ipynb) jupyter notebook for details on how SpanMarker is commonly used. That notebook explains the following snippet in more detail.
+Please have a look at our [Getting Started](notebooks/getting_started.ipynb) notebook for details on how SpanMarker is commonly used. It explains the following snippet in more detail.
 
 ```python
 from datasets import load_dataset
 from span_marker import SpanMarkerModel, Trainer
 from transformers import TrainingArguments
 
 dataset = load_dataset("DFKI-SLT/few-nerd", "supervised")
@@ -50,14 +77,16 @@
 trainer.train()
 trainer.save_model("my_span_marker_model/checkpoint-final")
 
 metrics = trainer.evaluate()
 print(metrics)
 ```
 
-For this work is based on [PL-Marker](https://arxiv.org/pdf/2109.06067v5.pdf), you may expect similar results to its [Papers with Code Leaderboard](https://paperswithcode.com/paper/pack-together-entity-and-relation-extraction). Tests, documentation and further information on expected performance will come soon.
+Because this work is based on [PL-Marker](https://arxiv.org/pdf/2109.06067v5.pdf), you may expect similar results to its [Papers with Code Leaderboard](https://paperswithcode.com/paper/pack-together-entity-and-relation-extraction) results. Tests, documentation and further information on expected performance will come soon.
 
 ## Pretrained Models
 
-* [`tomaarsen/span-marker-bert-base-fewnerd-fine-super`](https://huggingface.co/tomaarsen/span-marker-bert-base-fewnerd-fine-super) is a model that I have trained in just 4 hours on the finegrained, supervised [Few-NERD dataset](https://huggingface.co/datasets/DFKI-SLT/few-nerd). It reached a 0.7020 Test F1, competitive in the all-time [Few-NERD leaderboard](https://paperswithcode.com/sota/named-entity-recognition-on-few-nerd-sup).
-See this [Weights and Biases report](https://api.wandb.ai/links/tomaarsen/dm21vbbm) for details. You can observe the model inferences in this [Argilla dataset](https://argilla-span-marker.hf.space/datasets/team/span-marker-bert-base-fewnerd-fine-super) (username: `argilla`, password: `1234`).
+* [`tomaarsen/span-marker-bert-base-fewnerd-fine-super`](https://huggingface.co/tomaarsen/span-marker-bert-base-fewnerd-fine-super) is a model that I have trained in just 4 hours on the finegrained, supervised [Few-NERD dataset](https://huggingface.co/datasets/DFKI-SLT/few-nerd). It reached a 0.7020 Test F1, competitive in the all-time [Few-NERD leaderboard](https://paperswithcode.com/sota/named-entity-recognition-on-few-nerd-sup). My training script resembles the one that you can see above.
+  * See this [Weights and Biases report](https://api.wandb.ai/links/tomaarsen/dm21vbbm) for training details.
 
+## Changelog
+See [CHANGELOG.md](CHANGELOG.md) for news on all SpanMarker versions.
```

### Comparing `span_marker-0.1.1/pyproject.toml` & `span_marker-0.2.0/pyproject.toml`

 * *Files 26% similar despite different names*

```diff
@@ -32,37 +32,49 @@
 ]
 dynamic = ["version"]
 
 [project.optional-dependencies]
 dev = [
     "pre-commit",
     "ruff",
-    "black"
+    "black",
+    "pytest",
+    "pytest-cov"
+]
+docs = [
+    "nltk_theme",
+    "sphinx",
+    "m2r2",
+    "better-apidoc",
+    "nbsphinx",
+    "nbconvert<7",
+    "pandoc<3"
 ]
 wandb = [
     "wandb"
 ]
 
 [project.urls]
-Homepage = "https://github.com/tomaarsen/SpanMarkerNER"
+Documentation = "https://tomaarsen.github.io/SpanMarkerNER"
 Repository = "https://github.com/tomaarsen/SpanMarkerNER"
 
 [tool.setuptools.packages.find]
 include = ["span_marker"]
 
 [tool.setuptools.dynamic]
 version = {attr = "span_marker.__version__"}
 
 [tool.pytest.ini_options]
-log_format = "%(asctime)s %(name)s %(levelname)s %(message)s"
-log_date_format = "%Y-%m-%d %H:%M:%S"
-log_cli = "True"
 testpaths = [
     "tests"
 ]
+filterwarnings = [
+    "ignore::DeprecationWarning:tensorboard.*:"
+]
+addopts = "--cov=span_marker --durations=10"
 
 [tool.coverage.report]
 exclude_lines = [
     "pragma: no cover",
     "def __repr__",
     "def __str__",
     "raise AssertionError",
```

### Comparing `span_marker-0.1.1/span_marker/configuration.py` & `span_marker-0.2.0/span_marker/configuration.py`

 * *Files 21% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 from typing import Any, Dict, Iterable, Optional, Set, Union
 
 from transformers import PretrainedConfig
 
 
 class SpanMarkerConfig(PretrainedConfig):
     model_type: str = "span-marker"
+    is_composition = True
 
     def __init__(
         self,
         encoder_config: Optional[Dict[str, Any]] = None,
         model_max_length: Optional[int] = None,
         marker_max_length: int = 256,
         entity_max_length: int = 16,
@@ -17,62 +18,57 @@
     ) -> None:
         self.encoder = encoder_config
         self.model_max_length = model_max_length
         self.model_max_length_default = 512
         self.marker_max_length = marker_max_length
         self.entity_max_length = entity_max_length
         super().__init__(**kwargs)
-        # These are automatically set by super().__init__, but we want to rely on
-        # the encoder configs instead if we can, so we delete them.
-        del self.id2label
-        del self.label2id
 
-        if encoder_config is None:
-            return
-
-        # If the id2label of the encoder is not overridden
-        if self.id2label == {0: "LABEL_0", 1: "LABEL_1"}:
-            raise ValueError(
-                "Please provide a `labels` list to `SpanMarkerModel.from_pretrained()`, e.g.\n"
-                ">>> SpanMarkerModel.from_pretrained(\n"
-                '...     "roberta-large",\n'
-                '...     labels=["O", "B-PER", "I-PER", "B-ORG", "I-ORG", ...]\n'
-                "... )\n"
-                "or\n"
-                ">>> SpanMarkerModel.from_pretrained(\n"
-                '...     "roberta-large",\n'
-                '...     labels=["O", "PER", "ORG", "LOC", "MISC"]\n'
-                "... )"
-            )
-
-        if self.id2label and "O" not in self.label2id:
-            raise Exception("There must be an 'O' label.")
-
-        # TODO: Consider converting this into several properties
-        if self.are_labels_schemed():
+        # label2id and id2label are automatically set by super().__init__, but we want to rely on
+        # the encoder configs instead if we can, so we delete them under two conditions
+        # 1. if they're the default ({0: "LABEL_0", 1: "LABEL_1"})
+        # 2. if they're identical to the encoder label2id
+        span_marker_label2id = super().__getattribute__("label2id")
+        if span_marker_label2id == {"LABEL_0": 0, "LABEL_1": 1} or span_marker_label2id == self.encoder.get("label2id"):
+            del self.id2label
+            del self.label2id
+
+        # We need the "O" label for label normalization, etc.
+        if self.label2id and "O" not in self.label2id:
+            raise ValueError("There must be an 'O' label in the list of `labels`.")
+
+        # Keys are always strings in JSON so convert ids to int here.
+        self.encoder["id2label"] = {int(label_id): label for label_id, label in self.encoder["id2label"].items()}
+        if hasattr(self, "id2reduced_id"):
+            self.id2reduced_id = {int(label_id): reduced_id for label_id, reduced_id in self.id2reduced_id.items()}
+        elif self.are_labels_schemed():
             reduced_labels = {label[2:] for label in self.label2id.keys() if label != "O"}
             reduced_labels = ["O"] + sorted(reduced_labels)
             self.id2reduced_id = {
                 _id: reduced_labels.index(label[2:] if label != "O" else label) for label, _id in self.label2id.items()
             }
             self.id2label = dict(enumerate(reduced_labels))
             self.label2id = {v: k for k, v in self.id2label.items()}
-            self.outside_id = 0
-        else:
-            self.outside_id = self.label2id["O"]
+
+    @property
+    def outside_id(self) -> None:
+        return self.label2id["O"]
 
     def __setattr__(self, name, value) -> None:
         """Whenever the vocab_size is updated, update it for both the SpanMarkerConfig and the
         underlying encoder config.
         """
         if name == "vocab_size":
             self.encoder[name] = value
+        # `outside_id` is now a property instead.
+        if name == "outside_id":
+            return
         return super().__setattr__(name, value)
 
-    def __getattribute__(self, key: str):
+    def __getattribute__(self, key: str) -> Any:
         try:
             return super().__getattribute__(key)
         except AttributeError as e:
             try:
                 return super().__getattribute__("encoder")[key]
             except KeyError:
                 raise e
```

### Comparing `span_marker-0.1.1/span_marker/evaluation.py` & `span_marker-0.2.0/span_marker/evaluation.py`

 * *Files 4% similar despite different names*

```diff
@@ -49,17 +49,15 @@
             }
         else:
             sample_dict[token_hash]["gold_labels"] += gold_labels[sample_idx].tolist()
             sample_dict[token_hash]["pred_labels"] += pred_labels[sample_idx].tolist()
             sample_dict[token_hash]["scores"] += scores[sample_idx].tolist()
 
     outside_id = tokenizer.config.outside_id
-    id2label = {int(label_id): label for label_id, label in tokenizer.config.id2label.items()}
-    if tokenizer.config.are_labels_schemed():
-        id2label = {label_id: id2label[tokenizer.config.id2reduced_id[label_id]] for label_id in id2label}
+    id2label = tokenizer.config.id2label
     # seqeval works wonders for NER evaluation
     seqeval = evaluate.load("seqeval")
     for sample in sample_dict.values():
         spans = sample["spans"]
         scores = sample["scores"]
         num_words = sample["num_words"]
         gold_labels = sample["gold_labels"]
```

### Comparing `span_marker-0.1.1/span_marker/label_normalizer.py` & `span_marker-0.2.0/span_marker/label_normalizer.py`

 * *Files 1% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 
     def __init__(self, config: SpanMarkerConfig) -> None:
         super().__init__()
         self.config = config
 
     @abstractmethod
     def __call__(self, ner_tags: List[int]) -> Dict[str, List[Any]]:
-        return
+        raise NotImplementedError
 
 
 class LabelNormalizerScheme(LabelNormalizer):
     def __init__(self, config: SpanMarkerConfig) -> None:
         super().__init__(config)
         self.label_ids_by_tag = self.config.group_label_ids_by_tag()
         self.start_ids = set()
```

### Comparing `span_marker-0.1.1/span_marker/tokenizer.py` & `span_marker-0.2.0/span_marker/tokenizer.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,59 +1,51 @@
 import itertools
 import os
 import warnings
-from typing import Dict, Iterator, List, Tuple, Union
+from typing import Any, Dict, Iterator, List, Tuple, Union
 
 from transformers import AutoTokenizer, PreTrainedTokenizer
 
 from span_marker.configuration import SpanMarkerConfig
 
 
 class SpanMarkerTokenizer:
-    # def __init__(self, model: SpanMarkerModel, tokenizer: PreTrainedTokenizer, **kwargs):
     def __init__(self, tokenizer: PreTrainedTokenizer, config: SpanMarkerConfig, **kwargs) -> None:
-        # super().__init__(**kwargs)
-        # self.model = model
         self.tokenizer = tokenizer
         self.config = config
 
         tokenizer.add_tokens(["<start>", "<end>"], special_tokens=True)
-        # tokenizer.add_special_tokens({"additional_special_tokens": ["<start>", "<end>"]})
         self.start_marker_id, self.end_marker_id = self.tokenizer.convert_tokens_to_ids(["<start>", "<end>"])
-        # self.start_marker_id, self.end_marker_id = self.tokenizer.convert_tokens_to_ids(['madeupword0000', 'madeupword0001'])
-
-        # TODO: This could be done more cleverly. Perhaps I can just subclass PreTrainedTokenizerFast?
-        # I'm concerned about .from_pretrained not initializing a SpanMarkerTokenizer though.
 
         if self.tokenizer.model_max_length > 1e29 and self.config.model_max_length is None:
             warnings.warn(
-                f"Base {self.tokenizer.__class__.__name__} nor {self.config.__class__.__name__} specify"
-                f" `model_max_length`: defaulting to {self.model_max_length_default} tokens."
+                f"The underlying {self.tokenizer.__class__.__name__!r} tokenizer nor {self.config.__class__.__name__!r}"
+                f" specify `model_max_length`: defaulting to {self.config.model_max_length_default} tokens."
             )
         self.model_max_length = min(
             self.tokenizer.model_max_length, self.config.model_max_length or self.config.model_max_length_default
         )
-        self.pad = tokenizer.pad
-        self.save_pretrained = tokenizer.save_pretrained
-        self.push_to_hub = tokenizer.push_to_hub
-        self.decode = tokenizer.decode
-        self.pad_token_id = self.tokenizer.pad_token_id
-        self.eos_token_id = self.tokenizer.eos_token_id
 
     def get_all_valid_spans(self, num_words: int, entity_max_length: int) -> Iterator[Tuple[int, int]]:
         for start_idx in range(num_words):
             for end_idx in range(start_idx + 1, min(num_words + 1, start_idx + 1 + entity_max_length)):
                 yield (start_idx, end_idx)
 
     def get_all_valid_spans_and_labels(
         self, num_words: int, span_to_label: Dict[Tuple[int, int], int], entity_max_length: int, outside_id: int
     ) -> Iterator[Tuple[Tuple[int, int], int]]:
         for span in self.get_all_valid_spans(num_words, entity_max_length):
             yield span, span_to_label.get(span, outside_id)
 
+    def __getattribute__(self, key: str) -> Any:
+        try:
+            return super().__getattribute__(key)
+        except AttributeError:
+            return super().__getattribute__("tokenizer").__getattribute__(key)
+
     def __call__(
         self, inputs, labels=None, return_num_words: bool = False, return_batch_encoding=False, **kwargs
     ) -> Dict[str, List]:
         # TODO: Increase robustness of this
         is_split_into_words = True
         if isinstance(inputs, str) or (inputs and " " in inputs[0]):
             is_split_into_words = False
@@ -135,12 +127,11 @@
         return output
 
     def __len__(self) -> int:
         return len(self.tokenizer)
 
     @classmethod
     def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], *inputs, config=None, **kwargs):
-        # TODO: Consider subclassing an AutoTokenizer directly instead of loading one like this:
         tokenizer = AutoTokenizer.from_pretrained(
             pretrained_model_name_or_path, *inputs, **kwargs, add_prefix_space=True
         )
         return cls(tokenizer, config=config, **kwargs)
```

### Comparing `span_marker-0.1.1/span_marker/trainer.py` & `span_marker-0.2.0/span_marker/trainer.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,60 +1,61 @@
+import warnings
 from typing import Callable, Dict, List, Optional, Tuple
 
 import torch
 from datasets import Dataset
+from torch.utils.data import DataLoader
 from transformers import (
     EvalPrediction,
     TrainerCallback,
     TrainingArguments,
 )
-from transformers import (
-    Trainer as TransformersTrainer,
-)
+from transformers import Trainer as TransformersTrainer
+from transformers.trainer_utils import PredictionOutput
 
 from span_marker.evaluation import compute_f1_via_seqeval
 from span_marker.label_normalizer import AutoLabelNormalizer, LabelNormalizer
 from span_marker.modeling import SpanMarkerModel
 from span_marker.tokenizer import SpanMarkerTokenizer
 
 
 class Trainer(TransformersTrainer):
     """
     Trainer is a simple but feature-complete training and eval loop for SpanMarker,
-    built tightly on top of the 🤗 Transformers Trainer.
+    built tightly on top of the 🤗 Transformers `Trainer <https://huggingface.co/docs/transformers/main_classes/trainer>`_.
 
     Args:
-        model (`SpanMarkerModel`, *optional*):
+        model (Optional[SpanMarkerModel]):
             The model to train, evaluate or use for predictions. If not provided, a `model_init` must be passed.
-        args (`TrainingArguments`, *optional*):
+        args (Optional[TrainingArguments]):
             The arguments to tweak for training. Will default to a basic instance of [`TrainingArguments`] with the
             `output_dir` set to a directory named *tmp_trainer* in the current directory if not provided.
-        train_dataset (`datasets.Dataset`, *optional*):
+        train_dataset (Optional[datasets.Dataset]):
             The dataset to use for training.
-        eval_dataset (`datasets.Dataset`, *optional*):
+        eval_dataset (Optional[datasets.Dataset]):
              The dataset to use for evaluation.
-        model_init (`Callable[[], SpanMarkerModel]`, *optional*):
+        model_init (Optional[Callable[[], SpanMarkerModel]]):
             A function that instantiates the model to be used. If provided, each call to `Trainer.train` will start
             from a new instance of the model as given by this function.
 
             The function may have zero argument, or a single one containing the optuna/Ray Tune/SigOpt trial object, to
             be able to choose different architectures according to hyper parameters (such as layer count, sizes of
             inner layers, dropout probabilities etc).
-        compute_metrics (`Callable[[EvalPrediction], Dict]`, *optional*):
+        compute_metrics (Optional[Callable[[EvalPrediction], Dict]]):
             The function that will be used to compute metrics at evaluation. Must take a [`EvalPrediction`] and return
             a dictionary string to metric values.
-        callbacks (List of [`TrainerCallback`], *optional*):
+        callbacks (Optional[List[TrainerCallback]]):
             A list of callbacks to customize the training loop. Will add those to the list of default callbacks
             detailed in [here](https://huggingface.co/docs/transformers/main/en/main_classes/callback).
 
             If you want to remove one of the default callbacks used, use the [`Trainer.remove_callback`] method.
-        optimizers (`Tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LambdaLR]`, *optional*): A tuple
+        optimizers (Tuple[Optional[torch.optim.Optimizer], Optional[torch.optim.lr_scheduler.LambdaLR]]): A tuple
             containing the optimizer and the scheduler to use. Will default to an instance of `AdamW` on your model
             and a scheduler given by `get_linear_schedule_with_warmup` controlled by `args`.
-        preprocess_logits_for_metrics (`Callable[[torch.Tensor, torch.Tensor], torch.Tensor]`, *optional*):
+        preprocess_logits_for_metrics (Optional[Callable[[torch.Tensor, torch.Tensor], torch.Tensor]]):
             A function that preprocess the logits right before caching them at each evaluation step. Must take two
             tensors, the logits and the labels, and return the logits once processed as desired. The modifications made
             by this function will be reflected in the predictions received by `compute_metrics`.
 
             Note that the labels (second parameter) will be `None` if the dataset does not have them.
 
     Important attributes:
@@ -71,63 +72,56 @@
           `TrainingArguments.place_model_on_device` is overridden to return `False` .
         - **is_in_train** -- Whether or not a model is currently running `train` (e.g. when `evaluate` is called while
           in `train`)
     """
 
     def __init__(
         self,
-        model: SpanMarkerModel = None,
-        args: TrainingArguments = None,
+        model: Optional[SpanMarkerModel] = None,
+        args: Optional[TrainingArguments] = None,
         train_dataset: Optional[Dataset] = None,
         eval_dataset: Optional[Dataset] = None,
         model_init: Callable[[], SpanMarkerModel] = None,
         compute_metrics: Optional[Callable[[EvalPrediction], Dict]] = None,
         callbacks: Optional[List[TrainerCallback]] = None,
-        optimizers: Tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LambdaLR] = (None, None),
-        preprocess_logits_for_metrics: Callable[[torch.Tensor, torch.Tensor], torch.Tensor] = None,
+        optimizers: Tuple[Optional[torch.optim.Optimizer], Optional[torch.optim.lr_scheduler.LambdaLR]] = (None, None),
+        preprocess_logits_for_metrics: Optional[Callable[[torch.Tensor, torch.Tensor], torch.Tensor]] = None,
     ) -> None:
         # Extract the model from an initializer function
         if model_init:
             self.model_init = model_init
             model = self.call_model_init()
 
         # To convert dataset labels to a common format (list of label-start-end tuples)
-        label_normalizer = AutoLabelNormalizer.from_config(model.config)
-        # Normalize labels & tokenize the provided datasets
-        if train_dataset:
-            train_dataset = self.preprocess_dataset(train_dataset, label_normalizer, model.tokenizer)
-        if eval_dataset:
-            eval_dataset = self.preprocess_dataset(
-                eval_dataset, label_normalizer, model.tokenizer, dataset_name="eval", is_evaluate=True
-            )
+        self.label_normalizer = AutoLabelNormalizer.from_config(model.config)
 
         # Set some Training arguments that must be set for SpanMarker
         if args is None:
             args = TrainingArguments(output_dir="models/my_span_marker_model")
         args.include_inputs_for_metrics = True
         args.remove_unused_columns = False
 
         # Always compute `compute_f1_via_seqeval` - optionally compute user-provided metrics
         if compute_metrics is not None:
-            compute_metrics = lambda eval_prediction: {
+            compute_metrics_func = lambda eval_prediction: {
                 **compute_f1_via_seqeval(model.tokenizer, eval_prediction),
                 **compute_metrics(eval_prediction),
             }
         else:
-            compute_metrics = lambda eval_prediction: compute_f1_via_seqeval(model.tokenizer, eval_prediction)
+            compute_metrics_func = lambda eval_prediction: compute_f1_via_seqeval(model.tokenizer, eval_prediction)
 
         super().__init__(
             model=model,
             args=args,
             data_collator=model.data_collator,
             train_dataset=train_dataset,
             eval_dataset=eval_dataset,
             tokenizer=model.tokenizer,
             model_init=None,
-            compute_metrics=compute_metrics,
+            compute_metrics=compute_metrics_func,
             callbacks=callbacks,
             optimizers=optimizers,
             preprocess_logits_for_metrics=preprocess_logits_for_metrics,
         )
         # We have to provide the __init__ with None for model_init and then override it here again
         # We do this because we need `model` to already be defined in this SpanMarker Trainer class
         # and the Transformers Trainer would complain if we provide both a model and a model_init
@@ -174,7 +168,39 @@
         dataset = dataset.map(
             lambda batch: tokenizer(batch["tokens"], labels=batch["ner_tags"], return_num_words=is_evaluate),
             batched=True,
             remove_columns=dataset.column_names,
             desc=f"Tokenizing the {dataset_name} dataset",
         )
         return dataset
+
+    def get_train_dataloader(self) -> DataLoader:
+        """Return the preprocessed training DataLoader."""
+        self.train_dataset = self.preprocess_dataset(self.train_dataset, self.label_normalizer, self.tokenizer)
+        return super().get_train_dataloader()
+
+    def get_eval_dataloader(self, eval_dataset: Optional[Dataset] = None) -> DataLoader:
+        """Return the preprocessed evaluation DataLoader."""
+        eval_dataset = eval_dataset or self.eval_dataset
+        if eval_dataset is not None:
+            eval_dataset = self.preprocess_dataset(
+                eval_dataset, self.label_normalizer, self.tokenizer, dataset_name="evaluation", is_evaluate=True
+            )
+        return super().get_eval_dataloader(eval_dataset)
+
+    def get_test_dataloader(self, test_dataset: Dataset) -> DataLoader:
+        """Return the preprocessed evaluation DataLoader."""
+        test_dataset = self.preprocess_dataset(
+            test_dataset, self.label_normalizer, self.tokenizer, dataset_name="test", is_evaluate=True
+        )
+        return super().get_test_dataloader(test_dataset)
+
+    def predict(
+        self, test_dataset: Dataset, ignore_keys: Optional[List[str]] = None, metric_key_prefix: str = "test"
+    ) -> PredictionOutput:
+        warnings.warn(
+            f"`Trainer.predict` is not recommended for a {self.model.__class__.__name__}. "
+            f"Consider using `{self.model.__class__.__name__}.predict` instead.",
+            UserWarning,
+            stacklevel=2,
+        )
+        return super().predict(test_dataset, ignore_keys, metric_key_prefix)
```

### Comparing `span_marker-0.1.1/span_marker.egg-info/PKG-INFO` & `span_marker-0.2.0/span_marker.egg-info/PKG-INFO`

 * *Files 23% similar despite different names*

```diff
@@ -1,38 +1,50 @@
 Metadata-Version: 2.1
 Name: span-marker
-Version: 0.1.1
+Version: 0.2.0
 Summary: Few-Shot Named Entity Recognition using Span Markers
 Author: Tom Aarsen
 Maintainer: Tom Aarsen
-Project-URL: Homepage, https://github.com/tomaarsen/SpanMarkerNER
+Project-URL: Documentation, https://tomaarsen.github.io/SpanMarkerNER
 Project-URL: Repository, https://github.com/tomaarsen/SpanMarkerNER
 Keywords: data-science,natural-language-processing,artificial-intelligence,mlops,nlp,machine-learning,transformers
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 Provides-Extra: dev
+Provides-Extra: docs
 Provides-Extra: wandb
 License-File: LICENSE
 
-# SpanMarker for Named Entity Recognition
+<h1 align="center">
+SpanMarker for Named Entity Recognition
+</h1>
+<div align="center">
+
+[🤗 Models](https://huggingface.co/models?other=span-marker) |
+[🛠️ Getting Started In Google Colab](https://colab.research.google.com/github/tomaarsen/SpanMarkerNER/blob/main/notebooks/getting_started.ipynb) |
+[📄 Documentation](https://tomaarsen.github.io/SpanMarkerNER)
+</div>
 
 SpanMarker is a framework for training powerful Named Entity Recognition models using familiar encoders such as BERT, RoBERTa and DeBERTa.
 Tightly implemented on top of the [🤗 Transformers](https://github.com/huggingface/transformers/) library, SpanMarker can take advantage of its valuable functionality.
 <!-- like performance dashboard integration, automatic mixed precision, 8-bit inference-->
 
 Based on the [PL-Marker](https://arxiv.org/pdf/2109.06067.pdf) paper, SpanMarker breaks the mold through its accessibility and ease of use. Crucially, SpanMarker works out of the box with many common encoders such as `bert-base-cased` and `roberta-large`, and automatically works with datasets using the `IOB`, `IOB2`, `BIOES`, `BILOU` or no label annotation scheme.
 
+## Documentation
+Feel free to have a look at the [documentation](https://tomaarsen.github.io/SpanMarkerNER).
+
 ## Installation
-You may install the `span_marker` Python module via `pip` like so:
+You may install the [`span_marker`](https://pypi.org/project/span-marker) Python module via `pip` like so:
 ```
 pip install span_marker
 ```
 
 ## Quick Start
-Please have a look at our [Getting Started](examples/getting_started.ipynb) jupyter notebook for details on how SpanMarker is commonly used. That notebook explains the following snippet in more detail.
+Please have a look at our [Getting Started](notebooks/getting_started.ipynb) notebook for details on how SpanMarker is commonly used. It explains the following snippet in more detail.
 
 ```python
 from datasets import load_dataset
 from span_marker import SpanMarkerModel, Trainer
 from transformers import TrainingArguments
 
 dataset = load_dataset("DFKI-SLT/few-nerd", "supervised")
@@ -65,14 +77,16 @@
 trainer.train()
 trainer.save_model("my_span_marker_model/checkpoint-final")
 
 metrics = trainer.evaluate()
 print(metrics)
 ```
 
-For this work is based on [PL-Marker](https://arxiv.org/pdf/2109.06067v5.pdf), you may expect similar results to its [Papers with Code Leaderboard](https://paperswithcode.com/paper/pack-together-entity-and-relation-extraction). Tests, documentation and further information on expected performance will come soon.
+Because this work is based on [PL-Marker](https://arxiv.org/pdf/2109.06067v5.pdf), you may expect similar results to its [Papers with Code Leaderboard](https://paperswithcode.com/paper/pack-together-entity-and-relation-extraction) results. Tests, documentation and further information on expected performance will come soon.
 
 ## Pretrained Models
 
-* [`tomaarsen/span-marker-bert-base-fewnerd-fine-super`](https://huggingface.co/tomaarsen/span-marker-bert-base-fewnerd-fine-super) is a model that I have trained in just 4 hours on the finegrained, supervised [Few-NERD dataset](https://huggingface.co/datasets/DFKI-SLT/few-nerd). It reached a 0.7020 Test F1, competitive in the all-time [Few-NERD leaderboard](https://paperswithcode.com/sota/named-entity-recognition-on-few-nerd-sup).
-See this [Weights and Biases report](https://api.wandb.ai/links/tomaarsen/dm21vbbm) for details. You can observe the model inferences in this [Argilla dataset](https://argilla-span-marker.hf.space/datasets/team/span-marker-bert-base-fewnerd-fine-super) (username: `argilla`, password: `1234`).
+* [`tomaarsen/span-marker-bert-base-fewnerd-fine-super`](https://huggingface.co/tomaarsen/span-marker-bert-base-fewnerd-fine-super) is a model that I have trained in just 4 hours on the finegrained, supervised [Few-NERD dataset](https://huggingface.co/datasets/DFKI-SLT/few-nerd). It reached a 0.7020 Test F1, competitive in the all-time [Few-NERD leaderboard](https://paperswithcode.com/sota/named-entity-recognition-on-few-nerd-sup). My training script resembles the one that you can see above.
+  * See this [Weights and Biases report](https://api.wandb.ai/links/tomaarsen/dm21vbbm) for training details.
 
+## Changelog
+See [CHANGELOG.md](CHANGELOG.md) for news on all SpanMarker versions.
```

