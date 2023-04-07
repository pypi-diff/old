# Comparing `tmp/fortitudo_tech-0.9.tar.gz` & `tmp/fortitudo_tech-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "fortitudo_tech-0.9.tar", max compression
+gzip compressed data, was "fortitudo_tech-0.9.1.tar", max compression
```

## Comparing `fortitudo_tech-0.9.tar` & `fortitudo_tech-0.9.1.tar`

### file list

```diff
@@ -1,15 +1,15 @@
--rw-r--r--   0        0        0    35149 2023-02-16 14:26:58.240514 fortitudo_tech-0.9/LICENSE
--rw-r--r--   0        0        0     2700 2023-02-16 14:26:58.240514 fortitudo_tech-0.9/README.rst
--rw-r--r--   0        0        0     1191 2023-02-17 13:29:26.136061 fortitudo_tech-0.9/fortitudo/tech/__init__.py
--rw-r--r--   0        0        0      636 2023-02-16 14:26:58.260514 fortitudo_tech-0.9/fortitudo/tech/data/parameters.csv
--rw-r--r--   0        0        0  2056742 2023-02-16 14:26:58.260514 fortitudo_tech-0.9/fortitudo/tech/data/pnl.csv
--rw-r--r--   0        0        0  3725592 2023-02-16 14:26:58.280514 fortitudo_tech-0.9/fortitudo/tech/data/time_series.csv
--rw-r--r--   0        0        0     3224 2023-02-28 11:29:40.252506 fortitudo_tech-0.9/fortitudo/tech/data.py
--rw-r--r--   0        0        0     3122 2023-02-16 14:26:58.280514 fortitudo_tech-0.9/fortitudo/tech/entropy_pooling.py
--rw-r--r--   0        0        0     7353 2023-02-16 14:26:58.280514 fortitudo_tech-0.9/fortitudo/tech/functions.py
--rw-r--r--   0        0        0    13161 2023-02-16 14:26:58.280514 fortitudo_tech-0.9/fortitudo/tech/optimization.py
--rw-r--r--   0        0        0     2406 2023-02-16 14:26:58.280514 fortitudo_tech-0.9/fortitudo/tech/option_pricing.py
--rw-r--r--   0        0        0     2083 2023-02-16 14:26:58.280514 fortitudo_tech-0.9/fortitudo/tech/simulation.py
--rw-r--r--   0        0        0     1611 2023-02-17 13:50:02.606058 fortitudo_tech-0.9/pyproject.toml
--rw-r--r--   0        0        0     3555 1970-01-01 00:00:00.000000 fortitudo_tech-0.9/setup.py
--rw-r--r--   0        0        0     4283 1970-01-01 00:00:00.000000 fortitudo_tech-0.9/PKG-INFO
+-rw-r--r--   0        0        0    35149 2023-03-21 10:40:42.267200 fortitudo_tech-0.9.1/LICENSE
+-rw-r--r--   0        0        0     3015 2023-04-07 10:53:16.835693 fortitudo_tech-0.9.1/README.rst
+-rw-r--r--   0        0        0     1191 2023-03-21 10:40:42.287200 fortitudo_tech-0.9.1/fortitudo/tech/__init__.py
+-rw-r--r--   0        0        0      636 2023-03-21 10:40:42.287200 fortitudo_tech-0.9.1/fortitudo/tech/data/parameters.csv
+-rw-r--r--   0        0        0  2056742 2023-03-21 10:40:42.297200 fortitudo_tech-0.9.1/fortitudo/tech/data/pnl.csv
+-rw-r--r--   0        0        0  3725592 2023-03-21 10:40:42.307200 fortitudo_tech-0.9.1/fortitudo/tech/data/time_series.csv
+-rw-r--r--   0        0        0     3224 2023-03-21 10:40:42.287200 fortitudo_tech-0.9.1/fortitudo/tech/data.py
+-rw-r--r--   0        0        0     3122 2023-03-21 10:40:42.307200 fortitudo_tech-0.9.1/fortitudo/tech/entropy_pooling.py
+-rw-r--r--   0        0        0     7353 2023-03-21 10:40:42.307200 fortitudo_tech-0.9.1/fortitudo/tech/functions.py
+-rw-r--r--   0        0        0    13161 2023-03-21 10:40:42.307200 fortitudo_tech-0.9.1/fortitudo/tech/optimization.py
+-rw-r--r--   0        0        0     2406 2023-03-21 10:40:42.307200 fortitudo_tech-0.9.1/fortitudo/tech/option_pricing.py
+-rw-r--r--   0        0        0     2083 2023-03-21 10:40:42.307200 fortitudo_tech-0.9.1/fortitudo/tech/simulation.py
+-rw-r--r--   0        0        0     1614 2023-04-07 13:28:09.511256 fortitudo_tech-0.9.1/pyproject.toml
+-rw-r--r--   0        0        0     3875 1970-01-01 00:00:00.000000 fortitudo_tech-0.9.1/setup.py
+-rw-r--r--   0        0        0     4597 1970-01-01 00:00:00.000000 fortitudo_tech-0.9.1/PKG-INFO
```

### Comparing `fortitudo_tech-0.9/LICENSE` & `fortitudo_tech-0.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `fortitudo_tech-0.9/README.rst` & `fortitudo_tech-0.9.1/README.rst`

 * *Files 12% similar despite different names*

```diff
@@ -1,56 +1,62 @@
 .. image:: https://github.com/fortitudo-tech/fortitudo.tech/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/fortitudo-tech/fortitudo.tech/actions/workflows/tests.yml
 
 .. image:: https://codecov.io/gh/fortitudo-tech/fortitudo.tech/branch/main/graph/badge.svg?token=Z16XK92Gkl 
    :target: https://codecov.io/gh/fortitudo-tech/fortitudo.tech
 
-.. image:: https://static.pepy.tech/personalized-badge/fortitudo-tech?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads
-   :target: https://pepy.tech/project/fortitudo-tech
+.. image:: https://mybinder.org/badge_logo.svg
+   :target: https://mybinder.org/v2/gh/fortitudo-tech/fortitudo.tech/main?labpath=examples
 
 Fortitudo Technologies Open Source
 ==================================
 
 This package allows you to freely explore open-source implementations of some
 of our fundamental technologies, e.g., Entropy Pooling and CVaR optimization 
 in Python.
 
 The package is intended for advanced users who are comfortable specifying
 portfolio constraints and Entropy Pooling views using matrices and vectors.
-This gives full flexibility in relation to working with these technologies
-and allows you to build your own high-level interfaces if you wish. Hence,
-input checking is intentionally kept to a minimum.
-
-Fortitudo Technologies is a fintech company that offers novel investment
-technologies as well as quantitative and digitalization consultancy to the
-investment management industry. For more information, please visit our
+This gives full flexibility in relation to working with these technologies.
+Hence, input checking is intentionally kept to a minimum.
+
+Fortitudo Technologies is a fintech offering novel investment technologies
+as well as quantitative and digitalization consultancy to the investment
+management industry. For more information, please visit our
 `website <https://fortitudo.tech>`_.
 
 Installation Instructions
 -------------------------
 
 Installation can be done via pip::
 
    pip install fortitudo.tech
 
 For best performance, we recommend that you install the package in a `conda environment
 <https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html>`_
 and let conda handle the installation of dependencies before installing the
 package using pip. You can do this by following these steps::
 
-   conda create -n fortitudo.tech python scipy pandas -y
+   conda create -n fortitudo.tech python=3.10 scipy pandas matplotlib -y
    conda activate fortitudo.tech
    conda install -c conda-forge cvxopt=1.3 -y
    pip install fortitudo.tech
 
 The examples might require you to install additional packages, e.g., seaborn and
 ipykernel / notebook / jupyterlab if you want to run the notebooks. Using pip to
 install these packages should not cause any dependency issues.
 
+You can also explore the examples in the cloud without any local installations using
+`Binder <https://mybinder.org/v2/gh/fortitudo-tech/fortitudo.tech/main?labpath=examples>`_.
+However, note that Binder servers have very limited ressources and might not support
+some of the optimized routines this package uses. For best performance, you should
+install the package on a machine that supports the `Math Kernel Library <https://en.
+wikipedia.org/wiki/Math_Kernel_Library>`_.
+
 Disclaimer
 ----------
 
 This package is completely separate from our proprietary solutions and therefore
 not representative of neither the quality nor the functionality offered by the Simulation
 Engine and Investment Analysis modules. If you are an institutional investor and want
-to experience how some of these methods can be used in practice for sophisticated
-investment analysis, please request a demo by sending an email to demo@fortitudo.tech.
+to experience how these methods can be used for sophisticated analysis in practice,
+please request a demo by sending an email to demo@fortitudo.tech.
```

### Comparing `fortitudo_tech-0.9/fortitudo/tech/__init__.py` & `fortitudo_tech-0.9.1/fortitudo/tech/__init__.py`

 * *Files identical despite different names*

### Comparing `fortitudo_tech-0.9/fortitudo/tech/data/parameters.csv` & `fortitudo_tech-0.9.1/fortitudo/tech/data/parameters.csv`

 * *Files identical despite different names*

### Comparing `fortitudo_tech-0.9/fortitudo/tech/data/pnl.csv` & `fortitudo_tech-0.9.1/fortitudo/tech/data/pnl.csv`

 * *Files identical despite different names*

### Comparing `fortitudo_tech-0.9/fortitudo/tech/data/time_series.csv` & `fortitudo_tech-0.9.1/fortitudo/tech/data/time_series.csv`

 * *Files identical despite different names*

### Comparing `fortitudo_tech-0.9/fortitudo/tech/data.py` & `fortitudo_tech-0.9.1/fortitudo/tech/data.py`

 * *Files identical despite different names*

### Comparing `fortitudo_tech-0.9/fortitudo/tech/entropy_pooling.py` & `fortitudo_tech-0.9.1/fortitudo/tech/entropy_pooling.py`

 * *Files identical despite different names*

### Comparing `fortitudo_tech-0.9/fortitudo/tech/functions.py` & `fortitudo_tech-0.9.1/fortitudo/tech/functions.py`

 * *Files identical despite different names*

### Comparing `fortitudo_tech-0.9/fortitudo/tech/optimization.py` & `fortitudo_tech-0.9.1/fortitudo/tech/optimization.py`

 * *Files identical despite different names*

### Comparing `fortitudo_tech-0.9/fortitudo/tech/option_pricing.py` & `fortitudo_tech-0.9.1/fortitudo/tech/option_pricing.py`

 * *Files identical despite different names*

### Comparing `fortitudo_tech-0.9/fortitudo/tech/simulation.py` & `fortitudo_tech-0.9.1/fortitudo/tech/simulation.py`

 * *Files identical despite different names*

### Comparing `fortitudo_tech-0.9/pyproject.toml` & `fortitudo_tech-0.9.1/pyproject.toml`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "fortitudo.tech"
-version = "0.9"
+version = "0.9.1"
 description = "Investment and risk technologies maintained by Fortitudo Technologies."
 authors = ["Fortitudo Technologies <software@fortitudo.tech>"]
 license = "GPL-3.0-or-later"
 readme = "README.rst"
 homepage = "https://fortitudo.tech"
 repository = "https://github.com/fortitudo-tech/fortitudo.tech"
 documentation = "https://os.fortitudo.tech"
@@ -29,15 +29,15 @@
 
 [tool.poetry.urls]
 "Issues" = "https://github.com/fortitudo-tech/fortitudo.tech/issues"
 
 [tool.poetry.dependencies]
 python = "^3.8, <3.11"
 scipy = "^1.6"
-cvxopt = "^1.2"
+cvxopt = "1.3.0"
 pandas = "^1.3.4"
 numpy = "^1.22"
 matplotlib = "^3.4"
 
 [tool.poetry.dev-dependencies]
 pytest-cov = "^3.0.0"
 sphinx-rtd-theme = "^1.0.0"
```

### Comparing `fortitudo_tech-0.9/setup.py` & `fortitudo_tech-0.9.1/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -4,25 +4,25 @@
 packages = \
 ['tech']
 
 package_data = \
 {'': ['*'], 'tech': ['data/*']}
 
 install_requires = \
-['cvxopt>=1.2,<2.0',
+['cvxopt==1.3.0',
  'matplotlib>=3.4,<4.0',
  'numpy>=1.22,<2.0',
  'pandas>=1.3.4,<2.0.0',
  'scipy>=1.6,<2.0']
 
 setup_kwargs = {
     'name': 'fortitudo-tech',
-    'version': '0.9',
+    'version': '0.9.1',
     'description': 'Investment and risk technologies maintained by Fortitudo Technologies.',
-    'long_description': '.. image:: https://github.com/fortitudo-tech/fortitudo.tech/actions/workflows/tests.yml/badge.svg\n   :target: https://github.com/fortitudo-tech/fortitudo.tech/actions/workflows/tests.yml\n\n.. image:: https://codecov.io/gh/fortitudo-tech/fortitudo.tech/branch/main/graph/badge.svg?token=Z16XK92Gkl \n   :target: https://codecov.io/gh/fortitudo-tech/fortitudo.tech\n\n.. image:: https://static.pepy.tech/personalized-badge/fortitudo-tech?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads\n   :target: https://pepy.tech/project/fortitudo-tech\n\nFortitudo Technologies Open Source\n==================================\n\nThis package allows you to freely explore open-source implementations of some\nof our fundamental technologies, e.g., Entropy Pooling and CVaR optimization \nin Python.\n\nThe package is intended for advanced users who are comfortable specifying\nportfolio constraints and Entropy Pooling views using matrices and vectors.\nThis gives full flexibility in relation to working with these technologies\nand allows you to build your own high-level interfaces if you wish. Hence,\ninput checking is intentionally kept to a minimum.\n\nFortitudo Technologies is a fintech company that offers novel investment\ntechnologies as well as quantitative and digitalization consultancy to the\ninvestment management industry. For more information, please visit our\n`website <https://fortitudo.tech>`_.\n\nInstallation Instructions\n-------------------------\n\nInstallation can be done via pip::\n\n   pip install fortitudo.tech\n\nFor best performance, we recommend that you install the package in a `conda environment\n<https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html>`_\nand let conda handle the installation of dependencies before installing the\npackage using pip. You can do this by following these steps::\n\n   conda create -n fortitudo.tech python scipy pandas -y\n   conda activate fortitudo.tech\n   conda install -c conda-forge cvxopt=1.3 -y\n   pip install fortitudo.tech\n\nThe examples might require you to install additional packages, e.g., seaborn and\nipykernel / notebook / jupyterlab if you want to run the notebooks. Using pip to\ninstall these packages should not cause any dependency issues.\n\nDisclaimer\n----------\n\nThis package is completely separate from our proprietary solutions and therefore\nnot representative of neither the quality nor the functionality offered by the Simulation\nEngine and Investment Analysis modules. If you are an institutional investor and want\nto experience how some of these methods can be used in practice for sophisticated\ninvestment analysis, please request a demo by sending an email to demo@fortitudo.tech.\n',
+    'long_description': '.. image:: https://github.com/fortitudo-tech/fortitudo.tech/actions/workflows/tests.yml/badge.svg\n   :target: https://github.com/fortitudo-tech/fortitudo.tech/actions/workflows/tests.yml\n\n.. image:: https://codecov.io/gh/fortitudo-tech/fortitudo.tech/branch/main/graph/badge.svg?token=Z16XK92Gkl \n   :target: https://codecov.io/gh/fortitudo-tech/fortitudo.tech\n\n.. image:: https://mybinder.org/badge_logo.svg\n   :target: https://mybinder.org/v2/gh/fortitudo-tech/fortitudo.tech/main?labpath=examples\n\nFortitudo Technologies Open Source\n==================================\n\nThis package allows you to freely explore open-source implementations of some\nof our fundamental technologies, e.g., Entropy Pooling and CVaR optimization \nin Python.\n\nThe package is intended for advanced users who are comfortable specifying\nportfolio constraints and Entropy Pooling views using matrices and vectors.\nThis gives full flexibility in relation to working with these technologies.\nHence, input checking is intentionally kept to a minimum.\n\nFortitudo Technologies is a fintech offering novel investment technologies\nas well as quantitative and digitalization consultancy to the investment\nmanagement industry. For more information, please visit our\n`website <https://fortitudo.tech>`_.\n\nInstallation Instructions\n-------------------------\n\nInstallation can be done via pip::\n\n   pip install fortitudo.tech\n\nFor best performance, we recommend that you install the package in a `conda environment\n<https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html>`_\nand let conda handle the installation of dependencies before installing the\npackage using pip. You can do this by following these steps::\n\n   conda create -n fortitudo.tech python=3.10 scipy pandas matplotlib -y\n   conda activate fortitudo.tech\n   conda install -c conda-forge cvxopt=1.3 -y\n   pip install fortitudo.tech\n\nThe examples might require you to install additional packages, e.g., seaborn and\nipykernel / notebook / jupyterlab if you want to run the notebooks. Using pip to\ninstall these packages should not cause any dependency issues.\n\nYou can also explore the examples in the cloud without any local installations using\n`Binder <https://mybinder.org/v2/gh/fortitudo-tech/fortitudo.tech/main?labpath=examples>`_.\nHowever, note that Binder servers have very limited ressources and might not support\nsome of the optimized routines this package uses. For best performance, you should\ninstall the package on a machine that supports the `Math Kernel Library <https://en.\nwikipedia.org/wiki/Math_Kernel_Library>`_.\n\nDisclaimer\n----------\n\nThis package is completely separate from our proprietary solutions and therefore\nnot representative of neither the quality nor the functionality offered by the Simulation\nEngine and Investment Analysis modules. If you are an institutional investor and want\nto experience how these methods can be used for sophisticated analysis in practice,\nplease request a demo by sending an email to demo@fortitudo.tech.\n',
     'author': 'Fortitudo Technologies',
     'author_email': 'software@fortitudo.tech',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://fortitudo.tech',
     'packages': packages,
     'package_data': package_data,
```

### Comparing `fortitudo_tech-0.9/PKG-INFO` & `fortitudo_tech-0.9.1/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fortitudo-tech
-Version: 0.9
+Version: 0.9.1
 Summary: Investment and risk technologies maintained by Fortitudo Technologies.
 Home-page: https://fortitudo.tech
 License: GPL-3.0-or-later
 Keywords: CVaR,Efficient Frontier,Entropy Pooling,Mathematical Finance,Portfolio Optimization
 Author: Fortitudo Technologies
 Author-email: software@fortitudo.tech
 Requires-Python: >=3.8,<3.11
@@ -18,15 +18,15 @@
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Topic :: Office/Business :: Financial
 Classifier: Topic :: Office/Business :: Financial :: Investment
 Classifier: Topic :: Scientific/Engineering :: Mathematics
-Requires-Dist: cvxopt (>=1.2,<2.0)
+Requires-Dist: cvxopt (==1.3.0)
 Requires-Dist: matplotlib (>=3.4,<4.0)
 Requires-Dist: numpy (>=1.22,<2.0)
 Requires-Dist: pandas (>=1.3.4,<2.0.0)
 Requires-Dist: scipy (>=1.6,<2.0)
 Project-URL: Documentation, https://os.fortitudo.tech
 Project-URL: Issues, https://github.com/fortitudo-tech/fortitudo.tech/issues
 Project-URL: Repository, https://github.com/fortitudo-tech/fortitudo.tech
@@ -34,58 +34,64 @@
 
 .. image:: https://github.com/fortitudo-tech/fortitudo.tech/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/fortitudo-tech/fortitudo.tech/actions/workflows/tests.yml
 
 .. image:: https://codecov.io/gh/fortitudo-tech/fortitudo.tech/branch/main/graph/badge.svg?token=Z16XK92Gkl 
    :target: https://codecov.io/gh/fortitudo-tech/fortitudo.tech
 
-.. image:: https://static.pepy.tech/personalized-badge/fortitudo-tech?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads
-   :target: https://pepy.tech/project/fortitudo-tech
+.. image:: https://mybinder.org/badge_logo.svg
+   :target: https://mybinder.org/v2/gh/fortitudo-tech/fortitudo.tech/main?labpath=examples
 
 Fortitudo Technologies Open Source
 ==================================
 
 This package allows you to freely explore open-source implementations of some
 of our fundamental technologies, e.g., Entropy Pooling and CVaR optimization 
 in Python.
 
 The package is intended for advanced users who are comfortable specifying
 portfolio constraints and Entropy Pooling views using matrices and vectors.
-This gives full flexibility in relation to working with these technologies
-and allows you to build your own high-level interfaces if you wish. Hence,
-input checking is intentionally kept to a minimum.
-
-Fortitudo Technologies is a fintech company that offers novel investment
-technologies as well as quantitative and digitalization consultancy to the
-investment management industry. For more information, please visit our
+This gives full flexibility in relation to working with these technologies.
+Hence, input checking is intentionally kept to a minimum.
+
+Fortitudo Technologies is a fintech offering novel investment technologies
+as well as quantitative and digitalization consultancy to the investment
+management industry. For more information, please visit our
 `website <https://fortitudo.tech>`_.
 
 Installation Instructions
 -------------------------
 
 Installation can be done via pip::
 
    pip install fortitudo.tech
 
 For best performance, we recommend that you install the package in a `conda environment
 <https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html>`_
 and let conda handle the installation of dependencies before installing the
 package using pip. You can do this by following these steps::
 
-   conda create -n fortitudo.tech python scipy pandas -y
+   conda create -n fortitudo.tech python=3.10 scipy pandas matplotlib -y
    conda activate fortitudo.tech
    conda install -c conda-forge cvxopt=1.3 -y
    pip install fortitudo.tech
 
 The examples might require you to install additional packages, e.g., seaborn and
 ipykernel / notebook / jupyterlab if you want to run the notebooks. Using pip to
 install these packages should not cause any dependency issues.
 
+You can also explore the examples in the cloud without any local installations using
+`Binder <https://mybinder.org/v2/gh/fortitudo-tech/fortitudo.tech/main?labpath=examples>`_.
+However, note that Binder servers have very limited ressources and might not support
+some of the optimized routines this package uses. For best performance, you should
+install the package on a machine that supports the `Math Kernel Library <https://en.
+wikipedia.org/wiki/Math_Kernel_Library>`_.
+
 Disclaimer
 ----------
 
 This package is completely separate from our proprietary solutions and therefore
 not representative of neither the quality nor the functionality offered by the Simulation
 Engine and Investment Analysis modules. If you are an institutional investor and want
-to experience how some of these methods can be used in practice for sophisticated
-investment analysis, please request a demo by sending an email to demo@fortitudo.tech.
+to experience how these methods can be used for sophisticated analysis in practice,
+please request a demo by sending an email to demo@fortitudo.tech.
```

