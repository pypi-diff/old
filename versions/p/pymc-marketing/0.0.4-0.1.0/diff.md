# Comparing `tmp/pymc-marketing-0.0.4.tar.gz` & `tmp/pymc-marketing-0.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pymc-marketing-0.0.4.tar", last modified: Tue Feb 28 12:12:12 2023, max compression
+gzip compressed data, was "pymc-marketing-0.1.0.tar", last modified: Thu Apr  6 12:34:13 2023, max compression
```

## Comparing `pymc-marketing-0.0.4.tar` & `pymc-marketing-0.1.0.tar`

### file list

```diff
@@ -1,35 +1,35 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 12:12:12.132322 pymc-marketing-0.0.4/
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)    19070 2023-02-28 12:12:12.132322 pymc-marketing-0.0.4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5725 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 12:12:12.128322 pymc-marketing-0.0.4/pymc_marketing/
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 12:12:12.128322 pymc-marketing-0.0.4/pymc_marketing/clv/
--rw-r--r--   0 runner    (1001) docker     (123)      555 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/clv/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14430 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/clv/distributions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 12:12:12.128322 pymc-marketing-0.0.4/pymc_marketing/clv/models/
--rw-r--r--   0 runner    (1001) docker     (123)      448 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/clv/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3752 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/clv/models/basic.py
--rw-r--r--   0 runner    (1001) docker     (123)    12574 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/clv/models/beta_geo.py
--rw-r--r--   0 runner    (1001) docker     (123)    16215 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/clv/models/gamma_gamma.py
--rw-r--r--   0 runner    (1001) docker     (123)     7266 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/clv/models/shifted_beta_geo.py
--rw-r--r--   0 runner    (1001) docker     (123)     4500 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/clv/plotting.py
--rw-r--r--   0 runner    (1001) docker     (123)    12842 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/clv/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 12:12:12.132322 pymc-marketing-0.0.4/pymc_marketing/mmm/
--rw-r--r--   0 runner    (1001) docker     (123)      334 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/mmm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14726 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/mmm/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     5044 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/mmm/delayed_saturated_mmm.py
--rw-r--r--   0 runner    (1001) docker     (123)     2081 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/mmm/preprocessing.py
--rw-r--r--   0 runner    (1001) docker     (123)     4738 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/mmm/transformers.py
--rw-r--r--   0 runner    (1001) docker     (123)      948 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/mmm/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2750 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/mmm/validating.py
--rw-r--r--   0 runner    (1001) docker     (123)      266 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/version.py
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pymc_marketing/version.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-28 12:12:12.128322 pymc-marketing-0.0.4/pymc_marketing.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    19070 2023-02-28 12:12:12.000000 pymc-marketing-0.0.4/pymc_marketing.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      859 2023-02-28 12:12:12.000000 pymc-marketing-0.0.4/pymc_marketing.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-28 12:12:12.000000 pymc-marketing-0.0.4/pymc_marketing.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      414 2023-02-28 12:12:12.000000 pymc-marketing-0.0.4/pymc_marketing.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-02-28 12:12:12.000000 pymc-marketing-0.0.4/pymc_marketing.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1588 2023-02-28 12:12:02.000000 pymc-marketing-0.0.4/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-28 12:12:12.132322 pymc-marketing-0.0.4/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:34:13.707226 pymc-marketing-0.1.0/
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)    20911 2023-04-06 12:34:13.707226 pymc-marketing-0.1.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     7566 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:34:13.707226 pymc-marketing-0.1.0/pymc_marketing/
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:34:13.707226 pymc-marketing-0.1.0/pymc_marketing/clv/
+-rw-r--r--   0 runner    (1001) docker     (123)      555 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/clv/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14430 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/clv/distributions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:34:13.707226 pymc-marketing-0.1.0/pymc_marketing/clv/models/
+-rw-r--r--   0 runner    (1001) docker     (123)      448 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/clv/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3728 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/clv/models/basic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12544 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/clv/models/beta_geo.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16215 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/clv/models/gamma_gamma.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7266 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/clv/models/shifted_beta_geo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4500 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/clv/plotting.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12842 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/clv/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:34:13.707226 pymc-marketing-0.1.0/pymc_marketing/mmm/
+-rw-r--r--   0 runner    (1001) docker     (123)      334 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/mmm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14741 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/mmm/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4286 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/mmm/delayed_saturated_mmm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2031 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/mmm/preprocessing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6050 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/mmm/transformers.py
+-rw-r--r--   0 runner    (1001) docker     (123)      948 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/mmm/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2708 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/mmm/validating.py
+-rw-r--r--   0 runner    (1001) docker     (123)      266 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/version.py
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pymc_marketing/version.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:34:13.707226 pymc-marketing-0.1.0/pymc_marketing.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    20911 2023-04-06 12:34:13.000000 pymc-marketing-0.1.0/pymc_marketing.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      859 2023-04-06 12:34:13.000000 pymc-marketing-0.1.0/pymc_marketing.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 12:34:13.000000 pymc-marketing-0.1.0/pymc_marketing.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      421 2023-04-06 12:34:13.000000 pymc-marketing-0.1.0/pymc_marketing.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-06 12:34:13.000000 pymc-marketing-0.1.0/pymc_marketing.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1602 2023-04-06 12:34:03.000000 pymc-marketing-0.1.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 12:34:13.707226 pymc-marketing-0.1.0/setup.cfg
```

### Comparing `pymc-marketing-0.0.4/LICENSE` & `pymc-marketing-0.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `pymc-marketing-0.0.4/PKG-INFO` & `pymc-marketing-0.1.0/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pymc-marketing
-Version: 0.0.4
+Version: 0.1.0
 Summary: Marketing Statistical Models in PyMC
 Maintainer-email: PyMC Labs <info@pymc-labs.io>
 License:                                  Apache License
                                    Version 2.0, January 2004
                                 http://www.apache.org/licenses/
         
            TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
@@ -211,24 +211,51 @@
 Provides-Extra: docs
 Provides-Extra: lint
 Provides-Extra: test
 License-File: LICENSE
 
 # PyMC-Marketing
 
-![Build](https://github.com/pymc-labs/pymmmc/workflows/ci/badge.svg)
+![Build](https://github.com/pymc-labs/pymc-marketing/workflows/ci/badge.svg)
 [![codecov](https://codecov.io/gh/pymc-labs/pymc-marketing/branch/main/graph/badge.svg?token=OBV3BS5TYE)](https://codecov.io/gh/pymc-labs/pymc-marketing)
 [![docs](https://readthedocs.org/projects/pymc-marketing/badge/?version=latest)](https://docs.readthedocs.io/en/latest/)
 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 [![PyPI Version](https://img.shields.io/pypi/v/pymc-marketing.svg)](https://pypi.python.org/pypi/pymc-marketing)
 [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
 
+**Unlock the power of marketing analytics with PyMC-Marketing – the open source solution for smarter decision-making.** Media mix modeling and customer lifetime value modules allow businesses to make data-driven decisions about their marketing campaigns. Optimize your marketing strategy and unlock the full potential of your customer data.
+
+---
+
+## Installation
+
+Start by setting up an environment (e.g. `marketing_env`) with PyMC. It may look something like the following:
+
+```bash
+mamba create -c conda-forge -n marketing_env python "pymc>=5"
+mamba activate marketing_env
+```
+
+See the official [PyMC installation guide](https://www.pymc.io/projects/docs/en/latest/installation.html) if more detail is needed.
+
+Assuming you have an environment set up then install PyMC-Marketing with the following command. This will give you the latest version of the library from PyPI.
+
+```bash
+pip install pymc-marketing
+```
+
+Alternatively you can install from GitHub directly:
+
+```bash
+pip install git+https://github.com/pymc-labs/pymc-marketing.git
+```
+
 ## Bayesian Media Mix Models (MMMs) in PyMC
 
-In this package we provide an API for a Bayesian media mix model (MMM) specification following [Jin, Yuxue, et al. “Bayesian methods for media mix modeling with carryover and shape effects.” (2017).](https://research.google/pubs/pub46001/). Concretely, given a time series target variable $y_{t}$ (e.g. sales on conversions), media variiables $x_{m, t}$ (e.g. impressions, clicks or costs) and a set of control covariates $z_{c, t}$ (e.g. holidays, special events) we consider a linear model of the form
+In this package we provide an API for a Bayesian media mix model (MMM) specification following [Jin, Yuxue, et al. “Bayesian methods for media mix modeling with carryover and shape effects.” (2017).](https://research.google/pubs/pub46001/) Concretely, given a time series target variable $y_{t}$ (e.g. sales on conversions), media variables $x_{m, t}$ (e.g. impressions, clicks or costs) and a set of control covariates $z_{c, t}$ (e.g. holidays, special events) we consider a linear model of the form
 
 $$
 y_{t} = \alpha + \sum_{m=1}^{M}\beta_{m}f(x_{m, t}) +  \sum_{c=1}^{C}\gamma_{c}z_{c, t} + \varepsilon_{t},
 $$
 
 where $\alpha$ is the intercept, $f$ is a media transformation function and $\varepsilon_{t}$ is the error therm which we assume is normally distributed. The function $f$ encodes the contribution of media on the target variable. Typically we consider two types of transformation: adstock (carry-over) and saturation effects.
 
@@ -246,70 +273,42 @@
   - [Improving the Speed and Accuracy of Bayesian Media Mix Models](https://www.pymc-labs.io/blog-posts/reducing-customer-acquisition-costs-how-we-helped-optimizing-hellofreshs-marketing-budget/)
 - [Johns, Michael and Wang,  Zhenyu. "A Bayesian Approach to Media Mix Modeling"](https://www.youtube.com/watch?v=UznM_-_760Y)
 - [Orduz, Juan. "Media Effect Estimation with PyMC: Adstock, Saturation & Diminishing Returns"](https://juanitorduz.github.io/pymc_mmm/)
 
 ---
 
 ## Bayesian CLVs in PyMC
-[Customer Lifetime Value](https://en.wikipedia.org/wiki/Customer_lifetime_value) models is another important class of models. There are many different types of CLV models and it can be helpful to conceptualise them as fitting in a 2-dimensional grid as below. An excellent set of introduction slides to CLV's is provided in [Probability Models for Customer-Base Analysis](https://www.brucehardie.com/talks/ho_cba_tut_art_09.pdf) by Fader & Hardie (2009).
+[Customer Lifetime Value](https://en.wikipedia.org/wiki/Customer_lifetime_value) (CLV) models are another important class of models. There are many different types of CLV models and it can be helpful to conceptualise them as fitting in a 2-dimensional grid as below. An excellent set of introduction slides to CLV's is provided in [Probability Models for Customer-Base Analysis](https://www.brucehardie.com/talks/ho_cba_tut_art_09.pdf) by Fader & Hardie (2009).
 
 ### Examples
 
 |                | **Non-contractual** | **Contractual**                 |
 |----------------|---------------------|---------------------------------|
 | **Continuous** | Buying groceries    | Audible                         |
 | **Discrete**   | Cinema ticket       | Monthly or yearly subscriptions |
 
 To explain further:
-- **Contractual:** In contractual settings a customer has a contract which continues to be active until it is explicitly cancelled. Therefore in contractual settings, customer churn events are observed.
+- **Contractual:** In contractual settings, a customer has a contract which continues to be active until it is explicitly cancelled. Therefore, customer churn events are observed.
 
 - **Non-contractual:** In non-contractual settings, there is no ongoing contract that a customer has with a company. Instead, purchases can be ad hoc and churn events are unobserved.
 
 - **Discrete:** Here, purchases are made at discrete points in time. This obviously depends upon the timescale that we are working on, but typically a relevant time period would be a month or year. However it could be more granualar than this - think of taking the 2nd of 4 inter-city train journeys offered per day.
 
-- **Continuous:** In the continuous-time domain, purchases can be made at any point within a firms opening hours. For online ordering this could be any point within a 24 hour cycle, or purchases in physical stores could be made at any point during the trading day.
+- **Continuous:** In the continuous-time domain, purchases can be made at any point within a firms opening hours. For online ordering, this could be any point within a 24 hour cycle, or purchases in physical stores could be made at any point during the trading day.
 
-In the documentation we provide some examples on how to use the CLV API. We use the data from the [`lifetimes`](https://github.com/CamDavidsonPilon/lifetimes) package to illustrate the models.
+In the documentation, we provide some examples on how to use the CLV API. We use the data from the [`lifetimes`](https://github.com/CamDavidsonPilon/lifetimes) package to illustrate the models.
 
 - [CLV Quickstart](https://pymc-marketing.readthedocs.io/en/stable/notebooks/clv/clv_quickstart.html)
 - [BG/NBD model](https://pymc-marketing.readthedocs.io/en/stable/notebooks/clv/bg_nbd.html)
 - [Gamma-Gamma model](https://pymc-marketing.readthedocs.io/en/stable/notebooks/clv/gamma_gamma.html)
 
 ---
 
-## Local Development
+## 📞 Schedule a Consultation
+Unlock your potential with a free 30-minute strategy session with our PyMC experts. Discover how open source solutions and pymc-marketing can elevate your media-mix models and customer lifetime value analyses. Boost your career and organization by making smarter, data-driven decisions. Don't wait—[claim your complimentary session](https://calendly.com/benjamin-vincent/pymc-marketing) today and lead the way in marketing and data science innovation.
 
-1. Create conda environment. For example:
+## Using PyMC-Marketing and how PyMC Labs can help you
+PyMC-Marketing uses the [Apache 2.0 licence](LICENSE) which permits commercial use, amongst other things.
 
-```shell
-conda create -n pymc_marketing_env
-```
+If you want to build upon the package, please feel free to fork the repo and submit a pull request. If in doubt, please open an issue.
 
-2. Activate environment.
-
-```shell
-conda activate pymc_marketing_env
-```
-
-3. Install `pymc_marketing` package:
-
-```shell
-make init
-```
-
-4. To run tests:
-
-```shell
-make test
-```
-
-5. To check code style:
-
-```shell
-make check_lint
-```
-
-6. Set [pre-commit hooks](https://pre-commit.com/) (Optional):
-
-```shell
-pre-commit install
-```
+For companies that want to use PyMC-Marketing in production, [PyMC Labs](https://www.pymc-labs.io) is available for consulting and training. We can help you build and deploy your models in production. We have experience with cutting edge Bayesian modelling techniques in general, and in particular with MMMs and CLVs. For example, see our video on [Bayesian Marketing Mix Models: State of the Art and their Future](https://www.youtube.com/watch?v=xVx91prC81g).
```

### Comparing `pymc-marketing-0.0.4/README.md` & `pymc-marketing-0.1.0/README.md`

 * *Files 20% similar despite different names*

```diff
@@ -1,19 +1,46 @@
 # PyMC-Marketing
 
-![Build](https://github.com/pymc-labs/pymmmc/workflows/ci/badge.svg)
+![Build](https://github.com/pymc-labs/pymc-marketing/workflows/ci/badge.svg)
 [![codecov](https://codecov.io/gh/pymc-labs/pymc-marketing/branch/main/graph/badge.svg?token=OBV3BS5TYE)](https://codecov.io/gh/pymc-labs/pymc-marketing)
 [![docs](https://readthedocs.org/projects/pymc-marketing/badge/?version=latest)](https://docs.readthedocs.io/en/latest/)
 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 [![PyPI Version](https://img.shields.io/pypi/v/pymc-marketing.svg)](https://pypi.python.org/pypi/pymc-marketing)
 [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
 
+**Unlock the power of marketing analytics with PyMC-Marketing – the open source solution for smarter decision-making.** Media mix modeling and customer lifetime value modules allow businesses to make data-driven decisions about their marketing campaigns. Optimize your marketing strategy and unlock the full potential of your customer data.
+
+---
+
+## Installation
+
+Start by setting up an environment (e.g. `marketing_env`) with PyMC. It may look something like the following:
+
+```bash
+mamba create -c conda-forge -n marketing_env python "pymc>=5"
+mamba activate marketing_env
+```
+
+See the official [PyMC installation guide](https://www.pymc.io/projects/docs/en/latest/installation.html) if more detail is needed.
+
+Assuming you have an environment set up then install PyMC-Marketing with the following command. This will give you the latest version of the library from PyPI.
+
+```bash
+pip install pymc-marketing
+```
+
+Alternatively you can install from GitHub directly:
+
+```bash
+pip install git+https://github.com/pymc-labs/pymc-marketing.git
+```
+
 ## Bayesian Media Mix Models (MMMs) in PyMC
 
-In this package we provide an API for a Bayesian media mix model (MMM) specification following [Jin, Yuxue, et al. “Bayesian methods for media mix modeling with carryover and shape effects.” (2017).](https://research.google/pubs/pub46001/). Concretely, given a time series target variable $y_{t}$ (e.g. sales on conversions), media variiables $x_{m, t}$ (e.g. impressions, clicks or costs) and a set of control covariates $z_{c, t}$ (e.g. holidays, special events) we consider a linear model of the form
+In this package we provide an API for a Bayesian media mix model (MMM) specification following [Jin, Yuxue, et al. “Bayesian methods for media mix modeling with carryover and shape effects.” (2017).](https://research.google/pubs/pub46001/) Concretely, given a time series target variable $y_{t}$ (e.g. sales on conversions), media variables $x_{m, t}$ (e.g. impressions, clicks or costs) and a set of control covariates $z_{c, t}$ (e.g. holidays, special events) we consider a linear model of the form
 
 $$
 y_{t} = \alpha + \sum_{m=1}^{M}\beta_{m}f(x_{m, t}) +  \sum_{c=1}^{C}\gamma_{c}z_{c, t} + \varepsilon_{t},
 $$
 
 where $\alpha$ is the intercept, $f$ is a media transformation function and $\varepsilon_{t}$ is the error therm which we assume is normally distributed. The function $f$ encodes the contribution of media on the target variable. Typically we consider two types of transformation: adstock (carry-over) and saturation effects.
 
@@ -31,70 +58,42 @@
   - [Improving the Speed and Accuracy of Bayesian Media Mix Models](https://www.pymc-labs.io/blog-posts/reducing-customer-acquisition-costs-how-we-helped-optimizing-hellofreshs-marketing-budget/)
 - [Johns, Michael and Wang,  Zhenyu. "A Bayesian Approach to Media Mix Modeling"](https://www.youtube.com/watch?v=UznM_-_760Y)
 - [Orduz, Juan. "Media Effect Estimation with PyMC: Adstock, Saturation & Diminishing Returns"](https://juanitorduz.github.io/pymc_mmm/)
 
 ---
 
 ## Bayesian CLVs in PyMC
-[Customer Lifetime Value](https://en.wikipedia.org/wiki/Customer_lifetime_value) models is another important class of models. There are many different types of CLV models and it can be helpful to conceptualise them as fitting in a 2-dimensional grid as below. An excellent set of introduction slides to CLV's is provided in [Probability Models for Customer-Base Analysis](https://www.brucehardie.com/talks/ho_cba_tut_art_09.pdf) by Fader & Hardie (2009).
+[Customer Lifetime Value](https://en.wikipedia.org/wiki/Customer_lifetime_value) (CLV) models are another important class of models. There are many different types of CLV models and it can be helpful to conceptualise them as fitting in a 2-dimensional grid as below. An excellent set of introduction slides to CLV's is provided in [Probability Models for Customer-Base Analysis](https://www.brucehardie.com/talks/ho_cba_tut_art_09.pdf) by Fader & Hardie (2009).
 
 ### Examples
 
 |                | **Non-contractual** | **Contractual**                 |
 |----------------|---------------------|---------------------------------|
 | **Continuous** | Buying groceries    | Audible                         |
 | **Discrete**   | Cinema ticket       | Monthly or yearly subscriptions |
 
 To explain further:
-- **Contractual:** In contractual settings a customer has a contract which continues to be active until it is explicitly cancelled. Therefore in contractual settings, customer churn events are observed.
+- **Contractual:** In contractual settings, a customer has a contract which continues to be active until it is explicitly cancelled. Therefore, customer churn events are observed.
 
 - **Non-contractual:** In non-contractual settings, there is no ongoing contract that a customer has with a company. Instead, purchases can be ad hoc and churn events are unobserved.
 
 - **Discrete:** Here, purchases are made at discrete points in time. This obviously depends upon the timescale that we are working on, but typically a relevant time period would be a month or year. However it could be more granualar than this - think of taking the 2nd of 4 inter-city train journeys offered per day.
 
-- **Continuous:** In the continuous-time domain, purchases can be made at any point within a firms opening hours. For online ordering this could be any point within a 24 hour cycle, or purchases in physical stores could be made at any point during the trading day.
+- **Continuous:** In the continuous-time domain, purchases can be made at any point within a firms opening hours. For online ordering, this could be any point within a 24 hour cycle, or purchases in physical stores could be made at any point during the trading day.
 
-In the documentation we provide some examples on how to use the CLV API. We use the data from the [`lifetimes`](https://github.com/CamDavidsonPilon/lifetimes) package to illustrate the models.
+In the documentation, we provide some examples on how to use the CLV API. We use the data from the [`lifetimes`](https://github.com/CamDavidsonPilon/lifetimes) package to illustrate the models.
 
 - [CLV Quickstart](https://pymc-marketing.readthedocs.io/en/stable/notebooks/clv/clv_quickstart.html)
 - [BG/NBD model](https://pymc-marketing.readthedocs.io/en/stable/notebooks/clv/bg_nbd.html)
 - [Gamma-Gamma model](https://pymc-marketing.readthedocs.io/en/stable/notebooks/clv/gamma_gamma.html)
 
 ---
 
-## Local Development
+## 📞 Schedule a Consultation
+Unlock your potential with a free 30-minute strategy session with our PyMC experts. Discover how open source solutions and pymc-marketing can elevate your media-mix models and customer lifetime value analyses. Boost your career and organization by making smarter, data-driven decisions. Don't wait—[claim your complimentary session](https://calendly.com/benjamin-vincent/pymc-marketing) today and lead the way in marketing and data science innovation.
 
-1. Create conda environment. For example:
+## Using PyMC-Marketing and how PyMC Labs can help you
+PyMC-Marketing uses the [Apache 2.0 licence](LICENSE) which permits commercial use, amongst other things.
 
-```shell
-conda create -n pymc_marketing_env
-```
+If you want to build upon the package, please feel free to fork the repo and submit a pull request. If in doubt, please open an issue.
 
-2. Activate environment.
-
-```shell
-conda activate pymc_marketing_env
-```
-
-3. Install `pymc_marketing` package:
-
-```shell
-make init
-```
-
-4. To run tests:
-
-```shell
-make test
-```
-
-5. To check code style:
-
-```shell
-make check_lint
-```
-
-6. Set [pre-commit hooks](https://pre-commit.com/) (Optional):
-
-```shell
-pre-commit install
-```
+For companies that want to use PyMC-Marketing in production, [PyMC Labs](https://www.pymc-labs.io) is available for consulting and training. We can help you build and deploy your models in production. We have experience with cutting edge Bayesian modelling techniques in general, and in particular with MMMs and CLVs. For example, see our video on [Bayesian Marketing Mix Models: State of the Art and their Future](https://www.youtube.com/watch?v=xVx91prC81g).
```

### Comparing `pymc-marketing-0.0.4/pymc_marketing/clv/__init__.py` & `pymc-marketing-0.1.0/pymc_marketing/clv/__init__.py`

 * *Files identical despite different names*

### Comparing `pymc-marketing-0.0.4/pymc_marketing/clv/distributions.py` & `pymc-marketing-0.1.0/pymc_marketing/clv/distributions.py`

 * *Files identical despite different names*

### Comparing `pymc-marketing-0.0.4/pymc_marketing/clv/models/basic.py` & `pymc-marketing-0.1.0/pymc_marketing/clv/models/basic.py`

 * *Files 6% similar despite different names*

```diff
@@ -33,33 +33,33 @@
             raise ValueError("Prior variables must be unique")
 
         # Related to https://github.com/pymc-devs/pymc/issues/6311
         for prior in priors:
             prior.str_repr = types.MethodType(str_for_dist, prior)
         return priors
 
-    def fit(self, fitting_method="mcmc", **kwargs):
+    def fit(self, fit_method="mcmc", **kwargs):
         """Infer model posterior
 
         Parameters
         ----------
-        fitting_method: str
+        fit_method: str
             Method used to fit the model. Options are:
             - "mcmc": Samples from the posterior via `pymc.sample` (default)
             - "map": Finds maximum a posteriori via `pymc.find_MAP`
         kwargs:
             Other keyword arguments passed to the underlying PyMC routines
         """
-        if fitting_method == "mcmc":
+        if fit_method == "mcmc":
             res = self._fit_mcmc(**kwargs)
-        elif fitting_method == "map":
+        elif fit_method == "map":
             res = self._fit_MAP(**kwargs)
         else:
             raise ValueError(
-                f"Fitting method options are ['mcmc', 'map'], got: {fitting_method}"
+                f"Fit method options are ['mcmc', 'map'], got: {fit_method}"
             )
         self.fit_result = res
         return res
 
     def _fit_mcmc(self, **kwargs):
         """Draw samples from model posterior using MCMC sampling"""
         with self.model:
```

### Comparing `pymc-marketing-0.0.4/pymc_marketing/clv/models/beta_geo.py` & `pymc-marketing-0.1.0/pymc_marketing/clv/models/beta_geo.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from typing import Optional, Union
 
 import numpy as np
 import pandas as pd
 import pymc as pm
 import pytensor.tensor as pt
 import xarray as xr
-from pymc.distributions.dist_math import betaln, check_parameters
+from pymc.distributions.dist_math import check_parameters
 from pytensor.tensor import TensorVariable
 from scipy.special import expit, hyp2f1
 
 from pymc_marketing.clv.models.basic import CLVModel
 from pymc_marketing.clv.utils import to_xarray
 
 
@@ -141,32 +141,31 @@
             r = self.model.register_rv(r_prior, name="r")
 
             def logp(t_x, x, a, b, r, alpha, T):
                 """
                 The log-likelihood expression here aligns with expression (4) from [3]
                 due to the possible numerical instability of expression (3).
                 """
-                zero_observations = pt.eq(x, 0)
+                x_non_zero = x > 0
 
-                A = betaln(a, b + x) - betaln(a, b) + pt.gammaln(r + x) - pt.gammaln(r)
-                A += r * pt.log(alpha) - (r + x) * pt.log(alpha + T)
-
-                B = (
-                    betaln(a + 1, b + x - 1)
-                    - betaln(a, b)
-                    + pt.gammaln(r + x)
+                # Refactored for numerical error
+                d1 = (
+                    pt.gammaln(r + x)
                     - pt.gammaln(r)
+                    + pt.gammaln(a + b)
+                    + pt.gammaln(b + x)
+                    - pt.gammaln(b)
+                    - pt.gammaln(a + b + x)
                 )
-                B += r * pt.log(alpha) - (r + x) * pt.log(alpha + t_x)
 
-                logp = pt.switch(
-                    zero_observations,
-                    A,
-                    pt.logaddexp(A, B),
-                )
+                d2 = r * pt.log(alpha) - (r + x) * pt.log(alpha + t_x)
+                c3 = ((alpha + t_x) / (alpha + T)) ** (r + x)
+                c4 = a / (b + x - 1)
+
+                logp = d1 + d2 + pt.log(c3 + pt.switch(x_non_zero, c4, 0))
 
                 return check_parameters(
                     logp,
                     a > 0,
                     b > 0,
                     alpha > 0,
                     r > 0,
```

### Comparing `pymc-marketing-0.0.4/pymc_marketing/clv/models/gamma_gamma.py` & `pymc-marketing-0.1.0/pymc_marketing/clv/models/gamma_gamma.py`

 * *Files identical despite different names*

### Comparing `pymc-marketing-0.0.4/pymc_marketing/clv/models/shifted_beta_geo.py` & `pymc-marketing-0.1.0/pymc_marketing/clv/models/shifted_beta_geo.py`

 * *Files identical despite different names*

### Comparing `pymc-marketing-0.0.4/pymc_marketing/clv/plotting.py` & `pymc-marketing-0.1.0/pymc_marketing/clv/plotting.py`

 * *Files identical despite different names*

### Comparing `pymc-marketing-0.0.4/pymc_marketing/clv/utils.py` & `pymc-marketing-0.1.0/pymc_marketing/clv/utils.py`

 * *Files identical despite different names*

### Comparing `pymc-marketing-0.0.4/pymc_marketing/mmm/base.py` & `pymc-marketing-0.1.0/pymc_marketing/mmm/base.py`

 * *Files 19% similar despite different names*

```diff
@@ -28,36 +28,36 @@
 
 __all__ = ("BaseMMM", "MMM")
 
 
 class BaseMMM:
     def __init__(
         self,
-        data_df: pd.DataFrame,
+        data: pd.DataFrame,
         target_column: str,
         date_column: str,
         channel_columns: Union[List[str], Tuple[str]],
         validate_data: bool = True,
         **kwargs,
     ) -> None:
-        self.data_df: pd.DataFrame = data_df
+        self.data: pd.DataFrame = data
         self.target_column: str = target_column
         self.date_column: str = date_column
         self.channel_columns: Union[List[str], Tuple[str]] = channel_columns
-        self.n_obs: int = data_df.shape[0]
+        self.n_obs: int = data.shape[0]
         self.n_channel: int = len(channel_columns)
         self._fit_result: Optional[az.InferenceData] = None
         self._posterior_predictive: Optional[az.InferenceData] = None
 
         if validate_data:
-            self.validate(self.data_df)
-        self.preprocessed_data = self.preprocess(self.data_df.copy())
+            self.validate(self.data)
+        self.preprocessed_data = self.preprocess(self.data.copy())
 
         self.build_model(
-            data_df=self.preprocessed_data,
+            data=self.preprocessed_data,
             **kwargs,
         )
 
     @property
     def methods(self) -> List[Any]:
         maybe_methods = [getattr_static(self, attr) for attr in dir(self)]
         return [
@@ -91,22 +91,22 @@
     def get_target_transformer(self) -> Pipeline:
         try:
             return self.target_transformer
         except AttributeError:
             identity_transformer = FunctionTransformer()
             return Pipeline(steps=[("scaler", identity_transformer)])
 
-    def validate(self, data_df: pd.DataFrame):
+    def validate(self, data: pd.DataFrame):
         for method in self.validation_methods:
-            method(self, data_df)
+            method(self, data)
 
-    def preprocess(self, data_df: pd.DataFrame) -> pd.DataFrame:
+    def preprocess(self, data: pd.DataFrame) -> pd.DataFrame:
         for method in self.preprocessing_methods:
-            data_df = method(self, data_df)
-        return data_df
+            data = method(self, data)
+        return data
 
     @abstractmethod
     def build_model(*args, **kwargs):
         raise NotImplementedError()
 
     def get_prior_predictive_data(self, *args, **kwargs) -> az.InferenceData:
         try:
@@ -158,33 +158,33 @@
         likelihood_hdi_50: DataArray = az.hdi(
             ary=prior_predictive_data["prior_predictive"], hdi_prob=0.50
         )["likelihood"]
 
         fig, ax = plt.subplots(**plt_kwargs)
 
         ax.fill_between(
-            x=self.data_df[self.date_column],
+            x=self.data[self.date_column],
             y1=likelihood_hdi_94[:, 0],
             y2=likelihood_hdi_94[:, 1],
             color="C0",
             alpha=0.2,
             label="94% HDI",
         )
 
         ax.fill_between(
-            x=self.data_df[self.date_column],
+            x=self.data[self.date_column],
             y1=likelihood_hdi_50[:, 0],
             y2=likelihood_hdi_50[:, 1],
             color="C0",
             alpha=0.3,
             label="50% HDI",
         )
 
         ax.plot(
-            self.data_df[self.date_column],
+            self.data[self.date_column],
             self.preprocessed_data[self.target_column],
             color="black",
         )
         ax.set(title="Prior Predictive Check", xlabel="date", ylabel=self.target_column)
         return fig
 
     def plot_posterior_predictive(
@@ -206,37 +206,37 @@
             likelihood_hdi_50 = self.get_target_transformer().inverse_transform(
                 Xt=likelihood_hdi_50
             )
 
         fig, ax = plt.subplots(**plt_kwargs)
 
         ax.fill_between(
-            x=self.data_df[self.date_column],
+            x=self.data[self.date_column],
             y1=likelihood_hdi_94[:, 0],
             y2=likelihood_hdi_94[:, 1],
             color="C0",
             alpha=0.2,
             label="94% HDI",
         )
 
         ax.fill_between(
-            x=self.data_df[self.date_column],
+            x=self.data[self.date_column],
             y1=likelihood_hdi_50[:, 0],
             y2=likelihood_hdi_50[:, 1],
             color="C0",
             alpha=0.3,
             label="50% HDI",
         )
 
         target_to_plot: pd.Series = (
-            self.data_df[self.target_column]
+            self.data[self.target_column]
             if original_scale
             else self.preprocessed_data[self.target_column]
         )
-        ax.plot(self.data_df[self.date_column], target_to_plot, color="black")
+        ax.plot(self.data[self.date_column], target_to_plot, color="black")
         ax.set(
             title="Posterior Predictive Check",
             xlabel="date",
             ylabel=self.target_column,
         )
         return fig
 
@@ -286,50 +286,50 @@
             zip(
                 means,
                 contribution_vars,
                 ["channel_contribution", "control_contribution"],
             )
         ):
             ax.fill_between(
-                x=self.data_df[self.date_column],
+                x=self.data[self.date_column],
                 y1=hdi.isel(hdi=0),
                 y2=hdi.isel(hdi=1),
                 color=f"C{i}",
                 alpha=0.25,
                 label=f"$94 %$ HDI ({var_contribution})",
             )
             sns.lineplot(
-                x=self.data_df[self.date_column],
+                x=self.data[self.date_column],
                 y=mean,
                 color=f"C{i}",
                 ax=ax,
             )
 
         intercept = az.extract(self.fit_result, var_names=["intercept"], combined=False)
         intercept_hdi = np.repeat(
             a=az.hdi(intercept).intercept.data[None, ...],
             repeats=self.n_obs,
             axis=0,
         )
         sns.lineplot(
-            x=self.data_df[self.date_column],
+            x=self.data[self.date_column],
             y=intercept.mean().data,
             color=f"C{i + 1}",
             ax=ax,
         )
         ax.fill_between(
-            x=self.data_df[self.date_column],
+            x=self.data[self.date_column],
             y1=intercept_hdi[:, 0],
             y2=intercept_hdi[:, 1],
             color=f"C{i + 1}",
             alpha=0.25,
             label="$94 %$ HDI (intercept)",
         )
         ax.plot(
-            self.data_df[self.date_column],
+            self.data[self.date_column],
             self.preprocessed_data[self.target_column],
             color="black",
         )
         ax.legend(title="components", loc="center left", bbox_to_anchor=(1, 0.5))
         ax.set(
             title="Posterior Predictive Model Components",
             xlabel="date",
@@ -388,15 +388,15 @@
             figsize=(12, 4 * self.n_channel),
             layout="constrained",
         )
 
         for i, channel in enumerate(self.channel_columns):
             ax = axes[i]
             sns.regplot(
-                x=self.data_df[self.channel_columns].to_numpy()[:, i],
+                x=self.data[self.channel_columns].to_numpy()[:, i],
                 y=channel_contributions.sel(channel=channel),
                 color=f"C{i}",
                 order=2,
                 ci=None,
                 line_kws={
                     "linestyle": "--",
                     "alpha": 0.5,
@@ -432,10 +432,13 @@
             backend_kwargs=plot_kwargs,
         )
         ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda y, _: f"{y: 0.0%}"))
         fig: plt.Figure = plt.gcf()
         fig.suptitle("channel Contribution Share", fontsize=16, y=1.05)
         return fig
 
+    def graphviz(self, **kwargs):
+        return pm.model_to_graphviz(self.model, **kwargs)
+
 
 class MMM(BaseMMM, ValidateTargetColumn, ValidateDateColumn, ValidateChannelColumns):
     pass
```

### Comparing `pymc-marketing-0.0.4/pymc_marketing/mmm/delayed_saturated_mmm.py` & `pymc-marketing-0.1.0/pymc_marketing/mmm/delayed_saturated_mmm.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,58 +1,53 @@
 from typing import Any, Dict, List, Optional
 
-import arviz as az
 import pandas as pd
 import pymc as pm
-from xarray import DataArray
 
 from pymc_marketing.mmm.base import MMM
-from pymc_marketing.mmm.preprocessing import MaxAbsScaleChannels, MixMaxScaleTarget
-from pymc_marketing.mmm.transformers import (
-    geometric_adstock_vectorized,
-    logistic_saturation,
-)
+from pymc_marketing.mmm.preprocessing import MaxAbsScaleChannels, MaxAbsScaleTarget
+from pymc_marketing.mmm.transformers import geometric_adstock, logistic_saturation
 from pymc_marketing.mmm.validating import ValidateControlColumns
 
 
 class DelayedSaturatedMMM(
-    MMM, MixMaxScaleTarget, MaxAbsScaleChannels, ValidateControlColumns
+    MMM, MaxAbsScaleTarget, MaxAbsScaleChannels, ValidateControlColumns
 ):
     def __init__(
         self,
-        data_df: pd.DataFrame,
+        data: pd.DataFrame,
         target_column: str,
         date_column: str,
         channel_columns: List[str],
         validate_data: bool = True,
         control_columns: Optional[List[str]] = None,
         adstock_max_lag: int = 4,
         **kwargs,
     ) -> None:
         self.control_columns = control_columns
         self.adstock_max_lag = adstock_max_lag
         super().__init__(
-            data_df=data_df,
+            data=data,
             target_column=target_column,
             date_column=date_column,
             channel_columns=channel_columns,
             validate_data=validate_data,
             adstock_max_lag=adstock_max_lag,
         )
 
     def build_model(
         self,
-        data_df: pd.DataFrame,
+        data: pd.DataFrame,
         adstock_max_lag: int = 4,
     ) -> None:
-        date_data = data_df[self.date_column]
-        target_data = data_df[self.target_column]
-        channel_data = data_df[self.channel_columns]
+        date_data = data[self.date_column]
+        target_data = data[self.target_column]
+        channel_data = data[self.channel_columns]
         if self.control_columns is not None:
-            control_data: Optional[pd.DataFrame] = data_df[self.control_columns]
+            control_data: Optional[pd.DataFrame] = data[self.control_columns]
         else:
             control_data = None
         coords: Dict[str, Any] = {
             "date": date_data,
             "channel": channel_data.columns,
         }
 
@@ -78,19 +73,20 @@
 
             lam = pm.Gamma(name="lam", alpha=3, beta=1, dims="channel")
 
             sigma = pm.HalfNormal(name="sigma", sigma=2)
 
             channel_adstock = pm.Deterministic(
                 name="channel_adstock",
-                var=geometric_adstock_vectorized(
+                var=geometric_adstock(
                     x=channel_data_,
                     alpha=alpha,
                     l_max=adstock_max_lag,
                     normalize=True,
+                    axis=0,
                 ),
                 dims=("date", "channel"),
             )
             channel_adstock_saturated = pm.Deterministic(
                 name="channel_adstock_saturated",
                 var=logistic_saturation(x=channel_adstock, lam=lam),
                 dims=("date", "channel"),
@@ -125,25 +121,7 @@
             pm.Normal(
                 name="likelihood",
                 mu=mu,
                 sigma=sigma,
                 observed=target_,
                 dims="date",
             )
-
-    def compute_channel_contribution_original_scale(self) -> DataArray:
-        beta_channel_samples_extended: DataArray = az.extract(
-            data=self.fit_result, var_names=["beta_channel"], combined=False
-        ).expand_dims({"date": self.n_obs}, axis=2)
-
-        channel_transformed: DataArray = az.extract(
-            data=self.fit_result,
-            var_names=["channel_adstock_saturated"],
-            combined=False,
-        )
-
-        normalization_factor: float = self.target_transformer.named_steps[
-            "scaler"
-        ].scale_.item()
-        return (
-            beta_channel_samples_extended * channel_transformed
-        ) / normalization_factor
```

### Comparing `pymc-marketing-0.0.4/pymc_marketing/mmm/preprocessing.py` & `pymc-marketing-0.1.0/pymc_marketing/mmm/preprocessing.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,58 +1,58 @@
 from typing import Callable
 
 import pandas as pd
 from sklearn.pipeline import Pipeline
-from sklearn.preprocessing import MaxAbsScaler, MinMaxScaler, StandardScaler
+from sklearn.preprocessing import MaxAbsScaler, StandardScaler
 
 __all__ = [
     "preprocessing_method",
-    "MixMaxScaleTarget",
+    "MaxAbsScaleTarget",
     "MaxAbsScaleChannels",
     "StandardizeControls",
 ]
 
 
 def preprocessing_method(method: Callable) -> Callable:
     if not hasattr(method, "_tags"):
         method._tags = {}
     method._tags["preprocessing"] = True
     return method
 
 
-class MixMaxScaleTarget:
+class MaxAbsScaleTarget:
     @preprocessing_method
-    def min_max_scale_target_data(self, data_df: pd.DataFrame) -> pd.DataFrame:
-        target_vector = data_df[self.target_column].to_numpy().reshape(-1, 1)
-        transformers = [("scaler", MinMaxScaler())]
+    def max_abs_scale_target_data(self, data: pd.DataFrame) -> pd.DataFrame:
+        target_vector = data[self.target_column].to_numpy().reshape(-1, 1)
+        transformers = [("scaler", MaxAbsScaler())]
         pipeline = Pipeline(steps=transformers)
         self.target_transformer: Pipeline = pipeline.fit(X=target_vector)
-        data_df[self.target_column] = self.target_transformer.transform(
+        data[self.target_column] = self.target_transformer.transform(
             X=target_vector
         ).flatten()
-        return data_df
+        return data
 
 
 class MaxAbsScaleChannels:
     @preprocessing_method
-    def max_abs_scale_channel_data(self, data_df: pd.DataFrame) -> pd.DataFrame:
-        channel_data: pd.DataFrame = data_df[self.channel_columns]
+    def max_abs_scale_channel_data(self, data: pd.DataFrame) -> pd.DataFrame:
+        channel_data: pd.DataFrame = data[self.channel_columns]
         transformers = [("scaler", MaxAbsScaler())]
         pipeline: Pipeline = Pipeline(steps=transformers)
         self.channel_transformer: Pipeline = pipeline.fit(X=channel_data.to_numpy())
-        data_df[self.channel_columns] = self.channel_transformer.transform(
+        data[self.channel_columns] = self.channel_transformer.transform(
             channel_data.to_numpy()
         )
-        return data_df
+        return data
 
 
 class StandardizeControls:
     @preprocessing_method
-    def standardize_control_data(self, data_df: pd.DataFrame) -> pd.DataFrame:
-        control_data: pd.DataFrame = data_df[self.control_columns]
+    def standardize_control_data(self, data: pd.DataFrame) -> pd.DataFrame:
+        control_data: pd.DataFrame = data[self.control_columns]
         transformers = [("scaler", StandardScaler())]
         pipeline: Pipeline = Pipeline(steps=transformers)
         self.control_transformer: Pipeline = pipeline.fit(X=control_data.to_numpy())
-        data_df[self.control_columns] = self.control_transformer.transform(
+        data[self.control_columns] = self.control_transformer.transform(
             control_data.to_numpy()
         )
-        return data_df
+        return data
```

### Comparing `pymc-marketing-0.0.4/pymc_marketing/mmm/utils.py` & `pymc-marketing-0.1.0/pymc_marketing/mmm/utils.py`

 * *Files identical despite different names*

### Comparing `pymc-marketing-0.0.4/pymc_marketing/mmm/validating.py` & `pymc-marketing-0.1.0/pymc_marketing/mmm/validating.py`

 * *Files 13% similar despite different names*

```diff
@@ -16,57 +16,57 @@
         method._tags = {}
     method._tags["validation"] = True
     return method
 
 
 class ValidateTargetColumn:
     @validation_method
-    def validate_target(self, data_df: pd.DataFrame) -> None:
-        if self.target_column not in data_df.columns:
-            raise ValueError(f"target {self.target_column} not in data_df")
+    def validate_target(self, data: pd.DataFrame) -> None:
+        if self.target_column not in data.columns:
+            raise ValueError(f"target {self.target_column} not in data")
 
 
 class ValidateDateColumn:
     @validation_method
-    def validate_date_col(self, data_df: pd.DataFrame) -> None:
-        if self.date_column not in data_df.columns:
-            raise ValueError(f"date_col {self.date_column} not in data_df")
-        if not data_df[self.date_column].is_unique:
+    def validate_date_col(self, data: pd.DataFrame) -> None:
+        if self.date_column not in data.columns:
+            raise ValueError(f"date_col {self.date_column} not in data")
+        if not data[self.date_column].is_unique:
             raise ValueError(f"date_col {self.date_column} has repeated values")
 
 
 class ValidateChannelColumns:
     @validation_method
-    def validate_channel_columns(self, data_df: pd.DataFrame) -> None:
+    def validate_channel_columns(self, data: pd.DataFrame) -> None:
         if not isinstance(self.channel_columns, (list, tuple)):
             raise ValueError("channel_columns must be a list or tuple")
         if len(self.channel_columns) == 0:
             raise ValueError("channel_columns must not be empty")
-        if not set(self.channel_columns).issubset(data_df.columns):
-            raise ValueError(f"channel_columns {self.channel_columns} not in data_df")
+        if not set(self.channel_columns).issubset(data.columns):
+            raise ValueError(f"channel_columns {self.channel_columns} not in data")
         if len(set(self.channel_columns)) != len(self.channel_columns):
             raise ValueError(
                 f"channel_columns {self.channel_columns} contains duplicates"
             )
-        if (data_df[self.channel_columns] < 0).any().any():
+        if (data[self.channel_columns] < 0).any().any():
             raise ValueError(
                 f"channel_columns {self.channel_columns} contains negative values"
             )
 
 
 class ValidateControlColumns:
     @validation_method
-    def validate_control_columns(self, data_df: pd.DataFrame) -> None:
+    def validate_control_columns(self, data: pd.DataFrame) -> None:
         if self.control_columns is None:
             return None
         if not isinstance(self.control_columns, (list, tuple)):
             raise ValueError("control_columns must be None, a list or tuple")
         if len(self.control_columns) == 0:
             raise ValueError(
                 "If control_columns is not None, then it must not be empty"
             )
-        if not set(self.control_columns).issubset(data_df.columns):
-            raise ValueError(f"control_columns {self.control_columns} not in data_df")
+        if not set(self.control_columns).issubset(data.columns):
+            raise ValueError(f"control_columns {self.control_columns} not in data")
         if len(set(self.control_columns)) != len(self.control_columns):
             raise ValueError(
                 f"control_columns {self.control_columns} contains duplicates"
             )
```

### Comparing `pymc-marketing-0.0.4/pymc_marketing.egg-info/PKG-INFO` & `pymc-marketing-0.1.0/pymc_marketing.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pymc-marketing
-Version: 0.0.4
+Version: 0.1.0
 Summary: Marketing Statistical Models in PyMC
 Maintainer-email: PyMC Labs <info@pymc-labs.io>
 License:                                  Apache License
                                    Version 2.0, January 2004
                                 http://www.apache.org/licenses/
         
            TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
@@ -211,24 +211,51 @@
 Provides-Extra: docs
 Provides-Extra: lint
 Provides-Extra: test
 License-File: LICENSE
 
 # PyMC-Marketing
 
-![Build](https://github.com/pymc-labs/pymmmc/workflows/ci/badge.svg)
+![Build](https://github.com/pymc-labs/pymc-marketing/workflows/ci/badge.svg)
 [![codecov](https://codecov.io/gh/pymc-labs/pymc-marketing/branch/main/graph/badge.svg?token=OBV3BS5TYE)](https://codecov.io/gh/pymc-labs/pymc-marketing)
 [![docs](https://readthedocs.org/projects/pymc-marketing/badge/?version=latest)](https://docs.readthedocs.io/en/latest/)
 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 [![PyPI Version](https://img.shields.io/pypi/v/pymc-marketing.svg)](https://pypi.python.org/pypi/pymc-marketing)
 [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
 
+**Unlock the power of marketing analytics with PyMC-Marketing – the open source solution for smarter decision-making.** Media mix modeling and customer lifetime value modules allow businesses to make data-driven decisions about their marketing campaigns. Optimize your marketing strategy and unlock the full potential of your customer data.
+
+---
+
+## Installation
+
+Start by setting up an environment (e.g. `marketing_env`) with PyMC. It may look something like the following:
+
+```bash
+mamba create -c conda-forge -n marketing_env python "pymc>=5"
+mamba activate marketing_env
+```
+
+See the official [PyMC installation guide](https://www.pymc.io/projects/docs/en/latest/installation.html) if more detail is needed.
+
+Assuming you have an environment set up then install PyMC-Marketing with the following command. This will give you the latest version of the library from PyPI.
+
+```bash
+pip install pymc-marketing
+```
+
+Alternatively you can install from GitHub directly:
+
+```bash
+pip install git+https://github.com/pymc-labs/pymc-marketing.git
+```
+
 ## Bayesian Media Mix Models (MMMs) in PyMC
 
-In this package we provide an API for a Bayesian media mix model (MMM) specification following [Jin, Yuxue, et al. “Bayesian methods for media mix modeling with carryover and shape effects.” (2017).](https://research.google/pubs/pub46001/). Concretely, given a time series target variable $y_{t}$ (e.g. sales on conversions), media variiables $x_{m, t}$ (e.g. impressions, clicks or costs) and a set of control covariates $z_{c, t}$ (e.g. holidays, special events) we consider a linear model of the form
+In this package we provide an API for a Bayesian media mix model (MMM) specification following [Jin, Yuxue, et al. “Bayesian methods for media mix modeling with carryover and shape effects.” (2017).](https://research.google/pubs/pub46001/) Concretely, given a time series target variable $y_{t}$ (e.g. sales on conversions), media variables $x_{m, t}$ (e.g. impressions, clicks or costs) and a set of control covariates $z_{c, t}$ (e.g. holidays, special events) we consider a linear model of the form
 
 $$
 y_{t} = \alpha + \sum_{m=1}^{M}\beta_{m}f(x_{m, t}) +  \sum_{c=1}^{C}\gamma_{c}z_{c, t} + \varepsilon_{t},
 $$
 
 where $\alpha$ is the intercept, $f$ is a media transformation function and $\varepsilon_{t}$ is the error therm which we assume is normally distributed. The function $f$ encodes the contribution of media on the target variable. Typically we consider two types of transformation: adstock (carry-over) and saturation effects.
 
@@ -246,70 +273,42 @@
   - [Improving the Speed and Accuracy of Bayesian Media Mix Models](https://www.pymc-labs.io/blog-posts/reducing-customer-acquisition-costs-how-we-helped-optimizing-hellofreshs-marketing-budget/)
 - [Johns, Michael and Wang,  Zhenyu. "A Bayesian Approach to Media Mix Modeling"](https://www.youtube.com/watch?v=UznM_-_760Y)
 - [Orduz, Juan. "Media Effect Estimation with PyMC: Adstock, Saturation & Diminishing Returns"](https://juanitorduz.github.io/pymc_mmm/)
 
 ---
 
 ## Bayesian CLVs in PyMC
-[Customer Lifetime Value](https://en.wikipedia.org/wiki/Customer_lifetime_value) models is another important class of models. There are many different types of CLV models and it can be helpful to conceptualise them as fitting in a 2-dimensional grid as below. An excellent set of introduction slides to CLV's is provided in [Probability Models for Customer-Base Analysis](https://www.brucehardie.com/talks/ho_cba_tut_art_09.pdf) by Fader & Hardie (2009).
+[Customer Lifetime Value](https://en.wikipedia.org/wiki/Customer_lifetime_value) (CLV) models are another important class of models. There are many different types of CLV models and it can be helpful to conceptualise them as fitting in a 2-dimensional grid as below. An excellent set of introduction slides to CLV's is provided in [Probability Models for Customer-Base Analysis](https://www.brucehardie.com/talks/ho_cba_tut_art_09.pdf) by Fader & Hardie (2009).
 
 ### Examples
 
 |                | **Non-contractual** | **Contractual**                 |
 |----------------|---------------------|---------------------------------|
 | **Continuous** | Buying groceries    | Audible                         |
 | **Discrete**   | Cinema ticket       | Monthly or yearly subscriptions |
 
 To explain further:
-- **Contractual:** In contractual settings a customer has a contract which continues to be active until it is explicitly cancelled. Therefore in contractual settings, customer churn events are observed.
+- **Contractual:** In contractual settings, a customer has a contract which continues to be active until it is explicitly cancelled. Therefore, customer churn events are observed.
 
 - **Non-contractual:** In non-contractual settings, there is no ongoing contract that a customer has with a company. Instead, purchases can be ad hoc and churn events are unobserved.
 
 - **Discrete:** Here, purchases are made at discrete points in time. This obviously depends upon the timescale that we are working on, but typically a relevant time period would be a month or year. However it could be more granualar than this - think of taking the 2nd of 4 inter-city train journeys offered per day.
 
-- **Continuous:** In the continuous-time domain, purchases can be made at any point within a firms opening hours. For online ordering this could be any point within a 24 hour cycle, or purchases in physical stores could be made at any point during the trading day.
+- **Continuous:** In the continuous-time domain, purchases can be made at any point within a firms opening hours. For online ordering, this could be any point within a 24 hour cycle, or purchases in physical stores could be made at any point during the trading day.
 
-In the documentation we provide some examples on how to use the CLV API. We use the data from the [`lifetimes`](https://github.com/CamDavidsonPilon/lifetimes) package to illustrate the models.
+In the documentation, we provide some examples on how to use the CLV API. We use the data from the [`lifetimes`](https://github.com/CamDavidsonPilon/lifetimes) package to illustrate the models.
 
 - [CLV Quickstart](https://pymc-marketing.readthedocs.io/en/stable/notebooks/clv/clv_quickstart.html)
 - [BG/NBD model](https://pymc-marketing.readthedocs.io/en/stable/notebooks/clv/bg_nbd.html)
 - [Gamma-Gamma model](https://pymc-marketing.readthedocs.io/en/stable/notebooks/clv/gamma_gamma.html)
 
 ---
 
-## Local Development
+## 📞 Schedule a Consultation
+Unlock your potential with a free 30-minute strategy session with our PyMC experts. Discover how open source solutions and pymc-marketing can elevate your media-mix models and customer lifetime value analyses. Boost your career and organization by making smarter, data-driven decisions. Don't wait—[claim your complimentary session](https://calendly.com/benjamin-vincent/pymc-marketing) today and lead the way in marketing and data science innovation.
 
-1. Create conda environment. For example:
+## Using PyMC-Marketing and how PyMC Labs can help you
+PyMC-Marketing uses the [Apache 2.0 licence](LICENSE) which permits commercial use, amongst other things.
 
-```shell
-conda create -n pymc_marketing_env
-```
+If you want to build upon the package, please feel free to fork the repo and submit a pull request. If in doubt, please open an issue.
 
-2. Activate environment.
-
-```shell
-conda activate pymc_marketing_env
-```
-
-3. Install `pymc_marketing` package:
-
-```shell
-make init
-```
-
-4. To run tests:
-
-```shell
-make test
-```
-
-5. To check code style:
-
-```shell
-make check_lint
-```
-
-6. Set [pre-commit hooks](https://pre-commit.com/) (Optional):
-
-```shell
-pre-commit install
-```
+For companies that want to use PyMC-Marketing in production, [PyMC Labs](https://www.pymc-labs.io) is available for consulting and training. We can help you build and deploy your models in production. We have experience with cutting edge Bayesian modelling techniques in general, and in particular with MMMs and CLVs. For example, see our video on [Bayesian Marketing Mix Models: State of the Art and their Future](https://www.youtube.com/watch?v=xVx91prC81g).
```

### Comparing `pymc-marketing-0.0.4/pymc_marketing.egg-info/SOURCES.txt` & `pymc-marketing-0.1.0/pymc_marketing.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pymc-marketing-0.0.4/pyproject.toml` & `pymc-marketing-0.1.0/pyproject.toml`

 * *Files 7% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 maintainers = [{ name = "PyMC Labs", email = "info@pymc-labs.io" }]
 
 dependencies = [
     "arviz>=0.13.0",
     "matplotlib>=3.5.1",
     "numpy>=1.17",
     "pandas",
-    "pymc>=5.0.0",
+    "pymc>=5.1.2",
     "scikit-learn>=1.1.1",
     "seaborn>=0.12.2",
     "xarray"
 ]
 
 [project.optional-dependencies]
 docs = [
@@ -35,15 +35,16 @@
     "sphinx-notfound-page",
     "sphinx-design"
 ]
 lint = [
     "black>=22.3.0",
     "flake8>=4.0.1",
     "isort>=5.10.1",
-    "pre-commit>=2.19.0"
+    "pre-commit>=2.19.0",
+    "pylint"
 ]
 test = [
     "lifetimes==0.11.3",
     "pytest==7.0.1",
     "pytest-cov==3.0.0"
 ]
```

