# Comparing `tmp/pythonpredictions-cobra-1.1.0.tar.gz` & `tmp/pythonpredictions-cobra-1.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "C:\Users\samuel.borms\Desktop\code\cobra\dist\tmpqhkt6u7i\pythonpredictions-cobra-1.1.0.tar", last modified: Tue Oct  5 12:36:07 2021, max compression
+gzip compressed data, was "C:\Users\sander.vandenhautte\PycharmProjects\cobra\dist\.tmp-jeg98v8w\pythonpredictions-cobra-1.1.1.tar", last modified: Fri Apr  7 12:40:37 2023, max compression
```

## Comparing `pythonpredictions-cobra-1.1.0.tar` & `pythonpredictions-cobra-1.1.1.tar`

### file list

```diff
@@ -1,32 +1,32 @@
-drwxrwxrwx   0        0        0        0 2021-10-05 12:36:07.240255 pythonpredictions-cobra-1.1.0/
--rw-rw-rw-   0        0        0     1096 2021-03-22 09:56:34.000000 pythonpredictions-cobra-1.1.0/LICENSE
--rw-rw-rw-   0        0        0     5104 2021-10-05 12:36:07.238262 pythonpredictions-cobra-1.1.0/PKG-INFO
--rw-rw-rw-   0        0        0     4680 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/README.rst
-drwxrwxrwx   0        0        0        0 2021-10-05 12:36:07.191727 pythonpredictions-cobra-1.1.0/cobra/
--rw-rw-rw-   0        0        0       32 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/__init__.py
-drwxrwxrwx   0        0        0        0 2021-10-05 12:36:07.201958 pythonpredictions-cobra-1.1.0/cobra/evaluation/
--rw-rw-rw-   0        0        0      806 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/evaluation/__init__.py
--rw-rw-rw-   0        0        0    25720 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/evaluation/evaluator.py
--rw-rw-rw-   0        0        0    10369 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/evaluation/pigs_tables.py
--rw-rw-rw-   0        0        0     7024 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/evaluation/plotting_utils.py
-drwxrwxrwx   0        0        0        0 2021-10-05 12:36:07.213035 pythonpredictions-cobra-1.1.0/cobra/model_building/
--rw-rw-rw-   0        0        0      553 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/model_building/__init__.py
--rw-rw-rw-   0        0        0    14693 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/model_building/forward_selection.py
--rw-rw-rw-   0        0        0    15917 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/model_building/models.py
--rw-rw-rw-   0        0        0     7870 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/model_building/univariate_selection.py
-drwxrwxrwx   0        0        0        0 2021-10-05 12:36:07.226325 pythonpredictions-cobra-1.1.0/cobra/preprocessing/
--rw-rw-rw-   0        0        0      329 2021-03-22 09:56:34.000000 pythonpredictions-cobra-1.1.0/cobra/preprocessing/__init__.py
--rw-rw-rw-   0        0        0    19100 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/preprocessing/categorical_data_processor.py
--rw-rw-rw-   0        0        0    20502 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/preprocessing/kbins_discretizer.py
--rw-rw-rw-   0        0        0    19417 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/preprocessing/preprocessor.py
--rw-rw-rw-   0        0        0    12954 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/preprocessing/target_encoder.py
--rw-rw-rw-   0        0        0      361 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/utils.py
--rw-rw-rw-   0        0        0       21 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/cobra/version.py
-drwxrwxrwx   0        0        0        0 2021-10-05 12:36:07.237311 pythonpredictions-cobra-1.1.0/pythonpredictions_cobra.egg-info/
--rw-rw-rw-   0        0        0     5104 2021-10-05 12:36:07.000000 pythonpredictions-cobra-1.1.0/pythonpredictions_cobra.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      785 2021-10-05 12:36:07.000000 pythonpredictions-cobra-1.1.0/pythonpredictions_cobra.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2021-10-05 12:36:07.000000 pythonpredictions-cobra-1.1.0/pythonpredictions_cobra.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      109 2021-10-05 12:36:07.000000 pythonpredictions-cobra-1.1.0/pythonpredictions_cobra.egg-info/requires.txt
--rw-rw-rw-   0        0        0        6 2021-10-05 12:36:07.000000 pythonpredictions-cobra-1.1.0/pythonpredictions_cobra.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2021-10-05 12:36:07.240400 pythonpredictions-cobra-1.1.0/setup.cfg
--rw-rw-rw-   0        0        0     1033 2021-10-05 12:27:37.000000 pythonpredictions-cobra-1.1.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:40:37.755214 pythonpredictions-cobra-1.1.1/
+-rw-rw-rw-   0        0        0     1096 2021-03-12 14:39:56.000000 pythonpredictions-cobra-1.1.1/LICENSE
+-rw-rw-rw-   0        0        0     4916 2023-04-07 12:40:37.755214 pythonpredictions-cobra-1.1.1/PKG-INFO
+-rw-rw-rw-   0        0        0     4515 2023-04-07 08:28:57.000000 pythonpredictions-cobra-1.1.1/README.rst
+drwxrwxrwx   0        0        0        0 2023-04-07 12:40:37.551122 pythonpredictions-cobra-1.1.1/cobra/
+-rw-rw-rw-   0        0        0      171 2023-04-07 08:28:57.000000 pythonpredictions-cobra-1.1.1/cobra/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:40:37.588473 pythonpredictions-cobra-1.1.1/cobra/evaluation/
+-rw-rw-rw-   0        0        0      806 2021-09-24 12:58:18.000000 pythonpredictions-cobra-1.1.1/cobra/evaluation/__init__.py
+-rw-rw-rw-   0        0        0    25978 2023-04-07 08:28:57.000000 pythonpredictions-cobra-1.1.1/cobra/evaluation/evaluator.py
+-rw-rw-rw-   0        0        0    10435 2023-04-07 08:28:57.000000 pythonpredictions-cobra-1.1.1/cobra/evaluation/pigs_tables.py
+-rw-rw-rw-   0        0        0     7297 2023-04-07 08:28:57.000000 pythonpredictions-cobra-1.1.1/cobra/evaluation/plotting_utils.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:40:37.646564 pythonpredictions-cobra-1.1.1/cobra/model_building/
+-rw-rw-rw-   0        0        0      553 2021-09-02 19:53:03.000000 pythonpredictions-cobra-1.1.1/cobra/model_building/__init__.py
+-rw-rw-rw-   0        0        0    14693 2022-06-02 09:31:10.000000 pythonpredictions-cobra-1.1.1/cobra/model_building/forward_selection.py
+-rw-rw-rw-   0        0        0    15892 2023-04-07 08:33:37.000000 pythonpredictions-cobra-1.1.1/cobra/model_building/models.py
+-rw-rw-rw-   0        0        0     7870 2021-10-01 15:36:49.000000 pythonpredictions-cobra-1.1.1/cobra/model_building/univariate_selection.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:40:37.715224 pythonpredictions-cobra-1.1.1/cobra/preprocessing/
+-rw-rw-rw-   0        0        0      329 2021-03-12 14:39:56.000000 pythonpredictions-cobra-1.1.1/cobra/preprocessing/__init__.py
+-rw-rw-rw-   0        0        0    19100 2022-04-01 13:16:31.000000 pythonpredictions-cobra-1.1.1/cobra/preprocessing/categorical_data_processor.py
+-rw-rw-rw-   0        0        0    20502 2021-09-30 16:33:57.000000 pythonpredictions-cobra-1.1.1/cobra/preprocessing/kbins_discretizer.py
+-rw-rw-rw-   0        0        0    24082 2023-04-07 08:28:57.000000 pythonpredictions-cobra-1.1.1/cobra/preprocessing/preprocessor.py
+-rw-rw-rw-   0        0        0    12954 2023-04-07 08:27:26.000000 pythonpredictions-cobra-1.1.1/cobra/preprocessing/target_encoder.py
+-rw-rw-rw-   0        0        0      742 2023-04-07 08:28:57.000000 pythonpredictions-cobra-1.1.1/cobra/utils.py
+-rw-rw-rw-   0        0        0       21 2023-04-07 08:28:57.000000 pythonpredictions-cobra-1.1.1/cobra/version.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:40:37.755214 pythonpredictions-cobra-1.1.1/pythonpredictions_cobra.egg-info/
+-rw-rw-rw-   0        0        0     4916 2023-04-07 12:40:37.000000 pythonpredictions-cobra-1.1.1/pythonpredictions_cobra.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      785 2023-04-07 12:40:37.000000 pythonpredictions-cobra-1.1.1/pythonpredictions_cobra.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 12:40:37.000000 pythonpredictions-cobra-1.1.1/pythonpredictions_cobra.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      114 2023-04-07 12:40:37.000000 pythonpredictions-cobra-1.1.1/pythonpredictions_cobra.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        6 2023-04-07 12:40:37.000000 pythonpredictions-cobra-1.1.1/pythonpredictions_cobra.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 12:40:37.755214 pythonpredictions-cobra-1.1.1/setup.cfg
+-rw-rw-rw-   0        0        0     1059 2023-04-07 12:31:32.000000 pythonpredictions-cobra-1.1.1/setup.py
```

### Comparing `pythonpredictions-cobra-1.1.0/LICENSE` & `pythonpredictions-cobra-1.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `pythonpredictions-cobra-1.1.0/PKG-INFO` & `pythonpredictions-cobra-1.1.1/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,16 +1,15 @@
 Metadata-Version: 2.1
 Name: pythonpredictions-cobra
-Version: 1.1.0
+Version: 1.1.1
 Summary: A Python package to build predictive linear and logistic regression models focused on performance and interpretation.
 Home-page: https://github.com/PythonPredictions/cobra
 Author: Python Predictions
 Author-email: cobra@pythonpredictions.com
 License: MIT
-Platform: UNKNOWN
 Description-Content-Type: text/x-rst
 License-File: LICENSE
 
 
 .. image:: https://github.com/PythonPredictions/cobra/raw/master/material/logo.png
     :width: 700
 
@@ -50,15 +49,15 @@
 ------------
 
 This package requires only the usual Python libraries for data science, being numpy, pandas, scipy, scikit-learn, matplotlib, seaborn, and tqdm. These packages, along with their versions are listed in ``requirements.txt`` and can be installed using ``pip``:    ::
 
   pip install -r requirements.txt
 
 
-**Note**: if you want to install Cobra with e.g. pip, you don't have to install all of these requirements as these are automatically installed with Cobra itself.
+**Note**: if you want to install Cobra with e.g. pip, you don't have to install all these requirements as these are automatically installed with Cobra itself.
 
 Installation
 ------------
 
 The easiest way to install Cobra is using ``pip``:    ::
 
   pip install -U pythonpredictions-cobra
@@ -69,22 +68,18 @@
 
 - A `blog post <https://www.pythonpredictions.com/news/the-little-trick-we-apply-to-obtain-explainability-by-design/>`_ on the overall methodology.
 
 - A `research article <https://doi.org/10.1016/j.dss.2016.11.007>`_ by Geert Verstraeten (co-founder Python Predictions) discussing the preprocessing approach we use in Cobra.
 
 - HTML documentation of the `individual modules <https://pythonpredictions.github.io/cobra.io/docstring/modules.html>`_.
 
-- A step-by-step `tutorial <https://pythonpredictions.github.io/cobra/tutorials/tutorial_Cobra_logistic_regression.ipynb>`_ for **logistic regression**.
-
-- A step-by-step `tutorial <https://pythonpredictions.github.io/cobra/tutorials/tutorial_Cobra_linear_regression.ipynb>`__ for **linear regression**.
+- Step-by-step `tutorials <https://github.com/PythonPredictions/cobra/blob/master/tutorials>`_ for a logistic and a linear regression use case.
 
 - Check out the Data Science Leuven Meetup `talk <https://www.youtube.com/watch?v=w7ceZZqMEaA&feature=youtu.be>`_ by one of the core developers (second presentation). His `slides <https://github.com/PythonPredictions/Cobra-DS-meetup-Leuven/blob/main/DS_Leuven_meetup_20210209_cobra.pdf>`_ and `related material <https://github.com/PythonPredictions/Cobra-DS-meetup-Leuven>`_ are also available.
 
 Contributing to Cobra
 =====================
 
 We'd love you to contribute to the development of Cobra! There are many ways in which you can contribute, the most common of which is to contribute to the source code or documentation of the project. However, there are many other ways you can contribute (report issues, improve code coverage by adding unit tests, ...).
 We use GitHub issues to track all bugs and feature requests. Feel free to open an issue in case you found a bug or in case you wish to see a new feature added.
 
 For more details, check out our `wiki <https://github.com/PythonPredictions/cobra/wiki/Contributing-guidelines-&-workflows>`_.
-
-
```

### Comparing `pythonpredictions-cobra-1.1.0/README.rst` & `pythonpredictions-cobra-1.1.1/README.rst`

 * *Files 6% similar despite different names*

```diff
@@ -38,15 +38,15 @@
 ------------
 
 This package requires only the usual Python libraries for data science, being numpy, pandas, scipy, scikit-learn, matplotlib, seaborn, and tqdm. These packages, along with their versions are listed in ``requirements.txt`` and can be installed using ``pip``:    ::
 
   pip install -r requirements.txt
 
 
-**Note**: if you want to install Cobra with e.g. pip, you don't have to install all of these requirements as these are automatically installed with Cobra itself.
+**Note**: if you want to install Cobra with e.g. pip, you don't have to install all these requirements as these are automatically installed with Cobra itself.
 
 Installation
 ------------
 
 The easiest way to install Cobra is using ``pip``:    ::
 
   pip install -U pythonpredictions-cobra
@@ -57,17 +57,15 @@
 
 - A `blog post <https://www.pythonpredictions.com/news/the-little-trick-we-apply-to-obtain-explainability-by-design/>`_ on the overall methodology.
 
 - A `research article <https://doi.org/10.1016/j.dss.2016.11.007>`_ by Geert Verstraeten (co-founder Python Predictions) discussing the preprocessing approach we use in Cobra.
 
 - HTML documentation of the `individual modules <https://pythonpredictions.github.io/cobra.io/docstring/modules.html>`_.
 
-- A step-by-step `tutorial <https://pythonpredictions.github.io/cobra/tutorials/tutorial_Cobra_logistic_regression.ipynb>`_ for **logistic regression**.
-
-- A step-by-step `tutorial <https://pythonpredictions.github.io/cobra/tutorials/tutorial_Cobra_linear_regression.ipynb>`__ for **linear regression**.
+- Step-by-step `tutorials <https://github.com/PythonPredictions/cobra/blob/master/tutorials>`_ for a logistic and a linear regression use case.
 
 - Check out the Data Science Leuven Meetup `talk <https://www.youtube.com/watch?v=w7ceZZqMEaA&feature=youtu.be>`_ by one of the core developers (second presentation). His `slides <https://github.com/PythonPredictions/Cobra-DS-meetup-Leuven/blob/main/DS_Leuven_meetup_20210209_cobra.pdf>`_ and `related material <https://github.com/PythonPredictions/Cobra-DS-meetup-Leuven>`_ are also available.
 
 Contributing to Cobra
 =====================
 
 We'd love you to contribute to the development of Cobra! There are many ways in which you can contribute, the most common of which is to contribute to the source code or documentation of the project. However, there are many other ways you can contribute (report issues, improve code coverage by adding unit tests, ...).
```

### Comparing `pythonpredictions-cobra-1.1.0/cobra/evaluation/__init__.py` & `pythonpredictions-cobra-1.1.1/cobra/evaluation/__init__.py`

 * *Files identical despite different names*

### Comparing `pythonpredictions-cobra-1.1.0/cobra/evaluation/evaluator.py` & `pythonpredictions-cobra-1.1.1/cobra/evaluation/evaluator.py`

 * *Files 4% similar despite different names*

```diff
@@ -183,20 +183,22 @@
 
             ax.plot(self.roc_curve["fpr"],
                     self.roc_curve["tpr"],
                     color="cornflowerblue", linewidth=3,
                     label="ROC curve (area = {s:.3})".format(s=auc))
 
             ax.plot([0, 1], [0, 1], color="darkorange", linewidth=3,
-                    linestyle="--")
-            ax.set_xlabel("False Positive Rate", fontsize=15)
-            ax.set_ylabel("True Positive Rate", fontsize=15)
+                    linestyle="--", label="random selection")
+            ax.set_xlabel("False positive rate", fontsize=15)
+            ax.set_ylabel("True positive rate", fontsize=15)
             ax.legend(loc="lower right")
             ax.set_title("ROC curve", fontsize=20)
 
+            ax.set_ylim([0, 1])
+
             if path:
                 plt.savefig(path, format="png", dpi=300, bbox_inches="tight")
 
         plt.show()
 
     def plot_confusion_matrix(self, path: str=None, dim: tuple=(12, 8),
                               labels: list=["0", "1"]):
@@ -220,14 +222,16 @@
 
         fig, ax = plt.subplots(figsize=dim)
         ax = sns.heatmap(self.confusion_matrix,
                          annot=self.confusion_matrix.astype(str),
                          fmt="s", cmap="Blues",
                          xticklabels=labels, yticklabels=labels)
         ax.set_title("Confusion matrix", fontsize=20)
+        plt.ylabel('True labels', fontsize=15)
+        plt.xlabel('Predicted labels', fontsize=15)
 
         if path:
             plt.savefig(path, format="png", dpi=300, bbox_inches="tight")
 
         plt.show()
 
     def plot_cumulative_response_curve(self, path: str=None, dim: tuple=(12, 8)):
@@ -252,21 +256,21 @@
         lifts = np.array(lifts)*inc_rate*100
 
         with plt.style.context("seaborn-ticks"):
             fig, ax = plt.subplots(figsize=dim)
 
             plt.bar(x_labels[::-1], lifts, align="center",
                     color="cornflowerblue")
-            plt.ylabel("response (%)", fontsize=16)
-            plt.xlabel("decile", fontsize=16)
+            plt.ylabel("Response (%)", fontsize=15)
+            plt.xlabel("Decile", fontsize=15)
             ax.set_xticks(x_labels)
             ax.set_xticklabels(x_labels)
 
             plt.axhline(y=inc_rate*100, color="darkorange", linestyle="--",
-                        xmin=0.05, xmax=0.95, linewidth=3, label="Incidence")
+                        xmin=0.05, xmax=0.95, linewidth=3, label="incidence")
 
             # Legend
             ax.legend(loc="upper right")
 
             # Set Axis - make them pretty
             sns.despine(ax=ax, right=True, left=True)
 
@@ -301,21 +305,21 @@
         x_labels, lifts, _ = self.lift_curve
 
         with plt.style.context("seaborn-ticks"):
             fig, ax = plt.subplots(figsize=dim)
 
             plt.bar(x_labels[::-1], lifts, align="center",
                     color="cornflowerblue")
-            plt.ylabel("lift", fontsize=16)
-            plt.xlabel("decile", fontsize=16)
+            plt.ylabel("Lift", fontsize=15)
+            plt.xlabel("Decile", fontsize=15)
             ax.set_xticks(x_labels)
             ax.set_xticklabels(x_labels)
 
             plt.axhline(y=1, color="darkorange", linestyle="--",
-                        xmin=0.05, xmax=0.95, linewidth=3, label="Baseline")
+                        xmin=0.05, xmax=0.95, linewidth=3, label="baseline")
 
             # Legend
             ax.legend(loc="upper right")
 
             # Set Axis - make them pretty
             sns.despine(ax=ax, right=True, left=True)
 
@@ -350,15 +354,17 @@
             ax.plot(ax.get_xlim(), ax.get_ylim(), linewidth=3,
                     ls="--", color="darkorange", label="random selection")
 
             ax.set_title("Cumulative Gains curve", fontsize=20)
 
             # Format axes
             ax.set_xlim([0, 100])
-            ax.set_ylim([0, 105])
+            ax.set_ylim([0, 100])
+            plt.ylabel("Gain", fontsize=15)
+            plt.xlabel("Percentage", fontsize=15)
 
             # Format ticks
             ticks_loc_y = ax.get_yticks().tolist()
             ax.yaxis.set_major_locator(mticker.FixedLocator(ticks_loc_y))
             ax.set_yticklabels(["{:3.0f}%".format(x) for x in ticks_loc_y])
 
             ticks_loc_x = ax.get_xticks().tolist()
```

### Comparing `pythonpredictions-cobra-1.1.0/cobra/evaluation/pigs_tables.py` & `pythonpredictions-cobra-1.1.1/cobra/evaluation/pigs_tables.py`

 * *Files 7% similar despite different names*

```diff
@@ -9,641 +9,645 @@
 00000080: 2046 756e 6346 6f72 6d61 7474 6572 0d0a   FuncFormatter..
 00000090: 0d0a 696d 706f 7274 2063 6f62 7261 2e75  ..import cobra.u
 000000a0: 7469 6c73 2061 7320 7574 696c 730d 0a0d  tils as utils...
 000000b0: 0a64 6566 2067 656e 6572 6174 655f 7069  .def generate_pi
 000000c0: 675f 7461 626c 6573 2862 6173 6574 6162  g_tables(basetab
 000000d0: 6c65 3a20 7064 2e44 6174 6146 7261 6d65  le: pd.DataFrame
 000000e0: 2c0d 0a20 2020 2020 2020 2020 2020 2020  ,..             
-000000f0: 2020 2020 2020 2020 2020 2069 645f 636f             id_co
-00000100: 6c75 6d6e 5f6e 616d 653a 2073 7472 2c0d  lumn_name: str,.
-00000110: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00000120: 2020 2020 2020 2020 2074 6172 6765 745f           target_
-00000130: 636f 6c75 6d6e 5f6e 616d 653a 2073 7472  column_name: str
-00000140: 2c0d 0a20 2020 2020 2020 2020 2020 2020  ,..             
-00000150: 2020 2020 2020 2020 2020 2070 7265 7072             prepr
-00000160: 6f63 6573 7365 645f 7072 6564 6963 746f  ocessed_predicto
-00000170: 7273 3a20 6c69 7374 2920 2d3e 2070 642e  rs: list) -> pd.
-00000180: 4461 7461 4672 616d 653a 0d0a 2020 2020  DataFrame:..    
-00000190: 2222 2243 6f6d 7075 7465 2050 4947 2074  """Compute PIG t
-000001a0: 6162 6c65 7320 666f 7220 616c 6c20 7072  ables for all pr
-000001b0: 6564 6963 746f 7273 2069 6e20 7072 6570  edictors in prep
-000001c0: 726f 6365 7373 6564 5f70 7265 6469 6374  rocessed_predict
-000001d0: 6f72 732e 0d0a 0d0a 2020 2020 5468 6520  ors.....    The 
-000001e0: 6f75 7470 7574 2069 7320 6120 4461 7461  output is a Data
-000001f0: 4672 616d 6520 7769 7468 2063 6f6c 756d  Frame with colum
-00000200: 6e73 2060 6076 6172 6961 626c 6560 602c  ns ``variable``,
-00000210: 2060 606c 6162 656c 6060 2c0d 0a20 2020   ``label``,..   
-00000220: 2060 6070 6f70 5f73 697a 6560 602c 2060   ``pop_size``, `
-00000230: 6067 6c6f 6261 6c5f 6176 675f 7461 7267  `global_avg_targ
-00000240: 6574 6060 2061 6e64 2060 6061 7667 5f74  et`` and ``avg_t
-00000250: 6172 6765 7460 602e 0d0a 0d0a 2020 2020  arget``.....    
-00000260: 5061 7261 6d65 7465 7273 0d0a 2020 2020  Parameters..    
-00000270: 2d2d 2d2d 2d2d 2d2d 2d2d 0d0a 2020 2020  ----------..    
-00000280: 6261 7365 7461 626c 6520 3a20 7064 2e44  basetable : pd.D
-00000290: 6174 6146 7261 6d65 0d0a 2020 2020 2020  ataFrame..      
-000002a0: 2020 4261 7365 7461 626c 6520 746f 2063    Basetable to c
-000002b0: 6f6d 7075 7465 2050 4947 2074 6162 6c65  ompute PIG table
-000002c0: 7320 6672 6f6d 2e0d 0a20 2020 2069 645f  s from...    id_
-000002d0: 636f 6c75 6d6e 5f6e 616d 6520 3a20 7374  column_name : st
-000002e0: 720d 0a20 2020 2020 2020 204e 616d 6520  r..        Name 
-000002f0: 6f66 2074 6865 2062 6173 6574 6162 6c65  of the basetable
-00000300: 2063 6f6c 756d 6e20 636f 6e74 6169 6e69   column containi
-00000310: 6e67 2074 6865 2049 4473 206f 6620 7468  ng the IDs of th
-00000320: 6520 6261 7365 7461 626c 6520 726f 7773  e basetable rows
-00000330: 0d0a 2020 2020 2020 2020 2865 2e67 2e20  ..        (e.g. 
-00000340: 6375 7374 6f6d 6572 6e75 6d62 6572 292e  customernumber).
-00000350: 0d0a 2020 2020 7461 7267 6574 5f63 6f6c  ..    target_col
-00000360: 756d 6e5f 6e61 6d65 203a 2073 7472 0d0a  umn_name : str..
-00000370: 2020 2020 2020 2020 4e61 6d65 206f 6620          Name of 
-00000380: 7468 6520 6261 7365 7461 626c 6520 636f  the basetable co
-00000390: 6c75 6d6e 2063 6f6e 7461 696e 696e 6720  lumn containing 
-000003a0: 7468 6520 7461 7267 6574 2076 616c 7565  the target value
-000003b0: 7320 746f 2070 7265 6469 6374 2e0d 0a20  s to predict... 
-000003c0: 2020 2070 7265 7072 6f63 6573 7365 645f     preprocessed_
-000003d0: 7072 6564 6963 746f 7273 3a20 6c69 7374  predictors: list
-000003e0: 0d0a 2020 2020 2020 2020 4c69 7374 206f  ..        List o
-000003f0: 6620 6261 7365 7461 626c 6520 636f 6c75  f basetable colu
-00000400: 6d6e 206e 616d 6573 2063 6f6e 7461 696e  mn names contain
-00000410: 696e 6720 7072 6570 726f 6365 7373 6564  ing preprocessed
-00000420: 2070 7265 6469 6374 6f72 732e 0d0a 0d0a   predictors.....
-00000430: 2020 2020 5265 7475 726e 730d 0a20 2020      Returns..   
-00000440: 202d 2d2d 2d2d 2d2d 0d0a 2020 2020 7064   -------..    pd
-00000450: 2e44 6174 6146 7261 6d65 0d0a 2020 2020  .DataFrame..    
-00000460: 2020 2020 4461 7461 4672 616d 6520 636f      DataFrame co
-00000470: 6e74 6169 6e69 6e67 2061 2050 4947 2074  ntaining a PIG t
-00000480: 6162 6c65 2066 6f72 2061 6c6c 2070 7265  able for all pre
-00000490: 6469 6374 6f72 732e 0d0a 2020 2020 2222  dictors...    ""
-000004a0: 220d 0a20 2020 2070 6967 7320 3d20 5b0d  "..    pigs = [.
-000004b0: 0a20 2020 2020 2020 2063 6f6d 7075 7465  .        compute
-000004c0: 5f70 6967 5f74 6162 6c65 2862 6173 6574  _pig_table(baset
-000004d0: 6162 6c65 2c0d 0a20 2020 2020 2020 2020  able,..         
-000004e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000004f0: 2063 6f6c 756d 6e5f 6e61 6d65 2c0d 0a20   column_name,.. 
-00000500: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000510: 2020 2020 2020 2020 2074 6172 6765 745f           target_
-00000520: 636f 6c75 6d6e 5f6e 616d 652c 0d0a 2020  column_name,..  
-00000530: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00000540: 2020 2020 2020 2020 6964 5f63 6f6c 756d          id_colum
-00000550: 6e5f 6e61 6d65 290d 0a20 2020 2020 2020  n_name)..       
-00000560: 2066 6f72 2063 6f6c 756d 6e5f 6e61 6d65   for column_name
-00000570: 2069 6e20 736f 7274 6564 2870 7265 7072   in sorted(prepr
-00000580: 6f63 6573 7365 645f 7072 6564 6963 746f  ocessed_predicto
-00000590: 7273 290d 0a20 2020 2020 2020 2069 6620  rs)..        if 
-000005a0: 636f 6c75 6d6e 5f6e 616d 6520 6e6f 7420  column_name not 
-000005b0: 696e 205b 6964 5f63 6f6c 756d 6e5f 6e61  in [id_column_na
-000005c0: 6d65 2c20 7461 7267 6574 5f63 6f6c 756d  me, target_colum
-000005d0: 6e5f 6e61 6d65 5d0d 0a20 2020 205d 0d0a  n_name]..    ]..
-000005e0: 2020 2020 6f75 7470 7574 203d 2070 642e      output = pd.
-000005f0: 636f 6e63 6174 2870 6967 7329 0d0a 2020  concat(pigs)..  
-00000600: 2020 7265 7475 726e 206f 7574 7075 740d    return output.
-00000610: 0a0d 0a0d 0a64 6566 2063 6f6d 7075 7465  .....def compute
-00000620: 5f70 6967 5f74 6162 6c65 2862 6173 6574  _pig_table(baset
-00000630: 6162 6c65 3a20 7064 2e44 6174 6146 7261  able: pd.DataFra
-00000640: 6d65 2c0d 0a20 2020 2020 2020 2020 2020  me,..           
-00000650: 2020 2020 2020 2020 2020 2070 7265 6469             predi
-00000660: 6374 6f72 5f63 6f6c 756d 6e5f 6e61 6d65  ctor_column_name
-00000670: 3a20 7374 722c 0d0a 2020 2020 2020 2020  : str,..        
-00000680: 2020 2020 2020 2020 2020 2020 2020 7461                ta
-00000690: 7267 6574 5f63 6f6c 756d 6e5f 6e61 6d65  rget_column_name
-000006a0: 3a20 7374 722c 0d0a 2020 2020 2020 2020  : str,..        
-000006b0: 2020 2020 2020 2020 2020 2020 2020 6964                id
-000006c0: 5f63 6f6c 756d 6e5f 6e61 6d65 3a20 7374  _column_name: st
-000006d0: 7229 202d 3e20 7064 2e44 6174 6146 7261  r) -> pd.DataFra
-000006e0: 6d65 3a0d 0a20 2020 2022 2222 436f 6d70  me:..    """Comp
-000006f0: 7574 6520 7468 6520 5049 4720 7461 626c  ute the PIG tabl
-00000700: 6520 6f66 2061 2067 6976 656e 2070 7265  e of a given pre
-00000710: 6469 6374 6f72 2066 6f72 2061 2067 6976  dictor for a giv
-00000720: 656e 2074 6172 6765 742e 0d0a 0d0a 2020  en target.....  
-00000730: 2020 5061 7261 6d65 7465 7273 0d0a 2020    Parameters..  
-00000740: 2020 2d2d 2d2d 2d2d 2d2d 2d2d 0d0a 2020    ----------..  
-00000750: 2020 6261 7365 7461 626c 6520 3a20 7064    basetable : pd
-00000760: 2e44 6174 6146 7261 6d65 0d0a 2020 2020  .DataFrame..    
-00000770: 2020 2020 496e 7075 7420 6461 7461 2066      Input data f
-00000780: 726f 6d20 7768 6963 6820 746f 2063 6f6d  rom which to com
-00000790: 7075 7465 2074 6865 2070 6967 2074 6162  pute the pig tab
-000007a0: 6c65 2e0d 0a20 2020 2070 7265 6469 6374  le...    predict
-000007b0: 6f72 5f63 6f6c 756d 6e5f 6e61 6d65 203a  or_column_name :
-000007c0: 2073 7472 0d0a 2020 2020 2020 2020 5072   str..        Pr
-000007d0: 6564 6963 746f 7220 6e61 6d65 206f 6620  edictor name of 
-000007e0: 7768 6963 6820 746f 2063 6f6d 7075 7465  which to compute
-000007f0: 2074 6865 2070 6967 2074 6162 6c65 2e0d   the pig table..
-00000800: 0a20 2020 2074 6172 6765 745f 636f 6c75  .    target_colu
-00000810: 6d6e 5f6e 616d 6520 3a20 7374 720d 0a20  mn_name : str.. 
-00000820: 2020 2020 2020 204e 616d 6520 6f66 2074         Name of t
-00000830: 6865 2074 6172 6765 7420 7661 7269 6162  he target variab
-00000840: 6c65 2e0d 0a20 2020 2069 645f 636f 6c75  le...    id_colu
-00000850: 6d6e 5f6e 616d 6520 3a20 7374 720d 0a20  mn_name : str.. 
-00000860: 2020 2020 2020 204e 616d 6520 6f66 2074         Name of t
-00000870: 6865 2069 6420 636f 6c75 6d6e 2028 7573  he id column (us
-00000880: 6564 2074 6f20 636f 756e 7420 706f 7075  ed to count popu
-00000890: 6c61 7469 6f6e 2073 697a 6529 2e0d 0a0d  lation size)....
-000008a0: 0a20 2020 2052 6574 7572 6e73 0d0a 2020  .    Returns..  
-000008b0: 2020 2d2d 2d2d 2d2d 2d0d 0a20 2020 2070    -------..    p
-000008c0: 642e 4461 7461 4672 616d 650d 0a20 2020  d.DataFrame..   
-000008d0: 2020 2020 2050 4947 2074 6162 6c65 2061       PIG table a
-000008e0: 7320 6120 4461 7461 4672 616d 650d 0a20  s a DataFrame.. 
-000008f0: 2020 2022 2222 0d0a 2020 2020 676c 6f62     """..    glob
-00000900: 616c 5f61 7667 5f74 6172 6765 7420 3d20  al_avg_target = 
-00000910: 6261 7365 7461 626c 655b 7461 7267 6574  basetable[target
-00000920: 5f63 6f6c 756d 6e5f 6e61 6d65 5d2e 6d65  _column_name].me
-00000930: 616e 2829 0d0a 0d0a 2020 2020 2320 6772  an()....    # gr
-00000940: 6f75 7020 6279 2074 6865 2062 696e 6e65  oup by the binne
-00000950: 6420 7661 7269 6162 6c65 2c20 636f 6d70  d variable, comp
-00000960: 7574 6520 7468 6520 696e 6369 6465 6e63  ute the incidenc
-00000970: 650d 0a20 2020 2023 2028 3d6d 6561 6e20  e..    # (=mean 
-00000980: 6f66 2074 6865 2074 6172 6765 7420 666f  of the target fo
-00000990: 7220 7468 6520 6769 7665 6e20 6269 6e29  r the given bin)
-000009a0: 2061 6e64 2063 6f6d 7075 7465 2074 6865   and compute the
-000009b0: 2062 696e 2073 697a 650d 0a20 2020 2023   bin size..    #
-000009c0: 2028 652e 672e 2043 4f55 4e54 2869 645f   (e.g. COUNT(id_
-000009d0: 636f 6c75 6d6e 5f6e 616d 6529 292e 2041  column_name)). A
-000009e0: 6674 6572 2074 6861 742c 2072 656e 616d  fter that, renam
-000009f0: 6520 7468 6520 636f 6c75 6d6e 730d 0a20  e the columns.. 
-00000a00: 2020 2072 6573 203d 2028 6261 7365 7461     res = (baseta
-00000a10: 626c 652e 6772 6f75 7062 7928 7072 6564  ble.groupby(pred
-00000a20: 6963 746f 725f 636f 6c75 6d6e 5f6e 616d  ictor_column_nam
-00000a30: 6529 0d0a 2020 2020 2020 2020 2020 202e  e)..           .
-00000a40: 6167 6728 7b74 6172 6765 745f 636f 6c75  agg({target_colu
-00000a50: 6d6e 5f6e 616d 653a 2022 6d65 616e 222c  mn_name: "mean",
-00000a60: 2069 645f 636f 6c75 6d6e 5f6e 616d 653a   id_column_name:
-00000a70: 2022 7369 7a65 227d 290d 0a20 2020 2020   "size"})..     
-00000a80: 2020 2020 2020 2e72 6573 6574 5f69 6e64        .reset_ind
-00000a90: 6578 2829 0d0a 2020 2020 2020 2020 2020  ex()..          
-00000aa0: 202e 7265 6e61 6d65 2863 6f6c 756d 6e73   .rename(columns
-00000ab0: 3d7b 7072 6564 6963 746f 725f 636f 6c75  ={predictor_colu
-00000ac0: 6d6e 5f6e 616d 653a 2022 6c61 6265 6c22  mn_name: "label"
-00000ad0: 2c0d 0a20 2020 2020 2020 2020 2020 2020  ,..             
-00000ae0: 2020 2020 2020 2020 2020 2020 2020 2074                 t
-00000af0: 6172 6765 745f 636f 6c75 6d6e 5f6e 616d  arget_column_nam
-00000b00: 653a 2022 6176 675f 7461 7267 6574 222c  e: "avg_target",
-00000b10: 0d0a 2020 2020 2020 2020 2020 2020 2020  ..              
-00000b20: 2020 2020 2020 2020 2020 2020 2020 6964                id
-00000b30: 5f63 6f6c 756d 6e5f 6e61 6d65 3a20 2270  _column_name: "p
-00000b40: 6f70 5f73 697a 6522 7d29 290d 0a0d 0a20  op_size"})).... 
-00000b50: 2020 2023 2061 6464 2074 6865 2063 6f6c     # add the col
-00000b60: 756d 6e20 6e61 6d65 2074 6f20 6120 7661  umn name to a va
-00000b70: 7269 6162 6c65 2063 6f6c 756d 6e0d 0a20  riable column.. 
-00000b80: 2020 2023 2061 6464 2074 6865 2061 7665     # add the ave
-00000b90: 7261 6765 2069 6e63 6964 656e 6365 0d0a  rage incidence..
-00000ba0: 2020 2020 2320 7265 706c 6163 6520 706f      # replace po
-00000bb0: 7075 6c61 7469 6f6e 2073 697a 6520 6279  pulation size by
-00000bc0: 2061 2070 6572 6365 6e74 6167 6520 6f66   a percentage of
-00000bd0: 2074 6f74 616c 2070 6f70 756c 6174 696f   total populatio
-00000be0: 6e0d 0a20 2020 2072 6573 5b22 7661 7269  n..    res["vari
-00000bf0: 6162 6c65 225d 203d 2075 7469 6c73 2e63  able"] = utils.c
-00000c00: 6c65 616e 5f70 7265 6469 6374 6f72 5f6e  lean_predictor_n
-00000c10: 616d 6528 7072 6564 6963 746f 725f 636f  ame(predictor_co
-00000c20: 6c75 6d6e 5f6e 616d 6529 0d0a 2020 2020  lumn_name)..    
-00000c30: 7265 735b 2267 6c6f 6261 6c5f 6176 675f  res["global_avg_
-00000c40: 7461 7267 6574 225d 203d 2067 6c6f 6261  target"] = globa
-00000c50: 6c5f 6176 675f 7461 7267 6574 0d0a 2020  l_avg_target..  
-00000c60: 2020 7265 735b 2270 6f70 5f73 697a 6522    res["pop_size"
-00000c70: 5d20 3d20 7265 735b 2270 6f70 5f73 697a  ] = res["pop_siz
-00000c80: 6522 5d2f 6c65 6e28 6261 7365 7461 626c  e"]/len(basetabl
-00000c90: 652e 696e 6465 7829 0d0a 0d0a 2020 2020  e.index)....    
-00000ca0: 2320 6d61 6b65 2073 7572 6520 746f 2061  # make sure to a
-00000cb0: 6c77 6179 7320 7265 7475 726e 2074 6865  lways return the
-00000cc0: 2064 6174 6120 7769 7468 2074 6865 2070   data with the p
-00000cd0: 726f 7065 7220 636f 6c75 6d6e 206f 7264  roper column ord
-00000ce0: 6572 0d0a 2020 2020 636f 6c75 6d6e 5f6f  er..    column_o
-00000cf0: 7264 6572 203d 205b 2276 6172 6961 626c  rder = ["variabl
-00000d00: 6522 2c20 226c 6162 656c 222c 2022 706f  e", "label", "po
-00000d10: 705f 7369 7a65 222c 0d0a 2020 2020 2020  p_size",..      
-00000d20: 2020 2020 2020 2020 2020 2020 2020 2267                "g
-00000d30: 6c6f 6261 6c5f 6176 675f 7461 7267 6574  lobal_avg_target
-00000d40: 222c 2022 6176 675f 7461 7267 6574 225d  ", "avg_target"]
-00000d50: 0d0a 0d0a 2020 2020 7265 7475 726e 2072  ....    return r
-00000d60: 6573 5b63 6f6c 756d 6e5f 6f72 6465 725d  es[column_order]
-00000d70: 0d0a 0d0a 0d0a 6465 6620 706c 6f74 5f69  ......def plot_i
-00000d80: 6e63 6964 656e 6365 2870 6967 5f74 6162  ncidence(pig_tab
-00000d90: 6c65 733a 2070 642e 4461 7461 4672 616d  les: pd.DataFram
-00000da0: 652c 0d0a 2020 2020 2020 2020 2020 2020  e,..            
-00000db0: 2020 2020 2020 2076 6172 6961 626c 653a         variable:
-00000dc0: 2073 7472 2c0d 0a20 2020 2020 2020 2020   str,..         
-00000dd0: 2020 2020 2020 2020 2020 6d6f 6465 6c5f            model_
-00000de0: 7479 7065 3a20 7374 722c 0d0a 2020 2020  type: str,..    
-00000df0: 2020 2020 2020 2020 2020 2020 2020 2063                 c
-00000e00: 6f6c 756d 6e5f 6f72 6465 723a 206c 6973  olumn_order: lis
-00000e10: 743d 4e6f 6e65 2c0d 0a20 2020 2020 2020  t=None,..       
-00000e20: 2020 2020 2020 2020 2020 2020 6469 6d3a              dim:
-00000e30: 2074 7570 6c65 3d28 3132 2c20 3829 293a   tuple=(12, 8)):
-00000e40: 0d0a 2020 2020 2222 2250 6c6f 7473 2061  ..    """Plots a
-00000e50: 2050 7265 6469 6374 6f72 2049 6e73 6967   Predictor Insig
-00000e60: 6874 7320 4772 6170 6820 2850 4947 292c  hts Graph (PIG),
-00000e70: 2061 2067 7261 7068 2069 6e20 7768 6963   a graph in whic
-00000e80: 6820 7468 6520 6d65 616e 0d0a 2020 2020  h the mean..    
-00000e90: 7461 7267 6574 2076 616c 7565 2069 7320  target value is 
-00000ea0: 706c 6f74 7465 6420 666f 7220 6120 6e75  plotted for a nu
-00000eb0: 6d62 6572 206f 6620 6269 6e73 2063 6f6e  mber of bins con
-00000ec0: 7374 7275 6374 6564 2066 726f 6d20 6120  structed from a 
-00000ed0: 7072 6564 6963 746f 720d 0a20 2020 2076  predictor..    v
-00000ee0: 6172 6961 626c 652e 2057 6865 6e20 7468  ariable. When th
-00000ef0: 6520 7461 7267 6574 2069 7320 6120 6269  e target is a bi
-00000f00: 6e61 7279 2063 6c61 7373 6966 6963 6174  nary classificat
-00000f10: 696f 6e20 7461 7267 6574 2c0d 0a20 2020  ion target,..   
-00000f20: 2074 6865 2070 6c6f 7474 6564 206d 6561   the plotted mea
-00000f30: 6e20 7461 7267 6574 2076 616c 7565 2069  n target value i
-00000f40: 7320 6120 7472 7565 2069 6e63 6964 656e  s a true inciden
-00000f50: 6365 2072 6174 652e 0d0a 0d0a 2020 2020  ce rate.....    
-00000f60: 4269 6e73 2061 7265 206f 7264 6572 6564  Bins are ordered
-00000f70: 2069 6e20 6465 7363 656e 6469 6e67 206f   in descending o
-00000f80: 7264 6572 206f 6620 6d65 616e 2074 6172  rder of mean tar
-00000f90: 6765 7420 7661 6c75 650d 0a20 2020 2075  get value..    u
-00000fa0: 6e6c 6573 7320 7370 6563 6966 6965 6420  nless specified 
-00000fb0: 6f74 6865 7277 6973 6520 7769 7468 2074  otherwise with t
-00000fc0: 6865 2060 636f 6c75 6d6e 5f6f 7264 6572  he `column_order
-00000fd0: 6020 6c69 7374 2e0d 0a0d 0a20 2020 2050  ` list.....    P
-00000fe0: 6172 616d 6574 6572 730d 0a20 2020 202d  arameters..    -
-00000ff0: 2d2d 2d2d 2d2d 2d2d 2d0d 0a20 2020 2070  ---------..    p
-00001000: 6967 5f74 6162 6c65 733a 2070 642e 4461  ig_tables: pd.Da
-00001010: 7461 4672 616d 650d 0a20 2020 2020 2020  taFrame..       
-00001020: 2044 6174 6166 7261 6d65 2077 6974 6820   Dataframe with 
-00001030: 636c 6561 6e65 642c 2062 696e 6e65 642c  cleaned, binned,
-00001040: 2070 6172 7469 7469 6f6e 6564 2061 6e64   partitioned and
-00001050: 2070 7265 7061 7265 6420 6461 7461 2c0d   prepared data,.
-00001060: 0a20 2020 2020 2020 2061 7320 6372 6561  .        as crea
-00001070: 7465 6420 6279 2067 656e 6572 6174 655f  ted by generate_
-00001080: 7069 675f 7461 626c 6573 2829 2066 726f  pig_tables() fro
-00001090: 6d20 7468 6973 206d 6f64 756c 652e 0d0a  m this module...
-000010a0: 2020 2020 7661 7269 6162 6c65 3a20 7374      variable: st
-000010b0: 720d 0a20 2020 2020 2020 204e 616d 6520  r..        Name 
-000010c0: 6f66 2074 6865 2070 7265 6469 6374 6f72  of the predictor
-000010d0: 2076 6172 6961 626c 6520 666f 7220 7768   variable for wh
-000010e0: 6963 6820 7468 6520 5049 4720 7769 6c6c  ich the PIG will
-000010f0: 2062 6520 706c 6f74 7465 642e 0d0a 2020   be plotted...  
-00001100: 2020 6d6f 6465 6c5f 7479 7065 3a20 7374    model_type: st
-00001110: 720d 0a20 2020 2020 2020 2054 7970 6520  r..        Type 
-00001120: 6f66 206d 6f64 656c 2028 6569 7468 6572  of model (either
-00001130: 2022 636c 6173 7369 6669 6361 7469 6f6e   "classification
-00001140: 2220 6f72 2022 7265 6772 6573 7369 6f6e  " or "regression
-00001150: 2229 2e0d 0a20 2020 2063 6f6c 756d 6e5f  ")...    column_
-00001160: 6f72 6465 723a 206c 6973 742c 2064 6566  order: list, def
-00001170: 6175 6c74 3d4e 6f6e 650d 0a20 2020 2020  ault=None..     
-00001180: 2020 2045 7870 6c69 6369 7420 6f72 6465     Explicit orde
-00001190: 7220 6f66 2074 6865 2076 616c 7565 2062  r of the value b
-000011a0: 696e 7320 6f66 2074 6865 2070 7265 6469  ins of the predi
-000011b0: 6374 6f72 2076 6172 6961 626c 6520 746f  ctor variable to
-000011c0: 2062 6520 7573 6564 0d0a 2020 2020 2020   be used..      
-000011d0: 2020 6f6e 2074 6865 2050 4947 2e0d 0a20    on the PIG... 
-000011e0: 2020 2064 696d 3a20 7475 706c 652c 2064     dim: tuple, d
-000011f0: 6566 6175 6c74 3d28 3132 2c20 3829 0d0a  efault=(12, 8)..
-00001200: 2020 2020 2020 2020 4f70 7469 6f6e 616c          Optional
-00001210: 2074 7570 6c65 2074 6f20 636f 6e66 6967   tuple to config
-00001220: 7572 6520 7468 6520 7769 6474 6820 616e  ure the width an
-00001230: 6420 6c65 6e67 7468 206f 6620 7468 6520  d length of the 
-00001240: 706c 6f74 2e0d 0a20 2020 2022 2222 0d0a  plot...    """..
-00001250: 2020 2020 6966 206d 6f64 656c 5f74 7970      if model_typ
-00001260: 6520 6e6f 7420 696e 205b 2263 6c61 7373  e not in ["class
-00001270: 6966 6963 6174 696f 6e22 2c20 2272 6567  ification", "reg
-00001280: 7265 7373 696f 6e22 5d3a 0d0a 2020 2020  ression"]:..    
-00001290: 2020 2020 7261 6973 6520 5661 6c75 6545      raise ValueE
-000012a0: 7272 6f72 2822 416e 2075 6e65 7870 6563  rror("An unexpec
-000012b0: 7465 6420 7661 6c75 6520 7761 7320 7365  ted value was se
-000012c0: 7420 666f 7220 7468 6520 6d6f 6465 6c5f  t for the model_
-000012d0: 7479 7065 2022 0d0a 2020 2020 2020 2020  type "..        
-000012e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000012f0: 2022 7061 7261 6d65 7465 722e 2045 7870   "parameter. Exp
-00001300: 6563 7465 6420 2763 6c61 7373 6966 6963  ected 'classific
-00001310: 6174 696f 6e27 206f 7220 220d 0a20 2020  ation' or "..   
-00001320: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001330: 2020 2020 2020 2227 7265 6772 6573 7369        "'regressi
-00001340: 6f6e 272e 2229 0d0a 0d0a 2020 2020 6466  on'.")....    df
-00001350: 5f70 6c6f 7420 3d20 7069 675f 7461 626c  _plot = pig_tabl
-00001360: 6573 5b70 6967 5f74 6162 6c65 735b 2776  es[pig_tables['v
-00001370: 6172 6961 626c 6527 5d20 3d3d 2076 6172  ariable'] == var
-00001380: 6961 626c 655d 2e63 6f70 7928 290d 0a0d  iable].copy()...
-00001390: 0a20 2020 2069 6620 636f 6c75 6d6e 5f6f  .    if column_o
-000013a0: 7264 6572 2069 7320 6e6f 7420 4e6f 6e65  rder is not None
-000013b0: 3a0d 0a20 2020 2020 2020 2069 6620 6e6f  :..        if no
-000013c0: 7420 7365 7428 6466 5f70 6c6f 745b 276c  t set(df_plot['l
-000013d0: 6162 656c 275d 2920 3d3d 2073 6574 2863  abel']) == set(c
-000013e0: 6f6c 756d 6e5f 6f72 6465 7229 3a0d 0a20  olumn_order):.. 
-000013f0: 2020 2020 2020 2020 2020 2072 6169 7365             raise
-00001400: 2056 616c 7565 4572 726f 7228 0d0a 2020   ValueError(..  
-00001410: 2020 2020 2020 2020 2020 2020 2020 2754                'T
-00001420: 6865 2063 6f6c 756d 6e5f 6f72 6465 7220  he column_order 
-00001430: 616e 6420 7069 675f 7461 626c 6573 2070  and pig_tables p
-00001440: 6172 616d 6574 6572 7320 646f 206e 6f74  arameters do not
-00001450: 2063 6f6e 7461 696e 2027 0d0a 2020 2020   contain '..    
-00001460: 2020 2020 2020 2020 2020 2020 2774 6865              'the
-00001470: 2073 616d 6520 7365 7420 6f66 2076 6172   same set of var
-00001480: 6961 626c 6573 2e27 290d 0a0d 0a20 2020  iables.')....   
-00001490: 2020 2020 2064 665f 706c 6f74 5b27 6c61       df_plot['la
-000014a0: 6265 6c27 5d20 3d20 6466 5f70 6c6f 745b  bel'] = df_plot[
-000014b0: 276c 6162 656c 275d 2e61 7374 7970 6528  'label'].astype(
-000014c0: 2763 6174 6567 6f72 7927 290d 0a20 2020  'category')..   
-000014d0: 2020 2020 2064 665f 706c 6f74 5b27 6c61       df_plot['la
-000014e0: 6265 6c27 5d2e 6361 742e 7265 6f72 6465  bel'].cat.reorde
-000014f0: 725f 6361 7465 676f 7269 6573 2863 6f6c  r_categories(col
-00001500: 756d 6e5f 6f72 6465 722c 0d0a 2020 2020  umn_order,..    
-00001510: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001520: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001530: 2020 2020 2020 2020 2020 2020 696e 706c              inpl
-00001540: 6163 653d 5472 7565 290d 0a0d 0a20 2020  ace=True)....   
-00001550: 2020 2020 2064 665f 706c 6f74 2e73 6f72       df_plot.sor
-00001560: 745f 7661 6c75 6573 2862 793d 5b27 6c61  t_values(by=['la
-00001570: 6265 6c27 5d2c 2061 7363 656e 6469 6e67  bel'], ascending
-00001580: 3d54 7275 652c 2069 6e70 6c61 6365 3d54  =True, inplace=T
-00001590: 7275 6529 0d0a 2020 2020 2020 2020 6466  rue)..        df
-000015a0: 5f70 6c6f 742e 7265 7365 745f 696e 6465  _plot.reset_inde
-000015b0: 7828 696e 706c 6163 653d 5472 7565 290d  x(inplace=True).
-000015c0: 0a20 2020 2065 6c73 653a 0d0a 2020 2020  .    else:..    
-000015d0: 2020 2020 6466 5f70 6c6f 742e 736f 7274      df_plot.sort
-000015e0: 5f76 616c 7565 7328 6279 3d5b 2761 7667  _values(by=['avg
-000015f0: 5f74 6172 6765 7427 5d2c 2061 7363 656e  _target'], ascen
-00001600: 6469 6e67 3d46 616c 7365 2c20 696e 706c  ding=False, inpl
-00001610: 6163 653d 5472 7565 290d 0a20 2020 2020  ace=True)..     
-00001620: 2020 2064 665f 706c 6f74 2e72 6573 6574     df_plot.reset
-00001630: 5f69 6e64 6578 2869 6e70 6c61 6365 3d54  _index(inplace=T
-00001640: 7275 6529 0d0a 0d0a 2020 2020 7769 7468  rue)....    with
-00001650: 2070 6c74 2e73 7479 6c65 2e63 6f6e 7465   plt.style.conte
-00001660: 7874 2822 7365 6162 6f72 6e2d 7469 636b  xt("seaborn-tick
-00001670: 7322 293a 0d0a 2020 2020 2020 2020 6669  s"):..        fi
-00001680: 672c 2061 7820 3d20 706c 742e 7375 6270  g, ax = plt.subp
-00001690: 6c6f 7473 2866 6967 7369 7a65 3d64 696d  lots(figsize=dim
-000016a0: 290d 0a0d 0a20 2020 2020 2020 2023 202d  )....        # -
-000016b0: 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d  ----------------
-000016c0: 2d2d 2d2d 2d2d 2d2d 2d0d 0a20 2020 2020  ---------..     
-000016d0: 2020 2023 204c 6566 7420 6178 6973 202d     # Left axis -
-000016e0: 2061 7665 7261 6765 2074 6172 6765 740d   average target.
-000016f0: 0a20 2020 2020 2020 2023 202d 2d2d 2d2d  .        # -----
-00001700: 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d  ----------------
-00001710: 2d2d 2d2d 2d0d 0a20 2020 2020 2020 2061  -----..        a
-00001720: 782e 706c 6f74 2864 665f 706c 6f74 5b27  x.plot(df_plot['
-00001730: 6c61 6265 6c27 5d2c 2064 665f 706c 6f74  label'], df_plot
-00001740: 5b27 6176 675f 7461 7267 6574 275d 2c0d  ['avg_target'],.
-00001750: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00001760: 2063 6f6c 6f72 3d22 2330 3063 6366 6622   color="#00ccff"
-00001770: 2c20 6d61 726b 6572 3d22 2e22 2c0d 0a20  , marker=".",.. 
-00001780: 2020 2020 2020 2020 2020 2020 2020 206d                 m
-00001790: 6172 6b65 7273 697a 653d 3230 2c20 6c69  arkersize=20, li
-000017a0: 6e65 7769 6474 683d 332c 0d0a 2020 2020  newidth=3,..    
-000017b0: 2020 2020 2020 2020 2020 2020 6c61 6265              labe
-000017c0: 6c3d 2769 6e63 6964 656e 6365 2072 6174  l='incidence rat
-000017d0: 6520 7065 7220 6269 6e27 2069 6620 6d6f  e per bin' if mo
-000017e0: 6465 6c5f 7479 7065 203d 3d20 2263 6c61  del_type == "cla
-000017f0: 7373 6966 6963 6174 696f 6e22 2065 6c73  ssification" els
-00001800: 6520 226d 6561 6e20 7461 7267 6574 2076  e "mean target v
-00001810: 616c 7565 2070 6572 2062 696e 222c 0d0a  alue per bin",..
-00001820: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001830: 7a6f 7264 6572 3d31 3029 0d0a 0d0a 2020  zorder=10)....  
-00001840: 2020 2020 2020 6178 2e70 6c6f 7428 6466        ax.plot(df
-00001850: 5f70 6c6f 745b 276c 6162 656c 275d 2c20  _plot['label'], 
-00001860: 6466 5f70 6c6f 745b 2767 6c6f 6261 6c5f  df_plot['global_
-00001870: 6176 675f 7461 7267 6574 275d 2c0d 0a20  avg_target'],.. 
-00001880: 2020 2020 2020 2020 2020 2020 2020 2063                 c
-00001890: 6f6c 6f72 3d22 2330 3232 3235 3222 2c20  olor="#022252", 
-000018a0: 6c69 6e65 7374 796c 653d 272d 2d27 2c20  linestyle='--', 
-000018b0: 6c69 6e65 7769 6474 683d 342c 0d0a 2020  linewidth=4,..  
-000018c0: 2020 2020 2020 2020 2020 2020 2020 6c61                la
-000018d0: 6265 6c3d 2761 7665 7261 6765 2069 6e63  bel='average inc
-000018e0: 6964 656e 6365 2072 6174 6527 2069 6620  idence rate' if 
-000018f0: 6d6f 6465 6c5f 7479 7065 203d 3d20 2263  model_type == "c
-00001900: 6c61 7373 6966 6963 6174 696f 6e22 2065  lassification" e
-00001910: 6c73 6520 2267 6c6f 6261 6c20 6d65 616e  lse "global mean
-00001920: 2074 6172 6765 7420 7661 6c75 6522 2c0d   target value",.
-00001930: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00001940: 207a 6f72 6465 723d 3130 290d 0a0d 0a20   zorder=10).... 
-00001950: 2020 2020 2020 2023 2044 756d 6d79 206c         # Dummy l
-00001960: 696e 6520 746f 2068 6176 6520 6c61 6265  ine to have labe
-00001970: 6c20 6f6e 2073 6563 6f6e 6420 6178 6973  l on second axis
-00001980: 2066 726f 6d20 6669 7273 740d 0a20 2020   from first..   
-00001990: 2020 2020 2061 782e 706c 6f74 286e 702e       ax.plot(np.
-000019a0: 6e61 6e2c 2022 2339 3339 3539 3822 2c20  nan, "#939598", 
-000019b0: 6c69 6e65 7769 6474 683d 362c 206c 6162  linewidth=6, lab
-000019c0: 656c 3d27 6269 6e20 7369 7a65 2729 0d0a  el='bin size')..
-000019d0: 0d0a 2020 2020 2020 2020 2320 5365 7420  ..        # Set 
-000019e0: 6c61 6265 6c73 2026 2074 6963 6b73 0d0a  labels & ticks..
-000019f0: 2020 2020 2020 2020 6178 2e73 6574 5f79          ax.set_y
-00001a00: 6c61 6265 6c28 2769 6e63 6964 656e 6365  label('incidence
-00001a10: 2720 6966 206d 6f64 656c 5f74 7970 6520  ' if model_type 
-00001a20: 3d3d 2022 636c 6173 7369 6669 6361 7469  == "classificati
-00001a30: 6f6e 2220 656c 7365 2022 6d65 616e 2074  on" else "mean t
-00001a40: 6172 6765 7420 7661 6c75 6522 2c0d 0a20  arget value",.. 
-00001a50: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00001a60: 2020 2020 2066 6f6e 7473 697a 653d 3136       fontsize=16
-00001a70: 290d 0a20 2020 2020 2020 2061 782e 7365  )..        ax.se
-00001a80: 745f 786c 6162 656c 2827 7b7d 2062 696e  t_xlabel('{} bin
-00001a90: 7327 2027 272e 666f 726d 6174 2876 6172  s' ''.format(var
-00001aa0: 6961 626c 6529 2c20 666f 6e74 7369 7a65  iable), fontsize
-00001ab0: 3d31 3629 0d0a 2020 2020 2020 2020 6178  =16)..        ax
-00001ac0: 2e78 6178 6973 2e73 6574 5f74 6963 6b5f  .xaxis.set_tick_
-00001ad0: 7061 7261 6d73 286c 6162 656c 7369 7a65  params(labelsize
-00001ae0: 3d31 3429 0d0a 2020 2020 2020 2020 706c  =14)..        pl
-00001af0: 742e 7365 7470 2861 782e 6765 745f 7874  t.setp(ax.get_xt
-00001b00: 6963 6b6c 6162 656c 7328 292c 0d0a 2020  icklabels(),..  
-00001b10: 2020 2020 2020 2020 2020 2020 2020 2072                 r
-00001b20: 6f74 6174 696f 6e3d 3435 2c20 6861 3d22  otation=45, ha="
-00001b30: 7269 6768 7422 2c20 726f 7461 7469 6f6e  right", rotation
-00001b40: 5f6d 6f64 653d 2261 6e63 686f 7222 290d  _mode="anchor").
-00001b50: 0a20 2020 2020 2020 2061 782e 7961 7869  .        ax.yaxi
-00001b60: 732e 7365 745f 7469 636b 5f70 6172 616d  s.set_tick_param
-00001b70: 7328 6c61 6265 6c73 697a 653d 3134 290d  s(labelsize=14).
-00001b80: 0a0d 0a20 2020 2020 2020 2069 6620 6d6f  ...        if mo
-00001b90: 6465 6c5f 7479 7065 203d 3d20 2263 6c61  del_type == "cla
-00001ba0: 7373 6966 6963 6174 696f 6e22 3a0d 0a20  ssification":.. 
-00001bb0: 2020 2020 2020 2020 2020 2023 204d 6561             # Mea
-00001bc0: 6e20 7461 7267 6574 2076 616c 7565 7320  n target values 
-00001bd0: 6172 6520 6265 7477 6565 6e20 3020 616e  are between 0 an
-00001be0: 6420 3120 2874 6172 6765 7420 696e 6369  d 1 (target inci
-00001bf0: 6465 6e63 6520 7261 7465 292c 0d0a 2020  dence rate),..  
-00001c00: 2020 2020 2020 2020 2020 2320 736f 2066            # so f
-00001c10: 6f72 6d61 7420 7468 656d 2061 7320 7065  ormat them as pe
-00001c20: 7263 656e 7461 6765 730d 0a20 2020 2020  rcentages..     
-00001c30: 2020 2020 2020 2061 782e 7365 745f 7974         ax.set_yt
-00001c40: 6963 6b73 286e 702e 6172 616e 6765 2830  icks(np.arange(0
-00001c50: 2c20 6d61 7828 6466 5f70 6c6f 745b 2761  , max(df_plot['a
-00001c60: 7667 5f74 6172 6765 7427 5d29 2b30 2e30  vg_target'])+0.0
-00001c70: 352c 2030 2e30 3529 290d 0a20 2020 2020  5, 0.05))..     
-00001c80: 2020 2020 2020 2061 782e 7961 7869 732e         ax.yaxis.
-00001c90: 7365 745f 6d61 6a6f 725f 666f 726d 6174  set_major_format
-00001ca0: 7465 7228 0d0a 2020 2020 2020 2020 2020  ter(..          
-00001cb0: 2020 2020 2020 4675 6e63 466f 726d 6174        FuncFormat
-00001cc0: 7465 7228 6c61 6d62 6461 2079 2c20 5f3a  ter(lambda y, _:
-00001cd0: 2027 7b3a 2e31 257d 272e 666f 726d 6174   '{:.1%}'.format
-00001ce0: 2879 2929 290d 0a20 2020 2020 2020 2065  (y)))..        e
-00001cf0: 6c69 6620 6d6f 6465 6c5f 7479 7065 203d  lif model_type =
-00001d00: 3d20 2272 6567 7265 7373 696f 6e22 3a0d  = "regression":.
-00001d10: 0a20 2020 2020 2020 2020 2020 2023 2049  .            # I
-00001d20: 6620 7468 6520 6469 6666 6572 656e 6365  f the difference
-00001d30: 2062 6574 7765 656e 2074 6865 2068 6967   between the hig
-00001d40: 6865 7374 2061 7667 2e20 7461 7267 6574  hest avg. target
-00001d50: 206f 6620 616c 6c20 6269 6e73 0d0a 2020   of all bins..  
-00001d60: 2020 2020 2020 2020 2020 2320 7665 7273            # vers
-00001d70: 7573 2074 6865 2067 6c6f 6261 6c20 6176  us the global av
-00001d80: 672e 2074 6172 6765 7420 414e 4420 7468  g. target AND th
-00001d90: 6520 6469 6666 6572 656e 6365 2062 6574  e difference bet
-00001da0: 7765 656e 2074 6865 0d0a 2020 2020 2020  ween the..      
-00001db0: 2020 2020 2020 2320 6c6f 7765 7374 2061        # lowest a
-00001dc0: 7667 2e20 7461 7267 6574 2076 6572 7375  vg. target versu
-00001dd0: 7320 7468 6520 676c 6f62 616c 2061 7667  s the global avg
-00001de0: 2e20 7461 7267 6574 2061 7265 2062 6f74  . target are bot
-00001df0: 6820 736d 616c 6c65 720d 0a20 2020 2020  h smaller..     
-00001e00: 2020 2020 2020 2023 2074 6861 6e20 3235         # than 25
-00001e10: 2520 6f66 2074 6865 2067 6c6f 6261 6c20  % of the global 
-00001e20: 6176 672e 2074 6172 6765 7420 6974 7365  avg. target itse
-00001e30: 6c66 2c20 7765 2069 6e63 7265 6173 6520  lf, we increase 
-00001e40: 7468 650d 0a20 2020 2020 2020 2020 2020  the..           
-00001e50: 2023 2079 2d61 7869 7320 7261 6e67 652c   # y-axis range,
-00001e60: 2074 6f20 6176 6f69 6420 7468 6174 2074   to avoid that t
-00001e70: 6865 206d 696e 6f72 2061 7667 2e20 7461  he minor avg. ta
-00001e80: 7267 6574 2064 6966 6665 7265 6e63 6573  rget differences
-00001e90: 2061 7265 0d0a 2020 2020 2020 2020 2020   are..          
-00001ea0: 2020 2320 7370 7265 6164 206f 7574 206f    # spread out o
-00001eb0: 7665 7220 7468 6520 636f 6e66 6967 7572  ver the configur
-00001ec0: 6564 2066 6967 7572 6520 6865 6967 6874  ed figure height
-00001ed0: 2c20 7375 6767 6573 7469 6e67 0d0a 2020  , suggesting..  
-00001ee0: 2020 2020 2020 2020 2020 2320 696e 636f            # inco
-00001ef0: 7272 6563 746c 7920 7468 6174 2074 6865  rrectly that the
-00001f00: 7265 2061 7265 2062 6967 2064 6966 6665  re are big diffe
-00001f10: 7265 6e63 6573 2069 6e20 6176 672e 2074  rences in avg. t
-00001f20: 6172 6765 7420 6163 726f 7373 0d0a 2020  arget across..  
-00001f30: 2020 2020 2020 2020 2020 2320 7468 6520            # the 
-00001f40: 6269 6e73 2061 6e64 2076 6572 7375 7320  bins and versus 
-00001f50: 7468 6520 676c 6f62 616c 2061 7667 2e20  the global avg. 
-00001f60: 7461 7267 6574 2e0d 0a20 2020 2020 2020  target...       
-00001f70: 2020 2020 2023 2028 4d6f 7469 7661 7469       # (Motivati
-00001f80: 6f6e 2066 6f72 2074 6865 2041 4e44 2061  on for the AND a
-00001f90: 626f 7665 3a20 6966 206f 6e20 6f6e 6520  bove: if on one 
-00001fa0: 656e 6420 7468 6572 6520 4953 2065 6e6f  end there IS eno
-00001fb0: 7567 680d 0a20 2020 2020 2020 2020 2020  ugh..           
-00001fc0: 2023 2064 6966 6665 7265 6e63 652c 2074   # difference, t
-00001fd0: 6865 2065 6666 6563 7420 7468 6174 2077  he effect that w
-00001fe0: 6520 6469 7363 7573 7320 6865 7265 2064  e discuss here d
-00001ff0: 6f65 7320 6e6f 7420 6f63 6375 722e 290d  oes not occur.).
-00002000: 0a20 2020 2020 2020 2020 2020 2067 6c6f  .            glo
-00002010: 6261 6c5f 6176 675f 7461 7267 6574 203d  bal_avg_target =
-00002020: 206d 6178 2864 665f 706c 6f74 5b27 676c   max(df_plot['gl
-00002030: 6f62 616c 5f61 7667 5f74 6172 6765 7427  obal_avg_target'
-00002040: 5d29 2020 2320 7365 7269 6573 206f 6620  ])  # series of 
-00002050: 7361 6d65 206e 756d 6265 722c 2066 6f72  same number, for
-00002060: 2065 7665 7279 2062 696e 2e0d 0a20 2020   every bin...   
-00002070: 2020 2020 2020 2020 2069 6620 2828 6e70           if ((np
-00002080: 2e61 6273 2828 6d61 7828 6466 5f70 6c6f  .abs((max(df_plo
-00002090: 745b 2761 7667 5f74 6172 6765 7427 5d29  t['avg_target'])
-000020a0: 202d 2067 6c6f 6261 6c5f 6176 675f 7461   - global_avg_ta
-000020b0: 7267 6574 2929 202f 2067 6c6f 6261 6c5f  rget)) / global_
-000020c0: 6176 675f 7461 7267 6574 203c 2030 2e32  avg_target < 0.2
-000020d0: 3529 0d0a 2020 2020 2020 2020 2020 2020  5)..            
-000020e0: 2020 2020 2020 2020 616e 6420 286e 702e          and (np.
-000020f0: 6162 7328 286d 696e 2864 665f 706c 6f74  abs((min(df_plot
-00002100: 5b27 6176 675f 7461 7267 6574 275d 2920  ['avg_target']) 
-00002110: 2d20 676c 6f62 616c 5f61 7667 5f74 6172  - global_avg_tar
-00002120: 6765 7429 2920 2f20 676c 6f62 616c 5f61  get)) / global_a
-00002130: 7667 5f74 6172 6765 7420 3c20 302e 3235  vg_target < 0.25
-00002140: 2929 3a0d 0a20 2020 2020 2020 2020 2020  )):..           
-00002150: 2020 2020 2061 782e 7365 745f 796c 696d       ax.set_ylim
-00002160: 2867 6c6f 6261 6c5f 6176 675f 7461 7267  (global_avg_targ
-00002170: 6574 202a 2030 2e37 352c 0d0a 2020 2020  et * 0.75,..    
-00002180: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00002190: 2020 2020 2020 2020 676c 6f62 616c 5f61          global_a
-000021a0: 7667 5f74 6172 6765 7420 2a20 312e 3235  vg_target * 1.25
-000021b0: 290d 0a0d 0a20 2020 2020 2020 2023 2052  )....        # R
-000021c0: 656d 6f76 6520 7469 636b 7320 6275 7420  emove ticks but 
-000021d0: 6b65 6570 2074 6865 206c 6162 656c 730d  keep the labels.
-000021e0: 0a20 2020 2020 2020 2061 782e 7469 636b  .        ax.tick
-000021f0: 5f70 6172 616d 7328 6178 6973 3d27 626f  _params(axis='bo
-00002200: 7468 272c 2077 6869 6368 3d27 626f 7468  th', which='both
-00002210: 272c 206c 656e 6774 683d 3029 0d0a 2020  ', length=0)..  
-00002220: 2020 2020 2020 6178 2e74 6963 6b5f 7061        ax.tick_pa
-00002230: 7261 6d73 2861 7869 733d 2779 272c 2063  rams(axis='y', c
-00002240: 6f6c 6f72 733d 2223 3030 6363 6666 2229  olors="#00ccff")
-00002250: 0d0a 2020 2020 2020 2020 6178 2e79 6178  ..        ax.yax
-00002260: 6973 2e6c 6162 656c 2e73 6574 5f63 6f6c  is.label.set_col
-00002270: 6f72 2827 2330 3063 6366 6627 290d 0a0d  or('#00ccff')...
-00002280: 0a20 2020 2020 2020 2023 202d 2d2d 2d2d  .        # -----
-00002290: 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 0d0a 2020  ------------..  
-000022a0: 2020 2020 2020 2320 5269 6768 7420 4178        # Right Ax
-000022b0: 6973 202d 2062 696e 730d 0a20 2020 2020  is - bins..     
-000022c0: 2020 2023 202d 2d2d 2d2d 2d2d 2d2d 2d2d     # -----------
-000022d0: 2d2d 2d2d 2d2d 0d0a 2020 2020 2020 2020  ------..        
-000022e0: 6178 3220 3d20 6178 2e74 7769 6e78 2829  ax2 = ax.twinx()
-000022f0: 0d0a 0d0a 2020 2020 2020 2020 6178 322e  ....        ax2.
-00002300: 6261 7228 6466 5f70 6c6f 745b 276c 6162  bar(df_plot['lab
-00002310: 656c 275d 2c20 6466 5f70 6c6f 745b 2770  el'], df_plot['p
-00002320: 6f70 5f73 697a 6527 5d2c 0d0a 2020 2020  op_size'],..    
-00002330: 2020 2020 2020 2020 2020 2020 616c 6967              alig
-00002340: 6e3d 2763 656e 7465 7227 2c20 636f 6c6f  n='center', colo
-00002350: 723d 2223 3933 3935 3938 222c 207a 6f72  r="#939598", zor
-00002360: 6465 723d 3129 0d0a 0d0a 2020 2020 2020  der=1)....      
-00002370: 2020 2320 5365 7420 6c61 6265 6c73 2026    # Set labels &
-00002380: 2074 6963 6b73 0d0a 2020 2020 2020 2020   ticks..        
-00002390: 6178 322e 7365 745f 786c 6162 656c 2827  ax2.set_xlabel('
-000023a0: 7b7d 2062 696e 7327 2027 272e 666f 726d  {} bins' ''.form
-000023b0: 6174 2876 6172 6961 626c 6529 2c20 666f  at(variable), fo
-000023c0: 6e74 7369 7a65 3d31 3629 0d0a 2020 2020  ntsize=16)..    
-000023d0: 2020 2020 6178 322e 7861 7869 732e 7365      ax2.xaxis.se
-000023e0: 745f 7469 636b 5f70 6172 616d 7328 726f  t_tick_params(ro
-000023f0: 7461 7469 6f6e 3d34 352c 206c 6162 656c  tation=45, label
-00002400: 7369 7a65 3d31 3429 0d0a 0d0a 2020 2020  size=14)....    
-00002410: 2020 2020 6178 322e 7961 7869 732e 7365      ax2.yaxis.se
-00002420: 745f 7469 636b 5f70 6172 616d 7328 6c61  t_tick_params(la
-00002430: 6265 6c73 697a 653d 3134 290d 0a20 2020  belsize=14)..   
-00002440: 2020 2020 2061 7832 2e79 6178 6973 2e73       ax2.yaxis.s
-00002450: 6574 5f6d 616a 6f72 5f66 6f72 6d61 7474  et_major_formatt
-00002460: 6572 280d 0a20 2020 2020 2020 2020 2020  er(..           
-00002470: 2046 756e 6346 6f72 6d61 7474 6572 286c   FuncFormatter(l
-00002480: 616d 6264 6120 792c 205f 3a20 277b 3a2e  ambda y, _: '{:.
-00002490: 3125 7d27 2e66 6f72 6d61 7428 7929 2929  1%}'.format(y)))
-000024a0: 0d0a 2020 2020 2020 2020 6178 322e 7365  ..        ax2.se
-000024b0: 745f 796c 6162 656c 2827 706f 7075 6c61  t_ylabel('popula
-000024c0: 7469 6f6e 2073 697a 6527 2c20 666f 6e74  tion size', font
-000024d0: 7369 7a65 3d31 3629 0d0a 2020 2020 2020  size=16)..      
-000024e0: 2020 6178 322e 7469 636b 5f70 6172 616d    ax2.tick_param
-000024f0: 7328 6178 6973 3d27 7927 2c20 636f 6c6f  s(axis='y', colo
-00002500: 7273 3d22 2339 3339 3539 3822 290d 0a20  rs="#939598").. 
-00002510: 2020 2020 2020 2061 7832 2e79 6178 6973         ax2.yaxis
-00002520: 2e6c 6162 656c 2e73 6574 5f63 6f6c 6f72  .label.set_color
-00002530: 2827 2339 3339 3539 3827 290d 0a0d 0a20  ('#939598').... 
-00002540: 2020 2020 2020 2023 2044 6573 7069 6e65         # Despine
-00002550: 2026 2070 7265 7474 6966 790d 0a20 2020   & prettify..   
-00002560: 2020 2020 2073 6e73 2e64 6573 7069 6e65       sns.despine
-00002570: 2861 783d 6178 2c20 7269 6768 743d 5472  (ax=ax, right=Tr
-00002580: 7565 2c20 6c65 6674 3d54 7275 6529 0d0a  ue, left=True)..
-00002590: 2020 2020 2020 2020 736e 732e 6465 7370          sns.desp
-000025a0: 696e 6528 6178 3d61 7832 2c20 6c65 6674  ine(ax=ax2, left
-000025b0: 3d54 7275 652c 2072 6967 6874 3d46 616c  =True, right=Fal
-000025c0: 7365 290d 0a20 2020 2020 2020 2061 7832  se)..        ax2
-000025d0: 2e73 7069 6e65 735b 2772 6967 6874 275d  .spines['right']
-000025e0: 2e73 6574 5f63 6f6c 6f72 2827 7768 6974  .set_color('whit
-000025f0: 6527 290d 0a0d 0a20 2020 2020 2020 2061  e')....        a
-00002600: 7832 2e67 7269 6428 4661 6c73 6529 0d0a  x2.grid(False)..
-00002610: 0d0a 2020 2020 2020 2020 2320 5469 746c  ..        # Titl
-00002620: 6520 2620 6c65 6765 6e64 0d0a 2020 2020  e & legend..    
-00002630: 2020 2020 6966 206d 6f64 656c 5f74 7970      if model_typ
-00002640: 6520 3d3d 2022 636c 6173 7369 6669 6361  e == "classifica
-00002650: 7469 6f6e 223a 0d0a 2020 2020 2020 2020  tion":..        
-00002660: 2020 2020 7469 746c 6520 3d20 2249 6e63      title = "Inc
-00002670: 6964 656e 6365 2070 6c6f 7420 2d20 2220  idence plot - " 
-00002680: 2b20 7661 7269 6162 6c65 0d0a 2020 2020  + variable..    
-00002690: 2020 2020 656c 7365 3a0d 0a20 2020 2020      else:..     
-000026a0: 2020 2020 2020 2074 6974 6c65 203d 2022         title = "
-000026b0: 4d65 616e 2074 6172 6765 7420 706c 6f74  Mean target plot
-000026c0: 202d 2022 202b 2076 6172 6961 626c 650d   - " + variable.
-000026d0: 0a20 2020 2020 2020 2066 6967 2e73 7570  .        fig.sup
-000026e0: 7469 746c 6528 7469 746c 652c 2066 6f6e  title(title, fon
-000026f0: 7473 697a 653d 3232 290d 0a20 2020 2020  tsize=22)..     
-00002700: 2020 2061 782e 6c65 6765 6e64 2866 7261     ax.legend(fra
-00002710: 6d65 6f6e 3d46 616c 7365 2c20 6262 6f78  meon=False, bbox
-00002720: 5f74 6f5f 616e 6368 6f72 3d28 302e 2c20  _to_anchor=(0., 
-00002730: 312e 3031 2c20 312e 2c20 2e31 3032 292c  1.01, 1., .102),
-00002740: 0d0a 2020 2020 2020 2020 2020 2020 2020  ..              
-00002750: 2020 2020 6c6f 633d 332c 206e 636f 6c3d      loc=3, ncol=
-00002760: 312c 206d 6f64 653d 2265 7870 616e 6422  1, mode="expand"
-00002770: 2c20 626f 7264 6572 6178 6573 7061 643d  , borderaxespad=
-00002780: 302e 2c0d 0a20 2020 2020 2020 2020 2020  0.,..           
-00002790: 2020 2020 2020 2070 726f 703d 7b22 7369         prop={"si
-000027a0: 7a65 223a 2031 347d 290d 0a0d 0a20 2020  ze": 14})....   
-000027b0: 2020 2020 2023 2053 6574 206f 7264 6572       # Set order
-000027c0: 206f 6620 6c61 7965 7273 0d0a 2020 2020   of layers..    
-000027d0: 2020 2020 6178 2e73 6574 5f7a 6f72 6465      ax.set_zorde
-000027e0: 7228 3129 0d0a 2020 2020 2020 2020 6178  r(1)..        ax
-000027f0: 2e70 6174 6368 2e73 6574 5f76 6973 6962  .patch.set_visib
-00002800: 6c65 2846 616c 7365 290d 0a0d 0a20 2020  le(False)....   
-00002810: 2020 2020 2064 656c 2064 665f 706c 6f74       del df_plot
-00002820: 0d0a 0d0a 2020 2020 2020 2020 706c 742e  ....        plt.
-00002830: 7469 6768 745f 6c61 796f 7574 2829 0d0a  tight_layout()..
-00002840: 2020 2020 2020 2020 706c 742e 6d61 7267          plt.marg
-00002850: 696e 7328 302e 3031 290d 0a0d 0a20 2020  ins(0.01)....   
-00002860: 2020 2020 2023 2053 686f 770d 0a20 2020       # Show..   
-00002870: 2020 2020 2070 6c74 2e73 686f 7728 290d       plt.show().
-00002880: 0a                                       .
+000000f0: 2020 2020 2020 2020 2020 2074 6172 6765             targe
+00000100: 745f 636f 6c75 6d6e 5f6e 616d 653a 2073  t_column_name: s
+00000110: 7472 2c0d 0a20 2020 2020 2020 2020 2020  tr,..           
+00000120: 2020 2020 2020 2020 2020 2020 2070 7265               pre
+00000130: 7072 6f63 6573 7365 645f 7072 6564 6963  processed_predic
+00000140: 746f 7273 3a20 6c69 7374 2c0d 0a20 2020  tors: list,..   
+00000150: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000160: 2020 2020 2069 645f 636f 6c75 6d6e 5f6e       id_column_n
+00000170: 616d 653a 2073 7472 203d 204e 6f6e 6529  ame: str = None)
+00000180: 202d 3e20 7064 2e44 6174 6146 7261 6d65   -> pd.DataFrame
+00000190: 3a0d 0a20 2020 2022 2222 436f 6d70 7574  :..    """Comput
+000001a0: 6520 5049 4720 7461 626c 6573 2066 6f72  e PIG tables for
+000001b0: 2061 6c6c 2070 7265 6469 6374 6f72 7320   all predictors 
+000001c0: 696e 2070 7265 7072 6f63 6573 7365 645f  in preprocessed_
+000001d0: 7072 6564 6963 746f 7273 2e0d 0a0d 0a20  predictors..... 
+000001e0: 2020 2054 6865 206f 7574 7075 7420 6973     The output is
+000001f0: 2061 2044 6174 6146 7261 6d65 2077 6974   a DataFrame wit
+00000200: 6820 636f 6c75 6d6e 7320 6060 7661 7269  h columns ``vari
+00000210: 6162 6c65 6060 2c20 6060 6c61 6265 6c60  able``, ``label`
+00000220: 602c 0d0a 2020 2020 6060 706f 705f 7369  `,..    ``pop_si
+00000230: 7a65 6060 2c20 6060 676c 6f62 616c 5f61  ze``, ``global_a
+00000240: 7667 5f74 6172 6765 7460 6020 616e 6420  vg_target`` and 
+00000250: 6060 6176 675f 7461 7267 6574 6060 2e0d  ``avg_target``..
+00000260: 0a0d 0a20 2020 2050 6172 616d 6574 6572  ...    Parameter
+00000270: 730d 0a20 2020 202d 2d2d 2d2d 2d2d 2d2d  s..    ---------
+00000280: 2d0d 0a20 2020 2062 6173 6574 6162 6c65  -..    basetable
+00000290: 203a 2070 642e 4461 7461 4672 616d 650d   : pd.DataFrame.
+000002a0: 0a20 2020 2020 2020 2042 6173 6574 6162  .        Basetab
+000002b0: 6c65 2074 6f20 636f 6d70 7574 6520 5049  le to compute PI
+000002c0: 4720 7461 626c 6573 2066 726f 6d2e 0d0a  G tables from...
+000002d0: 2020 2020 7461 7267 6574 5f63 6f6c 756d      target_colum
+000002e0: 6e5f 6e61 6d65 203a 2073 7472 0d0a 2020  n_name : str..  
+000002f0: 2020 2020 2020 4e61 6d65 206f 6620 7468        Name of th
+00000300: 6520 6261 7365 7461 626c 6520 636f 6c75  e basetable colu
+00000310: 6d6e 2063 6f6e 7461 696e 696e 6720 7468  mn containing th
+00000320: 6520 7461 7267 6574 2076 616c 7565 7320  e target values 
+00000330: 746f 2070 7265 6469 6374 2e0d 0a20 2020  to predict...   
+00000340: 2070 7265 7072 6f63 6573 7365 645f 7072   preprocessed_pr
+00000350: 6564 6963 746f 7273 3a20 6c69 7374 0d0a  edictors: list..
+00000360: 2020 2020 2020 2020 4c69 7374 206f 6620          List of 
+00000370: 6261 7365 7461 626c 6520 636f 6c75 6d6e  basetable column
+00000380: 206e 616d 6573 2063 6f6e 7461 696e 696e   names containin
+00000390: 6720 7072 6570 726f 6365 7373 6564 2070  g preprocessed p
+000003a0: 7265 6469 6374 6f72 732e 0d0a 2020 2020  redictors...    
+000003b0: 6964 5f63 6f6c 756d 6e5f 6e61 6d65 203a  id_column_name :
+000003c0: 2073 7472 2c20 6465 6661 756c 743d 4e6f   str, default=No
+000003d0: 6e65 0d0a 2020 2020 2020 2020 4e61 6d65  ne..        Name
+000003e0: 206f 6620 7468 6520 6261 7365 7461 626c   of the basetabl
+000003f0: 6520 636f 6c75 6d6e 2063 6f6e 7461 696e  e column contain
+00000400: 696e 6720 7468 6520 4944 7320 6f66 2074  ing the IDs of t
+00000410: 6865 2062 6173 6574 6162 6c65 2072 6f77  he basetable row
+00000420: 730d 0a20 2020 2020 2020 2028 652e 672e  s..        (e.g.
+00000430: 2063 7573 746f 6d65 726e 756d 6265 7229   customernumber)
+00000440: 2e20 0d0a 2020 2020 5265 7475 726e 730d  . ..    Returns.
+00000450: 0a20 2020 202d 2d2d 2d2d 2d2d 0d0a 2020  .    -------..  
+00000460: 2020 7064 2e44 6174 6146 7261 6d65 0d0a    pd.DataFrame..
+00000470: 2020 2020 2020 2020 4461 7461 4672 616d          DataFram
+00000480: 6520 636f 6e74 6169 6e69 6e67 2061 2050  e containing a P
+00000490: 4947 2074 6162 6c65 2066 6f72 2061 6c6c  IG table for all
+000004a0: 2070 7265 6469 6374 6f72 732e 0d0a 2020   predictors...  
+000004b0: 2020 2222 220d 0a0d 0a20 2020 2023 6368    """....    #ch
+000004c0: 6563 6b20 6966 2074 6865 7265 2069 7320  eck if there is 
+000004d0: 6120 6964 2d63 6f6c 756d 6e20 616e 6420  a id-column and 
+000004e0: 6465 6669 6e65 206e 6f5f 7072 6564 6963  define no_predic
+000004f0: 746f 7220 6163 636f 7264 696e 676c 790d  tor accordingly.
+00000500: 0a20 2020 2069 6620 6964 5f63 6f6c 756d  .    if id_colum
+00000510: 6e5f 6e61 6d65 203d 3d20 4e6f 6e65 3a0d  n_name == None:.
+00000520: 0a20 2020 2020 2020 206e 6f5f 7072 6564  .        no_pred
+00000530: 6963 746f 7220 3d20 5b74 6172 6765 745f  ictor = [target_
+00000540: 636f 6c75 6d6e 5f6e 616d 655d 0d0a 2020  column_name]..  
+00000550: 2020 656c 7365 3a0d 0a20 2020 2020 2020    else:..       
+00000560: 206e 6f5f 7072 6564 6963 746f 7220 3d20   no_predictor = 
+00000570: 5b69 645f 636f 6c75 6d6e 5f6e 616d 652c  [id_column_name,
+00000580: 2074 6172 6765 745f 636f 6c75 6d6e 5f6e   target_column_n
+00000590: 616d 655d 0d0a 2020 2020 0d0a 0d0a 2020  ame]..    ....  
+000005a0: 2020 7069 6773 203d 205b 0d0a 2020 2020    pigs = [..    
+000005b0: 2020 2020 636f 6d70 7574 655f 7069 675f      compute_pig_
+000005c0: 7461 626c 6528 6261 7365 7461 626c 652c  table(basetable,
+000005d0: 0d0a 2020 2020 2020 2020 2020 2020 2020  ..              
+000005e0: 2020 2020 2020 2020 2020 2020 636f 6c75              colu
+000005f0: 6d6e 5f6e 616d 652c 0d0a 2020 2020 2020  mn_name,..      
+00000600: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000610: 2020 2020 7461 7267 6574 5f63 6f6c 756d      target_colum
+00000620: 6e5f 6e61 6d65 2c0d 0a20 2020 2020 2020  n_name,..       
+00000630: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000640: 2020 2029 0d0a 2020 2020 2020 2020 666f     )..        fo
+00000650: 7220 636f 6c75 6d6e 5f6e 616d 6520 696e  r column_name in
+00000660: 2073 6f72 7465 6428 7072 6570 726f 6365   sorted(preproce
+00000670: 7373 6564 5f70 7265 6469 6374 6f72 7329  ssed_predictors)
+00000680: 0d0a 2020 2020 2020 2020 6966 2063 6f6c  ..        if col
+00000690: 756d 6e5f 6e61 6d65 206e 6f74 2069 6e20  umn_name not in 
+000006a0: 6e6f 5f70 7265 6469 6374 6f72 0d0a 2020  no_predictor..  
+000006b0: 2020 5d0d 0a20 2020 206f 7574 7075 7420    ]..    output 
+000006c0: 3d20 7064 2e63 6f6e 6361 7428 7069 6773  = pd.concat(pigs
+000006d0: 2c20 6967 6e6f 7265 5f69 6e64 6578 3d54  , ignore_index=T
+000006e0: 7275 6529 0d0a 2020 2020 7265 7475 726e  rue)..    return
+000006f0: 206f 7574 7075 740d 0a0d 0a0d 0a64 6566   output......def
+00000700: 2063 6f6d 7075 7465 5f70 6967 5f74 6162   compute_pig_tab
+00000710: 6c65 2862 6173 6574 6162 6c65 3a20 7064  le(basetable: pd
+00000720: 2e44 6174 6146 7261 6d65 2c0d 0a20 2020  .DataFrame,..   
+00000730: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000740: 2020 2070 7265 6469 6374 6f72 5f63 6f6c     predictor_col
+00000750: 756d 6e5f 6e61 6d65 3a20 7374 722c 0d0a  umn_name: str,..
+00000760: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000770: 2020 2020 2020 7461 7267 6574 5f63 6f6c        target_col
+00000780: 756d 6e5f 6e61 6d65 3a20 7374 7229 202d  umn_name: str) -
+00000790: 3e20 7064 2e44 6174 6146 7261 6d65 3a0d  > pd.DataFrame:.
+000007a0: 0a20 2020 2022 2222 436f 6d70 7574 6520  .    """Compute 
+000007b0: 7468 6520 5049 4720 7461 626c 6520 6f66  the PIG table of
+000007c0: 2061 2067 6976 656e 2070 7265 6469 6374   a given predict
+000007d0: 6f72 2066 6f72 2061 2067 6976 656e 2074  or for a given t
+000007e0: 6172 6765 742e 0d0a 0d0a 2020 2020 5061  arget.....    Pa
+000007f0: 7261 6d65 7465 7273 0d0a 2020 2020 2d2d  rameters..    --
+00000800: 2d2d 2d2d 2d2d 2d2d 0d0a 2020 2020 6261  --------..    ba
+00000810: 7365 7461 626c 6520 3a20 7064 2e44 6174  setable : pd.Dat
+00000820: 6146 7261 6d65 0d0a 2020 2020 2020 2020  aFrame..        
+00000830: 496e 7075 7420 6461 7461 2066 726f 6d20  Input data from 
+00000840: 7768 6963 6820 746f 2063 6f6d 7075 7465  which to compute
+00000850: 2074 6865 2070 6967 2074 6162 6c65 2e0d   the pig table..
+00000860: 0a20 2020 2070 7265 6469 6374 6f72 5f63  .    predictor_c
+00000870: 6f6c 756d 6e5f 6e61 6d65 203a 2073 7472  olumn_name : str
+00000880: 0d0a 2020 2020 2020 2020 5072 6564 6963  ..        Predic
+00000890: 746f 7220 6e61 6d65 206f 6620 7768 6963  tor name of whic
+000008a0: 6820 746f 2063 6f6d 7075 7465 2074 6865  h to compute the
+000008b0: 2070 6967 2074 6162 6c65 2e0d 0a20 2020   pig table...   
+000008c0: 2074 6172 6765 745f 636f 6c75 6d6e 5f6e   target_column_n
+000008d0: 616d 6520 3a20 7374 720d 0a20 2020 2020  ame : str..     
+000008e0: 2020 204e 616d 6520 6f66 2074 6865 2074     Name of the t
+000008f0: 6172 6765 7420 7661 7269 6162 6c65 2e0d  arget variable..
+00000900: 0a0d 0a20 2020 2052 6574 7572 6e73 0d0a  ...    Returns..
+00000910: 2020 2020 2d2d 2d2d 2d2d 2d0d 0a20 2020      -------..   
+00000920: 2070 642e 4461 7461 4672 616d 650d 0a20   pd.DataFrame.. 
+00000930: 2020 2020 2020 2050 4947 2074 6162 6c65         PIG table
+00000940: 2061 7320 6120 4461 7461 4672 616d 650d   as a DataFrame.
+00000950: 0a20 2020 2022 2222 0d0a 2020 2020 676c  .    """..    gl
+00000960: 6f62 616c 5f61 7667 5f74 6172 6765 7420  obal_avg_target 
+00000970: 3d20 6261 7365 7461 626c 655b 7461 7267  = basetable[targ
+00000980: 6574 5f63 6f6c 756d 6e5f 6e61 6d65 5d2e  et_column_name].
+00000990: 6d65 616e 2829 0d0a 0d0a 2020 2020 2320  mean()....    # 
+000009a0: 6772 6f75 7020 6279 2074 6865 2062 696e  group by the bin
+000009b0: 6e65 6420 7661 7269 6162 6c65 2c20 636f  ned variable, co
+000009c0: 6d70 7574 6520 7468 6520 696e 6369 6465  mpute the incide
+000009d0: 6e63 650d 0a20 2020 2023 2028 3d20 6d65  nce..    # (= me
+000009e0: 616e 206f 6620 7468 6520 7461 7267 6574  an of the target
+000009f0: 2066 6f72 2074 6865 2067 6976 656e 2062   for the given b
+00000a00: 696e 2920 616e 6420 636f 6d70 7574 6520  in) and compute 
+00000a10: 7468 6520 6269 6e20 7369 7a65 0d0a 2020  the bin size..  
+00000a20: 2020 2320 2865 2e67 2e20 434f 554e 5428    # (e.g. COUNT(
+00000a30: 6964 5f63 6f6c 756d 6e5f 6e61 6d65 2929  id_column_name))
+00000a40: 2e20 4166 7465 7220 7468 6174 2c20 7265  . After that, re
+00000a50: 6e61 6d65 2074 6865 2063 6f6c 756d 6e73  name the columns
+00000a60: 0d0a 0d0a 2020 2020 7265 7320 3d20 2862  ....    res = (b
+00000a70: 6173 6574 6162 6c65 2e67 726f 7570 6279  asetable.groupby
+00000a80: 2870 7265 6469 6374 6f72 5f63 6f6c 756d  (predictor_colum
+00000a90: 6e5f 6e61 6d65 290d 0a20 2020 2020 2020  n_name)..       
+00000aa0: 2020 2020 2e61 6767 280d 0a20 2020 2020      .agg(..     
+00000ab0: 2020 2020 2020 2020 2020 2061 7667 5f74             avg_t
+00000ac0: 6172 6765 7420 3d20 2874 6172 6765 745f  arget = (target_
+00000ad0: 636f 6c75 6d6e 5f6e 616d 652c 2022 6d65  column_name, "me
+00000ae0: 616e 2229 2c0d 0a20 2020 2020 2020 2020  an"),..         
+00000af0: 2020 2020 2020 2070 6f70 5f73 697a 6520         pop_size 
+00000b00: 3d20 2874 6172 6765 745f 636f 6c75 6d6e  = (target_column
+00000b10: 5f6e 616d 652c 2022 7369 7a65 2229 0d0a  _name, "size")..
+00000b20: 2020 2020 2020 2020 2020 2029 0d0a 2020             )..  
+00000b30: 2020 2020 2020 2020 202e 7265 7365 745f           .reset_
+00000b40: 696e 6465 7828 290d 0a20 2020 2020 2020  index()..       
+00000b50: 2020 2020 2e72 656e 616d 6528 0d0a 2020      .rename(..  
+00000b60: 2020 2020 2020 2020 2020 2020 2020 636f                co
+00000b70: 6c75 6d6e 733d 7b70 7265 6469 6374 6f72  lumns={predictor
+00000b80: 5f63 6f6c 756d 6e5f 6e61 6d65 3a20 226c  _column_name: "l
+00000b90: 6162 656c 227d 0d0a 2020 2020 2020 2020  abel"}..        
+00000ba0: 2020 2029 0d0a 2020 2020 290d 0a0d 0a0d     )..    ).....
+00000bb0: 0a20 2020 2023 2061 6464 2074 6865 2063  .    # add the c
+00000bc0: 6f6c 756d 6e20 6e61 6d65 2074 6f20 6120  olumn name to a 
+00000bd0: 7661 7269 6162 6c65 2063 6f6c 756d 6e0d  variable column.
+00000be0: 0a20 2020 2023 2061 6464 2074 6865 2061  .    # add the a
+00000bf0: 7665 7261 6765 2069 6e63 6964 656e 6365  verage incidence
+00000c00: 0d0a 2020 2020 2320 7265 706c 6163 6520  ..    # replace 
+00000c10: 706f 7075 6c61 7469 6f6e 2073 697a 6520  population size 
+00000c20: 6279 2061 2070 6572 6365 6e74 6167 6520  by a percentage 
+00000c30: 6f66 2074 6f74 616c 2070 6f70 756c 6174  of total populat
+00000c40: 696f 6e0d 0a20 2020 2072 6573 5b22 7661  ion..    res["va
+00000c50: 7269 6162 6c65 225d 203d 2075 7469 6c73  riable"] = utils
+00000c60: 2e63 6c65 616e 5f70 7265 6469 6374 6f72  .clean_predictor
+00000c70: 5f6e 616d 6528 7072 6564 6963 746f 725f  _name(predictor_
+00000c80: 636f 6c75 6d6e 5f6e 616d 6529 0d0a 2020  column_name)..  
+00000c90: 2020 7265 735b 2267 6c6f 6261 6c5f 6176    res["global_av
+00000ca0: 675f 7461 7267 6574 225d 203d 2067 6c6f  g_target"] = glo
+00000cb0: 6261 6c5f 6176 675f 7461 7267 6574 0d0a  bal_avg_target..
+00000cc0: 2020 2020 7265 735b 2270 6f70 5f73 697a      res["pop_siz
+00000cd0: 6522 5d20 3d20 7265 735b 2270 6f70 5f73  e"] = res["pop_s
+00000ce0: 697a 6522 5d2f 6c65 6e28 6261 7365 7461  ize"]/len(baseta
+00000cf0: 626c 652e 696e 6465 7829 0d0a 0d0a 2020  ble.index)....  
+00000d00: 2020 2320 6d61 6b65 2073 7572 6520 746f    # make sure to
+00000d10: 2061 6c77 6179 7320 7265 7475 726e 2074   always return t
+00000d20: 6865 2064 6174 6120 7769 7468 2074 6865  he data with the
+00000d30: 2070 726f 7065 7220 636f 6c75 6d6e 206f   proper column o
+00000d40: 7264 6572 0d0a 2020 2020 636f 6c75 6d6e  rder..    column
+00000d50: 5f6f 7264 6572 203d 205b 2276 6172 6961  _order = ["varia
+00000d60: 626c 6522 2c20 226c 6162 656c 222c 2022  ble", "label", "
+00000d70: 706f 705f 7369 7a65 222c 0d0a 2020 2020  pop_size",..    
+00000d80: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000d90: 2267 6c6f 6261 6c5f 6176 675f 7461 7267  "global_avg_targ
+00000da0: 6574 222c 2022 6176 675f 7461 7267 6574  et", "avg_target
+00000db0: 225d 0d0a 0d0a 2020 2020 7265 7475 726e  "]....    return
+00000dc0: 2072 6573 5b63 6f6c 756d 6e5f 6f72 6465   res[column_orde
+00000dd0: 725d 0d0a 0d0a 0d0a 6465 6620 706c 6f74  r]......def plot
+00000de0: 5f69 6e63 6964 656e 6365 2870 6967 5f74  _incidence(pig_t
+00000df0: 6162 6c65 733a 2070 642e 4461 7461 4672  ables: pd.DataFr
+00000e00: 616d 652c 0d0a 2020 2020 2020 2020 2020  ame,..          
+00000e10: 2020 2020 2020 2020 2076 6172 6961 626c           variabl
+00000e20: 653a 2073 7472 2c0d 0a20 2020 2020 2020  e: str,..       
+00000e30: 2020 2020 2020 2020 2020 2020 6d6f 6465              mode
+00000e40: 6c5f 7479 7065 3a20 7374 722c 0d0a 2020  l_type: str,..  
+00000e50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00000e60: 2063 6f6c 756d 6e5f 6f72 6465 723a 206c   column_order: l
+00000e70: 6973 743d 4e6f 6e65 2c0d 0a20 2020 2020  ist=None,..     
+00000e80: 2020 2020 2020 2020 2020 2020 2020 6469                di
+00000e90: 6d3a 2074 7570 6c65 3d28 3132 2c20 3829  m: tuple=(12, 8)
+00000ea0: 293a 0d0a 2020 2020 2222 2250 6c6f 7473  ):..    """Plots
+00000eb0: 2061 2050 7265 6469 6374 6f72 2049 6e73   a Predictor Ins
+00000ec0: 6967 6874 7320 4772 6170 6820 2850 4947  ights Graph (PIG
+00000ed0: 292c 2061 2067 7261 7068 2069 6e20 7768  ), a graph in wh
+00000ee0: 6963 6820 7468 6520 6d65 616e 0d0a 2020  ich the mean..  
+00000ef0: 2020 7461 7267 6574 2076 616c 7565 2069    target value i
+00000f00: 7320 706c 6f74 7465 6420 666f 7220 6120  s plotted for a 
+00000f10: 6e75 6d62 6572 206f 6620 6269 6e73 2063  number of bins c
+00000f20: 6f6e 7374 7275 6374 6564 2066 726f 6d20  onstructed from 
+00000f30: 6120 7072 6564 6963 746f 720d 0a20 2020  a predictor..   
+00000f40: 2076 6172 6961 626c 652e 2057 6865 6e20   variable. When 
+00000f50: 7468 6520 7461 7267 6574 2069 7320 6120  the target is a 
+00000f60: 6269 6e61 7279 2063 6c61 7373 6966 6963  binary classific
+00000f70: 6174 696f 6e20 7461 7267 6574 2c0d 0a20  ation target,.. 
+00000f80: 2020 2074 6865 2070 6c6f 7474 6564 206d     the plotted m
+00000f90: 6561 6e20 7461 7267 6574 2076 616c 7565  ean target value
+00000fa0: 2069 7320 6120 7472 7565 2069 6e63 6964   is a true incid
+00000fb0: 656e 6365 2072 6174 652e 0d0a 0d0a 2020  ence rate.....  
+00000fc0: 2020 4269 6e73 2061 7265 206f 7264 6572    Bins are order
+00000fd0: 6564 2069 6e20 6465 7363 656e 6469 6e67  ed in descending
+00000fe0: 206f 7264 6572 206f 6620 6d65 616e 2074   order of mean t
+00000ff0: 6172 6765 7420 7661 6c75 650d 0a20 2020  arget value..   
+00001000: 2075 6e6c 6573 7320 7370 6563 6966 6965   unless specifie
+00001010: 6420 6f74 6865 7277 6973 6520 7769 7468  d otherwise with
+00001020: 2074 6865 2060 636f 6c75 6d6e 5f6f 7264   the `column_ord
+00001030: 6572 6020 6c69 7374 2e0d 0a0d 0a20 2020  er` list.....   
+00001040: 2050 6172 616d 6574 6572 730d 0a20 2020   Parameters..   
+00001050: 202d 2d2d 2d2d 2d2d 2d2d 2d0d 0a20 2020   ----------..   
+00001060: 2070 6967 5f74 6162 6c65 733a 2070 642e   pig_tables: pd.
+00001070: 4461 7461 4672 616d 650d 0a20 2020 2020  DataFrame..     
+00001080: 2020 2044 6174 6166 7261 6d65 2077 6974     Dataframe wit
+00001090: 6820 636c 6561 6e65 642c 2062 696e 6e65  h cleaned, binne
+000010a0: 642c 2070 6172 7469 7469 6f6e 6564 2061  d, partitioned a
+000010b0: 6e64 2070 7265 7061 7265 6420 6461 7461  nd prepared data
+000010c0: 2c0d 0a20 2020 2020 2020 2061 7320 6372  ,..        as cr
+000010d0: 6561 7465 6420 6279 2067 656e 6572 6174  eated by generat
+000010e0: 655f 7069 675f 7461 626c 6573 2829 2066  e_pig_tables() f
+000010f0: 726f 6d20 7468 6973 206d 6f64 756c 652e  rom this module.
+00001100: 0d0a 2020 2020 7661 7269 6162 6c65 3a20  ..    variable: 
+00001110: 7374 720d 0a20 2020 2020 2020 204e 616d  str..        Nam
+00001120: 6520 6f66 2074 6865 2070 7265 6469 6374  e of the predict
+00001130: 6f72 2076 6172 6961 626c 6520 666f 7220  or variable for 
+00001140: 7768 6963 6820 7468 6520 5049 4720 7769  which the PIG wi
+00001150: 6c6c 2062 6520 706c 6f74 7465 642e 0d0a  ll be plotted...
+00001160: 2020 2020 6d6f 6465 6c5f 7479 7065 3a20      model_type: 
+00001170: 7374 720d 0a20 2020 2020 2020 2054 7970  str..        Typ
+00001180: 6520 6f66 206d 6f64 656c 2028 6569 7468  e of model (eith
+00001190: 6572 2022 636c 6173 7369 6669 6361 7469  er "classificati
+000011a0: 6f6e 2220 6f72 2022 7265 6772 6573 7369  on" or "regressi
+000011b0: 6f6e 2229 2e0d 0a20 2020 2063 6f6c 756d  on")...    colum
+000011c0: 6e5f 6f72 6465 723a 206c 6973 742c 2064  n_order: list, d
+000011d0: 6566 6175 6c74 3d4e 6f6e 650d 0a20 2020  efault=None..   
+000011e0: 2020 2020 2045 7870 6c69 6369 7420 6f72       Explicit or
+000011f0: 6465 7220 6f66 2074 6865 2076 616c 7565  der of the value
+00001200: 2062 696e 7320 6f66 2074 6865 2070 7265   bins of the pre
+00001210: 6469 6374 6f72 2076 6172 6961 626c 6520  dictor variable 
+00001220: 746f 2062 6520 7573 6564 0d0a 2020 2020  to be used..    
+00001230: 2020 2020 6f6e 2074 6865 2050 4947 2e0d      on the PIG..
+00001240: 0a20 2020 2064 696d 3a20 7475 706c 652c  .    dim: tuple,
+00001250: 2064 6566 6175 6c74 3d28 3132 2c20 3829   default=(12, 8)
+00001260: 0d0a 2020 2020 2020 2020 4f70 7469 6f6e  ..        Option
+00001270: 616c 2074 7570 6c65 2074 6f20 636f 6e66  al tuple to conf
+00001280: 6967 7572 6520 7468 6520 7769 6474 6820  igure the width 
+00001290: 616e 6420 6c65 6e67 7468 206f 6620 7468  and length of th
+000012a0: 6520 706c 6f74 2e0d 0a20 2020 2022 2222  e plot...    """
+000012b0: 0d0a 2020 2020 6966 206d 6f64 656c 5f74  ..    if model_t
+000012c0: 7970 6520 6e6f 7420 696e 205b 2263 6c61  ype not in ["cla
+000012d0: 7373 6966 6963 6174 696f 6e22 2c20 2272  ssification", "r
+000012e0: 6567 7265 7373 696f 6e22 5d3a 0d0a 2020  egression"]:..  
+000012f0: 2020 2020 2020 7261 6973 6520 5661 6c75        raise Valu
+00001300: 6545 7272 6f72 2822 416e 2075 6e65 7870  eError("An unexp
+00001310: 6563 7465 6420 7661 6c75 6520 7761 7320  ected value was 
+00001320: 7365 7420 666f 7220 7468 6520 6d6f 6465  set for the mode
+00001330: 6c5f 7479 7065 2022 0d0a 2020 2020 2020  l_type "..      
+00001340: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001350: 2020 2022 7061 7261 6d65 7465 722e 2045     "parameter. E
+00001360: 7870 6563 7465 6420 2763 6c61 7373 6966  xpected 'classif
+00001370: 6963 6174 696f 6e27 206f 7220 220d 0a20  ication' or ".. 
+00001380: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001390: 2020 2020 2020 2020 2227 7265 6772 6573          "'regres
+000013a0: 7369 6f6e 272e 2229 0d0a 0d0a 2020 2020  sion'.")....    
+000013b0: 6466 5f70 6c6f 7420 3d20 7069 675f 7461  df_plot = pig_ta
+000013c0: 626c 6573 5b70 6967 5f74 6162 6c65 735b  bles[pig_tables[
+000013d0: 2776 6172 6961 626c 6527 5d20 3d3d 2076  'variable'] == v
+000013e0: 6172 6961 626c 655d 2e63 6f70 7928 290d  ariable].copy().
+000013f0: 0a0d 0a20 2020 2069 6620 636f 6c75 6d6e  ...    if column
+00001400: 5f6f 7264 6572 2069 7320 6e6f 7420 4e6f  _order is not No
+00001410: 6e65 3a0d 0a20 2020 2020 2020 2069 6620  ne:..        if 
+00001420: 6e6f 7420 7365 7428 6466 5f70 6c6f 745b  not set(df_plot[
+00001430: 276c 6162 656c 275d 2920 3d3d 2073 6574  'label']) == set
+00001440: 2863 6f6c 756d 6e5f 6f72 6465 7229 3a0d  (column_order):.
+00001450: 0a20 2020 2020 2020 2020 2020 2072 6169  .            rai
+00001460: 7365 2056 616c 7565 4572 726f 7228 0d0a  se ValueError(..
+00001470: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001480: 2754 6865 2063 6f6c 756d 6e5f 6f72 6465  'The column_orde
+00001490: 7220 616e 6420 7069 675f 7461 626c 6573  r and pig_tables
+000014a0: 2070 6172 616d 6574 6572 7320 646f 206e   parameters do n
+000014b0: 6f74 2063 6f6e 7461 696e 2027 0d0a 2020  ot contain '..  
+000014c0: 2020 2020 2020 2020 2020 2020 2020 2774                't
+000014d0: 6865 2073 616d 6520 7365 7420 6f66 2076  he same set of v
+000014e0: 6172 6961 626c 6573 2e27 290d 0a0d 0a20  ariables.').... 
+000014f0: 2020 2020 2020 2064 665f 706c 6f74 5b27         df_plot['
+00001500: 6c61 6265 6c27 5d20 3d20 6466 5f70 6c6f  label'] = df_plo
+00001510: 745b 276c 6162 656c 275d 2e61 7374 7970  t['label'].astyp
+00001520: 6528 2763 6174 6567 6f72 7927 290d 0a20  e('category').. 
+00001530: 2020 2020 2020 2064 665f 706c 6f74 5b27         df_plot['
+00001540: 6c61 6265 6c27 5d2e 6361 742e 7265 6f72  label'].cat.reor
+00001550: 6465 725f 6361 7465 676f 7269 6573 2863  der_categories(c
+00001560: 6f6c 756d 6e5f 6f72 6465 722c 0d0a 2020  olumn_order,..  
+00001570: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001580: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001590: 2020 2020 2020 2020 2020 2020 2020 696e                in
+000015a0: 706c 6163 653d 5472 7565 290d 0a0d 0a20  place=True).... 
+000015b0: 2020 2020 2020 2064 665f 706c 6f74 2e73         df_plot.s
+000015c0: 6f72 745f 7661 6c75 6573 2862 793d 5b27  ort_values(by=['
+000015d0: 6c61 6265 6c27 5d2c 2061 7363 656e 6469  label'], ascendi
+000015e0: 6e67 3d54 7275 652c 2069 6e70 6c61 6365  ng=True, inplace
+000015f0: 3d54 7275 6529 0d0a 2020 2020 2020 2020  =True)..        
+00001600: 6466 5f70 6c6f 742e 7265 7365 745f 696e  df_plot.reset_in
+00001610: 6465 7828 696e 706c 6163 653d 5472 7565  dex(inplace=True
+00001620: 290d 0a20 2020 2065 6c73 653a 0d0a 2020  )..    else:..  
+00001630: 2020 2020 2020 6466 5f70 6c6f 742e 736f        df_plot.so
+00001640: 7274 5f76 616c 7565 7328 6279 3d5b 2761  rt_values(by=['a
+00001650: 7667 5f74 6172 6765 7427 5d2c 2061 7363  vg_target'], asc
+00001660: 656e 6469 6e67 3d46 616c 7365 2c20 696e  ending=False, in
+00001670: 706c 6163 653d 5472 7565 290d 0a20 2020  place=True)..   
+00001680: 2020 2020 2064 665f 706c 6f74 2e72 6573       df_plot.res
+00001690: 6574 5f69 6e64 6578 2869 6e70 6c61 6365  et_index(inplace
+000016a0: 3d54 7275 6529 0d0a 0d0a 2020 2020 7769  =True)....    wi
+000016b0: 7468 2070 6c74 2e73 7479 6c65 2e63 6f6e  th plt.style.con
+000016c0: 7465 7874 2822 7365 6162 6f72 6e2d 7469  text("seaborn-ti
+000016d0: 636b 7322 293a 0d0a 2020 2020 2020 2020  cks"):..        
+000016e0: 6669 672c 2061 7820 3d20 706c 742e 7375  fig, ax = plt.su
+000016f0: 6270 6c6f 7473 2866 6967 7369 7a65 3d64  bplots(figsize=d
+00001700: 696d 290d 0a0d 0a20 2020 2020 2020 2023  im)....        #
+00001710: 202d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d   ---------------
+00001720: 2d2d 2d2d 2d2d 2d2d 2d2d 2d0d 0a20 2020  -----------..   
+00001730: 2020 2020 2023 204c 6566 7420 6178 6973       # Left axis
+00001740: 202d 2061 7665 7261 6765 2074 6172 6765   - average targe
+00001750: 740d 0a20 2020 2020 2020 2023 202d 2d2d  t..        # ---
+00001760: 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d  ----------------
+00001770: 2d2d 2d2d 2d2d 2d0d 0a20 2020 2020 2020  -------..       
+00001780: 2061 782e 706c 6f74 2864 665f 706c 6f74   ax.plot(df_plot
+00001790: 5b27 6c61 6265 6c27 5d2c 2064 665f 706c  ['label'], df_pl
+000017a0: 6f74 5b27 6176 675f 7461 7267 6574 275d  ot['avg_target']
+000017b0: 2c0d 0a20 2020 2020 2020 2020 2020 2020  ,..             
+000017c0: 2020 2063 6f6c 6f72 3d22 2330 3063 6366     color="#00ccf
+000017d0: 6622 2c20 6d61 726b 6572 3d22 2e22 2c0d  f", marker=".",.
+000017e0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000017f0: 206d 6172 6b65 7273 697a 653d 3230 2c20   markersize=20, 
+00001800: 6c69 6e65 7769 6474 683d 332c 0d0a 2020  linewidth=3,..  
+00001810: 2020 2020 2020 2020 2020 2020 2020 6c61                la
+00001820: 6265 6c3d 2769 6e63 6964 656e 6365 2072  bel='incidence r
+00001830: 6174 6520 7065 7220 6269 6e27 2069 6620  ate per bin' if 
+00001840: 6d6f 6465 6c5f 7479 7065 203d 3d20 2263  model_type == "c
+00001850: 6c61 7373 6966 6963 6174 696f 6e22 2065  lassification" e
+00001860: 6c73 6520 226d 6561 6e20 7461 7267 6574  lse "mean target
+00001870: 2076 616c 7565 2070 6572 2062 696e 222c   value per bin",
+00001880: 0d0a 2020 2020 2020 2020 2020 2020 2020  ..              
+00001890: 2020 7a6f 7264 6572 3d31 3029 0d0a 0d0a    zorder=10)....
+000018a0: 2020 2020 2020 2020 6178 2e70 6c6f 7428          ax.plot(
+000018b0: 6466 5f70 6c6f 745b 276c 6162 656c 275d  df_plot['label']
+000018c0: 2c20 6466 5f70 6c6f 745b 2767 6c6f 6261  , df_plot['globa
+000018d0: 6c5f 6176 675f 7461 7267 6574 275d 2c0d  l_avg_target'],.
+000018e0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000018f0: 2063 6f6c 6f72 3d22 2330 3232 3235 3222   color="#022252"
+00001900: 2c20 6c69 6e65 7374 796c 653d 272d 2d27  , linestyle='--'
+00001910: 2c20 6c69 6e65 7769 6474 683d 342c 0d0a  , linewidth=4,..
+00001920: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00001930: 6c61 6265 6c3d 2761 7665 7261 6765 2069  label='average i
+00001940: 6e63 6964 656e 6365 2072 6174 6527 2069  ncidence rate' i
+00001950: 6620 6d6f 6465 6c5f 7479 7065 203d 3d20  f model_type == 
+00001960: 2263 6c61 7373 6966 6963 6174 696f 6e22  "classification"
+00001970: 2065 6c73 6520 2267 6c6f 6261 6c20 6d65   else "global me
+00001980: 616e 2074 6172 6765 7420 7661 6c75 6522  an target value"
+00001990: 2c0d 0a20 2020 2020 2020 2020 2020 2020  ,..             
+000019a0: 2020 207a 6f72 6465 723d 3130 290d 0a0d     zorder=10)...
+000019b0: 0a20 2020 2020 2020 2023 2044 756d 6d79  .        # Dummy
+000019c0: 206c 696e 6520 746f 2068 6176 6520 6c61   line to have la
+000019d0: 6265 6c20 6f6e 2073 6563 6f6e 6420 6178  bel on second ax
+000019e0: 6973 2066 726f 6d20 6669 7273 740d 0a20  is from first.. 
+000019f0: 2020 2020 2020 2061 782e 706c 6f74 286e         ax.plot(n
+00001a00: 702e 6e61 6e2c 2022 2339 3339 3539 3822  p.nan, "#939598"
+00001a10: 2c20 6c69 6e65 7769 6474 683d 362c 206c  , linewidth=6, l
+00001a20: 6162 656c 3d27 6269 6e20 7369 7a65 2729  abel='bin size')
+00001a30: 0d0a 0d0a 2020 2020 2020 2020 2320 5365  ....        # Se
+00001a40: 7420 6c61 6265 6c73 2026 2074 6963 6b73  t labels & ticks
+00001a50: 0d0a 2020 2020 2020 2020 6178 2e73 6574  ..        ax.set
+00001a60: 5f79 6c61 6265 6c28 2749 6e63 6964 656e  _ylabel('Inciden
+00001a70: 6365 2720 6966 206d 6f64 656c 5f74 7970  ce' if model_typ
+00001a80: 6520 3d3d 2022 636c 6173 7369 6669 6361  e == "classifica
+00001a90: 7469 6f6e 2220 656c 7365 2022 4d65 616e  tion" else "Mean
+00001aa0: 2074 6172 6765 7420 7661 6c75 6522 2c0d   target value",.
+00001ab0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001ac0: 2020 2020 2020 2066 6f6e 7473 697a 653d         fontsize=
+00001ad0: 3136 290d 0a20 2020 2020 2020 2061 782e  16)..        ax.
+00001ae0: 7365 745f 786c 6162 656c 2822 4269 6e73  set_xlabel("Bins
+00001af0: 222c 2066 6f6e 7473 697a 653d 3135 290d  ", fontsize=15).
+00001b00: 0a20 2020 2020 2020 2061 782e 7861 7869  .        ax.xaxi
+00001b10: 732e 7365 745f 7469 636b 5f70 6172 616d  s.set_tick_param
+00001b20: 7328 6c61 6265 6c73 697a 653d 3134 290d  s(labelsize=14).
+00001b30: 0a20 2020 2020 2020 2070 6c74 2e73 6574  .        plt.set
+00001b40: 7028 6178 2e67 6574 5f78 7469 636b 6c61  p(ax.get_xtickla
+00001b50: 6265 6c73 2829 2c0d 0a20 2020 2020 2020  bels(),..       
+00001b60: 2020 2020 2020 2020 2020 726f 7461 7469            rotati
+00001b70: 6f6e 3d34 352c 2068 613d 2272 6967 6874  on=45, ha="right
+00001b80: 222c 2072 6f74 6174 696f 6e5f 6d6f 6465  ", rotation_mode
+00001b90: 3d22 616e 6368 6f72 2229 0d0a 2020 2020  ="anchor")..    
+00001ba0: 2020 2020 6178 2e79 6178 6973 2e73 6574      ax.yaxis.set
+00001bb0: 5f74 6963 6b5f 7061 7261 6d73 286c 6162  _tick_params(lab
+00001bc0: 656c 7369 7a65 3d31 3429 0d0a 0d0a 2020  elsize=14)....  
+00001bd0: 2020 2020 2020 6966 206d 6f64 656c 5f74        if model_t
+00001be0: 7970 6520 3d3d 2022 636c 6173 7369 6669  ype == "classifi
+00001bf0: 6361 7469 6f6e 223a 0d0a 2020 2020 2020  cation":..      
+00001c00: 2020 2020 2020 2320 4d65 616e 2074 6172        # Mean tar
+00001c10: 6765 7420 7661 6c75 6573 2061 7265 2062  get values are b
+00001c20: 6574 7765 656e 2030 2061 6e64 2031 2028  etween 0 and 1 (
+00001c30: 7461 7267 6574 2069 6e63 6964 656e 6365  target incidence
+00001c40: 2072 6174 6529 2c0d 0a20 2020 2020 2020   rate),..       
+00001c50: 2020 2020 2023 2073 6f20 666f 726d 6174       # so format
+00001c60: 2074 6865 6d20 6173 2070 6572 6365 6e74   them as percent
+00001c70: 6167 6573 0d0a 2020 2020 2020 2020 2020  ages..          
+00001c80: 2020 6178 2e73 6574 5f79 7469 636b 7328    ax.set_yticks(
+00001c90: 6e70 2e61 7261 6e67 6528 302c 206d 6178  np.arange(0, max
+00001ca0: 2864 665f 706c 6f74 5b27 6176 675f 7461  (df_plot['avg_ta
+00001cb0: 7267 6574 275d 292b 302e 3035 2c20 302e  rget'])+0.05, 0.
+00001cc0: 3035 2929 0d0a 2020 2020 2020 2020 2020  05))..          
+00001cd0: 2020 6178 2e79 6178 6973 2e73 6574 5f6d    ax.yaxis.set_m
+00001ce0: 616a 6f72 5f66 6f72 6d61 7474 6572 280d  ajor_formatter(.
+00001cf0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00001d00: 2046 756e 6346 6f72 6d61 7474 6572 286c   FuncFormatter(l
+00001d10: 616d 6264 6120 792c 205f 3a20 277b 3a2e  ambda y, _: '{:.
+00001d20: 3125 7d27 2e66 6f72 6d61 7428 7929 2929  1%}'.format(y)))
+00001d30: 0d0a 2020 2020 2020 2020 656c 6966 206d  ..        elif m
+00001d40: 6f64 656c 5f74 7970 6520 3d3d 2022 7265  odel_type == "re
+00001d50: 6772 6573 7369 6f6e 223a 0d0a 2020 2020  gression":..    
+00001d60: 2020 2020 2020 2020 2320 4966 2074 6865          # If the
+00001d70: 2064 6966 6665 7265 6e63 6520 6265 7477   difference betw
+00001d80: 6565 6e20 7468 6520 6869 6768 6573 7420  een the highest 
+00001d90: 6176 672e 2074 6172 6765 7420 6f66 2061  avg. target of a
+00001da0: 6c6c 2062 696e 730d 0a20 2020 2020 2020  ll bins..       
+00001db0: 2020 2020 2023 2076 6572 7375 7320 7468       # versus th
+00001dc0: 6520 676c 6f62 616c 2061 7667 2e20 7461  e global avg. ta
+00001dd0: 7267 6574 2041 4e44 2074 6865 2064 6966  rget AND the dif
+00001de0: 6665 7265 6e63 6520 6265 7477 6565 6e20  ference between 
+00001df0: 7468 650d 0a20 2020 2020 2020 2020 2020  the..           
+00001e00: 2023 206c 6f77 6573 7420 6176 672e 2074   # lowest avg. t
+00001e10: 6172 6765 7420 7665 7273 7573 2074 6865  arget versus the
+00001e20: 2067 6c6f 6261 6c20 6176 672e 2074 6172   global avg. tar
+00001e30: 6765 7420 6172 6520 626f 7468 2073 6d61  get are both sma
+00001e40: 6c6c 6572 0d0a 2020 2020 2020 2020 2020  ller..          
+00001e50: 2020 2320 7468 616e 2032 3525 206f 6620    # than 25% of 
+00001e60: 7468 6520 676c 6f62 616c 2061 7667 2e20  the global avg. 
+00001e70: 7461 7267 6574 2069 7473 656c 662c 2077  target itself, w
+00001e80: 6520 696e 6372 6561 7365 2074 6865 0d0a  e increase the..
+00001e90: 2020 2020 2020 2020 2020 2020 2320 792d              # y-
+00001ea0: 6178 6973 2072 616e 6765 2c20 746f 2061  axis range, to a
+00001eb0: 766f 6964 2074 6861 7420 7468 6520 6d69  void that the mi
+00001ec0: 6e6f 7220 6176 672e 2074 6172 6765 7420  nor avg. target 
+00001ed0: 6469 6666 6572 656e 6365 7320 6172 650d  differences are.
+00001ee0: 0a20 2020 2020 2020 2020 2020 2023 2073  .            # s
+00001ef0: 7072 6561 6420 6f75 7420 6f76 6572 2074  pread out over t
+00001f00: 6865 2063 6f6e 6669 6775 7265 6420 6669  he configured fi
+00001f10: 6775 7265 2068 6569 6768 742c 2073 7567  gure height, sug
+00001f20: 6765 7374 696e 670d 0a20 2020 2020 2020  gesting..       
+00001f30: 2020 2020 2023 2069 6e63 6f72 7265 6374       # incorrect
+00001f40: 6c79 2074 6861 7420 7468 6572 6520 6172  ly that there ar
+00001f50: 6520 6269 6720 6469 6666 6572 656e 6365  e big difference
+00001f60: 7320 696e 2061 7667 2e20 7461 7267 6574  s in avg. target
+00001f70: 2061 6372 6f73 730d 0a20 2020 2020 2020   across..       
+00001f80: 2020 2020 2023 2074 6865 2062 696e 7320       # the bins 
+00001f90: 616e 6420 7665 7273 7573 2074 6865 2067  and versus the g
+00001fa0: 6c6f 6261 6c20 6176 672e 2074 6172 6765  lobal avg. targe
+00001fb0: 742e 0d0a 2020 2020 2020 2020 2020 2020  t...            
+00001fc0: 2320 284d 6f74 6976 6174 696f 6e20 666f  # (Motivation fo
+00001fd0: 7220 7468 6520 414e 4420 6162 6f76 653a  r the AND above:
+00001fe0: 2069 6620 6f6e 206f 6e65 2065 6e64 2074   if on one end t
+00001ff0: 6865 7265 2049 5320 656e 6f75 6768 0d0a  here IS enough..
+00002000: 2020 2020 2020 2020 2020 2020 2320 6469              # di
+00002010: 6666 6572 656e 6365 2c20 7468 6520 6566  fference, the ef
+00002020: 6665 6374 2074 6861 7420 7765 2064 6973  fect that we dis
+00002030: 6375 7373 2068 6572 6520 646f 6573 206e  cuss here does n
+00002040: 6f74 206f 6363 7572 2e29 0d0a 2020 2020  ot occur.)..    
+00002050: 2020 2020 2020 2020 676c 6f62 616c 5f61          global_a
+00002060: 7667 5f74 6172 6765 7420 3d20 6d61 7828  vg_target = max(
+00002070: 6466 5f70 6c6f 745b 2767 6c6f 6261 6c5f  df_plot['global_
+00002080: 6176 675f 7461 7267 6574 275d 2920 2023  avg_target'])  #
+00002090: 2073 6572 6965 7320 6f66 2073 616d 6520   series of same 
+000020a0: 6e75 6d62 6572 2c20 666f 7220 6576 6572  number, for ever
+000020b0: 7920 6269 6e2e 0d0a 2020 2020 2020 2020  y bin...        
+000020c0: 2020 2020 6966 2028 286e 702e 6162 7328      if ((np.abs(
+000020d0: 286d 6178 2864 665f 706c 6f74 5b27 6176  (max(df_plot['av
+000020e0: 675f 7461 7267 6574 275d 2920 2d20 676c  g_target']) - gl
+000020f0: 6f62 616c 5f61 7667 5f74 6172 6765 7429  obal_avg_target)
+00002100: 2920 2f20 676c 6f62 616c 5f61 7667 5f74  ) / global_avg_t
+00002110: 6172 6765 7420 3c20 302e 3235 290d 0a20  arget < 0.25).. 
+00002120: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00002130: 2020 2061 6e64 2028 6e70 2e61 6273 2828     and (np.abs((
+00002140: 6d69 6e28 6466 5f70 6c6f 745b 2761 7667  min(df_plot['avg
+00002150: 5f74 6172 6765 7427 5d29 202d 2067 6c6f  _target']) - glo
+00002160: 6261 6c5f 6176 675f 7461 7267 6574 2929  bal_avg_target))
+00002170: 202f 2067 6c6f 6261 6c5f 6176 675f 7461   / global_avg_ta
+00002180: 7267 6574 203c 2030 2e32 3529 293a 0d0a  rget < 0.25)):..
+00002190: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000021a0: 6178 2e73 6574 5f79 6c69 6d28 676c 6f62  ax.set_ylim(glob
+000021b0: 616c 5f61 7667 5f74 6172 6765 7420 2a20  al_avg_target * 
+000021c0: 302e 3735 2c0d 0a20 2020 2020 2020 2020  0.75,..         
+000021d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000021e0: 2020 2067 6c6f 6261 6c5f 6176 675f 7461     global_avg_ta
+000021f0: 7267 6574 202a 2031 2e32 3529 0d0a 0d0a  rget * 1.25)....
+00002200: 2020 2020 2020 2020 2320 5265 6d6f 7665          # Remove
+00002210: 2074 6963 6b73 2062 7574 206b 6565 7020   ticks but keep 
+00002220: 7468 6520 6c61 6265 6c73 0d0a 2020 2020  the labels..    
+00002230: 2020 2020 6178 2e74 6963 6b5f 7061 7261      ax.tick_para
+00002240: 6d73 2861 7869 733d 2762 6f74 6827 2c20  ms(axis='both', 
+00002250: 7768 6963 683d 2762 6f74 6827 2c20 6c65  which='both', le
+00002260: 6e67 7468 3d30 290d 0a20 2020 2020 2020  ngth=0)..       
+00002270: 2061 782e 7469 636b 5f70 6172 616d 7328   ax.tick_params(
+00002280: 6178 6973 3d27 7927 2c20 636f 6c6f 7273  axis='y', colors
+00002290: 3d22 2330 3063 6366 6622 290d 0a20 2020  ="#00ccff")..   
+000022a0: 2020 2020 2061 782e 7961 7869 732e 6c61       ax.yaxis.la
+000022b0: 6265 6c2e 7365 745f 636f 6c6f 7228 2723  bel.set_color('#
+000022c0: 3030 6363 6666 2729 0d0a 0d0a 2020 2020  00ccff')....    
+000022d0: 2020 2020 2320 2d2d 2d2d 2d2d 2d2d 2d2d      # ----------
+000022e0: 2d2d 2d2d 2d2d 2d0d 0a20 2020 2020 2020  -------..       
+000022f0: 2023 2052 6967 6874 2041 7869 7320 2d20   # Right Axis - 
+00002300: 6269 6e73 0d0a 2020 2020 2020 2020 2320  bins..        # 
+00002310: 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d 2d2d  ----------------
+00002320: 2d0d 0a20 2020 2020 2020 2061 7832 203d  -..        ax2 =
+00002330: 2061 782e 7477 696e 7828 290d 0a0d 0a20   ax.twinx().... 
+00002340: 2020 2020 2020 2061 7832 2e62 6172 2864         ax2.bar(d
+00002350: 665f 706c 6f74 5b27 6c61 6265 6c27 5d2c  f_plot['label'],
+00002360: 2064 665f 706c 6f74 5b27 706f 705f 7369   df_plot['pop_si
+00002370: 7a65 275d 2c0d 0a20 2020 2020 2020 2020  ze'],..         
+00002380: 2020 2020 2020 2061 6c69 676e 3d27 6365         align='ce
+00002390: 6e74 6572 272c 2063 6f6c 6f72 3d22 2339  nter', color="#9
+000023a0: 3339 3539 3822 2c20 7a6f 7264 6572 3d31  39598", zorder=1
+000023b0: 290d 0a0d 0a20 2020 2020 2020 2023 2053  )....        # S
+000023c0: 6574 206c 6162 656c 7320 2620 7469 636b  et labels & tick
+000023d0: 730d 0a20 2020 2020 2020 2061 7832 2e73  s..        ax2.s
+000023e0: 6574 5f78 6c61 6265 6c28 2242 696e 7322  et_xlabel("Bins"
+000023f0: 2c20 666f 6e74 7369 7a65 3d31 3529 0d0a  , fontsize=15)..
+00002400: 2020 2020 2020 2020 6178 322e 7861 7869          ax2.xaxi
+00002410: 732e 7365 745f 7469 636b 5f70 6172 616d  s.set_tick_param
+00002420: 7328 726f 7461 7469 6f6e 3d34 352c 206c  s(rotation=45, l
+00002430: 6162 656c 7369 7a65 3d31 3429 0d0a 0d0a  abelsize=14)....
+00002440: 2020 2020 2020 2020 6178 322e 7961 7869          ax2.yaxi
+00002450: 732e 7365 745f 7469 636b 5f70 6172 616d  s.set_tick_param
+00002460: 7328 6c61 6265 6c73 697a 653d 3134 290d  s(labelsize=14).
+00002470: 0a20 2020 2020 2020 2061 7832 2e79 6178  .        ax2.yax
+00002480: 6973 2e73 6574 5f6d 616a 6f72 5f66 6f72  is.set_major_for
+00002490: 6d61 7474 6572 280d 0a20 2020 2020 2020  matter(..       
+000024a0: 2020 2020 2046 756e 6346 6f72 6d61 7474       FuncFormatt
+000024b0: 6572 286c 616d 6264 6120 792c 205f 3a20  er(lambda y, _: 
+000024c0: 277b 3a2e 3125 7d27 2e66 6f72 6d61 7428  '{:.1%}'.format(
+000024d0: 7929 2929 0d0a 2020 2020 2020 2020 6178  y)))..        ax
+000024e0: 322e 7365 745f 796c 6162 656c 2827 506f  2.set_ylabel('Po
+000024f0: 7075 6c61 7469 6f6e 2073 697a 6527 2c20  pulation size', 
+00002500: 666f 6e74 7369 7a65 3d31 3529 0d0a 2020  fontsize=15)..  
+00002510: 2020 2020 2020 6178 322e 7469 636b 5f70        ax2.tick_p
+00002520: 6172 616d 7328 6178 6973 3d27 7927 2c20  arams(axis='y', 
+00002530: 636f 6c6f 7273 3d22 2339 3339 3539 3822  colors="#939598"
+00002540: 290d 0a20 2020 2020 2020 2061 7832 2e79  )..        ax2.y
+00002550: 6178 6973 2e6c 6162 656c 2e73 6574 5f63  axis.label.set_c
+00002560: 6f6c 6f72 2827 2339 3339 3539 3827 290d  olor('#939598').
+00002570: 0a0d 0a20 2020 2020 2020 2023 2044 6573  ...        # Des
+00002580: 7069 6e65 2026 2070 7265 7474 6966 790d  pine & prettify.
+00002590: 0a20 2020 2020 2020 2073 6e73 2e64 6573  .        sns.des
+000025a0: 7069 6e65 2861 783d 6178 2c20 7269 6768  pine(ax=ax, righ
+000025b0: 743d 5472 7565 2c20 6c65 6674 3d54 7275  t=True, left=Tru
+000025c0: 6529 0d0a 2020 2020 2020 2020 736e 732e  e)..        sns.
+000025d0: 6465 7370 696e 6528 6178 3d61 7832 2c20  despine(ax=ax2, 
+000025e0: 6c65 6674 3d54 7275 652c 2072 6967 6874  left=True, right
+000025f0: 3d46 616c 7365 290d 0a20 2020 2020 2020  =False)..       
+00002600: 2061 7832 2e73 7069 6e65 735b 2772 6967   ax2.spines['rig
+00002610: 6874 275d 2e73 6574 5f63 6f6c 6f72 2827  ht'].set_color('
+00002620: 7768 6974 6527 290d 0a0d 0a20 2020 2020  white')....     
+00002630: 2020 2061 7832 2e67 7269 6428 4661 6c73     ax2.grid(Fals
+00002640: 6529 0d0a 0d0a 2020 2020 2020 2020 2320  e)....        # 
+00002650: 5469 746c 6520 2620 6c65 6765 6e64 0d0a  Title & legend..
+00002660: 2020 2020 2020 2020 6966 206d 6f64 656c          if model
+00002670: 5f74 7970 6520 3d3d 2022 636c 6173 7369  _type == "classi
+00002680: 6669 6361 7469 6f6e 223a 0d0a 2020 2020  fication":..    
+00002690: 2020 2020 2020 2020 7469 746c 6520 3d20          title = 
+000026a0: 2249 6e63 6964 656e 6365 2070 6c6f 7422  "Incidence plot"
+000026b0: 0d0a 2020 2020 2020 2020 656c 7365 3a0d  ..        else:.
+000026c0: 0a20 2020 2020 2020 2020 2020 2074 6974  .            tit
+000026d0: 6c65 203d 2022 4d65 616e 2074 6172 6765  le = "Mean targe
+000026e0: 7420 706c 6f74 220d 0a20 2020 2020 2020  t plot"..       
+000026f0: 2066 6967 2e73 7570 7469 746c 6528 7469   fig.suptitle(ti
+00002700: 746c 652c 2066 6f6e 7473 697a 653d 3230  tle, fontsize=20
+00002710: 290d 0a20 2020 2020 2020 2070 6c74 2e74  )..        plt.t
+00002720: 6974 6c65 2876 6172 6961 626c 652c 2066  itle(variable, f
+00002730: 6f6e 7473 697a 653d 3137 290d 0a20 2020  ontsize=17)..   
+00002740: 2020 2020 2061 782e 6c65 6765 6e64 2866       ax.legend(f
+00002750: 7261 6d65 6f6e 3d46 616c 7365 2c20 6262  rameon=False, bb
+00002760: 6f78 5f74 6f5f 616e 6368 6f72 3d28 302e  ox_to_anchor=(0.
+00002770: 2c20 312e 3031 2c20 312e 2c20 2e31 3032  , 1.01, 1., .102
+00002780: 292c 0d0a 2020 2020 2020 2020 2020 2020  ),..            
+00002790: 2020 2020 2020 6c6f 633d 332c 206e 636f        loc=3, nco
+000027a0: 6c3d 312c 206d 6f64 653d 2265 7870 616e  l=1, mode="expan
+000027b0: 6422 2c20 626f 7264 6572 6178 6573 7061  d", borderaxespa
+000027c0: 643d 302e 2c0d 0a20 2020 2020 2020 2020  d=0.,..         
+000027d0: 2020 2020 2020 2020 2070 726f 703d 7b22           prop={"
+000027e0: 7369 7a65 223a 2031 347d 290d 0a0d 0a20  size": 14}).... 
+000027f0: 2020 2020 2020 2023 2053 6574 206f 7264         # Set ord
+00002800: 6572 206f 6620 6c61 7965 7273 0d0a 2020  er of layers..  
+00002810: 2020 2020 2020 6178 2e73 6574 5f7a 6f72        ax.set_zor
+00002820: 6465 7228 3129 0d0a 2020 2020 2020 2020  der(1)..        
+00002830: 6178 2e70 6174 6368 2e73 6574 5f76 6973  ax.patch.set_vis
+00002840: 6962 6c65 2846 616c 7365 290d 0a0d 0a20  ible(False).... 
+00002850: 2020 2020 2020 2064 656c 2064 665f 706c         del df_pl
+00002860: 6f74 0d0a 0d0a 2020 2020 2020 2020 706c  ot....        pl
+00002870: 742e 7469 6768 745f 6c61 796f 7574 2829  t.tight_layout()
+00002880: 0d0a 2020 2020 2020 2020 706c 742e 6d61  ..        plt.ma
+00002890: 7267 696e 7328 302e 3031 290d 0a0d 0a20  rgins(0.01).... 
+000028a0: 2020 2020 2020 2023 2053 686f 770d 0a20         # Show.. 
+000028b0: 2020 2020 2020 2070 6c74 2e73 686f 7728         plt.show(
+000028c0: 290d 0a                                  )..
```

### Comparing `pythonpredictions-cobra-1.1.0/cobra/evaluation/plotting_utils.py` & `pythonpredictions-cobra-1.1.1/cobra/evaluation/plotting_utils.py`

 * *Files 5% similar despite different names*

```diff
@@ -39,44 +39,48 @@
                  value_name=metric)
 
     # plot data
     with plt.style.context("seaborn-ticks"):
         fig, ax = plt.subplots(figsize=dim)
 
         ax = sns.barplot(x=metric, y="predictor", hue="split", data=df)
-        ax.set_title("Univariate Quality of Predictors")
+        ax.set_title("Univariate predictor quality", fontsize=20)
 
         # Set pretty axis
         sns.despine(ax=ax, right=True)
+        plt.ylabel("Predictor", fontsize=15)
+        plt.xlabel(metric, fontsize=15)
 
         # Remove white lines from the second axis
         ax.grid(False)
 
         if path is not None:
             plt.savefig(path, format="png", dpi=300, bbox_inches="tight")
 
+        plt.gca().legend().set_title("")
+
         plt.show()
 
 def plot_correlation_matrix(df_corr: pd.DataFrame,
                             dim: tuple=(12, 8),
                             path: str=None):
-    """Plot correlation matrix amongst the predictors.
+    """Plot correlation matrix of the predictors.
 
     Parameters
     ----------
     df_corr : pd.DataFrame
         Correlation matrix.
     dim : tuple, optional
         Width and length of the plot.
     path : str, optional
         Path to store the figure.
     """
     fig, ax = plt.subplots(figsize=dim)
-    ax = sns.heatmap(df_corr, cmap='Blues')
-    ax.set_title('Correlation Matrix')
+    ax = sns.heatmap(df_corr, cmap="Blues")
+    ax.set_title("Correlation matrix", fontsize=20)
 
     if path is not None:
         plt.savefig(path, format="png", dpi=300, bbox_inches="tight")
 
     plt.show()
 
 def plot_performance_curves(model_performance: pd.DataFrame,
@@ -146,15 +150,15 @@
             ax.set_ylim(0, max_metric*1.1)
 
         # Make pretty
         ax.legend(loc='lower right')
         fig.suptitle('Performance curves forward feature selection',
                      fontsize=20)
         plt.title("Metric: "+metric_name, fontsize=15, loc="left")
-        plt.ylabel('Model performance')
+        plt.ylabel('Model performance', fontsize=15)
 
         if path is not None:
             plt.savefig(path, format="png", dpi=300, bbox_inches="tight")
 
         plt.show()
 
 def plot_variable_importance(df_variable_importance: pd.DataFrame,
@@ -162,34 +166,36 @@
                              dim: tuple=(12, 8),
                              path: str=None):
     """Plot variable importance of a given model.
 
     Parameters
     ----------
     df_variable_importance : pd.DataFrame
-        DataFrame containing columns predictor and importance.
+        DataFrame containing columns "predictor" and "importance".
     title : str, optional
         Title of the plot.
     dim : tuple, optional
         Width and length of the plot.
     path : str, optional
         Path to store the figure.
     """
     with plt.style.context("seaborn-ticks"):
         fig, ax = plt.subplots(figsize=dim)
         ax = sns.barplot(x="importance", y="predictor",
                          data=df_variable_importance,
                          color="cornflowerblue")
         if title:
-            ax.set_title(title)
+            ax.set_title(title, fontsize=20)
         else:
-            ax.set_title("Variable importance")
+            ax.set_title("Variable importance", fontsize=20)
 
-        # Set Axis - make them pretty
+        # Make pretty axis
         sns.despine(ax=ax, right=True)
+        plt.ylabel('Predictor', fontsize=15)
+        plt.xlabel('Importance', fontsize=15)
 
         # Remove white lines from the second axis
         ax.grid(False)
 
         if path is not None:
             plt.savefig(path, format="png", dpi=300, bbox_inches="tight")
```

### Comparing `pythonpredictions-cobra-1.1.0/cobra/model_building/__init__.py` & `pythonpredictions-cobra-1.1.1/cobra/model_building/__init__.py`

 * *Files identical despite different names*

### Comparing `pythonpredictions-cobra-1.1.0/cobra/model_building/forward_selection.py` & `pythonpredictions-cobra-1.1.1/cobra/model_building/forward_selection.py`

 * *Files identical despite different names*

### Comparing `pythonpredictions-cobra-1.1.0/cobra/model_building/models.py` & `pythonpredictions-cobra-1.1.1/cobra/model_building/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -257,18 +257,17 @@
     linear : LinearRegression
         scikit-learn linear regression model.
     predictors : list
         List of predictors used in the model.
     """
 
     def __init__(self):
-        self.linear = LinearRegression(fit_intercept=True, normalize=False)
+        self.linear = LinearRegression(fit_intercept=True)
         self._is_fitted = False
-        # placeholder to keep track of a list of predictors
-        self.predictors = []
+        self.predictors = []  # placeholder to keep track of a list of predictors
         self._eval_metrics_by_split = {}
 
     def serialize(self) -> dict:
         """Serialize model as JSON.
 
         Returns
         -------
```

### Comparing `pythonpredictions-cobra-1.1.0/cobra/model_building/univariate_selection.py` & `pythonpredictions-cobra-1.1.1/cobra/model_building/univariate_selection.py`

 * *Files identical despite different names*

### Comparing `pythonpredictions-cobra-1.1.0/cobra/preprocessing/categorical_data_processor.py` & `pythonpredictions-cobra-1.1.1/cobra/preprocessing/categorical_data_processor.py`

 * *Files identical despite different names*

### Comparing `pythonpredictions-cobra-1.1.0/cobra/preprocessing/kbins_discretizer.py` & `pythonpredictions-cobra-1.1.1/cobra/preprocessing/kbins_discretizer.py`

 * *Files identical despite different names*

### Comparing `pythonpredictions-cobra-1.1.0/cobra/preprocessing/preprocessor.py` & `pythonpredictions-cobra-1.1.1/cobra/preprocessing/preprocessor.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,8 +1,7 @@
-
 # standard lib imports
 import inspect
 import time
 import math
 import logging
 from random import shuffle
 from datetime import datetime
@@ -15,14 +14,15 @@
 # custom imports
 from cobra.preprocessing import CategoricalDataProcessor
 from cobra.preprocessing import KBinsDiscretizer
 from cobra.preprocessing import TargetEncoder
 
 log = logging.getLogger(__name__)
 
+
 class PreProcessor(BaseEstimator):
     """This class implements a so-called facade pattern to define a
     higher-level interface to work with the CategoricalDataProcessor,
     KBinsDiscretizer and TargetEncoder classes, so that their fit and transform
     methods are called in the correct order.
 
     Additionally, it provides methods such as (de)serialization to/from JSON
@@ -44,47 +44,51 @@
     is_fitted : bool
         Whether or not object is yet fit.
     model_type : str
         The model_type variable as specified in CategoricalDataProcessor
         (``classification`` or ``regression``).
     """
 
-    def __init__(self,
-                 categorical_data_processor: CategoricalDataProcessor,
-                 discretizer: KBinsDiscretizer,
-                 target_encoder: TargetEncoder,
-                 is_fitted: bool = False):
+    def __init__(
+        self,
+        categorical_data_processor: CategoricalDataProcessor,
+        discretizer: KBinsDiscretizer,
+        target_encoder: TargetEncoder,
+        is_fitted: bool = False,
+    ):
 
         self._categorical_data_processor = categorical_data_processor
         self._discretizer = discretizer
         self._target_encoder = target_encoder
 
         self._is_fitted = is_fitted
 
         self.model_type = categorical_data_processor.model_type
 
     @classmethod
-    def from_params(cls,
-                    model_type: str="classification",
-                    n_bins: int=10,
-                    strategy: str="quantile",
-                    closed: str="right",
-                    auto_adapt_bins: bool=False,
-                    starting_precision: int=0,
-                    label_format: str="{} - {}",
-                    change_endpoint_format: bool=False,
-                    regroup: bool=True,
-                    regroup_name: str="Other",
-                    keep_missing: bool=True,
-                    category_size_threshold: int=5,
-                    p_value_threshold: float=0.001,
-                    scale_contingency_table: bool=True,
-                    forced_categories: dict={},
-                    weight: float=0.0,
-                    imputation_strategy: str="mean"):
+    def from_params(
+        cls,
+        model_type: str = "classification",
+        n_bins: int = 10,
+        strategy: str = "quantile",
+        closed: str = "right",
+        auto_adapt_bins: bool = False,
+        starting_precision: int = 0,
+        label_format: str = "{} - {}",
+        change_endpoint_format: bool = False,
+        regroup: bool = True,
+        regroup_name: str = "Other",
+        keep_missing: bool = True,
+        category_size_threshold: int = 5,
+        p_value_threshold: float = 0.001,
+        scale_contingency_table: bool = True,
+        forced_categories: dict = {},
+        weight: float = 0.0,
+        imputation_strategy: str = "mean",
+    ):
         """Constructor to instantiate PreProcessor from all the parameters
         that can be set in all its required (attribute) classes
         along with good default values.
 
         Parameters
         ----------
         model_type : str
@@ -143,29 +147,36 @@
             particular variable.
 
         Returns
         -------
         PreProcessor
             Class encapsulating CategoricalDataProcessor,
             KBinsDiscretizer, and TargetEncoder instances.
-        """       
-        categorical_data_processor = CategoricalDataProcessor(model_type,
-                                                              regroup,
-                                                              regroup_name, keep_missing,
-                                                              category_size_threshold,
-                                                              p_value_threshold,
-                                                              scale_contingency_table,
-                                                              forced_categories)
-        
-        discretizer = KBinsDiscretizer(n_bins, strategy, closed,
-                                       auto_adapt_bins,
-                                       starting_precision,
-                                       label_format,
-                                       change_endpoint_format)
-                
+        """
+        categorical_data_processor = CategoricalDataProcessor(
+            model_type,
+            regroup,
+            regroup_name,
+            keep_missing,
+            category_size_threshold,
+            p_value_threshold,
+            scale_contingency_table,
+            forced_categories,
+        )
+
+        discretizer = KBinsDiscretizer(
+            n_bins,
+            strategy,
+            closed,
+            auto_adapt_bins,
+            starting_precision,
+            label_format,
+            change_endpoint_format,
+        )
+
         target_encoder = TargetEncoder(weight, imputation_strategy)
 
         return cls(categorical_data_processor, discretizer, target_encoder)
 
     @classmethod
     def from_pipeline(cls, pipeline: dict):
         """Constructor to instantiate PreProcessor from a (fitted) pipeline
@@ -185,94 +196,184 @@
         ------
         ValueError
             If the loaded pipeline does not have all required parameters
             and no others.
         """
 
         if not PreProcessor._is_valid_pipeline(pipeline):
-            raise ValueError("Invalid pipeline, as it does not "
-                             "contain all and only the required parameters.")
+            raise ValueError(
+                "Invalid pipeline, as it does not "
+                "contain all and only the required parameters."
+            )
 
         categorical_data_processor = CategoricalDataProcessor()
         categorical_data_processor.set_attributes_from_dict(
             pipeline["categorical_data_processor"]
         )
         # model_type = categorical_data_processor.model_type
 
         discretizer = KBinsDiscretizer()
         discretizer.set_attributes_from_dict(pipeline["discretizer"])
 
         target_encoder = TargetEncoder()
         target_encoder.set_attributes_from_dict(pipeline["target_encoder"])
 
-        return cls(categorical_data_processor, discretizer, target_encoder,
-                   is_fitted=pipeline["_is_fitted"])
+        return cls(
+            categorical_data_processor,
+            discretizer,
+            target_encoder,
+            is_fitted=pipeline["_is_fitted"],
+        )
+        
+    def get_continuous_and_discrete_columns(
+        self, df: pd.DataFrame, id_col_name: str, target_column_name: str
+    ) -> tuple:
+        """Filters out the continuous and discrete  variables out of a dataframe and returns a tuple containing lists of column names
+        It assumes that numerical columns with less than or equal to 10 different values are categorical
+
+        Parameters
+        ----------
+        df : pd.DataFrame
+            DataFrame that you want to divide in discrete and continuous variables
+        id_col_name : str
+            column name of the id column, can be None
+        target_column_name : str
+            column name of the target column
+
+        Returns
+        -------
+        tuple
+            tuple containing 2 lists of column names. (continuous_vars, discrete_vars)
+        """
+        if id_col_name == None:
+            log.warning(
+                "id_col_name is equal to None. If there is no id column ignore this warning"
+            )
+
+        # find continuous_vars and discrete_vars in the dateframe
+        col_dtypes = df.dtypes
+        discrete_vars = [
+            col
+            for col in col_dtypes[col_dtypes == object].index.tolist()
+            if col not in [id_col_name, target_column_name]
+        ]
+
+        for col in df.columns:
+            if col not in discrete_vars and col not in [
+                id_col_name,
+                target_column_name,
+            ]:  # omit discrete because a string, and target
+                val_counts = df[col].nunique()
+                if (
+                    val_counts > 1 and val_counts <= 10
+                ):  # the column contains less than 10 different values
+                    discrete_vars.append(col)
+
+        continuous_vars = list(
+            set(df.columns)
+            - set(discrete_vars)
+            - set([id_col_name, target_column_name])
+        )
+        log.warning(
+            f"""Cobra automaticaly assumes that following variables are 
+            discrete: {discrete_vars}
+            continuous: {continuous_vars}
+            If you want to change this behaviour you can specify the discrete/continuous variables yourself with the continuous_vars and discrete_vars keywords.
+            It assumes that numerical columns with less than or equal to 10 different values are categorical"""
+        )
+        return continuous_vars, discrete_vars
 
-    def fit(self, train_data: pd.DataFrame, continuous_vars: list,
-            discrete_vars: list, target_column_name: str):
+    def fit(
+        self,
+        train_data: pd.DataFrame,
+        continuous_vars: list,
+        discrete_vars: list,
+        target_column_name: str,
+        id_col_name: str = None,
+    ):
         """Fit the data to the preprocessing pipeline.
+        If you put continuous_vars and target_vars equal to `None` and give the id_col_name Cobra will guess which variables are continuous and which are not.
 
         Parameters
         ----------
         train_data : pd.DataFrame
             Data to be preprocessed.
-        continuous_vars : list
-            List of continuous variables.
-        discrete_vars : list
-            List of discrete variables.
+        continuous_vars : list | None
+            List of continuous variables, can be None.
+        discrete_vars : list | None
+            List of discrete variables, can be None.
         target_column_name : str
             Column name of the target.
+        id_col_name : str, optional
+            _description_, by default None
         """
+        if not (continuous_vars and discrete_vars):
+            continuous_vars, discrete_vars = self.get_continuous_and_discrete_columns(
+                df=train_data,
+                id_col_name=id_col_name,
+                target_column_name=target_column_name,
+            )
 
         # get list of all variables
-        preprocessed_variable_names = (PreProcessor
-                                       ._get_variable_list(continuous_vars,
-                                                           discrete_vars))
+        preprocessed_variable_names = PreProcessor._get_variable_list(
+            continuous_vars, discrete_vars
+        )
 
         log.info("Starting to fit pipeline")
         start = time.time()
 
         # Ensure to operate on separate copy of data
         train_data = train_data.copy()
 
+        # drop NAN columns if they exist
+        train_data = (
+            PreProcessor._check_nan_columns_and_drop_columns_containing_only_nan(
+                train_data
+            )
+        )
+
         # Fit discretizer, categorical preprocessor & target encoder
         # Note that in order to fit target_encoder, we first have to transform
         # the data using the fitted discretizer & categorical_data_processor
         if continuous_vars:
             begin = time.time()
             self._discretizer.fit(train_data, continuous_vars)
-            log.info("Fitting KBinsDiscretizer took {} seconds"
-                     .format(time.time() - begin))
+            log.info(
+                "Fitting KBinsDiscretizer took {} seconds".format(time.time() - begin)
+            )
 
-            train_data = self._discretizer.transform(train_data,
-                                                     continuous_vars)
+            train_data = self._discretizer.transform(train_data, continuous_vars)
         if discrete_vars:
             begin = time.time()
-            self._categorical_data_processor.fit(train_data,
-                                                 discrete_vars,
-                                                 target_column_name)
-            log.info("Fitting categorical_data_processor class took {} seconds"
-                     .format(time.time() - begin))
-
-            train_data = (self._categorical_data_processor
-                          .transform(train_data, discrete_vars))
+            self._categorical_data_processor.fit(
+                train_data, discrete_vars, target_column_name
+            )
+            log.info(
+                "Fitting categorical_data_processor class took {} seconds".format(
+                    time.time() - begin
+                )
+            )
+
+            train_data = self._categorical_data_processor.transform(
+                train_data, discrete_vars
+            )
 
         begin = time.time()
-        self._target_encoder.fit(train_data, preprocessed_variable_names,
-                                 target_column_name)
-        log.info("Fitting TargetEncoder took {} seconds"
-                 .format(time.time() - begin))
+        self._target_encoder.fit(
+            train_data, preprocessed_variable_names, target_column_name
+        )
+        log.info("Fitting TargetEncoder took {} seconds".format(time.time() - begin))
 
         self._is_fitted = True  # set fitted boolean to True
 
-        log.info("Fitting pipeline took {} seconds"
-                 .format(time.time() - start))
+        log.info("Fitting pipeline took {} seconds".format(time.time() - start))
 
-    def transform(self, data: pd.DataFrame, continuous_vars: list,
-                  discrete_vars: list) -> pd.DataFrame:
+    def transform(
+        self, data: pd.DataFrame, continuous_vars: list, discrete_vars: list
+    ) -> pd.DataFrame:
         """Transform the data by applying the preprocessing pipeline.
 
         Parameters
         ----------
         data : pd.DataFrame
             Data to be preprocessed.
         continuous_vars : list
@@ -289,71 +390,90 @@
         ------
         NotFittedError
             In case PreProcessor was not fitted first.
         """
 
         start = time.time()
 
+        # Ensure to operate on separate copy of data
+        data = data.copy()
+
         if not self._is_fitted:
-            msg = ("This {} instance is not fitted yet. Call 'fit' with "
-                   "appropriate arguments before using this method.")
+            msg = (
+                "This {} instance is not fitted yet. Call 'fit' with "
+                "appropriate arguments before using this method."
+            )
 
             raise NotFittedError(msg.format(self.__class__.__name__))
 
-        preprocessed_variable_names = (PreProcessor
-                                       ._get_variable_list(continuous_vars,
-                                                           discrete_vars))
+        preprocessed_variable_names = PreProcessor._get_variable_list(
+            continuous_vars, discrete_vars
+        )
 
         if continuous_vars:
             data = self._discretizer.transform(data, continuous_vars)
 
         if discrete_vars:
-            data = self._categorical_data_processor.transform(data,
-                                                              discrete_vars)
+            data = self._categorical_data_processor.transform(data, discrete_vars)
 
-        data = self._target_encoder.transform(data,
-                                              preprocessed_variable_names)
+        data = self._target_encoder.transform(data, preprocessed_variable_names)
 
-        log.info("Transforming data took {} seconds"
-                 .format(time.time() - start))
+        log.info("Transforming data took {} seconds".format(time.time() - start))
 
         return data
 
-    def fit_transform(self, train_data: pd.DataFrame, continuous_vars: list,
-                      discrete_vars: list,
-                      target_column_name: str) -> pd.DataFrame:
+    def fit_transform(
+        self,
+        train_data: pd.DataFrame,
+        continuous_vars: list,
+        discrete_vars: list,
+        target_column_name: str,
+        id_col_name: str = None,
+    ) -> pd.DataFrame:
+
         """Fit preprocessing pipeline and transform the data.
+        If you put continuous_vars and target_vars equal to `None` and give the id_col_name Cobra will guess which variables are continuous and which are not.
 
         Parameters
         ----------
         train_data : pd.DataFrame
             Data to be preprocessed
         continuous_vars : list
-            List of continuous variables.
+            List of continuous variables, can be None.
         discrete_vars : list
-            List of discrete variables.
+            List of discrete variables, can be None.
         target_column_name : str
             Column name of the target.
+        id_col_name : str, optional
+            _description_, by default None
 
         Returns
         -------
         pd.DataFrame
             Transformed (preprocessed) data.
         """
-
-        self.fit(train_data, continuous_vars, discrete_vars,
-                 target_column_name)
+        if not (continuous_vars and discrete_vars) and id_col_name:
+            continuous_vars, discrete_vars = self.get_continuous_and_discrete_columns(
+                df=train_data,
+                id_col_name=id_col_name,
+                target_column_name=target_column_name,
+            )
+        self.fit(
+            train_data, continuous_vars, discrete_vars, target_column_name, id_col_name
+        )
 
         return self.transform(train_data, continuous_vars, discrete_vars)
 
     @staticmethod
-    def train_selection_validation_split(data: pd.DataFrame,
-                                         train_prop: float=0.6,
-                                         selection_prop: float=0.2,
-                                         validation_prop: float=0.2) -> pd.DataFrame:
+    def train_selection_validation_split(
+        data: pd.DataFrame,
+        train_prop: float = 0.6,
+        selection_prop: float = 0.2,
+        validation_prop: float = 0.2,
+    ) -> pd.DataFrame:
         """Adds `split` column with train/selection/validation values
         to the dataset.
 
         Train set = data on which the model is trained and on which the encoding is based.
         Selection set = data used for univariate and forward feature selection. Often called the validation set.
         Validation set = data that generates the final performance metrics. Often called the test set.
 
@@ -370,62 +490,63 @@
 
         Returns
         -------
         pd.DataFrame
             DataFrame with additional split column.
         """
         if not math.isclose(train_prop + selection_prop + validation_prop, 1.0):
-            raise ValueError("The sum of train_prop, selection_prop and "
-                             "validation_prop must be 1.0.")
+            raise ValueError(
+                "The sum of train_prop, selection_prop and "
+                "validation_prop must be 1.0."
+            )
 
         if train_prop == 0.0:
             raise ValueError("train_prop cannot be zero!")
 
         if selection_prop == 0.0:
             raise ValueError("selection_prop cannot be zero!")
 
         nrows = data.shape[0]
         size_train = int(train_prop * nrows)
         size_select = int(selection_prop * nrows)
         size_valid = int(validation_prop * nrows)
-        correction = nrows - (size_train+size_select+size_valid)
+        correction = nrows - (size_train + size_select + size_valid)
 
-        split = ['train'] * size_train \
-                + ['train'] * correction \
-                + ['selection'] * size_select \
-                + ['validation'] * size_valid
+        split = (
+            ["train"] * size_train
+            + ["train"] * correction
+            + ["selection"] * size_select
+            + ["validation"] * size_valid
+        )
 
         shuffle(split)
 
-        data['split'] = split
+        data["split"] = split
 
         return data
 
     def serialize_pipeline(self) -> dict:
         """Serialize the preprocessing pipeline by writing all its required
         parameters to a dictionary to later store it as a JSON file.
 
         Returns
         -------
         dict
             Return the pipeline as a dictionary.
         """
         pipeline = {
-            "metadata": {
-                "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
-            }
+            "metadata": {"timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
         }
 
-        pipeline["categorical_data_processor"] = (self
-                                                  ._categorical_data_processor
-                                                  .attributes_to_dict())
+        pipeline[
+            "categorical_data_processor"
+        ] = self._categorical_data_processor.attributes_to_dict()
 
         pipeline["discretizer"] = self._discretizer.attributes_to_dict()
-        pipeline["target_encoder"] = (self._target_encoder
-                                      .attributes_to_dict())
+        pipeline["target_encoder"] = self._target_encoder.attributes_to_dict()
 
         pipeline["_is_fitted"] = True
 
         return pipeline
 
     @staticmethod
     def _is_valid_pipeline(pipeline: dict) -> bool:
@@ -434,21 +555,21 @@
 
         Parameters
         ----------
         pipeline : dict
             Loaded pipeline from JSON file.
         """
         keys = inspect.getfullargspec(PreProcessor.from_params).args
-        valid_keys = set([key for key in keys
-                          if key not in ["cls", "serialization_path"]])
+        valid_keys = set(
+            [key for key in keys if key not in ["cls", "serialization_path"]]
+        )
 
         input_keys = set()
         for key in pipeline:
-            if key in ["categorical_data_processor", "discretizer",
-                       "target_encoder"]:
+            if key in ["categorical_data_processor", "discretizer", "target_encoder"]:
                 input_keys = input_keys.union(set(pipeline[key].keys()))
             elif key != "metadata":
                 input_keys.add(key)
 
         input_keys = sorted(list(input_keys))
         input_keys = [key for key in input_keys if not key.startswith("_")]
 
@@ -472,14 +593,63 @@
             Merged list of predictors with proper suffixes added.
 
         Raises
         ------
         ValueError
             In case both lists are empty.
         """
-        var_list = ([col + "_processed" for col in discrete_vars]
-                    + [col + "_bin" for col in continuous_vars])
+        var_list = [col + "_processed" for col in discrete_vars] + [
+            col + "_bin" for col in continuous_vars
+        ]
 
         if not var_list:
             raise ValueError("Variable var_list is None or empty list.")
 
         return var_list
+
+    def _check_nan_columns_and_drop_columns_containing_only_nan(
+        data: pd.DataFrame,
+    ) -> pd.DataFrame:
+        """Checks how much missing values are in the dataframe and drops columns that contain only missing values.
+        It also logs an error message displaying the percentage of missing values in the different columns
+        (columns are only displayed if they contain a missing values)
+
+        Parameters
+        ----------
+        data : pd.DataFrame
+            Data that should be checked for columns that contain only missing values
+
+        Returns
+        -------
+        pd.DataFrame
+            Data without columns containing only missing values
+        """
+        # Ensure to operate on separate copy of data
+        data = data.copy()
+
+        # Check how much NaN values are in each variable
+        # and output a warning if a variable has more than 0% of missing values
+
+        perc_na = data.isna().mean() * 100
+
+        if not perc_na[perc_na > 0].empty:
+            logging.warning(
+                "\nPercentage of missing values per variable:\n"
+                + perc_na[perc_na > 0]
+                .round(2)
+                .to_string(float_format=lambda x: str(x) + "%")
+            )
+
+        # drop variables that have only missing values
+        to_drop = [
+            perc_na.index[i]
+            for i, percentage in enumerate(perc_na)
+            if percentage == 100
+        ]
+
+        if to_drop:
+            data = data.drop(to_drop, axis=1)
+            logging.warning(
+                f"Following variables contain only missing values and were dropped: {to_drop}"
+            )
+
+        return data
```

### Comparing `pythonpredictions-cobra-1.1.0/cobra/preprocessing/target_encoder.py` & `pythonpredictions-cobra-1.1.1/cobra/preprocessing/target_encoder.py`

 * *Files identical despite different names*

### Comparing `pythonpredictions-cobra-1.1.0/pythonpredictions_cobra.egg-info/PKG-INFO` & `pythonpredictions-cobra-1.1.1/pythonpredictions_cobra.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,16 +1,15 @@
 Metadata-Version: 2.1
 Name: pythonpredictions-cobra
-Version: 1.1.0
+Version: 1.1.1
 Summary: A Python package to build predictive linear and logistic regression models focused on performance and interpretation.
 Home-page: https://github.com/PythonPredictions/cobra
 Author: Python Predictions
 Author-email: cobra@pythonpredictions.com
 License: MIT
-Platform: UNKNOWN
 Description-Content-Type: text/x-rst
 License-File: LICENSE
 
 
 .. image:: https://github.com/PythonPredictions/cobra/raw/master/material/logo.png
     :width: 700
 
@@ -50,15 +49,15 @@
 ------------
 
 This package requires only the usual Python libraries for data science, being numpy, pandas, scipy, scikit-learn, matplotlib, seaborn, and tqdm. These packages, along with their versions are listed in ``requirements.txt`` and can be installed using ``pip``:    ::
 
   pip install -r requirements.txt
 
 
-**Note**: if you want to install Cobra with e.g. pip, you don't have to install all of these requirements as these are automatically installed with Cobra itself.
+**Note**: if you want to install Cobra with e.g. pip, you don't have to install all these requirements as these are automatically installed with Cobra itself.
 
 Installation
 ------------
 
 The easiest way to install Cobra is using ``pip``:    ::
 
   pip install -U pythonpredictions-cobra
@@ -69,22 +68,18 @@
 
 - A `blog post <https://www.pythonpredictions.com/news/the-little-trick-we-apply-to-obtain-explainability-by-design/>`_ on the overall methodology.
 
 - A `research article <https://doi.org/10.1016/j.dss.2016.11.007>`_ by Geert Verstraeten (co-founder Python Predictions) discussing the preprocessing approach we use in Cobra.
 
 - HTML documentation of the `individual modules <https://pythonpredictions.github.io/cobra.io/docstring/modules.html>`_.
 
-- A step-by-step `tutorial <https://pythonpredictions.github.io/cobra/tutorials/tutorial_Cobra_logistic_regression.ipynb>`_ for **logistic regression**.
-
-- A step-by-step `tutorial <https://pythonpredictions.github.io/cobra/tutorials/tutorial_Cobra_linear_regression.ipynb>`__ for **linear regression**.
+- Step-by-step `tutorials <https://github.com/PythonPredictions/cobra/blob/master/tutorials>`_ for a logistic and a linear regression use case.
 
 - Check out the Data Science Leuven Meetup `talk <https://www.youtube.com/watch?v=w7ceZZqMEaA&feature=youtu.be>`_ by one of the core developers (second presentation). His `slides <https://github.com/PythonPredictions/Cobra-DS-meetup-Leuven/blob/main/DS_Leuven_meetup_20210209_cobra.pdf>`_ and `related material <https://github.com/PythonPredictions/Cobra-DS-meetup-Leuven>`_ are also available.
 
 Contributing to Cobra
 =====================
 
 We'd love you to contribute to the development of Cobra! There are many ways in which you can contribute, the most common of which is to contribute to the source code or documentation of the project. However, there are many other ways you can contribute (report issues, improve code coverage by adding unit tests, ...).
 We use GitHub issues to track all bugs and feature requests. Feel free to open an issue in case you found a bug or in case you wish to see a new feature added.
 
 For more details, check out our `wiki <https://github.com/PythonPredictions/cobra/wiki/Contributing-guidelines-&-workflows>`_.
-
-
```

### Comparing `pythonpredictions-cobra-1.1.0/pythonpredictions_cobra.egg-info/SOURCES.txt` & `pythonpredictions-cobra-1.1.1/pythonpredictions_cobra.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pythonpredictions-cobra-1.1.0/setup.py` & `pythonpredictions-cobra-1.1.1/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -9,25 +9,26 @@
 
 # The text of the README file
 README = (ROOT / "README.rst").read_text()
 
 setup(
     name="pythonpredictions-cobra",
     version=__version__,
-    description=("A Python package to build predictive linear and logistic regression "
-                 "models focused on performance and interpretation."),
+    description=("A Python package to build predictive linear and logistic "
+                 "regression models focused on performance and "
+                 "interpretation."),
     long_description=README,
     long_description_content_type="text/x-rst",
     packages=find_packages(include=["cobra", "cobra.*"]),
     url="https://github.com/PythonPredictions/cobra",
     license="MIT",
     author="Python Predictions",
     author_email="cobra@pythonpredictions.com",
     install_requires=[
         "numpy>=1.19.4",
-        "pandas>=1.1.5",
+        "pandas>=1.1.5,<2.0",
         "scipy>=1.5.4",
         "scikit-learn>=0.24.1",
         "matplotlib>=3.4.3",
         "seaborn>=0.11.0",
         "tqdm>=4.62.2"]
 )
```

