# Comparing `tmp/autoplotlib-0.1.0.tar.gz` & `tmp/autoplotlib-0.1.1.tar.gz`

## Comparing `autoplotlib-0.1.0.tar` & `autoplotlib-0.1.1.tar`

### file list

```diff
@@ -1,15 +1,17 @@
--rw-r--r--   0        0        0      123 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/HISTORY.md
--rw-r--r--   0        0        0     1151 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/.github/workflows/release_pypi.yaml
--rw-r--r--   0        0        0       34 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/autoplotlib/__init__.py
--rw-r--r--   0        0        0     3846 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/autoplotlib/main.py
--rw-r--r--   0        0        0      897 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/autoplotlib/sandbox.py
--rw-r--r--   0        0        0  1102395 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/docs/autoplotlib_demo.gif
--rw-r--r--   0        0        0    43912 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/docs/autoplotlib_logo.png
--rw-r--r--   0        0        0   314183 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/notebooks/logo.ipynb
--rw-r--r--   0        0        0     1600 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/notebooks/test.ipynb
--rw-r--r--   0        0        0      516 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/tests/test_sandbox.py
--rw-r--r--   0        0        0     1838 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/.gitignore
--rw-r--r--   0        0        0     1063 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/LICENSE
--rw-r--r--   0        0        0     2271 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/README.md
--rw-r--r--   0        0        0      677 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/pyproject.toml
--rw-r--r--   0        0        0     2893 2020-02-02 00:00:00.000000 autoplotlib-0.1.0/PKG-INFO
+-rw-r--r--   0        0        0      245 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/HISTORY.md
+-rw-r--r--   0        0        0      300 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/setup.cfg
+-rw-r--r--   0        0        0     1151 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/.github/workflows/release_pypi.yaml
+-rw-r--r--   0        0        0      151 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/autoplotlib/__init__.py
+-rw-r--r--   0        0        0     3859 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/autoplotlib/main.py
+-rw-r--r--   0        0        0      897 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/autoplotlib/sandbox.py
+-rw-r--r--   0        0        0  1102395 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/docs/autoplotlib_demo.gif
+-rw-r--r--   0        0        0    43912 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/docs/autoplotlib_logo.png
+-rw-r--r--   0        0        0     1155 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/docs/dev_guide.md
+-rw-r--r--   0        0        0   314183 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/notebooks/logo.ipynb
+-rw-r--r--   0        0        0     1600 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/notebooks/test.ipynb
+-rw-r--r--   0        0        0      516 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/tests/test_sandbox.py
+-rw-r--r--   0        0        0     1838 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/.gitignore
+-rw-r--r--   0        0        0     1063 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/LICENSE
+-rw-r--r--   0        0        0     2405 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/README.md
+-rw-r--r--   0        0        0      742 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/pyproject.toml
+-rw-r--r--   0        0        0     3137 2020-02-02 00:00:00.000000 autoplotlib-0.1.1/PKG-INFO
```

### Comparing `autoplotlib-0.1.0/.github/workflows/release_pypi.yaml` & `autoplotlib-0.1.1/.github/workflows/release_pypi.yaml`

 * *Files identical despite different names*

### Comparing `autoplotlib-0.1.0/autoplotlib/main.py` & `autoplotlib-0.1.1/autoplotlib/main.py`

 * *Files 1% similar despite different names*

```diff
@@ -65,15 +65,15 @@
     except IndexError:
         raise ValueError(
             "The LLM did not return any code. "
             "Please try again (maybe with a different prompt)."
             f"LLM response: {llm_response}"
         )
 
-    safety_user_input_str = f"Code generated by LLM: \n{code} \n\nPress y and enter to confirm that the code is safe and to run the code. Press any other key and enter to abort."
+    safety_user_input_str = f"Code generated by LLM: \n{code} \n\nPress y and enter to confirm that the code is safe and to run the code. Press any other key and enter to abort. Your input: "
     if input(safety_user_input_str) != "y":
         raise ValueError("Code not confirmed as safe. Aborting.")
 
     if verbose:
         print(f"Code generated by LLM: {code}")
 
     fig = plt.figure(**fig_args)
```

### Comparing `autoplotlib-0.1.0/autoplotlib/sandbox.py` & `autoplotlib-0.1.1/autoplotlib/sandbox.py`

 * *Files identical despite different names*

### Comparing `autoplotlib-0.1.0/docs/autoplotlib_demo.gif` & `autoplotlib-0.1.1/docs/autoplotlib_demo.gif`

 * *Files identical despite different names*

### Comparing `autoplotlib-0.1.0/docs/autoplotlib_logo.png` & `autoplotlib-0.1.1/docs/autoplotlib_logo.png`

 * *Files identical despite different names*

### Comparing `autoplotlib-0.1.0/notebooks/logo.ipynb` & `autoplotlib-0.1.1/notebooks/logo.ipynb`

 * *Files identical despite different names*

### Comparing `autoplotlib-0.1.0/notebooks/test.ipynb` & `autoplotlib-0.1.1/notebooks/test.ipynb`

 * *Files identical despite different names*

### Comparing `autoplotlib-0.1.0/tests/test_sandbox.py` & `autoplotlib-0.1.1/tests/test_sandbox.py`

 * *Files identical despite different names*

### Comparing `autoplotlib-0.1.0/.gitignore` & `autoplotlib-0.1.1/.gitignore`

 * *Files identical despite different names*

### Comparing `autoplotlib-0.1.0/LICENSE` & `autoplotlib-0.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `autoplotlib-0.1.0/README.md` & `autoplotlib-0.1.1/README.md`

 * *Files 16% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 <p align="center">
-<img src="./docs/autoplotlib_logo.png" width="250" />
+<img src="https://raw.githubusercontent.com/rdnfn/autoplotlib/main/docs/autoplotlib_logo.png" width="250" />
 </p>
 
-# autoplotlib
+[![PyPI version](https://badge.fury.io/py/autoplotlib.svg)](https://pypi.org/project/autoplotlib/)
 
-*Quickly generate plots in Python by simply describing them through text.* For example, simply use the prompt "create a scatter plot with name labels" instead endlessly searching the docs and stackoverflow. Given such a prompt, the `autoplotlib` Python library uses the OpenAI API to automatically generate the corresponding code and plot - saving you time and effort.
+*Quickly generate plots in Python by simply describing them through text.* For example, simply use the prompt "create a scatter plot with name labels" instead of endlessly searching the docs and stackoverflow. Given such a prompt, the `autoplotlib` Python library uses the OpenAI API to automatically generate the corresponding code and plot - saving you time and effort.
 
 > **Warning**
 > This package is experimental. The package can execute code output from language models. Albeit unlikely, always check and confirm no malicious code was generated by the model before execution. Use at your own risk.
 
 ## Installation
 
 1. Install the Python package:
@@ -43,31 +43,19 @@
 Ensure the labels don't overlap.
 Mark people taller than 170 with a star instead of a point.
 """
 
 code, fig, llm_response = aplt.plot(figure_description, data=data)
 ```
 
-<img src="./docs/autoplotlib_demo.gif" width="690" />
+<img src="https://raw.githubusercontent.com/rdnfn/autoplotlib/main/docs/autoplotlib_demo.gif" width="690" />
 
-## Development
+## Contributing
 
-### Setup
-
-1. Fork the repository.
-
-2. Clone the repository:
-    ```
-    git clone <yourforkpath>
-    ```
-
-3. Install the package in development mode:
-    ```
-    pip install -e ".[dev]"
-    ```
+See the [development guide](https://github.com/rdnfn/autoplotlib/blob/main/docs/dev_guide.md) for information about contributing.
 
 ## Potential future features
 
 - [ ] Add sandboxing of code execution ([see here](https://stackoverflow.com/questions/3068139/how-can-i-sandbox-python-in-pure-python#3068475))
 
 ## License
```

### Comparing `autoplotlib-0.1.0/pyproject.toml` & `autoplotlib-0.1.1/pyproject.toml`

 * *Files 14% similar despite different names*

```diff
@@ -1,29 +1,31 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "autoplotlib"
-version = "0.1.0"
+version = "0.1.1"
 authors = [
   { name="rdnfn", email="info@arduin.io" },
 ]
-description = "Single-line plots from language prompt in Python."
+description = "Quickly generate plots in Python by simply describing them through text."
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
     "Programming Language :: Python :: 3",
     "License :: OSI Approved :: MIT License",
     "Operating System :: OS Independent",
 ]
 dependencies = [
     "matplotlib",
     "langchain",
+    "pandas",
+    "numpy",
 ]
 
 [project.urls]
 "Homepage" = "https://github.com/rdnfn/autoplotlib"
 "Bug Tracker" = "https://github.com/rdnfn/autoplotlib/issues"
 
 [project.optional-dependencies]
-dev = ["pytest"]
+dev = ["pytest","bump2version"]
```

### Comparing `autoplotlib-0.1.0/PKG-INFO` & `autoplotlib-0.1.1/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,32 +1,35 @@
 Metadata-Version: 2.1
 Name: autoplotlib
-Version: 0.1.0
-Summary: Single-line plots from language prompt in Python.
+Version: 0.1.1
+Summary: Quickly generate plots in Python by simply describing them through text.
 Project-URL: Homepage, https://github.com/rdnfn/autoplotlib
 Project-URL: Bug Tracker, https://github.com/rdnfn/autoplotlib/issues
 Author-email: rdnfn <info@arduin.io>
 License-File: LICENSE
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.7
 Requires-Dist: langchain
 Requires-Dist: matplotlib
+Requires-Dist: numpy
+Requires-Dist: pandas
 Provides-Extra: dev
+Requires-Dist: bump2version; extra == 'dev'
 Requires-Dist: pytest; extra == 'dev'
 Description-Content-Type: text/markdown
 
 <p align="center">
-<img src="./docs/autoplotlib_logo.png" width="250" />
+<img src="https://raw.githubusercontent.com/rdnfn/autoplotlib/main/docs/autoplotlib_logo.png" width="250" />
 </p>
 
-# autoplotlib
+[![PyPI version](https://badge.fury.io/py/autoplotlib.svg)](https://pypi.org/project/autoplotlib/)
 
-*Quickly generate plots in Python by simply describing them through text.* For example, simply use the prompt "create a scatter plot with name labels" instead endlessly searching the docs and stackoverflow. Given such a prompt, the `autoplotlib` Python library uses the OpenAI API to automatically generate the corresponding code and plot - saving you time and effort.
+*Quickly generate plots in Python by simply describing them through text.* For example, simply use the prompt "create a scatter plot with name labels" instead of endlessly searching the docs and stackoverflow. Given such a prompt, the `autoplotlib` Python library uses the OpenAI API to automatically generate the corresponding code and plot - saving you time and effort.
 
 > **Warning**
 > This package is experimental. The package can execute code output from language models. Albeit unlikely, always check and confirm no malicious code was generated by the model before execution. Use at your own risk.
 
 ## Installation
 
 1. Install the Python package:
@@ -61,31 +64,19 @@
 Ensure the labels don't overlap.
 Mark people taller than 170 with a star instead of a point.
 """
 
 code, fig, llm_response = aplt.plot(figure_description, data=data)
 ```
 
-<img src="./docs/autoplotlib_demo.gif" width="690" />
+<img src="https://raw.githubusercontent.com/rdnfn/autoplotlib/main/docs/autoplotlib_demo.gif" width="690" />
 
-## Development
+## Contributing
 
-### Setup
-
-1. Fork the repository.
-
-2. Clone the repository:
-    ```
-    git clone <yourforkpath>
-    ```
-
-3. Install the package in development mode:
-    ```
-    pip install -e ".[dev]"
-    ```
+See the [development guide](https://github.com/rdnfn/autoplotlib/blob/main/docs/dev_guide.md) for information about contributing.
 
 ## Potential future features
 
 - [ ] Add sandboxing of code execution ([see here](https://stackoverflow.com/questions/3068139/how-can-i-sandbox-python-in-pure-python#3068475))
 
 ## License
```
