# Comparing `tmp/so_vits_svc_fork-3.0.3.tar.gz` & `tmp/so_vits_svc_fork-3.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "so_vits_svc_fork-3.0.3.tar", max compression
+gzip compressed data, was "so_vits_svc_fork-3.0.4.tar", max compression
```

## Comparing `so_vits_svc_fork-3.0.3.tar` & `so_vits_svc_fork-3.0.4.tar`

### file list

```diff
@@ -1,51 +1,51 @@
--rw-r--r--   0        0        0    12463 2023-04-05 02:18:02.739768 so_vits_svc_fork-3.0.3/LICENSE
--rw-r--r--   0        0        0    17966 2023-04-05 02:18:02.739768 so_vits_svc_fork-3.0.3/README.md
--rw-r--r--   0        0        0     3073 2023-04-05 02:18:03.759776 so_vits_svc_fork-3.0.3/pyproject.toml
--rw-r--r--   0        0        0       70 2023-04-05 02:18:03.711775 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/__init__.py
--rw-r--r--   0        0        0    22647 2023-04-05 02:18:02.739768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/__main__.py
--rw-r--r--   0        0        0     1275 2023-04-05 02:18:02.739768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/cluster/__init__.py
--rw-r--r--   0        0        0     2659 2023-04-05 02:18:02.739768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/cluster/train_cluster.py
--rw-r--r--   0        0        0     2804 2023-04-05 02:18:02.739768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/data_utils.py
--rw-r--r--   0        0        0     2454 2023-04-05 02:18:02.739768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/default_gui_presets.json
--rw-r--r--   0        0        0     7215 2023-04-05 02:18:02.739768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/f0.py
--rw-r--r--   0        0        0    24882 2023-04-05 02:18:02.739768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/gui.py
--rw-r--r--   0        0        0      864 2023-04-05 02:18:02.739768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/hparams.py
--rw-r--r--   0        0        0        0 2023-04-05 02:18:02.739768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/inference/__init__.py
--rw-r--r--   0        0        0    22942 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/inference/core.py
--rw-r--r--   0        0        0     7491 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/inference/main.py
--rw-r--r--   0        0        0      731 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/logger.py
--rw-r--r--   0        0        0        0 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/__init__.py
--rw-r--r--   0        0        0    16683 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/attentions.py
--rw-r--r--   0        0        0     5854 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/commons.py
--rw-r--r--   0        0        0        0 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/__init__.py
--rw-r--r--   0        0        0     1419 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/f0.py
--rw-r--r--   0        0        0       56 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/hifigan/__init__.py
--rw-r--r--   0        0        0    11608 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/hifigan/_models.py
--rw-r--r--   0        0        0      340 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/hifigan/_utils.py
--rw-r--r--   0        0        0      318 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/mb_istft/__init__.py
--rw-r--r--   0        0        0    12479 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/mb_istft/_generators.py
--rw-r--r--   0        0        0      419 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/mb_istft/_loss.py
--rw-r--r--   0        0        0     4755 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/mb_istft/_pqmf.py
--rw-r--r--   0        0        0     9055 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/mb_istft/_stft.py
--rw-r--r--   0        0        0     4879 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/mb_istft/_stft_loss.py
--rw-r--r--   0        0        0     5604 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/descriminators.py
--rw-r--r--   0        0        0     4400 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/encoders.py
--rw-r--r--   0        0        0     1390 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/flows.py
--rw-r--r--   0        0        0     1405 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/losses.py
--rw-r--r--   0        0        0     5753 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/mel_processing.py
--rw-r--r--   0        0        0    14435 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/modules.py
--rw-r--r--   0        0        0     8158 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/synthesizers.py
--rw-r--r--   0        0        0        0 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/__init__.py
--rw-r--r--   0        0        0     1604 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/config_templates/quickvc.json
--rw-r--r--   0        0        0     1354 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/config_templates/so-vits-svc-4.0v1-legacy.json
--rw-r--r--   0        0        0     1415 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/config_templates/so-vits-svc-4.0v1.json
--rw-r--r--   0        0        0     2997 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/preprocess_flist_config.py
--rw-r--r--   0        0        0     4566 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/preprocess_hubert_f0.py
--rw-r--r--   0        0        0     4693 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/preprocess_resample.py
--rw-r--r--   0        0        0     2948 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/preprocess_speaker_diarization.py
--rw-r--r--   0        0        0     1878 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/preprocess_split.py
--rw-r--r--   0        0        0      126 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/preprocess_utils.py
--rw-r--r--   0        0        0        0 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/py.typed
--rw-r--r--   0        0        0    14601 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/train.py
--rw-r--r--   0        0        0    12981 2023-04-05 02:18:02.743768 so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/utils.py
--rw-r--r--   0        0        0    19861 1970-01-01 00:00:00.000000 so_vits_svc_fork-3.0.3/PKG-INFO
+-rw-r--r--   0        0        0    12463 2023-04-06 15:32:50.425493 so_vits_svc_fork-3.0.4/LICENSE
+-rw-r--r--   0        0        0    17966 2023-04-06 15:32:50.425493 so_vits_svc_fork-3.0.4/README.md
+-rw-r--r--   0        0        0     3073 2023-04-06 15:32:51.473489 so_vits_svc_fork-3.0.4/pyproject.toml
+-rw-r--r--   0        0        0       70 2023-04-06 15:32:51.425490 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/__init__.py
+-rw-r--r--   0        0        0    22654 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/__main__.py
+-rw-r--r--   0        0        0     1275 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/cluster/__init__.py
+-rw-r--r--   0        0        0     2659 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/cluster/train_cluster.py
+-rw-r--r--   0        0        0     2804 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/data_utils.py
+-rw-r--r--   0        0        0     2454 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/default_gui_presets.json
+-rw-r--r--   0        0        0     7215 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/f0.py
+-rw-r--r--   0        0        0    24882 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/gui.py
+-rw-r--r--   0        0        0      864 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/hparams.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/inference/__init__.py
+-rw-r--r--   0        0        0    22942 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/inference/core.py
+-rw-r--r--   0        0        0     7491 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/inference/main.py
+-rw-r--r--   0        0        0      731 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/logger.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/__init__.py
+-rw-r--r--   0        0        0    16683 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/attentions.py
+-rw-r--r--   0        0        0     5854 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/commons.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/__init__.py
+-rw-r--r--   0        0        0     1419 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/f0.py
+-rw-r--r--   0        0        0       56 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/hifigan/__init__.py
+-rw-r--r--   0        0        0    11608 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/hifigan/_models.py
+-rw-r--r--   0        0        0      340 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/hifigan/_utils.py
+-rw-r--r--   0        0        0      318 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/mb_istft/__init__.py
+-rw-r--r--   0        0        0    12479 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/mb_istft/_generators.py
+-rw-r--r--   0        0        0      419 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/mb_istft/_loss.py
+-rw-r--r--   0        0        0     4755 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/mb_istft/_pqmf.py
+-rw-r--r--   0        0        0     9055 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/mb_istft/_stft.py
+-rw-r--r--   0        0        0     4879 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/mb_istft/_stft_loss.py
+-rw-r--r--   0        0        0     5604 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/descriminators.py
+-rw-r--r--   0        0        0     4400 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/encoders.py
+-rw-r--r--   0        0        0     1390 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/flows.py
+-rw-r--r--   0        0        0     1405 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/losses.py
+-rw-r--r--   0        0        0     5753 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/mel_processing.py
+-rw-r--r--   0        0        0    14435 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/modules.py
+-rw-r--r--   0        0        0     8158 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/synthesizers.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/__init__.py
+-rw-r--r--   0        0        0     1604 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/config_templates/quickvc.json
+-rw-r--r--   0        0        0     1354 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/config_templates/so-vits-svc-4.0v1-legacy.json
+-rw-r--r--   0        0        0     1415 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/config_templates/so-vits-svc-4.0v1.json
+-rw-r--r--   0        0        0     2997 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/preprocess_flist_config.py
+-rw-r--r--   0        0        0     4566 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/preprocess_hubert_f0.py
+-rw-r--r--   0        0        0     4693 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/preprocess_resample.py
+-rw-r--r--   0        0        0     2948 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/preprocess_speaker_diarization.py
+-rw-r--r--   0        0        0     1878 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/preprocess_split.py
+-rw-r--r--   0        0        0      126 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/preprocess_utils.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/py.typed
+-rw-r--r--   0        0        0    14601 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/train.py
+-rw-r--r--   0        0        0    12981 2023-04-06 15:32:50.429493 so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/utils.py
+-rw-r--r--   0        0        0    19861 1970-01-01 00:00:00.000000 so_vits_svc_fork-3.0.4/PKG-INFO
```

### Comparing `so_vits_svc_fork-3.0.3/LICENSE` & `so_vits_svc_fork-3.0.4/LICENSE`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/README.md` & `so_vits_svc_fork-3.0.4/README.md`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/pyproject.toml` & `so_vits_svc_fork-3.0.4/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "so-vits-svc-fork"
-version = "3.0.3"
+version = "3.0.4"
 description = "A fork of so-vits-svc."
 authors = ["34j <34j.95a2p@simplelogin.com>"]
 license = "MIT"
 readme = "README.md"
 repository = "https://github.com/34j/so-vits-svc-fork"
 documentation = "https://so-vits-svc-fork.readthedocs.io"
 classifiers = [
```

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/__main__.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/__main__.py`

 * *Files 1% similar despite different names*

```diff
@@ -510,15 +510,15 @@
     default=Path("./configs/44k/config.json"),
     help="path to config",
 )
 @click.option(
     "-t",
     "--config-type",
     type=click.Choice([x.stem for x in CONFIG_TEMPLATE_DIR.rglob("*.json")]),
-    default="so-vits-svc-4.0v1",
+    default="so-vits-svc-4.0v1-legacy",
     help="config type",
 )
 def pre_config(
     input_dir: Path,
     filelist_path: Path,
     config_path: Path,
     config_type: str,
```

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/cluster/__init__.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/cluster/__init__.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/cluster/train_cluster.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/cluster/train_cluster.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/data_utils.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/data_utils.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/default_gui_presets.json` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/default_gui_presets.json`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/f0.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/f0.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/gui.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/gui.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/hparams.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/hparams.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/inference/core.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/inference/core.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/inference/main.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/inference/main.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/logger.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/logger.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/attentions.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/attentions.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/commons.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/commons.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/f0.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/f0.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/hifigan/_models.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/hifigan/_models.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/mb_istft/_generators.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/mb_istft/_generators.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/mb_istft/_pqmf.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/mb_istft/_pqmf.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/mb_istft/_stft.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/mb_istft/_stft.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/decoders/mb_istft/_stft_loss.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/decoders/mb_istft/_stft_loss.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/descriminators.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/descriminators.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/encoders.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/encoders.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/flows.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/flows.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/losses.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/losses.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/mel_processing.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/mel_processing.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/modules.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/modules.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/modules/synthesizers.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/modules/synthesizers.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/config_templates/quickvc.json` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/config_templates/quickvc.json`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/config_templates/so-vits-svc-4.0v1-legacy.json` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/config_templates/so-vits-svc-4.0v1-legacy.json`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/config_templates/so-vits-svc-4.0v1.json` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/config_templates/so-vits-svc-4.0v1.json`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/preprocess_flist_config.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/preprocess_flist_config.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/preprocess_hubert_f0.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/preprocess_hubert_f0.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/preprocess_resample.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/preprocess_resample.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/preprocess_speaker_diarization.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/preprocess_speaker_diarization.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/preprocessing/preprocess_split.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/preprocessing/preprocess_split.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/train.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/train.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/src/so_vits_svc_fork/utils.py` & `so_vits_svc_fork-3.0.4/src/so_vits_svc_fork/utils.py`

 * *Files identical despite different names*

### Comparing `so_vits_svc_fork-3.0.3/PKG-INFO` & `so_vits_svc_fork-3.0.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: so-vits-svc-fork
-Version: 3.0.3
+Version: 3.0.4
 Summary: A fork of so-vits-svc.
 Home-page: https://github.com/34j/so-vits-svc-fork
 License: MIT
 Author: 34j
 Author-email: 34j.95a2p@simplelogin.com
 Requires-Python: >=3.8,<3.11
 Classifier: Development Status :: 2 - Pre-Alpha
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: so-vits-svc-fork Version: 3.0.3 Summary: A fork of
+Metadata-Version: 2.1 Name: so-vits-svc-fork Version: 3.0.4 Summary: A fork of
 so-vits-svc. Home-page: https://github.com/34j/so-vits-svc-fork License: MIT
 Author: 34j Author-email: 34j.95a2p@simplelogin.com Requires-Python:
 >=3.8,<3.11 Classifier: Development Status :: 2 - Pre-Alpha Classifier:
 Intended Audience :: Developers Classifier: License :: OSI Approved :: MIT
 License Classifier: Natural Language :: English Classifier: Operating System ::
 OS Independent Classifier: Programming Language :: Python :: 3 Classifier:
 Programming Language :: Python :: 3.8 Classifier: Programming Language ::
```

