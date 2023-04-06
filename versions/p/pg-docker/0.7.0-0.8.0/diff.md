# Comparing `tmp/pg_docker-0.7.0.tar.gz` & `tmp/pg_docker-0.8.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pg_docker-0.7.0.tar", max compression
+gzip compressed data, was "pg_docker-0.8.0.tar", max compression
```

## Comparing `pg_docker-0.7.0.tar` & `pg_docker-0.8.0.tar`

### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0     2286 2022-12-19 20:16:34.229525 pg_docker-0.7.0/README.md
--rw-r--r--   0        0        0       88 2022-12-15 21:23:14.996919 pg_docker-0.7.0/pg_docker/__init__.py
--rw-r--r--   0        0        0     8213 2023-04-06 14:56:37.634490 pg_docker-0.7.0/pg_docker/_core.py
--rw-r--r--   0        0        0     1169 2022-12-15 22:40:13.976549 pg_docker-0.7.0/pg_docker/_plugin.py
--rw-r--r--   0        0        0        0 2022-12-19 18:30:52.443272 pg_docker-0.7.0/pg_docker/py.typed
--rw-r--r--   0        0        0      571 2023-04-06 14:58:26.063253 pg_docker-0.7.0/pyproject.toml
--rw-r--r--   0        0        0     3050 1970-01-01 00:00:00.000000 pg_docker-0.7.0/setup.py
--rw-r--r--   0        0        0     2740 1970-01-01 00:00:00.000000 pg_docker-0.7.0/PKG-INFO
+-rw-r--r--   0        0        0     2286 2022-12-19 20:16:34.229525 pg_docker-0.8.0/README.md
+-rw-r--r--   0        0        0       88 2022-12-15 21:23:14.996919 pg_docker-0.8.0/pg_docker/__init__.py
+-rw-r--r--   0        0        0     8213 2023-04-06 14:56:37.634490 pg_docker-0.8.0/pg_docker/_core.py
+-rw-r--r--   0        0        0     1169 2022-12-15 22:40:13.976549 pg_docker-0.8.0/pg_docker/_plugin.py
+-rw-r--r--   0        0        0        0 2022-12-19 18:30:52.443272 pg_docker-0.8.0/pg_docker/py.typed
+-rw-r--r--   0        0        0      569 2023-04-06 15:01:40.631392 pg_docker-0.8.0/pyproject.toml
+-rw-r--r--   0        0        0     3046 1970-01-01 00:00:00.000000 pg_docker-0.8.0/setup.py
+-rw-r--r--   0        0        0     2736 1970-01-01 00:00:00.000000 pg_docker-0.8.0/PKG-INFO
```

### Comparing `pg_docker-0.7.0/README.md` & `pg_docker-0.8.0/README.md`

 * *Files identical despite different names*

### Comparing `pg_docker-0.7.0/pg_docker/_core.py` & `pg_docker-0.8.0/pg_docker/_core.py`

 * *Files identical despite different names*

### Comparing `pg_docker-0.7.0/pg_docker/_plugin.py` & `pg_docker-0.8.0/pg_docker/_plugin.py`

 * *Files identical despite different names*

### Comparing `pg_docker-0.7.0/pyproject.toml` & `pg_docker-0.8.0/pyproject.toml`

 * *Files 20% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 [tool.poetry]
 name = "pg-docker"
-version = "0.7.0"
+version = "0.8.0"
 description = ""
 authors = ["Your Name <you@example.com>"]
 readme = "README.md"
 packages = [{include = "pg_docker"}]
 classifiers = [
     "Framework :: Pytest"
 ]
 
 
 [tool.poetry.dependencies]
 python = "^3.9"
-psycopg2 = "^2.9.5"
+psycopg2 = "^2.9"
 
 
 [tool.poetry.group.dev.dependencies]
 pytest = "^7.2.0"
 black = "^22.10.0"
 isort = "^5.10.1"
 mypy = "^0.991"
```

### Comparing `pg_docker-0.7.0/setup.py` & `pg_docker-0.8.0/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,22 +4,22 @@
 packages = \
 ['pg_docker']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['psycopg2>=2.9.5,<3.0.0']
+['psycopg2>=2.9,<3.0']
 
 entry_points = \
 {'pytest11': ['pg_docker = pg_docker._plugin']}
 
 setup_kwargs = {
     'name': 'pg-docker',
-    'version': '0.7.0',
+    'version': '0.8.0',
     'description': '',
     'long_description': '# PG Docker\n\nA python package to provide containerized postgres databases in python\n\n**Why would you need this?**\n\nIf you are using postgres and want to write tests that run against a real database, then this will make your life easier.\n\n## Installation\n\nInstall via pip:\n```\npip install pg-docker\n```\n\nYou will also need to have [docker](https://www.docker.com/).\n\n## Usage\n\nNote: *This package is mainly built with pytest in mind, but you can use the context managers documented below with other testing frameworks as well.*\n\n### Example\n\nWith pytest:\n```py\nimport psycopg2\n\n\npytest_plugins = ["pg_docker"]\n\n\ndef test_using_a_database(pg_database):\n    db_connection = psycopg2.connect(**pg_database.connection_kwargs())\n    cursor = db_connection.cursor()\n    cursor.execute("SELECT \'hello world!\'")\n\n    assert cursor.fetchone() == ("hello world!",)\n```\n\n### Usage with pytest\n\nYou first need to enable the plugin. To do this add a `conftest.py` to the root directory of your tests and add:\n```py\npytest_plugins = ["pg_docker"]\n```\nYou can find more details on how to activate plugins in the [pytest docs](https://docs.pytest.org/en/latest/how-to/plugins.html#requiring-loading-plugins-in-a-test-module-or-conftest-file)\n\nThe plugin The following fixtures:\n\n - `pg_database`: `DatabaseParams` for a clean database.\n - `pg_database_pool`: A `DatabasePool` instance. Use this if you need more than one database in your tests at a time.\n\n\n### Configuring Database Migrations\n\nUse the below template in your `conftest.py` to configure how your databases are set up. \n```py\ndef setup_db(pg_params):\n    """Add any setup logic for your database in here."""\n    pass\n\n@pytest.fixture(scope="session")\ndef pg_setup_db():\n    return setup_db\n```\nNote: *You might be inclined to edit the above code to nest the setup_db function inside of the fixture function. This will not work, because the fixture result needs to be [pickleable](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled)!*\n\n\n### Advanced Usage (and other testing frameworks)\n\nFor other use cases you can use the `database_pool` context manager:\n```py\nwith database_pool() as db_pool:\n    with db_pool.database as db_params:\n        connection = psycopg2.connect(**db_params.connection_kwargs())\n```\n',
     'author': 'Your Name',
     'author_email': 'you@example.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `pg_docker-0.7.0/PKG-INFO` & `pg_docker-0.8.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,20 +1,20 @@
 Metadata-Version: 2.1
 Name: pg-docker
-Version: 0.7.0
+Version: 0.8.0
 Summary: 
 Author: Your Name
 Author-email: you@example.com
 Requires-Python: >=3.9,<4.0
 Classifier: Framework :: Pytest
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
-Requires-Dist: psycopg2 (>=2.9.5,<3.0.0)
+Requires-Dist: psycopg2 (>=2.9,<3.0)
 Description-Content-Type: text/markdown
 
 # PG Docker
 
 A python package to provide containerized postgres databases in python
 
 **Why would you need this?**
```

