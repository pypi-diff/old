# Comparing `tmp/desktop-app-0.3.0.tar.gz` & `tmp/desktop-app-0.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "desktop-app-0.3.0.tar", last modified: Sun Jan 29 06:41:43 2023, max compression
+gzip compressed data, was "desktop-app-0.4.0.tar", last modified: Fri Apr  7 06:34:39 2023, max compression
```

## Comparing `desktop-app-0.3.0.tar` & `desktop-app-0.4.0.tar`

### file list

```diff
@@ -1,39 +1,39 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 06:41:43.781974 desktop-app-0.3.0/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 06:41:43.777974 desktop-app-0.3.0/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 06:41:43.777974 desktop-app-0.3.0/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)     8535 2023-01-29 06:41:30.000000 desktop-app-0.3.0/.github/workflows/release.yml
--rw-r--r--   0 runner    (1001) docker     (123)       78 2023-01-29 06:41:30.000000 desktop-app-0.3.0/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)     1287 2023-01-29 06:41:30.000000 desktop-app-0.3.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     4029 2023-01-29 06:41:43.781974 desktop-app-0.3.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3286 2023-01-29 06:41:30.000000 desktop-app-0.3.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 06:41:43.781974 desktop-app-0.3.0/desktop_app/
--rw-r--r--   0 runner    (1001) docker     (123)      219 2023-01-29 06:41:30.000000 desktop-app-0.3.0/desktop_app/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2048 2023-01-29 06:41:30.000000 desktop-app-0.3.0/desktop_app/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)      624 2023-01-29 06:41:30.000000 desktop-app-0.3.0/desktop_app/__version__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10910 2023-01-29 06:41:30.000000 desktop-app-0.3.0/desktop_app/environment.py
--rw-r--r--   0 runner    (1001) docker     (123)     1698 2023-01-29 06:41:30.000000 desktop-app-0.3.0/desktop_app/fix_entry_points.py
--rw-r--r--   0 runner    (1001) docker     (123)     3694 2023-01-29 06:41:30.000000 desktop-app-0.3.0/desktop_app/launcher.py
--rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-01-29 06:41:30.000000 desktop-app-0.3.0/desktop_app/linux.py
--rw-r--r--   0 runner    (1001) docker     (123)    12733 2023-01-29 06:41:30.000000 desktop-app-0.3.0/desktop_app/shell.py
--rw-r--r--   0 runner    (1001) docker     (123)     4224 2023-01-29 06:41:30.000000 desktop-app-0.3.0/desktop_app/windows.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 06:41:43.781974 desktop-app-0.3.0/desktop_app.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4029 2023-01-29 06:41:43.000000 desktop-app-0.3.0/desktop_app.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      723 2023-01-29 06:41:43.000000 desktop-app-0.3.0/desktop_app.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-29 06:41:43.000000 desktop-app-0.3.0/desktop_app.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-01-29 06:41:43.000000 desktop-app-0.3.0/desktop_app.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-29 06:41:43.000000 desktop-app-0.3.0/desktop_app.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       78 2023-01-29 06:41:43.000000 desktop-app-0.3.0/desktop_app.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       12 2023-01-29 06:41:43.000000 desktop-app-0.3.0/desktop_app.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 06:41:43.781974 desktop-app-0.3.0/example/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 06:41:43.781974 desktop-app-0.3.0/example/oink/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 06:41:30.000000 desktop-app-0.3.0/example/oink/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      618 2023-01-29 06:41:30.000000 desktop-app-0.3.0/example/oink/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)      201 2023-01-29 06:41:30.000000 desktop-app-0.3.0/example/oink/desktop-app.json
--rw-r--r--   0 runner    (1001) docker     (123)   106487 2023-01-29 06:41:30.000000 desktop-app-0.3.0/example/oink/oink.ico
--rw-r--r--   0 runner    (1001) docker     (123)    22906 2023-01-29 06:41:30.000000 desktop-app-0.3.0/example/oink/oink.svg
--rw-r--r--   0 runner    (1001) docker     (123)      502 2023-01-29 06:41:30.000000 desktop-app-0.3.0/example/setup.py
--rw-r--r--   0 runner    (1001) docker     (123)      107 2023-01-29 06:41:30.000000 desktop-app-0.3.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      985 2023-01-29 06:41:43.781974 desktop-app-0.3.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      666 2023-01-29 06:41:30.000000 desktop-app-0.3.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 06:41:43.781974 desktop-app-0.3.0/src/
--rw-r--r--   0 runner    (1001) docker     (123)     2323 2023-01-29 06:41:30.000000 desktop-app-0.3.0/src/wineventhook.cpp
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:34:39.136473 desktop-app-0.4.0/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:34:39.132473 desktop-app-0.4.0/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:34:39.132473 desktop-app-0.4.0/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)     8513 2023-04-07 06:34:26.000000 desktop-app-0.4.0/.github/workflows/release.yml
+-rw-r--r--   0 runner    (1001) docker     (123)       78 2023-04-07 06:34:26.000000 desktop-app-0.4.0/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)     1287 2023-04-07 06:34:26.000000 desktop-app-0.4.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     4029 2023-04-07 06:34:39.136473 desktop-app-0.4.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3286 2023-04-07 06:34:26.000000 desktop-app-0.4.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:34:39.136473 desktop-app-0.4.0/desktop_app/
+-rw-r--r--   0 runner    (1001) docker     (123)      219 2023-04-07 06:34:26.000000 desktop-app-0.4.0/desktop_app/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2048 2023-04-07 06:34:26.000000 desktop-app-0.4.0/desktop_app/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      624 2023-04-07 06:34:26.000000 desktop-app-0.4.0/desktop_app/__version__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10910 2023-04-07 06:34:26.000000 desktop-app-0.4.0/desktop_app/environment.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1698 2023-04-07 06:34:26.000000 desktop-app-0.4.0/desktop_app/fix_entry_points.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3694 2023-04-07 06:34:26.000000 desktop-app-0.4.0/desktop_app/launcher.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-04-07 06:34:26.000000 desktop-app-0.4.0/desktop_app/linux.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12733 2023-04-07 06:34:26.000000 desktop-app-0.4.0/desktop_app/shell.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4224 2023-04-07 06:34:26.000000 desktop-app-0.4.0/desktop_app/windows.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:34:39.136473 desktop-app-0.4.0/desktop_app.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4029 2023-04-07 06:34:39.000000 desktop-app-0.4.0/desktop_app.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      723 2023-04-07 06:34:39.000000 desktop-app-0.4.0/desktop_app.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 06:34:39.000000 desktop-app-0.4.0/desktop_app.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-04-07 06:34:39.000000 desktop-app-0.4.0/desktop_app.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 06:34:38.000000 desktop-app-0.4.0/desktop_app.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       78 2023-04-07 06:34:39.000000 desktop-app-0.4.0/desktop_app.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-07 06:34:39.000000 desktop-app-0.4.0/desktop_app.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:34:39.136473 desktop-app-0.4.0/example/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:34:39.136473 desktop-app-0.4.0/example/oink/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 06:34:26.000000 desktop-app-0.4.0/example/oink/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      618 2023-04-07 06:34:26.000000 desktop-app-0.4.0/example/oink/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      201 2023-04-07 06:34:26.000000 desktop-app-0.4.0/example/oink/desktop-app.json
+-rw-r--r--   0 runner    (1001) docker     (123)   106487 2023-04-07 06:34:26.000000 desktop-app-0.4.0/example/oink/oink.ico
+-rw-r--r--   0 runner    (1001) docker     (123)    22906 2023-04-07 06:34:26.000000 desktop-app-0.4.0/example/oink/oink.svg
+-rw-r--r--   0 runner    (1001) docker     (123)      502 2023-04-07 06:34:26.000000 desktop-app-0.4.0/example/setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)      107 2023-04-07 06:34:26.000000 desktop-app-0.4.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      985 2023-04-07 06:34:39.136473 desktop-app-0.4.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      666 2023-04-07 06:34:26.000000 desktop-app-0.4.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:34:39.136473 desktop-app-0.4.0/src/
+-rw-r--r--   0 runner    (1001) docker     (123)     2323 2023-04-07 06:34:26.000000 desktop-app-0.4.0/src/wineventhook.cpp
```

### Comparing `desktop-app-0.3.0/.github/workflows/release.yml` & `desktop-app-0.4.0/.github/workflows/release.yml`

 * *Files 16% similar despite different names*

```diff
@@ -33,33 +33,37 @@
 jobs:
   build:
     name: Build
     runs-on: ${{ matrix.os }}
     strategy:
       matrix:
         include:
-          - { os: ubuntu-latest,   python: '3.10',  arch: x64 }
-          - { os: ubuntu-latest,   python: '3.9',  arch: x64 }
-          - { os: ubuntu-latest,   python: '3.8',  arch: x64 }
-          - { os: ubuntu-latest,   python: '3.7',  arch: x64 }
-
-          - { os: macos-10.15,    python: '3.10',  arch: x64 }
-          - { os: macos-10.15,    python: '3.9',  arch: x64 }
-          - { os: macos-10.15,    python: '3.8',  arch: x64 }
-          - { os: macos-10.15,    python: '3.7',  arch: x64 }
-
-          - { os: windows-latest,  python: '3.10',  arch: x64 }
-          - { os: windows-latest,  python: '3.9',  arch: x64 }
-          - { os: windows-latest,  python: '3.8',  arch: x64 }
-          - { os: windows-latest,  python: '3.7',  arch: x64 }
-
-          - { os: windows-latest,  python: '3.10',  arch: x86 }
-          - { os: windows-latest,  python: '3.9',  arch: x86 }
-          - { os: windows-latest,  python: '3.8',  arch: x86 }
-          - { os: windows-latest,  python: '3.7',  arch: x86 }
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
 
     if: github.repository == 'chrisjbillington/desktop-app' && (github.event_name != 'create' || github.event.ref_type != 'branch')
     steps:
       - name: Checkout
         uses: actions/checkout@v3
         with:
           fetch-depth: 0
@@ -91,55 +95,55 @@
         if: strategy.job-index == 0 || (env.PURE == 'false' && runner.os != 'Linux')
         uses: actions/upload-artifact@v3
         with:
           name: dist
           path: ./dist
 
       - name: Set Variables for Conda Build
+        if: matrix.conda
         shell: bash
         run: |
           if [ $NOARCH == true ]; then
               CONDA_BUILD_ARGS="--noarch"
           else
               CONDA_BUILD_ARGS=""
           fi
           echo "CONDA_BUILD_ARGS=$CONDA_BUILD_ARGS" >> $GITHUB_ENV
 
       - name: Install Miniconda
-        # We need https://github.com/conda-incubator/setup-miniconda/pull/189 in order
-        # to be able to install 32-bit miniconda on Windows. Once setup-miniconda 2.1.2
-        # is released with this fix, can change to @v2.
-        uses: conda-incubator/setup-miniconda@1a875d105ac03256664b54c882c8c374ce617ef6
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
         shell: bash -l {0}
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
+        if: matrix.conda
         uses: actions/upload-artifact@v3
         with:
           name: conda_packages
           path: ./conda_packages
 
 
   manylinux:
@@ -157,15 +161,15 @@
         if: github.event.ref_type != 'tag' && env.PURE == 'false'
         run: git tag -d $(git tag --points-at HEAD)
 
       - name: Build Manylinux Wheels
         if: env.PURE == 'false'
         uses: RalfG/python-wheels-manylinux-build@v0.4.2
         with:
-          python-versions: 'cp37-cp37m cp38-cp38 cp39-cp39 cp310-cp310'
+          python-versions: 'cp37-cp37m cp38-cp38 cp39-cp39 cp310-cp310 cp311-cp311'
           pre-build-command: 'git config --global --add safe.directory "*"'
 
       - name: Upload Artifact
         if: env.PURE == 'false'
         uses: actions/upload-artifact@v3
         with:
           name: dist
@@ -185,53 +189,42 @@
 
       - name: Download Artifact
         uses: actions/download-artifact@v3
         with:
           name: conda_packages
           path: ./conda_packages
 
-      - name: Publish on TestPyPI
-        uses: pypa/gh-action-pypi-publish@release/v1
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
         uses: conda-incubator/setup-miniconda@v2
         with:
```

### Comparing `desktop-app-0.3.0/LICENSE` & `desktop-app-0.4.0/LICENSE`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/PKG-INFO` & `desktop-app-0.4.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: desktop-app
-Version: 0.3.0
+Version: 0.4.0
 Summary: OS menu shortcuts, correct taskbar behaviour, and environment activation for Python GUI apps
 Home-page: http://github.com/chrisjbillington/desktop-app
 Author: Chris Billington
 Author-email: chrisjbillington@gmail.com
 License: BSD
 Keywords: desktop windows launchers taskbar start-menu
 Classifier: License :: OSI Approved :: BSD License
```

### Comparing `desktop-app-0.3.0/README.md` & `desktop-app-0.4.0/README.md`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/desktop_app/__main__.py` & `desktop-app-0.4.0/desktop_app/__main__.py`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/desktop_app/__version__.py` & `desktop-app-0.4.0/desktop_app/__version__.py`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/desktop_app/environment.py` & `desktop-app-0.4.0/desktop_app/environment.py`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/desktop_app/fix_entry_points.py` & `desktop-app-0.4.0/desktop_app/fix_entry_points.py`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/desktop_app/launcher.py` & `desktop-app-0.4.0/desktop_app/launcher.py`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/desktop_app/linux.py` & `desktop-app-0.4.0/desktop_app/linux.py`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/desktop_app/shell.py` & `desktop-app-0.4.0/desktop_app/shell.py`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/desktop_app/windows.py` & `desktop-app-0.4.0/desktop_app/windows.py`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/desktop_app.egg-info/PKG-INFO` & `desktop-app-0.4.0/desktop_app.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: desktop-app
-Version: 0.3.0
+Version: 0.4.0
 Summary: OS menu shortcuts, correct taskbar behaviour, and environment activation for Python GUI apps
 Home-page: http://github.com/chrisjbillington/desktop-app
 Author: Chris Billington
 Author-email: chrisjbillington@gmail.com
 License: BSD
 Keywords: desktop windows launchers taskbar start-menu
 Classifier: License :: OSI Approved :: BSD License
```

### Comparing `desktop-app-0.3.0/desktop_app.egg-info/SOURCES.txt` & `desktop-app-0.4.0/desktop_app.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/example/oink/__main__.py` & `desktop-app-0.4.0/example/oink/__main__.py`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/example/oink/oink.ico` & `desktop-app-0.4.0/example/oink/oink.ico`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/example/oink/oink.svg` & `desktop-app-0.4.0/example/oink/oink.svg`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/setup.cfg` & `desktop-app-0.4.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/setup.py` & `desktop-app-0.4.0/setup.py`

 * *Files identical despite different names*

### Comparing `desktop-app-0.3.0/src/wineventhook.cpp` & `desktop-app-0.4.0/src/wineventhook.cpp`

 * *Files identical despite different names*

