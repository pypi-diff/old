# Comparing `tmp/labscript-c-extensions-1.0.2.tar.gz` & `tmp/labscript-c-extensions-1.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "labscript-c-extensions-1.0.2.tar", last modified: Fri Nov 19 04:51:38 2021, max compression
+gzip compressed data, was "labscript-c-extensions-1.1.0.tar", last modified: Fri Apr  7 08:31:22 2023, max compression
```

## Comparing `labscript-c-extensions-1.0.2.tar` & `labscript-c-extensions-1.1.0.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-19 04:51:38.582052 labscript-c-extensions-1.0.2/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-19 04:51:38.578052 labscript-c-extensions-1.0.2/.github/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-19 04:51:38.582052 labscript-c-extensions-1.0.2/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (121)     8553 2021-11-19 04:51:31.000000 labscript-c-extensions-1.0.2/.github/workflows/release.yml
--rw-r--r--   0 runner    (1001) docker     (121)     1926 2021-11-19 04:51:31.000000 labscript-c-extensions-1.0.2/.gitignore
--rw-r--r--   0 runner    (1001) docker     (121)     1329 2021-11-19 04:51:31.000000 labscript-c-extensions-1.0.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     3467 2021-11-19 04:51:38.582052 labscript-c-extensions-1.0.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2492 2021-11-19 04:51:31.000000 labscript-c-extensions-1.0.2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-19 04:51:38.582052 labscript-c-extensions-1.0.2/labscript_c_extensions/
--rw-r--r--   0 runner    (1001) docker     (121)      962 2021-11-19 04:51:31.000000 labscript-c-extensions-1.0.2/labscript_c_extensions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1464 2021-11-19 04:51:31.000000 labscript-c-extensions-1.0.2/labscript_c_extensions/__version__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-19 04:51:38.582052 labscript-c-extensions-1.0.2/labscript_c_extensions/runviewer/
--rw-r--r--   0 runner    (1001) docker     (121)      839 2021-11-19 04:51:31.000000 labscript-c-extensions-1.0.2/labscript_c_extensions/runviewer/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-19 04:51:38.582052 labscript-c-extensions-1.0.2/labscript_c_extensions.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3467 2021-11-19 04:51:38.000000 labscript-c-extensions-1.0.2/labscript_c_extensions.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      511 2021-11-19 04:51:38.000000 labscript-c-extensions-1.0.2/labscript_c_extensions.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-11-19 04:51:38.000000 labscript-c-extensions-1.0.2/labscript_c_extensions.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-11-19 04:51:38.000000 labscript-c-extensions-1.0.2/labscript_c_extensions.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       46 2021-11-19 04:51:38.000000 labscript-c-extensions-1.0.2/labscript_c_extensions.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       23 2021-11-19 04:51:38.000000 labscript-c-extensions-1.0.2/labscript_c_extensions.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      117 2021-11-19 04:51:31.000000 labscript-c-extensions-1.0.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)     1060 2021-11-19 04:51:38.582052 labscript-c-extensions-1.0.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)      583 2021-11-19 04:51:31.000000 labscript-c-extensions-1.0.2/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-19 04:51:38.578052 labscript-c-extensions-1.0.2/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-11-19 04:51:38.582052 labscript-c-extensions-1.0.2/src/runviewer/
--rw-r--r--   0 runner    (1001) docker     (121)     5239 2021-11-19 04:51:31.000000 labscript-c-extensions-1.0.2/src/runviewer/resample.pyx
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:31:22.745074 labscript-c-extensions-1.1.0/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:31:22.737074 labscript-c-extensions-1.1.0/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:31:22.741073 labscript-c-extensions-1.1.0/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)     8544 2023-04-07 08:31:08.000000 labscript-c-extensions-1.1.0/.github/workflows/release.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1926 2023-04-07 08:31:08.000000 labscript-c-extensions-1.1.0/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)     1329 2023-04-07 08:31:08.000000 labscript-c-extensions-1.1.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3549 2023-04-07 08:31:22.745074 labscript-c-extensions-1.1.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2492 2023-04-07 08:31:08.000000 labscript-c-extensions-1.1.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:31:22.741073 labscript-c-extensions-1.1.0/labscript_c_extensions/
+-rw-r--r--   0 runner    (1001) docker     (123)      962 2023-04-07 08:31:08.000000 labscript-c-extensions-1.1.0/labscript_c_extensions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1464 2023-04-07 08:31:08.000000 labscript-c-extensions-1.1.0/labscript_c_extensions/__version__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:31:22.745074 labscript-c-extensions-1.1.0/labscript_c_extensions/runviewer/
+-rw-r--r--   0 runner    (1001) docker     (123)      839 2023-04-07 08:31:08.000000 labscript-c-extensions-1.1.0/labscript_c_extensions/runviewer/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:31:22.745074 labscript-c-extensions-1.1.0/labscript_c_extensions.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3549 2023-04-07 08:31:22.000000 labscript-c-extensions-1.1.0/labscript_c_extensions.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      511 2023-04-07 08:31:22.000000 labscript-c-extensions-1.1.0/labscript_c_extensions.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 08:31:22.000000 labscript-c-extensions-1.1.0/labscript_c_extensions.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 08:31:22.000000 labscript-c-extensions-1.1.0/labscript_c_extensions.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       46 2023-04-07 08:31:22.000000 labscript-c-extensions-1.1.0/labscript_c_extensions.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-07 08:31:22.000000 labscript-c-extensions-1.1.0/labscript_c_extensions.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      117 2023-04-07 08:31:08.000000 labscript-c-extensions-1.1.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1140 2023-04-07 08:31:22.745074 labscript-c-extensions-1.1.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      583 2023-04-07 08:31:08.000000 labscript-c-extensions-1.1.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:31:22.741073 labscript-c-extensions-1.1.0/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:31:22.745074 labscript-c-extensions-1.1.0/src/runviewer/
+-rw-r--r--   0 runner    (1001) docker     (123)     5239 2023-04-07 08:31:08.000000 labscript-c-extensions-1.1.0/src/runviewer/resample.pyx
```

### Comparing `labscript-c-extensions-1.0.2/.github/workflows/release.yml` & `labscript-c-extensions-1.1.0/.github/workflows/release.yml`

 * *Files 20% similar despite different names*

```diff
@@ -5,21 +5,16 @@
     branches:
       - master
       - maintenance/*
   create:
     tags:
       - 'v[0-9]+.[0-9]+.[0-9]+*'
 
-defaults:
-  run:
-    shell: bash -l {0}
-
 env:
   PACKAGE_NAME: labscript-c-extensions
-  SCM_VERSION_SCHEME: release-branch-semver
   SCM_LOCAL_SCHEME: no-local-version
   ANACONDA_USER: labscript-suite
 
   # Configuration for a package with compiled extensions:
   PURE: false
   NOARCH: false
 
@@ -38,231 +33,224 @@
 jobs:
   build:
     name: Build
     runs-on: ${{ matrix.os }}
     strategy:
       matrix:
         include:
-          - { os: ubuntu-latest,   python: 3.9,  arch: x64 }
-          - { os: ubuntu-latest,   python: 3.8,  arch: x64 }
-          - { os: ubuntu-latest,   python: 3.7,  arch: x64 }
-          - { os: ubuntu-latest,   python: 3.6,  arch: x64 }
-
-          - { os: macos-latest,    python: 3.9,  arch: x64 }
-          - { os: macos-latest,    python: 3.8,  arch: x64 }
-          - { os: macos-latest,    python: 3.7,  arch: x64 }
-          - { os: macos-latest,    python: 3.6,  arch: x64 }
-
-          - { os: windows-latest,  python: 3.9,  arch: x64 }
-          - { os: windows-latest,  python: 3.8,  arch: x64 }
-          - { os: windows-latest,  python: 3.7,  arch: x64 }
-          - { os: windows-latest,  python: 3.6,  arch: x64 }
-
-          - { os: windows-latest,  python: 3.9,  arch: x86 }
-          - { os: windows-latest,  python: 3.8,  arch: x86 }
-          - { os: windows-latest,  python: 3.7,  arch: x86 }
-          - { os: windows-latest,  python: 3.6,  arch: x86 }
+          - { os: ubuntu-latest,   python: '3.11',  arch: x64, conda: true}
+          - { os: ubuntu-latest,   python: '3.10',  arch: x64, conda: true }
+          - { os: ubuntu-latest,   python: '3.9',  arch: x64, conda: true }
+          - { os: ubuntu-latest,   python: '3.8',  arch: x64, conda: true }
+          - { os: ubuntu-latest,   python: '3.7',  arch: x64, conda: true }
+
+          - { os: macos-11,    python: '3.11',  arch: x64, conda: true }
+          - { os: macos-11,    python: '3.10',  arch: x64, conda: true }
+          - { os: macos-11,    python: '3.9',  arch: x64, conda: true }
+          - { os: macos-11,    python: '3.8',  arch: x64, conda: true }
+          - { os: macos-11,    python: '3.7',  arch: x64, conda: true }
+
+          - { os: windows-latest,  python: '3.11',  arch: x64, conda: true }
+          - { os: windows-latest,  python: '3.10',  arch: x64, conda: true }
+          - { os: windows-latest,  python: '3.9',  arch: x64, conda: true }
+          - { os: windows-latest,  python: '3.8',  arch: x64, conda: true }
+          - { os: windows-latest,  python: '3.7',  arch: x64, conda: true }
+
+          - { os: windows-latest,  python: '3.11',  arch: x86, conda: false } # conda not yet available
+          - { os: windows-latest,  python: '3.10',  arch: x86, conda: true }
+          - { os: windows-latest,  python: '3.9',  arch: x86, conda: true }
+          - { os: windows-latest,  python: '3.8',  arch: x86, conda: true }
+          - { os: windows-latest,  python: '3.7',  arch: x86, conda: true }
 
     if: github.repository == 'labscript-suite/labscript-c-extensions' && (github.event_name != 'create' || github.event.ref_type != 'branch')
     steps:
       - name: Checkout
-        uses: actions/checkout@v2
+        uses: actions/checkout@v3
         with:
           fetch-depth: 0
 
       - name: Ignore Tags
         if: github.event.ref_type != 'tag'
         run: git tag -d $(git tag --points-at HEAD)
 
       - name: Install Python
-        uses: actions/setup-python@v2
+        uses: actions/setup-python@v4
         with:
           python-version: ${{ matrix.python }}
           architecture: ${{ matrix.arch }}
 
       - name: Source Distribution
         if: strategy.job-index == 0
         run: |
-          python -m pip install --upgrade pip setuptools wheel pep517
-          python -m pep517.build -s .
+          python -m pip install --upgrade pip setuptools wheel build
+          python -m build -s .
 
       - name: Wheel Distribution
         # Impure Linux wheels are built in the manylinux job.
         if: (env.PURE == 'true' && strategy.job-index == 0) || (env.PURE == 'false' && runner.os != 'Linux')
         run: |
-          python -m pip install --upgrade pip setuptools wheel pep517
-          python -m pep517.build -b .
+          python -m pip install --upgrade pip setuptools wheel build
+          python -m build -w .
 
       - name: Upload Artifact
         if: strategy.job-index == 0 || (env.PURE == 'false' && runner.os != 'Linux')
-        uses: actions/upload-artifact@v2
+        uses: actions/upload-artifact@v3
         with:
           name: dist
           path: ./dist
 
       - name: Set Variables for Conda Build
+        if: matrix.conda
+        shell: bash
         run: |
           if [ $NOARCH == true ]; then
               CONDA_BUILD_ARGS="--noarch"
           else
               CONDA_BUILD_ARGS=""
           fi
           echo "CONDA_BUILD_ARGS=$CONDA_BUILD_ARGS" >> $GITHUB_ENV
 
       - name: Install Miniconda
-        # 2.0.1 until https://github.com/conda-incubator/setup-miniconda/pull/189 merged
-        # and released. Then can change to v2
-        uses: conda-incubator/setup-miniconda@v2.0.1
+        if: matrix.conda
+        uses: conda-incubator/setup-miniconda@v2
         with:
           auto-update-conda: true
           python-version: ${{ matrix.python }}
           architecture: ${{ matrix.arch }}
           miniconda-version: "latest"
 
-      - name: Workaround conda-build incompatibility with xcode >12
+      - name: Workaround conda-build incompatibility with xcode 12+
         if: runner.os == 'macOS'
         uses: maxim-lobanov/setup-xcode@v1
         with:
           xcode-version: 11.7
 
       - name: Conda package (Unix)
-        if: runner.os != 'Windows'
+        if: (matrix.conda && runner.os != 'Windows')
+        shell: bash -l {0}
         run: |
           conda install -c labscript-suite setuptools-conda
           setuptools-conda build $CONDA_BUILD_ARGS .
 
       - name: Conda Package (Windows)
-        if: runner.os == 'Windows'
+        if: (matrix.conda && runner.os == 'Windows')
         shell: cmd /C CALL {0}
         run: |
           conda install -c labscript-suite setuptools-conda && ^
           setuptools-conda build %CONDA_BUILD_ARGS% --croot ${{ runner.temp }}\cb .
 
       - name: Upload Artifact
-        uses: actions/upload-artifact@v2
+        if: matrix.conda
+        uses: actions/upload-artifact@v3
         with:
           name: conda_packages
           path: ./conda_packages
 
 
   manylinux:
     name: Build Manylinux
     runs-on: ubuntu-latest
-    strategy:
-      matrix:
-        include:
-          - { python: 'cp36-cp36m cp37-cp37m cp38-cp38 cp39-cp39' }
-
     if: github.repository == 'labscript-suite/labscript-c-extensions' && (github.event_name != 'create' || github.event.ref_type != 'branch')
     steps:
       - name: Checkout
         if: env.PURE == 'false'
-        uses: actions/checkout@v2
+        uses: actions/checkout@v3
         with:
           fetch-depth: 0
 
       - name: Ignore Tags
         if: github.event.ref_type != 'tag' && env.PURE == 'false'
         run: git tag -d $(git tag --points-at HEAD)
 
       - name: Build Manylinux Wheels
         if: env.PURE == 'false'
-        uses: RalfG/python-wheels-manylinux-build@v0.2.2-manylinux2010_x86_64
+        uses: RalfG/python-wheels-manylinux-build@v0.4.2
         with:
-          python-versions: ${{ matrix.python }}
+          python-versions: 'cp37-cp37m cp38-cp38 cp39-cp39 cp310-cp310 cp311-cp311'
+          pre-build-command: 'git config --global --add safe.directory "*"'
 
       - name: Upload Artifact
         if: env.PURE == 'false'
-        uses: actions/upload-artifact@v2
+        uses: actions/upload-artifact@v3
         with:
           name: dist
-          path: wheelhouse/*manylinux*.whl
+          path: dist/*manylinux*.whl
 
   release:
     name: Release
     runs-on: ubuntu-latest
     needs: [build, manylinux]
     steps:
 
       - name: Download Artifact
-        uses: actions/download-artifact@v2
+        uses: actions/download-artifact@v3
         with:
           name: dist
           path: ./dist
 
       - name: Download Artifact
-        uses: actions/download-artifact@v2
+        uses: actions/download-artifact@v3
         with:
           name: conda_packages
           path: ./conda_packages
 
-      - name: Publish on TestPyPI
-        uses: pypa/gh-action-pypi-publish@master
-        with:
-          user: __token__
-          password: ${{ secrets.testpypi }}
-          repository_url: https://test.pypi.org/legacy/
-
       - name: Get Version Number
         if: github.event.ref_type == 'tag'
         run: |
           VERSION="${GITHUB_REF/refs\/tags\/v/}"
           echo "VERSION=$VERSION" >> $GITHUB_ENV
 
-      - name: Create GitHub Release
+      - name: Create GitHub Release and Upload Release Asset
         if: github.event.ref_type == 'tag'
-        id: create_release
-        uses: actions/create-release@latest
+        uses: softprops/action-gh-release@v1
         env:
           GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         with:
           tag_name: ${{ github.event.ref }}
-          release_name: ${{ env.PACKAGE_NAME }} ${{ env.VERSION }}
+          name: ${{ env.PACKAGE_NAME }} ${{ env.VERSION }}
           draft: true
           prerelease: ${{ contains(github.event.ref, 'rc') }}
+          files: ./dist/${{ env.PACKAGE_NAME }}-${{ env.VERSION }}.tar.gz
 
-      - name: Upload Release Asset
-        if: github.event.ref_type == 'tag'
-        uses: actions/upload-release-asset@v1
-        env:
-          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
+      - name: Publish on TestPyPI
+        uses: pypa/gh-action-pypi-publish@release/v1
         with:
-          upload_url: ${{ steps.create_release.outputs.upload_url }}
-          asset_path: ./dist/${{ env.PACKAGE_NAME }}-${{ env.VERSION }}.tar.gz
-          asset_name: ${{ env.PACKAGE_NAME }}-${{ env.VERSION }}.tar.gz
-          asset_content_type: application/gzip
+          user: __token__
+          password: ${{ secrets.testpypi }}
+          repository-url: https://test.pypi.org/legacy/
 
       - name: Publish on PyPI
         if: github.event.ref_type == 'tag'
-        uses: pypa/gh-action-pypi-publish@master
+        uses: pypa/gh-action-pypi-publish@release/v1
         with:
           user: __token__
           password: ${{ secrets.pypi }}
 
       - name: Install Miniconda
-        # 2.0.1 until https://github.com/conda-incubator/setup-miniconda/pull/189 merged
-        # and released. Then can change to v2
-        uses: conda-incubator/setup-miniconda@v2.0.1
+        uses: conda-incubator/setup-miniconda@v2
         with:
           auto-update-conda: true
 
       - name: Install Anaconda cloud client
+        shell: bash -l {0}
         run: conda install anaconda-client
 
       - name: Publish to Anaconda test label
         if: github.event.ref_type != 'tag'
+        shell: bash -l {0}
         run: |
           anaconda \
             --token ${{ secrets.ANACONDA_API_TOKEN }} \
             upload \
             --user $ANACONDA_USER \
             --label test \
             conda_packages/*/*
 
       - name: Publish to Anaconda main label
+        shell: bash -l {0}
         if: github.event.ref_type == 'tag'
         run: |
           anaconda \
             --token ${{ secrets.ANACONDA_API_TOKEN }} \
             upload \
             --user $ANACONDA_USER \
             conda_packages/*/*
```

### Comparing `labscript-c-extensions-1.0.2/.gitignore` & `labscript-c-extensions-1.1.0/.gitignore`

 * *Files identical despite different names*

### Comparing `labscript-c-extensions-1.0.2/LICENSE` & `labscript-c-extensions-1.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `labscript-c-extensions-1.0.2/PKG-INFO` & `labscript-c-extensions-1.1.0/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,26 +1,27 @@
 Metadata-Version: 2.1
 Name: labscript-c-extensions
-Version: 1.0.2
+Version: 1.1.0
 Summary: A module containing C-extensions for the labscript suite
 Home-page: http://labscriptsuite.org
 Author: The labscript suite community
 Author-email: labscriptsuite@googlegroups.com
 License: BSD
 Project-URL: Source Code, https://github.com/labscript-suite/labscript-c-extensions
 Project-URL: Download, https://github.com/labscript-suite/labscript-c-extensions/releases
 Project-URL: Tracker, https://github.com/labscript-suite/labscript-c-extensions/issues
 Keywords: experiment visualization
-Platform: UNKNOWN
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 <img src="https://raw.githubusercontent.com/labscript-suite/labscript-suite/master/art/labscript_32nx32n.svg" height="64" alt="the labscript suite" align="right">
 
 # the _labscript suite_ » labscript-c-extensions
@@ -41,9 +42,7 @@
 
 Bundling these extensions in a separate module ensures that developer installations of other _labscript suite_ components don't depend on build tools, as they can install the prebuilt wheel/conda package containing the extensions. Only developers of these extensions need the build tools (for example, [MSVC++ on Windows](https://wiki.python.org/moin/WindowsCompilers))
 
 
 ## Installation
 
 labscript-c-extensions is distributed as a Python package on [PyPI](https://pypi.org/user/labscript-suite) and [Anaconda Cloud](https://anaconda.org/labscript-suite), and should be installed with other components of the _labscript suite_. Please see the [installation guide](https://docs.labscriptsuite.org/en/latest/installation) for details.
-
-
```

### Comparing `labscript-c-extensions-1.0.2/README.md` & `labscript-c-extensions-1.1.0/README.md`

 * *Files identical despite different names*

### Comparing `labscript-c-extensions-1.0.2/labscript_c_extensions/__init__.py` & `labscript-c-extensions-1.1.0/labscript_c_extensions/__init__.py`

 * *Files identical despite different names*

### Comparing `labscript-c-extensions-1.0.2/labscript_c_extensions/__version__.py` & `labscript-c-extensions-1.1.0/labscript_c_extensions/__version__.py`

 * *Files identical despite different names*

### Comparing `labscript-c-extensions-1.0.2/labscript_c_extensions/runviewer/__init__.py` & `labscript-c-extensions-1.1.0/labscript_c_extensions/runviewer/__init__.py`

 * *Files identical despite different names*

### Comparing `labscript-c-extensions-1.0.2/labscript_c_extensions.egg-info/PKG-INFO` & `labscript-c-extensions-1.1.0/labscript_c_extensions.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,26 +1,27 @@
 Metadata-Version: 2.1
 Name: labscript-c-extensions
-Version: 1.0.2
+Version: 1.1.0
 Summary: A module containing C-extensions for the labscript suite
 Home-page: http://labscriptsuite.org
 Author: The labscript suite community
 Author-email: labscriptsuite@googlegroups.com
 License: BSD
 Project-URL: Source Code, https://github.com/labscript-suite/labscript-c-extensions
 Project-URL: Download, https://github.com/labscript-suite/labscript-c-extensions/releases
 Project-URL: Tracker, https://github.com/labscript-suite/labscript-c-extensions/issues
 Keywords: experiment visualization
-Platform: UNKNOWN
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 <img src="https://raw.githubusercontent.com/labscript-suite/labscript-suite/master/art/labscript_32nx32n.svg" height="64" alt="the labscript suite" align="right">
 
 # the _labscript suite_ » labscript-c-extensions
@@ -41,9 +42,7 @@
 
 Bundling these extensions in a separate module ensures that developer installations of other _labscript suite_ components don't depend on build tools, as they can install the prebuilt wheel/conda package containing the extensions. Only developers of these extensions need the build tools (for example, [MSVC++ on Windows](https://wiki.python.org/moin/WindowsCompilers))
 
 
 ## Installation
 
 labscript-c-extensions is distributed as a Python package on [PyPI](https://pypi.org/user/labscript-suite) and [Anaconda Cloud](https://anaconda.org/labscript-suite), and should be installed with other components of the _labscript suite_. Please see the [installation guide](https://docs.labscriptsuite.org/en/latest/installation) for details.
-
-
```

### Comparing `labscript-c-extensions-1.0.2/setup.cfg` & `labscript-c-extensions-1.1.0/setup.cfg`

 * *Files 9% similar despite different names*

```diff
@@ -15,14 +15,16 @@
 classifiers = 
 	License :: OSI Approved :: BSD License
 	Programming Language :: Python :: 3 :: Only
 	Programming Language :: Python :: 3.6
 	Programming Language :: Python :: 3.7
 	Programming Language :: Python :: 3.8
 	Programming Language :: Python :: 3.9
+	Programming Language :: Python :: 3.10
+	Programming Language :: Python :: 3.11
 
 [options]
 zip_safe = False
 include_package_data = True
 packages = find:
 python_requires = >=3.6
 install_requires =
```

### Comparing `labscript-c-extensions-1.0.2/setup.py` & `labscript-c-extensions-1.1.0/setup.py`

 * *Files identical despite different names*

### Comparing `labscript-c-extensions-1.0.2/src/runviewer/resample.pyx` & `labscript-c-extensions-1.1.0/src/runviewer/resample.pyx`

 * *Files identical despite different names*

