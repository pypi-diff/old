# Comparing `tmp/dvc-ssh-2.21.0.tar.gz` & `tmp/dvc-ssh-2.22.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dvc-ssh-2.21.0.tar", last modified: Sun Jan 22 23:13:52 2023, max compression
+gzip compressed data, was "dvc-ssh-2.22.0.tar", last modified: Thu Apr  6 09:28:29 2023, max compression
```

## Comparing `dvc-ssh-2.21.0.tar` & `dvc-ssh-2.22.0.tar`

### file list

```diff
@@ -1,35 +1,35 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-01-22 23:13:52.871180 dvc-ssh-2.21.0/
--rw-r--r--   0 runner    (1001) docker     (122)      348 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/.cruft.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-01-22 23:13:52.863180 dvc-ssh-2.21.0/.github/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-01-22 23:13:52.867180 dvc-ssh-2.21.0/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (122)      609 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/.github/workflows/release.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     1288 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/.github/workflows/tests.yaml
--rw-r--r--   0 runner    (1001) docker     (122)      632 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/.github/workflows/update-template.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     1829 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/.gitignore
--rw-r--r--   0 runner    (1001) docker     (122)     1298 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (122)    11357 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (122)      758 2023-01-22 23:13:52.871180 dvc-ssh-2.21.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)       28 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-01-22 23:13:52.867180 dvc-ssh-2.21.0/dvc_ssh/
--rw-r--r--   0 runner    (1001) docker     (122)     4423 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/dvc_ssh/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)      162 2023-01-22 23:13:52.000000 dvc-ssh-2.21.0/dvc_ssh/_dvc_ssh_version.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-01-22 23:13:52.871180 dvc-ssh-2.21.0/dvc_ssh/tests/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/dvc_ssh/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     1586 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/dvc_ssh/tests/cloud.py
--rw-r--r--   0 runner    (1001) docker     (122)      170 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/dvc_ssh/tests/conftest.py
--rw-r--r--   0 runner    (1001) docker     (122)      236 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/dvc_ssh/tests/docker-compose.yml
--rw-r--r--   0 runner    (1001) docker     (122)     1731 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/dvc_ssh/tests/fixtures.py
--rw-r--r--   0 runner    (1001) docker     (122)     1388 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/dvc_ssh/tests/test_dvc.py
--rw-r--r--   0 runner    (1001) docker     (122)     5215 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/dvc_ssh/tests/test_fs.py
--rw-r--r--   0 runner    (1001) docker     (122)     1679 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/dvc_ssh/tests/user.key
--rw-r--r--   0 runner    (1001) docker     (122)      394 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/dvc_ssh/tests/user.key.pub
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-01-22 23:13:52.867180 dvc-ssh-2.21.0/dvc_ssh.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)      758 2023-01-22 23:13:52.000000 dvc-ssh-2.21.0/dvc_ssh.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)      665 2023-01-22 23:13:52.000000 dvc-ssh-2.21.0/dvc_ssh.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-01-22 23:13:52.000000 dvc-ssh-2.21.0/dvc_ssh.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-01-22 23:13:52.000000 dvc-ssh-2.21.0/dvc_ssh.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (122)      512 2023-01-22 23:13:52.000000 dvc-ssh-2.21.0/dvc_ssh.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)        8 2023-01-22 23:13:52.000000 dvc-ssh-2.21.0/dvc_ssh.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (122)     2069 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (122)     1568 2023-01-22 23:13:52.871180 dvc-ssh-2.21.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (122)       38 2023-01-22 23:13:31.000000 dvc-ssh-2.21.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 09:28:29.152369 dvc-ssh-2.22.0/
+-rw-r--r--   0 runner    (1001) docker     (122)      348 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/.cruft.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 09:28:29.144369 dvc-ssh-2.22.0/.github/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 09:28:29.148369 dvc-ssh-2.22.0/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (122)      609 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/.github/workflows/release.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     1288 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/.github/workflows/tests.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)      632 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/.github/workflows/update-template.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     1829 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (122)     1299 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/.pre-commit-config.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)    11357 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)      758 2023-04-06 09:28:29.152369 dvc-ssh-2.22.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)       28 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 09:28:29.148369 dvc-ssh-2.22.0/dvc_ssh/
+-rw-r--r--   0 runner    (1001) docker     (122)     4389 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/dvc_ssh/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      162 2023-04-06 09:28:29.000000 dvc-ssh-2.22.0/dvc_ssh/_dvc_ssh_version.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 09:28:29.152369 dvc-ssh-2.22.0/dvc_ssh/tests/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/dvc_ssh/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1586 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/dvc_ssh/tests/cloud.py
+-rw-r--r--   0 runner    (1001) docker     (122)      170 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/dvc_ssh/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (122)      236 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/dvc_ssh/tests/docker-compose.yml
+-rw-r--r--   0 runner    (1001) docker     (122)     1674 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/dvc_ssh/tests/fixtures.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1388 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/dvc_ssh/tests/test_dvc.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5215 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/dvc_ssh/tests/test_fs.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1679 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/dvc_ssh/tests/user.key
+-rw-r--r--   0 runner    (1001) docker     (122)      394 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/dvc_ssh/tests/user.key.pub
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 09:28:29.148369 dvc-ssh-2.22.0/dvc_ssh.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)      758 2023-04-06 09:28:29.000000 dvc-ssh-2.22.0/dvc_ssh.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)      665 2023-04-06 09:28:29.000000 dvc-ssh-2.22.0/dvc_ssh.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 09:28:29.000000 dvc-ssh-2.22.0/dvc_ssh.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 09:28:29.000000 dvc-ssh-2.22.0/dvc_ssh.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (122)      510 2023-04-06 09:28:29.000000 dvc-ssh-2.22.0/dvc_ssh.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        8 2023-04-06 09:28:29.000000 dvc-ssh-2.22.0/dvc_ssh.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)     2069 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (122)     1566 2023-04-06 09:28:29.152369 dvc-ssh-2.22.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-06 09:28:02.000000 dvc-ssh-2.22.0/setup.py
```

### Comparing `dvc-ssh-2.21.0/.github/workflows/release.yaml` & `dvc-ssh-2.22.0/.github/workflows/release.yaml`

 * *Files identical despite different names*

### Comparing `dvc-ssh-2.21.0/.github/workflows/tests.yaml` & `dvc-ssh-2.22.0/.github/workflows/tests.yaml`

 * *Files identical despite different names*

### Comparing `dvc-ssh-2.21.0/.github/workflows/update-template.yaml` & `dvc-ssh-2.22.0/.github/workflows/update-template.yaml`

 * *Files identical despite different names*

### Comparing `dvc-ssh-2.21.0/.gitignore` & `dvc-ssh-2.22.0/.gitignore`

 * *Files identical despite different names*

### Comparing `dvc-ssh-2.21.0/.pre-commit-config.yaml` & `dvc-ssh-2.22.0/.pre-commit-config.yaml`

 * *Files 2% similar despite different names*

```diff
@@ -19,15 +19,15 @@
           - ba,datas,fo,uptodate
     repo: https://github.com/codespell-project/codespell
     rev: v2.1.0
   - hooks:
       - id: isort
         language_version: python3
     repo: https://github.com/timothycrosley/isort
-    rev: 5.9.3
+    rev: 5.12.0
   - hooks:
       - id: flake8
         language_version: python3
         additional_dependencies:
           - flake8-bugbear
           - flake8-comprehensions
           - flake8-debugger
```

### Comparing `dvc-ssh-2.21.0/LICENSE` & `dvc-ssh-2.22.0/LICENSE`

 * *Files identical despite different names*

### Comparing `dvc-ssh-2.21.0/PKG-INFO` & `dvc-ssh-2.22.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dvc-ssh
-Version: 2.21.0
+Version: 2.22.0
 Summary: ssh plugin for dvc
 Home-page: http://dvc.org
 Download-URL: https://github.com/iterative/dvc-ssh
 License: Apache License 2.0
 Project-URL: Documentation, https://dvc.org/doc
 Project-URL: Source, https://github.com/iterative/dvc-ssh
 Keywords: dvc,ssh
```

### Comparing `dvc-ssh-2.21.0/dvc_ssh/tests/cloud.py` & `dvc-ssh-2.22.0/dvc_ssh/tests/cloud.py`

 * *Files identical despite different names*

### Comparing `dvc-ssh-2.21.0/dvc_ssh/tests/fixtures.py` & `dvc-ssh-2.22.0/dvc_ssh/tests/fixtures.py`

 * *Files 10% similar despite different names*

```diff
@@ -9,17 +9,15 @@
 
 @pytest.fixture(scope="session")
 def docker_compose_file(pytestconfig):  # pylint: disable=unused-argument
     return os.path.join(os.path.dirname(__file__), "docker-compose.yml")
 
 
 @pytest.fixture(scope="session")
-def ssh_server(  # pylint: disable=unused-argument
-    docker_compose, docker_services
-):
+def ssh_server(docker_services):
     import asyncssh
     from sshfs import SSHFileSystem
 
     conn_info = {
         "host": "127.0.0.1",
         "port": docker_services.port_for("openssh-server", 2222),
     }
```

### Comparing `dvc-ssh-2.21.0/dvc_ssh/tests/test_dvc.py` & `dvc-ssh-2.22.0/dvc_ssh/tests/test_dvc.py`

 * *Files identical despite different names*

### Comparing `dvc-ssh-2.21.0/dvc_ssh/tests/test_fs.py` & `dvc-ssh-2.22.0/dvc_ssh/tests/test_fs.py`

 * *Files identical despite different names*

### Comparing `dvc-ssh-2.21.0/dvc_ssh/tests/user.key` & `dvc-ssh-2.22.0/dvc_ssh/tests/user.key`

 * *Files identical despite different names*

### Comparing `dvc-ssh-2.21.0/dvc_ssh.egg-info/PKG-INFO` & `dvc-ssh-2.22.0/dvc_ssh.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dvc-ssh
-Version: 2.21.0
+Version: 2.22.0
 Summary: ssh plugin for dvc
 Home-page: http://dvc.org
 Download-URL: https://github.com/iterative/dvc-ssh
 License: Apache License 2.0
 Project-URL: Documentation, https://dvc.org/doc
 Project-URL: Source, https://github.com/iterative/dvc-ssh
 Keywords: dvc,ssh
```

### Comparing `dvc-ssh-2.21.0/dvc_ssh.egg-info/SOURCES.txt` & `dvc-ssh-2.22.0/dvc_ssh.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `dvc-ssh-2.21.0/pyproject.toml` & `dvc-ssh-2.22.0/pyproject.toml`

 * *Files identical despite different names*

### Comparing `dvc-ssh-2.21.0/setup.cfg` & `dvc-ssh-2.22.0/setup.cfg`

 * *Files 8% similar despite different names*

```diff
@@ -26,28 +26,28 @@
 	setuptools_scm[toml]>=6.3.1
 python_requires = >=3.8
 zip_safe = False
 packages = find:
 include_package_data = True
 install_requires = 
 	dvc
-	sshfs[bcrypt]>=2023.1.0
+	sshfs[bcrypt]>=2023.4.0
 
 [options.extras_require]
 gssapi = 
 	sshfs[gssapi]>=2021.11.2
 tests = 
 	wheel==0.37.0
 	dvc[testing]
 	pytest==6.2.5
 	pytest-cov==3.0.0
 	pytest-xdist==2.4.0
 	pytest-mock==3.6.1
 	pytest-lazy-fixture==0.6.3
-	pytest-docker==0.10.3
+	pytest-docker>=1,<2
 	flaky==3.7.0
 	mock==4.0.3
 	wget==3.2
 	filelock==3.3.2
 	xmltodict==0.12.0
 	Pygments==2.10.0
 	collective.checkdocs==0.2
```

