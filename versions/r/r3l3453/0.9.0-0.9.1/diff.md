# Comparing `tmp/r3l3453-0.9.0.tar.gz` & `tmp/r3l3453-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\r3l3453-0.9.0.tar", last modified: Sat Sep 19 14:24:55 2020, max compression
+gzip compressed data, was "r3l3453-0.9.1.tar", last modified: Sat Oct 16 14:33:42 2021, max compression
```

## Comparing `r3l3453-0.9.0.tar` & `r3l3453-0.9.1.tar`

### file list

```diff
@@ -1,16 +1,17 @@
-drwxrwxrwx   0        0        0        0 2020-09-19 14:24:55.602681 r3l3453-0.9.0/
--rw-rw-rw-   0        0        0     1709 2020-09-19 14:24:55.601684 r3l3453-0.9.0/PKG-INFO
--rw-rw-rw-   0        0        0      800 2020-09-19 11:08:43.000000 r3l3453-0.9.0/README.rst
-drwxrwxrwx   0        0        0        0 2020-09-19 14:24:55.591594 r3l3453-0.9.0/r3l3453/
--rw-rw-rw-   0        0        0     7207 2020-09-19 14:24:54.000000 r3l3453-0.9.0/r3l3453/__init__.py
--rw-rw-rw-   0        0        0      111 2020-08-14 12:20:15.000000 r3l3453-0.9.0/r3l3453/__main__.py
-drwxrwxrwx   0        0        0        0 2020-09-19 14:24:55.600686 r3l3453-0.9.0/r3l3453.egg-info/
--rw-rw-rw-   0        0        0     1709 2020-09-19 14:24:55.000000 r3l3453-0.9.0/r3l3453.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      273 2020-09-19 14:24:55.000000 r3l3453-0.9.0/r3l3453.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2020-09-19 14:24:55.000000 r3l3453-0.9.0/r3l3453.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       74 2020-09-19 14:24:55.000000 r3l3453-0.9.0/r3l3453.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0       18 2020-09-19 14:24:55.000000 r3l3453-0.9.0/r3l3453.egg-info/requires.txt
--rw-rw-rw-   0        0        0        8 2020-09-19 14:24:55.000000 r3l3453-0.9.0/r3l3453.egg-info/top_level.txt
--rw-rw-rw-   0        0        0        2 2020-07-05 09:29:12.000000 r3l3453-0.9.0/r3l3453.egg-info/zip-safe
--rw-rw-rw-   0        0        0       42 2020-09-19 14:24:55.602681 r3l3453-0.9.0/setup.cfg
--rw-rw-rw-   0        0        0     1179 2020-09-19 14:24:54.000000 r3l3453-0.9.0/setup.py
+drwxrwxrwx   0        0        0        0 2021-10-16 14:33:42.515817 r3l3453-0.9.1/
+-rw-rw-rw-   0        0        0    35149 2020-07-05 04:25:19.000000 r3l3453-0.9.1/LICENSE
+-rw-rw-rw-   0        0        0     1571 2021-10-16 14:33:42.515817 r3l3453-0.9.1/PKG-INFO
+-rw-rw-rw-   0        0        0      800 2020-09-19 11:08:43.000000 r3l3453-0.9.1/README.rst
+drwxrwxrwx   0        0        0        0 2021-10-16 14:33:42.500307 r3l3453-0.9.1/r3l3453/
+-rw-rw-rw-   0        0        0     7177 2021-10-16 14:33:41.000000 r3l3453-0.9.1/r3l3453/__init__.py
+-rw-rw-rw-   0        0        0      111 2020-08-14 12:20:15.000000 r3l3453-0.9.1/r3l3453/__main__.py
+drwxrwxrwx   0        0        0        0 2021-10-16 14:33:42.515817 r3l3453-0.9.1/r3l3453.egg-info/
+-rw-rw-rw-   0        0        0     1571 2021-10-16 14:33:42.000000 r3l3453-0.9.1/r3l3453.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      281 2021-10-16 14:33:42.000000 r3l3453-0.9.1/r3l3453.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2021-10-16 14:33:42.000000 r3l3453-0.9.1/r3l3453.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       74 2021-10-16 14:33:42.000000 r3l3453-0.9.1/r3l3453.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0       30 2021-10-16 14:33:42.000000 r3l3453-0.9.1/r3l3453.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        8 2021-10-16 14:33:42.000000 r3l3453-0.9.1/r3l3453.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0        2 2020-07-05 09:29:12.000000 r3l3453-0.9.1/r3l3453.egg-info/zip-safe
+-rw-rw-rw-   0        0        0       42 2021-10-16 14:33:42.515817 r3l3453-0.9.1/setup.cfg
+-rw-rw-rw-   0        0        0     1197 2021-10-16 14:33:41.000000 r3l3453-0.9.1/setup.py
```

### Comparing `r3l3453-0.9.0/PKG-INFO` & `r3l3453-0.9.1/PKG-INFO`

 * *Files 22% similar despite different names*

```diff
@@ -1,38 +1,41 @@
 Metadata-Version: 2.1
 Name: r3l3453
-Version: 0.9.0
+Version: 0.9.1
 Summary: Bump version, tag, commit, release to pypi, bump again, and push.
 Home-page: https://github.com/5j9/r3l3453
 Author: 5j9
 Author-email: 5j9@users.noreply.github.com
 License: GNU General Public License v3 (GPLv3)
-Description: `r3l3453` is a small project that I use for semi-automating release cycle on a few of my projects.
-        
-        In short what it does is as follows:
-        
-        * Bump version(s) to a release version according to git log and `Conventional Commits`_.
-        * Change the title of `Unreleased`_ section in ``CHANGELOG.rst`` to the new version.
-        * Commit changes.
-        * Tag the commit.
-        * Release to PyPI.
-        * Bump the version again to dev0 version for the next release.
-        * Push changes to repository.
-        
-        ``r3l3453.json`` can be used to specify the location of version variables.
-        Refer to the ``r3l3453.json`` of this project to see how it is used.
-        
-        There is a ``--simulate`` cli option which allows one to see what is going to happen.
-        
-        .. _Conventional Commits: https://www.conventionalcommits.org/
-        .. _Unreleased: https://keepachangelog.com/
-        
 Platform: UNKNOWN
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Natural Language :: English
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Topic :: Software Development
 Classifier: Topic :: Software Development :: Build Tools
 Requires-Python: >=3.9
 Description-Content-Type: text/x-rst
+License-File: LICENSE
+
+`r3l3453` is a small project that I use for semi-automating release cycle on a few of my projects.
+
+In short what it does is as follows:
+
+* Bump version(s) to a release version according to git log and `Conventional Commits`_.
+* Change the title of `Unreleased`_ section in ``CHANGELOG.rst`` to the new version.
+* Commit changes.
+* Tag the commit.
+* Release to PyPI.
+* Bump the version again to dev0 version for the next release.
+* Push changes to repository.
+
+``r3l3453.json`` can be used to specify the location of version variables.
+Refer to the ``r3l3453.json`` of this project to see how it is used.
+
+There is a ``--simulate`` cli option which allows one to see what is going to happen.
+
+.. _Conventional Commits: https://www.conventionalcommits.org/
+.. _Unreleased: https://keepachangelog.com/
+
+
```

### Comparing `r3l3453-0.9.0/README.rst` & `r3l3453-0.9.1/README.rst`

 * *Files identical despite different names*

### Comparing `r3l3453-0.9.0/r3l3453/__init__.py` & `r3l3453-0.9.1/r3l3453/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #!/usr/bin/env bash
-__version__ = '0.9.0'
+__version__ = '0.9.1'
 
 from contextlib import contextmanager
 from enum import Enum
 from json import load
 from logging import warning
 from re import IGNORECASE, search
 from subprocess import CalledProcessError, check_call, check_output
@@ -146,15 +146,15 @@
     args = ('git', 'commit', '--all', f'--message=release: v{version}')
     if SIMULATE is True:
         print(' '.join(args))
         return
     check_call(args)
 
 
-def commit_and_tag_version_change(release_version: Version):
+def commit_and_tag(release_version: Version):
     commit(release_version)
     git_tag = ('git', 'tag', '-a', f'v{release_version}', '-m', '')
     if SIMULATE is True:
         print(' '.join(git_tag))
         return
     check_call(git_tag)
 
@@ -211,15 +211,15 @@
 
     assert check_output(('git', 'branch', '--show-current')) == b'master\n'
     assert check_output(('git', 'status', '--porcelain')) == b''
 
     with get_file_versions() as file_versions:
         release_version = update_versions(file_versions, type)
         update_changelog(release_version)
-        commit_and_tag_version_change(release_version)
+        commit_and_tag(release_version)
 
         if upload is True:
             upload_to_pypi()
 
         # prepare next dev0
         new_dev_version = update_versions(file_versions, DEV)
         commit(new_dev_version)
```

### Comparing `r3l3453-0.9.0/r3l3453.egg-info/PKG-INFO` & `r3l3453-0.9.1/r3l3453.egg-info/PKG-INFO`

 * *Files 22% similar despite different names*

```diff
@@ -1,38 +1,41 @@
 Metadata-Version: 2.1
 Name: r3l3453
-Version: 0.9.0
+Version: 0.9.1
 Summary: Bump version, tag, commit, release to pypi, bump again, and push.
 Home-page: https://github.com/5j9/r3l3453
 Author: 5j9
 Author-email: 5j9@users.noreply.github.com
 License: GNU General Public License v3 (GPLv3)
-Description: `r3l3453` is a small project that I use for semi-automating release cycle on a few of my projects.
-        
-        In short what it does is as follows:
-        
-        * Bump version(s) to a release version according to git log and `Conventional Commits`_.
-        * Change the title of `Unreleased`_ section in ``CHANGELOG.rst`` to the new version.
-        * Commit changes.
-        * Tag the commit.
-        * Release to PyPI.
-        * Bump the version again to dev0 version for the next release.
-        * Push changes to repository.
-        
-        ``r3l3453.json`` can be used to specify the location of version variables.
-        Refer to the ``r3l3453.json`` of this project to see how it is used.
-        
-        There is a ``--simulate`` cli option which allows one to see what is going to happen.
-        
-        .. _Conventional Commits: https://www.conventionalcommits.org/
-        .. _Unreleased: https://keepachangelog.com/
-        
 Platform: UNKNOWN
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Natural Language :: English
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Topic :: Software Development
 Classifier: Topic :: Software Development :: Build Tools
 Requires-Python: >=3.9
 Description-Content-Type: text/x-rst
+License-File: LICENSE
+
+`r3l3453` is a small project that I use for semi-automating release cycle on a few of my projects.
+
+In short what it does is as follows:
+
+* Bump version(s) to a release version according to git log and `Conventional Commits`_.
+* Change the title of `Unreleased`_ section in ``CHANGELOG.rst`` to the new version.
+* Commit changes.
+* Tag the commit.
+* Release to PyPI.
+* Bump the version again to dev0 version for the next release.
+* Push changes to repository.
+
+``r3l3453.json`` can be used to specify the location of version variables.
+Refer to the ``r3l3453.json`` of this project to see how it is used.
+
+There is a ``--simulate`` cli option which allows one to see what is going to happen.
+
+.. _Conventional Commits: https://www.conventionalcommits.org/
+.. _Unreleased: https://keepachangelog.com/
+
+
```

### Comparing `r3l3453-0.9.0/setup.py` & `r3l3453-0.9.1/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -5,29 +5,29 @@
 
 with open('README.rst', 'r') as fh:
     long_description = fh.read()
 
 here = abspath(dirname(__file__))
 setup(
     name='r3l3453',
-    version='0.9.0',
+    version='0.9.1',
     author='5j9',
     author_email='5j9@users.noreply.github.com',
     description=(
         'Bump version, tag, commit, release to pypi, bump again, and push.'),
     license='GNU General Public License v3 (GPLv3)',
     long_description=long_description,
     long_description_content_type='text/x-rst',
     url='https://github.com/5j9/r3l3453',
     packages=['r3l3453'],
     entry_points={
         'console_scripts': [
             'r3l3453 = r3l3453.__init__:console_scripts_entry_point']},
     python_requires='>=3.9',
-    install_requires=['parver', 'path', 'typer'],
+    install_requires=['parver', 'path', 'typer', 'wheel', 'twine'],
     classifiers=[
         'Development Status :: 1 - Planning',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
         'Natural Language :: English',
         'Programming Language :: Python :: 3.9',
         'Topic :: Software Development',
```

