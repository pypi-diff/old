# Comparing `tmp/django-jsheet-0.1.9.tar.gz` & `tmp/django_jsheet-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-jsheet-0.1.9.tar", last modified: Mon Apr  3 20:41:47 2023, max compression
+gzip compressed data, was "django_jsheet-0.2.0.tar", last modified: Thu Apr  6 09:32:16 2023, max compression
```

## Comparing `django-jsheet-0.1.9.tar` & `django_jsheet-0.2.0.tar`

### file list

```diff
@@ -1,20 +1,21 @@
-drwxr-xr-x   0 shadmod    (501) admin       (80)        0 2023-04-03 20:41:47.695307 django-jsheet-0.1.9/
--rw-r--r--   0 shadmod    (501) admin       (80)     1064 2023-04-02 11:32:45.000000 django-jsheet-0.1.9/LICENSE
--rw-r--r--   0 shadmod    (501) admin       (80)     1155 2023-04-03 20:41:47.694882 django-jsheet-0.1.9/PKG-INFO
--rw-r--r--   0 shadmod    (501) admin       (80)      178 2023-04-02 11:43:17.000000 django-jsheet-0.1.9/README.md
--rw-r--r--   0 shadmod    (501) admin       (80)     1085 2023-04-03 20:40:53.000000 django-jsheet-0.1.9/pyproject.toml
--rw-r--r--   0 shadmod    (501) admin       (80)       38 2023-04-03 20:41:47.695434 django-jsheet-0.1.9/setup.cfg
-drwxr-xr-x   0 shadmod    (501) admin       (80)        0 2023-04-03 20:41:47.688086 django-jsheet-0.1.9/src/
-drwxr-xr-x   0 shadmod    (501) admin       (80)        0 2023-04-03 20:41:47.690111 django-jsheet-0.1.9/src/django-jsheet/
--rw-r--r--   0 shadmod    (501) admin       (80)        0 2023-04-02 09:53:41.000000 django-jsheet-0.1.9/src/django-jsheet/__init__.py
-drwxr-xr-x   0 shadmod    (501) admin       (80)        0 2023-04-03 20:41:47.690700 django-jsheet-0.1.9/src/django-jsheet/core/
--rw-r--r--   0 shadmod    (501) admin       (80)        0 2023-04-02 09:53:41.000000 django-jsheet-0.1.9/src/django-jsheet/core/__init__.py
--rw-r--r--   0 shadmod    (501) admin       (80)    11745 2023-04-02 21:06:19.000000 django-jsheet-0.1.9/src/django-jsheet/core/django_sheet.py
-drwxr-xr-x   0 shadmod    (501) admin       (80)        0 2023-04-03 20:41:47.692082 django-jsheet-0.1.9/src/django-jsheet/templatetags/
--rw-r--r--   0 shadmod    (501) admin       (80)        0 2023-03-06 19:49:48.000000 django-jsheet-0.1.9/src/django-jsheet/templatetags/__init__.py
--rw-r--r--   0 shadmod    (501) admin       (80)     5623 2023-04-02 07:52:11.000000 django-jsheet-0.1.9/src/django-jsheet/templatetags/jsheet.py
-drwxr-xr-x   0 shadmod    (501) admin       (80)        0 2023-04-03 20:41:47.694296 django-jsheet-0.1.9/src/django_jsheet.egg-info/
--rw-r--r--   0 shadmod    (501) admin       (80)     1155 2023-04-03 20:41:47.000000 django-jsheet-0.1.9/src/django_jsheet.egg-info/PKG-INFO
--rw-r--r--   0 shadmod    (501) admin       (80)      384 2023-04-03 20:41:47.000000 django-jsheet-0.1.9/src/django_jsheet.egg-info/SOURCES.txt
--rw-r--r--   0 shadmod    (501) admin       (80)        1 2023-04-03 20:41:47.000000 django-jsheet-0.1.9/src/django_jsheet.egg-info/dependency_links.txt
--rw-r--r--   0 shadmod    (501) admin       (80)       14 2023-04-03 20:41:47.000000 django-jsheet-0.1.9/src/django_jsheet.egg-info/top_level.txt
+drwxr-xr-x   0 shadmod    (501) admin       (80)        0 2023-04-06 09:32:16.900966 django_jsheet-0.2.0/
+-rw-r--r--   0 shadmod    (501) admin       (80)     1064 2023-04-02 11:32:45.000000 django_jsheet-0.2.0/LICENSE
+-rw-r--r--   0 shadmod    (501) admin       (80)     1153 2023-04-06 09:32:16.900466 django_jsheet-0.2.0/PKG-INFO
+-rw-r--r--   0 shadmod    (501) admin       (80)      176 2023-04-05 21:03:08.000000 django_jsheet-0.2.0/README.md
+-rw-r--r--   0 shadmod    (501) admin       (80)     1085 2023-04-05 22:48:00.000000 django_jsheet-0.2.0/pyproject.toml
+-rw-r--r--   0 shadmod    (501) admin       (80)       38 2023-04-06 09:32:16.901102 django_jsheet-0.2.0/setup.cfg
+drwxr-xr-x   0 shadmod    (501) admin       (80)        0 2023-04-06 09:32:16.891602 django_jsheet-0.2.0/src/
+drwxr-xr-x   0 shadmod    (501) admin       (80)        0 2023-04-06 09:32:16.894656 django_jsheet-0.2.0/src/django_jsheet/
+-rw-r--r--   0 shadmod    (501) admin       (80)        0 2023-04-02 09:53:41.000000 django_jsheet-0.2.0/src/django_jsheet/__init__.py
+drwxr-xr-x   0 shadmod    (501) admin       (80)        0 2023-04-06 09:32:16.898113 django_jsheet-0.2.0/src/django_jsheet/core/
+-rw-r--r--   0 shadmod    (501) admin       (80)        0 2023-04-02 09:53:41.000000 django_jsheet-0.2.0/src/django_jsheet/core/__init__.py
+-rw-r--r--   0 shadmod    (501) admin       (80)    10692 2023-04-05 22:40:28.000000 django_jsheet-0.2.0/src/django_jsheet/core/django_sheet.py
+-rw-r--r--   0 shadmod    (501) admin       (80)       88 2023-04-05 21:00:16.000000 django_jsheet-0.2.0/src/django_jsheet/core/forms.py
+drwxr-xr-x   0 shadmod    (501) admin       (80)        0 2023-04-06 09:32:16.899410 django_jsheet-0.2.0/src/django_jsheet/templatetags/
+-rw-r--r--   0 shadmod    (501) admin       (80)        0 2023-03-06 19:49:48.000000 django_jsheet-0.2.0/src/django_jsheet/templatetags/__init__.py
+-rw-r--r--   0 shadmod    (501) admin       (80)     5753 2023-04-05 22:38:08.000000 django_jsheet-0.2.0/src/django_jsheet/templatetags/jsheet.py
+drwxr-xr-x   0 shadmod    (501) admin       (80)        0 2023-04-06 09:32:16.896364 django_jsheet-0.2.0/src/django_jsheet.egg-info/
+-rw-r--r--   0 shadmod    (501) admin       (80)     1153 2023-04-06 09:32:16.000000 django_jsheet-0.2.0/src/django_jsheet.egg-info/PKG-INFO
+-rw-r--r--   0 shadmod    (501) admin       (80)      416 2023-04-06 09:32:16.000000 django_jsheet-0.2.0/src/django_jsheet.egg-info/SOURCES.txt
+-rw-r--r--   0 shadmod    (501) admin       (80)        1 2023-04-06 09:32:16.000000 django_jsheet-0.2.0/src/django_jsheet.egg-info/dependency_links.txt
+-rw-r--r--   0 shadmod    (501) admin       (80)       14 2023-04-06 09:32:16.000000 django_jsheet-0.2.0/src/django_jsheet.egg-info/top_level.txt
```

### Comparing `django-jsheet-0.1.9/LICENSE` & `django_jsheet-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `django-jsheet-0.1.9/PKG-INFO` & `django_jsheet-0.2.0/src/django_jsheet.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-jsheet
-Version: 0.1.9
+Version: 0.2.0
 Summary: A small example package
 Author-email: ShadMod <support@shadmod.it>
 Maintainer-email: Brett Cannon <brett@python.org>
 License: MIT License
 Project-URL: Homepage, https://github.com/shadMod/django-jsheet
 Project-URL: Bug Tracker, https://github.com/shadMod/django-jsheet/issues
 Keywords: Django JSheet,Django-JSheet,Django_JSheet
@@ -24,8 +24,8 @@
 
 # Django JSheet
 
 Django JSheet is a little tool to render a simple excel sheet in webpage
 
 There are many around, but mine is cooler because it's made by me .-.
 
-Good luck! \o/``
+Good luck! \o/
```

### Comparing `django-jsheet-0.1.9/pyproject.toml` & `django_jsheet-0.2.0/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 [project]
-name = "django-jsheet"
-version = "0.1.9"
+name = "django_jsheet"
+version = "0.2.0"
 authors = [
     { name = "ShadMod", email = "support@shadmod.it" },
 ]
 maintainers = [
     { name = "Brett Cannon", email = "brett@python.org" }
 ]
 description = "A small example package"
```

### Comparing `django-jsheet-0.1.9/src/django-jsheet/core/django_sheet.py` & `django_jsheet-0.2.0/src/django_jsheet/core/django_sheet.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,54 +1,20 @@
-from decimal import Decimal
-from datetime import datetime
-
-from django.db.models.base import ModelBase
-from django.db.models.fields.files import FieldFile
 from django.urls import reverse_lazy
-from django.utils import timezone
-
-
-def cls_encode(value):
-    type_ = "text"
-    if value is None:
-        value = ""
-    if isinstance(value, int) or isinstance(value, Decimal) or isinstance(value, float):
-        type_ = "text"
-        value = str(value)
-    if isinstance(value, datetime):
-        type_ = "datetime-local"
-        # default to run jquery "%Y-%m-%dT%H:%M" // dont change!
-        value = value.strftime("%Y-%m-%dT%H:%M")
-    if type(type(value)) == ModelBase:
-        model_ = value.__class__
-        pk_ = str(value.pk)
-        type_ = "__select__/{0}/{1}".format(model_.__name__, pk_)
-        value = [(x.pk, x.__str__()) for x in model_.objects.all()]
-    if isinstance(value, FieldFile):
-        type_ = "text"
-        value = value.__str__()
-    return value, type_
 
 
 class DjangoSheet:
     """
     :param header: header of sheet (th), this param set the lenght of sheet
     :type header: list
     :param jquery: (QuerySet, form_class.base_fields)
     :type jquery: tuple
 
     :return: [ReturnDescription]
     :rtype: [ReturnType]
     """
-
-    # header = []
-    # jquery = {}
-    # colWidths = None
-    # alignWidths = None
-    # empty_row = 0
     force_clm = False
 
     def __init__(
             self,
             header,
             jquery,
             colWidths,
@@ -56,19 +22,17 @@
             empty_row,
             force_clm=force_clm,
     ):
         self.header = header
         self.jquery = jquery
         self.colWidths = colWidths
         self.alignWidths = alignWidths
-        self.force_clm = force_clm
         self.empty_row = empty_row
-
+        self.force_clm = force_clm
         self.set_header = []
-        self.set_header2 = self.set_header
 
     @property
     def len_row(self):
         return len(self.jquery[0])
 
     @property
     def len_row_sum(self):
@@ -95,18 +59,63 @@
                 for i in range(self.len_clm):
                     colWidths.append(self.colWidths)
             if isinstance(self.colWidths, list):
                 colWidths = self.colWidths
         return colWidths
 
     @property
-    def set_header2(self):
+    def set_cell(self):
+        """
+        :return:    {
+                        "title": "txt",
+                        "initial": "txt",
+                        "query": "array",  # only with choices and modelChoices
+                        "width": 160,
+                        "align": "center",  # left, center, right
+                        "input": "text",  # text, number, float, choices, modelChoices
+                    }
+        :rtype:     dict
+        """
         data = []
-        for label, field in self.jquery[1].items():
-            data.append((label, field.__class__.__name__))
+
+        for i, label in enumerate(self.jquery[1].keys()):
+            field = self.jquery[1][label]
+            field_class = field.__class__.__name__
+
+            # init cell dict
+            cell = {
+                "title": label,
+                "initial": "",
+                "width": self.set_col_width[i],
+                "align": self.alignWidths,
+            }
+
+            # set all types
+            if field_class == 'CharField':
+                cell["input"] = "text"
+            if field_class == 'FloatField':
+                cell["input"] = "text"
+            if field_class == 'DateTimeField' or field_class == 'DateField':
+                cell["input"] = "datetime-local"
+            if field_class == 'FileField':
+                cell["input"] = "file"
+            if field_class == 'TypedChoiceField':
+                cell["input"] = "__choices__"
+                cell["query"] = getattr(self.jquery[0][0].__class__, label).field.choices
+            if field_class == 'ModelChoiceField':
+                cell["input"] = "__select__"
+                # set default empty select
+                cell["query"] = [("0", "None")]
+                if len(self.jquery[0]) >= 1:
+                    model_ = getattr(self.jquery[0][0], label).__class__
+                    if model_.__name__ != "NoneType":
+                        cell["title"] = model_.__name__
+                        cell["query"] = [(x.pk, x.__str__()) for x in model_.objects.all()]
+
+            data.append(cell)
         return data
 
     @property
     def dict_jsheet(self):
         return {
             "class_table": None,
             "setup": {
@@ -120,94 +129,49 @@
         }
 
     @property
     def header_sheet(self):
         thead = []
         for i, value in enumerate(self.header):
             header_ = {
-                "title": value,
+                "title": value.capitalize(),
                 "value": value,
                 "width": self.set_col_width[i],
                 "align": self.alignWidths,
             }
             thead.append(header_)
         return thead
 
     @property
     def init_data(self):
         if isinstance(self.jquery, tuple):
             query = self.jquery[0]
             order_by = list(self.jquery[1].keys())
         else:
-            query = []
-            order_by = []
+            raise
 
         init_data = {}
         for i, g in enumerate(query):
             data = []
             # TODO: if form has '__all__' in field, what do you do?
             if isinstance(order_by, list):
-                for x in order_by:
-                    if getattr(g.__class__, x).field.choices:
-                        type_ = "__choices__/{}".format(getattr(g, x))
-                        value = getattr(g.__class__, x).field.choices
-                    else:
-                        value, type_ = cls_encode(getattr(g, x))
-
-                    if i == 0:
-                        if '__select__' in type_:
-                            self.set_header.append((type_, value))
-                        elif '__choices__' in type_:
-                            self.set_header.append((type_, value))
+                for j, x in enumerate(order_by):
+                    value_dict = self.set_cell[j]
+                    value = getattr(g, x)
+                    if value:
+                        if value_dict["input"] == "__select__":
+                            value_dict["initial"] = value.pk
                         else:
-                            self.set_header.append(type_)
+                            value_dict["initial"] = value
 
-                    title = None
-                    selected = None
-                    if '__select__' in type_:
-                        type_, title, selected = type_.split("/")
-                    if '__choices__' in type_:
-                        type_, selected = type_.split("/")
-
-                    value_dict = {
-                        "title": title,
-                        "value": value,
-                        "selected": selected,
-                        "width": self.colWidths,
-                        "align": self.alignWidths,
-                        "input": type_,
-                    }
                     data.append(value_dict)
             init_data[g.pk] = data
 
         for g in range(self.empty_row):
-            data = []
-            for type_ in self.set_header:
-                title = None
-                if isinstance(type_, tuple):
-                    type_, value = type_
-                    if "__choices__" in type_:
-                        type_, title = type_.split("/")
-                    else:
-                        type_, title, _ = type_.split("/")
-                else:
-                    if type_ == "datetime-local":
-                        value = timezone.now().strftime("%Y-%m-%dT%H:%M")
-                    else:
-                        value = ""
-
-                value_dict = {
-                    "title": title,
-                    "value": value,
-                    "width": self.colWidths,
-                    "align": self.alignWidths,
-                    "input": type_,
-                }
-                data.append(value_dict)
-            init_data[f"empty_{g}"] = data
+            init_data[f"empty_{g}"] = self.set_cell
 
         return init_data
 
     @property
     def js_script_row(self):
         # TODO: replace static splice with dynamic splice:
         #   get all input select and splice values in row_v
```

### Comparing `django-jsheet-0.1.9/src/django-jsheet/templatetags/jsheet.py` & `django_jsheet-0.2.0/src/django_jsheet/templatetags/jsheet.py`

 * *Files 5% similar despite different names*

```diff
@@ -78,39 +78,43 @@
         td_query = data["body"][key_]
         for td_ in td_query:
             if isinstance(td_, dict):
                 tbody += "<td width='{width}' align='{align}'>".format(
                     width=td_.get("width", ""), align=td_.get("align", "")
                 )
                 input_type = td_.get("input", "")
-                value = td_.get("value", "")
+                initial = td_.get("initial", "")
+                # select ModelChoiceField
                 if input_type == '__select__':
-                    selected = td_.get("selected", "")
+                    initial = td_.get("initial", "")
+                    query = td_.get("query", "")
                     tbody += "<select id='{title}{i}'>".format(i=i, title=td_.get("title", ""))
-                    for val_, label in value:
-                        if str(selected) == str(val_):
+                    for val_, label in query:
+                        if str(initial) == str(val_):
                             target = "selected"
                         else:
                             target = ""
                         tbody += "<option value='{0}' {2}>{1}</option>".format(val_, label, target)
                     tbody += "</select></td>"
+                # select TypedChoiceField
                 elif input_type == "__choices__":
-                    selected = td_.get("selected", "")
+
+                    query = td_.get("query", "")
                     tbody += "<select id='Choices{i}'>".format(i=i)
-                    for val_, label in value:
-                        if str(selected) == str(val_):
+                    for val_, label in query:
+                        if str(initial) == str(val_):
                             target = "selected"
                         else:
                             target = ""
                         tbody += "<option value='{0}' {2}>{1}</option>".format(val_, label, target)
                     tbody += "</select></td>"
                 else:
                     tbody += """
                         <input type="{input}" value="{value}"></td>
-                    """.format(i=i, input=input_type, value=value)
+                    """.format(i=i, input=input_type, value=initial)
             else:
                 raise
         tbody += "</tr>"
     tbody += "</tbody>"
 
     js_script = data.get("jsrows", "")
     jsfooter = data["jsfooter"]
```

### Comparing `django-jsheet-0.1.9/src/django_jsheet.egg-info/PKG-INFO` & `django_jsheet-0.2.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: django-jsheet
-Version: 0.1.9
+Name: django_jsheet
+Version: 0.2.0
 Summary: A small example package
 Author-email: ShadMod <support@shadmod.it>
 Maintainer-email: Brett Cannon <brett@python.org>
 License: MIT License
 Project-URL: Homepage, https://github.com/shadMod/django-jsheet
 Project-URL: Bug Tracker, https://github.com/shadMod/django-jsheet/issues
 Keywords: Django JSheet,Django-JSheet,Django_JSheet
@@ -24,8 +24,8 @@
 
 # Django JSheet
 
 Django JSheet is a little tool to render a simple excel sheet in webpage
 
 There are many around, but mine is cooler because it's made by me .-.
 
-Good luck! \o/``
+Good luck! \o/
```

