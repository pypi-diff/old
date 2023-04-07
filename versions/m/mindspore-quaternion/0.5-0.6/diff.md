# Comparing `tmp/mindspore-quaternion-0.5.tar.gz` & `tmp/mindspore-quaternion-0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mindspore-quaternion-0.5.tar", last modified: Wed Mar 22 09:23:49 2023, max compression
+gzip compressed data, was "mindspore-quaternion-0.6.tar", last modified: Fri Apr  7 03:42:31 2023, max compression
```

## Comparing `mindspore-quaternion-0.5.tar` & `mindspore-quaternion-0.6.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxrwxr-x   0 dechin    (1001) dechin    (1001)        0 2023-03-22 09:23:49.394828 mindspore-quaternion-0.5/
--rw-rw-r--   0 dechin    (1001) dechin    (1001)     1068 2023-02-27 07:31:19.000000 mindspore-quaternion-0.5/LICENSE
--rw-rw-r--   0 dechin    (1001) dechin    (1001)     9223 2023-03-22 09:23:49.390828 mindspore-quaternion-0.5/PKG-INFO
--rw-rw-r--   0 dechin    (1001) dechin    (1001)     8887 2023-03-22 09:22:51.000000 mindspore-quaternion-0.5/README.md
-drwxrwxr-x   0 dechin    (1001) dechin    (1001)        0 2023-03-22 09:23:49.390828 mindspore-quaternion-0.5/mindspore_quaternion.egg-info/
--rw-rw-r--   0 dechin    (1001) dechin    (1001)     9223 2023-03-22 09:23:49.000000 mindspore-quaternion-0.5/mindspore_quaternion.egg-info/PKG-INFO
--rw-rw-r--   0 dechin    (1001) dechin    (1001)      292 2023-03-22 09:23:49.000000 mindspore-quaternion-0.5/mindspore_quaternion.egg-info/SOURCES.txt
--rw-rw-r--   0 dechin    (1001) dechin    (1001)        1 2023-03-22 09:23:49.000000 mindspore-quaternion-0.5/mindspore_quaternion.egg-info/dependency_links.txt
--rw-rw-r--   0 dechin    (1001) dechin    (1001)       36 2023-03-22 09:23:49.000000 mindspore-quaternion-0.5/mindspore_quaternion.egg-info/requires.txt
--rw-rw-r--   0 dechin    (1001) dechin    (1001)       11 2023-03-22 09:23:49.000000 mindspore-quaternion-0.5/mindspore_quaternion.egg-info/top_level.txt
-drwxrwxr-x   0 dechin    (1001) dechin    (1001)        0 2023-03-22 09:23:49.390828 mindspore-quaternion-0.5/quaternion/
--rw-rw-r--   0 dechin    (1001) dechin    (1001)     7656 2023-03-22 02:48:15.000000 mindspore-quaternion-0.5/quaternion/__init__.py
--rw-rw-r--   0 dechin    (1001) dechin    (1001)     6185 2023-03-22 09:19:21.000000 mindspore-quaternion-0.5/quaternion/functions.py
--rw-rw-r--   0 dechin    (1001) dechin    (1001)       38 2023-03-22 09:23:49.394828 mindspore-quaternion-0.5/setup.cfg
--rw-rw-r--   0 dechin    (1001) dechin    (1001)     2017 2023-03-22 06:47:04.000000 mindspore-quaternion-0.5/setup.py
+drwxrwxr-x   0 dechin    (1001) dechin    (1001)        0 2023-04-07 03:42:31.719958 mindspore-quaternion-0.6/
+-rw-rw-r--   0 dechin    (1001) dechin    (1001)     1068 2023-02-27 07:31:19.000000 mindspore-quaternion-0.6/LICENSE
+-rw-rw-r--   0 dechin    (1001) dechin    (1001)     9355 2023-04-07 03:42:31.719958 mindspore-quaternion-0.6/PKG-INFO
+-rw-rw-r--   0 dechin    (1001) dechin    (1001)     9019 2023-03-23 07:05:00.000000 mindspore-quaternion-0.6/README.md
+drwxrwxr-x   0 dechin    (1001) dechin    (1001)        0 2023-04-07 03:42:31.719958 mindspore-quaternion-0.6/mindspore_quaternion.egg-info/
+-rw-rw-r--   0 dechin    (1001) dechin    (1001)     9355 2023-04-07 03:42:31.000000 mindspore-quaternion-0.6/mindspore_quaternion.egg-info/PKG-INFO
+-rw-rw-r--   0 dechin    (1001) dechin    (1001)      292 2023-04-07 03:42:31.000000 mindspore-quaternion-0.6/mindspore_quaternion.egg-info/SOURCES.txt
+-rw-rw-r--   0 dechin    (1001) dechin    (1001)        1 2023-04-07 03:42:31.000000 mindspore-quaternion-0.6/mindspore_quaternion.egg-info/dependency_links.txt
+-rw-rw-r--   0 dechin    (1001) dechin    (1001)       36 2023-04-07 03:42:31.000000 mindspore-quaternion-0.6/mindspore_quaternion.egg-info/requires.txt
+-rw-rw-r--   0 dechin    (1001) dechin    (1001)       11 2023-04-07 03:42:31.000000 mindspore-quaternion-0.6/mindspore_quaternion.egg-info/top_level.txt
+drwxrwxr-x   0 dechin    (1001) dechin    (1001)        0 2023-04-07 03:42:31.719958 mindspore-quaternion-0.6/quaternion/
+-rw-rw-r--   0 dechin    (1001) dechin    (1001)     7656 2023-03-22 02:48:15.000000 mindspore-quaternion-0.6/quaternion/__init__.py
+-rw-rw-r--   0 dechin    (1001) dechin    (1001)     6437 2023-04-07 03:16:13.000000 mindspore-quaternion-0.6/quaternion/functions.py
+-rw-rw-r--   0 dechin    (1001) dechin    (1001)       38 2023-04-07 03:42:31.719958 mindspore-quaternion-0.6/setup.cfg
+-rw-rw-r--   0 dechin    (1001) dechin    (1001)     2017 2023-04-07 02:59:31.000000 mindspore-quaternion-0.6/setup.py
```

### Comparing `mindspore-quaternion-0.5/LICENSE` & `mindspore-quaternion-0.6/LICENSE`

 * *Files identical despite different names*

### Comparing `mindspore-quaternion-0.5/PKG-INFO` & `mindspore-quaternion-0.6/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mindspore-quaternion
-Version: 0.5
+Version: 0.6
 Summary: Quaternion data structure based on MindSpore Framework
 Home-page: https://gitee.com/dechin/mindspore-quaternion
 Author: Dechin CHEN
 Author-email: dechin.phy@gmail.com
 License: MIT Licence
 Platform: any
 Description-Content-Type: text/markdown
@@ -13,17 +13,17 @@
 # mindspore-quaternion--基于MindSpore深度学习框架的四元数数据结构
 ![](https://img.shields.io/pypi/l/mindspore-quaternion)
 
 四元数在自动化等领域有非常广泛的应用，其必要性在于解决了使用欧拉角旋转的过程中有可能出现的欧拉角死锁问题。
 关于更多的四元数的原理和计算方法，可以阅读本readme末尾的参考博客。
 
 ## 安装与更新
-本软件支持pip一键安装与更新：
+本软件支持pip一键安装与更新（这里推荐使用pypi原始的资源，国内的一些镜像源同步的并不是很及时）：
 ```bash
-$ python3 -m pip install mindspore-quaternion --upgrade
+$ python3 -m pip install mindspore-quaternion --upgrade -i https://pypi.Python.org/simple/
 ```
 也可以使用源码进行安装：
 ```bash
 $ git clone https://gitee.com/dechin/mindspore-quaternion.git
 $ cd mindspore-quaternion
 $ python3 setup.py install
 ```
```

### Comparing `mindspore-quaternion-0.5/README.md` & `mindspore-quaternion-0.6/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 # mindspore-quaternion--基于MindSpore深度学习框架的四元数数据结构
 ![](https://img.shields.io/pypi/l/mindspore-quaternion)
 
 四元数在自动化等领域有非常广泛的应用，其必要性在于解决了使用欧拉角旋转的过程中有可能出现的欧拉角死锁问题。
 关于更多的四元数的原理和计算方法，可以阅读本readme末尾的参考博客。
 
 ## 安装与更新
-本软件支持pip一键安装与更新：
+本软件支持pip一键安装与更新（这里推荐使用pypi原始的资源，国内的一些镜像源同步的并不是很及时）：
 ```bash
-$ python3 -m pip install mindspore-quaternion --upgrade
+$ python3 -m pip install mindspore-quaternion --upgrade -i https://pypi.Python.org/simple/
 ```
 也可以使用源码进行安装：
 ```bash
 $ git clone https://gitee.com/dechin/mindspore-quaternion.git
 $ cd mindspore-quaternion
 $ python3 setup.py install
 ```
```

### Comparing `mindspore-quaternion-0.5/mindspore_quaternion.egg-info/PKG-INFO` & `mindspore-quaternion-0.6/mindspore_quaternion.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mindspore-quaternion
-Version: 0.5
+Version: 0.6
 Summary: Quaternion data structure based on MindSpore Framework
 Home-page: https://gitee.com/dechin/mindspore-quaternion
 Author: Dechin CHEN
 Author-email: dechin.phy@gmail.com
 License: MIT Licence
 Platform: any
 Description-Content-Type: text/markdown
@@ -13,17 +13,17 @@
 # mindspore-quaternion--基于MindSpore深度学习框架的四元数数据结构
 ![](https://img.shields.io/pypi/l/mindspore-quaternion)
 
 四元数在自动化等领域有非常广泛的应用，其必要性在于解决了使用欧拉角旋转的过程中有可能出现的欧拉角死锁问题。
 关于更多的四元数的原理和计算方法，可以阅读本readme末尾的参考博客。
 
 ## 安装与更新
-本软件支持pip一键安装与更新：
+本软件支持pip一键安装与更新（这里推荐使用pypi原始的资源，国内的一些镜像源同步的并不是很及时）：
 ```bash
-$ python3 -m pip install mindspore-quaternion --upgrade
+$ python3 -m pip install mindspore-quaternion --upgrade -i https://pypi.Python.org/simple/
 ```
 也可以使用源码进行安装：
 ```bash
 $ git clone https://gitee.com/dechin/mindspore-quaternion.git
 $ cd mindspore-quaternion
 $ python3 setup.py install
 ```
```

### Comparing `mindspore-quaternion-0.5/quaternion/__init__.py` & `mindspore-quaternion-0.6/quaternion/__init__.py`

 * *Files identical despite different names*

### Comparing `mindspore-quaternion-0.5/quaternion/functions.py` & `mindspore-quaternion-0.6/quaternion/functions.py`

 * *Files 3% similar despite different names*

```diff
@@ -20,14 +20,15 @@
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
 
 
 import mindspore as ms
 from mindspore import Tensor, nn, ops
 from mindspore import numpy as msnp
+from mindspore.ops.functional import vmap
 
 
 def _quaternion_multiply(tensor_1, tensor_2):
     """ Get the quaternion multiplication of the given tensor.
     Args:
         tensor_1(Tensor): A tensor with shape (B, 4).
         tensor_2(Tensor): A tensor with shape (B, 4).
@@ -83,14 +84,18 @@
         tensor_1 = msnp.pad(tensor_1, ((0, 0), (1, 0)), mode='constant', constant_value=0)
         return quaternion_multiply(tensor_1, tensor_2)
     if tensor_2.shape[-1] == 3:
         tensor_2 = msnp.pad(tensor_2, ((0, 0), (1, 0)), mode='constant', constant_value=0)
         return quaternion_multiply(tensor_1, tensor_2)
     return _quaternion_multiply(tensor_1, tensor_2)
 
+
+batch_quaternion_multiply = vmap(quaternion_multiply, in_axes=(0, 0))
+
+
 def quaternion_inverse(tensor_1):
     """ Get the quaternion conjugate of the given tensor.
     Args:
         tensor_1(Tensor): A tensor to calculate.
     Return:
         tensor_2(Tensor): The multiplication result with shape (B, 4).
     """
@@ -123,14 +128,18 @@
         tensor_2 = tensor_2[None, :]
 
     inverse_quaternion = quaternion_inverse(quaternion_1)
     op1 = quaternion_multiply(tensor_2, inverse_quaternion)
     res = quaternion_multiply(quaternion_1, op1)
     return res
 
+
+batch_hamiltonian_product = vmap(hamiltonian_product, in_axes=(0, 0))
+
+
 def quaternion_diff(tensor_1, tensor_2):
     """ Get the transform between tensor_1 and tensor_2.
     Args:
         tensor_1(Tensor): A tensor to calculate.
         tensor_2(Tensor): A tensor to calculate
     Returns:
         The transform quaternion result.
@@ -161,7 +170,10 @@
     qs = msnp.zeros_like(s_1)
     qv = msnp.zeros_like(v_1)
     qs += v_1.norm(-1, keep_dims=True) * v_2.norm(-1, keep_dims=True) + ops.batch_dot(v_1, v_2, axes=-1)
     qv += u
     q = msnp.hstack((qs, qv))
     q /= q.norm(-1, keep_dims=True)
     return q
+
+
+batch_quaternion_diff = vmap(quaternion_diff, in_axes=(0, 0))
```

### Comparing `mindspore-quaternion-0.5/setup.py` & `mindspore-quaternion-0.6/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -31,15 +31,15 @@
 from pathlib import Path
 
 this_directory = Path(__file__).parent
 long_description = (this_directory / "README.md").read_text()
 
 setup(
     name="mindspore-quaternion",
-    version="0.5",
+    version="0.6",
     description="Quaternion data structure based on MindSpore Framework",
     long_description=long_description,
     long_description_content_type='text/markdown',
     license="MIT Licence",
 
     url="https://gitee.com/dechin/mindspore-quaternion",
     author="Dechin CHEN",
```

