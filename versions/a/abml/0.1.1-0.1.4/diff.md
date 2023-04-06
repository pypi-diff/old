# Comparing `tmp/abml-0.1.1.tar.gz` & `tmp/abml-0.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "abml-0.1.1.tar", max compression
+gzip compressed data, was "abml-0.1.4.tar", max compression
```

## Comparing `abml-0.1.1.tar` & `abml-0.1.4.tar`

### file list

```diff
@@ -1,23 +1,24 @@
--rw-r--r--   0        0        0      586 2023-03-22 07:33:36.079432 abml-0.1.1/abml/__init__.py
--rw-r--r--   0        0        0    10264 2023-03-28 22:02:24.000000 abml-0.1.1/abml/abml_assembly.py
--rw-r--r--   0        0        0     3969 2023-03-22 07:48:31.449857 abml-0.1.1/abml/abml_bcs.py
--rw-r--r--   0        0        0        0 2023-03-27 09:39:35.000000 abml-0.1.1/abml/abml_config.py
--rw-r--r--   0        0        0     1280 2023-03-15 10:30:19.422097 abml-0.1.1/abml/abml_constraints.py
--rw-r--r--   0        0        0    17566 2023-03-29 09:56:34.014838 abml-0.1.1/abml/abml_dataclass.py
--rw-r--r--   0        0        0     6517 2023-03-28 20:51:27.000000 abml-0.1.1/abml/abml_helpers.py
--rw-r--r--   0        0        0     4177 2023-03-22 08:37:23.907979 abml-0.1.1/abml/abml_interaction_prop.py
--rw-r--r--   0        0        0     2107 2023-03-22 08:20:41.397361 abml-0.1.1/abml/abml_interactions.py
--rw-r--r--   0        0        0     5198 2023-03-28 12:54:48.239612 abml-0.1.1/abml/abml_jnl_loader.py
--rw-r--r--   0        0        0     1531 2023-03-21 14:08:55.673793 abml-0.1.1/abml/abml_jobs.py
--rw-r--r--   0        0        0     1779 2023-03-15 10:12:08.441083 abml-0.1.1/abml/abml_loads.py
--rw-r--r--   0        0        0     1657 2023-03-14 19:02:45.000000 abml-0.1.1/abml/abml_loggers.py
--rw-r--r--   0        0        0     4830 2023-03-28 19:17:12.000000 abml-0.1.1/abml/abml_materials.py
--rw-r--r--   0        0        0     6246 2023-03-22 10:24:36.906997 abml-0.1.1/abml/abml_mesh.py
--rw-r--r--   0        0        0    22187 2023-03-29 09:53:48.452203 abml-0.1.1/abml/abml_parts.py
--rw-r--r--   0        0        0      823 2023-03-14 07:49:32.486729 abml-0.1.1/abml/abml_sections.py
--rw-r--r--   0        0        0     4338 2023-03-29 10:42:42.555365 abml-0.1.1/abml/abml_sketch.py
--rw-r--r--   0        0        0      552 2023-03-21 10:29:46.264400 abml-0.1.1/abml/abml_steps.py
--rw-r--r--   0        0        0      381 2023-03-29 11:39:28.590776 abml-0.1.1/pyproject.toml
--rw-r--r--   0        0        0        0 2023-03-07 14:05:32.882361 abml-0.1.1/README.md
--rw-r--r--   0        0        0      673 1970-01-01 00:00:00.000000 abml-0.1.1/setup.py
--rw-r--r--   0        0        0      303 1970-01-01 00:00:00.000000 abml-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0      586 2023-03-22 07:33:36.000000 abml-0.1.4/abml/__init__.py
+-rw-r--r--   0        0        0    12263 2023-04-03 09:51:54.771609 abml-0.1.4/abml/abml_assembly.py
+-rw-r--r--   0        0        0     3969 2023-03-22 07:48:31.000000 abml-0.1.4/abml/abml_bcs.py
+-rw-r--r--   0        0        0        0 2023-03-27 09:39:35.423232 abml-0.1.4/abml/abml_config.py
+-rw-r--r--   0        0        0     1280 2023-03-15 10:30:19.000000 abml-0.1.4/abml/abml_constraints.py
+-rw-r--r--   0        0        0    18544 2023-04-06 12:53:25.948291 abml-0.1.4/abml/abml_dataclass.py
+-rw-r--r--   0        0        0     6639 2023-04-05 08:01:55.000000 abml-0.1.4/abml/abml_helpers.py
+-rw-r--r--   0        0        0     4223 2023-04-03 10:04:11.809675 abml-0.1.4/abml/abml_interaction_prop.py
+-rw-r--r--   0        0        0     2378 2023-04-05 08:02:24.000000 abml-0.1.4/abml/abml_interactions.py
+-rw-r--r--   0        0        0     5198 2023-03-28 12:54:48.000000 abml-0.1.4/abml/abml_jnl_loader.py
+-rw-r--r--   0        0        0     2494 2023-04-06 10:13:01.267344 abml-0.1.4/abml/abml_jobs.py
+-rw-r--r--   0        0        0     2028 2023-04-05 08:25:23.000000 abml-0.1.4/abml/abml_loads.py
+-rw-r--r--   0        0        0     1680 2023-04-05 06:54:56.000000 abml-0.1.4/abml/abml_loggers.py
+-rw-r--r--   0        0        0     4833 2023-03-30 12:29:52.222897 abml-0.1.4/abml/abml_materials.py
+-rw-r--r--   0        0        0     6246 2023-03-30 14:44:49.120625 abml-0.1.4/abml/abml_mesh.py
+-rw-r--r--   0        0        0    23005 2023-04-03 11:14:38.410167 abml-0.1.4/abml/abml_parts.py
+-rw-r--r--   0        0        0      823 2023-03-14 07:49:32.000000 abml-0.1.4/abml/abml_sections.py
+-rw-r--r--   0        0        0     4338 2023-04-05 07:47:19.000000 abml-0.1.4/abml/abml_sketch.py
+-rw-r--r--   0        0        0      552 2023-03-14 09:57:29.000000 abml-0.1.4/abml/abml_steps.py
+-rw-r--r--   0        0        0       22 2023-04-05 06:54:54.000000 abml-0.1.4/abml/logging.yaml
+-rw-r--r--   0        0        0      381 2023-04-06 14:17:11.729760 abml-0.1.4/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-03-07 14:05:32.000000 abml-0.1.4/README.md
+-rw-r--r--   0        0        0      673 1970-01-01 00:00:00.000000 abml-0.1.4/setup.py
+-rw-r--r--   0        0        0      303 1970-01-01 00:00:00.000000 abml-0.1.4/PKG-INFO
```

### Comparing `abml-0.1.1/abml/__init__.py` & `abml-0.1.4/abml/__init__.py`

 * *Files identical despite different names*

### Comparing `abml-0.1.1/abml/abml_assembly.py` & `abml-0.1.4/abml/abml_assembly.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,26 +1,33 @@
 from regionToolset import Region
 from abml_dataclass import Abml_Registry, to_object_key_mode, to_object_cmd_mode
 from abml_helpers import Abml_Helpers, cprint
 from abaqusConstants import ON, OFF, CARTESIAN
+from abaqusConstants import DELETE, SUPPRESS
 from numpy import array
 
 
 @Abml_Registry.register("assembly")
 class Abml_Assembly(Abml_Helpers):
-    def __init__(self, model, instances=None, surfaces=None, sets=None, commands=None, **kwargs):  # noqa
+    def __init__(self, model, **kwargs):  # noqa
         self.model = model
+        instances = kwargs.get("instances")
+        surfaces = kwargs.get("surfaces")
+        sets = kwargs.get("sets")
+        cut = kwargs.get("cut")
         if instances is not None:
             self.instances = to_object_key_mode(instances, "instances", model=self.model)
+        if cut is not None:
+            self.cuts = to_object_key_mode(cut, "cut", model=self.model)
         if surfaces is not None:
             self.surfaces = to_object_key_mode(surfaces, "assembly_surfaces", model=model, assembly=self)
         if sets is not None:
             self.sets = to_object_key_mode(sets, "assembly_sets", model=model, assembly=self)
-        if commands is not None:
-            self.commands = to_object_cmd_mode(commands, "assembly_commandss", model=model, assembly=self)
+        # if commands is not None:
+        #     self.commands = to_object_cmd_mode(commands, "assembly_commands", model=model, assembly=self)
 
     def get_seq_from_surface_list(self, surfaces):
         surfaces = self.convert_position_list(surfaces)
         instances = self.instances
         face_seq = None
 
         if surfaces is not None:
@@ -83,14 +90,48 @@
             if cell_seq is None:
                 cell_seq = seq
             elif seq is not None:
                 cell_seq += seq
         return cell_seq
 
 
+@Abml_Registry.register("cut")
+class Abml_Cut:
+    def __init__(self, name, model, **kwargs):
+        self.model = model
+        self.name = name
+        self.instances = array([kwargs["instance"]]).flatten()
+        self.cutters = array([kwargs["cutter"]]).flatten()
+        self.original_instance = kwargs.get("original_instance", "delete")
+
+        self.original_instance_map = {"delete": DELETE, "surpress": SUPPRESS, "place": SUPPRESS}
+
+        self.create()
+
+    def create(self):
+        cutting_instances = [self.model.a.instances[cutter] for cutter in self.cutters]
+
+        for instance in self.instances:
+            self.model.a.InstanceFromBooleanCut(
+                name="{}-1".format(self.name),
+                instanceToBeCut=self.model.a.instances[instance],
+                cuttingInstances=cutting_instances,
+                originalInstances=self.original_instance_map[self.original_instance],
+            )
+            if self.name in self.model.p:
+                del self.model.p[self.name]
+            self.model.p.changeKey(fromName="{}-1".format(self.name), toName=self.name)
+
+        if self.original_instance == "place":
+            del self.model.a.instances[self.name]
+            self.model.a.features.changeKey(fromName="{}-1-1".format(self.name), toName=self.name)
+            for cutter in cutting_instances:
+                self.model.a.features[cutter.name].resume()
+
+
 @Abml_Registry.register("instances")
 class Abml_Instance:
     def __init__(self, name, model, part, **kwargs):
         self.model = model
         self.name = name
         self.part = part
         self.dependent = kwargs.get("dependent", True)
@@ -103,16 +144,16 @@
 
         self.model.a.DatumCsysByDefault(CARTESIAN)
         self.model.a.Instance(dependent=dep_dict[self.dependent], name=self.name, part=self.model.p[self.part])
 
         if len(self.rotate) != 0:
             for rot_param in self.rotate:
                 angle = rot_param.get("angle")
-                axisDirection = rot_param.get("axisDirection")
-                axisPoint = rot_param.get("axisPoint")
+                axisDirection = rot_param.get("axis_direction")
+                axisPoint = rot_param.get("axis_point")
                 self.model.a.rotate(
                     angle=angle,
                     axisDirection=axisDirection,
                     axisPoint=axisPoint,
                     instanceList=(self.name,),
                 )
 
@@ -178,14 +219,19 @@
                 seq = None
             else:
                 seq = Region(edges=instance.edges[edge.index : edge.index + 1]).edges
         elif element.shape == (6,) and isinstance(element[0], (float, int)):  # getByBoundingBox
             edges = seq = instance.edges.getByBoundingBox(*element.astype(float))
             if len(edges) != 0:
                 seq = edges
+        elif isinstance(element.item(0), str):
+            if "point_on" in element.item(0):
+                instance_name, _ = element.item(0).split(".")
+                element = array([self.model.a.instances[instance_name].pointOn]).flatten()
+                seq = self.get_edge_sequence(element)
         return seq
 
 
 @Abml_Registry.register("assembly_surfaces")
 class Abml_Assembly_Surface(Abml_Helpers):
     def __init__(self, name, model, assembly, faces=None):
         self.name = name
```

### Comparing `abml-0.1.1/abml/abml_bcs.py` & `abml-0.1.4/abml/abml_bcs.py`

 * *Files identical despite different names*

### Comparing `abml-0.1.1/abml/abml_constraints.py` & `abml-0.1.4/abml/abml_constraints.py`

 * *Files identical despite different names*

### Comparing `abml-0.1.1/abml/abml_dataclass.py` & `abml-0.1.4/abml/abml_dataclass.py`

 * *Files 3% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 import sys
 import yaml
 from io import open
 from abaqus import mdb
 from abaqusConstants import STANDARD_EXPLICIT
 from abml import abml_helpers
 import interaction
+from abaqus import openMdb
 
 
 class Abml_Registry:
     registry = defaultdict(lambda: OrderedDict)
 
     @classmethod
     def register(cls, key):
@@ -23,16 +24,26 @@
 
         return decorator
 
 
 @Abml_Registry.register("cae")
 class Abml_Cae:
     def __init__(self, models, **kwargs):
+        self.kwargs = kwargs
+
+        cae_path = self.kwargs.get("cae", None)
+        cae_path = models.pop("cae") if "cae" in models else None
+        if cae_path is not None:
+            self.open_cae(cae_path)
+
         self.models = to_object_key_mode(models["models"], type_="models")
 
+    def open_cae(self, path):
+        openMdb(pathName=path)
+
     def save_cae(self, filename):
         mdb.saveAs(pathName=filename)
 
 
 @Abml_Registry.register("models")
 class Abml_Model:
     """
@@ -105,14 +116,15 @@
         Returns
         -------
         None
     """
 
     def __init__(self, name, **kwargs):
         self.name = name
+
         self.create()
         self.m, self.a, self.p = abml_helpers.get_objects(self.name)
         self.kwargs = kwargs
 
         self.materials = {}
         self.sections = {}
         self.parts = {}
@@ -123,15 +135,14 @@
         self.constraints = {}
         self.bcs = {}
         self.loads = {}
         self.jobs = {}
         self.sketches = {}
 
         self.create_instances(**kwargs)
-        self.create_modules(**kwargs)
 
     def create_instances(self, **kwargs):
         create_order = [
             self.create_sketches,
             self.create_materials,
             self.create_sections,
             self.create_parts,
@@ -139,19 +150,34 @@
             self.create_steps,
             self.create_interaction_props,
             self.create_interactions,
             self.create_constraints,
             self.create_bcs,
             self.create_loads,
             self.create_jobs,
+            self.create_modules,
         ]
 
         for creation in create_order:
             creation(**kwargs)
 
+    def update_nested_dict(self, nested_dict, update_dict):
+        """
+        Recursively update a nested dictionary with a dictionary of key-value pairs
+        if the keys are not already present.
+        """
+        for k, v in update_dict.iteritems():
+            if isinstance(v, dict):
+                # Recursively update nested dictionaries
+                nested_dict[k] = self.update_nested_dict(nested_dict.get(k, {}), v)
+            elif k not in nested_dict:
+                # Key is not present, update the dictionary
+                nested_dict[k] = v
+        return nested_dict
+
     def create_sketches(self, **kwargs):
         sketches_list = [value for key, value in kwargs.items() if "sketches" in key]
         for sketches in sketches_list:
             if sketches is not None:
                 sketches = OrderedDict(sorted(sketches.items()))
 
                 sketch_name = sketches.keys()[0]
@@ -196,24 +222,22 @@
                 self.interaction_props.update(to_object_key_mode(steps, "steps", model=self))
 
     def create_interaction_props(self, **kwargs):
         interaction_props_list = [value for key, value in self.kwargs.items() if "interaction_props" in key]
         for interaction_props in interaction_props_list:
             if interaction_props is not None:
                 interaction_props = OrderedDict(sorted(interaction_props.items()))
-                self.interaction_props.update(
-                    to_object_key_mode(interaction_props, "interaction_properties", model=self)
-                )
+                self.interaction_props.update(to_object_key_mode(interaction_props, "interaction_props", model=self))
 
     def create_interactions(self, **kwargs):
         interactions_list = [value for key, value in kwargs.items() if "interactions" in key]
         for interactions in interactions_list:
             if interactions is not None:
                 interactions = OrderedDict(sorted(interactions.items()))
-                self.interactions.udpate(to_object_key_mode(interactions, "interactions", model=self))
+                self.interactions.update(to_object_key_mode(interactions, "interactions", model=self))
 
     def create_constraints(self, **kwargs):
         constraints_list = [value for key, value in kwargs.items() if "constraints" in key]
         for constraints in constraints_list:
             if constraints is not None:
                 constraints = OrderedDict(sorted(constraints.items()))
                 self.constraints.update(to_object_key_mode(constraints, "constraints", model=self))
@@ -236,23 +260,31 @@
         jobs_list = [value for key, value in kwargs.items() if "jobs" in key]
         for jobs in jobs_list:
             if jobs is not None:
                 jobs = OrderedDict(sorted(jobs.items()))
                 self.jobs.update(to_object_key_mode(jobs, "jobs", model=self))
 
     def create_modules(self, **kwargs):
-        modules_list = [value for key, value in kwargs.items() if "modules" in key]
         modules_list = kwargs.get("modules", [])
+        # abml_helpers.cprint("############## {}".format(modules_list[0]))
+        modules_list = [value for key, value in kwargs.items() if "modules" in key]
+        # abml_helpers.cprint(modules_list[0])
         for modules in modules_list:
             if modules is not None:
-                modules = OrderedDict(sorted(modules.items()))
-                self.modules = self.create_instances(**modules)
+                if isinstance(modules, dict):
+                    modules = OrderedDict(sorted(modules.items()))
+                    self.create_instances(**modules)
+                elif isinstance(modules, list):
+                    for module in modules:
+                        module = OrderedDict(sorted(module.items()))
+                        self.create_instances(**module)
 
     def create(self):
-        mdb.Model(modelType=STANDARD_EXPLICIT, name=self.name)
+        if self.name not in mdb.models.keys():
+            mdb.Model(modelType=STANDARD_EXPLICIT, name=self.name)
 
         if "Model-1" in mdb.models.keys():
             del mdb.models["Model-1"]
 
 
 def data_to_object(data, type_="models", key_based=True, **kwargs):
     """
@@ -454,23 +486,12 @@
     -----
     This function expects the `data` dictionary to be hierarchical, with each key representing an attribute
     name and each value representing the attribute value. If a value is itself a dictionary, the attribute
     is treated as a sub-object, and this function is recursively called to create the sub-object. The `type_`
     parameter specifies the name of the class to create the object from, and must be a string that matches the
     name of a class registered with the `Abml_Registry.registry` dictionary.
 
-    Examples
-    --------
-    **python
-    >>> data = {'name': 'Alice', 'age': 25, 'address': {'street': '123 Main St', 'city': 'Anytown'}}
-    >>> obj = to_object_hierarchy_mode(data, 'Person', occupation='Engineer')
-    >>> obj.name
-    'Alice'
-    >>> obj.address.city
-    'Anytown'
-    >>> obj.occupation
-    'Engineer'
     """
     data.update(kwargs)
     object_ = Abml_Registry.registry[type_](**data)
 
     return object_
```

### Comparing `abml-0.1.1/abml/abml_helpers.py` & `abml-0.1.4/abml/abml_helpers.py`

 * *Files 3% similar despite different names*

```diff
@@ -242,7 +242,11 @@
     """
 
     m = mdb.models[model_name]
     a = m.rootAssembly
     p = m.parts
 
     return m, a, p
+
+
+def get_kwargs_string(**kwargs):
+    return " ".join(["{}:{}".format(key, value) for key, value in kwargs.items()])
```

### Comparing `abml-0.1.1/abml/abml_interaction_prop.py` & `abml-0.1.4/abml/abml_interaction_prop.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 from abaqusConstants import FRICTIONLESS, PENALTY, ISOTROPIC, FRACTION
 from abaqusConstants import HARD, DEFAULT
 from abaqusConstants import ALL_NODES
 from abaqusConstants import ON, OFF
 
 
 @Abml_Registry.register("interaction_properties")
+@Abml_Registry.register("interaction_props")
 class Abml_Interaction_Prop:
     def __init__(self, name, type, behaviors, model, **kwargs):  # noqa
         self.name = name
         self.type = type
         self.model = model
 
         self.create()
```

### Comparing `abml-0.1.1/abml/abml_jnl_loader.py` & `abml-0.1.4/abml/abml_jnl_loader.py`

 * *Files identical despite different names*

### Comparing `abml-0.1.1/abml/abml_jobs.py` & `abml-0.1.4/abml/abml_jobs.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,28 +1,30 @@
 from abml_dataclass import Abml_Registry
 
 # from abml_helpers import cprint
 from abaqus import mdb
 from abaqusConstants import ANALYSIS, DEFAULT, OFF
 import os
 from shutil import copy, move
+from io import open
+from abml_helpers import cprint
 
 
 @Abml_Registry.register("jobs")
 class Abml_Job:
     def __init__(self, name, model, **kwargs):  # noqa
         self.name = str(name)
         self.model = model
         self.kwargs = kwargs
         self.create()
 
     def create(self):
         subroutine_flag = self.kwargs.get("subroutine", False)
         if subroutine_flag:
-            subroutine_path = os.path.abspath("subs.for")
+            subroutine_path = os.path.abspath("{}.for".format(self.name))
         else:
             subroutine_path = None
 
         kwargs = {
             "name": self.name,
             "model": self.model.name,
             "description": self.kwargs.get("description", ""),
@@ -31,19 +33,37 @@
             "numCpus": self.kwargs.get("cpus", 1),
             "numGPUs": self.kwargs.get("gpus", 0),
             "multiprocessingMode": DEFAULT,
         }
 
         mdb.Job(**kwargs)
 
+        if self.kwargs.get("write_input", False):
+            self.write_input()
+            self.add_to_header(subroutine="{}.inp".format(self.name), priority=self.kwargs.get("priority", "default"))
+
     def write_input(self):
         mdb.jobs[self.name].writeInput(consistencyChecking=OFF)
 
     def write_and_copy_input_to_path(self, path):
         self.write_input()
+        self.add_to_header(subroutine="{}.inp".format(self.name), priority=self.kwargs.get("priority", "default"))
         filename = "{}.inp".format(self.name)
         copy(filename, os.path.join(path, filename))
 
     def write_and_move_input_to_path(self, path):
         self.write_input()
+        self.add_to_header(subroutine="{}.inp".format(self.name), priority=self.kwargs.get("priority", "default"))
         filename = "{}.inp".format(self.name)
         move(filename, os.path.join(path, filename))
+
+    def add_to_header(self, **kwargs):
+        filename = "{}.inp".format(self.name)
+        with open(filename, "r", encoding="utf-8") as f:
+            input_file = f.readlines()
+
+        for key, value in kwargs.items():
+            input_file.insert(1, "** {key}={value}\n".format(key=key, value=value))
+
+        with open(filename, "w", encoding="utf-8") as f:
+            input_file = "".join(input_file)
+            f.write(input_file)
```

### Comparing `abml-0.1.1/abml/abml_loads.py` & `abml-0.1.4/abml/abml_loads.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,11 +1,14 @@
 from abml_dataclass import Abml_Registry
-from abml_helpers import Abml_Helpers, cprint
+from abml_helpers import Abml_Helpers, cprint, get_kwargs_string
 from abaqusConstants import USER_DEFINED, UNSET, UNIFORM
 from regionToolset import Region
+import logging
+
+logger = logging.getLogger("abml_logger")
 
 
 @Abml_Registry.register("loads")
 class Abml_Loads(Abml_Helpers):
     def __init__(self, name, model, type, **kwargs):  # noqa
         self.name = name
         self.model = model
@@ -13,20 +16,23 @@
         self.kwargs = kwargs
         self.map = {"pressure": self.pressure, "gravity": self.gravity}
         self.distribution_type_map = {
             "user_defined": USER_DEFINED,
             "uniform": UNIFORM,
         }
 
+        logger.debug(get_kwargs_string(model=model.name, name=name, type=type))
+
         self.create()
 
     def create(self):
         self.map[self.type]()
 
     def pressure(self):
+        logger.debug(get_kwargs_string(type="pressure", faces=self.kwargs["faces"]))
         kwargs = {
             "name": self.name,
             "createStepName": self.kwargs["step"],
             "region": Region(side1Faces=self.model.assembly.get_seq_from_surface_list(self.kwargs["faces"])),
             "distributionType": self.distribution_type_map[self.kwargs.get("distribution_type", "uniform")],
             "magnitude": self.kwargs.get("magnitude", 0.0),
             "amplitude": self.kwargs.get("amplitude", UNSET),
```

### Comparing `abml-0.1.1/abml/abml_loggers.py` & `abml-0.1.4/abml/abml_loggers.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,10 @@
-# import logging
+import logging
+import logging.config
+
 
 # debug_level = logging.CRITICAL
 
 # parts_logger = logging.getLogger("abml.parser")
 # parts_logger.addHandler(logging.FileHandler("parser.log", encoding="utf-8", mode="w"))
 # parts_logger.setLevel(debug_level)
 # parts_logger.propagate = False
```

### Comparing `abml-0.1.1/abml/abml_materials.py` & `abml-0.1.4/abml/abml_materials.py`

 * *Files 0% similar despite different names*

```diff
@@ -42,15 +42,15 @@
             density: 1e-9
           elastic:
             type: isotropic
             E: 450
             nu: 0.3
     """
 
-    def __init__(self, model, name, behaviors, description="", **kwargs):  # noqa
+    def __init__(self, model, name, behaviors={}, description="", **kwargs):  # noqa
         self.model = model
         self.description = description
         self.name = name
         self.create()
         self.behaviors = to_object_key_based_type(behaviors, material=self)
 
     def create(self):
```

### Comparing `abml-0.1.1/abml/abml_mesh.py` & `abml-0.1.4/abml/abml_mesh.py`

 * *Files identical despite different names*

### Comparing `abml-0.1.1/abml/abml_parts.py` & `abml-0.1.4/abml/abml_parts.py`

 * *Files 2% similar despite different names*

```diff
@@ -60,14 +60,17 @@
     """
 
     def __init__(self, name, model, **kwargs):  # noqa
         self.model = model
         self.name = name
         self.create()
 
+        if self.name in model.parts:
+            self.inherit(model.parts[self.name])
+
         geometry = kwargs.get("geometry")
         if geometry is not None:
             params = {
                 "data": geometry,
                 "type_": "geometry",
                 "part": self,
             }
@@ -95,14 +98,15 @@
         if surfaces is not None:
             params = {
                 "data": surfaces,
                 "type_": "surfaces",
                 "part": self,
             }
             self.surfaces = to_object_key_mode(**params)
+            # to_object_key_mode(**params)
 
         sets = kwargs.get("sets")
 
         if sets is not None:
             params = {
                 "data": sets,
                 "type_": "sets",
@@ -126,16 +130,23 @@
                 "type_": "mesh",
                 "part": self,
             }
 
             self.mesh = to_object_cmd_mode(**params)
             self.generate_mesh()
 
+    def inherit(self, other):
+        if isinstance(other, Abml_Part):
+            for attr in dir(other):
+                if not attr.startswith("__") and not callable(getattr(other, attr)):
+                    setattr(self, attr, getattr(other, attr))
+
     def create(self):
-        self.model.m.Part(dimensionality=THREE_D, name=self.name, type=DEFORMABLE_BODY)
+        if self.name not in self.model.parts.keys():
+            self.model.m.Part(dimensionality=THREE_D, name=self.name, type=DEFORMABLE_BODY)
 
     def get_sequence_from_set_list(self, set_list):
         face_seq = None
         cell_seq = None
         edge_seq = None
         for set_ in set_list:
             seq = self.model.p[self.name].sets[set_].faces
@@ -521,24 +532,33 @@
         self.faces = self.convert_position_list(faces)
 
         self.create()
 
     def create(self):
         part = self.model.p[self.part.name]
 
-        face_seq = self.part.geometry.get_sequence_from_list(self.faces, "face")
+        try:
+            face_seq = self.part.geometry.get_sequence_from_list(self.faces, "face")
+        except AttributeError:
+            face_seq = self.part.model.parts[self.part.name].geometry.get_sequence_from_list(self.faces, "face")
 
         try:
             part.Surface(side1Faces=face_seq, name=self.name)
         except Exception as e:
             error_msg = """
             surface_name: {name}
+            faces_inp: {faces}
+            face_seq: {face_seq}
+            part: {part}
             {e}
             """.format(
                 name=self.name,
+                faces=self.faces,
+                face_seq=face_seq,
+                part=self.part.name,
                 e=e,
             )
             raise ValueError(error_msg)
 
 
 @Abml_Registry.register("sets")
 class Abml_Sets(Abml_Helpers):
```

### Comparing `abml-0.1.1/abml/abml_sections.py` & `abml-0.1.4/abml/abml_sections.py`

 * *Files identical despite different names*

### Comparing `abml-0.1.1/abml/abml_sketch.py` & `abml-0.1.4/abml/abml_sketch.py`

 * *Files identical despite different names*

### Comparing `abml-0.1.1/abml/abml_steps.py` & `abml-0.1.4/abml/abml_steps.py`

 * *Files identical despite different names*

### Comparing `abml-0.1.1/setup.py` & `abml-0.1.4/setup.py`

 * *Files 11% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 {'': ['*']}
 
 install_requires = \
 ['pyaml>=21.10.1,<22.0.0']
 
 setup_kwargs = {
     'name': 'abml',
-    'version': '0.1.1',
+    'version': '0.1.4',
     'description': '',
     'long_description': '',
     'author': 'DavidNaizheZhou',
     'author_email': '70525024+DavidNaizheZhou@users.noreply.github.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

