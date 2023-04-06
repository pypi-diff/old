# Comparing `tmp/bsmschema-0.0.3.tar.gz` & `tmp/bsmschema-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/chris/Projects/bids/stats-models/bsmschema/dist/tmpysj5mww7/bsmschema-0.0.3.tar", last modified: Sun Sep  4 22:18:51 2022, max compression
+gzip compressed data, last modified: Sun Feb  2 00:00:00 2020, max compression
```

## Comparing `bsmschema-0.0.3.tar` & `bsmschema-0.0.4.tar`

### file list

```diff
@@ -1,14 +1,9 @@
-drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-09-04 22:18:51.344612 bsmschema-0.0.3/
--rw-rw-r--   0 chris     (1000) chris     (1000)      547 2022-09-04 22:18:51.344612 bsmschema-0.0.3/PKG-INFO
-drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-09-04 22:18:51.344612 bsmschema-0.0.3/bsmschema/
--rw-rw-r--   0 chris     (1000) chris     (1000)       21 2022-05-11 01:34:20.000000 bsmschema-0.0.3/bsmschema/__init__.py
--rw-rw-r--   0 chris     (1000) chris     (1000)      442 2022-05-11 01:34:20.000000 bsmschema-0.0.3/bsmschema/__main__.py
--rw-rw-r--   0 chris     (1000) chris     (1000)    21508 2022-09-04 22:16:23.000000 bsmschema-0.0.3/bsmschema/models.py
-drwxrwxr-x   0 chris     (1000) chris     (1000)        0 2022-09-04 22:18:51.344612 bsmschema-0.0.3/bsmschema.egg-info/
--rw-rw-r--   0 chris     (1000) chris     (1000)      547 2022-09-04 22:18:51.000000 bsmschema-0.0.3/bsmschema.egg-info/PKG-INFO
--rw-rw-r--   0 chris     (1000) chris     (1000)      252 2022-09-04 22:18:51.000000 bsmschema-0.0.3/bsmschema.egg-info/SOURCES.txt
--rw-rw-r--   0 chris     (1000) chris     (1000)        1 2022-09-04 22:18:51.000000 bsmschema-0.0.3/bsmschema.egg-info/dependency_links.txt
--rw-rw-r--   0 chris     (1000) chris     (1000)        9 2022-09-04 22:18:51.000000 bsmschema-0.0.3/bsmschema.egg-info/requires.txt
--rw-rw-r--   0 chris     (1000) chris     (1000)       15 2022-09-04 22:18:51.000000 bsmschema-0.0.3/bsmschema.egg-info/top_level.txt
--rw-rw-r--   0 chris     (1000) chris     (1000)       60 2022-05-11 01:34:20.000000 bsmschema-0.0.3/pyproject.toml
--rw-rw-r--   0 chris     (1000) chris     (1000)      597 2022-09-04 22:18:51.344612 bsmschema-0.0.3/setup.cfg
+-rw-r--r--   0        0        0       21 2020-02-02 00:00:00.000000 bsmschema-0.0.4/bsmschema/__init__.py
+-rw-r--r--   0        0        0      442 2020-02-02 00:00:00.000000 bsmschema-0.0.4/bsmschema/__main__.py
+-rw-r--r--   0        0        0    21586 2020-02-02 00:00:00.000000 bsmschema-0.0.4/bsmschema/models.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 bsmschema-0.0.4/bsmschema/py.typed
+-rw-r--r--   0        0        0      200 2020-02-02 00:00:00.000000 bsmschema-0.0.4/.gitignore
+-rw-r--r--   0        0        0    11360 2020-02-02 00:00:00.000000 bsmschema-0.0.4/LICENSE
+-rw-r--r--   0        0        0      787 2020-02-02 00:00:00.000000 bsmschema-0.0.4/README.md
+-rw-r--r--   0        0        0     1006 2020-02-02 00:00:00.000000 bsmschema-0.0.4/pyproject.toml
+-rw-r--r--   0        0        0    14534 2020-02-02 00:00:00.000000 bsmschema-0.0.4/PKG-INFO
```

### Comparing `bsmschema-0.0.3/bsmschema/models.py` & `bsmschema-0.0.4/bsmschema/models.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,17 +11,16 @@
       * :py:class:`DummyContrasts`
    * :py:class:`Edge`
 
 Note that these are the structured and validatable objects.
 
 """
 import sys
-from enum import Enum
-from typing import List, Optional, Dict, Literal, Any, Union
-from pydantic import BaseModel, StrictStr, StrictInt, StrictFloat
+from typing import List, Optional, Dict, Literal, Any, Union, TYPE_CHECKING
+from pydantic import BaseModel, Extra
 
 __all__ = [
     'BIDSStatsModel',
     'Node',
     'Edge',
     'Transformations',
     'Model',
@@ -29,18 +28,20 @@
     'Options',
     'Contrast',
     'DummyContrasts',
 ]
 
 # Hack to avoid unnecessary verbosity when generating documentation
 # Has no impact on emitted JSON, only on whether Python will attempt to cast instead of error
-if 'sphinxcontrib.autodoc_pydantic' in sys.modules:
-    StrictStr = str
-    StrictInt = int
-    StrictFloat = float
+if not TYPE_CHECKING and 'sphinxcontrib.autodoc_pydantic' in sys.modules:
+    StrictStr = str      # noqa: F811
+    StrictInt = int      # noqa: F811
+    StrictFloat = float  # noqa: F811
+else:
+    from pydantic import StrictStr, StrictInt, StrictFloat
 
 # Notes
 # HRF model parameters are unclear how to specify
 # Transformation instructions should be doable (if tedious), but unclear
 # how to make the restriction to them contingent on Transformer == "pybids-transforms-v1"
 # Skipping Variance structure and Error distribution for now
 
@@ -76,21 +77,24 @@
 
 # Aliases
 Filter = Dict[StrictStr, List[Any]]
 VariableList = List[Union[Literal[1], StrictStr]]
 Weights = List[Union[StrictInt, StrictFloat, StrictStr]]
 
 
-class _Commentable(BaseModel):
+class _BSMBase(BaseModel):
     # Docstring missing to avoid polluting every object description with this field
     # This permits users to write comments on objects.
     Description: Optional[str]
 
+    class Config:
+        extra = Extra.forbid
 
-class Edge(_Commentable):
+
+class Edge(_BSMBase):
     r"""An Edge connects two :py:class:`Node`\s, indicating the outputs (contrasts) of
     the :py:attr:`Source` Node are to be made available as inputs to the
     :py:attr:`Destination` Node.
 
     Contrasts may be filtered by any metadata field, including entities.
     Each contrast has an additional entity ``"contrast"`` that may be used to filter contrasts by name.
 
@@ -120,15 +124,15 @@
     If :py:attr:`Filter` is defined,
     The outputs of the Source node are the inputs of the Destination node, after filtering (if any)."""
     Filter: Optional[Filter]
     """Maps a grouping variable to a list of values to pass to Destination.
     If multiple grouping variables are passed, the result is the conjunction of filters."""
 
 
-class Transformations(_Commentable):
+class Transformations(_BSMBase):
     """Transformations describe modifications of variables to prepare a design matrix.
 
     This field is indirect, with a :py:attr:`Transformer` name identifying an instruction
     set, and a sequence of :py:attr:`Instructions`.
 
     A Transformer accepts data frames of sparse (onset, duration, amplitude) and
     dense (onset, sampling rate, values) variables along with the list of Instructions,
@@ -158,15 +162,15 @@
     Transformer: TransformerID
     """Name of the specification of an instruction set."""
     Instructions: List[Any]
     """Sequence of instructions to pass to an implementation of :py:attr:`Transformer`.
     The format of these instructions is determined by the :py:attr:`Transformer`."""
 
 
-class HRF(_Commentable):
+class HRF(_BSMBase):
     """Specification of a hemodynamic response function (HRF) model.
 
     Most design matrix constructors permit sparse events of the form
     (onset, duration, amplitude) to be convolved by a named HRF,
     possibly with some parameters.
     Some may permit dense time series to be convolved as well.
 
@@ -212,15 +216,15 @@
     """Parameters to the hemodynamic model.
 
     Options will be software specific and are not controlled.
     For ``"fir"``, the parameter ``"fir_delays"`` is required.
     """
 
 
-class Options(_Commentable):
+class Options(_BSMBase):
     """Estimation options that are common to multiple estimation packages."""
     HighPassFilterCutoffHz: Optional[float]
     """The cutoff frequency, in Hz, for a high-pass filter."""
     LowPassFilterCutoffHz: Optional[float]
     """The cutoff frequency, in Hz, for a low-pass filter."""
     ReplaceVariables: Optional[Dict[StrictStr, Any]]
     """Allows a specification of design matrix columns that are to be replaced by the estimating software.
@@ -238,15 +242,15 @@
     The following values are valid: "none", "mean", "pca".
     "none" (the default) indicates no dimensionality reduction; a separate timecourse is returned for each voxel
     that contains at least one non-zero value in its timecourse.
     "mean" returns the average of all voxels within each discrete non-zero value found in the image.
     "pca" returns the first principal component of all voxels within each discrete non-zero value found in the image."""
 
 
-class Contrast(_Commentable):
+class Contrast(_BSMBase):
     r"""Contrasts are weighted sums of parameter estimates (betas) generated by a model fit.
 
     ``Contrast`` defines the structure of the elements of the :py:attr:`Node.Contrasts` list.
 
     Along with :py:class:`DummyContrasts`, Contrasts define the outputs of a :py:class:`Node`.
 
     While ``"t"`` and ``"pass"`` contrasts are passed as inputs to the next node, ``"F"``
@@ -308,15 +312,15 @@
     r"""The type of test statistic to compute on the contrast.
     The special value ``"pass"`` indicates that no statistical test is to be performed.
 
     Note that ``"F"`` contrasts are terminal and not passed as inputs to following
     :py:class:`Node`\s."""
 
 
-class DummyContrasts(_Commentable):
+class DummyContrasts(_BSMBase):
     r"""Dummy contrasts are contrasts with one condition, a weight of one,
     and the same name as the condition. That is,
 
     ::
 
         "DummyContrasts": {"Contrasts": ["A", "B"], "Test": "t"}
 
@@ -339,15 +343,15 @@
     r"""The type of test statistic to compute on the contrast.
     The special value "pass" indicates that no statistical test is to be performed.
 
     Note that ``"F"`` contrasts are terminal and not passed as inputs to following
     :py:class:`Node`\s."""
 
 
-class Model(_Commentable):
+class Model(_BSMBase):
     """The model to fit to the collection of input images.
 
     This section defines the design matrix construction, estimator type,
     and additional options needed to estimate the model parameters.
     """
     Type: ModelType
     """The type of analysis to run.
@@ -387,15 +391,15 @@
     Each key in the object is the name of the software package (FSL, SPM, etc.),
     and the value is an object containing software-specific parameters.
     The BIDS Stats Models spec makes no attempt to control the vocabulary available for
     use in any particular software package;
     we expect that the developers of each package will, over time, fill in these specifications."""
 
 
-class Node(_Commentable):
+class Node(_BSMBase):
     """A node represents an estimator that applies to a given level of analysis.
     It contains sufficient information to construct a design matrix, estimate
     parameter weights (betas) and construct contrasts.
     """
     Level: NodeLevel
     """Level of analysis being described."""
     Name: StrictStr
@@ -418,15 +422,15 @@
     to generate contrast maps and (optionally) run statistical tests."""
     DummyContrasts: Optional[DummyContrasts]
     """A convenient shortcut for specifying contrasts;
     allows automatic creation of indicator contrasts
     for either all variables in the design matrix, or all named variables."""
 
 
-class BIDSStatsModel(_Commentable):
+class BIDSStatsModel(_BSMBase):
     """A BIDS Stats Model is a JSON file that defines one or more hierarchical models
     on brain imaging data.
 
     A hierarchical model is a sequence of estimator **nodes**. These nodes are connected
     via **edges** to form a directed, acyclic graph. The graph contains a single "root"
     node, which only has outgoing edges, and may have many "leaf" nodes that only have
     incoming edges. Each path from the root to a leaf may be thought of as a single
@@ -493,28 +497,27 @@
         {"IntField": 0}
 
     Invalid examples::
 
         {"IntField": 1.0}
         {"IntField": "2"}
     """
-    SomeOptions: Literal[1, "stringval", 2.0]
+    SomeOptions: Literal[1, "stringval"]
     """The ``Literal`` type allows a specific value or set of values.
 
     Valid examples::
 
         {"SomeOptions": 1}
         {"SomeOptions": "stringval"}
-        {"SomeOptions": 2.0}
 
     Invalid examples::
 
         {"SomeOptions": "1"}
         {"SomeOptions": "differentstringval"}
-        {"SomeOptions": 2}
+        {"SomeOptions": 2.0}
     """
     ArrayOfInts: List[str]
     """JSON arrays appear as ``List`` types, and ``List[str]`` means
     the values must be integers.
 
     Valid example::
```

