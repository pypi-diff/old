# Comparing `tmp/audiolm-pytorch-0.9.6.tar.gz` & `tmp/audiolm-pytorch-0.9.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "audiolm-pytorch-0.9.6.tar", last modified: Thu Feb  2 20:41:49 2023, max compression
+gzip compressed data, was "audiolm-pytorch-0.9.7.tar", last modified: Thu Feb  2 20:43:32 2023, max compression
```

## Comparing `audiolm-pytorch-0.9.6.tar` & `audiolm-pytorch-0.9.7.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 20:41:49.233814 audiolm-pytorch-0.9.6/
--rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      698 2023-02-02 20:41:49.233814 audiolm-pytorch-0.9.6/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    13581 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 20:41:49.233814 audiolm-pytorch-0.9.6/audiolm_pytorch/
--rw-r--r--   0 runner    (1001) docker     (123)      632 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/audiolm_pytorch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    57921 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/audiolm_pytorch/audiolm_pytorch.py
--rw-r--r--   0 runner    (1001) docker     (123)     4554 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/audiolm_pytorch/data.py
--rw-r--r--   0 runner    (1001) docker     (123)     2370 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/audiolm_pytorch/hubert_kmeans.py
--rw-r--r--   0 runner    (1001) docker     (123)      943 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/audiolm_pytorch/optimizer.py
--rw-r--r--   0 runner    (1001) docker     (123)    22495 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/audiolm_pytorch/soundstream.py
--rw-r--r--   0 runner    (1001) docker     (123)     2548 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/audiolm_pytorch/t5.py
--rw-r--r--   0 runner    (1001) docker     (123)    35059 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/audiolm_pytorch/trainer.py
--rw-r--r--   0 runner    (1001) docker     (123)      307 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/audiolm_pytorch/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2236 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/audiolm_pytorch/vq_wav2vec.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 20:41:49.233814 audiolm-pytorch-0.9.6/audiolm_pytorch.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      698 2023-02-02 20:41:49.000000 audiolm-pytorch-0.9.6/audiolm_pytorch.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      504 2023-02-02 20:41:49.000000 audiolm-pytorch-0.9.6/audiolm_pytorch.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 20:41:49.000000 audiolm-pytorch-0.9.6/audiolm_pytorch.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      195 2023-02-02 20:41:49.000000 audiolm-pytorch-0.9.6/audiolm_pytorch.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-02-02 20:41:49.000000 audiolm-pytorch-0.9.6/audiolm_pytorch.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-02 20:41:49.233814 audiolm-pytorch-0.9.6/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1162 2023-02-02 20:41:31.000000 audiolm-pytorch-0.9.6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 20:43:32.766771 audiolm-pytorch-0.9.7/
+-rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      698 2023-02-02 20:43:32.766771 audiolm-pytorch-0.9.7/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    13581 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 20:43:32.766771 audiolm-pytorch-0.9.7/audiolm_pytorch/
+-rw-r--r--   0 runner    (1001) docker     (123)      632 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/audiolm_pytorch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    57921 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/audiolm_pytorch/audiolm_pytorch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4554 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/audiolm_pytorch/data.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2370 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/audiolm_pytorch/hubert_kmeans.py
+-rw-r--r--   0 runner    (1001) docker     (123)      943 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/audiolm_pytorch/optimizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18951 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/audiolm_pytorch/soundstream.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2548 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/audiolm_pytorch/t5.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35059 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/audiolm_pytorch/trainer.py
+-rw-r--r--   0 runner    (1001) docker     (123)      307 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/audiolm_pytorch/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2236 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/audiolm_pytorch/vq_wav2vec.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 20:43:32.766771 audiolm-pytorch-0.9.7/audiolm_pytorch.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      698 2023-02-02 20:43:32.000000 audiolm-pytorch-0.9.7/audiolm_pytorch.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      504 2023-02-02 20:43:32.000000 audiolm-pytorch-0.9.7/audiolm_pytorch.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 20:43:32.000000 audiolm-pytorch-0.9.7/audiolm_pytorch.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      195 2023-02-02 20:43:32.000000 audiolm-pytorch-0.9.7/audiolm_pytorch.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-02-02 20:43:32.000000 audiolm-pytorch-0.9.7/audiolm_pytorch.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-02 20:43:32.766771 audiolm-pytorch-0.9.7/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1162 2023-02-02 20:43:21.000000 audiolm-pytorch-0.9.7/setup.py
```

### Comparing `audiolm-pytorch-0.9.6/LICENSE` & `audiolm-pytorch-0.9.7/LICENSE`

 * *Files identical despite different names*

### Comparing `audiolm-pytorch-0.9.6/PKG-INFO` & `audiolm-pytorch-0.9.7/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: audiolm-pytorch
-Version: 0.9.6
+Version: 0.9.7
 Summary: AudioLM - Language Modeling Approach to Audio Generation from Google Research - Pytorch
 Home-page: https://github.com/lucidrains/audiolm-pytorch
 Author: Phil Wang
 Author-email: lucidrains@gmail.com
 License: MIT
 Keywords: artificial intelligence,deep learning,transformers,attention mechanism,audio generation
 Classifier: Development Status :: 4 - Beta
```

### Comparing `audiolm-pytorch-0.9.6/README.md` & `audiolm-pytorch-0.9.7/README.md`

 * *Files identical despite different names*

### Comparing `audiolm-pytorch-0.9.6/audiolm_pytorch/__init__.py` & `audiolm-pytorch-0.9.7/audiolm_pytorch/__init__.py`

 * *Files identical despite different names*

### Comparing `audiolm-pytorch-0.9.6/audiolm_pytorch/audiolm_pytorch.py` & `audiolm-pytorch-0.9.7/audiolm_pytorch/audiolm_pytorch.py`

 * *Files identical despite different names*

### Comparing `audiolm-pytorch-0.9.6/audiolm_pytorch/data.py` & `audiolm-pytorch-0.9.7/audiolm_pytorch/data.py`

 * *Files identical despite different names*

### Comparing `audiolm-pytorch-0.9.6/audiolm_pytorch/hubert_kmeans.py` & `audiolm-pytorch-0.9.7/audiolm_pytorch/hubert_kmeans.py`

 * *Files identical despite different names*

### Comparing `audiolm-pytorch-0.9.6/audiolm_pytorch/optimizer.py` & `audiolm-pytorch-0.9.7/audiolm_pytorch/optimizer.py`

 * *Files identical despite different names*

### Comparing `audiolm-pytorch-0.9.6/audiolm_pytorch/soundstream.py` & `audiolm-pytorch-0.9.7/audiolm_pytorch/soundstream.py`

 * *Files 10% similar despite different names*

```diff
@@ -24,36 +24,19 @@
 
 def exists(val):
     return val is not None
 
 def default(val, d):
     return val if exists(val) else d
 
-# decorators
-
-def auto_handle_complex(fn):
-    @wraps(fn)
-    def inner(*args):
-        if args[0].dtype not in (torch.complex64, torch.complex32):
-            return fn(*args)
-
-        real_args = tuple(arg.real for arg in args)
-        imag_args = tuple(arg.imag for arg in args)
-
-        return (fn(*real_args) + fn(*imag_args)) * 0.5
-
-    return inner
-
 # gan losses
 
-@auto_handle_complex
 def hinge_discr_loss(fake, real):
     return (F.relu(1 + fake) + F.relu(1 - real)).mean()
 
-@auto_handle_complex
 def hinge_gen_loss(fake):
     return -fake.mean()
 
 def leaky_relu(p = 0.1):
     return nn.LeakyReLU(p)
 
 def gradient_penalty(wave, output, weight = 10):
@@ -116,109 +99,14 @@
         out = self.final_conv(x)
 
         if not return_intermediates:
             return out
 
         return out, intermediates
 
-# complex stft discriminator
-
-class ModReLU(nn.Module):
-    """
-    https://arxiv.org/abs/1705.09792
-    https://github.com/pytorch/pytorch/issues/47052#issuecomment-718948801
-    """
-    def __init__(self):
-        super().__init__()
-        self.b = nn.Parameter(torch.tensor(0.))
-
-    def forward(self, x):
-        return F.relu(torch.abs(x) + self.b) * torch.exp(1.j * torch.angle(x))
-
-def ComplexSTFTResidualUnit(chan_in, chan_out, strides):
-    kernel_sizes = tuple(map(lambda t: t + 2, strides))
-    paddings = tuple(map(lambda t: t // 2, kernel_sizes))
-
-    return nn.Sequential(
-        nn.Conv2d(chan_in, chan_in, 3, padding = 1, dtype = torch.complex64),
-        ModReLU(),
-        nn.Conv2d(chan_in, chan_out, kernel_sizes, stride = strides, padding = paddings, dtype = torch.complex64)
-    )
-
-class ComplexSTFTDiscriminator(nn.Module):
-    def __init__(
-        self,
-        *,
-        channels = 32,
-        strides = ((1, 2), (2, 2), (1, 2), (2, 2), (1, 2), (2, 2)),
-        chan_mults = (1, 2, 4, 4, 8, 8),
-        input_channels = 1,
-        n_fft = 1024,
-        hop_length = 256,
-        win_length = 1024
-    ):
-        super().__init__()
-        self.init_conv = nn.Conv2d(input_channels, channels, 7, padding = 3, dtype = torch.complex64)
-
-        layer_channels = tuple(map(lambda mult: mult * channels, chan_mults))
-        layer_channels = (channels, *layer_channels)
-        layer_channels_pairs = tuple(zip(layer_channels[:-1], layer_channels[1:]))
-
-        curr_channels = channels
-
-        self.layers = nn.ModuleList([])
-
-        for layer_stride, (chan_in, chan_out) in zip(strides, layer_channels_pairs):
-            self.layers.append(ComplexSTFTResidualUnit(chan_in, chan_out, layer_stride))
-
-        self.final_conv = nn.Conv2d(layer_channels[-1], 1, (16, 1), dtype = torch.complex64) # todo: remove hardcoded 16
-
-        # stft settings
-
-        self.n_fft = n_fft
-        self.hop_length = hop_length
-        self.win_length = win_length
-
-    def forward(self, x, return_intermediates = False):
-        x = rearrange(x, 'b 1 n -> b n')
-
-        '''
-        reference: The content of the paper( https://arxiv.org/pdf/2107.03312.pdf)is as follows:
-        The STFT-based discriminator is illustrated in Figure 4
-        and operates on a single scale, computing the STFT with a
-        window length of W = 1024 samples and a hop length of
-        H = 256 samples
-        '''
-
-        x = torch.stft(
-            x,
-            self.n_fft,
-            hop_length = self.hop_length,
-            win_length = self.win_length,
-            return_complex = True
-        )
-
-        x = rearrange(x, 'b ... -> b 1 ...')
-
-        intermediates = []
-
-        x = self.init_conv(x)
-        intermediates.append(x)
-
-        for layer in self.layers:
-            x = layer(x)
-            intermediates.append(x)
-
-        complex_logits = self.final_conv(x)
-
-        if not return_intermediates:
-            return complex_logits
-
-        return complex_logits, intermediates
-
 # simulated complex stft discriminator
 
 class ComplexConv2d(nn.Module):
     def __init__(
         self,
         *args,
         **kwargs
@@ -457,16 +345,15 @@
         target_sample_hz = 24000,
         use_local_attn = True,
         use_mhesa = True,
         mhesa_heads = 4,
         mhesa_dim_head = 32,
         attn_window_size = 128,
         attn_dim_head = 64,
-        attn_heads = 8,
-        use_complex_stft_discriminator = False
+        attn_heads = 8
     ):
         super().__init__()
         self.target_sample_hz = target_sample_hz # for resampling on the fly
 
         self.single_channel = input_channels == 1
         self.strides = strides
 
@@ -532,16 +419,15 @@
         )
 
         # discriminators
 
         self.discr_multi_scales = discr_multi_scales
         self.discriminators = nn.ModuleList([MultiScaleDiscriminator() for _ in range(len(discr_multi_scales))])
 
-        stft_klass = ComplexSTFTDiscriminator if use_complex_stft_discriminator else STFTDiscriminator
-        self.stft_discriminator = stft_klass()
+        self.stft_discriminator = STFTDiscriminator()
 
         # loss weights
 
         self.recon_loss_weight = recon_loss_weight
         self.adversarial_loss_weight = adversarial_loss_weight
         self.feature_loss_weight = feature_loss_weight
```

### Comparing `audiolm-pytorch-0.9.6/audiolm_pytorch/t5.py` & `audiolm-pytorch-0.9.7/audiolm_pytorch/t5.py`

 * *Files identical despite different names*

### Comparing `audiolm-pytorch-0.9.6/audiolm_pytorch/trainer.py` & `audiolm-pytorch-0.9.7/audiolm_pytorch/trainer.py`

 * *Files identical despite different names*

### Comparing `audiolm-pytorch-0.9.6/audiolm_pytorch/vq_wav2vec.py` & `audiolm-pytorch-0.9.7/audiolm_pytorch/vq_wav2vec.py`

 * *Files identical despite different names*

### Comparing `audiolm-pytorch-0.9.6/audiolm_pytorch.egg-info/PKG-INFO` & `audiolm-pytorch-0.9.7/audiolm_pytorch.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: audiolm-pytorch
-Version: 0.9.6
+Version: 0.9.7
 Summary: AudioLM - Language Modeling Approach to Audio Generation from Google Research - Pytorch
 Home-page: https://github.com/lucidrains/audiolm-pytorch
 Author: Phil Wang
 Author-email: lucidrains@gmail.com
 License: MIT
 Keywords: artificial intelligence,deep learning,transformers,attention mechanism,audio generation
 Classifier: Development Status :: 4 - Beta
```

### Comparing `audiolm-pytorch-0.9.6/setup.py` & `audiolm-pytorch-0.9.7/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from setuptools import setup, find_packages
 
 setup(
   name = 'audiolm-pytorch',
   packages = find_packages(exclude=[]),
-  version = '0.9.6',
+  version = '0.9.7',
   license='MIT',
   description = 'AudioLM - Language Modeling Approach to Audio Generation from Google Research - Pytorch',
   author = 'Phil Wang',
   author_email = 'lucidrains@gmail.com',
   long_description_content_type = 'text/markdown',
   url = 'https://github.com/lucidrains/audiolm-pytorch',
   keywords = [
```

