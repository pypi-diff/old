# Comparing `tmp/daqp-0.1.0.tar.gz` & `tmp/daqp-0.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "daqp-0.1.0.tar", last modified: Fri Mar 31 11:45:45 2023, max compression
+gzip compressed data, was "daqp-0.4.0.tar", last modified: Thu Apr  6 14:38:36 2023, max compression
```

## Comparing `daqp-0.1.0.tar` & `daqp-0.4.0.tar`

### file list

```diff
@@ -1,17 +1,24 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:45:45.795822 daqp-0.1.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1073 2023-03-31 11:45:45.000000 daqp-0.1.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1207 2023-03-31 11:45:45.795822 daqp-0.1.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      934 2023-03-31 11:40:04.000000 daqp-0.1.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-31 11:45:45.795822 daqp-0.1.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3083 2023-03-31 11:40:04.000000 daqp-0.1.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:45:45.795822 daqp-0.1.0/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:45:45.795822 daqp-0.1.0/src/daqp/
--rw-r--r--   0 runner    (1001) docker     (123)       69 2023-03-31 11:40:04.000000 daqp-0.1.0/src/daqp/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2530 2023-03-31 11:40:04.000000 daqp-0.1.0/src/daqp/daqp.py
--rw-r--r--   0 runner    (1001) docker     (123)     1955 2023-03-31 11:40:04.000000 daqp-0.1.0/src/daqp/types.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-31 11:45:45.795822 daqp-0.1.0/src/daqp.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1207 2023-03-31 11:45:45.000000 daqp-0.1.0/src/daqp.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      241 2023-03-31 11:45:45.000000 daqp-0.1.0/src/daqp.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-31 11:45:45.000000 daqp-0.1.0/src/daqp.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-31 11:45:45.000000 daqp-0.1.0/src/daqp.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-03-31 11:45:45.000000 daqp-0.1.0/src/daqp.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:38:36.020512 daqp-0.4.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1073 2023-04-06 14:38:35.000000 daqp-0.4.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1207 2023-04-06 14:38:36.016512 daqp-0.4.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      934 2023-04-06 14:29:56.000000 daqp-0.4.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:38:36.012512 daqp-0.4.0/csrc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:38:36.016512 daqp-0.4.0/csrc/src/
+-rw-r--r--   0 runner    (1001) docker     (123)     9129 2023-04-06 14:29:56.000000 daqp-0.4.0/csrc/src/api.c
+-rw-r--r--   0 runner    (1001) docker     (123)    14022 2023-04-06 14:29:56.000000 daqp-0.4.0/csrc/src/auxiliary.c
+-rw-r--r--   0 runner    (1001) docker     (123)     7098 2023-04-06 14:29:56.000000 daqp-0.4.0/csrc/src/bnb.c
+-rw-r--r--   0 runner    (1001) docker     (123)     3925 2023-04-06 14:29:56.000000 daqp-0.4.0/csrc/src/daqp.c
+-rw-r--r--   0 runner    (1001) docker     (123)     5576 2023-04-06 14:29:56.000000 daqp-0.4.0/csrc/src/daqp_prox.c
+-rw-r--r--   0 runner    (1001) docker     (123)     4111 2023-04-06 14:29:56.000000 daqp-0.4.0/csrc/src/factorization.c
+-rw-r--r--   0 runner    (1001) docker     (123)    10570 2023-04-06 14:29:56.000000 daqp-0.4.0/csrc/src/utils.c
+-rw-r--r--   0 runner    (1001) docker     (123)   808116 2023-04-06 14:38:35.000000 daqp-0.4.0/daqp.c
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:38:36.016512 daqp-0.4.0/daqp.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1207 2023-04-06 14:38:36.000000 daqp-0.4.0/daqp.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      326 2023-04-06 14:38:36.000000 daqp-0.4.0/daqp.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:38:36.000000 daqp-0.4.0/daqp.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:38:35.000000 daqp-0.4.0/daqp.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 14:38:36.000000 daqp-0.4.0/daqp.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1135 2023-04-06 14:29:56.000000 daqp-0.4.0/daqp.pxd
+-rw-r--r--   0 runner    (1001) docker     (123)      100 2023-04-06 14:29:56.000000 daqp-0.4.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 14:38:36.020512 daqp-0.4.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2044 2023-04-06 14:29:56.000000 daqp-0.4.0/setup.py
```

### Comparing `daqp-0.1.0/LICENSE` & `daqp-0.4.0/LICENSE`

 * *Files identical despite different names*

### Comparing `daqp-0.1.0/PKG-INFO` & `daqp-0.4.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: daqp
-Version: 0.1.0
+Version: 0.4.0
 Summary: DAQP: A dual active-set QP solver
 Home-page: http://github.com/darnstrom/daqp
 Author: Daniel Arnström
 Author-email: daniel.arnstrom@liu.se
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `daqp-0.1.0/README.md` & `daqp-0.4.0/README.md`

 * *Files identical despite different names*

### Comparing `daqp-0.1.0/setup.py` & `daqp-0.4.0/setup.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 from setuptools import setup,find_packages, Extension
-from setuptools.command.build_ext import build_ext as build_ext_orig
 import os
 from shutil import copyfile,copytree,rmtree
 from platform import system
 import pathlib
+from Cython.Distutils import build_ext 
+from Cython.Build import cythonize
 
 
 # Copy C source
 try:
     src_path = pathlib.Path(os.environ["PWD"], "../../../daqp")
 except:
     src_path = []
@@ -19,78 +20,40 @@
     copytree(os.path.join(src_path,'codegen'),os.path.join(csrc_dir,'codegen'))
     copyfile(os.path.join(src_path,'CMakeLists.txt'),os.path.join(csrc_dir,'CMakeLists.txt'))
     copyfile(os.path.join(src_path,'LICENSE'),pathlib.Path('./LICENSE'))
 else:
     print("Could not find daqp directory")
 
 
-class CMakeExtension(Extension):
-
-    def __init__(self, name):
-        super().__init__(name, sources=[])
-
-
-class build_ext(build_ext_orig):
-
-    def run(self):
-        for ext in self.extensions:
-            self.build_cmake(ext)
-        super().run()
-
-    def build_cmake(self, ext):
-        cwd = pathlib.Path().absolute()
-        cmake_path = os.path.join(pathlib.Path().absolute(),'csrc')
-
-
-        build_temp = pathlib.Path(self.build_temp)
-        build_temp.mkdir(parents=True, exist_ok=True)
-        extdir = pathlib.Path(self.get_ext_fullpath(ext.name))
-        extdir.mkdir(parents=True, exist_ok=True)
-
-        config = 'Debug' if self.debug else 'Release'
-        cmake_args = [
-            '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + str(extdir.parent.absolute()),
-            '-DCMAKE_BUILD_TYPE=' + config
-        ]
-
-        if system() == 'Windows':
-            cmake_args += ['-G', 'MinGW Makefiles']
-        else:  # Unix 
-            cmake_args += ['-G', 'Unix Makefiles']
-
-        build_args = [
-        ]
-
-        os.chdir(str(build_temp))
-        self.spawn(['cmake', str(cmake_path)] + cmake_args)
-        if not self.dry_run:
-            self.spawn(['cmake', '--build', '.'] + build_args)
-        os.chdir(str(cwd))
-
-        if system() == 'Windows':
-            copyfile(os.path.join(build_temp,'libdaqp.dll'),
-                     os.path.join(str(extdir.parent.absolute()),'libdaqp.dll'))
-
+cython_ext = Extension('daqp',
+        sources = ['daqp.pyx','daqp.pxd', 
+            'csrc/src/api.c', 
+            'csrc/src/auxiliary.c', 
+            'csrc/src/bnb.c', 
+            'csrc/src/daqp.c', 
+            'csrc/src/daqp_prox.c', 
+            'csrc/src/factorization.c', 
+            'csrc/src/utils.c', 
+            ],
+        library_dirs=['.'],
+        extra_compile_args=["-O3"],
+        include_dirs=['csrc/include'])
 
 setup(name='daqp',
-        version='0.1.0',
+        version='0.4.0',
         description='DAQP: A dual active-set QP solver',
         url='http://github.com/darnstrom/daqp',
         author='Daniel Arnström',
         author_email='daniel.arnstrom@liu.se',
         license='MIT',
-        packages=find_packages(
-            where='src',
-            include=['daqp']),
-        package_dir={"": "src"},
         long_description=open('README.md','r').read(),
         long_description_content_type='text/markdown',
-        ext_modules=[CMakeExtension('daqp/daqp')],
-        cmdclass={
-            'build_ext': build_ext,
-            },
+        ext_modules=cythonize(cython_ext),
+        cmdclass={'build_ext': build_ext},
+        package_data = {'':["daqp.pyx","daqp.pxd"]},
+        include_package_data = True,
         zip_safe=False)
 
 # Cleanup C-source
 if src_path and os.path.exists(src_path):
     rmtree(csrc_dir)
     os.remove(pathlib.Path('./LICENSE'))
```

### Comparing `daqp-0.1.0/src/daqp.egg-info/PKG-INFO` & `daqp-0.4.0/daqp.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: daqp
-Version: 0.1.0
+Version: 0.4.0
 Summary: DAQP: A dual active-set QP solver
 Home-page: http://github.com/darnstrom/daqp
 Author: Daniel Arnström
 Author-email: daniel.arnstrom@liu.se
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

