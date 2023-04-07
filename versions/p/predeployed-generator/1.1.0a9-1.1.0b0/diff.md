# Comparing `tmp/predeployed-generator-1.1.0a9.tar.gz` & `tmp/predeployed-generator-1.1.0b0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "predeployed-generator-1.1.0a9.tar", last modified: Tue Aug  2 10:58:11 2022, max compression
+gzip compressed data, was "predeployed-generator-1.1.0b0.tar", last modified: Fri Apr  7 13:13:21 2023, max compression
```

## Comparing `predeployed-generator-1.1.0a9.tar` & `predeployed-generator-1.1.0b0.tar`

### file list

```diff
@@ -1,40 +1,40 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-02 10:58:11.575546 predeployed-generator-1.1.0a9/
--rw-r--r--   0 runner    (1001) docker     (121)    34523 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      118 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)      631 2022-08-02 10:58:11.575546 predeployed-generator-1.1.0a9/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)       99 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      103 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)      716 2022-08-02 10:58:11.575546 predeployed-generator-1.1.0a9/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-02 10:58:11.571546 predeployed-generator-1.1.0a9/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-02 10:58:11.571546 predeployed-generator-1.1.0a9/src/predeployed_generator/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6938 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/contract_generator.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-02 10:58:11.571546 predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1852 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/access_control_enumerable_generator.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-02 10:58:11.575546 predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/artifacts/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/artifacts/.keep
--rw-r--r--   0 runner    (1001) docker     (121)    11036 2022-08-02 10:58:04.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/artifacts/ProxyAdmin.json
--rw-r--r--   0 runner    (1001) docker     (121)   518781 2022-08-02 10:58:04.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/artifacts/ProxyAdmin.meta.json
--rw-r--r--   0 runner    (1001) docker     (121)    15442 2022-08-02 10:58:04.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/artifacts/TransparentUpgradeableProxy.json
--rw-r--r--   0 runner    (1001) docker     (121)   518798 2022-08-02 10:58:04.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/artifacts/TransparentUpgradeableProxy.meta.json
--rw-r--r--   0 runner    (1001) docker     (121)     1329 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/openzeppelin_contract_generator.py
--rw-r--r--   0 runner    (1001) docker     (121)      888 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/proxy_admin_generator.py
--rw-r--r--   0 runner    (1001) docker     (121)     1871 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/transparent_upgradeable_proxy_generator.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/py.typed
--rw-r--r--   0 runner    (1001) docker     (121)     2015 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/tools.py
--rw-r--r--   0 runner    (1001) docker     (121)     2749 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/src/predeployed_generator/upgradeable_contract_generator.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-02 10:58:11.571546 predeployed-generator-1.1.0a9/src/predeployed_generator.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)      631 2022-08-02 10:58:11.000000 predeployed-generator-1.1.0a9/src/predeployed_generator.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1478 2022-08-02 10:58:11.000000 predeployed-generator-1.1.0a9/src/predeployed_generator.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-02 10:58:11.000000 predeployed-generator-1.1.0a9/src/predeployed_generator.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        5 2022-08-02 10:58:11.000000 predeployed-generator-1.1.0a9/src/predeployed_generator.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       22 2022-08-02 10:58:11.000000 predeployed-generator-1.1.0a9/src/predeployed_generator.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-02 10:58:11.575546 predeployed-generator-1.1.0a9/test/
--rw-r--r--   0 runner    (1001) docker     (121)     2519 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/test/test_access_control_enumerable_generator.py
--rw-r--r--   0 runner    (1001) docker     (121)     1081 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/test/test_artifacts_handler.py
--rw-r--r--   0 runner    (1001) docker     (121)     4211 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/test/test_contract_generator.py
--rw-r--r--   0 runner    (1001) docker     (121)     1431 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/test/test_proxy_admin_generator.py
--rw-r--r--   0 runner    (1001) docker     (121)     2474 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/test/test_transparent_upgradeable_proxy_generator.py
--rw-r--r--   0 runner    (1001) docker     (121)     5148 2022-08-02 10:56:40.000000 predeployed-generator-1.1.0a9/test/test_upgradeable_contract_generator.py
--rw-r--r--   0 runner    (1001) docker     (121)        8 2022-08-02 10:56:48.000000 predeployed-generator-1.1.0a9/version.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:21.507429 predeployed-generator-1.1.0b0/
+-rw-r--r--   0 runner    (1001) docker     (123)    34523 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      118 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)      631 2023-04-07 13:13:21.507429 predeployed-generator-1.1.0b0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)       99 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-07 13:13:21.507429 predeployed-generator-1.1.0b0/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:21.499429 predeployed-generator-1.1.0b0/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:21.503429 predeployed-generator-1.1.0b0/src/predeployed_generator/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6988 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/contract_generator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:21.503429 predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1852 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/access_control_enumerable_generator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:21.507429 predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/artifacts/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/artifacts/.keep
+-rw-r--r--   0 runner    (1001) docker     (123)    11036 2023-04-07 13:13:12.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/artifacts/ProxyAdmin.json
+-rw-r--r--   0 runner    (1001) docker     (123)   518781 2023-04-07 13:13:12.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/artifacts/ProxyAdmin.meta.json
+-rw-r--r--   0 runner    (1001) docker     (123)    15442 2023-04-07 13:13:13.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/artifacts/TransparentUpgradeableProxy.json
+-rw-r--r--   0 runner    (1001) docker     (123)   518798 2023-04-07 13:13:13.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/artifacts/TransparentUpgradeableProxy.meta.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1329 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/openzeppelin_contract_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)      888 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/proxy_admin_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1874 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/transparent_upgradeable_proxy_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)     2015 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2740 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/src/predeployed_generator/upgradeable_contract_generator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:21.503429 predeployed-generator-1.1.0b0/src/predeployed_generator.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      631 2023-04-07 13:13:21.000000 predeployed-generator-1.1.0b0/src/predeployed_generator.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1478 2023-04-07 13:13:21.000000 predeployed-generator-1.1.0b0/src/predeployed_generator.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:13:21.000000 predeployed-generator-1.1.0b0/src/predeployed_generator.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-07 13:13:21.000000 predeployed-generator-1.1.0b0/src/predeployed_generator.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-07 13:13:21.000000 predeployed-generator-1.1.0b0/src/predeployed_generator.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:21.507429 predeployed-generator-1.1.0b0/test/
+-rw-r--r--   0 runner    (1001) docker     (123)     2521 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/test/test_access_control_enumerable_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1081 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/test/test_artifacts_handler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4215 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/test/test_contract_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1432 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/test/test_proxy_admin_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2476 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/test/test_transparent_upgradeable_proxy_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5153 2023-04-07 13:11:09.000000 predeployed-generator-1.1.0b0/test/test_upgradeable_contract_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-07 13:11:26.000000 predeployed-generator-1.1.0b0/version.txt
```

### Comparing `predeployed-generator-1.1.0a9/LICENSE` & `predeployed-generator-1.1.0b0/LICENSE`

 * *Files identical despite different names*

### Comparing `predeployed-generator-1.1.0a9/PKG-INFO` & `predeployed-generator-1.1.0b0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: predeployed-generator
-Version: 1.1.0a9
+Version: 1.1.0b0
 Summary: A tool for generating memory layout of smart contracts written in solidity
 Home-page: https://github.com/skalenetwork/predeployed-generator
 Author: Dmytro Stebaiev
 Author-email: dmytro@skalelabs.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU Affero General Public License v3
 Classifier: Operating System :: OS Independent
```

### Comparing `predeployed-generator-1.1.0a9/setup.cfg` & `predeployed-generator-1.1.0b0/setup.cfg`

 * *Files 17% similar despite different names*

```diff
@@ -15,15 +15,15 @@
 [options]
 package_dir = 
 	= src
 packages = find:
 include_package_data = True
 python_requires = >=3.7
 install_requires = 
-	web3
+	web3 >= 6.0.0
 
 [options.packages.find]
 where = src
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator/contract_generator.py` & `predeployed-generator-1.1.0b0/src/predeployed_generator/contract_generator.py`

 * *Files 5% similar despite different names*

```diff
@@ -114,15 +114,20 @@
         """
         if not self.meta:
             raise MetaNotFoundError()
         return self.meta
 
     # private
 
-    def _generate(self, storage: Storage = None, balance: int = 0, nonce: int = 0) -> Account:
+    def _generate(
+        self,
+        storage: Optional[Storage] = None,
+        balance: int = 0,
+        nonce: int = 0
+    ) -> Account:
         """Produce smart contract allocation object.
 
         It consists of fields 'code', 'balance', 'nonce' and 'storage'
         """
         assert isinstance(self.bytecode, str)
         assert isinstance(balance, int)
         assert isinstance(nonce, int)
@@ -193,20 +198,20 @@
                 int(key, 16).to_bytes(32, 'big'),
                 'bytes32')
         elif key_type == 'uint256':
             assert isinstance(key, int)
         else:
             raise TypeError(f'{key_type} is unknown key type')
 
-        return int.from_bytes(w3.solidityKeccak([key_type, 'uint256'], [key, slot]), 'big')
+        return int.from_bytes(w3.solidity_keccak([key_type, 'uint256'], [key, slot]), 'big')
 
     @staticmethod
     def calculate_array_value_slot(slot: int, index: int) -> int:
         """Calculate slot in smart contract storage
         where value of the array in the index is stored
         """
-        return int.from_bytes(w3.solidityKeccak(['uint256'], [slot]), 'big') + index
+        return int.from_bytes(w3.solidity_keccak(['uint256'], [slot]), 'big') + index
 
     @staticmethod
     def next_slot(previous_slot: int) -> int:
         """Return next slot in smart contract storage"""
         return previous_slot + 1
```

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/access_control_enumerable_generator.py` & `predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/access_control_enumerable_generator.py`

 * *Files identical despite different names*

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/artifacts/ProxyAdmin.json` & `predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/artifacts/ProxyAdmin.json`

 * *Files identical despite different names*

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/artifacts/ProxyAdmin.meta.json` & `predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/artifacts/ProxyAdmin.meta.json`

 * *Files identical despite different names*

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/artifacts/TransparentUpgradeableProxy.json` & `predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/artifacts/TransparentUpgradeableProxy.json`

 * *Files identical despite different names*

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/artifacts/TransparentUpgradeableProxy.meta.json` & `predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/artifacts/TransparentUpgradeableProxy.meta.json`

 * *Files identical despite different names*

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/openzeppelin_contract_generator.py` & `predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/openzeppelin_contract_generator.py`

 * *Files identical despite different names*

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/proxy_admin_generator.py` & `predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/proxy_admin_generator.py`

 * *Files identical despite different names*

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator/openzeppelin/transparent_upgradeable_proxy_generator.py` & `predeployed-generator-1.1.0b0/src/predeployed_generator/openzeppelin/transparent_upgradeable_proxy_generator.py`

 * *Files 15% similar despite different names*

```diff
@@ -15,21 +15,21 @@
 
 class TransparentUpgradeableProxyGenerator(OpenzeppelinContractGenerator):
     '''Generates transparent upgradeable proxy
     '''
     ARTIFACT_FILENAME = 'TransparentUpgradeableProxy.json'
     META_FILENAME = 'TransparentUpgradeableProxy.meta.json'
     ROLLBACK_SLOT = int.from_bytes(
-        w3.solidityKeccak(['string'], ['eip1967.proxy.rollback']),
+        w3.solidity_keccak(['string'], ['eip1967.proxy.rollback']),
         byteorder='big') - 1
     IMPLEMENTATION_SLOT = int.from_bytes(
-        w3.solidityKeccak(['string'], ['eip1967.proxy.implementation']),
+        w3.solidity_keccak(['string'], ['eip1967.proxy.implementation']),
         byteorder='big') - 1
     ADMIN_SLOT = int.from_bytes(
-        w3.solidityKeccak(['string'], ['eip1967.proxy.admin']),
+        w3.solidity_keccak(['string'], ['eip1967.proxy.admin']),
         byteorder='big') - 1
 
     @staticmethod
     def generate_storage(**kwargs) -> dict:
         '''Generate contract storage
 
         Arguments:
```

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator/tools.py` & `predeployed-generator-1.1.0b0/src/predeployed_generator/tools.py`

 * *Files identical despite different names*

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator/upgradeable_contract_generator.py` & `predeployed-generator-1.1.0b0/src/predeployed_generator/upgradeable_contract_generator.py`

 * *Files 1% similar despite different names*

```diff
@@ -61,18 +61,18 @@
                 'storage': ...
             }
         }
         """
         proxy_admin_address = kwargs.pop('proxy_admin_address')
         implementation_address = kwargs.pop(
             'implementation_address',
-            w3.toChecksumAddress(w3.solidityKeccak(['address'], [contract_address])[:20]))
+            w3.to_checksum_address(w3.solidity_keccak(['address'], [contract_address])[:20]))
 
         return {
             contract_address: super().generate(
                 admin_address=proxy_admin_address,
                 implementation_address=implementation_address,
                 initial_storage=self.implementation_generator.generate_storage(**kwargs),
                 balance=balance,
                 nonce=nonce),
             # pylint: disable=W0212
-            implementation_address: self.implementation_generator._generate(storage=None)}
+            implementation_address: self.implementation_generator._generate()}
```

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator.egg-info/PKG-INFO` & `predeployed-generator-1.1.0b0/src/predeployed_generator.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: predeployed-generator
-Version: 1.1.0a9
+Version: 1.1.0b0
 Summary: A tool for generating memory layout of smart contracts written in solidity
 Home-page: https://github.com/skalenetwork/predeployed-generator
 Author: Dmytro Stebaiev
 Author-email: dmytro@skalelabs.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU Affero General Public License v3
 Classifier: Operating System :: OS Independent
```

### Comparing `predeployed-generator-1.1.0a9/src/predeployed_generator.egg-info/SOURCES.txt` & `predeployed-generator-1.1.0b0/src/predeployed_generator.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `predeployed-generator-1.1.0a9/test/test_access_control_enumerable_generator.py` & `predeployed-generator-1.1.0b0/test/test_access_control_enumerable_generator.py`

 * *Files 2% similar despite different names*

```diff
@@ -22,27 +22,27 @@
             testers=[self.TESTER_ADDRESS, self.TESTER2_ADDRESS]))
     
     def test_default_admin_role(self, tmpdir):
         self.datadir = tmpdir
         genesis = self.prepare_genesis()
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
 
             test_contract = w3.eth.contract(address=self.CONTRACT_ADDRESS, abi=self.get_test_contract_abi())
             assert test_contract.functions.getRoleMemberCount(CustomContractGenerator.DEFAULT_ADMIN_ROLE).call() == 1
             assert test_contract.functions.getRoleMember(CustomContractGenerator.DEFAULT_ADMIN_ROLE, 0).call() == self.OWNER_ADDRESS            
             assert test_contract.functions.hasRole(CustomContractGenerator.DEFAULT_ADMIN_ROLE, self.OWNER_ADDRESS).call()
 
     def test_tester_role(self, tmpdir):
         self.datadir = tmpdir
         genesis = self.prepare_genesis()
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
 
             test_contract = w3.eth.contract(address=self.CONTRACT_ADDRESS, abi=self.get_test_contract_abi())
             assert test_contract.functions.getRoleMemberCount(CustomContractGenerator.TESTER_ROLE).call() == 2
             assert test_contract.functions.getRoleMember(CustomContractGenerator.TESTER_ROLE, 0).call() == self.TESTER_ADDRESS
             assert test_contract.functions.getRoleMember(CustomContractGenerator.TESTER_ROLE, 1).call() == self.TESTER2_ADDRESS
             assert test_contract.functions.hasRole(CustomContractGenerator.TESTER_ROLE, self.TESTER_ADDRESS).call()
             assert test_contract.functions.hasRole(CustomContractGenerator.TESTER_ROLE, self.TESTER2_ADDRESS).call()
```

### Comparing `predeployed-generator-1.1.0a9/test/test_artifacts_handler.py` & `predeployed-generator-1.1.0b0/test/test_artifacts_handler.py`

 * *Files identical despite different names*

### Comparing `predeployed-generator-1.1.0a9/test/test_contract_generator.py` & `predeployed-generator-1.1.0b0/test/test_contract_generator.py`

 * *Files 1% similar despite different names*

```diff
@@ -25,45 +25,45 @@
             testers=[self.TESTER_ADDRESS, self.TESTER2_ADDRESS]))
 
     def test_short_string(self, tmpdir):
         self.datadir = tmpdir
         genesis = self.prepare_genesis()
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
 
             test_contract = w3.eth.contract(address=self.CONTRACT_ADDRESS, abi=self.get_test_contract_abi())
             assert test_contract.functions.shortString().call() == 'short string'
 
     def test_long_string(self, tmpdir):
         self.datadir = tmpdir
         genesis = self.prepare_genesis()
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
 
             test_contract = w3.eth.contract(address=self.CONTRACT_ADDRESS, abi=self.get_test_contract_abi())
             assert test_contract.functions.longString().call() == ' '.join(['very'] * 32) + ' long string'
 
     def test_bytes32(self, tmpdir):
         self.datadir = tmpdir
         genesis = self.prepare_genesis()
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
 
             test_contract = w3.eth.contract(address=self.CONTRACT_ADDRESS, abi=self.get_test_contract_abi())
             assert test_contract.functions.bytes32Value().call() == CustomContractGenerator.TESTER_ROLE
 
     def test_addresses_array(self, tmpdir):
         self.datadir = tmpdir
         genesis = self.prepare_genesis()
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
 
             test_contract = w3.eth.contract(address=self.CONTRACT_ADDRESS, abi=self.get_test_contract_abi())
             assert test_contract.functions.testers(0).call() == self.TESTER_ADDRESS
             assert test_contract.functions.testers(1).call() == self.TESTER2_ADDRESS
 
     def test_generator_without_storage(self):
         class EmptyGenerator(ContractGenerator):
```

### Comparing `predeployed-generator-1.1.0a9/test/test_proxy_admin_generator.py` & `predeployed-generator-1.1.0b0/test/test_proxy_admin_generator.py`

 * *Files 0% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 
     def test_owner(self, tmpdir):
         self.datadir = tmpdir
         owner_address = '0xd200000000000000000000000000000000000000'
         proxy_admin_address = '0xd200000000000000000000000000000000000001'
         generator = ProxyAdminGenerator()
         with self.run_geth(tmpdir, self.generate_genesis({proxy_admin_address: generator.generate(owner_address=owner_address)})):
-            assert w3.isConnected()
+            assert w3.is_connected()
             
             proxy_admin = w3.eth.contract(address=proxy_admin_address, abi=self.get_proxy_admin_abi())
             assert proxy_admin.functions.owner().call() == owner_address
 
     def test_wrong_inheritance(self):
         class GeneratorWithoutArtifact(OpenzeppelinContractGenerator):
             pass
```

### Comparing `predeployed-generator-1.1.0a9/test/test_transparent_upgradeable_proxy_generator.py` & `predeployed-generator-1.1.0b0/test/test_transparent_upgradeable_proxy_generator.py`

 * *Files 1% similar despite different names*

```diff
@@ -36,22 +36,22 @@
     # tests
 
     def test_admin(self, tmpdir):   
         self.datadir = tmpdir     
         genesis = self.prepare_genesis()
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
             
             proxy_admin = w3.eth.contract(address=self.PROXY_ADMIN_ADDRESS, abi=self.get_proxy_admin_abi())
             assert proxy_admin.functions.getProxyAdmin(self.PROXY_ADDRESS).call() == self.PROXY_ADMIN_ADDRESS
 
     def test_implementation(self, tmpdir):
         self.datadir = tmpdir
         genesis = self.prepare_genesis()
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
             
             proxy_admin = w3.eth.contract(address=self.PROXY_ADMIN_ADDRESS, abi=self.get_proxy_admin_abi())
             assert proxy_admin.functions.getProxyImplementation(self.PROXY_ADDRESS).call() == self.IMPLEMENTATION_ADDRESS
```

### Comparing `predeployed-generator-1.1.0a9/test/test_upgradeable_contract_generator.py` & `predeployed-generator-1.1.0b0/test/test_upgradeable_contract_generator.py`

 * *Files 5% similar despite different names*

```diff
@@ -37,25 +37,25 @@
     # tests
 
     def test_admin(self, tmpdir):     
         self.datadir = tmpdir   
         genesis = self.prepare_genesis()
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
             
             proxy_admin = w3.eth.contract(address=self.PROXY_ADMIN_ADDRESS, abi=self.get_proxy_admin_abi())
             assert proxy_admin.functions.getProxyAdmin(self.PROXY_ADDRESS).call() == self.PROXY_ADMIN_ADDRESS
 
     def test_implementation(self, tmpdir):
         self.datadir = tmpdir
         genesis = self.prepare_genesis()
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
             
             proxy_admin = w3.eth.contract(address=self.PROXY_ADMIN_ADDRESS, abi=self.get_proxy_admin_abi())
             assert proxy_admin.functions.getProxyImplementation(self.PROXY_ADDRESS).call() == self.IMPLEMENTATION_ADDRESS
 
     def test_default_implementation_address(self, tmpdir):
         self.datadir = tmpdir
         proxy_admin_generator = ProxyAdminGenerator()
@@ -67,25 +67,25 @@
                 contract_address=self.PROXY_ADDRESS,
                 proxy_admin_address=self.PROXY_ADMIN_ADDRESS,
                 owner_address=self.OWNER_ADDRESS
             )
         })
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
             
             proxy_admin = w3.eth.contract(address=self.PROXY_ADMIN_ADDRESS, abi=self.get_proxy_admin_abi())
             assert proxy_admin.functions.getProxyImplementation(self.PROXY_ADDRESS).call() == self.PROXY_ADDRESS_HASH
     
     def test_owner(self, tmpdir):
         self.datadir = tmpdir
         genesis = self.prepare_genesis()
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
             
             proxy_admin = w3.eth.contract(address=self.PROXY_ADDRESS, abi=self.get_proxy_admin_abi())
             assert proxy_admin.functions.owner().call() == self.OWNER_ADDRESS
 
     def test_wrong_generation(self):
         with pytest.raises(RuntimeError):
             contract_generator = UpgradeableContractGenerator(ProxyAdminGenerator())
@@ -108,12 +108,12 @@
                 implementation_address=self.IMPLEMENTATION_ADDRESS,
                 proxy_admin_address=self.PROXY_ADMIN_ADDRESS,
                 owner_address=self.OWNER_ADDRESS
             )
         })
 
         with self.run_geth(tmpdir, genesis):
-            assert w3.isConnected()
+            assert w3.is_connected()
             
             assert w3.eth.get_balance(self.PROXY_ADDRESS) == balance
             assert w3.eth.get_transaction_count(self.PROXY_ADDRESS) == nonce
```

